#!/usr/bin/env bash
# Verify an installed Noetra Claude setup.   ./verify.sh [--home DIR]
# Exit 0 = no FAIL (warnings are things only a human can fix, like logging in).
set -uo pipefail

TARGET_HOME="$HOME"
while [ $# -gt 0 ]; do
  case "$1" in
    --home) TARGET_HOME="${2:?--home needs a directory}"; shift 2 ;;
    -h|--help) sed -n '2,3p' "$0"; exit 0 ;;
    *) echo "unknown argument: $1" >&2; exit 2 ;;
  esac
done
HERE="$(cd "$(dirname "$0")" && pwd)"
CL="$TARGET_HOME/.claude"
PASS=0; WARN=0; FAIL=0
ok()   { printf '  \033[32mPASS\033[0m %s\n' "$*"; PASS=$((PASS + 1)); }
warn() { printf '  \033[33mWARN\033[0m %s\n' "$*"; WARN=$((WARN + 1)); }
bad()  { printf '  \033[31mFAIL\033[0m %s\n' "$*"; FAIL=$((FAIL + 1)); }
have() { command -v "$1" >/dev/null 2>&1; }

echo "Verifying Noetra Claude setup in $CL"

# Tools the hooks run on.
for t in node python3 git; do have "$t" && ok "$t installed" || bad "$t missing (brew install $t / xcode-select --install)"; done
if have claude; then ok "claude CLI: $(claude --version 2>/dev/null | head -1)"; else warn "claude CLI not on PATH"; fi
have node || { echo; echo "node is required for the remaining checks."; exit 1; }

# settings.json
S="$CL/settings.json"
if [ ! -f "$S" ]; then bad "settings.json missing"; else
  if node -e 'JSON.parse(require("fs").readFileSync(process.argv[1],"utf8"))' "$S" 2>/dev/null; then ok "settings.json is valid JSON"; else bad "settings.json is not valid JSON"; fi
  grep -q '__HOME__' "$S" && bad "settings.json still has __HOME__ placeholders" || ok "no unrendered placeholders"
fi

# Core files
[ -f "$CL/CLAUDE.md" ] && grep -q 'Mandatory workflow' "$CL/CLAUDE.md" && ok "CLAUDE.md installed (with Mandatory workflow)" || bad "CLAUDE.md missing or outdated"
[ -f "$CL/noetra/CONTEXT.md" ] && ok "noetra/CONTEXT.md present" || warn "noetra/CONTEXT.md missing"

