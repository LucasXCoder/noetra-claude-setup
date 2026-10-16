"""Oracles for ~/.claude/noetra/memory-fix/GATES.md (2026-09-25 memory-system repair). Read-only: measures, never changes.
Usage: python memory_check.py --bridge | --captured | --launchers | --observer | --recall | --vault | --graph | --docs
"""
from __future__ import annotations

import json
import re
import sqlite3
import subprocess
import sys
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

HOME = Path.home()
CM = HOME / ".claude-mem"
VAULT = HOME / "noetra-vault"
FIX_START = "2026-09-26T01:15:00Z"        # UTC, when bridge v2 first ran
PROJECTS = ("mql-orb-lab", "liquidity-lizard", "noetra", "permitpulse-selffund", "birdquant", "odysseus", "scholarship-office",
            "dreamcaster", "meme-coins", "parked-404-protocol-and-underwear-brand")


def fail(msg: str) -> int:
    print("FAIL " + msg)
    return 1


def db():
    return sqlite3.connect("file:{}?mode=ro".format(CM / "claude-mem.db"), uri=True)


def bridge() -> int:
    out = subprocess.run(["powershell", "-NoProfile", "-Command",
                          "Get-CimInstance Win32_Process -Filter \"Name='python.exe'\" | Where-Object { $_.CommandLine -like '*capture-bridge.py*' } | "
                          "Measure-Object | Select-Object -ExpandProperty Count"], capture_output=True, text=True, timeout=60)
    n = int((out.stdout.strip() or "0").splitlines()[-1])
    if n < 1:
        return fail("capture bridge is not running")
    st = json.load(open(CM / "capture-bridge-state.json", encoding="utf-8"))
    if st.get("version") != 2 or not st.get("last_pass_utc"):
        return fail("bridge state is not v2 or no full pass completed yet")
    age = (datetime.now(timezone.utc) - datetime.strptime(st["last_pass_utc"], "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)).total_seconds()
    if age > 900:
        return fail("last full pass {:.0f}s ago".format(age))
    src = (CM / "capture-bridge.py").read_text(encoding="utf-8")
    if "for raw in f:" not in src or "PASS_BYTES" not in src:
        return fail("bridge is not the streaming v2")
    print("BRIDGE OK  {} process(es) | last full pass {:.0f}s ago | {} transcripts tracked".format(n, age, len(st["files"])))
    return 0


def captured() -> int:
    c = db()
    n, last = c.execute("select count(*), max(created_at) from observations where project='noetra' and created_at >= ? and generated_by_model is null",
                        (FIX_START,)).fetchone()
    st = json.load(open(CM / "capture-bridge-state.json", encoding="utf-8"))
    real = {p: v for p, v in st["files"].items() if "claude-mem-observer-sessions" not in p and Path(p).exists()}
    behind = {p: Path(p).stat().st_size - v["offset"] for p, v in real.items()}
    lag = [p for p, b in behind.items() if b > 70 * 2**20]
    if n < 80 or lag:
        return fail("{} bridge memories since the fix; transcripts more than 70 MB behind: {}".format(n, lag))
    print("CAPTURED OK  {} no-LLM memories in the global 'noetra' memory since the fix, latest {}".format(n, last))
    return 0


def launchers() -> int:
    b = (CM / "start-capture-bridge.ps1").read_text(encoding="utf-8")
    g = (CM / "refresh-vault-graph.ps1").read_text(encoding="utf-8")
    ok = "'run --quiet python \"{0}\"' -f $script" in b and "'update \"{0}\"' -f $vault" in g
    lnk = HOME / "AppData" / "Roaming" / "Microsoft" / "Windows" / "Start Menu" / "Programs" / "Startup"
    have = all((lnk / f).exists() for f in ("noetra-capture-bridge.lnk", "noetra-vault-graph.lnk"))
    if not (ok and have):
        return fail("launchers quoted={} startup shortcuts present={}".format(ok, have))
    print("LAUNCHERS OK  both startup scripts quote their spaced paths; both startup shortcuts present")
    return 0


def observer() -> int:
    out = subprocess.run([sys.executable, str(CM / "noetra-patch-hooks.py"), "--check"], capture_output=True, text=True, timeout=30)
    if "NOETRA HOOKS OK" not in out.stdout:
        return fail(out.stdout.strip())
    # Check the INSTALLED version (not a pinned one) and read exec-form hooks (command + args[]).
    installed = json.load(open(HOME / ".claude/plugins/installed_plugins.json", encoding="utf-8"))["plugins"]["claude-mem@thedotmack"][0]["installPath"]
    h = json.load(open(Path(installed) / "hooks" / "hooks.json", encoding="utf-8"))["hooks"]
    cmds = [" ".join([x.get("command", "")] + [str(a) for a in x.get("args") or []]) for ev in h.values() for g in ev for x in g["hooks"]]
    if any(k in c for c in cmds for k in ("hook claude-code observation", "hook claude-code summarize", "hook claude-code session-init")):
        return fail("an AI-feeding hook is still registered")
    if not any("noetra-recall-hook.py" in c for c in cmds):
        return fail("recall hook not registered")
    print("OBSERVER OFF OK  no AI-feeding claude-mem hooks in any copy; recall served by noetra-recall-hook.py (no LLM)")
    return 0


def recall() -> int:
    p = subprocess.run([sys.executable, str(CM / "noetra-recall-hook.py")], input=json.dumps({"prompt": "Beat the Market noise area replication on MES and MNQ LucidPro"}),
                       capture_output=True, text=True, timeout=60)
    o = json.loads(p.stdout)
    ctx = o.get("hookSpecificOutput", {}).get("additionalContext", "")
    if len(ctx) < 500:
        return fail("recall returned {} chars".format(len(ctx)))
    body = json.dumps({"q": "auto-capture v2 Beat the Market H-049", "limit": "20"}).encode()
    req = urllib.request.Request("http://localhost:37777/api/context/semantic", data=body, headers={"Content-Type": "application/json"})
    got = json.loads(urllib.request.urlopen(req, timeout=15).read().decode()).get("count", 0)
    print("RECALL OK  recall hook injected {} chars with no LLM; search returned {} memories".format(len(ctx), got))
    return 0


def vault() -> int:
    bad = []
    for s in PROJECTS:
        p = VAULT / "notes" / "projects" / (s + ".md")
        if not p.exists():
            bad.append(s + " missing")
            continue
        t = p.read_text(encoding="utf-8")
        if not t.startswith("---") or "## Next step" not in t or "sources:" not in t:
            bad.append(s + " malformed")
    topics = list((VAULT / "wiki" / "topics").glob("*.md"))
    uncited = []
    for p in topics:
        t = p.read_text(encoding="utf-8")
        srcs = re.findall(r"raw-sources/[^\s\"'\])]+", t)
        if not srcs or not all((VAULT / s.rstrip(".,;")).exists() for s in srcs):
            uncited.append(p.name)
    brief = VAULT / "wiki" / "briefings" / "2026-09-25-prop-firm-month-goal.md"
    master = (VAULT / "notes" / "_noetra-master.md").read_text(encoding="utf-8")
    links = sum(1 for s in PROJECTS if "[[" + s + "]]" in master)
    if bad or len(topics) < 8 or uncited or not brief.exists() or links < len(PROJECTS):
        return fail("projects {} | topics {} | uncited {} | briefing {} | master links {}/{}".format(bad, len(topics), uncited[:5], brief.exists(), links, len(PROJECTS)))
    print("VAULT OK  {} project notes | {} cited wiki topics | month-goal briefing | master note links every project".format(len(PROJECTS), len(topics)))
    return 0


def graph() -> int:
    m = json.load(open(VAULT / "graphify-out" / "manifest.json", encoding="utf-8"))
    keys = [k.replace("\\", "/") for k in m]
    need = ["notes/projects/mql-orb-lab.md", "notes/_noetra-master.md"]
    wiki = [k for k in keys if k.startswith("wiki/topics/")]
    if not all(n in keys for n in need) or len(wiki) < 8:
        return fail("graph covers {} files; wiki topics {}; missing {}".format(len(keys), len(wiki), [n for n in need if n not in keys]))
    print("GRAPH OK  {} vault files in the graph, {} wiki topics".format(len(keys), len(wiki)))
    return 0


def docs() -> int:
    t = (HOME / ".claude" / "CLAUDE.md").read_text(encoding="utf-8")
    need = ("capture bridge", "noetra-recall-hook", "no LLM")
    miss = [w for w in need if w.lower() not in t.lower()]
    if miss:
        return fail("CLAUDE.md memory section lacks {}".format(miss))
    print("DOCS OK  CLAUDE.md describes the repaired memory system")
    return 0


if __name__ == "__main__":
    flag = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"--bridge": bridge, "--captured": captured, "--launchers": launchers, "--observer": observer, "--recall": recall,
          "--vault": vault, "--graph": graph, "--docs": docs}.get(flag)
    raise SystemExit(fn() if fn else "usage: memory_check.py --bridge|--captured|--launchers|--observer|--recall|--vault|--graph|--docs")
