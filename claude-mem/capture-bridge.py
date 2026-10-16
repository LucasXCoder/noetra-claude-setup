#!/usr/bin/env python3
"""
Noetra capture bridge v2 — reliable, no-LLM auto-capture into the one global Noetra memory.

Tails Claude Code transcripts and POSTs deterministic digests to the claude-mem worker's
/api/memory/save endpoint (title/text/project). No LLM, no SDK spawn, zero allowance used.

v2 (2026-09-25): v1 read each transcript's whole unread tail into RAM (this machine has
multi-hundred-MB transcripts), died every start, and saved nothing after 2026-06-11.
v2 streams line by line in binary with byte offsets, digests the backlog in bounded
chunks, caps work per pass, and logs to ~/.claude-mem/logs/capture-bridge.log.

One global memory: every capture lands in project "noetra" (no per-folder islands).
Run: `python capture-bridge.py --once`  (default: poll loop every 120s).
"""
import json, os, re, sys, time, glob, urllib.request
from collections import Counter
from datetime import datetime, timezone

PROJECTS_DIR  = os.path.expanduser("~/.claude/projects")
STATE_FILE    = os.path.expanduser("~/.claude-mem/capture-bridge-state.json")
LOG_FILE      = os.path.expanduser("~/.claude-mem/logs/capture-bridge.log")
SAVE_URL      = "http://localhost:37777/api/memory/save"
PROJECT       = "noetra"            # single global namespace — no islands
POLL_SECONDS  = 120
MIN_TOOLS     = 4                   # don't post trivial digests
MAX_TEXT      = 4000
CHUNK_BYTES   = 4 * 1024 * 1024     # one digest per ~4 MB of backlog
PASS_BYTES    = 64 * 1024 * 1024    # bounded work per pass per file (catches up over passes)
FILE_TOOLS    = {"Edit", "Write", "MultiEdit", "NotebookEdit"}
SECRET_RE     = re.compile(                        # never store credentials in memory (2026-09-25: a Databento key leaked via a digest)
    r"(db-[A-Za-z0-9]{16,}|sk-[A-Za-z0-9_\-]{16,}|sk_(?:live|test)_[A-Za-z0-9]{16,}|gh[pousr]_[A-Za-z0-9]{20,}|xox[abpr]-[A-Za-z0-9\-]{10,}"
    r"|AKIA[0-9A-Z]{16}|AIza[0-9A-Za-z_\-]{30,}|eyJ[A-Za-z0-9_\-]{20,}\.[A-Za-z0-9_\-]{20,}\.[A-Za-z0-9_\-]{10,}"
    r"|(?i:api[_\-]?key|secret|token|passw(?:or)?d|bearer)[\"']?\s*[=:]\s*[\"']?[A-Za-z0-9_\-\./+]{8,})")


def redact(text):
    return SECRET_RE.sub("[REDACTED]", text)
NOISE_STARTS  = ("You are", "<", "[", "Stop hook feedback", "Base directory for this skill", "This session is being continued")
NOISE_HAS     = ("specialized observer", "claude-mem", "two-agent shared-memory", "<observed", "<what_happened",
                 "<system-reminder", "<task_reminder", "<nested_memory", "[intelligence]", "tool_result")