# Skills and agents against the manifest
read -r WANT_SKILLS WANT_AGENTS < <(node -e 'const m=require(process.argv[1]);console.log(m.skills.length,m.agents.length)' "$HERE/manifest.json" 2>/dev/null || echo "0 0")
GOT_SKILLS=0; BADSKILL=0
for d in "$CL"/skills/*/; do
  [ -d "$d" ] || continue
  [ -f "$d/SKILL.md" ] || continue
  GOT_SKILLS=$((GOT_SKILLS + 1))
  head -12 "$d/SKILL.md" | grep -q '^name:' || BADSKILL=$((BADSKILL + 1))
done
[ "$GOT_SKILLS" -ge "$WANT_SKILLS" ] && ok "skills: $GOT_SKILLS installed (bundle has $WANT_SKILLS)" || bad "skills: $GOT_SKILLS installed, bundle has $WANT_SKILLS"
[ "$BADSKILL" -eq 0 ] && ok "every skill has name frontmatter" || bad "$BADSKILL skills lack name frontmatter"
GOT_AGENTS=$(ls "$CL"/agents/*.md 2>/dev/null | wc -l | tr -d ' ')
[ "$GOT_AGENTS" -ge "$WANT_AGENTS" ] && ok "agents: $GOT_AGENTS installed" || bad "agents: $GOT_AGENTS installed, bundle has $WANT_AGENTS"

# Every script path a hook or the status line points at must exist.
# Paths are resolved relative to .claude/ (or .claude-mem/), so this works whatever the absolute home is.
# It must examine at least one path, or the check itself is broken.
HOOKCHECK=$(node -e '
  const fs=require("fs"),path=require("path");
  const [settings,cl,home]=process.argv.slice(1);
  const s=JSON.parse(fs.readFileSync(settings,"utf8")),found=new Set();
  const grab=(str)=>{ for(const m of str.matchAll(/\.claude(-mem)?\/([^"\s\x27]+\.(?:mjs|js|cjs|py|sh))/g))
    found.add(m[1] ? path.join(home,".claude-mem",m[2]) : path.join(cl,m[2])); };
  (function walk(v){ if(typeof v==="string") grab(v); else if(v&&typeof v==="object") Object.values(v).forEach(walk); })({hooks:s.hooks,statusLine:s.statusLine});
  const missing=[...found].filter(p=>!fs.existsSync(p));
  console.log(found.size+"|"+missing.join(" "));' "$S" "$CL" "$TARGET_HOME" 2>/dev/null)
CHECKED="${HOOKCHECK%%|*}"; MISSING="${HOOKCHECK#*|}"
if [ -z "$CHECKED" ] || [ "$CHECKED" -lt 3 ] 2>/dev/null; then bad "hook script check examined ${CHECKED:-0} paths (expected 3+): settings has no hooks?"
elif [ -n "$MISSING" ]; then bad "missing hook scripts: $MISSING"
else ok "all $CHECKED hook / status line scripts exist"; fi

# Behavior: the safety hooks must actually block.
G="$CL/hooks/guard-shell.mjs"; P="$CL/hooks/protect-files.mjs"
if [ -f "$G" ]; then
  OUT=$(printf '%s' '{"tool_name":"Bash","tool_input":{"command":"git reset --hard HEAD~1"}}' | node "$G" 2>/dev/null)
  case "$OUT" in *'"deny"'*) ok "guard-shell denies git reset --hard" ;; *) bad "guard-shell did not deny git reset --hard" ;; esac
  OUT=$(printf '%s' '{"tool_name":"Bash","tool_input":{"command":"ls -la"}}' | node "$G" 2>/dev/null)
  [ -z "$OUT" ] && ok "guard-shell allows ordinary commands" || bad "guard-shell blocked an ordinary command"
else bad "hooks/guard-shell.mjs missing"; fi
if [ -f "$P" ]; then
  printf '%s' '{"tool_input":{"file_path":"/Users/x/proj/.env"}}' | node "$P" >/dev/null 2>&1; RC=$?
  [ "$RC" -eq 2 ] && ok "protect-files blocks .env edits" || bad "protect-files did not block .env (exit $RC)"
else bad "hooks/protect-files.mjs missing"; fi
if [ -f "$CL/statusline.mjs" ]; then
  OUT=$(printf '%s' '{"model":{"display_name":"Sonnet"},"context_window":{"used_percentage":40}}' | node "$CL/statusline.mjs" 2>/dev/null)
  case "$OUT" in *Sonnet*) ok "status line renders" ;; *) bad "status line printed nothing useful" ;; esac
fi

# The knowledge brain
if [ -f "$CL/skills/nocodealex/atoms.jsonl" ]; then
  N=$(wc -l < "$CL/skills/nocodealex/atoms.jsonl" | tr -d ' ')
  [ "$N" -ge 8000 ] && ok "nocodealex brain: $N atoms" || bad "nocodealex brain looks truncated ($N atoms)"
else bad "nocodealex brain missing"; fi

# Memory: only meaningful on the real home, with the plugin installed.
if [ "$TARGET_HOME" = "$HOME" ]; then
  if [ -f "$TARGET_HOME/.claude-mem/noetra-patch-hooks.py" ] && have python3; then
    R=$(python3 -I "$TARGET_HOME/.claude-mem/noetra-patch-hooks.py" --check 2>&1)
    case "$R" in
      *"HOOKS OK"*) ok "claude-mem AI note-taker is off" ;;
      *) warn "claude-mem hooks need patching — run: python3 ~/.claude-mem/noetra-patch-hooks.py" ;;
    esac
  else warn "claude-mem not installed yet (it installs with the plugins)"; fi
  if have claude; then
    L=$(claude mcp list 2>&1 | head -20)
    echo "$L" | grep -q 'Failed to connect' && warn "an MCP server fails to connect (see: claude mcp list)" || ok "no MCP server reports a connection failure"
  fi
fi

echo
echo "PASS $PASS · WARN $WARN · FAIL $FAIL"
if [ "$FAIL" -gt 0 ]; then echo "VERIFY FAILED"; exit 1; fi
echo "VERIFY OK"
