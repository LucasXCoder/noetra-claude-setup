# CHANGELOG — Claude re-optimization (2026-10-16)

Every change to the live setup, with its backup and how to revert. Backups live in
`~/.claude/noetra/claude-optimize/backups/2026-10-16/`. Verified by `node tools/verify.mjs applied`.

## fix-claude-mem-observer — claude-mem AI note-taker was silently back ON (allowance drain)
- **Found:** claude-mem auto-updated to 13.39.0 (2026-10-15 22:41), which moved its hooks to exec
  form (`"command": "claude-mem", "args": ["hook","claude-code","observation"]`) and added a
  `PostToolUseFailure` observation hook. `noetra-patch-hooks.py` matched only the `command` string,
  so all 9 hooks.json copies had the observer, summarizer and per-prompt session-init re-enabled.
  The Noetra recall hook (which carried the 6-hourly self-heal) had been replaced by the plugin's
  own session-init, so nothing re-patched it. `observer-health.json` showed recent observer
  successes and an earlier "inference allowance exhausted" error.
- **Changed:** `~/.claude-mem/noetra-patch-hooks.py` — matches `command + args`, and patches
  `PostToolUseFailure` too. Re-ran it: 9 files patched (each original kept once as `hooks.json.orig`).
- **Verify:** `python ~/.claude-mem/noetra-patch-hooks.py --check` → `NOETRA HOOKS OK`.
- **Revert:** copy `backups/2026-10-16/claude-mem/noetra-patch-hooks.py` back; restore each
  `hooks.json.orig` over `hooks.json`.

## fix-mcp-magic — removed the dead 21st.dev `magic` MCP server
- **Found:** every session showed `magic … ✘ Failed to connect — -32001: Not authenticated - your
  API key is missing or was reset`. It is also a third-party AI generator behind an external API
  key, which CLAUDE.md's "Claude via Max only, no external API keys" rule excludes.
- **Changed:** `claude mcp remove magic -s user` (user scope in `~/.claude.json`).
- **Revert:** `claude mcp add magic -s user -e API_KEY=<new key from 21st.dev/mcp> -- npx -y @21st-dev/magic@latest`,
  or restore `backups/2026-10-16/dot-claude.json` (contains secrets — keep local).

## fix-engram-audit — engram's coverage audit could not audit current brains
- **Found:** `~/.claude/skills/engram/coverage_audit.py` read only the legacy `claims.jsonl` and
  only `sources/transcripts/`, while engram's SKILL.md requires `atoms.jsonl` and brains now carry
  guides/docs/repos — so the mandatory Step 3e gate could not run on a new brain.
- **Changed:** reads `atoms.jsonl` (falls back to `claims.jsonl`), takes source texts from
  `sources/manifest.json` `text_path` entries (falls back to transcripts), skips <20-word trivial
  sources, reports edge connectivity, and fails when nothing was audited.
- **Revert:** copy `backups/2026-10-16/skills/engram/coverage_audit.py` back.

## opt-claude-mem-selfheal — self-heal that survives plugin updates
- **Changed:** `~/.claude/settings.json` → `hooks.SessionStart` (matcher `startup`) runs
  `python -I ~/.claude-mem/noetra-patch-hooks.py --quiet` every session. Silent when hooks are
  already patched; prints a one-line notice into context when it had to re-patch.
- **Revert:** delete that SessionStart entry, or restore `backups/2026-10-16/settings.json`.

## opt-skill-listing-diet — 58 niche, never-used skills shown by name only
- **Why:** 86 local skills ≈ 6,000 tokens of descriptions re-sent every turn; 74 had never been
  used (`optimization/overhead.json`, from `~/.claude.json` skillUsage). Crowded listings also get
  truncated to fit the 1% skill budget, which hurts triggering of the skills you do use.
- **Changed:** `skillOverrides` → `"name-only"` for 58 skills (list in `tools/apply-settings.mjs`).
  They stay installed and invocable as `/name`; Claude still sees their names.
- **Revert:** remove the `skillOverrides` block (or set any one back to `"on"`).

## rec-12-mac-transfer — Mac bundle
- **Added:** `mac-bundle/` (built by `tools/build-mac-bundle.mjs`): CLAUDE.md, 86 skills, 32 agents,
  Noetra docs, portable `settings.template.json`, claude-mem bridge scripts + LaunchAgent, plugin list,
  `install.sh` (backs up first; `--dry-run`, `--no-network`). Verified by a real install into a scratch HOME.
- **Revert:** delete the folder (nothing on this PC depends on it).

## Pending your approval (blocked by the auto-mode self-modification guard)
Written and tested, but NOT wired into `settings.json`: `~/.claude/statusline.mjs`,
`~/.claude/hooks/guard-shell.mjs`, `~/.claude/hooks/protect-files.mjs` (fixtures: `node tools/test-hooks.mjs`).
Decisions rec-01 … rec-11 in `optimization/plan.json` list each pending change.

## fix-claude-mem-observer (again) — 13.40.0 auto-updated mid-session
- claude-mem updated to 13.40.0 during this session and re-enabled the observer in 2 hooks.json
  files. The fixed patcher handled the new version; `--check` → `NOETRA HOOKS OK`. This is why
  rec-03 (thedotmack `autoUpdate: false` + `CLAUDE_MEM_DISABLE_OBSERVATION=1`) is worth approving.

