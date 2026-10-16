# unlazy self-setup

Proof that the `unlazy` skill is installed and actually enforces on this machine.
`GATES.md` is the ledger; the `verify-*.mjs` / `lint-ledger.mjs` files are its oracles.

Re-check at any time (nothing is trusted from memory):

    node ~/.claude/skills/unlazy/scripts/gate-check.mjs --reverify ~/.claude/noetra/unlazy-setup/GATES.md

`--status` only reads recorded history; `--reverify` re-executes. Approvals bind the full inherited
`PATH`, so re-approve if you run this from PowerShell rather than Git Bash.

Rollback: `node ~/.claude/skills/unlazy/scripts/install-hooks.mjs --global --uninstall`
Backups: `~/.claude/settings.json.unlazy.bak`, `~/.claude/CLAUDE.md.pre-unlazy.bak`
