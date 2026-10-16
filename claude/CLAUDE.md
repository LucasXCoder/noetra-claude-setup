# CLAUDE.md — Master (Noetra)

## Mission
Noetra is my personal AI operating system: persistent memory, specialized multi-agent
"offices" per domain, and one premium design language across everything I build.

## Models — Claude / Max plan ONLY (hard rule)
ALL agent work + office orchestration runs on Claude via the Max plan (Claude Code Task tool).
NEVER use OpenRouter, OpenAI, Gemini, or any third-party model provider. No external API keys.

## Master TODO — single source of truth → `~/.claude/noetra/master-todo.md`
All work across lanes (my projects · school · AI self-funding hunt · parked tools), each with next
step + status. **Phase 4 standup reads it FIRST to plan the day.**
**Priority order: #1 MQL · #2 LL · #3 Noetra** (Scholarship = lowest concern) — finish what's near-built.
**Lanes are separate:** the AI **self-funding hunt** lives in `~/noetra-selffund/` and does NOT touch
LL/MQL/Noetra (those are mine). Money gate everywhere: $0 autonomous spend; I approve before anything goes live.

## TRADING RESEARCH — THREE PERMANENT RULES (set 2026-09-07, non-negotiable)
Full text + enforcement: `~/mql/orb_lab/orb_factory/PAPER_ORB/RULES.md`. These OUTRANK every gate,
preregistration, objective and prior finding. A violating result is **not a result** — withdraw it,
don't caveat it.
1. **REAL AND HONEST.** Every number must be something that could actually happen at a real broker.
   Stop fills slip; gaps jump stops; costs hit every fill. Unmeasurable = UNKNOWN, never 0. A `0`
   true by construction is never reported as if measured. Nothing is delivered until it's honest.
2. **RISK ≤ WHAT THE ACCOUNT CAN LOSE.** Worst plausible realized loss on a position — slippage and
   gaps included, not just the declared stop — must be strictly less than the room remaining at that
   instant. Risking $3,000 to win $1,200 on a $1,000 max-loss account is not bad odds, it's an
   account that is already dead. Never rank, shortlist or headline it. Size is never the free
   variable that manufactures a pass rate.
3. **THE PATH KILLS, NOT THE CLOSE.** Death happens the instant equity breaches the trailing floor;
   what happens after is irrelevant. Netting a day's P&L and checking at the close FABRICATES
   survival and voids the result. Down to 4,000 then back up to win 1,000 is still a dead account.
4. **ONE ACCOUNT, ONE PURCHASE, PASS20.** Every result is for a single account bought once.
   The headline pass figure is PASS20 — target reached within 20 sessions without dying. Campaign
   /re-buy numbers are NEVER called a pass rate. Scope: LucidFlex 25K and TopStep 50K. Caveat that
   must always ride along: PASS20 rises with VARIANCE as well as edge, so any PASS20 claim must be
   tested against its own order-destroying null or declared unproven.

## Memory — ONE global Noetra memory (no islands)
Every session in **every folder** reads/writes the same memory. Two reinforcing layers:
- **This CLAUDE.md** (user-level `~/.claude/`) loads in every session everywhere = the always-on Noetra backbone.
- **Capture = the Noetra capture bridge, no LLM** (`~/.claude-mem/capture-bridge.py` v2, autostarts at logon):
  streams every session transcript into ONE global memory (project `noetra`) via the worker's save API.
  Zero allowance used. Log: `~/.claude-mem/logs/capture-bridge.log`.
- **Store + recall = claude-mem, no LLM** — central store `~/.claude-mem/`, viewer http://localhost:37777.
  Its AI note-taker is **switched off** (it burned the Max allowance): `noetra-patch-hooks.py` removes the
  observation/summarize/session-init hooks; recall on every prompt is `noetra-recall-hook.py` (search only,
  all projects, 8 memories max). The recall hook re-applies the patch if a plugin update restores the hooks.
  Repair record + gates: `~/.claude/noetra/memory-fix/GATES.md` (2026-09-25).
- **Asset vault:** `~/noetra-vault/` is the master long-term store (notes/logs/ideas/screenshots/docs).
  Put anything to remember here. Graphify graph auto-refreshes at logon (`later-tools/` excluded).
- **Second brain:** drop sources in `~/noetra-vault/raw-sources/`; the **noetra-librarian** skill
  distills them into a cited, cross-linked `wiki/` and answers "brief me on X / gaps in my knowledge"
  (answers saved back so it compounds). Weekly contradiction/staleness check runs in the Phase 4 standup.
- Native `~/.claude/projects/.../memory/` is a **FROZEN read-only backup** — don't write; retire on/after **2026-06-24**.

