#!/usr/bin/env python3
"""UserPromptSubmit: local semantic router for skills hidden from the listing (skillOverrides "name-only").

Embeds the prompt with the all-MiniLM-L6-v2 ONNX model that Chroma/claude-mem already cached on this machine
(no network, no API key, no Claude call) and compares it with each hidden skill's name + description.
A keyword score on the skill name is blended in so exact mentions still win. Prints a short
additionalContext note only when a skill clearly fits; otherwise prints nothing. Never blocks a prompt.

  skill_router.py                 hook mode (reads the hook JSON on stdin)
  skill_router.py --query "text"  debug: print the ranked list with scores
"""
import hashlib
import json
import os
import re
import sys
from pathlib import Path

HOME = Path(os.environ.get("USERPROFILE") or Path.home())
CLAUDE = HOME / ".claude"
MODEL_DIR = HOME / ".cache" / "chroma" / "onnx_models" / "all-MiniLM-L6-v2" / "onnx"
INDEX = CLAUDE / "hooks" / ".skill-router-index.json"
MAX_SHOWN, MIN_SIM, MIN_Z, WINDOW = 3, 0.25, 3.0, 0.08   # best score floor, how far above the pack (std devs), band of runners-up


def read_skill(name):
    """Return the description text of a skill ('' if unreadable)."""
    for folder in (name, name.split(":", 1)[-1]):
        path = CLAUDE / "skills" / folder / "SKILL.md"
        if path.exists():
            front = re.match(r"^---\r?\n(.*?)\r?\n---", path.read_text(encoding="utf-8", errors="replace"), re.S)
            if front:
                m = re.search(r"^description:\s*(?:[>|][-+]?\s*\r?\n)?((?:[ \t]+.*\r?\n?)+|.*)", front.group(1), re.M)
                if m:
                    return re.sub(r"\s+", " ", m.group(1)).strip().strip("\"'")
    return ""


class Embedder:
    def __init__(self):
        import numpy as np
        import onnxruntime as ort
        from tokenizers import Tokenizer
        self.np = np
        opts = ort.SessionOptions()
        opts.log_severity_level = 3
        self.session = ort.InferenceSession(str(MODEL_DIR / "model.onnx"), opts, providers=["CPUExecutionProvider"])
        self.tok = Tokenizer.from_file(str(MODEL_DIR / "tokenizer.json"))
        self.tok.enable_truncation(max_length=256)
        self.tok.enable_padding(length=None)
        self.inputs = {i.name for i in self.session.get_inputs()}

    def encode(self, texts):
        np = self.np
        enc = self.tok.encode_batch(texts)
        ids = np.array([e.ids for e in enc], dtype=np.int64)
        mask = np.array([e.attention_mask for e in enc], dtype=np.int64)
        feed = {"input_ids": ids, "attention_mask": mask}
        if "token_type_ids" in self.inputs:
            feed["token_type_ids"] = np.zeros_like(ids)
        hidden = self.session.run(None, feed)[0]
        m = mask[..., None].astype(np.float32)
        pooled = (hidden * m).sum(1) / np.clip(m.sum(1), 1e-9, None)
        return pooled / np.clip(np.linalg.norm(pooled, axis=1, keepdims=True), 1e-9, None)


def hidden_skills():
    settings = json.loads((CLAUDE / "settings.json").read_text(encoding="utf-8"))
    return sorted(k for k, v in (settings.get("skillOverrides") or {}).items() if v == "name-only")


def load_index(embedder, names):
    """Skill vectors, cached on disk and rebuilt only for skills whose text changed."""
    try:
        cache = json.loads(INDEX.read_text(encoding="utf-8"))
    except Exception:
        cache = {}
    docs, fresh = {}, {}
    for n in names:
        desc = read_skill(n)
        text = f"{n.replace('-', ' ').replace(':', ' ')}. {desc}"
        docs[n] = (desc, text, hashlib.sha1(text.encode()).hexdigest())
    todo = [n for n in names if cache.get(n, {}).get("h") != docs[n][2]]
    if todo:
        vecs = embedder.encode([docs[n][1] for n in todo])
        for n, v in zip(todo, vecs):
            cache[n] = {"h": docs[n][2], "v": [round(float(x), 5) for x in v]}
        INDEX.write_text(json.dumps({k: cache[k] for k in names}), encoding="utf-8")
    for n in names:
        fresh[n] = cache[n]["v"]
    return docs, fresh


def name_bonus(prompt_low, name):
    bare = name.split(":", 1)[-1].lower()
    return 0.25 if (bare in prompt_low or bare.replace("-", " ") in prompt_low) else 0.0


STOP = set("a an the and or of to for in on with is are be use used when this that it as at by from your you any not if do does "
           "how what which can will should my me i we our so up out all also more than only about into them they their make build "
           "create need want help get set run file files project work one".split())


def stems(text):
    return {re.sub(r"(ing|ers|er|ed|es|s)$", "", w) for w in re.findall(r"[a-z][a-z0-9]{3,}", text.lower()) if w not in STOP}


def lexical_bonus(prompt_stems, text):
    """Small boost for literal word overlap, which catches jargon the embedding model is weak on (borrow, lifetimes...)."""
    return min(0.18, 0.06 * max(0, len(prompt_stems & stems(text)) - 1))   # one shared word is noise; two or more is signal


def rank(prompt, with_scores=False):
    names = hidden_skills()
    if not names:
        return []
    emb = Embedder()
    docs, vecs = load_index(emb, names)
    q = emb.encode([prompt[:1500]])[0]
    np = emb.np
    scored = []
    low, pstems = prompt.lower(), stems(prompt)
    for n in names:
        sim = float(np.dot(q, np.array(vecs[n], dtype=np.float32)))
        sim += name_bonus(low, n) + lexical_bonus(pstems, docs[n][1])
        scored.append((sim, n, docs[n][0]))
    scored.sort(reverse=True)
    if with_scores:
        return scored
    values = [x[0] for x in scored]
    mean = sum(values) / len(values)
    spread = (sum((v - mean) ** 2 for v in values) / len(values)) ** 0.5 or 1e-9
    best = values[0]
    if best < MIN_SIM or (best - mean) / spread < MIN_Z:
        return []
    return [x for x in scored[:MAX_SHOWN] if x[0] >= MIN_SIM and x[0] >= best - WINDOW]


def main():
    if "--query" in sys.argv:
        for sim, n, _ in rank(sys.argv[sys.argv.index("--query") + 1], with_scores=True)[:6]:
            print(f"{sim:.3f}  {n}")
        return
    data = json.loads(sys.stdin.read() or "{}")
    prompt = str(data.get("prompt") or "")
    if len(prompt) < 12:
        return
    hits = rank(prompt)
    if not hits:
        return
    lines = [f"- {n}: {desc[:160]}" for _, n, desc in hits]
    note = ("Skills that look relevant to this request but are hidden from the skill list "
            "(load one with the Skill tool if it fits; ignore if not):\n" + "\n".join(lines))
    sys.stdout.write(json.dumps({"hookSpecificOutput": {"hookEventName": "UserPromptSubmit", "additionalContext": note}}))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        pass   # a router failure must never block a prompt
    sys.exit(0)
