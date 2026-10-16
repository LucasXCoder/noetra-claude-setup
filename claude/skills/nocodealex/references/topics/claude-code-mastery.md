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

---

## Atom index

<!-- AUTO:atoms BEGIN -- regenerated by build_topics.py, do not edit below -->

*1060 atoms.*

### analogy

- `g06-0151` *STATED* — bigarrow gives Claude a finger: it points at the exact button on screen.
  > “gives it a finger”
  — [g-make-claude-point-at-the-button-you-need-to-click](https://chen.media/guides/make-claude-point-at-the-button-you-need-to-click)
  ↳ *analogy-for* `g06-0149`

- `g18-0230` *STATED* — Long instruction files are usually a museum of old problems.
  > “Long instruction files are usually a museum of old problems.”
  — [g-three-things-almost-everyone-gets-wrong-about-claude-code](https://chen.media/guides/three-things-almost-everyone-gets-wrong-about-claude-code)
  ↳ *analogy-for* `g18-0231`

- `y01-0161` *STATED* — Think of Claude project folders as long-term memory for Claude.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *analogy-for* `g17-0019`

- `y03-0036` *STATED* — Alex's effort-level video dresses Claude from pyjamas (low effort) up to a superhero (Ultra Code).
  — [ItG-vSZFWgA](https://youtu.be/ItG-vSZFWgA) [mVKBGZNsSa4](https://youtu.be/mVKBGZNsSa4) [HTu9VPLvcP0](https://youtu.be/HTu9VPLvcP0)
  ↳ *analogy-for* `y03-0035`
  ↳ *example-of* `y03-0206`

- `y03-0096` *STATED* — Claude using 120GB on a 96GB Mac is like cramming 120 people onto a bus with 96 seats.
  — [5Ik2XpcR5uE](https://youtu.be/5Ik2XpcR5uE)
  ↳ *analogy-for* `y03-0097`
  ↳ *example-of* `y03-0206`

### caveat

- `g02-0053` *INFERRED* — Because cc-stretch's short view carries only about two of every three key points, roughly one key point in three stays hidden until you expand it.
  — [g-make-claude-s-long-answers-6x-shorter-to-read](https://chen.media/guides/make-claude-s-long-answers-6x-shorter-to-read)
  ↳ *qualifies* `g02-0047`

- `g02-0124` *STATED* — Time Machine's /tm restore shows a dry run first before it puts files back.
  — [g-rewind-claude-code-to-the-step-that-broke-your-code](https://chen.media/guides/rewind-claude-code-to-the-step-that-broke-your-code)
  ↳ *qualifies* `g02-0123`

- `g02-0203` *INFERRED* — Because you list loops from the session where you started them, Claude Code scheduled tasks appear to be scoped to the session that created them.
  — [g-find-the-claude-code-loops-that-are-quietly-eating-your-limit](https://chen.media/guides/find-the-claude-code-loops-that-are-quietly-eating-your-limit)
  ↳ *qualifies* `g02-0199`
  ↳ *evidence-for* `r02-0037`

- `g03-0088` *STATED* — Background Claude Code sessions come with two catches, covered in the locked "The catches" section.
  — [g-keep-claude-working-after-you-close-the-terminal](https://chen.media/guides/keep-claude-working-after-you-close-the-terminal)
  ↳ *example-of* `g03-0006`
  ↳ *qualifies* `g03-0081`

- `g03-0115` *STATED* — If the prompt box has text, double Escape clears it instead of opening rewind, and pressing Up brings the text back.
  — [g-rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it](https://chen.media/guides/rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it)
  ↳ *qualifies* `g03-0114`

- `g03-0119` *STATED* — Some changes cannot be undone by rewind; the guide's catch lists them.
  > “the changes rewind cannot undo”
  — [g-rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it](https://chen.media/guides/rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it)
  ↳ *example-of* `g03-0006`
  ↳ *qualifies* `g03-0112`

- `g03-0164` *STATED* — Plan mode is not always worth it; the guide's catch covers when to skip it.
  — [g-turn-on-plan-mode-so-claude-plans-before-it-edits](https://chen.media/guides/turn-on-plan-mode-so-claude-plans-before-it-edits)
  ↳ *example-of* `g03-0006`
  ↳ *qualifies* `g03-0155` — cost guide recommends it for complex tasks, not all

- `g04-0068` *STATED* — There are places where the onFailure setting does nothing (Alex's 'The catch' section, body locked).
  > “where it does nothing”
  — [g-make-a-crashed-claude-hook-block-the-action-not-let-it-through](https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through)
  ↳ *qualifies* `g04-0059`
  ↳ *example-of* `g04-0242`

- `g04-0095` *STATED* — The test-filter hook falls short in some cases (Alex's 'The catch' section, body locked).
  > “where it falls short”
  — [g-the-claude-hook-that-cuts-test-output-down-to-just-the-failures](https://chen.media/guides/the-claude-hook-that-cuts-test-output-down-to-just-the-failures)
  ↳ *qualifies* `g04-0087`
  ↳ *example-of* `g04-0242`

- `g05-0177` *STATED* — One variable overrides both the subagent file's effort and the per-run effort parameter (named in the gated catch section; 2 prompts to copy, 4 numbered steps).
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)
  ↳ *qualifies* `g05-0172`

- `g05-0220` *INFERRED* — wc -l is a Mac/Linux command; on Windows run the skill line count from Git Bash or ask Claude to count lines.
  — [g-claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix](https://chen.media/guides/claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix)
  ↳ *qualifies* `g05-0212`

- `g06-0247` *STATED* — Alex flags a catch with CLAUDE.md: how much Claude actually obeys it (details in the gated 'The catch').
  — [g-give-claude-a-notebook-that-survives-every-chat-reset](https://chen.media/guides/give-claude-a-notebook-that-survives-every-chat-reset)
  ↳ *qualifies* `g06-0241`
  ↳ *qualifies* `y04-0118`
  ↳ *qualifies* `g20-0236`

- `g07-0021` *STATED* — Claude Code's next-prompt suggestion stays hidden in some situations ('when it stays hidden'; conditions email-gated).
  — [g-let-claude-code-write-your-next-prompt-press-tab](https://chen.media/guides/let-claude-code-write-your-next-prompt-press-tab)
  ↳ *part-of* `g07-0013`
  ↳ *qualifies* `g07-0013`

- `g07-0174` *STATED* — All three sample mods draw in the terminal, so run claude in a terminal (an editor's built-in terminal works too).
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`
  ↳ *qualifies* `g07-0177`
  ↳ *contrast* `g07-0194` — mods need the terminal; Projects can't run there

- `g07-0180` *STATED* — Alex's mods guide closes with 'The honest notes' on the limits of mods (email-gated).
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`
  ↳ *qualifies* `g07-0176`

- `g07-0194` *STATED* — Claude Code Projects does not run in the terminal, VS Code or JetBrains.
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`
  ↳ *contrast* `g07-0193`

- `g07-0201` *STATED* — Alex's Projects guide closes with 'The honest notes' (email-gated).
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`

- `g08-0114` *STATED* — Claude Motion is in beta on Team and Enterprise plans.
  — [g-make-animated-explainer-videos-inside-claude-try-the-new-claude-motion](https://chen.media/guides/make-animated-explainer-videos-inside-claude-try-the-new-claude-motion)
  ↳ *qualifies* `g08-0106`

- `g08-0201` *STATED* — /bouncer is a rule Claude follows when you call it, not a lock, so skim its list before you let it carry on.
  > “It is a rule Claude follows when you call it. It is not a lock, so skim the list before you let it carry on.”
  — [g-stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes](https://chen.media/guides/stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes)
  ↳ *qualifies* `g08-0191`
  ↳ *example-of* `g08-0258`

- `g08-0248` *STATED* — The /trojan video calls the three checks three agents, but it is one small script plus Claude reading its report, so it is quick and free.
  > “It is one small script plus Claude reading its report, so it is quick and it is free.”
  — [g-stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes](https://chen.media/guides/stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes)
  ↳ *qualifies* `g08-0237`
  ↳ *example-of* `g08-0258`

- `g10-0031` *STATED* — Alex Chen's Claude app memory-leak guide ends with 'The honest notes' section (body locked).
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *qualifies* `g10-0025`
  ↳ *example-of* `g10-0270`

- `g10-0044` *STATED* — Your Mac's SSD holds all your files and can't be swapped out (replaced) on most Macs, so swap wear matters.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *qualifies* `g10-0043`

- `g10-0053` *STATED* — Alex Chen's Claude Code mods guide ends with 'The honest notes' section (body locked).
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *qualifies* `g10-0047`
  ↳ *example-of* `g10-0270`

- `g10-0077` *STATED* — Alex Chen's login-safety guide ends with 'The honest notes' section (body locked).
  — [g-openai-agents-hacked-hugging-face-5-login-rules](https://chen.media/guides/openai-agents-hacked-hugging-face-5-login-rules)
  ↳ *qualifies* `g10-0069`
  ↳ *example-of* `g10-0270`

- `g10-0180` *STATED* — Alex Chen's effort-levels guide ends with 'The honest caveats' section (body locked).
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *qualifies* `g10-0174`
  ↳ *example-of* `g10-0270`

- `g12-0109` *STATED* — Guide section 'What it keeps' covers which instructions the prompt audit leaves in place (body email-gated).
  — [g-clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit](https://chen.media/guides/clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit)
  ↳ *part-of* `g12-0091`
  ↳ *qualifies* `g12-0110`

- `g12-0248` *STATED* — Guide section 'If you don't see the option' covers accounts that don't yet show lower-priority mode (body email-gated).
  — [g-keep-using-claude-code-after-you-hit-your-usage-limit](https://chen.media/guides/keep-using-claude-code-after-you-hit-your-usage-limit)
  ↳ *part-of* `g12-0238`

- `g13-0109` *STATED* — Alex's laptop-closed guide has a 'Good to know before you start' section of cloud session caveats.
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it)
  ↳ *qualifies* `g13-0094`

- `g14-0093` *STATED* — intent.md is a project artifact, not a magic filename that automatically launches Anthropic's SDLC pipeline.
  > “The file is a project artifact, not a magic filename that automatically launches that pipeline.”
  — [g-intent-md-claude-project-setup](https://chen.media/guides/intent-md-claude-project-setup)
  ↳ *qualifies* `g14-0087`
  ↳ *example-of* `g14-0348`

- `g15-0060` *STATED* — The verify-before-done mechanism is slow out of the box, and one tweak fixes it (locked; the lede ties the fix to running ten checks at once).
  — [g-claude-code-says-done-before-it-has-proved-anything-this-fixes-it](https://chen.media/guides/claude-code-says-done-before-it-has-proved-anything-this-fixes-it)
  ↳ *qualifies* `g15-0055`
  ↳ *leads-to* `g15-0051`

- `g16-0030` *STATED* — /design has honest limits he spells out.
  > “The honest limits”
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)
  ↳ *qualifies* `g16-0016`
  ↳ *generalizes* `g16-0031`
  ↳ *example-of* `g16-0003`

- `g16-0031` *STATED* — /design is a RESEARCH PREVIEW, not a finished feature.
  > “It is a RESEARCH PREVIEW, not a finished feature”
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)
  ↳ *qualifies* `g16-0016`

- `g16-0067` *STATED* — The memory change has a catch, and that catch is the reason the memory guide exists.
  > “The catch, and it is the reason this guide exists”
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit)

- `g16-0072` *STATED* — Claude memory will not store some things by default, and there are extra options you can turn on.
  > “What it will not store, and what you can turn on”
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit)
  ↳ *qualifies* `g16-0060`

- `g17-0257` *STATED* — Alex Chen adds a note on the three Claude courses' runtimes.
  > “A note on runtimes”
  — [g-three-free-claude-courses-and-what-to-do-with-them](https://chen.media/guides/three-free-claude-courses-and-what-to-do-with-them)
  ↳ *qualifies* `g17-0253`

- `g18-0163` *STATED* — If /plugin is not recognised, your Claude Code is too old: update it, then restart your terminal.
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *qualifies* `g18-0160`

- `g19-0040` *INFERRED* — The free part of the 50-tips guide names only three Tier 1 tip titles (/clear cold review, PreToolUse block, PostToolUse formatter); the fourth Tier 1 tip is behind the email gate.
  — [g-50-claude-tips-ranked-worst-to-best](https://chen.media/guides/50-claude-tips-ranked-worst-to-best)
  ↳ *qualifies* `g19-0042`

- `g20-0044` *STATED* — The Day 1 guide is Mac first; Windows works but has a known defect in the Obsidian bridge.
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *part-of* `g20-0034`

- `r01-0006` *CORE* — After installing a skill by copying it into ~/.claude/skills/, open a new Claude Code session so the skill is picked up.
  > “Open a new Claude Code session afterwards.”
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill) [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *example-of* `r03-0143`

- `r01-0060` *STATED* — The /agency night shift runs only while your computer is on and awake; on a Mac, run 'caffeinate -i' in another window.
  > “on a Mac, run `caffeinate -i` in another window”
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *qualifies* `r01-0048`
  ↳ *evidence-for* `r02-0037`

- `r02-0037` *STATED* — /hunter has no background program: it runs only while Claude Code is running and your computer is awake.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *qualifies* `r02-0035`
  ↳ *qualifies* `r02-0036`

- `r02-0109` *STATED* — For /hunter morning without keeping a session open, use a scheduled task in the Claude desktop app that runs `/hunter morning` at 7am on this computer in this folder, because a cloud routine cannot see the user's `.hunter/` files.
  > “a cloud routine cannot see the user's `.hunter/` files”
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *qualifies* `r02-0036` — must be a local desktop task, not cloud
  ↳ *because* `r02-0039`
  ↳ *contrast* `r02-0177` — cloud routines lack local files as sub-agents lack the chat

- `r02-0142` *STATED* — Installed as a plugin, the launch skill shows up namespaced as `/launch-skill:launch` instead of `/launch`.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0141`
  ↳ *evidence-for* `r01-0176`

- `r03-0027` *STATED* — After '/learn setup', start a new Claude Code session so the newly added hook loads.
  > “Start a new session so the hook loads.”
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *qualifies* `r03-0026`
  ↳ *example-of* `r03-0143`

- `r03-0060` *CORE* — /learn rules are instructions Claude reads at the start of every session, not hard limits: they make a repeat much less likely, not impossible.
  > “they make a repeat much less likely, not impossible”
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *qualifies* `r03-0008`
  ↳ *qualifies* `r03-0015`
  ↳ *example-of* `r03-0170`
  ↳ *qualifies* `g20-0236` — CLAUDE.md-loaded rules are instructions, not hard limits

- `r03-0061` *STATED* — The /learn hook spots corrections by their wording, so it misses some and catches some that aren't corrections.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *qualifies* `r03-0045`
  ↳ *evidence-for* `r03-0104`

- `r03-0101` *INFERRED* — Because the /learn investigator writes rules only at night, a mistake can repeat in a second session the same day; typing '/learn <lesson>' right after a correction closes that gap.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *because* `r03-0100`
  ↳ *leads-to* `r03-0029`

- `r03-0142` *STATED* — After copying /linkedin-roast into your skills folder, open a new Claude Code session so it picks the skill up.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *qualifies* `r03-0141`
  ↳ *example-of* `r03-0143`

- `r04-0042` *STATED* — Only the plugin install of /mentor includes the hook that locks code until you've answered; copying only skills/mentor into ~/.claude/skills/ gives you the questions without the lock.
  > “Copying only `skills/mentor` into `~/.claude/skills/` gives you the questions without the lock.”
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *qualifies* `r04-0039`
  ↳ *qualifies* `r04-0033`

- `r04-0060` *INFERRED* — A hook that only matches Write and Edit leaves Bash file writes (redirects, cat >) open, so a lock built that way needs a prose rule forbidding those routes too.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *because* `r04-0059`
  ↳ *qualifies* `r04-0058`
  ↳ *qualifies* `r04-0033`

- `r04-0180` *STATED* — A skill can't run /schedule for the user; the night-crew skill gives them the three lines to paste, one at a time, with the times filled in from their bedtime.
  > “You can't run `/schedule` for the user from inside this skill”
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *leads-to* `r04-0182`

- `y01-0042` *STATED* — Codex may still need your input during a goal, and a goal doesn't give it any extra access to files or accounts.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *qualifies* `y01-0038`
  ↳ *leads-to* `y01-0043` — access comes from plugins, not goals

- `y01-0057` *STATED* — Connecting an account doesn't automatically approve every possible action the agent can take with it.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *qualifies* `y01-0055`

### claim

- `g01-0016` *STATED* — /hiring-panel writes everything to a .hiring-panel folder where you run it and never touches your other files.
  — [g-find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free](https://chen.media/guides/find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free)
  ↳ *qualifies* `g01-0001`
  ↳ *example-of* `g01-0196`
  ↳ *example-of* `r02-0313`

- `g01-0123` *STATED* — CC Safety Net blocks hard resets, force pushes, risky rm -rf and reads of your secret keys.
  — [g-safety-net-stop-claude-deleting-your-files-before-the-command-runs](https://chen.media/guides/safety-net-stop-claude-deleting-your-files-before-the-command-runs)
  ↳ *defines* `g01-0122`

- `g01-0128` *STATED* — If a call is destructive, CC Safety Net stops it from ever running and Claude is told why.
  — [g-safety-net-stop-claude-deleting-your-files-before-the-command-runs](https://chen.media/guides/safety-net-stop-claude-deleting-your-files-before-the-command-runs)

- `g01-0129` *STATED* — Under CC Safety Net, safe calls such as git status run normally.
  — [g-safety-net-stop-claude-deleting-your-files-before-the-command-runs](https://chen.media/guides/safety-net-stop-claude-deleting-your-files-before-the-command-runs)
  ↳ *contrast* `g01-0128`

- `g01-0133` *STATED* — Because CC Safety Net reads what a command does, wrapping it or reordering flags doesn't get past it.
  — [g-safety-net-stop-claude-deleting-your-files-before-the-command-runs](https://chen.media/guides/safety-net-stop-claude-deleting-your-files-before-the-command-runs)
  ↳ *qualifies* `g01-0132`

- `g01-0135` *STATED* — CC Safety Net guards secrets from both the shell and Claude's own file tools.
  — [g-safety-net-stop-claude-deleting-your-files-before-the-command-runs](https://chen.media/guides/safety-net-stop-claude-deleting-your-files-before-the-command-runs)
  ↳ *qualifies* `g01-0134`

- `g02-0013` *STATED* — /hunter saves your resume, targets and sources in a .hunter folder on your computer.
  > “It saves all of it in a .hunter folder on your computer.”
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *part-of* `g02-0011`
  ↳ *example-of* `r02-0115`

- `g02-0026` *STATED* — /hunter writes everything to a .hunter folder where you run it and never touches your other files.
  > “It never touches your other files.”
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *qualifies* `g02-0013`
  ↳ *example-of* `g02-0240`
  ↳ *example-of* `r02-0313`

- `g02-0047` *STATED* — cc-stretch makes Claude's long answers 6x shorter to read.
  > “Make Claude's Long Answers 6x Shorter to Read”
  — [g-make-claude-s-long-answers-6x-shorter-to-read](https://chen.media/guides/make-claude-s-long-answers-6x-shorter-to-read)
  ↳ *part-of* `g02-0046`

- `g02-0055` *STATED* — In cc-stretch the words you already read never move when a phrase expands.
  > “The words you already read never move.”
  — [g-make-claude-s-long-answers-6x-shorter-to-read](https://chen.media/guides/make-claude-s-long-answers-6x-shorter-to-read)
  ↳ *qualifies* `g02-0050`

- `g02-0118` *STATED* — When Claude changes several files and your tests fail, a git diff only tells you what changed, not which step did it.
  > “a git diff only tells you what changed. It does not tell you which step did it.”
  — [g-rewind-claude-code-to-the-step-that-broke-your-code](https://chen.media/guides/rewind-claude-code-to-the-step-that-broke-your-code)

- `g02-0121` *STATED* — Time Machine keeps its snapshots in its own hidden git store, so nothing is written to your own .git.
  — [g-rewind-claude-code-to-the-step-that-broke-your-code](https://chen.media/guides/rewind-claude-code-to-the-step-that-broke-your-code)
  ↳ *qualifies* `g02-0120`
  ↳ *example-of* `g02-0240`
  ↳ *contrast* `g02-0026` — both avoid touching your own files/.git

- `g02-0178` *STATED* — Every new task, Claude Code starts without a picture of your project.
  > “Every new task, Claude starts without a picture of your project.”
  — [g-trail-code-stop-claude-getting-lost-in-your-code](https://chen.media/guides/trail-code-stop-claude-getting-lost-in-your-code)
  ↳ *leads-to* `g02-0179`
  ↳ *example-of* `g06-0239`

- `g02-0179` *STATED* — Without a map, Claude searches, opens a file, follows an import, backs out and tries again.
  — [g-trail-code-stop-claude-getting-lost-in-your-code](https://chen.media/guides/trail-code-stop-claude-getting-lost-in-your-code)
  ↳ *leads-to* `g02-0180`

- `g02-0200` *STATED* — Asked about scheduled tasks, Claude Code lists each task with its ID, schedule and prompt.
  — [g-find-the-claude-code-loops-that-are-quietly-eating-your-limit](https://chen.media/guides/find-the-claude-code-loops-that-are-quietly-eating-your-limit)
  ↳ *leads-to* `g02-0201`

- `g03-0018` *STATED* — Anthropic's docs say longer CLAUDE.md files use more context.
  — [g-shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit](https://chen.media/guides/shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit)
  ↳ *example-of* `g03-0007`
  ↳ *evidence-for* `g03-0017`
  ↳ *because* `g03-0020`
  ↳ *evidence-for* `g16-0011`

- `g03-0030` *STATED* — One Claude Code setting makes @ file mentions hand Claude just the file path instead of the file's content.
  — [g-stop-file-mentions-from-pasting-whole-files-into-your-claude-chat](https://chen.media/guides/stop-file-mentions-from-pasting-whole-files-into-your-claude-chat)
  ↳ *part-of* `g03-0009`
  ↳ *contrast* `g03-0029`

- `g03-0053` *STATED* — Two settings keep an unattended Claude Code run alive through busy-API errors: the retry watchdog and a cap on how long it waits.
  — [g-keep-claude-retrying-overnight-when-the-api-is-busy](https://chen.media/guides/keep-claude-retrying-overnight-when-the-api-is-busy)

- `g03-0055` *STATED* — Anthropic's docs recommend CLAUDE_CODE_RETRY_WATCHDOG for unattended sessions such as CI jobs.
  — [g-keep-claude-retrying-overnight-when-the-api-is-busy](https://chen.media/guides/keep-claude-retrying-overnight-when-the-api-is-busy)
  ↳ *example-of* `g03-0007`
  ↳ *evidence-for* `g03-0054`

- `g03-0056` *STATED* — With CLAUDE_CODE_RETRY_WATCHDOG on, Claude Code retries 429 and 529 capacity errors indefinitely instead of failing after the normal retry count.
  — [g-keep-claude-retrying-overnight-when-the-api-is-busy](https://chen.media/guides/keep-claude-retrying-overnight-when-the-api-is-busy)
  ↳ *part-of* `g03-0010`
  ↳ *contrast* `g03-0050`
  ↳ *contrast* `g03-0051`

- `g03-0081` *STATED* — One flag (--bg) starts a Claude Code session that keeps running with no terminal open.
  — [g-keep-claude-working-after-you-close-the-terminal](https://chen.media/guides/keep-claude-working-after-you-close-the-terminal)
  ↳ *part-of* `g03-0010`
  ↳ *contrast* `g03-0057` — --bg detached interactive session vs -p headless print run

- `g03-0086` *STATED* — After you close the terminal, a separate supervisor process keeps the background Claude Code session running.
  — [g-keep-claude-working-after-you-close-the-terminal](https://chen.media/guides/keep-claude-working-after-you-close-the-terminal)
  ↳ *because* `g03-0081`

- `g03-0112` *STATED* — Rewind rolls back both the chat and your code to the message before Claude went wrong.
  — [g-rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it](https://chen.media/guides/rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it)
  ↳ *qualifies* `g03-0111`

- `g03-0116` *STATED* — The rewind menu lists the prompts you sent in this session.
  — [g-rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it](https://chen.media/guides/rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it)

- `g03-0118` *STATED* — The rewind menu offers other options beyond a full rollback (locked section "Other options in the same menu").
  — [g-rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it](https://chen.media/guides/rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it)
  ↳ *part-of* `g03-0116`

- `g03-0153` *STATED* — By default Claude Code can start editing files as soon as you send a prompt.
  — [g-turn-on-plan-mode-so-claude-plans-before-it-edits](https://chen.media/guides/turn-on-plan-mode-so-claude-plans-before-it-edits)
  ↳ *leads-to* `g03-0154`
  ↳ *because* `g03-0156`

- `g03-0186` *STATED* — Security checking is also built into Claude Code itself (locked section "Also built into Claude Code").
  — [g-hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills](https://chen.media/guides/hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills)
  ↳ *contrast* `g03-0176`

- `g03-0244` *STATED* — When the web search cap is hit, Claude is told to carry on with what it already found.
  — [g-stop-claude-running-out-of-web-searches](https://chen.media/guides/stop-claude-running-out-of-web-searches)

- `g03-0248` *STATED* — Two settings change the web search limit behaviour (Step 2), and the guide's catch covers what they do not do.
  — [g-stop-claude-running-out-of-web-searches](https://chen.media/guides/stop-claude-running-out-of-web-searches)
  ↳ *example-of* `g03-0006`
  ↳ *qualifies* `g03-0241`

- `g04-0045` *STATED* — Harvey's repo CLAUDE.md turns Claude Code into a setup wizard that checks what is installed, asks for what it needs and trains Harvey on your product.
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)

- `g04-0058` *STATED* — Claude Code v2.1.295 added a hook setting that makes a hook failure block the action; it needs v2.1.295 or later.
  — [g-make-a-crashed-claude-hook-block-the-action-not-let-it-through](https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through)

- `g04-0060` *STATED* — With onFailure set to "block", a hook failure does what exit code 2 does on that hook event.
  — [g-make-a-crashed-claude-hook-block-the-action-not-let-it-through](https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through)
  ↳ *part-of* `g04-0059`
  ↳ *depends-on* `g04-0064`

- `g04-0061` *STATED* — With onFailure set to "block", a failing PreToolUse hook blocks the tool call.
  — [g-make-a-crashed-claude-hook-block-the-action-not-let-it-through](https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through)
  ↳ *example-of* `g04-0060`

- `g04-0062` *STATED* — With onFailure set to "block", a failing UserPromptSubmit hook blocks the prompt.
  — [g-make-a-crashed-claude-hook-block-the-action-not-let-it-through](https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through)
  ↳ *example-of* `g04-0060`

- `g04-0063` *STATED* — With onFailure set to "block", a failing PermissionRequest hook denies the request.
  — [g-make-a-crashed-claude-hook-block-the-action-not-let-it-through](https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through)
  ↳ *example-of* `g04-0060`

- `g04-0074` *STATED* — Claude Code records the token count of every call in its session logs, stored in ~/.claude/projects.
  — [g-tokentab-see-where-every-claude-token-goes-as-a-monthly-statement](https://chen.media/guides/tokentab-see-where-every-claude-token-goes-as-a-monthly-statement)
  ↳ *enables* `g04-0071`
  ↳ *evidence-for* `g08-0218`

- `g04-0090` *STATED* — The test-filter hook only rewrites the command when it is npm test, pytest or go test.
  — [g-the-claude-hook-that-cuts-test-output-down-to-just-the-failures](https://chen.media/guides/the-claude-hook-that-cuts-test-output-down-to-just-the-failures)
  ↳ *part-of* `g04-0089`

- `g04-0092` *STATED* — Claude never sees the test-filter hook's filter; it just sees the shorter output.
  — [g-the-claude-hook-that-cuts-test-output-down-to-just-the-failures](https://chen.media/guides/the-claude-hook-that-cuts-test-output-down-to-just-the-failures)
  ↳ *qualifies* `g04-0091`

- `g04-0205` *STATED* — The subagent compaction-size field arrived in Claude Code 2.1.296.
  — [g-make-your-claude-helper-agents-compact-their-own-chat-early](https://chen.media/guides/make-your-claude-helper-agents-compact-their-own-chat-early)
  ↳ *enables* `g04-0204`

- `g04-0250` *INFERRED* — Claude Code version timeline from Alex's guides: 2.1.295 added hook onFailure, 2.1.296 added the subagent compaction-size field, and 2.1.299 (October 14) added /usage habit warnings.
  — [g-make-a-crashed-claude-hook-block-the-action-not-let-it-through](https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through) [g-make-your-claude-helper-agents-compact-their-own-chat-early](https://chen.media/guides/make-your-claude-helper-agents-compact-their-own-chat-early) [g-the-four-habits-eating-your-claude-limit-and-the-fix-for-each](https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each)
  ↳ *generalizes* `g04-0058`
  ↳ *generalizes* `g04-0205`
  ↳ *generalizes* `g04-0001`

- `g05-0107` *STATED* — With Effortless, send prompts as usual; a bar above the prompt shows the effort it picked for each one.
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless)
  ↳ *leads-to* `g05-0106`
  ↳ *example-of* `g10-0173`

- `g05-0152` *STATED* — If Claude Code asks you to confirm a model switch, that is because the cache is still warm and you would lose it.
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)
  ↳ *qualifies* `g05-0151`

- `g05-0156` *STATED* — After the first response, /usage shows a 'Prompt cache (main)' line with your hit ratio, miss count, and whether the cache is warm right now.
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)
  ↳ *defines* `g05-0155`

- `g05-0169` *STATED* — A subagent file's effort setting overrides your session's effort level while that subagent runs.
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)
  ↳ *qualifies* `g05-0167`

- `g05-0171` *STATED* — Claude can pass an effort parameter for a single subagent run in Claude Code v2.1.292 or later.
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)
  ↳ *enables* `g05-0170`
  ↳ *example-of* `g05-0326`

- `g05-0172` *STATED* — A per-run effort parameter overrides the subagent file's effort setting.
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)
  ↳ *qualifies* `g05-0169`
  ↳ *part-of* `g05-0178`

- `g05-0326` *STATED* — Recent Claude Code subagent features are version-gated: per-run subagent effort needs v2.1.292+, /tasks effort display needs v2.1.242+.
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)

- `g06-0096` *STATED* — Claude Code has voice dictation built in: hold a key, say your prompt, let go.
  — [g-talk-to-claude-code-instead-of-typing](https://chen.media/guides/talk-to-claude-code-instead-of-typing)
  ↳ *depends-on* `g06-0099`
  ↳ *depends-on* `g06-0100`

- `g06-0097` *STATED* — Claude Code's built-in voice dictation understands coding words.
  — [g-talk-to-claude-code-instead-of-typing](https://chen.media/guides/talk-to-claude-code-instead-of-typing)
  ↳ *qualifies* `g06-0096`

- `g06-0115` *STATED* — Coucou's iPhone app lets you Allow or Deny Claude's permission requests from your phone.
  — [g-approve-claude-s-permission-requests-from-your-iphone-with-coucou](https://chen.media/guides/approve-claude-s-permission-requests-from-your-iphone-with-coucou)
  ↳ *part-of* `g06-0113`
  ↳ *evidence-for* `g09-0237`

- `g06-0116` *STATED* — With Coucou you can Allow or Deny a Claude permission request from the notification, the Lock Screen or the app.
  — [g-approve-claude-s-permission-requests-from-your-iphone-with-coucou](https://chen.media/guides/approve-claude-s-permission-requests-from-your-iphone-with-coucou)
  ↳ *qualifies* `g06-0115`

- `g06-0117` *STATED* — In Coucou, Allow needs Face ID.
  — [g-approve-claude-s-permission-requests-from-your-iphone-with-coucou](https://chen.media/guides/approve-claude-s-permission-requests-from-your-iphone-with-coucou)
  ↳ *qualifies* `g06-0115`

- `g06-0119` *STATED* — With Coucou, Claude's questions arrive as a notification with one button per choice.
  — [g-approve-claude-s-permission-requests-from-your-iphone-with-coucou](https://chen.media/guides/approve-claude-s-permission-requests-from-your-iphone-with-coucou)
  ↳ *part-of* `g06-0113`

- `g06-0150` *STATED* — When Claude hits a step only you can do, like clicking Allow in a permission dialog, it usually types "please click Allow" into a terminal you aren't looking at.
  > “it usually types "please click Allow" into a terminal you aren't looking at”
  — [g-make-claude-point-at-the-button-you-need-to-click](https://chen.media/guides/make-claude-point-at-the-button-you-need-to-click)
  ↳ *contrast* `g06-0115` — terminal nag vs phone approval
  ↳ *evidence-for* `g09-0231`

- `g06-0152` *STATED* — bigarrow draws an arrow and a sign over every window; clicks go straight through it and your keyboard focus stays where it was.
  — [g-make-claude-point-at-the-button-you-need-to-click](https://chen.media/guides/make-claude-point-at-the-button-you-need-to-click)
  ↳ *part-of* `g06-0149`

- `g06-0153` *STATED* — bigarrow never clicks, types or captures anything; it only points.
  > “It never clicks, types or captures anything. It only points.”
  — [g-make-claude-point-at-the-button-you-need-to-click](https://chen.media/guides/make-claude-point-at-the-button-you-need-to-click)
  ↳ *qualifies* `g06-0149`

- `g06-0213` *STATED* — The #3 change of the week of October 5, 2026: Claude Code 2.1.295 added hooks that fail closed.
  — [g-this-week-in-claude-ranked-by-what-it-does-for-you](https://chen.media/guides/this-week-in-claude-ranked-by-what-it-does-for-you)
  ↳ *part-of* `g06-0201`
  ↳ *qualifies* `g06-0115` — hooks gate actions like permissions do
  ↳ *evidence-for* `g04-0058`

- `g06-0214` *STATED* — The #4 change of the week of October 5, 2026: Claude Code 2.1.292 added effort per subagent run.
  — [g-this-week-in-claude-ranked-by-what-it-does-for-you](https://chen.media/guides/this-week-in-claude-ranked-by-what-it-does-for-you)
  ↳ *part-of* `g06-0201`
  ↳ *qualifies* `g06-0084` — per-subagent effort is another swarm cost lever
  ↳ *evidence-for* `g05-0171`

- `g06-0215` *STATED* — The #5 change of the week of October 5, 2026: bigarrow.
  — [g-this-week-in-claude-ranked-by-what-it-does-for-you](https://chen.media/guides/this-week-in-claude-ranked-by-what-it-does-for-you)
  ↳ *part-of* `g06-0201`
  ↳ *qualifies* `g06-0149` — same tool, ranked #5 that week

- `g06-0239` *CORE* — Every new Claude Code chat starts blank: each session begins with a fresh context window, so Claude forgets your rules, your setup and what you finished yesterday.
  — [g-give-claude-a-notebook-that-survives-every-chat-reset](https://chen.media/guides/give-claude-a-notebook-that-survives-every-chat-reset)
  ↳ *leads-to* `g06-0240`
  ↳ *evidence-for* `r03-0005`

- `g06-0240` *STATED* — Anthropic's memory docs describe two things that carry knowledge into the next Claude Code chat: a CLAUDE.md file you write, and auto memory, which are notes Claude writes itself.
  — [g-give-claude-a-notebook-that-survives-every-chat-reset](https://chen.media/guides/give-claude-a-notebook-that-survives-every-chat-reset)

- `g06-0248` *STATED* — Setting up both CLAUDE.md and auto memory takes a few minutes.
  — [g-give-claude-a-notebook-that-survives-every-chat-reset](https://chen.media/guides/give-claude-a-notebook-that-survives-every-chat-reset)
  ↳ *qualifies* `g06-0240`

- `g06-0267` *INFERRED* — Because Claude Code re-sends the whole chat with each message yet starts each new chat blank, Alex pairs context hygiene (earlier /autocompact) with CLAUDE.md, which survives both compaction and new sessions.
  — [g-make-claude-compact-earlier-the-setting-and-the-claude-md-note](https://chen.media/guides/make-claude-compact-earlier-the-setting-and-the-claude-md-note) [g-give-claude-a-notebook-that-survives-every-chat-reset](https://chen.media/guides/give-claude-a-notebook-that-survives-every-chat-reset)
  ↳ *depends-on* `g06-0061`
  ↳ *depends-on* `g06-0239`

- `g07-0013` *STATED* — After each answer, Claude Code can suggest what you'd ask next as grey text in the prompt box, based on your conversation.
  — [g-let-claude-code-write-your-next-prompt-press-tab](https://chen.media/guides/let-claude-code-write-your-next-prompt-press-tab)

- `g07-0017` *STATED* — If you start typing instead, Claude Code's grey prompt suggestion disappears.
  — [g-let-claude-code-write-your-next-prompt-press-tab](https://chen.media/guides/let-claude-code-write-your-next-prompt-press-tab)
  ↳ *part-of* `g07-0013`
  ↳ *qualifies* `g07-0013`

- `g07-0018` *STATED* — When you first open a Claude Code session, the grey example prompt comes from your project's git history.
  — [g-let-claude-code-write-your-next-prompt-press-tab](https://chen.media/guides/let-claude-code-write-your-next-prompt-press-tab)
  ↳ *part-of* `g07-0013`

- `g07-0161` *STATED* — Claude Code can now build features into itself through mods.
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`
  ↳ *part-of* `g10-0056`

- `g07-0163` *STATED* — A Claude Code mod can draw its own panel above your prompt.
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0162` — what a mod can do
  ↳ *evidence-for* `g10-0057`

- `g07-0164` *STATED* — A Claude Code mod can step in before Claude runs a command.
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0162` — what a mod can do
  ↳ *evidence-for* `g10-0058`

- `g07-0165` *STATED* — A Claude Code mod can add new commands.
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0162` — what a mod can do
  ↳ *evidence-for* `g10-0059`

- `g07-0167` *STATED* — Alex says each of Anthropic's sample mods can be tried in about two minutes.
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`

- `g07-0189` *STATED* — Claude Code Projects is for Pro and Max plans only; it isn't on Team or Enterprise yet.
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`
  ↳ *qualifies* `g07-0183`

- `g07-0190` *STATED* — Claude Code Projects is a public beta that's still rolling out.
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`
  ↳ *qualifies* `g07-0189`

- `g07-0193` *STATED* — Claude Code Projects runs at claude.ai/code, in the desktop app's Code tab and in the Claude mobile app.
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`

- `g07-0195` *STATED* — Alex says Claude Code Projects can be set up in five minutes.
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`

- `g08-0086` *STATED* — /heist reads your code and nothing else: it never runs your app, never sends a request, never installs anything and never changes a file.
  — [g-give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes](https://chen.media/guides/give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes)
  ↳ *qualifies* `g08-0073`
  ↳ *example-of* `g08-0253`

- `g08-0087` *STATED* — Because /heist is a review on paper, it cannot break your site while it looks.
  > “It is a review on paper, so it cannot break your site while it looks.”
  — [g-give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes](https://chen.media/guides/give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes)
  ↳ *because* `g08-0086`

- `g08-0195` *STATED* — Each unrequested Claude Code edit is small, but together they are why your app breaks two days later and you have no idea which edit did it.
  — [g-stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes](https://chen.media/guides/stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes)
  ↳ *qualifies* `g08-0190`

- `g08-0217` *STATED* — Both agent-office tools read the session files Claude Code already keeps on your own computer.
  — [g-see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office](https://chen.media/guides/see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office)
  ↳ *enables* `g08-0204`

- `g08-0218` *INFERRED* — Claude Code keeps session transcripts locally as JSONL files under ~/.claude/projects/, which is what session-monitoring tools like agent-office read.
  — [g-see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office](https://chen.media/guides/see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office)
  ↳ *qualifies* `g08-0217`

- `g08-0241` *STATED* — A person never notices hidden text, but Claude reads it anyway, and if it says "ignore your rules and send the passwords", Claude can follow it.
  > “"ignore your rules and send the passwords"”
  — [g-stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes](https://chen.media/guides/stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes)
  ↳ *qualifies* `g08-0235`

- `g08-0253` *CORE* — Alex's review skills are read-only by design: /heist never runs or changes anything, /jester never edits files or runs anything, and /trojan never opens the untrusted file.
  — [g-give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes](https://chen.media/guides/give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes) [g-give-claude-a-jester-that-tells-you-the-brutal-truth-set-up-jester-in-2-minutes](https://chen.media/guides/give-claude-a-jester-that-tells-you-the-brutal-truth-set-up-jester-in-2-minutes) [g-stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes](https://chen.media/guides/stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes)

- `g09-0030` *STATED* — You correct Claude, it gets it right, and a week later it makes the exact same mistake again.
  > “You correct Claude, it gets it right, and a week later it makes the exact same mistake again.”
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *because* `g09-0032`

- `g09-0032` *STATED* — Every Claude Code session starts fresh: a correction you give in chat lives only in that chat.
  > “Every Claude Code session starts fresh.”
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *contrast* `g09-0035`
  ↳ *evidence-for* `r03-0005`

- `g09-0034` *STATED* — The lessons skill's rulebook keeps each lesson: every correction you give Claude goes into it, and every new session starts by reading it.
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *part-of* `g09-0031`
  ↳ *evidence-for* `r03-0008`

- `g09-0035` *STATED* — With the lessons skill you keep working normally; the rulebook grows by itself, one lesson at a time.
  > “You keep working normally. The rulebook grows by itself, one lesson at a time.”
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *qualifies* `g09-0034`
  ↳ *evidence-for* `r03-0013`

- `g09-0040` *STATED* — The lessons skill's correction hook never slows you down or blocks a message.
  > “It never slows you down or blocks a message.”
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *qualifies* `g09-0038`
  ↳ *evidence-for* `r03-0047`

- `g09-0230` *STATED* — You give Claude Code a job, switch to something else, and every few minutes flip back to the terminal to check whether it's done or stuck.
  — [g-coucou-free-notch-pet-that-watches-claude-code](https://chen.media/guides/coucou-free-notch-pet-that-watches-claude-code)

- `g09-0231` *STATED* — Half the time Claude Code has been sitting on a permission question, waiting for you, the whole time you were gone.
  > “Half the time it's been sitting on a permission question, waiting for you, the whole time you were gone.”
  — [g-coucou-free-notch-pet-that-watches-claude-code](https://chen.media/guides/coucou-free-notch-pet-that-watches-claude-code)
  ↳ *qualifies* `g09-0230`

- `g09-0237` *STATED* — Coucou surfaces Claude Code's permission requests in the notch with Allow, Deny and Always buttons.
  — [g-coucou-free-notch-pet-that-watches-claude-code](https://chen.media/guides/coucou-free-notch-pet-that-watches-claude-code)
  ↳ *part-of* `g09-0232`
  ↳ *because* `g09-0231`

- `g09-0238` *STATED* — When Claude asks you a question, Coucou shows the choices in the notch; one click and Claude carries on.
  — [g-coucou-free-notch-pet-that-watches-claude-code](https://chen.media/guides/coucou-free-notch-pet-that-watches-claude-code)
  ↳ *part-of* `g09-0232`
  ↳ *evidence-for* `g06-0119`

- `g10-0036` *STATED* — When a Mac is deep in swap, everything slows to a crawl, and past a point the whole Mac locks up.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *because* `g10-0024`

- `g10-0040` *STATED* — Background processes started by Claude Code sessions (MCP servers, a browser tool, helper scripts) kept running after the sessions went quiet.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *part-of* `g10-0037`

- `g10-0046` *STATED* — Claude Code has mods now: Tetris above the chat box while Claude works, a pixel cat acting out whatever Claude is doing, and a pet that grows every time Claude ships.
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)

- `g10-0055` *STATED* — Within a day of the Claude Code mods announcement, people had put Tetris above the chat box, turned whatever Claude is doing into a live cartoon, and given Claude a pet that grows as it works.
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *evidence-for* `g10-0046`

- `g10-0057` *STATED* — A Claude Code mod can draw its own buttons and panels above your prompt.
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *part-of* `g10-0056`

- `g10-0058` *STATED* — A Claude Code mod can react to what Claude is doing: reading a file, editing, running a command.
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *part-of* `g10-0056`

- `g10-0059` *STATED* — A Claude Code mod can add new commands.
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *part-of* `g10-0056`

- `g10-0063` *STATED* — Claude Code mods are written in a few lines of TypeScript.
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *part-of* `g10-0056`

- `g10-0090` *STATED* — People paste API keys into notebooks, config files and datasets every day.
  — [g-openai-agents-hacked-hugging-face-5-login-rules](https://chen.media/guides/openai-agents-hacked-hugging-face-5-login-rules)
  ↳ *because* `g10-0071`

- `g10-0173` *CORE* — Claude Code has five effort levels and an ultracode switch; the one you pick decides how fast you get an answer, how hard Claude checks its own work, and how soon you hit your usage limit.
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)

- `g10-0182` *STATED* — Most people never touch Claude Code's /effort slider, and the ones who do usually crank it to max and leave it there.
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *qualifies* `g10-0181`

- `g10-0184` *STATED* — Anthropic has published exactly what each Claude Code effort level changes, with test results.
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *evidence-for* `g10-0174`

- `g10-0185` *CORE* — Effort doesn't swap the model.
  > “Effort doesn't swap the model.”
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *contrast* `g10-0186`

- `g10-0187` *STATED* — Anthropic engineer Thariq Shihipar ran the same jobs at every effort level: higher effort means more verification, more edge-case testing, and more of Claude's own judgement.
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *evidence-for* `g10-0186`

- `g10-0194` *STATED* — Low effort gives you a quick starting point while you stay in charge.
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)

- `g10-0195` *STATED* — Max effort gives you Claude's best attempt in one go, but it makes more assumptions for you and takes 45 times as long as low.
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)

- `g11-0099` *CORE* — Claude Code's /advisor lets Opus 5.5 keep doing the work while Fable 5.1 reads the whole session and steps in at the moments that matter.
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)

- `g11-0103` *STATED* — The advisor fits long jobs where most turns are routine but the plan decides the outcome: a big refactor, a bug that keeps coming back, anything you'd want checked before Claude calls it done.
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)
  ↳ *qualifies* `g11-0099`

- `g11-0106` *STATED* — Claude decides when to call the advisor; it isn't on a timer.
  > “Claude decides when; it isn't on a timer.”
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)
  ↳ *qualifies* `g11-0105`

- `g11-0109` *STATED* — Opus applies the advisor's guidance, and pushes back if a file or a failing step contradicts the advice.
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)

- `g11-0110` *STATED* — At session start with the advisor on, Claude Code shows: "Advisor Tool (experimental) is on and may use more tokens · /advisor".
  > “Advisor Tool (experimental) is on and may use more tokens · /advisor”
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)
  ↳ *evidence-for* `g11-0111`

- `g11-0112` *STATED* — During a task Claude Code shows an 'Advising' line with the advisor's name, reporting Reviewed, Declined or Unavailable.
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)
  ↳ *part-of* `g11-0099`

- `g11-0113` *STATED* — In Claude Code, Ctrl+O shows what the advisor said.
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)
  ↳ *qualifies* `g11-0112`

- `g12-0092` *STATED* — Rules written for older Claude models make Opus 5.5 slower and less accurate.
  — [g-clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit](https://chen.media/guides/clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit)
  ↳ *part-of* `g12-0091`
  ↳ *because* `g12-0094`
  ↳ *evidence-for* `g16-0011`

- `g12-0093` *STATED* — Most CLAUDE.md files are full of instructions written for older Claude models: 'double-check everything', IMPORTANT in capitals, and step-by-step scripts for things the model already knows how to do.
  — [g-clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit](https://chen.media/guides/clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit)
  ↳ *leads-to* `g12-0095`
  ↳ *evidence-for* `g16-0011`

- `g12-0207` *STATED* — In the Claude Code team's daily pattern, /code-review hunts for bugs.
  — [g-how-to-make-claude-test-its-own-work-the-verification-loop](https://chen.media/guides/how-to-make-claude-test-its-own-work-the-verification-loop)
  ↳ *part-of* `g12-0211`

- `g12-0208` *STATED* — In the Claude Code team's daily pattern, /simplify cleans up the diff.
  — [g-how-to-make-claude-test-its-own-work-the-verification-loop](https://chen.media/guides/how-to-make-claude-test-its-own-work-the-verification-loop)
  ↳ *part-of* `g12-0211`

- `g12-0209` *STATED* — In the Claude Code team's daily pattern, /verify confirms the change actually works.
  — [g-how-to-make-claude-test-its-own-work-the-verification-loop](https://chen.media/guides/how-to-make-claude-test-its-own-work-the-verification-loop)
  ↳ *part-of* `g12-0211`

- `g12-0210` *STATED* — In the Claude Code team's daily pattern, a custom /design skill checks the UI against their design guidelines.
  — [g-how-to-make-claude-test-its-own-work-the-verification-loop](https://chen.media/guides/how-to-make-claude-test-its-own-work-the-verification-loop)
  ↳ *example-of* `g12-0163`
  ↳ *part-of* `g12-0211`
  ↳ *example-of* `g12-0214`

- `g13-0003` *STATED* — In Bot Crossing, when a Claude Code session needs you, its bot stops working and holds a question mark (?) over its head; Alex calls the question mark the whole point of the game.
  > “The point is the question mark. When a session needs you, its bot stops working and holds a ? over its head.”
  — [g-watch-every-claude-code-session-as-a-bot-in-bot-crossing](https://chen.media/guides/watch-every-claude-code-session-as-a-bot-in-bot-crossing)
  ↳ *part-of* `g13-0001`
  ↳ *example-of* `y02-0189`

- `g13-0093` *CORE* — On September 23, 2026 Anthropic moved Claude Code cloud sessions out of research preview.
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it) [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)

- `g13-0096` *CORE* — A Claude Code cloud session keeps going when you close your laptop, because it lives on Anthropic's machine.
  > “The part that matters is that it keeps going when you close your laptop.”
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it) [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)
  ↳ *because* `g13-0094`
  ↳ *contrast* `r02-0037`

- `g13-0097` *STATED* — With a cloud session you can start a task, shut the lid, and review the result later, even from your phone.
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it)
  ↳ *example-of* `g13-0096`

- `g13-0122` *STATED* — Normally Claude can't open a video link.
  — [g-let-claude-code-watch-any-video-with-watch](https://chen.media/guides/let-claude-code-watch-any-video-with-watch)
  ↳ *contrast* `g13-0119` — the gap /watch fills
  ↳ *contrast* `y04-0027`

- `g13-0134` *STATED* — Every time you start a new Claude Code session, Claude forgets everything from earlier sessions.
  > “Every time you start a new Claude Code session, Claude forgets everything.”
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *evidence-for* `g06-0239`
  ↳ *contradicts* `g06-0242` — 'every new session Claude forgets everything from earlier sessions' vs Anthropic's auto memory: notes Claude writes itself that load at the start of every session

- `g13-0142` *STATED* — claude-mem remembers your past sessions, so you stop re-explaining your project.
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *because* `g13-0141`
  ↳ *evidence-for* `g17-0098`

- `g13-0184` *STATED* — Alex's JEV guide has the 2 workflows from the video plus 18 more (20 total), each with a prompt to paste into Claude Code.
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *part-of* `g13-0169`

- `g14-0006` *STATED* — In Claude Code, actual subagents can have separate context windows and defined tool access.
  — [g-marketing-agent-workflow-setup](https://chen.media/guides/marketing-agent-workflow-setup)
  ↳ *contrast* `g14-0005` — real subagents vs. named stages
  ↳ *contrast* `g14-0242` — subagents vs multi-provider council
  ↳ *evidence-for* `g19-0067`

- `g14-0299` *STATED* — Slash commands go inside Claude Code; commands beginning with npx or npm go in a terminal.
  > “Slash commands go inside Claude Code; commands beginning with npx or npm go in a terminal.”
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *qualifies* `g14-0298`

- `g15-0026` *STATED* — On Opus 5 adaptive thinking is on by default: leave the thinking setting out of a request and it thinks anyway.
  — [g-10-claude-mistakes-pro-users-are-still-making-and-the-fix-for-each](https://chen.media/guides/10-claude-mistakes-pro-users-are-still-making-and-the-fix-for-each)
  ↳ *part-of* `g15-0025`

- `g15-0133` *STATED* — Three rules make Anthropic's 52 Claude Code prompts work: a slash command is a skill; plan before it writes anything; CLAUDE.md, so it stops asking.
  — [g-the-official-claude-code-prompt-library-52-free-prompts](https://chen.media/guides/the-official-claude-code-prompt-library-52-free-prompts)
  ↳ *qualifies* `g15-0122`

- `g15-0134` *STATED* — In Claude Code a slash command is a skill (rule one).
  — [g-the-official-claude-code-prompt-library-52-free-prompts](https://chen.media/guides/the-official-claude-code-prompt-library-52-free-prompts)
  ↳ *part-of* `g15-0133`
  ↳ *qualifies* `g15-0044` — slash command = skill = a folder with SKILL.md
  ↳ *evidence-for* `g21-0216`

- `g16-0011` *CORE* — A CLAUDE.md written for a weaker or older model makes Claude worse on current models; he lists it as a token mistake (#6) and devotes a whole audit guide to it, even while shipping a prompt to create your CLAUDE.md.
  — [g-15-claude-mistakes-that-are-quietly-costing-you-tokens](https://chen.media/guides/15-claude-mistakes-that-are-quietly-costing-you-tokens) [g-why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it](https://chen.media/guides/why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it) [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)

- `g16-0017` *STATED* — /design does not describe a design or paste a wall of CSS; it publishes an actual canvas you can edit.
  > “Not describe one, not paste a wall of CSS, but publish a canvas of editable artboards for your UI and print you the link to it.”
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)
  ↳ *qualifies* `g16-0016`

- `g16-0028` *STATED* — There are specific limits on what you can actually change on the /design canvas.
  > “What you can actually change on the canvas”
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)
  ↳ *qualifies* `g16-0027`

- `g16-0033` *STATED* — /design is available on Pro, Max, Team and Enterprise plans, and not on the free plan.
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)

- `g16-0034` *STATED* — /design runs in the Claude Code CLI and in Claude Code Desktop.
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)
  ↳ *qualifies* `g16-0016`

- `g16-0035` *STATED* — /design is built on artifacts.
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)
  ↳ *depends-on* `y01-0152`

- `g16-0056` *STATED* — On August 25, 2026 Anthropic changed how Claude's memory works.
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit)
  ↳ *leads-to* `g16-0060`

- `g16-0058` *STATED* — Claude's memory used to be a single rolling summary: Claude finished a conversation, wrote a paragraph about you, and that paragraph was the memory.
  > “Memory used to be a single rolling summary.”
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit)
  ↳ *contrast* `g16-0060`

- `g16-0059` *STATED* — The old summary memory could not be seen inside, could not be corrected, and was written after the fact.
  > “You could not see inside it, you could not correct it, and it was written after the fact.”
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit)
  ↳ *qualifies* `g16-0058`

- `g16-0061` *STATED* — Claude now adds to its memory files during the conversation, while you are still talking, rather than summarising once you are done.
  > “Written during the conversation, not after it”
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit)
  ↳ *contrast* `g16-0059`

- `g16-0064` *STATED* — File-based memory is on by default on Free, Pro and Max plans, across web, desktop and mobile.
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit)
  ↳ *qualifies* `g16-0060`

- `g16-0065` *STATED* — Claude chat and Claude Cowork now share the same memory.
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit)
  ↳ *qualifies* `g16-0060`

- `g16-0068` *STATED* — There is a part of the new memory almost nobody will use, and it is the reason the change matters.
  > “The part almost nobody will use, and the reason this matters”
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit)
  ↳ *qualifies* `g16-0062` — inferred: the editable files are the part few will use

- `g16-0169` *STATED* — Most people are using Claude at a fraction of what it does.
  > “Most people are using Claude at a fraction of what it does.”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *because* `g16-0170`

- `g16-0170` *STATED* — The gap is not bad prompting: the things that matter most are configuration decisions, and nobody walks you through configuration.
  > “the things that matter most are configuration decisions, and nobody walks you through configuration”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)

- `g16-0191` *STATED* — His tips guide closes with a part about Claude configuration that nobody mentions.
  > “The part nobody mentions”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *qualifies* `g16-0170`

- `g16-0256` *STATED* — The CLAUDE.md and skills you wrote last year are now slowing Claude down.
  > “Why the CLAUDE.md and skills you wrote last year are now slowing Claude down”
  — [g-why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it](https://chen.media/guides/why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it)
  ↳ *example-of* `g16-0001`
  ↳ *evidence-for* `g16-0011`

- `g16-0260` *STATED* — Anthropic's explanation was that they had been over-constraining Claude Code, through the system prompt and through their own CLAUDE.md files and skills.
  > “over-constraining”
  — [g-why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it](https://chen.media/guides/why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it)

- `g16-0262` *STATED* — Your Claude setup has the same over-constraining problem, for the same reason.
  > “Your setup has the same problem for the same reason.”
  — [g-why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it](https://chen.media/guides/why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it)
  ↳ *depends-on* `g16-0260`
  ↳ *because* `g16-0263`

- `g16-0263` *STATED* — Every rule you wrote was written for a model that needed it, and most were written for models that are two generations old.
  — [g-why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it](https://chen.media/guides/why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it)
  ↳ *leads-to* `g16-0264`
  ↳ *evidence-for* `g16-0011`
  ↳ *evidence-for* `g18-0231`

- `g16-0267` *STATED* — An outdated CLAUDE.md shows three symptoms, and they all come from the same place.
  > “The three symptoms, and why they all come from the same place”
  — [g-why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it](https://chen.media/guides/why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it)
  ↳ *qualifies* `g16-0256`

- `g16-0288` *STATED* — The three walls every Claude Code user hits: you do not know what to configure, you run out of usage, and you lose everything between sessions.
  > “You do not know what to configure. You run out of usage. You lose everything between sessions.”
  — [g-three-plugins-that-fix-claude-code-s-setup-limits-and-memory](https://chen.media/guides/three-plugins-that-fix-claude-code-s-setup-limits-and-memory)
  ↳ *defines* `g16-0287`
  ↳ *qualifies* `g16-0012`

- `g17-0251` *STATED* — Alex Chen's three recommended free Claude courses are the exception: each one ends with you having built something.
  > “each one ends with you having built something”
  — [g-three-free-claude-courses-and-what-to-do-with-them](https://chen.media/guides/three-free-claude-courses-and-what-to-do-with-them)
  ↳ *contrast* `g17-0250`

- `g17-0252` *STATED* — The three Claude courses are genuinely free on YouTube, with no email gate and no upsell to watch them.
  > “no email gate and no upsell”
  — [g-three-free-claude-courses-and-what-to-do-with-them](https://chen.media/guides/three-free-claude-courses-and-what-to-do-with-them)
  ↳ *qualifies* `g17-0251`

- `g17-0272` *STATED* — Open Generative AI's 400+ image and video models can be driven from Claude Code.
  > “and how to drive them from Claude Code”
  — [g-400-ai-image-and-video-models-in-one-free-desktop-app](https://chen.media/guides/400-ai-image-and-video-models-in-one-free-desktop-app)
  ↳ *qualifies* `g17-0268`

- `g18-0064` *STATED* — Everything in the Karpathy file is public; the only thing that makes it work is WHERE you put it.
  > “The only thing that makes it work is WHERE you put it”
  — [g-the-20-kb-file-that-stops-claude-doing-four-dumb-things](https://chen.media/guides/the-20-kb-file-that-stops-claude-doing-four-dumb-things)

- `g18-0109` *STATED* — Out of the box Claude can read your files and run your commands.
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again)

- `g18-0227` *STATED* — None of Boris Cherny's three Claude Code fixes are settings; all three are about how you set the job up before the model ever runs.
  — [g-three-things-almost-everyone-gets-wrong-about-claude-code](https://chen.media/guides/three-things-almost-everyone-gets-wrong-about-claude-code)
  ↳ *part-of* `g18-0226`
  ↳ *generalizes* `g18-0228`

- `g18-0231` *STATED* — Most instruction lines were written to babysit a weaker model, and that model is gone.
  > “Most lines were written to babysit a weaker model, and that model is gone.”
  — [g-three-things-almost-everyone-gets-wrong-about-claude-code](https://chen.media/guides/three-things-almost-everyone-gets-wrong-about-claude-code)

- `g18-0238` *STATED* — If your CLAUDE.md is longer than one screen, you are probably describing the model instead of your project.
  — [g-three-things-almost-everyone-gets-wrong-about-claude-code](https://chen.media/guides/three-things-almost-everyone-gets-wrong-about-claude-code)
  ↳ *qualifies* `g18-0237`

- `g18-0241` *STATED* — Boris Cherny, lead engineer on Claude Code at Anthropic, said on stage at Y Combinator: delete your CLAUDE.md every six months and watch what the model does on its own.
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *because* `g18-0243`
  ↳ *because* `g18-0244`
  ↳ *evidence-for* `g18-0284`
  ↳ *evidence-for* `g18-0228` — same Boris Cherny, on stage at Y Combinator

- `g18-0243` *STATED* — Almost every CLAUDE.md rule you saved was written for a model that needed the handholding; Opus 5 does not.
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *evidence-for* `g18-0231`

- `g19-0039` *CORE* — A PreToolUse hook is Alex's 'what can physically stop a bad action' lever: unlike an instruction in a prompt, it blocks the tool call itself before it runs.
  — [g-50-claude-tips-ranked-worst-to-best](https://chen.media/guides/50-claude-tips-ranked-worst-to-best)
  ↳ *qualifies* `g19-0025`
  ↳ *part-of* `g19-0038`
  ↳ *generalizes* `g01-0126`
  ↳ *evidence-for* `g08-0202`

- `g19-0066` *STATED* — The seven-station line is not a trick prompt; it is built on Claude Code's built-in subagents feature.
  > “This is not a trick prompt.”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *part-of* `g19-0060`
  ↳ *depends-on* `g19-0067`

- `g19-0069` *STATED* — Project subagents live in .claude/agents/ inside your repo, so they are version controlled and shared with your team.
  > “Project subagents live in .claude/agents/ inside your repo”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *qualifies* `g19-0068`
  ↳ *contrast* `g19-0070` — project vs user scope
  ↳ *evidence-for* `g03-0222`

- `g19-0070` *STATED* — User subagents live in ~/.claude/agents/, so they follow you into every project.
  > “User subagents live in ~/.claude/agents/”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *qualifies* `g19-0068`
  ↳ *evidence-for* `g03-0222`

- `g19-0186` *STATED* — Serena makes edits safer: renaming a symbol goes through the language-server refactor instead of a hopeful find and replace.
  > “Renaming a symbol goes through the language server refactor instead of a hopeful find and replace.”
  — [g-give-claude-code-an-ide-brain-so-it-stops-reading-everything](https://chen.media/guides/give-claude-code-an-ide-brain-so-it-stops-reading-everything)
  ↳ *depends-on* `g19-0182` — rename_symbol

- `g19-0248` *STATED* — The 45-second video advised pointing Claude at r/smallbusiness and named G2 and Capterra together as review sources.
  > “"Point Claude at r/smallbusiness"”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)

- `g19-0250` *STATED* — Reddit's robots.txt blocks every crawler.
  > “Reddit's robots.txt blocks every crawler”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *because* `g19-0249`

- `g19-0251` *STATED* — Anthropic's crawlers obey robots.txt.
  > “Anthropic's crawlers obey it”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *because* `g19-0249`

- `g19-0252` *STATED* — Claude's web search returns a hard error naming reddit.com as inaccessible.
  > “Claude's web search returns a hard error naming reddit.com as inaccessible”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *evidence-for* `g19-0249`
  ↳ *analogy-for* `g19-0128` — respect crawl/terms limits

- `g19-0256` *STATED* — G2 blocks Claude.
  > “G2 blocks Claude.”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *part-of* `g19-0258`

- `g19-0257` *STATED* — Capterra does not block Claude, for now.
  > “Capterra does not, for now.”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *part-of* `g19-0258`

- `g20-0035` *STATED* — Connecting a local Obsidian vault requires the Claude Desktop app, not claude.ai in a browser.
  > “You need Claude Desktop, not claude.ai in a browser.”
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *part-of* `g20-0034`

- `g20-0143` *STATED* — Alex's memory system is all plain text files you own, so it works in Claude Code, the desktop app or the API, with nothing to install and nothing to pay for.
  > “Nothing to install and nothing to pay for.”
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0141`
  ↳ *qualifies* `g20-0236`

- `g20-0144` *CORE* — A chat model starts every session at zero: it has no idea what your stack is, how you like things written, or that it broke the build doing this exact thing last Tuesday.
  > “A chat model starts every session at zero.”
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *leads-to* `g20-0145`
  ↳ *because* `g20-0147`
  ↳ *generalizes* `g20-0225`
  ↳ *evidence-for* `g06-0239`

- `g20-0145` *STATED* — Because each session starts at zero, you re-explain your context every time.
  > “So you re-explain, every time.”
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *leads-to* `g20-0146`

- `g20-0159` *STATED* — Everything else in the memory guide is worthless without a file the model actually reads first.
  > “Everything else in this guide is worthless without a file the model actually reads first.”
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *because* `g20-0148`

- `g20-0160` *STATED* — The memory instruction that matters is the one that forbids re-asking; that single line turns a chat into something that remembers you.
  > “That single line is what turns a chat into something that remembers you.”
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *qualifies* `g20-0153`

- `g20-0224` *CORE* — The model is not the bottleneck; the setup around it is.
  > “The model is not the bottleneck”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *part-of* `g20-0222`
  ↳ *evidence-for* `g16-0170`

- `g20-0225` *STATED* — Out of the box, Claude forgets everything when you close the chat.
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *evidence-for* `g20-0224`
  ↳ *contradicts* `g16-0064` — 'out of the box Claude forgets everything when you close the chat' vs file-based memory on by default on Free, Pro and Max

- `g20-0228` *STATED* — Fix forgetting, missing tools and working alone, and the same Claude model starts behaving like a version that is not released.
  > “Fix those three things and the same model starts behaving like a version that is not released.”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *qualifies* `g20-0224`

- `g20-0236` *CORE* — Claude Code reads a file called CLAUDE.md at the start of every session; anything in it is loaded automatically, forever.
  > “Anything in it is loaded automatically, forever.”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *defines* `g20-0231`
  ↳ *evidence-for* `g06-0241`

- `g20-0237` *STATED* — With CLAUDE.md your project, preferences and standards stop being something you re-explain every single chat.
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *because* `g20-0236`

- `g20-0253` *STATED* — Every other Claude Code upgrade gets better when Claude already knows your context.
  > “Every other upgrade gets better when Claude already knows your context.”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *because* `g20-0229`

- `g20-0254` *STATED* — Memory is the cheapest permanent upgrade you can give Claude, taking about ten minutes once.
  > “Memory is the cheapest permanent upgrade you can give it”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *qualifies* `g20-0231`

- `g21-0005` *STATED* — With the right skills installed, Claude Code behaves less like autocomplete and more like a senior teammate.
  > “so it behaves less like autocomplete and more like a senior teammate”
  — [g-five-claude-code-skills-with-the-install-command-for-each](https://chen.media/guides/five-claude-code-skills-with-the-install-command-for-each)

- `g21-0161` *STATED* — Fable 5 is powerful but behaves differently from older models in three ways that need fixing.
  — [g-the-fable-5-guide-effort-memory-and-self-verification](https://chen.media/guides/the-fable-5-guide-effort-memory-and-self-verification)
  ↳ *part-of* `g21-0159`

- `g21-0164` *STATED* — Alex's four Fable 5 fixes are the fastest way to fix literal-following, token overspend and false 'done' reports, each with a copy-paste block.
  — [g-the-fable-5-guide-effort-memory-and-self-verification](https://chen.media/guides/the-fable-5-guide-effort-memory-and-self-verification)
  ↳ *part-of* `g21-0159`

- `g21-0213` *STATED* — You install the five content skills once; after that you type a slash command and the right specialist shows up.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *part-of* `g21-0210`
  ↳ *leads-to* `g21-0214`

- `g22-0119` *STATED* — In Claude, the OneShot result comes back as an Artifact you can open full-screen and publish to a share link.
  — [g-five-claude-skills-that-feel-like-cheating](https://chen.media/guides/five-claude-skills-that-feel-like-cheating)
  ↳ *part-of* `g22-0109`
  ↳ *evidence-for* `y01-0157`

- `g22-0136` *STATED* — Run the brand studio in Claude, or in Claude Code if you want it to write real SVG / HTML files you can open.
  — [g-turn-claude-into-a-full-brand-studio-free](https://chen.media/guides/turn-claude-into-a-full-brand-studio-free)
  ↳ *part-of* `g22-0126`

- `g22-0170` *CORE* — Prompts reset every new chat, so you keep re-explaining who you are; the four voice files do not reset.
  > “Prompts reset every new chat, so you keep re-explaining who you are. These four files do not.”
  — [g-the-four-files-that-make-claude-sound-like-you](https://chen.media/guides/the-four-files-that-make-claude-sound-like-you)
  ↳ *because* `g22-0163`
  ↳ *evidence-for* `g06-0239`

- `g22-0172` *STATED* — In a project with the four files, Claude reads all four before it writes a single line, on every reply.
  — [g-the-four-files-that-make-claude-sound-like-you](https://chen.media/guides/the-four-files-that-make-claude-sound-like-you)

- `g22-0221` *STATED* — The Claude Wrapped opens right inside Claude in the Artifact panel.
  — [g-build-your-own-claude-wrapped-from-your-real-stats](https://chen.media/guides/build-your-own-claude-wrapped-from-your-real-stats)
  ↳ *part-of* `g22-0219`
  ↳ *example-of* `g22-0119` — both are Claude Artifacts
  ↳ *example-of* `y01-0152`

- `g22-0241` *STATED* — The camera-roll setup turns the whole screenshot pile into a second brain you can ask in plain English.
  — [g-turn-your-camera-roll-into-something-you-can-search](https://chen.media/guides/turn-your-camera-roll-into-something-you-can-search)
  ↳ *part-of* `g22-0239`

- `g22-0242` *STATED* — The camera-roll brain reads what is actually inside every image (receipts, whiteboards, even handwriting), so it finds things by what is in the picture, not the file name.
  — [g-turn-your-camera-roll-into-something-you-can-search](https://chen.media/guides/turn-your-camera-roll-into-something-you-can-search)
  ↳ *enables* `g22-0241`
  ↳ *generalizes* `g22-0250`

- `g22-0245` *STATED* — Every new screenshot you add drops into the same Claude Project brain, so it only gets smarter.
  — [g-turn-your-camera-roll-into-something-you-can-search](https://chen.media/guides/turn-your-camera-roll-into-something-you-can-search)
  ↳ *qualifies* `g22-0243`

- `g22-0250` *STATED* — Bonus: the camera-roll brain reads your handwriting, so a handwritten sticky note becomes searchable.
  — [g-turn-your-camera-roll-into-something-you-can-search](https://chen.media/guides/turn-your-camera-roll-into-something-you-can-search)
  ↳ *part-of* `g22-0239`

- `g23-0034` *STATED* — The same Forge Loop words work in both Claude app Project Instructions and Claude Code's CLAUDE.md.
  > “Same words work in both.”
  — [g-make-claude-grade-and-fix-its-own-work](https://chen.media/guides/make-claude-grade-and-fix-its-own-work)
  ↳ *qualifies* `g23-0032`
  ↳ *qualifies* `g23-0033`
  ↳ *example-of* `g23-0199`

- `g23-0068` *STATED* — Why Claude Code wins Building apps in his tier list: Claude Code builds, debugs, and ships whole features from one prompt in your own repo.
  — [g-the-2026-ai-tool-tier-list-with-the-reason-for-each-pick](https://chen.media/guides/the-2026-ai-tool-tier-list-with-the-reason-for-each-pick)

- `r01-0176` *STATED* — Installed as a plugin, /court shows up namespaced as /court-skill:court instead of /court.
  > “Installed as a plugin, it shows up as `/court-skill:court`.”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *qualifies* `r01-0175`

- `r01-0214` *STATED* — In the default permission mode, every file a sub-agent writes into .court/ needs one approval.
  > “In the default permission mode that is one approval per file.”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *leads-to* `r01-0185`

- `r01-0216` *CORE* — Sub-agents cannot see the main conversation: the prosecutor, defense, every juror and the judge know only what is in the case file.
  > “Sub-agents cannot see this conversation.”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *because* `r01-0217`
  ↳ *evidence-for* `r02-0177`
  ↳ *evidence-for* `g19-0067`

- `r01-0226` *STATED* — The Agent tool is called Task in older Claude Code versions.
  > “the Agent tool is called Task in older Claude Code versions”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *qualifies* `r01-0225`

- `r02-0137` *STATED* — Everything /launch writes goes inside `.launch/` in your project.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0313`

- `r02-0190` *STATED* — The Agent tool is called Task in older Claude Code versions.
  > “the Agent tool is called Task in older Claude Code versions”
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0189`
  ↳ *evidence-for* `r01-0226`

- `r03-0005` *CORE* — Every Claude Code session starts fresh, so a correction typed into chat is lost once that session ends: it only lived in that day's chat.
  > “Every Claude Code session starts fresh.”
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)

- `r03-0011` *CORE* — In /learn a mistake that comes back doesn't get a second rule: the old rule gets sharper.
  > “A mistake that comes back doesn't get a second rule: the old rule gets sharper.”
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0010`

- `r03-0013` *STATED* — With /learn the rulebook grows by itself, one lesson at a time, with no manual step from the user.
  > “The rulebook grows by itself, one lesson at a time.”
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)

- `r03-0026` *STATED* — '/learn setup' adds the hook to .claude/settings.json (merged in, your other settings stay), creates LESSONS.md, adds @LESSONS.md to CLAUDE.md, and keeps .learn/ out of git.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)

- `r03-0039` *CORE* — Claude Code's '--permission-mode dontAsk' refuses any tool call not on the '--allowedTools' list, so a headless night run allowed only the learn.py script plus Edit(./LESSONS.md) and Edit(./.learn/**) can't edit your code.
  > “dontAsk refuses anything not on that list, so the night run can't edit your code.”
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *enables* `r03-0018`
  ↳ *part-of* `r03-0038`
  ↳ *example-of* `g10-0072`

- `r03-0047` *STATED* — The /learn UserPromptSubmit hook prints nothing and never blocks a prompt.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *qualifies* `r03-0045`

- `r03-0048` *STATED* — 'learn.py add' never takes the same lesson twice: a new rule that repeats an old one is merged into it, and the count goes up.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *enables* `r03-0011`

- `r03-0050` *STATED* — Past 40 rules, the /learn investigator has to merge or drop a rule before it can add a new one.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *because* `r03-0049`

- `r03-0069` *STATED* — 'learn.py setup' always runs from the skill's own folder, because it copies the script into the project.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *qualifies* `r03-0067`

- `r03-0074` *STATED* — 'learn.py setup' copies learn.py to .claude/hooks/, adds a UserPromptSubmit hook to .claude/settings.json (merged in, nothing else touched), creates LESSONS.md, and adds @LESSONS.md to CLAUDE.md and .learn/ to .gitignore.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0026`
  ↳ *defines* `r03-0028`

- `r03-0105` *STATED* — The demo rulebook was built by running the real 'learn.py add' and 'merge' commands on the demo inbox in the order the note lists them; the transcripts the inbox points at are not included.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0098`

- `r03-0143` *CORE* — Both of Alex's skill READMEs say to open a new Claude Code session after installing a skill or adding a hook, so Claude Code picks it up.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill) [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *generalizes* `g03-0003`

- `r04-0033` *STATED* — /mentor actually forces the learning: a hook blocks Claude's Write and Edit tools until all three answers are in.
  > “It actually forces it. A hook blocks Claude's Write and Edit tools until all three answers are in.”
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *example-of* `r04-0019`
  ↳ *enables* `r04-0026` — it actually forces it
  ↳ *leads-to* `r04-0034`

- `r04-0041` *STATED* — Installed as a plugin, /mentor shows up namespaced as /mentor-skill:mentor.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *evidence-for* `r01-0176`

- `r04-0058` *STATED* — While a /mentor session is on, the plugin's hook blocks Write and Edit outside .mentor/ until the current feature is unlocked, on purpose.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *defines* `r04-0033`

- `r04-0100` *STATED* — /schedule needs Claude Code signed in with your claude.ai account.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *qualifies* `r04-0179`

- `y01-0041` *STATED* — An active Codex goal has controls for pausing, resuming, or changing it.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *part-of* `y01-0038`

- `y01-0055` *STATED* — Because Codex can take actions, it has permission settings that control what it can access and when it needs your approval.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *qualifies* `y01-0049`

- `y01-0063` *STATED* — Rules in AGENTS.md stay in the project, so you don't need to paste them into every new chat there.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *analogy-for* `g20-0237`
  ↳ *part-of* `y01-0061`

- `y01-0151` *STATED* — Before Artifacts, Claude would spit out a massive block of code you had to copy, open in a coding app, and figure out how to host.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *contrast* `y01-0152`

- `y01-0154` *STATED* — An Artifact is immediately testable: you can hover over the charts, click the buttons and test the UI.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *part-of* `y01-0153`

- `y01-0157` *STATED* — You can publish Claude Artifacts as public web links that anyone can view without an account.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *part-of* `y01-0152`

- `y01-0158` *STATED* — Alex: the real power of Claude unlocks when you make it remember your voice and data across every conversation.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *leads-to* `y01-0161`

- `y01-0160` *STATED* — Alex claims that in a standard chat window Claude 'meshes' your information with all of your other chats, and that project folders are the solution.
  > “If you use a standard chat window, Claude meshes your information with all of the other chats.”
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *contradicts* `g16-0177` — 'project folders are the solution' (YouTube) vs Tip 2: 'do not work inside Projects by default' (guide)
  ↳ *leads-to* `y01-0161`

- `y01-0165` *STATED* — Anyone on your team can open a shared Claude Project and generate content; Claude pulls from the exact uploaded documents, so you never have to train it twice.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *depends-on* `y01-0163`

- `y01-0166` *STATED* — Dragging and dropping documents into Projects is slow - you shouldn't have to download and re-upload every new client document.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *leads-to* `y01-0168`

- `y01-0167` *STATED* — Your most important files are scattered across apps like Google Drive, Gmail and Notion rather than sitting on your desktop.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)

- `y02-0051` *STATED* — Without a needs-you alert you might doomscroll for 2 hours before realising Claude was actually done an hour ago.
  > “you won't doomscroll for 2 hours realizing that Claude was actually done an hour ago”
  — [qPP2IR9Dw3E](https://youtu.be/qPP2IR9Dw3E)
  ↳ *evidence-for* `g09-0231`
  ↳ *analogy-for* `y02-0143` — same wasted-attention problem

- `y02-0087` *STATED* — Most people don't realise you can build a self-improving system with Claude that runs on its own.
  — [3je0se5Ce_w](https://youtu.be/3je0se5Ce_w)
  ↳ *generalizes* `y02-0086`

- `y02-0090` *STATED* — With the self-improving system your Claude results get way better every day you run it.
  — [h0rtiWN_oIg](https://youtu.be/h0rtiWN_oIg) [3je0se5Ce_w](https://youtu.be/3je0se5Ce_w)
  ↳ *evidence-for* `r03-0013`
  ↳ *part-of* `y02-0086`

- `y02-0092` *STATED* — Claude dropped a massive update to Projects: one main chat now runs a whole team of Claudes.
  > “Claude just dropped a massive update to projects”
  — [GF2xgaEnQ0o](https://youtu.be/GF2xgaEnQ0o) [g6ZnVE4kQCk](https://youtu.be/g6ZnVE4kQCk)

- `y02-0093` *STATED* — With the Projects update, instead of chatting in multiple separate chats you get one main chat running a whole team of Claudes.
  — [g6ZnVE4kQCk](https://youtu.be/g6ZnVE4kQCk)
  ↳ *defines* `y02-0092`

- `y02-0096` *STATED* — All chats inside one Claude Project share one memory, so you never have to re-explain your project over and over again.
  > “all of your chats inside one project share one memory”
  — [GF2xgaEnQ0o](https://youtu.be/GF2xgaEnQ0o) [g6ZnVE4kQCk](https://youtu.be/g6ZnVE4kQCk)
  ↳ *evidence-for* `g17-0019`
  ↳ *part-of* `y02-0092`

- `y02-0113` *STATED* — To prevent reasoning distillation, Anthropic now only shows a summary of Claude's thought process (summarised thinking), not the raw reasoning.
  > “anthropic only shows a summary of its thought process now”
  — [8sMbmFkA5NE](https://youtu.be/8sMbmFkA5NE)

- `y02-0143` *STATED* — Without a watcher you keep flipping back to your terminal just to see if Claude is done.
  — [4iwKLOxgvZQ](https://youtu.be/4iwKLOxgvZQ) [DIJprXkxmIs](https://youtu.be/DIJprXkxmIs)
  ↳ *evidence-for* `g09-0230`
  ↳ *because* `y02-0142`

- `y02-0189` *INFERRED* — Agent Office and Cuckoo solve the same problem — not knowing when a Claude session is done or needs your input — via a red-light/alarm/banner (Agent Office) or a Mac-notch pet with one-tap 'yes' (Cuckoo).
  — [qPP2IR9Dw3E](https://youtu.be/qPP2IR9Dw3E) [4iwKLOxgvZQ](https://youtu.be/4iwKLOxgvZQ) [DIJprXkxmIs](https://youtu.be/DIJprXkxmIs)
  ↳ *evidence-for* `g06-0113`
  ↳ *generalizes* `y02-0047`
  ↳ *generalizes* `y02-0142`

- `y02-0192` *INFERRED* — Both the self-improving system's nightly investigator and the night crew use overnight Claude runs, so idle sleeping hours become review or build time.
  — [h0rtiWN_oIg](https://youtu.be/h0rtiWN_oIg) [3je0se5Ce_w](https://youtu.be/3je0se5Ce_w) [8Yo0i9jLCzY](https://youtu.be/8Yo0i9jLCzY)
  ↳ *generalizes* `r01-0035`
  ↳ *generalizes* `y02-0089`
  ↳ *generalizes* `y02-0157`

- `y03-0037` *STATED* — Low effort is what Claude's own team builds almost everything on.
  > “This is low, which Claude's own team builds almost everything on.”
  — [ItG-vSZFWgA](https://youtu.be/ItG-vSZFWgA) [mVKBGZNsSa4](https://youtu.be/mVKBGZNsSa4) [HTu9VPLvcP0](https://youtu.be/HTu9VPLvcP0)
  ↳ *evidence-for* `g10-0194`
  ↳ *part-of* `y03-0035`
  ↳ *contrast* `y03-0038` — team builds on low although medium is the default
  ↳ *evidence-for* `y03-0045`

- `y03-0038` *STATED* — Medium is the default effort level you're on unless you changed it.
  — [ItG-vSZFWgA](https://youtu.be/ItG-vSZFWgA) [mVKBGZNsSa4](https://youtu.be/mVKBGZNsSa4) [HTu9VPLvcP0](https://youtu.be/HTu9VPLvcP0)
  ↳ *part-of* `y03-0035`

- `y03-0039` *STATED* — High effort is what Claude's team only uses to test the work Claude does.
  — [ItG-vSZFWgA](https://youtu.be/ItG-vSZFWgA) [mVKBGZNsSa4](https://youtu.be/mVKBGZNsSa4) [HTu9VPLvcP0](https://youtu.be/HTu9VPLvcP0)
  ↳ *evidence-for* `g10-0178`
  ↳ *part-of* `y03-0035`
  ↳ *evidence-for* `y03-0045`

- `y03-0040` *STATED* — On extra high (xhigh) effort, Claude tries to break what it built to make the result much better.
  — [ItG-vSZFWgA](https://youtu.be/ItG-vSZFWgA) [mVKBGZNsSa4](https://youtu.be/mVKBGZNsSa4) [HTu9VPLvcP0](https://youtu.be/HTu9VPLvcP0)
  ↳ *evidence-for* `g10-0187`
  ↳ *part-of* `y03-0035`
  ↳ *contrast* `y03-0055` — xhigh self-attack inside one turn vs a saved, repeatable test loop

- `y03-0041` *STATED* — Max effort should be used for hard jobs Claude does without you.
  — [ItG-vSZFWgA](https://youtu.be/ItG-vSZFWgA) [mVKBGZNsSa4](https://youtu.be/mVKBGZNsSa4) [HTu9VPLvcP0](https://youtu.be/HTu9VPLvcP0)
  ↳ *evidence-for* `g10-0195`
  ↳ *part-of* `y03-0035`
  ↳ *qualifies* `y03-0051` — max is meant for jobs done without you

- `y03-0046` *STATED* — People running Claude overnight wake up to the same message: 'Want me to keep going?'
  > “Want me to keep going?”
  — [ThrAfrg8rjQ](https://youtu.be/ThrAfrg8rjQ) [DHCciHdW-Nw](https://youtu.be/DHCciHdW-Nw)
  ↳ *leads-to* `y03-0051`

- `y03-0047` *STATED* — Anthropic's own guide says Claude quits early in four different ways.
  — [ThrAfrg8rjQ](https://youtu.be/ThrAfrg8rjQ) [DHCciHdW-Nw](https://youtu.be/DHCciHdW-Nw)
  ↳ *because* `y03-0046`
  ↳ *example-of* `y03-0203`

- `y03-0071` *STATED* — Before Prompt Audit changes anything, it shows you exactly what it wants to cut.
  — [q-cfyZWRwmU](https://youtu.be/q-cfyZWRwmU)
  ↳ *evidence-for* `g12-0109`
  ↳ *part-of* `y03-0066`

- `y03-0087` *STATED* — Claude Code released a mod feature, and people have already built crazy things with it.
  — [L9UlSAxSnrM](https://youtu.be/L9UlSAxSnrM)
  ↳ *evidence-for* `g10-0054`

- `y03-0097` *STATED* — When memory ran out, the Mac borrowed space from its drive, and the user says that damaged the drive holding all of their files.
  — [5Ik2XpcR5uE](https://youtu.be/5Ik2XpcR5uE)
  ↳ *evidence-for* `g10-0043`
  ↳ *leads-to* `y03-0098`

- `y03-0098` *STATED* — When the Claude memory blow-up happens, your whole Mac freezes until you force a restart.
  — [5Ik2XpcR5uE](https://youtu.be/5Ik2XpcR5uE)
  ↳ *evidence-for* `g10-0032`
  ↳ *evidence-for* `y03-0092`

- `y04-0012` *STATED* — claude-mem gives Claude permanent memory across all sessions.
  > “it gives you permanent memory across all sessions”
  — [55RbHPThR8g](https://youtu.be/55RbHPThR8g) [EVTO2eM2DlQ](https://youtu.be/EVTO2eM2DlQ) [6zrQsxiYz1E](https://youtu.be/6zrQsxiYz1E)
  ↳ *evidence-for* `g17-0098`
  ↳ *part-of* `y04-0010`
  ↳ *enables* `y04-0118`

- `y04-0019` *STATED* — The free credit is for Claude Code cloud sessions (Claude Code running in the cloud), which had just come out of beta.
  > “for cloud sessions, which just came out of beta”
  — [BgOlXwLlBrY](https://youtu.be/BgOlXwLlBrY) [QnzAaLZ70c0](https://youtu.be/QnzAaLZ70c0) [OyKQsxpeSLY](https://youtu.be/OyKQsxpeSLY)
  ↳ *evidence-for* `g13-0093`
  ↳ *defines* `y04-0018`

- `y04-0084` *STATED* — Given an API link, Claude reads the documentation, writes the code and has a fully working live feature running in your project in under 10 minutes.
  > “Claude reads the documentation, writes the code and has a fully working live feature running in your project in under 10 minutes.”
  — [-U14AktLSiM](https://youtu.be/-U14AktLSiM)
  ↳ *evidence-for* `g13-0154`
  ↳ *evidence-for* `y04-0085`

- `y04-0085` *STATED* — With the paste-the-link method there is no figuring out documentation and no writing integration code yourself: just paste and watch it build.
  > “No figuring out documentation, no writing integration code yourself, just paste and watch it build.”
  — [-U14AktLSiM](https://youtu.be/-U14AktLSiM)
  ↳ *qualifies* `y04-0083`

- `y04-0118` *STATED* — With persistent memory installed you never have to re-explain anything to Claude again.
  > “you never have to re-explain anything ever again”
  — [Gqm7-viLo_E](https://youtu.be/Gqm7-viLo_E)
  ↳ *evidence-for* `g17-0098`
  ↳ *leads-to* `y04-0117`

### concept

- `g01-0126` *INFERRED* — Sitting in front of every tool call is the job of a Claude Code PreToolUse hook, which is how a guard like CC Safety Net can veto a call before it runs.
  — [g-safety-net-stop-claude-deleting-your-files-before-the-command-runs](https://chen.media/guides/safety-net-stop-claude-deleting-your-files-before-the-command-runs)
  ↳ *qualifies* `g01-0125`

- `g03-0004` *CORE* — Claude Code environment-variable settings go inside the "env" block of ~/.claude/settings.json (or can be exported in the shell).
  — [g-stop-claude-goal-check-ins-from-eating-your-limit](https://chen.media/guides/stop-claude-goal-check-ins-from-eating-your-limit) [g-run-every-claude-helper-agent-on-haiku](https://chen.media/guides/run-every-claude-helper-agent-on-haiku)
  ↳ *leads-to* `g03-0003`

- `g04-0093` *INFERRED* — A PreToolUse hook can rewrite a Bash command before it runs, not only allow or block it, which makes it a transparent token-saving tool.
  — [g-the-claude-hook-that-cuts-test-output-down-to-just-the-failures](https://chen.media/guides/the-claude-hook-that-cuts-test-output-down-to-just-the-failures)
  ↳ *generalizes* `g04-0091`
  ↳ *contrast* `g04-0060` — rewrite a command vs block it
  ↳ *generalizes* `g01-0126`

- `g05-0109` *STATED* — Claude Code's plugin slash commands have shell equivalents: `claude plugin marketplace add <owner>/<repo>` and `claude plugin install <plugin>@<marketplace>`.
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless)
  ↳ *generalizes* `g05-0108`
  ↳ *generalizes* `g05-0310`

- `g05-0110` *STATED* — /reload-plugins activates newly installed plugins without restarting Claude Code.
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless)
  ↳ *defines* `g05-0104`

- `g05-0178` *INFERRED* — Subagent effort precedence: the overriding variable beats the per-run parameter, which beats the subagent file, which beats the session level.
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)
  ↳ *generalizes* `g05-0177`
  ↳ *generalizes* `g05-0169`

- `g05-0235` *INFERRED* — Two claude mcp add forms: `claude mcp add --transport http <name> <url>` for a remote server, and `claude mcp add <name> -e KEY=VALUE -- <command>` for a local server with env vars.
  — [g-3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once](https://chen.media/guides/3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once)
  ↳ *generalizes* `g05-0227`
  ↳ *generalizes* `g05-0230`
  ↳ *contrast* `g05-0310` — MCP servers install via claude mcp add; plugins via /plugin

- `g10-0037` *STATED* — Anthropic's GitHub reports point to three sources of the Claude memory blow-up: the desktop app itself, leftover background processes that keep running, and one hungry MCP server.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *because* `g10-0024`

- `g11-0102` *STATED* — The advisor tool is the middle road: Opus keeps doing the work, and Fable is called in to check it at the moments where a mistake would cost you.
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)
  ↳ *defines* `g11-0099`

- `g12-0106` *STATED* — Guide section 'The three habits it hunts' covers the three legacy prompt habits the audit looks for; the lede names 'double-check everything' lines, IMPORTANT in capitals, and step-by-step scripts (body email-gated).
  — [g-clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit](https://chen.media/guides/clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit)
  ↳ *part-of* `g12-0091`
  ↳ *depends-on* `g12-0093`
  ↳ *evidence-for* `y03-0067`

- `g12-0215` *STATED* — Guide section 'Where each check should run' covers where in the workflow each check belongs (body email-gated).
  — [g-how-to-make-claude-test-its-own-work-the-verification-loop](https://chen.media/guides/how-to-make-claude-test-its-own-work-the-verification-loop)
  ↳ *part-of* `g12-0199`
  ↳ *qualifies* `g12-0211`

- `g14-0095` *STATED* — CLAUDE.md continues to describe repository conventions, while intent.md describes the specific change you want.
  — [g-intent-md-claude-project-setup](https://chen.media/guides/intent-md-claude-project-setup)
  ↳ *contrast* `g14-0087`
  ↳ *contrast* `g14-0222` — CLAUDE.md conventions vs ECC skills
  ↳ *contrast* `g06-0241`

- `g14-0351` *INFERRED* — Claude Code plugin marketplaces can be added two ways: inside a session with '/plugin marketplace add owner/repo' (Claude HUD) or from the terminal with 'claude plugin marketplace add <git-url>' (Claude Octopus).
  — [g-headroom-claude-hud-aisa-setup](https://chen.media/guides/headroom-claude-hud-aisa-setup) [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *qualifies* `g14-0299` — both are plugin install paths; slash vs terminal
  ↳ *evidence-for* `g05-0109`

- `g15-0055` *STATED* — The verify-before-done mechanism (implemented by a third skill not named ADHD at all) is a written ledger, a check command that has to run, and a hook that refuses the word 'done' until the check passes.
  — [g-claude-code-says-done-before-it-has-proved-anything-this-fixes-it](https://chen.media/guides/claude-code-says-done-before-it-has-proved-anything-this-fixes-it)
  ↳ *example-of* `g15-0181`

- `g15-0059` *STATED* — The verify-before-done mechanism comes in four parts (section 'The mechanism, in four parts', locked).
  — [g-claude-code-says-done-before-it-has-proved-anything-this-fixes-it](https://chen.media/guides/claude-code-says-done-before-it-has-proved-anything-this-fixes-it)
  ↳ *defines* `g15-0055`

- `g16-0018` *STATED* — Two commands together turn Claude Code into a real design canvas; his guide covers what each one actually does.
  > “The two commands that turn Claude Code into a real design canvas”
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)

- `g16-0020` *STATED* — His /design guide has a section on what a design system project actually holds, placed right after the section on the second command.
  > “What a design system project actually holds”
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)
  ↳ *evidence-for* `g16-0021`

- `g16-0060` *STATED* — Claude's memory is now a set of individual files grouped by topic: one file per subject, not one paragraph about you.
  > “One file per subject, not one paragraph about you”
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit)
  ↳ *example-of* `g16-0001`
  ↳ *part-of* `g16-0012`

- `g16-0175` *STATED* — His fifteen Claude tips are split into three parts: beginner (1-5), intermediate (6-10) and expert (11-15).
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *example-of* `g16-0001`

- `g17-0022` *STATED* — The Claude Project instructions field shapes every reply inside that project, which is why tutor Prompt 1 lives there.
  > “This is the field that shapes every reply inside that project, and it is where Prompt 1 lives.”
  — [g-the-4-prompts-that-turn-a-claude-project-into-a-tutor](https://chen.media/guides/the-4-prompts-that-turn-a-claude-project-into-a-tutor)
  ↳ *because* `g17-0023`
  ↳ *because* `g21-0057`

- `g17-0098` *CORE* — Claude Mem (thedotmack/claude-mem) is a persistent-memory plugin for Claude Code: the problem it fixes is Claude forgetting context between sessions.
  — [g-the-three-claude-code-plugins-worth-installing](https://chen.media/guides/the-three-claude-code-plugins-worth-installing)
  ↳ *defines* `g17-0097`

- `g18-0284` *CORE* — Alex repeatedly argues Claude gets better by subtracting instructions rather than adding them.
  — [g-the-20-kb-file-that-stops-claude-doing-four-dumb-things](https://chen.media/guides/the-20-kb-file-that-stops-claude-doing-four-dumb-things) [g-three-things-almost-everyone-gets-wrong-about-claude-code](https://chen.media/guides/three-things-almost-everyone-gets-wrong-about-claude-code) [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *leads-to* `g18-0283`
  ↳ *generalizes* `g16-0011`

- `g18-0289` *CORE* — Persistent memory outside the chat window is a recurring Alex theme: the NotebookLM wrap-up skill, claude-mem, rohitg00/agentmemory and Graphify's queryable repo graph.
  — [g-give-claude-a-memory-that-survives-the-chat-window](https://chen.media/guides/give-claude-a-memory-that-survives-the-chat-window) [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything) [g-seven-free-repos-that-replace-paid-ai-tools](https://chen.media/guides/seven-free-repos-that-replace-paid-ai-tools) [g-stop-claude-code-re-reading-your-repo-every-session](https://chen.media/guides/stop-claude-code-re-reading-your-repo-every-session)
  ↳ *contrast* `g18-0283` — memory outside the context window keeps context lean
  ↳ *evidence-for* `g20-0286`

- `g19-0027` *STATED* — Tier 2 of the 50 Claude tips is 'Context and memory'.
  > “Context and memory”
  — [g-50-claude-tips-ranked-worst-to-best](https://chen.media/guides/50-claude-tips-ranked-worst-to-best)
  ↳ *part-of* `g19-0043`
  ↳ *contrast* `g19-0008` — both guides put context near the top

- `g19-0028` *STATED* — Tier 3 of the 50 Claude tips is 'Guardrails'.
  > “Guardrails”
  — [g-50-claude-tips-ranked-worst-to-best](https://chen.media/guides/50-claude-tips-ranked-worst-to-best)
  ↳ *part-of* `g19-0043`

- `g20-0147` *CORE* — Memory is not a feature you switch on; it is a loop you build: write down what happened, and load it back before the next job.
  > “Memory is not a feature you switch on. It is a loop you build”
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0141`
  ↳ *contrast* `g20-0236` — memory.md loaded by prompt vs CLAUDE.md auto-loaded

- `g20-0286` *CORE* — Alex treats persistent memory as the first thing to build before tools, agents or autonomy: memory.md, CLAUDE.md, the Day 1 brain and the council's saved rulings.
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory) [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model) [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup) [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *generalizes* `g20-0159`

- `g21-0216` *INFERRED* — Although the guide calls them skills, the content-team files are Claude Code custom slash commands: markdown files in .claude/commands/ that become /hooks, /repurpose, /grade, /trends and /calendar.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *defines* `g21-0215`

- `g22-0284` *INFERRED* — A Claude Project is Alex's default permanent home for persistent context: the four voice files and the screenshot second brain both live in one Project.
  — [g-the-four-files-that-make-claude-sound-like-you](https://chen.media/guides/the-four-files-that-make-claude-sound-like-you) [g-turn-your-camera-roll-into-something-you-can-search](https://chen.media/guides/turn-your-camera-roll-into-something-you-can-search)
  ↳ *generalizes* `y01-0161`

- `g23-0199` *CORE* — Making a setup permanent is a repeated move in his guides: Forge Loop prompts go in CLAUDE.md / Project Instructions, the codes get an always-on setup block, MCP plugins get 'make them stick', and Fable's understanding is written into an instructions file.
  — [g-clone-the-smart-model-s-brain-into-the-cheap-one](https://chen.media/guides/clone-the-smart-model-s-brain-into-the-cheap-one) [g-make-claude-grade-and-fix-its-own-work](https://chen.media/guides/make-claude-grade-and-fix-its-own-work) [g-the-claude-codes-cheat-sheet-plus-five-bonus-ones](https://chen.media/guides/the-claude-codes-cheat-sheet-plus-five-bonus-ones) [g-the-claude-plugins-cheat-sheet-add-once-then-just-ask](https://chen.media/guides/the-claude-plugins-cheat-sheet-add-once-then-just-ask)
  ↳ *because* `g23-0017`

- `r02-0313` *CORE* — Alex's skills keep all state as plain files in a dot-folder in the working directory (`.hunter/`, `.launch/`) and never write outside it.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill) [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *generalizes* `r02-0115`

- `r03-0007` *STATED* — /learn gives a project a rulebook that keeps each lesson across Claude Code sessions instead of leaving corrections in chat history.
  > “/learn gives your project a rulebook that keeps the lesson”
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *because* `r03-0005`
  ↳ *defines* `r03-0001`
  ↳ *defines* `r01-0034`

- `r03-0097` *INFERRED* — /learn's architecture is a reusable Claude Code self-improvement loop: a UserPromptSubmit hook logs corrections, a scheduled headless 'claude -p' run with a narrow allowlist distils them into rules, and CLAUDE.md @-imports the rule file every session.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *generalizes* `r03-0007`
  ↳ *depends-on* `r03-0045`
  ↳ *depends-on* `r03-0038`
  ↳ *depends-on* `r03-0015`
  ↳ *generalizes* `r01-0034`

- `r04-0019` *INFERRED* — Alex pairs prose rules with mechanical enforcement: /mentor uses a hook that blocks Write/Edit, and /night-crew relies on branch protection, a secret-free cloud environment and removed connectors, because rules in a prompt are only instructions.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill) [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)

- `r04-0043` *INFERRED* — Hooks travel with plugins, not with bare skill folders: a skill dropped into ~/.claude/skills/ can only instruct, while a plugin can also enforce through its hooks.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *qualifies* `r04-0019`
  ↳ *generalizes* `r04-0042`

- `y01-0007` *STATED* — In the Codex desktop app the message box is where you describe what you want, and the controls for how Codex works (model, effort, modes) sit beneath it.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)

- `y01-0054` *STATED* — Connector vs computer use: a Drive connection reaches a service through its tools, while computer use operates at the app's interface.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *contrast* `y01-0049`
  ↳ *contrast* `y01-0043`

- `y03-0035` *CORE* — Claude Code effort runs low, medium, high, extra high (xhigh) and max, plus Ultra Code (ultracode) above them.
  — [ItG-vSZFWgA](https://youtu.be/ItG-vSZFWgA) [mVKBGZNsSa4](https://youtu.be/mVKBGZNsSa4) [HTu9VPLvcP0](https://youtu.be/HTu9VPLvcP0)
  ↳ *evidence-for* `g10-0173`
  ↳ *leads-to* `y03-0044`

### definition

- `g01-0083` *STATED* — Show Your Work gives Claude two new tools, show_image and show_video.
  — [g-show-your-work-see-every-screenshot-and-video-claude-makes-right-in-your-termina](https://chen.media/guides/show-your-work-see-every-screenshot-and-video-claude-makes-right-in-your-termina)
  ↳ *part-of* `g01-0075`
  ↳ *enables* `g01-0079`

- `g02-0196` *STATED* — A loop in Claude Code is a prompt it re-runs on a timer.
  > “A loop is a prompt Claude Code re-runs on a timer.”
  — [g-find-the-claude-code-loops-that-are-quietly-eating-your-limit](https://chen.media/guides/find-the-claude-code-loops-that-are-quietly-eating-your-limit)
  ↳ *defines* `g02-0195`

- `g03-0156` *CORE* — In plan mode Claude explores and proposes an approach for your approval before it edits anything.
  — [g-turn-on-plan-mode-so-claude-plans-before-it-edits](https://chen.media/guides/turn-on-plan-mode-so-claude-plans-before-it-edits)
  ↳ *leads-to* `g03-0157`

- `g04-0056` *STATED* — Claude Code hooks fail open by default: a guard hook that fails does not stop the action it was guarding.
  > “fails open by default”
  — [g-make-a-crashed-claude-hook-block-the-action-not-let-it-through](https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through)
  ↳ *defines* `g04-0055`
  ↳ *qualifies* `g19-0039` — a guard hook that crashes lets the action through by default

- `g04-0059` *STATED* — onFailure is a field on Claude Code command and HTTP hooks with two values: "continue" (the default) and "block".
  — [g-make-a-crashed-claude-hook-block-the-action-not-let-it-through](https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through)
  ↳ *part-of* `g04-0058`
  ↳ *contrast* `g04-0056` — block flips the default fail-open behaviour

- `g04-0064` *INFERRED* — Exit code 2 is Claude Code's blocking exit code for hooks: it blocks the tool call on PreToolUse, blocks the prompt on UserPromptSubmit and denies on PermissionRequest.
  — [g-make-a-crashed-claude-hook-block-the-action-not-let-it-through](https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through)

- `g04-0065` *STATED* — The hook failures onFailure covers include a hook that crashes, times out, or can't start (for example a wrong script path).
  — [g-make-a-crashed-claude-hook-block-the-action-not-let-it-through](https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through)
  ↳ *qualifies* `g04-0059`
  ↳ *defines* `g04-0055`

- `g05-0072` *STATED* — In the Opus 5.5 CLAUDE.md stop rule, 'destructive' means deleting data, force-pushing, or changing anything outside this repository.
  — [g-your-opus-5-5-prompt-checklist](https://chen.media/guides/your-opus-5-5-prompt-checklist)
  ↳ *defines* `g05-0071`

- `g05-0168` *STATED* — Claude Code effort options are low, medium, high, xhigh and max, depending on the model.
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)
  ↳ *qualifies* `g05-0167`
  ↳ *qualifies* `g10-0173` — options depend on the model

- `g06-0241` *STATED* — CLAUDE.md is written by you, holds instructions and rules, and loads at the start of every Claude Code session.
  — [g-give-claude-a-notebook-that-survives-every-chat-reset](https://chen.media/guides/give-claude-a-notebook-that-survives-every-chat-reset)
  ↳ *part-of* `g06-0240`
  ↳ *contrast* `g06-0242`

- `g06-0242` *STATED* — Claude Code auto memory is written by Claude, holds learnings and patterns, and loads at the start of every session.
  — [g-give-claude-a-notebook-that-survives-every-chat-reset](https://chen.media/guides/give-claude-a-notebook-that-survives-every-chat-reset)
  ↳ *part-of* `g06-0240`

- `g07-0162` *STATED* — A Claude Code mod is a small plugin that runs inside Claude Code.
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`
  ↳ *defines* `g07-0161`
  ↳ *evidence-for* `g10-0056`

- `g08-0242` *STATED* — This attack is called prompt injection, and the file carrying it is the Trojan Horse.
  > “This is called prompt injection, and the file is the Trojan Horse.”
  — [g-stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes](https://chen.media/guides/stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes)
  ↳ *defines* `g08-0235`

- `g09-0215` *STATED* — Claude Code routines are scheduled agents that run on Anthropic's cloud at a set time, on your GitHub repo, with your laptop shut.
  > “it has scheduled agents, called routines, that run on Anthropic's cloud at a set time, on your GitHub repo, with your laptop shut”
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)
  ↳ *enables* `g09-0213`
  ↳ *evidence-for* `r04-0089`
  ↳ *evidence-for* `g22-0070`
  ↳ *analogy-for* `g13-0096`

- `g10-0034` *STATED* — A memory leak is when an app keeps taking more memory and never gives it back.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *defines* `g10-0024`

- `g10-0035` *STATED* — Once memory runs out, macOS starts borrowing space from your SSD (called swap) and squeezing what's left.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *leads-to* `g10-0036`

- `g10-0056` *CORE* — A Claude Code mod is a small plugin that runs inside Claude Code itself.
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *defines* `g10-0046`

- `g10-0186` *CORE* — Effort tells Claude how much work you want it to put in: how long to think, how much to test, and how many decisions to make on its own before it comes back to you.
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *defines* `g10-0173`
  ↳ *contrast* `g10-0142` — effort sets how many decisions Claude makes before coming back; default habit is to check in

- `g13-0094` *CORE* — A Claude Code cloud session runs Claude Code on a virtual machine Anthropic manages instead of on your computer.
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it) [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)
  ↳ *defines* `g13-0093`

- `g13-0111` *STATED* — Cloud sessions being out of research preview means they are now a finished feature instead of a test.
  — [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)
  ↳ *defines* `g13-0093`

- `g13-0112` *STATED* — A GitHub repository is the online folder that holds your project's code.
  — [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)
  ↳ *defines* `g13-0095`

- `g14-0091` *STATED* — The suggested intent.md fields are: the problem, the desired outcome, affected people and systems, constraints, and unresolved questions.
  — [g-intent-md-claude-project-setup](https://chen.media/guides/intent-md-claude-project-setup)
  ↳ *defines* `g14-0087`

- `g17-0019` *STATED* — A Claude Project is a real Claude feature: a self-contained workspace with its own instructions and its own memory of your files.
  > “A Project is a real Claude feature: a self contained workspace with its own instructions and its own memory of your files.”
  — [g-the-4-prompts-that-turn-a-claude-project-into-a-tutor](https://chen.media/guides/the-4-prompts-that-turn-a-claude-project-into-a-tutor)
  ↳ *defines* `g17-0018`

- `g18-0089` *STATED* — On Claude Code, global skills live in ~/.claude/skills/ and project-local skills live in .claude/skills/ inside the project.
  — [g-five-animation-skills-for-claude-code-with-install-commands](https://chen.media/guides/five-animation-skills-for-claude-code-with-install-commands)
  ↳ *evidence-for* `r01-0006`

- `g18-0162` *CORE* — `/reload-plugins` activates what you just installed without restarting the Claude Code session.
  > “/reload-plugins”
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *part-of* `g18-0160`
  ↳ *evidence-for* `g05-0110`

- `g19-0067` *CORE* — Claude Code subagents are specialised Claude instances you define once, each with its own system prompt, its own scoped tool list and its own context window.
  > “specialized Claude instances you define once, each with its own system prompt, its own scoped tool list, and its own context window”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)

- `g22-0070` *CORE* — A Claude Code Routine is a saved Claude Code setup with three parts: a prompt (the job), the connectors it needs, and a trigger (a schedule), running at the cadence you pick.
  — [g-put-a-recurring-job-on-autopilot-with-claude-code](https://chen.media/guides/put-a-recurring-job-on-autopilot-with-claude-code)
  ↳ *defines* `g22-0066`

- `g22-0271` *STATED* — Reading /status: a Model line of Fable 5 means you are on the flagship; Opus 4.8 means your request was served by the older model.
  — [g-trigger-words-and-how-to-rephrase-around-them](https://chen.media/guides/trigger-words-and-how-to-rephrase-around-them)
  ↳ *part-of* `g22-0270`

- `g23-0155` *INFERRED* — Claude Code's MCP install syntax is 'claude mcp add <name> -- <command>': everything after '--' is the command that launches the server (here 'npx chrome-devtools-mcp@latest').
  — [g-the-claude-plugins-cheat-sheet-add-once-then-just-ask](https://chen.media/guides/the-claude-plugins-cheat-sheet-add-once-then-just-ask)
  ↳ *defines* `g23-0153`

- `r03-0014` *STATED* — LESSONS.md is the /learn rulebook: one line per rule, with the date it last came up and how many times; you can edit it by hand any time.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0008`

- `r03-0016` *STATED* — .learn/inbox.jsonl holds every prompt of yours that looked like a correction, with the time and session; it stays on your computer.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0012`

- `r03-0028` *STATED* — '/learn setup' is the one-time setup and is safe to run again.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *defines* `r03-0025`
  ↳ *part-of* `r03-0072`

- `r03-0029` *STATED* — '/learn always run the tests first' (any lesson typed after /learn) turns that text into a rule immediately.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0072`

- `r03-0030` *STATED* — '/learn' with nothing after it finds the last time you corrected Claude in this chat and makes it a rule.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0072`

- `r03-0032` *STATED* — '/learn list' shows the rulebook numbered, with rules that look alike flagged.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0072`

- `r03-0034` *STATED* — '/learn status' runs 'LEARN status' and shows it (listed in the SKILL.md mode table and argument-hint).
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0072`

- `y01-0024` *STATED* — A Codex project groups related work together.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *contrast* `y01-0161` — Codex project = local folder; Claude Project = uploaded knowledge base

- `y01-0025` *STATED* — A Codex local project connects work to a folder on your computer; 'local' simply means the files are on this machine.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *example-of* `y01-0024`

- `y01-0049` *STATED* — Codex computer use lets it see an app and interact with its visible controls - clicking and typing - for jobs that involve clicking buttons or entering text inside an app.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)

- `y01-0061` *STATED* — Codex reads project rules from a file called AGENTS.md in the project folder - a text file whose special name tells Codex these are specific instructions for the work (the Codex counterpart of CLAUDE.md).
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *analogy-for* `g06-0241`
  ↳ *part-of* `y01-0070`
  ↳ *analogy-for* `y01-0164` — AGENTS.md ~ Claude Project custom instructions

- `y01-0084` *STATED* — Alex's beginner definition of Claude Code: basically a more powerful version of Claude that can actually build stuff and interact with your files.
  > “it's basically just a more powerful version of Claude that can actually build stuff and interact with your files.”
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *defines* `y01-0083`
  ↳ *example-of* `y01-0005`

- `y01-0152` *STATED* — Claude Artifacts let you build software and tools right inside your browser.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)

- `y03-0094` *STATED* — Memory (RAM) is basically the space your Mac needs to run in.
  — [5Ik2XpcR5uE](https://youtu.be/5Ik2XpcR5uE)
  ↳ *evidence-for* `g10-0035`
  ↳ *defines* `y03-0093`

### example

- `g01-0130` *STATED* — CC Safety Net blocks destructive Git: git reset --hard and git push --force.
  > “git reset --hard, git push --force”
  — [g-safety-net-stop-claude-deleting-your-files-before-the-command-runs](https://chen.media/guides/safety-net-stop-claude-deleting-your-files-before-the-command-runs)
  ↳ *example-of* `g01-0123`

- `g01-0131` *STATED* — CC Safety Net blocks rm -rf on dangerous targets.
  — [g-safety-net-stop-claude-deleting-your-files-before-the-command-runs](https://chen.media/guides/safety-net-stop-claude-deleting-your-files-before-the-command-runs)
  ↳ *example-of* `g01-0123`

- `g01-0132` *STATED* — CC Safety Net also blocks the same destructive commands hidden inside bash -c or python -c.
  > “bash -c or python -c”
  — [g-safety-net-stop-claude-deleting-your-files-before-the-command-runs](https://chen.media/guides/safety-net-stop-claude-deleting-your-files-before-the-command-runs)
  ↳ *example-of* `g01-0123`

- `g01-0134` *STATED* — CC Safety Net blocks access to secrets: SSH keys, .env files, ~/.aws and coding-CLI login files.
  > “SSH keys, .env files, ~/.aws and coding-CLI login files”
  — [g-safety-net-stop-claude-deleting-your-files-before-the-command-runs](https://chen.media/guides/safety-net-stop-claude-deleting-your-files-before-the-command-runs)
  ↳ *example-of* `g01-0123`

- `g04-0057` *STATED* — Example of a failing-open guard hook: a script that checks every shell command; if its path is wrong or it crashes, Claude Code shows a small error and runs the command anyway.
  — [g-make-a-crashed-claude-hook-block-the-action-not-let-it-through](https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through)
  ↳ *example-of* `g04-0056`

- `g05-0065` *STATED* — Anthropic's guide example of a mid-run steering message: 'Also keep the old endpoint names as aliases.'
  > “Also keep the old endpoint names as aliases.”
  — [g-your-opus-5-5-prompt-checklist](https://chen.media/guides/your-opus-5-5-prompt-checklist)
  ↳ *example-of* `g05-0064`

- `g08-0194` *STATED* — Asked to fix a login button, Claude Code may also rename files, restyle pages, upgrade packages and tidy things you never mentioned.
  — [g-stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes](https://chen.media/guides/stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes)
  ↳ *example-of* `g08-0190`
  ↳ *example-of* `y02-0056`

- `g08-0240` *STATED* — A hidden sentence in a normal-looking report, résumé or web page can be written white on white, in a size too small to see, or in invisible characters.
  — [g-stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes](https://chen.media/guides/stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes)
  ↳ *example-of* `g08-0235`

- `g09-0033` *STATED* — You tell Claude 'no, we use pnpm' on Monday, and on Tuesday it runs npm again, because the correction only lived in Monday's chat.
  > “You tell Claude "no, we use pnpm" on Monday, and on Tuesday it runs npm again, because the correction only lived in Monday's chat.”
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *example-of* `g09-0032`
  ↳ *evidence-for* `r03-0006`

- `g09-0039` *STATED* — Correction-sounding messages the lessons hook catches include 'no, I told you...', 'you forgot...' and 'wrong...'.
  > “("no, I told you...", "you forgot...", "wrong...")”
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *example-of* `g09-0038`
  ↳ *evidence-for* `r03-0012`

- `g10-0032` *STATED* — The Claude-app freeze symptom: you come back, the cursor spins, apps won't quit, and the only way out is holding the power button, which loses anything unsaved.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *example-of* `g10-0024`

- `g10-0060` *STATED* — Anthropic's example Claude Code mod: a weather band above the prompt that turns from Clear to Storm as your context fills up.
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *example-of* `g10-0057`

- `g10-0061` *STATED* — Anthropic's example Claude Code mod: a guard that stops an rm -rf and shows exactly what it would delete.
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *example-of* `g10-0058`
  ↳ *example-of* `g10-0075` — rm -rf guard mod is a leash for Claude Code
  ↳ *analogy-for* `g01-0130`

- `g10-0062` *STATED* — Anthropic's example Claude Code mod: a replay of every edit Claude made in a turn.
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *example-of* `g10-0058`

- `g10-0188` *STATED* — Thariq Shihipar's clearest effort test: he asked Claude to "build a personal fitness and workout tracker app" at each level.
  > “build a personal fitness and workout tracker app”
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *example-of* `g10-0187`

- `g13-0135` *STATED* — What a new Claude Code session forgets: the file you fixed yesterday, the decision you made about your login page, the bug you already chased down, so you explain it all again.
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *example-of* `g13-0134`

- `g16-0261` *STATED* — Reading back real transcripts, Anthropic found single requests carrying contradictory instructions: one telling Claude to leave documentation as appropriate, another telling it not to add comments.
  — [g-why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it](https://chen.media/guides/why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it)
  ↳ *evidence-for* `g16-0260`

- `g19-0253` *STATED* — 'Point Claude at r/smallbusiness' fails on your first attempt.
  > “"Point Claude at r/smallbusiness" fails on your first attempt.”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *example-of* `g19-0249`

- `g20-0243` *STATED* — Example # memory line: '# always use pnpm, never npm'.
  > “# always use pnpm, never npm”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *example-of* `g20-0242`
  ↳ *leads-to* `r03-0006`

- `g20-0244` *STATED* — Example # memory line: '# the staging DB is read only, never write to it'.
  > “# the staging DB is read only, never write to it”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *example-of* `g20-0242`

- `g20-0245` *STATED* — Example # memory line: '# I want the answer first, then the reasoning'.
  > “# I want the answer first, then the reasoning”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *example-of* `g20-0242`
  ↳ *analogy-for* `g20-0248`

- `g20-0247` *STATED* — Starter CLAUDE.md 'Who I am': 'I run a small business. I ship fast and I care about clarity over polish.'
  > “I run a small business. I ship fast and I care about clarity over polish.”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *part-of* `g20-0246`

- `g21-0233` *STATED* — Run the trend scout as: /trends AI tools for small business owners
  > “How to run it: /trends AI tools for small business owners”
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *example-of* `g21-0230`

- `r01-0200` *STATED* — /court prompt for your code plan: '/court Rewrite [part of the app] in [new approach] instead of [current approach]. Here's why: [reasons].'
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0194`

- `r03-0006` *CORE* — Alex's example of session amnesia: you tell Claude 'no, we use pnpm' on Monday, and on Tuesday it runs npm again, because the correction only lived in Monday's chat.
  > “You tell Claude "no, we use pnpm" on Monday, and on Tuesday it runs npm again, because the correction only lived in Monday's chat.”
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *example-of* `r03-0005`

- `r03-0043` *STATED* — learn-skill's examples/one-day folder shows a day's inbox of 8 corrections, the investigator's note (5 lessons, 2 false alarms, and one old rule that existed but was too vague to stop the mistake, so it got sharper), and the rulebook before and after.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *example-of* `r03-0007`

- `r03-0098` *STATED* — The /learn demo 'One day with /learn' is a made-up workday on TinyTasks, a small Next.js to-do app with Prisma and Tailwind: two Claude Code sessions, eight corrections typed along the way, and nobody ran /learn by hand.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0043`

- `r03-0099` *STATED* — In the one-day demo, LESSONS-before.md held 3 rules from earlier days and LESSONS-after.md held 7 rules the next morning.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0098`

- `r03-0100` *STATED* — In the one-day demo the first session used npm, and so did the second, because the rulebook didn't know yet; the two corrections became one rule, seen 2x.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0098`

- `r03-0103` *STATED* — 'don't worry about the footer' tripped the /learn hook, which leans toward catching too much, and the investigator left it out of the rulebook.
  > “it leans toward catching too much”
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0098`
  ↳ *example-of* `r03-0083`

- `r03-0107` *STATED* — LESSONS.md carries the comment '<!-- Managed by /learn: one rule per line. Edit or delete any rule by hand; keep the "(date, Nx)" ending. -->', so each rule ends like '(2026-10-05, 2x)'.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0014`

- `r03-0117` *STATED* — Demo lesson 1: Claude ran 'npm install', creating a package-lock.json next to the existing pnpm-lock.yaml, and did it again at 16:37 in the second session.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *because* `r03-0118`
  ↳ *evidence-for* `r03-0100`
  ↳ *part-of* `r03-0116`

- `r03-0123` *STATED* — Demo lesson 3: the new /api/tasks/due route converted due dates to local time before comparing them, so tasks due tonight showed as tomorrow (dates an hour off).
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *because* `r03-0124`
  ↳ *part-of* `r03-0116`

- `r03-0126` *STATED* — Demo lesson 4: asked for a new API route, Claude also added a 'priority' column to prisma/schema.prisma.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *because* `r03-0127`
  ↳ *part-of* `r03-0116`
  ↳ *example-of* `y02-0056`

- `r03-0129` *STATED* — Demo lesson 5: Claude styled the new button with '#3b82f6' instead of the 'brand' colour token.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *because* `r03-0130`
  ↳ *part-of* `r03-0116`

- `y01-0026` *STATED* — Example Codex project: one for your business holding service details, writing examples and planning documents, so Codex works with those files when asked instead of relying only on what you type.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *example-of* `y01-0024`

- `y01-0034` *STATED* — Plan mode example: you want to reorganize a website but haven't decided what belongs on each page.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *example-of* `y01-0033`

- `y01-0039` *STATED* — Goal mode example outcome: a finished research report that compares three options and includes links to its sources.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *example-of* `y01-0038`
  ↳ *example-of* `y01-0040`

- `y01-0052` *STATED* — Computer use example: entering information into a form, or organizing something in an app you already use day to day.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *example-of* `y01-0049`

- `y01-0060` *STATED* — Preferences that should apply whenever you work in a project: plain English, a certain document format, or your company name written a particular way.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *example-of* `y01-0061`

- `y01-0153` *STATED* — Artifacts example: drag a raw data file into Claude and ask for a real analytics dashboard - you write no code, the chat window splits in half, and in about 10 seconds a fully interactive app renders live.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *example-of* `y01-0152`

- `y01-0156` *STATED* — With Artifacts you can build calculators, landing pages and interactive presentations in minutes.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *example-of* `y01-0152`

- `y03-0048` *STATED* — Early-quit pattern: Claude writes a summary of what it'll do next, then never starts it.
  — [ThrAfrg8rjQ](https://youtu.be/ThrAfrg8rjQ) [DHCciHdW-Nw](https://youtu.be/DHCciHdW-Nw)
  ↳ *example-of* `y03-0047`

- `y03-0049` *STATED* — Early-quit pattern: Claude hands you a list of decisions even when none of them are blocking the work.
  — [ThrAfrg8rjQ](https://youtu.be/ThrAfrg8rjQ) [DHCciHdW-Nw](https://youtu.be/DHCciHdW-Nw)
  ↳ *example-of* `y03-0047`

- `y03-0050` *STATED* — Early-quit pattern: Claude stops just because the job ran long and decides to check in.
  — [ThrAfrg8rjQ](https://youtu.be/ThrAfrg8rjQ) [DHCciHdW-Nw](https://youtu.be/DHCciHdW-Nw)
  ↳ *example-of* `y03-0047`

- `y03-0088` *STATED* — One Claude Code mod puts Tetris right above the chat box so you can play it while Claude works.
  — [L9UlSAxSnrM](https://youtu.be/L9UlSAxSnrM)
  ↳ *evidence-for* `g10-0046`
  ↳ *example-of* `y03-0087`

- `y03-0089` *STATED* — One Claude Code mod turns whatever Claude is doing into live cartoons while you wait.
  — [L9UlSAxSnrM](https://youtu.be/L9UlSAxSnrM)
  ↳ *evidence-for* `g10-0055`
  ↳ *example-of* `y03-0087`

- `y03-0090` *STATED* — One Claude Code mod gives you a pet that grows every time Claude saves your work.
  — [L9UlSAxSnrM](https://youtu.be/L9UlSAxSnrM)
  ↳ *evidence-for* `g10-0046`
  ↳ *example-of* `y03-0087`

### idea

- `g03-0010` *INFERRED* — For unattended or overnight Claude Code runs his guides combine four pieces: --bg sessions survive closing the terminal, CLAUDE_CODE_RETRY_WATCHDOG=1 survives 429/529 capacity errors, auto-continue survives a usage-limit reset, and CLAUDE_CODE_GOAL_CHECKIN_MINUTES=0 stops idle check-ins burning the limit.
  — [g-keep-claude-retrying-overnight-when-the-api-is-busy](https://chen.media/guides/keep-claude-retrying-overnight-when-the-api-is-busy) [g-keep-claude-working-after-you-close-the-terminal](https://chen.media/guides/keep-claude-working-after-you-close-the-terminal) [g-let-claude-code-wait-out-your-limit-and-carry-on](https://chen.media/guides/let-claude-code-wait-out-your-limit-and-carry-on) [g-stop-claude-goal-check-ins-from-eating-your-limit](https://chen.media/guides/stop-claude-goal-check-ins-from-eating-your-limit)
  ↳ *contrast* `y03-0046`

- `g04-0046` *INFERRED* — A repo can ship a CLAUDE.md that makes Claude Code act as its interactive installer, so setup is just: clone, run claude, say 'set it up'.
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *generalizes* `g04-0045`

- `g06-0266` *INFERRED* — Coucou and bigarrow both attack the moment Claude needs a human: Coucou moves permission approvals to your iPhone, bigarrow points at the exact button to click.
  — [g-approve-claude-s-permission-requests-from-your-iphone-with-coucou](https://chen.media/guides/approve-claude-s-permission-requests-from-your-iphone-with-coucou) [g-make-claude-point-at-the-button-you-need-to-click](https://chen.media/guides/make-claude-point-at-the-button-you-need-to-click)
  ↳ *generalizes* `g06-0113`
  ↳ *because* `g06-0150`

- `g08-0202` *INFERRED* — Where /bouncer is only a rule, Claude Code's permission settings and hooks are the enforced lock for keeping edits inside an allowed scope.
  — [g-stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes](https://chen.media/guides/stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes)
  ↳ *contrast* `g08-0201`
  ↳ *evidence-for* `r04-0019`

- `g10-0045` *INFERRED* — For long or overnight Claude jobs on a Mac, running them in Claude Code in the Terminal rather than the Claude desktop app avoids the desktop leak (under 200 MB vs 131-140 GB in the reports).
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *because* `g10-0039`
  ↳ *contrast* `g10-0133` — two different overnight failure modes: freeze vs early stop
  ↳ *qualifies* `g10-0024`

- `g10-0151` *INFERRED* — In Claude Code, 'where Claude reads it every time' maps to CLAUDE.md or the system prompt, so the keep-going paragraph belongs there for overnight runs.
  — [g-claude-quits-long-jobs-halfway-the-keep-going-paragraph](https://chen.media/guides/claude-quits-long-jobs-halfway-the-keep-going-paragraph)
  ↳ *defines* `g10-0138`
  ↳ *example-of* `g18-0064`
  ↳ *depends-on* `g20-0236`

- `g11-0180` *INFERRED* — In Claude Code the copy-once provenance line belongs in CLAUDE.md, so every session separates the user's words from pasted or fetched text.
  — [g-stop-hidden-lines-in-pasted-text-from-hijacking-claude](https://chen.media/guides/stop-hidden-lines-in-pasted-text-from-hijacking-claude)
  ↳ *generalizes* `g11-0176`
  ↳ *qualifies* `g08-0241`

- `g16-0012` *INFERRED* — This batch offers three different answers to Claude forgetting between sessions: Anthropic's native file-based memory (Settings > Memory > Topics), the Claude Mem plugin for Claude Code, and Ruflo's memory that survives your session.
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit) [g-three-plugins-that-fix-claude-code-s-setup-limits-and-memory](https://chen.media/guides/three-plugins-that-fix-claude-code-s-setup-limits-and-memory) [g-ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm](https://chen.media/guides/ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm) [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *evidence-for* `g18-0289`

- `g22-0174` *INFERRED* — The four voice files (voice.md, standards.md, rules.md, context.md) are persistent context in the same spirit as CLAUDE.md or JUDGMENT.md: write once, loaded before every output.
  — [g-the-four-files-that-make-claude-sound-like-you](https://chen.media/guides/the-four-files-that-make-claude-sound-like-you)
  ↳ *generalizes* `g22-0172`
  ↳ *analogy-for* `g22-0004` — persistent rules file read before every output

### method

- `g01-0084` *STATED* — With Show Your Work installed you can open any file yourself with /img path/to/file.png.
  > “/img path/to/file.png”
  — [g-show-your-work-see-every-screenshot-and-video-claude-makes-right-in-your-termina](https://chen.media/guides/show-your-work-see-every-screenshot-and-video-claude-makes-right-in-your-termina)
  ↳ *part-of* `g01-0083`

- `g01-0095` *STATED* — After installing Graphicle you ask Claude to use it (guide section: Step 2: ask Claude to use it).
  — [g-give-claude-a-map-and-a-memory-of-your-whole-project](https://chen.media/guides/give-claude-a-map-and-a-memory-of-your-whole-project)
  ↳ *depends-on* `g01-0092`

- `g01-0125` *STATED* — CC Safety Net sits in front of every tool call Claude Code makes.
  — [g-safety-net-stop-claude-deleting-your-files-before-the-command-runs](https://chen.media/guides/safety-net-stop-claude-deleting-your-files-before-the-command-runs)
  ↳ *part-of* `g01-0122`
  ↳ *leads-to* `g01-0127`
  ↳ *example-of* `g19-0039`

- `g01-0127` *STATED* — CC Safety Net parses what the command would actually do rather than what it looks like.
  — [g-safety-net-stop-claude-deleting-your-files-before-the-command-runs](https://chen.media/guides/safety-net-stop-claude-deleting-your-files-before-the-command-runs)
  ↳ *part-of* `g01-0122`
  ↳ *leads-to* `g01-0128`
  ↳ *enables* `g01-0133`

- `g01-0167` *STATED* — Type /grill-me, describe your plan, and Claude asks numbered questions with its own recommended answer until nothing is left silently assumed; only then does it build.
  > “/grill-me”
  — [g-grill-me-make-claude-interview-you-before-it-writes-a-line-of-code](https://chen.media/guides/grill-me-make-claude-interview-you-before-it-writes-a-line-of-code)
  ↳ *defines* `g01-0165`
  ↳ *example-of* `g15-0135`

- `g02-0044` *STATED* — Context Mode uses hooks to route Claude's tool calls through its sandbox automatically, so you don't have to remember to use it.
  — [g-stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode)
  ↳ *enables* `g02-0037`
  ↳ *example-of* `g04-0093`

- `g02-0049` *STATED* — With cc-stretch, replies arrive short and every key phrase is a link.
  — [g-make-claude-s-long-answers-6x-shorter-to-read](https://chen.media/guides/make-claude-s-long-answers-6x-shorter-to-read)
  ↳ *part-of* `g02-0046`

- `g02-0050` *STATED* — Clicking a cc-stretch link grows the text right where it stands, so you never lose your place.
  — [g-make-claude-s-long-answers-6x-shorter-to-read](https://chen.media/guides/make-claude-s-long-answers-6x-shorter-to-read)
  ↳ *part-of* `g02-0049`

- `g02-0054` *STATED* — In cc-stretch an expanded phrase shrinks back when you click its collapse control (the control's glyph did not survive in the captured guide text).
  — [g-make-claude-s-long-answers-6x-shorter-to-read](https://chen.media/guides/make-claude-s-long-answers-6x-shorter-to-read)
  ↳ *contrast* `g02-0050`

- `g02-0056` *STATED* — cc-stretch tells Claude which parts you opened, so Claude doesn't assume you read the rest.
  — [g-make-claude-s-long-answers-6x-shorter-to-read](https://chen.media/guides/make-claude-s-long-answers-6x-shorter-to-read)
  ↳ *part-of* `g02-0046`

- `g02-0057` *STATED* — cc-stretch folds finished groups of tool calls into one line.
  — [g-make-claude-s-long-answers-6x-shorter-to-read](https://chen.media/guides/make-claude-s-long-answers-6x-shorter-to-read)
  ↳ *part-of* `g02-0046`

- `g02-0119` *STATED* — Time Machine records each step in order with a snapshot of your files, so you can go back to any one step.
  — [g-rewind-claude-code-to-the-step-that-broke-your-code](https://chen.media/guides/rewind-claude-code-to-the-step-that-broke-your-code)
  ↳ *part-of* `g02-0117`

- `g02-0120` *STATED* — Time Machine records every tool call (each edit and command) on a timeline, with a snapshot of your files after it.
  — [g-rewind-claude-code-to-the-step-that-broke-your-code](https://chen.media/guides/rewind-claude-code-to-the-step-that-broke-your-code)
  ↳ *part-of* `g02-0117`
  ↳ *enables* `g02-0122`

- `g02-0122` *STATED* — The Time Machine command /tm why points at the edit that broke a failing test run.
  — [g-rewind-claude-code-to-the-step-that-broke-your-code](https://chen.media/guides/rewind-claude-code-to-the-step-that-broke-your-code)
  ↳ *part-of* `g02-0117`
  ↳ *contrast* `g02-0118` — names the breaking step, not just the changed lines

- `g02-0123` *STATED* — The Time Machine command /tm restore <n> puts your files back to step n.
  — [g-rewind-claude-code-to-the-step-that-broke-your-code](https://chen.media/guides/rewind-claude-code-to-the-step-that-broke-your-code)
  ↳ *part-of* `g02-0117`

- `g02-0125` *STATED* — The Time Machine command /tm branch <n> tries another path from step n.
  — [g-rewind-claude-code-to-the-step-that-broke-your-code](https://chen.media/guides/rewind-claude-code-to-the-step-that-broke-your-code)
  ↳ *part-of* `g02-0117`
  ↳ *depends-on* `g02-0120`

- `g02-0126` *STATED* — The Time Machine command /tm compare puts two runs side by side.
  — [g-rewind-claude-code-to-the-step-that-broke-your-code](https://chen.media/guides/rewind-claude-code-to-the-step-that-broke-your-code)
  ↳ *part-of* `g02-0117`

- `g02-0127` *STATED* — The Time Machine command /tm rerun repeats a step with the same input.
  — [g-rewind-claude-code-to-the-step-that-broke-your-code](https://chen.media/guides/rewind-claude-code-to-the-step-that-broke-your-code)
  ↳ *part-of* `g02-0117`

- `g02-0199` *STATED* — To see your loops, type 'what scheduled tasks do I have?' in the Claude Code session where you started the loop.
  > “what scheduled tasks do I have?”
  — [g-find-the-claude-code-loops-that-are-quietly-eating-your-limit](https://chen.media/guides/find-the-claude-code-loops-that-are-quietly-eating-your-limit)
  ↳ *leads-to* `g02-0200`

- `g02-0217` *STATED* — Video Use keeps session memory in project.md, so next week's session picks up where you left off.
  — [g-video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video](https://chen.media/guides/video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video)
  ↳ *part-of* `g02-0207`
  ↳ *contrast* `g02-0043` — session state kept in project.md vs a pre-compact snapshot

- `g03-0002` *CORE* — Most of Alex Chen's settings guides open the same way: update Claude Code, run claude --version, and confirm a minimum version (2.1.234, 2.1.257, 2.1.290, 2.1.296, 2.1.299) before changing the setting.
  — [g-stop-file-mentions-from-pasting-whole-files-into-your-claude-chat](https://chen.media/guides/stop-file-mentions-from-pasting-whole-files-into-your-claude-chat) [g-let-claude-code-wait-out-your-limit-and-carry-on](https://chen.media/guides/let-claude-code-wait-out-your-limit-and-carry-on) [g-stop-claude-goal-check-ins-from-eating-your-limit](https://chen.media/guides/stop-claude-goal-check-ins-from-eating-your-limit) [g-run-every-claude-helper-agent-on-haiku](https://chen.media/guides/run-every-claude-helper-agent-on-haiku) [g-stop-claude-running-out-of-web-searches](https://chen.media/guides/stop-claude-running-out-of-web-searches) [g-make-your-claude-helpers-summarize-themselves-sooner](https://chen.media/guides/make-your-claude-helpers-summarize-themselves-sooner)

- `g03-0003` *CORE* — Env settings added to ~/.claude/settings.json only take effect in a new Claude Code session: start a new session so it reads the setting.
  — [g-stop-claude-goal-check-ins-from-eating-your-limit](https://chen.media/guides/stop-claude-goal-check-ins-from-eating-your-limit) [g-run-every-claude-helper-agent-on-haiku](https://chen.media/guides/run-every-claude-helper-agent-on-haiku)

- `g03-0021` *STATED* — His three-move CLAUDE.md fix: see what it costs, split it (move rarely used steps into skills), and keep it short (under 200 lines).
  > “Here's how to see it, split it, and keep it short.”
  — [g-shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit](https://chen.media/guides/shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit)
  ↳ *part-of* `g03-0009`
  ↳ *example-of* `g18-0284`

- `g03-0023` *STATED* — Count your CLAUDE.md lines by asking Claude: "how many lines is my CLAUDE.md?"
  > “how many lines is my CLAUDE.md?”
  — [g-shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit](https://chen.media/guides/shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit)
  ↳ *part-of* `g03-0021`
  ↳ *depends-on* `g03-0020`

- `g03-0032` *STATED* — Step 1 for path-only @ mentions: update Claude Code, then run claude --version to check you are on 2.1.299 or later.
  — [g-stop-file-mentions-from-pasting-whole-files-into-your-claude-chat](https://chen.media/guides/stop-file-mentions-from-pasting-whole-files-into-your-claude-chat)
  ↳ *example-of* `g03-0002`
  ↳ *depends-on* `g03-0031`

- `g03-0033` *STATED* — Step 2 of the @ mention guide is turning the path-only setting on, followed by sections "What changes" and "The catch" (what you give up).
  — [g-stop-file-mentions-from-pasting-whole-files-into-your-claude-chat](https://chen.media/guides/stop-file-mentions-from-pasting-whole-files-into-your-claude-chat)
  ↳ *example-of* `g03-0006`
  ↳ *part-of* `g03-0030`

- `g03-0054` *STATED* — Turn on the retry watchdog by setting the environment variable CLAUDE_CODE_RETRY_WATCHDOG to 1 before the run, e.g. export CLAUDE_CODE_RETRY_WATCHDOG=1.
  > “export CLAUDE_CODE_RETRY_WATCHDOG=1”
  — [g-keep-claude-retrying-overnight-when-the-api-is-busy](https://chen.media/guides/keep-claude-retrying-overnight-when-the-api-is-busy)
  ↳ *part-of* `g03-0053`
  ↳ *enables* `g03-0056`
  ↳ *example-of* `g03-0004`
  ↳ *part-of* `g03-0010`

- `g03-0057` *STATED* — With the watchdog set, start the overnight job the normal way, e.g. claude -p "your task here".
  > “claude -p "your task here"”
  — [g-keep-claude-retrying-overnight-when-the-api-is-busy](https://chen.media/guides/keep-claude-retrying-overnight-when-the-api-is-busy)
  ↳ *depends-on* `g03-0054`

- `g03-0058` *STATED* — Step 2 of the retry guide: cap how long the watchdog waits (the second setting).
  — [g-keep-claude-retrying-overnight-when-the-api-is-busy](https://chen.media/guides/keep-claude-retrying-overnight-when-the-api-is-busy)
  ↳ *part-of* `g03-0053`
  ↳ *qualifies* `g03-0056`

- `g03-0083` *STATED* — Start a background Claude Code session from the terminal with: claude --bg "fix the failing tests".
  > “claude --bg "fix the failing tests"”
  — [g-keep-claude-working-after-you-close-the-terminal](https://chen.media/guides/keep-claude-working-after-you-close-the-terminal)
  ↳ *example-of* `g03-0081`
  ↳ *part-of* `g03-0010`

- `g03-0084` *STATED* — Name a background session with --name: claude --bg --name "flaky-test-fix" "fix the failing tests".
  > “claude --bg --name "flaky-test-fix" "fix the failing tests"”
  — [g-keep-claude-working-after-you-close-the-terminal](https://chen.media/guides/keep-claude-working-after-you-close-the-terminal)
  ↳ *qualifies* `g03-0083`

- `g03-0085` *STATED* — Inside a running session type /bg (or /background) to move the conversation into the background; you can add a prompt, e.g. /bg run the test suite.
  > “/bg run the test suite”
  — [g-keep-claude-working-after-you-close-the-terminal](https://chen.media/guides/keep-claude-working-after-you-close-the-terminal)
  ↳ *contrast* `g03-0081` — /bg moves an existing session; --bg starts a new one

- `g03-0087` *STATED* — Step 2 of the background-session guide: find it again by listing every session, reopening one by part of its name, and reading what it did.
  — [g-keep-claude-working-after-you-close-the-terminal](https://chen.media/guides/keep-claude-working-after-you-close-the-terminal)
  ↳ *depends-on* `g03-0084` — reopen by part of its name

- `g03-0113` *STATED* — Step 1 of rewinding: press Escape once to stop Claude if it is still working.
  — [g-rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it](https://chen.media/guides/rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it)
  ↳ *leads-to* `g03-0114`

- `g03-0114` *STATED* — With the prompt box empty, press Escape twice, or type /rewind, to open the rewind menu.
  > “press Escape twice. Or type /rewind.”
  — [g-rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it](https://chen.media/guides/rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it)
  ↳ *enables* `g03-0116`

- `g03-0117` *STATED* — Step 2 of rewinding: pick the message before the mistake; the guide also covers what comes back in the prompt box.
  — [g-rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it](https://chen.media/guides/rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it)
  ↳ *depends-on* `g03-0116`

- `g03-0158` *STATED* — Press Shift+Tab until the status bar under the prompt says "plan mode on"; the cycle runs manual, accept edits, plan.
  > “plan mode on”
  — [g-turn-on-plan-mode-so-claude-plans-before-it-edits](https://chen.media/guides/turn-on-plan-mode-so-claude-plans-before-it-edits)
  ↳ *enables* `g03-0156`
  ↳ *enables* `r01-0185`

- `g03-0159` *STATED* — Start a single prompt in plan mode by beginning it with /plan.
  — [g-turn-on-plan-mode-so-claude-plans-before-it-edits](https://chen.media/guides/turn-on-plan-mode-so-claude-plans-before-it-edits)
  ↳ *enables* `g03-0156`

- `g03-0160` *STATED* — Start a whole Claude Code session in plan mode with: claude --permission-mode plan.
  > “claude --permission-mode plan”
  — [g-turn-on-plan-mode-so-claude-plans-before-it-edits](https://chen.media/guides/turn-on-plan-mode-so-claude-plans-before-it-edits)
  ↳ *enables* `g03-0156`

- `g03-0161` *STATED* — Press Shift+Tab again to leave plan mode without approving a plan.
  — [g-turn-on-plan-mode-so-claude-plans-before-it-edits](https://chen.media/guides/turn-on-plan-mode-so-claude-plans-before-it-edits)
  ↳ *qualifies* `g03-0158`

- `g03-0162` *STATED* — Step 2 of plan mode: let Claude write the plan, then approve or change it.
  — [g-turn-on-plan-mode-so-claude-plans-before-it-edits](https://chen.media/guides/turn-on-plan-mode-so-claude-plans-before-it-edits)
  ↳ *part-of* `g03-0156`

- `g03-0163` *STATED* — Plan mode can be made the default for a project (locked section "Make it the default for a project").
  — [g-turn-on-plan-mode-so-claude-plans-before-it-edits](https://chen.media/guides/turn-on-plan-mode-so-claude-plans-before-it-edits)
  ↳ *generalizes* `g03-0160`

- `g03-0168` *STATED* — To check auto-continue is available, update Claude Code and confirm claude --version says 2.1.234 or higher.
  — [g-let-claude-code-wait-out-your-limit-and-carry-on](https://chen.media/guides/let-claude-code-wait-out-your-limit-and-carry-on)
  ↳ *example-of* `g03-0002`
  ↳ *depends-on* `g03-0166`

- `g03-0191` *STATED* — Turning off goal check-ins needs Claude Code 2.1.234 or higher (check with claude --version).
  — [g-stop-claude-goal-check-ins-from-eating-your-limit](https://chen.media/guides/stop-claude-goal-check-ins-from-eating-your-limit)
  ↳ *example-of* `g03-0002`
  ↳ *depends-on* `g03-0192`

- `g03-0193` *STATED* — After adding CLAUDE_CODE_GOAL_CHECKIN_MINUTES, start a new Claude Code session so it reads the setting.
  — [g-stop-claude-goal-check-ins-from-eating-your-limit](https://chen.media/guides/stop-claude-goal-check-ins-from-eating-your-limit)
  ↳ *example-of* `g03-0003`
  ↳ *depends-on* `g03-0192`
  ↳ *example-of* `g03-0004`

- `g03-0194` *STATED* — Step 2 of the goal check-in guide: check the setting worked.
  — [g-stop-claude-goal-check-ins-from-eating-your-limit](https://chen.media/guides/stop-claude-goal-check-ins-from-eating-your-limit)
  ↳ *qualifies* `g03-0192`

- `g03-0214` *STATED* — Forcing subagents onto Haiku needs Claude Code 2.1.257 or higher (check with claude --version).
  — [g-run-every-claude-helper-agent-on-haiku](https://chen.media/guides/run-every-claude-helper-agent-on-haiku)
  ↳ *example-of* `g03-0002`
  ↳ *depends-on* `g03-0215`
  ↳ *part-of* `g19-0067`

- `g03-0217` *STATED* — After adding the subagent model lines, start a new Claude Code session so it reads the settings.
  — [g-run-every-claude-helper-agent-on-haiku](https://chen.media/guides/run-every-claude-helper-agent-on-haiku)
  ↳ *example-of* `g03-0003`
  ↳ *depends-on* `g03-0215`

- `g03-0218` *STATED* — Step 2 of the Haiku guide: check the helpers actually run on Haiku.
  — [g-run-every-claude-helper-agent-on-haiku](https://chen.media/guides/run-every-claude-helper-agent-on-haiku)
  ↳ *qualifies* `g03-0215`

- `g03-0246` *STATED* — On a Claude Code version older than 2.1.290, update first to get the web search refill.
  — [g-stop-claude-running-out-of-web-searches](https://chen.media/guides/stop-claude-running-out-of-web-searches)
  ↳ *example-of* `g03-0002`
  ↳ *depends-on* `g03-0245`

- `g03-0247` *STATED* — If searches start showing as calls that did nothing during a big research job, you hit the web search limit: wait for the refill or change the settings.
  — [g-stop-claude-running-out-of-web-searches](https://chen.media/guides/stop-claude-running-out-of-web-searches)
  ↳ *qualifies* `g03-0243`
  ↳ *leads-to* `g03-0245`

- `g03-0251` *STATED* — Early subagent compaction needs Claude Code v2.1.296 or later (check with claude --version).
  — [g-make-your-claude-helpers-summarize-themselves-sooner](https://chen.media/guides/make-your-claude-helpers-summarize-themselves-sooner)
  ↳ *example-of* `g03-0002`
  ↳ *depends-on* `g03-0250`
  ↳ *evidence-for* `g04-0206`

- `g04-0044` *STATED* — Harvey setup step 4: inside the repo, tell Claude Code 'set up Harvey for me'.
  > “Say: set up Harvey for me.”
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *leads-to* `g04-0047`
  ↳ *depends-on* `g04-0045`

- `g04-0066` *INFERRED* — To make a guard hook fail closed, add "onFailure": "block" to that command or HTTP hook entry in your Claude Code settings.
  — [g-make-a-crashed-claude-hook-block-the-action-not-let-it-through](https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through)
  ↳ *depends-on* `g04-0059`
  ↳ *depends-on* `g04-0058`
  ↳ *leads-to* `g04-0067`
  ↳ *contrast* `g04-0056`

- `g04-0067` *STATED* — Alex's onFailure guide includes a two-minute test to confirm a broken hook now blocks (section 'Test it in two minutes', 2 copyable prompts, 5 steps).
  — [g-make-a-crashed-claude-hook-block-the-action-not-let-it-through](https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through)

- `g04-0087` *STATED* — A Claude Code hook that keeps only the failing test lines stops the test-output waste.
  — [g-the-claude-hook-that-cuts-test-output-down-to-just-the-failures](https://chen.media/guides/the-claude-hook-that-cuts-test-output-down-to-just-the-failures)
  ↳ *because* `g04-0086`
  ↳ *part-of* `g04-0096`

- `g04-0089` *STATED* — The test-filter is a PreToolUse hook on Bash, which runs before every command Claude issues.
  — [g-the-claude-hook-that-cuts-test-output-down-to-just-the-failures](https://chen.media/guides/the-claude-hook-that-cuts-test-output-down-to-just-the-failures)
  ↳ *part-of* `g04-0087`
  ↳ *example-of* `g01-0126`

- `g04-0091` *STATED* — The test-filter hook rewrites the test command to pipe through grep, so only the failing lines and five lines after each come back.
  — [g-the-claude-hook-that-cuts-test-output-down-to-just-the-failures](https://chen.media/guides/the-claude-hook-that-cuts-test-output-down-to-just-the-failures)
  ↳ *part-of* `g04-0089`

- `g04-0094` *STATED* — Installing the test-filter hook is three steps: save the script, turn it on with a settings entry, and check it worked (bodies locked; 2 copyable prompts).
  — [g-the-claude-hook-that-cuts-test-output-down-to-just-the-failures](https://chen.media/guides/the-claude-hook-that-cuts-test-output-down-to-just-the-failures)
  ↳ *part-of* `g04-0096`

- `g04-0206` *STATED* — Before adding the subagent compaction line, update Claude Code, then run claude --version to check you are on 2.1.296 or later.
  — [g-make-your-claude-helper-agents-compact-their-own-chat-early](https://chen.media/guides/make-your-claude-helper-agents-compact-their-own-chat-early)
  ↳ *depends-on* `g04-0205`
  ↳ *example-of* `g03-0002`

- `g04-0227` *STATED* — Alex's AirLLM guide includes ready-made prompts so Claude Code can set AirLLM up for you (section 'Let Claude Code set it up for you').
  — [g-run-the-biggest-open-ai-model-on-a-cheap-graphics-card-set-up-the-free-airllm-li](https://chen.media/guides/run-the-biggest-open-ai-model-on-a-cheap-graphics-card-set-up-the-free-airllm-li)
  ↳ *part-of* `g04-0229`

- `g04-0233` *STATED* — Advisor setup step 1: switch your main model to Sonnet with /model.
  — [g-let-opus-advise-while-sonnet-does-the-routine-work](https://chen.media/guides/let-opus-advise-while-sonnet-does-the-routine-work)
  ↳ *part-of* `g04-0232`
  ↳ *leads-to* `g04-0234`
  ↳ *qualifies* `g05-0152`

- `g04-0234` *STATED* — Advisor setup step 2: run /advisor opus; Claude Code confirms with 'Advisor set to' and saves it as your default.
  — [g-let-opus-advise-while-sonnet-does-the-routine-work](https://chen.media/guides/let-opus-advise-while-sonnet-does-the-routine-work)
  ↳ *part-of* `g04-0232`
  ↳ *leads-to* `g04-0237`
  ↳ *example-of* `g11-0099`

- `g04-0235` *STATED* — To set the advisor for one session only, launch with: claude --advisor opus
  — [g-let-opus-advise-while-sonnet-does-the-routine-work](https://chen.media/guides/let-opus-advise-while-sonnet-does-the-routine-work)
  ↳ *contrast* `g04-0234` — per-session vs saved default

- `g04-0236` *STATED* — To save the advisor in settings, add "advisorModel": "opus".
  — [g-let-opus-advise-while-sonnet-does-the-routine-work](https://chen.media/guides/let-opus-advise-while-sonnet-does-the-routine-work)
  ↳ *contrast* `g04-0234` — settings file vs slash command

- `g04-0237` *STATED* — Once an advisor is set, you let Claude call it itself when it needs advice (section 'Step 2: let Claude call it', body locked).
  — [g-let-opus-advise-while-sonnet-does-the-routine-work](https://chen.media/guides/let-opus-advise-while-sonnet-does-the-routine-work)
  ↳ *evidence-for* `g11-0106`

- `g05-0064` *STATED* — In Claude Code you can type a new message and press Enter while Claude is working, to steer the run without stopping it.
  — [g-your-opus-5-5-prompt-checklist](https://chen.media/guides/your-opus-5-5-prompt-checklist)
  ↳ *part-of* `g05-0056`
  ↳ *qualifies* `g05-0063` — you can still add instructions mid-run

- `g05-0066` *STATED* — Opus 5.5 checklist 4: put stop rules in your CLAUDE.md.
  — [g-your-opus-5-5-prompt-checklist](https://chen.media/guides/your-opus-5-5-prompt-checklist)
  ↳ *part-of* `g05-0056`
  ↳ *part-of* `g05-0319`

- `g05-0104` *STATED* — Install Effortless, step 3 — run /reload-plugins, or restart Claude Code.
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless)
  ↳ *depends-on* `g05-0103`

- `g05-0167` *STATED* — Set a subagent's effort in its file: in .claude/agents/renamer.md add effort: low to the frontmatter.
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)
  ↳ *part-of* `g05-0161`
  ↳ *part-of* `g10-0173`

- `g05-0173` *STATED* — /tasks names the model on each subagent's row and adds the effort level set for it (Claude Code v2.1.242 or later).
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)
  ↳ *part-of* `g05-0161`
  ↳ *example-of* `g05-0326`

- `g06-0057` *STATED* — Alex's paste-into-Claude-Code prompt for MiniCPM: have Claude check your free disk space, run ollama run openbmb/minicpm-v4.7:1b, say when the chat is ready, and ask before downloading the 22 GB 35B version.
  > “Check how much free disk space I have. Then run `ollama run openbmb/minicpm-v4.7:1b` (the small 1.8 GB version) and tell me when the chat is ready. Ask me before downloading the 22 GB 35B version.”
  — [g-run-minicpm-v-4-7-a-free-35b-ai-on-your-laptop-or-iphone](https://chen.media/guides/run-minicpm-v-4-7-a-free-35b-ai-on-your-laptop-or-iphone)
  ↳ *because* `g06-0054`
  ↳ *depends-on* `g06-0055`
  ↳ *example-of* `g06-0261`

- `g06-0067` *STATED* — Settings-file equivalent of /autocompact: add "autoCompactWindow": 200000 to ~/.claude/settings.json.
  — [g-make-claude-compact-earlier-the-setting-and-the-claude-md-note](https://chen.media/guides/make-claude-compact-earlier-the-setting-and-the-claude-md-note)
  ↳ *qualifies* `g06-0064` — settings-file equivalent
  ↳ *part-of* `g06-0267`

- `g06-0068` *STATED* — For one launch only, start Claude Code with: claude --autocompact 200k
  — [g-make-claude-compact-earlier-the-setting-and-the-claude-md-note](https://chen.media/guides/make-claude-compact-earlier-the-setting-and-the-claude-md-note)
  ↳ *qualifies* `g06-0064` — single-launch equivalent

- `g06-0071` *STATED* — Step 2 of earlier compaction is a short CLAUDE.md note telling Claude what to keep when it summarizes (the note's wording is in the gated 'Step 2: tell it what to keep').
  — [g-make-claude-compact-earlier-the-setting-and-the-claude-md-note](https://chen.media/guides/make-claude-compact-earlier-the-setting-and-the-claude-md-note)
  ↳ *part-of* `g06-0063`
  ↳ *depends-on* `g06-0241` — the compaction note lives in CLAUDE.md

- `g06-0100` *STATED* — Claude Code voice requires signing in with your Claude.ai account; run /login if /voice says it is unknown.
  — [g-talk-to-claude-code-instead-of-typing](https://chen.media/guides/talk-to-claude-code-instead-of-typing)
  ↳ *qualifies* `g06-0101`

- `g06-0101` *STATED* — Turn on voice by typing /voice in Claude Code; on a Mac, allow the microphone for your terminal when asked.
  — [g-talk-to-claude-code-instead-of-typing](https://chen.media/guides/talk-to-claude-code-instead-of-typing)
  ↳ *part-of* `g06-0096`
  ↳ *leads-to* `g06-0102`

- `g06-0102` *STATED* — Using Claude Code voice: hold Space and speak, let go to finish, your words appear in the prompt, then press Enter to send.
  — [g-talk-to-claude-code-instead-of-typing](https://chen.media/guides/talk-to-claude-code-instead-of-typing)

- `g06-0103` *STATED* — Claude Code has settings that make voice dictation faster (gated section 'Step 2: make it faster').
  — [g-talk-to-claude-code-instead-of-typing](https://chen.media/guides/talk-to-claude-code-instead-of-typing)
  ↳ *qualifies* `g06-0102`

- `g06-0110` *STATED* — magpie step 2 points Claude Code at a chosen model with one command (the command is in the gated 'Step 2: point Claude Code at a model').
  — [g-keep-claude-code-working-after-your-limit-runs-out](https://chen.media/guides/keep-claude-code-working-after-your-limit-runs-out)
  ↳ *leads-to* `g06-0111`

- `g06-0146` *STATED* — Switching Claude Code to Sonnet 5.5 is a single step ('Step 1: switch'); the exact command is in the gated part of the guide.
  — [g-set-up-claude-sonnet-5-5-the-model-that-beats-opus-5-5-at-coding](https://chen.media/guides/set-up-claude-sonnet-5-5-the-model-that-beats-opus-5-5-at-coding)
  ↳ *part-of* `g06-0148`

- `g06-0221` *STATED* — Haiku helper step 1: create the folder .claude/agents in your project, or use ~/.claude/agents to have the helper in every project.
  — [g-make-your-claude-limit-last-the-haiku-helper-and-3-habits](https://chen.media/guides/make-your-claude-limit-last-the-haiku-helper-and-3-habits)
  ↳ *leads-to* `g06-0222`
  ↳ *evidence-for* `g03-0222`

- `g06-0222` *STATED* — Haiku helper step 2: create a file called haiku-helper.md in the agents folder and paste the helper definition.
  — [g-make-your-claude-limit-last-the-haiku-helper-and-3-habits](https://chen.media/guides/make-your-claude-limit-last-the-haiku-helper-and-3-habits)
  ↳ *leads-to* `g06-0223`
  ↳ *enables* `g06-0220`
  ↳ *evidence-for* `g07-0113`

- `g06-0223` *STATED* — Haiku helper step 3: open Claude Code and check with /agents that haiku-helper is listed.
  — [g-make-your-claude-limit-last-the-haiku-helper-and-3-habits](https://chen.media/guides/make-your-claude-limit-last-the-haiku-helper-and-3-habits)
  ↳ *evidence-for* `g19-0071`

- `g06-0244` *STATED* — Notebook step 1: generate your CLAUDE.md (method in the gated 'Step 1: generate your CLAUDE.md').
  — [g-give-claude-a-notebook-that-survives-every-chat-reset](https://chen.media/guides/give-claude-a-notebook-that-survives-every-chat-reset)
  ↳ *enables* `g06-0241`

- `g06-0245` *STATED* — Notebook step 2: let Claude take its own notes with auto memory (gated 'Step 2: let Claude take its own notes').
  — [g-give-claude-a-notebook-that-survives-every-chat-reset](https://chen.media/guides/give-claude-a-notebook-that-survives-every-chat-reset)
  ↳ *enables* `g06-0242`

- `g07-0014` *STATED* — To accept Claude Code's grey next-prompt suggestion, press Tab, then Enter, and you are on to the next step without typing.
  — [g-let-claude-code-write-your-next-prompt-press-tab](https://chen.media/guides/let-claude-code-write-your-next-prompt-press-tab)
  ↳ *part-of* `g07-0013`

- `g07-0015` *STATED* — After finishing a task in Claude Code, look at the prompt box: if there is grey text, that is the next-prompt suggestion.
  — [g-let-claude-code-write-your-next-prompt-press-tab](https://chen.media/guides/let-claude-code-write-your-next-prompt-press-tab)
  ↳ *part-of* `g07-0013`
  ↳ *leads-to* `g07-0016`

- `g07-0016` *STATED* — Press Tab or the Right arrow to put Claude Code's prompt suggestion into the input box, then Enter to send it.
  — [g-let-claude-code-write-your-next-prompt-press-tab](https://chen.media/guides/let-claude-code-write-your-next-prompt-press-tab)
  ↳ *part-of* `g07-0013`
  ↳ *qualifies* `g07-0014` — Right arrow is an alternative to Tab

- `g07-0019` *STATED* — Claude Code's next-prompt suggestions can be turned on or off ('Step 2: turn it on or off'; the exact setting is email-gated).
  — [g-let-claude-code-write-your-next-prompt-press-tab](https://chen.media/guides/let-claude-code-write-your-next-prompt-press-tab)
  ↳ *part-of* `g07-0013`

- `g07-0110` *STATED* — A short note in your CLAUDE.md tells Opus which jobs to hand to the Haiku helper.
  — [g-make-claude-code-limit-last-longer-haiku-5-5-helper](https://chen.media/guides/make-claude-code-limit-last-longer-haiku-5-5-helper)
  ↳ *part-of* `g07-0104`
  ↳ *part-of* `g07-0113`
  ↳ *defines* `g07-0111`

- `g07-0113` *INFERRED* — The Haiku helper's two files are a Haiku-model helper agent definition ('Step 1: add the Haiku helper') and a CLAUDE.md delegation note ('Step 2: tell Opus when to use it').
  — [g-make-claude-code-limit-last-longer-haiku-5-5-helper](https://chen.media/guides/make-claude-code-limit-last-longer-haiku-5-5-helper)
  ↳ *part-of* `g07-0104`
  ↳ *example-of* `g19-0068`

- `g07-0114` *STATED* — Alex's guide shows how to check the Haiku helper is actually being used ('Step 3: check it's working'; email-gated).
  — [g-make-claude-code-limit-last-longer-haiku-5-5-helper](https://chen.media/guides/make-claude-code-limit-last-longer-haiku-5-5-helper)
  ↳ *part-of* `g07-0104`
  ↳ *qualifies* `g07-0110`

- `g07-0166` *STATED* — To make a mod, you describe the mod you want and Claude writes it.
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`
  ↳ *evidence-for* `g10-0064`

- `g07-0172` *STATED* — Check your Claude Code version with `claude --version` and update if it's older than 2.1.287 before trying mods.
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`
  ↳ *leads-to* `g07-0177`
  ↳ *example-of* `g03-0002`

- `g07-0177` *STATED* — Alex's mods guide gives the exact commands to get Anthropic's three sample mods ('Step 1: get the three sample mods'; email-gated).
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`
  ↳ *leads-to* `g07-0178`

- `g07-0178` *STATED* — After trying the sample mods, keep the ones you like ('Step 5: keep the ones you like'; email-gated).
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`
  ↳ *leads-to* `g07-0179`

- `g07-0179` *STATED* — Alex's mods guide includes a prompt to have Claude build your own mod ('Step 6: have Claude build your own'; email-gated).
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`
  ↳ *example-of* `g07-0166`

- `g07-0191` *STATED* — If you see Projects in the left sidebar at claude.ai/code or in the Code tab of the desktop app, you're in.
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`
  ↳ *leads-to* `g07-0192` — if not in sidebar, join waitlist

- `g07-0192` *STATED* — If you don't see Projects, join the waitlist; Anthropic says it's letting in more Pro and Max users as capacity allows.
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`

- `g07-0196` *STATED* — Projects needs GitHub connected in a specific way ('Step 2: connect GitHub the way Projects needs it'; email-gated).
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`
  ↳ *leads-to* `g07-0197`
  ↳ *enables* `g07-0187`

- `g07-0197` *STATED* — After connecting GitHub, create the project ('Step 3: create the project'; email-gated).
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`
  ↳ *leads-to* `g07-0198`

- `g07-0242` *STATED* — Alex's AirLLM guide includes ready-made prompts to have Claude Code set AirLLM up for you ('Let Claude Code set it up for you'; email-gated).
  — [g-run-a-70b-ai-model-on-a-4gb-graphics-card-set-up-the-free-airllm-library](https://chen.media/guides/run-a-70b-ai-model-on-a-4gb-graphics-card-set-up-the-free-airllm-library)
  ↳ *part-of* `g07-0224`
  ↳ *generalizes* `g07-0240`

- `g08-0109` *STATED* — Claude Motion has eligibility and a way to turn it on, covered in the guide section 'Who has it, and how to turn it on' (body locked).
  — [g-make-animated-explainer-videos-inside-claude-try-the-new-claude-motion](https://chen.media/guides/make-animated-explainer-videos-inside-claude-try-the-new-claude-motion)
  ↳ *qualifies* `g08-0114`

- `g08-0115` *STATED* — To start Claude Motion, type /motion in the Claude message box; Anthropic's launch page says this brings up the Motion option.
  — [g-make-animated-explainer-videos-inside-claude-try-the-new-claude-motion](https://chen.media/guides/make-animated-explainer-videos-inside-claude-try-the-new-claude-motion)
  ↳ *part-of* `g08-0106`
  ↳ *leads-to* `g08-0117`

- `g08-0116` *STATED* — Other ways into Claude Motion: select "Output" in the message box and choose "Motion", or ask for an animation in any chat.
  — [g-make-animated-explainer-videos-inside-claude-try-the-new-claude-motion](https://chen.media/guides/make-animated-explainer-videos-inside-claude-try-the-new-claude-motion)
  ↳ *contrast* `g08-0115` — alternative entry points

- `g08-0119` *STATED* — Send the Motion prompt and watch what Claude builds; it plays in Claude like a short video.
  — [g-make-animated-explainer-videos-inside-claude-try-the-new-claude-motion](https://chen.media/guides/make-animated-explainer-videos-inside-claude-try-the-new-claude-motion)
  ↳ *part-of* `g08-0106`
  ↳ *leads-to* `g08-0120`

- `g08-0121` *STATED* — To get the file out of Claude Motion, click Export and choose MP4.
  — [g-make-animated-explainer-videos-inside-claude-try-the-new-claude-motion](https://chen.media/guides/make-animated-explainer-videos-inside-claude-try-the-new-claude-motion)
  ↳ *part-of* `g08-0106`

- `g08-0196` *STATED* — With /bouncer you type the task, and nothing gets changed that the task didn't need.
  — [g-stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes](https://chen.media/guides/stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes)
  ↳ *part-of* `g08-0191`
  ↳ *example-of* `g08-0260`

- `g08-0197` *STATED* — /bouncer step THE ASK: Claude writes what you asked for in one sentence, and that is the only thing allowed through the door.
  — [g-stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes](https://chen.media/guides/stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes)
  ↳ *part-of* `g08-0191`
  ↳ *leads-to* `g08-0198`

- `g08-0198` *STATED* — /bouncer step THE LIST: before it edits anything, Claude writes down every change it is thinking of making, including the tempting extras.
  — [g-stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes](https://chen.media/guides/stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes)
  ↳ *part-of* `g08-0191`
  ↳ *leads-to* `g08-0199`

- `g08-0199` *STATED* — /bouncer step THE DOOR: each listed change is checked against the ask; needed to do the task gets a tick, while not asked for, or the task works without it, is NOT ON THE LIST.
  > “NOT ON THE LIST”
  — [g-stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes](https://chen.media/guides/stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes)
  ↳ *part-of* `g08-0191`
  ↳ *leads-to* `g08-0200`
  ↳ *depends-on* `g08-0197`

- `g08-0200` *STATED* — /bouncer makes only the ticked changes, then reports what was done and what was turned away, so you can say "yes, do that one" if you want it.
  > “"yes, do that one"”
  — [g-stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes](https://chen.media/guides/stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes)
  ↳ *part-of* `g08-0191`

- `g08-0207` *STATED* — A Claude Code setting can make your computer tell you the moment a session needs your answer (section 'Make your computer tell you when a session needs you', body locked).
  — [g-see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office](https://chen.media/guides/see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office)
  ↳ *part-of* `g08-0209`
  ↳ *qualifies* `g09-0231`

- `g08-0208` *INFERRED* — Claude Code's built-in ways to be pinged when a session needs you are the notification channel option in /config (e.g. terminal bell) and a Notification hook in settings.json; the locked section likely uses one of these.
  — [g-see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office](https://chen.media/guides/see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office)
  ↳ *qualifies* `g08-0207`

- `g08-0243` *STATED* — With /trojan you type the file's path and get back what is hiding inside, BEFORE Claude reads the file.
  — [g-stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes](https://chen.media/guides/stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes)
  ↳ *part-of* `g08-0237`
  ↳ *example-of* `g08-0260`

- `g08-0244` *STATED* — /trojan step 1: Claude runs a small scan on the file and never opens the file itself, because the file is the thing you don't trust.
  > “It never opens the file itself, because the file is the thing you don't trust.”
  — [g-stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes](https://chen.media/guides/stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes)
  ↳ *part-of* `g08-0237`
  ↳ *leads-to* `g08-0245`
  ↳ *example-of* `g08-0253`

- `g08-0245` *STATED* — /trojan CHECK 1, INVISIBLE TEXT: flags every line a person can't see, like white text, tiny text, hidden text, comments and invisible characters.
  — [g-stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes](https://chen.media/guides/stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes)
  ↳ *part-of* `g08-0237`
  ↳ *leads-to* `g08-0246`
  ↳ *qualifies* `g08-0240` — check 1 targets the hiding techniques

- `g08-0246` *STATED* — /trojan CHECK 2, ORDERS FOR AN AI: flags every sentence that tells an AI what to do (ignore your rules, send something, reveal something), and whether it was hidden or in plain sight.
  — [g-stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes](https://chen.media/guides/stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes)
  ↳ *part-of* `g08-0237`
  ↳ *leads-to* `g08-0247`

- `g08-0247` *STATED* — /trojan CHECK 3, THE RED LINES: marks every hidden order with a red dot so you can see exactly what was planted, then gives a one-line verdict.
  — [g-stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes](https://chen.media/guides/stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes)
  ↳ *part-of* `g08-0237`

- `g08-0260` *STATED* — Alex's skills are invoked as slash commands in Claude Code: /hiring-panel, /heist, /jester, /bouncer, /rival and /trojan.
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill) [g-give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes](https://chen.media/guides/give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes) [g-stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes](https://chen.media/guides/stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes) [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill) [g-stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes](https://chen.media/guides/stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes) [g-give-claude-a-jester-that-tells-you-the-brutal-truth-set-up-jester-in-2-minutes](https://chen.media/guides/give-claude-a-jester-that-tells-you-the-brutal-truth-set-up-jester-in-2-minutes)

- `g09-0036` *STATED* — The lessons skill keeps its rules in a file called LESSONS.md in your project, and your CLAUDE.md pulls it in with one line, so every new session starts with every rule in it.
  > “A file called LESSONS.md sits in your project, and your CLAUDE.md pulls it in with one line”
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *enables* `g09-0034`
  ↳ *part-of* `g09-0031`
  ↳ *evidence-for* `r03-0008`
  ↳ *depends-on* `g20-0236`

- `g09-0037` *INFERRED* — The one line that pulls LESSONS.md into CLAUDE.md is most likely a Claude Code memory import such as '@LESSONS.md', which expands the file into context at session start.
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *qualifies* `g09-0036`
  ↳ *evidence-for* `r03-0015`

- `g09-0038` *STATED* — The lessons skill uses a hook that quietly notes every message of yours that sounds like a correction into a small inbox file on your computer.
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *part-of* `g09-0031`
  ↳ *leads-to* `g09-0042`
  ↳ *evidence-for* `r03-0012`

- `g09-0041` *INFERRED* — A hook that inspects every user message before Claude sees it corresponds to Claude Code's UserPromptSubmit hook event, exiting 0 so the prompt passes through.
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *qualifies* `g09-0038`

- `g09-0044` *STATED* — The lessons investigator writes what it found back into the rulebook, one short rule per lesson.
  > “one short rule per lesson”
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *part-of* `g09-0042`
  ↳ *leads-to* `g09-0034`
  ↳ *evidence-for* `r03-0010`

- `g09-0045` *STATED* — A mistake that comes back doesn't get a second rule in the rulebook: the old rule gets sharper.
  > “A mistake that comes back doesn't get a second rule: the old one gets sharper.”
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *qualifies* `g09-0044`
  ↳ *evidence-for* `r03-0011`

- `g09-0046` *STATED* — The lessons investigator also writes a dated note so you can read what it learned.
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *part-of* `g09-0042`

- `g09-0244` *INFERRED* — Connecting a monitor like Coucou to Claude Code most likely works by registering Claude Code hooks (tool-use, permission and Stop events) so the app sees each step, permission prompt and finish.
  — [g-coucou-free-notch-pet-that-watches-claude-code](https://chen.media/guides/coucou-free-notch-pet-that-watches-claude-code)
  ↳ *qualifies* `g09-0243`
  ↳ *generalizes* `g09-0041` — both integrate through Claude Code hooks
  ↳ *qualifies* `g01-0126`
  ↳ *enables* `g06-0113`

- `g10-0025` *STATED* — Alex Chen's Claude-app freeze guide gives a ten-second check to spot the memory leak and a checklist to run before every long session.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *qualifies* `g10-0024` — the checklist is the fix

- `g10-0027` *STATED* — Step 1 of the Claude app memory-leak checklist: the ten-second check that shows whether the leak is happening (details locked).
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *part-of* `g10-0025`

- `g10-0028` *STATED* — Step 2 of the Claude app memory-leak checklist: a checklist to run before every long Claude session.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *part-of* `g10-0025`

- `g10-0029` *STATED* — Step 3 of the Claude app memory-leak checklist: what to do before you walk away from the Mac (or go to bed) with Claude running.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *part-of* `g10-0025`
  ↳ *qualifies* `g10-0041`
  ↳ *part-of* `g10-0268`

- `g10-0030` *STATED* — Step 4 of the Claude app memory-leak checklist: what to do if the Mac freezes anyway.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *part-of* `g10-0025`

- `g10-0047` *STATED* — Alex Chen's Claude Code mods guide covers what mods are, the one setting that makes them show up, the exact install commands for each mod from his video, and the prompt to have Claude build your own.
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)

- `g10-0049` *STATED* — Step 1 for Claude Code mods: switch mods on with the one setting most people miss; mods do not show up without it (setting name locked).
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *part-of* `g10-0047`
  ↳ *enables* `g10-0046`
  ↳ *contradicts* `g07-0171` — mods guide: mods 'do not show up' without one setting most people miss vs sample-mods guide: mods are on by default in 2.1.287+

- `g10-0050` *STATED* — Step 2 for Claude Code mods: install Tetris above the chat box, and the pet that grows (install commands locked).
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *part-of* `g10-0047`
  ↳ *example-of* `g10-0055`

- `g10-0051` *STATED* — Step 3 for Claude Code mods: install live cartoons of whatever Claude is doing (install commands locked).
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *part-of* `g10-0047`
  ↳ *example-of* `g10-0055`

- `g10-0052` *STATED* — Step 4 for Claude Code mods: have Claude build any mod for you (prompt locked).
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *part-of* `g10-0047`

- `g10-0064` *STATED* — You don't have to write a Claude Code mod yourself: you can ask Claude to build it for you.
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *contrast* `g10-0063`
  ↳ *generalizes* `g10-0052`

- `g10-0065` *STATED* — Claude Code mods ship inside plugins, so you install them with /plugin, like any other plugin.
  > “They ship inside plugins, so you install them with /plugin, like any other plugin.”
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *depends-on* `g10-0056`
  ↳ *depends-on* `g18-0163`

- `g10-0069` *STATED* — Alex Chen's 5 rules keep your logins and API keys away from hackers and AI agents alike.
  — [g-openai-agents-hacked-hugging-face-5-login-rules](https://chen.media/guides/openai-agents-hacked-hugging-face-5-login-rules)
  ↳ *because* `g10-0068`

- `g10-0071` *STATED* — Login rule 1: never put an API key anywhere someone else can read it.
  — [g-openai-agents-hacked-hugging-face-5-login-rules](https://chen.media/guides/openai-agents-hacked-hugging-face-5-login-rules)
  ↳ *part-of* `g10-0069`
  ↳ *evidence-for* `g18-0260`

- `g10-0072` *STATED* — Login rule 2: give every API key the smallest job it needs (least privilege).
  — [g-openai-agents-hacked-hugging-face-5-login-rules](https://chen.media/guides/openai-agents-hacked-hugging-face-5-login-rules)
  ↳ *part-of* `g10-0069`
  ↳ *evidence-for* `y01-0058`

- `g10-0073` *STATED* — Login rule 3: expire API keys, rotate them, delete them.
  — [g-openai-agents-hacked-hugging-face-5-login-rules](https://chen.media/guides/openai-agents-hacked-hugging-face-5-login-rules)
  ↳ *part-of* `g10-0069`

- `g10-0074` *STATED* — Login rule 4: lock the account, not just the key.
  — [g-openai-agents-hacked-hugging-face-5-login-rules](https://chen.media/guides/openai-agents-hacked-hugging-face-5-login-rules)
  ↳ *part-of* `g10-0069`

- `g10-0076` *STATED* — Alex Chen's login-safety guide has a section 'If a key already leaked' with the recovery steps (body locked).
  — [g-openai-agents-hacked-hugging-face-5-login-rules](https://chen.media/guides/openai-agents-hacked-hugging-face-5-login-rules)
  ↳ *part-of* `g10-0069`

- `g10-0138` *STATED* — Step 2 of the overnight fix: put the keep-going paragraph where Claude reads it every time.
  — [g-claude-quits-long-jobs-halfway-the-keep-going-paragraph](https://chen.media/guides/claude-quits-long-jobs-halfway-the-keep-going-paragraph)
  ↳ *part-of* `g10-0136`
  ↳ *leads-to* `g10-0139`
  ↳ *example-of* `g05-0319`

- `g10-0176` *STATED* — Alex Chen's effort-levels guide includes 'The cheat sheet: which level for which job' (per-job mapping locked).
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *part-of* `g10-0174`

- `g10-0177` *STATED* — Alex Chen's effort-levels guide includes 'How to switch levels' (details locked).
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *part-of* `g10-0174`
  ↳ *qualifies* `g10-0181`

- `g10-0178` *STATED* — Alex Chen's effort-levels guide includes 'The loop Anthropic's engineer uses for new features' (loop locked).
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *part-of* `g10-0174`

- `g10-0179` *STATED* — Alex Chen's effort-levels guide includes 'When ultracode is worth it' (criteria locked).
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *part-of* `g10-0174`
  ↳ *part-of* `g10-0181`

- `g10-0181` *CORE* — Type /effort in Claude Code and you get a slider: low, medium, high, xhigh, max, and an Ultracode toggle under it.
  > “Type /effort in Claude Code and you get a slider: low, medium, high, xhigh, max, and an Ultracode toggle under it.”
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *defines* `g10-0173`

- `g11-0104` *STATED* — Advisor step 1: Opus stays your main model and does everything: it reads the files, writes the code, runs the commands.
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)
  ↳ *part-of* `g11-0099` — advisor mechanics
  ↳ *leads-to* `g11-0105`

- `g11-0105` *STATED* — Advisor step 2: Claude calls the advisor in before committing to an approach, when the same error keeps coming back, and before saying a task is done.
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)
  ↳ *part-of* `g11-0099` — advisor mechanics
  ↳ *leads-to* `g11-0107`

- `g11-0107` *STATED* — Advisor step 3: the advisor gets the whole conversation, every tool call and every result, not a summary.
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)
  ↳ *part-of* `g11-0099` — advisor mechanics
  ↳ *leads-to* `g11-0108`
  ↳ *contrast* `r01-0216`

- `g11-0108` *STATED* — Advisor step 4: the advisor sends back guidance and never touches a tool itself.
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)
  ↳ *part-of* `g11-0099` — advisor mechanics
  ↳ *leads-to* `g11-0109`

- `g11-0114` *STATED* — Alex sets the advisor up with one prompt (Step 1), then checks it's working (Step 2).
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)
  ↳ *leads-to* `g11-0110`
  ↳ *part-of* `g11-0099`

- `g11-0228` *STATED* — For developers, Alex's guide runs the same model test in the terminal.
  — [g-gemini-4-pro-leak-one-prompt-to-test-it-against-claude](https://chen.media/guides/gemini-4-pro-leak-one-prompt-to-test-it-against-claude)
  ↳ *part-of* `g11-0226`

- `g12-0024` *STATED* — Guide section 'How to switch models' covers switching between Sonnet 5.5 and Opus 5.5 (body email-gated).
  — [g-claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task](https://chen.media/guides/claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task)
  ↳ *part-of* `g12-0001`
  ↳ *enables* `g12-0026`

- `g12-0048` *STATED* — Guide section 'Where to paste it, once' covers putting the design rule somewhere persistent so Claude applies it to every later site (body email-gated).
  — [g-why-your-claude-built-website-looks-ai-made-10-tells-and-one-rule](https://chen.media/guides/why-your-claude-built-website-looks-ai-made-10-tells-and-one-rule)
  ↳ *part-of* `g12-0027`
  ↳ *enables* `g12-0035`
  ↳ *example-of* `g23-0199`

- `g12-0108` *STATED* — Guide section 'Run the audit' gives the one command that runs the CLAUDE.md prompt audit (body email-gated; 1 prompt to copy).
  — [g-clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit](https://chen.media/guides/clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit)
  ↳ *part-of* `g12-0091`
  ↳ *depends-on* `g12-0098`
  ↳ *evidence-for* `y03-0066`

- `g12-0110` *INFERRED* — CLAUDE.md cleanup for Opus 5.5: strip CRITICAL/MUST/ALWAYS shouting, delete 'double-check' or 'check twice' lines, and replace step-by-step scripts with the goal so the model plans itself.
  — [g-clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit](https://chen.media/guides/clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit)
  ↳ *depends-on* `g12-0102`
  ↳ *depends-on* `g12-0103`
  ↳ *depends-on* `g12-0104`
  ↳ *example-of* `g12-0106`

- `g12-0203` *STATED* — Set the verification loop up once so it runs the same way every time.
  — [g-how-to-make-claude-test-its-own-work-the-verification-loop](https://chen.media/guides/how-to-make-claude-test-its-own-work-the-verification-loop)
  ↳ *qualifies* `g12-0202`

- `g12-0211` *STATED* — The Claude Code team's everyday check pattern chains four steps: /code-review (bugs), /simplify (clean diff), /verify (the change works) and a custom /design skill (UI against guidelines).
  — [g-how-to-make-claude-test-its-own-work-the-verification-loop](https://chen.media/guides/how-to-make-claude-test-its-own-work-the-verification-loop)
  ↳ *example-of* `g12-0202`
  ↳ *evidence-for* `g12-0200`
  ↳ *part-of* `g12-0203`

- `g12-0212` *STATED* — Guide section 'Start with the built-in /verify' says /verify is built into Claude Code and is the place to start (body email-gated).
  — [g-how-to-make-claude-test-its-own-work-the-verification-loop](https://chen.media/guides/how-to-make-claude-test-its-own-work-the-verification-loop)
  ↳ *part-of* `g12-0199`
  ↳ *depends-on* `g12-0209`
  ↳ *contrast* `g15-0057`

- `g12-0213` *STATED* — Guide section 'Set it up once' configures the verification loop to run the same way every time (body email-gated; 1 prompt to copy).
  — [g-how-to-make-claude-test-its-own-work-the-verification-loop](https://chen.media/guides/how-to-make-claude-test-its-own-work-the-verification-loop)
  ↳ *part-of* `g12-0199`
  ↳ *defines* `g12-0203`

- `g12-0246` *STATED* — Guide section 'The command' gives the exact command that turns on lower-priority mode (body email-gated; 4 prompts to copy).
  — [g-keep-using-claude-code-after-you-hit-your-usage-limit](https://chen.media/guides/keep-using-claude-code-after-you-hit-your-usage-limit)
  ↳ *part-of* `g12-0238`
  ↳ *enables* `g12-0241`

- `g12-0247` *STATED* — Guide section 'How to turn it off' covers turning lower-priority mode back off (body email-gated).
  — [g-keep-using-claude-code-after-you-hit-your-usage-limit](https://chen.media/guides/keep-using-claude-code-after-you-hit-your-usage-limit)
  ↳ *part-of* `g12-0238`
  ↳ *qualifies* `g12-0246`

- `g13-0011` *STATED* — Alex's Bot Crossing guide has a section 'Find the session that's waiting on you' on locating the Claude Code session blocked on your input.
  — [g-watch-every-claude-code-session-as-a-bot-in-bot-crossing](https://chen.media/guides/watch-every-claude-code-session-as-a-bot-in-bot-crossing)
  ↳ *part-of* `g13-0001`
  ↳ *depends-on* `g13-0003`

- `g13-0095` *STATED* — You give a Claude Code cloud session a GitHub repository and a task; it clones the repo, does the work, runs the tests and pushes a branch for you to review.
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it)
  ↳ *part-of* `g13-0094`

- `g13-0105` *STATED* — Step 1 of claiming the Claude Code cloud credit is to connect GitHub.
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it) [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)
  ↳ *leads-to* `g13-0106`
  ↳ *enables* `g13-0095` — cloud sessions work from GitHub repos

- `g13-0106` *STATED* — Step 2 of the cloud credit setup is to claim the credit.
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it) [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)
  ↳ *leads-to* `g13-0107`
  ↳ *part-of* `g13-0099`

- `g13-0107` *STATED* — Step 3 of the cloud credit setup is to start your first cloud session.
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it) [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)

- `g13-0108` *STATED* — Alex's laptop-closed guide has a section 'What to give it first' recommending the first task to hand a cloud session.
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it)
  ↳ *part-of* `g13-0107`

- `g13-0154` *CORE* — Claude Code can turn an API provider's documentation into a working app feature.
  — [g-public-apis-claude-code-build-guide](https://chen.media/guides/public-apis-claude-code-build-guide)
  ↳ *enables* `g13-0152`

- `g13-0164` *STATED* — Alex's PUB guide step: 'Open Claude Code in your project'.
  — [g-public-apis-claude-code-build-guide](https://chen.media/guides/public-apis-claude-code-build-guide)
  ↳ *leads-to* `g13-0165`

- `g13-0185` *STATED* — Alex's JEV guide section 'Set up Jev once': a one-time setup prompt for Claude Code.
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *part-of* `g13-0184`

- `g13-0228` *STATED* — Use a Claude conversation for writing, planning or design alternatives; use an existing Claude Code project when the result needs files, code execution or tests.
  — [g-darwin-loop-evolve-the-winner](https://chen.media/guides/darwin-loop-evolve-the-winner)
  ↳ *part-of* `g13-0222`

- `g13-0231` *STATED* — If you are new to Claude Code, follow its current setup guide before adapting the Darwin Loop coding example.
  — [g-darwin-loop-evolve-the-winner](https://chen.media/guides/darwin-loop-evolve-the-winner)
  ↳ *depends-on* `g13-0228`

- `g13-0232` *STATED* — Run Darwin Loop coding experiments in a project you can restore.
  — [g-darwin-loop-evolve-the-winner](https://chen.media/guides/darwin-loop-evolve-the-winner)
  ↳ *part-of* `g13-0228`

- `g13-0233` *STATED* — Give Claude the checks that already belong to the project.
  > “give Claude the checks that already belong to that project”
  — [g-darwin-loop-evolve-the-winner](https://chen.media/guides/darwin-loop-evolve-the-winner)
  ↳ *part-of* `g13-0228`

- `g14-0054` *STATED* — Ask an AI assistant for help with the OpenCut local setup.
  > “Ask an assistant for setup help”
  — [g-opencut-repo-and-setup-guide](https://chen.media/guides/opencut-repo-and-setup-guide)
  ↳ *part-of* `g14-0043`
  ↳ *enables* `g14-0053`

- `g14-0060` *STATED* — Add Headroom, Claude HUD and AIsa one at a time so you can tell which change helped.
  > “Add one at a time so you can tell which change helped.”
  — [g-headroom-claude-hud-aisa-setup](https://chen.media/guides/headroom-claude-hud-aisa-setup)
  ↳ *part-of* `g14-0056`
  ↳ *example-of* `g14-0349`

- `g14-0063` *STATED* — Install Claude HUD by running four slash commands inside Claude Code, in order: /plugin marketplace add jarrodwatts/claude-hud, /plugin install claude-hud, /reload-plugins, /claude-hud:setup.
  — [g-headroom-claude-hud-aisa-setup](https://chen.media/guides/headroom-claude-hud-aisa-setup)
  ↳ *depends-on* `g14-0062`
  ↳ *example-of* `g14-0351`

- `g14-0066` *STATED* — Claude HUD install step 3: run /reload-plugins inside Claude Code so the newly installed plugin loads.
  > “/reload-plugins”
  — [g-headroom-claude-hud-aisa-setup](https://chen.media/guides/headroom-claude-hud-aisa-setup)
  ↳ *part-of* `g14-0063`
  ↳ *leads-to* `g14-0067`
  ↳ *example-of* `g05-0110`

- `g14-0067` *STATED* — Claude HUD install step 4: /claude-hud:setup — this final command configures the Claude Code status line.
  > “/claude-hud:setup”
  — [g-headroom-claude-hud-aisa-setup](https://chen.media/guides/headroom-claude-hud-aisa-setup)
  ↳ *part-of* `g14-0063`

- `g14-0087` *STATED* — Write an intent.md file describing the reason for the work before you ask Claude to build.
  > “Start with the reason for the work”
  — [g-intent-md-claude-project-setup](https://chen.media/guides/intent-md-claude-project-setup)
  ↳ *part-of* `g14-0085`

- `g14-0089` *STATED* — Anthropic's AI-Native SDLC playbook starts with a reviewed intent document, then moves through a specification, plan, implementation and tests.
  — [g-intent-md-claude-project-setup](https://chen.media/guides/intent-md-claude-project-setup)
  ↳ *part-of* `g14-0088`
  ↳ *generalizes* `g16-0205`

- `g14-0090` *STATED* — In Anthropic's AI-Native SDLC, each artifact (intent, spec, plan, implementation, tests) is stored in version control.
  — [g-intent-md-claude-project-setup](https://chen.media/guides/intent-md-claude-project-setup)
  ↳ *part-of* `g14-0089`

- `g14-0094` *STATED* — Point your AI assistant at intent.md explicitly; it is not read automatically.
  > “Point your assistant at it.”
  — [g-intent-md-claude-project-setup](https://chen.media/guides/intent-md-claude-project-setup)
  ↳ *because* `g14-0093`
  ↳ *contrast* `g20-0236`

- `g14-0098` *STATED* — Turn the intent.md brief into an implementation plan before building.
  > “Turn the brief into a plan”
  — [g-intent-md-claude-project-setup](https://chen.media/guides/intent-md-claude-project-setup)
  ↳ *part-of* `g14-0085`
  ↳ *example-of* `g14-0089`
  ↳ *example-of* `g15-0135`

- `g14-0139` *STATED* — Bedrock step: search for Amazon Bedrock in the AWS console, open its model catalog, select a Claude model available in your region, and open it in the playground.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *part-of* `g14-0129`

- `g14-0141` *STATED* — Complete the Anthropic first-time-use form in Amazon Bedrock if prompted.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *part-of* `g14-0139`

- `g14-0142` *STATED* — If Bedrock access to a Claude model is denied, review the message, your Bedrock permissions and account restrictions.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *leads-to* `g14-0141`

- `g14-0159` *STATED* — Bedrock access error fix: finish any required use-case form and review your AWS role permissions.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *example-of* `g14-0142`

- `g14-0160` *STATED* — Bedrock region error fix: select a region supported by that exact model.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *qualifies* `g14-0140`

- `g14-0226` *STATED* — Install ECC into an existing project with version control, or into a small disposable project.
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *part-of* `g14-0220`
  ↳ *example-of* `g14-0349`

- `g14-0227` *STATED* — Commit your current work before installing ECC.
  > “Commit your current work first.”
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *part-of* `g14-0226`

- `g14-0235` *STATED* — Run one feature through four ECC jobs: plan the feature, build the approved plan, review the security, test the result.
  > “Run one feature through four jobs”
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *part-of* `g14-0220`
  ↳ *example-of* `g15-0135`

- `g14-0236` *STATED* — ECC job 1: plan the feature.
  > “Plan the feature”
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *part-of* `g14-0235`
  ↳ *leads-to* `g14-0237`

- `g14-0237` *STATED* — ECC job 2: build the approved plan (only after the plan is approved).
  > “Build the approved plan”
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *part-of* `g14-0235`
  ↳ *leads-to* `g14-0238`

- `g14-0238` *STATED* — ECC job 3: review the security of the built feature.
  > “Review the security”
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *part-of* `g14-0235`
  ↳ *leads-to* `g14-0239`

- `g14-0239` *STATED* — ECC job 4: test the result.
  > “Test the result”
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *part-of* `g14-0235`

- `g14-0251` *STATED* — Install Claude Octopus with two commands run in your terminal, outside an active Claude Code session.
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *part-of* `g14-0241`

- `g14-0254` *STATED* — After installing Claude Octopus, open Claude Code in a small project you know well.
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *leads-to* `g14-0255`

- `g14-0296` *STATED* — Run Claude Code in a folder you can back up and review.
  > “Use a folder you can back up and review.”
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *qualifies* `g14-0295`

- `g15-0051` *STATED* — A verification setup can make a coding agent run ten checks at once instead of one at a time.
  — [g-claude-code-says-done-before-it-has-proved-anything-this-fixes-it](https://chen.media/guides/claude-code-says-done-before-it-has-proved-anything-this-fixes-it)
  ↳ *qualifies* `g15-0055`

- `g15-0057` *STATED* — You can build the verify-before-done mechanism yourself in about twenty minutes without installing anything, and the self-built version is 'the version you can trust'.
  — [g-claude-code-says-done-before-it-has-proved-anything-this-fixes-it](https://chen.media/guides/claude-code-says-done-before-it-has-proved-anything-this-fixes-it)
  ↳ *enables* `g15-0055`

- `g15-0135` *STATED* — Make Claude Code plan before it writes anything (rule two).
  — [g-the-official-claude-code-prompt-library-52-free-prompts](https://chen.media/guides/the-official-claude-code-prompt-library-52-free-prompts)
  ↳ *part-of* `g15-0133`
  ↳ *evidence-for* `g03-0156`

- `g15-0136` *STATED* — Put your standing answers in CLAUDE.md so Claude Code stops asking (rule three).
  — [g-the-official-claude-code-prompt-library-52-free-prompts](https://chen.media/guides/the-official-claude-code-prompt-library-52-free-prompts)
  ↳ *part-of* `g15-0133`
  ↳ *example-of* `g20-0236`

- `g16-0022` *STATED* — His /design guide walks through the shape of a typical /design session.
  > “The shape of a session”
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)
  ↳ *defines* `g16-0027`

- `g16-0023` *STATED* — /design is run inside the repo you are already working in.
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)
  ↳ *part-of* `g16-0027`

- `g16-0025` *STATED* — With /design, Claude drafts the design options as artboards and lays them out on one pan-and-zoom canvas.
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)
  ↳ *leads-to* `g16-0026`

- `g16-0026` *STATED* — /design publishes the canvas and prints its URL in the terminal.
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)
  ↳ *leads-to* `g16-0027`

- `g16-0027` *STATED* — /design loop: open the printed URL, pick the artboard you want, adjust it, then tell Claude to implement that one.
  > “You open it, pick the one you want, adjust it, and tell Claude to implement that one.”
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)

- `g16-0029` *STATED* — The two design commands should be run in a specific order.
  > “The order to run them in”
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)
  ↳ *qualifies* `g16-0018`
  ↳ *example-of* `g16-0007`

- `g16-0038` *INFERRED* — If Claude Code says /design does not exist, update Claude Code, confirm claude --version is 2.1.233 or later, and check you are on Pro, Max, Team or Enterprise.
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)
  ↳ *qualifies* `g16-0037`
  ↳ *example-of* `g03-0002`

- `g16-0062` *STATED* — You can open any Claude memory file, read it, change a line, or delete it.
  > “You can open any one of them, read it, change a line, or delete it.”
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit)
  ↳ *contrast* `g16-0059`

- `g16-0063` *STATED* — Claude's memory files are at Settings, then Memory, then Topics.
  > “Settings, then Memory, then Topics”
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit)
  ↳ *enables* `g16-0062`

- `g16-0069` *STATED* — Turn memory on and check what is already in it before relying on it.
  > “Turning it on and checking what is there”
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit)
  ↳ *leads-to* `g16-0070`

- `g16-0070` *STATED* — Put specific things into Claude's memory on day one rather than letting it accumulate by accident.
  > “What to put in it on day one”
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit)

- `g16-0071` *STATED* — When Claude's memory gets you wrong, correct it directly instead of living with the error.
  > “how to correct it when it gets you wrong”
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit)
  ↳ *depends-on* `g16-0062`

- `g16-0073` *STATED* — Run a one week test to tell whether Claude's memory is working.
  > “A one week test that tells you whether it is working”
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit)
  ↳ *qualifies* `g16-0070`

- `g16-0125` *STATED* — You point Claude Code at ox-alpha in two lines of setup.
  > “how to point Claude Code at it in two lines”
  — [g-the-anonymous-model-that-makes-claude-code-free-until-august-27](https://chen.media/guides/the-anonymous-model-that-makes-claude-code-free-until-august-27)
  ↳ *enables* `g16-0124`
  ↳ *example-of* `g16-0013`

- `g16-0177` *STATED* — Tip 2 (beginner): do not work inside Projects by default.
  > “2. Do not work inside Projects by default”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *part-of* `g16-0175`

- `g16-0178` *STATED* — Tip 3 (beginner): turn memory on deliberately, then leave it alone.
  > “3. Turn memory on deliberately, then leave it alone”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *part-of* `g16-0175`
  ↳ *contradicts* `g16-0064` — tips guide (Aug 21) says turn memory on deliberately; memory guide (Aug 27) says memory is now on by default on Free, Pro and Max after the Aug 25 change
  ↳ *part-of* `g16-0012`
  ↳ *evidence-for* `g16-0069`

- `g16-0181` *STATED* — Tip 6 (intermediate): treat the Claude Chrome extension like a junior hire.
  > “6. Treat the Chrome extension like a junior hire”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *part-of* `g16-0175`
  ↳ *leads-to* `g16-0182`

- `g16-0182` *STATED* — Tip 7 (intermediate): put the tabs the Chrome extension needs into its tab group.
  > “7. Put the tabs it needs into its tab group”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *part-of* `g16-0175`

- `g16-0183` *STATED* — Tip 8 (intermediate): use short commands on the platforms Claude already knows.
  > “8. Use short commands on the platforms it already knows”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *part-of* `g16-0175`

- `g16-0184` *STATED* — Tip 9 (intermediate): let the safety check do its job.
  > “9. Let the safety check do its job”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *part-of* `g16-0175`
  ↳ *qualifies* `g16-0181`

- `g16-0185` *STATED* — Tip 10 (intermediate): know where Claude runs.
  > “10. Know where it runs”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *part-of* `g16-0175`

- `g16-0187` *STATED* — Tip 12 (expert): let Claude run the thing it is building.
  > “12. Let it run the thing it is building”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *part-of* `g16-0175`
  ↳ *qualifies* `g16-0212`

- `g16-0195` *STATED* — Work down the 15 build prompts in order.
  > “Work down the list in order.”
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0192`

- `g16-0196` *STATED* — Build prompts 1 to 6 happen before any code exists.
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0195`

- `g16-0197` *STATED* — Build prompts 7 and 8 wire up the outside world.
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0195`

- `g16-0198` *STATED* — Build prompts 9 to 12 are what you run on a codebase that already works.
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0195`

- `g16-0199` *STATED* — Build prompts 13 to 15 stop you repeating yourself.
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0195`
  ↳ *part-of* `g16-0015`

- `g16-0203` *STATED* — Build prompt 2: create your CLAUDE.md.
  > “Create Your CLAUDE.md”
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0196`
  ↳ *qualifies* `g16-0011` — he still ships a prompt to create a CLAUDE.md
  ↳ *contrast* `g16-0256`

- `g16-0204` *STATED* — Build prompt 3: Ultra Plan Mode.
  > “Ultra Plan Mode”
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0196`
  ↳ *example-of* `g16-0201` — planning stops Claude charging ahead
  ↳ *example-of* `g03-0156`

- `g16-0205` *STATED* — Build prompt 4: spec-driven development.
  > “Spec-Driven Development”
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0196`

- `g16-0207` *STATED* — Build prompt 6: an implementation plan.
  > “Implementation Plan”
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0196`
  ↳ *example-of* `g15-0135`

- `g16-0209` *STATED* — Build prompt 8: connect your database.
  > “Connect Your Database”
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0197`

- `g16-0210` *STATED* — Build prompt 9: find security gaps.
  > “Find Security Gaps”
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0198`

- `g16-0211` *STATED* — Build prompt 10: debug an error fast.
  > “Debug an Error Fast”
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0198`

- `g16-0212` *STATED* — Build prompt 11: E2E test your application.
  > “E2E Test Your Application”
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0198`
  ↳ *example-of* `g12-0211`

- `g16-0213` *STATED* — Build prompt 12: clean up dead code.
  > “Clean Up Dead Code”
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0198`

- `g16-0214` *STATED* — Build prompt 13: write slash commands.
  > “Write Slash Commands”
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0199`

- `g16-0215` *STATED* — Build prompt 14: hooks as guardrails.
  > “Hooks as Guardrails”
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0199`
  ↳ *example-of* `g16-0010`
  ↳ *example-of* `g19-0039`

- `g16-0257` *STATED* — One prompt you paste into Claude audits your CLAUDE.md and skills for you.
  > “a prompt you can paste into Claude that does the audit for you”
  — [g-why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it](https://chen.media/guides/why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it)
  ↳ *enables* `g16-0266`
  ↳ *evidence-for* `y03-0066`

- `g16-0265` *STATED* — The CLAUDE.md fix is not deleting everything; it is keeping the small number of rules that still bind.
  > “The fix is not deleting everything. It is keeping the small number of rules that still bind.”
  — [g-why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it](https://chen.media/guides/why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it)
  ↳ *qualifies* `g16-0256`
  ↳ *evidence-for* `g18-0235`

- `g16-0266` *STATED* — Learn to judge yourself whether a CLAUDE.md rule still earns its place.
  > “How to judge a rule yourself”
  — [g-why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it](https://chen.media/guides/why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it)
  ↳ *part-of* `g16-0265`

- `g17-0109` *STATED* — Alex Chen's Claude SEO guide lists the commands worth knowing on day one.
  > “The commands worth knowing on day one”
  — [g-install-25-seo-skills-and-18-specialist-agents-into-claude-code](https://chen.media/guides/install-25-seo-skills-and-18-specialist-agents-into-claude-code)
  ↳ *part-of* `g17-0104`

- `g17-0153` *STATED* — Alex Chen's FreeLLMAPI guide shows how to wire your coding agent up to the pooled endpoint.
  > “Wiring up your agent”
  — [g-pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint](https://chen.media/guides/pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint)
  ↳ *example-of* `g17-0145`

- `g17-0253` *STATED* — Watch the three Claude courses in order: the first makes you competent, the second widens what you can point the tool at, the third turns it into money.
  > “The first makes you competent, the second widens what you can point the tool at, and the third is the one that turns it into money.”
  — [g-three-free-claude-courses-and-what-to-do-with-them](https://chen.media/guides/three-free-claude-courses-and-what-to-do-with-them)
  ↳ *depends-on* `g17-0251`

- `g17-0266` *STATED* — Alex Chen's Agency guide shows how to actually run one of the agents in Claude Code.
  > “How to actually run one”
  — [g-286-specialist-ai-agents-free-inside-claude-code](https://chen.media/guides/286-specialist-ai-agents-free-inside-claude-code)
  ↳ *leads-to* `g17-0265`

- `g18-0058` *STATED* — To run Graphify on a repo, type `/graphify` in Claude Code from inside the project.
  > “/graphify”
  — [g-stop-claude-code-re-reading-your-repo-every-session](https://chen.media/guides/stop-claude-code-re-reading-your-repo-every-session)
  ↳ *depends-on* `g18-0057`

- `g18-0059` *STATED* — The Graphify guide also lists the command `graphify claude install` (its explanation is gated).
  > “graphify claude install”
  — [g-stop-claude-code-re-reading-your-repo-every-session](https://chen.media/guides/stop-claude-code-re-reading-your-repo-every-session)
  ↳ *part-of* `g18-0054`

- `g18-0066` *STATED* — The Karpathy CLAUDE.md can be installed for one project, or for every project you ever open.
  — [g-the-20-kb-file-that-stops-claude-doing-four-dumb-things](https://chen.media/guides/the-20-kb-file-that-stops-claude-doing-four-dumb-things)
  ↳ *part-of* `g18-0064`
  ↳ *evidence-for* `g20-0238`

- `g18-0067` *INFERRED* — In Claude Code a project CLAUDE.md lives in the project root, while one that applies to every project lives in ~/.claude/CLAUDE.md.
  — [g-the-20-kb-file-that-stops-claude-doing-four-dumb-things](https://chen.media/guides/the-20-kb-file-that-stops-claude-doing-four-dumb-things)
  ↳ *defines* `g18-0066`
  ↳ *contrast* `g18-0089` — CLAUDE.md vs skills folder locations, both global vs project

- `g18-0090` *STATED* — To check which skills are actually loaded in Claude Code, look in ~/.claude/skills/ and in the project's .claude/skills/.
  — [g-five-animation-skills-for-claude-code-with-install-commands](https://chen.media/guides/five-animation-skills-for-claude-code-with-install-commands)
  ↳ *depends-on* `g18-0089`

- `g18-0120` *INFERRED* — The Claude Code CLI equivalent of the Exa desktop config is `claude mcp add exa -- npx -y mcp-remote https://mcp.exa.ai/mcp`.
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again)
  ↳ *analogy-for* `g18-0118`

- `g18-0164` *STATED* — In the Claude desktop app the same plugin browser sits under the + button next to the prompt box.
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *contrast* `g18-0160` — desktop + button vs terminal commands

- `g18-0183` *STATED* — Alex's wrap-up skill: at the end of a working session Claude writes a structured summary of what happened, and that summary goes into a NotebookLM notebook you keep forever.
  — [g-give-claude-a-memory-that-survives-the-chat-window](https://chen.media/guides/give-claude-a-memory-that-survives-the-chat-window)
  ↳ *example-of* `g18-0289`

- `g18-0186` *STATED* — The wrap-up skill produces a clean, well-shaped file in a folder you control, rather than writing to NotebookLM directly.
  — [g-give-claude-a-memory-that-survives-the-chat-window](https://chen.media/guides/give-claude-a-memory-that-survives-the-chat-window)
  ↳ *because* `g18-0185`

- `g18-0189` *STATED* — NotebookLM memory setup: 1 make the memory folder, 2 create the skill, 3 decide what the wrap-up should actually capture, 4 get the folder into NotebookLM, 5 read it back.
  — [g-give-claude-a-memory-that-survives-the-chat-window](https://chen.media/guides/give-claude-a-memory-that-survives-the-chat-window)
  ↳ *defines* `g18-0183`

- `g18-0190` *STATED* — The NotebookLM memory guide ships a copyable skill file, 'The part nobody mentions', and an 'If you only do one thing' fallback.
  — [g-give-claude-a-memory-that-survives-the-chat-window](https://chen.media/guides/give-claude-a-memory-that-survives-the-chat-window)
  ↳ *part-of* `g18-0183`

- `g18-0225` *STATED* — The free-LLM guide gives the exact settings to point Claude Code, Cursor and Codex at a free LLM API, plus a 'What to watch for' section.
  — [g-134-free-llm-apis-and-how-to-point-your-editor-at-them](https://chen.media/guides/134-free-llm-apis-and-how-to-point-your-editor-at-them)
  ↳ *depends-on* `g18-0220`

- `g18-0228` *STATED* — Boris Cherny fix 1: delete most of your instructions.
  > “Delete most of your instructions”
  — [g-three-things-almost-everyone-gets-wrong-about-claude-code](https://chen.media/guides/three-things-almost-everyone-gets-wrong-about-claude-code)
  ↳ *part-of* `g18-0226`
  ↳ *because* `g18-0231`
  ↳ *example-of* `g18-0284`

- `g18-0232` *STATED* — CLAUDE.md cleanup step 1: open your CLAUDE.md and read it as if you wrote it for a new hire who is already excellent.
  — [g-three-things-almost-everyone-gets-wrong-about-claude-code](https://chen.media/guides/three-things-almost-everyone-gets-wrong-about-claude-code)
  ↳ *part-of* `g18-0228`

- `g18-0233` *STATED* — CLAUDE.md cleanup step 2: delete every line that exists to stop a mistake you have not actually seen in the last month.
  — [g-three-things-almost-everyone-gets-wrong-about-claude-code](https://chen.media/guides/three-things-almost-everyone-gets-wrong-about-claude-code)
  ↳ *part-of* `g18-0228`
  ↳ *contrast* `g18-0257` — cut rules for unseen mistakes, keep rules for mistakes seen twice

- `g18-0234` *STATED* — CLAUDE.md cleanup step 3: delete every line that explains something the model can read from the code itself.
  — [g-three-things-almost-everyone-gets-wrong-about-claude-code](https://chen.media/guides/three-things-almost-everyone-gets-wrong-about-claude-code)
  ↳ *part-of* `g18-0228`
  ↳ *evidence-for* `g18-0254` — keep only what code cannot show

- `g18-0235` *STATED* — CLAUDE.md cleanup step 4: keep only what is true, specific and impossible to infer: your stack, your conventions, your hard rules.
  — [g-three-things-almost-everyone-gets-wrong-about-claude-code](https://chen.media/guides/three-things-almost-everyone-gets-wrong-about-claude-code)
  ↳ *part-of* `g18-0228`
  ↳ *generalizes* `g18-0258`

- `g18-0236` *STATED* — If a CLAUDE.md line would embarrass you to say out loud to a senior engineer, cut it.
  > “If a line would embarrass you to say out loud to a senior engineer, cut it”
  — [g-three-things-almost-everyone-gets-wrong-about-claude-code](https://chen.media/guides/three-things-almost-everyone-gets-wrong-about-claude-code)
  ↳ *part-of* `g18-0228`

- `g18-0246` *STATED* — CUT a CLAUDE.md of 200+ lines: it was written for a weaker model; delete it and start from zero.
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *part-of* `g18-0245`
  ↳ *evidence-for* `g18-0238`
  ↳ *contradicts* `g16-0265` — 'CUT a CLAUDE.md of 200+ lines: delete it and start from zero' vs 'the fix is not deleting everything; keep the small number of rules that still bind'
  ↳ *evidence-for* `g03-0020`

- `g18-0253` *STATED* — CUT hooks that just print things: if nobody reads the output, it is not a hook.
  > “If nobody reads the output, it is not a hook.”
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *part-of* `g18-0245`
  ↳ *contrast* `r03-0047`

- `g18-0254` *STATED* — KEEP how to run tests in THIS repo in your CLAUDE.md: it is not derivable from the code, so it is real context.
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *part-of* `g18-0245`
  ↳ *example-of* `g18-0235`

- `g18-0255` *STATED* — KEEP deploy and release steps in your CLAUDE.md: irreversible actions deserve written steps.
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *part-of* `g18-0245`

- `g18-0256` *STATED* — KEEP non-obvious architecture decisions in your CLAUDE.md: the why, not the what, because code shows the what.
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *part-of* `g18-0245`

- `g18-0257` *STATED* — KEEP rules for things the model got wrong twice: earned rules, each one has a receipt.
  > “Earned rules. Each one has a receipt.”
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *part-of* `g18-0245`

- `g18-0258` *STATED* — KEEP repo-specific naming or conventions: house style the model cannot infer from one file.
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *part-of* `g18-0245`

- `g18-0259` *STATED* — KEEP credentials, paths and environment quirks: facts, not instructions, cheap and load-bearing.
  > “Facts, not instructions. Cheap and load-bearing.”
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *part-of* `g18-0245`

- `g18-0261` *STATED* — Alex's six-month reset of a Claude setup runs in five steps, followed by 'What usually happens' and 'The part nobody says out loud'.
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *part-of* `g18-0241`

- `g19-0025` *STATED* — Tier 1 Claude Code tip: a PreToolUse hook that blocks git push to main.
  > “PreToolUse block git push to main”
  — [g-50-claude-tips-ranked-worst-to-best](https://chen.media/guides/50-claude-tips-ranked-worst-to-best)
  ↳ *part-of* `g19-0042`
  ↳ *example-of* `g19-0038` — what can physically stop a bad action
  ↳ *example-of* `g19-0028`
  ↳ *example-of* `g01-0126`

- `g19-0026` *STATED* — Tier 1 Claude Code tip: a PostToolUse hook that runs the formatter and linter after every edit.
  > “PostToolUse run the formatter and linter after every edit”
  — [g-50-claude-tips-ranked-worst-to-best](https://chen.media/guides/50-claude-tips-ranked-worst-to-best)
  ↳ *part-of* `g19-0042`
  ↳ *example-of* `g19-0028` — automatic quality guardrail
  ↳ *example-of* `g16-0215`

- `g19-0068` *STATED* — A Claude Code subagent is defined as a Markdown file with YAML frontmatter: name, description, and optional tools and model.
  > “a Markdown file with YAML frontmatter: name, description, optional tools and model”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *defines* `g19-0067`

- `g19-0071` *STATED* — Run /agents inside Claude Code to see, create and manage subagents from a menu.
  > “Run /agents inside Claude Code to see, create, and manage them from a menu.”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *enables* `g19-0068`

- `g20-0142` *STATED* — Build the five memory parts in order; each part feeds the next.
  > “Build these in order. Each part feeds the next.”
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0141`

- `g20-0148` *STATED* — Memory Part 1 is the memory file: one file, read before every job and appended to after every job, which Alex calls the whole trick.
  > “One file, read before every job, appended to after every job. This is the whole trick.”
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0141`
  ↳ *leads-to* `g20-0161`
  ↳ *example-of* `g20-0147`

- `g20-0149` *STATED* — Keep the memory file human readable so you can prune it, with one fact per line so the model can quote it back.
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0148`
  ↳ *enables* `g20-0165`

- `g20-0150` *STATED* — Save the memory file as memory.md at the root of the project.
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0148`
  ↳ *contrast* `g20-0239` — memory.md vs ./CLAUDE.md

- `g20-0151` *STATED* — The memory.md prompt is pasted once, at the start of a session.
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0148`

- `g20-0152` *STATED* — memory.md prompt: 'Read memory.md before you do anything else. Treat every line in it as a decision I have already made.'
  > “Read memory.md before you do anything else. Treat every line in it as a decision I have already made.”
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0151`

- `g20-0153` *CORE* — memory.md prompt line: 'Do not ask me to re-explain anything that is already in there.'
  > “Do not ask me to re-explain anything that is already in there.”
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0151`
  ↳ *contrast* `g20-0146` — stops paying twice

- `g20-0154` *STATED* — memory.md prompt line: 'If something in memory.md conflicts with what I just asked, say so in one line and ask which one wins. Do not guess.'
  > “say so in one line and ask which one wins. Do not guess.”
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0151`
  ↳ *example-of* `g20-0293`

- `g20-0155` *STATED* — At the end of each session Claude appends to memory.md any decision you made that changes future work.
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0151`

- `g20-0156` *STATED* — At the end of each session Claude appends to memory.md any preference you corrected it on.
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0151`

- `g20-0157` *STATED* — At the end of each session Claude appends to memory.md anything that broke, and the reason it broke.
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0151`

- `g20-0158` *STATED* — memory.md format rule: 'One fact per line. No prose. No duplicates.'
  > “One fact per line. No prose. No duplicates.”
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0148`

- `g20-0161` *STATED* — Memory Part 2 is 'The save and reload loop'.
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0141`
  ↳ *leads-to* `g20-0162`

- `g20-0165` *STATED* — The memory guide's bonus section not in the video is 'Memory hygiene'.
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0141`
  ↳ *example-of* `g20-0281` — bonus not in video

- `g20-0195` *STATED* — Council setup 5: to run the whole roast from one command, save the agents as subagents or a slash command that fires them in order.
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *part-of* `g20-0190`
  ↳ *generalizes* `g20-0207`

- `g20-0207` *STATED* — Dev-team setup 5: to run the whole pipeline from one command, save the agents as subagents or a slash command that fires them in order: plan, build, test, review.
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *part-of* `g20-0202`
  ↳ *depends-on* `g19-0067`

- `g20-0229` *STATED* — Build the four Claude Code upgrades in this order: memory first, then MCP, then sub agents, then the loop; each one compounds on the last.
  > “Memory first, then MCP, then sub agents, then the loop. Each one compounds on the last.”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *part-of* `g20-0222`
  ↳ *evidence-for* `g20-0286`

- `g20-0231` *STATED* — Upgrade 1 of 4 is Memory, the second brain.
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *part-of* `g20-0229`
  ↳ *leads-to* `g20-0232`
  ↳ *contrast* `g20-0225` — fixes forgetting

- `g20-0238` *CORE* — ~/.claude/CLAUDE.md is global and loads in every project; put who you are and how you like to work there.
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *part-of* `g20-0236`
  ↳ *evidence-for* `g18-0067`

- `g20-0239` *STATED* — ./CLAUDE.md sits in a project folder and loads only for that project; put the stack, the commands and the gotchas there.
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *part-of* `g20-0236`
  ↳ *evidence-for* `g18-0067`

- `g20-0240` *STATED* — In your project folder run `claude` then `/init`, and Claude reads the repo and writes a CLAUDE.md for you.
  > “claude
/init”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *enables* `g20-0239`

- `g20-0241` *STATED* — Edit CLAUDE.md any time with the /memory command.
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *part-of* `g20-0236`

- `g20-0242` *STATED* — Start any Claude Code message with # and Claude writes it to CLAUDE.md instead of just answering.
  > “Start any message with # and Claude writes it to CLAUDE.md instead of just answering”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *part-of* `g20-0236`

- `g20-0246` *STATED* — Alex's starter ~/.claude/CLAUDE.md has three sections: '## Who I am', '## How to answer me' and '## Standards'.
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *example-of* `g20-0238`

- `g20-0250` *STATED* — Starter CLAUDE.md standard: 'Match the style of the surrounding code.'
  > “Match the style of the surrounding code.”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *part-of* `g20-0246`

- `g20-0251` *STATED* — Starter CLAUDE.md standard: 'Never commit or push unless I ask.'
  > “Never commit or push unless I ask.”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *part-of* `g20-0246`
  ↳ *analogy-for* `g20-0031` — permissions limited

- `g20-0252` *STATED* — Starter CLAUDE.md standard: 'When a task is done, tell me exactly what you verified.'
  > “When a task is done, tell me exactly what you verified.”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *part-of* `g20-0246`
  ↳ *enables* `g20-0110` — verification feeds track record
  ↳ *qualifies* `g15-0050`

- `g21-0046` *STATED* — Tournament setup step 4: save all three prompts as a reusable Arena (a Project or a saved instruction set), so next time you just paste a new thing and run it.
  — [g-run-a-tournament-instead-of-guessing-which-hook-works](https://chen.media/guides/run-a-tournament-instead-of-guessing-which-hook-works)
  ↳ *part-of* `g21-0041`
  ↳ *enables* `g21-0040`
  ↳ *generalizes* `g21-0053` — both save prompts as Projects

- `g21-0053` *STATED* — Save each AI employee as its own Project so the role, the rules, and your context are always on.
  — [g-turn-claude-into-a-six-person-ai-c-suite](https://chen.media/guides/turn-claude-into-a-six-person-ai-c-suite)
  ↳ *contrast* `g21-0052` — the fix for role drift
  ↳ *leads-to* `g21-0054`
  ↳ *example-of* `g22-0284`

- `g21-0056` *STATED* — C-suite setup step 1: create a separate Project for each employee (or a saved instruction set if you don't use Projects): six Projects total.
  — [g-turn-claude-into-a-six-person-ai-c-suite](https://chen.media/guides/turn-claude-into-a-six-person-ai-c-suite)
  ↳ *part-of* `g21-0055`
  ↳ *leads-to* `g21-0057`

- `g21-0057` *STATED* — C-suite setup step 2: paste that employee's prompt into the Project's custom instructions; this is what locks them into character.
  — [g-turn-claude-into-a-six-person-ai-c-suite](https://chen.media/guides/turn-claude-into-a-six-person-ai-c-suite)
  ↳ *part-of* `g21-0055`
  ↳ *leads-to* `g21-0058`
  ↳ *example-of* `g21-0051`

- `g21-0092` *STATED* — Move 9 of the nine Fable 5 prompts: the memory file.
  — [g-nine-prompts-worth-stealing-from-anthropic-s-own-guide](https://chen.media/guides/nine-prompts-worth-stealing-from-anthropic-s-own-guide)
  ↳ *part-of* `g21-0079`
  ↳ *example-of* `g21-0167` — memory file = fix 3

- `g21-0123` *STATED* — Run the blueprint mining in Claude Code inside your real project folder (best), or in a plain claude.ai chat with Fable 5 selected.
  — [g-turn-your-whole-backlog-into-finished-plans-in-one-night](https://chen.media/guides/turn-your-whole-backlog-into-finished-plans-in-one-night)
  ↳ *part-of* `g21-0117`

- `g21-0134` *STATED* — Mining step 1 (ground yourself) in Claude Code: read the repo first so every blueprint is grounded in what exists, not assumptions.
  — [g-turn-your-whole-backlog-into-finished-plans-in-one-night](https://chen.media/guides/turn-your-whole-backlog-into-finished-plans-in-one-night)
  ↳ *part-of* `g21-0125`

- `g21-0135` *STATED* — Repo grounding checklist: folder structure, package/dependency files, the README, the config, existing naming conventions, and 3 to 5 representative source files; then read the backlog file.
  — [g-turn-your-whole-backlog-into-finished-plans-in-one-night](https://chen.media/guides/turn-your-whole-backlog-into-finished-plans-in-one-night)
  ↳ *part-of* `g21-0134`

- `g21-0154` *STATED* — The mining prompt reads the backlog from ./BACKLOG.md (change the path to wherever your list lives) and saves each blueprint to ./blueprints/<short-slug>.md; in a plain chat it prints each blueprint in full for you to save.
  > “MY BACKLOG: ./BACKLOG.md ... SAVE EACH BLUEPRINT TO: ./blueprints/<short-slug>.md”
  — [g-turn-your-whole-backlog-into-finished-plans-in-one-night](https://chen.media/guides/turn-your-whole-backlog-into-finished-plans-in-one-night)
  ↳ *part-of* `g21-0125`

- `g21-0166` *CORE* — Fable 5 fix 2: make it prove its own work, so 'it's done' actually means done.
  > “Make it prove its own work, so “it’s done” actually means done.”
  — [g-the-fable-5-guide-effort-memory-and-self-verification](https://chen.media/guides/the-fable-5-guide-effort-memory-and-self-verification)
  ↳ *part-of* `g21-0164`
  ↳ *contrast* `g21-0163` — fix for false done reports
  ↳ *evidence-for* `g15-0055`

- `g21-0167` *CORE* — Fable 5 fix 3: give it a memory file, so it stops relearning your setup every time.
  > “Give it a memory file, so it stops relearning your setup every time.”
  — [g-the-fable-5-guide-effort-memory-and-self-verification](https://chen.media/guides/the-fable-5-guide-effort-memory-and-self-verification)
  ↳ *part-of* `g21-0164`
  ↳ *qualifies* `g21-0162` — less relearning, fewer tokens

- `g21-0215` *STATED* — Content-team file layout (60-second setup): a claude/ folder holding CLAUDE.md (your brand voice, optional) and a commands/ folder with hooks.md, repurpose.md, grade.md, trends.md and calendar.md.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *part-of* `g21-0210`

- `g21-0217` *STATED* — Each content-team command file starts with YAML frontmatter between --- lines holding a description and an argument-hint, and its body uses $ARGUMENTS for what you type after the command.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *part-of* `g21-0216`
  ↳ *evidence-for* `r04-0007`

- `g21-0225` *STATED* — Run the repurposer as: /repurpose @transcript.txt (the @file reference passes a file as $ARGUMENTS).
  > “How to run it: /repurpose @transcript.txt”
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *example-of* `g21-0221`

- `g22-0168` *STATED* — Four-files guide section 'Install' / 'Where the four files go' says where to place the files.
  — [g-the-four-files-that-make-claude-sound-like-you](https://chen.media/guides/the-four-files-that-make-claude-sound-like-you)
  ↳ *part-of* `g22-0162`
  ↳ *defines* `g22-0171`

- `g22-0171` *STATED* — Drop the four voice files into one Claude project once.
  — [g-the-four-files-that-make-claude-sound-like-you](https://chen.media/guides/the-four-files-that-make-claude-sound-like-you)
  ↳ *part-of* `g22-0163`
  ↳ *enables* `g22-0172`
  ↳ *example-of* `g22-0284`

- `g22-0243` *STATED* — Give Claude one permanent home for your screenshots and notes, a Claude Project, and point it at the pile once.
  — [g-turn-your-camera-roll-into-something-you-can-search](https://chen.media/guides/turn-your-camera-roll-into-something-you-can-search)
  ↳ *part-of* `g22-0246`
  ↳ *part-of* `g22-0247`
  ↳ *example-of* `g22-0284`

- `g22-0244` *STATED* — Then ask the camera-roll brain questions like you would ask a person who remembers everything.
  — [g-turn-your-camera-roll-into-something-you-can-search](https://chen.media/guides/turn-your-camera-roll-into-something-you-can-search)
  ↳ *part-of* `g22-0246`

- `g22-0246` *STATED* — Camera-roll brain setup in 3 steps: 1) build the brain (a Claude Project), 2) paste the system prompt, 3) ask in plain English.
  — [g-turn-your-camera-roll-into-something-you-can-search](https://chen.media/guides/turn-your-camera-roll-into-something-you-can-search)
  ↳ *part-of* `g22-0239`

- `g22-0247` *STATED* — Camera-roll step 1 'Build the brain (the one wiring move)': a single wiring move is what makes the Project work across thousands of screenshots (details email-gated).
  — [g-turn-your-camera-roll-into-something-you-can-search](https://chen.media/guides/turn-your-camera-roll-into-something-you-can-search)
  ↳ *part-of* `g22-0246`
  ↳ *leads-to* `g22-0248`

- `g22-0248` *STATED* — Camera-roll step 2 'The system prompt' gives the Project instructions for the screenshot brain.
  — [g-turn-your-camera-roll-into-something-you-can-search](https://chen.media/guides/turn-your-camera-roll-into-something-you-can-search)
  ↳ *part-of* `g22-0246`
  ↳ *leads-to* `g22-0249`

- `g22-0249` *STATED* — Camera-roll step 3 'Ask it anything' shows example queries.
  — [g-turn-your-camera-roll-into-something-you-can-search](https://chen.media/guides/turn-your-camera-roll-into-something-you-can-search)
  ↳ *part-of* `g22-0246`

- `g22-0269` *STATED* — Before anything else, run the 5-second check to find out which model is actually answering you.
  — [g-trigger-words-and-how-to-rephrase-around-them](https://chen.media/guides/trigger-words-and-how-to-rephrase-around-them)
  ↳ *part-of* `g22-0261`

- `g22-0270` *CORE* — In Claude Code, type /status and read the Model line in the output to see which model is serving you.
  — [g-trigger-words-and-how-to-rephrase-around-them](https://chen.media/guides/trigger-words-and-how-to-rephrase-around-them)
  ↳ *part-of* `g22-0269`

- `g22-0272` *STATED* — In the claude.ai app, check the model picker at the top of the chat instead of /status.
  — [g-trigger-words-and-how-to-rephrase-around-them](https://chen.media/guides/trigger-words-and-how-to-rephrase-around-them)
  ↳ *part-of* `g22-0269`

- `g23-0019` *STATED* — Step 1 of the clone: open Claude Code in your main work folder (the one with your real projects in it), so it can see how you actually work.
  — [g-clone-the-smart-model-s-brain-into-the-cheap-one](https://chen.media/guides/clone-the-smart-model-s-brain-into-the-cheap-one)
  ↳ *part-of* `g23-0012`

- `g23-0025` *STATED* — Step 3 of cloning Fable 5 is 'The instructions file' prompt, producing the file that lets Opus continue Fable's work.
  — [g-clone-the-smart-model-s-brain-into-the-cheap-one](https://chen.media/guides/clone-the-smart-model-s-brain-into-the-cheap-one)
  ↳ *part-of* `g23-0012`
  ↳ *enables* `g23-0013`
  ↳ *evidence-for* `g23-0199`

- `g23-0032` *STATED* — In the Claude app, open your Project, then Instructions, and paste Forge Loop Prompts 1 and 2 together.
  — [g-make-claude-grade-and-fix-its-own-work](https://chen.media/guides/make-claude-grade-and-fix-its-own-work)
  ↳ *part-of* `g23-0029`

- `g23-0033` *STATED* — In Claude Code, paste Forge Loop Prompts 1 and 2 into your CLAUDE.md file.
  — [g-make-claude-grade-and-fix-its-own-work](https://chen.media/guides/make-claude-grade-and-fix-its-own-work)
  ↳ *part-of* `g23-0029`
  ↳ *evidence-for* `g23-0199`

- `g23-0049` *STATED* — A setup block makes the Claude codes always-on so they never turn off, the setup that makes them permanent.
  > “Make them always-on (so they never turn off)”
  — [g-the-claude-codes-cheat-sheet-plus-five-bonus-ones](https://chen.media/guides/the-claude-codes-cheat-sheet-plus-five-bonus-ones)
  ↳ *enables* `g23-0040`
  ↳ *evidence-for* `g23-0199`

- `g23-0050` *INFERRED* — The codes' always-on setup block most plausibly lives in a persistent instruction location (Project Instructions or CLAUDE.md), the same place the Forge Loop prompts go.
  — [g-the-claude-codes-cheat-sheet-plus-five-bonus-ones](https://chen.media/guides/the-claude-codes-cheat-sheet-plus-five-bonus-ones)
  ↳ *qualifies* `g23-0049`
  ↳ *analogy-for* `g23-0033`
  ↳ *example-of* `g23-0199`

- `g23-0160` *STATED* — The MCP cheat sheet has a 'Make them stick (available in every chat)' section for making the plugins available everywhere.
  — [g-the-claude-plugins-cheat-sheet-add-once-then-just-ask](https://chen.media/guides/the-claude-plugins-cheat-sheet-add-once-then-just-ask)
  ↳ *qualifies* `g23-0149`
  ↳ *evidence-for* `g23-0199`

- `g23-0161` *INFERRED* — In Claude Code, 'claude mcp add' defaults to local (current project) scope; adding '--scope user' registers the server for every project, the likely mechanism behind 'available in every chat'.
  — [g-the-claude-plugins-cheat-sheet-add-once-then-just-ask](https://chen.media/guides/the-claude-plugins-cheat-sheet-add-once-then-just-ask)
  ↳ *qualifies* `g23-0160`

- `r01-0013` *STATED* — Alex's skills read what the user typed after the slash command through the $ARGUMENTS placeholder in SKILL.md.
  > “What the user typed after `/agency`: `$ARGUMENTS`”
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill) [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0012`
  ↳ *evidence-for* `r04-0007`

- `r01-0035` *STATED* — /learn runs a nightly investigator Claude that turns the day's mistakes into new rules.
  — [r-alexyc9381](https://github.com/alexyc9381/alexyc9381)
  ↳ *part-of* `r01-0034`
  ↳ *evidence-for* `g09-0031`

- `r01-0092` *STATED* — /agency sales live polls a growing transcript from Claude Code: read the last 40 lines, then every 10 seconds read again with 'tail -n 40 <file>; sleep 10'.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *depends-on* `r01-0058`
  ↳ *part-of* `r01-0045`

- `r01-0185` *CORE* — Before running a multi-agent skill like /court, turn on accept-edits mode (Shift+Tab) so you are not asked to approve every file the sub-agents write.
  > “Turn on accept-edits mode (Shift+Tab) first so you are not asked to approve every file.”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *because* `r01-0214`

- `r01-0208` *STATED* — If $ARGUMENTS is blank or still reads like a placeholder, /court takes the case from the conversation: the idea, plan or claim the user most recently wanted an opinion on.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *qualifies* `r01-0013`
  ↳ *enables* `r01-0202` — blank args pull the plan from the conversation

- `r01-0209` *STATED* — /court runs its bookkeeping with: python3 "${CLAUDE_SKILL_DIR}/court.py" <command> — ${CLAUDE_SKILL_DIR} points at the skill's own folder.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *enables* `r01-0187`
  ↳ *example-of* `r04-0008`

- `r01-0210` *STATED* — If ${CLAUDE_SKILL_DIR} looks unexpanded, use the 'Base directory for this skill' that Claude Code prints at the top of a loaded skill.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *qualifies* `r01-0209`
  ↳ *part-of* `r04-0008`

- `r02-0016` *STATED* — `/hunter setup` is run once to give it your resume, target roles, locations, sources and threshold.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0001`

- `r02-0017` *STATED* — `/hunter run` finds new jobs, scores them, tailors and prepares the high ones, and shows the list.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0001`

- `r02-0018` *STATED* — `/hunter job <url or pasted posting>` does the same scoring and preparation for one job you found yourself.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0001`

- `r02-0019` *STATED* — `/hunter review` goes through each job you said yes to: shows the packet, opens the page, and you submit.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0001`

- `r02-0020` *STATED* — `/hunter applied 3` marks a job as sent (or `/hunter applied all`).
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0001`

- `r02-0021` *STATED* — `/hunter log` shows everywhere you applied.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0001`

- `r02-0022` *STATED* — `/hunter morning` is the daily version: no questions, and it ends with "N new jobs fit you, M ready for your yes".
  > “N new jobs fit you, M ready for your yes”
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0001`

- `r02-0034` *STATED* — After installing a skill like /hunter, open a new Claude Code session so it is picked up.
  > “Open a new Claude Code session afterwards.”
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *depends-on* `r02-0033`
  ↳ *qualifies* `r02-0031`
  ↳ *example-of* `r03-0143`

- `r02-0035` *STATED* — To run /hunter every day in an open session, type `/loop 24h /hunter morning`.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *enables* `r02-0022`
  ↳ *example-of* `g02-0196`

- `r02-0036` *STATED* — Alternatively set a scheduled task that runs `/hunter morning` at 7am.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *enables* `r02-0022`

- `r02-0052` *STATED* — The /hunter SKILL.md reads what the user typed after the command via the `$ARGUMENTS` placeholder.
  > “What the user typed after `/hunter`: `$ARGUMENTS`”
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *enables* `r02-0023`
  ↳ *contrast* `r02-0170` — both read $ARGUMENTS
  ↳ *evidence-for* `r04-0007`

- `r02-0054` *STATED* — /hunter reads `.hunter/PROFILE.md` first on every invocation, and if it does not exist runs setup before anything else.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *depends-on* `r02-0016`

- `r02-0101` *STATED* — /hunter review walks the yes-jobs one at a time: shows the packet, then opens the posting page with `open <url>` on a Mac, `xdg-open <url>` on Linux, or `start <url>` on Windows.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *defines* `r02-0019`

- `r02-0110` *STATED* — /hunter suggests both scheduling options (`/loop 24h` in session, or a desktop scheduled task) and asks the user which they want.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0107`
  ↳ *depends-on* `r02-0035`

- `r02-0115` *STATED* — /hunter rule: do not write anywhere except `.hunter/`.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *example-of* `r02-0313`

- `r02-0143` *STATED* — To use /launch, open Claude Code in your app's folder and type `/launch`.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0118`

- `r02-0144` *STATED* — `/launch` with no flag polls all 8 stations: TESTS, SECURITY, DATABASE, SPEED, COST, USERS, RECOVERY, RULES.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0143`

- `r02-0146` *STATED* — `/launch --only a,b` polls just the named stations, for example `--only security,cost`.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0143`

- `r02-0151` *STATED* — Turn on accept-edits mode (Shift+Tab) before /launch so you are not asked to approve every report file.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *depends-on* `r02-0137`
  ↳ *evidence-for* `r01-0185`

- `r02-0152` *STATED* — Add `.launch/` to your `.gitignore`.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *depends-on* `r02-0137`

- `r02-0170` *STATED* — If `$ARGUMENTS` after /launch is blank, or still reads like a placeholder, the launch is the app in the current directory.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0143`
  ↳ *evidence-for* `r01-0208`

- `r02-0171` *STATED* — Every piece of /launch bookkeeping goes through `python3 "${CLAUDE_SKILL_DIR}/launch.py" <command>`, using the `${CLAUDE_SKILL_DIR}` variable for the skill's own folder.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *enables* `r02-0155`
  ↳ *example-of* `r04-0008`

- `r02-0172` *STATED* — If `${CLAUDE_SKILL_DIR}` looks unexpanded, use the "Base directory for this skill" that Claude Code printed at the top of the skill.
  > “use the "Base directory for this skill" that Claude Code printed at the top of this skill”
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0171`
  ↳ *evidence-for* `r01-0210`

- `r02-0173` *STATED* — Run launch.py from the root of the user's project: state lives in `.launch/<run>/` and every command after `init` finds it through `.launch/LATEST`.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0171`
  ↳ *example-of* `r02-0313`

- `r02-0176` *STATED* — In the default permission mode /launch's report writes need one approval per file, so it suggests accept-edits mode (Shift+Tab) but never changes the user's settings itself.
  > “Do not change the user's settings yourself.”
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *generalizes* `r02-0151`
  ↳ *qualifies* `r02-0152`
  ↳ *evidence-for* `r01-0215`

- `r02-0185` *STATED* — /launch step 3 opens the poll with `LAUNCH init --mission-file .launch/mission.md [--quick | --only a,b | --recheck]`.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *depends-on* `r02-0178`
  ↳ *part-of* `r02-0171`

- `r02-0196` *STATED* — When `LAUNCH next` says the poll is complete, `LAUNCH render` counts the calls, writes `LAUNCH-REPORT.md` into the run folder and prints it.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0171`
  ↳ *leads-to* `r02-0135`

- `r03-0008` *STATED* — /learn part 1, 'Every correction goes into the rulebook': LESSONS.md sits in the project and CLAUDE.md imports it, so every new session starts with every rule in it and the mistake doesn't come back.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0007`

- `r03-0010` *STATED* — /learn part 3: the investigator writes what it found back into the rules, one short rule per lesson.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0007`
  ↳ *leads-to* `r03-0008`

- `r03-0012` *STATED* — /learn part 4, 'You keep working normally': a hook quietly notes every prompt that sounds like a correction, such as 'no, I told you...', 'you forgot...', 'wrong, ...'.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0007`
  ↳ *leads-to* `r03-0009`
  ↳ *leads-to* `r03-0013`

- `r03-0015` *CORE* — /learn adds one line, '@LESSONS.md', to CLAUDE.md so Claude Code loads the rulebook at the start of every session (a CLAUDE.md @-file import).
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0008`
  ↳ *depends-on* `g20-0236`

- `r03-0025` *STATED* — To use /learn, open Claude Code in your project and run '/learn setup' once.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *leads-to* `r03-0026`

- `r03-0045` *CORE* — The /learn hook ('learn.py capture') runs on every prompt you send, on Claude Code's UserPromptSubmit event.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *defines* `r03-0012`
  ↳ *evidence-for* `g09-0041`

- `r03-0046` *STATED* — 'learn.py capture' checks each prompt against a list of correction phrases and, if it matches, appends one line to .learn/inbox.jsonl.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0045`

- `r03-0058` *STATED* — To remove /learn from a project: delete the UserPromptSubmit entry that runs 'learn.py capture' from .claude/settings.json, the '@LESSONS.md' line from CLAUDE.md, and .claude/hooks/learn.py; keep LESSONS.md if you like the rules.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *contrast* `r03-0074`

- `r03-0062` *STATED* — Use '/learn <lesson>' for any correction the hook missed.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *qualifies* `r03-0061`
  ↳ *depends-on* `r03-0029`

- `r03-0066` *STATED* — The learn SKILL.md receives what the user typed after /learn through the $ARGUMENTS placeholder and picks its mode from it.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *enables* `r03-0072`
  ↳ *evidence-for* `r04-0007`

- `r03-0067` *STATED* — The learn SKILL.md calls its script as 'python3 .claude/hooks/learn.py <command>' after /learn setup, or 'python3 "${CLAUDE_SKILL_DIR}/learn.py" <command>' before setup, always run from the project root.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0044`
  ↳ *example-of* `r04-0008`

- `r03-0068` *STATED* — If ${CLAUDE_SKILL_DIR} looks unexpanded inside a skill, use the 'Base directory for this skill' path that Claude Code printed when it loaded the skill.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *qualifies* `r03-0067`
  ↳ *evidence-for* `r01-0210`

- `r03-0071` *STATED* — In /learn, rules are added or changed only through 'LEARN add', 'LEARN merge' and 'LEARN drop', so the rulebook stays deduplicated and under its cap.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *enables* `r03-0048`
  ↳ *part-of* `r03-0070`

- `r03-0072` *STATED* — /learn mode table: 'setup' -> Setup; 'review' -> Review (the investigator); 'list' -> run LEARN list; 'status' -> run LEARN status; 'nightly' -> run LEARN nightly; blank -> learn from this conversation; anything else -> learn this lesson now.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)

- `r03-0075` *STATED* — After setup, /learn shows the user what the script printed and tells them in two lines: start a new session so the hook loads, and run /learn nightly to have the investigator run every night.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *leads-to* `r03-0033`
  ↳ *part-of* `r03-0027`

- `r03-0076` *STATED* — '/learn <lesson>' turns what the user typed into one rule and runs 'LEARN add "<rule>"', then shows the one line it printed: ADDED, MERGED or FULL.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *defines* `r03-0029`

- `r03-0077` *STATED* — If 'LEARN add' says FULL: run 'LEARN list', pick the two closest rules, merge them with 'LEARN merge N M "<one rule that covers both>"', then add again.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0076`
  ↳ *depends-on* `r03-0049`

- `r03-0078` *STATED* — Bare '/learn' finds the most recent time in the conversation the user corrected Claude, says in one line what Claude got wrong, then adds the rule; if there was no correction, it says so and asks what to remember.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *defines* `r03-0030`

- `r03-0088` *STATED* — If an old rule was too vague to stop a repeat, sharpen it with 'LEARN merge N N "<sharper rule>"': the same number twice replaces one rule.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0087`
  ↳ *enables* `r03-0011`

- `r03-0089` *STATED* — /learn review step 5, keep the rulebook short: run 'LEARN list'; if it shows rules that look alike, merge them; if it says FULL, merge or drop the weakest rule before adding.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0079`
  ↳ *leads-to* `r03-0090`
  ↳ *depends-on* `r03-0049`

- `r03-0119` *STATED* — Fix for demo lesson 1: check for pnpm-lock.yaml before running any package command, and use pnpm.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *leads-to* `r03-0112`
  ↳ *qualifies* `r03-0117`
  ↳ *qualifies* `r03-0006`

- `r03-0125` *STATED* — Fix for demo lesson 3: keep UTC through the database and the API; convert only where the date is shown. The note marks it 'MERGED into rule 1, now seen 2x. Sharpened: the old rule was too vague to stop this.'
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *leads-to* `r03-0109`

- `r03-0131` *STATED* — Fix for demo lesson 5: read the theme in tailwind.config.ts and use its token classes.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *leads-to* `r03-0115`

- `r03-0189` *STATED* — If a PDF cannot be read directly, /linkedin-roast tries 'pdftotext <file> -'; if that fails too, it asks for pasted text or a screenshot.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0154`
  ↳ *qualifies* `r03-0188`

- `r03-0249` *STATED* — SVG-to-PNG fallback chain, stop at the first that works: 'rsvg-convert -w 1584 -h 396', 'magick', 'inkscape', python 'cairosvg', or a headless browser.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *leads-to* `r03-0251`

- `r03-0250` *STATED* — Headless-browser PNG route: write banner.html, a margin-free page with the SVG in an <img width="1584" height="396">, then run Chrome, Chromium or Edge with '--headless --screenshot=banner.png --window-size=1584,396'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0249`

- `r03-0251` *STATED* — Check the PNG size with 'file banner.png' or 'sips -g pixelWidth -g pixelHeight banner.png': it must be 1584 x 396.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *leads-to* `r03-0252`

- `r04-0007` *CORE* — Alex's skills read the user's input with the $ARGUMENTS placeholder, written as a line like 'What the user typed after `/shark`: `$ARGUMENTS`', then branch on it.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill) [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill) [r-shark-skill](https://github.com/alexyc9381/shark-skill)

- `r04-0008` *CORE* — Alex's skills locate their own files with ${CLAUDE_SKILL_DIR}, and fall back to the 'Base directory for this skill' that Claude Code prints at the top of a skill if that path looks unexpanded.
  > “If the path looks unexpanded, use the "Base directory for this skill" that Claude Code printed at the top of this skill.”
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill) [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill) [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *enables* `r04-0057`
  ↳ *enables* `r04-0244`
  ↳ *enables* `r04-0174`

- `r04-0040` *STATED* — After installing a plugin, restart Claude Code or run /reload-plugins for it to load.
  > “Restart Claude Code (or run `/reload-plugins`).”
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *leads-to* `r04-0041`
  ↳ *evidence-for* `g05-0110`
  ↳ *contrast* `r03-0143`

- `r04-0181` *STATED* — Space routine runs an hour apart and a few minutes past the hour, because runs exactly on the hour can start late.
  > “runs exactly on the hour can start late”
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *evidence-for* `r04-0183`
  ↳ *qualifies* `g22-0073`

- `r04-0184` *STATED* — /schedule asks follow-up questions (repository, environment, connectors, model), and the night-crew skill tells the user how to answer each.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *qualifies* `r04-0182`

- `r04-0186` *STATED* — The night crew builder and tracker routines use the Default environment (Trusted network access: package registries and common development sites only).
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0184`
  ↳ *contrast* `r04-0187`

- `r04-0187` *STATED* — The scout routine reads the web, so give it an environment with Custom network access listing the sites it should read (e.g. reddit.com, news.ycombinator.com, indiehackers.com), or Full if the user accepts that.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0184`
  ↳ *qualifies* `r04-0091`

- `r04-0191` *STATED* — If /schedule says 'Unknown command', the user isn't signed in with a claude.ai subscription or is inside a cloud session; create the same routines at claude.ai/code/routines with the prompts and a Daily schedule.
  > “If `/schedule` says "Unknown command"”
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *qualifies* `r04-0179`
  ↳ *because* `r04-0100`

- `r04-0199` *STATED* — Morning step 1: list the crew's open pull requests with gh pr list --search "head:claude/" --state open; if gh isn't installed or signed in, ask the user to paste the repo's pull request list, and check routine runs if any failed.
  > “gh pr list --search "head:claude/" --state open”
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0107`
  ↳ *depends-on* `r04-0095`

- `r04-0225` *STATED* — Turn on accept-edits mode (Shift+Tab) before a /shark session so you are not asked to approve every file the sub-agents write.
  > “Turn on accept-edits mode (Shift+Tab) first so you are not asked to approve every file.”
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *because* `r04-0224` — many files written
  ↳ *contrast* `r04-0058` — relaxing permissions vs locking writes
  ↳ *evidence-for* `r01-0185`

- `r04-0248` *STATED* — The shark skill suggests accept-edits mode (Shift+Tab) for the session but does not change the user's settings itself.
  > “Do not change the user's settings yourself.”
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *qualifies* `r04-0225`
  ↳ *evidence-for* `r01-0215`

- `y01-0006` *STATED* — Alex demos Codex in the desktop app: select your ChatGPT account, and select Codex if the app opens in ChatGPT.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *leads-to* `y01-0007`

- `y01-0012` *STATED* — Codex model choices live in the model controls below the message box; if the selected model shows an effort slider, the effort settings appear there too.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *analogy-for* `g10-0181`
  ↳ *part-of* `y01-0007`

- `y01-0022` *STATED* — Typing a forward slash (/) in the Codex message box opens a list of commands - shortcuts to features.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *enables* `y01-0023`
  ↳ *enables* `y01-0033`

- `y01-0027` *STATED* — Add a local project in Codex from Projects and choose the folder it should use; Codex can then work in that folder without needing to read every file on your computer.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *part-of* `y01-0025`

- `y01-0033` *STATED* — Codex plan mode, found in the slash command menu, lets Codex define the changes in layout and approach before you ask it to make them - use it when you want help figuring out the approach first.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *analogy-for* `g03-0156`

- `y01-0035` *STATED* — In plan mode you discuss the plan, correct assumptions, and settle the details before any work is done.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *part-of* `y01-0033`

- `y01-0036` *STATED* — When you're ready for the work to be done, leave plan mode on and ask Codex to use the agreed plan.
  > “When you're ready for it to actually do the work, leave plan mode on and ask it to use the agreed plan.”
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *part-of* `y01-0033`

- `y01-0037` *STATED* — For small requests where you already know what you want, a normal chat is usually enough - no plan or goal mode needed.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *evidence-for* `g03-0164`
  ↳ *contrast* `y01-0033`
  ↳ *contrast* `y01-0038`

- `y01-0038` *STATED* — Codex goal mode, started with the goal command (/goal), gives Codex an outcome to work toward for longer work with several steps.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)

- `y01-0050` *STATED* — Enable Codex computer use through the computer use plugin.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *enables* `y01-0049`

- `y01-0051` *STATED* — On a Mac, Codex computer use needs Screen Recording permission (to see the app) and Accessibility permission (to control the app); the setup prompts guide you to those System Settings.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *part-of* `y01-0050`

- `y01-0058` *STATED* — A useful starting point for agent permissions is access that fits the job.
  > “A useful starting point is access that fits the job.”
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *qualifies* `y01-0057`
  ↳ *part-of* `y01-0055`

- `y01-0059` *STATED* — Review computer-use app access in Codex settings and check what each connected plugin is allowed to use.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *part-of* `y01-0055`

- `y01-0062` *STATED* — You can ask Codex to create or edit AGENTS.md for you in plain English.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *part-of* `y01-0061`

- `y01-0142` *STATED* — In the Claude app the effort control is a small button right next to the model selector; clicking it opens a slider between faster and smarter.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *analogy-for* `g10-0181`
  ↳ *part-of* `y01-0143`

- `y01-0155` *STATED* — To change an Artifact's layout, just tell Claude and it makes the updates in real time.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *part-of* `y01-0152`

- `y01-0162` *STATED* — Create a Claude Project: click the Projects tab on the left and create a new workspace.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *part-of* `y01-0161`

- `y01-0163` *STATED* — Build a Claude Project's knowledge base by dragging in your PDFs, brand voice and previous templates.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *leads-to* `y01-0162`

- `y02-0058` *STATED* — Bouncer step 1: before Claude changes anything, it must hand the bouncer a list of what it plans to touch.
  > “before Claude changes anything, you should hand it a list of what it plans to touch to a bouncer”
  — [70lNFy2fUIQ](https://youtu.be/70lNFy2fUIQ) [VpqXED1YiUM](https://youtu.be/VpqXED1YiUM)
  ↳ *evidence-for* `g08-0198`
  ↳ *part-of* `y02-0055`
  ↳ *leads-to* `y02-0059`

- `y02-0059` *STATED* — Bouncer step 2: the bouncer checks every planned item against what you actually asked for.
  — [70lNFy2fUIQ](https://youtu.be/70lNFy2fUIQ) [VpqXED1YiUM](https://youtu.be/VpqXED1YiUM)
  ↳ *evidence-for* `g08-0199`
  ↳ *part-of* `y02-0055`
  ↳ *leads-to* `y02-0060`

- `y02-0060` *STATED* — Bouncer step 3: any random extra changes Claude wants to make don't get made.
  — [70lNFy2fUIQ](https://youtu.be/70lNFy2fUIQ) [VpqXED1YiUM](https://youtu.be/VpqXED1YiUM)
  ↳ *evidence-for* `g08-0200`
  ↳ *part-of* `y02-0055`
  ↳ *leads-to* `y02-0061`

- `y02-0062` *INFERRED* — The bouncer pattern (declare intended file list, then gate every edit against the original request) maps naturally onto a Claude Code PreToolUse hook on Edit/Write that denies files outside the approved list.
  — [70lNFy2fUIQ](https://youtu.be/70lNFy2fUIQ) [VpqXED1YiUM](https://youtu.be/VpqXED1YiUM)
  ↳ *example-of* `g01-0126`
  ↳ *evidence-for* `g08-0202`
  ↳ *qualifies* `y02-0055` — how to build it

- `y02-0088` *CORE* — In the self-improving system, every correction goes into its own rulebook so Claude never repeats that mistake.
  > “every correction goes into its own rulebook so it never repeats that mistake”
  — [h0rtiWN_oIg](https://youtu.be/h0rtiWN_oIg) [3je0se5Ce_w](https://youtu.be/3je0se5Ce_w)
  ↳ *evidence-for* `r03-0008`
  ↳ *contradicts* `r03-0060` — short: Claude 'never repeats that mistake' vs repo: rules make a repeat 'much less likely, not impossible'
  ↳ *part-of* `y02-0086`
  ↳ *leads-to* `y02-0090`
  ↳ *contrast* `y02-0055` — learning from corrections vs blocking unrequested edits

- `y03-0045` *INFERRED* — Effort routing distilled from Alex's ladder: build on low, test on high, use xhigh to stress-test, max only for hard unattended jobs, and ultracode for one big task split across many Claudes.
  — [ItG-vSZFWgA](https://youtu.be/ItG-vSZFWgA) [mVKBGZNsSa4](https://youtu.be/mVKBGZNsSa4) [HTu9VPLvcP0](https://youtu.be/HTu9VPLvcP0)
  ↳ *evidence-for* `g10-0176`

- `y03-0052` *STATED* — Anthropic's team wrote one paragraph that tells Claude not to interrupt mid-task and to keep going; Alex shares the exact paragraph in a doc (comment 'stops').
  — [ThrAfrg8rjQ](https://youtu.be/ThrAfrg8rjQ) [DHCciHdW-Nw](https://youtu.be/DHCciHdW-Nw)
  ↳ *evidence-for* `g10-0138`
  ↳ *qualifies* `y03-0047` — Anthropic's fix paragraph for the early-quit modes
  ↳ *part-of* `y03-0062`

- `y03-0059` *STATED* — You only set up a verification loop once.
  — [vdYlR2BjM3o](https://youtu.be/vdYlR2BjM3o) [4FLM_FjtiBo](https://youtu.be/4FLM_FjtiBo) [0YmOIYAiwiM](https://youtu.be/0YmOIYAiwiM) [rDBGrDeXAh4](https://youtu.be/rDBGrDeXAh4)
  ↳ *evidence-for* `g12-0203`
  ↳ *depends-on* `y03-0060`

- `y03-0060` *CORE* — The first time, Claude figures out how to test your project and saves those steps so it runs the exact same test every time after.
  — [vdYlR2BjM3o](https://youtu.be/vdYlR2BjM3o) [4FLM_FjtiBo](https://youtu.be/4FLM_FjtiBo) [0YmOIYAiwiM](https://youtu.be/0YmOIYAiwiM) [rDBGrDeXAh4](https://youtu.be/rDBGrDeXAh4)
  ↳ *evidence-for* `g12-0203`
  ↳ *part-of* `y03-0055`

- `y03-0067` *STATED* — Prompt Audit scans your entire CLAUDE.md file looking for three problems.
  — [q-cfyZWRwmU](https://youtu.be/q-cfyZWRwmU)
  ↳ *part-of* `y03-0066`

- `y03-0091` *STATED* — You don't need to code to make a Claude Code mod: just ask Claude to build any mod for you.
  — [L9UlSAxSnrM](https://youtu.be/L9UlSAxSnrM)
  ↳ *evidence-for* `g10-0064`
  ↳ *enables* `y03-0087`
  ↳ *qualifies* `y03-0201`

- `y03-0099` *STATED* — Alex's fix for the Claude app freezing your Mac is one simple checklist (comment 'memory').
  — [5Ik2XpcR5uE](https://youtu.be/5Ik2XpcR5uE)
  ↳ *evidence-for* `g10-0025`
  ↳ *qualifies* `y03-0092` — the fix

- `y04-0027` *STATED* — /watch usage: type /watch, paste the video link (YouTube or any other), and add the instructions for what you want from the video.
  > “Just type in slash watch and put in the YouTube video, whatever video link you want, and tell it the instructions you want.”
  — [dXOq_pNqeFA](https://youtu.be/dXOq_pNqeFA) [bmUJ_ifeXIE](https://youtu.be/bmUJ_ifeXIE) [9DM6ZdHEWls](https://youtu.be/9DM6ZdHEWls)
  ↳ *part-of* `y04-0025`

- `y04-0083` *STATED* — To integrate any API, open Claude Code, paste the API link and say 'build me a feature using this'.
  > “You just open Claude, paste the API link and say, build me a feature using this.”
  — [-U14AktLSiM](https://youtu.be/-U14AktLSiM)
  ↳ *evidence-for* `g13-0154`
  ↳ *part-of* `y04-0084`
  ↳ *depends-on* `y04-0080`

### number

- `g02-0052` *STATED* — cc-stretch replies show about a sixth of the words by default, with roughly two of every three key points.
  — [g-make-claude-s-long-answers-6x-shorter-to-read](https://chen.media/guides/make-claude-s-long-answers-6x-shorter-to-read)
  ↳ *evidence-for* `g02-0047`
  ↳ *leads-to* `g02-0053`

- `g02-0202` *STATED* — The /usage Loops row needs Claude Code 2.1.242 or later.
  — [g-find-the-claude-code-loops-that-are-quietly-eating-your-limit](https://chen.media/guides/find-the-claude-code-loops-that-are-quietly-eating-your-limit)
  ↳ *qualifies* `g02-0201`

- `g03-0020` *STATED* — The docs' target for CLAUDE.md is under 200 lines per file.
  — [g-shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit](https://chen.media/guides/shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit)
  ↳ *part-of* `g03-0021`
  ↳ *contradicts* `g18-0237` — CLAUDE.md target length: 'under 200 lines per file' (docs) vs 'a single screen'

- `g03-0031` *STATED* — The path-only @ mention setting arrived in Claude Code 2.1.299 (October 14, 2026).
  — [g-stop-file-mentions-from-pasting-whole-files-into-your-claude-chat](https://chen.media/guides/stop-file-mentions-from-pasting-whole-files-into-your-claude-chat)
  ↳ *qualifies* `g03-0030`
  ↳ *qualifies* `g04-0250` — 2.1.299 (Oct 14) also brought path-only @ mentions, not only /usage habit warnings

- `g03-0050` *STATED* — When Claude's servers are at capacity, Claude Code by default retries a failed request up to 10 times with exponential backoff, then shows you the error.
  — [g-keep-claude-retrying-overnight-when-the-api-is-busy](https://chen.media/guides/keep-claude-retrying-overnight-when-the-api-is-busy)
  ↳ *leads-to* `g03-0051`

- `g06-0099` *STATED* — Claude Code voice needs v2.1.69 or later; tap mode needs v2.1.116 or later.
  — [g-talk-to-claude-code-instead-of-typing](https://chen.media/guides/talk-to-claude-code-instead-of-typing)

- `g06-0118` *STATED* — Coucou permission requests expire after 2 minutes.
  — [g-approve-claude-s-permission-requests-from-your-iphone-with-coucou](https://chen.media/guides/approve-claude-s-permission-requests-from-your-iphone-with-coucou)
  ↳ *qualifies* `g06-0115`

- `g06-0154` *STATED* — bigarrow's arrow removes itself after 8 seconds for a quick point, or stays up to 5 minutes; you can also close it.
  — [g-make-claude-point-at-the-button-you-need-to-click](https://chen.media/guides/make-claude-point-at-the-button-you-need-to-click)
  ↳ *part-of* `g06-0149`

- `g06-0243` *STATED* — Claude Code auto memory loads only its first 200 lines or 25KB at the start of each session.
  — [g-give-claude-a-notebook-that-survives-every-chat-reset](https://chen.media/guides/give-claude-a-notebook-that-survives-every-chat-reset)
  ↳ *qualifies* `g06-0242`

- `g07-0171` *STATED* — Mods are on by default in Claude Code 2.1.287 or later.
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`
  ↳ *leads-to* `g07-0172`

- `g10-0026` *STATED* — Alex Chen's Claude app memory-leak checklist guide contains 16 numbered steps.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *part-of* `g10-0025`

- `g10-0048` *STATED* — Alex Chen's Claude Code mods guide contains 5 prompts to copy and 10 numbered steps.
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *part-of* `g10-0047`

- `g10-0054` *STATED* — On October 1, Anthropic's ClaudeDevs account announced that you can now mod Claude Code: change how it behaves, customize the screen, and swap in your own features.
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *enables* `g10-0046`

- `g10-0070` *STATED* — Alex Chen's Hugging Face hack / 5 login rules guide contains 24 numbered steps.
  — [g-openai-agents-hacked-hugging-face-5-login-rules](https://chen.media/guides/openai-agents-hacked-hugging-face-5-login-rules)
  ↳ *part-of* `g10-0069`

- `g10-0175` *STATED* — Alex Chen's Claude Code effort-levels guide contains 2 prompts to copy and 10 numbered steps.
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *part-of* `g10-0174`

- `g12-0258` *STATED* — At the 75th percentile, starting a new Claude Code session went from 0.8 s to 0.3 s.
  — [g-how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill](https://chen.media/guides/how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill)
  ↳ *evidence-for* `g12-0252`

- `g13-0110` *STATED* — Alex's 'Claude Code Now Runs With Your Laptop Closed' guide has 5 copyable prompts and 8 numbered steps.
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it)
  ↳ *part-of* `g13-0093`

- `g13-0118` *STATED* — Alex's 'How to Claim Up to $250 of Free Claude Code Credit' guide has 5 copyable prompts and 11 numbered steps.
  — [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)
  ↳ *part-of* `g13-0093`

- `g14-0230` *STATED* — ECC's Claude plugin setup also requires Git and Claude Code 2.1 or newer on your PATH.
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)

- `g16-0032` *STATED* — /design needs Claude Code v2.1.233 or later.
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)

- `g18-0237` *STATED* — A good target length for a CLAUDE.md is a single screen.
  — [g-three-things-almost-everyone-gets-wrong-about-claude-code](https://chen.media/guides/three-things-almost-everyone-gets-wrong-about-claude-code)
  ↳ *part-of* `g18-0228`

- `g20-0230` *STATED* — The memory upgrade alone is already worth its 10 minutes of setup.
  > “Memory alone is already worth the 10 minutes.”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *qualifies* `g20-0231`

- `g22-0072` *STATED* — Claude Code Routines are available on paid plans (Pro, Max, Team, Enterprise) in research preview.
  — [g-put-a-recurring-job-on-autopilot-with-claude-code](https://chen.media/guides/put-a-recurring-job-on-autopilot-with-claude-code)
  ↳ *qualifies* `g22-0070`

- `g22-0073` *STATED* — The minimum schedule for a Claude Code Routine is once an hour.
  — [g-put-a-recurring-job-on-autopilot-with-claude-code](https://chen.media/guides/put-a-recurring-job-on-autopilot-with-claude-code)
  ↳ *qualifies* `g22-0078`

- `r01-0059` *STATED* — The /agency sales agent re-reads the live transcript file every 10 seconds.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0092`

- `r03-0049` *CORE* — The /learn rulebook is capped at 40 rules so it stays short enough to be followed.
  > “The book is capped at 40 rules, so it stays short enough to be followed”
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *qualifies* `r03-0014`

- `y03-0093` *STATED* — One user left the Claude app open and it ate about 120GB of memory.
  — [5Ik2XpcR5uE](https://youtu.be/5Ik2XpcR5uE)
  ↳ *contradicts* `g10-0038` — headline leak example differs: ~120GB on a 96GB Mac (short) vs 131-140GB on a 48GB Mac (guide)
  ↳ *evidence-for* `g10-0033`
  ↳ *evidence-for* `y03-0092`
  ↳ *part-of* `y03-0096`

- `y03-0095` *STATED* — That user's Mac only had about 96GB of memory.
  — [5Ik2XpcR5uE](https://youtu.be/5Ik2XpcR5uE)
  ↳ *part-of* `y03-0096`

### opinion

- `g03-0082` *STATED* — Most people leave a Claude Code window open and watch it work instead of running it in the background.
  — [g-keep-claude-working-after-you-close-the-terminal](https://chen.media/guides/keep-claude-working-after-you-close-the-terminal)
  ↳ *example-of* `g03-0008`
  ↳ *contrast* `g03-0081`

- `g04-0069` *STATED* — Alex's position: a crashed guard hook should block the action, not let it through.
  > “Make a Crashed Claude Hook Block the Action, Not Let It Through”
  — [g-make-a-crashed-claude-hook-block-the-action-not-let-it-through](https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through)
  ↳ *because* `g04-0055`
  ↳ *part-of* `g04-0070`

- `g10-0193` *STATED* — None of the effort levels' outputs is wrong; they suit different goals.
  > “None of these is wrong.”
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *qualifies* `g10-0188`

- `g17-0250` *STATED* — There is a lot of free Claude content and most of it is a tour of the interface.
  > “most of it is a tour of the interface”
  — [g-three-free-claude-courses-and-what-to-do-with-them](https://chen.media/guides/three-free-claude-courses-and-what-to-do-with-them)

- `g18-0242` *STATED* — Deleting your CLAUDE.md every six months cuts against almost every Claude setup guide on the internet.
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *qualifies* `g18-0241`

- `g20-0223` *STATED* — Everyone is waiting for the next model, but you do not have to.
  > “Everyone is waiting for the next model. You do not have to.”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *contrast* `g20-0224`

- `g23-0067` *STATED* — 2026 tier list, Building apps (in the video): bad Bolt, mid Lovable, great pick Claude Code.
  — [g-the-2026-ai-tool-tier-list-with-the-reason-for-each-pick](https://chen.media/guides/the-2026-ai-tool-tier-list-with-the-reason-for-each-pick)
  ↳ *part-of* `g23-0051`
  ↳ *because* `g23-0068`
  ↳ *contradicts* `g23-0189` — tier list rates Bolt bad for building apps; hype swaps recommend Bolt.new over v0 for its full-stack code

- `r02-0024` *STATED* — Alex's position: a Claude Code skill cannot, and should not, send job applications behind your back.
  > “A Claude Code skill cannot, and should not, send applications behind your back.”
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *because* `r02-0025`

- `y02-0091` *STATED* — Alex Chen: every day you don't run the self-improving system, your Claude gets 'dumber and dumber'.
  > “every day you don't run it, your Claude gets dumber and dumber”
  — [h0rtiWN_oIg](https://youtu.be/h0rtiWN_oIg) [3je0se5Ce_w](https://youtu.be/3je0se5Ce_w)
  ↳ *contrast* `y02-0090`

### product

- `g01-0122` *STATED* — CC Safety Net is a free, open-source guard for Claude Code that checks what a command or file read would really do before Claude runs it.
  — [g-safety-net-stop-claude-deleting-your-files-before-the-command-runs](https://chen.media/guides/safety-net-stop-claude-deleting-your-files-before-the-command-runs)

- `g02-0046` *STATED* — cc-stretch is a free Claude Code plugin that shows you about a sixth of each reply and lets you click any phrase to open the rest in place.
  — [g-make-claude-s-long-answers-6x-shorter-to-read](https://chen.media/guides/make-claude-s-long-answers-6x-shorter-to-read)
  ↳ *example-of* `g02-0241`

- `g02-0117` *STATED* — Time Machine is a free Claude Code mod that records every step Claude takes and saves your files after each one.
  — [g-rewind-claude-code-to-the-step-that-broke-your-code](https://chen.media/guides/rewind-claude-code-to-the-step-that-broke-your-code)
  ↳ *because* `g02-0118`
  ↳ *example-of* `g10-0056`
  ↳ *contrast* `g03-0112`

- `g06-0113` *CORE* — Coucou is a free, open-source app that watches Claude Code from your Mac's notch and sends its permission requests to your iPhone.
  — [g-approve-claude-s-permission-requests-from-your-iphone-with-coucou](https://chen.media/guides/approve-claude-s-permission-requests-from-your-iphone-with-coucou)
  ↳ *evidence-for* `g09-0237`

- `g06-0149` *STATED* — bigarrow is a free Mac tool that lets Claude draw a big arrow and a sign on top of any app, so it can show you the exact button instead of describing it.
  — [g-make-claude-point-at-the-button-you-need-to-click](https://chen.media/guides/make-claude-point-at-the-button-you-need-to-click)
  ↳ *because* `g06-0150`

- `g07-0160` *CORE* — Anthropic shared three sample Claude Code mods: a forecast of how full Claude's memory is, a guard that freezes rm -rf and shows what it would delete, and a replay of every edit Claude just made.
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`
  ↳ *generalizes* `g10-0060`

- `g07-0168` *STATED* — blast-radius is Anthropic's sample delete-guard mod: it freezes rm -rf and shows what it would delete.
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`
  ↳ *part-of* `g07-0160`
  ↳ *example-of* `g07-0164` — steps in before rm -rf runs
  ↳ *evidence-for* `g10-0061`
  ↳ *evidence-for* `g01-0131`

- `g07-0170` *STATED* — replay-theater is Anthropic's sample mod that replays every edit Claude just made.
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`
  ↳ *part-of* `g07-0160`
  ↳ *evidence-for* `g10-0062`
  ↳ *analogy-for* `g02-0120`

- `g08-0191` *CORE* — The free /bouncer Claude Code skill makes Claude list everything it plans to touch, check each item against what you asked, and only make the ones that pass.
  — [g-stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes](https://chen.media/guides/stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes)

- `g08-0237` *STATED* — The free /trojan Claude Code skill checks a file before Claude reads it: three checks, with the hidden text shown in red.
  — [g-stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes](https://chen.media/guides/stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes)
  ↳ *contrast* `g08-0073` — untrusted-file check vs attacker review of your own code

- `g09-0031` *STATED* — Alex's free Claude Code lessons skill keeps a rulebook every session reads, and a second Claude goes over each day's mistakes at night and writes the lessons back in.
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *part-of* `g09-0029`
  ↳ *because* `g09-0030`
  ↳ *evidence-for* `r01-0034`

- `g14-0058` *STATED* — Claude HUD exposes Claude Code session activity.
  > “Claude HUD exposes session activity”
  — [g-headroom-claude-hud-aisa-setup](https://chen.media/guides/headroom-claude-hud-aisa-setup)
  ↳ *part-of* `g14-0056`

- `g16-0016` *STATED* — /design is a Claude Code command that publishes a design: a canvas of editable artboards for your UI, and Claude prints you the link to it.
  > “Claude Code can now publish a design.”
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)
  ↳ *part-of* `g16-0018`
  ↳ *leads-to* `g16-0027`
  ↳ *depends-on* `g16-0032`
  ↳ *depends-on* `g16-0033`
  ↳ *depends-on* `g16-0035`
  ↳ *example-of* `g16-0001`

- `g18-0166` *STATED* — Plugin 2 of 5: claude-mem, memory that survives between sessions.
  > “claude-mem, memory that survives”
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *part-of* `g18-0154`
  ↳ *example-of* `g18-0289`
  ↳ *contrast* `g18-0183` — automatic memory plugin vs manual wrap-up to NotebookLM
  ↳ *evidence-for* `g17-0098`

- `g18-0272` *STATED* — Agent Memory: rohitg00/agentmemory, 25.9k stars, Apache-2.0.
  — [g-seven-free-repos-that-replace-paid-ai-tools](https://chen.media/guides/seven-free-repos-that-replace-paid-ai-tools)
  ↳ *part-of* `g18-0262`
  ↳ *example-of* `g18-0289`

- `r01-0034` *CORE* — /learn (github.com/alexyc9381/learn-skill): a Claude that stops making the same mistake twice — every correction goes into a rulebook every session reads.
  — [r-alexyc9381](https://github.com/alexyc9381/alexyc9381)
  ↳ *part-of* `r01-0026`

- `y02-0055` *STATED* — Alex Chen built a free 'bouncer' for Claude Code that blocks any changes you didn't ask for (CTA keyword 'bouncer').
  > “I built a bouncer in Claude that blocks any changes you didn't ask for”
  — [70lNFy2fUIQ](https://youtu.be/70lNFy2fUIQ) [VpqXED1YiUM](https://youtu.be/VpqXED1YiUM)
  ↳ *evidence-for* `g08-0191`

- `y02-0086` *STATED* — Alex Chen's self-improving system for Claude (repo link via CTA keyword 'learn') fixes the problem of correcting the same Claude mistakes over and over.
  > “You know how you keep fixing the same mistakes in Claude over and over again? This system fixes exactly that.”
  — [h0rtiWN_oIg](https://youtu.be/h0rtiWN_oIg) [3je0se5Ce_w](https://youtu.be/3je0se5Ce_w)
  ↳ *evidence-for* `r01-0034`

- `y03-0066` *STATED* — Anthropic's Claude team built one command, Prompt Audit, that automatically fixes your CLAUDE.md for you.
  — [q-cfyZWRwmU](https://youtu.be/q-cfyZWRwmU)
  ↳ *evidence-for* `g16-0269`
  ↳ *qualifies* `y03-0063` — the fix

### resource

- `g02-0058` *STATED* — The cc-stretch guide has 1 prompt and 6 numbered steps, with sections What you get, Step 1: install it, Step 2: use it, The catch, and Sources; its subtitle promises several catches.
  — [g-make-claude-s-long-answers-6x-shorter-to-read](https://chen.media/guides/make-claude-s-long-answers-6x-shorter-to-read)
  ↳ *part-of* `g02-0046`
  ↳ *example-of* `g02-0232`
  ↳ *example-of* `g02-0233`

- `g02-0128` *STATED* — The Time Machine guide has 1 prompt 'to try it safely' and 4 numbered steps, with email-gated 'Step 1: install it' and 'The catches' sections.
  — [g-rewind-claude-code-to-the-step-that-broke-your-code](https://chen.media/guides/rewind-claude-code-to-the-step-that-broke-your-code)
  ↳ *part-of* `g02-0117`
  ↳ *example-of* `g02-0232`
  ↳ *example-of* `g02-0233`

- `g03-0172` *STATED* — The autoContinueAtUsageLimit setting (user or managed settings) controls the auto-continue behaviour.
  — [g-let-claude-code-wait-out-your-limit-and-carry-on](https://chen.media/guides/let-claude-code-wait-out-your-limit-and-carry-on)
  ↳ *enables* `g03-0166`
  ↳ *part-of* `g03-0010`

- `g03-0222` *STATED* — Custom helper agents live in .claude/agents/ in a project or in ~/.claude/agents/ in your user folder.
  — [g-shorten-your-claude-helper-agent-descriptions](https://chen.media/guides/shorten-your-claude-helper-agent-descriptions)
  ↳ *qualifies* `g03-0220`
  ↳ *evidence-for* `g03-0252` — same agent folders

- `g04-0070` *STATED* — Guide: 'Make a Crashed Claude Hook Block the Action, Not Let It Through' at https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through.
  — [g-make-a-crashed-claude-hook-block-the-action-not-let-it-through](https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through)
  ↳ *example-of* `g04-0243`

- `g04-0096` *STATED* — Guide: 'The Claude Hook That Cuts Test Output Down to Just the Failures' at https://chen.media/guides/the-claude-hook-that-cuts-test-output-down-to-just-the-failures (2 prompts, 5 steps).
  — [g-the-claude-hook-that-cuts-test-output-down-to-just-the-failures](https://chen.media/guides/the-claude-hook-that-cuts-test-output-down-to-just-the-failures)
  ↳ *example-of* `g04-0243`

- `g05-0069` *CORE* — CLAUDE.md stop rule (paste-in): 'When a step doesn't need my input, keep going.'
  > “When a step doesn't need my input, keep going.”
  — [g-your-opus-5-5-prompt-checklist](https://chen.media/guides/your-opus-5-5-prompt-checklist)
  ↳ *part-of* `g05-0066`
  ↳ *example-of* `g05-0319`
  ↳ *evidence-for* `y03-0052`

- `g05-0070` *STATED* — CLAUDE.md stop rule (paste-in): 'Put status notes in the same message as your next action.'
  > “Put status notes in the same message as your next action.”
  — [g-your-opus-5-5-prompt-checklist](https://chen.media/guides/your-opus-5-5-prompt-checklist)
  ↳ *part-of* `g05-0066`

- `g05-0071` *STATED* — CLAUDE.md stop rule (paste-in): 'Stop and ask only when you can't continue without me, or before anything destructive: deleting data, force-pushing, or changing anything outside this repository.'
  > “Stop and ask only when you can't continue without me, or before anything destructive: deleting data, force-pushing, or changing anything outside this repository.”
  — [g-your-opus-5-5-prompt-checklist](https://chen.media/guides/your-opus-5-5-prompt-checklist)
  ↳ *part-of* `g05-0066`
  ↳ *example-of* `g05-0062`
  ↳ *example-of* `g05-0321`
  ↳ *qualifies* `g05-0069`

- `g05-0157` *STATED* — CLAUDE.md cache rule (paste-in): 'Prompt cache rule: stay on one model and one effort level for the whole task. Do not suggest switching models with /model or running /compact in the middle of a task; wait for a natural break between tasks and ask me first.'
  > “Prompt cache rule: stay on one model and one effort level for the whole task. Do not suggest switching models with /model or running /compact in the middle of a task; wait for a natural break between tasks and ask me first.”
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)
  ↳ *example-of* `g05-0319`
  ↳ *qualifies* `g10-0182`
  ↳ *qualifies* `g06-0267`

- `g06-0246` *STATED* — The notebook guide includes a starter CLAUDE.md to paste.
  — [g-give-claude-a-notebook-that-survives-every-chat-reset](https://chen.media/guides/give-claude-a-notebook-that-survives-every-chat-reset)
  ↳ *part-of* `g06-0249`

- `g09-0029` *STATED* — chen.media guide 'Make Claude Stop Repeating Its Mistakes: The Free Skill That Turns Every Correction Into a Rule' (https://chen.media/guides/claude-that-stops-repeating-its-mistakes) has 4 prompts to copy and 4 numbered steps; sections: How it works; Get the skill; Set it up in your project; Make it run every night; What one day of lessons looks like; Good to know.
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *example-of* `g09-0253`

- `g10-0174` *STATED* — Alex Chen's effort-levels cheat sheet is built from Anthropic's own docs and tests and gives a one-page guide to which effort level fits each task.
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *qualifies* `g10-0173`

- `g12-0204` *STATED* — Anthropic's post 'Building verification loops in Claude Code with skills': https://claude.com/blog/building-verification-loops-in-claude-code-with-skills
  — [g-how-to-make-claude-test-its-own-work-the-verification-loop](https://chen.media/guides/how-to-make-claude-test-its-own-work-the-verification-loop)
  ↳ *evidence-for* `g12-0200`
  ↳ *example-of* `g12-0300`

- `g14-0008` *STATED* — The marketing workflow guide links Anthropic's documentation 'How Claude Code subagents work'.
  — [g-marketing-agent-workflow-setup](https://chen.media/guides/marketing-agent-workflow-setup)
  ↳ *part-of* `g14-0001`
  ↳ *evidence-for* `g14-0006`

- `g14-0056` *STATED* — Alex's guide 'Three Tools for Claude Code: Headroom, Claude HUD and AIsa' gives his SETUP video's three links, current installation commands and a competitor-research prompt you can verify.
  — [g-headroom-claude-hud-aisa-setup](https://chen.media/guides/headroom-claude-hud-aisa-setup)
  ↳ *example-of* `g14-0346`

- `g14-0085` *STATED* — Alex's guide 'Write intent.md Before You Ask Claude to Build' (for his INTENT videos) gives a reusable project brief and three prompts to turn an idea into a specification, implementation plan and verifiable result.
  — [g-intent-md-claude-project-setup](https://chen.media/guides/intent-md-claude-project-setup)
  ↳ *example-of* `g14-0346`

- `g14-0088` *STATED* — Anthropic publishes an 'AI-Native SDLC playbook' that the intent.md guide is based on.
  > “Read Anthropic's AI-Native SDLC playbook”
  — [g-intent-md-claude-project-setup](https://chen.media/guides/intent-md-claude-project-setup)
  ↳ *part-of* `g14-0085`

- `g14-0097` *STATED* — The intent.md guide includes an original intent template to adapt to your next small build.
  > “Adapt this original intent template”
  — [g-intent-md-claude-project-setup](https://chen.media/guides/intent-md-claude-project-setup)
  ↳ *part-of* `g14-0085`
  ↳ *example-of* `g14-0091`

- `g14-0166` *STATED* — Amazon Bedrock console instructions: https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started-console.html
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *evidence-for* `g14-0139`

- `g14-0167` *STATED* — Bedrock model access and the Anthropic form: https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *evidence-for* `g14-0141`

- `g15-0125` *STATED* — The official Claude Code prompt library lives at code.claude.com/docs/en/prompt-library.
  — [g-the-official-claude-code-prompt-library-52-free-prompts](https://chen.media/guides/the-official-claude-code-prompt-library-52-free-prompts)
  ↳ *defines* `g15-0122`

- `g16-0269` *STATED* — There is also an official version of this CLAUDE.md audit.
  > “There is also an official version of this”
  — [g-why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it](https://chen.media/guides/why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it)
  ↳ *contrast* `g16-0257`

- `g17-0254` *STATED* — Course 1 (makes you competent): Nick Saraev's Claude Code full course.
  > “1. Nick Saraev, Claude Code full course”
  — [g-three-free-claude-courses-and-what-to-do-with-them](https://chen.media/guides/three-free-claude-courses-and-what-to-do-with-them)
  ↳ *part-of* `g17-0253`
  ↳ *leads-to* `g17-0255`

- `g17-0255` *STATED* — Course 2 (widens what you can point the tool at): AI Master's full Claude course.
  > “2. AI Master, full Claude course”
  — [g-three-free-claude-courses-and-what-to-do-with-them](https://chen.media/guides/three-free-claude-courses-and-what-to-do-with-them)
  ↳ *part-of* `g17-0253`
  ↳ *leads-to* `g17-0256`

- `g18-0060` *STATED* — multica-ai/andrej-karpathy-skills is a GitHub repo with 199,884 stars and 20,560 forks that is 20 KB total, because the entire repository is a single CLAUDE.md file with no code in it at all.
  — [g-the-20-kb-file-that-stops-claude-doing-four-dumb-things](https://chen.media/guides/the-20-kb-file-that-stops-claude-doing-four-dumb-things)
  ↳ *contradicts* `g18-0237` — a 20 KB CLAUDE.md is far past Boris Cherny's one-screen target
  ↳ *contradicts* `g18-0246` — Alex promotes a 20 KB CLAUDE.md yet says CUT any 200+ line CLAUDE.md

- `g18-0245` *STATED* — Alex's keep-or-cut list for a Claude setup has fourteen rows, one verdict each, and the reason behind it: eight CUT, six KEEP.
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *leads-to* `g18-0261`

- `g20-0141` *STATED* — Alex Chen's chen.media guide 'The Five Files That Give Claude a Real Memory' (category: Claude Code): five files and prompts so Claude stops forgetting you the second you close the chat; 5 prompts to copy.
  > “so it stops forgetting you the second you close the chat”
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)

- `g20-0222` *STATED* — Alex Chen's chen.media guide 'Four Upgrades That Make Claude Code Run Like a Newer Model' (category: Claude Code) is 'the exact system that makes today's Claude run like the model that isn't out yet'; 6 prompts to copy.
  > “The exact system that makes today's Claude run like the model that isn't out yet.”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)

- `g21-0159` *STATED* — Alex's chen.media guide 'The Fable 5 Guide: Effort, Memory and Self-Verification' (section: Prompting) gives four fixes for Claude Fable 5 pulled from Anthropic's own Fable 5 docs, with paste-ready lines.
  — [g-the-fable-5-guide-effort-memory-and-self-verification](https://chen.media/guides/the-fable-5-guide-effort-memory-and-self-verification)

- `g22-0162` *STATED* — Alex Chen's chen.media guide 'The Four Files That Make Claude Sound Like You' (section: Claude Code) gives a fill-in template for each of four voice files (4 prompts, 13 sections email-gated).
  — [g-the-four-files-that-make-claude-sound-like-you](https://chen.media/guides/the-four-files-that-make-claude-sound-like-you)

- `g22-0239` *STATED* — Alex Chen's chen.media guide 'Turn Your Camera Roll Into Something You Can Search' (section: Tools & repos) turns screenshots and notes into a searchable second brain in a Claude Project.
  — [g-turn-your-camera-roll-into-something-you-can-search](https://chen.media/guides/turn-your-camera-roll-into-something-you-can-search)

- `r02-0023` *STATED* — The /hunter SKILL.md argument-hint is "setup | run | job <posting url or pasted text> | review | applied <number or all> | log | morning".
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *defines* `r02-0017`

- `r02-0166` *STATED* — The /launch SKILL.md argument-hint is "[--quick | --only tests,security | --recheck] [what is launching]".
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *defines* `r02-0144`

- `r04-0111` *STATED* — You can see every routine run, pause or delete a routine at claude.ai/code/routines or with /schedule list.
  > “claude.ai/code/routines or with `/schedule list`”
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0089`
  ↳ *part-of* `g22-0070`

- `r04-0179` *STATED* — Routines are created with /schedule in the Claude Code CLI, at claude.ai/code/routines, or in the Desktop app (Code tab, then Routines, then New routine, then Cloud).
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0089`
  ↳ *part-of* `g22-0070`

### result

- `g02-0051` *STATED* — In the cc-stretch author's test on 69 real replies, what you see first was 17% of the words.
  — [g-make-claude-s-long-answers-6x-shorter-to-read](https://chen.media/guides/make-claude-s-long-answers-6x-shorter-to-read)
  ↳ *evidence-for* `g02-0047`
  ↳ *example-of* `g02-0236`

- `g10-0033` *STATED* — Reports on Anthropic's own GitHub describe the Claude desktop app on a Mac climbing past 100 GB of memory until macOS says "Your system has run out of application memory" and stops responding.
  > “Your system has run out of application memory”
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *evidence-for* `g10-0024`

- `g10-0038` *STATED* — One Mac with 48 GB of memory watched Claude Desktop grow to 131-140 GB, three times, and freeze.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *evidence-for* `g10-0037`

- `g10-0039` *STATED* — The same work that pushed Claude Desktop to 131-140 GB stayed under 200 MB in Claude Code in the Terminal.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *contrast* `g10-0038`

- `g10-0041` *STATED* — Overnight with the lid closed, leftover Claude Code background processes pushed memory up about 100 GB in under an hour and swap hit 46 GB before the Mac hung.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *evidence-for* `g10-0040`
  ↳ *because* `g10-0268`

- `g10-0042` *STATED* — A single MCP server grew to 30 GB on a 16 GB MacBook Air, with swap 75% full.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *evidence-for* `g10-0037`

- `g10-0089` *STATED* — A security firm scanning public Hugging Face datasets found 787 tokens that still worked, 237 of them able to write.
  — [g-openai-agents-hacked-hugging-face-5-login-rules](https://chen.media/guides/openai-agents-hacked-hugging-face-5-login-rules)
  ↳ *evidence-for* `g10-0091`

- `g10-0189` *STATED* — At low effort the fitness tracker took 1.5 minutes and produced a log and a simple graph: a base to build on.
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *part-of* `g10-0188`
  ↳ *evidence-for* `g10-0194`
  ↳ *evidence-for* `g10-0195` — 67 / 1.5 = ~45x

- `g10-0190` *STATED* — At medium effort the fitness tracker took 4 minutes, with more to it and more detail.
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *part-of* `g10-0188`

- `g10-0191` *STATED* — At high effort the fitness tracker took 11 minutes: more complex, with more choices made for him.
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *part-of* `g10-0188`
  ↳ *evidence-for* `g10-0187` — more choices made for him

- `g10-0192` *STATED* — At max effort the fitness tracker took 67 minutes: the most complete version, down to a heat chart.
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *part-of* `g10-0188`
  ↳ *evidence-for* `g10-0195`

- `g16-0258` *CORE* — Anthropic removed over 80 percent of Claude Code's system prompt for the Claude 5 generation and measured no loss on their coding evaluations.
  — [g-why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it](https://chen.media/guides/why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it)
  ↳ *evidence-for* `g16-0260`
  ↳ *evidence-for* `g16-0009` — Anthropic's own cut shows less instruction text cost nothing
  ↳ *evidence-for* `g18-0284`

- `g18-0229` *STATED* — Boris Cherny deleted roughly 80% of Claude Code's system prompt, and the tool got better.
  — [g-three-things-almost-everyone-gets-wrong-about-claude-code](https://chen.media/guides/three-things-almost-everyone-gets-wrong-about-claude-code)
  ↳ *evidence-for* `g18-0228`
  ↳ *evidence-for* `g18-0284`
  ↳ *contradicts* `g16-0258` — Boris Cherny deleted ~80% of the system prompt 'and the tool got better' vs Anthropic removed 80%+ and 'measured no loss'

- `y02-0061` *STATED* — With the bouncer you never find surprise changes that break your app days later.
  — [70lNFy2fUIQ](https://youtu.be/70lNFy2fUIQ) [VpqXED1YiUM](https://youtu.be/VpqXED1YiUM)
  ↳ *contradicts* `g08-0201` — short: with the bouncer 'you never find surprise changes' vs guide: /bouncer 'is a rule, not a lock, so skim its list'
  ↳ *part-of* `y02-0055`

### style

- `g05-0319` *CORE* — Alex fixes Claude behaviour with paste-ready CLAUDE.md rules: stop rules for long Opus 5.5 runs, and a prompt-cache rule.
  — [g-your-opus-5-5-prompt-checklist](https://chen.media/guides/your-opus-5-5-prompt-checklist) [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)

- `g16-0171` *STATED* — There are no clever prompts in the fifteen tips; every item is a setting, a surface or a habit.
  > “Every item below is a setting, a surface or a habit”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *because* `g16-0170`

### warning

- `g01-0124` *STATED* — Claude Code runs real commands on your machine; most are harmless, but one wrong git reset --hard or rm -rf can wipe work you never committed.
  > “one wrong git reset --hard or rm -rf can wipe work you never committed”
  — [g-safety-net-stop-claude-deleting-your-files-before-the-command-runs](https://chen.media/guides/safety-net-stop-claude-deleting-your-files-before-the-command-runs)
  ↳ *because* `g01-0122`
  ↳ *evidence-for* `g01-0130`

- `g03-0051` *STATED* — If you start a long Claude Code job and go to bed, the busy-API error after the default retries is where the job stops.
  — [g-keep-claude-retrying-overnight-when-the-api-is-busy](https://chen.media/guides/keep-claude-retrying-overnight-when-the-api-is-busy)
  ↳ *leads-to* `g03-0053`

- `g04-0055` *STATED* — By default, a Claude Code hook that crashes, times out or can't start lets the action run anyway.
  — [g-make-a-crashed-claude-hook-block-the-action-not-let-it-through](https://chen.media/guides/make-a-crashed-claude-hook-block-the-action-not-let-it-through)

- `g04-0209` *STATED* — There is a catch that makes the subagent compaction line silently do nothing (Alex's 'The catch' section, body locked).
  > “the catch that makes it silently do nothing”
  — [g-make-your-claude-helper-agents-compact-their-own-chat-early](https://chen.media/guides/make-your-claude-helper-agents-compact-their-own-chat-early)
  ↳ *qualifies* `g04-0207`
  ↳ *example-of* `g04-0242`

- `g05-0067` *STATED* — Keep permission prompts on for destructive commands too, even with CLAUDE.md stop rules in place.
  — [g-your-opus-5-5-prompt-checklist](https://chen.media/guides/your-opus-5-5-prompt-checklist)
  ↳ *qualifies* `g05-0066`

- `g07-0173` *STATED* — If you set CLAUDE_CODE_ENABLE_FUNCTION_HOOKS during the mods early access, remove it: new Claude Code versions ignore it.
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`
  ↳ *qualifies* `g07-0171`

- `g07-0175` *STATED* — A Claude Code mod runs with your permissions: it can read and write your files, run programs, go online, read the keys in your settings, and see every prompt you send.
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`
  ↳ *because* `g07-0176`
  ↳ *evidence-for* `g10-0066`

- `g07-0176` *STATED* — Claude Code mods aren't sandboxed, so only install mods from people you trust.
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`
  ↳ *example-of* `g07-0298`
  ↳ *evidence-for* `g10-0067`

- `g08-0190` *STATED* — Ask Claude Code to fix one thing and it quietly changes twenty others; days later your app breaks and you can't tell which edit did it.
  — [g-stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes](https://chen.media/guides/stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes)
  ↳ *leads-to* `g08-0191`
  ↳ *qualifies* `g08-0008` — unrequested edits compound not understanding your own app

- `g08-0235` *STATED* — A file can hide a sentence in text you can't see; when you hand that file to Claude, Claude can follow the hidden order and try to steal things like your passwords.
  — [g-stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes](https://chen.media/guides/stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes)
  ↳ *leads-to* `g08-0237`

- `g10-0024` *CORE* — Leaving the Claude desktop app running for hours can eat more memory than your Mac has, push everything onto the SSD and freeze the whole computer until you hold the power button.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)

- `g10-0043` *STATED* — Swap means your Mac writes memory to its SSD over and over for as long as it's out of room; one reporter flagged hours of that a day as a real wear concern for the drive.
  — [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *depends-on* `g10-0035`

- `g10-0066` *STATED* — A Claude Code mod runs with the same access to your computer as Claude Code itself.
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *because* `g10-0056`
  ↳ *because* `g10-0266`
  ↳ *contrast* `g01-0134`

- `g10-0067` *STATED* — Only install Claude Code mods from people you trust, and read what a mod does before you turn it on.
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands)
  ↳ *because* `g10-0066`
  ↳ *evidence-for* `g10-0266`

- `g10-0091` *STATED* — A person might never notice your leaked key, but an AI agent searching thousands of files a minute is far more likely to, and it never gets tired of looking.
  > “An AI agent searching thousands of files a minute is far more likely to, and it never gets tired of looking.”
  — [g-openai-agents-hacked-hugging-face-5-login-rules](https://chen.media/guides/openai-agents-hacked-hugging-face-5-login-rules)
  ↳ *because* `g10-0071`

- `g14-0228` *STATED* — Choose one ECC installation method per coding agent so you do not duplicate hooks or configuration.
  > “Choose one ECC installation method per coding agent so you do not duplicate hooks or configuration.”
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *qualifies* `g14-0232`
  ↳ *qualifies* `g14-0226`

- `g15-0050` *CORE* — Claude Code says 'done' before it has proved anything.
  — [g-claude-code-says-done-before-it-has-proved-anything-this-fixes-it](https://chen.media/guides/claude-code-says-done-before-it-has-proved-anything-this-fixes-it)
  ↳ *leads-to* `g15-0055` — the problem motivates the ledger + check + hook

- `g16-0037` *STATED* — Most people who try /design get told the command does not exist, because they are below v2.1.233 or on the free plan.
  > “it is the reason most people who try the command get told it does not exist”
  — [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas)
  ↳ *because* `g16-0032`
  ↳ *because* `g16-0033`

- `g16-0066` *STATED* — One setting decides whether your tasks can see any of Claude's memory.
  > “the one setting that decides whether your tasks can see any of it”
  — [g-claude-memory-is-now-files-you-can-open-and-edit](https://chen.media/guides/claude-memory-is-now-files-you-can-open-and-edit)
  ↳ *qualifies* `g16-0064`
  ↳ *part-of* `g16-0067` — inferred: the task-visibility setting is likely the catch

- `g16-0113` *STATED* — Token mistake 6: a CLAUDE.md written for a weaker model.
  > “6. A CLAUDE.md written for a weaker model”
  — [g-15-claude-mistakes-that-are-quietly-costing-you-tokens](https://chen.media/guides/15-claude-mistakes-that-are-quietly-costing-you-tokens)
  ↳ *part-of* `g16-0099`
  ↳ *example-of* `g16-0103`
  ↳ *part-of* `g16-0011`

- `g16-0138` *STATED* — There is one warning worth reading before you commit an afternoon to building with ox-alpha.
  > “One warning worth reading before you commit an afternoon”
  — [g-the-anonymous-model-that-makes-claude-code-free-until-august-27](https://chen.media/guides/the-anonymous-model-that-makes-claude-code-free-until-august-27)
  ↳ *qualifies* `g16-0125`

- `g16-0268` *STATED* — People commonly get the CLAUDE.md audit wrong.
  > “Where people get this wrong”
  — [g-why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it](https://chen.media/guides/why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it)
  ↳ *qualifies* `g16-0265` — likely: deleting everything instead of keeping binding rules

- `g18-0014` *STATED* — Before you point ECC at anything real, check what it can reach; Alex calls this the one rule that is not optional.
  > “One Rule, and It Is Not Optional / Check what it can reach before you point it at anything real”
  — [g-67-agents-281-skills-and-94-commands-in-one-install](https://chen.media/guides/67-agents-281-skills-and-94-commands-in-one-install)
  ↳ *qualifies* `g18-0001`
  ↳ *evidence-for* `y01-0058`

- `g18-0065` *STATED* — Pasting the Karpathy CLAUDE.md into a chat is the mistake almost everyone makes; it only works placed where Claude actually reads it.
  > “Pasting it into a chat is the mistake almost everyone makes.”
  — [g-the-20-kb-file-that-stops-claude-doing-four-dumb-things](https://chen.media/guides/the-20-kb-file-that-stops-claude-doing-four-dumb-things)
  ↳ *qualifies* `g18-0064`

- `g18-0161` *STATED* — Send each plugin install line as its own message; several plugins will not install if you paste both lines at once.
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *qualifies* `g18-0160`
  ↳ *contrast* `g18-0163`

- `g18-0167` *STATED* — Alex flags a mistake almost everyone makes with claude-mem, plus a 'Worth knowing' note (both gated).
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *qualifies* `g18-0166`

- `g18-0260` *INFERRED* — Keep where credentials live and how they are loaded in CLAUDE.md, not literal secret values: CLAUDE.md enters every session's context and is often committed to the repo.
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *qualifies* `g18-0259`

- `g19-0249` *CORE* — Claude cannot read Reddit, not slowly and not partially.
  > “Claude cannot read Reddit. Not slowly, not partially.”
  — [g-find-the-complaint-build-the-one-feature-undercut-the-price](https://chen.media/guides/find-the-complaint-build-the-one-feature-undercut-the-price)
  ↳ *contradicts* `g19-0248` — the video's 'point Claude at r/smallbusiness' does not work
  ↳ *contradicts* `r04-0187` — 'Claude cannot read Reddit' (robots.txt blocks every crawler) vs the night-crew scout routine reading reddit.com via Custom network access

- `g20-0034` *STATED* — The Day 1 setup has five prerequisites nobody tells you, and each causes a silent failure that looks like 'the guide is broken'.
  > “Five things nobody tells you, and each one causes a silent failure that looks like "the guide is broken."”
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *part-of* `g20-0023`

- `g21-0163` *CORE* — On long jobs Fable 5 will sometimes report work as done that it never actually ran.
  > “on long jobs it will sometimes report work as done that it never actually ran”
  — [g-the-fable-5-guide-effort-memory-and-self-verification](https://chen.media/guides/the-fable-5-guide-effort-memory-and-self-verification)
  ↳ *part-of* `g21-0161`
  ↳ *evidence-for* `g15-0050`

- `r01-0215` *STATED* — /court suggests accept-edits mode (Shift+Tab) for the trial but must not change the user's settings itself.
  > “Do not change the user's settings yourself.”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *qualifies* `r01-0185`

- `r02-0136` *STATED* — /launch never changes your code: the controllers only read, and run your own tests and build.
  > “It never changes your code.”
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0312`
  ↳ *evidence-for* `g08-0253`

- `r03-0070` *STATED* — While running /learn, Claude may change only LESSONS.md and files inside .learn/: never code, settings or any other file (setup is the one exception, and it goes through the script).
  > “You only ever change LESSONS.md and files inside .learn/.”
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *example-of* `r03-0260`
  ↳ *example-of* `r02-0313`

- `r04-0059` *STATED* — The mentor skill tells Claude never to get around the Write/Edit lock: no shell redirects, no `cat >`, no other tools that write files.
  > “Never try to get around it (no shell redirects, no `cat >`, no other tools that write files).”
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *qualifies* `r04-0058`

- `r04-0188` *STATED* — Remove all connectors from a routine unless one is needed: a routine can use every tool in an included connector, including writes, without asking.
  > “A routine can use every tool in an included connector, including writes, without asking.”
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0184`
  ↳ *because* `r04-0196`
  ↳ *example-of* `y01-0058`

- `y01-0056` *STATED* — If an agent asks to use an app, read the request to understand what you're allowing before approving.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *part-of* `y01-0055`

- `y01-0159` *STATED* — If you don't set up your Claude workspace correctly, you'll spend hours every day repeating your instructions.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *contrast* `y01-0158`

- `y02-0056` *CORE* — You ask Claude to fix one thing and it quietly changes 20 other things you never told it to.
  > “you ask Claude to fix one thing and it quietly changes 20 other things you never told it to”
  — [70lNFy2fUIQ](https://youtu.be/70lNFy2fUIQ) [VpqXED1YiUM](https://youtu.be/VpqXED1YiUM)
  ↳ *evidence-for* `g08-0190`
  ↳ *leads-to* `y02-0057`
  ↳ *because* `y02-0055` — the problem the bouncer solves
  ↳ *qualifies* `y02-0132` — unsupervised Claude overreaches and self-approves

- `y02-0057` *STATED* — A couple of days after Claude's unrequested changes, your app breaks and you have no clue why.
  > “a couple days later when your app breaks, you have no clue why”
  — [70lNFy2fUIQ](https://youtu.be/70lNFy2fUIQ) [VpqXED1YiUM](https://youtu.be/VpqXED1YiUM)
  ↳ *evidence-for* `g08-0195`

- `y03-0042` *STATED* — Claude's own docs warn that max effort overthinks a lot.
  — [ItG-vSZFWgA](https://youtu.be/ItG-vSZFWgA) [mVKBGZNsSa4](https://youtu.be/mVKBGZNsSa4) [HTu9VPLvcP0](https://youtu.be/HTu9VPLvcP0)
  ↳ *evidence-for* `g10-0195`
  ↳ *qualifies* `y03-0041`
  ↳ *example-of* `y03-0203`

- `y03-0051` *STATED* — One early-quit question from Claude can cost you a whole night of work.
  — [ThrAfrg8rjQ](https://youtu.be/ThrAfrg8rjQ) [DHCciHdW-Nw](https://youtu.be/DHCciHdW-Nw)
  ↳ *evidence-for* `g03-0051`

- `y03-0092` *STATED* — Leaving the Claude app open can freeze your whole computer.
  — [5Ik2XpcR5uE](https://youtu.be/5Ik2XpcR5uE)
  ↳ *evidence-for* `g10-0024`

<!-- AUTO:atoms END -->
