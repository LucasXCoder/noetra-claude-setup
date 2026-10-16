# Permission changes for you to apply (the auto-mode safety guard won't let Claude edit these)

Claude Code's auto-mode classifier blocks Claude from editing its own permission rules and auto-mode
rulebook, even when you ask in chat. That is a sensible guard, so these are yours to apply.

## Easiest: you already ran `/auto-mode-setup`
It drafts and applies the auto-mode rulebook through Claude Code's own flow (which is allowed to).
When it shows its draft, make sure it includes these two lines. Then run `claude auto-mode critique`.

- **hard_deny:** "Never place, modify or cancel live (non-paper) orders on TopstepX/ProjectX or any broker API"
- **hard_deny:** "Never make purchases, payments or subscriptions, and never turn on usage credits or extra usage"
- **soft_deny:** "Never send email or messages to people outside this machine; drafts are fine"

Keep `"$defaults"` as the first entry of each list.

## Or paste this into `~/.claude/settings.json` yourself (merge into the existing blocks)
```json
"permissions": {
  "defaultMode": "auto",
  "deny": [
    "Read(./.env)", "Read(./.env.*)",
    "Bash(git push --force *)", "PowerShell(git push --force *)",
    "Edit(~/mql/orb_lab/orb_factory/PAPER_ORB/RULES.md)",
    "Skill(claude-mem:wowerpoint)", "Skill(claude-mem:cloud-sync)", "Skill(claude-mem:screenpipe)"
  ],
  "ask": [
    "Bash(git push *)", "PowerShell(git push *)",
    "mcp__composio-gmail__GMAIL_SEND_EMAIL", "mcp__composio-gmail__GMAIL_REPLY_TO_THREAD"
  ]
},
"autoMode": {
  "hard_deny": ["$defaults",
    "Never place, modify or cancel live (non-paper) orders on TopstepX/ProjectX or any broker API",
    "Never make purchases, payments or subscriptions, and never turn on usage credits or extra usage"],
  "soft_deny": ["$defaults", "Never send email or messages to people outside this machine; drafts are fine"]
}
```
Keep your existing `allow` entries. Auto mode only reads these from your **user** settings.
Revert: set `"defaultMode"` back to `"acceptEdits"`.
The PreToolUse safety hooks (guard-shell, protect-files) are already live and cover the worst cases in the meantime.
