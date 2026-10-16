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

---

## Atom index

<!-- AUTO:atoms BEGIN -- regenerated by build_topics.py, do not edit below -->

*1063 atoms.*

### analogy

- `g08-0095` *STATED* — Asking one Claude to build your app, write your ads, design the screens and plan your Reddit launch gets you one generalist doing four jobs; an agency works the other way, with a specialist for each job, each with their own way of working.
  — [g-run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents](https://chen.media/guides/run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents)
  ↳ *analogy-for* `g08-0089`
  ↳ *evidence-for* `g18-0286`

- `g08-0213` *STATED* — An Agent Office turns each session into a worker at a desk: you look at the room and see who is typing, who has a hand up for you, and who is done.
  — [g-see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office](https://chen.media/guides/see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office)
  ↳ *analogy-for* `g08-0204`
  ↳ *analogy-for* `y04-0105`

- `g09-0111` *STATED* — Before a NASA rocket leaves the pad, the flight director polls every flight controller, each answers GO or NO-GO for their own system, and one NO-GO holds the countdown.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *analogy-for* `g09-0110`
  ↳ *evidence-for* `r02-0121`

- `g20-0291` *STATED* — Alex uses 'hands' as the metaphor for giving Claude the ability to act: MCP 'gives it hands' and Part 2 of the JARVIS build is 'the hands'.
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model) [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *analogy-for* `g20-0232`
  ↳ *analogy-for* `g20-0030`

- `r02-0121` *CORE* — Before a NASA rocket leaves the pad, the flight director polls every flight controller, each answers GO or NO-GO for their own system, and one NO-GO holds the countdown; /launch runs an app's launch the same way.
  > “One NO-GO and the countdown holds.”
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *analogy-for* `r02-0118`
  ↳ *analogy-for* `r02-0133`

- `y02-0065` *STATED* — Jester analogy: in medieval times everyone around the king just agreed ('Yes, Lord. Your idea is so good'), so he kept one jester who would actually tell him the truth.
  > “everyone around the king would just agree with him and say, "Yes, Lord. Your idea is so good." So he would have one jester who would actually tell him the truth.”
  — [AJ0uGlJEL2U](https://youtu.be/AJ0uGlJEL2U) [BuoCqoRvG2U](https://youtu.be/BuoCqoRvG2U)
  ↳ *analogy-for* `g09-0245`
  ↳ *analogy-for* `y02-0063`

- `y02-0131` *STATED* — Launch your app the way NASA launches a rocket.
  > “you should launch your app the way NASA launches a rocket”
  — [Bn4UhbHJzxo](https://youtu.be/Bn4UhbHJzxo) [7cYKEcBNFV4](https://youtu.be/7cYKEcBNFV4) [DE32ZPcENjY](https://youtu.be/DE32ZPcENjY)
  ↳ *evidence-for* `r02-0121`
  ↳ *analogy-for* `y02-0134`

- `y02-0133` *STATED* — NASA only launches a rocket after every flight controller says GO.
  — [Bn4UhbHJzxo](https://youtu.be/Bn4UhbHJzxo) [7cYKEcBNFV4](https://youtu.be/7cYKEcBNFV4) [DE32ZPcENjY](https://youtu.be/DE32ZPcENjY)
  ↳ *evidence-for* `r02-0121`
  ↳ *analogy-for* `y02-0131`

### bio

- `g13-0255` *STATED* — The Delegation was created by Arturo Paracuellos.
  — [g-give-ai-agents-an-office-the-delegation](https://chen.media/guides/give-ai-agents-an-office-the-delegation)
  ↳ *part-of* `g13-0254`

### caveat

- `g03-0208` *STATED* — Roast Room advisors are simulations, not the real people, and none of them endorses the project.
  > “They are simulations, not the real people”
  — [g-roast-room-a-free-claude-council-that-argues-over-your-business-decisions](https://chen.media/guides/roast-room-a-free-claude-council-that-argues-over-your-business-decisions)
  ↳ *example-of* `g03-0006`
  ↳ *qualifies* `g03-0207`

- `g03-0226` *STATED* — Shortening subagent descriptions has a cost (the guide's catch, "what it costs you").
  — [g-shorten-your-claude-helper-agent-descriptions](https://chen.media/guides/shorten-your-claude-helper-agent-descriptions)
  ↳ *example-of* `g03-0006`
  ↳ *qualifies* `g03-0225`

- `g03-0227` *INFERRED* — Because Claude picks which helper to call from its description, over-trimmed descriptions risk Claude calling the wrong helper or none.
  — [g-shorten-your-claude-helper-agent-descriptions](https://chen.media/guides/shorten-your-claude-helper-agent-descriptions)
  ↳ *because* `g03-0220`
  ↳ *qualifies* `g03-0226`

- `g03-0254` *STATED* — There are three cases where the early-compaction line does nothing (covered in the guide's catch).
  — [g-make-your-claude-helpers-summarize-themselves-sooner](https://chen.media/guides/make-your-claude-helpers-summarize-themselves-sooner)
  ↳ *example-of* `g03-0006`
  ↳ *qualifies* `g03-0250`

- `g06-0090` *STATED* — The 'Large workflow' warning is a warning only; it doesn't stop the run.
  — [g-run-claude-agent-swarms-without-burning-your-limit](https://chen.media/guides/run-claude-agent-swarms-without-burning-your-limit)
  ↳ *qualifies* `g06-0089`

- `g06-0094` *STATED* — The swarm guide flags what a smaller model is worse at, so routing workflow stages to a smaller model has a quality cost.
  — [g-run-claude-agent-swarms-without-burning-your-limit](https://chen.media/guides/run-claude-agent-swarms-without-burning-your-limit)
  ↳ *qualifies* `g06-0091`
  ↳ *qualifies* `g06-0232` — the 96% saving was on an easy job
  ↳ *qualifies* `g22-0048`

- `g07-0072` *STATED* — Alex's agency guide spells out what stays in your hands ('Good to know'; email-gated).
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0073`
  ↳ *qualifies* `g07-0069`

- `g12-0278` *STATED* — Polsia only runs ads once you switch them on, so paid spend stays behind a human switch.
  > “runs ads once you switch them on”
  — [g-set-up-polsia-the-ai-co-founder-that-runs-your-business](https://chen.media/guides/set-up-polsia-the-ai-co-founder-that-runs-your-business)
  ↳ *qualifies* `g12-0268`
  ↳ *example-of* `g09-0247`

- `g13-0267` *STATED* — Delegation guide section: 'What to know before adapting it'.
  — [g-give-ai-agents-an-office-the-delegation](https://chen.media/guides/give-ai-agents-an-office-the-delegation)
  ↳ *qualifies* `g13-0254`

- `g14-0005` *STATED* — Calling the steps of a prompt workflow 'stages' does not create autonomous agents.
  > “Calling them stages does not create autonomous agents.”
  — [g-marketing-agent-workflow-setup](https://chen.media/guides/marketing-agent-workflow-setup)
  ↳ *qualifies* `g14-0004`
  ↳ *qualifies* `g19-0201` — 'calling the steps of a prompt workflow stages does not create autonomous agents' vs Agent Graph 'is plain prompting'

- `g14-0244` *STATED* — More AI opinions alone do not establish a tenfold improvement (the video's 10x framing).
  > “More opinions alone do not establish a tenfold improvement.”
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *qualifies* `g14-0243`
  ↳ *example-of* `g14-0348`
  ↳ *qualifies* `g11-0057`

- `g14-0249` *STATED* — An independent provider must be configured in Claude Octopus before you can expect a cross-provider comparison.
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *contrast* `g14-0248`

- `g14-0257` *STATED* — Asking an ordinary Claude question after installing Claude Octopus does not demonstrate that multiple providers contributed.
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)

- `g15-0084` *STATED* — Munder Difflin's source is MIT licensed, but its pixel-art tileset is licensed separately from LimeZu and needs credit: the app is free to use, the art is not yours to lift.
  — [g-munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents](https://chen.media/guides/munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents)
  ↳ *qualifies* `g15-0083`

- `g15-0095` *STATED* — The Judge Loop needs a stopping rule that keeps it from looping forever.
  — [g-the-judge-loop-three-lines-that-put-claude-s-output-on-trial](https://chen.media/guides/the-judge-loop-three-lines-that-put-claude-s-output-on-trial)
  ↳ *qualifies* `g15-0092`
  ↳ *contrast* `g15-0167` — explicit stopping rule vs stop when the boss scores it good
  ↳ *qualifies* `g16-0159`

- `g16-0167` *STATED* — There are cases when the Gauntlet Loop does not work.
  > “When it does not work”
  — [g-the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work](https://chen.media/guides/the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work)
  ↳ *qualifies* `g16-0156`

- `g17-0083` *STATED* — Alex Chen's finance-agents guide flags a line Anthropic's finance agents do not cross.
  > “the line they do not cross”
  — [g-anthropic-s-ten-finance-agents-for-equity-research-and-modelling](https://chen.media/guides/anthropic-s-ten-finance-agents-for-equity-research-and-modelling)
  ↳ *qualifies* `g17-0073`
  ↳ *example-of* `g17-0307`

- `g17-0267` *STATED* — Alex Chen gives two honest caveats about The Agency.
  > “Two honest caveats”
  — [g-286-specialist-ai-agents-free-inside-claude-code](https://chen.media/guides/286-specialist-ai-agents-free-inside-claude-code)
  ↳ *qualifies* `g17-0258`
  ↳ *example-of* `g17-0306`

- `g18-0076` *STATED* — Alex flags three things worth knowing before you install contains-studio/agents.
  — [g-an-entire-ai-company-in-one-repo-eight-departments](https://chen.media/guides/an-entire-ai-company-in-one-repo-eight-departments)
  ↳ *qualifies* `g18-0073`

- `g22-0079` *STATED* — Routine setup section 'Make it bulletproof': hardening steps so the unattended Routine does not fail silently.
  — [g-put-a-recurring-job-on-autopilot-with-claude-code](https://chen.media/guides/put-a-recurring-job-on-autopilot-with-claude-code)
  ↳ *part-of* `g22-0065`

- `r01-0192` *STATED* — The /court jury is made of language models, so treat the verdict as a structured second opinion, not legal, financial or professional advice.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0018`

- `r03-0037` *STATED* — A local Claude Desktop routine runs only while the app is open and the computer is awake.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *qualifies* `r03-0035`
  ↳ *contrast* `g22-0066` — local Desktop routine runs only while the app is open and the computer awake vs cloud Routines run with the laptop closed

- `r03-0162` *CORE* — The five /linkedin-roast readers are one model playing five roles: a structured second opinion, not five real people, and not career advice.
  > “They are a structured second opinion, not five real people, and not career advice.”
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0170`
  ↳ *qualifies* `r03-0194`

- `r04-0101` *STATED* — Routines are a research preview from Anthropic, so names and limits may change.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *qualifies* `r04-0089`
  ↳ *evidence-for* `g22-0072`

- `r04-0192` *STATED* — Claude can't switch on the three night crew guardrails for the user; the skill walks them through it.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *qualifies* `r04-0097`

- `r04-0299` *STATED* — Every /shark board footer says the full session is in the run folder and that the investors are language models and the offers are practice, not real money.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0298`
  ↳ *example-of* `r04-0232`

- `y01-0072` *STATED* — Saving a skill doesn't mean it runs every Friday by itself - recurring runs need a scheduled task.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *evidence-for* `g22-0067`
  ↳ *leads-to* `y01-0073`
  ↳ *contrast* `y01-0178` — Claude demo triggers the report skill manually; Codex scheduled task runs it on time

- `y01-0076` *STATED* — For Codex scheduled tasks that use files on your computer, the computer must be on and the desktop app running when the task is due.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *evidence-for* `r03-0037`
  ↳ *qualifies* `y01-0073`

- `y02-0046` *INFERRED* — The heist video names only three attacker roles plus the mastermind; the fifth crew member's job is not described.
  — [VsD9g0sDNpY](https://youtu.be/VsD9g0sDNpY) [QC6Qzg-qHds](https://youtu.be/QC6Qzg-qHds) [iB8f2suhV04](https://youtu.be/iB8f2suhV04)
  ↳ *qualifies* `y02-0039`

- `y04-0006` *STATED* — Without a monitor, a Claude Code session blocked waiting on your answer can sit idle for hours before you realise Claude was waiting on you the whole time.
  > “instead of hours passing and only finally realizing that Claude was waiting on you the whole time”
  — [Hfgfyi4-xOI](https://youtu.be/Hfgfyi4-xOI)
  ↳ *leads-to* `y04-0001` — the problem Bot Crossing exists to solve

### claim

- `g01-0162` *STATED* — ReelMimic lets you see what each agent is thinking, what it ran and which frames it looked at.
  — [g-reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style)
  ↳ *part-of* `g01-0152`
  ↳ *analogy-for* `y04-0102`

- `g02-0009` *STATED* — /hunter hands every step of the job-hunting chore except the last one (submitting) to five Claudes.
  > “This skill hands every step except the last one to five Claudes.”
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *because* `g02-0008`

- `g03-0197` *STATED* — Roast Room hands you a verdict, the cheapest test to run first, and a PDF.
  — [g-roast-room-a-free-claude-council-that-argues-over-your-business-decisions](https://chen.media/guides/roast-room-a-free-claude-council-that-argues-over-your-business-decisions)
  ↳ *part-of* `g03-0196`

- `g03-0220` *STATED* — Every custom helper agent (subagent) has a description, and Claude reads those descriptions to decide which helper to call.
  — [g-shorten-your-claude-helper-agent-descriptions](https://chen.media/guides/shorten-your-claude-helper-agent-descriptions)
  ↳ *because* `g03-0221`
  ↳ *evidence-for* `g15-0120`

- `g03-0242` *STATED* — Web searches made by Claude's helper agents (subagents) count toward the same 200-search session cap.
  — [g-stop-claude-running-out-of-web-searches](https://chen.media/guides/stop-claude-running-out-of-web-searches)
  ↳ *example-of* `g03-0015`
  ↳ *because* `g03-0243`

- `g03-0249` *STATED* — A helper agent (subagent) keeps its whole pile of work in its own chat until its window is nearly full.
  — [g-make-your-claude-helpers-summarize-themselves-sooner](https://chen.media/guides/make-your-claude-helpers-summarize-themselves-sooner)
  ↳ *example-of* `g03-0015`
  ↳ *because* `g03-0250`

- `g03-0250` *STATED* — Since Claude Code v2.1.296 you can tell one helper agent to summarize (compact) itself earlier with a single line in its settings.
  — [g-make-your-claude-helpers-summarize-themselves-sooner](https://chen.media/guides/make-your-claude-helpers-summarize-themselves-sooner)
  ↳ *part-of* `g03-0009`

- `g04-0035` *STATED* — Harvey runs on your own machine, in a loop, using the Claude plan you already pay for.
  > “It runs on your own machine, in a loop, using the Claude plan you already pay for.”
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *part-of* `g04-0029`

- `g04-0111` *STATED* — None of the five /hiring-panel readers sees the others' notes.
  > “None of them sees the others' notes.”
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *qualifies* `g04-0109`
  ↳ *example-of* `g04-0245`
  ↳ *evidence-for* `r01-0016`

- `g04-0155` *STATED* — None of the five /linkedin-roast Claudes sees the others' answers, so nobody goes easy on you.
  > “None of them sees the others' answers, so nobody goes easy on you.”
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *qualifies* `g04-0153`
  ↳ *example-of* `g04-0245`
  ↳ *evidence-for* `r03-0155`
  ↳ *evidence-for* `r01-0016`

- `g05-0034` *STATED* — Each Chrome Relay agent only sees and controls the tabs it opened.
  — [g-let-claude-use-your-real-chrome-signed-in-in-background-tabs](https://chen.media/guides/let-claude-use-your-real-chrome-signed-in-in-background-tabs)
  ↳ *part-of* `g05-0031`
  ↳ *contrast* `g05-0313` — agent isolation by tab vs cross-agent review
  ↳ *example-of* `g19-0073`

- `g05-0254` *STATED* — In OpenQodex, the Claude that wrote the code does not review it.
  > “The Claude that wrote the code does not review it.”
  — [g-install-openqodex-a-second-claude-reviews-your-code-before-you-push](https://chen.media/guides/install-openqodex-a-second-claude-reviews-your-code-before-you-push)
  ↳ *because* `g05-0252`
  ↳ *example-of* `g05-0313`
  ↳ *evidence-for* `g20-0284`

- `g06-0084` *CORE* — Claude Code dynamic workflows run many Claude agents at once, and every one of them draws on your plan's limit.
  — [g-run-claude-agent-swarms-without-burning-your-limit](https://chen.media/guides/run-claude-agent-swarms-without-burning-your-limit)
  ↳ *qualifies* `g07-0185`

- `g07-0056` *STATED* — In Alex's agency skill, each job has its own agent inside Claude Code and the agents hand work to each other.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0073`
  ↳ *part-of* `g07-0052`
  ↳ *evidence-for* `r01-0040`

- `g07-0067` *STATED* — The night shift leaves you a log in the morning.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0052` — night shift

- `g07-0068` *STATED* — Everything in Alex's agency skill lives in a .agency folder where you run it.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0073`
  ↳ *example-of* `g07-0294`

- `g07-0069` *STATED* — In Alex's agency skill, nothing is sent without your yes.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0073`
  ↳ *example-of* `g07-0297`
  ↳ *example-of* `g09-0247`

- `g07-0138` *STATED* — /brain-grade's five judges cover IQ, logic, emotional intelligence, creativity and street smarts; each grades you alone out of 100 and compares you to the average person.
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *part-of* `g07-0137`
  ↳ *defines* `g07-0149`

- `g07-0139` *STATED* — After the /brain-grade judges, a coach tells you exactly what to fix.
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *part-of* `g07-0137`

- `g07-0143` *STATED* — /brain-grade reads only what YOU wrote, never Claude's replies.
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *part-of* `g07-0137`
  ↳ *part-of* `g07-0142`

- `g07-0145` *STATED* — /brain-grade masks passwords, tokens, emails and phone numbers in the messages it reads.
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *part-of* `g07-0137`
  ↳ *part-of* `g07-0142`
  ↳ *contrast* `g07-0175` — skill redacts secrets vs mods that can read your keys

- `g07-0146` *STATED* — /brain-grade saves its data only in a .brain-grade folder where you run it.
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *part-of* `g07-0137`
  ↳ *part-of* `g07-0142`
  ↳ *example-of* `g07-0294`

- `g07-0148` *STATED* — /brain-grade can also read a ChatGPT export or a folder of your own writing, if you point it at one.
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *part-of* `g07-0137`
  ↳ *qualifies* `g07-0147`

- `g07-0157` *STATED* — /brain-grade never touches your other files.
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *part-of* `g07-0137`
  ↳ *example-of* `g07-0294`

- `g07-0186` *STATED* — Each Claude Code Projects thread is its own Claude working in the cloud on its own branch of your code.
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`
  ↳ *part-of* `g07-0185`

- `g07-0187` *STATED* — A Claude Code Projects thread can open a pull request when it's done.
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`
  ↳ *part-of* `g07-0186`

- `g07-0188` *STATED* — All threads in a Claude Code project share one memory, so the decisions you make stay put.
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`
  ↳ *part-of* `g07-0182`
  ↳ *contrast* `r02-0177` — Projects threads all share one memory vs panel sub-agents that see only their brief

- `g07-0247` *STATED* — The five /linkedin-roast reviewers are a recruiter, a hiring manager, a founder, an expert in your field and a peer at your level.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *defines* `g07-0252`
  ↳ *evidence-for* `r03-0134`

- `g07-0266` *STATED* — /linkedin-roast writes everything to a linkedin-roast-output folder where you run it.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *example-of* `g07-0294`

- `g07-0267` *STATED* — /linkedin-roast never logs in to LinkedIn and never touches your other files.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *example-of* `g07-0294`

- `g07-0297` *CORE* — Alex's agent tools keep a human gate: the agency sends nothing without your yes, Find Skills offers rather than installs, /linkedin-roast asks for numbers it doesn't know, and /brain-grade asks once before reading.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents) [g-let-claude-find-and-install-the-right-skill-for-any-job](https://chen.media/guides/let-claude-find-and-install-the-right-skill-for-any-job) [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill) [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *evidence-for* `g09-0247`

- `g08-0045` *STATED* — /hiring-panel writes everything to a .hiring-panel folder where you run it and never touches your other files.
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill)
  ↳ *qualifies* `g08-0028`
  ↳ *example-of* `g08-0252`
  ↳ *evidence-for* `g07-0294`

- `g08-0088` *STATED* — Most people ask one Claude to do everything: the code, the design, the ads, the Reddit post.
  — [g-run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents](https://chen.media/guides/run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents)
  ↳ *leads-to* `g08-0095`
  ↳ *evidence-for* `g18-0286`

- `g08-0203` *STATED* — Run a few Claude Code chats at once and you end up clicking through windows to find the one that has been waiting for you.
  — [g-see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office](https://chen.media/guides/see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office)
  ↳ *leads-to* `g08-0204`

- `g08-0211` *STATED* — With three or four Claude Code sessions open you don't know which one is working, which one has finished, and which one has been sitting there for an hour waiting for you to say yes.
  — [g-see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office](https://chen.media/guides/see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office)
  ↳ *qualifies* `g08-0203`
  ↳ *evidence-for* `y04-0006`

- `g08-0212` *STATED* — Without a status view you click through every window, or scroll your phone and come back to find Claude was done long ago.
  — [g-see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office](https://chen.media/guides/see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office)
  ↳ *qualifies* `g08-0203`

- `g08-0234` *STATED* — /rival writes everything to a .rival folder where you run it and never touches your other files.
  — [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill)
  ↳ *qualifies* `g08-0220`
  ↳ *example-of* `g08-0252`
  ↳ *evidence-for* `g07-0294`

- `g08-0252` *STATED* — Alex's panel skills write all output to their own dot-folder (.hiring-panel, .rival) in the directory where you run them and never touch other files.
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill) [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill)
  ↳ *qualifies* `g08-0253` — panel skills write only inside their own folder
  ↳ *evidence-for* `g07-0294`

- `g09-0016` *STATED* — Ask one AI whether your idea is good and it tends to say yes.
  > “Ask one AI whether your idea is good and it tends to say yes.”
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives)
  ↳ *evidence-for* `g09-0245`

- `g09-0020` *STATED* — One friendly answer from one AI won't save you from building the wrong thing, because it rarely tells you the case against you.
  > “One friendly answer from one AI won't save you from it, because it rarely tells you the case against you.”
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives)
  ↳ *qualifies* `g09-0016`

- `g09-0021` *STATED* — Ten Claude executives look at your idea from ten jobs, and they can't all just agree with you.
  > “Ten Claude executives look at your idea from ten jobs, and they can't all just agree with you.”
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives)
  ↳ *contrast* `g09-0020`

- `g09-0028` *STATED* — The Boardroom's memo is only advice: you approve it, change it, or throw it out.
  > “You approve it, change it, or throw it out.”
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives)
  ↳ *qualifies* `g09-0027`
  ↳ *example-of* `g09-0247`

- `g09-0109` *STATED* — The Claude that built your app grades its own work, so it tells you it's ready even when there's a ton of issues.
  > “The Claude that built your app grades its own work, so it tells you it's ready even when there's a ton of issues.”
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *evidence-for* `g09-0245`
  ↳ *because* `g20-0173`

- `g09-0112` *STATED* — Most apps launch the other way: you build with Claude, then the same Claude checks its own work and tells you it's amazing, and whatever it missed ships with it.
  > “Whatever it missed ships with it.”
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *qualifies* `g09-0109`
  ↳ *evidence-for* `g09-0245`

- `g09-0146` *STATED* — Claude says almost every business idea is great.
  > “Claude says almost every business idea is great.”
  — [g-pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill](https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill)
  ↳ *evidence-for* `g09-0245`
  ↳ *because* `g09-0148`

- `g09-0148` *STATED* — Claude usually says your business idea is good because it's built to be helpful, so it finds the best version of whatever you bring it.
  > “It's built to be helpful, so it finds the best version of whatever you bring it.”
  — [g-pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill](https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill)
  ↳ *evidence-for* `g09-0245`

- `g09-0150` *STATED* — In the shark skill every shark is looking for a reason to say no.
  > “every one of them is looking for a reason to say no”
  — [g-pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill](https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill)
  ↳ *part-of* `g09-0147`
  ↳ *example-of* `g08-0250`

- `g09-0161` *STATED* — Claude agrees with almost everything you say.
  > “Claude agrees with almost everything you say.”
  — [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill)
  ↳ *evidence-for* `g09-0245`

- `g09-0164` *STATED* — In the court skill the jury doesn't know what the others voted.
  > “the jury doesn't know what the others voted”
  — [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill)
  ↳ *part-of* `g09-0162`
  ↳ *example-of* `g09-0246`
  ↳ *evidence-for* `r01-0016`

- `g09-0170` *STATED* — Nobody on the court jury sees anyone else's vote, so nobody can just go along with the room.
  > “Nobody sees anyone else's vote, so nobody can just go along with the room.”
  — [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill)
  ↳ *qualifies* `g09-0168`
  ↳ *because* `g09-0164`
  ↳ *evidence-for* `r01-0016`

- `g09-0214` *STATED* — The night crew only ever leaves pull requests, so nothing reaches your live app until you say so.
  > “They only ever leave pull requests, so nothing reaches your live app until you say so.”
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)
  ↳ *qualifies* `g09-0213`
  ↳ *example-of* `g09-0247`
  ↳ *evidence-for* `r04-0095`

- `g09-0224` *STATED* — Every night-crew output is a proposal: nothing is merged, deployed, posted or paid for until you do it yourself.
  > “Nothing is merged, deployed, posted or paid for until you do it yourself.”
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)
  ↳ *qualifies* `g09-0223`
  ↳ *example-of* `g09-0247`

- `g09-0225` *STATED* — Night-crew setup takes about ten minutes.
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)
  ↳ *qualifies* `g09-0213`

- `g09-0226` *STATED* — The night crew is set up so it can't spend money, delete anything or touch your live app.
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)
  ↳ *qualifies* `g09-0214`
  ↳ *evidence-for* `r04-0094`

- `g09-0245` *CORE* — Claude defaults to agreeing with you (asked whether your idea or app is good, it usually says yes), and Alex's multi-Claude skills (Boardroom, shark, court, launch poll) exist to break that.
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives) [g-pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill](https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill) [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill) [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *leads-to* `g08-0250`

- `g09-0247` *CORE* — Alex's agent setups keep a human gate: outputs are memos, pull requests or drafts, agents are fenced to what they may edit, and nothing ships, posts or spends until you act.
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives) [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes) [g-run-a-jarvis-on-your-own-claude-code](https://chen.media/guides/run-a-jarvis-on-your-own-claude-code) [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)

- `g11-0058` *STATED* — The 100-Claude tournament skill has a 16-Claude quick mode.
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *qualifies* `g11-0057`

- `g11-0061` *STATED* — Alex says the tournament skill is for answers that matter: a business idea, a résumé, an email you have to get right, a headline, a bug that won't go away.
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *qualifies* `g11-0057`

- `g11-0073` *STATED* — In the tournament, an answer with a real fatal flaw can't win.
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *qualifies* `g11-0071`

- `g11-0136` *CORE* — OpenAI on stage at DevDay: "Our engineers have their dot fixing dozens of bugs every day."
  > “Our engineers have their dot fixing dozens of bugs every day.”
  — [g-let-chatgpt-fix-your-apps-bugs-while-you-sleep](https://chen.media/guides/let-chatgpt-fix-your-apps-bugs-while-you-sleep) [g-get-your-own-chatgpt-dot](https://chen.media/guides/get-your-own-chatgpt-dot)
  ↳ *part-of* `g11-0117`

- `g11-0138` *STATED* — Most bug reports sit in a GitHub tab until you have a free evening.
  — [g-let-chatgpt-fix-your-apps-bugs-while-you-sleep](https://chen.media/guides/let-chatgpt-fix-your-apps-bugs-while-you-sleep)
  ↳ *because* `g11-0137`

- `g11-0140` *STATED* — The overnight bug-fix work runs on a machine in the cloud, not your laptop, so it keeps going while your laptop is closed and you're asleep.
  — [g-let-chatgpt-fix-your-apps-bugs-while-you-sleep](https://chen.media/guides/let-chatgpt-fix-your-apps-bugs-while-you-sleep)
  ↳ *enables* `g11-0137`
  ↳ *evidence-for* `g20-0288`

- `g11-0141` *STATED* — Nothing in the overnight bug-fix flow goes live until you approve it.
  > “Nothing goes live until you approve it.”
  — [g-let-chatgpt-fix-your-apps-bugs-while-you-sleep](https://chen.media/guides/let-chatgpt-fix-your-apps-bugs-while-you-sleep)
  ↳ *qualifies* `g11-0137`
  ↳ *part-of* `g11-0150`
  ↳ *example-of* `g09-0247`

- `g11-0146` *STATED* — Alex's GitHub bug-fix setup works on any plan with an OpenAI API key.
  — [g-let-chatgpt-fix-your-apps-bugs-while-you-sleep](https://chen.media/guides/let-chatgpt-fix-your-apps-bugs-while-you-sleep)
  ↳ *contrast* `g11-0145` — API key vs dots' paid plans

- `g11-0151` *STATED* — ChatGPT has always waited for you: you type, it answers, and the moment you close the tab it stops; a dot doesn't stop.
  > “A dot doesn't stop.”
  — [g-get-your-own-chatgpt-dot](https://chen.media/guides/get-your-own-chatgpt-dot)
  ↳ *qualifies* `g11-0135`

- `g11-0154` *STATED* — ChatGPT dots are powered by GPT-6 Astra, OpenAI's top model.
  — [g-get-your-own-chatgpt-dot](https://chen.media/guides/get-your-own-chatgpt-dot)
  ↳ *qualifies* `g11-0135`

- `g11-0155` *STATED* — You can open a dot's cloud computer at any time to watch what it's doing.
  — [g-get-your-own-chatgpt-dot](https://chen.media/guides/get-your-own-chatgpt-dot)
  ↳ *qualifies* `g11-0135`
  ↳ *analogy-for* `y04-0102`

- `g11-0157` *STATED* — Dots remember context from ChatGPT, so they learn what matters to you and how you like things done.
  — [g-get-your-own-chatgpt-dot](https://chen.media/guides/get-your-own-chatgpt-dot)
  ↳ *enables* `g11-0135`

- `g11-0158` *STATED* — You can message a dot in ChatGPT on desktop, web and mobile, and in Slack or Teams.
  — [g-get-your-own-chatgpt-dot](https://chen.media/guides/get-your-own-chatgpt-dot)
  ↳ *qualifies* `g11-0135`

- `g12-0253` *STATED* — In Anthropic's speed sprint, Claude found the bottlenecks and wrote the fixes.
  — [g-how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill](https://chen.media/guides/how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill)
  ↳ *qualifies* `g12-0252`
  ↳ *example-of* `g12-0200` — Claude doing the engineering on Anthropic's own apps

- `g12-0268` *STATED* — Polsia keeps working after you log off: it posts, sends outreach emails, runs ads once you switch them on, and fixes bugs.
  — [g-set-up-polsia-the-ai-co-founder-that-runs-your-business](https://chen.media/guides/set-up-polsia-the-ai-co-founder-that-runs-your-business)
  ↳ *part-of* `g12-0267`
  ↳ *evidence-for* `g20-0288`

- `g12-0269` *STATED* — Polsia sends you a plan in the morning and a summary at night.
  — [g-set-up-polsia-the-ai-co-founder-that-runs-your-business](https://chen.media/guides/set-up-polsia-the-ai-co-founder-that-runs-your-business)
  ↳ *part-of* `g12-0267`

- `g12-0271` *STATED* — In Polsia, separate agents handle building, marketing, outreach, support and research, each on its own schedule.
  — [g-set-up-polsia-the-ai-co-founder-that-runs-your-business](https://chen.media/guides/set-up-polsia-the-ai-co-founder-that-runs-your-business)
  ↳ *part-of* `g12-0267`

- `g12-0272` *STATED* — You steer Polsia in plain English, like messaging a co-founder.
  — [g-set-up-polsia-the-ai-co-founder-that-runs-your-business](https://chen.media/guides/set-up-polsia-the-ai-co-founder-that-runs-your-business)
  ↳ *qualifies* `g12-0267`

- `g12-0303` *CORE* — Alex's tool guides flag human approval before anything touches your accounts or money: the go-live skill changes nothing until you approve its plan, and Polsia gets a 'Before it spends your money' check.
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments) [g-set-up-polsia-the-ai-co-founder-that-runs-your-business](https://chen.media/guides/set-up-polsia-the-ai-co-founder-that-runs-your-business)
  ↳ *generalizes* `g12-0056`
  ↳ *generalizes* `g12-0277`
  ↳ *evidence-for* `g09-0247`

- `g13-0175` *STATED* — Jev's narrow, confidence-scored answers make it a good gatekeeper in a workflow.
  > “That makes it a good gatekeeper.”
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *because* `g13-0174`
  ↳ *evidence-for* `y04-0064`

- `g13-0229` *STATED* — The basic Darwin Loop does not require three simultaneous agents: Claude can propose three alternatives in one conversation.
  — [g-darwin-loop-evolve-the-winner](https://chen.media/guides/darwin-loop-evolve-the-winner)
  ↳ *qualifies* `g13-0222`

- `g13-0256` *STATED* — The Delegation visualizes multi-agent collaboration through characters, workstations and task activity.
  — [g-give-ai-agents-an-office-the-delegation](https://chen.media/guides/give-ai-agents-an-office-the-delegation)
  ↳ *part-of* `g13-0254`
  ↳ *evidence-for* `y04-0105`

- `g13-0257` *STATED* — The Delegation runs on Gemini.
  — [g-give-ai-agents-an-office-the-delegation](https://chen.media/guides/give-ai-agents-an-office-the-delegation)
  ↳ *qualifies* `g13-0254`

- `g13-0272` *STATED* — The full Claudex Loop covers planning, review, implementation and inspection.
  — [g-split-claude-and-codex-with-claudex-loop](https://chen.media/guides/split-claude-and-codex-with-claudex-loop)
  ↳ *part-of* `g13-0268`

- `g13-0308` *INFERRED* — Bot Crossing and The Delegation both visualise agents as characters in a 3D world, but Bot Crossing reads your real local coding sessions while The Delegation runs its own Gemini agents in the browser.
  — [g-watch-every-claude-code-session-as-a-bot-in-bot-crossing](https://chen.media/guides/watch-every-claude-code-session-as-a-bot-in-bot-crossing) [g-give-ai-agents-an-office-the-delegation](https://chen.media/guides/give-ai-agents-an-office-the-delegation)
  ↳ *contrast* `g13-0001`
  ↳ *contrast* `g13-0254`

- `g14-0002` *STATED* — A useful AI marketing workflow produces more than a first draft: it carries evidence into the writing, checks the result against your brand, and leaves you with an asset you can review.
  > “A useful marketing workflow produces more than a first draft.”
  — [g-marketing-agent-workflow-setup](https://chen.media/guides/marketing-agent-workflow-setup)
  ↳ *part-of* `g14-0001`

- `g14-0243` *CORE* — The useful part of AI disagreement is the evidence it produces: a missed requirement, a failing test or a design tradeoff you can act on.
  > “The useful part of AI disagreement is the evidence it produces”
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *part-of* `g14-0241`

- `g14-0246` *STATED* — Claude Octopus requires a working Claude Code installation to start with.
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *part-of* `g14-0241`

- `g14-0248` *STATED* — The Claude Octopus plugin can start with Claude alone as its only provider.
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *qualifies* `g14-0242`

- `g14-0256` *STATED* — Claude Octopus stays dormant until you invoke an /octo:* command.
  > “Octopus stays dormant until you invoke an /octo:* command.”
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *because* `g14-0257`

- `g15-0077` *STATED* — Give MetaGPT one line of requirement and it gives you back a repo plus the documents a team would have produced on the way there.
  — [g-metagpt-one-line-in-a-whole-software-company-out](https://chen.media/guides/metagpt-one-line-in-a-whole-software-company-out)

- `g15-0081` *STATED* — Almost every 'AI agent team' is a folder of markdown role definitions you copy into a prompt; Munder Difflin is a running program with state.
  — [g-munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents](https://chen.media/guides/munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents)
  ↳ *contrast* `g15-0107` — running stateful program vs markdown role definitions
  ↳ *contrast* `g15-0113`
  ↳ *contrast* `g17-0262` — 'almost every AI agent team is a folder of markdown role definitions; Munder Difflin is a running program with state' vs The Agency: 'the file is the product'

- `g15-0103` *STATED* — Every serious Claude Code user hits the same wall: one model, one context window and one set of instructions asked to be a frontend engineer, a database designer and a security reviewer in the same session.
  — [g-the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build](https://chen.media/guides/the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build)
  ↳ *leads-to* `g15-0104`
  ↳ *evidence-for* `g18-0286`

- `g15-0120` *STATED* — Routing (which agent gets which task) is the part that decides whether The Agency is useful.
  — [g-the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install](https://chen.media/guides/the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install)
  ↳ *qualifies* `g15-0114`
  ↳ *evidence-for* `g15-0186`

- `g15-0121` *STATED* — The video names three Agency agents worth installing, and the guide explains why those three (locked).
  — [g-the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install](https://chen.media/guides/the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install)
  ↳ *contrast* `g15-0116` — install a chosen three, not all 273
  ↳ *depends-on* `g15-0120`

- `g15-0168` *STATED* — 'The boss loop' is Alex Chen's own name; nobody in the industry calls it that and it is not in Anthropic's documentation. The published names for this family of technique are loop engineering and agent loops.
  — [g-the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer](https://chen.media/guides/the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer)
  ↳ *qualifies* `g15-0164`

- `g15-0170` *STATED* — The boss-loop mechanism is real and is what the Claude Code team themselves describe doing.
  — [g-the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer](https://chen.media/guides/the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer)
  ↳ *evidence-for* `g15-0164`

- `g15-0186` *INFERRED* — Both agent-marketplace guides (wshobson/agents and The Agency) open with 'the mistake almost everyone makes' on day one, and both frame the value as choosing and routing a few agents rather than the raw count (bodies locked).
  — [g-the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build](https://chen.media/guides/the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build) [g-the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install](https://chen.media/guides/the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install)
  ↳ *qualifies* `g15-0105`
  ↳ *qualifies* `g15-0121`

- `g16-0157` *STATED* — The Gauntlet Loop is a way of writing one prompt so that you stop being the person who checks the output.
  — [g-the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work](https://chen.media/guides/the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work)
  ↳ *defines* `g16-0156`

- `g16-0162` *STATED* — The demo is the reason people are copying the Gauntlet Loop; the mechanism is the reason it works.
  > “The demo is the reason people are copying it. The mechanism is the reason it works.”
  — [g-the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work](https://chen.media/guides/the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work)
  ↳ *qualifies* `g16-0161`

- `g16-0163` *STATED* — Boris Cherny, who built Claude Code, describes his own day as writing loops.
  > “My job is to write loops.”
  — [g-the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work](https://chen.media/guides/the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work)
  ↳ *evidence-for* `g16-0156`
  ↳ *qualifies* `g16-0010` — loops as the job
  ↳ *evidence-for* `g15-0170`

- `g16-0298` *STATED* — Ruflo adds specialist agents to Claude Code.
  — [g-ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm](https://chen.media/guides/ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm)
  ↳ *part-of* `g16-0297`

- `g16-0299` *STATED* — Ruflo adds coordinated swarms of agents.
  — [g-ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm](https://chen.media/guides/ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm)
  ↳ *part-of* `g16-0297`

- `g16-0300` *STATED* — Ruflo adds memory that survives your session.
  — [g-ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm](https://chen.media/guides/ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm)
  ↳ *part-of* `g16-0297`
  ↳ *part-of* `g16-0012`

- `g17-0259` *STATED* — The Agency is MIT licensed, so you can use it commercially and sell what it helps you make.
  > “you can use it commercially and sell what it helps you make”
  — [g-286-specialist-ai-agents-free-inside-claude-code](https://chen.media/guides/286-specialist-ai-agents-free-inside-claude-code)
  ↳ *qualifies* `g17-0258`
  ↳ *example-of* `g17-0310`

- `g17-0262` *STATED* — The Agency has no hidden logic: the file is the product, so you can read it before you trust it.
  > “There is no hidden logic. The file is the product, so you can read it before you trust it.”
  — [g-286-specialist-ai-agents-free-inside-claude-code](https://chen.media/guides/286-specialist-ai-agents-free-inside-claude-code)
  ↳ *because* `g17-0260`
  ↳ *evidence-for* `g17-0232` — agents and skills are both readable text
  ↳ *evidence-for* `g17-0311`

- `g18-0016` *STATED* — Alex's Rowboat guide covers what the tool two YC founders gave away actually is today, and how to run it yourself.
  — [g-the-open-source-agent-tool-two-yc-founders-gave-away](https://chen.media/guides/the-open-source-agent-tool-two-yc-founders-gave-away)
  ↳ *part-of* `g18-0015`

- `g18-0074` *STATED* — Alex's contains-studio guide lists the Engineering department's agents in full.
  — [g-an-entire-ai-company-in-one-repo-eight-departments](https://chen.media/guides/an-entire-ai-company-in-one-repo-eight-departments)
  ↳ *part-of* `g18-0073`

- `g18-0170` *STATED* — For the code-review plugin the threshold is the whole point.
  > “Why the threshold is the whole point”
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *qualifies* `g18-0169`

- `g18-0207` *STATED* — Most automation advice tells you to learn a tool and then build the thing yourself; the 280-workflow repo skips both steps.
  — [g-280-ready-made-n8n-automations-you-do-not-have-to-build](https://chen.media/guides/280-ready-made-n8n-automations-you-do-not-have-to-build)
  ↳ *qualifies* `g18-0206`

- `g18-0209` *STATED* — With the ready-made n8n workflows there is no builder to learn first; the wiring is already done.
  > “There is no builder to learn first. The wiring is already done.”
  — [g-280-ready-made-n8n-automations-you-do-not-have-to-build](https://chen.media/guides/280-ready-made-n8n-automations-you-do-not-have-to-build)
  ↳ *qualifies* `g18-0207`

- `g18-0217` *STATED* — With the 268-role roster you name the job and the right specialists pick themselves up.
  > “You name the job. The right specialists pick themselves up.”
  — [g-268-expert-roles-in-one-repo-free](https://chen.media/guides/268-expert-roles-in-one-repo-free)
  ↳ *part-of* `g18-0215`

- `g18-0240` *STATED* — Boris Cherny fix 3: your tasks are far too small; give Claude Code bigger jobs.
  > “Your tasks are far too small”
  — [g-three-things-almost-everyone-gets-wrong-about-claude-code](https://chen.media/guides/three-things-almost-everyone-gets-wrong-about-claude-code)
  ↳ *part-of* `g18-0226`
  ↳ *contrast* `g18-0285` — install small, but hand Claude bigger tasks

- `g19-0061` *STATED* — One Claude playing researcher, architect, builder and tester at once guesses early and builds on that guess.
  > “One Claude playing researcher, architect, builder and tester at once guesses early and builds on that guess.”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *part-of* `g19-0060`
  ↳ *because* `g19-0062`
  ↳ *evidence-for* `g20-0199`

- `g19-0065` *STATED* — The seven-station line is set up once and reused on every feature after.
  > “Set it up once, reuse it on every feature after.”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *part-of* `g19-0060`

- `g19-0076` *STATED* — What makes the seven subagents a line rather than just seven agents is the gate in the orchestration prompt, covered in 'The Part That Makes It a Line, Not Just Seven Agents'.
  > “The Part That Makes It a Line, Not Just Seven Agents”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *part-of* `g19-0060`
  ↳ *defines* `g19-0074`

- `g19-0099` *STATED* — One /route command runs the whole Claude-plans, Gemini-builds loop.
  > “One command runs the whole loop”
  — [g-run-gemini-inside-claude-code-with-claude-as-the-boss](https://chen.media/guides/run-gemini-inside-claude-code-with-claude-as-the-boss)
  ↳ *part-of* `g19-0091`
  ↳ *leads-to* `g19-0092`
  ↳ *analogy-for* `g06-0158`

- `g19-0193` *STATED* — With an attacker agent on the team, what reaches you has already survived, so you never have to double-check it.
  > “so what reaches you already survived and you never have to double check it”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)
  ↳ *part-of* `g19-0192`
  ↳ *contrast* `g19-0268` — 'never double check' vs 'a Claude quote is a lead, not a citation'

- `g19-0194` *STATED* — Most people use about ten percent of what Claude can do: one model, one answer, take it or leave it.
  > “Most people use about ten percent of what Claude can do: one model, one answer, take it or leave it.”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)
  ↳ *contrast* `g19-0195`

- `g19-0199` *STATED* — What reaches you from an Agent Graph is not Claude's first answer but the answer that already got torn apart by Claude and lived.
  > “It is the answer that already got torn apart by Claude and lived.”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)
  ↳ *because* `g19-0198`
  ↳ *evidence-for* `g19-0193`

- `g19-0200` *STATED* — You build the Agent Graph once and it hardens everything you feed it after that.
  > “You build the graph once and it hardens everything you feed it after that.”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)
  ↳ *because* `g19-0209`

- `g19-0201` *STATED* — The Agent Graph is plain prompting, so it works in Claude Code, the desktop app or the API, on any plan.
  > “It is plain prompting, so it works in Claude Code, the desktop app, or the API, on any plan.”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)
  ↳ *part-of* `g19-0192`
  ↳ *contrast* `g19-0066` — plain prompting graph vs real subagents with separate context windows

- `g19-0293` *CORE* — A recurring Alex principle: build the setup once and reuse it on every later job, e.g. the seven-station line, the attacker Agent Graph, the reskinned voice line, the one-industry carousel workflow and the swap-the-niche lead machine.
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line) [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work) [g-build-the-voice-line-that-answers-a-local-shop-s-missed-calls](https://chen.media/guides/build-the-voice-line-that-answers-a-local-shop-s-missed-calls) [g-one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch](https://chen.media/guides/one-idea-to-a-finished-carousel-in-a-minute-and-the-pitch) [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *generalizes* `g19-0065`
  ↳ *generalizes* `g19-0200`
  ↳ *generalizes* `g19-0227`
  ↳ *generalizes* `g19-0279`
  ↳ *generalizes* `g19-0119`

- `g20-0095` *CORE* — Independence is the whole point of parallel attempts: five copies with shared memory would just agree with each other, giving one answer wearing five hats.
  > “five copies with shared memory would just agree with each other, so you would be back to one answer wearing five hats.”
  — [g-run-the-job-five-times-and-let-a-blind-grader-pick](https://chen.media/guides/run-the-job-five-times-and-let-a-blind-grader-pick)
  ↳ *because* `g20-0094`
  ↳ *leads-to* `g20-0096`
  ↳ *generalizes* `r01-0016`

- `g20-0096` *STATED* — Kept separate, the five attempts genuinely diverge, giving five real attempts to choose from.
  — [g-run-the-job-five-times-and-let-a-blind-grader-pick](https://chen.media/guides/run-the-job-five-times-and-let-a-blind-grader-pick)
  ↳ *leads-to* `g20-0103`

- `g20-0101` *STATED* — Five attempts give enough spread that they meaningfully differ, and are few enough that a single grader can hold them all at once.
  — [g-run-the-job-five-times-and-let-a-blind-grader-pick](https://chen.media/guides/run-the-job-five-times-and-let-a-blind-grader-pick)
  ↳ *because* `g20-0092`

- `g20-0106` *STATED* — Claude can run for hours by itself and do a week of work in one night.
  > “Claude can run for hours by itself and do a week of work in one night.”
  — [g-how-to-let-claude-run-for-hours-without-supervising-it](https://chen.media/guides/how-to-let-claude-run-for-hours-without-supervising-it)
  ↳ *part-of* `g20-0105`

- `g20-0107` *STATED* — Almost nobody lets Claude run alone for hours, because nobody actually trusts it.
  > “Almost nobody lets it, because nobody actually trusts it.”
  — [g-how-to-let-claude-run-for-hours-without-supervising-it](https://chen.media/guides/how-to-let-claude-run-for-hours-without-supervising-it)
  ↳ *qualifies* `g20-0106`

- `g20-0185` *CORE* — The council's magic is not one clever prompt: it is four agents, each locked to a single lens, arguing about the SAME idea, with a judge that has to pick a side.
  > “The magic is not one clever prompt.”
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *part-of* `g20-0178`
  ↳ *generalizes* `g20-0198`

- `g20-0187` *STATED* — Splitting the evaluation into a believer, a skeptic, an investor and a judge is what forces a real answer.
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *evidence-for* `g20-0185`

- `g20-0198` *CORE* — The dev team's magic is not one clever prompt: it is four agents, each locked to a single role, handing work down an assembly line, with a read-only reviewer as the last gate.
  > “handing work down an assembly line, with a read-only reviewer as the last gate.”
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *part-of* `g20-0196`

- `g20-0200` *STATED* — Splitting the jobs across agents is what makes the dev pipeline reliable.
  > “Splitting the jobs is what makes it reliable.”
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *evidence-for* `g20-0198`

- `g20-0208` *STATED* — In the dev pipeline the order is the whole point: each agent only trusts the file the last one left.
  > “The order is the whole point: each one only trusts the file the last one left.”
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *part-of* `g20-0196`

- `g20-0227` *STATED* — Out of the box, Claude works one task at a time, alone.
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *evidence-for* `g20-0224`
  ↳ *evidence-for* `g18-0286`

- `g21-0034` *STATED* — In the tournament method the magic is not asking for one great version; it is the JUDGE.
  > “The magic is not asking for one great version. It is the JUDGE.”
  — [g-run-a-tournament-instead-of-guessing-which-hook-works](https://chen.media/guides/run-a-tournament-instead-of-guessing-which-hook-works)
  ↳ *because* `g21-0033`
  ↳ *evidence-for* `g11-0073`

- `g21-0035` *STATED* — When Fable compares versions head to head, eliminates the losers and has to justify every call, a genuinely stronger winner surfaces than you get from asking 'please give me 10 options'.
  — [g-run-a-tournament-instead-of-guessing-which-hook-works](https://chen.media/guides/run-a-tournament-instead-of-guessing-which-hook-works)
  ↳ *evidence-for* `g21-0034`

- `g21-0040` *STATED* — The whole tournament is three prompts; saved once, they become an 'Arena' you can point at any ad, hook, headline, email, or name for the rest of the year.
  — [g-run-a-tournament-instead-of-guessing-which-hook-works](https://chen.media/guides/run-a-tournament-instead-of-guessing-which-hook-works)
  ↳ *part-of* `g21-0029`
  ↳ *evidence-for* `g19-0293`

- `g21-0051` *CORE* — For AI employees the model is not the magic; the magic is a locked role plus your business context living in the instructions.
  > “The model is not the magic. The magic is a locked role plus your business context living in the instructions.”
  — [g-turn-claude-into-a-six-person-ai-c-suite](https://chen.media/guides/turn-claude-into-a-six-person-ai-c-suite)
  ↳ *part-of* `g21-0048`
  ↳ *because* `g21-0050`
  ↳ *evidence-for* `g20-0285`

- `g21-0054` *STATED* — An always-on Project with role, rules and context is the difference between a chatbot and an employee, and its absence is why most people's AI-team version falls apart.
  > “That is the difference between a chatbot and an employee, and it is why most people's version falls apart.”
  — [g-turn-claude-into-a-six-person-ai-c-suite](https://chen.media/guides/turn-claude-into-a-six-person-ai-c-suite)
  ↳ *evidence-for* `g20-0285`

- `g21-0193` *CORE* — The people getting a real edge run a flagship model as a system: they let it spawn a swarm, route cheap work to a cheaper model, and let it drive their tools while they are gone.
  — [g-three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team](https://chen.media/guides/three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team)
  ↳ *part-of* `g21-0190`
  ↳ *generalizes* `g22-0048`

- `g21-0198` *STATED* — Ultra mode takes a job that would eat a person a week and hands it back in minutes.
  — [g-three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team](https://chen.media/guides/three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team)
  ↳ *qualifies* `g21-0197`

- `g21-0201` *STATED* — Ultra mode shines when the work is large and splittable.
  — [g-three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team](https://chen.media/guides/three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team)
  ↳ *qualifies* `g21-0194`

- `g21-0212` *STATED* — You do not need to hire a five-person content team: hand each job to Claude as its own skill, then run them like a team.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *part-of* `g21-0210`

- `g22-0066` *CORE* — Claude Code Routines run in the cloud on a schedule, even with your laptop closed, and drop the finished work in your folder by morning.
  — [g-put-a-recurring-job-on-autopilot-with-claude-code](https://chen.media/guides/put-a-recurring-job-on-autopilot-with-claude-code)
  ↳ *part-of* `g22-0065`
  ↳ *enables* `g22-0279` — Routines run monthly re-checks unattended
  ↳ *evidence-for* `r04-0089`
  ↳ *evidence-for* `g20-0288`

- `g22-0067` *STATED* — Claude Code Routines let you save one job as a prompt, connect the tools it needs, and set it on a schedule.
  — [g-put-a-recurring-job-on-autopilot-with-claude-code](https://chen.media/guides/put-a-recurring-job-on-autopilot-with-claude-code)
  ↳ *part-of* `g22-0065`
  ↳ *part-of* `g22-0070`

- `g22-0068` *STATED* — Once saved, a Claude Code Routine runs on its own in Anthropic's cloud: no laptop on, no babysitting.
  > “No laptop on, no babysitting.”
  — [g-put-a-recurring-job-on-autopilot-with-claude-code](https://chen.media/guides/put-a-recurring-job-on-autopilot-with-claude-code)
  ↳ *qualifies* `g22-0066`

- `r01-0040` *STATED* — /agency gives each agency job to an agent inside Claude, and the agents hand work to each other.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0037`
  ↳ *evidence-for* `g07-0052`

- `r01-0050` *CORE* — In /agency nothing is sent without your yes.
  > “Nothing is sent without your yes.”
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *qualifies* `r01-0037`
  ↳ *evidence-for* `g07-0069`
  ↳ *example-of* `g09-0247`

- `r02-0177` *CORE* — Sub-agents cannot see the conversation: every /launch controller knows only the mission file and the project, so `.launch/mission.md` must stand on its own.
  > “Sub-agents cannot see this conversation.”
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *because* `r02-0178` — mission must stand alone
  ↳ *generalizes* `r02-0077`

- `r02-0242` *INFERRED* — In the CaptionPal poll, isolated stations that never saw each other's calls independently converged on the same root bugs (admin leak, migration restart, captions never saved), which is evidence the blind-panel design catches real issues rather than noise.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0311`
  ↳ *evidence-for* `r01-0016`

- `r04-0094` *STATED* — The night crew can't spend money, delete anything or touch your live app.
  > “They can't spend money, delete anything or touch your live app.”
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)

- `r04-0095` *STATED* — Every night crew member only opens draft pull requests on claude/ branches, so nothing reaches your app until you merge it.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *because* `r04-0094`
  ↳ *example-of* `g09-0247`

- `r04-0099` *STATED* — The night crew needs your app in a GitHub repo, connected to Claude Code on the web.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *depends-on* `r04-0087`

- `r04-0109` *STATED* — The night crew has no server and nothing to host: the skill writes the standing orders and helps you create three routines in your own claude.ai account.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *because* `r04-0089`

- `r04-0158` *STATED* — Night crew routines run against the GitHub repository every night on Anthropic's cloud while the laptop is closed, and each opens a pull request in the morning.
  > “on Anthropic's cloud, while their laptop is closed”
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *qualifies* `r04-0089`
  ↳ *evidence-for* `g22-0068`
  ↳ *evidence-for* `g20-0288`

- `r04-0162` *STATED* — A routine clones the repo from its default branch every run and pushes to claude/ branches, so the night crew's standing orders must be committed on the default branch in NIGHT-CREW.md at the repo root.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *defines* `r04-0110`
  ↳ *leads-to* `r04-0178`

- `r04-0194` *STATED* — With the default branch protected, the night crew can only ever propose changes.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *evidence-for* `r04-0095`

- `r04-0215` *STATED* — /shark returns BOARD.md: how many sharks are in, every decision and offer, what would change their minds, and the questions you could not answer yet.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `g09-0248`

- `r04-0228` *STATED* — In /shark, Claude only hosts: it never invests, never answers for you and never edits a decision.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0021`

- `r04-0249` *STATED* — Sub-agents cannot see the conversation: the /shark investors and founder know only what is in .shark/pitch.md, so it must stand on its own.
  > “Sub-agents cannot see this conversation.”
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *evidence-for* `r04-0018`
  ↳ *leads-to* `r04-0250`
  ↳ *evidence-for* `r02-0177`

- `y01-0080` *STATED* — The ai-agency-claude teams don't just give generic advice: they write landing pages, build email sequences, create ads, research prospects and more.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *qualifies* `y01-0079`

- `y01-0090` *STATED* — With the agency installed Claude stops being a basic chatbot: separate teams handle finding clients, researching businesses, building social media posts, SEO and GEO.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *depends-on* `y01-0087`

- `y02-0035` *STATED* — Each specialist agent in The Agency has its own personality and process.
  > “each with its own personality and process”
  — [SChgKT-vXHk](https://youtu.be/SChgKT-vXHk) [GaXO0ZKN4WI](https://youtu.be/GaXO0ZKN4WI) [Di7KzYJ7NwA](https://youtu.be/Di7KzYJ7NwA)
  ↳ *evidence-for* `g17-0261`
  ↳ *part-of* `y02-0033`
  ↳ *qualifies* `y02-0034`

- `y02-0152` *STATED* — MiroFish's simulated customers talk about your launch with each other like a real feed.
  — [tQRaHRjRROk](https://youtu.be/tQRaHRjRROk) [fYrca_-P1NI](https://youtu.be/fYrca_-P1NI)
  ↳ *part-of* `y02-0148`

- `y02-0166` *STATED* — Because Claude agrees with everything you say, Alex Chen made it argue with itself instead.
  > “Claude agrees with everything you say, so I made it argue with itself instead”
  — [LpUuv9AtUTo](https://youtu.be/LpUuv9AtUTo) [a6Qw-Dg_SNk](https://youtu.be/a6Qw-Dg_SNk)
  ↳ *evidence-for* `g09-0245`
  ↳ *because* `y02-0165`

- `y03-0043` *STATED* — In Ultra Code (ultracode), dozens of Claudes split one task and check each other's work.
  — [ItG-vSZFWgA](https://youtu.be/ItG-vSZFWgA) [mVKBGZNsSa4](https://youtu.be/mVKBGZNsSa4) [HTu9VPLvcP0](https://youtu.be/HTu9VPLvcP0)
  ↳ *example-of* `g02-0245`
  ↳ *part-of* `y03-0035`

- `y04-0003` *STATED* — In Bot Crossing each bot (one Claude Code session) claims a plot for its project and starts building on it, so every project has its own visible spot in the colony.
  > “each one claims a plot for its project and starts building”
  — [Hfgfyi4-xOI](https://youtu.be/Hfgfyi4-xOI)
  ↳ *part-of* `y04-0001`

- `y04-0004` *STATED* — In Bot Crossing, the moment a Claude Code session needs you it stops working and its bot holds a question mark over its head.
  > “The second one needs you and stops working and holds a question mark over its head.”
  — [Hfgfyi4-xOI](https://youtu.be/Hfgfyi4-xOI)
  ↳ *part-of* `y04-0001`
  ↳ *enables* `y04-0005`
  ↳ *enables* `y04-0009`

- `y04-0009` *STATED* — With Bot Crossing you can run as many Claude Code sessions as you want in parallel and never lose track of them.
  > “you can run as many Claude sessions as you want and never lose track”
  — [Hfgfyi4-xOI](https://youtu.be/Hfgfyi4-xOI)

- `y04-0099` *STATED* — In the 3D office, the agents pick roles, claim tasks and collaborate in real time.
  > “They pick roles, claim tasks, and collaborate in real time.”
  — [A3XmoC6Ybws](https://youtu.be/A3XmoC6Ybws)
  ↳ *evidence-for* `g13-0256`
  ↳ *part-of* `y04-0098`

- `y04-0100` *STATED* — The 3D agent office offers team setups such as a creative agency, a game studio or a music team.
  > “You can choose setups like a creative agency, game studio, or music team.”
  — [A3XmoC6Ybws](https://youtu.be/A3XmoC6Ybws)
  ↳ *qualifies* `y04-0097`
  ↳ *contrast* `y04-0031` — agency of visible agents vs agency packed into one app

- `y04-0101` *STATED* — Each agent in the 3D office handles its tasks, shares updates, and asks you when it gets stuck.
  > “each agent handles tasks, shares updates, and even asks you when it gets stuck”
  — [A3XmoC6Ybws](https://youtu.be/A3XmoC6Ybws)
  ↳ *part-of* `y04-0097`

- `y04-0102` *STATED* — You can watch everything the agents do happen live in the 3D office.
  > “you can literally watch everything happen live”
  — [A3XmoC6Ybws](https://youtu.be/A3XmoC6Ybws)
  ↳ *part-of* `y04-0097`

- `y04-0103` *STATED* — The 3D agent office runs right in your browser.
  > “it even runs right in your browser”
  — [A3XmoC6Ybws](https://youtu.be/A3XmoC6Ybws)
  ↳ *evidence-for* `g13-0254`
  ↳ *qualifies* `y04-0097`

### concept

- `g01-0192` *INFERRED* — Recurring multi-Claude quality pattern: several reviewers judge in isolation (no shared notes, fresh context, or a different agent from the builder) so no verdict is anchored and nobody grades their own work.
  — [g-find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free](https://chen.media/guides/find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free) [g-let-claude-tailor-your-resume-to-every-job-without-inventing-anything](https://chen.media/guides/let-claude-tailor-your-resume-to-every-job-without-inventing-anything) [g-reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style)
  ↳ *contrast* `g01-0173` — reviewer subagents vs fact-finding subagent
  ↳ *generalizes* `g20-0284`

- `g02-0027` *INFERRED* — The five Claudes in /hunter are the headhunter (finds and filters), the recruiter (scores), the hiring manager (scores), the resume writer (resume and cover letter) and the form filler (application packet).
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *defines* `g02-0001`
  ↳ *evidence-for* `r02-0055`
  ↳ *evidence-for* `g20-0285`

- `g03-0015` *CORE* — Helper agents (subagents) carry hidden costs he keeps returning to: they inherit the session model, their descriptions sit in context, their web searches share the session cap, and they hold their whole work pile until their window is nearly full.
  — [g-run-every-claude-helper-agent-on-haiku](https://chen.media/guides/run-every-claude-helper-agent-on-haiku) [g-shorten-your-claude-helper-agent-descriptions](https://chen.media/guides/shorten-your-claude-helper-agent-descriptions) [g-stop-claude-running-out-of-web-searches](https://chen.media/guides/stop-claude-running-out-of-web-searches) [g-make-your-claude-helpers-summarize-themselves-sooner](https://chen.media/guides/make-your-claude-helpers-summarize-themselves-sooner) [g-roast-room-a-free-claude-council-that-argues-over-your-business-decisions](https://chen.media/guides/roast-room-a-free-claude-council-that-argues-over-your-business-decisions)

- `g03-0199` *STATED* — Each Roast Room advisor is built from a famous founder's public work, and each seat owns one question.
  — [g-roast-room-a-free-claude-council-that-argues-over-your-business-decisions](https://chen.media/guides/roast-room-a-free-claude-council-that-argues-over-your-business-decisions)
  ↳ *defines* `g03-0196`

- `g04-0019` *STATED* — The Academic Research Skills journal-style review includes a devil's advocate reviewer.
  > “run a journal-style review with a devil's advocate”
  — [g-academic-research-skills-make-claude-check-every-source-in-your-paper-is-real](https://chen.media/guides/academic-research-skills-make-claude-check-every-source-in-your-paper-is-real)
  ↳ *part-of* `g04-0018`
  ↳ *example-of* `g19-0197`

- `g04-0101` *STATED* — /hiring-panel's Claudes are told to try to reject your resume rather than approve it: adversarial review before a real employer sees it.
  > “seven Claudes that try to reject it”
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *part-of* `g04-0099`
  ↳ *example-of* `g08-0250`

- `g04-0110` *STATED* — The five /hiring-panel reader personas are: the hiring manager, another applicant for the same job, the CEO, the recruiter with 30 seconds, and the teammate you would sit next to.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *part-of* `g04-0109`
  ↳ *contrast* `g04-0154` — overlapping persona sets: both seat a hiring manager
  ↳ *evidence-for* `g08-0041`

- `g04-0154` *STATED* — The five /linkedin-roast personas are: a recruiter, a hiring manager, a founder, an expert in your field, and a peer at your level.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *part-of* `g04-0153`
  ↳ *evidence-for* `g07-0247`

- `g04-0245` *CORE* — Alex's review skills run several Claude personas in parallel that each judge alone without seeing each other's notes, so no reviewer anchors on or softens another's verdict.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free) [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked) [g-academic-research-skills-make-claude-check-every-source-in-your-paper-is-real](https://chen.media/guides/academic-research-skills-make-claude-check-every-source-in-your-paper-is-real)
  ↳ *enables* `g04-0249`
  ↳ *evidence-for* `r01-0016`

- `g05-0239` *STATED* — The Founder skills act like a company team: a board, a CFO, a marketing director and a panel of 100 buyer agents.
  — [g-the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar](https://chen.media/guides/the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar)
  ↳ *part-of* `g05-0238`

- `g05-0249` *INFERRED* — Founder's shared founder/ folder works as a file-based message bus: agents hand off state through files instead of chat.
  — [g-the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar](https://chen.media/guides/the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar)
  ↳ *generalizes* `g05-0241`
  ↳ *part-of* `g20-0285`

- `g09-0152` *STATED* — Each shark has its own lens: the numbers shark, the customer shark, the skeptic, the one who only invests for a cut of every sale, and the one who asks whether this is a business or a hobby.
  — [g-pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill](https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill)
  ↳ *part-of* `g09-0151`
  ↳ *evidence-for* `r04-0211`

- `g09-0169` *STATED* — The court's twelve juror personas: an accountant, a first-time customer, a competitor, a retired judge, a teenager, an engineer, a small-business owner, a statistician, a parent, an investor, a designer and a lawyer.
  — [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill)
  ↳ *part-of* `g09-0168`
  ↳ *evidence-for* `r01-0166`

- `g09-0228` *INFERRED* — Scheduling the tracker routine after the builder lets one cloud agent audit another's pull request before a human ever reads it.
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)
  ↳ *qualifies* `g09-0222`
  ↳ *because* `r04-0183`

- `g12-0180` *STATED* — Guide section 'The second AI that decides' says a second AI decides which old tool output Fast-Jev Compaction drops (body email-gated).
  — [g-stop-claude-code-s-compact-from-summarizing-away-your-chat](https://chen.media/guides/stop-claude-code-s-compact-from-summarizing-away-your-chat)
  ↳ *part-of* `g12-0171`
  ↳ *qualifies* `g12-0178`

- `g13-0243` *STATED* — The SWARM Loop's three reviewers are a skeptic, a beginner and a critic.
  — [g-swarm-loop-three-reviewers-guide](https://chen.media/guides/swarm-loop-three-reviewers-guide)
  ↳ *part-of* `g13-0242`
  ↳ *evidence-for* `y04-0046`

- `g15-0074` *STATED* — MetaGPT's core idea is written in its README as a formula: Code = SOP(Team).
  > “Code = SOP(Team)”
  — [g-metagpt-one-line-in-a-whole-software-company-out](https://chen.media/guides/metagpt-one-line-in-a-whole-software-company-out)
  ↳ *defines* `g15-0075`

- `g15-0076` *STATED* — MetaGPT's roles include a product manager, an architect and engineers, each doing their own job before passing the work on.
  — [g-metagpt-one-line-in-a-whole-software-company-out](https://chen.media/guides/metagpt-one-line-in-a-whole-software-company-out)
  ↳ *part-of* `g15-0075`
  ↳ *example-of* `g15-0183`

- `g15-0082` *STATED* — Each Munder Difflin agent has its own working directory, its own memory that survives the app being closed, and its own mailbox that other agents post into.
  — [g-munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents](https://chen.media/guides/munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents)
  ↳ *part-of* `g15-0079`
  ↳ *evidence-for* `g15-0081`
  ↳ *example-of* `g15-0183`
  ↳ *analogy-for* `g05-0249`

- `g15-0094` *STATED* — The Judge Loop's three roles are a prosecutor, a defense and a judge (role bodies locked).
  — [g-the-judge-loop-three-lines-that-put-claude-s-output-on-trial](https://chen.media/guides/the-judge-loop-three-lines-that-put-claude-s-output-on-trial)
  ↳ *part-of* `g15-0092`
  ↳ *analogy-for* `r01-0157`

- `g15-0107` *STATED* — wshobson/agents generates every agent from a single Markdown source into whatever harness you run.
  — [g-the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build](https://chen.media/guides/the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build)
  ↳ *part-of* `g15-0105`
  ↳ *enables* `g15-0110`

- `g15-0169` *STATED* — The two-agent version of this technique is written up on chen.media as the Gauntlet Loop; the boss loop adds the fan-out (a TEAM of builders) and the cost control.
  — [g-the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer](https://chen.media/guides/the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer)
  ↳ *generalizes* `g16-0156`

- `g15-0182` *INFERRED* — A human approval gate is treated as a feature, not friction: linkedin-skills drafts and waits for your yes, and Munder Difflin keeps a permission gate switched on.
  — [g-linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes](https://chen.media/guides/linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes) [g-munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents](https://chen.media/guides/munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents)
  ↳ *evidence-for* `g09-0247`

- `g15-0183` *INFERRED* — Specialist roles beat one generalist session: wshobson/agents (202 agents), The Agency (273 agents), MetaGPT's product-manager/architect/engineer SOP and Munder Difflin's office all split work across role-specific agents.
  — [g-the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build](https://chen.media/guides/the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build) [g-the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install](https://chen.media/guides/the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install) [g-metagpt-one-line-in-a-whole-software-company-out](https://chen.media/guides/metagpt-one-line-in-a-whole-software-company-out) [g-munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents](https://chen.media/guides/munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents)
  ↳ *evidence-for* `g18-0286`

- `g16-0158` *STATED* — Instead of you reading a result and asking for another pass, the Gauntlet prompt sets up two kinds of agent and lets them argue.
  > “the prompt sets up two kinds of agent and lets them argue”
  — [g-the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work](https://chen.media/guides/the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work)
  ↳ *part-of* `g16-0156`

- `g16-0165` *STATED* — The separate critic agent is the whole trick of the Gauntlet Loop.
  > “Why the separate critic is the whole trick”
  — [g-the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work](https://chen.media/guides/the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work)
  ↳ *qualifies* `g16-0158`
  ↳ *because* `g16-0164`
  ↳ *example-of* `g16-0010`
  ↳ *evidence-for* `g19-0210`
  ↳ *evidence-for* `g20-0284`

- `g16-0297` *STATED* — Ruflo sits around Claude Code rather than replacing it.
  > “It sits around Claude Code”
  — [g-ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm](https://chen.media/guides/ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm)
  ↳ *part-of* `g16-0296`

- `g17-0075` *STATED* — Each Anthropic finance agent template packages three things: skills, connectors and subagents.
  — [g-anthropic-s-ten-finance-agents-for-equity-research-and-modelling](https://chen.media/guides/anthropic-s-ten-finance-agents-for-equity-research-and-modelling)
  ↳ *defines* `g17-0074`

- `g17-0085` *STATED* — Alex Chen's finance-agents guide explains where the agents' data comes from.
  > “Where the data comes from”
  — [g-anthropic-s-ten-finance-agents-for-equity-research-and-modelling](https://chen.media/guides/anthropic-s-ten-finance-agents-for-equity-research-and-modelling)
  ↳ *qualifies* `g17-0077`

- `g17-0110` *STATED* — Alex Chen's Claude SEO guide names all eighteen specialist agents.
  > “The eighteen agents, by name”
  — [g-install-25-seo-skills-and-18-specialist-agents-into-claude-code](https://chen.media/guides/install-25-seo-skills-and-18-specialist-agents-into-claude-code)
  ↳ *part-of* `g17-0104`

- `g17-0261` *STATED* — Each Agency agent file contains the agent's personality, the rules it must follow and the deliverables it owes you.
  > “its personality, the rules it must follow and the deliverables it owes you”
  — [g-286-specialist-ai-agents-free-inside-claude-code](https://chen.media/guides/286-specialist-ai-agents-free-inside-claude-code)
  ↳ *defines* `g17-0260`

- `g17-0264` *STATED* — Alex Chen ranks The Agency's 18 divisions by size.
  > “The 18 divisions, by size”
  — [g-286-specialist-ai-agents-free-inside-claude-code](https://chen.media/guides/286-specialist-ai-agents-free-inside-claude-code)
  ↳ *part-of* `g17-0258`

- `g18-0286` *CORE* — Alex repeatedly promotes pre-written specialist-agent rosters: ECC's 67 agents, contains-studio's eight departments, the 268-role repo and msitarzewski/agency-agents.
  — [g-67-agents-281-skills-and-94-commands-in-one-install](https://chen.media/guides/67-agents-281-skills-and-94-commands-in-one-install) [g-an-entire-ai-company-in-one-repo-eight-departments](https://chen.media/guides/an-entire-ai-company-in-one-repo-eight-departments) [g-268-expert-roles-in-one-repo-free](https://chen.media/guides/268-expert-roles-in-one-repo-free) [g-seven-free-repos-that-replace-paid-ai-tools](https://chen.media/guides/seven-free-repos-that-replace-paid-ai-tools)
  ↳ *contrast* `g18-0284` — add many agents vs subtract instructions

- `g19-0031` *STATED* — Tier 6 of the 50 Claude tips is 'Workflow and automation'.
  > “Workflow and automation”
  — [g-50-claude-tips-ranked-worst-to-best](https://chen.media/guides/50-claude-tips-ranked-worst-to-best)
  ↳ *part-of* `g19-0043`

- `g19-0072` *STATED* — The assembly-line effect means one job per station and nothing moves until it is signed off.
  > “one job per station, nothing moves until it is signed off”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *defines* `g19-0060`

- `g19-0075` *STATED* — The seven-station guide's section 'The seven stations' names the seven single-job roles.
  > “The seven stations”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *part-of* `g19-0060`
  ↳ *part-of* `g19-0062`

- `g19-0195` *STATED* — The other ninety percent of what Claude can do is an Agent Graph.
  > “The other ninety percent is an Agent Graph.”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)

- `g19-0202` *STATED* — Agent Graph step: name the five agents.
  > “Name the five agents”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)
  ↳ *part-of* `g19-0192`
  ↳ *part-of* `g19-0196`

- `g20-0030` *STATED* — Part 2 of the JARVIS build is 'the hands': making Claude do things instead of just knowing things, a separate build from the brain.
  > “Part 2 is the hands: making it do things instead of just knowing things.”
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *part-of* `g20-0023`

- `g20-0113` *STATED* — Alex contrasts 'Babysitting vs the agentic OS': supervising every step versus a system where Claude has earned autonomy.
  > “Babysitting vs the agentic OS”
  — [g-how-to-let-claude-run-for-hours-without-supervising-it](https://chen.media/guides/how-to-let-claude-run-for-hours-without-supervising-it)
  ↳ *part-of* `g20-0105`
  ↳ *generalizes* `g20-0108`
  ↳ *example-of* `g20-0282`

- `g20-0284` *CORE* — Across Alex's agent-team guides, the maker never grades its own work: a separate reviewer, blind grader, read-only gate or judge with nothing to defend does the grading.
  — [g-the-second-claude-that-reviews-the-first-one-s-work](https://chen.media/guides/the-second-claude-that-reviews-the-first-one-s-work) [g-run-the-job-five-times-and-let-a-blind-grader-pick](https://chen.media/guides/run-the-job-five-times-and-let-a-blind-grader-pick) [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team) [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it) [g-how-to-let-claude-run-for-hours-without-supervising-it](https://chen.media/guides/how-to-let-claude-run-for-hours-without-supervising-it)

- `g20-0285` *CORE* — Alex's multi-agent pattern locks each Claude agent to one job or lens in its own space, and hands work between them through shared files or folders.
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it) [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team) [g-the-second-claude-that-reviews-the-first-one-s-work](https://chen.media/guides/the-second-claude-that-reviews-the-first-one-s-work)

- `g20-0288` *CORE* — Overnight unattended runs recur across Alex's guides: a week of work in one night, 'The overnight run', a dev team shipping while you sleep, and 'the night shift'.
  — [g-how-to-let-claude-run-for-hours-without-supervising-it](https://chen.media/guides/how-to-let-claude-run-for-hours-without-supervising-it) [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model) [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team) [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *generalizes* `g20-0106`

- `r01-0016` *CORE* — Alex's panel skills keep reviewers independent: no juror or reader sees another's notes or vote, so nobody can just go along with the room.
  — [r-court-skill](https://github.com/alexyc9381/court-skill) [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *because* `r01-0167`
  ↳ *because* `r01-0129`

- `r01-0167` *STATED* — No /court juror sees another's vote, so nobody can just go along with the room.
  > “No juror sees another's vote, so nobody can just go along with the room.”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *qualifies* `r01-0165`

- `r01-0188` *STATED* — In /court Claude only orchestrates: it never argues a side, never votes and never edits the verdict.
  > “Claude only orchestrates: it never argues a side, never votes and never edits the verdict.”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *evidence-for* `r04-0021`

- `r02-0311` *CORE* — Alex's panel skills give each Claude one job and keep them blind to each other's answers (/hunter's two scorers, /launch's 8 stations) so no reviewer anchors on another.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill) [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *contrast* `r02-0122`
  ↳ *evidence-for* `g04-0245`

- `r02-0312` *CORE* — Alex's skills prepare everything but leave the irreversible action to the human: /hunter never submits an application, /launch never changes code.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill) [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *contrast* `r02-0107` — autonomous prep, human send
  ↳ *evidence-for* `g09-0247`

- `r03-0104` *INFERRED* — /learn splits correction-detection in two: a cheap phrase-matching hook tuned to over-catch, and a Claude investigator that throws out the false alarms.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *generalizes* `r03-0103`

- `r03-0337` *INFERRED* — Both repos use a second Claude as a checker with a narrow brief: /learn's nightly investigator reviews the day's corrections, and /linkedin-roast's five isolated sub-agents review one profile.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill) [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *generalizes* `r03-0009`
  ↳ *generalizes* `r03-0155`
  ↳ *evidence-for* `g20-0284`

- `r04-0018` *INFERRED* — Agents that run without the conversation (shark sub-agents, night-crew cloud routines) see only the file they are handed, so Alex makes that one file the whole briefing.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill) [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *generalizes* `r02-0177`

- `r04-0021` *CORE* — In Alex's skills Claude only hosts and never fills in the other party's part: /mentor never writes the learner's answers, and /shark never answers for the founder, never invests and never writes a decision.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill) [r-shark-skill](https://github.com/alexyc9381/shark-skill)

- `r04-0093` *STATED* — All three night crew members work from one file, NIGHT-CREW.md, that the skill writes with you: your app, your backlog, your customers, and the house rules.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0087`
  ↳ *defines* `r04-0117`
  ↳ *part-of* `g20-0285`

- `r04-0117` *STATED* — NIGHT-CREW.md opens: three Claude Code routines read this file every night and do one job each; they run on their own with nobody watching, so this file is the whole briefing.
  > “They run on their own, with nobody watching, so this file is the whole briefing.”
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *evidence-for* `r04-0018`
  ↳ *leads-to* `r04-0112`

- `r04-0211` *STATED* — Each /shark investor has a personality and a signature line: the tech billionaire shark ('Is this a business or a hobby?'), the royalty shark (only offers money for a cut of every sale), the customer shark, the numbers shark and the skeptic shark.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *qualifies* `r04-0210`

- `y01-0086` *STATED* — In ai-agency-claude the main agency system is only the command center; the actual work is done by the specialized teams inside the repo.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *qualifies* `y01-0085`

- `y01-0089` *STATED* — ai-agency-claude departments are driven by slash commands of the form /<department> <subcommand> <website or company>: /market..., /sales..., /geo....
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *part-of* `y01-0086`

- `y01-0104` *STATED* — The five /sales agents split roles: one researches the business, one judges how strong a prospect it is, one looks for decision makers, one analyzes its competitors, and one builds the outreach strategy.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *evidence-for* `g20-0285`
  ↳ *part-of* `y01-0103`
  ↳ *example-of* `y01-0005`

- `y02-0034` *STATED* — The Agency ships a full roster of specialist agents — front-end designers, ad writers, Reddit community wizards, and more.
  > “front-end designers, ad writers, Reddit community wizards”
  — [SChgKT-vXHk](https://youtu.be/SChgKT-vXHk) [GaXO0ZKN4WI](https://youtu.be/GaXO0ZKN4WI) [Di7KzYJ7NwA](https://youtu.be/Di7KzYJ7NwA)
  ↳ *evidence-for* `g15-0113`
  ↳ *part-of* `y02-0033`

- `y04-0105` *CORE* — Bot Crossing and the 3D agent office share one design idea: render agents as visible characters so an agent that is stuck and asking for you is obvious at a glance.
  — [Hfgfyi4-xOI](https://youtu.be/Hfgfyi4-xOI) [A3XmoC6Ybws](https://youtu.be/A3XmoC6Ybws)
  ↳ *evidence-for* `g13-0308`
  ↳ *generalizes* `y04-0004`
  ↳ *generalizes* `y04-0101`

### definition

- `g01-0002` *STATED* — The seven /hiring-panel Claudes are an automated screen, a hiring manager, and five readers who each judge the resume alone as someone different.
  — [g-find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free](https://chen.media/guides/find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free)
  ↳ *defines* `g01-0001`
  ↳ *evidence-for* `g08-0029`

- `g04-0201` *STATED* — A Claude Code helper agent (subagent) works in its own chat, separate from the main conversation.
  — [g-make-your-claude-helper-agents-compact-their-own-chat-early](https://chen.media/guides/make-your-claude-helper-agents-compact-their-own-chat-early)
  ↳ *defines* `g04-0011` — what a subagent is
  ↳ *because* `r02-0177`

- `g06-0020` *STATED* — The /iq pattern-speed reader judges how fast you notice the same problem coming back in a new costume, and whether you fix the whole class of it.
  > “how fast you notice the same problem coming back in a new costume”
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *part-of* `g06-0019`

- `g06-0021` *STATED* — The /iq planning-depth reader judges how many steps ahead you plan, what you check before you build, and whether you think about what happens after it works.
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *part-of* `g06-0019`

- `g06-0085` *STATED* — A Claude Code dynamic workflow runs dozens of Claude agents from one script.
  — [g-run-claude-agent-swarms-without-burning-your-limit](https://chen.media/guides/run-claude-agent-swarms-without-burning-your-limit)
  ↳ *defines* `g06-0084`

- `g07-0182` *CORE* — Claude Code Projects turns one chat into a coordinator that splits your goal into threads, each its own Claude on its own branch, all sharing one memory.
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`

- `g07-0184` *STATED* — A Claude Code project is one ongoing conversation where Claude runs a stream of work for you.
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`
  ↳ *defines* `g07-0182`

- `g08-0029` *STATED* — The /hiring-panel skill's seven Claudes are an automated screen, a hiring manager and five readers who each judge the resume alone as someone different.
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill)
  ↳ *defines* `g08-0028`

- `g08-0215` *STATED* — An Agent Office shows one worker at one desk for each Claude Code session you have open.
  — [g-see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office](https://chen.media/guides/see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office)
  ↳ *defines* `g08-0204`

- `g08-0216` *STATED* — Agent Office statuses are readable from across the room: working, waiting for you, your turn, or finished.
  — [g-see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office](https://chen.media/guides/see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office)
  ↳ *part-of* `g08-0204`

- `g09-0172` *STATED* — In the court skill, 'conditions for acquittal' are the specific changes that would flip the most juror votes.
  > “the conditions for acquittal: the specific changes that would flip the most votes”
  — [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill)
  ↳ *defines* `g09-0171`

- `g11-0063` *STATED* — A tournament strategy card combines a way of reasoning, a way of working, and a priority.
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *defines* `g11-0062`

- `g11-0135` *CORE* — OpenAI's dots are always-on agents inside ChatGPT with their own computer (and browser) in the cloud that keep working between your chats.
  — [g-let-chatgpt-fix-your-apps-bugs-while-you-sleep](https://chen.media/guides/let-chatgpt-fix-your-apps-bugs-while-you-sleep) [g-get-your-own-chatgpt-dot](https://chen.media/guides/get-your-own-chatgpt-dot)
  ↳ *part-of* `g11-0117`

- `g12-0267` *STATED* — Polsia is an AI co-founder: you give it a business goal, and a team of AI agents plans the company, builds the app, launches it and markets it.
  — [g-set-up-polsia-the-ai-co-founder-that-runs-your-business](https://chen.media/guides/set-up-polsia-the-ai-co-founder-that-runs-your-business)
  ↳ *part-of* `g12-0266`

- `g15-0164` *STATED* — The boss loop is a way of writing one prompt so that Claude does the checking instead of you.
  — [g-the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer](https://chen.media/guides/the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer)
  ↳ *generalizes* `g15-0169` — team fan-out of the two-agent Gauntlet Loop
  ↳ *example-of* `g15-0181`

- `g16-0296` *STATED* — A model writes; a harness gives it tools, memory, loops and controls so it can actually work. Ruflo is the harness.
  > “a model writes, a harness gives it tools, memory, loops and controls so it can actually work. Ruflo is the harness.”
  — [g-ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm](https://chen.media/guides/ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm)
  ↳ *defines* `g16-0292`

- `g17-0074` *STATED* — Anthropic's finance agents are not a product you buy; they are reference architectures published in a public repo.
  > “They are not a product you buy. They are reference architectures published in a public repo”
  — [g-anthropic-s-ten-finance-agents-for-equity-research-and-modelling](https://chen.media/guides/anthropic-s-ten-finance-agents-for-equity-research-and-modelling)
  ↳ *qualifies* `g17-0073`

- `g17-0076` *STATED* — In Anthropic's finance agent templates, skills are the instructions and domain knowledge for the task.
  > “skills (the instructions and domain knowledge for the task)”
  — [g-anthropic-s-ten-finance-agents-for-equity-research-and-modelling](https://chen.media/guides/anthropic-s-ten-finance-agents-for-equity-research-and-modelling)
  ↳ *part-of* `g17-0075`

- `g17-0077` *STATED* — In Anthropic's finance agent templates, connectors are governed access to the data the task runs on.
  > “connectors (governed access to the data the task runs on)”
  — [g-anthropic-s-ten-finance-agents-for-equity-research-and-modelling](https://chen.media/guides/anthropic-s-ten-finance-agents-for-equity-research-and-modelling)
  ↳ *part-of* `g17-0075`

- `g17-0078` *STATED* — In Anthropic's finance agent templates, subagents are extra Claude models the main agent calls for sub-tasks such as comparables selection or a methodology check.
  > “subagents (extra Claude models the main agent calls for sub tasks like comparables selection or a methodology check)”
  — [g-anthropic-s-ten-finance-agents-for-equity-research-and-modelling](https://chen.media/guides/anthropic-s-ten-finance-agents-for-equity-research-and-modelling)
  ↳ *part-of* `g17-0075`
  ↳ *contrast* `g17-0261` — Anthropic subagents = extra Claude models; Agency agents = markdown personas

- `g17-0260` *STATED* — Each agent in The Agency is a single markdown file.
  > “Each agent is a single markdown file.”
  — [g-286-specialist-ai-agents-free-inside-claude-code](https://chen.media/guides/286-specialist-ai-agents-free-inside-claude-code)
  ↳ *part-of* `g17-0258`

- `g18-0003` *STATED* — ECC is not a prompt pack and not a course; it is an agent harness that runs inside a tool you already use.
  > “It is not a prompt pack and it is not a course.”
  — [g-67-agents-281-skills-and-94-commands-in-one-install](https://chen.media/guides/67-agents-281-skills-and-94-commands-in-one-install)
  ↳ *defines* `g18-0001`

- `g18-0216` *STATED* — Each of the 268 agent definitions already knows its role, its scope, and what it is supposed to hand back.
  — [g-268-expert-roles-in-one-repo-free](https://chen.media/guides/268-expert-roles-in-one-repo-free)
  ↳ *defines* `g18-0215`

- `g19-0196` *STATED* — An Agent Graph splits Claude into a small team that hands work down a line.
  > “You split Claude into a small team that hands work down a line”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)
  ↳ *defines* `g19-0195`

- `g21-0197` *STATED* — Ultra mode is a multi-agent system built into GPT-5.6 Sol: instead of one long reasoning chain, Sol spins up several subagents that each take a different piece, work in parallel, and merge into one result.
  — [g-three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team](https://chen.media/guides/three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team)
  ↳ *defines* `g21-0194`
  ↳ *analogy-for* `y03-0043`

- `r01-0028` *STATED* — In /shark each Claude shark goes IN or OUT with a practice offer.
  — [r-alexyc9381](https://github.com/alexyc9381/alexyc9381)
  ↳ *defines* `r01-0027`

- `r01-0041` *STATED* — The five /agency agents are outbound, sales, workflow, customer service and the night shift.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *defines* `r01-0037`
  ↳ *evidence-for* `g07-0052`

- `r01-0119` *STATED* — The seven /hiring-panel reviewers are an automated screen, a hiring manager, and five readers who each judge the resume alone as someone different.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *defines* `r01-0116`
  ↳ *evidence-for* `g08-0029`

- `r01-0162` *STATED* — The /court prosecutor Claude builds the strongest honest case that your idea fails as described.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0161`
  ↳ *contrast* `r01-0163`

- `r01-0163` *STATED* — The /court defense Claude builds the strongest honest case that your idea works.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0161`

- `r01-0166` *STATED* — The 12 /court juror personas: an accountant, a first-time customer, a competitor, a retired judge, a teenager, an engineer, a small-business owner, a statistician, a parent, an investor, a designer and a lawyer.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *defines* `r01-0165`

- `r01-0168` *STATED* — The /court judge Claude reads the verdict, the charges that stuck, what the defense got right, and the conditions for acquittal.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0161`
  ↳ *example-of* `g09-0246`

- `r01-0207` *STATED* — /court casts the main Claude as the clerk of the court: it never argues, never votes, and never softens the verdict.
  > “You are the clerk of the court. You never argue, never vote, and never soften the verdict.”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *defines* `r01-0188`
  ↳ *evidence-for* `r04-0021`

- `r01-0223` *STATED* — The /court phases run in order: opening, rebuttal, jury, judge.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *defines* `r01-0222`

- `r01-0275` *STATED* — The standing /court charge: 'The case fails as stated: it should not go ahead the way it is described.'
  > “The case fails as stated: it should not go ahead the way it is described.”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0274`
  ↳ *defines* `r01-0162` — prosecution argues the charge

- `r02-0007` *STATED* — Claude 1 of /hunter, the headhunter, finds new postings from the sources you list and drops the ones that clearly don't fit.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0001`
  ↳ *part-of* `g02-0001`

- `r02-0009` *STATED* — Claude 2 of /hunter, the recruiter, scores your fit out of 100 on must-haves, keywords, level, location and (per SKILL.md) work authorization.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0001`
  ↳ *part-of* `r02-0080`
  ↳ *part-of* `g02-0001`

- `r02-0010` *STATED* — Claude 3 of /hunter, the hiring manager, scores your fit out of 100 on whether you could do the job on day one and what the proof is.
  > “could you do the job on day one, and what is the proof?”
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0001`
  ↳ *part-of* `r02-0080`
  ↳ *part-of* `g02-0001`
  ↳ *evidence-for* `r01-0131`

- `r02-0011` *STATED* — Claude 4 of /hunter, the resume writer, rewrites your resume and writes a cover letter for each job that scores high.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0001`
  ↳ *part-of* `g02-0001`

- `r02-0012` *STATED* — Claude 5 of /hunter, the form filler, answers every field of the application and puts it all in one packet.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0001`
  ↳ *part-of* `g02-0001`

- `r02-0134` *STATED* — After the poll a flight director Claude writes up the holds, the fixes in the order to do them, and a watch list for the first week.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0118`
  ↳ *leads-to* `r02-0135`

- `r02-0169` *STATED* — In /launch the main Claude is the launch coordinator: it writes the mission, runs the poll and reads out the result.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *defines* `r02-0156`

- `r03-0017` *STATED* — .learn/reviews/ holds one note per night: each mistake, why it happened, what to do instead, and the rule it became.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0009`

- `r03-0031` *STATED* — '/learn review' runs the investigator: it goes over every correction not reviewed yet and writes the lessons.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0072`

- `r03-0033` *STATED* — '/learn nightly' prints the copy-paste setup to run the review every night, filled in for your project.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0072`

- `r03-0051` *STATED* — The /learn investigator is Claude following the review steps in skills/learn/SKILL.md; the script hands it the inbox and, when Claude Code's session file can be read, what Claude had just said before each correction.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *defines* `r03-0009`

- `r04-0089` *STATED* — Claude Code routines are scheduled cloud agents (docs: code.claude.com/docs/en/routines); /night-crew sets up three of them on your app's GitHub repo.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *defines* `r04-0087`

- `r04-0155` *STATED* — In NIGHT-CREW.md, <date> means the date the run started, as YYYY-MM-DD.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *qualifies* `r04-0142`
  ↳ *qualifies* `r04-0145`

- `y01-0005` *STATED* — An AI agent (Alex's plain-English definition) can take steps toward a result - reading files, making changes, and checking its work - rather than only returning an answer in the chat.
  > “That means it can take steps toward a result, such as reading files, making changes, and checking its work.”
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *defines* `y01-0004`

- `y04-0047` *STATED* — The Swarm Loop's skeptic agent challenges claims.
  > “a skeptic to challenge claims”
  — [kDh_gdXsJJU](https://youtu.be/kDh_gdXsJJU) [PG_HanOn_KE](https://youtu.be/PG_HanOn_KE) [jw25LS4GgUg](https://youtu.be/jw25LS4GgUg)
  ↳ *part-of* `g13-0243`
  ↳ *part-of* `y04-0046`

- `y04-0048` *STATED* — The Swarm Loop's beginner agent flags confusing parts.
  > “a beginner to flag confusing parts”
  — [kDh_gdXsJJU](https://youtu.be/kDh_gdXsJJU) [PG_HanOn_KE](https://youtu.be/PG_HanOn_KE) [jw25LS4GgUg](https://youtu.be/jw25LS4GgUg)
  ↳ *part-of* `g13-0243`
  ↳ *part-of* `y04-0046`

- `y04-0049` *STATED* — The Swarm Loop's ruthless critic cuts the fluff.
  > “a ruthless critic to cut the fluff”
  — [kDh_gdXsJJU](https://youtu.be/kDh_gdXsJJU) [PG_HanOn_KE](https://youtu.be/PG_HanOn_KE) [jw25LS4GgUg](https://youtu.be/jw25LS4GgUg)
  ↳ *part-of* `g13-0243`
  ↳ *part-of* `y04-0046`

### example

- `g01-0185` *STATED* — The Scientific Agent Skills Drug Discovery Pipeline example has Claude prioritise EGFR inhibitor candidates for preclinical lung-cancer research using six skills: database-lookup, rdkit, datamol, diffdock, paper-lookup and scientific-visualization.
  — [g-give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills](https://chen.media/guides/give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills)
  ↳ *example-of* `g01-0177`
  ↳ *depends-on* `g01-0184`
  ↳ *depends-on* `g01-0183`

- `g03-0200` *STATED* — Roast Room seat Jeff Bezos owns: Is this the right bet, and how reversible is it?
  — [g-roast-room-a-free-claude-council-that-argues-over-your-business-decisions](https://chen.media/guides/roast-room-a-free-claude-council-that-argues-over-your-business-decisions)
  ↳ *part-of* `g03-0199`

- `g03-0201` *STATED* — Roast Room seat Paul Graham owns: Do people actually want this, and is it growing?
  — [g-roast-room-a-free-claude-council-that-argues-over-your-business-decisions](https://chen.media/guides/roast-room-a-free-claude-council-that-argues-over-your-business-decisions)
  ↳ *part-of* `g03-0199`

- `g03-0202` *STATED* — Roast Room seat Alex Hormozi owns: Will people pay, how much, and how do we close?
  — [g-roast-room-a-free-claude-council-that-argues-over-your-business-decisions](https://chen.media/guides/roast-room-a-free-claude-council-that-argues-over-your-business-decisions)
  ↳ *part-of* `g03-0199`

- `g03-0203` *STATED* — Roast Room seat Gary Vaynerchuk owns: Where does the attention come from?
  — [g-roast-room-a-free-claude-council-that-argues-over-your-business-decisions](https://chen.media/guides/roast-room-a-free-claude-council-that-argues-over-your-business-decisions)
  ↳ *part-of* `g03-0199`

- `g03-0204` *STATED* — Roast Room seat Dan Martell owns: Who does this, and what does it cost your calendar?
  — [g-roast-room-a-free-claude-council-that-argues-over-your-business-decisions](https://chen.media/guides/roast-room-a-free-claude-council-that-argues-over-your-business-decisions)
  ↳ *part-of* `g03-0199`

- `g03-0205` *STATED* — Roast Room seat Gino Wickman owns: Can the business run this without you holding it together?
  — [g-roast-room-a-free-claude-council-that-argues-over-your-business-decisions](https://chen.media/guides/roast-room-a-free-claude-council-that-argues-over-your-business-decisions)
  ↳ *part-of* `g03-0199`

- `g03-0206` *STATED* — Roast Room seat Warren Buffett owns: What does it do to cash, risk and long-term value?
  — [g-roast-room-a-free-claude-council-that-argues-over-your-business-decisions](https://chen.media/guides/roast-room-a-free-claude-council-that-argues-over-your-business-decisions)
  ↳ *part-of* `g03-0199`

- `g05-0176` *STATED* — The renamer subagent body scopes it tightly: 'You rename files and symbols exactly as asked, update every import, and report what changed. Do not refactor anything else.'
  > “You rename files and symbols exactly as asked, update every import, and report what changed. Do not refactor anything else.”
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)
  ↳ *part-of* `g05-0175`
  ↳ *example-of* `g19-0073`

- `g08-0090` *STATED* — The Agency's specialists include a frontend developer, a UI designer, an ad creative strategist and a Reddit community builder.
  — [g-run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents](https://chen.media/guides/run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents)
  ↳ *example-of* `g08-0089`
  ↳ *evidence-for* `y02-0034`

- `g09-0025` *STATED* — In the Boardroom the marketing head asks why anyone would care, and the sales head asks where your first customers would even come from.
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives)
  ↳ *example-of* `g09-0024`

- `g11-0142` *STATED* — In OpenAI's keynote demo, a user's bug report landed in a feedback channel and an engineer's dot picked it up and opened a pull request with the fix.
  — [g-let-chatgpt-fix-your-apps-bugs-while-you-sleep](https://chen.media/guides/let-chatgpt-fix-your-apps-bugs-while-you-sleep)
  ↳ *example-of* `g11-0136`

- `g11-0159` *STATED* — In OpenAI's demo a dot noticed a finance review had been moved to the same time as the owner's daughter's recital, flagged it on its own and set about rescheduling it.
  — [g-get-your-own-chatgpt-dot](https://chen.media/guides/get-your-own-chatgpt-dot)
  ↳ *example-of* `g11-0152`

- `g11-0160` *STATED* — Inside OpenAI, a bug report posted in Slack gets picked up by a dot.
  — [g-get-your-own-chatgpt-dot](https://chen.media/guides/get-your-own-chatgpt-dot)
  ↳ *example-of* `g11-0136`
  ↳ *evidence-for* `g11-0142`

- `g13-0004` *STATED* — With five Claude Code sessions running, Bot Crossing shows at a glance which one is stuck, instead of you finding out hours later that Claude was waiting on you the whole time.
  — [g-watch-every-claude-code-session-as-a-bot-in-bot-crossing](https://chen.media/guides/watch-every-claude-code-session-as-a-bot-in-bot-crossing)
  ↳ *example-of* `g13-0003`
  ↳ *evidence-for* `y04-0005`

- `g14-0121` *STATED* — Jev example: a support workflow asks which department owns a ticket and whether the customer is reporting an urgent problem, and the result changes the ticket's route without a person reading a generated explanation first.
  — [g-jev-typesafe-ai-explained](https://chen.media/guides/jev-typesafe-ai-explained)
  ↳ *example-of* `g14-0117`

- `g16-0161` *STATED* — Matt Shumer's Claude of Duty demo: a playable browser shooter, roughly 55,000 lines of Three.js, produced from a single prompt by Claude Opus 5.
  — [g-the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work](https://chen.media/guides/the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work)
  ↳ *evidence-for* `g16-0156`

- `g17-0084` *STATED* — Alex Chen's video covered three of Anthropic's ten finance agents; the guide covers the other seven.
  > “The three from the video / The other seven”
  — [g-anthropic-s-ten-finance-agents-for-equity-research-and-modelling](https://chen.media/guides/anthropic-s-ten-finance-agents-for-equity-research-and-modelling)
  ↳ *part-of* `g17-0080`
  ↳ *qualifies* `g17-0309`

- `g21-0059` *STATED* — C-suite setup step 4: name each Project after the employee so you can find them fast: Mia, Jack, Max, Ben, Kate, Leo.
  — [g-turn-claude-into-a-six-person-ai-c-suite](https://chen.media/guides/turn-claude-into-a-six-person-ai-c-suite)
  ↳ *part-of* `g21-0055`
  ↳ *leads-to* `g21-0060`

- `g21-0205` *STATED* — Example Ultra-mode goal: a full teardown of [company]: positioning, pricing, product gaps, and 3 ways to beat them.
  — [g-three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team](https://chen.media/guides/three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team)
  ↳ *part-of* `g21-0204`

- `r01-0177` *STATED* — Example: '/court Quit my job to sell candles on Etsy full time. I have $8,000 saved and 40 sales so far.'
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0157`
  ↳ *leads-to* `r01-0186`

- `r01-0239` *STATED* — The 3-juror candle trial seated the Statistician, the Parent and the Lawyer; all three voted GUILTY.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0186`
  ↳ *example-of* `r01-0178`

- `r03-0197` *STATED* — Recruiter persona: 'You are a recruiter hiring for roles like the ones this person seems to want. You look at 100 profiles a day and search by job title and keyword. You decide in six seconds whether to message.'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0195`

- `r03-0198` *STATED* — Hiring manager persona: 'You manage the team this person would join and you have an open seat. You ask one thing: can they do the job from day one, and what is the proof?'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0195`

- `r03-0199` *STATED* — Founder persona: 'You run a small company and can make one hire. You have no patience for buzzwords. You want someone who owns results and ships.'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0195`

- `r03-0200` *STATED* — Expert persona: 'You are a senior expert in {field} with 15 years in it. You can tell real depth from borrowed jargon, and you notice claims that do not add up.'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0195`

- `r03-0201` *STATED* — Peer persona: 'You work at the same level as this person, in {field} ({level}). Would you trust this profile? What would you copy? What makes you roll your eyes?'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0195`

- `r04-0116` *STATED* — The example NIGHT-CREW.md is for a made-up app, Groomly; yours is written from your answers and your repo.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *defines* `r04-0108`

- `r04-0119` *STATED* — Groomly's stack line: Next.js 15 (TypeScript), Postgres via Prisma, hosted on Vercel.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0116`

- `r04-0120` *STATED* — Groomly backlog item 1: a signup page for groomers: email and password, then their business name and city.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0116`
  ↳ *example-of* `r04-0168`

- `r04-0121` *STATED* — Groomly backlog item 2: a public pricing page with the two plans from lib/plans.ts.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0116`

- `r04-0122` *STATED* — Groomly backlog item 3 embeds its own limit: booking reminder emails 24 hours before an appointment (write the template and the job; don't send anything).
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0116`
  ↳ *example-of* `r04-0134` — backlog item embeds don't-send rule

- `r04-0123` *STATED* — Groomly backlog item 4: dark mode for the groomer dashboard.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0116`

- `r04-0127` *STATED* — Groomly 'How to check your work': Install npm ci, Test npm test, Build npm run build, Lint npm run lint.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0116`
  ↳ *example-of* `r04-0175`

- `r04-0128` *STATED* — Groomly's owner never-touch list: prisma/migrations/, app/api/payments/, anything in .github/workflows/.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0116`
  ↳ *example-of* `r04-0172`

- `r04-0221` *STATED* — Example /shark invocation: /shark A subscription box of local hot sauces. $35 a month, 12 customers so far, I want to reach 500.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0206`

- `y01-0074` *STATED* — Scheduled task example: a weekly report that uses your saved skill and is prepared for review each Friday morning.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *example-of* `y01-0073`
  ↳ *depends-on* `y01-0066`

- `y02-0081` *STATED* — Rebuild example: Alex Chen ran it on Duolingo ('because I hate the bird mascot') — the Spy scans the entire Duolingo app.
  — [Tvhn8L2lOL0](https://youtu.be/Tvhn8L2lOL0)
  ↳ *example-of* `y02-0077`

- `y02-0082` *STATED* — Rebuild example: the Entrepreneur found that people hate losing hearts in Duolingo, so the clone avoids making that feature in the first place.
  — [Tvhn8L2lOL0](https://youtu.be/Tvhn8L2lOL0)
  ↳ *example-of* `y02-0080`

- `y02-0083` *STATED* — Rebuild example: the system then automatically rebuilds Duolingo entirely from scratch.
  — [Tvhn8L2lOL0](https://youtu.be/Tvhn8L2lOL0)
  ↳ *example-of* `y02-0078`
  ↳ *leads-to* `y02-0084`

- `y02-0095` *STATED* — Projects example: tell Claude to 'launch your app' and one Claude writes the emails while another builds your site at the exact same time.
  — [GF2xgaEnQ0o](https://youtu.be/GF2xgaEnQ0o) [g6ZnVE4kQCk](https://youtu.be/g6ZnVE4kQCk)
  ↳ *example-of* `g07-0185`
  ↳ *example-of* `y02-0094`
  ↳ *analogy-for* `y02-0163` — parallel Claudes shipping launch assets

- `y02-0141` *STATED* — The launch panel means a leaked password gets caught before a stranger spends thousands of your hard-earned money.
  — [Bn4UhbHJzxo](https://youtu.be/Bn4UhbHJzxo) [7cYKEcBNFV4](https://youtu.be/7cYKEcBNFV4) [DE32ZPcENjY](https://youtu.be/DE32ZPcENjY)
  ↳ *example-of* `g09-0116`
  ↳ *example-of* `y02-0136`
  ↳ *analogy-for* `y02-0045`

- `y02-0163` *STATED* — Night crew example: by the time you wake up you get a brand new signup page, a week's worth of social media posts, and a launch video ready to post.
  — [8Yo0i9jLCzY](https://youtu.be/8Yo0i9jLCzY)
  ↳ *qualifies* `r04-0134` — video promises social posts and a launch video 'ready to post'; house rule 5 says the crew never posts, it only writes drafts
  ↳ *example-of* `y02-0157`
  ↳ *evidence-for* `y02-0164`

- `y02-0183` *STATED* — If your idea sucks the sharks say 'I'm out' — 'even though Barbara was never going to invest anyway'.
  > “the sharks will say, I'm out even though Barbara was never going to invest anyway”
  — [O-ngH7V3_U0](https://youtu.be/O-ngH7V3_U0)
  ↳ *evidence-for* `r04-0214`
  ↳ *part-of* `y02-0180`

- `y04-0005` *STATED* — If you run five Claude Code sessions and one of them is stuck waiting on you, Bot Crossing lets you spot it instantly.
  > “if you're running five sessions and one of them is stuck waiting on you, you can spot it instantly”
  — [Hfgfyi4-xOI](https://youtu.be/Hfgfyi4-xOI)
  ↳ *because* `y04-0006` — the instant spot replaces hours of silent idling
  ↳ *example-of* `y04-0009`

### idea

- `g03-0210` *INFERRED* — Roast Room's design gives each persona-agent a single owned question (reversibility, demand, pricing, attention, time, operations, cash) so the panel covers distinct angles instead of seven similar opinions.
  — [g-roast-room-a-free-claude-council-that-argues-over-your-business-decisions](https://chen.media/guides/roast-room-a-free-claude-council-that-argues-over-your-business-decisions)
  ↳ *generalizes* `g03-0199`
  ↳ *contrast* `g03-0181` — diverse owned questions vs three independent identical votes
  ↳ *evidence-for* `g20-0285`

- `g06-0265` *INFERRED* — Alex's quality pattern is to separate maker from judge: two independent Claude readers in /iq, and Codex auditing Claude's plan (and Claude auditing Codex's build) in Pair.
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill) [g-pair-make-claude-and-codex-check-each-other-s-work](https://chen.media/guides/pair-make-claude-and-codex-check-each-other-s-work)
  ↳ *generalizes* `g06-0019`
  ↳ *generalizes* `g06-0159`
  ↳ *evidence-for* `g20-0284`

- `g11-0116` *INFERRED* — The /advisor is a two-model review loop: one model executes every turn, a second model reviews only at decision points with full context and no tool access.
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)
  ↳ *generalizes* `g11-0099`
  ↳ *contrast* `g11-0071` — advisor reviews one trajectory; tournament judge compares rivals
  ↳ *evidence-for* `g06-0265`

- `g11-0150` *INFERRED* — The overnight bug-to-pull-request flow is a night-shift automation whose only human gate is approving the pull request.
  — [g-let-chatgpt-fix-your-apps-bugs-while-you-sleep](https://chen.media/guides/let-chatgpt-fix-your-apps-bugs-while-you-sleep)
  ↳ *generalizes* `g11-0137`
  ↳ *example-of* `g09-0247`

- `g16-0015` *INFERRED* — Recurring advice: stop doing repeated work by hand — automate the job you keep redoing (tip 13), turn tasks into slash commands, hooks and skills (prompts 13-15), and install repos that take over jobs you currently do manually.
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert) [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build) [g-seven-free-claude-code-repos-that-fix-what-claude-gets-wrong](https://chen.media/guides/seven-free-claude-code-repos-that-fix-what-claude-gets-wrong)
  ↳ *generalizes* `g22-0069`

- `r01-0189` *CORE* — Alex's /court design moves counting and state into a Python script so the orchestrating Claude cannot fudge the tally — deterministic code for bookkeeping, models only for judgment.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *generalizes* `r01-0187`
  ↳ *because* `r01-0188`
  ↳ *enables* `r04-0021`

- `y03-0062` *INFERRED* — The keep-going paragraph and the verification loop solve the two halves of unattended Claude runs: one stops Claude quitting early, the other stops it declaring done when the work is broken.
  — [ThrAfrg8rjQ](https://youtu.be/ThrAfrg8rjQ) [DHCciHdW-Nw](https://youtu.be/DHCciHdW-Nw) [vdYlR2BjM3o](https://youtu.be/vdYlR2BjM3o) [4FLM_FjtiBo](https://youtu.be/4FLM_FjtiBo) [0YmOIYAiwiM](https://youtu.be/0YmOIYAiwiM) [rDBGrDeXAh4](https://youtu.be/rDBGrDeXAh4)
  ↳ *qualifies* `g20-0288`

### method

- `g01-0007` *STATED* — Step 2 of /hiring-panel: one Claude plays the automated system (applicant screen) that decides whether a real human should even see your resume.
  — [g-find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free](https://chen.media/guides/find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free)
  ↳ *part-of* `g01-0001`
  ↳ *leads-to* `g01-0010`

- `g01-0010` *STATED* — Step 3 of /hiring-panel: a second Claude plays the hiring manager who decides whether you get the interview and says what decided it in the first ten seconds.
  — [g-find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free](https://chen.media/guides/find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free)
  ↳ *part-of* `g01-0001`
  ↳ *leads-to* `g01-0011`
  ↳ *evidence-for* `g08-0040`

- `g01-0011` *STATED* — Step 4 of /hiring-panel: five more Claudes start at the same time and read the resume alone, each as someone different.
  — [g-find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free](https://chen.media/guides/find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free)
  ↳ *part-of* `g01-0001`
  ↳ *leads-to* `g01-0014`

- `g01-0013` *STATED* — None of the five parallel /hiring-panel readers sees the others' notes, so each verdict is independent.
  > “None of them sees the others' notes.”
  — [g-find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free](https://chen.media/guides/find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free)
  ↳ *qualifies* `g01-0011`
  ↳ *example-of* `g01-0192`
  ↳ *evidence-for* `r01-0016`

- `g01-0014` *STATED* — Step 5 of /hiring-panel: all seven answers are merged into one numbered list of mistakes, worst first, each with the resume line it is about.
  — [g-find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free](https://chen.media/guides/find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free)
  ↳ *part-of* `g01-0001`
  ↳ *leads-to* `g01-0015`
  ↳ *evidence-for* `g08-0043`

- `g01-0040` *STATED* — Claude Resume Kit's /critique command has five reader personas, from an ATS bot to a technical reviewer, score the result on eight dimensions in a fresh context.
  — [g-let-claude-tailor-your-resume-to-every-job-without-inventing-anything](https://chen.media/guides/let-claude-tailor-your-resume-to-every-job-without-inventing-anything)
  ↳ *part-of* `g01-0034`
  ↳ *contrast* `g01-0002` — 5 personas in a fresh context vs 7-Claude panel
  ↳ *example-of* `g01-0192`
  ↳ *example-of* `g04-0245`

- `g01-0153` *STATED* — ReelMimic takes a reference video apart (shots, pacing, transitions, colours, camera moves), plans a new video with you, then up to six Claude agents build it while a different agent checks every shot.
  — [g-reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style)
  ↳ *defines* `g01-0152`

- `g01-0159` *STATED* — In ReelMimic up to 6 AI agents work on different parts of the video at the same time.
  — [g-reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style)
  ↳ *leads-to* `g01-0160`
  ↳ *example-of* `g02-0245`

- `g01-0160` *STATED* — In ReelMimic each finished shot goes to a new agent for review, so nobody grades their own work.
  > “so nobody grades their own work”
  — [g-reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style)
  ↳ *leads-to* `g01-0163`
  ↳ *example-of* `g01-0192`
  ↳ *evidence-for* `g20-0284`

- `g01-0173` *STATED* — In Grill Me, finding facts is Claude's job: it sends a sub-agent to look things up in your project instead of asking you.
  — [g-grill-me-make-claude-interview-you-before-it-writes-a-line-of-code](https://chen.media/guides/grill-me-make-claude-interview-you-before-it-writes-a-line-of-code)
  ↳ *part-of* `g01-0169`

- `g02-0003` *STATED* — /hunter runs every morning and finds new jobs that fit you.
  > “every morning it finds new jobs that fit you”
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *part-of* `g02-0001`
  ↳ *leads-to* `g02-0014`

- `g02-0004` *STATED* — In /hunter a recruiter Claude and a hiring-manager Claude each score a job's fit out of 100.
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *part-of* `g02-0001`

- `g02-0005` *STATED* — For the high-scoring jobs, /hunter rewrites your resume, writes a cover letter and fills out the whole application; you tap yes and send it.
  > “You tap yes and send it.”
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *part-of* `g02-0001`

- `g02-0011` *STATED* — /hunter step 1: you give it your resume once, plus the jobs you want, where you want them, and the places to look.
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *leads-to* `g02-0014`
  ↳ *part-of* `g02-0029`

- `g02-0014` *STATED* — /hunter step 2: the headhunter Claude reads your sources and finds the postings you have not seen yet.
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *leads-to* `g02-0015`

- `g02-0015` *STATED* — The /hunter headhunter drops postings that clearly miss on title, location or your dealbreakers before any scoring happens.
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *leads-to* `g02-0016`

- `g02-0016` *STATED* — /hunter step 3: for every job left, two Claudes read it alone, each as someone different, so the two fit scores are independent.
  > “two Claudes read it alone, each as someone different”
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *leads-to* `g02-0020`
  ↳ *part-of* `g02-0004`
  ↳ *example-of* `g02-0245`
  ↳ *evidence-for* `r02-0056`
  ↳ *evidence-for* `r01-0016`

- `g02-0017` *STATED* — The /hunter recruiter Claude checks the posting's must-haves, keywords and level.
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *part-of* `g02-0016`
  ↳ *contrast* `g02-0018` — must-haves/keywords vs day-one ability
  ↳ *evidence-for* `r02-0009`

- `g02-0018` *STATED* — The /hunter hiring-manager Claude asks whether you could do the job on day one.
  > “The hiring manager asks if you could do the job on day one.”
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *part-of* `g02-0016`
  ↳ *evidence-for* `r02-0010`

- `g02-0019` *STATED* — Each /hunter scorer gives a fit score out of 100 and says why; you see one combined score, like 94/100.
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *part-of* `g02-0016`
  ↳ *evidence-for* `r02-0078`

- `g02-0021` *STATED* — Jobs below the /hunter threshold are listed with the reason and nothing else is written for them, so no resume or cover-letter work is spent on weak fits.
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *part-of* `g02-0020`

- `g02-0022` *STATED* — /hunter step 5: the resume-writer Claude rewrites your resume to lead with what that job asks for and writes a cover letter.
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *leads-to* `g02-0024`
  ↳ *part-of* `g02-0005`
  ↳ *evidence-for* `r02-0011`

- `g02-0024` *STATED* — /hunter step 6: the form-filler Claude writes an application packet with an answer for every field and a flag on the fields only you can answer.
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *leads-to* `g02-0025`
  ↳ *part-of* `g02-0005`
  ↳ *evidence-for* `r02-0012`

- `g02-0025` *STATED* — After writing the packets, the /hunter form filler stops and shows you the list; you say yes to the ones you want.
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *evidence-for* `g02-0010`
  ↳ *evidence-for* `r02-0003`

- `g02-0029` *STATED* — /hunter is set up once and then runs every morning (guide sections 'Set it up once' and 'Every morning').
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *qualifies* `g02-0003`

- `g02-0153` *STATED* — claude-seo's team of agents checks your content, your technical setup and whether AI search can find you, then hands back a prioritized fix list.
  — [g-have-claude-audit-your-whole-website-for-google](https://chen.media/guides/have-claude-audit-your-whole-website-for-google)
  ↳ *part-of* `g02-0151`
  ↳ *leads-to* `g02-0157`
  ↳ *evidence-for* `g17-0101`
  ↳ *example-of* `g09-0248`

- `g02-0169` *STATED* — For never-reviewed PRs, github-triage can spawn a review agent per PR.
  — [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say)
  ↳ *part-of* `g02-0166`
  ↳ *example-of* `g02-0245`

- `g02-0215` *STATED* — Video Use builds animation overlays (HyperFrames, Remotion, Manim or PIL) with one sub-agent per animation, in parallel.
  — [g-video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video](https://chen.media/guides/video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video)
  ↳ *part-of* `g02-0207`
  ↳ *example-of* `g02-0245`

- `g02-0245` *CORE* — Featured skills fan work out to parallel sub-agents per unit of work: claude-seo runs up to 17 agents at once, github-triage spawns one review agent per PR, Video Use one sub-agent per animation, /hunter two independent scorer Claudes per job.
  — [g-have-claude-audit-your-whole-website-for-google](https://chen.media/guides/have-claude-audit-your-whole-website-for-google) [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say) [g-video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video](https://chen.media/guides/video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video) [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)

- `g03-0181` *STATED* — /triage re-checks every finding with three independent votes, drops duplicates and false alarms, and ranks the rest by danger.
  — [g-hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills](https://chen.media/guides/hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills)
  ↳ *part-of* `g03-0178`
  ↳ *leads-to* `g03-0182`
  ↳ *analogy-for* `g03-0044` — both add a second, AI-driven pass to cut false alarms
  ↳ *example-of* `r01-0016`

- `g03-0207` *STATED* — Each Roast Room advisor is a Claude sub-agent that reads its own notes compiled from that person's public letters, essays, talks and videos.
  — [g-roast-room-a-free-claude-council-that-argues-over-your-business-decisions](https://chen.media/guides/roast-room-a-free-claude-council-that-argues-over-your-business-decisions)
  ↳ *example-of* `g03-0015`
  ↳ *enables* `g03-0199`

- `g03-0209` *STATED* — Running Roast Room: Step 1 set it up, Step 2 run a roast, plus a section on what to put in your question.
  — [g-roast-room-a-free-claude-council-that-argues-over-your-business-decisions](https://chen.media/guides/roast-room-a-free-claude-council-that-argues-over-your-business-decisions)
  ↳ *part-of* `g03-0196`

- `g03-0225` *STATED* — Step 2 of the descriptions guide: trim them with a copy-paste prompt that shortens every subagent description.
  — [g-shorten-your-claude-helper-agent-descriptions](https://chen.media/guides/shorten-your-claude-helper-agent-descriptions)
  ↳ *part-of* `g03-0009`
  ↳ *contrast* `g03-0221`

- `g03-0252` *STATED* — Open the helper's file in .claude/agents/ (or ~/.claude/agents/); its settings sit between the two --- lines at the top.
  > “The settings sit between the two --- lines at the top.”
  — [g-make-your-claude-helpers-summarize-themselves-sooner](https://chen.media/guides/make-your-claude-helpers-summarize-themselves-sooner)
  ↳ *leads-to* `g03-0253`

- `g03-0253` *STATED* — Step 2 of the early-compaction guide: add the line, using the exact number format that works.
  — [g-make-your-claude-helpers-summarize-themselves-sooner](https://chen.media/guides/make-your-claude-helpers-summarize-themselves-sooner)
  ↳ *part-of* `g03-0250`

- `g04-0018` *STATED* — After the integrity check, Academic Research Skills has a panel of Claude reviewers review the paper the way a journal would.
  — [g-academic-research-skills-make-claude-check-every-source-in-your-paper-is-real](https://chen.media/guides/academic-research-skills-make-claude-check-every-source-in-your-paper-is-real)
  ↳ *part-of* `g04-0014`
  ↳ *example-of* `g04-0245`

- `g04-0104` *STATED* — In /hiring-panel, one Claude plays the automated screening system (the 'robot screen') that decides whether a real human should even see your resume.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *part-of* `g04-0100`

- `g04-0108` *STATED* — In /hiring-panel, a second Claude plays the hiring manager who decides whether you get the interview, and says what decided it in the first ten seconds.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *part-of* `g04-0100`
  ↳ *contrast* `g04-0158` — 10-second vs 6-second first-impression windows
  ↳ *evidence-for* `g08-0040`

- `g04-0109` *STATED* — In /hiring-panel, five more Claudes start at the same time and each reads the resume alone as a different person.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *part-of* `g04-0100`
  ↳ *leads-to* `g04-0112`

- `g04-0112` *STATED* — /hiring-panel merges all seven answers into one numbered list of mistakes, worst first, with the resume line each one is about.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *leads-to* `g04-0113`
  ↳ *example-of* `g04-0246`
  ↳ *evidence-for* `g08-0043`

- `g04-0153` *STATED* — /linkedin-roast starts five Claudes at the same time, each reading your profile alone as someone different.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *leads-to* `g04-0161`
  ↳ *evidence-for* `r03-0134`

- `g04-0161` *STATED* — After the five roasts, /linkedin-roast shows a short list of what all five reviewers agree on.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *leads-to* `g04-0162`
  ↳ *evidence-for* `r03-0217`

- `g04-0249` *CORE* — Alex's panel skills follow critique-then-fix: independent Claude reviews are merged first, then Claude rewrites the work with the problems fixed.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free) [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *leads-to* `g09-0246`

- `g05-0120` *STATED* — Up to six Claude agents build different parts of a ReelMimic video at the same time.
  — [g-reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style)
  ↳ *part-of* `g05-0114`
  ↳ *leads-to* `g05-0121`
  ↳ *contrast* `g05-0239` — parallel builder agents vs simulated company roles
  ↳ *evidence-for* `g01-0159`

- `g05-0121` *STATED* — Each finished ReelMimic shot goes to a different agent to check, so nobody grades their own work.
  > “Each finished shot goes to a different agent to check, so nobody grades their own work.”
  — [g-reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style)
  ↳ *part-of* `g05-0114`
  ↳ *example-of* `g05-0313`
  ↳ *evidence-for* `g01-0160`

- `g05-0130` *STATED* — At every Mortiflix stage Claude stops and waits; only you can approve the stage.
  > “At every stage Claude stops and waits. Only you can approve it”
  — [g-mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer](https://chen.media/guides/mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer)
  ↳ *part-of* `g05-0128`
  ↳ *qualifies* `g05-0135`
  ↳ *example-of* `g05-0312`
  ↳ *example-of* `g09-0247`

- `g05-0135` *STATED* — A Mortiflix Claude session works until it has something for you to review, submits it, and stops.
  — [g-mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer](https://chen.media/guides/mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer)
  ↳ *part-of* `g05-0128`

- `g05-0170` *STATED* — Or set effort per run by telling Claude: 'Run the renamer subagent at low effort for this job.'
  > “Run the renamer subagent at low effort for this job.”
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)
  ↳ *part-of* `g05-0161`

- `g05-0241` *STATED* — Each Founder skill writes into a founder/ folder in your project, and the next skill reads it, so they work as one team.
  — [g-the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar](https://chen.media/guides/the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar)
  ↳ *part-of* `g05-0238`
  ↳ *enables* `g05-0239`

- `g05-0252` *STATED* — A separate Claude Code process, on your own login, has to keep or drop every OpenQodex scanner finding and give a reason.
  — [g-install-openqodex-a-second-claude-reviews-your-code-before-you-push](https://chen.media/guides/install-openqodex-a-second-claude-reviews-your-code-before-you-push)
  ↳ *part-of* `g05-0250`
  ↳ *example-of* `g05-0314`
  ↳ *evidence-for* `g20-0284`

- `g05-0313` *CORE* — Separate-reviewer rule: the agent that made the work never grades it — ReelMimic sends each shot to a different agent, OpenQodex uses a separate Claude Code process.
  — [g-reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style) [g-install-openqodex-a-second-claude-reviews-your-code-before-you-push](https://chen.media/guides/install-openqodex-a-second-claude-reviews-your-code-before-you-push)
  ↳ *evidence-for* `g20-0284`

- `g06-0005` *STATED* — The /iq skill uses two readers that each score you: one on how fast you spot patterns, one on how many steps ahead you plan.
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *part-of* `g06-0001`

- `g06-0019` *STATED* — Step 3 of /iq: two Claudes read the evidence file at the same time and alone, so neither sees the other's judgement.
  > “Two Claudes read it at the same time and alone.”
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *part-of* `g06-0001`
  ↳ *leads-to* `g06-0022`
  ↳ *part-of* `g06-0005`
  ↳ *evidence-for* `g07-0150`
  ↳ *evidence-for* `r01-0016`

- `g06-0022` *STATED* — Step 4 of /iq: each reader scores you out of 100 and says where the score came from.
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *part-of* `g06-0001`
  ↳ *leads-to* `g06-0026`
  ↳ *evidence-for* `g07-0151`

- `g06-0126` *STATED* — Point Claude at a game folder and universal-modder has it follow a safe loop to build the mod.
  — [g-set-up-universal-modder-the-free-repo-that-lets-claude-mod-your-pc-games](https://chen.media/guides/set-up-universal-modder-the-free-repo-that-lets-claude-mod-your-pc-games)
  ↳ *part-of* `g06-0124`

- `g06-0134` *STATED* — universal-modder writes a field note for the next agent after a modding run.
  > “write a field note for the next agent”
  — [g-set-up-universal-modder-the-free-repo-that-lets-claude-mod-your-pc-games](https://chen.media/guides/set-up-universal-modder-the-free-repo-that-lets-claude-mod-your-pc-games)
  ↳ *part-of* `g06-0124`
  ↳ *analogy-for* `g06-0242` — notes for the next agent vs notes for the next session
  ↳ *part-of* `g20-0285`

- `g06-0160` *STATED* — Pair step 1: Claude writes PLAN.md with the goal, steps, files, and how to test.
  — [g-pair-make-claude-and-codex-check-each-other-s-work](https://chen.media/guides/pair-make-claude-and-codex-check-each-other-s-work)
  ↳ *part-of* `g06-0158`
  ↳ *leads-to* `g06-0161`
  ↳ *part-of* `g20-0285`

- `g06-0161` *STATED* — Pair step 2: Codex audits PLAN.md read-only and ends with VERDICT: PASS or VERDICT: BLOCK.
  > “VERDICT: PASS or VERDICT: BLOCK”
  — [g-pair-make-claude-and-codex-check-each-other-s-work](https://chen.media/guides/pair-make-claude-and-codex-check-each-other-s-work)
  ↳ *part-of* `g06-0158`
  ↳ *leads-to* `g06-0163`
  ↳ *contrast* `g06-0024` — external auditor vs instructed self-restraint

- `g06-0162` *STATED* — In Pair, on VERDICT: BLOCK Claude fixes the plan and Codex audits again, up to 3 times.
  — [g-pair-make-claude-and-codex-check-each-other-s-work](https://chen.media/guides/pair-make-claude-and-codex-check-each-other-s-work)
  ↳ *qualifies* `g06-0161`
  ↳ *contradicts* `y04-0108` — plan-audit loop: Pair re-audits 'up to 3 times' vs split video 'go back and forth until they agree' (no cap)

- `g06-0163` *STATED* — Pair step 3: Codex builds from the passed plan and writes BUILD-NOTES.md.
  — [g-pair-make-claude-and-codex-check-each-other-s-work](https://chen.media/guides/pair-make-claude-and-codex-check-each-other-s-work)
  ↳ *part-of* `g06-0158`
  ↳ *leads-to* `g06-0164`

- `g06-0164` *STATED* — Pair step 4: Claude checks every changed file against the plan and runs the tests.
  — [g-pair-make-claude-and-codex-check-each-other-s-work](https://chen.media/guides/pair-make-claude-and-codex-check-each-other-s-work)
  ↳ *part-of* `g06-0158`

- `g06-0165` *STATED* — In Pair, test failures go to FIXES.md and back to Codex.
  — [g-pair-make-claude-and-codex-check-each-other-s-work](https://chen.media/guides/pair-make-claude-and-codex-check-each-other-s-work)
  ↳ *qualifies* `g06-0164`

- `g07-0057` *STATED* — The agency skill's outbound agent reads your list of businesses and finds one true detail about each one.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0052` — outbound agent
  ↳ *leads-to* `g07-0058`

- `g07-0061` *STATED* — During a sales call, the sales agent reads your live transcript and gives you one line to say next.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0052` — sales agent

- `g07-0063` *STATED* — Once you approve the proposal, the workflow agent builds the automation with a README and a test that proves it works.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0052` — workflow agent
  ↳ *example-of* `g07-0297` — builds only after you approve

- `g07-0064` *STATED* — The agency skill's customer service agent sorts your client emails and drafts every reply in your voice.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0052` — customer service agent

- `g07-0065` *STATED* — The customer service agent puts anything that needs a decision or money at the top.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0052` — customer service agent
  ↳ *qualifies* `g07-0064`

- `g07-0066` *STATED* — The agency skill's night shift works through a to-do list of jobs for the other four agents while your computer stays on.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0052` — night shift
  ↳ *leads-to* `g07-0067`
  ↳ *example-of* `g07-0056`
  ↳ *evidence-for* `g20-0288`
  ↳ *contrast* `r04-0158` — /agency night shift runs 'while your computer stays on' vs night crew runs on Anthropic's cloud with the laptop closed

- `g07-0070` *STATED* — The agency skill has a one-time setup ('Set it up once') before you run the agents (details email-gated).
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0073`
  ↳ *leads-to* `g07-0071`

- `g07-0071` *STATED* — Alex's agency guide lists the first commands to run ('Then run the agents'; command names email-gated).
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0073`

- `g07-0109` *STATED* — The Haiku helper is a small helper agent that runs on Haiku, which is now Haiku 5.5 in Claude Code.
  — [g-make-claude-code-limit-last-longer-haiku-5-5-helper](https://chen.media/guides/make-claude-code-limit-last-longer-haiku-5-5-helper)
  ↳ *part-of* `g07-0104`
  ↳ *part-of* `g07-0113`
  ↳ *depends-on* `g07-0091` — helper now runs Haiku 5.5
  ↳ *example-of* `g03-0015`

- `g07-0142` *STATED* — When you type /brain-grade, it tells you what it is about to read and asks once before reading.
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *part-of* `g07-0137`
  ↳ *leads-to* `g07-0147`
  ↳ *example-of* `g07-0297`

- `g07-0147` *STATED* — A small script in /brain-grade collects your messages from your past Claude Code chats into one evidence file.
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *part-of* `g07-0137`
  ↳ *leads-to* `g07-0149`

- `g07-0149` *STATED* — In /brain-grade, five Claudes start at the same time and judge you alone, each grading a different kind of smart.
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *part-of* `g07-0137`
  ↳ *leads-to* `g07-0151`
  ↳ *example-of* `g07-0295`

- `g07-0150` *STATED* — None of the five /brain-grade judges sees the others' answers.
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *part-of* `g07-0137`
  ↳ *qualifies* `g07-0149`
  ↳ *example-of* `g07-0295`
  ↳ *evidence-for* `r01-0016`

- `g07-0151` *STATED* — Each /brain-grade judge gives a score out of 100 and says where it came from.
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *part-of* `g07-0137`
  ↳ *leads-to* `g07-0155`

- `g07-0155` *STATED* — A sixth Claude, the /brain-grade coach, reads all five judgments and lists the three habits that cost you the most, each with the quote that proves it and the exact fix.
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *part-of* `g07-0137`
  ↳ *leads-to* `g07-0156`
  ↳ *defines* `g07-0139`
  ↳ *example-of* `g09-0246`

- `g07-0185` *STATED* — You give a Claude Code project a goal, and it splits the work into threads that all run at the same time.
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`
  ↳ *part-of* `g07-0182`
  ↳ *because* `g07-0200` — parallel threads multiply usage
  ↳ *contrast* `g07-0056` — Anthropic's native parallel threads vs Alex's skill-based agent handoff

- `g07-0198` *STATED* — Set a Claude Code project up before you send it a big batch of work ('Step 4: set it up before you send a big batch'; email-gated).
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`
  ↳ *leads-to* `g07-0199`

- `g07-0199` *STATED* — Alex's Projects guide gives the first messages to send a project ('Step 5: send it real work'; 3 prompts, email-gated).
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`
  ↳ *leads-to* `g07-0200`

- `g07-0252` *STATED* — In /linkedin-roast, five Claudes start at the same time and each reads your profile alone, as someone different.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *leads-to* `g07-0254`
  ↳ *example-of* `g07-0295`

- `g07-0253` *STATED* — None of the /linkedin-roast reviewers sees the others' answers, so nobody goes easy on you.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *qualifies* `g07-0252`
  ↳ *evidence-for* `g07-0296` — so nobody goes easy on you
  ↳ *evidence-for* `r03-0155`
  ↳ *evidence-for* `r01-0016`

- `g07-0254` *STATED* — Each /linkedin-roast reviewer roasts your headline and your About section and picks your three weakest bullets.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *leads-to* `g07-0258`

- `g07-0256` *STATED* — Each /linkedin-roast reviewer gives a score out of 10 and names the one fix it would make first.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *part-of* `g07-0254`
  ↳ *contrast* `g07-0151` — out of 10 vs out of 100
  ↳ *evidence-for* `r03-0218`

- `g07-0258` *STATED* — /linkedin-roast shows you the five roasts plus a short list of what all five reviewers agree on.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *leads-to* `g07-0248`
  ↳ *example-of* `g07-0295` — agreement-list aggregation
  ↳ *evidence-for* `r03-0156`

- `g07-0295` *CORE* — Alex's multi-Claude panel pattern: N Claudes start at the same time, each judges alone without seeing the others, every claim must quote the exact evidence, and a final step aggregates (a coach or an agreement list).
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill) [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *enables* `g07-0296`

- `g08-0036` *STATED* — /hiring-panel step 1: type /hiring-panel plus your resume (a file or pasted text), plus the job posting if you have one.
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill)
  ↳ *part-of* `g08-0028`
  ↳ *leads-to* `g08-0037`
  ↳ *example-of* `g08-0260`

- `g08-0037` *STATED* — /hiring-panel step 2: one Claude plays the automated system that decides whether a real human should even see your resume.
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill)
  ↳ *part-of* `g08-0028`

- `g08-0039` *STATED* — The /hiring-panel automated screen answers PASS or REJECT, with the resume lines that decided it.
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill)
  ↳ *part-of* `g08-0037`
  ↳ *evidence-for* `r01-0121`

- `g08-0040` *STATED* — /hiring-panel step 3: a second Claude plays the hiring manager who decides whether you get the interview, and says what decided it in the first ten seconds.
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill)
  ↳ *part-of* `g08-0028`
  ↳ *evidence-for* `r01-0127`

- `g08-0041` *STATED* — /hiring-panel step 4: five more Claudes start at the same time and read the resume alone, each as someone different: the hiring manager, another applicant for the same job, the CEO, the recruiter with 30 seconds and the teammate you would sit next to.
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill)
  ↳ *part-of* `g08-0028`
  ↳ *leads-to* `g08-0043`
  ↳ *evidence-for* `r01-0128`

- `g08-0042` *STATED* — In /hiring-panel none of the five parallel readers sees the others' notes, keeping each judgement independent.
  > “None of them sees the others' notes.”
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill)
  ↳ *qualifies* `g08-0041`
  ↳ *example-of* `g08-0251`
  ↳ *evidence-for* `r01-0129`
  ↳ *evidence-for* `r01-0016`

- `g08-0043` *STATED* — /hiring-panel step 5: all seven answers are merged into one numbered list of mistakes, worst first, with the resume line each one is about.
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill)
  ↳ *part-of* `g08-0028`
  ↳ *example-of* `g08-0251`
  ↳ *example-of* `g09-0246`

- `g08-0044` *STATED* — After rebuilding the resume, /hiring-panel runs the automated screen once more so you see before and after.
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill)
  ↳ *part-of* `g08-0030`
  ↳ *depends-on* `g08-0037` — re-runs the same automated screen
  ↳ *example-of* `g04-0249`

- `g08-0078` *STATED* — You type /heist and get a report of every way in the crew found.
  — [g-give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes](https://chen.media/guides/give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes)
  ↳ *part-of* `g08-0073`
  ↳ *example-of* `g08-0260`

- `g08-0079` *STATED* — The /heist scout maps your app: the routes, the login, the password reset, the database calls and the places that use secrets.
  — [g-give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes](https://chen.media/guides/give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes)
  ↳ *part-of* `g08-0073`
  ↳ *leads-to* `g08-0080`
  ↳ *qualifies* `y02-0046`

- `g08-0080` *STATED* — In /heist, three attackers each plan their own separate break-in.
  — [g-give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes](https://chen.media/guides/give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes)
  ↳ *part-of* `g08-0073`
  ↳ *leads-to* `g08-0084`

- `g08-0081` *STATED* — The /heist code attacker goes after your code; the classic trick of typing SQL into a login box is one thing it looks for.
  — [g-give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes](https://chen.media/guides/give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes)
  ↳ *part-of* `g08-0080`

- `g08-0082` *STATED* — The /heist users attacker goes after your users: password reset links, sessions and trust in an email link.
  — [g-give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes](https://chen.media/guides/give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes)
  ↳ *part-of* `g08-0080`

- `g08-0083` *STATED* — The /heist data attacker pretends to be an ordinary user and tries to open other people's data.
  — [g-give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes](https://chen.media/guides/give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes)
  ↳ *part-of* `g08-0080`

- `g08-0084` *STATED* — The /heist mastermind reads all three attack reports and tries to chain the holes together to find which combination gets an attacker the furthest.
  — [g-give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes](https://chen.media/guides/give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes)
  ↳ *part-of* `g08-0073`
  ↳ *leads-to* `g08-0085`
  ↳ *example-of* `g08-0251`
  ↳ *example-of* `g09-0246`

- `g08-0085` *STATED* — The /heist report gives the best break-in path, every hole with where it is and how to fix it, and the one change to make first.
  — [g-give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes](https://chen.media/guides/give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes)
  ↳ *example-of* `g09-0248`

- `g08-0098` *STATED* — You install The Agency once, then call its specialist agents by name.
  > “You install them once, then call them by name.”
  — [g-run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents](https://chen.media/guides/run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents)
  ↳ *part-of* `g08-0089`
  ↳ *part-of* `g15-0113`

- `g08-0164` *STATED* — Replica's spy (recon) skill reverse engineers the target app: its screens, its flows, its components and the data behind them.
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *part-of* `g08-0156`
  ↳ *leads-to* `g08-0165`
  ↳ *evidence-for* `y02-0077`
  ↳ *part-of* `y02-0075`

- `g08-0165` *STATED* — Replica's builder (build) skill rebuilds the app screen by screen from the recon map.
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *part-of* `g08-0156`
  ↳ *leads-to* `g08-0166`
  ↳ *evidence-for* `y02-0078`

- `g08-0166` *STATED* — Replica's inspector (test) skill clicks through every flow, finds the bugs and logs them until the serious ones are gone.
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *part-of* `g08-0156`
  ↳ *evidence-for* `y02-0079`

- `g08-0209` *STATED* — Alex recommends putting an Agent Office and the Claude Code notification setting together (section 'Put them together', body locked).
  — [g-see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office](https://chen.media/guides/see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office)
  ↳ *part-of* `g08-0204`

- `g08-0225` *STATED* — /rival step 1: type /rival and your idea.
  — [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill)
  ↳ *part-of* `g08-0220`
  ↳ *leads-to* `g08-0226`
  ↳ *example-of* `g08-0260`

- `g08-0226` *STATED* — /rival step 2: five rival Claudes start at the same time, each playing one enemy and writing a specific plan to take your customers.
  — [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill)
  ↳ *part-of* `g08-0220`
  ↳ *leads-to* `g08-0232`

- `g08-0232` *STATED* — /rival step 3: a judge Claude reads all five plans, shuffled and without names, and picks the one that would hurt you most.
  — [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill)
  ↳ *part-of* `g08-0220`
  ↳ *leads-to* `g08-0233`
  ↳ *example-of* `g08-0251`
  ↳ *evidence-for* `r01-0016`
  ↳ *example-of* `g09-0246`

- `g08-0250` *CORE* — Alex's recurring fix for Claude's agreeableness is a skill that makes Claude role-play adversaries whose job is to find what is wrong: rejecting recruiters (/hiring-panel), thieves (/heist), rival companies (/rival) and a jester (/jester).
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill) [g-give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes](https://chen.media/guides/give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes) [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill) [g-give-claude-a-jester-that-tells-you-the-brutal-truth-set-up-jester-in-2-minutes](https://chen.media/guides/give-claude-a-jester-that-tells-you-the-brutal-truth-set-up-jester-in-2-minutes)
  ↳ *because* `g08-0249`

- `g08-0251` *CORE* — Alex's multi-Claude skills run several role-played Claudes at the same time, keep them independent (no shared notes; plans shuffled and unnamed), then a merge or judge step ranks the findings worst first.
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill) [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill) [g-give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes](https://chen.media/guides/give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes)
  ↳ *evidence-for* `g07-0295`

- `g09-0018` *STATED* — In the Boardroom each executive thinks on its own first, then the board argues it out, with a mentor whose job is to poke holes.
  > “each thinking on its own first, then arguing it out, with a mentor whose job is to poke holes”
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives)
  ↳ *part-of* `g09-0017`

- `g09-0022` *STATED* — Boardroom step 1: you bring the idea, or any decision: a launch, a price, a hire, a pivot.
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives)
  ↳ *part-of* `g09-0018`
  ↳ *leads-to* `g09-0023`

- `g09-0023` *STATED* — Boardroom step 2: only the right executives for the topic are called in, from a roster of CEO, CFO, marketing head, sales head, product, operations, security, people and more.
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives)
  ↳ *qualifies* `g09-0021` — only the executives relevant to the topic are seated
  ↳ *part-of* `g09-0018`

- `g09-0024` *STATED* — Boardroom step 3: each executive thinks alone first, without seeing the others' answers, so nobody just follows the room.
  > “Each one thinks alone first, without seeing the others' answers, so nobody just follows the room.”
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives)
  ↳ *part-of* `g09-0018`
  ↳ *leads-to* `g09-0026`
  ↳ *example-of* `g09-0246`
  ↳ *evidence-for* `r01-0016`

- `g09-0026` *STATED* — Boardroom step 4: a mentor reads every answer at once and goes looking for trouble: where the board agreed too easily, what nobody checked, and the risk no one mentioned.
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives)
  ↳ *part-of* `g09-0018`
  ↳ *leads-to* `g09-0027`
  ↳ *example-of* `g09-0246`

- `g09-0027` *STATED* — Boardroom step 5: you get a board memo with each executive's view, where they agree, where they don't, the uncomfortable truth, and what to do next.
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives)
  ↳ *part-of* `g09-0018`

- `g09-0042` *STATED* — Every night a second Claude, the investigator, goes over the corrections inbox: what went wrong, why it happened, and what to do instead.
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *part-of* `g09-0031`
  ↳ *evidence-for* `r03-0009`

- `g09-0043` *STATED* — The lessons investigator throws out inbox messages that weren't really mistakes.
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *part-of* `g09-0042`
  ↳ *evidence-for* `r03-0104`

- `g09-0048` *STATED* — The lessons guide's 'Make it run every night' step schedules the investigator review to run automatically each night.
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *enables* `g09-0042`
  ↳ *depends-on* `g09-0215` — a nightly run can be scheduled as a Claude Code routine (inferred)
  ↳ *evidence-for* `r03-0035`

- `g09-0113` *STATED* — Launch poll step 1: Claude reads your project and writes a mission file: what's launching, how to run your tests, what changed, and anything you tell it, like how many users you expect or your budget for running costs.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *part-of* `g09-0110`
  ↳ *leads-to* `g09-0114`

- `g09-0114` *STATED* — Launch poll step 2: eight flight controllers check one part each: Tests, Security, Database, Speed, Cost, Users, Recovery and Rules.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *part-of* `g09-0110`
  ↳ *evidence-for* `r01-0032`

- `g09-0115` *STATED* — Launch-poll Tests controller: runs your tests and build.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *part-of* `g09-0114`

- `g09-0116` *STATED* — Launch-poll Security controller: hunts for leaked keys and passwords and pages anyone can reach.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *part-of* `g09-0114`

- `g09-0117` *STATED* — Launch-poll Database controller: checks migrations, backups and who can read whose data.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *part-of* `g09-0114`

- `g09-0118` *STATED* — Launch-poll Speed controller: checks for pages that get slower with every user.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *part-of* `g09-0114`

- `g09-0119` *STATED* — Launch-poll Cost controller: checks the actual cost of every paid service your code calls, and whether a stranger could run up your bill.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *part-of* `g09-0114`

- `g09-0120` *STATED* — Launch-poll Users controller: walks sign-up, sign-in and payment.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *part-of* `g09-0114`

- `g09-0121` *STATED* — Launch-poll Recovery controller: checks you can see errors and roll back.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *part-of* `g09-0114`

- `g09-0122` *STATED* — Launch-poll Rules controller: checks privacy policies, data deletion and promises your code doesn't keep.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *part-of* `g09-0114`

- `g09-0123` *STATED* — Launch poll step 3: each controller answers GO or NO-GO with its evidence: the file and line, or the command and what it printed.
  > “Each one answers GO or NO-GO with its evidence: the file and line, or the command and what it printed.”
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *part-of* `g09-0110`
  ↳ *contrast* `g09-0109` — evidence-backed calls replace self-grading

- `g09-0124` *STATED* — In the launch poll no controller sees another's call.
  > “No controller sees another's call.”
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *qualifies* `g09-0123`
  ↳ *example-of* `g09-0246`
  ↳ *evidence-for* `r02-0123`
  ↳ *evidence-for* `r01-0016`

- `g09-0125` *STATED* — Launch poll step 4: if even one controller says NO-GO, your app doesn't launch.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *part-of* `g09-0110`
  ↳ *evidence-for* `r02-0133`

- `g09-0126` *STATED* — In the launch poll a flight director Claude writes up the holds, the fixes in the order to make them, and what to watch in the first week.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *part-of* `g09-0125`
  ↳ *leads-to* `g09-0127`
  ↳ *example-of* `g09-0246`
  ↳ *evidence-for* `r02-0134`

- `g09-0129` *STATED* — Run the launch poll as a gate before you launch ('Run it before you launch').
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *qualifies* `g09-0110`

- `g09-0151` *STATED* — Shark step 1: five sharks read your pitch, and each writes its biggest worry and its three hardest questions.
  — [g-pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill](https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill)
  ↳ *part-of* `g09-0147`
  ↳ *evidence-for* `r04-0210`

- `g09-0153` *STATED* — Shark step 2: a founder Claude answers every question, using only what you told it.
  > “A founder Claude answers every question, using only what you told it.”
  — [g-pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill](https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill)
  ↳ *part-of* `g09-0147`
  ↳ *evidence-for* `r04-0212`

- `g09-0154` *STATED* — When your pitch doesn't have the answer, the founder Claude says so, and that question goes on your homework list.
  — [g-pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill](https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill)
  ↳ *part-of* `g09-0153`
  ↳ *leads-to* `g09-0157`

- `g09-0155` *STATED* — Shark step 3: each shark decides IN or OUT, with a practice offer like '$50,000 for 10%', one line of why, and the one thing that would change its mind.
  > “a practice offer like "$50,000 for 10%"”
  — [g-pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill](https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill)
  ↳ *part-of* `g09-0147`
  ↳ *leads-to* `g09-0156`
  ↳ *evidence-for* `r04-0213`

- `g09-0165` *STATED* — Court step 1: a prosecutor Claude builds the strongest honest case that your idea fails as described.
  — [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill)
  ↳ *part-of* `g09-0162`
  ↳ *contrast* `g09-0166`
  ↳ *evidence-for* `r01-0162`

- `g09-0166` *STATED* — Court step 2: a defense Claude builds the strongest honest case that your idea works.
  — [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill)
  ↳ *part-of* `g09-0162`
  ↳ *evidence-for* `r01-0163`

- `g09-0167` *STATED* — In the court skill the prosecutor and the defense each answer the other's points before the jury votes.
  > “Then each side answers the other's points.”
  — [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill)
  ↳ *part-of* `g09-0166`
  ↳ *evidence-for* `r01-0164`

- `g09-0168` *STATED* — Court step 3: twelve jurors read the whole record and each votes guilty or not guilty on their own.
  — [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill)
  ↳ *part-of* `g09-0162`
  ↳ *evidence-for* `r01-0165`

- `g09-0171` *STATED* — Court step 4: a judge Claude reads the verdict, the charges that stuck, what the defense got right, and the conditions for acquittal.
  — [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill)
  ↳ *part-of* `g09-0162`
  ↳ *leads-to* `g09-0173`
  ↳ *evidence-for* `r01-0168`

- `g09-0216` *STATED* — The night-crew skill sets up three routines with one job each.
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)
  ↳ *part-of* `g09-0213`
  ↳ *depends-on* `g09-0215`

- `g09-0217` *STATED* — The night crew's routines share one set of orders: what your app is, what to build next, who your customers are, and the rules they can't break.
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)
  ↳ *part-of* `g09-0213`
  ↳ *evidence-for* `r04-0093`

- `g09-0218` *STATED* — Night-crew builder: takes the next item off your backlog, like a signup page or a pricing page, builds it with tests, checks it, and opens a pull request.
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)
  ↳ *part-of* `g09-0216`
  ↳ *evidence-for* `r04-0090`

- `g09-0222` *STATED* — Night-crew tracker: goes last, runs your tests and build, checks the builder's work, and writes up what's working, what's broken, and the three things it would build next.
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)
  ↳ *part-of* `g09-0216`
  ↳ *depends-on* `g09-0218`
  ↳ *leads-to* `g09-0223`
  ↳ *evidence-for* `r04-0092`

- `g09-0246` *CORE* — Alex's panel skills make every member judge alone without seeing the others, then hand all answers to one separate synthesiser Claude (mentor, judge or flight director).
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives) [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill) [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *because* `g09-0245`

- `g10-0075` *STATED* — Login rule 5: keep your own AI agents on a leash.
  — [g-openai-agents-hacked-hugging-face-5-login-rules](https://chen.media/guides/openai-agents-hacked-hugging-face-5-login-rules)
  ↳ *part-of* `g10-0069`
  ↳ *qualifies* `g10-0266`
  ↳ *evidence-for* `r04-0164`

- `g10-0268` *INFERRED* — Before an overnight Claude run, Alex's guides call for two preparations: the keep-going paragraph so Claude doesn't stop early, and the walk-away memory-leak checklist so the Mac doesn't freeze.
  — [g-claude-quits-long-jobs-halfway-the-keep-going-paragraph](https://chen.media/guides/claude-quits-long-jobs-halfway-the-keep-going-paragraph) [g-claude-app-memory-leak-freeze-checklist](https://chen.media/guides/claude-app-memory-leak-freeze-checklist)
  ↳ *qualifies* `g20-0288`

- `g11-0062` *STATED* — Tournament step 1: every Claude gets your question word for word, plus its own strategy card.
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *part-of* `g11-0057` — tournament steps
  ↳ *leads-to* `g11-0068`
  ↳ *evidence-for* `g20-0094`

- `g11-0068` *STATED* — Tournament step 2: Claudes pair off and each attacks the other's answer: what's wrong with it, what it missed, the exact case that breaks it.
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *part-of* `g11-0057` — tournament steps
  ↳ *leads-to* `g11-0070`

- `g11-0070` *STATED* — Tournament step 3: each side answers the attacks it took, concedes or pushes back, and rewrites its answer.
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *part-of* `g11-0057` — tournament steps
  ↳ *leads-to* `g11-0071`

- `g11-0071` *STATED* — Tournament step 4: a separate judge checks every attack and scores both answers out of 100.
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *part-of* `g11-0057` — tournament steps
  ↳ *leads-to* `g11-0074`
  ↳ *evidence-for* `g20-0284`
  ↳ *example-of* `g09-0246`

- `g11-0074` *STATED* — Tournament step 5: the loser is out and the winner takes its improved answer into the next round.
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *part-of* `g11-0057` — tournament steps

- `g11-0137` *STATED* — Alex's overnight bug-fix setup: a bug report comes in on GitHub, Codex finds the broken code and writes the fix on GitHub's machines, and you wake up to a pull request waiting for your approval.
  — [g-let-chatgpt-fix-your-apps-bugs-while-you-sleep](https://chen.media/guides/let-chatgpt-fix-your-apps-bugs-while-you-sleep)
  ↳ *because* `g11-0136` — bringing OpenAI's internal practice to your own app
  ↳ *analogy-for* `r04-0087`

- `g11-0139` *STATED* — In the overnight flow the agent reads the report, finds the broken code, writes the fix and hands you a pull request; you review it over coffee and click approve.
  — [g-let-chatgpt-fix-your-apps-bugs-while-you-sleep](https://chen.media/guides/let-chatgpt-fix-your-apps-bugs-while-you-sleep)
  ↳ *part-of* `g11-0137`
  ↳ *analogy-for* `r04-0090`

- `g11-0147` *STATED* — Step 1 of the overnight bug-fix setup is two settings on GitHub.
  — [g-let-chatgpt-fix-your-apps-bugs-while-you-sleep](https://chen.media/guides/let-chatgpt-fix-your-apps-bugs-while-you-sleep)
  ↳ *part-of* `g11-0137`
  ↳ *leads-to* `g11-0148`

- `g11-0148` *STATED* — Step 2 of the overnight bug-fix setup is one setup prompt; Step 3 is testing it.
  — [g-let-chatgpt-fix-your-apps-bugs-while-you-sleep](https://chen.media/guides/let-chatgpt-fix-your-apps-bugs-while-you-sleep)
  ↳ *part-of* `g11-0137`

- `g11-0149` *STATED* — Alex's no-workflow alternative to the GitHub setup is a ChatGPT dot.
  — [g-let-chatgpt-fix-your-apps-bugs-while-you-sleep](https://chen.media/guides/let-chatgpt-fix-your-apps-bugs-while-you-sleep)
  ↳ *example-of* `g11-0135`
  ↳ *contrast* `g11-0137`

- `g11-0152` *STATED* — You give a dot a goal, it gets its own computer in the cloud, keeps working between your conversations even while you're asleep, then comes back with the result or a question only you can answer.
  — [g-get-your-own-chatgpt-dot](https://chen.media/guides/get-your-own-chatgpt-dot)
  ↳ *defines* `g11-0135`
  ↳ *evidence-for* `g20-0288`

- `g11-0162` *STATED* — Alex's dot setup is four steps: create your dot, connect what it should work with, give it its first jobs, and set its rules.
  — [g-get-your-own-chatgpt-dot](https://chen.media/guides/get-your-own-chatgpt-dot)
  ↳ *part-of* `g11-0135`

- `g11-0163` *STATED* — Step 4 of the dot setup sets the rules that keep the always-on agent in check.
  — [g-get-your-own-chatgpt-dot](https://chen.media/guides/get-your-own-chatgpt-dot)
  ↳ *part-of* `g11-0162`
  ↳ *analogy-for* `g11-0141` — rules/approval gates on autonomous agents
  ↳ *qualifies* `r04-0164`

- `g12-0089` *STATED* — Guide section 'Run your own arena' explains running your own AI-model arena (body email-gated; 1 prompt to copy).
  — [g-the-ai-arena-where-models-fight-to-the-death-and-claude-wins-by-waiting](https://chen.media/guides/the-ai-arena-where-models-fight-to-the-death-and-claude-wins-by-waiting)
  ↳ *part-of* `g12-0070`

- `g12-0274` *STATED* — Polsia setup step 1: open Polsia and give it a goal (body email-gated).
  — [g-set-up-polsia-the-ai-co-founder-that-runs-your-business](https://chen.media/guides/set-up-polsia-the-ai-co-founder-that-runs-your-business)
  ↳ *part-of* `g12-0266`
  ↳ *leads-to* `g12-0275`

- `g12-0275` *STATED* — Polsia setup step 2: let the AI co-founder get to work (body email-gated).
  — [g-set-up-polsia-the-ai-co-founder-that-runs-your-business](https://chen.media/guides/set-up-polsia-the-ai-co-founder-that-runs-your-business)
  ↳ *part-of* `g12-0266`
  ↳ *leads-to* `g12-0276`

- `g12-0276` *STATED* — Polsia setup step 3: just check its progress (body email-gated).
  — [g-set-up-polsia-the-ai-co-founder-that-runs-your-business](https://chen.media/guides/set-up-polsia-the-ai-co-founder-that-runs-your-business)
  ↳ *part-of* `g12-0266`

- `g13-0251` *STATED* — SWARM Loop guide section 'Choose chat roles or actual subagents': the three reviewers can be roles in one chat or optional Claude Code subagents.
  — [g-swarm-loop-three-reviewers-guide](https://chen.media/guides/swarm-loop-three-reviewers-guide)
  ↳ *qualifies* `g13-0243`
  ↳ *qualifies* `y04-0046` — video says 'unleash three critic agents'; guide says the three can be roles in one chat or optional subagents

- `g13-0259` *STATED* — With The Delegation, start with one deliverable you can judge yourself, then expand the team once that first run makes sense.
  — [g-give-ai-agents-an-office-the-delegation](https://chen.media/guides/give-ai-agents-an-office-the-delegation)
  ↳ *part-of* `g13-0254`
  ↳ *evidence-for* `g20-0109`

- `g13-0261` *STATED* — Alex's Delegation guide includes Gemini setup, a copyable first project brief and a review checklist for your first AI team (3 prompts, 4 numbered steps).
  — [g-give-ai-agents-an-office-the-delegation](https://chen.media/guides/give-ai-agents-an-office-the-delegation)
  ↳ *part-of* `g13-0254`

- `g13-0262` *STATED* — Delegation guide section: 'Set up your first run'.
  — [g-give-ai-agents-an-office-the-delegation](https://chen.media/guides/give-ai-agents-an-office-the-delegation)
  ↳ *leads-to* `g13-0263`
  ↳ *part-of* `g13-0261`

- `g13-0263` *STATED* — Delegation guide section: 'Copy this first project brief'.
  — [g-give-ai-agents-an-office-the-delegation](https://chen.media/guides/give-ai-agents-an-office-the-delegation)
  ↳ *leads-to* `g13-0264`
  ↳ *part-of* `g13-0259`

- `g13-0264` *STATED* — Delegation guide section: 'Follow the work behind the animation'.
  — [g-give-ai-agents-an-office-the-delegation](https://chen.media/guides/give-ai-agents-an-office-the-delegation)
  ↳ *leads-to* `g13-0265`

- `g13-0265` *STATED* — Delegation guide section: 'Try a useful second pass'.
  — [g-give-ai-agents-an-office-the-delegation](https://chen.media/guides/give-ai-agents-an-office-the-delegation)

- `g13-0266` *STATED* — Delegation guide section: 'Optional: run it locally'.
  — [g-give-ai-agents-an-office-the-delegation](https://chen.media/guides/give-ai-agents-an-office-the-delegation)
  ↳ *qualifies* `g13-0254`

- `g13-0269` *STATED* — The SPLIT workflow: challenge the plan, choose a builder, then have the other provider inspect the finished changes.
  > “challenge the plan, choose a builder, then have the other provider inspect the finished changes”
  — [g-split-claude-and-codex-with-claudex-loop](https://chen.media/guides/split-claude-and-codex-with-claudex-loop)
  ↳ *part-of* `g13-0268`
  ↳ *evidence-for* `g06-0158`

- `g13-0271` *STATED* — Start Claudex Loop with one small feature and a result you can actually check.
  — [g-split-claude-and-codex-with-claudex-loop](https://chen.media/guides/split-claude-and-codex-with-claudex-loop)
  ↳ *qualifies* `g13-0268`
  ↳ *evidence-for* `g13-0259`

- `g13-0274` *STATED* — Choose the full Claudex Loop over Claudex Route when you want the complete plan-review-build-inspect workflow.
  — [g-split-claude-and-codex-with-claudex-loop](https://chen.media/guides/split-claude-and-codex-with-claudex-loop)
  ↳ *qualifies* `g13-0273`

- `g13-0278` *STATED* — Claudex Loop guide step: 'Review the plan before the build'.
  — [g-split-claude-and-codex-with-claudex-loop](https://chen.media/guides/split-claude-and-codex-with-claudex-loop)
  ↳ *leads-to* `g13-0279`
  ↳ *part-of* `g13-0269`

- `g13-0279` *STATED* — Claudex Loop guide step: 'Choose the builder, then inspect the result'.
  — [g-split-claude-and-codex-with-claudex-loop](https://chen.media/guides/split-claude-and-codex-with-claudex-loop)
  ↳ *leads-to* `g13-0280`

- `g13-0280` *STATED* — Claudex Loop guide step: 'Try one small change first'.
  — [g-split-claude-and-codex-with-claudex-loop](https://chen.media/guides/split-claude-and-codex-with-claudex-loop)
  ↳ *example-of* `g13-0271`

- `g14-0003` *STATED* — Alex's marketing workflow starts with four jobs, each with a clear deliverable: research, draft, review and publication preparation.
  > “Start with four jobs: research, draft, review and publication preparation.”
  — [g-marketing-agent-workflow-setup](https://chen.media/guides/marketing-agent-workflow-setup)
  ↳ *part-of* `g14-0001`
  ↳ *analogy-for* `g20-0197`

- `g14-0004` *STATED* — The four marketing-workflow stages can be run manually by passing the approved output of one stage into the next prompt.
  — [g-marketing-agent-workflow-setup](https://chen.media/guides/marketing-agent-workflow-setup)
  ↳ *qualifies* `g14-0003` — stages can be run by hand

- `g14-0012` *STATED* — The marketing workflow runs as four handoffs between its research, draft, review and publication-preparation stages.
  > “Run the four handoffs”
  — [g-marketing-agent-workflow-setup](https://chen.media/guides/marketing-agent-workflow-setup)
  ↳ *part-of* `g14-0001`
  ↳ *depends-on* `g14-0003`

- `g14-0039` *STATED* — Design a small decision-loop experiment to test a fast structured-decision model like Jev.
  > “Design a small decision loop”
  — [g-jev-doom-demo-explained](https://chen.media/guides/jev-doom-demo-explained)
  ↳ *part-of* `g14-0028`

- `g14-0040` *STATED* — When testing a real-time decision model, measure the whole loop, not only the model call.
  > “Measure the whole loop”
  — [g-jev-doom-demo-explained](https://chen.media/guides/jev-doom-demo-explained)
  ↳ *part-of* `g14-0028`
  ↳ *part-of* `g14-0039`

- `g14-0092` *STATED* — In the AI-Native SDLC, a human reviews the work at the relevant gates.
  > “A human reviews the work at the relevant gates.”
  — [g-intent-md-claude-project-setup](https://chen.media/guides/intent-md-claude-project-setup)
  ↳ *part-of* `g14-0089`
  ↳ *generalizes* `g14-0237` — human approval gate before build
  ↳ *example-of* `g09-0247`

- `g14-0255` *STATED* — Run /octo:setup inside the Claude Code session and follow its provider configuration steps.
  > “/octo:setup”
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *enables* `g14-0249`

- `g14-0258` *STATED* — Confirm the available Claude Octopus providers before your first council run.
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *because* `g14-0257`
  ↳ *leads-to* `g14-0259`

- `g14-0259` *STATED* — Make the Claude Octopus council decide something specific, not an open-ended question.
  > “Make the council decide something specific”
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *part-of* `g14-0241`
  ↳ *leads-to* `g14-0260`
  ↳ *contrast* `g14-0098`

- `g14-0260` *STATED* — Turn the Claude Octopus council's decision into a bounded build.
  > “Turn the decision into a bounded build”
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *part-of* `g14-0241`
  ↳ *leads-to* `g14-0261`

- `g14-0262` *STATED* — Give the Claude Octopus security pass a real boundary (a defined scope to check).
  > “Give the security pass a real boundary”
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *part-of* `g14-0241`

- `g15-0075` *STATED* — MetaGPT takes a standard operating procedure, the kind a real software company runs on, and hands each step to a different LLM role.
  — [g-metagpt-one-line-in-a-whole-software-company-out](https://chen.media/guides/metagpt-one-line-in-a-whole-software-company-out)
  ↳ *part-of* `g15-0072`
  ↳ *leads-to* `g15-0077`
  ↳ *evidence-for* `g20-0197`

- `g15-0078` *STATED* — MetaGPT can also be used as a library instead of a standalone tool (section 'Using it as a library instead', locked).
  — [g-metagpt-one-line-in-a-whole-software-company-out](https://chen.media/guides/metagpt-one-line-in-a-whole-software-company-out)
  ↳ *qualifies* `g15-0072`

- `g15-0080` *STATED* — In Munder Difflin you brief one agent and it hands parts of the work to the others while you watch it happen.
  — [g-munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents](https://chen.media/guides/munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents)
  ↳ *part-of* `g15-0079`
  ↳ *example-of* `g15-0183`

- `g15-0088` *STATED* — Run Munder Difflin pointed at a real repository, with a real briefing, and with the permission gate left switched on.
  — [g-munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents](https://chen.media/guides/munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents)

- `g15-0090` *STATED* — Munder Difflin can be run when you are not there (section 'Running it when you are not there', locked), and the guide also covers who is actually in charge during delegation.
  — [g-munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents](https://chen.media/guides/munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents)
  ↳ *depends-on* `g15-0089`
  ↳ *qualifies* `g15-0080`

- `g15-0092` *STATED* — The Judge Loop puts Claude's own output on trial: instead of you reading the output and hunting for what is wrong, you make the model do that job, adversarially, before it reaches you.
  — [g-the-judge-loop-three-lines-that-put-claude-s-output-on-trial](https://chen.media/guides/the-judge-loop-three-lines-that-put-claude-s-output-on-trial)
  ↳ *example-of* `g15-0181`
  ↳ *evidence-for* `g19-0197`

- `g15-0111` *STATED* — There are two ways to call a wshobson/agents agent, and each is right in different situations (section locked).
  — [g-the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build](https://chen.media/guides/the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build)
  ↳ *part-of* `g15-0105`

- `g15-0112` *STATED* — Put four specialized wshobson/agents agents on one build instead of one generalist session (section 'Putting four agents on one build', locked).
  — [g-the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build](https://chen.media/guides/the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build)
  ↳ *depends-on* `g15-0105`
  ↳ *contrast* `g15-0103` — four specialists instead of one generalist session
  ↳ *evidence-for* `g20-0197`

- `g15-0165` *STATED* — Boss-loop prompt in three parts: hand Claude the task; tell it to spawn a team of worker sub-agents to do the building; appoint one agent as a strict boss whose only job is to tear the work apart.
  — [g-the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer](https://chen.media/guides/the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer)
  ↳ *defines* `g15-0164`
  ↳ *leads-to* `g15-0167`
  ↳ *evidence-for* `g19-0197`

- `g15-0167` *STATED* — In the boss loop the workers build, the boss rejects, they rebuild, and the loop only ends when the boss scores the work as good.
  — [g-the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer](https://chen.media/guides/the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer)
  ↳ *evidence-for* `g19-0198`

- `g15-0174` *STATED* — The boss-loop guide specifies what the boss should actually be checking, how to run it without surprises, and when not to use it (locked).
  — [g-the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer](https://chen.media/guides/the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer)
  ↳ *qualifies* `g15-0165`

- `g16-0156` *STATED* — The Gauntlet Loop is a three line prompt that makes Claude build, judge and rebuild its own work until a separate critic agent runs out of complaints.
  > “The three line prompt that makes Claude build, judge and rebuild its own work until a separate critic agent runs out of complaints”
  — [g-the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work](https://chen.media/guides/the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work)
  ↳ *example-of* `g16-0001`
  ↳ *evidence-for* `g19-0198`

- `g16-0159` *STATED* — In the Gauntlet Loop the agents argue until the work clears a bar you defined at the start.
  > “until the work clears a bar you defined at the start”
  — [g-the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work](https://chen.media/guides/the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work)
  ↳ *part-of* `g16-0158`

- `g16-0168` *STATED* — Use a checklist before you press go on a Gauntlet Loop.
  > “A checklist before you press go”
  — [g-the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work](https://chen.media/guides/the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work)
  ↳ *part-of* `g16-0156`

- `g16-0188` *STATED* — Tip 13 (expert): automate the job you keep redoing.
  > “13. Automate the job you keep redoing”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *part-of* `g16-0175`
  ↳ *part-of* `g16-0015`
  ↳ *evidence-for* `g22-0069`

- `g16-0303` *STATED* — He gives the order he would install Ruflo's parts in, and what each part is for.
  > “The order I would install them in”
  — [g-ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm](https://chen.media/guides/ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm)
  ↳ *leads-to* `g16-0302`
  ↳ *example-of* `g16-0007`

- `g17-0101` *STATED* — Point Claude SEO at a URL and it fans out across the site, running sub-skills in parallel for technical SEO, content quality, Schema.org markup, AI search visibility, local search and more.
  > “You point it at a URL and it fans out across the site, running sub skills in parallel”
  — [g-install-25-seo-skills-and-18-specialist-agents-into-claude-code](https://chen.media/guides/install-25-seo-skills-and-18-specialist-agents-into-claude-code)
  ↳ *part-of* `g17-0099`
  ↳ *part-of* `g02-0151`

- `g17-0265` *STATED* — Start The Agency with five agents rather than all 286.
  > “Pick your first five”
  — [g-286-specialist-ai-agents-free-inside-claude-code](https://chen.media/guides/286-specialist-ai-agents-free-inside-claude-code)
  ↳ *leads-to* `g17-0264`
  ↳ *evidence-for* `g15-0120`
  ↳ *evidence-for* `g15-0186`
  ↳ *evidence-for* `g13-0259`

- `g17-0312` *INFERRED* — Recurring Alex Chen principle: sequence work by dependency, doing first the thing everything else depends on (install production skills before outbound ones; Claude SEO orders fixes by dependency).
  — [g-seven-free-claude-skills-that-cover-a-marketing-department](https://chen.media/guides/seven-free-claude-skills-that-cover-a-marketing-department) [g-install-25-seo-skills-and-18-specialist-agents-into-claude-code](https://chen.media/guides/install-25-seo-skills-and-18-specialist-agents-into-claude-code)
  ↳ *generalizes* `g17-0008`

- `g18-0013` *STATED* — The ECC guide includes a 'Your First Week' section on what to do with the harness after installing it.
  — [g-67-agents-281-skills-and-94-commands-in-one-install](https://chen.media/guides/67-agents-281-skills-and-94-commands-in-one-install)
  ↳ *part-of* `g18-0001`

- `g18-0021` *STATED* — Rowboat can be run yourself; the guide has a 'Running it yourself' section with numbered steps (9 in the guide overall).
  — [g-the-open-source-agent-tool-two-yc-founders-gave-away](https://chen.media/guides/the-open-source-agent-tool-two-yc-founders-gave-away)
  ↳ *part-of* `g18-0016`

- `g18-0208` *STATED* — Using a ready-made n8n workflow: download one file, import it, connect your accounts, and it runs.
  — [g-280-ready-made-n8n-automations-you-do-not-have-to-build](https://chen.media/guides/280-ready-made-n8n-automations-you-do-not-have-to-build)
  ↳ *part-of* `g18-0206`

- `g18-0211` *STATED* — Alex names five n8n workflows worth importing first.
  — [g-280-ready-made-n8n-automations-you-do-not-have-to-build](https://chen.media/guides/280-ready-made-n8n-automations-you-do-not-have-to-build)
  ↳ *part-of* `g18-0206`

- `g18-0218` *STATED* — The 268-role repo installs in under a minute, and the guide lists where it works.
  — [g-268-expert-roles-in-one-repo-free](https://chen.media/guides/268-expert-roles-in-one-repo-free)
  ↳ *part-of* `g18-0215`

- `g18-0252` *STATED* — CUT sub-agent definitions that duplicate each other: two agents with the same job means neither is trusted.
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *part-of* `g18-0245`
  ↳ *qualifies* `g18-0286` — stacking several agent rosters risks duplicate sub-agents
  ↳ *qualifies* `g20-0285`

- `g19-0062` *STATED* — Split one overloaded Claude into seven single-job Claude Code subagents.
  > “Split it into seven single-job Claude Code subagents”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *part-of* `g19-0072`

- `g19-0063` *STATED* — Run the seven station subagents in a strict order.
  > “run them in a strict order”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *part-of* `g19-0072`

- `g19-0064` *CORE* — Refuse to move the seven-station line forward until each station approves the work before it.
  > “refuse to move forward until each station approves the work before it”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *part-of* `g19-0072`
  ↳ *part-of* `g19-0076`
  ↳ *evidence-for* `g20-0213`

- `g19-0073` *STATED* — Give each station subagent a narrow job and a narrow toolset.
  > “giving each subagent a narrow job and a narrow toolset”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *enables* `g19-0072`
  ↳ *depends-on* `g19-0067` — scoped tool list
  ↳ *evidence-for* `g20-0285`

- `g19-0074` *STATED* — Give the main Claude Code session an orchestration prompt that enforces the station order and the approval gate.
  > “giving the main session an orchestration prompt that enforces the order and the gate”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *enables* `g19-0072`

- `g19-0078` *STATED* — The seven-station guide includes 'How to tell it is actually running as a line', a check that the gate is really enforced.
  > “How to tell it is actually running as a line”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *part-of* `g19-0060`
  ↳ *qualifies* `g19-0064`

- `g19-0118` *STATED* — Each lead-machine prompt writes a file the next one reads.
  > “Each one writes a file the next one reads.”
  — [g-turn-one-line-into-hundreds-of-verified-leads-for-nothing](https://chen.media/guides/turn-one-line-into-hundreds-of-verified-leads-for-nothing)
  ↳ *qualifies* `g19-0117`
  ↳ *analogy-for* `g19-0072` — stations hand work down the line via files
  ↳ *part-of* `g20-0285`

- `g19-0197` *CORE* — Put one agent on the team whose only job is to attack the work: hunt every weak spot, every hole, every lazy shortcut; Alex calls this the move nobody makes.
  > “the move nobody makes is putting one agent on that team whose only job is to attack the work”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)
  ↳ *part-of* `g19-0196`
  ↳ *analogy-for* `g19-0064` — attacker gate vs station approval gate

- `g19-0198` *STATED* — The attacker agent throws the work back to be rebuilt until it survives.
  > “throw it back to be rebuilt until it survives”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)
  ↳ *part-of* `g19-0197`

- `g19-0203` *STATED* — Agent Graph prompt 1 is pasted once to set up the graph.
  > “Paste This Once to Set Up the Graph”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)
  ↳ *part-of* `g19-0192`
  ↳ *leads-to* `g19-0202`

- `g19-0204` *STATED* — Agent Graph step 'Plan and build the first version' is pasted with your task: 'Task: [describe what you want in one or two lines]'.
  > “Task: [describe What you Want in One or Two Lines]”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)
  ↳ *part-of* `g19-0192`

- `g19-0206` *STATED* — Agent Graph step 'Unleash the attacker' uses a dedicated prompt to attack the work.
  > “Paste This to Attack the Work”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)
  ↳ *part-of* `g19-0192`

- `g19-0208` *STATED* — Agent Graph step 'Rebuild until it survives' uses a prompt that runs the attack-rebuild loop.
  > “Paste This to Run the Loop”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)
  ↳ *part-of* `g19-0192`
  ↳ *defines* `g19-0198`

- `g19-0209` *STATED* — Agent Graph step 'Build it once, reuse it forever' uses a prompt that makes the graph permanent.
  > “Paste This to Make It Permanent”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)
  ↳ *part-of* `g19-0192`
  ↳ *evidence-for* `g19-0293`

- `g20-0092` *STATED* — Best-of-five setup: one command runs the whole job five separate times, and a sixth pass with no ego grades them blind and hands you the winner.
  > “one command runs the whole job five separate times, and a sixth pass with no ego grades them blind and hands you the winner.”
  — [g-run-the-job-five-times-and-let-a-blind-grader-pick](https://chen.media/guides/run-the-job-five-times-and-let-a-blind-grader-pick)
  ↳ *part-of* `g20-0089`
  ↳ *contrast* `g21-0036`

- `g20-0094` *STATED* — Spin up five separate copies of the task, each with its own fresh context, so none can see what the others are writing.
  — [g-run-the-job-five-times-and-let-a-blind-grader-pick](https://chen.media/guides/run-the-job-five-times-and-let-a-blind-grader-pick)
  ↳ *part-of* `g20-0092`

- `g20-0097` *STATED* — Best-of-five prompt opening: 'Do this job five separate times, independently. Do not let the attempts see or reference each other.'
  > “Do this job five separate times, independently. Do not let the attempts see or reference each other.”
  — [g-run-the-job-five-times-and-let-a-blind-grader-pick](https://chen.media/guides/run-the-job-five-times-and-let-a-blind-grader-pick)
  ↳ *part-of* `g20-0092`
  ↳ *example-of* `g20-0095`

- `g20-0099` *STATED* — Best-of-five prompt line: 'Return all five, labelled Attempt 1 through Attempt 5.'
  > “Return all five, labelled Attempt 1 through Attempt 5.”
  — [g-run-the-job-five-times-and-let-a-blind-grader-pick](https://chen.media/guides/run-the-job-five-times-and-let-a-blind-grader-pick)
  ↳ *part-of* `g20-0092`

- `g20-0103` *STATED* — Best-of-five step 2: grade the attempts with something that has nothing to defend.
  > “Grade them with something that has nothing to defend”
  — [g-run-the-job-five-times-and-let-a-blind-grader-pick](https://chen.media/guides/run-the-job-five-times-and-let-a-blind-grader-pick)
  ↳ *part-of* `g20-0089`
  ↳ *leads-to* `g20-0104`
  ↳ *part-of* `g20-0284`
  ↳ *example-of* `g20-0172` — nothing to defend = no skin in the game

- `g20-0108` *STATED* — The run-for-hours system fixes the trust, not the model: it makes Claude earn the right to work alone, one graded job at a time.
  > “This is the system that fixes the trust, not the model: it makes Claude earn the right to work alone, one graded job at a time.”
  — [g-how-to-let-claude-run-for-hours-without-supervising-it](https://chen.media/guides/how-to-let-claude-run-for-hours-without-supervising-it)
  ↳ *part-of* `g20-0105`
  ↳ *contrast* `g20-0107` — fix trust, not model
  ↳ *part-of* `g20-0284` — graded jobs

- `g20-0109` *CORE* — The one rule for unsupervised Claude: it does not get to work alone until it has proven it can.
  > “It does not get to work alone until it has proven it can.”
  — [g-how-to-let-claude-run-for-hours-without-supervising-it](https://chen.media/guides/how-to-let-claude-run-for-hours-without-supervising-it)
  ↳ *part-of* `g20-0108`
  ↳ *qualifies* `g20-0288`

- `g20-0110` *STATED* — You are not hoping Claude gets more trustworthy; you are building a track record it has to pass before it earns autonomy.
  > “You are not hoping Claude gets more trustworthy. You are building a track record it has to pass before it earns autonomy”
  — [g-how-to-let-claude-run-for-hours-without-supervising-it](https://chen.media/guides/how-to-let-claude-run-for-hours-without-supervising-it)
  ↳ *defines* `g20-0109`

- `g20-0111` *STATED* — Autonomy is conditional: Claude must keep its grade to keep working alone.
  > “and a grade it has to keep to keep it.”
  — [g-how-to-let-claude-run-for-hours-without-supervising-it](https://chen.media/guides/how-to-let-claude-run-for-hours-without-supervising-it)
  ↳ *qualifies* `g20-0110`

- `g20-0112` *STATED* — The run-for-hours guide lays out 'The loop, step by step' for the trust-earning system.
  — [g-how-to-let-claude-run-for-hours-without-supervising-it](https://chen.media/guides/how-to-let-claude-run-for-hours-without-supervising-it)
  ↳ *part-of* `g20-0105`
  ↳ *part-of* `g20-0109`

- `g20-0164` *STATED* — Memory Part 5 is 'The workspace and the night shift'.
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0141`
  ↳ *example-of* `g20-0288`

- `g20-0172` *STATED* — The fix for self-review is not a smarter prompt; it is a second opinion with no skin in the game.
  > “The fix isn't a smarter prompt, it's a second opinion with no skin in the game.”
  — [g-the-second-claude-that-reviews-the-first-one-s-work](https://chen.media/guides/the-second-claude-that-reviews-the-first-one-s-work)
  ↳ *leads-to* `g20-0173`

- `g20-0173` *CORE* — THE ONE RULE of review: never let the same model grade its own work.
  > “THE ONE RULE: Never let the same model grade its own work.”
  — [g-the-second-claude-that-reviews-the-first-one-s-work](https://chen.media/guides/the-second-claude-that-reviews-the-first-one-s-work)
  ↳ *part-of* `g20-0167`
  ↳ *part-of* `g20-0284`

- `g20-0174` *STATED* — The reviewer setup is two Claudes with one job each: one makes, the other reviews.
  > “The setup: two Claudes, one job each”
  — [g-the-second-claude-that-reviews-the-first-one-s-work](https://chen.media/guides/the-second-claude-that-reviews-the-first-one-s-work)
  ↳ *part-of* `g20-0167`
  ↳ *example-of* `g20-0173`
  ↳ *example-of* `g20-0285`
  ↳ *evidence-for* `g20-0284`

- `g20-0176` *STATED* — The reviewer guide covers 'Where to run it' and closes with 'The real takeaway'.
  — [g-the-second-claude-that-reviews-the-first-one-s-work](https://chen.media/guides/the-second-claude-that-reviews-the-first-one-s-work)
  ↳ *part-of* `g20-0167`

- `g20-0179` *STATED* — Set the idea council up once, drop in any idea, and let the agents tear it apart.
  > “Set it up once, drop in any idea, and let them tear it apart.”
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *part-of* `g20-0178`
  ↳ *evidence-for* `g19-0293`

- `g20-0180` *STATED* — Council agent 1, the Believer, argues FOR the idea.
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *part-of* `g20-0185`
  ↳ *contrast* `g20-0001` — council roast vs simulation

- `g20-0181` *STATED* — Council agent 2, the Skeptic, attacks the idea.
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *part-of* `g20-0185`

- `g20-0182` *STATED* — Council agent 3, the Investor, checks whether real money shows up.
  > “one checks whether real money shows up”
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *part-of* `g20-0185`

- `g20-0183` *STATED* — Council agent 4, the Judge, reads the whole fight and hands down a single verdict.
  > “a judge reads the whole fight and hands down a single verdict.”
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *part-of* `g20-0185`
  ↳ *part-of* `g20-0284`
  ↳ *example-of* `g09-0246`

- `g20-0184` *STATED* — The idea council saves every ruling, so tomorrow you pick up where you left off instead of starting over.
  > “The council saves every ruling, so tomorrow you pick up where you left off instead of starting over.”
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *part-of* `g20-0178`
  ↳ *example-of* `g20-0286`
  ↳ *evidence-for* `g19-0293`

- `g20-0188` *CORE* — Give each council agent its own space (a Project, a subagent, or a saved instruction set) so its role and bias are always on.
  > “Give each agent its own space (a Project, a subagent, or a saved instruction set) so its role and bias are always on.”
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *enables* `g20-0185`
  ↳ *part-of* `g20-0285`
  ↳ *generalizes* `g20-0201`
  ↳ *example-of* `g20-0289`

- `g20-0191` *STATED* — Council setup 1: make one shared note or folder the whole council works in; your idea and every verdict lives there, so the council remembers.
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *part-of* `g20-0190`
  ↳ *leads-to* `g20-0192`
  ↳ *enables* `g20-0184`
  ↳ *part-of* `g20-0285`

- `g20-0192` *STATED* — Council setup 2: create four agents, one per role, as separate Projects, subagents or saved instruction sets.
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *part-of* `g20-0190`
  ↳ *leads-to* `g20-0193`

- `g20-0193` *STATED* — Council setup 3: paste each agent's prompt into its instructions; this is what locks it to one lens.
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *part-of* `g20-0190`
  ↳ *leads-to* `g20-0194`

- `g20-0194` *STATED* — Council setup 4, wire the handoff: drop your idea in, run the Believer, then the Skeptic, then the Investor, then feed all three to the Judge for the verdict.
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *part-of* `g20-0190`
  ↳ *leads-to* `g20-0195`
  ↳ *depends-on* `g20-0183`

- `g20-0197` *STATED* — The four dev agents are each locked to ONE job and hand off through a single shared folder: one plans, one builds, one tries to break it, and a read-only reviewer guards the gate before anything touches your real project.
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *part-of* `g20-0196`
  ↳ *evidence-for* `g20-0285`
  ↳ *evidence-for* `g19-0062`

- `g20-0203` *STATED* — Dev-team setup 1: make one shared folder (or repo) the whole team works in; everything they produce lives there.
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *part-of* `g20-0202`
  ↳ *leads-to* `g20-0204`
  ↳ *part-of* `g20-0285`

- `g20-0204` *STATED* — Dev-team setup 2: create four agents, one per role, as separate Projects, subagents or saved instruction sets.
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *part-of* `g20-0202`
  ↳ *leads-to* `g20-0205`

- `g20-0205` *STATED* — Dev-team setup 3: paste each agent's prompt into its instructions; this is what locks it to one job.
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *part-of* `g20-0202`
  ↳ *leads-to* `g20-0206`

- `g20-0206` *STATED* — Dev-team setup 4, wire the handoff through files: the Planner writes spec.md, the Coder writes the code, the Tester writes test-report.md, and the Reviewer writes the verdict; each next agent reads the previous file.
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *part-of* `g20-0202`
  ↳ *leads-to* `g20-0207`
  ↳ *evidence-for* `g20-0208`
  ↳ *part-of* `g20-0285`

- `g20-0209` *STATED* — Dev agent 1, the Planner, uses your smartest model and turns your rough idea into an exact spec.
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *part-of* `g20-0198`
  ↳ *leads-to* `g20-0211`

- `g20-0212` *STATED* — Dev agent 3, the Tester, breaks the build on purpose and writes test-report.md.
  > “The Tester (breaks it on purpose)”
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *part-of* `g20-0198`
  ↳ *leads-to* `g20-0213`

- `g20-0213` *STATED* — Dev agent 4, the Reviewer, is read-only and acts as the gate before anything touches your real project.
  > “The Reviewer (read-only, the gate)”
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *part-of* `g20-0198`
  ↳ *part-of* `g20-0284`

- `g20-0221` *STATED* — The Planner saves its output as spec.md.
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *part-of* `g20-0214`
  ↳ *part-of* `g20-0206`

- `g20-0233` *STATED* — Upgrade 3 of 4 is sub agents: one lead, twenty specialists.
  > “Sub agents: one lead, twenty specialists”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *part-of* `g20-0229`
  ↳ *leads-to* `g20-0234`
  ↳ *contrast* `g20-0227` — fixes working alone
  ↳ *enables* `g20-0094`

- `g20-0234` *STATED* — Upgrade 4 of 4 is the loop, in which Claude catches its own mistakes.
  > “The loop: it catches its own mistakes”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *part-of* `g20-0229`
  ↳ *enables* `g20-0235`
  ↳ *analogy-for* `g20-0112`
  ↳ *evidence-for* `g15-0167`

- `g20-0235` *STATED* — The four upgrades are put together in 'The overnight run'.
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *part-of* `g20-0222`
  ↳ *example-of* `g20-0288`

- `g21-0033` *STATED* — Alex's tournament method: make Fable 5 judge a tournament of 20 versions against each other, crown one battle-tested champion, then save the tournament to run on every launch forever.
  — [g-run-a-tournament-instead-of-guessing-which-hook-works](https://chen.media/guides/run-a-tournament-instead-of-guessing-which-hook-works)
  ↳ *part-of* `g21-0029`
  ↳ *evidence-for* `g11-0057`

- `g21-0036` *CORE* — The tournament runs in three moves: generate 20 truly different versions, judge them in a bracket with a scoring rubric, then breed the finalists together and stress test the champion.
  — [g-run-a-tournament-instead-of-guessing-which-hook-works](https://chen.media/guides/run-a-tournament-instead-of-guessing-which-hook-works)
  ↳ *part-of* `g21-0033`

- `g21-0037` *STATED* — Tournament move 1: generate 20 truly different versions of the thing being optimised.
  — [g-run-a-tournament-instead-of-guessing-which-hook-works](https://chen.media/guides/run-a-tournament-instead-of-guessing-which-hook-works)
  ↳ *part-of* `g21-0036`
  ↳ *leads-to* `g21-0038`

- `g21-0038` *STATED* — Tournament move 2: judge the versions in a bracket using a scoring rubric.
  — [g-run-a-tournament-instead-of-guessing-which-hook-works](https://chen.media/guides/run-a-tournament-instead-of-guessing-which-hook-works)
  ↳ *part-of* `g21-0036`
  ↳ *leads-to* `g21-0039`
  ↳ *example-of* `g21-0034`
  ↳ *evidence-for* `g11-0071`

- `g21-0039` *STATED* — Tournament move 3: breed the finalists together into a combined version, then stress test the champion.
  — [g-run-a-tournament-instead-of-guessing-which-hook-works](https://chen.media/guides/run-a-tournament-instead-of-guessing-which-hook-works)
  ↳ *part-of* `g21-0036`

- `g21-0041` *STATED* — The tournament's one-time setup takes about 10 minutes and is best done before the 12th while Fable 5 is still the sharpest judge.
  — [g-run-a-tournament-instead-of-guessing-which-hook-works](https://chen.media/guides/run-a-tournament-instead-of-guessing-which-hook-works)
  ↳ *part-of* `g21-0029`

- `g21-0045` *STATED* — Tournament setup step 3: run the three prompts in order: generate, then judge the bracket, then breed and stress test.
  — [g-run-a-tournament-instead-of-guessing-which-hook-works](https://chen.media/guides/run-a-tournament-instead-of-guessing-which-hook-works)
  ↳ *part-of* `g21-0041`
  ↳ *leads-to* `g21-0046`

- `g21-0050` *STATED* — The AI C-suite method: set Fable up ONE time as six different employees, each with a locked role, then run your whole business through them.
  — [g-turn-claude-into-a-six-person-ai-c-suite](https://chen.media/guides/turn-claude-into-a-six-person-ai-c-suite)
  ↳ *part-of* `g21-0048`
  ↳ *depends-on* `g21-0031` — same 12th deadline

- `g21-0055` *STATED* — The AI C-suite one-time setup takes about 15 minutes, ideally before the 12th while Fable 5 is still free.
  — [g-turn-claude-into-a-six-person-ai-c-suite](https://chen.media/guides/turn-claude-into-a-six-person-ai-c-suite)
  ↳ *part-of* `g21-0048`
  ↳ *because* `g21-0031`

- `g21-0060` *STATED* — C-suite setup step 5: to use an employee, open its Project and paste your raw input (the voice note, the leads, the code) with no re-explaining who they are.
  — [g-turn-claude-into-a-six-person-ai-c-suite](https://chen.media/guides/turn-claude-into-a-six-person-ai-c-suite)
  ↳ *part-of* `g21-0055`

- `g21-0153` *STATED* — Write blueprints ONE AT A TIME (the batch loop controls this) so altitude and grounding do not drift; do not dump them all silently.
  — [g-turn-your-whole-backlog-into-finished-plans-in-one-night](https://chen.media/guides/turn-your-whole-backlog-into-finished-plans-in-one-night)
  ↳ *qualifies* `g21-0152`
  ↳ *depends-on* `g21-0156`
  ↳ *evidence-for* `g20-0288`

- `g21-0174` *STATED* — Use the four resume agents in order: each one hands its output to the next, fixing the resume in one pass.
  — [g-four-claude-agents-that-get-your-resume-past-the-bot](https://chen.media/guides/four-claude-agents-that-get-your-resume-past-the-bot)
  ↳ *part-of* `g21-0170`
  ↳ *part-of* `g20-0285`

- `g21-0194` *STATED* — Sol workflow 1, Ultra mode: for one big, messy job, have Sol split it across parallel subagents and merge the result.
  — [g-three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team](https://chen.media/guides/three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team)
  ↳ *part-of* `g21-0193`
  ↳ *example-of* `g02-0245`

- `g21-0196` *STATED* — Sol workflow 3, the agent: give Sol a goal plus guardrails and let it drive your browser and tools end to end.
  — [g-three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team](https://chen.media/guides/three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team)
  ↳ *part-of* `g21-0193`
  ↳ *depends-on* `r04-0164`

- `g21-0199` *STATED* — Reserve Ultra mode for big jobs that naturally break into parts: a full competitor teardown, a research report, refactoring a codebase, producing a whole set of assets.
  — [g-three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team](https://chen.media/guides/three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team)
  ↳ *example-of* `g21-0201`

- `g21-0206` *STATED* — The Ultra-mode brief asks subagents to flag any place they disagree so the human decides, rather than silently merging conflicts.
  — [g-three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team](https://chen.media/guides/three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team)
  ↳ *part-of* `g21-0204`
  ↳ *part-of* `g21-0202`
  ↳ *contrast* `r01-0016` — Ultra-mode subagents merge and flag disagreements for a human vs blind panels kept independent until a separate aggregator

- `g21-0236` *STATED* — The content-team guide has a section 'How to run them as a team' for chaining the five commands.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *part-of* `g21-0210`

- `g22-0048` *CORE* — Run a factory instead of one model: Sol (the architect) writes ONE master spec and the quality bar, the cheaper models do the reps, and Sol comes back at the end as the inspector.
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)
  ↳ *part-of* `g22-0045`
  ↳ *leads-to* `g22-0049`
  ↳ *example-of* `g22-0277`

- `g22-0050` *STATED* — Station 1 ('Sol writes the master spec'): Sol writes a master spec so clear that a cheaper model cannot mess it up.
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)
  ↳ *part-of* `g22-0048`
  ↳ *leads-to* `g22-0051`

- `g22-0051` *STATED* — Station 2 ('The line: Terra drafts, Luna mass-produces'): the spec goes down the line, Terra drafts, then Luna mass-produces all 50 units.
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)
  ↳ *part-of* `g22-0048`
  ↳ *leads-to* `g22-0053`

- `g22-0053` *STATED* — Station 3 ('The QA gate: Sol inspects the batch'): Sol comes back as the QA inspector, passes the good units and kicks the weak ones back.
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)
  ↳ *part-of* `g22-0048`
  ↳ *analogy-for* `g20-0213`

- `g22-0054` *STATED* — The model-line guide's final part, 'Run the whole line', strings the three stations together end to end (prompt body email-gated).
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)
  ↳ *part-of* `g22-0044`
  ↳ *part-of* `g22-0048`

- `g22-0069` *STATED* — Routine selection: pick the task you redo every week, set it once, and wake up to it finished.
  — [g-put-a-recurring-job-on-autopilot-with-claude-code](https://chen.media/guides/put-a-recurring-job-on-autopilot-with-claude-code)
  ↳ *example-of* `g22-0075`

- `g22-0074` *STATED* — The Routines guide's 'How it works (4 steps)' section lays out a four-step setup.
  — [g-put-a-recurring-job-on-autopilot-with-claude-code](https://chen.media/guides/put-a-recurring-job-on-autopilot-with-claude-code)
  ↳ *part-of* `g22-0065`

- `g22-0075` *STATED* — Routine setup section 'Pick one job': start a Routine with a single job.
  — [g-put-a-recurring-job-on-autopilot-with-claude-code](https://chen.media/guides/put-a-recurring-job-on-autopilot-with-claude-code)
  ↳ *part-of* `g22-0074`
  ↳ *leads-to* `g22-0076`

- `g22-0076` *STATED* — Routine setup section 'Write the routine prompt': the job is written as a saved prompt (template email-gated).
  — [g-put-a-recurring-job-on-autopilot-with-claude-code](https://chen.media/guides/put-a-recurring-job-on-autopilot-with-claude-code)
  ↳ *part-of* `g22-0074`
  ↳ *leads-to* `g22-0077`

- `g22-0077` *STATED* — Routine setup section 'Connect what it needs (safely)': attach only the connectors the job needs, with safety in mind.
  — [g-put-a-recurring-job-on-autopilot-with-claude-code](https://chen.media/guides/put-a-recurring-job-on-autopilot-with-claude-code)
  ↳ *part-of* `g22-0074`
  ↳ *leads-to* `g22-0078`
  ↳ *evidence-for* `r04-0196`

- `g22-0078` *STATED* — Routine setup section 'Put it on a schedule': set the Routine's trigger cadence.
  — [g-put-a-recurring-job-on-autopilot-with-claude-code](https://chen.media/guides/put-a-recurring-job-on-autopilot-with-claude-code)
  ↳ *part-of* `g22-0074`
  ↳ *leads-to* `g22-0079`

- `g22-0080` *INFERRED* — The four Routine steps are most likely Pick one job, Write the routine prompt, Connect what it needs (safely), Put it on a schedule, with 'Make it bulletproof' as a hardening pass afterwards.
  — [g-put-a-recurring-job-on-autopilot-with-claude-code](https://chen.media/guides/put-a-recurring-job-on-autopilot-with-claude-code)
  ↳ *defines* `g22-0074`

- `g22-0099` *STATED* — The PURGE system from the video is 3 steps: FIND every account, DELETE the ones you do not use, GUARD against new leaks every month.
  — [g-make-claude-hunt-down-every-forgotten-account-you-have](https://chen.media/guides/make-claude-hunt-down-every-forgotten-account-you-have)
  ↳ *part-of* `g22-0097`

- `g22-0106` *STATED* — PURGE step 3 GUARD: every month, Claude re-scans for new accounts and old ones that leaked your info, and hands you a one-tap kill list.
  — [g-make-claude-hunt-down-every-forgotten-account-you-have](https://chen.media/guides/make-claude-hunt-down-every-forgotten-account-you-have)
  ↳ *part-of* `g22-0099`
  ↳ *example-of* `g22-0279`

- `g22-0257` *STATED* — Bill prompt 4 'Never Pay It Twice' ('Re-check every month, automatically'): Claude re-checks every month so the price never quietly creeps back up.
  — [g-the-prompts-and-call-scripts-that-lower-every-bill](https://chen.media/guides/the-prompts-and-call-scripts-that-lower-every-bill)
  ↳ *part-of* `g22-0253`
  ↳ *example-of* `g22-0279`

- `g22-0278` *INFERRED* — Agentic actions with real-world side effects should default to human approval: PURGE pauses for your OK per account, and the Meta Ads connector creates everything PAUSED.
  — [g-make-claude-hunt-down-every-forgotten-account-you-have](https://chen.media/guides/make-claude-hunt-down-every-forgotten-account-you-have) [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)
  ↳ *evidence-for* `g09-0247`

- `g22-0279` *INFERRED* — Recurring monthly re-checks recur across Alex's guides (PURGE GUARD, bills 'Never Pay It Twice', brokers 'Keep it gone', the Judgment Vault maintenance loop); a Claude Code Routine is the native way to run them unattended.
  — [g-make-claude-hunt-down-every-forgotten-account-you-have](https://chen.media/guides/make-claude-hunt-down-every-forgotten-account-you-have) [g-the-prompts-and-call-scripts-that-lower-every-bill](https://chen.media/guides/the-prompts-and-call-scripts-that-lower-every-bill) [g-wipe-your-name-and-address-off-the-data-brokers](https://chen.media/guides/wipe-your-name-and-address-off-the-data-brokers) [g-bank-the-judgment-calls-not-just-the-output](https://chen.media/guides/bank-the-judgment-calls-not-just-the-output) [g-put-a-recurring-job-on-autopilot-with-claude-code](https://chen.media/guides/put-a-recurring-job-on-autopilot-with-claude-code)

- `r01-0033` *STATED* — /launch is a unanimous gate: all 8 flight controllers must say GO.
  > “All 8 must say GO.”
  — [r-alexyc9381](https://github.com/alexyc9381/alexyc9381)
  ↳ *defines* `r01-0032`
  ↳ *contrast* `r01-0165` — unanimous GO vs majority vote
  ↳ *evidence-for* `r02-0157`

- `r01-0048` *STATED* — '/agency night' (night shift) works through .agency/queue.md while your computer stays on.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0037`
  ↳ *evidence-for* `g07-0066`

- `r01-0069` *STATED* — /agency always reads .agency/AGENCY.md first; if it does not exist, it runs setup before anything else.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *depends-on* `r01-0077`
  ↳ *leads-to* `r01-0042` — missing AGENCY.md triggers setup

- `r01-0077` *STATED* — /agency setup writes .agency/AGENCY.md with the answers under the headings Offer, Customer, Price, Promise, Voice, Sign-off.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0042`

- `r01-0096` *STATED* — The /agency workflow agent works in two parts, in order: Proposal, then Build.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *defines* `r01-0046`

- `r01-0098` *STATED* — /agency shows the proposal to the user and waits for 'approved' before building.
  > “Show it to the user and wait for "approved".”
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0096`
  ↳ *leads-to* `r01-0099`
  ↳ *evidence-for* `g07-0063`
  ↳ *example-of* `g12-0303`

- `r01-0106` *STATED* — The /agency night shift works through .agency/queue.md from the top; each line is one job for one agent (for example 'outbound leads/dentists.csv' or 'build acme').
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0048`
  ↳ *depends-on* `r01-0078` — queue.md created at setup

- `r01-0107` *STATED* — /agency night-shift loop: do the job, tick it, write one line about it to .agency/NIGHT-LOG.md, then take the next.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0048`
  ↳ *evidence-for* `g07-0067`

- `r01-0108` *STATED* — The /agency night shift does not stop to ask questions: when something needs the user, it writes the question to the log and moves on.
  > “Do not stop to ask questions: when something needs the user, write the question to the log and move on.”
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0048`
  ↳ *enables* `r01-0107` — unattended loop never blocks

- `r01-0121` *STATED* — The /hiring-panel automated screen answers PASS or REJECT, then at most five reasons, each quoting the line it is about.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *part-of* `r01-0122`
  ↳ *leads-to* `r01-0136`

- `r01-0122` *STATED* — /hiring-panel step 2 starts one sub-agent as the automated system that decides whether a real human should see the resume, given the resume and the job (if any).
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *defines* `r01-0120`

- `r01-0127` *STATED* — The /hiring-panel hiring manager sub-agent answers INTERVIEW or NO, what decided it in the first ten seconds, what it would ask in the interview, and the three weakest lines (quoted).
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *part-of* `r01-0119`
  ↳ *leads-to* `r01-0136`

- `r01-0128` *STATED* — /hiring-panel starts the five readers at once: one message, five sub-agent calls.
  > “Start five sub-agents at once (one message, five calls).”
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *part-of* `r01-0119`
  ↳ *leads-to* `r01-0136`
  ↳ *evidence-for* `r03-0194`

- `r01-0129` *STATED* — Each /hiring-panel reader sub-agent gets ONLY the resume (and the job) and ONE reader persona; nobody sees anybody else's notes.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *part-of* `r01-0128`
  ↳ *example-of* `r01-0016`

- `r01-0161` *STATED* — Instead of one polite answer, /court takes the same idea and runs a trial.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *contrast* `r01-0160`

- `r01-0164` *STATED* — In /court each side answers the other's points in a rebuttal round.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0161`

- `r01-0165` *STATED* — In /court 12 jurors read the record and vote GUILTY or NOT GUILTY on their own.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0161`

- `r01-0178` *STATED* — /court flag '--jury N' sets 3 to 12 jurors; default 12.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *qualifies* `r01-0165`

- `r01-0180` *STATED* — /court flag '--seed S' fixes which jurors sit on a smaller jury; the default is random, and recorded.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *qualifies* `r01-0178`

- `r01-0187` *STATED* — In /court, skills/court/court.py does the bookkeeping: opens the trial, writes one brief per sub-agent, checks every output exists, counts the votes and renders the verdict.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *enables* `r01-0188`

- `r01-0211` *STATED* — /court state lives in .court/<run>/state.json, and every command after init finds it through .court/LATEST.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0187`

- `r01-0221` *STATED* — /court step 3 opens the trial: COURT init --case-file .court/case.md [--jury N | --quick] [--seed S]
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *depends-on* `r01-0217`
  ↳ *part-of* `r01-0187`
  ↳ *leads-to* `r01-0222`

- `r01-0222` *STATED* — /court is always driven with 'COURT next', which reads the files on disk and tells Claude the next phase and the exact command.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0187`
  ↳ *evidence-for* `r02-0186`

- `r01-0224` *STATED* — 'COURT prompts <phase>' writes one brief per job and lists the jobs still to run, in waves.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0187`
  ↳ *leads-to* `r01-0225`
  ↳ *evidence-for* `r02-0188`

- `r01-0225` *STATED* — /court launches one wave at a time: a single message with one Agent tool call per job in that wave.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0223`
  ↳ *contrast* `r01-0128` — waves of many calls vs one 5-call fan-out
  ↳ *evidence-for* `r03-0194`

- `r01-0227` *STATED* — Each /court sub-agent call is subagent_type 'general-purpose', description 'court <job id>', prompt 'Read <brief path> and follow it exactly. It is your whole brief.'
  > “Read <brief path> and follow it exactly. It is your whole brief.”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0225`
  ↳ *depends-on* `r01-0216` — brief file is the sub-agent's whole context
  ↳ *evidence-for* `r02-0191`

- `r01-0228` *STATED* — /court waits until every agent in a wave has replied before launching the next wave.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *qualifies* `r01-0225`
  ↳ *evidence-for* `r02-0192`

- `r01-0229` *STATED* — After the last wave Claude runs 'COURT next'; if an output is missing it sends Claude back to the same phase, where 'prompts' lists only the missing jobs, which are re-run once.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0222`
  ↳ *evidence-for* `r02-0193`

- `r01-0230` *STATED* — If a /court juror fails twice, Claude writes the single line 'NO VOTE' into its file ('COURT check jury' lists it) and moves on.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *qualifies* `r01-0229`
  ↳ *evidence-for* `r02-0194`

- `r01-0232` *STATED* — 'COURT render' counts the votes, writes VERDICT.md into the run folder and prints it.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0187`
  ↳ *leads-to* `r01-0170`

- `r01-0236` *STATED* — If the user disagrees with the verdict, /court offers a retrial with the changes from 'Conditions for acquittal' written into a new case file, without arguing for either side.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *depends-on* `r01-0169`
  ↳ *leads-to* `r01-0217` — new case file with the changes
  ↳ *example-of* `g04-0249`

- `r01-0240` *STATED* — Each /court juror file has four fields: VOTE, REASON, DECIDING FACT, WOULD FLIP IF.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0165`

- `r01-0274` *STATED* — VERDICT.md layout: '# The verdict: GUILTY, 3 to 0', the case, the charge, a How the jury voted table (Juror | Vote | Why), Charges that stuck, What the defense got right, Conditions for acquittal, The sentence.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *defines* `r01-0170`

- `r02-0003` *STATED* — After preparing everything, /hunter stops and shows you the list of jobs for a yes before anything is sent.
  > “Then it stops and shows you the list for a yes.”
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0001`

- `r02-0055` *CORE* — Each of /hunter's five Claudes is a sub-agent with ONE job and ONLY what it needs.
  > “Each is a sub-agent with ONE job and ONLY what it needs.”
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0311`
  ↳ *evidence-for* `g20-0285`

- `r02-0056` *CORE* — /hunter's two scorers (recruiter and hiring manager) never see each other's answer.
  > “The two scorers never see each other's answer.”
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0311`
  ↳ *qualifies* `r02-0080`
  ↳ *evidence-for* `r01-0016`

- `r02-0076` *STATED* — /hunter run step 3 (Score): for each kept job start TWO sub-agents at once, the recruiter and the hiring manager, up to five jobs at a time.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0017`
  ↳ *example-of* `g02-0245`

- `r02-0077` *STATED* — /hunter gives each scorer sub-agent only the resume, the profile and the posting.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *example-of* `r02-0055`
  ↳ *part-of* `r02-0076`

- `r02-0078` *STATED* — Each /hunter scorer answers with a score out of 100, one reason, and the biggest gap, quoting the posting line.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0076`

- `r02-0107` *STATED* — /hunter morning does **run** without asking questions: anything that needs the user goes in the packet as `YOU` and it moves on, never applying.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *defines* `r02-0022`
  ↳ *evidence-for* `r03-0079`

- `r02-0123` *CORE* — /launch splits the checking between 8 flight controllers who each own one part and never see each other's calls.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0118`
  ↳ *example-of* `r02-0311`
  ↳ *evidence-for* `r01-0016`

- `r02-0133` *STATED* — If even one /launch station says NO-GO, the app doesn't launch.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0157`

- `r02-0155` *STATED* — `skills/launch/launch.py` does the /launch bookkeeping: opens the poll, writes one brief per controller, checks every report exists, counts the calls and renders the board.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *enables* `r02-0157`
  ↳ *evidence-for* `r01-0189`

- `r02-0156` *CORE* — In /launch, Claude only coordinates: it never makes a call, never softens one and never fixes anything during the poll.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *depends-on* `r02-0155`
  ↳ *evidence-for* `r04-0021`

- `r02-0157` *STATED* — The /launch call is a rule, not an opinion: GO for launch only if every station says GO.
  > “The call is a rule, not an opinion”
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0317`

- `r02-0186` *STATED* — /launch always drives the poll with `LAUNCH next`, which reads the files on disk and tells Claude the next phase and the exact command.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0171`

- `r02-0187` *STATED* — /launch phases run in order: `poll` (the stations), then `director` (the flight director).
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0186`

- `r02-0188` *STATED* — `LAUNCH prompts <phase>` writes one brief per job and lists the jobs still to run, in waves.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0186`

- `r02-0189` *STATED* — /launch launches one wave at a time: a single message with one Agent tool call per job in that wave.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *depends-on* `r02-0188`
  ↳ *contrast* `r02-0076` — launch waits per wave; hunter runs up to five jobs x2 scorers at once
  ↳ *evidence-for* `r03-0194`

- `r02-0191` *STATED* — Each /launch Agent call uses `subagent_type: general-purpose`, `description: launch <job id>`, and `prompt: Read <brief path> and follow it exactly. It is your whole brief.`
  > “Read <brief path> and follow it exactly. It is your whole brief.”
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0189`
  ↳ *depends-on* `r02-0177` — brief file carries all context

- `r02-0192` *STATED* — /launch waits until every agent in a wave has replied before launching the next wave.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0189`

- `r02-0193` *STATED* — After the last wave run `LAUNCH next`; if a report is missing it sends Claude back to the same phase, `prompts` lists only the missing jobs, and those are re-run once.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0186`

- `r02-0194` *STATED* — If a /launch station fails twice it is left without a report, and the board counts it as NO CALL, which holds the launch.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0193`
  ↳ *evidence-for* `r02-0157` — missing report = NO CALL = HOLD

- `r02-0243` *STATED* — /launch stations note overlaps but defer to the owning station, e.g. USERS writes "(DATABASE station's area)" and RULES writes "(security's call)".
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0242`
  ↳ *part-of* `r02-0123`

- `r03-0009` *CORE* — /learn part 2, 'Every night, a second Claude investigates': an investigator Claude goes over the day's corrections: what went wrong, why, and what to do instead.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0007`
  ↳ *leads-to* `r03-0010`

- `r03-0035` *STATED* — Easiest nightly /learn run, in Claude Desktop: Code tab, Routines, New routine, Local; Instructions '/learn review', your project folder, schedule Daily.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0033`

- `r03-0036` *STATED* — After creating a Claude Desktop routine, click 'Run now' once and choose 'always allow' for each prompt so later unattended runs don't stall.
  > “Click Run now once and choose "always allow" for each prompt so later runs don't stall.”
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0035`
  ↳ *qualifies* `r04-0163`

- `r03-0038` *STATED* — Nightly /learn via Mac launchd or Linux cron: cd /path/to/your/project && claude -p "/learn review" --permission-mode dontAsk --allowedTools "Bash(python3 .claude/hooks/learn.py *),Edit(./LESSONS.md),Edit(./.learn/**)"
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0033`
  ↳ *contrast* `r03-0035` — headless cron vs desktop routine

- `r03-0079` *CORE* — The /learn review runs every night with nobody watching, often as 'claude -p "/learn review"', so its instructions say: 'Don't ask questions; finish on your own.'
  > “Don't ask questions; finish on your own.”
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *defines* `r03-0031`
  ↳ *analogy-for* `r03-0192` — both avoid blocking questions in unattended/fan-out runs
  ↳ *evidence-for* `r01-0108`

- `r03-0080` *STATED* — /learn review step 1: 'LEARN inbox' prints every correction not reviewed yet, with what Claude had just said when the transcript could be read, and the rulebook as it is now.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0079`
  ↳ *leads-to* `r03-0082`

- `r03-0087` *STATED* — /learn review step 4: add each rule with 'LEARN add "<rule>"'; a MERGED reply means the mistake came back although a rule existed, and the note must say so.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0079`
  ↳ *leads-to* `r03-0089`

- `r03-0090` *STATED* — /learn review step 6: write the note to .learn/reviews/YYYY-MM-DD.md (today's date) in a fixed shape, and nothing else.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0079`
  ↳ *leads-to* `r03-0092`
  ↳ *leads-to* `r03-0017`

- `r03-0091` *STATED* — The /learn review note shape: '# Review, YYYY-MM-DD'; 'N corrections, N lessons, N false alarms. Rulebook: N of 40 rules.'; one '## N. <short name of the mistake>' block per lesson with What went wrong / Why / Instead / Rule (ADDED as rule N / MERGED into rule N, now seen Nx); a '## Not lessons' list; then the credit line.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0090`

- `r03-0092` *STATED* — /learn review step 7: run 'LEARN done' to mark the inbox reviewed, then print the note's first two lines and its path.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0079`

- `r03-0155` *CORE* — /linkedin-roast step 2: it starts five sub-agents at the same time; each gets only your profile and one role, and none sees the others' answers, 'so nobody goes easy on you'.
  > “None sees the others' answers, so nobody goes easy on you.”
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0134`
  ↳ *leads-to* `r03-0156`
  ↳ *evidence-for* `r01-0016`

- `r03-0156` *STATED* — /linkedin-roast step 3: it prints the roasts and the problems at least three of the five agree on.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0134`
  ↳ *leads-to* `r03-0157`

- `r03-0194` *CORE* — To run five roasters in parallel, start FIVE sub-agents at once: one message with five Agent calls (older Claude Code versions call the tool Task), then wait for all five.
  > “one message with five Agent calls (older Claude Code versions call the tool Task)”
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *defines* `r03-0155`

- `r03-0195` *STATED* — Each /linkedin-roast sub-agent prompt is its persona, the cleaned profile text, the rules and the answer format, and nothing else.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0194`

- `r03-0196` *CORE* — Never put one roaster's persona or answer into another's prompt, and never run a second round: 'That is what keeps them honest: five readers who cannot copy each other.'
  > “That is what keeps them honest: five readers who cannot copy each other.”
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *because* `r03-0155`
  ↳ *qualifies* `r03-0195`
  ↳ *evidence-for* `r01-0016`

- `r03-0202` *STATED* — The /linkedin-roast persona texts are used word for word, filling in the {field} and {level} placeholders from the 'Assumed:' line.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *qualifies* `r03-0200`
  ↳ *qualifies* `r03-0201`

- `r03-0214` *STATED* — Every /linkedin-roast sub-agent must 'Answer in exactly this format', a fixed 6-part template, so five independent answers can be compared and tallied.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0195`
  ↳ *enables* `r03-0217`

- `r03-0215` *STATED* — /linkedin-roast prints the five answers one block each with the role and score, recruiter first, opening with the recruiter's headline roast.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0156`

- `r03-0217` *STATED* — 'What all five agree on' is a short numbered list of the problems at least three roasters raised, worst first, each ending '(n of 5)'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0156`
  ↳ *example-of* `g09-0248`

- `r03-0218` *STATED* — /linkedin-roast reports the average score, and the lowest score with whose it is.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0156`

- `r04-0090` *STATED* — The night crew builder takes the next item off your backlog, builds it with tests, and opens a pull request: 'Wake up to a new signup page, a pricing page, the bug fix you kept putting off.'
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0087`

- `r04-0092` *STATED* — The night crew tracker runs your tests and builds, checks the builder's work, and writes up what's working, what isn't, and what to build next.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0087`
  ↳ *contrast* `r04-0228` — night crew self-checks via a tracker; shark host never edits

- `r04-0096` *STATED* — The night crew house rules forbid deploys, purchases, deleting, posting and secrets, and anything that would need those comes back as NEEDS YOUR OK instead.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *because* `r04-0094`

- `r04-0097` *STATED* — Night crew setup walks you through three switches that enforce the house rules: a protected default branch, no real secrets in the cloud environment, and no connectors that can pay or publish.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *example-of* `r04-0019`
  ↳ *enables* `r04-0094`

- `r04-0106` *STATED* — Run /night-crew in Claude Code inside your app's folder: it reads your repo, asks six quick questions (the app, your backlog, your customers, what marketing to draft, your bedtime, anything off limits), writes NIGHT-CREW.md, and gives you the three /schedule lines to create the routines, then walks you through the guardrails.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0087`
  ↳ *leads-to* `r04-0093`

- `r04-0110` *STATED* — Each night crew routine clones your repo from its default branch, reads NIGHT-CREW.md, does its one job and opens a draft pull request.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *defines* `r04-0089`

- `r04-0112` *STATED* — Change the night crew's orders by editing NIGHT-CREW.md: the next run reads the new version from the default branch.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *qualifies* `r04-0093`

- `r04-0129` *STATED* — The night crew House rules apply to every crew member, every night, no exceptions, and the skill keeps the eight rules exactly as written.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0093`

- `r04-0130` *STATED* — Night crew house rule 1, Pull requests only: work on a new branch whose name starts with claude/night-crew-, open a draft pull request into the default branch, never merge anything, never push to the default branch or to anyone else's branch.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0129`
  ↳ *defines* `r04-0095`

- `r04-0131` *STATED* — Night crew house rule 2, Never touch the live app: no deploys, releases or publishing packages; no changes to production configuration, environment files, secrets, CI deploy steps or infrastructure; never connect to or run migrations against a real database.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0129`
  ↳ *evidence-for* `r04-0094`

- `r04-0132` *STATED* — Night crew house rule 3, Never spend money: no purchases, no paid sign-ups, no upgrading any plan, no calls to paid APIs, no ads.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0129`
  ↳ *evidence-for* `r04-0094`

- `r04-0133` *STATED* — Night crew house rule 4, Never delete anything you didn't create tonight (files, branches, issues, data or accounts); changing existing code to build a backlog item is fine, removing a feature is not.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0129`
  ↳ *evidence-for* `r04-0094`

- `r04-0134` *STATED* — Night crew house rule 5, Never post or send anything (social posts, emails, messages, comments on other sites, replies to customers): write drafts into the report; the owner posts them.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0129`
  ↳ *qualifies* `r04-0091`

- `r04-0135` *STATED* — Night crew house rule 6, Never put secrets in anything you write: no keys, tokens or passwords in code, reports or pull request descriptions.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0129`

- `r04-0136` *STATED* — Night crew house rule 7: when a job needs any forbidden action, don't do it; write 'NEEDS YOUR OK:' with what you would do and why at the top of your report, then carry on with the rest of your job.
  > “Write `NEEDS YOUR OK:` and what you would do and why at the top of your report, then carry on with the rest of your job.”
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0129`
  ↳ *defines* `r04-0096`
  ↳ *analogy-for* `r04-0080` — flag-and-ask instead of acting
  ↳ *evidence-for* `r01-0108`

- `r04-0137` *STATED* — Night crew house rule 8, Stay small: one backlog item a night is a good night; if something is bigger than one night, split it and say so.
  > “One backlog item a night is a good night.”
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0129`
  ↳ *evidence-for* `g13-0271`

- `r04-0138` *STATED* — Builder step 1: take the first unchecked Backlog item; if it's already done in the code, or an open claude/night-crew- pull request already covers it, take the next one.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0090`
  ↳ *qualifies* `r04-0137`

- `r04-0139` *STATED* — Builder step 2: build the item following the code's existing style, and add or update tests for it.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0090`

- `r04-0140` *STATED* — Builder step 3: run every command in 'How to check your work' and fix what fails because of your change.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0090`
  ↳ *depends-on* `r04-0127`

- `r04-0141` *STATED* — Builder step 4: in the same branch, tick the item in NIGHT-CREW.md's Backlog (- [x]) so merging the pull request records it as done.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0090`
  ↳ *enables* `r04-0143` — merging records the item as done

- `r04-0142` *STATED* — Builder step 5: write night-crew/reports/<date>-builder.md: what you built, how to try it, what you tested, anything left over, and any NEEDS YOUR OK: items.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0090`
  ↳ *depends-on* `r04-0136`

- `r04-0143` *STATED* — Builder step 6: open a draft pull request titled 'Night crew (builder): <the backlog item>', with the report as its description.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0090`
  ↳ *example-of* `r04-0130`

- `r04-0150` *STATED* — Tracker step 1: check out the default branch and run every command in 'How to check your work', recording what passes and what fails, with the errors.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0092`

- `r04-0151` *STATED* — Tracker step 2: check out every open claude/night-crew- pull request from tonight, run the same commands, and say whether it's safe to review.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0092`
  ↳ *depends-on* `r04-0143`

- `r04-0152` *STATED* — Tracker step 3: read the code for broken links and pages, TODOs and FIXMEs, missing tests, errors in recent commits, slow or risky spots; be specific, with file paths.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0092`

- `r04-0153` *STATED* — Tracker report night-crew/reports/<date>-tracker.md has four sections: Works; Doesn't work (most serious first, with where and why); Tonight's pull requests (safe to review or not, and why); Build next (the 3 things to add to the Backlog, most valuable first).
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0092`

- `r04-0154` *STATED* — Tracker step 5: open a draft pull request titled 'Night crew (tracker): report for <date>' containing only the report file.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0092`

- `r04-0165` *STATED* — Night crew Setup 1, find the repo: check it's a git repo with a GitHub remote (git remote -v) and note the default branch (git symbolic-ref refs/remotes/origin/HEAD, or ask); with no GitHub remote, stop and tell the user the crew needs the app on GitHub first.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0106`

- `r04-0168` *STATED* — Night crew interview question 2: a backlog of 3 to 10 things to build, most important first ('a signup page with email and Google', 'a pricing page', 'dark mode'), each finishable in one night; split anything bigger.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0166`
  ↳ *evidence-for* `r04-0137`

- `r04-0171` *STATED* — Night crew interview question 5: bedtime, when they go to sleep and wake up, and their time zone.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0166`
  ↳ *enables* `r04-0183`

- `r04-0172` *STATED* — Night crew interview question 6: anything the crew must never touch (folders, files or services beyond the house rules).
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0166`

- `r04-0174` *STATED* — Night crew Setup 3: copy NIGHT-CREW.template.md from ${CLAUDE_SKILL_DIR} to NIGHT-CREW.md at the repo root and fill every {{...}} from the interview and the repo; keep the backlog a checklist, most important first, one line each.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0106`

- `r04-0175` *STATED* — Fill NIGHT-CREW.md's 'How to check your work' with the real install, test, build and lint commands; if there are no tests, say so plainly, and the tracker will note it every morning.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0174`

- `r04-0176` *STATED* — Keep NIGHT-CREW.md's House rules section exactly as written, then add the user's own never-touch list under it.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *example-of* `r04-0017`
  ↳ *part-of* `r04-0174`
  ↳ *depends-on* `r04-0129`

- `r04-0177` *STATED* — Show the user the finished NIGHT-CREW.md and ask them to read the house rules.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0174`

- `r04-0178` *STATED* — Night crew Setup 4: ask whether to commit; on a yes, commit only NIGHT-CREW.md with the message 'Add the night crew's standing orders' and push it to the default branch, or open a pull request if the branch is protected and tell them to merge it before bedtime; never commit anything else.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0106`

- `r04-0185` *STATED* — /schedule Repository answer for the night crew: only this app's repo.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0184`

- `r04-0193` *STATED* — Guardrail 1, protect the default branch on GitHub: Settings, then Rules (or Branches), add a rule that requires a pull request before merging and blocks force pushes and deletions, with no bypass for the account the routines push as (the user's own account, so admins must not be exempt).
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0097`
  ↳ *leads-to* `r04-0194`

- `r04-0195` *STATED* — Guardrail 2, no real secrets in the cloud environment: no production database URLs, payment keys or admin tokens in a routine's environment variables; test keys only, and only if the tests need them.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0097`
  ↳ *qualifies* `r04-0135`

- `r04-0196` *STATED* — Guardrail 3: no connectors that can spend or publish.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0097`
  ↳ *defines* `r04-0189`

- `r04-0197` *STATED* — Night crew Setup 7: tell the user in two or three lines that tonight the routines run, tomorrow there will be up to three pull requests from claude/ branches (code from the builder, reports from the scout and tracker), to run /night-crew morning with coffee, and that nothing ships until they merge it.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0106`
  ↳ *leads-to* `r04-0107`

- `r04-0200` *STATED* — Morning step 2: for each crew pull request, read the description and the report files it adds under night-crew/.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0107`

- `r04-0201` *STATED* — Morning step 3: one screen, most important first: Ready to review (what the builder built, which item, whether checks passed); Needs your OK (spending, deleting, live-app, public posting flags); What the scout found (best 3 leads with links, where post drafts are); What the tracker says.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0107`
  ↳ *depends-on* `r04-0096`
  ↳ *analogy-for* `r04-0263` — one-screen, most-important-first readout

- `r04-0202` *STATED* — Morning step 4: offer the next step: review a pull request together, move a backlog item, or change the crew's orders in NIGHT-CREW.md.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0107`
  ↳ *leads-to* `r04-0112`

- `r04-0210` *STATED* — /shark step 1: 5 sharks read your pitch, and each writes their biggest worry and their three hardest questions.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0206`

- `r04-0212` *STATED* — /shark step 2: a founder Claude answers every question only from what you told it; when your pitch lacks the answer it says so, and that question goes on your homework list.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0206`

- `r04-0213` *STATED* — /shark step 3: each shark decides IN or OUT with a practice offer ('$50,000 for 10%'), one line of why, and the one thing that would change their mind.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0206`
  ↳ *leads-to* `r04-0215`

- `r04-0240` *STATED* — Want a tougher /shark room? Add --investors 10.
  > “Want a tougher room? Add `--investors 10`.”
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0222`

- `r04-0242` *STATED* — The shark skill makes Claude the host: never invest, never answer for the founder yourself, and never soften a decision.
  > “You are the host. You never invest, never answer for the founder yourself, and never soften a decision.”
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *defines* `r04-0228`
  ↳ *evidence-for* `r04-0021`

- `r04-0255` *STATED* — /shark panel phases, always driven with SHARK next, run in order: grill (each investor writes three hardest questions), answers (one founder sub-agent answers them all, only from the pitch file), decide (each investor goes IN or OUT).
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *evidence-for* `r01-0222`

- `r04-0256` *STATED* — SHARK prompts <phase> writes one brief per job and lists the jobs still to run, in waves.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0255`
  ↳ *part-of* `r04-0227`
  ↳ *evidence-for* `r02-0188`

- `r04-0257` *STATED* — Launch /shark sub-agents one wave at a time: a single message with one Agent tool call per job in that wave (the Agent tool is called Task in older Claude Code versions).
  > “a single message with one Agent tool call per job in that wave (the Agent tool is called Task in older Claude Code versions)”
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0255`
  ↳ *qualifies* `r04-0016`
  ↳ *evidence-for* `r03-0194`

- `r04-0258` *STATED* — Each /shark Agent call uses subagent_type general-purpose, description 'shark <job id>', and prompt 'Read <brief path> and follow it exactly. It is your whole brief.'
  > “Read <brief path> and follow it exactly. It is your whole brief.”
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *evidence-for* `r04-0018`
  ↳ *part-of* `r04-0255`
  ↳ *evidence-for* `r02-0191`

- `r04-0259` *STATED* — Wait until every agent in a wave has replied before you launch the next wave.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0255`
  ↳ *evidence-for* `r02-0192`

- `r04-0260` *STATED* — After the last wave run SHARK next; if an output is missing, re-run those jobs once, and if one fails twice write the single line 'NO DECISION' into its file and move on.
  > “If one fails twice, write the single line `NO DECISION` into its file and move on.”
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0255`
  ↳ *qualifies* `r04-0261`
  ↳ *evidence-for* `r02-0194`

- `r04-0267` *STATED* — For another /shark round, write the user's new answers into the pitch file and run a new session.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0242`
  ↳ *depends-on* `r04-0233`

- `r04-0273` *STATED* — A /shark grill file has the format 'BIGGEST WORRY: <one line>' then 'QUESTIONS:' numbered 1 to 3.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *defines* `r04-0210`

- `r04-0282` *STATED* — The /shark founder sub-agent answers in the form 'NOT ANSWERED: the founder needs to find out ...' whenever the pitch lacks the fact, and each such line becomes homework.
  > “NOT ANSWERED: the founder needs to find out”
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *defines* `r04-0212`

- `r04-0293` *STATED* — A /shark decision file has four lines: DECISION: (IN or OUT), OFFER:, REASON:, and WHAT WOULD CHANGE MY MIND:.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *defines* `r04-0213`

- `r04-0298` *STATED* — A /shark BOARD.md has a headline (e.g. 'No deal: all 2 sharks are out'), the pitch line, a 'The sharks' table (Shark | Decision | Offer | Why), 'What would change their minds', and 'Your homework: questions you could not answer'.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *defines* `r04-0215`
  ↳ *example-of* `r04-0226`

- `y01-0073` *STATED* — Use a Codex scheduled task when you want it to repeat work at a particular time, and describe what it should produce.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *evidence-for* `g22-0069`

- `y01-0075` *STATED* — The Codex Scheduled section is where you review scheduled tasks and their runs, or pause work you no longer need.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *part-of* `y01-0073`

- `y01-0092` *STATED* — /market copy <website link> sends the ai-agency-claude marketing team through the client's website to find the weak copy and rewrite it.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *part-of* `y01-0101`
  ↳ *example-of* `y01-0089`

- `y01-0095` *STATED* — For email sequences, run the ai-agency-claude /market email command (captioned 'slash market Claude', likely a mis-hearing) with information about the client's offer.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *part-of* `y01-0101`
  ↳ *example-of* `y01-0089`

- `y01-0099` *STATED* — /market ads <website link> outputs actual ads you can copy and paste.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *part-of* `y01-0101`
  ↳ *example-of* `y01-0089`

- `y01-0100` *STATED* — /market social plus as much information about the business as possible makes Claude build an entire month of social content.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *part-of* `y01-0101`
  ↳ *example-of* `y01-0089`

- `y01-0103` *STATED* — /sales <website link> starts five different sales agents researching the target company at the same time.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *example-of* `g02-0245`
  ↳ *example-of* `y01-0089`
  ↳ *leads-to* `y01-0105`

- `y01-0105` *STATED* — /sales contacts <website link> scrapes the internet to find the contacts you should actually reach out to.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *leads-to* `y01-0106`

- `y01-0106` *STATED* — /sales outreach <company website> turns everything learned about the company into a personalized cold email sequence.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *leads-to* `y01-0108`

- `y01-0108` *STATED* — /sales follow up <company> builds a follow-up when a prospect doesn't respond.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *leads-to* `y01-0109`

- `y01-0109` *STATED* — /sales prep <company> prepares talking points, questions to ask, objections to handle and everything you need before the Zoom call.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)

- `y01-0114` *STATED* — /geo <website link> audits how visible a website is to traditional search engines and to AI search engines.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *part-of* `y01-0113`
  ↳ *example-of* `y01-0089`

- `y01-0115` *STATED* — /geo content <website link> shows how the site can be optimized for GEO and AI - the fix, not just the audit.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *leads-to* `y01-0114`

- `y01-0116` *STATED* — /geo schema <website link> analyzes and generates the structured data that helps AI understand what the website is.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *part-of* `y01-0113`

- `y01-0117` *STATED* — /geo llms.txt <website> - which Alex calls the most important command - analyzes and generates an llms.txt file that makes the site's structure clearer for crawlers.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *part-of* `y01-0113`

- `y01-0118` *STATED* — /geo llms.txt also checks whether crawlers from companies like OpenAI, Anthropic (Claude) and Perplexity can access the website.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *part-of* `y01-0117`

- `y02-0040` *STATED* — Heist step 1: you hand over your app, and each member of the heist crew plans its break-in on its own (independently).
  > “each guy in the heist crew plans to break in on its own”
  — [VsD9g0sDNpY](https://youtu.be/VsD9g0sDNpY) [QC6Qzg-qHds](https://youtu.be/QC6Qzg-qHds) [iB8f2suhV04](https://youtu.be/iB8f2suhV04)
  ↳ *evidence-for* `g08-0080`
  ↳ *evidence-for* `r01-0016`
  ↳ *part-of* `y02-0039`

- `y02-0041` *STATED* — One heist-crew Claude tries to hack your code.
  — [VsD9g0sDNpY](https://youtu.be/VsD9g0sDNpY) [QC6Qzg-qHds](https://youtu.be/QC6Qzg-qHds) [iB8f2suhV04](https://youtu.be/iB8f2suhV04)
  ↳ *evidence-for* `g08-0081`
  ↳ *part-of* `y02-0040`

- `y02-0042` *STATED* — One heist-crew Claude tries to trick your users out of their login info (phishing / social engineering).
  — [VsD9g0sDNpY](https://youtu.be/VsD9g0sDNpY) [QC6Qzg-qHds](https://youtu.be/QC6Qzg-qHds) [iB8f2suhV04](https://youtu.be/iB8f2suhV04)
  ↳ *evidence-for* `g08-0082`
  ↳ *part-of* `y02-0040`

- `y02-0043` *STATED* — One heist-crew Claude pretends to be a user to try to steal other people's data (broken access control / data leakage).
  — [VsD9g0sDNpY](https://youtu.be/VsD9g0sDNpY) [QC6Qzg-qHds](https://youtu.be/QC6Qzg-qHds) [iB8f2suhV04](https://youtu.be/iB8f2suhV04)
  ↳ *evidence-for* `g08-0083`
  ↳ *part-of* `y02-0040`

- `y02-0044` *STATED* — The heist 'mastermind' Claude coordinates everything and actually breaks into your app.
  > “the mastermind coordinates everything and actually breaks into your app”
  — [VsD9g0sDNpY](https://youtu.be/VsD9g0sDNpY) [QC6Qzg-qHds](https://youtu.be/QC6Qzg-qHds) [iB8f2suhV04](https://youtu.be/iB8f2suhV04)
  ↳ *evidence-for* `g08-0084`
  ↳ *part-of* `y02-0039`
  ↳ *leads-to* `y02-0045`

- `y02-0066` *STATED* — Claude Jester step 1: you give it your idea and three yes-men Claudes agree with it.
  — [AJ0uGlJEL2U](https://youtu.be/AJ0uGlJEL2U) [BuoCqoRvG2U](https://youtu.be/BuoCqoRvG2U)
  ↳ *part-of* `y02-0063`
  ↳ *contrast* `y02-0067` — yes-men vs jester

- `y02-0067` *STATED* — Claude Jester step 2: the jester Claude steps in and tells you the biggest problems with your idea without sugarcoating anything.
  > “the jester Claude steps in and tells you the biggest problems with your idea without sugarcoating anything”
  — [AJ0uGlJEL2U](https://youtu.be/AJ0uGlJEL2U) [BuoCqoRvG2U](https://youtu.be/BuoCqoRvG2U)
  ↳ *contrast* `g08-0249`
  ↳ *part-of* `y02-0063`

- `y02-0070` *STATED* — In the 10-executive boardroom, the marketing head asks why anyone would care.
  — [5_QGHfYUT7c](https://youtu.be/5_QGHfYUT7c) [5IVs3Eg0rCs](https://youtu.be/5IVs3Eg0rCs)
  ↳ *evidence-for* `g09-0025`
  ↳ *part-of* `y02-0069`

- `y02-0071` *STATED* — In the 10-executive boardroom, the sales head asks where your first customers would even come from.
  — [5_QGHfYUT7c](https://youtu.be/5_QGHfYUT7c) [5IVs3Eg0rCs](https://youtu.be/5IVs3Eg0rCs)
  ↳ *evidence-for* `g09-0025`
  ↳ *part-of* `y02-0069`
  ↳ *analogy-for* `y02-0181` — who pays / where do first customers come from

- `y02-0072` *CORE* — In the boardroom each Claude executive thinks alone first, then they argue it out, so nobody just agrees with you like a yes-man.
  > “each one thinks alone first, then they argue it out so nobody just agrees with you like a yes man”
  — [5_QGHfYUT7c](https://youtu.be/5_QGHfYUT7c) [5IVs3Eg0rCs](https://youtu.be/5IVs3Eg0rCs)
  ↳ *evidence-for* `g09-0024`
  ↳ *evidence-for* `r01-0016`
  ↳ *part-of* `y02-0069`
  ↳ *evidence-for* `y02-0185`

- `y02-0077` *STATED* — Rebuild step: the Spy agent reverse-engineers the entire app — every screen and all the data behind it.
  — [Tvhn8L2lOL0](https://youtu.be/Tvhn8L2lOL0)
  ↳ *part-of* `y02-0075`
  ↳ *leads-to* `y02-0078`

- `y02-0078` *STATED* — Rebuild step: the Spy passes its findings to Bobby the Builder, who rebuilds the app screen by screen.
  — [Tvhn8L2lOL0](https://youtu.be/Tvhn8L2lOL0)
  ↳ *example-of* `g20-0197`
  ↳ *part-of* `y02-0075`
  ↳ *leads-to* `y02-0079`

- `y02-0079` *STATED* — Rebuild step: Isaac the Inspector tests what Bobby built for bugs and kills them.
  — [Tvhn8L2lOL0](https://youtu.be/Tvhn8L2lOL0)
  ↳ *part-of* `y02-0075`

- `y02-0080` *STATED* — Rebuild step: the Entrepreneur agent reads real user reviews and finds out what users hate, so you don't add those features into your app.
  — [Tvhn8L2lOL0](https://youtu.be/Tvhn8L2lOL0)
  ↳ *part-of* `y02-0075`
  ↳ *analogy-for* `y02-0154` — mining what customers hate vs asking simulated customers why they didn't buy

- `y02-0089` *STATED* — Every night an 'investigator' Claude comes in, figures out everything that went wrong, and remembers it for the future.
  > “every night, an investigator Claude comes in and figures out everything that went wrong and actually remembers it for the future”
  — [h0rtiWN_oIg](https://youtu.be/h0rtiWN_oIg) [3je0se5Ce_w](https://youtu.be/3je0se5Ce_w)
  ↳ *evidence-for* `r03-0009`
  ↳ *part-of* `y02-0086`
  ↳ *leads-to* `y02-0090`

- `y02-0094` *STATED* — In the updated Claude Projects you talk to the main chat like your chief of staff and it splits up the work for you.
  > “you just talk to it like you're chief of staff and it splits up the work for you”
  — [GF2xgaEnQ0o](https://youtu.be/GF2xgaEnQ0o) [g6ZnVE4kQCk](https://youtu.be/g6ZnVE4kQCk)
  ↳ *evidence-for* `g07-0182`
  ↳ *part-of* `y02-0092`

- `y02-0135` *STATED* — Launch-panel check: one Claude runs your tests.
  — [Bn4UhbHJzxo](https://youtu.be/Bn4UhbHJzxo) [7cYKEcBNFV4](https://youtu.be/7cYKEcBNFV4) [DE32ZPcENjY](https://youtu.be/DE32ZPcENjY)
  ↳ *evidence-for* `g09-0115`
  ↳ *part-of* `y02-0134`

- `y02-0136` *STATED* — Launch-panel check: one Claude hunts for security holes.
  — [Bn4UhbHJzxo](https://youtu.be/Bn4UhbHJzxo) [7cYKEcBNFV4](https://youtu.be/7cYKEcBNFV4) [DE32ZPcENjY](https://youtu.be/DE32ZPcENjY)
  ↳ *evidence-for* `g09-0116`
  ↳ *part-of* `y02-0134`
  ↳ *contrast* `y02-0039` — passive security check vs active red-team crew

- `y02-0137` *STATED* — Launch-panel check: one Claude checks your database.
  — [Bn4UhbHJzxo](https://youtu.be/Bn4UhbHJzxo) [7cYKEcBNFV4](https://youtu.be/7cYKEcBNFV4) [DE32ZPcENjY](https://youtu.be/DE32ZPcENjY)
  ↳ *evidence-for* `g09-0117`
  ↳ *part-of* `y02-0134`

- `y02-0138` *STATED* — Launch-panel check: one Claude checks your speed (performance).
  — [Bn4UhbHJzxo](https://youtu.be/Bn4UhbHJzxo) [7cYKEcBNFV4](https://youtu.be/7cYKEcBNFV4) [DE32ZPcENjY](https://youtu.be/DE32ZPcENjY)
  ↳ *evidence-for* `g09-0118`
  ↳ *part-of* `y02-0134`

- `y02-0139` *STATED* — Launch-panel check: one Claude checks the actual costs.
  — [Bn4UhbHJzxo](https://youtu.be/Bn4UhbHJzxo) [7cYKEcBNFV4](https://youtu.be/7cYKEcBNFV4) [DE32ZPcENjY](https://youtu.be/DE32ZPcENjY)
  ↳ *evidence-for* `g09-0119`
  ↳ *part-of* `y02-0134`

- `y02-0140` *CORE* — Launch rule: if even one Claude says no, your app doesn't launch (single-veto, unanimous GO).
  > “if even one Claude says no, your app doesn't launch”
  — [Bn4UhbHJzxo](https://youtu.be/Bn4UhbHJzxo) [7cYKEcBNFV4](https://youtu.be/7cYKEcBNFV4) [DE32ZPcENjY](https://youtu.be/DE32ZPcENjY)
  ↳ *evidence-for* `r02-0157`
  ↳ *part-of* `y02-0134`
  ↳ *enables* `y02-0141`

- `y02-0151` *STATED* — In MiroFish, Claude plays a crowd of customers with different ages, jobs and budgets.
  — [tQRaHRjRROk](https://youtu.be/tQRaHRjRROk) [fYrca_-P1NI](https://youtu.be/fYrca_-P1NI)
  ↳ *part-of* `y02-0148`
  ↳ *analogy-for* `y02-0169` — persona-varied Claude crowds

- `y02-0159` *STATED* — Night crew role: one worker builds new features.
  — [8Yo0i9jLCzY](https://youtu.be/8Yo0i9jLCzY)
  ↳ *evidence-for* `g09-0218`
  ↳ *part-of* `y02-0157`

- `y02-0160` *STATED* — Night crew role: one worker does market research to find potential customers.
  — [8Yo0i9jLCzY](https://youtu.be/8Yo0i9jLCzY)
  ↳ *part-of* `r04-0087`
  ↳ *part-of* `y02-0157`
  ↳ *analogy-for* `y02-0002` — Claude hunting customers

- `y02-0161` *STATED* — Night crew role: one worker tracks which parts of your app are working well and which aren't.
  — [8Yo0i9jLCzY](https://youtu.be/8Yo0i9jLCzY)
  ↳ *evidence-for* `g09-0222`
  ↳ *part-of* `y02-0157`

- `y02-0167` *STATED* — Court step: one Claude argues that your idea will fail and another Claude argues it will work.
  — [LpUuv9AtUTo](https://youtu.be/LpUuv9AtUTo) [a6Qw-Dg_SNk](https://youtu.be/a6Qw-Dg_SNk)
  ↳ *evidence-for* `g09-0165`
  ↳ *part-of* `y02-0165`
  ↳ *leads-to* `y02-0168`

- `y02-0168` *CORE* — Court step: 12 Claude jurors read both sides and vote guilty or not guilty without seeing each other's votes.
  > “12 Claude jurors read both sides and vote guilty or not guilty without seeing each other's votes”
  — [LpUuv9AtUTo](https://youtu.be/LpUuv9AtUTo) [a6Qw-Dg_SNk](https://youtu.be/a6Qw-Dg_SNk)
  ↳ *evidence-for* `r01-0165`
  ↳ *part-of* `y02-0165`
  ↳ *leads-to* `y02-0171`

- `y02-0169` *STATED* — Every court juror judges the idea as someone different, like an accountant, a customer or a competitor.
  — [LpUuv9AtUTo](https://youtu.be/LpUuv9AtUTo) [a6Qw-Dg_SNk](https://youtu.be/a6Qw-Dg_SNk)
  ↳ *evidence-for* `r01-0166`
  ↳ *part-of* `y02-0165`

- `y02-0171` *STATED* — Court step: a judge Claude reads the verdict and makes a decision.
  — [LpUuv9AtUTo](https://youtu.be/LpUuv9AtUTo) [a6Qw-Dg_SNk](https://youtu.be/a6Qw-Dg_SNk)
  ↳ *evidence-for* `r01-0168`
  ↳ *part-of* `y02-0165`

- `y02-0180` *STATED* — Shark panel: you pitch your idea (like your new app) and five sharks from the TV show tear into it.
  — [O-ngH7V3_U0](https://youtu.be/O-ngH7V3_U0)
  ↳ *evidence-for* `r04-0210`
  ↳ *part-of* `y02-0179`

- `y02-0181` *STATED* — In the Shark panel, Mark Cuban asks who is actually going to pay for it.
  — [O-ngH7V3_U0](https://youtu.be/O-ngH7V3_U0)
  ↳ *example-of* `r04-0211`
  ↳ *part-of* `y02-0180`

- `y02-0182` *STATED* — In the Shark panel, Kevin O'Leary only offers you money for a cut of every sale forever (a royalty deal).
  — [O-ngH7V3_U0](https://youtu.be/O-ngH7V3_U0)
  ↳ *example-of* `r04-0211`
  ↳ *part-of* `y02-0180`

- `y02-0186` *CORE* — Independence before discussion is a repeated design rule in his panels: court jurors vote without seeing each other's votes, board executives think alone first, and heist-crew members each plan their attack on their own.
  — [LpUuv9AtUTo](https://youtu.be/LpUuv9AtUTo) [a6Qw-Dg_SNk](https://youtu.be/a6Qw-Dg_SNk) [5_QGHfYUT7c](https://youtu.be/5_QGHfYUT7c) [5IVs3Eg0rCs](https://youtu.be/5IVs3Eg0rCs) [VsD9g0sDNpY](https://youtu.be/VsD9g0sDNpY) [QC6Qzg-qHds](https://youtu.be/QC6Qzg-qHds) [iB8f2suhV04](https://youtu.be/iB8f2suhV04)
  ↳ *evidence-for* `r01-0016`
  ↳ *generalizes* `y02-0168`
  ↳ *generalizes* `y02-0072`
  ↳ *generalizes* `y02-0040`

- `y02-0190` *CORE* — Autonomous Claude workers must be permission-gated: the night crew can't spend money, delete or touch the live app without permission, and Harvey runs only on your existing Claude plan with a live dashboard to watch it.
  — [8Yo0i9jLCzY](https://youtu.be/8Yo0i9jLCzY) [DYsc09LJB0o](https://youtu.be/DYsc09LJB0o)
  ↳ *evidence-for* `g09-0247`
  ↳ *generalizes* `y02-0162`
  ↳ *generalizes* `y02-0006`
  ↳ *generalizes* `y02-0007`

- `y04-0041` *STATED* — In the Darwin Loop, agents take your favourite version and create three improved variations of it.
  > “Agents take your favorite version and create three improved variations.”
  — [gUOs9YjmZDo](https://youtu.be/gUOs9YjmZDo)
  ↳ *evidence-for* `g13-0229`
  ↳ *analogy-for* `g21-0039`
  ↳ *part-of* `y04-0039`

- `y04-0046` *CORE* — Swarm Loop: instead of chatting back and forth, unleash three critic agents on Claude's answer: a skeptic, a beginner and a ruthless critic.
  > “Instead of chatting back and forth, unleash a skeptic to challenge claims, a beginner to flag confusing parts, and a ruthless critic to cut the fluff.”
  — [kDh_gdXsJJU](https://youtu.be/kDh_gdXsJJU) [PG_HanOn_KE](https://youtu.be/PG_HanOn_KE) [jw25LS4GgUg](https://youtu.be/jw25LS4GgUg)
  ↳ *evidence-for* `g16-0158`
  ↳ *contrast* `y04-0108` — role personas on one model vs two different models

- `y04-0064` *STATED* — After Jev triages the leads, Claude drafts replies only for the ones worth pursuing: the cheap model sorts, the expensive model writes.
  > “Then, Claude drafts replies for the ones worth pursuing”
  — [Hdc86XqcDWM](https://youtu.be/Hdc86XqcDWM) [N8_l0apeaQE](https://youtu.be/N8_l0apeaQE) [1FXRIeZ2-lE](https://youtu.be/1FXRIeZ2-lE)
  ↳ *evidence-for* `g22-0048`
  ↳ *depends-on* `y04-0063`
  ↳ *contrast* `y04-0071` — cheap triage then Claude writes vs cheap triage then human handles uncertain cases

- `y04-0071` *STATED* — Decision-plus-confidence routing: let AI handle the straightforward reports and send the uncertain ones to a real human.
  > “a business could handle straightforward reports with AI and send out uncertain ones to a real human”
  — [XgGitmLoaWM](https://youtu.be/XgGitmLoaWM)
  ↳ *example-of* `g09-0247`
  ↳ *leads-to* `y04-0073`

- `y04-0098` *STATED* — Give the 3D agent office a project brief and a team of AI agents walks into a 3D workspace and starts working.
  > “You give it a project brief and a team of AI agents walks into a 3D workspace and starts working.”
  — [A3XmoC6Ybws](https://youtu.be/A3XmoC6Ybws)
  ↳ *part-of* `y04-0097`

- `y04-0108` *STATED* — Split-skill phase 1: Fable writes a plan and Astro audits it, and they go back and forth until they agree.
  > “Fable writes a plan and Astro audits it, and then they go back and forth until they agree.”
  — [_gYzRT-j_ls](https://youtu.be/_gYzRT-j_ls)
  ↳ *evidence-for* `g06-0161`
  ↳ *part-of* `y04-0106`
  ↳ *leads-to* `y04-0109`

- `y04-0109` *STATED* — Split-skill phase 2: the models swap roles - Astro builds it and Fable 5 audits it.
  > “Then, they swap roles. Astro becomes the one to build it and Fable 5 audits it.”
  — [_gYzRT-j_ls](https://youtu.be/_gYzRT-j_ls)
  ↳ *evidence-for* `g06-0163`
  ↳ *part-of* `y04-0106`

### number

- `g02-0020` *STATED* — /hunter step 4: only jobs at or above your threshold go on; the default threshold is 80 out of 100 and you can change it.
  > “Only the jobs at or above your threshold (80 unless you change it) go on.”
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *leads-to* `g02-0022`
  ↳ *example-of* `g02-0243`
  ↳ *contrast* `g02-0106` — 80/100 vs 4.0/5 fit gates

- `g02-0154` *STATED* — claude-seo runs a full-site audit with up to 17 agents at once, 19 in total.
  — [g-have-claude-audit-your-whole-website-for-google](https://chen.media/guides/have-claude-audit-your-whole-website-for-google)
  ↳ *qualifies* `g02-0153`
  ↳ *example-of* `g02-0245`
  ↳ *contradicts* `g17-0107` — claude-seo parallelism: 'up to 17 agents at once, 19 in total' vs 'up to 15 specialist agents at once'
  ↳ *contradicts* `g17-0104` — claude-seo agent total: 19 agents vs 18 specialist agents

- `g04-0100` *STATED* — The /hiring-panel skill's seven Claudes are one automated screen, one hiring manager, and five readers who each judge the resume alone as someone different.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *part-of* `g04-0099`
  ↳ *evidence-for* `g08-0029`

- `g06-0023` *STATED* — On the /iq reader scale, 50 is the average adult, so most people land near the middle.
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *qualifies* `g06-0022`
  ↳ *evidence-for* `g07-0152`

- `g06-0089` *STATED* — Claude Code shows a 'Large workflow' warning when a run schedules more than 25 agents or projects over 1.5 million tokens.
  — [g-run-claude-agent-swarms-without-burning-your-limit](https://chen.media/guides/run-claude-agent-swarms-without-burning-your-limit)
  ↳ *qualifies* `g06-0085`
  ↳ *qualifies* `g11-0057` — Claude Code warns above 25 agents / 1.5M tokens; the tournament runs 100 Claudes

- `g07-0144` *STATED* — /brain-grade reads up to 320 of your messages.
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *part-of* `g07-0137`
  ↳ *part-of* `g07-0142`

- `g07-0152` *STATED* — In /brain-grade, 50 is the average adult, so most people land near the middle on most things.
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *part-of* `g07-0137`
  ↳ *qualifies* `g07-0151`

- `g11-0067` *STATED* — The tournament skill has 2,160 possible strategy cards, and no two Claudes get the same one.
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *qualifies* `g11-0063`

- `g11-0069` *STATED* — Each tournament Claude makes up to seven attacks, each labelled fatal, major or minor.
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *qualifies* `g11-0068`

- `g11-0075` *STATED* — The tournament bracket goes 100 → 50 → 25 → 13 → 7 → 4 → 2 → 1: seven rounds.
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *evidence-for* `g11-0074`

- `g11-0156` *STATED* — Dots connect to your apps; OpenAI says over 4,000 through plugins.
  — [g-get-your-own-chatgpt-dot](https://chen.media/guides/get-your-own-chatgpt-dot)
  ↳ *enables* `g11-0135`

- `g13-0275` *STATED* — Alex's Claudex Loop guide has 3 copyable prompts.
  — [g-split-claude-and-codex-with-claudex-loop](https://chen.media/guides/split-claude-and-codex-with-claudex-loop)
  ↳ *part-of* `g13-0268`

- `g15-0085` *STATED* — Munder Difflin runs on macOS, Windows and Linux and is marked pre-release at v0.4.6.
  — [g-munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents](https://chen.media/guides/munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents)
  ↳ *qualifies* `g15-0083`
  ↳ *evidence-for* `g15-0087` — pre-release v0.4.6

- `g15-0106` *STATED* — wshobson/agents ships 202 role-specific agents, each with its own instructions, its own conventions and its own definition of done.
  — [g-the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build](https://chen.media/guides/the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build)
  ↳ *part-of* `g15-0105`
  ↳ *evidence-for* `g18-0286`
  ↳ *evidence-for* `g17-0261`

- `g15-0108` *STATED* — wshobson/agents' 202 agents span architecture, languages, infrastructure, security, data, machine learning, docs, business and SEO.
  — [g-the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build](https://chen.media/guides/the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build)
  ↳ *qualifies* `g15-0106`

- `g15-0115` *STATED* — msitarzewski/agency-agents has over 149,000 stars and 24,000 forks, is MIT licensed and free.
  — [g-the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install](https://chen.media/guides/the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install)
  ↳ *evidence-for* `g15-0113`
  ↳ *contradicts* `g18-0271` — msitarzewski/agency-agents stars: 'over 149,000 stars' vs '137.4k stars'

- `g15-0116` *STATED* — The Agency holds 273 agents counted across 18 divisions.
  — [g-the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install](https://chen.media/guides/the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install)
  ↳ *part-of* `g15-0113`
  ↳ *contradicts* `g17-0258` — The Agency size: 273 agents vs 286 specialist agents (both 18 divisions)

- `g17-0080` *STATED* — github.com/anthropics/financial-services ships ten named agents, nine vertical plugin bundles and eleven data connectors.
  — [g-anthropic-s-ten-finance-agents-for-equity-research-and-modelling](https://chen.media/guides/anthropic-s-ten-finance-agents-for-equity-research-and-modelling)
  ↳ *part-of* `g17-0079`

- `g17-0107` *STATED* — A full Claude SEO site audit can spawn up to 15 specialist agents at once, which is why a site-level audit finishes in minutes instead of hours.
  — [g-install-25-seo-skills-and-18-specialist-agents-into-claude-code](https://chen.media/guides/install-25-seo-skills-and-18-specialist-agents-into-claude-code)
  ↳ *because* `g17-0101`
  ↳ *evidence-for* `g17-0099` — why ~15 minutes
  ↳ *example-of* `g02-0245`

- `g18-0210` *STATED* — Importing your first ready-made n8n workflow takes about four minutes.
  — [g-280-ready-made-n8n-automations-you-do-not-have-to-build](https://chen.media/guides/280-ready-made-n8n-automations-you-do-not-have-to-build)
  ↳ *part-of* `g18-0208`

- `g20-0190` *STATED* — The one-time council setup takes about 10 minutes.
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *part-of* `g20-0178`

- `g20-0202` *STATED* — The one-time dev-team setup takes about 15 minutes.
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *part-of* `g20-0196`

- `r01-0130` *STATED* — Each /hiring-panel reader answers in under 120 words: HIRE, MAYBE or PASS, the one line that hurt most (quoted), and two more problems.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *qualifies* `r01-0128`

- `r01-0141` *INFERRED* — /hiring-panel's eight calls are the automated screen, the hiring manager, five readers, and the second automated screen on the rebuilt resume.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *defines* `r01-0140`
  ↳ *qualifies* `g08-0029` — repo counts 8 calls (1 screen + 1 manager + 5 readers + rescreen) while guides say 7 Claudes; the 8th is the before/after re-screen
  ↳ *because* `g08-0044`

- `r04-0183` *STATED* — Default night crew schedule for someone asleep 11pm to 7am: builder 1:07am, scout 2:07am, tracker 5:07am (the tracker goes last so it can check the builder's pull request).
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)

- `y02-0076` *STATED* — The rebuild system has 11 free Claude agents, each with a specific job (the video names four: the Spy, Bobby the Builder, Isaac the Inspector and the Entrepreneur).
  > “this rebuild has 11 free Claude agents, and each one does a specific job”
  — [Tvhn8L2lOL0](https://youtu.be/Tvhn8L2lOL0)
  ↳ *part-of* `y02-0075`

- `y02-0158` *STATED* — The night crew gets you an additional 8 hours of work done by the time you wake up.
  — [8Yo0i9jLCzY](https://youtu.be/8Yo0i9jLCzY)
  ↳ *contradicts* `r04-0205` — video: night crew gives 'an additional 8 hours of work' done by morning vs repo: 'Never promise the night crew will finish everything: one backlog item a night is a good night'
  ↳ *part-of* `y02-0157`

- `y03-0016` *STATED* — A Claude Code agent team uses about 7 times more tokens than a normal session.
  — [Rgb7FFLwz60](https://youtu.be/Rgb7FFLwz60)
  ↳ *qualifies* `g20-0233` — an agent team uses ~7x the tokens of a normal session
  ↳ *evidence-for* `g06-0084`
  ↳ *part-of* `y03-0012`
  ↳ *qualifies* `y03-0043` — ultracode's dozens of Claudes is an agent-team-style multiplier on tokens

### opinion

- `g02-0237` *CORE* — The tools Alex features keep a human approval gate: they draft, plan or prepare but never send, post or apply without your yes (/hunter applications, career-ops LinkedIn notes, Atticus replies, GoLive plans, github-triage merges and reviews, Video Use's agreed plan).
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill) [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi) [g-control-your-whole-mac-with-your-voice-powered-by-claude](https://chen.media/guides/control-your-whole-mac-with-your-voice-powered-by-claude) [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive) [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say) [g-video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video](https://chen.media/guides/video-use-drop-raw-clips-in-a-folder-and-claude-edits-the-finished-video)
  ↳ *evidence-for* `g09-0247`

- `g09-0163` *STATED* — One friendly answer is the worst kind of feedback, because it never shows you the case against you.
  > “One friendly answer is the worst kind of feedback, because it never shows you the case against you.”
  — [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill)
  ↳ *qualifies* `g09-0161`
  ↳ *generalizes* `g09-0020`

- `g13-0227` *STATED* — A clear comparison and a stopping point matter more than the number of agents you run.
  > “A clear comparison and a stopping point matter more than the number of agents you run.”
  — [g-darwin-loop-evolve-the-winner](https://chen.media/guides/darwin-loop-evolve-the-winner)
  ↳ *qualifies* `g13-0222`
  ↳ *qualifies* `g11-0057` — 'a clear comparison and a stopping point matter more than the number of agents' vs 100-Claude tournament

- `g15-0089` *STATED* — Munder Difflin's permission gate, which stops the agents at the door you tell them to, is the feature, not the friction.
  > “That gate is the feature, not the friction.”
  — [g-munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents](https://chen.media/guides/munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents)
  ↳ *part-of* `g15-0088`
  ↳ *example-of* `g15-0182`
  ↳ *example-of* `g09-0247`
  ↳ *evidence-for* `r04-0164`

- `g15-0114` *STATED* — The Agency is worth your time not for its count but because somebody already did the boring half: deciding what a Reddit Community Builder should care about that a Frontend Developer should not, and writing that difference down.
  — [g-the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install](https://chen.media/guides/the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install)
  ↳ *qualifies* `g15-0113`

- `g18-0075` *STATED* — Narrow specialist agents beat one big prompt.
  > “Why Narrow Beats One Big Prompt”
  — [g-an-entire-ai-company-in-one-repo-eight-departments](https://chen.media/guides/an-entire-ai-company-in-one-repo-eight-departments)
  ↳ *contrast* `g18-0213` — specialist agents vs hand-written role brief every chat
  ↳ *evidence-for* `g18-0286`

- `g19-0211` *STATED* — Stop running Claude as one model answering once.
  > “Stop running Claude as one model answering once”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)
  ↳ *because* `g19-0194`

- `g20-0031` *STATED* — Get the brain right first, because a JARVIS with hands and no memory of you is just a chatbot with extra permissions.
  > “a JARVIS with hands and no memory of you is just a chatbot with extra permissions.”
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *qualifies* `g20-0030`
  ↳ *evidence-for* `g20-0286`

- `g20-0102` *STATED* — For best-of-N runs, three attempts is thin and ten is noise you will not read.
  > “Three is thin. Ten is noise you will not read.”
  — [g-run-the-job-five-times-and-let-a-blind-grader-pick](https://chen.media/guides/run-the-job-five-times-and-let-a-blind-grader-pick)
  ↳ *qualifies* `g20-0101`
  ↳ *contradicts* `g11-0057` — best-of-N size: 'three attempts is thin and ten is noise you will not read' vs a tournament of 100 Claudes (16 in quick mode)
  ↳ *contradicts* `g21-0033` — best-of-N size: 'ten is noise' vs a bracket of 20 versions

- `g20-0189` *STATED* — Persistent single-lens agents are the difference between a yes-man and a council.
  > “That is the difference between a yes-man and a council.”
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *qualifies* `g20-0188`
  ↳ *evidence-for* `g20-0201`

- `g20-0201` *STATED* — Giving each dev agent its own space (a Project, a subagent, or a saved instruction set) keeps its role and rules always on, and is the difference between a chatbot and a dev team.
  > “That is the difference between a chatbot and a dev team.”
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *enables* `g20-0198`
  ↳ *part-of* `g20-0285`
  ↳ *example-of* `g20-0289`

- `r04-0164` *CORE* — Rules in a prompt are instructions; the guardrails are what actually stop a mistake.
  > “Rules in a prompt are instructions; the guardrails are what actually stop a mistake.”
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *evidence-for* `r04-0019`
  ↳ *qualifies* `r04-0163`
  ↳ *because* `r04-0097`

- `y04-0104` *STATED* — We've always seen AI as text, but agent visualisers like the 3D office turn it into something visual.
  > “We've always seen AI as text, but this turns into something visual.”
  — [A3XmoC6Ybws](https://youtu.be/A3XmoC6Ybws)
  ↳ *qualifies* `y04-0105`
  ↳ *because* `y04-0102`

### product

- `g02-0001` *CORE* — /hunter is a free Claude Code skill that works as a headhunter made of five Claudes: it finds jobs that fit you and prepares the applications.
  > “This free Claude Code skill is a headhunter made of five Claudes”
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *because* `g02-0002`
  ↳ *contrast* `g02-0098` — daily 5-Claude autopilot vs paste-a-job agent

- `g03-0196` *STATED* — Roast Room is a free, open-source Claude Code skill: you bring a hard business decision and seven Claude advisors argue it out, score every option and hand you a verdict.
  — [g-roast-room-a-free-claude-council-that-argues-over-your-business-decisions](https://chen.media/guides/roast-room-a-free-claude-council-that-argues-over-your-business-decisions)

- `g06-0158` *CORE* — Pair is a free Claude Code skill that splits one job between two models: Claude plans and Codex audits, then they swap and Codex builds while Claude audits.
  — [g-pair-make-claude-and-codex-check-each-other-s-work](https://chen.media/guides/pair-make-claude-and-codex-check-each-other-s-work)
  ↳ *because* `g06-0159`

- `g07-0052` *CORE* — Alex's free AI-agency Claude Code skill gives each agency job to an agent: one writes personal emails to every business on your list, one preps and coaches sales calls, one writes the proposal and builds the automation, one answers client emails, and a night shift works the queue.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0073`

- `g07-0137` *STATED* — /brain-grade is a free Claude Code skill that grades how smart you are from your own past chats, using five judges and a coach.
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)

- `g07-0246` *STATED* — /linkedin-roast is a free Claude Code skill that puts your LinkedIn profile in front of five Claudes that roast it alone, each as someone different, then fixes it.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *evidence-for* `r03-0134`

- `g08-0028` *CORE* — The free /hiring-panel Claude Code skill puts your resume in front of a hiring panel of seven Claudes that try to reject it.
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill)
  ↳ *example-of* `g08-0250`

- `g08-0073` *CORE* — The free /heist Claude Code skill sends a crew of five roles through your code the way a thief would: a scout, three attackers that go after your code, your users and your data, and a mastermind that chains what they find into one report.
  — [g-give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes](https://chen.media/guides/give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes)
  ↳ *example-of* `g08-0250`
  ↳ *qualifies* `y02-0046` — guide names the 5th role: a scout that maps the app (plus 3 attackers and a mastermind); the video named only the attackers and mastermind

- `g08-0204` *STATED* — An Agent Office puts each Claude Code session at its own desk, with a status you can read at a glance: working, waiting on you, or done.
  — [g-see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office](https://chen.media/guides/see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office)
  ↳ *evidence-for* `y04-0105`

- `g08-0220` *STATED* — The free /rival Claude Code skill has five rival Claudes each write a plan to take your customers, then a judge picks the plan that would hurt most and tells you what to fix first.
  — [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill)
  ↳ *example-of* `g08-0250`

- `g09-0017` *CORE* — The free Boardroom is a Claude Code setup that puts your idea in front of a whole board of Claude executives (a CEO, a CFO, marketing, sales, product and more) before you build it.
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives)
  ↳ *part-of* `g09-0015`
  ↳ *because* `g09-0016`
  ↳ *because* `g09-0019`
  ↳ *example-of* `g09-0254`
  ↳ *evidence-for* `y02-0069`

- `g09-0110` *STATED* — Alex's free Claude Code launch-poll skill runs a NASA-style launch poll: eight Claudes each check one part of your app, and if even one says no, it doesn't launch.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *part-of* `g09-0108`
  ↳ *because* `g09-0109`
  ↳ *example-of* `g09-0254`
  ↳ *evidence-for* `r02-0118`

- `g09-0147` *STATED* — Alex's free Claude Code shark skill puts your idea in front of five Claude investors who grill it, decide in or out, and hand you the questions you couldn't answer.
  — [g-pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill](https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill)
  ↳ *part-of* `g09-0145`
  ↳ *because* `g09-0149`
  ↳ *contrast* `g09-0162` — five investors deciding IN/OUT vs twelve jurors voting guilty/not guilty
  ↳ *example-of* `g09-0254`
  ↳ *evidence-for* `r04-0206`

- `g09-0162` *STATED* — Alex's free Claude Code court skill makes Claude argue with itself: a prosecutor, a defense, twelve jurors who each see your idea through different eyes, and a judge who tells you what would flip the verdict.
  — [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill)
  ↳ *part-of* `g09-0160`
  ↳ *because* `g09-0163`
  ↳ *example-of* `g09-0254`
  ↳ *evidence-for* `r01-0157`

- `g09-0213` *STATED* — Alex's free Claude Code night-crew skill sets up three cloud workers: one builds the next feature, one finds people who need it, one checks what works.
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)
  ↳ *part-of* `g09-0211`
  ↳ *because* `g09-0212`
  ↳ *evidence-for* `r04-0087`

- `g11-0057` *STATED* — A free Claude Code skill gives your question to 100 Claudes at once, each thinking about it a different way, makes them attack each other's answers in a bracket, and hands back the one answer that beat all the others.
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *example-of* `g11-0008` — 'Get a better winner' section

- `g11-0143` *STATED* — Codex in the cloud lets you start a coding task from any device, and it runs on a cloud machine, not yours.
  — [g-let-chatgpt-fix-your-apps-bugs-while-you-sleep](https://chen.media/guides/let-chatgpt-fix-your-apps-bugs-while-you-sleep)
  ↳ *evidence-for* `g11-0140`

- `g11-0144` *STATED* — Codex Security Cloud scans GitHub repositories and "prepares fixes in the cloud, even with your laptop closed".
  > “prepares fixes in the cloud, even with your laptop closed”
  — [g-let-chatgpt-fix-your-apps-bugs-while-you-sleep](https://chen.media/guides/let-chatgpt-fix-your-apps-bugs-while-you-sleep)
  ↳ *evidence-for* `g11-0140`

- `g13-0254` *STATED* — The Delegation is a browser-based playground where AI agents work inside a shared 3D office (the app in Alex's OFFICE reel).
  — [g-give-ai-agents-an-office-the-delegation](https://chen.media/guides/give-ai-agents-an-office-the-delegation)

- `g13-0268` *STATED* — Claudex Loop brings Claude Code and Codex into the same development process; it is the repository behind Alex's SPLIT reel.
  — [g-split-claude-and-codex-with-claudex-loop](https://chen.media/guides/split-claude-and-codex-with-claudex-loop)

- `g13-0273` *STATED* — Claudex Route is a separate, lighter skill for a model recommendation or a single handoff between Claude and Codex.
  — [g-split-claude-and-codex-with-claudex-loop](https://chen.media/guides/split-claude-and-codex-with-claudex-loop)
  ↳ *contrast* `g13-0268`
  ↳ *contrast* `g13-0186` — Claudex Route recommends a model; Jev routes tasks between models

- `g14-0242` *STATED* — Claude Octopus is a Claude Code plugin that brings additional model perspectives into a Claude Code workflow as a council.
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *part-of* `g14-0241`

- `g15-0065` *STATED* — herdrdev/herdr (Apache 2.0, over 35,000 stars) is a terminal workspace that runs your coding agents in their own panes and tells you which one is stuck.
  — [g-four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute](https://chen.media/guides/four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute)
  ↳ *part-of* `g15-0061`
  ↳ *enables* `g15-0066`
  ↳ *contrast* `g15-0079` — both manage several coding agents: herdr panes vs Munder Difflin office
  ↳ *evidence-for* `y04-0105`

- `g15-0072` *STATED* — FoundationAgents/MetaGPT is an open-source multi-agent framework; verified 2026-09-04 on the GitHub API: 70,211 stars, 8,924 forks, MIT licence, Python.
  — [g-metagpt-one-line-in-a-whole-software-company-out](https://chen.media/guides/metagpt-one-line-in-a-whole-software-company-out)
  ↳ *example-of* `g15-0176`
  ↳ *qualifies* `g15-0185`

- `g15-0079` *STATED* — Munder Difflin is a desktop app, not a prompt pack: it opens a small 2D office where every character at a desk is a real command-line agent running on your own machine.
  — [g-munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents](https://chen.media/guides/munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents)
  ↳ *example-of* `g15-0179`

- `g15-0105` *STATED* — wshobson/agents (github.com/wshobson/agents, 39.4k stars, free) is a marketplace of specialized Claude Code agents that fixes the shape of the problem rather than the prompt.
  — [g-the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build](https://chen.media/guides/the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build)
  ↳ *example-of* `g15-0183`

- `g15-0113` *CORE* — The Agency (github.com/msitarzewski/agency-agents) is a public repo of AI specialists, not prompt templates or a starter pack: each is a written character with a name, a domain, a working process and a stated definition of done, and drops into Claude Code as an agent you call by name.
  — [g-the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install](https://chen.media/guides/the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install)
  ↳ *example-of* `g15-0183`
  ↳ *example-of* `g15-0179`

- `g15-0157` *STATED* — Jules is the Google AI tool that works while you sleep, such as clearing a pull request backlog overnight.
  — [g-the-four-google-ai-tools-worth-your-time](https://chen.media/guides/the-four-google-ai-tools-worth-your-time)
  ↳ *example-of* `g15-0156`
  ↳ *example-of* `g20-0288`

- `g16-0292` *STATED* — Ruflo is an agent harness that runs Claude Code as a swarm instead of a single session.
  > “the agent harness that runs Claude Code as a swarm instead of a single session”
  — [g-ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm](https://chen.media/guides/ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm)
  ↳ *example-of* `g16-0001`

- `g17-0258` *STATED* — The Agency (repo msitarzewski/agency-agents) is an open-source roster of 286 specialist agents across 18 divisions, usable free inside Claude Code.
  — [g-286-specialist-ai-agents-free-inside-claude-code](https://chen.media/guides/286-specialist-ai-agents-free-inside-claude-code)
  ↳ *evidence-for* `g15-0113`
  ↳ *contradicts* `g15-0116` — The Agency size: 286 agents across 18 divisions vs 273 agents counted across 18 divisions
  ↳ *evidence-for* `g08-0089`

- `g18-0001` *STATED* — ECC is an open source agent harness by Affaan Mustafa that installs 67 specialist agents, 281 skills and 94 commands into the AI tool you already have open.
  — [g-67-agents-281-skills-and-94-commands-in-one-install](https://chen.media/guides/67-agents-281-skills-and-94-commands-in-one-install)
  ↳ *example-of* `g18-0286`

- `g18-0015` *STATED* — Rowboat is an open source agent tool from Rowboat Labs, a Y Combinator S24 company founded by Arjun Maheswaran and Ramnique Singh.
  — [g-the-open-source-agent-tool-two-yc-founders-gave-away](https://chen.media/guides/the-open-source-agent-tool-two-yc-founders-gave-away)

- `g18-0169` *STATED* — Plugin 4 of 5: code-review, which runs four review agents at once.
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *part-of* `g18-0154`
  ↳ *depends-on* `g18-0158` — code-review lives in claude-plugins-official
  ↳ *example-of* `g18-0075` — parallel specialised reviewers
  ↳ *evidence-for* `g20-0284`

- `g18-0271` *STATED* — Agency Agents: msitarzewski/agency-agents, 137.4k stars, MIT, the most-starred of the seven.
  — [g-seven-free-repos-that-replace-paid-ai-tools](https://chen.media/guides/seven-free-repos-that-replace-paid-ai-tools)
  ↳ *part-of* `g18-0262`
  ↳ *example-of* `g18-0286`
  ↳ *evidence-for* `g15-0113`

- `g18-0275` *STATED* — Orca: stablyai/orca, 32.2k stars, MIT.
  — [g-seven-free-repos-that-replace-paid-ai-tools](https://chen.media/guides/seven-free-repos-that-replace-paid-ai-tools)
  ↳ *part-of* `g18-0262`

- `g19-0108` *STATED* — Activepieces (23k stars), which Alex calls 'the clever one', is tool 5 of 5, the repo that lets Claude run your week while you sleep.
  > “Activepieces · 23k stars (the clever one)”
  — [g-five-free-repos-that-give-claude-actual-hands](https://chen.media/guides/five-free-repos-that-give-claude-actual-hands)
  ↳ *part-of* `g19-0101`
  ↳ *example-of* `g19-0031` — automation
  ↳ *evidence-for* `g20-0288`

- `g19-0159` *STATED* — Task Master: https://github.com/eyaltoledano/claude-task-master.
  > “Repo: https://github.com/eyaltoledano/claude-task-master”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *part-of* `g19-0155`

- `r01-0027` *STATED* — /shark (github.com/alexyc9381/shark-skill): pitch your business idea to a Shark Tank of 5 Claude sharks who want to say no.
  — [r-alexyc9381](https://github.com/alexyc9381/alexyc9381)
  ↳ *part-of* `r01-0026`
  ↳ *contrast* `r01-0157` — 5 sharks who want to say no vs 12-juror trial
  ↳ *evidence-for* `r04-0206`

- `r01-0029` *STATED* — /court (github.com/alexyc9381/court-skill): put your idea on trial with a prosecutor Claude, a defense Claude, 12 juror Claudes who vote on their own, and a judge.
  — [r-alexyc9381](https://github.com/alexyc9381/alexyc9381)
  ↳ *part-of* `r01-0026`
  ↳ *defines* `r01-0157` — profile blurb for the court repo

- `r01-0030` *STATED* — /night-crew (github.com/alexyc9381/night-crew-skill): a night crew for your app — three Claude Code routines that build the next feature, find customers and check what works while you sleep.
  — [r-alexyc9381](https://github.com/alexyc9381/alexyc9381)
  ↳ *part-of* `r01-0026`
  ↳ *contrast* `r01-0048` — night routines for an app vs agency night shift
  ↳ *evidence-for* `r04-0087`

- `r01-0032` *STATED* — /launch (github.com/alexyc9381/launch-skill): launch your app the way NASA launches a rocket, with 8 Claude flight controllers checking tests, security, the database, speed, cost, your users' path, recovery and the rules.
  — [r-alexyc9381](https://github.com/alexyc9381/alexyc9381)
  ↳ *part-of* `r01-0026`
  ↳ *evidence-for* `r02-0118`

- `r01-0157` *CORE* — The /court skill (github.com/alexyc9381/court-skill): when Claude agrees with everything you say, put your idea on trial in front of a jury of 12 Claudes.
  > “When Claude agrees with everything you say, put your idea on trial in front of a jury of 12 Claudes.”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0001`

- `r02-0118` *CORE* — /launch (github.com/alexyc9381/launch-skill) launches your app the way NASA launches a rocket: 8 Claudes each check one part of it, and all 8 have to say GO.
  > “Launch your app the way NASA launches a rocket: 8 Claudes each check one part of it, and all 8 have to say GO.”
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)

- `r03-0134` *CORE* — The /linkedin-roast skill (github.com/alexyc9381/linkedin-roast-skill) has five Claudes roast your LinkedIn profile, each one alone: a recruiter, a hiring manager, a founder, an expert in your field and a peer at your level.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *depends-on* `r03-0003` — made by

- `r04-0087` *CORE* — /night-crew (github.com/alexyc9381/night-crew-skill) gives your app a night crew: three Claude Code workers that run in the cloud every night while you sleep and leave you pull requests to review in the morning.
  > “Give your app a night crew: three Claude Code workers that run in the cloud every night while you sleep”
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)

- `r04-0206` *CORE* — /shark (github.com/alexyc9381/shark-skill): when Claude says your business idea is great, put it in front of a Shark Tank where every shark is a Claude, and they all want to say no.
  > “put it in front of a Shark Tank where every shark is a Claude, and they all want to say no.”
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *because* `r04-0209`

- `y02-0039` *STATED* — Alex Chen built a 'heist crew' of five Claudes that tries to hack into your vibe-coded app (CTA keyword 'heist').
  > “I built a heist crew of five Claudes that tries to hack into your vibe coded app”
  — [VsD9g0sDNpY](https://youtu.be/VsD9g0sDNpY) [QC6Qzg-qHds](https://youtu.be/QC6Qzg-qHds) [iB8f2suhV04](https://youtu.be/iB8f2suhV04)
  ↳ *evidence-for* `g08-0073`

- `y02-0063` *STATED* — Alex Chen built a free 'Claude Jester' skill that isn't afraid of telling the brutal truth about your idea (CTA keyword 'jester').
  > “I built a Claude Jester that isn't afraid of telling the brutal truth about your idea.”
  — [AJ0uGlJEL2U](https://youtu.be/AJ0uGlJEL2U) [BuoCqoRvG2U](https://youtu.be/BuoCqoRvG2U)
  ↳ *evidence-for* `g08-0176`
  ↳ *example-of* `y02-0185`

- `y02-0069` *STATED* — A free 20,000-star repo lets you run your business idea past 10 Claude executives before you waste 6 months building an idea nobody wants (CTA keyword 'board').
  > “you can run your business idea past 10 Claude executives before you waste 6 months building an idea nobody wants. The repo has 20,000 stars”
  — [5_QGHfYUT7c](https://youtu.be/5_QGHfYUT7c) [5IVs3Eg0rCs](https://youtu.be/5IVs3Eg0rCs)

- `y02-0075` *STATED* — Alex Chen built a 'Claude Spy' (CTA keyword 'rebuild') that reverse-engineers any app you pay for, 'so you never pay a single subscription again'.
  > “I built a Claude Spy that reverse-engineers any app you pay for, so you never pay a single subscription again.”
  — [Tvhn8L2lOL0](https://youtu.be/Tvhn8L2lOL0)

- `y02-0134` *STATED* — The free launch repo has 8 Claudes that each check one part of your launch, and all 8 must say GO (CTA keyword 'launch'; the video names five of the eight checks).
  > “this repo has eight Claudes where each check one part of your launch, and all eight must say go”
  — [Bn4UhbHJzxo](https://youtu.be/Bn4UhbHJzxo) [7cYKEcBNFV4](https://youtu.be/7cYKEcBNFV4) [DE32ZPcENjY](https://youtu.be/DE32ZPcENjY)
  ↳ *evidence-for* `r02-0118`
  ↳ *example-of* `y02-0185`

- `y02-0157` *STATED* — Alex Chen built a free 'night crew' of Claude workers that code while you sleep (CTA keyword 'night').
  > “I built a night crew of Claude workers that literally code in your sleep”
  — [8Yo0i9jLCzY](https://youtu.be/8Yo0i9jLCzY)
  ↳ *evidence-for* `r04-0087`
  ↳ *evidence-for* `g20-0288`

- `y02-0165` *STATED* — Alex Chen built a free courtroom where 12 Claudes put your idea on trial (CTA keyword 'court').
  > “I built a courtroom where 12 Claudes put your idea on trial.”
  — [LpUuv9AtUTo](https://youtu.be/LpUuv9AtUTo) [a6Qw-Dg_SNk](https://youtu.be/a6Qw-Dg_SNk)
  ↳ *evidence-for* `r01-0157`
  ↳ *example-of* `y02-0185`

- `y02-0179` *STATED* — Alex Chen's free Claude skill turns Claude into a Shark Tank panel that destroys your idea (CTA: 'Comment SHARK and I'll DM you the free Claude skill').
  > “you can turn Claude into a shark tank and destroy your idea”
  — [O-ngH7V3_U0](https://youtu.be/O-ngH7V3_U0)
  ↳ *evidence-for* `r04-0206`
  ↳ *example-of* `y02-0185`

- `y04-0097` *STATED* — An open-source GitHub project gives your AI agents an actual 3D office to work in.
  > “Imagine giving your AI agents an actual office to work in. Someone on GitHub just built this.”
  — [A3XmoC6Ybws](https://youtu.be/A3XmoC6Ybws)
  ↳ *evidence-for* `g13-0254`
  ↳ *example-of* `y04-0151`

- `y04-0106` *STATED* — A free open-sourced skill (CTA 'split') runs two frontier models together, Fable 5.1 and GPT Astro (names as transcribed; the video also says 'Fable 5' and 'Astro 6').
  > “Someone just open-sourced a skill that lets you run Fable 5.1 and GPT Astro and the outputs are crazy good.”
  — [_gYzRT-j_ls](https://youtu.be/_gYzRT-j_ls)
  ↳ *evidence-for* `g06-0158`
  ↳ *example-of* `y04-0151`

### resource

- `g02-0028` *STATED* — The /hunter guide's email-gated sections are titled Get the skill, Set it up once, Run it, Every morning, What an answer looks like, and Good to know.
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *part-of* `g02-0007`
  ↳ *example-of* `g02-0234`

- `g04-0211` *STATED* — Guide: 'Make Your Claude Helper Agents Compact Their Own Chat Early' at https://chen.media/guides/make-your-claude-helper-agents-compact-their-own-chat-early (1 prompt, 4 steps).
  — [g-make-your-claude-helper-agents-compact-their-own-chat-early](https://chen.media/guides/make-your-claude-helper-agents-compact-their-own-chat-early)
  ↳ *example-of* `g04-0243`

- `g05-0175` *STATED* — Subagent file to copy (.claude/agents/renamer.md): frontmatter 'name: renamer', 'description: Renames files and symbols across the repo. Use for small mechanical edits.', 'effort: low'.
  > “---
name: renamer
description: Renames files and symbols across the repo. Use for small mechanical edits.
effort: low
---”
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)
  ↳ *example-of* `g05-0167`
  ↳ *example-of* `g05-0321`

- `g07-0156` *STATED* — The /brain-grade report is saved as .brain-grade/<date>/REPORT.md.
  — [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *part-of* `g07-0137`
  ↳ *part-of* `g07-0146`

- `g09-0015` *STATED* — chen.media guide 'Run Your Idea Past a Board of 10 Claude Executives Before You Build It: How to Set Up the Free Boardroom' (https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives) has 2 prompts to copy and 5 numbered steps; sections: How the board meeting works; Set it up; Run your first meeting; Good questions to bring; Why it works.
  — [g-run-your-idea-past-a-board-of-10-claude-executives](https://chen.media/guides/run-your-idea-past-a-board-of-10-claude-executives)
  ↳ *example-of* `g09-0253`

- `g09-0108` *STATED* — chen.media guide 'Launch Your App the Way NASA Launches a Rocket: The Free Claude Skill Where 8 Claudes Must Say GO' (https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill) has 7 prompts to copy and 4 numbered steps; sections: How the launch poll works; Get the skill; Run it before you launch; Ready-made launch polls; A real launch poll; Good to know.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *example-of* `g09-0253`

- `g09-0128` *STATED* — The launch-poll guide ships ready-made launch polls and walks through a real launch poll.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *part-of* `g09-0108`
  ↳ *example-of* `g09-0249`

- `g09-0145` *STATED* — chen.media guide 'Pitch Your Idea to a Panel of Claude Sharks Who Want to Say No: How to Install the Free Skill' (https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill) has 9 prompts to copy and 3 numbered steps; sections: What happens when you pitch; Get the skill; Pitch your idea; Six ready-made pitches; A real session; Good to know.
  — [g-pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill](https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill)
  ↳ *example-of* `g09-0253`

- `g09-0158` *STATED* — The shark guide ships six ready-made pitches and a real session.
  — [g-pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill](https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill)
  ↳ *part-of* `g09-0145`
  ↳ *example-of* `g09-0249`

- `g09-0160` *STATED* — chen.media guide 'Put Your Idea on Trial in Front of a Jury of 12 Claudes: How to Install the Free Skill' (https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill) has 10 prompts to copy and 4 numbered steps; sections: How the trial works; Get the skill; Start a trial; Seven ready-made trials; A real verdict; Good to know.
  — [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill)
  ↳ *example-of* `g09-0253`

- `g09-0174` *STATED* — The court guide ships seven ready-made trials and a real verdict.
  — [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill)
  ↳ *part-of* `g09-0160`
  ↳ *example-of* `g09-0249`

- `g09-0211` *STATED* — chen.media guide 'Give Your App a Night Crew: The Free Claude Skill That Builds, Finds Customers and Checks Your App While You Sleep' (https://chen.media/guides/free-claude-night-crew-skill) has 7 prompts to copy and 8 numbered steps; sections: What the night crew does; What you need; Get the skill; Set it up in about ten minutes; Why it can't spend money, delete anything or touch your live app; What you wake up to; Backlogs to start from; Good to know.
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)
  ↳ *example-of* `g09-0253`

- `g09-0227` *STATED* — The night-crew guide ships backlogs to start from.
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)
  ↳ *enables* `g09-0218`
  ↳ *example-of* `g09-0249`

- `g13-0240` *STATED* — Darwin Loop guide section: 'What Anthropic's loop guidance supports'.
  — [g-darwin-loop-evolve-the-winner](https://chen.media/guides/darwin-loop-evolve-the-winner)
  ↳ *qualifies* `g13-0222`

- `g13-0260` *STATED* — Alex's Delegation guide links the official app ('Launch The Delegation') and its official GitHub repository.
  — [g-give-ai-agents-an-office-the-delegation](https://chen.media/guides/give-ai-agents-an-office-the-delegation)
  ↳ *part-of* `g13-0254`

- `g14-0001` *STATED* — Alex Chen's chen.media guide 'Build a Marketing Workflow with Research, Writing and Review' (category: Agent teams) accompanies his MK and MAR videos and promises a brand brief, focused handoffs, reusable prompts and a documented example implementation.
  > “The MK and MAR workflow: a brand brief, focused handoffs, reusable prompts and a documented example implementation.”
  — [g-marketing-agent-workflow-setup](https://chen.media/guides/marketing-agent-workflow-setup)
  ↳ *example-of* `g14-0346`

- `g14-0013` *STATED* — The marketing workflow guide includes a documented example implementation you can install.
  > “A documented example you can install”
  — [g-marketing-agent-workflow-setup](https://chen.media/guides/marketing-agent-workflow-setup)
  ↳ *part-of* `g14-0001`

- `g14-0241` *STATED* — Alex's 'Claude Octopus Setup Guide: Make AI Models Challenge Your Code' covers installing Claude Octopus, running a focused council, and practical prompts for building, code review and security checks.
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *example-of* `g14-0353`

- `g14-0264` *STATED* — The Claude Octopus guide includes troubleshooting for when the workflow does not start, a 'first useful run', and official project references.
  > “When the workflow does not start”
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *part-of* `g14-0241`

- `g15-0073` *STATED* — MetaGPT describes itself as the first AI software company.
  > “The Multi-Agent Framework: First AI Software Company, Towards Natural Language Programming”
  — [g-metagpt-one-line-in-a-whole-software-company-out](https://chen.media/guides/metagpt-one-line-in-a-whole-software-company-out)
  ↳ *defines* `g15-0072`

- `g15-0083` *STATED* — Munder Difflin lives at github.com/chaitanyagiri/munder-difflin and had 6,161 stars when the guide was written.
  — [g-munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents](https://chen.media/guides/munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents)
  ↳ *evidence-for* `g15-0079`

- `g18-0073` *STATED* — contains-studio/agents (github.com/contains-studio/agents) packs an entire AI company into one repo, organised as eight departments of agents.
  — [g-an-entire-ai-company-in-one-repo-eight-departments](https://chen.media/guides/an-entire-ai-company-in-one-repo-eight-departments)
  ↳ *because* `g18-0075`
  ↳ *example-of* `g18-0286`
  ↳ *example-of* `g18-0278`

- `g18-0206` *STATED* — A free GitHub repo holds 280 finished n8n workflows sorted into 18 categories; import one file and it runs.
  — [g-280-ready-made-n8n-automations-you-do-not-have-to-build](https://chen.media/guides/280-ready-made-n8n-automations-you-do-not-have-to-build)
  ↳ *enables* `g18-0034` — ready-made workflows lower the cost of leaving Zapier

- `g18-0215` *STATED* — A free GitHub roster of 268 pre-written agent definitions, sorted into 20 divisions, gives your AI a job title before you type a word.
  — [g-268-expert-roles-in-one-repo-free](https://chen.media/guides/268-expert-roles-in-one-repo-free)
  ↳ *example-of* `g18-0286`

- `g19-0060` *STATED* — Alex's chen.media guide 'Split One Overloaded Claude Into a Seven-Station Line' (category: Agent teams) turns one overloaded Claude into a 7-station line where nothing ships until the work is checked.
  > “Turn one overloaded Claude into a 7-station line where nothing ships until the work is checked.”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)

- `g19-0077` *STATED* — The seven-station guide gives 'The one prompt that runs the line': a single orchestration prompt for the main session.
  > “The one prompt that runs the line”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *part-of* `g19-0060`
  ↳ *example-of* `g19-0074`

- `g19-0079` *STATED* — The seven-station guide ends with '3 quick wins to try' and a Troubleshooting section.
  > “3 quick wins to try”
  — [g-split-one-overloaded-claude-into-a-seven-station-line](https://chen.media/guides/split-one-overloaded-claude-into-a-seven-station-line)
  ↳ *part-of* `g19-0060`

- `g19-0192` *STATED* — Alex's chen.media guide 'Build an Agent Team Where One Agent Attacks the Others' Work' (category: Agent teams) gives five prompts that build a team of Claude agents where one agent attacks the work.
  > “The five prompts that build a team of Claude agents where one agent attacks the work”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)

- `g20-0089` *STATED* — Alex Chen's chen.media guide 'Run the Job Five Times and Let a Blind Grader Pick' (category: Agent teams): stop shipping Claude's first take, run the whole job five times and keep the winner; 2 prompts to copy.
  > “Stop shipping Claude's first take. Run the whole job five times and keep the winner.”
  — [g-run-the-job-five-times-and-let-a-blind-grader-pick](https://chen.media/guides/run-the-job-five-times-and-let-a-blind-grader-pick)

- `g20-0105` *STATED* — Alex Chen's chen.media guide 'How to Let Claude Run for Hours Without Supervising It' (category: Claude Code) has 5 prompts to copy and 5 numbered steps.
  — [g-how-to-let-claude-run-for-hours-without-supervising-it](https://chen.media/guides/how-to-let-claude-run-for-hours-without-supervising-it)

- `g20-0167` *STATED* — Alex Chen's chen.media guide 'The Second Claude That Reviews the First One's Work' (category: Agent teams) turns Claude into the brutally honest reviewer that catches what you can't; 1 prompt to copy, 3 numbered steps.
  > “Turn Claude into the brutally honest reviewer that catches what you can't”
  — [g-the-second-claude-that-reviews-the-first-one-s-work](https://chen.media/guides/the-second-claude-that-reviews-the-first-one-s-work)

- `g20-0178` *STATED* — Alex Chen's chen.media guide 'The Four-Agent Council That Roasts Your Idea Before You Build It' (category: Agent teams) promises to roast your idea before you waste six months building it.
  > “roasts your idea before you waste six months building it.”
  — [g-the-four-agent-council-that-roasts-your-idea-before-you-build-it](https://chen.media/guides/the-four-agent-council-that-roasts-your-idea-before-you-build-it)
  ↳ *contrast* `g20-0001` — two idea-validation methods

- `g20-0196` *STATED* — Alex Chen's chen.media guide 'Four Claude Agents That Work Like a Dev Team' (category: Agent teams) turns Claude into a four-agent dev team that ships real features while you sleep, set up once and run from one command.
  > “Turn Claude into a four-agent dev team that ships real features while you sleep.”
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *example-of* `g20-0288`

- `g21-0029` *STATED* — Alex's chen.media guide 'Run a Tournament Instead of Guessing Which Hook Works' (section: Agent teams) makes Fable 5 run 20 versions of an ad, hook or headline through a bracket and hand back the proven winner.
  — [g-run-a-tournament-instead-of-guessing-which-hook-works](https://chen.media/guides/run-a-tournament-instead-of-guessing-which-hook-works)

- `g21-0047` *STATED* — The tournament guide's locked sections are 'Your 3 prompts' and 'Run it forever for pennies'.
  — [g-run-a-tournament-instead-of-guessing-which-hook-works](https://chen.media/guides/run-a-tournament-instead-of-guessing-which-hook-works)
  ↳ *part-of* `g21-0029`

- `g21-0048` *STATED* — Alex's chen.media guide 'Turn Claude Into a Six-Person AI C-Suite' (section: Agent teams) sets up Fable 5 once as six employees to run a business for months.
  > “Turn Fable 5 into your 6 person AI C-suite. Set it up once, run it for months.”
  — [g-turn-claude-into-a-six-person-ai-c-suite](https://chen.media/guides/turn-claude-into-a-six-person-ai-c-suite)

- `g21-0061` *STATED* — The C-suite guide's locked sections are 'Your 6 employees' and 'Keep the crew running for pennies after the 12th'.
  — [g-turn-claude-into-a-six-person-ai-c-suite](https://chen.media/guides/turn-claude-into-a-six-person-ai-c-suite)
  ↳ *part-of* `g21-0048`

- `g21-0190` *STATED* — Alex's chen.media guide 'Three Workflows That Turn GPT-5.6 Sol Into a Whole Team' (section: Prompting) covers Ultra mode swarms, a Sol-plans/Luna-executes cost stack, and Sol as a tool-driving agent.
  — [g-three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team](https://chen.media/guides/three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team)

- `g21-0204` *STATED* — The Ultra-mode brief prompt: 'Use ultra mode. This is a big job, so split it across parallel subagents instead of doing it in one pass. Goal: [outcome]. 1. Break this into independent sub-tasks. 2. Assign one subagent to each and run them in parallel. 3. Merge everything into a single [report / doc / plan]. 4. Flag any place the subagents disagree so I can decide. Use max reasoning effort. Take the time to get it right.'
  — [g-three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team](https://chen.media/guides/three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team)
  ↳ *example-of* `g21-0202`

- `g21-0209` *STATED* — The Sol guide's locked sections are 'The cost stack: Sol plans, Luna executes', 'The agent: let Sol drive your tools', 'Guardrails, in plain terms' and 'Why this is the real edge'.
  — [g-three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team](https://chen.media/guides/three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team)
  ↳ *part-of* `g21-0190`
  ↳ *qualifies* `g21-0195`

- `g22-0065` *STATED* — Alex Chen's chen.media guide 'Put a Recurring Job on Autopilot With Claude Code' (section: Claude Code) gives 2 prompts for setting up Claude Code Routines.
  — [g-put-a-recurring-job-on-autopilot-with-claude-code](https://chen.media/guides/put-a-recurring-job-on-autopilot-with-claude-code)

- `g22-0107` *STATED* — PURGE GUARD runs from a monthly scheduled task or a calendar reminder.
  — [g-make-claude-hunt-down-every-forgotten-account-you-have](https://chen.media/guides/make-claude-hunt-down-every-forgotten-account-you-have)
  ↳ *enables* `g22-0106`
  ↳ *contrast* `g22-0070` — scheduled task vs Claude Code Routine

- `r01-0159` *STATED* — The /court guide is at chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0024`

- `r01-0190` *STATED* — The /court jurors are defined in skills/court/jurors.json.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0187`
  ↳ *defines* `r01-0166`

- `r04-0107` *STATED* — /night-crew morning gives one screen: what the builder built, what needs your OK, the scout's best leads, and the tracker's verdict; it's read-only and you decide what to merge.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0087`

- `r04-0108` *STATED* — The night-crew repo's examples/NIGHT-CREW.md is a filled-in set of standing orders.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *example-of* `r04-0093`

- `r04-0156` *STATED* — NIGHT-CREW.template.md has {{...}} placeholders: the app in one sentence and who it's for; Stack (framework, language, where it's hosted); a Backlog checklist of things small enough for one night; Who pays and Where they talk online ('or "unknown, scout should find out"'); check commands (test 'or "there are no tests yet"', lint 'or "none"'); and the owner's own never-touch list.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *defines* `r04-0093`
  ↳ *enables* `r04-0174`

- `r04-0182` *STATED* — Night crew routine prompt pattern: '/schedule every night at {{builder time}}: in {{owner/repo}}, read NIGHT-CREW.md and do the Builder's job. Follow its house rules exactly.' (same line for the Scout's and the Tracker's job).
  > “/schedule every night at {{builder time}}: in {{owner/repo}}, read NIGHT-CREW.md and do the Builder's job. Follow its house rules exactly.”
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *depends-on* `r04-0093`

- `r04-0222` *STATED* — /shark --investors N sets 2 to 10 sharks; default 5.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *depends-on* `r04-0224`

- `r04-0223` *STATED* — /shark --seed S picks a random panel from all 10 sharks, reproducibly.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *depends-on* `r04-0229`

### result

- `g03-0183` *STATED* — In the repo's example run on a small test program: 5 findings, 4 confirmed after triage, 3 patches written, every patch accepted by an independent reviewer agent.
  — [g-hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills](https://chen.media/guides/hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills)
  ↳ *evidence-for* `g03-0181`
  ↳ *example-of* `g03-0178`
  ↳ *evidence-for* `g20-0284`

- `g09-0127` *STATED* — The launch poll returns one page: GO for launch, or HOLD with how many stations said no, every station's one-line reason, and a fix list you can paste straight into Claude.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill)
  ↳ *example-of* `g09-0248`

- `g09-0156` *STATED* — The shark session returns one page: how many sharks are in, every decision and offer, what would change their minds, and every question you couldn't answer yet.
  — [g-pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill](https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill)
  ↳ *example-of* `g09-0248`
  ↳ *evidence-for* `r04-0215`

- `g09-0173` *STATED* — The court returns one page: the vote (say, guilty 9 to 3), every juror's one-line reason, and exactly what to change before you try again.
  — [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill)
  ↳ *example-of* `g09-0248`
  ↳ *evidence-for* `r01-0170`

- `g09-0223` *STATED* — You wake up to up to three pull requests and one command that sums them up.
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)
  ↳ *evidence-for* `r04-0197`

- `g11-0076` *STATED* — The tournament returns the one answer that beat the 99 others, the attacks it survived, the strategy card that produced it, and how many rounds it took.
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *part-of* `g11-0057`

- `r01-0170` *STATED* — /court returns VERDICT.md: the vote (for example GUILTY, 9 to 3), every juror's one-line reason, and what to change before you try again.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0161`
  ↳ *example-of* `g09-0248`

- `r01-0186` *STATED* — examples/candles/VERDICT.md in the court-skill repo is a real 3-juror trial: 'Quit my job as a nurse to sell handmade candles on Etsy full time' came back GUILTY, 3 to 0, with the conditions that would flip it.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *evidence-for* `r01-0161`

- `r03-0116` *STATED* — The demo review note (2026-10-05) opens: '8 corrections, 5 lessons, 2 false alarms. Rulebook: 7 of 40 rules.'
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0098`
  ↳ *example-of* `r03-0091`
  ↳ *evidence-for* `r03-0049`

- `r03-0297` *STATED* — The Jordan Sample roast scored an average of 3.0 out of 10, with all five roasters giving a 3.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0218`
  ↳ *contrast* `r03-0264` — weak profile, unanimous low score

- `r03-0316` *STATED* — Jordan Sample consensus: the headline names no job and no search words (5 of 5); the About is self-praise with no proof (5 of 5); 'Assisted with various marketing tasks as needed' says nothing (5 of 5); 'Worked with the team on marketing campaigns' names no campaign and no part (3 of 5).
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0217`
  ↳ *evidence-for* `r03-0297`

- `y01-0094` *STATED* — /market copy outputs a new headline, a new offer and a new call to action - direct before-and-after copy you can hand to the client.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *part-of* `y01-0092`

- `y01-0097` *STATED* — The agency's email command builds the entire email sequence, not just one email.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *part-of* `y01-0095`

- `y02-0164` *STATED* — With the night crew you start every day with most of yesterday's to-do list already done.
  — [8Yo0i9jLCzY](https://youtu.be/8Yo0i9jLCzY)
  ↳ *contradicts* `r04-0137` — video: 'most of yesterday's to-do list already done' vs house rule 8: 'one backlog item a night is a good night'
  ↳ *part-of* `y02-0157`

### style

- `g07-0294` *CORE* — Alex's skills write only to a dedicated folder where you run them (.agency, .brain-grade, linkedin-roast-output) and never touch your other files.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents) [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill) [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *contrast* `g07-0298` — Alex's own skills are scoped; third-party mods are not

- `g09-0248` *CORE* — Alex's panel skills each return one page: the verdict or count, every member's one-line reason, and a list you can act on or paste straight into Claude.
  — [g-launch-your-app-like-nasa-free-claude-skill](https://chen.media/guides/launch-your-app-like-nasa-free-claude-skill) [g-pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill](https://chen.media/guides/pitch-your-idea-to-a-panel-of-claude-sharks-who-want-to-say-no-how-to-install-the-free-skill) [g-put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill](https://chen.media/guides/put-your-idea-on-trial-in-front-of-a-jury-of-12-claudes-how-to-install-the-free-skill)
  ↳ *depends-on* `g09-0246`

- `r04-0214` *STATED* — A /shark investor who is out says it the classic way: 'For that reason, I'm out.'
  > “For that reason, I'm out.”
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0213`

### warning

- `g02-0010` *STATED* — /hunter never sends an application for you; it gets each one to the point where all you do is say yes and press submit.
  > “It never sends an application for you.”
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *qualifies* `g02-0009`
  ↳ *example-of* `g02-0237`
  ↳ *example-of* `g09-0247`

- `g09-0047` *STATED* — The lessons investigator never touches your code: at night it can only edit the rulebook and its own notes, and anything else it tries is refused.
  > “The investigator never touches your code. At night it can only edit the rulebook and its own notes; anything else it tries is refused.”
  — [g-claude-that-stops-repeating-its-mistakes](https://chen.media/guides/claude-that-stops-repeating-its-mistakes)
  ↳ *qualifies* `g09-0042`
  ↳ *example-of* `g09-0247`
  ↳ *evidence-for* `r03-0018`

- `g09-0221` *STATED* — The night-crew scout writes drafts only: it never posts.
  > “Drafts only: it never posts.”
  — [g-free-claude-night-crew-skill](https://chen.media/guides/free-claude-night-crew-skill)
  ↳ *qualifies* `g09-0219`
  ↳ *example-of* `g09-0247`
  ↳ *evidence-for* `r04-0134`

- `g12-0277` *STATED* — Guide section 'Before it spends your money' covers what to check before Polsia spends your money (body email-gated).
  — [g-set-up-polsia-the-ai-co-founder-that-runs-your-business](https://chen.media/guides/set-up-polsia-the-ai-co-founder-that-runs-your-business)
  ↳ *part-of* `g12-0266`
  ↳ *generalizes* `g12-0278`

- `g15-0032` *STATED* — Claude mistake 2: not making it run the boss loop (a strict reviewer that rejects work until it is good).
  — [g-10-claude-mistakes-pro-users-are-still-making-and-the-fix-for-each](https://chen.media/guides/10-claude-mistakes-pro-users-are-still-making-and-the-fix-for-each)
  ↳ *part-of* `g15-0024`
  ↳ *depends-on* `g15-0164` — mistake 2 refers to the boss loop
  ↳ *part-of* `g15-0181`
  ↳ *evidence-for* `g15-0165`

- `g15-0066` *STATED* — Stop running four agents in one terminal window; herdr gives each coding agent its own pane.
  — [g-four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute](https://chen.media/guides/four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute)

- `g15-0087` *STATED* — Munder Difflin is early software with a busy issue tracker, and an office of agents left running unsupervised will happily produce an office of nonsense.
  — [g-munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents](https://chen.media/guides/munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents)
  ↳ *leads-to* `g15-0088`

- `g15-0166` *STATED* — The third boss-loop instruction, appointing a strict boss, is the one most people leave out.
  — [g-the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer](https://chen.media/guides/the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer)
  ↳ *qualifies* `g15-0165`

- `g16-0302` *STATED* — Pick your Ruflo install path first, because the install paths are not the same product.
  > “Pick your install path first, because they are not the same product”
  — [g-ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm](https://chen.media/guides/ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm)
  ↳ *qualifies* `g16-0292`

- `g18-0212` *STATED* — Three things commonly go wrong when importing the ready-made n8n workflows, and the repo has one honest limitation.
  — [g-280-ready-made-n8n-automations-you-do-not-have-to-build](https://chen.media/guides/280-ready-made-n8n-automations-you-do-not-have-to-build)
  ↳ *qualifies* `g18-0206`
  ↳ *example-of* `g18-0279`

- `g19-0210` *CORE* — The one rule that makes the Agent Graph work: the attacker must never be the same pass as the builder.
  > “The attacker must never be the same pass as the builder”
  — [g-build-an-agent-team-where-one-agent-attacks-the-others-work](https://chen.media/guides/build-an-agent-team-where-one-agent-attacks-the-others-work)
  ↳ *part-of* `g19-0192`
  ↳ *qualifies* `g19-0197`
  ↳ *depends-on* `g19-0067` — a separate pass = fresh context
  ↳ *analogy-for* `g19-0024` — /clear cold review is a separate pass
  ↳ *evidence-for* `g20-0284`

- `g20-0199` *STATED* — One giant 'build me this' prompt in a fresh chat plans, builds and grades its own work in one blur, then ships whatever it happened to make.
  > “it plans, builds, and grades its own work in one blur, then ships whatever it happened to make.”
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *because* `g20-0200`
  ↳ *evidence-for* `g20-0170` — self-grading blur
  ↳ *because* `g20-0173`

- `r01-0031` *STATED* — /night-crew works through pull requests only, so nothing lands without review.
  > “Pull requests only.”
  — [r-alexyc9381](https://github.com/alexyc9381/alexyc9381)
  ↳ *qualifies* `r01-0030`
  ↳ *contrast* `r01-0053` — two overnight safety rules: PRs only / never send email
  ↳ *evidence-for* `r04-0095`

- `r01-0053` *STATED* — The /agency night shift never sends email.
  > “Never send emails at night.”
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *example-of* `r01-0050`

- `r01-0088` *STATED* — /agency never sends anything itself unless the user says 'send them' for that batch.
  > “Never send anything yourself unless the user says "send them" for that batch.”
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *example-of* `r01-0050`

- `r01-0113` *STATED* — /agency rule: nothing is sent, posted or charged without the user saying so for that batch.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *generalizes* `r01-0050`
  ↳ *example-of* `g09-0247`

- `r01-0231` *STATED* — The /court orchestrator must never write a vote, a statement or a judgment itself.
  > “Never write a vote, a statement or a judgment yourself.”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *qualifies* `r01-0230` — NO VOTE is the only thing the clerk may write
  ↳ *part-of* `r01-0207`
  ↳ *evidence-for* `r04-0021`

- `r02-0195` *STATED* — The /launch coordinator must never write a report or a call itself.
  > “Never write a report or a call yourself.”
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0194`
  ↳ *part-of* `r02-0156`
  ↳ *evidence-for* `r04-0021`

- `r03-0018` *STATED* — The /learn investigator never touches your code: at night it can only run the skill's script and edit LESSONS.md and .learn/; anything else it tries is refused.
  > “The investigator never touches your code.”
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *qualifies* `r03-0009`
  ↳ *depends-on* `r03-0070`
  ↳ *depends-on* `r03-0039`
  ↳ *analogy-for* `r03-0259` — both fence where the checker may write
  ↳ *example-of* `r04-0164`

- `r03-0073` *STATED* — In nightly mode /learn runs 'LEARN nightly' and shows its output as is, with the instruction 'Don't install anything yourself': the user sets up the schedule.
  > “Don't install anything yourself.”
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *qualifies* `r03-0033`

- `r04-0115` *STATED* — The night crew is Claude running on your own plan: read every pull request before you merge it.
  > “The crew is Claude running on your own plan: read every pull request before you merge it.”
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *qualifies* `r04-0095`

- `r04-0163` *STATED* — Routines run with no permission prompts; that is why the night crew house rules exist and why setup ends with three hard guardrails switched on in GitHub and claude.ai.
  > “Routines run with no permission prompts.”
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *because* `r04-0129`
  ↳ *because* `r04-0097`

- `r04-0189` *STATED* — Never include a payments, banking, email or social-posting connector in a night crew routine.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *qualifies* `r04-0188`

- `r04-0198` *STATED* — The night crew Morning briefing is read-only: don't merge, close, push or edit anything.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0107`

- `r04-0203` *STATED* — The night-crew skill never merges a pull request, never pushes to the default branch (except the one approved standing-orders commit), and never changes GitHub, claude.ai or routine settings itself.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *qualifies* `r04-0178`
  ↳ *generalizes* `r04-0198`

- `r04-0204` *STATED* — Never put secrets, keys or tokens into NIGHT-CREW.md or any routine prompt.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *generalizes* `r04-0135`

- `r04-0205` *STATED* — Never promise the night crew will finish everything: one backlog item a night is a good night.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *evidence-for* `r04-0137`

- `r04-0261` *STATED* — The /shark host never writes a question, an answer or a decision itself.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0021`
  ↳ *part-of* `r04-0242`

- `y02-0162` *CORE* — Guardrail: the night crew can't spend money, delete anything, or touch your live app unless you give it permission.
  > “the night crew can't spend money, delete anything or touch your live app unless you give it permission to”
  — [8Yo0i9jLCzY](https://youtu.be/8Yo0i9jLCzY)
  ↳ *evidence-for* `r04-0094`
  ↳ *part-of* `y02-0157`

<!-- AUTO:atoms END -->
