#!/usr/bin/env bash
# Noetra Claude Code setup — installer for macOS (works on Linux too).
#
#   ./install.sh                 install into $HOME, then add marketplaces/plugins via the claude CLI
#   ./install.sh --no-network    files only (skip plugin installs)
#   ./install.sh --dry-run       print what would happen, change nothing
#   ./install.sh --home DIR      install into DIR instead of $HOME (used by the bundle self-test)
#
# Safe to re-run. Anything it would overwrite is first copied to
# ~/.claude/backups/pre-noetra-<timestamp>/.
set -euo pipefail

TARGET_HOME="$HOME"
NETWORK=1
DRY=0
usage() { sed -n '2,11p' "$0" | sed 's/^# \{0,1\}//'; }
while [ $# -gt 0 ]; do
  case "$1" in
    --home) TARGET_HOME="${2:?--home needs a directory}"; shift 2 ;;
    --no-network) NETWORK=0; shift ;;
    --dry-run) DRY=1; shift ;;
    -h|--help) usage; exit 0 ;;
    *) echo "unknown argument: $1" >&2; usage; exit 2 ;;
  esac
done

HERE="$(cd "$(dirname "$0")" && pwd)"
CL="$TARGET_HOME/.claude"
MEM="$TARGET_HOME/.claude-mem"
STAMP="$(date +%Y%m%d-%H%M%S)"
BACKUP="$CL/backups/pre-noetra-$STAMP"

say()  { printf '\033[1;36m==>\033[0m %s\n' "$*"; }
warn() { printf '\033[1;33m!!\033[0m %s\n' "$*" >&2; }
run()  { if [ "$DRY" = 1 ]; then printf 'DRY: %s\n' "$*"; else "$@"; fi; }
have() { command -v "$1" >/dev/null 2>&1; }

backup() {  # backup <path relative to ~/.claude>
  if [ -e "$CL/$1" ]; then
    run mkdir -p "$BACKUP/$(dirname "$1")"
    run cp -Rp "$CL/$1" "$BACKUP/$1"
  fi
}

say "Installing Noetra Claude setup into $CL"
run mkdir -p "$CL" "$MEM"