## Approved by Lucas 2026-10-16 — research settings applied (`tools/apply-settings-research.mjs`)
- **rec-01-effort-per-model:** `modelSettings` → `claude-sonnet-5-5` and `claude-opus-5-5` `effortLevel: "high"`
  (top-level effortLevel is ignored on 5.5 models since v2.1.280 — Sonnet had been running at medium).
- **rec-02-money-gate:** `env.CLAUDE_CODE_DISABLE_FAST_MODE=1`. Still manual: turn **Usage credits OFF** at claude.ai/settings/usage.
- **rec-03-claude-mem-seal:** `env.CLAUDE_MEM_DISABLE_OBSERVATION=1`; marketplace `thedotmack` `autoUpdate: false`.
- **rec-04-autocompact-400k:** `autoCompactWindow` 700000 → 400000. Also `env.PYTHONUTF8=1` (cp1252 crash fix).
- **rec-05-statusline:** `statusLine` → `~/.claude/statusline.mjs` (model·effort, context %, 5h/7d usage, cache timer).
- **rec-11-guard-hooks:** `PreToolUse` `Bash|PowerShell` → `~/.claude/hooks/guard-shell.mjs` (deny/ask on destructive
  commands); `Edit|Write|MultiEdit` → `~/.claude/hooks/protect-files.mjs` (blocks PAPER_ORB/RULES.md, .env, keys, .ssh, .git).
  Both `onFailure: "block"`. Fixtures: `node tools/test-hooks.mjs`.
- **rec-07-lsp-plugins:** `npm i -g pyright typescript-language-server typescript`;
  `claude plugin install pyright-lsp@claude-plugins-official` and `typescript-lsp@claude-plugins-official`.
- **Revert:** restore `backups/2026-10-16/settings.json`; `claude plugin uninstall pyright-lsp typescript-lsp`.

## Round 2: "Yes do all these things" (2026-10-16)
- **rec-10 skills/plugins:** `skillOverrides`: `ckm:design`, `ckm:banner-design`, `data-scraper-agent` (Gemini-keyed) and
  `verification-loop` (duplicate) set to `off`; `skill-creator` to `name-only`. `code-review@claude-plugins-official` disabled
  (the bundled `/code-review` supersedes it). Skills `security-review` renamed `ecc-security-checklist` and `deep-research`
  renamed `deep-research-exa`, so the built-in `/security-review` and `/deep-research` are no longer shadowed.
  Revert: `backups/2026-10-16/final/` (settings, skills); rename the two dirs back.
- **opt-auto-memory-off:** `autoMemoryEnabled: false` (native memory is the frozen backup; claude-mem + the vault are the memory).
- **opt-explore-haiku:** new `~/.claude/agents/Explore.md` (`model: haiku`, effort low, 100K compact cap); `code-explorer` and
  `docs-lookup` agents set to `model: haiku`. Revert: delete Explore.md; `backups/2026-10-16/final/agents/`.
- **rec-08/09 + opt-mandatory-workflow (CLAUDE.md):** 154 to 114 lines (13.0 to 9.9 KB). Projects, yearly goals, roadmap, offices and
  parked tools moved to `~/.claude/noetra/CONTEXT.md` (loaded on demand). Added **Mandatory workflow** (done = a check exits 0;
  superpowers in order; unlazy for big work; DESIGN.md for UI; nocodealex for Claude questions; librarian; find-skills) and
  **Compact instructions**. Trading rules, Memory and Unlazy sections kept verbatim: two existing oracles depend on them.
  Revert: `backups/2026-10-16/final/CLAUDE.md`.
- **opt-memory-check-fix:** `noetra/memory-fix/memory_check.py --observer` crashed on a removed hard-coded plugin version; it now reads
  the installed version and exec-form hooks.
- **rec-06 auto mode: NOT applied.** The auto-mode classifier blocks Claude from editing its own permission rules even with chat
  approval. Exact change and the safe route are in `PERMISSIONS-FOR-LUCAS.md`.
- **opt-github-public-repo:** https://github.com/LucasXCoder/noetra-claude-setup (public). Built by `tools/build-mac-bundle.mjs --public`,
  published by `tools/publish-public.mjs "message"` (scrub scan first; refuses to push on any hit). Left out on purpose: the
  `delta`/`tradexlabs` brains (other creators' teaching), raw scraped transcripts/guide text/repo clones, `master-todo.md` (stub only),
  the claude-mem database, all secrets. Redacted: local paths, a prospect's name, the owner's email. Commits use the GitHub no-reply address.
- **Verified live:** a brand-new `claude -p` session loaded the new settings, saw the nocodealex skill, and the claude-mem observer made
  no call (its last-success timestamp did not move). The 13.39/13.40 regression is closed in practice.

**Change ids in this round:** rec-08-verification, rec-09-claudemd-slim, rec-10-gemini-skills-off, opt-auto-memory-off, opt-explore-haiku, opt-mandatory-workflow, opt-memory-check-fix, opt-github-public-repo, rec-06-auto-mode (deferred).
