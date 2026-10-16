# Claude Code commands, settings, effort levels, hooks and fixes

Alex teaches Claude Code as configuration, not prompting: "the model is not the bottleneck; the setup around it is" `g20-0224`. His fifteen tips hold "no clever prompts", only settings, surfaces and habits `g16-0171`.

## What he believes (CORE first)

- **Every session starts blank.** A correction you type in chat dies with that chat. His example is "no, we use pnpm" on Monday and npm again on Tuesday `g06-0239` `r03-0005` `r03-0006`. So persistent memory comes before tools, agents or autonomy `g20-0286`. Memory is "a loop you build" `g20-0147`.
- **Subtract instructions.** A CLAUDE.md written for an older model makes current models worse `g16-0011` `g12-0092` `g18-0284`. Anthropic cut over 80% of the Claude Code system prompt and measured no loss on its coding evals `g16-0258`.
- **Corrections become rules.** A mistake that comes back sharpens the old rule. It does not get a second one `r03-0011`.
- **Rules are only instructions; hooks enforce.** He pairs prose rules with hooks, branch protection or removed connectors `r04-0019` (INFERRED).
- **Check the version first.** Most of his settings guides open with `claude --version` against a minimum version, from 2.1.234 to 2.1.299 `g03-0002`. Env settings take effect only in a new session `g03-0003`.

## Frameworks, step by step

**Four upgrades, in order:** memory, then MCP, then subagents, then the loop. Each one builds on the last `g20-0229`.

**memory.md loop:** one root file, read before every job and appended after `g20-0148` `g20-0150`. Prompt: "Read memory.md before you do anything else. Treat every line in it as a decision I have already made." `g20-0152` plus "Do not ask me to re-explain anything that is already in there" `g20-0153`. Append decisions, corrected preferences, and breaks with their cause `g20-0155`–`g20-0157`. "One fact per line. No prose. No duplicates." `g20-0158`

**/learn self-improving loop** (github.com/alexyc9381/learn-skill) `r01-0034`:
1. `/learn setup` does four things: it copies learn.py to `.claude/hooks/`, merges a UserPromptSubmit hook into `.claude/settings.json`, creates LESSONS.md and adds `@LESSONS.md` to CLAUDE.md `r03-0074`.
2. The hook logs prompts that sound like corrections ("no, I told you…") to `.learn/inbox.jsonl`. It never blocks a prompt `r03-0012` `r03-0047`.
3. A nightly headless investigator turns the inbox into rules. It runs with `--permission-mode dontAsk` and an allowlist of the script plus `Edit(./LESSONS.md)`, so it cannot touch your code `r03-0039` `r03-0097`.
4. The rulebook is capped at 40 rules. Once it is full, a rule has to be merged or dropped before a new one goes in `r03-0049` `r03-0050`.

**CLAUDE.md cleanup:** read it as if written for an excellent new hire. Delete lines guarding against mistakes not seen in the last month, and anything the code already shows. Keep stack, conventions and hard rules `g18-0232`–`g18-0235`. His 14-row list has 8 CUT and 6 KEEP `g18-0245`. KEEP: test commands, deploy steps, architecture whys, rules broken twice, naming, credential locations and quirks `g18-0254`–`g18-0259`. For Opus 5.5, also drop CRITICAL/MUST shouting and swap step-by-step scripts for the goal `g12-0110` (INFERRED).

**/bouncer:** THE ASK (your request in one sentence), THE LIST (every change considered), THE DOOR (tick only what the ask needs), then report what was turned away `g08-0197`–`g08-0200`.

## Exact commands and numbers

