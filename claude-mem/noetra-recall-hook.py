#!/usr/bin/env python3
"""
Noetra recall hook (UserPromptSubmit) — memory recall with ZERO LLM calls.

Replaces claude-mem's `session-init` hook, which woke the AI observer on every prompt (a Claude call
per prompt on the Max allowance). This hook only asks the worker's search route for the most
relevant past memories across ALL projects (one global memory: includes the capture bridge's
"noetra" digests) and injects them as context.

Self-heal: at most every 6 hours it checks that a claude-mem update has not re-enabled the
AI-feeding hooks; if one has, it re-applies noetra-patch-hooks.py and says so.
"""
import json, os, subprocess, sys, time, urllib.request

WORKER   = "http://localhost:37777"
MIN_LEN  = 20
MAX_INJECT = 8                                   # 20 memories was ~23 KB (~6k tokens) on every prompt; 8 keeps recall useful and cheap
HERE     = os.path.dirname(os.path.abspath(__file__))
STAMP    = os.path.join(HERE, "state", "noetra-recall-hook.last-heal")
HEAL_SEC = 6 * 3600


def recall(prompt):
    limit = max(1, min(int(os.environ.get("CLAUDE_MEM_SEMANTIC_INJECT_LIMIT", "8") or 8), MAX_INJECT))
    body = json.dumps({"q": prompt[:2000], "limit": str(limit)}).encode()
    req = urllib.request.Request(WORKER + "/api/context/semantic", data=body, headers={"Content-Type": "application/json"})
    with urllib.request.urlopen(req, timeout=8) as r:
        return (json.loads(r.read().decode()) or {}).get("context") or ""


def self_heal():
    try:
        if time.time() - os.path.getmtime(STAMP) < HEAL_SEC:
            return ""
    except OSError:
        pass
    os.makedirs(os.path.dirname(STAMP), exist_ok=True)
    with open(STAMP, "w") as f:
        f.write(str(time.time()))
    out = subprocess.run([sys.executable, os.path.join(HERE, "noetra-patch-hooks.py"), "--quiet"], capture_output=True, text=True, timeout=20)
    return out.stdout.strip()


def main():
    try:
        data = json.load(sys.stdin)
    except Exception:
        data = {}
    notes = []
    try:
        healed = self_heal()
        if healed:
            notes.append(healed)
    except Exception:
        pass
    prompt = (data.get("prompt") or "").strip()
    ctx = ""
    if os.environ.get("CLAUDE_MEM_SEMANTIC_INJECT", "true").lower() != "false" and len(prompt) >= MIN_LEN:
        try:
            ctx = recall(prompt)
        except Exception:
            ctx = ""                                       # worker down: never block the prompt
    out = {"continue": True, "suppressOutput": True}
    if ctx:
        out["hookSpecificOutput"] = {"hookEventName": "UserPromptSubmit", "additionalContext": ctx}
    if notes:
        out["systemMessage"] = " ".join(notes)
    sys.stdout.write(json.dumps(out))


if __name__ == "__main__":
    main()
