# KNOWLEDGE BASE: Alex Chen (@nocodealex)

**Domain:** Claude and Claude Code optimisation (usage limits, context, model routing, effort, hooks, CLAUDE.md, memory), Claude skills/plugins/MCP and free open-source tool swaps, multi-Claude review panels and agent teams, prompting and output quality, and building/selling/careers with AI.
**Sources:** YouTube @alexchenbuildsai (118 videos: 4 long-form + 114 shorts, the cross-posts of his Instagram reels), chen.media (385 guides — free part only: lede, section 1 and every section title; bodies email-gated), GitHub alexyc9381 (11 original skill repos), Instagram @nocodealex (login-walled; covered via cross-posts)
**Videos processed:** 118 of 118 (20 YouTube captions + 98 local Whisper transcripts) · 385 of 385 guides · 11 of 11 repos
**Atoms / edges:** 8291 / 13428 (incl. 2,656 cross-source links)
**Last updated:** 2026-10-16

Atom id prefixes: `y01-y04` = YouTube batches, `g01-g23` = chen.media guides, `r01-r04` = GitHub repos. "INFERRED" = a distiller's reading, not his words. Model names, prices and versions are as of his Sept-Oct 2026 posts.

## Topic Map — deep files (load on demand)

| topic file | load it when |
|---|---|
| references/topics/usage-limits.md | Any question about Claude/Claude Code usage limits, running out of messages, token cost, context bloat, /usage /context /compact /autocompact /model, effort levels, which model (Haiku/Sonnet/Opus/Fable) for which job, subagent model settings, plan pricing, monthly API credits, or working past the limit. |
| references/topics/claude-code-mastery.md | Claude Code commands, settings.json or env vars, effort levels and ultracode, hooks and onFailure, CLAUDE.md or memory files, the /learn and /bouncer skills, plan mode, rewind, background or overnight runs, mods and plugins, version minimums, or fixes for Claude forgetting, stopping early, making surprise edits or freezing a Mac. |
| references/topics/skills-mcp-ecosystem.md | Finding, installing, vetting or writing Claude skills, plugins, MCP servers or connectors: install commands, Find Skills, claude-mem, ECC, Superpowers, The Agency, SkillSpector, Alex's own skill repos and SKILL.md format, and free open-source replacements for paid AI tools. |
| references/topics/agent-teams.md | Running several Claudes together: review panels and juries (/court, /shark, /launch, /hiring-panel, /linkedin-roast, /hunter, /rival, /heist, /brain-grade), judge/boss/Gauntlet/tournament loops, subagent fan-out and Agent-call waves, specialist rosters, Claude Code routines or /schedule night crews, unattended overnight runs, human approval gates, agent-team token cost. |
| references/topics/prompting-quality.md | How to prompt Claude / Opus 5.5 / Fable 5 for better output: honest (non-sycophantic) feedback, stopping fabrication or false "done", verification loops, cleaning CLAUDE.md of old scaffolding, Darwin/Swarm/Forge/best-of-five loops, prompt "codes" like brutal mode, de-slopping AI design or writing, interview-first prompting. |
| references/topics/build-sell-career.md | Job hunting, resumes/ATS, LinkedIn profiles, career-ops / /hunter / /hiring-panel / /linkedin-roast, testing an idea or launch (/court, /shark, /launch, MiroFish), selling AI services or running an agency, lead generation, cold email, going live (GoLive, Stripe, hosting), free-vs-paid tool swaps and prices, licences, content research, SEO/GEO, making money with Claude. |
| references/topics/creator-news.md | Who Alex Chen / @nocodealex is, his chen.media guide and comment-keyword funnel, credit-line and honesty conventions, tool ratings and tier lists, or his takes on AI news (Sonnet 5.5 vs Opus 5.5, Gemini 4 Argon, AirLLM/local models, distillation, Jev, NVIDIA free models, Anthropic policy and economy reports). |

## 1. Identity & Bio

- AI creator who builds free Claude Code skills: @nocodealex (Instagram), @alexchenbuildsai (YouTube), repos at github.com/alexyc9381, guides at chen.media `r01-0002` `r01-0023` `r04-0001`
- Profile README headlines five free skills: /shark, /court, /night-crew, /launch, /learn `r01-0026`. Other repos/skills: /bouncer, /trojan, /heist, /jester, /hunter, /mentor, /agency, /hiring-panel, /linkedin-roast `r01-0034` `g08-0260` `r01-0037` `r01-0116` `r02-0001`
- chen.media guides are filed under Agent teams, Tools & repos, Claude Code and Build & sell `g04-0199` `g18-0282`
- Heavy Claude Code user on a $200/mo plan; his month would have cost ~$4,500 at API prices (20x+ what he paid); priciest single day ~$500 `y03-0018` `g12-0114` `y03-0020` `g12-0115` `g12-0113`
- Says he tested 100+ Claude Code skills to pick the 5 he never starts a project without `g21-0003`
- Treats Claude Code as a configuration discipline, not a prompting one: his 15 tips contain "no clever prompts" — every item is a setting, a surface or a habit `g16-0171` `g16-0170`
- Prompting as structure: of 50 tips he ran, 46 were forgettable and 4 changed his defaults, all structural (who reviews, what stops a bad action, where work runs, how many versions you keep) `g19-0035` `g19-0036` `g19-0037` `g19-0038`
- Recurring thesis: a single Claude is a yes-man, so honest feedback needs multiple adversarial Claudes `y02-0185`
- Conventions: every skill README ends "Not made by Anthropic." (/launch adds "not affiliated with NASA") `r04-0014` `r02-0162`; READMEs state sub-agent call counts up front (/linkedin-roast = 5, /learn = 1 run) `r03-0169` `r01-0017`; honest-limits sections frame output as "a structured second opinion" `r03-0170` `r01-0018`
- Covers many tools he did not build (Chrome Relay by Alexey Indeev, career-ops by santifer, the Craft apps) and names his own techniques openly ("nobody in the industry uses the name 'boss loop'") `g02-0186` `g01-0046` `g08-0050` `g15-0168`

## 2. Core Philosophy