- **Effort:** `/effort` opens a slider (low, medium, high, xhigh, max) with an Ultracode toggle `g10-0181`. Medium is the default `y03-0038`. Claude's own team builds on low and tests on high `y03-0037` `y03-0039`. Thariq Shihipar's fitness-tracker test took 1.5 min on low, 4 on medium, 11 on high and 67 on max `g10-0189`–`g10-0192`. Max takes about 45x as long as low `g10-0195`. Effort does not change the model `g10-0185`. A subagent's file can set it with `effort: low` `g05-0167`. Per-run subagent effort needs v2.1.292 or later `g05-0171`.
- **Hooks:** hooks fail open by default `g04-0056`. Adding `"onFailure": "block"` (v2.1.295+) makes a failure act like exit code 2 `g04-0058` `g04-0060`. Tier 1 tips are a PreToolUse hook that blocks a push to main and a PostToolUse hook that runs the formatter `g19-0025` `g19-0026`.
- **Unattended runs:** `CLAUDE_CODE_RETRY_WATCHDOG=1` retries 429/529 indefinitely (default: 10 tries) `g03-0056` `g03-0050`. `claude --bg --name "x" "task"` survives closing the terminal `g03-0084`. Also `autoContinueAtUsageLimit` `g03-0172`, and the CLAUDE.md stop rule "When a step doesn't need my input, keep going" `g05-0069` `g05-0071`.
- **Compaction:** `"autoCompactWindow": 200000`, or `claude --autocompact 200k` for one launch `g06-0067` `g06-0068`.
- **Plan mode:** Shift+Tab cycles manual → accept edits → plan. You can also start a prompt with `/plan` or launch with `claude --permission-mode plan` `g03-0158`–`g03-0160`.
- **Memory commands:** `/init` writes a CLAUDE.md, `/memory` edits it, and a message starting with `#` saves that line to CLAUDE.md `g20-0240`–`g20-0242`. Auto memory loads only its first 200 lines or 25KB `g06-0243`.
- **Other:** Escape twice or `/rewind` rolls back chat and code `g03-0114`. `/reload-plugins` loads new plugins without a restart `g05-0110`.
- **Skill conventions:** `$ARGUMENTS` for input, `${CLAUDE_SKILL_DIR}` for the skill's files `r04-0007` `r04-0008`, accept-edits for multi-agent skills `r01-0185`, and a new session after installing `r03-0143`.
- **Mods** are unsandboxed TypeScript plugins installed with /plugin, so install only from people you trust `g07-0176` `g10-0065`.
- **Desktop leak:** Claude Desktop reached 131-140GB on a 48GB Mac. The same work in terminal Claude Code stayed under 200MB `g10-0038` `g10-0039`.

## Contradictions and caveats

- "Never repeats a mistake" `y02-0088` vs "much less likely, not impossible" `r03-0060`. Rules are written only at night, so a same-day repeat is possible `r03-0101` (INFERRED).
- Bouncer "no surprise changes" `y02-0061` vs "a rule, not a lock" `g08-0201`.
- Prompt cut: "the tool got better" `g18-0229` vs "measured no loss" `g16-0258`.
- CLAUDE.md: "delete it, start from zero" `g18-0246` vs "not deleting everything" `g16-0265`. Under 200 lines `g03-0020` vs one screen `g18-0237`.
- Mods: "one setting most people miss" `g10-0049` vs on by default since 2.1.287 `g07-0171`.
- Leak: ~120GB on a 96GB Mac `y03-0093` vs 131-140GB on a 48GB Mac `g10-0038`.
- Projects "are the solution" `y01-0160` vs "do not work inside Projects by default" `g16-0177`.
- Reddit unreadable `g19-0249` vs the scout routine reading it via Custom network access `r04-0187`.
- **Toc-only:** many guide bodies are email-gated, with titles only. This includes the effort cheat sheet `g10-0176`, the mods setting `g10-0049` and the onFailure catch `g04-0068`. Don't invent their contents.

## What to load next

- usage-limits: /compact, caching and model routing
- skills-mcp-ecosystem: plugins and MCP installs
- agent-teams: /court, /launch, /night-crew
- prompting-quality: Fable 5 fixes