def log(msg):
    line = "{} {}\n".format(datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"), msg)
    try:
        os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(line)
    except OSError:
        pass


def load_state():
    try:
        with open(STATE_FILE, "r", encoding="utf-8") as f:
            st = json.load(f)
    except Exception:
        return {"version": 2, "files": {}}
    if st.get("version") != 2:                  # v1 offsets were text-mode positions: restart them as bytes from 0
        st = {"version": 2, "files": {}, "migrated_from_v1": True}
    return st


def save_state(st):
    tmp = STATE_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(st, f)
    os.replace(tmp, STATE_FILE)


def post_observation(title, text):
    body = json.dumps({"title": redact(title)[:140], "text": redact(text)[:MAX_TEXT], "project": PROJECT}).encode()
    req = urllib.request.Request(SAVE_URL, data=body, headers={"Content-Type": "application/json"})
    try:
        with urllib.request.urlopen(req, timeout=15) as r:
            return json.loads(r.read().decode()).get("id")
    except Exception as e:
        log("save failed: {}".format(e))
        return None


def user_text(content):
    if isinstance(content, str):
        return content.strip()
    if isinstance(content, list):
        return " ".join(c.get("text", "") for c in content if isinstance(c, dict) and c.get("type") == "text").strip()
    return ""


class Digest:
    def __init__(self):
        self.prompts, self.tools, self.files, self.cmds, self.bits = [], [], set(), [], []
        self.errors, self.first_ts, self.last_ts, self.bytes = 0, None, None, 0

    def add(self, obj):
        ts = obj.get("timestamp")
        if ts:
            self.first_ts = self.first_ts or ts
            self.last_ts = ts
        msg = obj.get("message")
        if not isinstance(msg, dict):
            return
        role, content = msg.get("role"), msg.get("content")
        if role == "user":
            t = user_text(content)
            low = t.lower()
            if t and not t.startswith(NOISE_STARTS) and not any(n in low for n in NOISE_HAS):
                self.prompts.append(t[:220])
            if isinstance(content, list):
                self.errors += sum(1 for c in content if isinstance(c, dict) and c.get("type") == "tool_result" and c.get("is_error"))
        elif role == "assistant" and isinstance(content, list):
            for c in content:
                if not isinstance(c, dict):
                    continue
                if c.get("type") == "text" and c.get("text"):
                    self.bits.append(c["text"][:240])
                elif c.get("type") == "tool_use":
                    name = c.get("name", "?")
                    self.tools.append(name)
                    inp = c.get("input", {}) or {}
                    if name in FILE_TOOLS and inp.get("file_path"):
                        self.files.add(inp["file_path"])
                    elif name == "Bash" and inp.get("command"):
                        self.cmds.append(str(inp["command"])[:120])

    def worth_saving(self):
        return bool(self.prompts) and (len(self.tools) >= MIN_TOOLS or self.files)

    def text(self, where):
        span = "{} .. {}".format((self.first_ts or "?")[:16], (self.last_ts or "?")[:16])
        out = ["[auto-capture v2 | {} | {}]".format(where, span)]
        out.append("Prompts:\n" + "\n".join("- " + p for p in self.prompts[:8]))
        top = ", ".join("{}x{}".format(n, c) for n, c in Counter(self.tools).most_common(8))
        out.append("Tools used ({}): {}".format(len(self.tools), top))
        if self.files:
            out.append("Files modified:\n" + "\n".join("- " + f for f in sorted(self.files)[:20]))
        if self.cmds:
            out.append("Commands:\n" + "\n".join("- " + c for c in self.cmds[:10]))
        if self.errors:
            out.append("Tool errors: {}".format(self.errors))
        if self.bits:
            out.append("Outcome notes:\n" + "\n".join("- " + b for b in self.bits[-5:]))
        return "\n\n".join(out)


def flush(d, where):
    if not d.worth_saving():
        return 0
    title = next((p for p in d.prompts if len(p) >= 15 and not p.startswith(("--", "@"))), d.prompts[0])
    oid = post_observation(" ".join(title.split())[:70], d.text(where))
    if oid:
        log("saved obs #{} from {} ({} prompts, {} tools)".format(oid, where, len(d.prompts), len(d.tools)))
        return 1
    raise RuntimeError("worker save failed")          # keep the offset where it was; retry next pass


def transcripts():
    for path in glob.glob(os.path.join(PROJECTS_DIR, "**", "*.jsonl"), recursive=True):
        base = os.path.basename(path)
        if base.startswith("agent-") or (os.sep + "subagents" + os.sep) in path or "claude-mem-observer-sessions" in path:
            continue                                   # sub-agent sidechains and claude-mem's own observer sessions are noise
        yield path


def process_file(path, files_state):
    size = os.path.getsize(path)
    offset = files_state.get(path, {}).get("offset", 0)
    if size < offset:
        offset = 0                                     # truncated / rotated
    if size == offset:
        return 0
    where = os.path.basename(os.path.dirname(path)) + "/" + os.path.basename(path)[:8]
    saved, d, pos, stop_at = 0, Digest(), offset, offset + PASS_BYTES
    with open(path, "rb") as f:
        f.seek(offset)
        for raw in f:
            if not raw.endswith(b"\n"):
                break                                  # incomplete last line: wait for it
            pos += len(raw)
            d.bytes += len(raw)
            try:
                d.add(json.loads(raw))
            except ValueError:
                pass
            if d.bytes >= CHUNK_BYTES:
                saved += flush(d, where)
                files_state[path] = {"offset": pos}
                d = Digest()
                if pos >= stop_at:
                    return saved
    saved += flush(d, where)
    files_state[path] = {"offset": pos}
    return saved


def process_once():
    st = load_state()
    files_state, saved = st.setdefault("files", {}), 0
    for path in sorted(transcripts(), key=lambda p: os.path.getmtime(p)):
        try:
            saved += process_file(path, files_state)
        except RuntimeError:
            log("worker unreachable; will retry {}".format(path))
            save_state(st)
            return saved
        except OSError as e:
            log("skip {}: {}".format(path, e))
        save_state(st)
    st["last_pass_utc"] = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    save_state(st)
    return saved


def main():
    once = "--once" in sys.argv
    log("bridge v2 start (once={})".format(once))
    while True:
        try:
            n = process_once()
            if n:
                log("pass saved {}".format(n))
        except Exception as e:                         # never die: log and try again next poll
            log("loop error: {!r}".format(e))
        if once:
            break
        time.sleep(POLL_SECONDS)


if __name__ == "__main__":
    main()