# 1. Back up what we are about to replace.
for item in CLAUDE.md settings.json agents noetra; do backup "$item"; done
if [ -d "$CL/skills" ]; then
  for s in "$HERE"/claude/skills/*/; do backup "skills/$(basename "$s")"; done
fi

# 2. Memory file, skills, agents, Noetra docs, optional extras.
run cp -p "$HERE/claude/CLAUDE.md" "$CL/CLAUDE.md"
for dir in skills agents noetra output-styles commands hooks; do
  if [ -d "$HERE/claude/$dir" ]; then
    run mkdir -p "$CL/$dir"
    run cp -Rp "$HERE/claude/$dir/." "$CL/$dir/"
  fi
done
for f in keybindings.json statusline.mjs; do
  [ -f "$HERE/claude/$f" ] && run cp -p "$HERE/claude/$f" "$CL/$f"
done

# 3. settings.json: render __HOME__, then merge into any existing Mac settings.
RENDERED="$(mktemp "${TMPDIR:-/tmp}/noetra-settings.XXXXXX")"
trap 'rm -f "$RENDERED"' EXIT
ESCAPED_HOME="$(printf '%s' "$TARGET_HOME" | sed 's/[\/&|]/\\&/g')"
sed "s|__HOME__|$ESCAPED_HOME|g" "$HERE/claude/settings.template.json" > "$RENDERED"
if [ "$DRY" = 1 ]; then
  echo "DRY: merge rendered settings into $CL/settings.json"
elif [ -f "$CL/settings.json" ] && have node; then
  node "$HERE/merge-settings.mjs" "$CL/settings.json" "$RENDERED" > "$CL/settings.json.new"
  mv "$CL/settings.json.new" "$CL/settings.json"
elif [ -f "$CL/settings.json" ] && have python3; then
  python3 "$HERE/merge_settings.py" "$CL/settings.json" "$RENDERED" > "$CL/settings.json.new"
  mv "$CL/settings.json.new" "$CL/settings.json"
else
  cp "$RENDERED" "$CL/settings.json"
fi

# 4. Noetra memory bridge scripts (claude-mem stays the store; these keep its AI note-taker off).
if [ -d "$HERE/claude-mem" ]; then
  run cp -p "$HERE"/claude-mem/*.py "$MEM/"
fi
if [ "$(uname -s)" = Darwin ] && [ "$TARGET_HOME" = "$HOME" ] && [ -f "$HERE/com.noetra.capture-bridge.plist.template" ]; then
  AGENT_DIR="$HOME/Library/LaunchAgents"
  run mkdir -p "$AGENT_DIR" "$MEM/logs"
  if [ "$DRY" = 0 ]; then
    sed -e "s|__HOME__|$ESCAPED_HOME|g" -e "s|__PYTHON__|$(command -v python3 || echo /usr/bin/python3)|g" \
      "$HERE/com.noetra.capture-bridge.plist.template" > "$AGENT_DIR/com.noetra.capture-bridge.plist"
  fi
  say "Capture bridge LaunchAgent written. Start it after claude-mem is installed:"
  echo "    launchctl bootstrap gui/$(id -u) $AGENT_DIR/com.noetra.capture-bridge.plist"
fi

# 5. Marketplaces + plugins through the official CLI (needs network and a logged-in claude).
if [ "$NETWORK" = 1 ]; then
  if have claude; then
    while IFS='|' read -r kind name repo; do
      [ -z "$kind" ] && continue
      if [ "$kind" = market ]; then
        run claude plugin marketplace add "$repo" || warn "marketplace $repo: add failed (already added?)"
      else
        run claude plugin install "$name" || warn "plugin $name: install failed"
      fi
    done < <(node -e '
      const m = require(process.argv[1]);
      for (const x of m.marketplaces) console.log(`market|${x.name}|${x.repo}`);
      for (const p of m.plugins) console.log(`plugin|${p}|`);' "$HERE/manifest.json" 2>/dev/null \
      || python3 -c '
import json,sys
m=json.load(open(sys.argv[1]))
for x in m["marketplaces"]: print("market|%s|%s" % (x["name"], x["repo"]))
for p in m["plugins"]: print("plugin|%s|" % p)' "$HERE/manifest.json")
    if have python3 && [ -f "$MEM/noetra-patch-hooks.py" ]; then
      run python3 "$MEM/noetra-patch-hooks.py" || warn "claude-mem hook patch failed — run it after the plugin installs"
    fi
  else
    warn "claude CLI not found — install it (curl -fsSL https://claude.ai/install.sh | bash), log in, then re-run."
  fi
else
  say "Skipping plugin installs (--no-network)."
fi

# 5b. Language servers the pyright-lsp / typescript-lsp plugins call (they do nothing without the binaries).
if [ "$NETWORK" = 1 ] && have npm; then
  run npm install -g pyright typescript-language-server typescript || warn "language servers: npm install failed (try with sudo or fix npm's prefix)"
fi

# 5c. Skill router (hooks/skill_router.py): local embedding model + runtime. Best effort; without it the hook does nothing.
if [ "$NETWORK" = 1 ] && have python3; then
  MODEL_DIR="$TARGET_HOME/.cache/chroma/onnx_models/all-MiniLM-L6-v2"
  run python3 -m pip install --user --quiet onnxruntime tokenizers numpy || warn "skill router: pip install failed (the hook stays inert)"
  if [ ! -f "$MODEL_DIR/onnx/model.onnx" ]; then
    run mkdir -p "$MODEL_DIR"
    run curl -fsSL -o "$MODEL_DIR/onnx.tar.gz" https://chroma-onnx-models.s3.amazonaws.com/all-MiniLM-L6-v2/onnx.tar.gz \
      && run tar -xzf "$MODEL_DIR/onnx.tar.gz" -C "$MODEL_DIR" || warn "skill router: model download failed (the hook stays inert)"
  fi
fi

# 5d. Keyless MCP servers (user scope; telemetry off). Playwright/Serena/Context7 come with their plugins.
if [ "$NETWORK" = 1 ] && have claude; then
  while IFS='|' read -r name args; do
    [ -z "$name" ] && continue
    # shellcheck disable=SC2086
    run claude mcp add "$name" -s user $args || warn "mcp $name: add failed (already added?)"
  done < <(node -e 'for (const e of require(process.argv[1]).mcp_install || []) console.log(e)' "$HERE/manifest.json" 2>/dev/null)
  have uvx || warn "uv not found: Semgrep/Serena MCP need it (brew install uv)."
fi

# 6. Prerequisites the hooks need.
have node || warn "node not found: the unlazy Stop hook and statusline need it (brew install node)."
have python3 || warn "python3 not found: the claude-mem recall/patch hooks need it (xcode-select --install)."

say "Done. Backup of anything replaced: $BACKUP"
say "Next: open README.md → 'After installing' (MCP re-auth, /terminal-setup, Mac checklist)."
