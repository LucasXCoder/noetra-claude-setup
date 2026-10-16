#!/usr/bin/env bash
# One-command setup for a fresh Mac:
#
#   curl -fsSL https://raw.githubusercontent.com/LucasXCoder/noetra-claude-setup/main/bootstrap.sh | bash
#
# Installs the prerequisites (Xcode command line tools, Homebrew, Node, Claude Code), clones this repo
# to ~/noetra-claude-setup, runs install.sh, then verify.sh. Safe to re-run: it resumes where it stopped.
# Extra arguments pass through to install.sh, e.g.  ... | bash -s -- --dry-run
set -euo pipefail

REPO="LucasXCoder/noetra-claude-setup"
DEST="${NOETRA_DIR:-$HOME/noetra-claude-setup}"
say()  { printf '\033[1;36m==>\033[0m %s\n' "$*"; }
warn() { printf '\033[1;33m!!\033[0m %s\n' "$*" >&2; }
have() { command -v "$1" >/dev/null 2>&1; }

[ "$(uname -s)" = Darwin ] || warn "Built for macOS ($(uname -s) detected); continuing, but Homebrew steps may not apply."

# 1. Xcode command line tools provide git and python3.
if [ "$(uname -s)" = Darwin ] && ! xcode-select -p >/dev/null 2>&1; then
  say "Installing Xcode command line tools (a dialog will open)…"
  xcode-select --install || true
  warn "Finish the install dialog, then run this same command again."
  exit 1
fi

# 2. Homebrew, then Node (the hooks, status line and settings merge run on Node).
if [ "$(uname -s)" = Darwin ] && ! have brew; then
  say "Installing Homebrew…"
  NONINTERACTIVE=1 /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
fi
for b in /opt/homebrew/bin/brew /usr/local/bin/brew; do [ -x "$b" ] && eval "$("$b" shellenv)" && break; done
if ! have node; then
  have brew && { say "Installing Node…"; brew install node; } || warn "node missing: install it from nodejs.org, then re-run."
fi

# 3. Claude Code (official installer). Needs a one-time login afterwards.
export PATH="$HOME/.local/bin:$PATH"
if ! have claude; then
  say "Installing Claude Code…"
  curl -fsSL https://claude.ai/install.sh | bash
  export PATH="$HOME/.local/bin:$PATH"
fi
have claude || { warn "claude not on PATH yet — open a new terminal and re-run."; exit 1; }

# 4. Fetch (or update) this repo.
if [ -d "$DEST/.git" ]; then
  say "Updating $DEST…"
  git -C "$DEST" pull --ff-only
else
  say "Cloning $REPO → $DEST…"
  git clone --depth 1 "https://github.com/$REPO.git" "$DEST"
fi

# 5. Install, then verify.
say "Installing the Noetra Claude setup…"
bash "$DEST/install.sh" "$@"
say "Verifying…"
bash "$DEST/verify.sh" || warn "verify.sh reported problems — see above."

cat <<'EOF'

Next (3 minutes, by hand — these are account/secret steps nothing can do for you):
  1. Run `claude` once and log in with your Max account, then /exit and start it again.
  2. Settings → Usage on claude.ai: make sure "Usage credits" is OFF.
  3. Re-add MCP servers that need secrets (see INSTALL-FOR-CLAUDE.md, "Manual steps").
  4. In Claude Code run /doctor and /usage once to confirm a clean start.
EOF
