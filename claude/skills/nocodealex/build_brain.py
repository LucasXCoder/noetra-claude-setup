"""Merge mining shards, validate the nocodealex atom/edge store, gate density + connectivity,
regenerate topic indexes and graph.html.

Run after every mining batch:   python -I build_brain.py

Sources come from sources/manifest.json (YouTube transcripts, chen.media guides, GitHub repo
prose). Exits non-zero while any substantive source is unmined or under-extracted, any edge
dangles, or connectivity is below the gate — a multi-pass build reports "N of M done" honestly.
Density gates match engram's: long-form (>=1500 words) must beat 150 words/atom, shorter 170.
"""
import collections
import json
import pathlib
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")

HERE = pathlib.Path(__file__).resolve().parent
SHARDS = HERE / "shards"
GATE_LONGFORM, GATE_DEFAULT, LONGFORM_WORDS, MIN_WORDS = 150, 170, 1500, 20
MIN_CONNECTIVITY = 0.85

VALID_TYPES = {"claim", "concept", "definition", "number", "result", "example", "analogy",
               "method", "caveat", "idea", "product", "opinion", "warning", "prediction",
               "bio", "resource", "style"}
VALID_REL = {"because", "defines", "part-of", "example-of", "analogy-for", "evidence-for",
             "qualifies", "contrast", "contradicts", "leads-to", "enables", "depends-on",
             "generalizes"}
VALID_CONF = {"CORE", "STATED", "INFERRED"}
VALID_TOPICS = {"usage-limits", "claude-code-mastery", "skills-mcp-ecosystem", "agent-teams",
                "prompting-quality", "build-sell-career", "creator-news"}


def read_jsonl(path: pathlib.Path) -> list[dict]:
    out = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if line.strip():
            try:
                out.append(json.loads(line))
            except json.JSONDecodeError as e:
                sys.exit(f"{path.name}:{n} is not valid JSON — {e}")
    return out


def merge() -> tuple[list[dict], list[dict]]:
    """Shards are the write path; atoms.jsonl / edges.jsonl are the merged store."""
    atoms, edges = [], []
    for kind, bucket in (("atoms", atoms), ("edges", edges)):
        d = SHARDS / kind
        if d.is_dir():
            for f in sorted(d.glob("*.jsonl")):
                bucket.extend(read_jsonl(f))
    seen = set()
    edges = [e for e in edges if (k := (e.get("from"), e.get("to"), e.get("rel"))) not in seen and not seen.add(k)]
    # Cross-link passes may promote an atom's confidence (e.g. STATED → CORE when the same claim
    # recurs across sources) without rewriting another agent's shard.
    overrides = {}
    if (SHARDS / "overrides").is_dir():
        for f in sorted((SHARDS / "overrides").glob("*.jsonl")):
            for o in read_jsonl(f):
                overrides[o["id"]] = o["confidence"]
    for a in atoms:
        if a.get("id") in overrides:
            a["confidence"] = overrides[a["id"]]
    (HERE / "atoms.jsonl").write_text("".join(json.dumps(a, ensure_ascii=False) + "\n" for a in atoms), encoding="utf-8")
    (HERE / "edges.jsonl").write_text("".join(json.dumps(e, ensure_ascii=False) + "\n" for e in edges), encoding="utf-8")
    return atoms, edges


