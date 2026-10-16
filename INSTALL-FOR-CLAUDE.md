# Install guide for Claude Code (read this if you are the Claude running on the Mac)

You are setting up this Mac's Claude Code to match the owner's tuned Windows setup. Do it in order,
show real command output, and do not claim success without `verify.sh` printing `VERIFY OK`.

## Ground rules
- **Do not edit `permissions`, `autoMode` or `defaultMode` in `settings.json`.** Those are the owner's call
  (see `claude/noetra/claude-optimize/PERMISSIONS-FOR-LUCAS.md`). Everything else is fair game.
- **Never print, copy or commit secrets** (API keys, OAuth tokens, `~/.claude.json`). If a step needs one, stop and ask.
- **Back up before replacing.** `install.sh` already copies anything it overwrites to
  `~/.claude/backups/pre-noetra-<timestamp>/`. Tell the owner where.
- **Claude models via the Max plan only.** Do not add any other model provider or paid API key, ever.
- Money gate: spend $0 autonomously. Do not turn on usage credits or extra usage.

## Steps
1. **Check the machine.** `uname -s` should print `Darwin`. Run `claude --version`, `node --version`, `python3 --version`, `git --version`.
   If anything is missing, run `./bootstrap.sh` (it installs Xcode tools, Homebrew, Node and Claude Code) and re-check.
2. **Get the repo** (skip if you are already inside it):
   `git clone https://github.com/LucasXCoder/noetra-claude-setup.git ~/noetra-claude-setup && cd ~/noetra-claude-setup`
3. **Preview.** `./install.sh --dry-run` — read the plan back to the owner in two or three lines.
4. **Install.** `./install.sh`. It copies `CLAUDE.md`, skills, agents, hooks, the status line and the Noetra docs;
   renders `settings.json` for this home folder (merging with any existing one); adds the plugin marketplaces and
   plugins with `claude plugin …`; and re-applies the claude-mem patch that keeps its AI note-taker off.
5. **Verify.** `./verify.sh`. Fix every `FAIL`. A `WARN` is something only the owner can do (log in, re-auth a connector).
6. **Memory.** claude-mem installs with the plugins; its store starts fresh on this Mac. To capture sessions at login:
   `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.noetra.capture-bridge.plist`
   (the file is written by `install.sh`). Check the worker with `curl -s -o /dev/null -w '%{http_code}\n' http://localhost:37777/` → `200`.
7. **Restart Claude Code**, then run `/doctor`, `/context` and `/usage` once.
8. **Report** to the owner: what was installed, the `verify.sh` summary line, the backup folder, and the manual steps below.

## Manual steps (tell the owner; do not attempt)
- Log in to Claude Code with the Max account (`claude`, then follow the prompt).
- claude.ai → Settings → Usage: **Usage credits OFF**.
- Re-add MCP servers that need a secret. `manifest.json → mcp` lists them by name only
  (`composio-gmail`: recreate the connection in Composio, then `claude mcp add --transport http composio-gmail <url> --header "x-api-key: <key>"`).
- Private items that are deliberately not in this public repo (`manifest.json → private_items`): the trading brains
  (`skills/delta`, `skills/tradexlabs`), the real `~/.claude/noetra/master-todo.md`, and the 600 MB+ claude-mem database.
  Copy them from the PC over OneDrive/AirDrop if wanted.
- Optional: apply the permission/auto-mode rules from `PERMISSIONS-FOR-LUCAS.md` via `/auto-mode-setup`.

## What "same level as the PC" means
`CLAUDE.md` (mandatory workflow: verify-before-done, superpowers order, unlazy gates), 86 skills incl. the `nocodealex`
brain (8,291 facts about Claude/Claude Code optimisation), 32 agents (Explore on Haiku), the guard hooks
(destructive-command guard, protected files), a status line, and the plugins: superpowers, claude-mem,
frontend-design and the Python/TypeScript code-intelligence plugins.