- **The model is not the bottleneck; the setup around it is.** Fix forgetting, missing tools and working alone and the same model behaves like an unreleased one `g20-0224` `g20-0228`
- **Usage limits are a context problem, not a plan problem.** Claude re-reads the whole conversation on every message and tool call, so carried history sets the price of each turn `g19-0016` `g19-0017` `g04-0009` `g12-0122`
- **Route by difficulty.** The best model sets the ceiling — spend it on planning, specs and inspection; cheap models do the volume `g22-0282` `g20-0210` `y02-0187`
- **Lean beats loaded.** Always-on context (skill descriptions, MCP schemas, CLAUDE.md, plugins) costs tokens every request; a lean setup is cheaper and works better `g18-0283` `y02-0125` `g18-0113`
- **Subtract instructions.** A CLAUDE.md written for older/weaker models makes current, literal-following models worse `g18-0284` `g16-0011` `g12-0092` `g12-0094`
- **Every session starts blank; memory is a loop you build.** Write down what happened, load it back next job; build memory first, before tools, agents or autonomy `g06-0239` `g20-0147` `g20-0286`
- **Corrections become rules**; a recurring mistake sharpens the old rule rather than adding a second `r03-0011` `y02-0088`
- **Make setups permanent**: prompts live in CLAUDE.md / Project Instructions, not pasted chats — "the difference between a trick and a system" `g23-0199` `g20-0289`
- **A single Claude is a yes-man; the maker never grades its own work.** Separate blind judges, read-only reviewers or attackers do the grading `g09-0245` `g20-0284` `g20-0173` `g20-0292`
- **Independence is the whole point**: five copies with shared memory are "one answer wearing five hats" `g04-0245` `g20-0095` `y02-0186`
- **Guardrails, not prompts, stop mistakes**: "Rules in a prompt are instructions; the guardrails are what actually stop a mistake" `r04-0164` `g16-0010`
- **Human gate**: agents draft; nothing sends, posts, spends or merges without your yes `g09-0247` `g02-0237` `r02-0312` `g15-0089`
- **Autonomy is earned** one graded job at a time and lost if the grade drops `g20-0109` `g20-0110`
- **Never invent**: use only what the user said or what is verifiable; label guesses "assumed", else leave a placeholder `r01-0015` `g02-0238` `r02-0111`
- **Don't take "done" on trust**: verification loops with a stop condition and evidence `g15-0091` `g01-0195` `r03-0336`
- **Free, local, open source over paid** — but "free" usually means a capped free tier and prices move `y02-0188` `g18-0126` `g17-0194` `g02-0240`
- **Every recommendation names its downside** ("The catch"); a list of only upsides is an advert `g01-0189` `g18-0279`
- **Benchmark scepticism**: a 0.1-point gap is a tie, a leak is not a release `g11-0010` `g11-0040` `g11-0213`
- **Rehearse before spending**: test an idea/launch against simulated critics or customers first `g09-0254` `g09-0149`

## 3. Mental Models & Frameworks

**Claude Code setup**
- **Four upgrades** (when Claude Code feels weak): memory → MCP → subagents → the loop, in that order; each compounds `g20-0229` `g20-0231`
- **Limit triage**: run /usage → read which of four habit flags shows (max effort, workflows, always-on context, large tool results) → fix the top culprit `g04-0003` `g04-0002` `g03-0080`
- **28-ways guide, six tiers**: the three video fixes → context hygiene (biggest lever) → right model → right first time → session hygiene → make savings permanent `g19-0002` `g19-0008` `g19-0015`
- **Four cache rules**: pick model + effort at the top; no /model mid-task; /compact only at natural breaks; check cache with /usage `g05-0149` `g05-0151` `g05-0153` `g05-0155`
- **RATE / VOLUME / WASTE**: three independent cost levers (price per token, prose volume, tokens paid twice via the cache clock) `g16-0042` `g16-0039`
- **Effort ladder** (INFERRED): build on low, test on high, xhigh to stress-test, max only for hard unattended jobs, ultracode for one big task split across many Claudes `y03-0045` `y03-0037` `y03-0041`
- **CLAUDE.md cleanup**: read it as for an excellent new hire → delete guards against mistakes not seen in a month → delete what the code shows → keep only true, specific, non-inferable lines `g18-0232` `g18-0233` `g18-0234` `g18-0235`
- **/learn loop**: UserPromptSubmit hook logs correction-sounding prompts → nightly headless investigator distils them → LESSONS.md (40-rule cap) → CLAUDE.md @-imports it `r03-0097` `r03-0012` `r03-0049` `r03-0015`
- **Bouncer**: THE ASK (one sentence) → THE LIST (every change considered) → THE DOOR (only changes the ask needs) → report what was turned away `g08-0197` `g08-0198` `g08-0199` `g08-0200`
- **Unattended-run stack** (INFERRED): --bg + CLAUDE_CODE_RETRY_WATCHDOG=1 + auto-continue + CLAUDE_CODE_GOAL_CHECKIN_MINUTES=0 `g03-0010`
- **Claude Code team daily check**: /code-review → /simplify → /verify → custom /design skill `g12-0211`

**Model economics**
- **Model line / Sol factory**: flagship writes the spec + quality bar and returns as QA inspector (touches the batch twice); mid tier drafts; cheap tier (~5x cheaper) mass-produces. On Claude: Fable/Opus → Sonnet → Haiku (INFERRED) `g22-0061` `g22-0048` `g22-0053` `g22-0064`
- **Judgment Vault**: flagship back-solves your decision rules into JUDGMENT.md; cheap models load it before deciding; monthly maintenance loop `g22-0010` `g22-0009` `g22-0015`
- **Advisor**: a cheaper main model does routine turns and asks Opus only at outcome-deciding moments `g04-0231` `g11-0099`

**Multi-Claude panels**
- **Blind panel pattern**: N Claudes start at once, each judges alone, every claim quotes evidence, a separate synthesiser merges worst-first, then a rewrite `g07-0295` `g08-0251` `g09-0246`
- **NASA launch poll (/launch)**: mission file → 8 stations (Tests, Security, Database, Speed, Cost, Users, Recovery, Rules) → GO/NO-GO with file:line evidence → one NO-GO holds the launch → flight director writes holds, fix order, first-week watch list `g09-0113` `g09-0114` `g09-0123` `g09-0126`
- **Court**: prosecutor vs defense, rebuttals, 12 blind jurors, judge verdict + "conditions for acquittal" `g09-0165` `g09-0168` `g09-0171` `r01-0223`
- **Boss loop**: task + team of worker sub-agents + one strict boss who tears the work apart; loop until the boss passes it (the third part is the one people skip) `g15-0165` `g15-0167`
- **Agent Graph**: five named agents, build v1, unleash an attacker, rebuild until it survives, make it permanent `g19-0202` `g19-0206` `g19-0209`
- **100-Claude tournament**: unique strategy cards, pairwise attacks (fatal/major/minor), rebut + rewrite, separate judge /100, bracket to 1; 16-Claude quick mode `g11-0062` `g11-0067` `g11-0075` `g11-0058`
- **Best-of-five**: 5 fresh blind runs, a sixth grader with nothing to defend picks `g20-0092` `g20-0097` `g20-0103`
- **Four-agent dev team**: Planner (smartest model, spec.md) → Coder → Tester (test-report.md) → read-only Reviewer; shared folder, each trusts only the last file `g20-0206` `g20-0209` `g20-0213`
- **Idea council**: Believer, Skeptic, Investor, Judge, rulings to one shared note `g20-0180` `g20-0183`
- **Split-model audit (Pair/Claudex)**: Claude writes PLAN.md, Codex audits read-only (PASS/BLOCK, up to 3 rounds), builds, Claude verifies `g06-0160` `g06-0162` `g06-0164` — *non-Claude provider; see §12*
- **Night crew**: 3 Claude Code routines (builder, scout, tracker) read one NIGHT-CREW.md nightly; each opens a draft PR `r04-0089` `r04-0093` `g09-0216`

