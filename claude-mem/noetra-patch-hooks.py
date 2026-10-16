#!/usr/bin/env python3
"""
Noetra patch for claude-mem hooks — stop the AI observer, keep recall. Idempotent.

claude-mem has no setting that turns its LLM observer off (verified in 13.25.3 source,
workflow wf_0f587327-280). Three hooks feed it:
  PostToolUse `observation`, Stop `summarize`, UserPromptSubmit `session-init` (wakes it per prompt).
This removes the first two and swaps the third for noetra-recall-hook.py (search-only recall).
Kept: SessionStart start/context, PreToolUse file-context, SessionEnd, Setup (no LLM).

Patches every claude-mem hooks.json under ~/.claude/plugins (cache versions + marketplace copy),
backing each original up once as hooks.json.orig. Plugin updates bring the hooks back; the recall
hook re-runs this check every 6 hours and reports when it re-applied.
Usage: python noetra-patch-hooks.py [--check] [--quiet]
"""
import glob, json, os, shutil, sys

PLUGINS = os.path.expanduser("~/.claude/plugins")
# macOS ships python3 but no `python`; Windows installs `python`.
RECALL  = ('python' if os.name == 'nt' else 'python3') + ' "$HOME/.claude-mem/noetra-recall-hook.py"'
AI_FEEDERS = ("hook claude-code observation", "hook claude-code summarize", "hook claude-code session-init")
# 13.39.0 added PostToolUseFailure -> observation (fixed 2026-10-16).
AI_EVENTS = ("PostToolUse", "PostToolUseFailure", "Stop", "UserPromptSubmit")


def targets():
    pats = [os.path.join(PLUGINS, "cache", "thedotmack", "claude-mem", "*", "hooks", "hooks.json"),
            os.path.join(PLUGINS, "marketplaces", "thedotmack", "plugin", "hooks", "hooks.json")]
    return sorted({p for pat in pats for p in glob.glob(pat)})


def hook_text(h):
    # <=13.35 hooks were one shell string; 13.39+ use exec form (command + args[]), which the
    # string-only match missed, so the update silently re-enabled the observer (fixed 2026-10-16).
    return " ".join([h.get("command", "")] + [str(a) for a in h.get("args") or []])


def feeds_ai(h):
    return any(k in hook_text(h) for k in AI_FEEDERS)


def patch(doc):
    hooks = doc.get("hooks", {})
    changed = False
    for event in AI_EVENTS:
        groups = hooks.get(event, [])
        new_groups = []
        for g in groups:
            kept = [h for h in g.get("hooks", []) if not feeds_ai(h)]
            if len(kept) != len(g.get("hooks", [])):
                changed = True
            if kept:
                new_groups.append({**g, "hooks": kept})
        if event == "UserPromptSubmit" and not any(RECALL in h.get("command", "") for g in new_groups for h in g.get("hooks", [])):
            new_groups.append({"hooks": [{"type": "command", "shell": "bash", "command": RECALL, "timeout": 30}]})
            changed = True
        if new_groups:
            hooks[event] = new_groups
        elif event in hooks:
            del hooks[event]
            changed = True
    return changed


def main():
    check, quiet = "--check" in sys.argv, "--quiet" in sys.argv
    bad, fixed = [], []
    for p in targets():
        doc = json.load(open(p, encoding="utf-8"))
        probe = json.loads(json.dumps(doc))
        if not patch(probe):
            continue
        bad.append(p)
        if check:
            continue
        orig = p + ".orig"
        if not os.path.exists(orig):
            shutil.copy2(p, orig)
        tmp = p + ".tmp"
        with open(tmp, "w", encoding="utf-8") as f:
            json.dump(probe, f, indent=2)
        os.replace(tmp, p)
        fixed.append(p)
    if check:
        print("NOETRA HOOKS OK" if not bad else "NOETRA HOOKS NEED PATCH: " + "; ".join(bad))
        return 0 if not bad else 1
    if fixed:
        print("Noetra: claude-mem AI note-taker hooks were re-enabled (plugin update?) and have been switched off again in {} file(s); takes effect next session.".format(len(fixed)))
    elif not quiet:
        print("NOETRA HOOKS OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
