# Claude Code Optimization Report

**For:** Lucas · **Machine:** Windows 11 Pro (Mac next) · **Claude Code:** 2.1.301 · **Plan:** Claude Max · **Date:** 2026-10-16

**Rules applied to every recommendation:** only Claude models on the Max plan, no third-party model providers, no external API keys, and $0 autonomous spend. Anything that could break those rules is fenced off and labelled **⛔ MONEY/PROVIDER GATE**.

**Legend.** Every item was checked against a second, adversarial review. Refuted claims were dropped. Where the review corrected a claim, the corrected version is the one shown. **[unverified]** marks a claim that rests on a third-party source or that could not be measured. **[already done]** marks a fix that is already live on this machine. Citations such as [n] link to the Source list in §11.

---

## 1. Executive summary: top 12 changes, ranked by impact

| # | Change | Why it matters | Effort |
|---|---|---|---|
| 1 | Set effort for each model under `modelSettings`. Your `effortLevel: "high"` is ignored on Sonnet 5.5, so every session has been running at **medium**. [[1]](https://code.claude.com/docs/en/settings-reference#effortlevel)[[2]](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) | quality | 1 min |
| 2 | Close every path that bills past the plan: `CLAUDE_CODE_DISABLE_FAST_MODE=1`, usage credits OFF, no Fable in headless runs, and auto-mode `hard_deny` rules. [[3]](https://code.claude.com/docs/en/fast-mode)[[4]](https://code.claude.com/docs/en/model-config#fable-and-usage-credits) | $0 rule | 5 min |
| 3 | Seal the claude-mem AI note-taker. The patch has been re-applied **[already done]**. Still to do: add `CLAUDE_MEM_DISABLE_OBSERVATION=1` and turn off thedotmack auto-update so the 13.39-style regression can't come back. [[5]](https://github.com/thedotmack/claude-mem)[[6]](https://code.claude.com/docs/en/discover-plugins) | limits | 3 min |
| 4 | Lower `autoCompactWindow` from 700K to **400K** and adopt `/clear`, `/compact <focus>` and rewind habits. Every request re-sends the whole history. [[7]](https://code.claude.com/docs/en/costs#why-usage-climbs-in-a-long-session)[[8]](https://code.claude.com/docs/en/best-practices#manage-context-aggressively) | limits + quality | 1 min |
| 5 | Add a Node status line that shows model·effort, context %, 5h/7d plan usage and minutes until the prompt cache goes cold. It works on both machines. [[9]](https://code.claude.com/docs/en/statusline) | limits | 5 min |
| 6 | Make `defaultMode: "auto"` with a classifier rulebook (`hard_deny` for live trades, purchases and outbound sends) plus **PowerShell** `ask`/`deny` rules. [[10]](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)[[11]](https://code.claude.com/docs/en/auto-mode-config)[[12]](https://code.claude.com/docs/en/permissions) | flow | 10 min |
| 7 | Install the official `pyright-lsp` and `typescript-lsp` plugins. Today you have no code intelligence at all. [[13]](https://code.claude.com/docs/en/plugins/code-intelligence) | quality + limits | 5 min |
| 8 | Make "done" mean a check that exits 0: add a Verification block to CLAUDE.md, use `/goal` with a measurable condition, and run the bundled `/code-review` in a fresh-context subagent. [[14]](https://code.claude.com/docs/en/best-practices#give-claude-a-way-to-verify-its-work)[[15]](https://code.claude.com/docs/en/goal)[[16]](https://code.claude.com/docs/en/code-review-local) | quality | 10 min |
| 9 | Slim the global CLAUDE.md (13 KB loads into every session and subagent), set `autoMemoryEnabled: false` (the retire date passed months ago), and run `/doctor prompt-audit`. [[17]](https://code.claude.com/docs/en/memory#audit-your-instruction-files)[[18]](https://code.claude.com/docs/en/memory#auto-memory) | limits + quality | 30 min |
| 10 | Clean up skills: switch **off** the ones that call Gemini, rename the two that shadow built-ins (`security-review`, `deep-research`), and uninstall the duplicate `code-review` plugin. [[19]](https://code.claude.com/docs/en/skills#resolve-skills-that-share-a-name)[[20]](https://code.claude.com/docs/en/skills#override-skill-visibility-from-settings) | quality + rules | 10 min |
| 11 | Add portable Node hooks: a Bash **and** PowerShell guard, a hard lock on `PAPER_ORB/RULES.md` and secrets, lint feedback after each edit, and state re-injected after compaction. [[21]](https://code.claude.com/docs/en/hooks)[[22]](https://code.claude.com/docs/en/hooks-guide) | reliability | 20 min |
| 12 | Mac transfer: make `~/.claude` a private git repo with a whitelist `.gitignore`, LF line endings, a portable `$HOME` hook, and rebuild plugins, MCP and claude-mem on the Mac itself. [[23]](https://code.claude.com/docs/en/claude-directory)[[24]](https://code.claude.com/docs/en/plugins/loading) | portability | 1 h |

Also cheap and worth doing: the **Concise** output style [[25]](https://code.claude.com/docs/en/output-styles#concise), **Explore on Haiku** [[26]](https://code.claude.com/docs/en/sub-agents), **PYTHONUTF8=1** [[27]](https://peps.python.org/pep-0686/), **PowerShell 7** [[28]](https://code.claude.com/docs/en/tools-reference), and the **stable** update channel with a version floor [[29]](https://code.claude.com/docs/en/settings-reference#autoupdateschannel)[[30]](https://code.claude.com/docs/en/settings-reference#minimumversion).

---

## 2. Usage limits & token economy

**The model of what costs you.** Claude Code re-sends the whole conversation on every request, and every tool call is its own request. Cached tokens still count against your limits. In the docs' own `/usage` example, cache reads are about 51% of cost, cache writes about 34% and output about 14% [[7]](https://code.claude.com/docs/en/costs#why-usage-climbs-in-a-long-session)[[31]](https://code.claude.com/docs/en/costs). A community audit found the same: roughly ⅔ of cost goes to re-reading context **[unverified, community]** [[32]](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything). The levers that matter most are smaller context, a warm cache, and less raw tool output. Anthropic doesn't publish how Max weights tokens, so every $ figure below is a list-price proxy [[33]](https://platform.claude.com/docs/en/about-claude/pricing)[[34]](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan).

### 2.1 Compaction window: 700K → 400K
- At 700K, a single request re-reads about $0.07 of cache. At 250K it is about $0.025. The first turn after more than 1 h idle rewrites everything: about $2.80 versus $1.00 [[35]](https://code.claude.com/docs/en/model-config)[[33]](https://platform.claude.com/docs/en/about-claude/pricing). 400K is a judgment call that trades usage against more frequent, lossy compactions. Use 250K if you want the maximum saving [[36]](https://code.claude.com/docs/en/model-config#set-the-auto-compact-window)[[37]](https://code.claude.com/docs/en/context-window#when-your-context-fills-up).
- Idle compaction was **added in 2.1.299**. It summarizes conversations over 200K about 54 min into idle time, before the 1 h cache expires. Leave it on [[38]](https://code.claude.com/docs/en/settings-reference#idlecompaction)[[2]](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)[[39]](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md).

```text
/autocompact 400k                 # saves under modelSettings for the current model
claude --autocompact 700k         # one deliberate long-context launch only
/autocompact auto                 # or: return to the model-tuned default (~967K)
```

### 2.2 Session habits [[40]](https://code.claude.com/docs/en/best-practices)[[31]](https://code.claude.com/docs/en/costs)[[41]](https://code.claude.com/docs/en/context-window)
- `/clear` costs nothing. `/compact` reads the whole conversation, so it is itself a large request. `/rename` before `/clear`, and use `/resume <name>` later.
- After **two failed corrections**, rewind or `/clear` and re-prompt with what you learned. "A clean session with a better prompt almost always outperforms" a long one.
- `/btw <question>` sees the whole conversation, has no tools, and never enters history [[42]](https://code.claude.com/docs/en/interactive-mode).
- Esc Esc → rewind → **Summarize from here** condenses a noisy stretch and reuses the cached prefix.

```text
/rename auth-refactor
/clear
/compact Focus on the API changes and the failing test names
/btw what was the name of that config file?
```

### 2.3 Keep the prompt cache warm [[43]](https://code.claude.com/docs/en/prompt-caching)[[44]](https://code.claude.com/docs/en/prompt-caching#switching-models)[[45]](https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything)[[46]](https://chen.media/guides/three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha)
- Each model has its own cache. A mid-task `/model` switch, every opusplan plan-mode toggle, and any skill whose frontmatter names a model all re-read the history uncached.
- On 5.5 models with a subscription, **changing effort keeps the cache**, so per-task effort changes are free [[47]](https://code.claude.com/docs/en/prompt-caching#changing-effort-level). Changing output style does break the cache, so set it once [[48]](https://code.claude.com/docs/en/prompt-caching#changing-output-style).
- TTL is 1 h for the main conversation and 5 min for subagents and workflows. While you draw on usage credits it drops to 5 min.
- Edits to CLAUDE.md made mid-session apply only after `/clear`, `/compact` or a restart.

```text
claude --model sonnet --effort high      # decide up front
/usage  -> "Prompt cache (main)" -> read "likely cause:" when misses climb
"Use the architect subagent to design X" # instead of /model opus mid-session
```

### 2.4 Model routing for limits [[35]](https://code.claude.com/docs/en/model-config)[[2]](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)[[34]](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)
List prices per MTok (in/out): Opus 5.5 $4/$20, Sonnet 5.5 $2/$10, Haiku 5.5 $0.10/$0.50, rising to $0.50/$2.50 for prompts over 100K. Keep `"model": "sonnet"`. Get Opus reasoning from your `architect` and `planner` subagents, which are already `model: opus`, or from the advisor (§3.4). Session and weekly limits are shared across models, so switching models does not restore access.

**Explore on Haiku.** The built-in Explore agent now inherits the main model. A user agent named `Explore` overrides it [[26]](https://code.claude.com/docs/en/sub-agents)[[45]](https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything):

```bash
cat > ~/.claude/agents/Explore.md <<'EOF'
---
name: Explore
description: Fast read-only codebase search. Use to find files, symbols, call sites and answer where/how-is-X-done questions.
tools: Read, Grep, Glob
model: haiku
effort: low
autoCompactWindow: 100000
---
You are a read-only code search specialist. Use Grep/Glob first, Read only the relevant line ranges, and return a compact answer: file paths with line numbers, the key snippet, one-line conclusions. Never edit files. Never paste whole files.
EOF
sed -i 's/^model: sonnet$/model: haiku/' ~/.claude/agents/code-explorer.md ~/.claude/agents/docs-lookup.md
```
The `autoCompactWindow: 100000` cap (v2.1.296+) keeps Haiku in its cheap price tier. **[unverified]** whether a user-defined Explore agent also skips CLAUDE.md the way the built-in one does.

### 2.5 Subagents, teams, workflows [[26]](https://code.claude.com/docs/en/sub-agents)[[31]](https://code.claude.com/docs/en/costs)[[49]](https://code.claude.com/docs/en/agent-teams)[[50]](https://code.claude.com/docs/en/workflows)[[51]](https://code.claude.com/docs/en/workflows#cost)
- Each subagent pays a fixed startup cost: system prompt, about 3.2K tokens of CLAUDE.md and about 6K of skill listing, all on a 5-minute cache. Delegate noisy work that produces a lot of output ("run pytest and return only failures"). Don't delegate one-file lookups.
- Agent teams use about **7×** the tokens in plan mode. Leave `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` unset.
- Workflows: set `workflowSizeGuideline: "small"` (under 5 agents) and **delete `skipWorkflowUsageWarning: true`** (undocumented; it hides the usage caution). Pilot each workflow on a small slice first.
- **ultracode only per task**, never as a global key. With it on, Claude "reaches a session or weekly limit sooner" and skips the Large-workflow warning [[52]](https://code.claude.com/docs/en/workflows#let-claude-decide-with-ultracode)[[53]](https://code.claude.com/docs/en/settings-reference#ultracode).

```text
/config workflowSizeGuideline=small
ultracode: <one big task>          # one-off
/effort ultracode off
# mechanical fan-out on Opus main only (changelog-only var, [unverified] beyond CHANGELOG 2.1.296):
$env:CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL='sonnet'; claude
```

### 2.6 Idle and background consumers [[31]](https://code.claude.com/docs/en/costs)[[42]](https://code.claude.com/docs/en/interactive-mode)[[54]](https://code.claude.com/docs/en/cli-reference)[[55]](https://code.claude.com/docs/en/scheduled-tasks)
- Every `/loop` fire, every inbound cross-session message, and every idle goal check-in re-sends the full context. Hourly or slower loops get 0–30 min of jitter and usually find the cache cold (inferred from the TTL and jitter tables) [[55]](https://code.claude.com/docs/en/scheduled-tasks)[[56]](https://chen.media/guides/find-the-claude-code-loops-that-are-quietly-eating-your-limit). For waiting on a process, prefer self-paced `/loop` or the **Monitor** tool.
- Check the `/usage` Loops rows weekly. Emergency stop: `CLAUDE_CODE_DISABLE_CRON=1`.
- `promptSuggestionEnabled: false` and `CLAUDE_CODE_GOAL_CHECKIN_MINUTES=0` (both in §6).
- `crossSessionInbound: "hold"` is **optional**. Leave it off if Noetra offices depend on live cross-session messages.
- Run scheduled automation as a fresh, lean headless session (§5.10). **Never use `--bare`**: it requires `ANTHROPIC_API_KEY` ⛔.

### 2.7 Shrink tool output [[13]](https://code.claude.com/docs/en/plugins/code-intelligence)[[31]](https://code.claude.com/docs/en/costs)[[57]](https://code.claude.com/docs/en/env-vars)
- LSP: a single go-to-definition call replaces a grep plus several file reads (§4).
- A PreToolUse hook rewrites test commands to quiet flags (§5.4).
- Keep the default caps: Bash 30K chars, Read 25K tokens, MCP 25K tokens. Raising them makes every later request heavier.
- Name a file and symbol in the prompt instead of `@`-mentioning folders.

### 2.8 Skill listing and CLAUDE.md overhead [[58]](https://code.claude.com/docs/en/skills)[[59]](https://code.claude.com/docs/en/skills#find-unused-skills)[[60]](https://code.claude.com/docs/en/settings-reference#skilllistingbudgetfraction)[[61]](https://code.claude.com/docs/en/plugins/measure)
Measured: 88 personal skill folders with about 24–27K chars of descriptions (about 6K tokens), claude-mem at about 2,323 always-on tokens (23 skills), superpowers at about 848 plus about 1.1K injected at SessionStart, and 32 agents at about 1.6K. The listing is capped at 1% of the context window. On overflow, the least-used skills lose their descriptions and stop triggering. Measure first:

```text
claude plugin details claude-mem@thedotmack
claude plugin details superpowers@claude-plugins-official
/skill-doctor     # per-skill cost vs times invoked (v2.1.252+ per docs; needs flag fetching)
/doctor           # listing cost + unused plugins/MCP
/context          # Skills + Memory files rows
```
Pruning keys are in §4.3 and the CLAUDE.md surgery is in §3.9.

### 2.9 claude-mem: seal the note-taker **[already done + 2 steps left]** [[5]](https://github.com/thedotmack/claude-mem)[[62]](https://code.claude.com/docs/en/settings)[[6]](https://code.claude.com/docs/en/discover-plugins)[[24]](https://code.claude.com/docs/en/plugins/loading)
claude-mem 13.39.0 auto-updated at 2026-10-16 05:42Z and switched to exec-form hooks (`command` plus `args`). That got past the string-only matcher in `noetra-patch-hooks.py`, so the observer ran Claude inferences on your allowance. **Already fixed:** `hook_text()` now joins command and args, `PostToolUseFailure` is covered, `--check` prints `NOETRA HOOKS OK`, and a SessionStart `startup` self-heal hook exists. Remaining:

```text
# 1) version-proof switch (covers observation + file-context; patcher still covers summarize/session-init)
"env": { "CLAUDE_MEM_DISABLE_OBSERVATION": "1" }          # merged in §6
# 2) stop silent plugin updates: /plugin -> Marketplaces -> thedotmack -> Disable auto-update
#    (persisted in §6 via extraKnownMarketplaces.thedotmack.autoUpdate=false)
# 3) next day, confirm the observer is quiet (PowerShell):
(Select-String -Path "$HOME\.claude-mem\logs\claude-mem-$(Get-Date -f yyyy-MM-dd).log" -Pattern 'Response received').Count   # expect ~0
python -I "$HOME\.claude-mem\noetra-patch-hooks.py" --check                                                                  # expect NOETRA HOOKS OK
```
Observer usage may not appear in `/usage` attribution **[unverified]**.

### 2.10 Monitoring [[31]](https://code.claude.com/docs/en/costs)[[9]](https://code.claude.com/docs/en/statusline)[[63]](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/session-report)[[64]](https://github.com/ryoppippi/ccusage)[[65]](https://ccusage.com/guide/blocks-reports)[[66]](https://github.com/ccusage/ccusage)
- `/usage` (press `w` for 7 days) gives attribution per skill, plugin, MCP server and subagent, flags any behavior at 10% or more of usage, and shows the Prompt cache line. Limits are shared with claude.ai and Desktop, but `/usage` counts only this machine.
- The status line (§5.1) is the live 5h/7d source.
- Deep dive: the official `session-report` plugin (a local analyzer) with `/session-report:session-report 7d`.
- History: `npx ccusage@latest daily --offline` and `npx ccusage@latest blocks --recent`. Its $ figures are API-equivalent, not your bill. Don't use its status line, because it is slow [[67]](https://ccusage.com/guide/statusline).

### 2.11 At a limit: wait, don't pay [[31]](https://code.claude.com/docs/en/costs)[[50]](https://code.claude.com/docs/en/workflows)[[43]](https://code.claude.com/docs/en/prompt-caching)
- Keep `autoContinueAtUsageLimit: true`. Claude Code then waits for the reset and continues, at most twice. Workflows pause the same way.
- ⛔ **MONEY GATE:** keep usage credits **OFF** (`/usage-credits` opens claude.ai/settings/usage), and decline every in-CLI "raise spend limit" offer. The API credits bundled with Max can't be used in Claude Code.

### 2.12 Output tokens
`"outputStyle": "Concise"` makes Claude lead with the result and drop narration and recaps, while engineering work stays "as thorough as in the Default style". Errors, test output and security warnings stay full length. The value is **case-sensitive**: `"concise"` silently gives you Default [[25]](https://code.claude.com/docs/en/output-styles#concise)[[68]](https://code.claude.com/docs/en/settings-reference#outputstyle).

### 2.13 Optional community levers (trial at project scope only) **[unverified claims]**
- **effortless** (MIT) has Haiku pick the effort level per prompt, using your own login. The README reports about 21% savings on easy tasks. ⛔ Keep its optional "Jev" judge **off**: it needs a TypeSafe key [[69]](https://github.com/HeyCubit/effortless)[[70]](https://chen.media/guides/cut-your-claude-code-costs-with-effortless).
- **rtk** compresses Bash output, so it pays off mainly on the Mac (§9) [[71]](https://github.com/rtk-ai/rtk).
- **context-mode**: rejected, see §10 [[72]](https://github.com/mksglu/context-mode)[[73]](https://agentskill.sh/plugins/mksglu/context-mode)[[74]](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode).

```text
claude plugin marketplace add HeyCubit/effortless
claude plugin install effortless@effortless --scope project     # read hooks/ first; Jev OFF
```

---

## 3. Output quality

### 3.1 Effort is broken today: fix it per model [[75]](https://code.claude.com/docs/en/costs#choose-the-right-model)[[76]](https://www.anthropic.com/engineering/april-23-postmortem)[[1]](https://code.claude.com/docs/en/settings-reference#effortlevel)[[77]](https://code.claude.com/docs/en/settings-reference#modelsettings)[[78]](https://code.claude.com/docs/en/model-config#adjust-effort-level)[[2]](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
Since 2.1.280, a top-level `effortLevel` no longer applies to Opus 5.5 "and models released after it". Sonnet 5.5 shipped in 2.1.284, so your `sonnet` sessions run at the model default, **medium**. The docs call medium fine for well-scoped features and high right for bug fixing where edge cases matter. You asked for high, so restore it per model (JSON in §6). Check with `/effort status` or look for "with high effort" in the header.

```text
/model sonnet
/effort high            # typed level = saved for this model
/effort                 # slider -> xhigh -> press s = THIS SESSION ONLY (hard debugging/architecture)
ultrathink <prompt>     # deeper reasoning for one turn; "think hard" is plain text, not a keyword
```
- **Correction:** `/effort auto` does **not** return to your saved level. It clears the saved level, so the model default (medium) applies [[35]](https://code.claude.com/docs/en/model-config)[[79]](https://www.schemastore.org/claude-code-settings.json).
- `max` is session-only, "prone to overthinking", and flagged by `/usage`. Cap it with `"maxEffortLevel": "xhigh"` [[80]](https://code.claude.com/docs/en/settings-reference#maxeffortlevel).
- Don't set `MAX_THINKING_TOKENS`, `alwaysThinkingEnabled`, `CLAUDE_CODE_EFFORT_LEVEL` or `CLAUDE_CODE_MAX_OUTPUT_TOKENS`. They do nothing on 5.5 models, override your per-task control, or shrink the context window [[81]](https://code.claude.com/docs/en/model-config#extended-thinking)[[82]](https://code.claude.com/docs/en/model-config#use-ultrathink-for-one-off-deep-reasoning)[[57]](https://code.claude.com/docs/en/env-vars).
- Agent frontmatter: `effort: low` for `docs-lookup` and `code-explorer`, `effort: high` for `code-reviewer` and `security-reviewer` [[26]](https://code.claude.com/docs/en/sub-agents).

### 3.2 Definition of done = a command that exits 0 [[14]](https://code.claude.com/docs/en/best-practices#give-claude-a-way-to-verify-its-work)[[83]](https://code.claude.com/docs/en/memory#write-effective-instructions)[[40]](https://code.claude.com/docs/en/best-practices)
"Claude stops when the work looks done. Without a check it can run, 'looks done' is the only signal available." Append this to `~/.claude/CLAUDE.md`:

```markdown
## Verification (all code work)
- Done = the project's check (tests / build / typecheck) exits 0. Paste the exact command and its output. No evidence = not done.
- Bug fix: first write a failing test that reproduces it and run it, then fix it.
- Never delete, skip or loosen a test to make it pass. Fix the root cause; don't suppress errors.
- UI change: screenshot the result, compare it to the target, then list and fix the differences.
- Third-party library/framework API or config: query Context7 (or delegate to docs-lookup) before writing code; use the version pinned in the lockfile.
```
Per repo, add a `## Commands` block with the exact test, type and lint commands (for example `uv run pytest -q`, `uv run pyright`, `uvx ruff check .`).

### 3.3 `/goal` for multi-turn work [[15]](https://code.claude.com/docs/en/goal)[[84]](https://code.claude.com/docs/en/hooks#stop-input)[[22]](https://code.claude.com/docs/en/hooks-guide)
`/goal` is a session-scoped prompt Stop hook. A small, fast evaluator model decides whether the goal is met, and its tokens are "typically negligible". It **can't run commands**, so write the condition so the proof shows up in the transcript. It works alongside unlazy: use unlazy for formal ledgers and `/goal` for ad hoc work.

```text
/goal "uv run pytest -q" exits 0 and its output is shown; "uv run pyright" reports 0 errors; no file under tests/ modified; or stop after 20 turns
/goal            # status
/goal clear
```

### 3.4 Reasoning routing: Sonnet + Opus advisor [[85]](https://code.claude.com/docs/en/advisor)[[86]](https://code.claude.com/docs/en/settings-reference#advisormodel)[[87]](https://code.claude.com/docs/en/model-config#opusplan-model-setting)[[44]](https://code.claude.com/docs/en/prompt-caching#switching-models)
- `"advisorModel": "opus"` lets Sonnet 5.5 do the turns while Claude consults Opus 5.5 during planning, on recurring failures, and before declaring work done. The docs say this "typically costs less than running the stronger model throughout". It counts toward plan limits. The feature is experimental and needs feature-flag fetching. ⛔ **Never pick Fable as the advisor**, because a Fable advisor bills to usage credits.
- `opusplan` uses Opus only in plan mode. With acceptEdits or auto as your default mode it acts like plain Sonnet, and every toggle re-reads the conversation uncached. Use it only for a fresh session that starts in plan mode: `claude --model opusplan --permission-mode plan`.

```text
/advisor            # pick Opus; "No advisor" or /advisor off to disable
claude --advisor opus
```

### 3.5 Plan first, spec for big features [[88]](https://code.claude.com/docs/en/best-practices#explore-first-then-plan-then-code)[[89]](https://code.claude.com/docs/en/best-practices#let-claude-interview-you)[[90]](https://code.claude.com/docs/en/commands)[[91]](https://www.anthropic.com/engineering/harness-design-long-running-apps)
Use plan mode (Shift+Tab, `/plan …` or `--permission-mode plan`) for any change across several files. Ctrl+G edits the plan in your editor. For large features, have Claude interview you into `SPEC.md`, then `/clear` and implement it. This pairs with `superpowers:brainstorming → writing-plans → subagent-driven-development`.

```text
I want to build [brief description]. Interview me in detail using the AskUserQuestion tool. Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs. Don't ask obvious questions, dig into the hard parts I might not have considered. Keep interviewing until we've covered everything, then write a complete spec to SPEC.md.
```

### 3.6 Independent review [[16]](https://code.claude.com/docs/en/code-review-local)[[92]](https://code.claude.com/docs/en/best-practices#add-an-adversarial-review-step)[[93]](https://code.claude.com/docs/en/ultrareview#pricing-and-free-runs)[[94]](https://code.claude.com/docs/en/ultrareview)[[91]](https://www.anthropic.com/engineering/harness-design-long-running-apps)
Agents "reliably skew positive when grading their own work". The bundled `/code-review` runs in a background subagent with fresh context and follows CLAUDE.md. Scope reviews to correctness, because reviewers asked to find gaps will invent some.

```text
/code-review high
/code-review high --fix        # edits outside checkpoints -> revert with git
/code-review max main...my-feature
/simplify                      # cleanup only
Use a subagent to review the diff against SPEC.md. Report only gaps that affect correctness or the stated requirements, not style preferences.
```
⛔ **MONEY GATE:** `/code-review ultra` gives 3 one-time free runs. After that each review costs $5–25 in usage credits. With credits OFF, paid launches are blocked.

### 3.7 Built-in verification hooks
- **`/verify` once per active repo** (LL, MQL, Odysseus, Scholarship Office). It records `.claude/skills/verify/SKILL.md`, and a project skill named `verify` then runs before each commit (v2.1.286+). Commit that file [[95]](https://code.claude.com/docs/en/skills#run-and-verify-your-app)[[90]](https://code.claude.com/docs/en/commands). **[unverified]** The exact trigger wording came from a page summary, so confirm it in one repo.
- **Red-green TDD** for LL signals and the MQL Monte Carlo and barrier math: commit the failing tests, implement without touching `tests/`, then have a subagent check for overfitting. Or run `/superpowers:test-driven-development` [[96]](https://code.claude.com/docs/en/best-practices#provide-specific-context-in-your-prompts)[[97]](https://code.claude.com/docs/en/best-practices#run-multiple-claude-sessions)[[98]](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)[[99]](https://github.com/obra/superpowers).

```text
/goal "uv run pytest -q" exits 0 and git diff HEAD~1 -- tests/ is empty
```

### 3.8 Long rebuilds (LL/MQL): Anthropic's harness pattern [[98]](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)[[91]](https://www.anthropic.com/engineering/harness-design-long-running-apps)
Keep a `features.json` where every feature has a `passes` flag starting `false`, plus `claude-progress.txt` and `init.ps1`/`init.sh`. Work one feature per session and commit after each. JSON is "less likely to [be] inappropriately change[d]" than Markdown.

```json
[{"id":"F01","desc":"Load .llstrat JSON and validate schema","steps":["uv run pytest tests/test_llstrat.py -q"],"passes":false}]
```
```text
Run pwd. Read claude-progress.txt and git log -20. Run ./init.ps1 and the smoke test; fix anything broken first. Pick the highest-priority feature in features.json with passes:false and implement only that one. Verify end to end. Set passes:true only with pasted evidence. Commit with a descriptive message and append a dated entry to claude-progress.txt. You may only change the 'passes' field in features.json. It is unacceptable to remove or edit tests.
```

### 3.9 CLAUDE.md surgery [[100]](https://code.claude.com/docs/en/memory)[[101]](https://code.claude.com/docs/en/memory#import-additional-files)[[102]](https://code.claude.com/docs/en/memory#how-claude-md-files-load)[[103]](https://code.claude.com/docs/en/costs#move-instructions-from-claude-md-to-skills)[[104]](https://code.claude.com/docs/en/best-practices#write-an-effective-claudemd)[[105]](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
The global file is 153 lines and 13,009 bytes (about 3.2K tokens) and loads into every session and every non-Explore subagent. "Bloated CLAUDE.md files cause Claude to ignore your actual instructions." `@imports` don't save anything, because imported files also load at launch.

```text
1) /doctor prompt-audit          # v2.1.283+; read-only until you approve. Don't turn off the bundled claude-api skill (it runs the audit).
2) ~/mql/CLAUDE.md  <- move the TRADING RESEARCH block; first line:  @orb_lab/orb_factory/PAPER_ORB/RULES.md
   global keeps ONE line: "Trading research: before reporting any trading number, read and obey ~/mql/orb_lab/orb_factory/PAPER_ORB/RULES.md."
3) ~/.claude/noetra/CONTEXT.md <- Active projects, Yearly goals, Roadmap; global keeps:
   "Project/goal context: read ~/.claude/noetra/CONTEXT.md when planning, prioritising or running the standup."
4) ~/noetra-selffund/CLAUDE.md <- PermitPulse detail
5) Shrink Unlazy to 3 lines + "details: ~/.claude/skills/unlazy/SKILL.md" (the Stop hook enforces it)
6) Add the Verification block (§3.2) and:
   ## Compact instructions
   When compacting, preserve: modified-file list, test/build commands and last result, open gates/TODOs, decisions and why, every user correction.
7) Human-only notes -> <!-- ... --> (block comments are stripped before injection)
8) /clear, /context -> Memory files should drop by ~2K tokens
```
The global pointer line matters: rules moved into `~/mql/CLAUDE.md` stop loading in sessions started outside `~/mql`, such as `~/noetra-offices`. Use `IMPORTANT` on one line at most.

### 3.10 Parallel and experimental work [[106]](https://code.claude.com/docs/en/worktrees)[[97]](https://code.claude.com/docs/en/best-practices#run-multiple-claude-sessions)[[50]](https://code.claude.com/docs/en/workflows)
```text
claude -w feature-montecarlo          # each parallel task in its own worktree (repo must be git)
echo ".claude/worktrees/" >> .gitignore ; printf ".env\n.env.local\n" > .worktreeinclude
isolation: worktree                   # agent frontmatter for agents that edit many files
/batch migrate src/ from JavaScript to TypeScript
```
**Best-of-N with a judge** is only for high-stakes code such as core LL logic or the MQL barrier simulation. Keep `workflowSizeGuideline: small` and check `/usage` afterwards [[50]](https://code.claude.com/docs/en/workflows)[[31]](https://code.claude.com/docs/en/costs):
```text
ultracode: implement SPEC.md three independent ways, each in its own isolated copy. Run "uv run pytest -q" in each. Then one skeptical judge agent that wrote none of them compares the diffs and test results against SPEC.md, picks the best, and explains why the others lost.
```

### 3.11 Repeat-mistake loop [[40]](https://code.claude.com/docs/en/best-practices)[[100]](https://code.claude.com/docs/en/memory)[[107]](https://code.claude.com/docs/en/debug-your-config)
After the second miss, write the lesson as one line in the project CLAUDE.md, for example `- IMPORTANT: Python file I/O must pass encoding="utf-8"`. Anything that must *never* happen belongs in a deny rule or a hook, not in prose.

---

## 4. Skills, plugins & MCP: keep / add / remove

### 4.1 Plugins
| Action | Plugin | Why |
|---|---|---|
| **Keep** | `superpowers` 7.0.0 | Your main pipeline. 7.0.0 fixed the Windows `run-hook.cmd` (per-user Git, WSL bash skipped, exit codes). Its real always-on cost is about 2K tokens. `subagent-driven-development` costs about 11.8K per call, so save it for plans with independent tasks [[108]](https://github.com/obra/superpowers/releases)[[61]](https://code.claude.com/docs/en/plugins/measure) |
| **Keep** | `claude-mem` | It backs Noetra memory. Deny its out-of-policy skills (§6) [[58]](https://code.claude.com/docs/en/skills)[[61]](https://code.claude.com/docs/en/plugins/measure) |
| **Add** | `pyright-lsp`, `typescript-lsp`; later `rust-analyzer-lsp` | Diagnostics after every edit plus symbol navigation. Today none of the binaries are on PATH [[13]](https://code.claude.com/docs/en/plugins/code-intelligence)[[109]](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/pyright-lsp)[[110]](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/typescript-lsp)[[111]](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/rust-analyzer-lsp) |
| **Add (medium)** | `security-guidance` | Free regex warnings at edit time (secrets, pickle, innerHTML) for LL/MQL broker code. **Turn off its per-turn Stop review**, which sends each diff to Opus and stacks a second Stop hook. **[unverified]** log path and cost visibility [[112]](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/security-guidance) |
| **Add** | `session-report` | Local HTML usage report [[63]](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/session-report) |
| **Remove** | `code-review@claude-plugins-official` | The bundled `/code-review` supersedes it (effort levels, `--fix`, `--comment`, background subagent) [[16]](https://code.claude.com/docs/en/code-review-local) |
| **Disable** | `frontend-design` | `impeccable` extends it, and one fewer competing UI trigger helps the right skill fire (judgment call; **[unverified]** NOTICE credit) [[113]](https://github.com/pbakaus/impeccable)[[114]](https://emelia.io/hub/impeccable-design-skill-review)[[115]](https://github.com/anthropics/claude-plugins-official) |
| **Remove marketplace** | `claude-code-plugins` (anthropics/claude-code demo) | It duplicates official plugins and is re-cloned while it stays in `extraKnownMarketplaces` [[116]](https://code.claude.com/docs/en/plugins/anthropic-marketplaces)[[24]](https://code.claude.com/docs/en/plugins/loading) |
| **Skip** | feature-dev, pr-review-toolkit, code-simplifier, ralph-loop, skill-creator, commit-commands, document-skills | Already covered by your local agents, superpowers, bundled `/simplify` and `/loop`, and the synced anthropic-skills. ralph-loop's blocking Stop hook would fight unlazy [[117]](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-loop)[[118]](https://github.com/anthropics/skills) |

```bash
npm install -g pyright typescript-language-server typescript
claude plugin install pyright-lsp@claude-plugins-official
claude plugin install typescript-lsp@claude-plugins-official
claude plugin install security-guidance@claude-plugins-official      # env vars in §6 first
claude plugin install session-report@claude-plugins-official
claude plugin uninstall code-review@claude-plugins-official
claude plugin disable frontend-design@claude-plugins-official
claude plugin marketplace remove claude-code-plugins
claude plugin marketplace list    # expect: anthropic-plugin-directory, claude-plugins-official, thedotmack
# Rust later: winget install Rustlang.Rustup; rustup component add rust-analyzer; claude plugin install rust-analyzer-lsp@claude-plugins-official
# verify LSP: ask Claude to introduce and fix a type error -> "Found N new diagnostic issues"; /plugin -> Errors must not say "Executable not found"
```

### 4.2 MCP
| Action | Server | Why |
|---|---|---|
| **Keep** | `composio-gmail` | PermitPulse drafts. Gate sends with `ask` rules (§6) |
| **Add** | `context7` (user scope, named exactly `context7`) | Your `docs-lookup` agent already allows `mcp__context7__*`, but the server isn't installed, so the agent has no doc tools. It is a docs service, not a model provider. Sign-in is free, and doc queries go to Upstash [[119]](https://github.com/upstash/context7)[[120]](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/context7)[[121]](https://context7.com/docs/clients/claude-code)[[122]](https://context7.com/docs/resources/all-clients)[[123]](https://code.claude.com/docs/en/mcp) |
| **Remove** | claude.ai **HIGGSFIELD** connector | A third-party generative-media service that shows "Needs authentication" ⛔ |
| **Gone** | `magic` (21st.dev) | **[already done]** It no longer exists in config. It needed a 21st.dev key and hosted AI ⛔ [[124]](https://github.com/21st-dev/magic-mcp)[[125]](https://mcp.directory/blog/21st-dev-magic-mcp-complete-guide-2026) |
| **Prefer CLI/built-in** | gh, Claude in Chrome, `playwright-cli`, LSP | Instead of the GitHub, Playwright, Chrome DevTools and Serena MCPs. CLIs are more context-efficient [[31]](https://code.claude.com/docs/en/costs)[[126]](https://github.com/microsoft/playwright-cli)[[127]](https://github.com/oraios/serena) |
| **Optional** | shadcn MCP per React project | Needs no key for the public registry [[128]](https://ui.shadcn.com/docs/mcp) |

```bash
claude mcp add --scope user --transport http context7 https://mcp.context7.com/mcp/oauth   # then /mcp -> context7 -> Authenticate
# fallback with a free key:  claude mcp add --scope user --header "Authorization: Bearer <free-key>" --transport http context7 https://mcp.context7.com/mcp
# Higgsfield: https://claude.ai/customize/connectors -> HIGGSFIELD.ai -> Disconnect
# unused claude.ai connectors in the CLI: /mcp toggle (per project), or "disableClaudeAiConnectors": true / ENABLE_CLAUDEAI_MCP_SERVERS=false
npm install -g @playwright/cli@latest ; playwright-cli install --skills    # per web project
npx shadcn@latest mcp init --client claude                                # per React/Tailwind project
```
Leave `ENABLE_TOOL_SEARCH` unset (it defaults to deferred schemas) [[123]](https://code.claude.com/docs/en/mcp)[[57]](https://code.claude.com/docs/en/env-vars). Use `/mcp reconnect all` after outages [[123]](https://code.claude.com/docs/en/mcp)[[107]](https://code.claude.com/docs/en/debug-your-config).

### 4.3 Personal skills
Your `skillOverrides` already has about 60 `name-only` entries. **Merge these keys into it. Don't paste a new object over it** [[20]](https://code.claude.com/docs/en/skills#override-skill-visibility-from-settings)[[129]](https://code.claude.com/docs/en/settings-reference#skilloverrides)[[130]](https://code.claude.com/docs/en/skills#skill-descriptions-are-cut-short)[[79]](https://www.schemastore.org/claude-code-settings.json)[[2]](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md).

| Skill | Set to | Reason |
|---|---|---|
| `ckm:design`, `ckm:banner-design`, `data-scraper-agent` | `off` | They call Gemini or need `GEMINI_API_KEY`. banner-design is also broken (its ai-multimodal dependency is missing) ⛔ |
| `deep-research` | rename to `deep-research-exa` (or `off`) | Needs firecrawl and exa MCPs with keys, and **likely** shadows the bundled WebSearch `/deep-research` **[partly unverified]** [[131]](https://code.claude.com/docs/en/workflows#bundled-workflows) |
| `security-review` | rename to `ecc-security-checklist` | It **replaces** the built-in branch-diff `/security-review` [[19]](https://code.claude.com/docs/en/skills#resolve-skills-that-share-a-name)[[90]](https://code.claude.com/docs/en/commands) |
| `verification-loop` | `off` | Duplicates superpowers verification, unlazy and `/verify` |
| `skill-creator`, `engram`, `agentic-engineering` | `name-only` | They duplicate synced or superpowers skills, or are rarely used |
| `taste-skill` | keep, but review it | It says "use any image tool, including OpenAI" ⛔. Never follow that branch |
| `delta`, `tradexlabs` | leave on, or move to `~/mql/.claude/skills/` | They are trading brains, so scoping them to the project keeps them out of every other session |
| claude-mem `wowerpoint`, `cloud-sync`, `screenpipe` | **deny rule** (§6) | NotebookLM (Google), paid cmem.ai Pro, and a third-party recorder. Plugin skills ignore `skillOverrides` **[unverified]** whether a deny rule matches plugin-namespaced skills |

```bash
# Git Bash (mac: sed -i '')
mv ~/.claude/skills/security-review ~/.claude/skills/ecc-security-checklist && sed -i 's/^name: security-review$/name: ecc-security-checklist/' ~/.claude/skills/ecc-security-checklist/SKILL.md
mv ~/.claude/skills/deep-research ~/.claude/skills/deep-research-exa && sed -i 's/^name: deep-research$/name: deep-research-exa/' ~/.claude/skills/deep-research-exa/SKILL.md
# new session: /security-review and /deep-research must show the built-in descriptions
```
For colon-named keys (`ckm:*`), the safest path is `/skills` → highlight → Space → Esc. Then copy the key it writes into `~/.claude/settings.json` **[unverified that colon keys match]** [[58]](https://code.claude.com/docs/en/skills).

### 4.4 Agents
- 16 of 32 agents say "MUST BE USED" or "PROACTIVELY", so overlapping reviewers can each spawn a subagent. Reword all but one review agent to "Use when the user asks for … or before committing a multi-file … change." This is a judgment call; the docs themselves encourage "use proactively" [[26]](https://code.claude.com/docs/en/sub-agents)[[7]](https://code.claude.com/docs/en/costs#why-usage-climbs-in-a-long-session).
- Of the reviewer agents, only `code-reviewer.md` ends with a literal `Verdict:` line. Add `End your report with exactly one line: Verdict: APPROVE | WARNING | BLOCK` to the other seven before you widen the SubagentStop matcher (§5.6).

---

## 5. Hooks, status line & automation

**Foundation.** `jq` is missing on this machine, and stock Windows has no POSIX tools. `bash` on PATH is WSL, but hooks run through Git Bash. Write every hook as Node `.mjs` and call it as `node "$HOME/.claude/hooks/<name>.mjs"`. That shell form works in Git Bash, macOS `sh` and PowerShell. Exec form (`args`) can't spawn `.cmd` shims such as npx or eslint, so call `node <script.js>` directly. A hook that exits 1 is **non-blocking**, which means a crashed guard fails open. Use `onFailure: "block"` (2.1.295+) on guards [[21]](https://code.claude.com/docs/en/hooks)[[132]](https://code.claude.com/docs/en/hooks#exec-form-and-shell-form)[[22]](https://code.claude.com/docs/en/hooks-guide)[[133]](https://code.claude.com/docs/en/plugins-reference)[[57]](https://code.claude.com/docs/en/env-vars).

```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\hooks" | Out-Null
```
Every script below was tested standalone on this PC with sample stdin. None has run inside a live session yet. The merged `hooks` JSON is in §6.

### 5.1 Status line [[9]](https://code.claude.com/docs/en/statusline)[[134]](https://code.claude.com/docs/en/settings-reference#statusline)[[31]](https://code.claude.com/docs/en/costs)
It shows model·effort, a context bar, 5h/7d usage with reset times, minutes of prompt cache left, and the session's cost at API list price, labelled as an estimate (you aren't billed it on Max). Rate-limit fields appear only on Pro/Max and only after the first response. A status line costs zero tokens. The trade-off is that it hides footer hints such as "esc to interrupt".

```js
// ~/.claude/statusline.mjs : zero-dependency status line, same file on Windows and macOS
let raw = '';
process.stdin.setEncoding('utf8');
process.stdin.on('data', (c) => (raw += c));
process.stdin.on('end', () => {
  let d = {};
  try { d = JSON.parse(raw.trim() || '{}'); } catch {}
  const R = '\x1b[0m';
  const dim = (s) => `\x1b[2m${s}${R}`;
  const tint = (p) => `\x1b[${p >= 85 ? 31 : p >= 60 ? 33 : 32}m`;
  const num = (v) => (typeof v === 'number' ? Math.round(v) : null);
  const clock = (s) => new Date(s * 1000).toLocaleTimeString([], { hour: 'numeric', minute: '2-digit' });
  const parts = [`${d.model?.display_name ?? '?'}${d.effort?.level ? '·' + d.effort.level : ''}`];
  const ctx = num(d.context_window?.used_percentage);
  if (ctx !== null) {
    const n = Math.min(10, Math.round(ctx / 10));
    parts.push(`${tint(ctx)}${'█'.repeat(n)}${'░'.repeat(10 - n)} ${ctx}%${R}`);
  }
  for (const [key, label] of [['five_hour', '5h'], ['seven_day', '7d']]) {
    const w = d.rate_limits?.[key];
    const p = num(w?.used_percentage);
    if (p !== null) parts.push(`${label} ${tint(p)}${p}%${R}${w.resets_at ? dim(' ↻' + clock(w.resets_at)) : ''}`);
  }
  const pc = d.prompt_cache;
  if (pc?.warm && pc.expires_at) parts.push(dim(`cache ${Math.max(0, Math.round((pc.expires_at - Date.now() / 1000) / 60))}m`));
  else if (pc?.caching_observed) parts.push('\x1b[33mcache cold\x1b[0m');
  if (typeof d.cost?.total_cost_usd === 'number') parts.push(dim(`≈$${d.cost.total_cost_usd.toFixed(2)} API-eq`));
  process.stdout.write(parts.join(dim(' │ ')) + '\n');
});
```
```powershell
'{"model":{"display_name":"Sonnet"},"context_window":{"used_percentage":63},"rate_limits":{"five_hour":{"used_percentage":24}}}' | node "$HOME/.claude/statusline.mjs"
```
Community alternatives are `claude-hud` (local only) and `ccstatusline` [[135]](https://github.com/jarrodwatts/claude-hud)[[136]](https://github.com/sirmalloc/ccstatusline).

### 5.2 Shell guard: Bash **and** PowerShell, fails closed [[21]](https://code.claude.com/docs/en/hooks)[[22]](https://code.claude.com/docs/en/hooks-guide)[[137]](https://code.claude.com/docs/en/changelog)[[138]](https://github.com/kenryu42/claude-code-safety-net)
"A hook that matches only Bash never fires" in the PowerShell tool. A PreToolUse deny holds in every permission mode, including auto and headless Phase 4 runs. Deny beats ask, and ask beats allow. Tested: `rm -rf /` and `git push -f` are denied, `Remove-Item -Recurse -Force` asks, and `--force-with-lease` passes.

```js
// ~/.claude/hooks/guard-shell.mjs : PreToolUse guard for the Bash AND PowerShell tools
const DENY = [
  [/\brm\s+-\w*(?:rf|fr)\w*\s+["']?(?:\/|~|\$HOME|\.\.?|\*|\/[a-z]|[a-z]:)[\\/]?["']?(?:\s|$)/i, 'rm -rf on a root, home, parent or wildcard target'],
  [/\bgit\s+reset\s+--hard\b/i, 'git reset --hard discards uncommitted work'],
  [/\bgit\s+clean\s+-\w*f/i, 'git clean -f deletes untracked files'],
  [/\bgit\s+push\b.*(?:--force(?!-with-lease)|\s-f\b)/i, 'force push (use --force-with-lease)'],
  [/\b(?:Format-Volume|Clear-Disk|diskpart|mkfs)\b/i, 'disk formatting'],
  [/\b(?:drop\s+(?:table|database)|truncate\s+table)\b/i, 'destructive SQL'],
];
const ASK = [
  [/\brm\s+-\w*(?:rf|fr)\w*\b/i, 'recursive force delete'],
  [/\bRemove-Item\b(?=.*-Recurse)(?=.*-Force)/i, 'Remove-Item -Recurse -Force'],
  [/\b(?:del|erase|rd|rmdir)\s+\/s\b/i, 'cmd recursive delete'],
  [/\bgit\s+(?:checkout|restore)\s+(?:--\s+)?\.(?:\s|$)/i, 'discards all working-tree changes'],
  [/\bgit\s+branch\s+-D\b/, 'force-deletes a branch'],
];
let raw = '';
process.stdin.on('data', (c) => (raw += c)).on('end', () => {
  const cmd = String(JSON.parse(raw || '{}').tool_input?.command ?? '');
  const hit = (rules) => rules.find(([re]) => re.test(cmd));
  const deny = hit(DENY);
  const ask = deny ? null : hit(ASK);
  if (!deny && !ask) process.exit(0);
  const [decision, reason] = deny ? ['deny', deny[1]] : ['ask', ask[1]];
  process.stdout.write(JSON.stringify({
    hookSpecificOutput: { hookEventName: 'PreToolUse', permissionDecision: decision, permissionDecisionReason: `guard-shell: ${reason}` },
  }));
});
```
Pattern matching is best-effort. The permission deny rules in §6 stay the hard boundary.

### 5.3 Lock the trading rules and secrets [[22]](https://code.claude.com/docs/en/hooks-guide)[[21]](https://code.claude.com/docs/en/hooks)[[12]](https://code.claude.com/docs/en/permissions)
This backs Rule-zero: an agent can never reword `PAPER_ORB/RULES.md` to get a result through. A PreToolUse exit 2 cancels the edit and tells Claude why. The §6 deny rule `Edit(~/mql/orb_lab/orb_factory/PAPER_ORB/RULES.md)` also covers Write.

```js
// ~/.claude/hooks/protect-files.mjs : PreToolUse(Edit|Write) blocks edits to rule files and secrets
const PROTECTED = [
  /\/PAPER_ORB\/RULES\.md$/i,              // permanent trading rules: human-edited only
  /(^|\/)\.env(?!\.example$)(\.[\w-]+)?$/i, // .env, .env.local (not .env.example)
  /\.(pem|key|p12|pfx)$/i,
  /\/\.claude\/\.credentials\.json$/i,
  /\/\.git\//,
  /\/\.ssh\//,
];
let raw = '';
process.stdin.on('data', (c) => (raw += c)).on('end', () => {
  const p = String(JSON.parse(raw || '{}').tool_input?.file_path ?? '').split('\\').join('/');
  const hit = PROTECTED.find((re) => re.test(p));
  if (!hit) process.exit(0);
  process.stderr.write(`Blocked: ${p} is protected (${hit}). Propose the change in chat; Lucas edits it by hand.\n`);
  process.exit(2);
});
```

### 5.4 Trim test output before it runs (corrected regex) [[31]](https://code.claude.com/docs/en/costs)[[21]](https://code.claude.com/docs/en/hooks)[[137]](https://code.claude.com/docs/en/changelog)
This adds quiet flags with `updatedInput`, without pipes, so the exit code survives and it works in PowerShell. **Correction applied:** only the *last* `pytest` token is rewritten, so `uv run --with pytest pytest tests/` no longer breaks. **[unverified]** whether `updatedInput` applies when no `permissionDecision` is given. Check once with `claude --debug-file "$HOME/cc-debug.txt"` and look for "modified tool input keys".

```js
// ~/.claude/hooks/trim-test-output.mjs : PreToolUse(Bash|PowerShell) adds quiet flags to test runners (exit code preserved, no pipes)
let raw = '';
process.stdin.on('data', (c) => (raw += c)).on('end', () => {
  const ti = JSON.parse(raw || '{}').tool_input ?? {};
  const cmd = String(ti.command ?? '');
  if (/\b(pip|install|uninstall)\b/.test(cmd)) process.exit(0);
  const pytestCount = (cmd.match(/\bpytest\b/g) || []).length;
  if (/--with\s+pytest\b/.test(cmd) && pytestCount < 2) process.exit(0);
  let next = cmd;
  if (pytestCount && !/(\s-[qv]+\b|--tb=|--quiet|--verbose)/.test(cmd)) {
    next = cmd.replace(/\bpytest\b(?![\s\S]*\bpytest\b)/, 'pytest -q --tb=short --no-header -rfE');
  } else if (/\bvitest\b/.test(cmd) && !/--reporter/.test(cmd)) {
    next = cmd.replace(/\bvitest(\s+run)?\b/, (m) => `${m} --reporter=dot`);
  }
  if (next === cmd) process.exit(0);
  process.stdout.write(JSON.stringify({ hookSpecificOutput: { hookEventName: 'PreToolUse', updatedInput: { ...ti, command: next } } }));
});
```

### 5.5 Lint feedback after each edit (read-only) [[139]](https://code.claude.com/docs/en/hooks-guide#auto-format-code-after-edits)[[21]](https://code.claude.com/docs/en/hooks)[[140]](https://code.claude.com/docs/en/best-practices#set-up-hooks)[[141]](https://claudeissues.com/issue/51361-edit-tool-fails-when-linter-formatter-modifies-file-between-read-and-edit)
A PostToolUse exit 2 keeps the edit and shows the errors to Claude in the same turn. This hook **doesn't rewrite the file**, because a formatter that changes the file right after an edit can trip Claude's stale-read check (a community report). Do formatting at commit time with `uvx pre-commit install`. Type checking is left to the LSP plugins.

```js
// ~/.claude/hooks/post-edit-lint.mjs : PostToolUse(Edit|Write) lint feedback; never rewrites the file
import { spawnSync } from 'node:child_process';
import { existsSync } from 'node:fs';
import { extname, join } from 'node:path';

let raw = '';
process.stdin.on('data', (c) => (raw += c)).on('end', () => {
  const input = JSON.parse(raw || '{}');
  const file = input.tool_input?.file_path;
  if (!file || !existsSync(file)) process.exit(0);
  const root = process.env.CLAUDE_PROJECT_DIR || input.cwd || process.cwd();
  const ext = extname(file).toLowerCase();
  let run = null;
  if (ext === '.py') {
    run = ['uvx', ['-q', 'ruff', 'check', '--output-format', 'concise', '--quiet', file]];
  } else if (['.ts', '.tsx', '.js', '.jsx', '.mjs', '.cjs'].includes(ext)) {
    const eslint = join(root, 'node_modules', 'eslint', 'bin', 'eslint.js');
    if (existsSync(eslint)) run = [process.execPath, [eslint, file]];
  }
  if (!run) process.exit(0);
  const r = spawnSync(run[0], run[1], { cwd: root, encoding: 'utf8', timeout: 60000, windowsHide: true });
  if (r.error || r.status === 0) process.exit(0); // linter missing or clean: stay silent
  const out = `${r.stdout ?? ''}${r.stderr ?? ''}`.trim().split('\n').slice(0, 40).join('\n');
  process.stderr.write(`Lint issues in ${file} (fix before moving on):\n${out}\n`);
  process.exit(2); // PostToolUse exit 2: stderr is shown to Claude, edit is kept
});
```

### 5.6 Reviewer contract (SubagentStop) [[21]](https://code.claude.com/docs/en/hooks)[[57]](https://code.claude.com/docs/en/env-vars)[[15]](https://code.claude.com/docs/en/goal)
This sends a reviewer agent back if it skips its `Verdict:` line. **Correction applied:** only `code-reviewer` has that line today, so the §6 matcher starts as `code-reviewer`. Widen it after you edit the other seven agents (§4.4).

```js
// ~/.claude/hooks/subagent-contract.mjs : SubagentStop. Reviewer agents must end with their Verdict line
let raw = '';
process.stdin.on('data', (c) => (raw += c)).on('end', () => {
  const d = JSON.parse(raw || '{}');
  if (d.stop_hook_active) process.exit(0);
  if (/Verdict:\s*(APPROVE|WARNING|BLOCK)\b/i.test(String(d.last_assistant_message ?? ''))) process.exit(0);
  process.stdout.write(JSON.stringify({ decision: 'block', reason: 'Finish with your required "Verdict: APPROVE | WARNING | BLOCK" line and file:line evidence for every finding.' }));
});
```

### 5.7 Per-repo gates (put in `<repo>/.claude/settings.json`, not global) [[21]](https://code.claude.com/docs/en/hooks)
These scripts cost no model tokens. They self-cap at 3 blocks, because Claude Code's 8-block cap resets on every tool call. Use them in LL and MQL.

```js
// ~/.claude/hooks/stop-typecheck.mjs : Stop gate. Blocks "done" while changed TS/Python fails typecheck (max 3 blocks/session)
import { spawnSync } from 'node:child_process';
import { existsSync, readFileSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
let raw = '';
process.stdin.on('data', (c) => (raw += c)).on('end', () => {
  const d = JSON.parse(raw || '{}');
  const root = process.env.CLAUDE_PROJECT_DIR || d.cwd || process.cwd();
  const sh = (cmd, args, timeout = 110000) => spawnSync(cmd, args, { cwd: root, encoding: 'utf8', timeout, windowsHide: true });
  const status = sh('git', ['status', '--porcelain'], 5000);
  if (status.status !== 0) process.exit(0); // not a git repo
  const changed = status.stdout;
  const checks = [];
  const tsc = join(root, 'node_modules', 'typescript', 'bin', 'tsc');
  if (/\.(ts|tsx)\s*$/m.test(changed) && existsSync(tsc)) checks.push(['tsc', process.execPath, [tsc, '--noEmit', '--pretty', 'false']]);
  if (/\.py\s*$/m.test(changed) && existsSync(join(root, 'pyproject.toml'))) checks.push(['basedpyright', 'uvx', ['-q', 'basedpyright', '--level', 'error']]);
  const fails = [];
  for (const [name, cmd, args] of checks) {
    const r = sh(cmd, args);
    if (!r.error && r.status !== 0) fails.push(`## ${name}\n${`${r.stdout}${r.stderr}`.trim().split('\n').slice(0, 30).join('\n')}`);
  }
  if (!fails.length) process.exit(0);
  const counter = join(tmpdir(), `cc-typecheck-${d.session_id ?? 'x'}.n`);
  const n = existsSync(counter) ? Number(readFileSync(counter, 'utf8')) || 0 : 0;
  if (n >= 3) { process.stdout.write(JSON.stringify({ systemMessage: 'stop-typecheck: still failing after 3 retries; letting the turn end.' })); process.exit(0); }
  writeFileSync(counter, String(n + 1));
  process.stdout.write(JSON.stringify({ decision: 'block', reason: `Typecheck is failing on changed code. Fix these before finishing:\n${fails.join('\n')}`.slice(0, 6000) }));
});
```
```js
// ~/.claude/hooks/bg-tests.mjs : PostToolUse asyncRewake. Runs tests in background; wakes Claude ONLY on failure
import { spawnSync } from 'node:child_process';
import { existsSync, readFileSync, statSync, writeFileSync } from 'node:fs';
import { tmpdir } from 'node:os';
import { join } from 'node:path';
let raw = '';
process.stdin.on('data', (c) => (raw += c)).on('end', () => {
  const d = JSON.parse(raw || '{}');
  const root = process.env.CLAUDE_PROJECT_DIR || d.cwd || process.cwd();
  const lock = join(tmpdir(), `cc-bgtests-${d.session_id ?? 'x'}.lock`);
  if (existsSync(lock) && Date.now() - statSync(lock).mtimeMs < 120000) process.exit(0); // debounce bursts of edits
  writeFileSync(lock, String(Date.now()));
  let run = null;
  if (existsSync(join(root, 'pyproject.toml')) && existsSync(join(root, 'tests'))) run = ['uv', ['run', '--quiet', '--with', 'pytest', 'pytest', '-q', '-x', '--tb=short', '--no-header']];
  else if (existsSync(join(root, 'package.json')) && /"test"\s*:/.test(readFileSync(join(root, 'package.json'), 'utf8'))) run = ['npm', ['test', '--silent'], true];
  if (!run) process.exit(0);
  const r = spawnSync(run[0], run[1], { cwd: root, encoding: 'utf8', timeout: 280000, windowsHide: true, shell: Boolean(run[2]) });
  if (r.error || r.status === 0) process.exit(0);
  process.stderr.write(`Background tests FAILED after your edits:\n${`${r.stdout}${r.stderr}`.trim().split('\n').slice(-60).join('\n')}\n`);
  process.exit(2); // asyncRewake: exit 2 wakes Claude with this stderr
});
```
```json
{
  "hooks": {
    "Stop": [{ "hooks": [{ "type": "command", "command": "node \"$HOME/.claude/hooks/stop-typecheck.mjs\"", "timeout": 120 }] }],
    "PostToolUse": [{ "matcher": "Edit|Write", "hooks": [{ "type": "command", "command": "node \"$HOME/.claude/hooks/bg-tests.mjs\"", "asyncRewake": true, "timeout": 300 }] }]
  }
}
```
(Project hooks add to user hooks; handlers that appear in more than one file run once.)

### 5.8 Survive compaction [[41]](https://code.claude.com/docs/en/context-window)[[21]](https://code.claude.com/docs/en/hooks)[[22]](https://code.claude.com/docs/en/hooks-guide)[[31]](https://code.claude.com/docs/en/costs)[[23]](https://code.claude.com/docs/en/claude-directory)[[142]](https://code.claude.com/docs/en/settings-reference#cleanupperioddays)
Only these survive compaction: the project-root CLAUDE.md, the plan, up to 5 recent files, and invoked skills (5K tokens each, 25K total). The skill listing, nested CLAUDE.md files and anything said only in chat are summarized away. Re-inject the **dynamic** state (git status and open gates) on `resume|compact`, and file the free compaction summary in the vault.

```js
// ~/.claude/hooks/session-context.mjs : SessionStart(resume|compact) fresh, dynamic state only
import { execFileSync } from 'node:child_process';
import { existsSync, readFileSync } from 'node:fs';
import { join } from 'node:path';
let raw = '';
process.stdin.on('data', (c) => (raw += c)).on('end', () => {
  const d = JSON.parse(raw || '{}');
  const cwd = d.cwd || process.cwd();
  const git = (...a) => { try { return execFileSync('git', a, { cwd, encoding: 'utf8', timeout: 5000, windowsHide: true, stdio: ['ignore', 'pipe', 'ignore'] }).trimEnd(); } catch { return ''; } };
  const out = [];
  const branch = git('branch', '--show-current');
  if (branch) {
    const dirty = git('status', '--porcelain').split('\n').filter(Boolean).map((l) => l.slice(3));
    out.push(`git ${branch}: ${dirty.length} uncommitted${dirty.length ? ' (' + dirty.slice(0, 8).join(', ') + ')' : ''}`);
    const log = git('log', '--oneline', '-5');
    if (log) out.push(`recent commits:\n${log}`);
  }
  const gates = join(cwd, 'GATES.md');
  if (existsSync(gates)) {
    const t = readFileSync(gates, 'utf8');
    out.push(`unlazy GATES.md: ${(t.match(/^\s*- \[x\]/gim) || []).length} checked, ${(t.match(/^\s*- \[ \]/gm) || []).length} open`);
  }
  if (out.length) process.stdout.write(`[fresh state after ${d.source}]\n${out.join('\n')}\n`);
});
```
```js
// ~/.claude/hooks/compact-capture.mjs : PreCompact = raw transcript copy; PostCompact = summary into the vault (no LLM)
import { appendFileSync, copyFileSync, existsSync, mkdirSync } from 'node:fs';
import { homedir } from 'node:os';
import { basename, join } from 'node:path';
let raw = '';
process.stdin.on('data', (c) => (raw += c)).on('end', () => {
  const d = JSON.parse(raw || '{}');
  const stamp = new Date().toISOString().replace(/[:.]/g, '-');
  if (d.hook_event_name === 'PreCompact' && d.transcript_path && existsSync(d.transcript_path)) {
    const dir = join(homedir(), '.claude', 'transcript-backups');
    mkdirSync(dir, { recursive: true });
    copyFileSync(d.transcript_path, join(dir, `${stamp}-${d.trigger}-${basename(d.transcript_path)}`));
  }
  if (d.hook_event_name === 'PostCompact' && d.compact_summary) {
    const dir = join(homedir(), 'noetra-vault', 'logs', 'compactions');
    mkdirSync(dir, { recursive: true });
    appendFileSync(join(dir, `${stamp.slice(0, 10)}.md`), `\n## ${stamp} · ${d.trigger} · ${d.cwd}\nsession: ${d.session_id}\n\n${d.compact_summary}\n`);
  }
});
```
The transcript backups stay out of the vault so graphify doesn't bloat. `cleanupPeriodDays: 365` protects the transcripts the capture bridge streams from.

### 5.9 Notifications: Windows Terminal, VS Code terminal, Mac, and failed turns [[21]](https://code.claude.com/docs/en/hooks)[[22]](https://code.claude.com/docs/en/hooks-guide)[[143]](https://code.claude.com/docs/en/terminal-config)[[144]](https://www.powershellgallery.com/packages/AutomatedLabNotifications/5.14.0/Content/Private%5CSend-ALToastNotification.ps1)
Built-in desktop notifications fire only in Ghostty, Kitty and iTerm2. `StopFailure` fires when a turn dies on a rate limit, so you learn that a long run stalled. **[unverified]** The WinRT toast parsed but was never actually displayed. The no-script alternative is `"preferredNotifChannel": "terminal_bell"`.

```js
// ~/.claude/hooks/notify.mjs : Notification + StopFailure alert; Windows Terminal, VS Code/other Windows, macOS
import { spawn } from 'node:child_process';
let raw = '';
process.stdin.on('data', (c) => (raw += c)).on('end', () => {
  const d = JSON.parse(raw || '{}');
  const body = String(d.message ?? (d.error ? `Turn failed: ${d.error}` : 'Needs your attention')).replace(/[\x00-\x1f]/g, ' ').slice(0, 180);
  const bg = (cmd, args, env) => spawn(cmd, args, { detached: true, stdio: 'ignore', windowsHide: true, env: { ...process.env, ...env } }).unref();
  if (process.platform === 'darwin') {
    bg('osascript', ['-e', `display notification ${JSON.stringify(body)} with title "Claude Code"`]);
  } else if (process.platform === 'win32' && process.env.WT_SESSION) {
    process.stdout.write(JSON.stringify({ terminalSequence: `\x1b]9;Claude Code: ${body}\x07` })); // OSC 9 toast in Windows Terminal
  } else if (process.platform === 'win32') {
    const ps = "$m=[Windows.UI.Notifications.ToastNotificationManager,Windows.UI.Notifications,ContentType=WindowsRuntime];" +
      "$x=[Windows.Data.Xml.Dom.XmlDocument,Windows.Data.Xml.Dom.XmlDocument,ContentType=WindowsRuntime]::new();" +
      "$b=[Security.SecurityElement]::Escape($env:CC_BODY);" +
      "$x.LoadXml(\"<toast><visual><binding template='ToastGeneric'><text>Claude Code</text><text>$b</text></binding></visual></toast>\");" +
      "$m::CreateToastNotifier('{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\\WindowsPowerShell\\v1.0\\powershell.exe').Show([Windows.UI.Notifications.ToastNotification]::new($x))";
    bg('powershell.exe', ['-NoProfile', '-NonInteractive', '-Command', ps], { CC_BODY: body });
  }
});
```
Phone pushes come separately, through Remote Control (§5.11).

### 5.10 Phase 4 morning standup: two $0 routes
**A. Claude Desktop local task.** It runs with local files, claude-mem and your MCP servers, needs no terminal open, and catches up once after a missed run. It needs Desktop running and the machine awake [[145]](https://code.claude.com/docs/en/desktop-scheduled-tasks)[[55]](https://code.claude.com/docs/en/scheduled-tasks).
```text
Claude Desktop > Code > Routines > New routine > Local
  Name: noetra-morning-standup   Folder: ~\noetra-offices   Model: sonnet   Permission mode: Accept edits   Daily 06:07
  Instructions: You are the Noetra Head Office. Read ~/.claude/noetra/master-todo.md first, then ~/.claude/noetra/PHASE4-AUTONOMOUS-MODE.md. Review yesterday (git log --since=yesterday in each active repo; claude-mem search for the last 24h). Plan today by priority MQL > LL > Noetra. Write the brief to ~/noetra-vault/logs/standup/<YYYY-MM-DD>.md with sections Done / Planned today / Decisions awaiting approval. If the local time is after 11:00, write a short catch-up brief only. Research and propose only: never spend money, send email, deploy, or place trades.
Settings > This computer > System > Keep computer awake: ON ; open the task > Run now > "always allow" each prompt
```
**B. Task Scheduler + `claude -p`.** It runs on your claude.ai login with no API key. `dontAsk` denies anything not pre-approved. ⛔ Never pass `--model fable` or `--model best` here: headless Fable "bills it without asking" [[146]](https://code.claude.com/docs/en/headless)[[21]](https://code.claude.com/docs/en/hooks)[[4]](https://code.claude.com/docs/en/model-config#fable-and-usage-credits)[[147]](https://learn.microsoft.com/en-us/powershell/module/scheduledtasks/register-scheduledtask). **Corrections:** add `git log` to the allowed tools; the task runs only while you're logged on unless you set `-User`/`-LogonType`; `-WakeToRun` needs "Allow wake timers" on in the power plan; the unlazy Stop hook also runs in `-p`.
```powershell
New-Item -ItemType Directory -Force "$HOME\.claude\noetra\standup","$HOME\noetra-vault\logs\standup" | Out-Null
@'
Set-Location "$HOME\noetra-offices"
$day = Get-Date -Format yyyy-MM-dd
$env:CLAUDE_CODE_RETRY_WATCHDOG = "1"
$env:CLAUDE_CODE_RETRY_WATCHDOG_MAX_USAGE_LIMIT_WAIT_MS = "7200000"
& claude -p "Noetra morning standup for $day. Follow ~/.claude/noetra/PHASE4-AUTONOMOUS-MODE.md; read ~/.claude/noetra/master-todo.md first; write the brief to ~/noetra-vault/logs/standup/$day.md (Done / Planned today / Decisions awaiting approval). Research and propose only: no spending, sending, deploying or trading." --model sonnet --effort medium --permission-mode dontAsk --allowedTools Read Grep Glob WebSearch WebFetch mcp__plugin_claude-mem_mcp-search "Bash(git log *)" "PowerShell(git log *)" "Edit(~/noetra-vault/**)" *>> "$HOME\noetra-vault\logs\standup\runner.log"
'@ | Set-Content -Encoding utf8 "$HOME\.claude\noetra\standup\run-standup.ps1"
$a = New-ScheduledTaskAction -Execute 'powershell.exe' -Argument "-NoProfile -ExecutionPolicy Bypass -File `"$HOME\.claude\noetra\standup\run-standup.ps1`""
$t = New-ScheduledTaskTrigger -Daily -At 6:07am
$s = New-ScheduledTaskSettingsSet -StartWhenAvailable -WakeToRun -ExecutionTimeLimit (New-TimeSpan -Hours 1)
Register-ScheduledTask -TaskName 'Noetra Morning Standup' -Action $a -Trigger $t -Settings $s
```
The retry watchdog variables come from the 2.1.295 and 2.1.301 changelog entries [[148]](https://code.claude.com/docs/en/errors)[[2]](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md).

**Cloud routines (`/schedule`)** are for GitHub-repo jobs that run while the PC is off. ⛔ Turn usage credits **OFF first**, or routines can keep running on metered overage. Also remove the connectors a routine doesn't need, because all of them are attached by default with write access [[149]](https://code.claude.com/docs/en/routines)[[31]](https://code.claude.com/docs/en/costs).
```text
/schedule weekdays at 7:07am in <you>/liquidity-lizard: run the test suite and review commits since yesterday for correctness; open a claude/ branch PR only for fixes whose tests pass; otherwise post a one-line summary
```

### 5.11 Remote Control, background sessions, loops [[150]](https://code.claude.com/docs/en/remote-control)[[151]](https://code.claude.com/docs/en/agent-view)[[137]](https://code.claude.com/docs/en/changelog)[[55]](https://code.claude.com/docs/en/scheduled-tasks)
```text
"remoteControlAtStartup": true            # §6; or claude --rc "LL rebuild"
/config > Push when actions required: on ; Push when Claude decides: on
https://claude.ai/settings/account > Require trusted devices: on
claude --bg --name ll-tests "run the LL test suite, fix failures, stop when green"   # own worktree; run at most 2–3 at once
claude agents | claude attach ll-tests | claude logs ll-tests | claude rm <id>       # commit before deleting in agent view
claude daemon stop --any   ->  taskkill /PID <pid> /F   (Windows stuck supervisor)
/loop 5m check whether the LL backtest in ./runs finished; report and stop when done
```

### 5.12 Verify and debug hooks [[21]](https://code.claude.com/docs/en/hooks)[[22]](https://code.claude.com/docs/en/hooks-guide)[[137]](https://code.claude.com/docs/en/changelog)[[107]](https://code.claude.com/docs/en/debug-your-config)
```text
/hooks
claude --debug-file "$HOME/cc-debug.txt"     # search for:  Hooks:   'does not start with {'   'unrecognized keys'
'{"tool_name":"Bash","tool_input":{"command":"git reset --hard"}}' | node "$HOME/.claude/hooks/guard-shell.mjs"; $LASTEXITCODE
claude --safe-mode                            # recovery; or "disableAllHooks": true (also kills the status line)
```
If your Git Bash `~/.bashrc` echoes anything, the hook JSON is read as plain text. Wrap any echo in `if [[ $- == *i* ]]; then …; fi`.

---

## 6. Settings & environment (exact JSON)

**Apply it this way.** Back the file up, then **merge** these keys into `~/.claude/settings.json`. Two warnings:
- Keep your existing `skillOverrides` object and apply the §4.3 edits to it. Don't replace it.
- Don't duplicate `SessionStart` or `env` keys. A duplicate JSON key silently drops one of them.

The `startup` patch hook below is the portable form of your current Windows-only one [[152]](https://code.claude.com/docs/en/settings#edit-a-settings-file)[[62]](https://code.claude.com/docs/en/settings)[[153]](https://code.claude.com/docs/en/settings-reference)[[79]](https://www.schemastore.org/claude-code-settings.json).

```powershell
Copy-Item "$HOME\.claude\settings.json" "$HOME\.claude\settings.backup-2026-10-16.json"
```

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "model": "sonnet",
  "advisorModel": "opus",
  "outputStyle": "Concise",
  "effortLevel": "high",
  "modelSettings": {
    "claude-sonnet-5-5": { "effortLevel": "high" },
    "claude-opus-5-5": { "effortLevel": "high" },
    "claude-fable-5-1": { "effortLevel": "high" }
  },
  "maxEffortLevel": "xhigh",
  "fallbackModel": ["opus", "haiku"],
  "autoCompactWindow": 400000,
  "autoMemoryEnabled": false,
  "cleanupPeriodDays": 365,
  "autoUpdatesChannel": "stable",
  "minimumVersion": "2.1.301",
  "autoContinueAtUsageLimit": true,
  "promptSuggestionEnabled": false,
  "workflowSizeGuideline": "small",
  "remoteControlAtStartup": true,
  "agentPushNotifEnabled": true,
  "skipAutoPermissionPrompt": true,
  "tui": "fullscreen",
  "theme": "dark",

  "permissions": {
    "defaultMode": "auto",
    "allow": [
      "PowerShell(graphify:*)",
      "PowerShell(& \"~\\AppData\\Roaming\\uv\\tools\\graphifyy\\Scripts\\python.exe\":*)"
    ],
    "deny": [
      "Read(./.env)",
      "Read(./.env.*)",
      "Bash(git push --force *)",
      "PowerShell(git push --force *)",
      "Edit(~/mql/orb_lab/orb_factory/PAPER_ORB/RULES.md)",
      "Skill(claude-mem:wowerpoint)",
      "Skill(claude-mem:cloud-sync)",
      "Skill(claude-mem:screenpipe)"
    ],
    "ask": [
      "Bash(git push *)",
      "PowerShell(git push *)",
      "mcp__composio-gmail__GMAIL_SEND_EMAIL",
      "mcp__composio-gmail__GMAIL_REPLY_TO_THREAD"
    ]
  },
  "autoMode": {
    "hard_deny": [
      "$defaults",
      "Never place, modify or cancel live (non-paper) orders on TopstepX/ProjectX or any broker API",
      "Never make purchases, payments or subscriptions, and never turn on usage credits or extra usage"
    ],
    "soft_deny": [
      "$defaults",
      "Never send email or messages to people outside this machine; drafts are fine"
    ]
  },

  "env": {
    "CLAUDE_CODE_DISABLE_FAST_MODE": "1",
    "CLAUDE_MEM_DISABLE_OBSERVATION": "1",
    "BASH_DEFAULT_TIMEOUT_MS": "300000",
    "BASH_MAX_TIMEOUT_MS": "1800000",
    "CLAUDE_BASH_MAINTAIN_PROJECT_WORKING_DIR": "1",
    "CLAUDE_CODE_GOAL_CHECKIN_MINUTES": "0",
    "CLAUDE_CODE_USE_POWERSHELL_TOOL": "1",
    "PYTHONUTF8": "1",
    "ENABLE_STOP_REVIEW": "0",
    "SG_AGENTIC_MODEL": "claude-sonnet-5-5"
  },

  "statusLine": { "type": "command", "command": "node \"$HOME/.claude/statusline.mjs\"", "padding": 0, "refreshInterval": 30 },

  "hooks": {
    "SessionStart": [
      { "matcher": "startup", "hooks": [{ "type": "command", "command": "PY=python; [ \"$(uname)\" = Darwin ] && PY=python3; $PY -I \"$HOME/.claude-mem/noetra-patch-hooks.py\" --quiet", "timeout": 30 }] },
      { "matcher": "resume|compact", "hooks": [{ "type": "command", "command": "node \"$HOME/.claude/hooks/session-context.mjs\"", "timeout": 15 }] },
      { "matcher": "compact", "hooks": [{ "type": "command", "command": "node \"$HOME/.claude/skills/unlazy/scripts/gate-check.mjs\" --status || true", "timeout": 20 }] }
    ],
    "PreToolUse": [
      { "matcher": "Bash|PowerShell", "hooks": [
        { "type": "command", "command": "node \"$HOME/.claude/hooks/guard-shell.mjs\"", "timeout": 10, "onFailure": "block" },
        { "type": "command", "command": "node \"$HOME/.claude/hooks/trim-test-output.mjs\"", "timeout": 10 }
      ] },
      { "matcher": "Edit|Write", "hooks": [{ "type": "command", "command": "node \"$HOME/.claude/hooks/protect-files.mjs\"", "timeout": 10, "onFailure": "block" }] }
    ],
    "PostToolUse": [
      { "matcher": "Edit|Write", "hooks": [{ "type": "command", "command": "node \"$HOME/.claude/hooks/post-edit-lint.mjs\"", "timeout": 60 }] }
    ],
    "Stop": [
      { "hooks": [{ "type": "command", "command": "node \"$HOME/.claude/skills/unlazy/scripts/stop-hook.mjs\" --unlazy", "timeout": 20 }] }
    ],
    "SubagentStop": [
      { "matcher": "code-reviewer", "hooks": [{ "type": "command", "command": "node \"$HOME/.claude/hooks/subagent-contract.mjs\"", "timeout": 10 }] }
    ],
    "PreCompact": [{ "hooks": [{ "type": "command", "command": "node \"$HOME/.claude/hooks/compact-capture.mjs\"", "timeout": 30 }] }],
    "PostCompact": [{ "hooks": [{ "type": "command", "command": "node \"$HOME/.claude/hooks/compact-capture.mjs\"", "timeout": 30 }] }],
    "Notification": [{ "matcher": "permission_prompt|idle_prompt|agent_needs_input|agent_completed|quota_auto_resume_fired", "hooks": [{ "type": "command", "command": "node \"$HOME/.claude/hooks/notify.mjs\"", "timeout": 10 }] }],
    "StopFailure": [{ "matcher": "rate_limit|authentication_failed|server_error", "hooks": [{ "type": "command", "command": "node \"$HOME/.claude/hooks/notify.mjs\"", "timeout": 10 }] }]
  },

  "enabledPlugins": {
    "claude-mem@thedotmack": true,
    "superpowers@claude-plugins-official": true,
    "frontend-design@claude-plugins-official": false,
    "pyright-lsp@claude-plugins-official": true,
    "typescript-lsp@claude-plugins-official": true,
    "security-guidance@claude-plugins-official": true,
    "session-report@claude-plugins-official": true
  },
  "extraKnownMarketplaces": {
    "thedotmack": { "source": { "source": "github", "repo": "thedotmack/claude-mem" }, "autoUpdate": false }
  },

  "skillOverrides": { "...": "KEEP your existing ~60 entries; apply §4.3 edits here" }
}
```

**What each change does and where it comes from.**
- **Effort per model:** see §3.1.
- **Advisor:** experimental, so drop the key if it misbehaves [[85]](https://code.claude.com/docs/en/advisor).
- **`fallbackModel`:** switches models for one turn on a 529 "overloaded" error only. A 529 is not your usage limit [[148]](https://code.claude.com/docs/en/errors)[[35]](https://code.claude.com/docs/en/model-config).
- **Stable channel with `minimumVersion`:** stable "skips releases with major regressions", and the floor stops a downgrade [[29]](https://code.claude.com/docs/en/settings-reference#autoupdateschannel)[[30]](https://code.claude.com/docs/en/settings-reference#minimumversion)[[154]](https://code.claude.com/docs/en/setup)[[2]](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md).
- **Auto mode:** works only from user settings. Keep `"$defaults"` in every array. Check it with `claude auto-mode config`, `claude auto-mode critique` and `/auto-mode-setup`, or trial it with `claude --permission-mode auto`. On Max, review runs server-side with no separate classifier calls (not measured). Native Windows has no sandbox, so the deny rules are your floor. Broad interpreter allow rules, including your graphify python one, are paused while auto mode is on [[10]](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)[[11]](https://code.claude.com/docs/en/auto-mode-config)[[155]](https://code.claude.com/docs/en/settings-reference#permissions-defaultmode)[[156]](https://code.claude.com/docs/en/settings-reference#automode)[[12]](https://code.claude.com/docs/en/permissions)[[157]](https://code.claude.com/docs/en/permission-modes).
- **Env values must be strings.** The 1800000 ms ceiling stays under the 2 h background threshold [[57]](https://code.claude.com/docs/en/env-vars)[[158]](https://code.claude.com/docs/en/settings-reference#env).
- **`SG_AGENTIC_MODEL`** takes a canonical model ID; the `sonnet` alias isn't documented. Drop both SG keys if you skip security-guidance [[112]](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/security-guidance).
- **Optional:**
  - `"availableModels": ["opus","sonnet","haiku"]` blocks Fable outright [[159]](https://code.claude.com/docs/en/settings-reference#availablemodels).
  - `"crossSessionInbound": "hold"` (see §2.6).
  - `"disableClaudeAiConnectors": true` (see §4.2).
- **Delete:** `skipWorkflowUsageWarning` (undocumented; **[unverified]** exactly what it suppresses) and the `claude-code-plugins` marketplace.
- **Never set:** `DISABLE_TELEMETRY`, `DO_NOT_TRACK`, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`, `DISABLE_GROWTHBOOK`. They turn off feature-flag fetching, which kills Remote Control (fully, for the last two), idle compaction, the advisor, `/skill-doctor`, claude.ai skill and plugin sync, the default PowerShell tool and `/auto-mode-setup`. Use the narrow switches instead: `DISABLE_AUTOUPDATER`, `CLAUDE_CODE_DISABLE_FEEDBACK_SURVEY`, `DISABLE_ERROR_REPORTING` [[160]](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching)[[57]](https://code.claude.com/docs/en/env-vars).

**Check it worked:**
```text
claude doctor                      # Auto-update channel line; no settings errors
/effort status                     # high on Sonnet 5.5
/hooks                             # every event listed; no 'observation'/'summarize' claude-mem entries
/context                           # Memory files no longer list MEMORY.md
/usage                             # no usage-credits row
```

**Retire native memory first** [[18]](https://code.claude.com/docs/en/memory#auto-memory)[[161]](https://code.claude.com/docs/en/settings-reference#automemoryenabled):
```bash
cp -r ~/.claude/projects/C--Users-Lucas-Jackson/memory ~/noetra-vault/archive-native-memory-2026-10
```

---

## 7. Known problems & fixes

| Problem | Root cause | Fix |
|---|---|---|
| Sessions feel shallower than "high" | Sonnet 5.5 ignores the top-level `effortLevel` and runs at medium | `modelSettings` (§6) [[1]](https://code.claude.com/docs/en/settings-reference#effortlevel)[[78]](https://code.claude.com/docs/en/model-config#adjust-effort-level) |
| Allowance drains with no visible cause | claude-mem 13.39 hooks got past the patch; long 700K contexts; idle loops | §2.9, §2.1, §2.6 [[5]](https://github.com/thedotmack/claude-mem)[[31]](https://code.claude.com/docs/en/costs) |
| "Want me to continue?" check-ins | acceptEdits does nothing to discourage stopping; nothing defines done | Auto mode, which "nudges Claude to keep working", plus `/goal`. If check-ins persist, switch `outputStyle` to `"Proactive"` (it replaces Concise; only one style applies) [[162]](https://code.claude.com/docs/en/output-styles)[[15]](https://code.claude.com/docs/en/goal)[[157]](https://code.claude.com/docs/en/permission-modes)[[2]](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) |
| Claims done without proof | "Looks done" is the only signal; the goal evaluator can't run tools | §3.2 prompt suffix plus `/goal … exits 0 and output shown`, `/code-review`, and the unlazy Stop hook [[40]](https://code.claude.com/docs/en/best-practices)[[15]](https://code.claude.com/docs/en/goal)[[21]](https://code.claude.com/docs/en/hooks) |
| Forgets constraints after compaction | Only the root CLAUDE.md, plan, 5 files and skills survive | `# Compact instructions`, plus SessionStart `compact` gate and git re-injection (§5.8) [[41]](https://code.claude.com/docs/en/context-window)[[100]](https://code.claude.com/docs/en/memory)[[21]](https://code.claude.com/docs/en/hooks) |
| Repeats the same mistake | Failed attempts anchor the next try | Rewind or `/clear` after two corrections; one-line lesson in CLAUDE.md; hard rules as hooks or deny rules [[40]](https://code.claude.com/docs/en/best-practices)[[100]](https://code.claude.com/docs/en/memory)[[107]](https://code.claude.com/docs/en/debug-your-config)[[28]](https://code.claude.com/docs/en/tools-reference) |
| Two memory systems giving conflicting orders | Auto memory on by default, MEMORY.md "FROZEN" | `autoMemoryEnabled: false` [[100]](https://code.claude.com/docs/en/memory) |
| Wrong or no skill triggers | Listing overflows its 1% budget; least-used skills lose their descriptions | §4.3 prune. Only if you keep everything: `"skillListingBudgetFraction": 0.02` [[58]](https://code.claude.com/docs/en/skills)[[41]](https://code.claude.com/docs/en/context-window) |
| Permission-prompt fatigue | acceptEdits approves only edits; native Windows has no sandbox | Auto mode (§6). After 3 blocks in a row or 20 total it pauses. Retry with `/permissions` → Recently denied → `r` [[157]](https://code.claude.com/docs/en/permission-modes)[[40]](https://code.claude.com/docs/en/best-practices) |
| `docs-lookup` agent does nothing | It allows `mcp__context7__*`, but no server exists | Add Context7 (§4.2) [[119]](https://github.com/upstash/context7) |
| `/security-review` is a static checklist | ECC skill shadows the built-in | Rename it (§4.3) [[19]](https://code.claude.com/docs/en/skills#resolve-skills-that-share-a-name) |
| Dead MCP noise at startup | Higgsfield is unauthenticated; magic **[already removed]** | Disconnect at claude.ai/customize/connectors. Use `/mcp reconnect all` and `claude --debug=mcp` [[123]](https://code.claude.com/docs/en/mcp)[[107]](https://code.claude.com/docs/en/debug-your-config) |
| Sluggish UI, high memory | The heap holds the transcript; in **fullscreen** `/compact` doesn't free memory | `/rename`, exit, `claude --continue`; `/heapdump` (share only `*-diagnostics.json`); `claude --safe-mode` to isolate. Leak fixes landed in 2.1.290, .293 and .299 [[163]](https://code.claude.com/docs/en/troubleshooting)[[107]](https://code.claude.com/docs/en/debug-your-config)[[2]](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) |
| Slow startup | Every MCP connect plus SessionStart hooks plus skill and agent loading | Compare against `claude --safe-mode`; `claude --debug --debug-file "$env:TEMP\cc-startup.log"`; then `Select-String -Path "$env:TEMP\cc-startup.log" -Pattern 'MCP|hook|ms'` (per-hook durations since 2.1.296) [[163]](https://code.claude.com/docs/en/troubleshooting)[[107]](https://code.claude.com/docs/en/debug-your-config)[[2]](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md) |
| 529 overloaded errors | API at capacity for one model, separate from your quota | `fallbackModel`; check https://status.claude.com [[148]](https://code.claude.com/docs/en/errors)[[35]](https://code.claude.com/docs/en/model-config) |
| Hit usage limit mid-task | Shared 5h/7d windows across all surfaces | Wait-and-continue; `/rate-limit-options`; credits stay OFF [[31]](https://code.claude.com/docs/en/costs)[[34]](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan) |
| Release regressions | `latest` channel installs every build | `stable` plus `minimumVersion` [[154]](https://code.claude.com/docs/en/setup) |
| Mac Desktop freezes | DST scheduled-task loop (official fix in 1.1.5749); multi-day blank window and 100% CPU (community reports, no official fix) | Update; Cmd+Q daily; move `scheduled-tasks.json` aside; run long jobs in the CLI (§9) [[164]](https://status.claude.com/incidents/pqpgkf52p3tg)[[165]](https://github.com/anthropics/claude-code/issues/68316)[[166]](https://github.com/anthropics/claude-code/issues/32167)[[167]](https://github.com/anthropics/claude-code/issues/39303)[[168]](https://code.claude.com/docs/en/desktop) |

Exec-form Stop hook, optional: your current Stop hook already quotes both paths, so the 2.1.290 space-in-path loop never affected it. Exec form only saves one Git Bash spawn per Stop and isn't portable, so this report prefers the `$HOME` shell form [[21]](https://code.claude.com/docs/en/hooks)[[107]](https://code.claude.com/docs/en/debug-your-config)[[2]](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md).

---

## 8. Windows specifics

1. **Python UTF-8.** Measured here: `utf8_mode=0` with a cp1252 default. `open()` without `encoding=` mangles ✓ and emoji, and child processes Claude Code spawns can crash (#69171). Python 3.15 makes UTF-8 the default [[169]](https://docs.python.org/3/library/os.html#utf8-mode)[[27]](https://peps.python.org/pep-0686/)[[28]](https://code.claude.com/docs/en/tools-reference)[[170]](https://claudeissues.com/issue/69171-bug-windows-statusline-command-is-spawned-with-cp1252-stdout-scripts-printing-no)[[171]](https://github.com/anthropics/claude-code/issues/69171)[[2]](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md).
   ```powershell
   setx PYTHONUTF8 1
   python -c "import sys,locale;print(sys.flags.utf8_mode, locale.getpreferredencoding(False))"   # new terminal -> 1 utf-8
   ```
2. **PowerShell 7.** Only 5.1 is installed. 5.1 has no `&&`/`||`, no `?:`/`??`, and wraps 2>&1 output as NativeCommandError, so model-written commands fail and get retried. Claude Code picks up `pwsh.exe` automatically [[28]](https://code.claude.com/docs/en/tools-reference)[[154]](https://code.claude.com/docs/en/setup)[[172]](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows).
   ```powershell
   winget install --id Microsoft.PowerShell --source winget
   pwsh -v      # then restart claude; only after this: "defaultShell": "powershell" (optional)
   ```
3. **A Bash deny rule silently turns off the PowerShell tool** unless a PowerShell rule exists or `CLAUDE_CODE_USE_POWERSHELL_TOOL=1` is set. §6 does both [[28]](https://code.claude.com/docs/en/tools-reference).
4. **The `bash` on PATH is WSL**, while hooks and the status line run through Git Bash. For Task Scheduler contexts, optionally pin it [[57]](https://code.claude.com/docs/en/env-vars)[[21]](https://code.claude.com/docs/en/hooks):
   ```powershell
   [Environment]::SetEnvironmentVariable('CLAUDE_CODE_GIT_BASH_PATH','C:\Program Files\Git\bin\bash.exe','User')
   ```
5. **No jq and no POSIX tools.** That's why every hook is Node. Never use jq-based examples from the docs as-is [[22]](https://code.claude.com/docs/en/hooks-guide).
6. **The space in `~`.** Quote every path. Shell form with `"$HOME/…"` is converted correctly for node.exe (tested) [[132]](https://code.claude.com/docs/en/hooks#exec-form-and-shell-form).
7. **CRLF.** The system gitconfig sets `core.autocrlf=true`. CRLF has broken Workflow scripts (fixed in 2.1.296) and multi-line `!` blocks (2.1.290). Add `.gitattributes` to every repo you'll move [[173]](https://docs.github.com/en/get-started/git-basics/configuring-git-to-handle-line-endings)[[2]](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md):
   ```gitattributes
   * text=auto eol=lf
   *.ps1 text eol=crlf
   *.bat text eol=crlf
   *.cmd text eol=crlf
   *.png binary
   *.jpg binary
   ```
   ```bash
   git add --renormalize . && git commit -m "Normalize line endings"
   ```
8. **No sandbox on native Windows.** Deny rules and hooks are the floor; WSL2 is the only sandboxed option [[174]](https://code.claude.com/docs/en/sandboxing).
9. **Notifications.** Windows Terminal needs OSC 9 and the VS Code terminal needs a WinRT toast; see `notify.mjs` (§5.9) [[143]](https://code.claude.com/docs/en/terminal-config).
10. **Worktrees.** On Windows, "don't ask again" approvals stay with the worktree they were granted in [[106]](https://code.claude.com/docs/en/worktrees).

---

## 9. Mac transfer

**Principle.** Sync only the files you wrote yourself. Rebuild machine state (login, MCP, plugin caches, transcripts, the claude-mem DB) on the Mac [[23]](https://code.claude.com/docs/en/claude-directory)[[62]](https://code.claude.com/docs/en/settings)[[24]](https://code.claude.com/docs/en/plugins/loading)[[175]](https://code.claude.com/docs/en/authentication)[[2]](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)[[176]](https://www.steeman.be/posts/syncing-claude-code-across-multiple-machines/).

**Never sync:**
- `~/.claude.json` (login, MCP, path-keyed trust)
- `~/.claude/.credentials.json`
- `~/.claude/config.json` (it holds a legacy `primaryApiKey`)
- `~/.claude/.claude.json` (oauthAccount)
- `settings.local.json`
- `plugins/` (1.9 GB, with Windows `installPath` values)
- `projects/` (1.2 GB, path-keyed)
- `skills/synced/` and `plugins/synced/` (these re-download from claude.ai, v2.1.273+)
- `~/.unlazy/approved` (PATH-bound, so re-approve)
- the live `~/.claude-mem` files

### 9.1 Windows side: build the repo [[24]](https://code.claude.com/docs/en/plugins/loading)[[2]](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)[[177]](https://www.chezmoi.io/user-guide/manage-machine-to-machine-differences/)[[178]](https://github.com/funkadelic/claude-nomad)[[58]](https://code.claude.com/docs/en/skills)[[179]](https://code.claude.com/docs/en/skills#where-synced-skills-load)[[180]](https://code.claude.com/docs/en/plugins/loading#synced-plugins)
```gitignore
# ~/.claude/.gitignore  (whitelist)
/*
!/.gitignore
!/.gitattributes
!/CLAUDE.md
!/settings.json
!/keybindings.json
!/statusline.mjs
!/hooks/
!/skills/
!/agents/
!/commands/
!/rules/
!/output-styles/
!/themes/
!/workflows/
!/agent-memory/
!/noetra/
/skills/synced/
/skills/.trash/
/skills/graphify/
**/node_modules/
**/__pycache__/
**/.venv/
*.bak
```
```bash
# Git Bash, in ~/.claude (.gitattributes = the §8 block plus *.ico binary)
rm skills/find-skills && cp -rL ~/.agents/skills/find-skills skills/find-skills      # symlink -> real folder
du -sh ~/.claude/noetra/* | sort -h | tail                                          # noetra/ is 288 MB: no file > 100 MB
mkdir -p ~/.claude/noetra/memory-fix/scripts
cp ~/.claude-mem/noetra-patch-hooks.py ~/.claude-mem/noetra-recall-hook.py ~/.claude-mem/capture-bridge.py ~/.claude/noetra/memory-fix/scripts/
claude plugin list --json > ~/.claude/noetra/plugins-snapshot.json
cd ~/.claude && git init -b main && git config core.autocrlf false
git add --renormalize . && git add -A
git ls-files -z '*.sh' | xargs -0 git update-index --chmod=+x
git status --short                                   # no .credentials.json / config.json / .claude.json
git grep -nE 'sk-ant-|primaryApiKey|x-api-key|Bearer ' -- . ; echo '^ must print nothing above'
git commit -m 'Portable Claude Code config'
gh repo create claude-config --private --source . --remote origin --push
```
The `RECALL` line in `noetra-patch-hooks.py` already picks `python3` on non-Windows **[already done]**. The §6 settings are already portable: `$HOME` hooks, the uname-switched Python, and Windows-only `PowerShell(...)` allow rules that are inert on macOS [[21]](https://code.claude.com/docs/en/hooks)[[181]](https://git-scm.com/docs/gitattributes).

### 9.2 Mac side, in order
**1. Toolchain and native install.** The native build auto-updates and follows `autoUpdatesChannel`. Homebrew casks don't auto-update and pick their channel by cask name. Requires macOS 13+ [[154]](https://code.claude.com/docs/en/setup)[[182]](https://formulae.brew.sh/cask/claude-code@latest).
```bash
xcode-select --install
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zprofile && eval "$(/opt/homebrew/bin/brew shellenv)"
brew install git gh node python uv jq ripgrep
curl -fsSL https://claude.ai/install.sh | bash
echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.zshrc && exec zsh
git config --global core.autocrlf input
```
**2. Clone before the first `claude` run.** If `~/.claude` already exists, move any colliding files aside first; otherwise the checkout aborts.
```bash
gh auth login
gh repo clone <you>/claude-config ~/.claude
# if ~/.claude already exists:
cd ~/.claude && mkdir -p ~/.claude-preclone && for f in CLAUDE.md settings.json keybindings.json; do [ -e "$f" ] && mv "$f" ~/.claude-preclone/; done
git init -b main && git remote add origin https://github.com/<you>/claude-config.git && git fetch origin && git checkout -B main origin/main
find ~/.claude/skills -name '*.sh' -exec chmod +x {} +
```
**3. Login.** It goes into the Keychain. Make sure no env var outranks your subscription: an approved API key moves you onto API billing ⛔, and `CLAUDE_CODE_OAUTH_TOKEN` disables connectors, Remote Control and sync [[175]](https://code.claude.com/docs/en/authentication).
```bash
claude auth login --claudeai
claude auth status --text
env | grep -E 'ANTHROPIC_(API_KEY|AUTH_TOKEN)|CLAUDE_CODE_OAUTH_TOKEN' || echo clean
```
**4. claude-mem plus the patch, before any session.** A fresh install ships with the AI note-taker hooks switched on [[183]](https://code.claude.com/docs/en/plugins/install)[[184]](https://code.claude.com/docs/en/plugin-marketplaces)[[5]](https://github.com/thedotmack/claude-mem).
```bash
claude plugin marketplace add anthropics/claude-plugins-official
claude plugin install claude-mem --marketplace thedotmack/claude-mem
mkdir -p ~/.claude-mem/logs ~/.claude-mem/state
cp ~/.claude/noetra/memory-fix/scripts/*.py ~/.claude-mem/
python3 ~/.claude-mem/noetra-patch-hooks.py && python3 ~/.claude-mem/noetra-patch-hooks.py --check    # NOETRA HOOKS OK
```
**5. Plugins, LSP, MCP.** MCP servers live in `~/.claude.json`, so re-add them by hand and keep their URLs and headers out of git [[183]](https://code.claude.com/docs/en/plugins/install)[[6]](https://code.claude.com/docs/en/discover-plugins)[[123]](https://code.claude.com/docs/en/mcp)[[185]](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)[[122]](https://context7.com/docs/resources/all-clients).
```bash
for p in superpowers pyright-lsp typescript-lsp security-guidance session-report; do claude plugin install "$p@claude-plugins-official"; done
npm install -g pyright typescript-language-server typescript && brew install rust-analyzer
claude mcp add --transport http --scope user composio-gmail "<your composio URL>" --header "<Header-Name>: <value>"
claude mcp add --scope user --transport http context7 https://mcp.context7.com/mcp/oauth
claude mcp list && claude doctor
```
**6. Memory data.** Use a consistent SQLite snapshot, not live sync. Don't copy `chroma/`; let it rebuild. `export-memories.ts` is **search-based**, so use it only for targeted top-ups. ⛔ Skip cmem.ai Pro sync, which is paid [[186]](https://docs.claude-mem.ai/usage/export-import)[[5]](https://github.com/thedotmack/claude-mem).
```bash
# Windows (worker stopped on both machines):
python -c "import sqlite3,os;s=sqlite3.connect(os.path.expanduser('~/.claude-mem/claude-mem.db'));d=sqlite3.connect(os.path.expanduser('~/claude-mem-seed.db'));s.backup(d);d.close()"
# move privately (AirDrop/USB), then on the Mac:
mv ~/claude-mem-seed.db ~/.claude-mem/claude-mem.db
# top-ups (worker running on the Mac): npx tsx scripts/export-memories.ts "<query>" out.json --project=noetra  ->  npx tsx scripts/import-memories.ts out.json
```
**7. Replace the Windows-only pieces.** The graphify skill is `graphify-windows`, so install it natively on each OS. The `.ps1` logon autostarts become LaunchAgents with absolute paths, and unlazy oracles need re-approval [[187]](https://github.com/safishamsi/graphify)[[188]](https://graphify.com/docs/install)[[189]](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html).
```bash
uv tool install graphifyy && graphify install
cat > ~/Library/LaunchAgents/ai.noetra.capture-bridge.plist <<'EOF'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0"><dict>
  <key>Label</key><string>ai.noetra.capture-bridge</string>
  <key>ProgramArguments</key><array>
    <string>/opt/homebrew/bin/python3</string>
    <string>/Users/YOUR_USER/.claude-mem/capture-bridge.py</string>
  </array>
  <key>RunAtLoad</key><true/>
  <key>KeepAlive</key><true/>
  <key>StandardErrorPath</key><string>/Users/YOUR_USER/.claude-mem/logs/capture-bridge.err.log</string>
</dict></plist>
EOF
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/ai.noetra.capture-bridge.plist
```
Port `noetra-start-cmem.ps1` and `refresh-vault-graph.ps1` the same way. **[unverified]** Whether `capture-bridge.py` and `noetra-recall-hook.py` are POSIX-clean, and which runtimes claude-mem needs on first run.

**8. Sandbox, Mac only.** Bash runs prompt-free inside the macOS Seatbelt boundary. Deny rules and content-scoped `ask` rules still prompt. `denyRead` doesn't cover the Read tool, so pair it with a `Read(...)` deny [[174]](https://code.claude.com/docs/en/sandboxing)[[190]](https://code.claude.com/docs/en/settings-reference#sandbox)[[2]](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md).
```json
"sandbox": { "enabled": true, "autoAllowBashIfSandboxed": true, "filesystem": { "denyRead": ["~/.aws/credentials"] } }
```
Keep `failIfUnavailable` unset, so that if this key syncs to Windows it is harmless there. Run `/sandbox` once on Windows to confirm it reports unsupported.

**9. Terminal and keys.** Ghostty notifies by default, handles Shift+Enter, and opens links on click. A MacBook can't send Ctrl+End in fullscreen, so bind jump-to-bottom yourself and keep the binding in the repo [[143]](https://code.claude.com/docs/en/terminal-config)[[191]](https://code.claude.com/docs/en/fullscreen)[[192]](https://formulae.brew.sh/cask/ghostty)[[193]](https://code.claude.com/docs/en/keybindings).
```bash
brew install --cask ghostty
mkdir -p ~/.config/ghostty && echo 'macos-option-as-alt = true' >> ~/.config/ghostty/config
```
```json
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "bindings": [ { "context": "Scroll", "bindings": { "ctrl+x ctrl+g": "scroll:bottom" } } ]
}
```
iTerm2 alternative: Option = Esc+, mouse reporting on, Filter Alerts → escape-sequence alerts, then `/terminal-setup`. Don't use `tmux -CC` with fullscreen. If notifications don't appear outside Ghostty and iTerm2, `notify.mjs` uses osascript. Run `osascript -e 'display notification "test"'` once, then allow Script Editor in System Settings → Notifications [[22]](https://code.claude.com/docs/en/hooks-guide)[[143]](https://code.claude.com/docs/en/terminal-config).

**10. VS Code and Desktop.** Both share `~/.claude/settings.json`. Desktop reads only PATH from `~/.zshrc`, so put other variables in the settings `env` block [[194]](https://code.claude.com/docs/en/vs-code)[[168]](https://code.claude.com/docs/en/desktop)[[195]](https://formulae.brew.sh/cask/claude)[[183]](https://code.claude.com/docs/en/plugins/install).
```bash
code --install-extension anthropic.claude-code      # VS Code: "terminal.integrated.macOptionIsMeta": true ; run /terminal-setup in its terminal
brew install --cask claude
claude --desktop --continue
# System Settings > Keyboard > Keyboard Shortcuts > Game Controllers > untick Game Overlay (frees Cmd+Esc)
```
**11. Optional rtk on the Mac.** It compresses Bash output, with self-reported savings of 60–90%; measure with `rtk gain`. ⛔ **Never enable `rtk-proxy`**, which routes calls to non-Claude models [[71]](https://github.com/rtk-ai/rtk).
```bash
brew install rtk && rtk init -g && rtk gain
```
**12. Mac standup.** Use a Desktop local task (§5.10 A), or launchd with `pmset repeat wakeorpoweron MTWRFSU 06:00:00` and the same `claude -p … --permission-mode dontAsk` line [[146]](https://code.claude.com/docs/en/headless). Mac Desktop hygiene: update it, quit fully with Cmd+Q daily, and if it freezes on launch, `mv` `scheduled-tasks.json` aside [[164]](https://status.claude.com/incidents/pqpgkf52p3tg)[[166]](https://github.com/anthropics/claude-code/issues/32167)[[168]](https://code.claude.com/docs/en/desktop).

**Daily sync, either machine:**
```bash
git -C ~/.claude pull --rebase && git -C ~/.claude add -A && git -C ~/.claude commit -m sync; git -C ~/.claude push
```

---

## 10. Rejected / risky ideas and why

| Idea | Verdict | Reason |
|---|---|---|
| Fast mode | ⛔ Block | Billed through usage credits only; the first enable charges the whole context uncached [[3]](https://code.claude.com/docs/en/fast-mode) |
| Usage credits / "raise spend limit" / extra usage | ⛔ Block | Real money, which breaks the $0 rule. It also drops the cache TTL to 5 min [[196]](https://code.claude.com/docs/en/costs#add-usage-credits-to-your-subscription)[[43]](https://code.claude.com/docs/en/prompt-caching) |
| Fable in `-p`, scheduled or advisor runs; `--model best` | ⛔ Block | Headless Fable bills without asking; a Fable advisor bills to credits [[4]](https://code.claude.com/docs/en/model-config#fable-and-usage-credits)[[85]](https://code.claude.com/docs/en/advisor) |
| Sonnet 4.6 `[1m]` | ⛔ Block | Needs credits on every plan, Max included [[197]](https://code.claude.com/docs/en/model-config#extended-context) |
| Fable "included up to 50% of the Max weekly limit since 2026-07-20" | **[unverified]** | Only third-party sources say this. The docs say only "can bill to usage credits" [[198]](https://claudelog.com/faqs/is-fable-5-available-on-claude-pro-max/)[[199]](https://gigazine.net/gsc_news/en/20260719-claude-fable-5-plan) |
| `--bare` for automation | ⛔ Reject | Requires `ANTHROPIC_API_KEY` [[54]](https://code.claude.com/docs/en/cli-reference) |
| Re-keying 21st.dev `magic` | ⛔ Reject | Needs an external key plus hosted, metered AI [[124]](https://github.com/21st-dev/magic-mcp) |
| Higgsfield connector | ⛔ Reject | Third-party generative-model service |
| Gemini skills (ckm:design/banner, data-scraper-agent), taste-skill's OpenAI branch, claude-code-router / PAL / Gemini CLI MCP, Greptile / CodeRabbit | ⛔ Reject | Non-Claude providers or paid keys |
| claude-mem cloud-sync (cmem.ai Pro), wowerpoint (NotebookLM) | ⛔ Deny | Paid service, or a Google model |
| Ultrareview beyond its 3 free runs | ⛔ Block | Then $5–25 per run in credits [[94]](https://code.claude.com/docs/en/ultrareview) |
| effortless "Jev" judge, rtk-proxy | ⛔ Keep off | One needs a TypeSafe key; the other routes to other models |
| Telemetry-off env vars | Reject | They silently turn off Remote Control, the advisor, idle compaction and more [[160]](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching) |
| Global `ultracode` | Reject | Every task becomes a fan-out and the warnings are skipped [[52]](https://code.claude.com/docs/en/workflows#let-claude-decide-with-ultracode) |
| `max` effort as a default; thinking-token env vars | Reject | Overthinking, flagged by `/usage`; the thinking vars do nothing on 5.5 models [[81]](https://code.claude.com/docs/en/model-config#extended-thinking) |
| Agent teams | Reject | About 7× tokens [[49]](https://code.claude.com/docs/en/agent-teams) |
| context-mode plugin | Reject | Six hooks that would interleave with claude-mem and unlazy; overlapping memory; ELv2 license; savings are self-reported [[72]](https://github.com/mksglu/context-mode) |
| ralph-loop | Reject | A second blocking Stop hook that would fight unlazy |
| Mutating PostToolUse formatter | Avoid | Stale-read Edit failures (community report). Format at commit time instead [[141]](https://claudeissues.com/issue/51361-edit-tool-fails-when-linter-formatter-modifies-file-between-read-and-edit) |
| `ENABLE_TOOL_SEARCH=false`; raising output caps | Reject | Every request gets heavier [[123]](https://code.claude.com/docs/en/mcp)[[57]](https://code.claude.com/docs/en/env-vars) |
| Serena / Playwright / GitHub MCPs | Skip | LSP, playwright-cli and gh are leaner; Serena says not to install it via a marketplace [[127]](https://github.com/oraios/serena)[[126]](https://github.com/microsoft/playwright-cli) |
| `opusplan` as your all-day model | Risky | With acceptEdits or auto it is plain Sonnet, and each plan toggle re-reads uncached [[44]](https://code.claude.com/docs/en/prompt-caching#switching-models) |
| Hourly `/loop` in a big session | Risky | Jitter means the cache is usually cold, so every fire reprocesses the whole context [[55]](https://code.claude.com/docs/en/scheduled-tasks) |
| Replacing the whole `hooks` block or `skillOverrides` object | Risky | It silently drops the claude-mem self-heal hook and about 60 overrides |
| Syncing `~/.claude.json`, credentials or live claude-mem files | Reject | Path-keyed secrets; SQLite WAL corruption [[23]](https://code.claude.com/docs/en/claude-directory)[[186]](https://docs.claude-mem.ai/usage/export-import) |
| `CLAUDE_CODE_OAUTH_TOKEN` as the Mac login | Avoid | No connectors, no Remote Control, no sync [[175]](https://code.claude.com/docs/en/authentication) |
| `claude mcp remove magic -s user` | Stale | The server is already gone, so the command now fails |
| Other unverified points | **[unverified]** | `skipWorkflowUsageWarning` semantics; `CLAUDE_CODE_WORKFLOW_SUBAGENT_MODEL` (changelog only); auto-mode classifier cost on Max (not measured); `/verify` pre-commit wording; colon `skillOverrides` keys; `Skill(plugin:x)` deny matching; `updatedInput` without a decision; WinRT toast display; savings claims for effortless, rtk and context-mode; security-guidance log path and cost visibility; the VPN details in #68316 |

---

## 11. Source list

1. [https://code.claude.com/docs/en/settings-reference#effortlevel](https://code.claude.com/docs/en/settings-reference#effortlevel)
2. [https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)
3. [https://code.claude.com/docs/en/fast-mode](https://code.claude.com/docs/en/fast-mode)
4. [https://code.claude.com/docs/en/model-config#fable-and-usage-credits](https://code.claude.com/docs/en/model-config#fable-and-usage-credits)
5. [https://github.com/thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
6. [https://code.claude.com/docs/en/discover-plugins](https://code.claude.com/docs/en/discover-plugins)
7. [https://code.claude.com/docs/en/costs#why-usage-climbs-in-a-long-session](https://code.claude.com/docs/en/costs#why-usage-climbs-in-a-long-session)
8. [https://code.claude.com/docs/en/best-practices#manage-context-aggressively](https://code.claude.com/docs/en/best-practices#manage-context-aggressively)
9. [https://code.claude.com/docs/en/statusline](https://code.claude.com/docs/en/statusline)
10. [https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode](https://code.claude.com/docs/en/permission-modes#eliminate-prompts-with-auto-mode)
11. [https://code.claude.com/docs/en/auto-mode-config](https://code.claude.com/docs/en/auto-mode-config)
12. [https://code.claude.com/docs/en/permissions](https://code.claude.com/docs/en/permissions)
13. [https://code.claude.com/docs/en/plugins/code-intelligence](https://code.claude.com/docs/en/plugins/code-intelligence)
14. [https://code.claude.com/docs/en/best-practices#give-claude-a-way-to-verify-its-work](https://code.claude.com/docs/en/best-practices#give-claude-a-way-to-verify-its-work)
15. [https://code.claude.com/docs/en/goal](https://code.claude.com/docs/en/goal)
16. [https://code.claude.com/docs/en/code-review-local](https://code.claude.com/docs/en/code-review-local)
17. [https://code.claude.com/docs/en/memory#audit-your-instruction-files](https://code.claude.com/docs/en/memory#audit-your-instruction-files)
18. [https://code.claude.com/docs/en/memory#auto-memory](https://code.claude.com/docs/en/memory#auto-memory)
19. [https://code.claude.com/docs/en/skills#resolve-skills-that-share-a-name](https://code.claude.com/docs/en/skills#resolve-skills-that-share-a-name)
20. [https://code.claude.com/docs/en/skills#override-skill-visibility-from-settings](https://code.claude.com/docs/en/skills#override-skill-visibility-from-settings)
21. [https://code.claude.com/docs/en/hooks](https://code.claude.com/docs/en/hooks)
22. [https://code.claude.com/docs/en/hooks-guide](https://code.claude.com/docs/en/hooks-guide)
23. [https://code.claude.com/docs/en/claude-directory](https://code.claude.com/docs/en/claude-directory)
24. [https://code.claude.com/docs/en/plugins/loading](https://code.claude.com/docs/en/plugins/loading)
25. [https://code.claude.com/docs/en/output-styles#concise](https://code.claude.com/docs/en/output-styles#concise)
26. [https://code.claude.com/docs/en/sub-agents](https://code.claude.com/docs/en/sub-agents)
27. [https://peps.python.org/pep-0686/](https://peps.python.org/pep-0686/)
28. [https://code.claude.com/docs/en/tools-reference](https://code.claude.com/docs/en/tools-reference)
29. [https://code.claude.com/docs/en/settings-reference#autoupdateschannel](https://code.claude.com/docs/en/settings-reference#autoupdateschannel)
30. [https://code.claude.com/docs/en/settings-reference#minimumversion](https://code.claude.com/docs/en/settings-reference#minimumversion)
31. [https://code.claude.com/docs/en/costs](https://code.claude.com/docs/en/costs)
32. [https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything)
33. [https://platform.claude.com/docs/en/about-claude/pricing](https://platform.claude.com/docs/en/about-claude/pricing)
34. [https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-pro-or-max-plan)
35. [https://code.claude.com/docs/en/model-config](https://code.claude.com/docs/en/model-config)
36. [https://code.claude.com/docs/en/model-config#set-the-auto-compact-window](https://code.claude.com/docs/en/model-config#set-the-auto-compact-window)
37. [https://code.claude.com/docs/en/context-window#when-your-context-fills-up](https://code.claude.com/docs/en/context-window#when-your-context-fills-up)
38. [https://code.claude.com/docs/en/settings-reference#idlecompaction](https://code.claude.com/docs/en/settings-reference#idlecompaction)
39. [https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md](https://raw.githubusercontent.com/anthropics/claude-code/main/CHANGELOG.md)
40. [https://code.claude.com/docs/en/best-practices](https://code.claude.com/docs/en/best-practices)
41. [https://code.claude.com/docs/en/context-window](https://code.claude.com/docs/en/context-window)
42. [https://code.claude.com/docs/en/interactive-mode](https://code.claude.com/docs/en/interactive-mode)
43. [https://code.claude.com/docs/en/prompt-caching](https://code.claude.com/docs/en/prompt-caching)
44. [https://code.claude.com/docs/en/prompt-caching#switching-models](https://code.claude.com/docs/en/prompt-caching#switching-models)
45. [https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything](https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything)
46. [https://chen.media/guides/three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha](https://chen.media/guides/three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha)
47. [https://code.claude.com/docs/en/prompt-caching#changing-effort-level](https://code.claude.com/docs/en/prompt-caching#changing-effort-level)
48. [https://code.claude.com/docs/en/prompt-caching#changing-output-style](https://code.claude.com/docs/en/prompt-caching#changing-output-style)
49. [https://code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams)
50. [https://code.claude.com/docs/en/workflows](https://code.claude.com/docs/en/workflows)
51. [https://code.claude.com/docs/en/workflows#cost](https://code.claude.com/docs/en/workflows#cost)
52. [https://code.claude.com/docs/en/workflows#let-claude-decide-with-ultracode](https://code.claude.com/docs/en/workflows#let-claude-decide-with-ultracode)
53. [https://code.claude.com/docs/en/settings-reference#ultracode](https://code.claude.com/docs/en/settings-reference#ultracode)
54. [https://code.claude.com/docs/en/cli-reference](https://code.claude.com/docs/en/cli-reference)
55. [https://code.claude.com/docs/en/scheduled-tasks](https://code.claude.com/docs/en/scheduled-tasks)
56. [https://chen.media/guides/find-the-claude-code-loops-that-are-quietly-eating-your-limit](https://chen.media/guides/find-the-claude-code-loops-that-are-quietly-eating-your-limit)
57. [https://code.claude.com/docs/en/env-vars](https://code.claude.com/docs/en/env-vars)
58. [https://code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills)
59. [https://code.claude.com/docs/en/skills#find-unused-skills](https://code.claude.com/docs/en/skills#find-unused-skills)
60. [https://code.claude.com/docs/en/settings-reference#skilllistingbudgetfraction](https://code.claude.com/docs/en/settings-reference#skilllistingbudgetfraction)
61. [https://code.claude.com/docs/en/plugins/measure](https://code.claude.com/docs/en/plugins/measure)
62. [https://code.claude.com/docs/en/settings](https://code.claude.com/docs/en/settings)
63. [https://github.com/anthropics/claude-plugins-official/tree/main/plugins/session-report](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/session-report)
64. [https://github.com/ryoppippi/ccusage](https://github.com/ryoppippi/ccusage)
65. [https://ccusage.com/guide/blocks-reports](https://ccusage.com/guide/blocks-reports)
66. [https://github.com/ccusage/ccusage](https://github.com/ccusage/ccusage)
67. [https://ccusage.com/guide/statusline](https://ccusage.com/guide/statusline)
68. [https://code.claude.com/docs/en/settings-reference#outputstyle](https://code.claude.com/docs/en/settings-reference#outputstyle)
69. [https://github.com/HeyCubit/effortless](https://github.com/HeyCubit/effortless)
70. [https://chen.media/guides/cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless)
71. [https://github.com/rtk-ai/rtk](https://github.com/rtk-ai/rtk)
72. [https://github.com/mksglu/context-mode](https://github.com/mksglu/context-mode)
73. [https://agentskill.sh/plugins/mksglu/context-mode](https://agentskill.sh/plugins/mksglu/context-mode)
74. [https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode)
75. [https://code.claude.com/docs/en/costs#choose-the-right-model](https://code.claude.com/docs/en/costs#choose-the-right-model)
76. [https://www.anthropic.com/engineering/april-23-postmortem](https://www.anthropic.com/engineering/april-23-postmortem)
77. [https://code.claude.com/docs/en/settings-reference#modelsettings](https://code.claude.com/docs/en/settings-reference#modelsettings)
78. [https://code.claude.com/docs/en/model-config#adjust-effort-level](https://code.claude.com/docs/en/model-config#adjust-effort-level)
79. [https://www.schemastore.org/claude-code-settings.json](https://www.schemastore.org/claude-code-settings.json)
80. [https://code.claude.com/docs/en/settings-reference#maxeffortlevel](https://code.claude.com/docs/en/settings-reference#maxeffortlevel)
81. [https://code.claude.com/docs/en/model-config#extended-thinking](https://code.claude.com/docs/en/model-config#extended-thinking)
82. [https://code.claude.com/docs/en/model-config#use-ultrathink-for-one-off-deep-reasoning](https://code.claude.com/docs/en/model-config#use-ultrathink-for-one-off-deep-reasoning)
83. [https://code.claude.com/docs/en/memory#write-effective-instructions](https://code.claude.com/docs/en/memory#write-effective-instructions)
84. [https://code.claude.com/docs/en/hooks#stop-input](https://code.claude.com/docs/en/hooks#stop-input)
85. [https://code.claude.com/docs/en/advisor](https://code.claude.com/docs/en/advisor)
86. [https://code.claude.com/docs/en/settings-reference#advisormodel](https://code.claude.com/docs/en/settings-reference#advisormodel)
87. [https://code.claude.com/docs/en/model-config#opusplan-model-setting](https://code.claude.com/docs/en/model-config#opusplan-model-setting)
88. [https://code.claude.com/docs/en/best-practices#explore-first-then-plan-then-code](https://code.claude.com/docs/en/best-practices#explore-first-then-plan-then-code)
89. [https://code.claude.com/docs/en/best-practices#let-claude-interview-you](https://code.claude.com/docs/en/best-practices#let-claude-interview-you)
90. [https://code.claude.com/docs/en/commands](https://code.claude.com/docs/en/commands)
91. [https://www.anthropic.com/engineering/harness-design-long-running-apps](https://www.anthropic.com/engineering/harness-design-long-running-apps)
92. [https://code.claude.com/docs/en/best-practices#add-an-adversarial-review-step](https://code.claude.com/docs/en/best-practices#add-an-adversarial-review-step)
93. [https://code.claude.com/docs/en/ultrareview#pricing-and-free-runs](https://code.claude.com/docs/en/ultrareview#pricing-and-free-runs)
94. [https://code.claude.com/docs/en/ultrareview](https://code.claude.com/docs/en/ultrareview)
95. [https://code.claude.com/docs/en/skills#run-and-verify-your-app](https://code.claude.com/docs/en/skills#run-and-verify-your-app)
96. [https://code.claude.com/docs/en/best-practices#provide-specific-context-in-your-prompts](https://code.claude.com/docs/en/best-practices#provide-specific-context-in-your-prompts)
97. [https://code.claude.com/docs/en/best-practices#run-multiple-claude-sessions](https://code.claude.com/docs/en/best-practices#run-multiple-claude-sessions)
98. [https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
99. [https://github.com/obra/superpowers](https://github.com/obra/superpowers)
100. [https://code.claude.com/docs/en/memory](https://code.claude.com/docs/en/memory)
101. [https://code.claude.com/docs/en/memory#import-additional-files](https://code.claude.com/docs/en/memory#import-additional-files)
102. [https://code.claude.com/docs/en/memory#how-claude-md-files-load](https://code.claude.com/docs/en/memory#how-claude-md-files-load)
103. [https://code.claude.com/docs/en/costs#move-instructions-from-claude-md-to-skills](https://code.claude.com/docs/en/costs#move-instructions-from-claude-md-to-skills)
104. [https://code.claude.com/docs/en/best-practices#write-an-effective-claudemd](https://code.claude.com/docs/en/best-practices#write-an-effective-claudemd)
105. [https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
106. [https://code.claude.com/docs/en/worktrees](https://code.claude.com/docs/en/worktrees)
107. [https://code.claude.com/docs/en/debug-your-config](https://code.claude.com/docs/en/debug-your-config)
108. [https://github.com/obra/superpowers/releases](https://github.com/obra/superpowers/releases)
109. [https://github.com/anthropics/claude-plugins-official/tree/main/plugins/pyright-lsp](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/pyright-lsp)
110. [https://github.com/anthropics/claude-plugins-official/tree/main/plugins/typescript-lsp](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/typescript-lsp)
111. [https://github.com/anthropics/claude-plugins-official/tree/main/plugins/rust-analyzer-lsp](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/rust-analyzer-lsp)
112. [https://github.com/anthropics/claude-plugins-official/tree/main/plugins/security-guidance](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/security-guidance)
113. [https://github.com/pbakaus/impeccable](https://github.com/pbakaus/impeccable)
114. [https://emelia.io/hub/impeccable-design-skill-review](https://emelia.io/hub/impeccable-design-skill-review)
115. [https://github.com/anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
116. [https://code.claude.com/docs/en/plugins/anthropic-marketplaces](https://code.claude.com/docs/en/plugins/anthropic-marketplaces)
117. [https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-loop](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-loop)
118. [https://github.com/anthropics/skills](https://github.com/anthropics/skills)
119. [https://github.com/upstash/context7](https://github.com/upstash/context7)
120. [https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/context7](https://github.com/anthropics/claude-plugins-official/tree/main/external_plugins/context7)
121. [https://context7.com/docs/clients/claude-code](https://context7.com/docs/clients/claude-code)
122. [https://context7.com/docs/resources/all-clients](https://context7.com/docs/resources/all-clients)
123. [https://code.claude.com/docs/en/mcp](https://code.claude.com/docs/en/mcp)
124. [https://github.com/21st-dev/magic-mcp](https://github.com/21st-dev/magic-mcp)
125. [https://mcp.directory/blog/21st-dev-magic-mcp-complete-guide-2026](https://mcp.directory/blog/21st-dev-magic-mcp-complete-guide-2026)
126. [https://github.com/microsoft/playwright-cli](https://github.com/microsoft/playwright-cli)
127. [https://github.com/oraios/serena](https://github.com/oraios/serena)
128. [https://ui.shadcn.com/docs/mcp](https://ui.shadcn.com/docs/mcp)
129. [https://code.claude.com/docs/en/settings-reference#skilloverrides](https://code.claude.com/docs/en/settings-reference#skilloverrides)
130. [https://code.claude.com/docs/en/skills#skill-descriptions-are-cut-short](https://code.claude.com/docs/en/skills#skill-descriptions-are-cut-short)
131. [https://code.claude.com/docs/en/workflows#bundled-workflows](https://code.claude.com/docs/en/workflows#bundled-workflows)
132. [https://code.claude.com/docs/en/hooks#exec-form-and-shell-form](https://code.claude.com/docs/en/hooks#exec-form-and-shell-form)
133. [https://code.claude.com/docs/en/plugins-reference](https://code.claude.com/docs/en/plugins-reference)
134. [https://code.claude.com/docs/en/settings-reference#statusline](https://code.claude.com/docs/en/settings-reference#statusline)
135. [https://github.com/jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud)
136. [https://github.com/sirmalloc/ccstatusline](https://github.com/sirmalloc/ccstatusline)
137. [https://code.claude.com/docs/en/changelog](https://code.claude.com/docs/en/changelog)
138. [https://github.com/kenryu42/claude-code-safety-net](https://github.com/kenryu42/claude-code-safety-net)
139. [https://code.claude.com/docs/en/hooks-guide#auto-format-code-after-edits](https://code.claude.com/docs/en/hooks-guide#auto-format-code-after-edits)
140. [https://code.claude.com/docs/en/best-practices#set-up-hooks](https://code.claude.com/docs/en/best-practices#set-up-hooks)
141. [https://claudeissues.com/issue/51361-edit-tool-fails-when-linter-formatter-modifies-file-between-read-and-edit](https://claudeissues.com/issue/51361-edit-tool-fails-when-linter-formatter-modifies-file-between-read-and-edit)
142. [https://code.claude.com/docs/en/settings-reference#cleanupperioddays](https://code.claude.com/docs/en/settings-reference#cleanupperioddays)
143. [https://code.claude.com/docs/en/terminal-config](https://code.claude.com/docs/en/terminal-config)
144. [https://www.powershellgallery.com/packages/AutomatedLabNotifications/5.14.0/Content/Private%5CSend-ALToastNotification.ps1](https://www.powershellgallery.com/packages/AutomatedLabNotifications/5.14.0/Content/Private%5CSend-ALToastNotification.ps1)
145. [https://code.claude.com/docs/en/desktop-scheduled-tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks)
146. [https://code.claude.com/docs/en/headless](https://code.claude.com/docs/en/headless)
147. [https://learn.microsoft.com/en-us/powershell/module/scheduledtasks/register-scheduledtask](https://learn.microsoft.com/en-us/powershell/module/scheduledtasks/register-scheduledtask)
148. [https://code.claude.com/docs/en/errors](https://code.claude.com/docs/en/errors)
149. [https://code.claude.com/docs/en/routines](https://code.claude.com/docs/en/routines)
150. [https://code.claude.com/docs/en/remote-control](https://code.claude.com/docs/en/remote-control)
151. [https://code.claude.com/docs/en/agent-view](https://code.claude.com/docs/en/agent-view)
152. [https://code.claude.com/docs/en/settings#edit-a-settings-file](https://code.claude.com/docs/en/settings#edit-a-settings-file)
153. [https://code.claude.com/docs/en/settings-reference](https://code.claude.com/docs/en/settings-reference)
154. [https://code.claude.com/docs/en/setup](https://code.claude.com/docs/en/setup)
155. [https://code.claude.com/docs/en/settings-reference#permissions-defaultmode](https://code.claude.com/docs/en/settings-reference#permissions-defaultmode)
156. [https://code.claude.com/docs/en/settings-reference#automode](https://code.claude.com/docs/en/settings-reference#automode)
157. [https://code.claude.com/docs/en/permission-modes](https://code.claude.com/docs/en/permission-modes)
158. [https://code.claude.com/docs/en/settings-reference#env](https://code.claude.com/docs/en/settings-reference#env)
159. [https://code.claude.com/docs/en/settings-reference#availablemodels](https://code.claude.com/docs/en/settings-reference#availablemodels)
160. [https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching](https://code.claude.com/docs/en/env-vars#features-that-need-feature-flag-fetching)
161. [https://code.claude.com/docs/en/settings-reference#automemoryenabled](https://code.claude.com/docs/en/settings-reference#automemoryenabled)
162. [https://code.claude.com/docs/en/output-styles](https://code.claude.com/docs/en/output-styles)
163. [https://code.claude.com/docs/en/troubleshooting](https://code.claude.com/docs/en/troubleshooting)
164. [https://status.claude.com/incidents/pqpgkf52p3tg](https://status.claude.com/incidents/pqpgkf52p3tg)
165. [https://github.com/anthropics/claude-code/issues/68316](https://github.com/anthropics/claude-code/issues/68316)
166. [https://github.com/anthropics/claude-code/issues/32167](https://github.com/anthropics/claude-code/issues/32167)
167. [https://github.com/anthropics/claude-code/issues/39303](https://github.com/anthropics/claude-code/issues/39303)
168. [https://code.claude.com/docs/en/desktop](https://code.claude.com/docs/en/desktop)
169. [https://docs.python.org/3/library/os.html#utf8-mode](https://docs.python.org/3/library/os.html#utf8-mode)
170. [https://claudeissues.com/issue/69171-bug-windows-statusline-command-is-spawned-with-cp1252-stdout-scripts-printing-no](https://claudeissues.com/issue/69171-bug-windows-statusline-command-is-spawned-with-cp1252-stdout-scripts-printing-no)
171. [https://github.com/anthropics/claude-code/issues/69171](https://github.com/anthropics/claude-code/issues/69171)
172. [https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows](https://learn.microsoft.com/en-us/powershell/scripting/install/install-powershell-on-windows)
173. [https://docs.github.com/en/get-started/git-basics/configuring-git-to-handle-line-endings](https://docs.github.com/en/get-started/git-basics/configuring-git-to-handle-line-endings)
174. [https://code.claude.com/docs/en/sandboxing](https://code.claude.com/docs/en/sandboxing)
175. [https://code.claude.com/docs/en/authentication](https://code.claude.com/docs/en/authentication)
176. [https://www.steeman.be/posts/syncing-claude-code-across-multiple-machines/](https://www.steeman.be/posts/syncing-claude-code-across-multiple-machines/)
177. [https://www.chezmoi.io/user-guide/manage-machine-to-machine-differences/](https://www.chezmoi.io/user-guide/manage-machine-to-machine-differences/)
178. [https://github.com/funkadelic/claude-nomad](https://github.com/funkadelic/claude-nomad)
179. [https://code.claude.com/docs/en/skills#where-synced-skills-load](https://code.claude.com/docs/en/skills#where-synced-skills-load)
180. [https://code.claude.com/docs/en/plugins/loading#synced-plugins](https://code.claude.com/docs/en/plugins/loading#synced-plugins)
181. [https://git-scm.com/docs/gitattributes](https://git-scm.com/docs/gitattributes)
182. [https://formulae.brew.sh/cask/claude-code@latest](https://formulae.brew.sh/cask/claude-code@latest)
183. [https://code.claude.com/docs/en/plugins/install](https://code.claude.com/docs/en/plugins/install)
184. [https://code.claude.com/docs/en/plugin-marketplaces](https://code.claude.com/docs/en/plugin-marketplaces)
185. [https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp)
186. [https://docs.claude-mem.ai/usage/export-import](https://docs.claude-mem.ai/usage/export-import)
187. [https://github.com/safishamsi/graphify](https://github.com/safishamsi/graphify)
188. [https://graphify.com/docs/install](https://graphify.com/docs/install)
189. [https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html](https://developer.apple.com/library/archive/documentation/MacOSX/Conceptual/BPSystemStartup/Chapters/CreatingLaunchdJobs.html)
190. [https://code.claude.com/docs/en/settings-reference#sandbox](https://code.claude.com/docs/en/settings-reference#sandbox)
191. [https://code.claude.com/docs/en/fullscreen](https://code.claude.com/docs/en/fullscreen)
192. [https://formulae.brew.sh/cask/ghostty](https://formulae.brew.sh/cask/ghostty)
193. [https://code.claude.com/docs/en/keybindings](https://code.claude.com/docs/en/keybindings)
194. [https://code.claude.com/docs/en/vs-code](https://code.claude.com/docs/en/vs-code)
195. [https://formulae.brew.sh/cask/claude](https://formulae.brew.sh/cask/claude)
196. [https://code.claude.com/docs/en/costs#add-usage-credits-to-your-subscription](https://code.claude.com/docs/en/costs#add-usage-credits-to-your-subscription)
197. [https://code.claude.com/docs/en/model-config#extended-context](https://code.claude.com/docs/en/model-config#extended-context)
198. [https://claudelog.com/faqs/is-fable-5-available-on-claude-pro-max/](https://claudelog.com/faqs/is-fable-5-available-on-claude-pro-max/)
199. [https://gigazine.net/gsc_news/en/20260719-claude-fable-5-plan](https://gigazine.net/gsc_news/en/20260719-claude-fable-5-plan)
