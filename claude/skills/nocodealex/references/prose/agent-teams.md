# Multi-Claude panels, judges, routines and agent teams

## What he believes (CORE first)

- **One Claude is a yes-man.** It says your idea is good; the panel skills exist to break that `g09-0245` `g09-0109`.
- **The maker never grades its own work.** A separate reviewer, blind grader or judge does `g20-0284` `g20-0173` `g19-0210`.
- **Independence first.** No shared notes `g04-0245` `r01-0016`; five copies sharing memory are "one answer wearing five hats" `g20-0095`.
- **Locked roles in their own space.** One job per agent, in its own Project/subagent, handing off through shared files `g20-0285` `g20-0188` `g21-0051`.
- **Human gate.** Drafts, PRs, memos; nothing sends, posts, spends or merges without your yes `g09-0247` `g02-0237` `r01-0050`. "Rules in a prompt are instructions; the guardrails are what actually stop a mistake" `r04-0164`.
- **Build once, reuse forever** `g19-0293`.

## Frameworks, step by step

**The panel pattern** `g07-0295` `g08-0251` `g09-0246`: N Claudes start together and judge blind, quote evidence, and a separate synthesiser (mentor, judge, coach, flight director) merges worst-first; then Claude fixes the work `g04-0249`. Output: one page, verdict + one-line reasons + pasteable fix list `g09-0248`.

**Panel roster** (all at github.com/alexyc9381):
- /hiring-panel: screen + hiring manager + 5 readers, each under 120 words `g08-0028` `r01-0130`.
- /linkedin-roast: 5 personas, consensus = raised by at least 3 of 5 `g07-0246` `r03-0217`.
- /shark: `--investors N` (2-10, default 5), `--seed S` `r04-0222` `r04-0223`.
- /court: prosecutor, defense, `--jury N` (3-12, default 12), judge, output VERDICT.md `r01-0029` `r01-0178` `r01-0170`.
- /launch: 8 stations (Tests, Security, Database, Speed, Cost, Users, Recovery, Rules) under a single-veto gate `g09-0114` `r01-0033`.
- /hunter: 5 Claudes, 2 blind scorers, threshold 80/100 `g02-0020` `r02-0056`.

**Orchestration mechanics** (/court, /launch, /shark share them): a Python script (`court.py`, `launch.py`) does the bookkeeping and counts the votes `r01-0187` `r02-0155`. The host Claude never argues, votes or edits `r01-0188` `r02-0156`. Drive it with `COURT next`, `COURT prompts <phase>` and `COURT render` `r01-0222` `r01-0224` `r01-0232`. Launch **one wave per message, one Agent call per job** (the tool is called Task in older versions), and wait for the whole wave before the next `r01-0225` `r01-0228` `r04-0257`. Each call is `subagent_type: general-purpose`, `prompt: Read <brief path> and follow it exactly. It is your whole brief.` `r02-0191`. Missing outputs are re-run once. A second failure gives NO VOTE or NO CALL, and NO CALL holds the launch `r01-0230` `r02-0194`. Sub-agents can't see the conversation, so the case or mission file must stand on its own `r02-0177` `r04-0249`.

**Attack-and-rebuild loops:**
- Boss loop: the task, a team of worker sub-agents, and one strict boss who rejects until the work is good. The third part is the one people skip `g15-0165` `g15-0166`.
- Gauntlet: two agents, with a separate critic `g16-0165`.
- Agent Graph: five agents plus an attacker `g19-0202` `g19-0197`.
- 100-Claude tournament: 2,160 strategy cards, 100→50→25→13→7→4→2→1, a fatal flaw can't win, 16-Claude quick mode `g11-0067` `g11-0075` `g11-0073` `g11-0058`.
- Best-of-five: fresh contexts and a blind sixth grader `g20-0092` `g20-0097`.

**Role pipelines:**
- Dev team: Planner writes spec.md, Coder, Tester writes test-report.md, then a read-only Reviewer gate. Setup takes about 15 minutes `g20-0206` `g20-0202`.
- Four-agent council: Believer, Skeptic, Investor, Judge, with one shared folder. Setup takes about 10 minutes `g20-0194` `g20-0190`.
- Split models: Pair (Claude plans, Codex audits with `VERDICT: PASS/BLOCK`, up to 3 times, then they swap) `g06-0161` `g06-0162` and Claudex Loop `g13-0268`.

## Routines and night crew

/night-crew sets up 3 Claude Code routines (builder, scout, tracker) from one NIGHT-CREW.md at the repo root `r04-0089` `r04-0093` `r04-0162`. Defaults 1:07/2:07/5:07am; tracker last to check the builder's PR `r04-0183`. Each one is created with `/schedule every night at {{time}}: in {{owner/repo}}, read NIGHT-CREW.md and do the Builder's job. Follow its house rules exactly.` `r04-0182`. There are 8 house rules: draft PRs on `claude/night-crew-` branches only, NEEDS YOUR OK for anything forbidden, and one item a night `r04-0130` `r04-0136` `r04-0137`.

Routines run with no permission prompts `r04-0163`, so three guardrails do the real stopping:
1. A protected default branch with no admin bypass `r04-0193`.
2. Test keys only in the cloud environment `r04-0195`.
3. No pay or publish connectors `r04-0196` `r04-0189`.

Nightly /learn runs as `claude -p "/learn review" --permission-mode dontAsk --allowedTools "Bash(python3 .claude/hooks/learn.py *),Edit(./LESSONS.md),Edit(./.learn/**)"` `r03-0038`. In Desktop you can use Routines → Local → Daily instead. Run it once with "always allow" `r03-0035` `r03-0036`. A local routine only runs while the app is open and the computer is awake `r03-0037`.

## Costs and numbers

- An agent team uses about 7x the tokens of a normal session `y03-0016`.
- The "Large workflow" warning appears above 25 agents or 1.5M tokens. It doesn't block the run `g06-0089` `g06-0090`.
- Subagents inherit the session model and share the 200-search cap `g03-0015` `g03-0242`. Start The Agency with 5 agents, not all `g17-0265`.

## Contradictions and caveats

- **The Agency's size** is given as more than 230, 273 or 286 agents `g08-0089` `g15-0116` `g17-0258`. Its stars as 149k or 137.4k `g15-0115` `g18-0271`.
- **claude-seo** is described as up to 17 agents at once (19 total) and as up to 15 (18 total) `g02-0154` `g17-0107`.
- **Night-crew output:** the video promises "8 hours of work" `y02-0158`, but the repo says one item a night `r04-0205`.
- **Best-of-N size:** "ten is noise" `g20-0102` against a 100-Claude tournament and a 20-version bracket `g11-0057` `g21-0033`.
- **Pair** is capped at 3 audits `g06-0162`, but the split video gives no cap `y04-0108`.
- **Panels are one model playing many roles,** not real people `r03-0162`. **Routines are a research preview** `r04-0101`.
- **INFERRED:** the routine steps `g22-0080` and the /court script rationale `r01-0189`.
- **Locked or toc-only:** boss-loop checks, Agency picks and the routine template are gated `g15-0174` `g15-0121` `g22-0076`.

## What to load next

- topics/usage-limits.md for agent token burn.
- topics/claude-code-mastery.md for subagent files, `/schedule` and hooks.
- topics/skills-mcp-ecosystem.md for roster installs.
- topics/prompting-quality.md for the keep-going and verification loops `y03-0062`.