## Context on demand
Active projects, yearly goals, the chapter roadmap, Noetra Offices and parked tools → `~/.claude/noetra/CONTEXT.md`. Read it when planning, prioritising or running the standup, or when a request names a project (BirdQuant, Odysseus, LL, MQL, Scholarship Office, 404 Protocol, PermitPulse, underwear brand). Current focus: Chapter 1 through Phase 3 done; next = Phase 4 (Autonomous Mode). Multi-agent offices are scoped to `~/noetra-offices` only.

## Mandatory workflow (every session, every project)
- **Done = a check exits 0.** Run the project's test/build/typecheck, paste the command and its output; no evidence = not done. Bug fix: write a failing test first. Never delete, skip or loosen a test to pass it. UI change: screenshot, compare, fix the differences. Library/framework API or config: query Context7 (or the `docs-lookup` agent) before writing code.
- **Superpowers, in order:** new feature or behaviour → `superpowers:brainstorming` first; multi-step build → `writing-plans`; bug or failing test → `systematic-debugging` before any fix; code → `test-driven-development`; before saying complete → `verification-before-completion`.
- **Substantial or multi-part work → unlazy** (write the gates first; see the Unlazy section).
- **Any UI/frontend → read `~/.claude/noetra/DESIGN.md` first**, then impeccable + taste-skill.
- **Claude / Claude Code / limits / skills / MCP questions → consult the `nocodealex` brain**, but take exact CLI and settings syntax from code.claude.com/docs.
- **"Brief me on X" → `noetra-librarian`.** Missing a capability → `find-skills`.

## Compact instructions
When compacting, preserve: modified-file list, test/build commands and the last result, open gates/TODOs, decisions and why, every user correction.

## Coding style
- **VS Code primary** (`.vscode/` settings, launch/workspace configs). **Modular always** — separate files, never monolithic.
- **Clear, intentional names** — build as if someone else reads it. **Premium & polished**, never templated. Quality over speed.
- **Token-efficient & terse** — minimal boilerplate, comments only where earned. **Typed & strict** (TS/type hints, fail-fast).
- **Match the repo** — existing project conventions override these global prefs.

## Design system
Noetra **DESIGN.md** (premium dark, 3D depth, glassmorphism, physics-based motion, awwwards-tier)
governs ALL UI — dashboards, landing pages, agents. → **`~/.claude/noetra/DESIGN.md`** (read before any frontend work; pair with impeccable + taste-skill + design-motion-principles).

## Pointers
- Foundation plan: `~/.claude/plans/noetra-master-peppy-ocean.md`
- Deeper project/goal detail: query claude-mem, or the project's own repo.
- **Skill discovery:** use **find-skills** to search/install new skills. Installed: ECC subset + graphify in `~/.claude/skills/`, subagents in `~/.claude/agents/`.
# graphify
- **graphify** (`~/.claude/skills/graphify/SKILL.md`) - any input to knowledge graph. Trigger: `/graphify`
When the user types `/graphify`, invoke the Skill tool with `skill: "graphify"` before doing anything else.

## Unlazy — completion discipline (installed 2026-08-24)
Skill `~/.claude/skills/unlazy` (v2.1.0) + **global Stop hook** in `~/.claude/settings.json`: a session
cannot end while its resolved pipeline has unmet gates (self-releases after 6 no-progress blocks; inert
when no ledger exists). Triggers: `/unlazy`, "gates", "tree N", "do not stop until it is done".
Setup ledger + verification oracles → `~/.claude/noetra/unlazy-setup/`.

**The rule:** never promise done — prove it against `GATES.md`. Every gate is one observable outcome with
an indented `CHECK:` + `EXPECT:`; success needs **both** exit 0 **and** an `EXPECT:` match, so a command
that prints the marker then exits nonzero still fails. A checked box whose `EVIDENCE:` is `pending` is
unmet. An impossible gate gets `ABANDON: <id> <reason>` — terminal handoff, never completion.
Lint before working a ledger (`gate-lint.mjs`); re-measure every number at report time.

**`CHECK:` is code.** Inherited ledgers: read with `--status` (never executes), inspect every called
script, then `--approve` explicitly. Approvals live in `~/.unlazy/approved`.

**Windows gotchas (this machine):** default shell resolves to `cmd.exe`; stock Windows has no `grep`,
`tail`, `tr`, or `sed` — write gates as portable Node scripts, not POSIX pipelines. Approval binds the
**full inherited `PATH`**, so an oracle approved from Git Bash needs re-approval when run from PowerShell.

**Fan-out — orchestrated mode only, never automatic:** fix interfaces, file ownership and naming in
`PLAN.md` *before* any dispatch. Give every leaf its own gates file with disjoint `OWNS:` paths and claim
them first. Launch the whole ready wave as background `Agent` tasks, record every handle, **seal the wave,
and only then wait for the first result** — sealing before waiting is what makes it parallel instead of
serial. Re-run each returned leaf's gates yourself with `--reverify`; a leaf's own report is not evidence.
Wave width follows host concurrency (~10 is a starting tune, not a spec). Fan-out stays opt-in: only on
explicit request or when orchestrated unlazy mode is invoked.