**Prompting loops**
- **Opus 5.5 checklist**: drop "think carefully" (use effort) → whole task in one message → name the finish line → say when to stop and ask → don't interrupt `g05-0059` `g05-0060` `g05-0061` `g05-0062` `g05-0063`
- **Fable 5 three fixes**: give an example, lead with the answer, give a goal not a script `g23-0004` `g23-0005` `g23-0006`
- **Verification loop**: Claude tries what it built (clicks, screenshots), fixes, re-tests, then says done `y03-0053` `y03-0058` `g12-0202`
- **Darwin Loop**: draft → 3 candidates → pick strongest → evolve winner into 3 → repeat `g13-0222` `y04-0040`. **Swarm Loop**: 3 reviewers each hunting a different weakness → fix → re-check `g13-0242` `y04-0050`. **Forge Loop**: persistent self-grade-and-fix setup `g23-0027` `g23-0030`. Bounded: draft cheaply, loop only on polish `y04-0055` `g13-0248`
- **Grill Me**: Claude interviews you along a design tree with numbered questions and recommended answers before building `g01-0169` `g01-0171`

**Judging tools / business**
- **Hype-vs-reality score** (/100 each): equal = lives up; reality higher = underrated; hype higher = overhyped `g10-0094` `g10-0097`
- **Tier list**: 15 categories × 3 tools, bad/mid/great with a one-line why `g23-0051` `g23-0055`
- **Start-small**: one job, one skill, a clear test; one MCP; one-week trial of any free tool `g13-0281` `g18-0285`
- **Vet-before-install**: author + installs/stars → SkillSpector scan → prefer human-approval gates `g10-0261` `g10-0263` `g03-0049`
- **career-ops four questions**: still open? → fit /5 vs real CV → worth it (ATS CV, letter, fields)? → who to talk to (draft note you send) `g01-0045` `g01-0050` `g01-0054`
- **AI agency formula**: find client → pinpoint problem (GEO) → personalised outbound → deliver via repo → upsell `y01-0127` `y01-0120`

## 4. Methods & Workflows

**Usage & routing**
- **Haiku helper**: create `haiku-helper.md` subagent (`model: haiku`, description: logs, searching, listing, renames, one-line edits); tell Claude in CLAUDE.md when to use it; Opus keeps planning/debugging/multi-file `g06-0224` `g06-0228` `g07-0111` `g07-0112`
- Force all subagents to Haiku: `CLAUDE_CODE_SUBAGENT_MODEL=haiku` + `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` in the `env` block of ~/.claude/settings.json (with a quality cost) `g03-0215` `g03-0213` `g06-0094`
- Stop idle /goal check-ins (each re-sends the whole chat): `CLAUDE_CODE_GOAL_CHECKIN_MINUTES=0` `g03-0192` `g03-0188`
- Compact earlier: `/autocompact 200k` (range 100K-1M; default ~967K on 1M models); undo `/autocompact auto` `g06-0064` `g06-0065` `g06-0069`
- `/model opusplan`: Opus plans, Sonnet builds `g19-0005` `g19-0006`
- Shrink context: /context to see what fills it; move rare procedures from CLAUDE.md into skills; prune skills/plugins with /skill-doctor `g03-0022` `g09-0132` `g09-0142`
- Rewind wrong turns instead of arguing: Esc to stop, Esc Esc on an empty prompt (or /rewind) rolls back chat + code `g03-0110` `g03-0113` `g03-0114`
- Convert PDFs/office files to Markdown first (MarkItDown); one PDF ≈ 70k tokens per message `g15-0180` `y03-0013`
- Filter test output to failures only (10,000-line log → hundreds of tokens) `g04-0088`
- Claim Max/Team monthly API credits: Settings > Billing > API credits > Link organization > accept terms `g06-0207` `g06-0208`

**Memory & CLAUDE.md**
- **memory.md**: one root file, read before every job, appended after; "Read memory.md before you do anything else. Treat every line in it as a decision I have already made." One fact per line `g20-0148` `g20-0152` `g20-0158`; at session end append decisions, corrected preferences, breakages + reason `g20-0155` `g20-0157`
- Placement: ~/.claude/CLAUDE.md = who you are/how you work; ./CLAUDE.md = stack, commands, gotchas; /init, /memory, `#` to save a line `g20-0238` `g20-0240` `g20-0242`
- Starter global sections: `## Who I am`, `## How to answer me`, `## Standards` ("Match the style of the surrounding code", "Never commit or push unless I ask", "tell me exactly what you verified") `g20-0246` `g20-0250` `g20-0252`
- /learn: `/learn setup` once (hook into .claude/hooks, LESSONS.md, @LESSONS.md in CLAUDE.md), new session; `/learn <lesson>` or bare `/learn`; when FULL: `LEARN list`, `LEARN merge N M` `r03-0074` `r03-0076` `r03-0078`
- Night /learn run: `claude -p "/learn review" --permission-mode dontAsk --allowedTools "Bash(python3 .claude/hooks/learn.py *),Edit(./LESSONS.md),Edit(./.learn/**)"` so it cannot edit code `r03-0038` `r03-0039`

**Session control**
- Plan mode: Shift+Tab cycle, `/plan`, or `claude --permission-mode plan` `g03-0158` `g03-0160`
- Background: `claude --bg --name "flaky-test-fix" "fix the failing tests"`; in-session `/bg` `g03-0084` `g03-0085`
- Subagents: Markdown + YAML frontmatter (name, description, tools, model, `effort: low`) in .claude/agents/ or ~/.claude/agents/ `g19-0068` `g19-0071` `g05-0167`

**Skills, plugins, MCP**
- Plugin shape: `/plugin marketplace add owner/repo` → `/plugin install name@marketplace` → `/reload-plugins`; one line per message `g18-0160` `g05-0310` `g18-0161`
- His repos: paste `https://github.com/alexyc9381/<repo>` + "Install this skill, then confirm /<name> works."; or git clone + copy to ~/.claude/skills/, `npx skills add alexyc9381/<repo>`, or the plugin marketplace `r01-0003` `r04-0005` `r01-0004`
- MCP: `claude mcp add context7 -- npx -y @upstash/context7-mcp`; `claude mcp add playwright npx @playwright/mcp@latest`; keys via `-e KEY=value` `g20-0276` `g21-0015` `g20-0279`
- Skill authoring: input via `$ARGUMENTS`, files via `${CLAUDE_SKILL_DIR}`, state in a dot-folder, bookkeeping in a Python helper so rules live in code; frontmatter with long description ending in "Use when the user ..." triggers; tests via `python3 -m unittest discover -s tests` `r04-0007` `r04-0008` `r04-0009` `r04-0006` `r01-0007`