def main() -> None:
    atoms, edges = merge()
    manifest = json.loads((HERE / "sources" / "manifest.json").read_text(encoding="utf-8"))
    sources = {it["id"]: it for it in manifest["items"] if it.get("text_path")}
    errs = []

    ids = set()
    for a in atoms:
        aid = a.get("id")
        if not aid:
            errs.append(f"atom with no id: {str(a.get('text', ''))[:60]}")
            continue
        if aid in ids:
            errs.append(f"duplicate atom id: {aid}")
        ids.add(aid)
        if a.get("type") not in VALID_TYPES:
            errs.append(f"{aid}: bad type {a.get('type')!r}")
        if a.get("confidence") not in VALID_CONF:
            errs.append(f"{aid}: bad confidence {a.get('confidence')!r}")
        if a.get("topic") not in VALID_TOPICS:
            errs.append(f"{aid}: bad topic {a.get('topic')!r}")
        if not a.get("sources"):
            errs.append(f"{aid}: no sources[]")
        for s in a.get("sources", []):
            if s not in sources:
                errs.append(f"{aid}: source {s!r} not in manifest")
        if not a.get("text"):
            errs.append(f"{aid}: empty text")

    touched = set()
    for e in edges:
        f, t, rel = e.get("from"), e.get("to"), e.get("rel")
        if rel not in VALID_REL:
            errs.append(f"edge {f}->{t}: bad rel {rel!r}")
        for end in (f, t):
            if end not in ids:
                errs.append(f"edge {f}->{t}: endpoint {end!r} resolves to no atom")
        touched.update((f, t))
    connectivity = len(touched & ids) / max(1, len(ids))

    per_src = collections.Counter(s for a in atoms for s in a.get("sources", []))
    substantive = {sid: it for sid, it in sources.items() if it["words"] >= MIN_WORDS}
    queue = [sid for sid in substantive if not per_src.get(sid)]
    thin = []
    for sid, it in substantive.items():
        c = per_src.get(sid, 0)
        if c:
            gate = GATE_LONGFORM if it["words"] >= LONGFORM_WORDS else GATE_DEFAULT
            if it["words"] / c > gate:
                thin.append((sid, it["words"], c, it["words"] / c, gate))

    mined = [sid for sid in substantive if per_src.get(sid)]
    kinds = collections.Counter(substantive[s]["kind"] for s in mined)
    print("\nBRAIN: nocodealex")
    print(f"atoms {len(atoms)} | edges {len(edges)} | connectivity {100 * connectivity:.0f}% of atoms touched "
          f"(gate {100 * MIN_CONNECTIVITY:.0f}%)")
    print(f"sources: {len(mined)} of {len(substantive)} substantive mined {dict(kinds)} "
          f"({len(sources) - len(substantive)} trivial <{MIN_WORDS}w excluded)")
    if mined:
        mw = sum(substantive[s]["words"] for s in mined)
        print(f"mined density: 1 atom / {mw / max(1, sum(per_src[s] for s in mined)):.1f} words")

    for script in ("build_topics.py", "build_graph.py"):
        if (HERE / script).exists() and atoms and not errs:
            subprocess.run([sys.executable, "-I", str(HERE / script)], check=False, cwd=HERE)

    if thin:
        print(f"\n[FAIL] {len(thin)} source(s) UNDER-EXTRACTED — re-mine:")
        for sid, w, c, wpc, gate in sorted(thin, key=lambda r: -r[1])[:60]:
            print(f"   {sid}  {w}w  {c} atoms  1/{wpc:.0f}  (gate 1/{gate})")
    if errs:
        print(f"\n[FAIL] {len(errs)} store error(s):")
        for e in errs[:60]:
            print(f"   {e}")
    if connectivity < MIN_CONNECTIVITY:
        print(f"\n[FAIL] connectivity {100 * connectivity:.0f}% below gate — link isolated atoms")

    remaining = len(queue) + len(thin)
    if remaining or errs or connectivity < MIN_CONNECTIVITY:
        if remaining:
            print(f"\nPARTIAL — {len(mined) - len(thin)} of {len(substantive)} sources done "
                  f"({len(thin)} part-mined, {len(queue)} untouched). Run /engram nocodealex again to continue.")
            if queue:
                print("   untouched: " + ", ".join(sorted(queue)[:40]) + (" …" if len(queue) > 40 else ""))
        sys.exit(1)
    print("\n[OK] every substantive source mined and clears the density gate.")


if __name__ == "__main__":
    main()