**Panels / agent teams**
- Fan out in waves: one message, one Agent (formerly Task) call per job, wait for the whole wave before the next `r01-0225` `r01-0228` `r02-0189`
- Brief as a standalone file (sub-agents can't see the chat); prompt "Read <brief path> and follow it exactly. It is your whole brief." `r02-0177` `r01-0227` `r04-0249`
- A Python script owns state and counting (court.py, launch.py, `.court/<run>/state.json`); orchestrating Claude only hosts — never argues, votes or softens `r01-0187` `r02-0155` `r01-0188` `r02-0156`
- Each reader gets only the artifact + one persona, verbatim; fixed answer formats (juror: VOTE/REASON/DECIDING FACT/WOULD FLIP IF); missing output re-run once, then NO VOTE/NO CALL `r01-0129` `r01-0240` `r01-0229` `r01-0230`
- Night crew: `/night-crew` asks 6 questions, writes NIGHT-CREW.md, gives three `/schedule` lines (builder 1:07, scout 2:07, tracker 5:07) `r04-0106` `r04-0182` `r04-0183`
- Unattended agents never block on questions: they write "NEEDS YOUR OK:" / "YOU" to the log and carry on `r04-0136` `r02-0107`

**Prompting**
- Prompt Audit: strip "double-check your work", ALL-CAPS rules and step scripts `y03-0068` `y03-0069` `y03-0070` `g12-0102`
- Attack, don't improve: make Claude a skeptical reader hunting reasons to leave `g21-0065` `g21-0068`
- Evidence-anchored critique: every point quotes the exact line / file:line `g04-0246` `r01-0251` `r02-0132`
- Placeholders over invention: `[ADD YOUR NUMBER: ...]` `r03-0220` `r03-0335`
- Interview one question at a time; mark UNCONFIRMED; list gaps at the end `g22-0033` `g22-0036` `r01-0020`
- De-slop design: ban defaults by name ("Do not use a cream or off-white background, italic accent words in headlines, numbered 01/02/03 section labels, monospace labels, or pill-shaped buttons."), give screenshots/references `g13-0025` `g13-0024` `g13-0020` `g20-0121`
- Handoff blueprints assume a zero-memory builder ("BUILDER: Claude Sonnet, working alone, cold start") `g21-0151` `g21-0124`

**Build & sell**
- /hunter: 7 setup questions → Find → Filter (seen.md) → Score → Tailor → PACKET.md; you submit, then `/hunter applied <n>` `r02-0058` `r02-0071` `r02-0104`
- /linkedin-roast: save profile as PDF, `/linkedin-roast <file>`; 5 roasters + rewrite + banner + headshot prompt `r03-0144` `r03-0258`
- Bullet rewrite: distinct action verb + specific action + numeric result; keep titles/dates; `[ADD YOUR NUMBER]` `r03-0158` `r03-0234` `r03-0285`
- Lead machine: Target (source plan) → Scraper → Verifier → Writer; swap niche/city to rerun `g19-0117` `g19-0119`
- Carousel service: one industry → build the workflow once → easy-yes price → exact pitch; prompt goes in Project instructions `g19-0276` `g19-0288` `g20-0076`
- Complaint play: pricing complaints live in Cons of 3-4 star Capterra reviews, not 1-star `g19-0265`
- Paid-to-free swap: run the free tool for a full week on real work before cancelling `g17-0195`

## 5. Rules & Heuristics

**Routing & limits**
- Search, logs, folder listing, rename, one-line edit → Haiku; planning, debugging, multi-file change → Opus `g07-0111` `g07-0112`
- Straightforward task → default/low effort; max only for security reviews, tricky bugs, big refactors — never summaries `y01-0018` `g05-0174` `y01-0149`
- Never switch /model mid-task: each model has its own cache, so the next turn is a full uncached re-read `g05-0315` `g05-0147` `g05-0157`
- Hitting a session/weekly limit: /model restores nothing (shared limits); only model-specific limits benefit from switching `g05-0198` `g05-0197`
- New job → new chat; related follow-ups → same chat `y01-0030` `y01-0029`
- Subagent descriptions > 15,000 tokens triggers a startup warning `g03-0223`; an @-mentioned file under 25,000 tokens is inlined whole `g03-0028`
- Near the limit: keep the session open so auto-continue (v2.1.234+) resumes at reset `g03-0170`
- Unused Max/Team API credits expire each billing cycle; Free/Pro/Enterprise ineligible `g06-0211` `g06-0206`

**Settings & hooks**
- Check `claude --version` against minimums: auto-continue/goal check-ins 2.1.234, Haiku subagents 2.1.257, onFailure 2.1.295, subagent compaction 2.1.296 `g03-0002` `g03-0168` `g04-0058` `g04-0206`
- New env setting, skill or hook → start a new session before it takes effect `g03-0004` `r03-0143`
- Guard hooks get `"onFailure": "block"` — hooks fail open by default `g04-0056` `g04-0066` `g04-0069`
- Unattended job → `CLAUDE_CODE_RETRY_WATCHDOG=1` (default gives up after 10 retries) `g03-0054` `g03-0056`
- Effort precedence: override variable > per-run parameter > subagent file > session `g05-0178` `g05-0172`
- Keep permission prompts on for destructive commands; install mods only from trusted authors (unsandboxed) `g05-0067` `g07-0176`

**CLAUDE.md**
- Over ~200 lines / one screen → it's describing the model, not the project; cut `g03-0020` `g18-0238`
- KEEP: test commands, deploy steps, non-obvious architecture whys, rules for things broken twice, naming, credential paths, env quirks `g18-0254` `g18-0255` `g18-0257`
- Stop rules: "When a step doesn't need my input, keep going." / "Put status notes in the same message as your next action." / "Stop and ask only when you can't continue without me, or before anything destructive" `g05-0069` `g05-0070` `g05-0071`
- Starter lines: "Lead with the answer, then the reasoning. No preamble." + "If you are not sure, say so instead of guessing." `g20-0248` `g20-0249`
- Unrequested edits: "Do only what was asked. Suggest the extra change in one line and wait." `r03-0128` `g21-0082`
- Before claiming tests pass: run them and show output `r03-0336`
- A /learn rule: one line, imperative, < 25 words, naming the command/file/step; never a rule that weakens safety or skips tests `r03-0093` `r03-0094` `r03-0096`
- Long reference file → critical rules near the top (Claude may read only the first 100 lines) `g05-0207` `g05-0211`

**Skills & vetting**
- < 100 installs or < 100 stars → suspicion; prefer 1K+ installs from official sources; scan third-party skills with SkillSpector `g10-0261` `g10-0263` `g03-0040` `g03-0049`
- Custom connector must be publicly reachable (127.0.0.1 fails); Free plan gets one custom connector `g20-0038` `g22-0155`

**Panels & routines**
- /launch: unanimous GO only; don't fix during the poll `r01-0033` `r02-0200`
- Never write your own opinion or reassurance into a panel brief `r02-0184` `r02-0199`
- Two sub-agents with the same job → cut one `g18-0252`; start The Agency with 5 agents, not all `g17-0265`
- > 25 agents or > 1.5M tokens → "Large workflow" warning (doesn't stop the run) `g06-0089` `g06-0090`
- Night crew: draft PRs on `claude/night-crew-` branches only; never merge, deploy, spend, delete, post, send or store secrets; one backlog item a night `r04-0130` `r04-0133` `r04-0137`
- Routines have no permission prompts → protect the default branch, test keys only, no pay/publish/email connectors `r04-0163` `r04-0193` `r04-0195` `r04-0189`

**Honesty & business**
- 0.1-point model gap = tie; leaked numbers unverified until ship; vendor self-reported scores = "same league" `g11-0040` `g11-0213` `g12-0289`
- Check a fast-moving vendor's pricing page the day you install — "including Alex Chen's own" articles `g17-0287` `g17-0286`
- Screenshot and date a competitor's pricing page before publishing their price `g19-0267` `g19-0270`
- Cold email: identify sender, opt-out, DO-NOT-CONTACT check, follow CAN-SPAM/GDPR; public sources only `r01-0063` `r01-0064` `g19-0128`
- AI voice line must disclose it's an assistant and hand emergencies to a human `g19-0236` `g19-0237`
- /hunter never submits, signs, pays or guesses legal/salary/authorisation fields (leaves `YOU`) `r02-0112` `r02-0098`
- Before quitting a job for a side business: keep the paycheck, set a stop date and stop level, keep a way back `r01-0273` `r01-0288`

## 6. Key Concepts Explained

- **Per-turn payload**: question + every tool schema + whole conversation + every file read, rebuilt each turn — the bill grows faster than the work `g17-0115` `g17-0118`
- **Skill notes**: each installed skill's name + description sits in context every message; the body loads only when used `g09-0134` `g09-0135`
- **Prompt caching**: re-reads billed at cached rate but still every turn; each model has its own cache `g05-0146` `g12-0123` `g05-0147`
- **/compact** rewrites history into a lossy summary that drops paths, errors and early rules ("dumb after compacting"); Fast-Jev Compaction instead deletes stale tool calls and keeps original messages `g12-0175` `g12-0177` `g12-0178`
- **Hidden re-senders**: forgotten /loops, /goal check-ins after 30 min, subagents each sending their own requests `g02-0195` `g03-0187` `g04-0011`
- **Effort**: how long Claude thinks, tests and decides alone; low/medium/high/xhigh/max + ultracode; does not swap the model `g10-0186` `g10-0173` `g10-0185`
- **Adaptive thinking**: current Claudes decide when/how much to think, so old "plan/check yourself" scaffolding gets in the way `g15-0025` `g15-0028`
- **CLAUDE.md vs auto memory**: you write rules, Claude writes learnings; both load each session; auto memory only first 200 lines / 25KB `g06-0241` `g06-0243`
- **Hooks**: PreToolUse can block/rewrite (exit code 2 blocks); UserPromptSubmit sees every prompt; hooks ship with plugins, not bare skill folders — a skill instructs, a plugin enforces (INFERRED) `g19-0039` `g04-0064` `r04-0043`
- **Skill / plugin / connector / MCP**: a skill is a folder with SKILL.md (frontmatter + instructions); a plugin bundles skills, connectors, commands, agents; a connector is an MCP server to a product's data; MCP gives Claude hands `g18-0100` `g12-0162` `g12-0164` `g16-0190`
- **Description = routing surface**: Claude auto-fires skills whose description matches; vague ones never fire `g15-0045` `g17-0229`
- **Mods**: small TypeScript plugins drawing panels, intercepting commands, adding commands (via /plugin) `g07-0162` `g10-0065`
- **Cloud sessions / routines**: Claude Code on an Anthropic VM, runs with laptop closed; routines = prompt + connectors + schedule against a GitHub repo, hourly minimum `g13-0094` `g09-0215` `g22-0073`
- **/advisor**: Opus works; a stronger model reads the session and advises at key moments with no tools `g11-0099` `g11-0108`
- **Early-quit patterns**: summarising next steps without starting, listing non-blocking decisions, stopping because it ran long `y03-0047` `y03-0048` `y03-0050`
- **Desktop memory leak**: app + leftover background processes + one hungry MCP server → SSD swap → frozen Mac `g10-0037` `g10-0035`
- **Yes-man Claude / king's jester**: a king with only yes-men never hears what's wrong `g08-0176` `g08-0181`
- **Unlazy**: removes the model's ability to declare itself finished; it must fill a ledger — "you do not promise you are done, you prove it" `g16-0142` `g16-0146`
- **Slop UI**: no one steering design; tells are Claude defaults (purple gradients, Inter, nested cards) `g12-0031` `g12-0036` `y02-0120`
- **Requirement dilution**: each extra requirement in one session dilutes the last `g15-0104`
- **Quotes as leads**: a quote Claude pulled is a lead, not a citation `g19-0268`
- **Separate maker from judge; synthesiser step; file-based message bus** (spec.md, queue.md) `g20-0284` `g09-0246` `g20-0206`
- **ATS**: parses resume into fields and ranks before a human; most rejections are structural (two columns, tables, unreadable dates) `g21-0171` `g21-0184`
- **GEO / AI visibility**: whether people asking Claude/ChatGPT/Perplexity can find a business `y01-0112` `g02-0156`
- **Licences**: MIT/Apache permissive (keep notices); AGPL-3.0 copyleft; open weights ≠ open source `g17-0293` `g18-0266` `g06-0190`
- **Distillation**: train on a frontier model's answers at scale `g09-0100`

## 7. Results & Data Points

- His month: ~$4,500 API-priced vs $200 paid; ~2/3 (~$3,000) was re-reading, ~11% writing `y03-0018` `g12-0117` `g12-0116`
- Haiku 5.5 vs Opus finding errors in 6 logs: both 6/6, $0.014 vs $0.347 (−96%) — one job, one run `g06-0233` `g06-0234` `g06-0235`
- $1,000 buys ~15,000 Haiku / ~7,000 Sonnet / ~5,800 Opus / ~3,200 Fable messages `y03-0002` `y03-0003` `y03-0005` `y03-0007`
- Fable 5.1 hard tasks: ~73k tokens at low vs ~222k at max (3x) `g10-0196`
- Effort timings (same prompt, Thariq Shihipar): low 1.5 min, medium 4, high 11, max 67 (~45x) `g10-0189` `g10-0192` `g10-0195`
- Anthropic removed 80%+ of the Claude Code system prompt for Claude 5 with no eval loss `g16-0258`; removing legacy prompt patterns cut cost ~9% and raised accuracy ~2 pts `g12-0096` `g12-0097`
- Desktop app grew to 131-140GB on a 48GB Mac; terminal Claude Code stayed < 200MB `g10-0038` `g10-0039`
- Context Mode: 315 KB tool output → 5.4 KB (vendor README) `g02-0039`
- /learn demo: 8 corrections → 5 lessons + 2 false alarms; rulebook 3 → 7 rules `r03-0043` `r03-0099`
- An agent team uses ~7x the tokens of a normal session `y03-0016`
- NVIDIA study of 31,132 skills: 26.1% vulnerable, 5.2% likely malicious `g03-0038` `g03-0039`
- Arena on Opus 5.5 writing: em dashes −95%, semicolons −73%, hedges +97% `g12-0221` `g12-0222` `g12-0230`
- Anthropic learning study (52 mostly junior engineers): AI group quiz 50% vs 67%, only ~2 min faster; explain/conceptual users 65%+, full delegators < 40% `g04-0180` `g04-0183` `g08-0016` `g08-0020`
- Sonnet 5.5 70.6% Terminal-Bench 4.0 vs Opus 5.5 66.4% at half the price; Opus still leads FrontierCode (54.4 vs 46.2) and OSWorld `g12-0005` `g12-0011` `g06-0143`
- CaptionPal /launch demo: HOLD, 8/8 NO-GO (admin leak of MD5 hashes, SQL injection, email-as-session cookie, unlimited paid endpoint, crashing migration) `r02-0211` `r02-0237` `r02-0238`
- Candle /court case: GUILTY; ~13 sales/month vs ~57 needed `r01-0238` `r01-0242`
- santifer career-ops: 740 posts → 68 applications → 12 interviews → 1 offer `g01-0047` `g01-0049`
- 15 business tools $1,057/mo at top tier, $870 switchable, 6 KEEP `g17-0167` `g17-0192`
- YouTube terminated 16 automated faceless channels (~35M subs) in Jan 2026 `g20-0062`

## 8. Products, Tools & Things They've Built

**His own skills (github.com/alexyc9381, all free)**
- **/learn** (learn-skill): self-improving rulebook — capture hook, nightly investigator, LESSONS.md capped at 40 `r01-0034` `r03-0026`
- **/bouncer**: lists every planned change, gates against the ask `g08-0191`. **/trojan**: read-only scan for invisible text / AI-directed orders `g08-0237`. **/jester**: shows the cheers, then three biggest problems + cheapest tests `g08-0177`
- **/court** (court-skill): prosecutor, defense, 12 blind jurors, judge → VERDICT.md; `--jury N` (3-12), `--seed`, `--quick` `r01-0029` `r01-0178` `r01-0182`
- **/shark** (shark-skill): 5 sharks, founder sub-agent answers only from pitch.md → BOARD.md `r01-0027` `r04-0255`
- **/launch** (launch-skill): 8 flight controllers, unanimous GO, flight-director write-up `r02-0118` `r02-0134`
- **/night-crew** (night-crew-skill): 3 cloud routines leave draft PRs; ~10 min setup; `/night-crew morning` summary `r04-0087` `r04-0107`
- **/hunter**: 5-Claude headhunter, scores /100, writes packet, never submits `r02-0001` `r02-0039`. **/hiring-panel**: 7 Claudes try to reject your resume, then rebuild it `r01-0116`. **/linkedin-roast**: 5 blind roasters + full rewrite + banner `r03-0134` `g04-0149`
- **/agency** (agency-skill): 5 agents (outbound, sales, workflow, support, night shift) in .agency/; nothing sends without "send them" `r01-0037` `r01-0041` `r01-0088`
- **/rival, /heist, /brain-grade, /mentor** `g08-0220` `g08-0073` `g07-0137`
- Every generated file ends "Made with /<skill> by Alex Chen (@nocodealex) · chen.media" — except files sent to employers `r01-0010` `r02-0116`

**Tools he recommends (built by others)**
- Usage: /usage (/cost, /stats) ranks skills/subagents/plugins/MCP by limit share `g03-0073`; /skill-doctor `g09-0132`; tokentab `g04-0071`; Effortless (Haiku sets effort) `g05-0098`; Context Mode `g02-0031`; Fast-Jev Compaction `y03-0026`; Trail-code `g02-0176`
- Safety: CC Safety Net (PreToolUse guard vs `git reset --hard`, force-push, risky `rm -rf`, secret reads) `g01-0122`; Time Machine mod `g02-0117`; SkillSpector (NVIDIA) `g03-0035`
- Ecosystem: Find Skills (Vercel Labs) `g10-0247`; claude-mem `g13-0136`; ECC `g14-0222`; Superpowers `g21-0008`; The Agency `g08-0096`; Context7, Playwright, Firecrawl MCPs `g18-0123` `g21-0014`
- Writing/design: Straight Talk `g12-0217`, Humanizer `g01-0137`, I Have ADHD `g01-0105`, /awwwards `g02-0140`, Impeccable `g09-0077`, Grill Me `g01-0169`, Prompt Master `g16-0271`
- Mac helpers: Coucou (permission requests to iPhone/notch), bigarrow, Claude HUD `g06-0113` `g06-0149` `g14-0063`
- Build & sell: career-ops `g01-0044`, GoLive (Vercel/Supabase/Stripe test mode) `g02-0080`, Harvey `g04-0029`, claude-seo `g02-0151`, MiroFish `y02-0148`, Founder `g05-0238`, Video Use, SupoClip `g02-0207` `g12-0186`
- Must-install lists: stop-slop, ClaudeMem, UI-UX Pro Max, Task Observer, Find Skills; MCPs Chrome DevTools, Firecrawl, Figma, Blender, ElevenLabs `g23-0100` `g23-0151`
- Lead magnet: model-choice cheat sheet (which model, effort, AI per job) `y03-0205`

## 9. Ideas & Things They're Exploring

- Spend a temporarily free flagship window mining your backlog into blueprints addressed to cheap builders, so they build for months `g21-0118` `g21-0149`
- Clone the flagship's understanding into files (audit → skills → instructions) before it goes pay-per-token: files survive, context doesn't `g23-0012` `g23-0017`
- Enforce /bouncer as a PreToolUse hook denying files outside the approved list (INFERRED) `y02-0062` `g08-0202`
- Schedule the tracker routine after the builder so one cloud agent audits another's PR first (INFERRED) `g09-0228`
- Cheap over-catching phrase hook + Claude investigator to discard false alarms (INFERRED) `r03-0104`
- Before overnight runs: keep-going paragraph + verification loop (INFERRED) `y03-0062` `g10-0268`
- Provenance line in CLAUDE.md separating the user's words from pasted/fetched text (prompt-injection defence) `g11-0180` `g11-0167`
- Run long Mac jobs in terminal Claude Code, not the desktop app `g10-0045`
- A repo whose CLAUDE.md makes Claude Code its own installer ("set it up") `g04-0046`
- Claude Marketplace as "the iPhone App Store in 2008 again" — build weekend-sized plugins now `g12-0158` `g12-0161`
- Sellable services: niche CRM agent, short-form editing package, phone agent; AI-visibility (GEO) audits as a standalone service `g14-0330` `y01-0119` `y01-0110`
- Once Gemini 4 opens, Claude won't be the automatic coding pick `y03-0191` `g11-0056`

## 10. Opinions & What They Reject

- Rejects blaming the plan: people hitting limits waste them on jobs a cheaper model could do; heavy users who never hit limits turn off unused skills `y02-0020` `y02-0124`
- "Almost every 'Claude is worse today' post is a context problem wearing a capability costume" `g16-0100`
- Rejects single-lever token advice; attack RATE, VOLUME and WASTE separately `g16-0040`
- Rejects leaving effort untouched or pinned at max `g10-0183`; making the flagship do all the volume is "paying an architect to lay every brick" `g22-0047`
- Ultrafast writes 8x faster but doesn't think/test 8x faster and burns allowance 8x as fast; the real question is whether it's worth $6,000/yr `g11-0129` `g11-0121`
- Rejects long instruction files: "a museum of old problems"; endorses deleting CLAUDE.md every six months (Boris Cherny) `g18-0230` `g18-0241`
- Rejects old prompting advice (think carefully, CRITICAL/MUST/ALWAYS, step scripts) as actively harmful now `g15-0028` `g12-0100` `y03-0065`
- Rejects self-review in the same chat: "telling Claude to double-check its own writing barely helps" `g21-0070` `g20-0171`
- "One friendly answer is the worst kind of feedback" `g09-0163`; Claude's default feedback is "pleasant and useless" `g21-0064`
- "You cannot out-prompt bad taste" — give references, not wishes `g20-0119` `g13-0082`
- Narrow specialist agents beat one generalist; persistent single-lens agents turn a chatbot into an employee `g18-0075` `g21-0054`; a clear comparison and stopping point matter more than agent count `g13-0227`
- The human permission gate is the feature, not the friction `g15-0089`; skills must never send or act behind your back `r02-0024`
- A crashed guard hook should block, not pass `g04-0069`
- Rejects re-prompting daily (make it a skill) and writing your own prompt library `y01-0175` `y04-0120`
- Rejects star counts as the metric; coverage matters `g18-0012`; "you only need three of the 90,000 skills" `y04-0113`
- Hype is not output; most people pay for the biggest marketing budget `g23-0185` `g23-0187`
- Hype-vs-reality: Claude 75/95 (underrated); Google AI Studio most underrated; Lovable 95/60 most overhyped `g10-0099` `g10-0111` `g10-0112`
- Picks: Claude Code > Cursor > Copilot for coding; n8n > Make > Zapier for automation `g16-0253` `g16-0254`
- Higgsfield is "literally just a wrapper" (yet also his video pick — see §11) `y01-0186`
- Rejects building six months before validating demand `g09-0019`; "AI is not banned on YouTube; templates are" `g20-0063`
- Default vibe coding = clicking yes on everything and learning nothing `r04-0025`

## 11. Open Questions / Contradictions / Gaps

**Recorded contradictions (all of them)**

*Usage & models*
- Starting model: "Anthropic says start with Opus for most work" `y03-0006` vs "start 90% of tasks on Sonnet" `y01-0138` vs default Sonnet 5.5, escalate to Opus `g12-0026`
- Max-effort cost: "+50%" `y01-0146` vs ~3x tokens (73k vs 222k) `g10-0196`
- Skill cost: "costs nothing until useful" `g18-0103` vs a note in context every message `g09-0131` (reconciled: description always on, body lazy `g09-0135`)
- /compact: a Tier 1 limit fix `g19-0003` vs "myth: /compact saves your limit" `g05-0202`
- Token breakdown: "Claude Code never shows a breakdown" `g04-0075` vs /usage ranks skills/subagents/plugins/MCP `g03-0073`
- Cloud credit eligibility: any Max/Pro `y04-0024` vs only those subscribed on Sept 23 2026 `g13-0114`
- Opus 2x Sonnet price per token `y03-0014` vs only ~1.2x fewer messages per $1,000 `y03-0005`
- Flagship: "Claude Fable 5 is the flagship" `g22-0274` vs "Opus 5.5, Anthropic's most capable" `g11-0092`

*Claude Code mastery*
- Memory leak headline: ~120GB on a 96GB Mac `y03-0093` vs 131-140GB on a 48GB Mac `g10-0038`
- Mods: hidden behind "one setting most people miss" `g10-0049` vs on by default in 2.1.287+ `g07-0171`
- /learn: "never repeats that mistake" `y02-0088` vs "much less likely, not impossible" `r03-0060`
- Bouncer: "you never find surprise changes" `y02-0061` vs "a rule, not a lock, so skim its list" `g08-0201`
- Session memory: "every new session forgets everything" `g13-0134` vs auto memory loading each start `g06-0242`; "forgets when you close the chat" `g20-0225` vs file-based memory on by default on Free/Pro/Max `g16-0064`
- System-prompt cut: "the tool got better" `g18-0229` vs "measured no loss" `g16-0258`
- CLAUDE.md: "delete a 200+ line file, start from zero" `g18-0246` vs "the fix is not deleting everything" `g16-0265`; "under 200 lines" `g03-0020` vs "a single screen" `g18-0237`
- Projects: "project folders are the solution" `y01-0160` vs "do not work inside Projects by default" `g16-0177`
- Reddit: "Claude cannot read Reddit" `g19-0249` vs night-crew scout reading reddit.com via Custom network access `r04-0187`

*Skills & ecosystem (counts drift)*
- AirLLM stars: 35K+ `g04-0215` vs 38K+ `g02-0235`; Find Skills installs 3.8M vs 3.6M `g07-0033` `g10-0248`; agents reached 75+ vs ~40 `y03-0104` `g18-0086`
- Total skills: 50,000 vs 90,000 vs over a million vs 1,499,600 `g23-0099` `y04-0113` `g07-0025` `g10-0256`
- The Agency: 230+ / 273 / 286 agents `g08-0089` `g15-0116` `g17-0258`; stars 158,347 / 149k+ / 137.4k / 124k+ `g15-0115` `g18-0271`
- claude-mem stars: 94K+ vs 90,651 (API) vs stale 46.1K `g13-0137` `g17-0088`; Claude SEO stars ~18,000 vs 14,028
- claude-seo: up to 17 agents at once / 19 total `g02-0154` vs up to 15 / 18 specialists `g17-0107` `g17-0104`
- NVIDIA free key: Claude-API-like (video) vs OpenAI-style API (guide); Photon Studio: Mac/Win/Linux vs Mac/Win
- Craft apps: "official open-source copy" of Adobe vs not made or approved by Adobe
- Agent Reach: installs in Claude or ChatGPT vs a ChatGPT chat can't run terminal tools
- Single-file AI hub: "no cloud" vs G0DM0D3 calls still go to providers; 50 tools vs 60+ models

*Agent teams*
- Night crew: "an additional 8 hours of work" / "most of yesterday's to-do list done" `y02-0158` `y02-0164` vs repo "one backlog item a night is a good night" `r04-0205` `r04-0137`
- Pair re-audits "up to 3 times" `g06-0162` vs "back and forth until they agree" `y04-0108`
- Best-of-N: "three is thin, ten is noise" `g20-0102` vs a 100-Claude tournament `g11-0057` and a 20-version bracket `g21-0033`

*Prompting*
- Self-check: "not asking Claude to check its work" is a token mistake vs Prompt Audit problem 1 "telling Claude to double-check" `y03-0068` vs "double-checking barely helps" `g21-0070` vs Forge Loop self-grading `g23-0030` vs "self-review never works" (reconcile: self-checks count only with tests/evidence)
- Opus 5.5 "always thinks before every reply" `g05-0059` vs adaptive thinking "decides when to think" `g15-0025`
- "Make it show its work" (build prompts) vs mistake 7 "asking it to show its work in the answer"
- Token mistake 2 "writing what you don't want" and mistake 5 "the prohibition list" `g15-0035` vs his named Opus 5.5 design ban prompt `g13-0025`
- Mistake 6 "hard length caps" `g15-0036` vs mistake 14 "no bound on length or scope" and his roast-skill caps `r03-0207`
- "Act like an expert" is token mistake 1 `g23-0092` vs ORACLE "most qualified expert alive" `g23-0094` and the 268-role repo
- Mistake 7 "burying the task at the bottom" vs best-of-five ending with "THE JOB:" `g20-0091`
- "You cannot out-prompt bad taste" `g20-0119` vs "the fix is one design rule pasted once"
- AI default look: cream/italics/01-02-03/mono/pills `g13-0026` vs purple gradient, Inter, one centered button `g20-0115`
- "Motion is the entire reason a site reads expensive" `g15-0004` vs "Apple looks expensive because it obeys a small set of numbers" `g15-0187`
- "Almost none of the prompt-wording advice survives" `g19-0034` vs "five short code phrases change Claude's answer completely" `g23-0040`
- Darwin/Swarm "build entire apps in a single prompt" `y04-0038` vs guide "illustrative, not a single-prompt guarantee" `g13-0235` `g13-0245`
- Grill Me "every question at once, numbered" `g01-0171` vs "ONE question at a time" `r01-0020` vs night crew "one short message" `r04-0166`
- Logo skill: 1,400+ real logos (guide) vs 1,000+ (video)

*Build & sell / tool picks*
- Framer swap: Durable `g18-0138` vs Lovable `g17-0212`; Framer price "up to $45/site" `y03-0127` vs Pro $30 / Basic $10 `g17-0212`
- CapCut: KEEP at $9 `g17-0187` vs swap $20 CapCut Pro to Edits `g17-0214`
- Adobe Firefly: $10, KEEP `g17-0186` vs Pro $30, swap to Photoroom `g17-0208`
- Higgsfield: replace with Hailuo `g17-0206` / "just a wrapper" `y01-0186` vs his AI-video pick `g23-0179` `g23-0201`
- Perplexity: replace with Consensus `g17-0200` / "overhyped 85/65" `g10-0102` vs his research pick `g23-0182` `g23-0203`
- v0 wins his design ranking `g19-0214` vs "replace v0 with Bolt.new" `g23-0189`; Midjourney → Nano Banana vs → Leonardo; Runway → Stable Diffusion vs → Higgsfield `g23-0190`
- Six-jobs list vs tier list: brainstorming (Claude 1st vs Claude mid), learning (NotebookLM 2nd vs great; ChatGPT 3rd vs bad), research (NotebookLM 1st vs Perplexity), images (Midjourney 1st vs mid) `g16-0249` `g23-0069` `g16-0251` `g23-0061`
- Candle break-even: 58 `r01-0259` vs ~57 `r01-0242`

*Creator / news*
- Gemini 4 Argon "announced Sept 30" `g11-0041` vs "released Oct 13" `g05-0265`; leaked 88.7 vs shipped 77.9 DeepSWE `g11-0211` `g11-0229`
- Jev founder: "Diego Almeida, a ChatGPT co-founder" `y04-0066` vs "former creators of ChatGPT, DeepMind and Meta" `y04-0075`; multipliers "up to 200x/400x" vs "20-200x/40-400x" `y04-0079`

**Coverage gaps**
- **Guide bodies are email-gated**: for all 385 guides only the lede, section 1 and section titles were captured; everything after is a toc-only atom (a heading with no body). Gated items include the four-habit fixes, the effort cheat sheet, the mods setting name, onFailure/compaction/background "catch" sections, boss-loop checks, the routine prompt template, prompt codes 02-05, the 10-mistakes list, career-ops' "one rule that is not optional", the faceless-YouTube numbers and the Argon catch `g04-0004` `g10-0176` `g10-0049` `g04-0068` `g15-0174` `g22-0076` `g23-0044` `g15-0031` `g17-0301` `g20-0068`. Never fabricate those bodies — say they are gated.
- **Instagram-only reels were not transcribed**: Instagram is login-walled; coverage is via the 114 YouTube Shorts cross-posts, so any reel never cross-posted is missing.
- **Claims are unverified**: star counts, install counts, vendor benchmarks (Chrome Relay 23/23, Jev, Context Mode, claude-mem 95%), his own savings and output promises were recorded as stated, not re-tested `g02-0193` `y04-0062` `y04-0011`
- Unconfirmed specifics: the exact /skill-doctor command name `y02-0130`; the 4 Routine steps (inferred) `g22-0080`; the heist video's fifth crew member `y02-0046`; "Karpathy at Anthropic" `y02-0106`; Fable 5 → Opus 4.8 downgrade (user reports only) `g22-0267`; DeepGEMM "98% token saving" (doubtful — server-side kernels) `y02-0115`; Stripe live-mode step in GoLive `g02-0093`; Superpowers "10x" (unmeasured) `y04-0116`

## 12. How To Apply This Base

**Good for**
- **Optimising Claude Code**: auditing a setup — /usage triage, version minimums, settings.json `env` block, subagent model vars, /autocompact, effort policy, hook `onFailure`, CLAUDE.md keep/cut, memory file, stop rules `g04-0003` `g03-0002` `g03-0215` `g04-0066` `g18-0245` `g05-0069`. Picking a model and effort per task, and planner/worker splits `g07-0111` `y03-0045` `g22-0056`
- **Choosing skills/tools**: exact install lines, writing SKILL.md files whose descriptions fire, vetting third-party skills (thresholds, SkillSpector, read the file), connector pitfalls `g18-0160` `r04-0006` `g10-0261` `g20-0038`
- **Multi-Claude review patterns**: blind parallel sub-agents in one wave, standalone brief files, fixed answer formats, a script that tallies, a separate judge; /launch before shipping, /court or /shark on ideas; budget ~7x tokens `r01-0225` `r02-0177` `r01-0187` `y03-0016`. Safe unattended routines: draft-PR-only, protected branch, no secrets, no pay/publish connectors `r04-0193` `r04-0196`
- **Prompting quality**: rewriting CLAUDE.md for Opus 5.5, getting honest feedback, stopping false "done" with verification loops or ledgers, de-slopping design/writing `y03-0068` `g07-0296` `g16-0150` `g13-0024`
- **Building and selling with AI**: career skills with exact thresholds, idea/launch stress tests, service playbooks (carousels, voice line, lead machine, /agency), always keeping the human gate `g01-0052` `g09-0254` `g19-0286` `r02-0112`
- Answering "as Alex would": attach his catch and the source date; route by task (Sonnet 5.5 for terminal volume at half price, Opus for hard coding) `g01-0189` `g12-0002`

**Do NOT trust it for**
- **Exact current CLI syntax, flags, env-var names, version numbers or plan terms** — dated to Sept-Oct 2026 and partly gated; check official Claude Code docs and the user's `claude --version` first `g04-0250` `g14-0169`
- **His star counts, install counts, prices and benchmarks** — they drift and contradict across guides; vendor tables and single-run tests (Haiku 96%) are not independent evidence `g17-0088` `g06-0235` `g05-0267` `g17-0314`
- **Video-level output promises** (8 hours of work, 10x, single-prompt apps) — the repo house rules are the reliable spec `y02-0158` `r04-0205` `y04-0116`
- **Panel verdicts as expert, legal or financial advice** — one model playing many roles `r03-0162` `r01-0192`
- **/learn, /bouncer and prompt rules as guarantees** — they are instructions; enforcement needs hooks or permissions `r03-0060` `g08-0201`
- **Anything routing work to non-Claude model providers** — Claude Code Router, OmniRoute failover, Codex in Pair/Claudex, Claude Octopus cross-provider councils, NVIDIA/Chinese free models, Jev, OpenRouter, deepclaude, Gemini picks. The user's own rules forbid non-Claude providers (Claude / Max plan only, no external API keys): keep only the Claude-internal version of each pattern (e.g. Pair → Opus plans, a separate read-only Claude subagent audits; routing → Haiku/Sonnet/Opus via subagent model settings) `g19-0156` `g15-0069` `g06-0160` `g14-0249`
- **Gated bodies** — when a toc-only atom is the only evidence, say the detail is gated; don't invent it

**How to use**: read this file first; load one topic file from the Topic Map when a question goes deeper; quote atom ids; label INFERRED items; when two atoms contradict, name both and prefer the repo-level or more specific source.
