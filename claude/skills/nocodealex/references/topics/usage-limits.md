# Usage limits, tokens, context and model routing

## What he believes (CORE first)

- **Limits are a context problem, not a plan problem** `g19-0016`. Claude re-reads the whole conversation on every message, not a summary of it `g19-0017` `g04-0009`. So the price of a message is set by how much history you drag behind it, not by how hard the question is `g19-0019`. Each tool call re-sends the chat with the new result on top `g12-0122`.
- **His own bill shows it.** He paid $200 for a month that would have cost about $4,500 at API prices `y03-0019` `g12-0114`, which is over 20x `y03-0020`. About two-thirds (~$3,000) was re-reading `g12-0117` `y03-0023`. Only ~11% was Claude writing anything `g12-0116`.
- **Model routing is his main lever** `y02-0187` `g06-0264`. Opus is the default even for renames and log reads, and burns limit like a hard job `y02-0018` `y02-0019`. Easy work goes to Haiku and hard thinking stays on Opus `y02-0022`.
- **The flagship sets the ceiling, and cheap models do the volume** `g22-0282` `g22-0016` `g20-0210`. Plan once with the expensive model, then let cheap models "cash the checks" `g21-0121`.
- **Always-on context is a tax on every message.** That includes skill notes `y02-0125` `g09-0131`, MCP tool schemas `g18-0113`, CLAUDE.md `g03-0016` and plugins `y03-0015`. Lean is cheaper and better `g18-0283`.
- **Panels spend your plan.** Every sub-agent in his skills counts toward usage `r02-0150` `r01-0017`. Skills, plugins and credits never make usage free `g14-0350`.

## Frameworks and methods

**Limit triage** `g04-0003`. Run `/usage` (`/cost` and `/stats` open the same screen) `g03-0076`. Press `d`/`w` to switch between 24h and 7d `g03-0078`. Read the habit flags `g03-0079`, then fix the top culprit first `g03-0080`. The four habits it warns about are max effort, workflows, always-on context and large tool results `g04-0002`. Also check the Loops row for forgotten `/loop`s, which can fire for a week `g02-0201` `g02-0198`. INFERRED: pair it with tokentab to see spend by project and model `g04-0083`.

**28-ways guide, six tiers** `g19-0002`: (1) the three fixes from the video, (2) context hygiene, which he calls by far the biggest lever `g19-0008`, (3) right model for the job, (4) get it right the first time, (5) session hygiene, (6) make the savings permanent.

**Cache rules** `g05-0149` `g05-0151` `g05-0153` `g05-0155`. Pick model and effort at the top of a session, don't `/model` mid-task, keep `/compact` for natural breaks, and check the cache with `/usage`. Each model has its own cache, so a switch means one uncached full re-read `g05-0315` `g05-0147`.

**Model line (role routing)** `g22-0056`. Sol writes the spec and inspects, and touches the batch only twice `g22-0061`. Terra drafts and Luna mass-produces `g22-0057`–`g22-0060`. Mapped onto Claude: Fable/Opus → Sonnet → Haiku (INFERRED `g22-0064`). He uses the same pattern in the Judgment Vault (the flagship back-solves rules, cheap models read them for pennies) `g22-0009` `g22-0014` and the Fable clone (write understanding into files before the free window closes) `g23-0016`.

**Bounded loops.** Get a cheap draft first and spend loops only on polish `y04-0055` `g13-0248`. Size panel runs up front, e.g. "12 jurors, 17 sub-agent calls" `r01-0212`, and use `--quick` when near the limit `r01-0183`.

## Exact commands, settings, numbers

- **Haiku helper** `g06-0224`: `name: haiku-helper; model: haiku`. It handles logs, file search, folder listing, renames and one-line edits `g07-0111`. Opus keeps planning, debugging and multi-file changes `g07-0112`. In his test both models got 6/6 log errors, at $0.347 for Opus vs $0.014 for Haiku, which is 96% less `g06-0233` `g06-0234` `g06-0232`. That was one job with one run each `g06-0235`.
- **Force all helpers onto Haiku**: in the `env` block of `~/.claude/settings.json`, set `CLAUDE_CODE_SUBAGENT_MODEL=haiku` and `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` `g03-0215`. This has a gated cost `g03-0219`.
- **/goal check-ins**: `CLAUDE_CODE_GOAL_CHECKIN_MINUTES=0` `g03-0192`. It also switches something else off `g03-0195`.
- `/autocompact 200k` (range 100K–1M; the default is ~967K on 1M models); reset with `/autocompact auto` `g06-0064` `g06-0065` `g06-0069` `g06-0066`.
- `/model opusplan` (Opus plans, Sonnet builds) `g19-0005`; `/context` `g19-0009`; `/compact focus on the auth` `g19-0004`; `/skill-doctor` to prune unused skills `g09-0132` (toc-only name, see `y02-0130`).
- **Prices**: Opus 5.5 is $4/$20 `g11-0037`, Sonnet 5.5 $2/$10 `g12-0016`, and Haiku 5.5 $0.10/$0.50 up to 100K prompts `g05-0179` `g07-0094`. Haiku 5.5's tokenizer counts ~30% more tokens, so $100 becomes ~$13 `g05-0186` `g05-0187`.
- **What $1,000 buys**: ~15,000 Haiku, ~7,000 Sonnet, ~5,800 Opus or ~3,200 Fable messages `y03-0002`–`y03-0007`.
- **Monthly API credits**: Max 5x gets $100 and Max 20x $200. Team gets $20 per Standard seat and $100 per Premium seat, pooled and capped at $500 `g06-0203`–`g06-0205`. You must claim them under Settings > Billing > Link organization `g06-0207` `g06-0208`. They expire monthly `g06-0211` and don't cover interactive Claude Code `g06-0210`.
- **Past the limit**: auto-continue (v2.1.234+) `g03-0166`, lower-priority mode, which still counts toward the weekly limit `g12-0244`, and OmniRoute fallback `g15-0069`. After a session or weekly limit, `/model` changes nothing `g05-0198`.
- **Other tools**: Claude Code Router (`npm install -g @musistudio/claude-code-router`, `ccr ui`) `g19-0168`; MarkItDown for PDFs, since one PDF costs ~70k tokens `g15-0180` `g15-0013`.

## Contradictions and caveats

- **Default model**: "start with Opus" `y03-0006` vs "start 90% on Sonnet" `y01-0138`. INFERRED: default to Sonnet `g12-0026`.
- **Max-effort cost**: "+50%" `y01-0146` vs ~3x tokens (73k vs 222k) `g10-0196`.
- **Skill cost**: "costs nothing until useful" `g18-0103` vs a note on every message `g09-0131`. Both hold: the body loads lazily, the description doesn't `g09-0135`.
- **`/compact`**: listed as a Tier 1 fix `g19-0003` vs "myth: /compact saves your limit" `g05-0202`. It is also lossy `g12-0176`, and Fast-Jev drops stale tool output instead `g12-0178`.
- **Opus vs Sonnet price**: 2x per token `y03-0014` but only ~1.2x per message `y03-0005`.
- **Cloud credit eligibility**: "any Max/Pro" `y04-0024` vs subscribed by Sept 23 2026 `g13-0114`. It has expired (Nov 4 2026) `g13-0103`.
- **Vendor savings claims** (Jev "80% more usage" `y04-0062`, claude-mem 95% `y04-0011`): measure them yourself first `g13-0183` `g14-0068`. Many guide bodies are email-gated (toc-only), e.g. `g04-0004`–`g04-0007`.

## What to load next

`topics/usage-limits.md` (full atoms); `claude-code-mastery` (settings, hooks, /compact); `skills-mcp-ecosystem` (Context Mode, Trail-code, tokentab, OmniRoute); `agent-teams` (panel sub-agent counts, model lines); `prompting-quality` (legacy-prompt cleanup, −9% `g12-0096`).

---

## Atom index

<!-- AUTO:atoms BEGIN -- regenerated by build_topics.py, do not edit below -->

*828 atoms.*

### analogy

- `g22-0047` *STATED* — Making the flagship Sol produce all 50 of anything (emails, pages, posts) is like paying an architect to lay every brick.
  > “is like paying an architect to lay every brick”
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)
  ↳ *analogy-for* `g22-0046`

- `y01-0136` *STATED* — Alex's model analogy: choosing a Claude model is like choosing who to hire for a job - the model decides how smart the AI is.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *leads-to* `y01-0135`

- `y01-0144` *STATED* — Opus 5 on low effort is like giving an expert 5 minutes to glance at your work - they know what to do but only give it a quick read.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *analogy-for* `y01-0143`
  ↳ *contrast* `y01-0145`

- `y01-0145` *STATED* — Dragging Opus to max effort is like giving the same expert the whole afternoon.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *analogy-for* `y01-0143`

- `y03-0033` *STATED* — The second-AI check in Fast-Jev Compaction is like your mom asking 'are you still eating this?' before tossing your leftovers.
  > “like your mom asking, are you still eating this before tossing your leftovers”
  — [20RWbPnejOE](https://youtu.be/20RWbPnejOE) [tq8Addr9brU](https://youtu.be/tq8Addr9brU) [kUH4J8VWe-I](https://youtu.be/kUH4J8VWe-I) [7eL_2dx0-bU](https://youtu.be/7eL_2dx0-bU)
  ↳ *analogy-for* `y03-0032`
  ↳ *example-of* `y03-0206`

### caveat

- `g02-0183` *STATED* — The Trail-code guide promises 'what the benchmark really shows' in an email-gated 'What the numbers say' section, signalling the headline benchmark needs a closer read.
  > “what the benchmark really shows”
  — [g-trail-code-stop-claude-getting-lost-in-your-code](https://chen.media/guides/trail-code-stop-claude-getting-lost-in-your-code)
  ↳ *qualifies* `g02-0176`
  ↳ *example-of* `g02-0236`

- `g03-0034` *INFERRED* — With path-only @ mentions Claude no longer sees the file up front, so it has to spend a Read call to open it when it actually needs the content.
  — [g-stop-file-mentions-from-pasting-whole-files-into-your-claude-chat](https://chen.media/guides/stop-file-mentions-from-pasting-whole-files-into-your-claude-chat)
  ↳ *qualifies* `g03-0030`

- `g03-0169` *STATED* — Auto-continue is for claude.ai usage limits: if you use an API key, run /login and sign in with your Claude subscription.
  — [g-let-claude-code-wait-out-your-limit-and-carry-on](https://chen.media/guides/let-claude-code-wait-out-your-limit-and-carry-on)
  ↳ *qualifies* `g03-0167`

- `g03-0175` *STATED* — There are cases where Claude Code will not carry on after the limit resets (covered in the guide's catch).
  — [g-let-claude-code-wait-out-your-limit-and-carry-on](https://chen.media/guides/let-claude-code-wait-out-your-limit-and-carry-on)
  ↳ *example-of* `g03-0006`
  ↳ *qualifies* `g03-0166`

- `g03-0195` *STATED* — Setting CLAUDE_CODE_GOAL_CHECKIN_MINUTES to 0 also switches off something else (the guide's catch says what).
  — [g-stop-claude-goal-check-ins-from-eating-your-limit](https://chen.media/guides/stop-claude-goal-check-ins-from-eating-your-limit)
  ↳ *example-of* `g03-0006`
  ↳ *qualifies* `g03-0192`

- `g03-0219` *STATED* — Forcing every helper onto Haiku has a cost, covered in the guide's catch ("what it costs you").
  — [g-run-every-claude-helper-agent-on-haiku](https://chen.media/guides/run-every-claude-helper-agent-on-haiku)
  ↳ *example-of* `g03-0006`
  ↳ *qualifies* `g03-0213`
  ↳ *qualifies* `y02-0023` — forcing every helper onto Haiku has a cost

- `g03-0224` *STATED* — No 15,000-token warning does not mean subagent descriptions are free: they still take up context, so shorter is still better.
  > “No warning does not mean the descriptions are free.”
  — [g-shorten-your-claude-helper-agent-descriptions](https://chen.media/guides/shorten-your-claude-helper-agent-descriptions)
  ↳ *qualifies* `g03-0223`

- `g04-0008` *STATED* — Alex warns there is a catch with the /usage habit warnings: the numbers can tell you some things and not others (section 'The catch', body locked).
  > “what the numbers can and can't tell you”
  — [g-the-four-habits-eating-your-claude-limit-and-the-fix-for-each](https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each)
  ↳ *qualifies* `g04-0001`
  ↳ *example-of* `g04-0242`

- `g04-0075` *STATED* — Claude Code never shows you a breakdown of where your tokens went, even though it logs every call's token count.
  — [g-tokentab-see-where-every-claude-token-goes-as-a-monthly-statement](https://chen.media/guides/tokentab-see-where-every-claude-token-goes-as-a-monthly-statement)
  ↳ *contrast* `g04-0076`
  ↳ *contradicts* `g03-0073` — tokentab guide: "Claude Code never shows you a breakdown of where your tokens went" vs /usage guide: /usage ranks skills, subagents, plugins and MCP servers by share of your limit

- `g04-0129` *STATED* — Free, Pro and Enterprise Claude plans aren't eligible for the monthly API credits.
  — [g-how-to-claim-your-monthly-claude-credits-on-max-and-team-plans](https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans)
  ↳ *qualifies* `g04-0121`

- `g04-0130` *STATED* — New subscribers can only claim the monthly API credits after 7 days on the plan.
  — [g-how-to-claim-your-monthly-claude-credits-on-max-and-team-plans](https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans)
  ↳ *qualifies* `g04-0122`

- `g04-0136` *STATED* — Alex's credits guides spell out what the monthly API credits cover and list catches (sections 'What they cover' and 'The catch', bodies locked).
  — [g-how-to-claim-your-monthly-claude-credits-on-max-and-team-plans](https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans) [g-how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets](https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets)
  ↳ *qualifies* `g04-0121`
  ↳ *example-of* `g04-0242`

- `g04-0137` *INFERRED* — The monthly credits are Claude API (Claude Platform / Console) credits, a separate pot from the Claude Code and claude.ai usage limits of the subscription itself.
  — [g-how-to-claim-your-monthly-claude-credits-on-max-and-team-plans](https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans) [g-how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets](https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets)
  ↳ *qualifies* `g04-0121`

- `g04-0238` *STATED* — Only some main-model and advisor pairings work; Alex's guide lists which ones (body locked).
  > “which pairings work”
  — [g-let-opus-advise-while-sonnet-does-the-routine-work](https://chen.media/guides/let-opus-advise-while-sonnet-does-the-routine-work)
  ↳ *qualifies* `g04-0231`

- `g04-0239` *STATED* — The advisor has a cost of its own and does not run everywhere; Alex's guide covers what it costs and where it does not run (body locked).
  > “what it costs, and where it does not run”
  — [g-let-opus-advise-while-sonnet-does-the-routine-work](https://chen.media/guides/let-opus-advise-while-sonnet-does-the-routine-work)
  ↳ *qualifies* `g04-0231`
  ↳ *example-of* `g04-0242`

- `g05-0113` *STATED* — The Effortless guide has a catch qualifying its savings (section 'The catch'; 1 prompt to copy, 5 numbered steps).
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless)
  ↳ *qualifies* `g05-0098`

- `g05-0160` *STATED* — The cache guide has a catch qualifying the four-rule setup (1 prompt to copy, 4 numbered steps).
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)
  ↳ *qualifies* `g05-0157`

- `g05-0186` *STATED* — Haiku 5.5 uses a newer tokenizer, so the same text counts as about 30% more tokens.
  — [g-claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command](https://chen.media/guides/claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command)
  ↳ *qualifies* `g05-0183`
  ↳ *qualifies* `g07-0090`

- `g05-0192` *STATED* — The Haiku 5.5 guide names one limit to respect when switching (gated catch).
  — [g-claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command](https://chen.media/guides/claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command)

- `g05-0193` *INFERRED* — The headline Haiku 5.5 prices are quoted for prompts up to 100,000 tokens, so very long prompts may be billed differently.
  — [g-claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command](https://chen.media/guides/claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command)
  ↳ *qualifies* `g05-0192`
  ↳ *depends-on* `g05-0181`
  ↳ *evidence-for* `g07-0101`

- `g05-0199` *STATED* — Exception: after 'You've hit your Opus limit' or 'Sonnet limit', switching to a model outside that family keeps you working.
  — [g-three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha](https://chen.media/guides/three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha)
  ↳ *qualifies* `g05-0197`

- `g05-0206` *STATED* — The limit-myths guide has a catch section qualifying the advice.
  — [g-three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha](https://chen.media/guides/three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha)
  ↳ *qualifies* `g05-0195`

- `g06-0206` *STATED* — Free, Pro and Enterprise plans aren't eligible for the monthly API credits, and you must have been on the plan for seven days.
  — [g-this-week-in-claude-ranked-by-what-it-does-for-you](https://chen.media/guides/this-week-in-claude-ranked-by-what-it-does-for-you)
  ↳ *qualifies* `g06-0202`
  ↳ *evidence-for* `g04-0129`
  ↳ *evidence-for* `g04-0130`

- `g06-0210` *STATED* — The monthly API credits cover the Claude API, Message Batches, the Console playground, Managed Agents and the Agent SDK, not interactive Claude Code or extra usage.
  — [g-this-week-in-claude-ranked-by-what-it-does-for-you](https://chen.media/guides/this-week-in-claude-ranked-by-what-it-does-for-you)
  ↳ *qualifies* `g06-0202`
  ↳ *evidence-for* `g04-0137`
  ↳ *evidence-for* `g07-0219`

- `g06-0211` *STATED* — Unused monthly API credits expire at the end of each billing cycle.
  — [g-this-week-in-claude-ranked-by-what-it-does-for-you](https://chen.media/guides/this-week-in-claude-ranked-by-what-it-does-for-you)
  ↳ *qualifies* `g06-0202`

- `g06-0235` *STATED* — The Haiku 5.5 test was one easy job with one run each, with cost as reported by Claude Code at API prices, including Claude Code's own setup text.
  — [g-send-claude-s-easy-jobs-to-haiku-5-5-with-one-helper-file](https://chen.media/guides/send-claude-s-easy-jobs-to-haiku-5-5-with-one-helper-file)
  ↳ *qualifies* `g06-0232`
  ↳ *example-of* `g06-0196`

- `g06-0236` *STATED* — Your numbers will differ, but the cost gap between Opus and Haiku 5.5 on simple jobs is large.
  > “Your numbers will differ, but the gap on simple jobs is large.”
  — [g-send-claude-s-easy-jobs-to-haiku-5-5-with-one-helper-file](https://chen.media/guides/send-claude-s-easy-jobs-to-haiku-5-5-with-one-helper-file)
  ↳ *qualifies* `g06-0232`

- `g07-0020` *STATED* — Alex's guide says Claude Code's next-prompt suggestion has a cost worth knowing about ('what it costs', covered under 'The catch'; email-gated).
  — [g-let-claude-code-write-your-next-prompt-press-tab](https://chen.media/guides/let-claude-code-write-your-next-prompt-press-tab)
  ↳ *part-of* `g07-0013`
  ↳ *because* `g07-0019` — cost is a reason to toggle it off

- `g07-0094` *STATED* — Haiku 5.5's $0.10 input and $0.50 output per-million-token prices apply to prompts up to 100K tokens.
  — [g-set-up-claude-haiku-5-5-10x-cheaper-claude-model](https://chen.media/guides/set-up-claude-haiku-5-5-10x-cheaper-claude-model)
  ↳ *qualifies* `g07-0092`
  ↳ *qualifies* `g07-0093`
  ↳ *evidence-for* `g07-0101`
  ↳ *evidence-for* `g05-0193`

- `g07-0100` *STATED* — Alex warns of two catches with Haiku 5.5 that change your bill ('The two catches'; email-gated).
  — [g-set-up-claude-haiku-5-5-10x-cheaper-claude-model](https://chen.media/guides/set-up-claude-haiku-5-5-10x-cheaper-claude-model)
  ↳ *part-of* `g07-0090`

- `g07-0101` *INFERRED* — A likely Haiku 5.5 bill catch: the headline $0.10/$0.50 rates are qualified to prompts up to 100K tokens, so prompts that use more of the 1M window probably cost more.
  — [g-set-up-claude-haiku-5-5-10x-cheaper-claude-model](https://chen.media/guides/set-up-claude-haiku-5-5-10x-cheaper-claude-model)
  ↳ *example-of* `g07-0100`

- `g07-0219` *STATED* — There is one thing the Max/Team API credits don't cover ('What it doesn't cover'; email-gated).
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *part-of* `g07-0203`
  ↳ *qualifies* `g07-0205`

- `g09-0141` *STATED* — /skill-doctor covers the skills in your session apart from Claude Code's bundled skills and your company's enterprise skills, which it leaves alone.
  — [g-find-the-claude-skills-eating-your-limit-skill-doctor](https://chen.media/guides/find-the-claude-skills-eating-your-limit-skill-doctor)
  ↳ *qualifies* `g09-0132`

- `g11-0111` *STATED* — Claude Code's advisor tool is experimental and may use more tokens.
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)
  ↳ *qualifies* `g11-0100`
  ↳ *qualifies* `g04-0240`

- `g11-0128` *STATED* — OpenAI's own docs say Ultrafast's 8x "measures token generation speed, not billing rates or overall task completion time".
  > “measures token generation speed, not billing rates or overall task completion time”
  — [g-is-openais-500-ultrafast-plan-worth-it](https://chen.media/guides/is-openais-500-ultrafast-plan-worth-it)
  ↳ *evidence-for* `g11-0129`
  ↳ *leads-to* `g11-0134`

- `g12-0123` *STATED* — Prompt caching makes the repeated part cheaper (cached tokens are billed at a fraction of the normal input price), but it is still billed on every turn and the conversation only gets longer.
  — [g-what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything)
  ↳ *qualifies* `g12-0121`
  ↳ *qualifies* `g19-0017` — prompt caching makes the re-read cheaper but it is still billed every turn
  ↳ *evidence-for* `g05-0146`

- `g12-0176` *CORE* — A /compact summary is lossy: the exact file path, the exact error message, or a rule you set at the start (e.g. 'never edit src/generated') can disappear, and Claude carries on without them.
  — [g-stop-claude-code-s-compact-from-summarizing-away-your-chat](https://chen.media/guides/stop-claude-code-s-compact-from-summarizing-away-your-chat)
  ↳ *qualifies* `g12-0175`
  ↳ *leads-to* `g12-0177`
  ↳ *qualifies* `g19-0003` — compaction summary is lossy

- `g12-0182` *STATED* — Guide section 'Good to know' holds the caveats for using Fast-Jev Compaction (body email-gated).
  — [g-stop-claude-code-s-compact-from-summarizing-away-your-chat](https://chen.media/guides/stop-claude-code-s-compact-from-summarizing-away-your-chat)
  ↳ *part-of* `g12-0171`
  ↳ *qualifies* `g12-0172`

- `g12-0243` *STATED* — In lower-priority mode, responses can pause while Claude Code waits for spare capacity.
  — [g-keep-using-claude-code-after-you-hit-your-usage-limit](https://chen.media/guides/keep-using-claude-code-after-you-hit-your-usage-limit)
  ↳ *qualifies* `g12-0242`

- `g12-0245` *STATED* — Claude Code's lower-priority mode is rolling out quietly, so not every account has it yet.
  — [g-keep-using-claude-code-after-you-hit-your-usage-limit](https://chen.media/guides/keep-using-claude-code-after-you-hit-your-usage-limit)
  ↳ *qualifies* `g12-0241`
  ↳ *leads-to* `g12-0248`

- `g12-0293` *STATED* — NVIDIA's free tier is rate-limited and meant for building and testing.
  — [g-free-kimi-k3-glm-and-deepseek-on-one-nvidia-key](https://chen.media/guides/free-kimi-k3-glm-and-deepseek-on-one-nvidia-key)
  ↳ *qualifies* `g12-0281`
  ↳ *example-of* `g17-0141`

- `g13-0104` *STATED* — Alex's laptop-closed guide has a section 'Who actually gets the credit' on cloud credit eligibility.
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it)
  ↳ *part-of* `g13-0099`
  ↳ *qualifies* `g13-0114`

- `g13-0114` *STATED* — The cloud credit is only for individual Pro and Max subscribers who were already subscribed on September 23, 2026.
  — [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)
  ↳ *qualifies* `g13-0099`

- `g13-0115` *STATED* — The cloud credit only pays for cloud sessions, not normal chats or Claude Code running on your own computer.
  — [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)
  ↳ *qualifies* `g13-0113`
  ↳ *qualifies* `y04-0021`

- `g13-0146` *INFERRED* — Because claude-mem shrinks notes with AI automatically in the background, its note-taking spends model usage on its own; watch it against your plan's usage limits.
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *because* `g13-0140`
  ↳ *depends-on* `g13-0145`
  ↳ *qualifies* `y04-0011` — claude-mem 95% less tokens claim vs its background AI note-taking spends usage on its own

- `g13-0182` *STATED* — Jev's 'faster' and 'cheaper' comparisons are TypeSafe's launch claims on their own workflow tests.
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *qualifies* `g13-0180`
  ↳ *qualifies* `g13-0181`
  ↳ *qualifies* `y04-0058` — TypeSafe launch claims on their own tests

- `g13-0183` *STATED* — How much Claude usage Jev saves depends on how many of your tasks are small, so measure it on your own work.
  > “How much Claude usage you save depends on how many of your tasks are small, so measure it on your own work.”
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *qualifies* `g13-0179`
  ↳ *evidence-for* `g17-0125`
  ↳ *qualifies* `y04-0062` — "80% more usage" vs savings depend on how many tasks are small; measure it

- `g13-0188` *STATED* — Alex's JEV guide ends with a 'Guardrails' section on limits for letting Jev make calls.
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *qualifies* `g13-0175`

- `g13-0230` *STATED* — Running Darwin Loop candidates as separate agents is optional and carries its own setup and usage costs.
  — [g-darwin-loop-evolve-the-winner](https://chen.media/guides/darwin-loop-evolve-the-winner)
  ↳ *qualifies* `g13-0229`

- `g14-0007` *STATED* — Claude Code subagents still consume model usage even though they run with their own separate context windows.
  > “they still consume model usage”
  — [g-marketing-agent-workflow-setup](https://chen.media/guides/marketing-agent-workflow-setup)
  ↳ *qualifies* `g14-0006`
  ↳ *evidence-for* `g14-0350`
  ↳ *evidence-for* `g04-0011`

- `g14-0082` *STATED* — Alex's Antigravity guide has a section on what the free plan actually means (free-tier limits).
  > “What the free plan means”
  — [g-antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you](https://chen.media/guides/antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you)
  ↳ *part-of* `g14-0072`

- `g14-0123` *STATED* — Alex's Jev guide explains what TypeSafe's 'free answers' (free output tokens) actually means and what is free versus paid.
  > “what “free answers” actually means”
  — [g-jev-typesafe-ai-explained](https://chen.media/guides/jev-typesafe-ai-explained)
  ↳ *part-of* `g14-0113`

- `g14-0131` *STATED* — AWS credits cover eligible AWS usage; they do not buy a Claude Max or consumer ChatGPT subscription.
  > “Credits cover eligible AWS usage; they do not buy a Claude Max or consumer ChatGPT subscription.”
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *part-of* `g14-0129`

- `g14-0140` *STATED* — Claude availability on Amazon Bedrock depends on your account, region, model and service permissions.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *qualifies* `g14-0139`

- `g14-0157` *STATED* — A model appearing in the Bedrock catalog does not guarantee your account can use it immediately or that a credit offer covers every charge.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *generalizes* `g14-0140`

- `g14-0169` *STATED* — Alex's AWS Bedrock guide was checked September 15 2026 and tells readers to recheck the account offer and model terms when they sign up.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *part-of* `g14-0129`
  ↳ *example-of* `g14-0347`

- `g14-0180` *STATED* — Spark-X2.5-4B's advertised maximum of one million tokens is a model capability, not a promise that a laptop has enough memory to use it.
  — [g-spark-x-local-ai-setup-guide](https://chen.media/guides/spark-x-local-ai-setup-guide)
  ↳ *example-of* `g14-0177`
  ↳ *generalizes* `g14-0276`

- `g14-0250` *STATED* — API usage or subscription limits still apply when Claude Octopus calls multiple providers.
  > “API usage or subscription limits still apply.”
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *qualifies* `g14-0249`
  ↳ *evidence-for* `g14-0350`

- `g14-0292` *STATED* — Running Claude Code or Cowork can require a paid plan or usage charges, even when the skills are free.
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *qualifies* `g14-0291`
  ↳ *evidence-for* `g14-0350`
  ↳ *qualifies* `g05-0314`

- `g14-0350` *CORE* — Skills, plugins, subagents and credits never make model usage free: subagents consume usage, Octopus is bound by API/subscription limits, free skill libraries still need a paid plan, and Bedrock calls are metered.
  — [g-marketing-agent-workflow-setup](https://chen.media/guides/marketing-agent-workflow-setup) [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide) [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills) [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock) [g-jev-typesafe-ai-explained](https://chen.media/guides/jev-typesafe-ai-explained)

- `g15-0096` *STATED* — The Judge Loop costs money: the guide states when it is worth running and when it is a waste of money.
  — [g-the-judge-loop-three-lines-that-put-claude-s-output-on-trial](https://chen.media/guides/the-judge-loop-three-lines-that-put-claude-s-output-on-trial)
  ↳ *qualifies* `g15-0092`
  ↳ *example-of* `g15-0177`
  ↳ *example-of* `g13-0305`

- `g15-0150` *STATED* — A one-tab aggregator costs you things a direct subscription does not (section 'What you give up, honestly', locked).
  — [g-every-premium-ai-model-in-one-place-how-the-one-tab-route-actually-works](https://chen.media/guides/every-premium-ai-model-in-one-place-how-the-one-tab-route-actually-works)
  ↳ *qualifies* `g15-0146`
  ↳ *example-of* `g15-0177`

- `g16-0048` *STATED* — deepclaude is genuinely worse at some work, so he says to split your day between it and normal Claude.
  > “What deepclaude is genuinely worse at, and how to split your day”
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you)
  ↳ *qualifies* `g16-0047`

- `g16-0291` *STATED* — The token figure in the plugins guide moves fortnightly, on purpose, and he flags it where it matters.
  > “The token figure moves fortnightly, on purpose”
  — [g-three-plugins-that-fix-claude-code-s-setup-limits-and-memory](https://chen.media/guides/three-plugins-that-fix-claude-code-s-setup-limits-and-memory)
  ↳ *qualifies* `g16-0284` — inferred: the moving token figure most likely belongs to OmniRoute

- `g17-0126` *STATED* — There are cases where context compression is not worth bothering with.
  > “When not to bother”
  — [g-cut-what-your-coding-agent-sends-to-the-model](https://chen.media/guides/cut-what-your-coding-agent-sends-to-the-model)
  ↳ *qualifies* `g17-0120`

- `g18-0098` *INFERRED* — Open Generative AI is free software but not free to run: generation is billed to your own API key, which is why the guide has a 'What it costs, honestly' section.
  — [g-the-open-source-ai-studio-that-replaces-a-video-subscription](https://chen.media/guides/the-open-source-ai-studio-that-replaces-a-video-subscription)
  ↳ *qualifies* `g18-0095`
  ↳ *example-of* `g18-0279`
  ↳ *qualifies* `g17-0313`

- `g19-0171` *STATED* — Claude Code Router needs Node.js 22 or newer.
  > “Needs Node.js 22 or newer.”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *qualifies* `g19-0168`

- `g19-0175` *INFERRED* — Routing 'easy work' to a cheaper model through Claude Code Router means configuring a second model provider; it is not a native Claude plan setting like /model opusplan.
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *qualifies* `g19-0170`
  ↳ *contrast* `g19-0005`

- `g20-0051` *STATED* — The Day 1 voice step uses Skills, which Anthropic describes as available to paid plans, so budget for Pro if you want the voice profile to persist.
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *qualifies* `g20-0028`

- `g21-0200` *STATED* — Skip Ultra mode for quick questions: it is slower to spin up and it costs more.
  — [g-three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team](https://chen.media/guides/three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team)
  ↳ *contrast* `g21-0201`

- `g22-0059` *STATED* — Use the Terra drafting station only when you want more than Luna quality.
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)
  ↳ *qualifies* `g22-0058`

- `r02-0038` *STATED* — Every /hunter run counts toward your Claude plan's usage, with two scorer sub-agents per job.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *qualifies* `r02-0076`
  ↳ *example-of* `r02-0150`

- `r02-0150` *CORE* — Every sub-agent an Alex Chen panel skill starts counts toward your Claude plan's usage.
  > “Every sub-agent counts toward your Claude plan's usage.”
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill) [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0311` — panels cost a sub-agent call per seat
  ↳ *evidence-for* `r01-0017`

- `r03-0041` *STATED* — Each /learn review is one Claude Code run and counts toward your plan's usage like any other session.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *qualifies* `r03-0031`
  ↳ *example-of* `r03-0169`
  ↳ *evidence-for* `r04-0161`

- `r03-0168` *STATED* — One /linkedin-roast run starts five sub-agents and counts toward your Claude plan's usage.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0169`
  ↳ *because* `r03-0155`

- `y01-0016` *STATED* — Higher reasoning effort gives the model more room to reason through a hard request, but it can take longer and uses more of your usage limit.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *evidence-for* `g10-0197`
  ↳ *evidence-for* `y01-0148`

- `y01-0020` *STATED* — Fast mode does not mean you are choosing a smarter model - it only changes speed (at a higher usage cost).
  > “It doesn't mean you're choosing a smarter model.”
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *qualifies* `y01-0019`

- `y01-0032` *STATED* — A new Codex chat doesn't automatically contain the project's other conversations - each chat has its own discussion and context, so rules meant for every chat must be saved separately.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *qualifies* `y01-0031`
  ↳ *leads-to* `y01-0063` — cross-chat rules need AGENTS.md
  ↳ *contrast* `y01-0160` — Codex: each chat has its own context; Claude video: standard chats 'mesh' info across chats

- `y02-0130` *INFERRED* — The video never spells out the Skill Doctor's exact command name (it is hidden behind the 'doctor' CTA); in Claude Code the documented ways to see skill/tool context cost are /context, and /doctor runs diagnostics — verify which one he means.
  — [Zy2NN8NydeA](https://youtu.be/Zy2NN8NydeA) [Eokwl898JUk](https://youtu.be/Eokwl898JUk)
  ↳ *qualifies* `g09-0132`
  ↳ *qualifies* `y02-0127`

- `y03-0107` *INFERRED* — Auto-installing skills with Find Skills sits against Alex's token warning that plugins load into every chat even when unused: each added extension can carry a standing context cost.
  — [wfwnTNtnomk](https://youtu.be/wfwnTNtnomk) [1j9mmXDW8Qw](https://youtu.be/1j9mmXDW8Qw) [Rgb7FFLwz60](https://youtu.be/Rgb7FFLwz60)

### claim

- `g01-0091` *STATED* — Graphicle's cited context names the file and lines of every excerpt, within a token budget.
  — [g-give-claude-a-map-and-a-memory-of-your-whole-project](https://chen.media/guides/give-claude-a-map-and-a-memory-of-your-whole-project)
  ↳ *part-of* `g01-0087`
  ↳ *qualifies* `g01-0088`

- `g01-0120` *INFERRED* — Cutting a reply from 94 to 35 words (about 63% fewer) also cuts output tokens, so answer-first skills like I Have ADHD double as a usage saver.
  — [g-i-have-adhd-make-claude-lead-with-the-answer-instead-of-burying-it](https://chen.media/guides/i-have-adhd-make-claude-lead-with-the-answer-instead-of-burying-it)
  ↳ *qualifies* `g01-0105`
  ↳ *evidence-for* `g03-0099`

- `g02-0034` *CORE* — Every web page, log file and GitHub issue Claude reads lands in its context window.
  > “Every web page, log file and GitHub issue Claude reads lands in its context window.”
  — [g-stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode)
  ↳ *evidence-for* `g02-0241`
  ↳ *evidence-for* `g04-0007`

- `g02-0130` *STATED* — Atticus runs on the Claude plan you already have rather than needing its own subscription.
  > “using the Claude plan you already pay for”
  — [g-control-your-whole-mac-with-your-voice-powered-by-claude](https://chen.media/guides/control-your-whole-mac-with-your-voice-powered-by-claude)
  ↳ *part-of* `g02-0129`
  ↳ *example-of* `g05-0314`

- `g02-0138` *STATED* — Simple Atticus asks like 'Open Spotify.' skip the AI entirely and run in a blink.
  — [g-control-your-whole-mac-with-your-voice-powered-by-claude](https://chen.media/guides/control-your-whole-mac-with-your-voice-powered-by-claude)
  ↳ *qualifies* `g02-0130` — fast path spares the Claude plan
  ↳ *part-of* `g02-0129`
  ↳ *example-of* `g02-0241`

- `g02-0180` *CORE* — Claude's codebase rediscovery burns tool calls, tokens and time, and it happens again next session.
  > “That rediscovery burns tool calls, tokens and time, and it happens again next session.”
  — [g-trail-code-stop-claude-getting-lost-in-your-code](https://chen.media/guides/trail-code-stop-claude-getting-lost-in-your-code)
  ↳ *evidence-for* `g02-0241`
  ↳ *evidence-for* `g03-0121`

- `g02-0181` *STATED* — Trail-code builds the code map once, on your machine, with no model and no API key.
  — [g-trail-code-stop-claude-getting-lost-in-your-code](https://chen.media/guides/trail-code-stop-claude-getting-lost-in-your-code)
  ↳ *part-of* `g02-0176`
  ↳ *example-of* `g02-0240`

- `g02-0182` *STATED* — Trail-code keeps its code map current when your code changes.
  — [g-trail-code-stop-claude-getting-lost-in-your-code](https://chen.media/guides/trail-code-stop-claude-getting-lost-in-your-code)
  ↳ *part-of* `g02-0176`

- `g02-0197` *CORE* — Each time a Claude Code loop fires, even while you are away from the keyboard, Claude sends your whole chat again, and that comes out of your plan's limit.
  — [g-find-the-claude-code-loops-that-are-quietly-eating-your-limit](https://chen.media/guides/find-the-claude-code-loops-that-are-quietly-eating-your-limit)
  ↳ *evidence-for* `g02-0195`
  ↳ *evidence-for* `g02-0241`
  ↳ *example-of* `g19-0017`

- `g02-0241` *CORE* — Several featured tools attack context and usage waste from different angles: Context Mode sandboxes tool output, Trail-code stops codebase rediscovery, finding forgotten /loops stops silent chat resends, and cc-stretch cuts what you have to read.
  — [g-stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode) [g-trail-code-stop-claude-getting-lost-in-your-code](https://chen.media/guides/trail-code-stop-claude-getting-lost-in-your-code) [g-find-the-claude-code-loops-that-are-quietly-eating-your-limit](https://chen.media/guides/find-the-claude-code-loops-that-are-quietly-eating-your-limit) [g-make-claude-s-long-answers-6x-shorter-to-read](https://chen.media/guides/make-claude-s-long-answers-6x-shorter-to-read)

- `g03-0016` *CORE* — Claude Code reads your CLAUDE.md at the start of every session, so it loads even when the session is about unrelated work.
  > “Your CLAUDE.md loads into every session, even for unrelated work.”
  — [g-shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit](https://chen.media/guides/shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit)
  ↳ *leads-to* `g03-0017`
  ↳ *evidence-for* `g03-0025`
  ↳ *part-of* `g18-0283`

- `g03-0017` *STATED* — A long CLAUDE.md rides along in context even when you are doing something unrelated, eating your Claude limit.
  — [g-shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit](https://chen.media/guides/shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit)
  ↳ *example-of* `g03-0001`

- `g03-0027` *STATED* — Tagging a file with @ in Claude Code puts the file's whole content into the conversation.
  — [g-stop-file-mentions-from-pasting-whole-files-into-your-claude-chat](https://chen.media/guides/stop-file-mentions-from-pasting-whole-files-into-your-claude-chat)
  ↳ *qualifies* `g03-0028`
  ↳ *leads-to* `g03-0029`
  ↳ *example-of* `g03-0121` — inlined files are another way files add to context
  ↳ *example-of* `g15-0015`

- `g03-0052` *STATED* — A 529 overloaded error is not your usage limit and does not count against your quota.
  > “A 529 overloaded error is not your usage limit and doesn't count against your quota.”
  — [g-keep-claude-retrying-overnight-when-the-api-is-busy](https://chen.media/guides/keep-claude-retrying-overnight-when-the-api-is-busy)
  ↳ *qualifies* `g03-0056`
  ↳ *contrast* `g03-0166` — capacity errors (watchdog) vs usage-limit resets (auto-continue)
  ↳ *contrast* `g03-0165`

- `g03-0073` *CORE* — The /usage command ranks skills, subagents, plugins and MCP servers by how much of your Claude limit they use, and flags the habits behind it.
  — [g-find-what-is-draining-your-claude-limit-with-usage](https://chen.media/guides/find-what-is-draining-your-claude-limit-with-usage)

- `g03-0074` *STATED* — On a Pro, Max, Team or Enterprise plan, Claude Code can show you what is counting against your plan limits.
  — [g-find-what-is-draining-your-claude-limit-with-usage](https://chen.media/guides/find-what-is-draining-your-claude-limit-with-usage)
  ↳ *qualifies* `g03-0073`

- `g03-0077` *STATED* — The /usage breakdown lists recent usage attributed to skills, subagents, plugins and individual MCP servers, each as a percentage of the total.
  — [g-find-what-is-draining-your-claude-limit-with-usage](https://chen.media/guides/find-what-is-draining-your-claude-limit-with-usage)
  ↳ *defines* `g03-0073`
  ↳ *evidence-for* `g03-0015` — /usage attributes cost to subagents, skills, plugins, MCP servers

- `g03-0099` *CORE* — Every polite opener and long recap Claude writes is output you pay for in your limit.
  > “Every polite opener and long recap Claude writes is output you pay for in your limit.”
  — [g-make-claude-answer-in-fewer-words-with-the-caveman-skill](https://chen.media/guides/make-claude-answer-in-fewer-words-with-the-caveman-skill)
  ↳ *because* `g03-0100`
  ↳ *contrast* `g03-0235` — Caveman cuts words; Answer me with HTML cuts markup tokens

- `g03-0109` *STATED* — Claude Code sends your full conversation with every request.
  > “Claude Code sends your full conversation with every request”
  — [g-rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it](https://chen.media/guides/rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it)
  ↳ *evidence-for* `g03-0001`
  ↳ *because* `g03-0110`
  ↳ *evidence-for* `g19-0017`

- `g03-0110` *STATED* — Arguing leaves the wrong turn and every correction in the chat, where they ride along on every later request.
  — [g-rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it](https://chen.media/guides/rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it)
  ↳ *example-of* `g03-0001`
  ↳ *evidence-for* `g16-0278`

- `g03-0111` *STATED* — Rewinding takes the wrong turn and the corrections out of the conversation instead of piling more on top.
  — [g-rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it](https://chen.media/guides/rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it)
  ↳ *part-of* `g03-0009`
  ↳ *contrast* `g03-0108`
  ↳ *contrast* `g03-0154` — rewind cleans up after a wrong turn; plan mode prevents it

- `g03-0120` *STATED* — To find one function, Claude often searches your code as plain text and then opens several candidate files to check each match.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *leads-to* `g03-0121`

- `g03-0121` *CORE* — Every file Claude opens adds to your context and your limit.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)

- `g03-0154` *CORE* — If Claude's first guess is wrong you pay for the re-work in your limit.
  — [g-turn-on-plan-mode-so-claude-plans-before-it-edits](https://chen.media/guides/turn-on-plan-mode-so-claude-plans-before-it-edits)
  ↳ *evidence-for* `g19-0012`

- `g03-0155` *STATED* — Anthropic's cost guide points to plan mode for complex tasks.
  — [g-turn-on-plan-mode-so-claude-plans-before-it-edits](https://chen.media/guides/turn-on-plan-mode-so-claude-plans-before-it-edits)
  ↳ *evidence-for* `g03-0156`

- `g03-0157` *STATED* — The docs say plan mode prevents expensive re-work when the initial direction is wrong.
  > “prevents expensive re-work when the initial direction is wrong”
  — [g-turn-on-plan-mode-so-claude-plans-before-it-edits](https://chen.media/guides/turn-on-plan-mode-so-claude-plans-before-it-edits)
  ↳ *example-of* `g03-0007`
  ↳ *contrast* `g03-0154`

- `g03-0165` *STATED* — When you hit your Claude usage limit mid-task, you used to have to come back later and type continue.
  — [g-let-claude-code-wait-out-your-limit-and-carry-on](https://chen.media/guides/let-claude-code-wait-out-your-limit-and-carry-on)

- `g03-0166` *STATED* — In Claude Code v2.1.234 and later, a session that hits the usage limit waits, shows when the limit resets, then picks the task back up where it stopped.
  — [g-let-claude-code-wait-out-your-limit-and-carry-on](https://chen.media/guides/let-claude-code-wait-out-your-limit-and-carry-on)
  ↳ *part-of* `g03-0010`
  ↳ *contrast* `g03-0165`

- `g03-0167` *STATED* — The docs say auto-continue at the usage limit is on by default for interactive sessions signed in with a Claude subscription.
  — [g-let-claude-code-wait-out-your-limit-and-carry-on](https://chen.media/guides/let-claude-code-wait-out-your-limit-and-carry-on)
  ↳ *example-of* `g03-0007`
  ↳ *qualifies* `g03-0166`

- `g03-0174` *STATED* — Step 2 of the auto-continue guide explains what happens at the limit reset.
  — [g-let-claude-code-wait-out-your-limit-and-carry-on](https://chen.media/guides/let-claude-code-wait-out-your-limit-and-carry-on)
  ↳ *part-of* `g03-0166`

- `g03-0187` *STATED* — When you set a goal with /goal and it waits on a slow background job, Claude Code checks in on that job after 30 minutes.
  — [g-stop-claude-goal-check-ins-from-eating-your-limit](https://chen.media/guides/stop-claude-goal-check-ins-from-eating-your-limit)
  ↳ *leads-to* `g03-0188`

- `g03-0188` *STATED* — A /goal check-in is a new turn, and every turn sends your whole conversation again.
  > “every turn sends your whole conversation again”
  — [g-stop-claude-goal-check-ins-from-eating-your-limit](https://chen.media/guides/stop-claude-goal-check-ins-from-eating-your-limit)
  ↳ *evidence-for* `g03-0001`
  ↳ *leads-to* `g03-0189`
  ↳ *example-of* `g19-0017`

- `g03-0190` *STATED* — One setting turns /goal check-ins off: CLAUDE_CODE_GOAL_CHECKIN_MINUTES.
  — [g-stop-claude-goal-check-ins-from-eating-your-limit](https://chen.media/guides/stop-claude-goal-check-ins-from-eating-your-limit)
  ↳ *contrast* `g03-0189`

- `g03-0198` *STATED* — Roast Room runs on your Claude plan with no API key needed.
  — [g-roast-room-a-free-claude-council-that-argues-over-your-business-decisions](https://chen.media/guides/roast-room-a-free-claude-council-that-argues-over-your-business-decisions)
  ↳ *qualifies* `g03-0196`
  ↳ *example-of* `g05-0314`

- `g03-0211` *STATED* — A helper agent (subagent) runs on your session's model unless something else picks one.
  — [g-run-every-claude-helper-agent-on-haiku](https://chen.media/guides/run-every-claude-helper-agent-on-haiku)
  ↳ *example-of* `g03-0015`
  ↳ *leads-to* `g03-0212`
  ↳ *evidence-for* `g06-0087`

- `g03-0213` *STATED* — Two settings lines put every subagent, teammate and workflow agent on Haiku.
  — [g-run-every-claude-helper-agent-on-haiku](https://chen.media/guides/run-every-claude-helper-agent-on-haiku)
  ↳ *part-of* `g03-0009`
  ↳ *example-of* `y02-0187`

- `g03-0221` *STATED* — Subagent descriptions take up room in Claude's context, and with many helpers with long descriptions that room adds up.
  — [g-shorten-your-claude-helper-agent-descriptions](https://chen.media/guides/shorten-your-claude-helper-agent-descriptions)
  ↳ *example-of* `g03-0001`
  ↳ *example-of* `g03-0015`
  ↳ *example-of* `g18-0283`

- `g04-0001` *STATED* — Claude Code 2.1.299, released October 14, added warnings to the /usage screen for habits that burn through a Claude plan's usage limit.
  > “On October 14, Claude Code 2.1.299 added warnings in /usage for four habits that burn through a plan”
  — [g-the-four-habits-eating-your-claude-limit-and-the-fix-for-each](https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each)
  ↳ *part-of* `g04-0013`
  ↳ *part-of* `g03-0073`

- `g04-0009` *CORE* — Claude Code sends your whole conversation with every request, so everything already in the chat is sent again on each new turn.
  > “Claude Code sends your whole conversation with every request”
  — [g-the-four-habits-eating-your-claude-limit-and-the-fix-for-each](https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each) [g-the-claude-hook-that-cuts-test-output-down-to-just-the-failures](https://chen.media/guides/the-claude-hook-that-cuts-test-output-down-to-just-the-failures) [g-make-your-claude-helper-agents-compact-their-own-chat-early](https://chen.media/guides/make-your-claude-helper-agents-compact-their-own-chat-early)
  ↳ *generalizes* `g04-0086`
  ↳ *generalizes* `g04-0202`
  ↳ *evidence-for* `g19-0017`

- `g04-0010` *STATED* — Each time Claude uses tools, Claude Code sends another request carrying that batch of tool results.
  — [g-the-four-habits-eating-your-claude-limit-and-the-fix-for-each](https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each)
  ↳ *qualifies* `g04-0009`

- `g04-0011` *STATED* — Every subagent, and every agent a workflow spawns, sends its own requests on top of the main conversation's requests.
  — [g-the-four-habits-eating-your-claude-limit-and-the-fix-for-each](https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each)

- `g04-0012` *INFERRED* — Because the whole conversation is re-sent on every request, a large tool result or always-on context is not a one-time cost: it is paid again on every later turn.
  — [g-the-four-habits-eating-your-claude-limit-and-the-fix-for-each](https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each)
  ↳ *because* `g04-0009`
  ↳ *leads-to* `g04-0006`
  ↳ *leads-to* `g04-0007`

- `g04-0072` *STATED* — A tokentab monthly statement shows the total up top, then every project, model and day itemised below.
  — [g-tokentab-see-where-every-claude-token-goes-as-a-monthly-statement](https://chen.media/guides/tokentab-see-where-every-claude-token-goes-as-a-monthly-statement)
  ↳ *part-of* `g04-0071`

- `g04-0073` *STATED* — tokentab runs entirely on your machine: no account, no API key, nothing uploaded.
  — [g-tokentab-see-where-every-claude-token-goes-as-a-monthly-statement](https://chen.media/guides/tokentab-see-where-every-claude-token-goes-as-a-monthly-statement)
  ↳ *qualifies* `g04-0071`

- `g04-0076` *STATED* — tokentab adds up the logged token counts so you can see which project, which model and which days ate your usage.
  — [g-tokentab-see-where-every-claude-token-goes-as-a-monthly-statement](https://chen.media/guides/tokentab-see-where-every-claude-token-goes-as-a-monthly-statement)
  ↳ *part-of* `g04-0071`

- `g04-0077` *STATED* — tokentab labels what kind of work each session was: feature, refactor, debugging, or chat.
  — [g-tokentab-see-where-every-claude-token-goes-as-a-monthly-statement](https://chen.media/guides/tokentab-see-where-every-claude-token-goes-as-a-monthly-statement)
  ↳ *part-of* `g04-0071`

- `g04-0080` *STATED* — Breakdowns like 'refactoring took 36% of spend' can't be seen from Claude's usage-limit bar alone.
  > “that's the kind of thing you can't see from the limit bar alone”
  — [g-tokentab-see-where-every-claude-token-goes-as-a-monthly-statement](https://chen.media/guides/tokentab-see-where-every-claude-token-goes-as-a-monthly-statement)
  ↳ *because* `g04-0075`

- `g04-0085` *STATED* — When Claude runs your tests, the whole test output lands in your chat.
  — [g-the-claude-hook-that-cuts-test-output-down-to-just-the-failures](https://chen.media/guides/the-claude-hook-that-cuts-test-output-down-to-just-the-failures)
  ↳ *leads-to* `g04-0086`
  ↳ *example-of* `g04-0007` — test logs are a large tool result

- `g04-0086` *STATED* — A full test log in the chat is sent again with every later request, which wastes tokens.
  > “your whole chat is sent again with every request after”
  — [g-the-claude-hook-that-cuts-test-output-down-to-just-the-failures](https://chen.media/guides/the-claude-hook-that-cuts-test-output-down-to-just-the-failures)
  ↳ *because* `g04-0009`
  ↳ *example-of* `g04-0012`

- `g04-0121` *STATED* — Claude Max and Team plans include monthly credits for the Claude API.
  — [g-how-to-claim-your-monthly-claude-credits-on-max-and-team-plans](https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans) [g-how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets](https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets)
  ↳ *part-of* `g04-0145`

- `g04-0123` *STATED* — You don't need to add a card to Claude Platform to claim the monthly Claude API credits.
  — [g-how-to-claim-your-monthly-claude-credits-on-max-and-team-plans](https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans) [g-how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets](https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets)
  ↳ *qualifies* `g04-0122`

- `g04-0127` *STATED* — Team plan API credits from every seat are pooled into one shared balance.
  — [g-how-to-claim-your-monthly-claude-credits-on-max-and-team-plans](https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans) [g-how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets](https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets)
  ↳ *qualifies* `g04-0126`

- `g04-0138` *STATED* — On a Claude Team plan, an owner has to claim the monthly API credits.
  — [g-how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets](https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets)
  ↳ *qualifies* `g04-0122`
  ↳ *part-of* `g04-0146`

- `g04-0141` *STATED* — A Team plan's API credit amount is based on the seats on the plan at the start of each billing month.
  — [g-how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets](https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets)
  ↳ *qualifies* `g04-0126`

- `g04-0202` *STATED* — Everything a Claude Code subagent reads stays in its chat, and each new step sends that whole pile again.
  — [g-make-your-claude-helper-agents-compact-their-own-chat-early](https://chen.media/guides/make-your-claude-helper-agents-compact-their-own-chat-early)
  ↳ *part-of* `g04-0201`
  ↳ *example-of* `g19-0017`

- `g04-0203` *STATED* — When a subagent's chat gets big, the subagent compacts it into a summary.
  — [g-make-your-claude-helper-agents-compact-their-own-chat-early](https://chen.media/guides/make-your-claude-helper-agents-compact-their-own-chat-early)
  ↳ *because* `g04-0202`

- `g04-0204` *STATED* — A Claude Code setting lets you choose the size at which a subagent compacts its own chat, so it can compact earlier.
  — [g-make-your-claude-helper-agents-compact-their-own-chat-early](https://chen.media/guides/make-your-claude-helper-agents-compact-their-own-chat-early)
  ↳ *qualifies* `g04-0203`
  ↳ *part-of* `g04-0211`
  ↳ *generalizes* `g06-0064`

- `g04-0210` *INFERRED* — Making subagents compact earlier cuts usage because every subagent step re-sends its whole chat, and subagents send requests on top of the main conversation.
  — [g-make-your-claude-helper-agents-compact-their-own-chat-early](https://chen.media/guides/make-your-claude-helper-agents-compact-their-own-chat-early) [g-the-four-habits-eating-your-claude-limit-and-the-fix-for-each](https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each)
  ↳ *because* `g04-0202`
  ↳ *because* `g04-0011`

- `g04-0230` *STATED* — Most turns in a Claude Code session are routine: reading files, running tests.
  > “Most turns in a Claude Code session are routine: reading files, running tests.”
  — [g-let-opus-advise-while-sonnet-does-the-routine-work](https://chen.media/guides/let-opus-advise-while-sonnet-does-the-routine-work)

- `g04-0240` *INFERRED* — The advisor is a model-routing cost lever: the cheaper Sonnet main model handles most turns and Opus is consulted only at decisive moments.
  — [g-let-opus-advise-while-sonnet-does-the-routine-work](https://chen.media/guides/let-opus-advise-while-sonnet-does-the-routine-work)
  ↳ *generalizes* `g04-0231`
  ↳ *example-of* `y02-0187`

- `g05-0036` *STATED* — Because one Chrome Relay command executes a whole goal, Claude doesn't need a model round trip per click.
  — [g-let-claude-use-your-real-chrome-signed-in-in-background-tabs](https://chen.media/guides/let-claude-use-your-real-chrome-signed-in-in-background-tabs)
  ↳ *because* `g05-0035`

- `g05-0101` *STATED* — With Effortless installed you never touch Claude Code's Effort setting again.
  > “You never touch the Effort setting again.”
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless)
  ↳ *part-of* `g05-0098`
  ↳ *because* `g05-0099`
  ↳ *contradicts* `g05-0149` — auto per-prompt effort vs 'pick your model and effort level at the top of a session'

- `g05-0112` *STATED* — The Effortless guide explains why automatic per-prompt effort saves money (section 'Why it saves').
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless)
  ↳ *part-of* `g05-0098`

- `g05-0136` *STATED* — In Mortiflix, waiting on you costs nothing because the Claude session has already stopped.
  > “Waiting on you costs nothing.”
  — [g-mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer](https://chen.media/guides/mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer)
  ↳ *because* `g05-0135`
  ↳ *contrast* `g05-0203` — a stopped session costs nothing; an old chat resumed costs the whole chat

- `g05-0137` *STATED* — Mortiflix runs on your own Claude Code login (your plan pays) or your own Anthropic API key (you pay per token).
  — [g-mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer](https://chen.media/guides/mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer)
  ↳ *part-of* `g05-0128`
  ↳ *example-of* `g05-0314`

- `g05-0144` *STATED* — Each Claude model keeps its own prompt cache, so switching models mid-chat makes the next message re-read the whole conversation uncached.
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)
  ↳ *evidence-for* `g05-0315`

- `g05-0145` *STATED* — Claude Code re-sends your whole conversation on every message.
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)
  ↳ *because* `g05-0146` — caching matters because the whole chat is re-sent
  ↳ *evidence-for* `g19-0017`

- `g05-0148` *STATED* — The cost of a mid-chat /model switch is one slower, more expensive turn.
  > “That one slower, more expensive turn is the cost.”
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)
  ↳ *qualifies* `g05-0144`

- `g05-0154` *STATED* — Compaction replaces your history with a summary, so the cache for the old history is not reused.
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)
  ↳ *because* `g05-0153`
  ↳ *evidence-for* `g05-0202` — compaction drops the cache for the old history
  ↳ *qualifies* `g06-0064` — compaction also discards the prompt cache for old history

- `g05-0158` *STATED* — The cache guide lists what does not break the prompt cache, per the docs ('What does not break the cache').
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)
  ↳ *qualifies* `g05-0144`

- `g05-0159` *STATED* — Besides /model and /compact, other actions also start a fresh prompt cache ('Other things that start a fresh cache').
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)
  ↳ *generalizes* `g05-0154`

- `g05-0163` *STATED* — Claude Code docs say lower effort is faster and cheaper for straightforward tasks.
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)
  ↳ *evidence-for* `g05-0166`
  ↳ *evidence-for* `y01-0014`

- `g05-0165` *STATED* — You are charged for all thinking tokens generated.
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)
  ↳ *evidence-for* `g05-0166`
  ↳ *evidence-for* `g05-0112` — thinking tokens are billed, so lower effort saves
  ↳ *evidence-for* `g10-0197`

- `g05-0166` *STATED* — A subagent that only renames files or searches the repo does not need to run at max effort.
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)

- `g05-0183` *STATED* — Haiku 5.5 is ten times cheaper per token than Haiku 4.5 ($1.00 -> $0.10 input, $5.00 -> $0.50 output).
  — [g-claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command](https://chen.media/guides/claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command)
  ↳ *generalizes* `g05-0179`
  ↳ *evidence-for* `y02-0024`
  ↳ *evidence-for* `y02-0026`

- `g05-0195` *STATED* — Claude Code's docs answer three things almost everyone gets wrong about their usage limit.
  — [g-three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha](https://chen.media/guides/three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha)

- `g05-0200` *STATED* — A model switch costs a cache rebuild: the first message after it rereads the whole chat with no cache hits.
  — [g-three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha](https://chen.media/guides/three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha)
  ↳ *qualifies* `g05-0196`
  ↳ *evidence-for* `g05-0315`
  ↳ *evidence-for* `g05-0144`

- `g05-0314` *CORE* — Featured tools run on your own Claude login instead of a paid API key: Effortless (Haiku, no key), Mortiflix (Claude Code login or API key), OpenQodex (your own login), Founder (no API key).
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless) [g-mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer](https://chen.media/guides/mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer) [g-install-openqodex-a-second-claude-reviews-your-code-before-you-push](https://chen.media/guides/install-openqodex-a-second-claude-reviews-your-code-before-you-push) [g-the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar](https://chen.media/guides/the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar)

- `g05-0315` *CORE* — Each Claude model has its own prompt cache, so a mid-task model switch forces a full uncached re-read of the conversation.
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup) [g-three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha](https://chen.media/guides/three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha)

- `g06-0061` *CORE* — Claude Code sends your whole chat with every message, so in a long session every request carries the whole conversation, old tangents included.
  > “Claude Code sends your whole chat with every message.”
  — [g-make-claude-compact-earlier-the-setting-and-the-claude-md-note](https://chen.media/guides/make-claude-compact-earlier-the-setting-and-the-claude-md-note)
  ↳ *evidence-for* `g19-0017`

- `g06-0062` *STATED* — Anthropic's cost guide says a one-line question late in a day-long session still draws usage for the entire history.
  — [g-make-claude-compact-earlier-the-setting-and-the-claude-md-note](https://chen.media/guides/make-claude-compact-earlier-the-setting-and-the-claude-md-note)
  ↳ *evidence-for* `g06-0061`
  ↳ *evidence-for* `g19-0017`
  ↳ *evidence-for* `g19-0019`

- `g06-0063` *STATED* — One command makes Claude Code summarize the conversation pile earlier, and a short CLAUDE.md note keeps the facts that matter.
  — [g-make-claude-compact-earlier-the-setting-and-the-claude-md-note](https://chen.media/guides/make-claude-compact-earlier-the-setting-and-the-claude-md-note)
  ↳ *because* `g06-0061`

- `g06-0073` *INFERRED* — Compacting at 200K instead of the ~967K default caps how much history each later message re-sends, which slows usage drain in long Claude Code sessions.
  — [g-make-claude-compact-earlier-the-setting-and-the-claude-md-note](https://chen.media/guides/make-claude-compact-earlier-the-setting-and-the-claude-md-note)
  ↳ *because* `g06-0061`
  ↳ *depends-on* `g06-0069`
  ↳ *evidence-for* `g19-0021`

- `g06-0086` *STATED* — Anthropic's docs say dynamic workflow runs count toward your plan's usage and rate limits.
  — [g-run-claude-agent-swarms-without-burning-your-limit](https://chen.media/guides/run-claude-agent-swarms-without-burning-your-limit)
  ↳ *evidence-for* `g06-0084`

- `g06-0087` *CORE* — A workflow agent with no other model assigned runs on your session's model, so an Opus session means an Opus swarm.
  > “an Opus session means an Opus swarm”
  — [g-run-claude-agent-swarms-without-burning-your-limit](https://chen.media/guides/run-claude-agent-swarms-without-burning-your-limit)
  ↳ *qualifies* `g06-0084`
  ↳ *evidence-for* `g03-0212`

- `g06-0088` *STATED* — Every workflow agent draws on the same plan limit as your normal chat.
  — [g-run-claude-agent-swarms-without-burning-your-limit](https://chen.media/guides/run-claude-agent-swarms-without-burning-your-limit)
  ↳ *qualifies* `g06-0086`
  ↳ *evidence-for* `g14-0350`

- `g06-0098` *STATED* — Claude Code voice dictation does not use up your Claude messages or usage limits.
  — [g-talk-to-claude-code-instead-of-typing](https://chen.media/guides/talk-to-claude-code-instead-of-typing)
  ↳ *qualifies* `g06-0096`
  ↳ *contrast* `g06-0088` — voice costs nothing; every swarm agent shares the limit

- `g06-0202` *STATED* — The #1 Claude change of the week of October 5, 2026: monthly API credits on Max and Team plans.
  — [g-this-week-in-claude-ranked-by-what-it-does-for-you](https://chen.media/guides/this-week-in-claude-ranked-by-what-it-does-for-you)
  ↳ *part-of* `g06-0201`
  ↳ *evidence-for* `g04-0121`

- `g06-0264` *CORE* — Alex's core limit lever: route easy jobs to a cheaper model (Haiku) instead of letting everything, including swarm agents, run on your Opus session model.
  — [g-make-your-claude-limit-last-the-haiku-helper-and-3-habits](https://chen.media/guides/make-your-claude-limit-last-the-haiku-helper-and-3-habits) [g-send-claude-s-easy-jobs-to-haiku-5-5-with-one-helper-file](https://chen.media/guides/send-claude-s-easy-jobs-to-haiku-5-5-with-one-helper-file) [g-run-claude-agent-swarms-without-burning-your-limit](https://chen.media/guides/run-claude-agent-swarms-without-burning-your-limit)
  ↳ *generalizes* `g06-0222`
  ↳ *because* `g06-0087`
  ↳ *example-of* `y02-0187`

- `g07-0090` *STATED* — Claude Haiku 5.5 costs a tenth of the old Haiku per token and reads a million tokens at once.
  — [g-set-up-claude-haiku-5-5-10x-cheaper-claude-model](https://chen.media/guides/set-up-claude-haiku-5-5-10x-cheaper-claude-model)
  ↳ *evidence-for* `g07-0300`
  ↳ *evidence-for* `y02-0024`

- `g07-0105` *STATED* — Every task you give Claude Code on Opus comes out of your plan's limit, even renaming a file.
  — [g-make-claude-code-limit-last-longer-haiku-5-5-helper](https://chen.media/guides/make-claude-code-limit-last-longer-haiku-5-5-helper)
  ↳ *part-of* `g07-0104`
  ↳ *because* `g07-0108`
  ↳ *evidence-for* `y02-0019`

- `g07-0106` *STATED* — Anthropic's own help page says Opus uses meaningfully more of your usage than Sonnet or Haiku.
  — [g-make-claude-code-limit-last-longer-haiku-5-5-helper](https://chen.media/guides/make-claude-code-limit-last-longer-haiku-5-5-helper)
  ↳ *part-of* `g07-0104`
  ↳ *evidence-for* `g07-0105`
  ↳ *example-of* `g07-0301` — Anthropic's own help page
  ↳ *evidence-for* `y02-0187`

- `g07-0107` *STATED* — Per Anthropic, Haiku is meant for quick lookups and simple edits.
  — [g-make-claude-code-limit-last-longer-haiku-5-5-helper](https://chen.media/guides/make-claude-code-limit-last-longer-haiku-5-5-helper)
  ↳ *part-of* `g07-0104`
  ↳ *evidence-for* `g07-0111`
  ↳ *evidence-for* `y01-0137`

- `g07-0111` *STATED* — Jobs the CLAUDE.md note hands to the Haiku helper: searching files, reading logs, listing folders, renames, one-line edits, and running a command and reporting the result.
  — [g-make-claude-code-limit-last-longer-haiku-5-5-helper](https://chen.media/guides/make-claude-code-limit-last-longer-haiku-5-5-helper)
  ↳ *part-of* `g07-0104`

- `g07-0112` *STATED* — With the Haiku helper, Opus keeps planning, debugging and anything that changes several files.
  — [g-make-claude-code-limit-last-longer-haiku-5-5-helper](https://chen.media/guides/make-claude-code-limit-last-longer-haiku-5-5-helper)
  ↳ *part-of* `g07-0104`
  ↳ *contrast* `g07-0111`

- `g07-0203` *STATED* — Claude Max and Team plans now come with up to $500 a month of Claude API credits, and you have to claim them yourself.
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *evidence-for* `g04-0122`

- `g07-0205` *STATED* — The Max/Team API credits are real money to run your own apps and agents on Claude, on top of your normal plan.
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *part-of* `g07-0203`

- `g07-0212` *STATED* — Team API credits are pooled into one balance and capped at $500 a month.
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *part-of* `g07-0203`
  ↳ *evidence-for* `g07-0203` — the $500 cap is the Team pool
  ↳ *evidence-for* `g04-0128`

- `g07-0214` *STATED* — Free, Pro and Enterprise plans don't get monthly API credits.
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *part-of* `g07-0203`
  ↳ *contrast* `g07-0189` — credits skip Pro; Projects is Pro and Max only
  ↳ *evidence-for* `g04-0129`

- `g07-0215` *STATED* — Claiming the monthly API credits takes about two minutes.
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *part-of* `g07-0203`

- `g07-0300` *INFERRED* — Haiku 5.5's 10x price cut and 1M context make Alex's routing rule (Opus plans and debugs, Haiku does lookups and one-line edits) cheaper on the API and lighter on plan limits.
  — [g-make-claude-code-limit-last-longer-haiku-5-5-helper](https://chen.media/guides/make-claude-code-limit-last-longer-haiku-5-5-helper) [g-set-up-claude-haiku-5-5-10x-cheaper-claude-model](https://chen.media/guides/set-up-claude-haiku-5-5-10x-cheaper-claude-model)
  ↳ *generalizes* `g07-0108`
  ↳ *generalizes* `g07-0221`

- `g09-0051` *STATED* — Jarvis needs no API key and runs up no cloud bill.
  > “No API key, no cloud bill.”
  — [g-run-a-jarvis-on-your-own-claude-code](https://chen.media/guides/run-a-jarvis-on-your-own-claude-code)
  ↳ *qualifies* `g09-0050`
  ↳ *because* `g09-0052`

- `g09-0052` *STATED* — Jarvis runs on your existing Claude Code subscription; its repo says that is the only subscription you need.
  > “The repo says it's the only subscription you need: no API keys and no cloud bill.”
  — [g-run-a-jarvis-on-your-own-claude-code](https://chen.media/guides/run-a-jarvis-on-your-own-claude-code)
  ↳ *example-of* `g05-0314`

- `g09-0061` *INFERRED* — Because Jarvis drives your local Claude Code rather than the Anthropic API, its usage counts against your subscription's usage limits instead of per-token billing.
  — [g-run-a-jarvis-on-your-own-claude-code](https://chen.media/guides/run-a-jarvis-on-your-own-claude-code)
  ↳ *qualifies* `g09-0052`
  ↳ *generalizes* `g09-0201` — third-party tools powered by your Claude plan draw from the same limit

- `g09-0086` *STATED* — Do the model's math faster on the same hardware and every answer costs less to serve.
  > “Do that math faster on the same hardware, and every answer costs less to serve.”
  — [g-deepgemm-free-engine-deepseek-runs-its-ai-on](https://chen.media/guides/deepgemm-free-engine-deepseek-runs-its-ai-on)
  ↳ *because* `g09-0085`
  ↳ *generalizes* `g09-0083`

- `g09-0095` *STATED* — DeepGEMM guide section 'No GPUs? Here's what it means for you': even without GPUs, DeepGEMM matters through your AI bill.
  — [g-deepgemm-free-engine-deepseek-runs-its-ai-on](https://chen.media/guides/deepgemm-free-engine-deepseek-runs-its-ai-on)
  ↳ *depends-on* `g09-0084`

- `g09-0131` *STATED* — Every skill you install leaves a short note in Claude's context on every single message, even the skills you never use.
  > “Every skill you install leaves a short note in Claude's context on every single message, even the ones you never use.”
  — [g-find-the-claude-skills-eating-your-limit-skill-doctor](https://chen.media/guides/find-the-claude-skills-eating-your-limit-skill-doctor)
  ↳ *because* `g09-0134`
  ↳ *qualifies* `g09-0036` — LESSONS.md imported into CLAUDE.md also rides in context every session
  ↳ *evidence-for* `y02-0125`

- `g09-0132` *STATED* — Claude Code's hidden /skill-doctor command shows what each skill costs and which ones never get used, so you can turn the dead weight off.
  — [g-find-the-claude-skills-eating-your-limit-skill-doctor](https://chen.media/guides/find-the-claude-skills-eating-your-limit-skill-doctor)
  ↳ *part-of* `g09-0130`
  ↳ *because* `g09-0131`
  ↳ *defines* `y02-0127`

- `g09-0137` *STATED* — /skill-doctor shows what each of your skills costs to keep in context.
  — [g-find-the-claude-skills-eating-your-limit-skill-doctor](https://chen.media/guides/find-the-claude-skills-eating-your-limit-skill-doctor)
  ↳ *part-of* `g09-0132`

- `g09-0138` *STATED* — /skill-doctor shows how often each skill actually gets used.
  — [g-find-the-claude-skills-eating-your-limit-skill-doctor](https://chen.media/guides/find-the-claude-skills-eating-your-limit-skill-doctor)
  ↳ *part-of* `g09-0132`
  ↳ *evidence-for* `y02-0128`

- `g09-0139` *STATED* — /skill-doctor flags skills that have never been used at all, with where to turn each one off.
  — [g-find-the-claude-skills-eating-your-limit-skill-doctor](https://chen.media/guides/find-the-claude-skills-eating-your-limit-skill-doctor)
  ↳ *part-of* `g09-0132`
  ↳ *leads-to* `g09-0142`

- `g09-0140` *STATED* — /skill-doctor also lists plugins you haven't used recently.
  — [g-find-the-claude-skills-eating-your-limit-skill-doctor](https://chen.media/guides/find-the-claude-skills-eating-your-limit-skill-doctor)
  ↳ *part-of* `g09-0132`

- `g09-0144` *INFERRED* — Because unused-skill notes are resent on every message, pruning them saves tokens on every turn of every session, which compounds into a longer-lasting limit.
  — [g-find-the-claude-skills-eating-your-limit-skill-doctor](https://chen.media/guides/find-the-claude-skills-eating-your-limit-skill-doctor)
  ↳ *generalizes* `g09-0131`

- `g09-0210` *INFERRED* — Because Claude plays every simulated person, a MiroFish run's usage scales with crowd size and rounds, which is why running small first protects your limit.
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)
  ↳ *generalizes* `g09-0144` — both are levers on how fast you burn the Claude limit
  ↳ *example-of* `g13-0305`

- `g10-0197` *CORE* — Higher effort spends more of your Claude usage.
  > “Higher effort spends more of your usage.”
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *evidence-for* `g10-0183`
  ↳ *part-of* `g10-0269`

- `g10-0199` *CORE* — Claude Design draws from the same usage limit as Claude Code, and a full deck uses more of it than a typical message.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *because* `g10-0198`
  ↳ *evidence-for* `g10-0269`

- `g10-0200` *STATED* — Claude's own page for Claude Design says: "Larger requests, like a full deck or design, use more of your limit than a typical message."
  > “Larger requests, like a full deck or design, use more of your limit than a typical message.”
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *evidence-for* `g10-0199`

- `g10-0238` *STATED* — Dyad uses your own AI key, Claude's included, so there's no credit meter: you pay the AI provider only for what you actually use, or nothing at all on a free tier.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *because* `g10-0224`
  ↳ *example-of* `g17-0313`

- `g10-0269` *INFERRED* — Alex frames Claude features by how much of the shared usage limit they burn: effort level (low ~73k vs max ~222k tokens on hard tasks) and Claude Design (a full deck costs more than a typical message, from the same pool as Claude Code).
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet) [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)

- `g11-0025` *STATED* — Because Instatic runs on your own key there is no credit plan to run out of; you pay Anthropic only for what you use.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *because* `g11-0024`
  ↳ *example-of* `g17-0313`

- `g11-0094` *STATED* — Anthropic says Sonnet 5.5 is 30% faster than Sonnet 5.
  — [g-turn-any-photo-into-a-painting-claude-draws-with-code](https://chen.media/guides/turn-any-photo-into-a-painting-claude-draws-with-code)
  ↳ *evidence-for* `g11-0096`

- `g11-0095` *STATED* — Anthropic says Sonnet 5.5 costs up to 30% less than Sonnet 5 for most work because it needs fewer tokens for the same job.
  — [g-turn-any-photo-into-a-painting-claude-draws-with-code](https://chen.media/guides/turn-any-photo-into-a-painting-claude-draws-with-code)
  ↳ *evidence-for* `g11-0096`

- `g11-0100` *STATED* — Running Fable 5.1 as the /advisor costs less than running Fable all the time.
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)
  ↳ *evidence-for* `g11-0102`

- `g11-0101` *STATED* — If you run Claude Code on Opus 5.5 and have Fable 5.1, Fable is probably sitting there doing nothing: you either pay for it on every turn or don't use it at all.
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)
  ↳ *because* `g11-0102`

- `g11-0131` *STATED* — Claude Code and Codex already have a cheaper speed-up you may not be using: fast mode.
  — [g-is-openais-500-ultrafast-plan-worth-it](https://chen.media/guides/is-openais-500-ultrafast-plan-worth-it)
  ↳ *evidence-for* `g11-0121`
  ↳ *contrast* `g11-0111` — Claude Code levers: fast mode for speed, advisor for quality
  ↳ *qualifies* `y01-0019`

- `g12-0003` *STATED* — Picking Sonnet 5.5 or Opus 5.5 per task is how Alex frames getting work done well while making the Claude usage limit last.
  > “Here is when to use each one, so the work gets done well and your usage limit lasts.”
  — [g-claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task](https://chen.media/guides/claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task)
  ↳ *part-of* `g12-0001`

- `g12-0017` *INFERRED* — Sonnet 5.5 kept Sonnet 5's $2 / $10 per 1M token price, so its jump from 10.3% to 70.6% on Terminal-Bench 4.0 came with no price increase.
  — [g-claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task](https://chen.media/guides/claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task)
  ↳ *depends-on* `g12-0016`
  ↳ *depends-on* `g12-0005`

- `g12-0019` *STATED* — Read the Sonnet 5.5 vs Opus 5.5 table as two groups: on everyday work (command-line coding, knowledge work, using a computer) Sonnet 5.5 matches or beats Opus.
  — [g-claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task](https://chen.media/guides/claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task)
  ↳ *contrast* `g12-0020`
  ↳ *evidence-for* `y01-0138`

- `g12-0020` *STATED* — On the hardest problems (FrontierCode, Humanity's Last Exam) Opus 5.5 keeps a clear lead over Sonnet 5.5.
  — [g-claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task](https://chen.media/guides/claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task)

- `g12-0021` *STATED* — Anthropic's own advice: Sonnet 5.5 is strongest at well-scoped everyday tasks, fixing bugs, and making polished documents, slides and spreadsheets.
  — [g-claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task](https://chen.media/guides/claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task)
  ↳ *evidence-for* `g12-0019`
  ↳ *contrast* `g12-0022`

- `g12-0022` *STATED* — Anthropic's own advice: Opus 5.5 is built for complex work that needs careful judgment.
  — [g-claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task](https://chen.media/guides/claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task)
  ↳ *evidence-for* `g12-0020`

- `g12-0095` *STATED* — Given legacy instructions, Opus 5.5 does the extra checks, over-applies the shouted rules and over-plans, and you pay for every token of it.
  — [g-clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit](https://chen.media/guides/clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit)
  ↳ *because* `g12-0094`

- `g12-0103` *STATED* — A 'check your work twice' line buys a second pass of tool calls and reasoning you did not need.
  — [g-clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit](https://chen.media/guides/clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit)
  ↳ *example-of* `g12-0101`
  ↳ *leads-to* `g12-0105`
  ↳ *contrast* `g12-0202` — a blanket 'check twice' line wastes tokens; a structured verification loop that runs real checks is what Anthropic recommends

- `g12-0105` *STATED* — Cost dropped in Anthropic's test because the extra tool calls and duplicated reasoning that the old instructions triggered went away.
  — [g-clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit](https://chen.media/guides/clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit)
  ↳ *evidence-for* `g12-0122` — extra tool calls re-send the conversation

- `g12-0118` *STATED* — The re-reading part of Claude's cost can be cut, whether you pay per token or are on a plan with usage limits.
  — [g-what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything)
  ↳ *qualifies* `g12-0117`

- `g12-0119` *STATED* — Anthropic's Claude Code docs say Claude Code sends your full conversation with every request, so a one-line question in a session open all day is charged for the whole conversation.
  — [g-what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything)
  ↳ *evidence-for* `g19-0017`

- `g12-0121` *STATED* — Every time you send a message, Claude Code sends the entire chat so far: your messages, Claude's replies, every file it opened and every command output.
  — [g-what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything)
  ↳ *part-of* `g12-0119`
  ↳ *evidence-for* `g19-0017`

- `g12-0122` *STATED* — Each tool Claude uses sends the whole conversation again with the new result on top.
  — [g-what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything)
  ↳ *qualifies* `g12-0121`

- `g12-0124` *STATED* — Re-reading outweighs writing because the writing happens once while the re-reading happens on every turn, and each turn carries everything that came before it.
  — [g-what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything)
  ↳ *because* `g12-0121`
  ↳ *because* `y03-0023`

- `g12-0174` *STATED* — Long Claude Code sessions get compacted, and Claude often seems dumber afterwards.
  — [g-stop-claude-code-s-compact-from-summarizing-away-your-chat](https://chen.media/guides/stop-claude-code-s-compact-from-summarizing-away-your-chat)
  ↳ *part-of* `g12-0171`
  ↳ *because* `g12-0176`

- `g12-0177` *STATED* — The lossy /compact summary is what causes the 'it got dumb after compacting' feeling.
  > “That's the "it got dumb after compacting" feeling.”
  — [g-stop-claude-code-s-compact-from-summarizing-away-your-chat](https://chen.media/guides/stop-claude-code-s-compact-from-summarizing-away-your-chat)

- `g12-0183` *INFERRED* — Fast-Jev Compaction targets what Alex's cost analysis blames: opened files and command outputs re-sent every turn, so dropping stale tool output shrinks re-reading without losing the conversation.
  — [g-stop-claude-code-s-compact-from-summarizing-away-your-chat](https://chen.media/guides/stop-claude-code-s-compact-from-summarizing-away-your-chat)
  ↳ *depends-on* `g12-0121`
  ↳ *depends-on* `g12-0178`
  ↳ *enables* `g12-0118`

- `g12-0239` *STATED* — One command keeps Claude Code working at lower priority instead of stopping when you hit your usage limit.
  — [g-keep-using-claude-code-after-you-hit-your-usage-limit](https://chen.media/guides/keep-using-claude-code-after-you-hit-your-usage-limit)
  ↳ *part-of* `g12-0238`
  ↳ *defines* `g12-0241`

- `g12-0240` *STATED* — Normally when you hit your usage limit Claude Code stops and you wait for the reset, often hours, even if you were one prompt away from finishing.
  — [g-keep-using-claude-code-after-you-hit-your-usage-limit](https://chen.media/guides/keep-using-claude-code-after-you-hit-your-usage-limit)
  ↳ *contrast* `g12-0241`

- `g12-0241` *STATED* — With Claude Code's lower-priority mode turned on, Claude keeps working on your session instead of stopping at the limit.
  — [g-keep-using-claude-code-after-you-hit-your-usage-limit](https://chen.media/guides/keep-using-claude-code-after-you-hit-your-usage-limit)
  ↳ *part-of* `g12-0238`
  ↳ *contrast* `g03-0166` — lower-priority mode keeps working at the limit (still counts toward weekly limit); auto-continue waits for the reset then resumes

- `g12-0242` *STATED* — In lower-priority mode your requests go to the back of the line and run when Anthropic has spare capacity, so it can be slower, but you are not locked out until the reset.
  — [g-keep-using-claude-code-after-you-hit-your-usage-limit](https://chen.media/guides/keep-using-claude-code-after-you-hit-your-usage-limit)
  ↳ *qualifies* `g12-0241`

- `g13-0098` *CORE* — If you hit your Claude usage limit locally, a cloud session keeps going on the cloud credit until the credit runs out.
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it) [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)
  ↳ *because* `g13-0113`
  ↳ *qualifies* `g13-0096`
  ↳ *contrast* `g13-0179` — two ways to stretch Claude usage: cloud credit vs routing small calls elsewhere

- `g13-0099` *STATED* — To get people trying cloud sessions, Anthropic gives existing Pro and Max subscribers a one-time credit with a deadline.
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it)
  ↳ *leads-to* `g13-0093`

- `g13-0113` *CORE* — The Claude Code cloud session credit sits on top of your plan and outside your usage limits.
  > “The best part: the credit sits on top of your plan and outside your usage limits.”
  — [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)

- `g13-0170` *STATED* — Jev does not write text; it answers narrow questions about a situation you describe.
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *part-of* `g13-0169`

- `g13-0174` *STATED* — Every Jev answer comes back with a confidence number your code can check.
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *part-of* `g13-0169`

- `g13-0176` *STATED* — Most of the calls inside a Claude Code workflow are small.
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *because* `g13-0179`

- `g13-0236` *STATED* — Alex presents the Darwin Loop as a bounded way to improve a draft without letting usage run away.
  — [g-darwin-loop-evolve-the-winner](https://chen.media/guides/darwin-loop-evolve-the-winner)
  ↳ *qualifies* `g13-0222`

- `g14-0149` *STATED* — AWS includes a Bedrock playground activity among its documented credit-earning options.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *part-of* `g14-0148`

- `g15-0014` *CORE* — Every file you hand an AI model gets read in full: not just the words you care about but the layout, tables, image data, headers and footers, and the invisible structure holding the page together.
  — [g-why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix](https://chen.media/guides/why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix)
  ↳ *because* `g15-0013`
  ↳ *leads-to* `g15-0015`
  ↳ *because* `g15-0180`

- `g15-0015` *CORE* — You pay for an uploaded file's full token cost again on every message for as long as that file stays in the conversation.
  > “You pay for all of it, on every message that file stays in the conversation.”
  — [g-why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix](https://chen.media/guides/why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix)
  ↳ *qualifies* `g15-0013`

- `g15-0070` *STATED* — With OmniRoute you never stop working because Claude ran out.
  — [g-four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute](https://chen.media/guides/four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute)
  ↳ *evidence-for* `g16-0284`

- `g15-0086` *STATED* — Munder Difflin uses the CLI subscription you already have rather than metered API keys.
  — [g-munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents](https://chen.media/guides/munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents)
  ↳ *qualifies* `g15-0079`
  ↳ *example-of* `g05-0314`

- `g15-0144` *STATED* — You are probably paying several AI companies for the same job.
  — [g-every-premium-ai-model-in-one-place-how-the-one-tab-route-actually-works](https://chen.media/guides/every-premium-ai-model-in-one-place-how-the-one-tab-route-actually-works)
  ↳ *leads-to* `g15-0146`

- `g15-0145` *STATED* — Chat, images and reasoning are three different bills in most setups, and each renews on its own date, which is what quietly makes it expensive.
  — [g-every-premium-ai-model-in-one-place-how-the-one-tab-route-actually-works](https://chen.media/guides/every-premium-ai-model-in-one-place-how-the-one-tab-route-actually-works)
  ↳ *evidence-for* `g15-0144`

- `g16-0040` *STATED* — Almost every "save tokens in Claude Code" post is the same trick told again: use a cheaper model, write shorter prompts, clear your context.
  > “Almost every "save tokens in Claude Code" post is the same trick told again.”
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you)

- `g16-0043` *STATED* — You can attack all three Claude Code cost levers at once because the tools that do it do not overlap.
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you)
  ↳ *enables* `g16-0054`

- `g16-0052` *STATED* — The cache clock is the actual point of the three-repos guide.
  > “The cache clock, which is the actual point of this guide”
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you)
  ↳ *qualifies* `g16-0046`

- `g16-0083` *STATED* — Everything you paste competes with everything else you paste, so the thing you actually needed becomes one item in a pile.
  > “the thing you actually needed is one item in a pile”
  — [g-the-one-page-that-points-claude-at-the-right-notes](https://chen.media/guides/the-one-page-that-points-claude-at-the-right-notes)

- `g16-0096` *STATED* — He compares the local build against what the same work costs to rent.
  > “What the same work costs to rent”
  — [g-what-it-really-costs-to-run-ai-locally](https://chen.media/guides/what-it-really-costs-to-run-ai-locally)
  ↳ *contrast* `g16-0086`
  ↳ *qualifies* `g16-0240`

- `g16-0100` *STATED* — Almost every "Claude is worse today" post is a context problem wearing a capability costume.
  > “Almost every "Claude is worse today" post is a context problem wearing a capability costume.”
  — [g-15-claude-mistakes-that-are-quietly-costing-you-tokens](https://chen.media/guides/15-claude-mistakes-that-are-quietly-costing-you-tokens)
  ↳ *generalizes* `g16-0099`
  ↳ *evidence-for* `g16-0009`

- `g16-0101` *STATED* — The context window is finite.
  > “The window is finite”
  — [g-15-claude-mistakes-that-are-quietly-costing-you-tokens](https://chen.media/guides/15-claude-mistakes-that-are-quietly-costing-you-tokens)
  ↳ *evidence-for* `g16-0100`

- `g16-0102` *STATED* — Most of what fills Claude's context window was never typed by you.
  > “most of what fills it was never typed by you”
  — [g-15-claude-mistakes-that-are-quietly-costing-you-tokens](https://chen.media/guides/15-claude-mistakes-that-are-quietly-costing-you-tokens)
  ↳ *evidence-for* `g16-0100`
  ↳ *evidence-for* `g17-0115`

- `g16-0106` *STATED* — Mistakes 1, 2 and 3 are the three in the video; the other twelve only show up once a session gets long or a workspace gets crowded.
  — [g-15-claude-mistakes-that-are-quietly-costing-you-tokens](https://chen.media/guides/15-claude-mistakes-that-are-quietly-costing-you-tokens)
  ↳ *qualifies* `g16-0099`
  ↳ *qualifies* `g16-0108`
  ↳ *qualifies* `g16-0109`
  ↳ *qualifies* `g16-0110`
  ↳ *example-of* `g16-0004`

- `g16-0124` *STATED* — An anonymous coding model, ox-alpha, made Claude Code free until August 27 (2026) when Claude Code is pointed at it.
  > “The Anonymous Model That Makes Claude Code Free Until August 27”
  — [g-the-anonymous-model-that-makes-claude-code-free-until-august-27](https://chen.media/guides/the-anonymous-model-that-makes-claude-code-free-until-august-27)
  ↳ *example-of* `g16-0001`
  ↳ *example-of* `g16-0008`

- `g16-0278` *STATED* — Re-prompting carries a cost you are not counting.
  > “The cost you are not counting”
  — [g-the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting](https://chen.media/guides/the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting)
  ↳ *evidence-for* `g19-0012`

- `g16-0301` *STATED* — Ruflo adds a router that decides which model each piece of work is worth.
  > “a router that decides which model each piece of work is worth”
  — [g-ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm](https://chen.media/guides/ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm)
  ↳ *part-of* `g16-0297`
  ↳ *example-of* `g16-0013`
  ↳ *example-of* `y02-0187`

- `g16-0312` *STATED* — None of the seven repos needs an API key beyond the Claude subscription you already have.
  > “Nothing here needs an API key beyond the Claude subscription you already have”
  — [g-seven-free-claude-code-repos-that-fix-what-claude-gets-wrong](https://chen.media/guides/seven-free-claude-code-repos-that-fix-what-claude-gets-wrong)
  ↳ *qualifies* `g16-0305`
  ↳ *contrast* `g16-0047` — seven repos need only the Claude subscription; deepclaude changes who you buy tokens from
  ↳ *contrast* `g16-0125`
  ↳ *example-of* `g05-0314`

- `g17-0113` *STATED* — You can cut what your coding agent sends to the model without changing a line of your code.
  > “without changing a line of your code”
  — [g-cut-what-your-coding-agent-sends-to-the-model](https://chen.media/guides/cut-what-your-coding-agent-sends-to-the-model)

- `g17-0114` *CORE* — A coding agent's token bill is mostly repetition.
  > “Why your token bill is mostly repetition”
  — [g-cut-what-your-coding-agent-sends-to-the-model](https://chen.media/guides/cut-what-your-coding-agent-sends-to-the-model)
  ↳ *because* `g17-0115`

- `g17-0116` *STATED* — A coding agent's prompt prefix (tool schemas, conversation, files read) is rebuilt and re-sent on every single turn.
  > “That prefix is rebuilt and re-sent on every single turn”
  — [g-cut-what-your-coding-agent-sends-to-the-model](https://chen.media/guides/cut-what-your-coding-agent-sends-to-the-model)
  ↳ *qualifies* `g17-0115`
  ↳ *evidence-for* `g19-0017`

- `g17-0118` *STATED* — Because the prefix is re-sent every turn, a coding agent's bill grows faster than the work does.
  > “This is why the bill grows faster than the work does.”
  — [g-cut-what-your-coding-agent-sends-to-the-model](https://chen.media/guides/cut-what-your-coding-agent-sends-to-the-model)
  ↳ *because* `g17-0116`

- `g17-0141` *STATED* — Every serious AI lab now hands out a free tier: a few million tokens a month here, a few thousand requests a day there.
  > “A few million tokens a month here, a few thousand requests a day there.”
  — [g-pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint](https://chen.media/guides/pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint)
  ↳ *leads-to* `g17-0142`

- `g17-0150` *STATED* — Pooling the free tiers of 29 AI providers behind one endpoint is pitched as the way to never hit a rate limit again.
  > “and never hit a rate limit again”
  — [g-pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint](https://chen.media/guides/pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint)

- `g18-0053` *STATED* — Claude Code re-reads your repository every session.
  — [g-stop-claude-code-re-reading-your-repo-every-session](https://chen.media/guides/stop-claude-code-re-reading-your-repo-every-session)
  ↳ *leads-to* `g18-0054`
  ↳ *example-of* `g18-0181` — repo context is rebuilt from scratch each session
  ↳ *evidence-for* `g02-0180`

- `g18-0103` *STATED* — Claude loads a skill only when its description matches what you are doing, so a skill costs nothing until it is useful.
  — [g-one-command-installs-anthropic-s-own-skill-library](https://chen.media/guides/one-command-installs-anthropic-s-own-skill-library)
  ↳ *contrast* `g18-0104`
  ↳ *contradicts* `g18-0250` — skills 'cost nothing until useful' vs unused skills are 'context you pay for on every request'
  ↳ *contrast* `g18-0113` — skills load on match; MCP tools describe themselves up front
  ↳ *contradicts* `g09-0131` — "a skill costs nothing until it is useful" vs "every skill you install leaves a short note in context on every single message"

- `g18-0104` *STATED* — Skills differ from a giant system prompt, which you pay for on every single message.
  > “That is the difference between this and a giant system prompt that you pay for on every single message.”
  — [g-one-command-installs-anthropic-s-own-skill-library](https://chen.media/guides/one-command-installs-anthropic-s-own-skill-library)
  ↳ *example-of* `g18-0283`
  ↳ *evidence-for* `g03-0025`

- `g18-0113` *CORE* — Every MCP server you add spends context describing its own tools before you have asked a single question.
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again)
  ↳ *example-of* `g18-0283`

- `g18-0176` *STATED* — The video-watching skill runs everything on your own machine, and the decoding costs nothing.
  — [g-the-skill-that-makes-claude-watch-a-video-not-read-about-it](https://chen.media/guides/the-skill-that-makes-claude-watch-a-video-not-read-about-it)
  ↳ *qualifies* `g18-0174`

- `g18-0181` *CORE* — Claude starts every conversation from zero; that is not a bug, it is how the context window works.
  — [g-give-claude-a-memory-that-survives-the-chat-window](https://chen.media/guides/give-claude-a-memory-that-survives-the-chat-window)
  ↳ *leads-to* `g18-0182`

- `g18-0182` *STATED* — Because Claude starts from zero you keep re-pasting the same background before you can ask the real question, and you pay for those tokens every single time.
  — [g-give-claude-a-memory-that-survives-the-chat-window](https://chen.media/guides/give-claude-a-memory-that-survives-the-chat-window)
  ↳ *leads-to* `g18-0183`
  ↳ *example-of* `g18-0283`
  ↳ *contrast* `g18-0085` — re-pasting background vs installing a skill once

- `g18-0221` *STATED* — Every API in Alex's free-LLM guide is on a permanent free tier, not a trial with credits that run out.
  — [g-134-free-llm-apis-and-how-to-point-your-editor-at-them](https://chen.media/guides/134-free-llm-apis-and-how-to-point-your-editor-at-them)
  ↳ *qualifies* `g18-0126` — permanent free tiers, still rate-limited
  ↳ *qualifies* `g18-0220`

- `g18-0244` *STATED* — Outdated instructions are not helping anymore: they sit in your context window, getting in the way, and you are the one still carrying them.
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *example-of* `g18-0283`
  ↳ *evidence-for* `g12-0095`

- `g19-0016` *CORE* — Claude usage limits are almost never a plan problem; they are a context problem.
  > “Usage limits are almost never a plan problem. They are a context problem.”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *evidence-for* `g16-0100`

- `g19-0017` *CORE* — Claude re-reads your entire conversation on every single message: the whole thing, not a summary of it.
  > “Claude re-reads your entire conversation on every single message. Not a summary of it, the whole thing.”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *because* `g19-0016`
  ↳ *evidence-for* `y03-0025`

- `g19-0019` *STATED* — The cost of a Claude message is set by how much conversation you are dragging behind you, not by how hard the question is.
  > “The cost of a message is set by how much you are dragging behind you, not by how hard the question is.”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *leads-to* `g19-0017`

- `g19-0021` *INFERRED* — Because every reply re-pays the whole carried history, trimming context with /compact or a fresh session cuts the price of every later message, not just the current one.
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *depends-on* `g19-0019`
  ↳ *qualifies* `g19-0003`

- `g19-0092` *STATED* — With /route, Claude as boss and Gemini as builder lets you ship far more while spending a fraction of your Claude usage.
  > “so you ship far more while spending a fraction of your Claude usage”
  — [g-run-gemini-inside-claude-code-with-claude-as-the-boss](https://chen.media/guides/run-gemini-inside-claude-code-with-claude-as-the-boss)
  ↳ *part-of* `g19-0091`
  ↳ *example-of* `y02-0187`

- `g19-0140` *STATED* — A Claude Code agent makes a hundred little decisions and burns your tokens, and you get to see almost none of it.
  > “your Claude Code agent runs, makes a hundred little decisions, and burns your tokens, and you get to see almost none of it”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *because* `g19-0139`
  ↳ *qualifies* `g19-0017`

- `g19-0142` *STATED* — The Langfuse timeline shows exactly what the agent did, how long each step took, and what each step cost, down to the fraction of a cent.
  > “what each one cost you, down to the fraction of a cent”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *part-of* `g19-0141`
  ↳ *contrast* `g19-0010` — per-call cost trace vs session total from /cost

- `g19-0161` *STATED* — Install Claude Code Router first because it cuts your bill immediately.
  > “Router first, because it cuts your bill immediately.”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *part-of* `g19-0160`

- `g19-0165` *STATED* — With Claude Code Router, easy work goes to a cheaper model while hard work still goes to the expensive one.
  > “The easy work goes to a cheaper model, the hard work still goes to the expensive one”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *part-of* `g19-0164`
  ↳ *because* `g19-0167`
  ↳ *example-of* `y02-0187`

- `g19-0166` *STATED* — Claude Code Router does not change how you work.
  > “you do not change how you work”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *qualifies* `g19-0164`

- `g19-0167` *STATED* — Of the four repos, Claude Code Router is the one that shows up on your bill first.
  > “This is the one that shows up on your bill first.”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *evidence-for* `g19-0161`

- `g19-0170` *STATED* — In Claude Code Router you configure providers and routing rules in the UI, so there is no config file to hand-write on day one.
  > “there is no config file to hand write on day one”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *qualifies* `g19-0169`

- `g19-0177` *STATED* — Claude Code reads whole files to change one function, and you pay for every line it did not need.
  > “Claude Code reads whole files to change one function, and you pay for every line it did not need.”
  — [g-give-claude-code-an-ide-brain-so-it-stops-reading-everything](https://chen.media/guides/give-claude-code-an-ide-brain-so-it-stops-reading-everything)
  ↳ *part-of* `g19-0176`
  ↳ *because* `g19-0178`
  ↳ *example-of* `g19-0020` — file reads are dragged context
  ↳ *evidence-for* `g03-0120`

- `g19-0185` *STATED* — Serena sends the 20 lines you need plus the call sites.
  > “Serena sends the 20 plus the call sites.”
  — [g-give-claude-code-an-ide-brain-so-it-stops-reading-everything](https://chen.media/guides/give-claude-code-an-ide-brain-so-it-stops-reading-everything)
  ↳ *contrast* `g19-0184`
  ↳ *depends-on* `g19-0182` — find_referencing_symbols supplies call sites
  ↳ *contrast* `g03-0121`

- `g19-0187` *STATED* — Serena's savings scale with file size, so the bigger and messier the repo, the bigger the win.
  > “the bigger and messier the repo, the bigger the win”
  — [g-give-claude-code-an-ide-brain-so-it-stops-reading-everything](https://chen.media/guides/give-claude-code-an-ide-brain-so-it-stops-reading-everything)
  ↳ *generalizes* `g19-0184`

- `g19-0189` *STATED* — Without Serena context fills up and quality drops late in a session; with Serena context stays lean for longer sessions.
  > “Context fills up, quality drops late in a session / Context stays lean for longer sessions”
  — [g-give-claude-code-an-ide-brain-so-it-stops-reading-everything](https://chen.media/guides/give-claude-code-an-ide-brain-so-it-stops-reading-everything)
  ↳ *because* `g19-0185`
  ↳ *evidence-for* `g19-0016` — lean context = longer sessions

- `g20-0050` *STATED* — Claude connectors work on the Free plan, but Free is limited to one custom connector.
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *part-of* `g20-0034`

- `g20-0081` *STATED* — The carousel system works on the Claude free plan: Projects, project instructions, artifacts and code execution are all available on Free.
  — [g-the-one-prompt-that-makes-claude-design-real-carousels](https://chen.media/guides/the-one-prompt-that-makes-claude-design-real-carousels)
  ↳ *part-of* `g20-0070`

- `g20-0146` *STATED* — Re-explaining context costs you twice: once in your own time, and once in the tokens Claude burns re-reading the same context.
  > “You pay for that twice: once in your own time, and once in the tokens it burns re-reading the same context.”
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *evidence-for* `g20-0237`
  ↳ *evidence-for* `g18-0182`

- `g20-0210` *CORE* — The plan sets the ceiling, so spend your best model on the Planner.
  > “The plan sets the ceiling, so spend your best model here.”
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *because* `g20-0209`
  ↳ *contrast* `g20-0211` — smartest vs cheaper model
  ↳ *example-of* `g21-0158`

- `g20-0290` *STATED* — Claude Free plan limits named across Alex's guides: one custom connector, 5 projects, and usage that resets on a rolling 5-hour window.
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup) [g-the-one-prompt-that-makes-claude-design-real-carousels](https://chen.media/guides/the-one-prompt-that-makes-claude-design-real-carousels)
  ↳ *generalizes* `g20-0050`
  ↳ *generalizes* `g20-0082`
  ↳ *generalizes* `g20-0083`

- `g21-0120` *CORE* — Fable 5's real edge is not typing your work but turning a vague backlog into specs so exact that a cheap model (Sonnet or Haiku) can build them later without a single judgment call.
  — [g-turn-your-whole-backlog-into-finished-plans-in-one-night](https://chen.media/guides/turn-your-whole-backlog-into-finished-plans-in-one-night)
  ↳ *leads-to* `g21-0121`

- `g22-0005` *STATED* — After the free Fable 5 window closes, every cheap model you run reads the JUDGMENT.md vault first and makes calls at your level for pennies.
  — [g-bank-the-judgment-calls-not-just-the-output](https://chen.media/guides/bank-the-judgment-calls-not-just-the-output)

- `g22-0010` *STATED* — Back-solving judgment from past decisions is flagship work, not cheap-model work.
  > “Back-solving judgment is flagship work.”
  — [g-bank-the-judgment-calls-not-just-the-output](https://chen.media/guides/bank-the-judgment-calls-not-just-the-output)
  ↳ *because* `g22-0018`
  ↳ *because* `g22-0012`

- `g22-0011` *STATED* — A cheap model cannot look at twenty of your decisions and find the three rules hiding behind them; only the top model can.
  — [g-bank-the-judgment-calls-not-just-the-output](https://chen.media/guides/bank-the-judgment-calls-not-just-the-output)
  ↳ *evidence-for* `g22-0010`

- `g22-0016` *STATED* — Judgment Vault rule of thumb: the flagship builds the vault, the cheap models spend from it.
  > “The flagship builds the vault, the cheap models spend from it.”
  — [g-bank-the-judgment-calls-not-just-the-output](https://chen.media/guides/bank-the-judgment-calls-not-just-the-output)
  ↳ *generalizes* `g22-0005`
  ↳ *example-of* `g22-0282`
  ↳ *analogy-for* `g22-0056` — flagship builds once, cheap tiers do volume
  ↳ *example-of* `g21-0158`

- `g22-0018` *STATED* — The Bank the Judgment Calls guide's opening part, 'Why This, Why Now', is subtitled 'The timing is the whole trick': the workflow pays because the flagship is temporarily free.
  — [g-bank-the-judgment-calls-not-just-the-output](https://chen.media/guides/bank-the-judgment-calls-not-just-the-output)
  ↳ *part-of* `g22-0001`

- `g22-0046` *STATED* — GPT-5.6 Sol is the flagship, and it is priced like one.
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)
  ↳ *because* `g22-0045`

- `g22-0056` *STATED* — The whole model-line trick is using each tier for the job it is priced for: the senior thinks, the juniors do the reps.
  > “the senior thinks, the juniors do the reps”
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)
  ↳ *generalizes* `g22-0048`
  ↳ *example-of* `g21-0158`

- `g22-0282` *CORE* — Spend the best model where it sets the ceiling (the Judgment Vault back-solve, the master spec and QA, the brand brief) and let cheaper models do the volume.
  — [g-bank-the-judgment-calls-not-just-the-output](https://chen.media/guides/bank-the-judgment-calls-not-just-the-output) [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model) [g-turn-claude-into-a-full-brand-studio-free](https://chen.media/guides/turn-claude-into-a-full-brand-studio-free)
  ↳ *evidence-for* `g21-0158`

- `g23-0013` *STATED* — The instructions file Fable 5 writes lets Opus pick up where Fable left off.
  > “the instructions file that lets Opus pick up where Fable left off”
  — [g-clone-the-smart-model-s-brain-into-the-cheap-one](https://chen.media/guides/clone-the-smart-model-s-brain-into-the-cheap-one)

- `g23-0014` *STATED* — Fable 5 had a free window that closes, after which it goes pay per token.
  — [g-clone-the-smart-model-s-brain-into-the-cheap-one](https://chen.media/guides/clone-the-smart-model-s-brain-into-the-cheap-one)
  ↳ *evidence-for* `g22-0002`

- `g23-0017` *STATED* — Files survive the deadline; the model's context does not.
  > “Files survive the deadline; the model's context does not.”
  — [g-clone-the-smart-model-s-brain-into-the-cheap-one](https://chen.media/guides/clone-the-smart-model-s-brain-into-the-cheap-one)
  ↳ *because* `g22-0012`

- `g23-0023` *STATED* — The audit's ranked list of repeated work is the raw material for every later step of the clone (skill files and instructions file).
  > “That list is the raw material for everything below.”
  — [g-clone-the-smart-model-s-brain-into-the-cheap-one](https://chen.media/guides/clone-the-smart-model-s-brain-into-the-cheap-one)
  ↳ *qualifies* `g23-0022`

- `r03-0042` *STATED* — On a quiet day with no corrections, the nightly /learn review stops after one command.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *qualifies* `r03-0041`
  ↳ *because* `r03-0081`

- `r04-0098` *STATED* — Claude Code routines need a Claude Pro, Max, Team or Enterprise plan; they run on it and count toward its usage.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *evidence-for* `r04-0016`
  ↳ *depends-on* `r04-0089`

- `r04-0161` *STATED* — Each routine run uses the user's plan usage like a normal session.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *evidence-for* `r04-0016`
  ↳ *defines* `r04-0098`

- `r04-0190` *STATED* — For night crew routines, the user's usual model is fine.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0184`
  ↳ *qualifies* `r04-0161`

- `y01-0019` *STATED* — Codex fast mode is a separate speed setting from model and effort: it returns responses sooner but uses up your usage allowance more quickly.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *evidence-for* `g11-0130`
  ↳ *contrast* `y01-0013` — speed setting vs reasoning depth

- `y01-0137` *STATED* — Haiku is 'your beginner': crazy fast, cheap, and perfect for tasks like making a PDF or cleaning up a lead list.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *example-of* `y01-0136`
  ↳ *contrast* `y01-0138`

- `y01-0140` *STATED* — Fable is 'your top expert': use it for deep research and bigger projects where Claude needs to plan, reason and execute multiple steps on its own.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *example-of* `y01-0136`

- `y02-0006` *STATED* — The Harvey customer agent runs on the Claude plan you already pay for, so there is no extra bill (no separate API spend).
  > “it runs on the Claude plan you already pay for, so there's no extra bill”
  — [DYsc09LJB0o](https://youtu.be/DYsc09LJB0o)
  ↳ *example-of* `g05-0314`
  ↳ *part-of* `y02-0001`
  ↳ *enables* `y02-0001`

- `y02-0016` *STATED* — A local model like MiniCPM V 4.7 means you never pay per message, unlike Claude.
  > “you never pay per message like you do for Claude”
  — [nJLWbwhr13o](https://youtu.be/nJLWbwhr13o) [_O69QaBeuVU](https://youtu.be/_O69QaBeuVU) [pibEuNPl9NU](https://youtu.be/pibEuNPl9NU)
  ↳ *part-of* `y02-0008`
  ↳ *contrast* `y02-0191` — local model: no limit at all

- `y02-0018` *STATED* — By default Opus does everything in Claude Code — reads every log, searches every file, fixes every typo, even renames a file — and every one of those jobs comes out of your usage limit.
  > “right now Opus reads every log, searches every file, and fixes every typo, and it all comes out of your limit”
  — [9JtUYiRPQYc](https://youtu.be/9JtUYiRPQYc) [aSznLprottg](https://youtu.be/aSznLprottg) [EWbnYkyO5VM](https://youtu.be/EWbnYkyO5VM)
  ↳ *evidence-for* `g07-0105`
  ↳ *evidence-for* `y02-0020`
  ↳ *evidence-for* `y02-0097` — Opus is the default everywhere

- `y02-0019` *STATED* — Asking Opus to search a file or fix a typo burns the same limit as a hard problem.
  > “when you ask Opus to search a file or fix a typo, it burns the same limit as a hard problem”
  — [9JtUYiRPQYc](https://youtu.be/9JtUYiRPQYc) [aSznLprottg](https://youtu.be/aSznLprottg) [EWbnYkyO5VM](https://youtu.be/EWbnYkyO5VM)
  ↳ *evidence-for* `y02-0020`

- `y02-0023` *STATED* — Routing the easy work to Haiku and only hard problems to Opus gives you the same results.
  > “only the hard problems go to Opus, so you get the same results”
  — [9JtUYiRPQYc](https://youtu.be/9JtUYiRPQYc) [aSznLprottg](https://youtu.be/aSznLprottg) [EWbnYkyO5VM](https://youtu.be/EWbnYkyO5VM)
  ↳ *part-of* `y02-0021`
  ↳ *qualifies* `y02-0019` — easy work doesn't need Opus quality

- `y02-0026` *STATED* — Because Haiku 5.5 is so cheap per token, the easy work barely counts against (barely touches) your limit.
  > “so the easy work barely counts”
  — [9JtUYiRPQYc](https://youtu.be/9JtUYiRPQYc) [aSznLprottg](https://youtu.be/aSznLprottg) [EWbnYkyO5VM](https://youtu.be/EWbnYkyO5VM)
  ↳ *part-of* `y02-0021`

- `y02-0027` *STATED* — With the limit-routing skill your limit lasts way longer and you don't change how you work at all, because the routing is automatic.
  > “your limit lasts way longer and you don't change how you work at all”
  — [9JtUYiRPQYc](https://youtu.be/9JtUYiRPQYc) [aSznLprottg](https://youtu.be/aSznLprottg) [EWbnYkyO5VM](https://youtu.be/EWbnYkyO5VM)
  ↳ *part-of* `y02-0021`

- `y02-0028` *STATED* — Model routing means the same Claude plan gets you way more work before you hit the wall.
  > “the same plan gets you way more work before you hit the wall”
  — [9JtUYiRPQYc](https://youtu.be/9JtUYiRPQYc) [aSznLprottg](https://youtu.be/aSznLprottg) [EWbnYkyO5VM](https://youtu.be/EWbnYkyO5VM)
  ↳ *part-of* `y02-0021`

- `y02-0124` *CORE* — The people who never hit their Claude limit aren't using it better than you — they turn off the skills they never use.
  > “The people who never hit their Claude limit aren't using it better than you. That's because they turn off the skills they never use.”
  — [Zy2NN8NydeA](https://youtu.be/Zy2NN8NydeA) [Eokwl898JUk](https://youtu.be/Eokwl898JUk)

- `y02-0126` *STATED* — Every skill you installed and forgot about is quietly eating your limit.
  — [Zy2NN8NydeA](https://youtu.be/Zy2NN8NydeA) [Eokwl898JUk](https://youtu.be/Eokwl898JUk)
  ↳ *evidence-for* `y02-0124`

- `y02-0128` *STATED* — The Skill Doctor also shows how often Claude uses each skill, so you spot which skills eat your limit for no reason.
  — [Zy2NN8NydeA](https://youtu.be/Zy2NN8NydeA) [Eokwl898JUk](https://youtu.be/Eokwl898JUk)
  ↳ *part-of* `y02-0127`

- `y02-0191` *CORE* — Alex Chen's usage-limit advice in this batch reduces to two moves: stop paying Opus prices for easy work (route to Haiku) and stop paying per-message context for skills you never use (turn them off).
  — [9JtUYiRPQYc](https://youtu.be/9JtUYiRPQYc) [aSznLprottg](https://youtu.be/aSznLprottg) [EWbnYkyO5VM](https://youtu.be/EWbnYkyO5VM) [Zy2NN8NydeA](https://youtu.be/Zy2NN8NydeA) [Eokwl898JUk](https://youtu.be/Eokwl898JUk) [GF2xgaEnQ0o](https://youtu.be/GF2xgaEnQ0o) [g6ZnVE4kQCk](https://youtu.be/g6ZnVE4kQCk)
  ↳ *generalizes* `y02-0187`
  ↳ *generalizes* `y02-0129`

- `y03-0001` *STATED* — Every Claude message rereads the whole chat, which is why a fixed $1,000 budget buys a limited number of messages even on the cheapest model.
  > “each one rereads the whole chat”
  — [FqOzuuip5iA](https://youtu.be/FqOzuuip5iA)
  ↳ *evidence-for* `g19-0017`
  ↳ *because* `y03-0002` — messages per $1,000 are bounded because every message rereads the chat
  ↳ *evidence-for* `y03-0025`

- `y03-0004` *STATED* — Anthropic describes Sonnet as the best mix of speed and intelligence among the Claude models.
  > “which Claude calls the best mix of speed and smart”
  — [FqOzuuip5iA](https://youtu.be/FqOzuuip5iA)
  ↳ *evidence-for* `y01-0138`
  ↳ *qualifies* `y03-0003`
  ↳ *evidence-for* `y03-0180`

- `y03-0006` *STATED* — Anthropic's team says to start with Opus for most work.
  > “Claude's team says to start here for most work”
  — [FqOzuuip5iA](https://youtu.be/FqOzuuip5iA)
  ↳ *contradicts* `y01-0138` — "Anthropic team says to start with Opus for most work" vs "Sonnet ... start 90% of your tasks there"
  ↳ *contradicts* `g12-0026` — start with Opus for most work vs default to Sonnet 5.5 and escalate to Opus only for the hardest work
  ↳ *qualifies* `y03-0005`
  ↳ *qualifies* `y03-0185` — start-here-for-most-work vs still-the-one-for-big-messy-projects

- `y03-0008` *STATED* — Claude Fable is the model meant for the hardest problems.
  — [FqOzuuip5iA](https://youtu.be/FqOzuuip5iA)
  ↳ *qualifies* `y03-0007` — fewest messages, reserved for hardest problems

- `y03-0011` *STATED* — The same Claude message uses far more tokens when it is sent in a long chat than as a single fresh message.
  — [Rgb7FFLwz60](https://youtu.be/Rgb7FFLwz60)
  ↳ *evidence-for* `y03-0025`

- `y03-0012` *STATED* — Alex's four actions that eat the most Claude tokens: a big PDF, choosing Opus, plugins, and agent teams.
  — [Rgb7FFLwz60](https://youtu.be/Rgb7FFLwz60)

- `y03-0025` *CORE* — Rereading is the thread through Alex's token advice: messages are counted 'because each one rereads the whole chat', big PDFs are reread every message, plugins load into every chat, and two thirds of his $4,500 API-priced bill was rereading.
  — [FqOzuuip5iA](https://youtu.be/FqOzuuip5iA) [Rgb7FFLwz60](https://youtu.be/Rgb7FFLwz60) [_I57Pc36DIg](https://youtu.be/_I57Pc36DIg)

- `y03-0027` *STATED* — Claude summarizing your conversation during compaction usually makes it stupid.
  > “stop Claude from summarizing your conversation which usually makes it stupid”
  — [20RWbPnejOE](https://youtu.be/20RWbPnejOE) [tq8Addr9brU](https://youtu.be/tq8Addr9brU) [kUH4J8VWe-I](https://youtu.be/kUH4J8VWe-I) [7eL_2dx0-bU](https://youtu.be/7eL_2dx0-bU)
  ↳ *evidence-for* `g12-0177`
  ↳ *because* `y03-0026`

- `y03-0029` *STATED* — Fast-Jev Compaction keeps every single word you and Claude said.
  — [20RWbPnejOE](https://youtu.be/20RWbPnejOE) [tq8Addr9brU](https://youtu.be/tq8Addr9brU) [kUH4J8VWe-I](https://youtu.be/kUH4J8VWe-I) [7eL_2dx0-bU](https://youtu.be/7eL_2dx0-bU)
  ↳ *evidence-for* `g12-0178`
  ↳ *part-of* `y03-0026`
  ↳ *enables* `y03-0034`

- `y03-0031` *STATED* — Files Claude opened earlier in a session are what make your context window fat.
  > “files it opened earlier which makes your context window pretty fat”
  — [20RWbPnejOE](https://youtu.be/20RWbPnejOE) [tq8Addr9brU](https://youtu.be/tq8Addr9brU) [kUH4J8VWe-I](https://youtu.be/kUH4J8VWe-I) [7eL_2dx0-bU](https://youtu.be/7eL_2dx0-bU)
  ↳ *evidence-for* `g12-0183`
  ↳ *evidence-for* `g02-0034`
  ↳ *because* `y03-0030`
  ↳ *evidence-for* `y03-0025` — opened files are part of what is reread every turn

- `y03-0034` *STATED* — With Fast-Jev Compaction all your important context is still there, even in a really long session.
  — [20RWbPnejOE](https://youtu.be/20RWbPnejOE) [tq8Addr9brU](https://youtu.be/tq8Addr9brU) [kUH4J8VWe-I](https://youtu.be/kUH4J8VWe-I) [7eL_2dx0-bU](https://youtu.be/7eL_2dx0-bU)

- `y03-0044` *STATED* — Picking the right effort level saves your Claude limit for the jobs that actually need it.
  — [ItG-vSZFWgA](https://youtu.be/ItG-vSZFWgA) [mVKBGZNsSa4](https://youtu.be/mVKBGZNsSa4) [HTu9VPLvcP0](https://youtu.be/HTu9VPLvcP0)
  ↳ *evidence-for* `y01-0018`
  ↳ *because* `y03-0045`

- `y03-0108` *STATED* — Making slides and websites in Claude Design wastes your Claude limit.
  > “Everyone making slides on websites and Claude Design is wasting their Claude limit.”
  — [NrJa3MCde-I](https://youtu.be/NrJa3MCde-I) [vdLceKphMoQ](https://youtu.be/vdLceKphMoQ)
  ↳ *evidence-for* `g10-0199`

- `y03-0109` *STATED* — Claude's own page says a full slide deck uses more of your limit than a normal message.
  — [NrJa3MCde-I](https://youtu.be/NrJa3MCde-I) [vdLceKphMoQ](https://youtu.be/vdLceKphMoQ)
  ↳ *evidence-for* `g10-0200`
  ↳ *evidence-for* `y03-0108`

- `y03-0185` *STATED* — Anthropic, the creators of Claude, say Opus is still the one for big, messy projects.
  — [JifO6tUsSlA](https://youtu.be/JifO6tUsSlA)
  ↳ *evidence-for* `g12-0022`
  ↳ *evidence-for* `g12-0020`
  ↳ *qualifies* `y03-0180` — Opus still for big, messy projects

- `y03-0186` *STATED* — Picking the right Claude model for each job makes your limits last way longer now.
  — [JifO6tUsSlA](https://youtu.be/JifO6tUsSlA)
  ↳ *evidence-for* `g12-0003`
  ↳ *leads-to* `y03-0205`

- `y04-0018` *STATED* — Anthropic offered free Claude Code credits for cloud sessions: $250 for Max subscribers and $100 for Pro subscribers.
  > “You get $250 on Max or $100 on Pro for cloud sessions”
  — [BgOlXwLlBrY](https://youtu.be/BgOlXwLlBrY) [QnzAaLZ70c0](https://youtu.be/QnzAaLZ70c0) [OyKQsxpeSLY](https://youtu.be/OyKQsxpeSLY)
  ↳ *evidence-for* `g13-0100`
  ↳ *evidence-for* `g13-0101`

- `y04-0020` *STATED* — The Claude Code cloud-session credit sits outside your usage limits.
  > “But here's the part that matters. The credit sits outside your usage limits.”
  — [BgOlXwLlBrY](https://youtu.be/BgOlXwLlBrY) [QnzAaLZ70c0](https://youtu.be/QnzAaLZ70c0) [OyKQsxpeSLY](https://youtu.be/OyKQsxpeSLY)
  ↳ *evidence-for* `g13-0113`
  ↳ *qualifies* `y04-0018`
  ↳ *enables* `y04-0021`

- `y04-0023` *STATED* — The cloud credit is not applied automatically: Max and Pro users have to claim it ('yours is just sitting there too').
  > “If you're on Max or Pro, yours is just sitting there too.”
  — [BgOlXwLlBrY](https://youtu.be/BgOlXwLlBrY) [QnzAaLZ70c0](https://youtu.be/QnzAaLZ70c0) [OyKQsxpeSLY](https://youtu.be/OyKQsxpeSLY)
  ↳ *evidence-for* `g13-0099`
  ↳ *qualifies* `y04-0018`

- `y04-0024` *STATED* — All you need to claim the cloud-session credit is a Claude account on a Max or Pro plan.
  > “all you need is a Claude account”
  — [BgOlXwLlBrY](https://youtu.be/BgOlXwLlBrY) [QnzAaLZ70c0](https://youtu.be/QnzAaLZ70c0) [OyKQsxpeSLY](https://youtu.be/OyKQsxpeSLY)
  ↳ *contradicts* `g13-0114` — video: "all you need is a Claude account on a Max or Pro plan" vs guide: only individual Pro/Max subscribers already subscribed on Sept 23 2026
  ↳ *depends-on* `y04-0018`
  ↳ *qualifies* `y04-0023`

- `y04-0059` *STATED* — Headline claim: 'This new AI model will 10x your Claude Code.'
  > “This new AI model will 10x your Claude Code.”
  — [Hdc86XqcDWM](https://youtu.be/Hdc86XqcDWM) [N8_l0apeaQE](https://youtu.be/N8_l0apeaQE) [1FXRIeZ2-lE](https://youtu.be/1FXRIeZ2-lE)
  ↳ *qualifies* `y04-0057`

### concept

- `g03-0001` *CORE* — Claude Code resends the whole conversation with every request/turn, so anything sitting in the chat (files, wrong turns, corrections, check-ins) is paid for again on every turn.
  — [g-rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it](https://chen.media/guides/rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it) [g-stop-claude-goal-check-ins-from-eating-your-limit](https://chen.media/guides/stop-claude-goal-check-ins-from-eating-your-limit)
  ↳ *because* `g03-0009`
  ↳ *evidence-for* `g19-0017`

- `g03-0025` *INFERRED* — Moving rare procedures from CLAUDE.md into skills saves context because CLAUDE.md is loaded every session while a skill's body is pulled in only when it is used.
  — [g-shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit](https://chen.media/guides/shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit)
  ↳ *because* `g03-0024`

- `g03-0216` *INFERRED* — CLAUDE_CODE_SUBAGENT_MODEL picks the helper model and CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1 makes that choice override any model a helper would otherwise pick.
  — [g-run-every-claude-helper-agent-on-haiku](https://chen.media/guides/run-every-claude-helper-agent-on-haiku)
  ↳ *qualifies* `g03-0215`
  ↳ *contrast* `g03-0211` — FORCE overrides 'unless something else picks one'

- `g03-0235` *STATED* — Answer me with HTML is fast because Claude only writes a short Markdown draft and the tool that ships with the skill draws the page.
  — [g-answer-me-with-html-make-claude-answer-with-one-clean-page-not-a-wall-of-text](https://chen.media/guides/answer-me-with-html-make-claude-answer-with-one-clean-page-not-a-wall-of-text)
  ↳ *part-of* `g03-0228`

- `g04-0002` *STATED* — The four usage-burning habits that Claude Code's /usage screen warns about are: max effort, workflows, always-on context, and large tool results.
  — [g-the-four-habits-eating-your-claude-limit-and-the-fix-for-each](https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each)
  ↳ *part-of* `g04-0001`

- `g09-0134` *STATED* — For every installed skill, Claude Code keeps a short note in the conversation, the skill's name and description, so Claude knows the skill is there.
  — [g-find-the-claude-skills-eating-your-limit-skill-doctor](https://chen.media/guides/find-the-claude-skills-eating-your-limit-skill-doctor)

- `g09-0135` *STATED* — The full skill body only loads when the skill is used, but its name-and-description note never leaves context.
  > “The full skill only loads when it's used, but the note never leaves.”
  — [g-find-the-claude-skills-eating-your-limit-skill-doctor](https://chen.media/guides/find-the-claude-skills-eating-your-limit-skill-doctor)
  ↳ *qualifies* `g09-0134`
  ↳ *qualifies* `g18-0103`

- `g12-0179` *STATED* — Guide section 'What it keeps and what it drops' details what Fast-Jev Compaction keeps versus removes (body email-gated).
  — [g-stop-claude-code-s-compact-from-summarizing-away-your-chat](https://chen.media/guides/stop-claude-code-s-compact-from-summarizing-away-your-chat)
  ↳ *part-of* `g12-0171`
  ↳ *qualifies* `g12-0178`

- `g12-0306` *INFERRED* — Alex's usage-limit toolkit across these guides has five levers: route to the cheaper model (Sonnet 5.5 at half Opus's price), trim legacy CLAUDE.md rules (-9% cost), stop whole-conversation re-reads, compact by dropping only tool output, and use lower-priority mode after the limit.
  — [g-claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task](https://chen.media/guides/claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task) [g-clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit](https://chen.media/guides/clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit) [g-what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything) [g-stop-claude-code-s-compact-from-summarizing-away-your-chat](https://chen.media/guides/stop-claude-code-s-compact-from-summarizing-away-your-chat) [g-keep-using-claude-code-after-you-hit-your-usage-limit](https://chen.media/guides/keep-using-claude-code-after-you-hit-your-usage-limit)
  ↳ *generalizes* `g12-0026`
  ↳ *generalizes* `g12-0096`
  ↳ *generalizes* `g12-0118`
  ↳ *generalizes* `g12-0178`
  ↳ *generalizes* `g12-0241`

- `g13-0171` *STATED* — Jev answer shape 1: pick one option from a list.
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *part-of* `g13-0170`

- `g13-0172` *STATED* — Jev answer shape 2: give a score on a rubric.
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *part-of* `g13-0170`

- `g13-0173` *STATED* — Jev answer shape 3: say how likely a statement is to be true.
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *part-of* `g13-0170`

- `g16-0042` *STATED* — A Claude Code session costs you money in three separate, independent ways: the RATE, the VOLUME and the WASTE.
  > “A Claude Code session costs you money in three separate ways, and they are independent.”
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you)
  ↳ *enables* `g16-0043`
  ↳ *defines* `g16-0039`

- `g16-0281` *STATED* — Prompt Master's Memory Block is the fix for long sessions.
  > “The Memory Block, which is the fix for long sessions”
  — [g-the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting](https://chen.media/guides/the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting)
  ↳ *part-of* `g16-0270`

- `g17-0115` *CORE* — A coding agent does not send just your question: it sends your question plus every tool schema it exposes, plus the whole conversation so far, plus every file it has read this session.
  > “It sends your question plus every tool schema it exposes, plus the whole conversation so far, plus every file it has read this session.”
  — [g-cut-what-your-coding-agent-sends-to-the-model](https://chen.media/guides/cut-what-your-coding-agent-sends-to-the-model)
  ↳ *contrast* `g17-0150` — cut tokens sent vs pool more free tokens
  ↳ *evidence-for* `g19-0017`

- `g18-0283` *CORE* — Everything loaded into Claude's context, from MCP tool schemas to unused skills to stale CLAUDE.md lines, costs tokens on every request, so a lean setup is both cheaper and better.
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again) [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep) [g-one-command-installs-anthropic-s-own-skill-library](https://chen.media/guides/one-command-installs-anthropic-s-own-skill-library) [g-give-claude-a-memory-that-survives-the-chat-window](https://chen.media/guides/give-claude-a-memory-that-survives-the-chat-window)
  ↳ *evidence-for* `g04-0006`

- `g19-0002` *STATED* — The 28-ways usage-limits guide is organised in six tiers: Tier 1 the three from the video, Tier 2 context hygiene, Tier 3 right model right job, Tier 4 get it right the first time, Tier 5 session hygiene, Tier 6 make the savings permanent, then a closing 'If you only do three things'.
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *part-of* `g19-0001`

- `g19-0011` *STATED* — Tier 3 of the usage-limits guide is 'Right model, right job': match each task to the model it actually needs.
  > “Right model, right job”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *part-of* `g19-0002`

- `g19-0012` *STATED* — Tier 4 of the usage-limits guide, 'Get it right the first time', treats avoiding redo cycles as a token-saving lever.
  > “Get it right the first time”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *part-of* `g19-0002`

- `g19-0013` *STATED* — Tier 5 of the usage-limits guide is 'Session hygiene'.
  > “Session hygiene”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *part-of* `g19-0002`

- `g19-0014` *STATED* — Tier 6 of the usage-limits guide is 'Make the savings permanent': bake the token savings into lasting setup rather than relying on remembering them.
  > “Make the savings permanent”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *part-of* `g19-0002`

- `g19-0029` *STATED* — Tier 4 of the 50 Claude tips is 'Speed and cost'.
  > “Speed and cost”
  — [g-50-claude-tips-ranked-worst-to-best](https://chen.media/guides/50-claude-tips-ranked-worst-to-best)
  ↳ *part-of* `g19-0043`
  ↳ *generalizes* `g19-0001`

- `g20-0287` *CORE* — Alex routes models by role: the smartest model plans, a cheaper model does the bulk work (the dev-team Coder, the memory guide's 'cheap model swap').
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team) [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *generalizes* `g20-0210`
  ↳ *example-of* `y02-0187`

- `g21-0158` *INFERRED* — A recurring Alex Chen pattern: the expensive flagship model plans and a much cheaper model executes (Fable 5 plans / Sonnet or Haiku builds; GPT-5.6 Sol plans / Luna executes).
  — [g-turn-your-whole-backlog-into-finished-plans-in-one-night](https://chen.media/guides/turn-your-whole-backlog-into-finished-plans-in-one-night) [g-three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team](https://chen.media/guides/three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team)

- `y02-0125` *CORE* — Claude rereads a short note (the description) about every skill you've installed on every single message.
  > “Claude rereads a short note about every skill you've installed on every single message”
  — [Zy2NN8NydeA](https://youtu.be/Zy2NN8NydeA) [Eokwl898JUk](https://youtu.be/Eokwl898JUk)
  ↳ *because* `y02-0126`

### definition

- `g04-0231` *STATED* — Claude Code's advisor lets a cheaper main model do the routine turns and ask a stronger model for advice at the moments that decide the outcome.
  — [g-let-opus-advise-while-sonnet-does-the-routine-work](https://chen.media/guides/let-opus-advise-while-sonnet-does-the-routine-work)
  ↳ *because* `g04-0230`
  ↳ *part-of* `g04-0241`
  ↳ *evidence-for* `g11-0100`

- `g05-0146` *STATED* — Prompt caching lets the API reuse what it already processed and bill the re-read at the cached token rate.
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)
  ↳ *defines* `g05-0144`

- `g05-0162` *STATED* — Effort levels control how much Claude thinks on each step.
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)
  ↳ *defines* `g05-0161`
  ↳ *evidence-for* `g05-0317`
  ↳ *evidence-for* `y01-0143`

- `g06-0227` *STATED* — Alex's 'easy, low-risk jobs' for Haiku: reading logs, searching files, listing folders, renames and one-line edits.
  — [g-make-your-claude-limit-last-the-haiku-helper-and-3-habits](https://chen.media/guides/make-your-claude-limit-last-the-haiku-helper-and-3-habits)
  ↳ *defines* `g06-0224`
  ↳ *evidence-for* `y02-0022`

- `g12-0175` *STATED* — When a Claude Code session fills its context window, /compact (or auto-compaction) asks Claude to rewrite the conversation so far into a shorter summary, and the summary replaces the chat.
  — [g-stop-claude-code-s-compact-from-summarizing-away-your-chat](https://chen.media/guides/stop-claude-code-s-compact-from-summarizing-away-your-chat)

- `g16-0044` *STATED* — The RATE is what you pay per token, which is a function of who you buy the tokens from.
  > “The RATE. What you pay per token, which is a function of who you buy them from.”
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you)
  ↳ *part-of* `g16-0042`
  ↳ *example-of* `g16-0013`

- `g16-0045` *STATED* — The VOLUME is how many tokens come back, which is a function of how much prose the model writes around the code.
  > “The VOLUME. How many tokens come back, which is a function of how much prose the model writes around the code.”
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you)
  ↳ *part-of* `g16-0042`
  ↳ *generalizes* `g03-0099`

- `g16-0046` *STATED* — The WASTE is tokens you pay for twice, which is a function of a cache clock you cannot see.
  > “The WASTE. Tokens you pay for twice, which is a function of a cache clock you cannot see.”
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you)
  ↳ *part-of* `g16-0042`
  ↳ *generalizes* `g05-0315`

- `g19-0164` *STATED* — Claude Code Router routes each request to the model that should actually handle it.
  > “Routes each request to the model that should actually handle it.”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *defines* `g19-0156`
  ↳ *example-of* `g19-0011`

- `y01-0013` *STATED* — The Codex reasoning effort slider controls how much thinking the chosen model does.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *evidence-for* `g05-0162`
  ↳ *part-of* `y01-0012`

- `y01-0017` *STATED* — Usage limit (Alex's plain-English definition): how many more messages you can send before you have to wait for your usage limit to reset.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *defines* `y01-0016`

- `y01-0031` *STATED* — Context is the information available to the AI while it's working: your messages, instructions, and information read from files or tools.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)

- `y01-0143` *STATED* — Claude's effort slider controls how much time the AI spends thinking about your problem.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)

### example

- `g02-0040` *STATED* — Context Mode README example: a 56 KB Playwright snapshot comes back as 299 bytes.
  — [g-stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode)
  ↳ *evidence-for* `g02-0037`

- `g02-0041` *STATED* — Context Mode README example: 47 file reads totalling 700 KB become one 3.6 KB call.
  — [g-stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode)
  ↳ *evidence-for* `g02-0037`

- `g03-0171` *STATED* — When auto-continue engages you see "Usage limit reached · limit resets 3:45pm" and under it "Continuing automatically at 3:45pm · esc to cancel".
  > “Continuing automatically at 3:45pm · esc to cancel”
  — [g-let-claude-code-wait-out-your-limit-and-carry-on](https://chen.media/guides/let-claude-code-wait-out-your-limit-and-carry-on)
  ↳ *example-of* `g03-0166`

- `g05-0100` *STATED* — Effortless picks Low effort for a quick question and High for a hard job.
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless)
  ↳ *example-of* `g05-0099`

- `g06-0233` *STATED* — The Haiku 5.5 vs Opus test job: find the errors in six log files; both models found all six (6 of 6).
  — [g-send-claude-s-easy-jobs-to-haiku-5-5-with-one-helper-file](https://chen.media/guides/send-claude-s-easy-jobs-to-haiku-5-5-with-one-helper-file)
  ↳ *evidence-for* `g06-0232`
  ↳ *example-of* `g06-0227`

- `g07-0213` *STATED* — Three Standard seats and two Premium seats come to $260 a month of Team API credits (3 x $20 + 2 x $100).
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *example-of* `g07-0212`
  ↳ *evidence-for* `g04-0139`

- `g09-0136` *STATED* — Install twenty skills, forget fifteen of them, and fifteen notes ride along with everything you send.
  > “Install twenty skills, forget fifteen of them, and fifteen notes ride along with everything you send.”
  — [g-find-the-claude-skills-eating-your-limit-skill-doctor](https://chen.media/guides/find-the-claude-skills-eating-your-limit-skill-doctor)
  ↳ *example-of* `g09-0131`

- `g13-0177` *STATED* — Small calls inside a Claude Code workflow: which model should do this, is this email worth answering, does this test failure look flaky.
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *example-of* `g13-0176`

- `g14-0145` *STATED* — Alex's Bedrock test prompt: 'Explain Amazon Bedrock in three short sentences for a beginner.'
  > “Explain Amazon Bedrock in three short sentences for a beginner.”
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *example-of* `g14-0144`

- `g17-0117` *STATED* — A twenty-turn coding agent session pays for the same file read twenty times.
  > “a twenty turn session pays for the same file read twenty times”
  — [g-cut-what-your-coding-agent-sends-to-the-model](https://chen.media/guides/cut-what-your-coding-agent-sends-to-the-model)
  ↳ *example-of* `g17-0116`
  ↳ *evidence-for* `g17-0118`
  ↳ *evidence-for* `g03-0121`

- `g19-0018` *STATED* — A Claude chat that has been running for two hours pays for two hours of history on every reply, whether or not any of it is still relevant.
  > “a chat that has been running for two hours is paying for two hours of history on every reply”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *example-of* `g19-0017`

- `y01-0014` *STATED* — Effort example: shortening a paragraph is a straightforward job, so use lower effort.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *example-of* `y01-0013`
  ↳ *contrast* `y01-0015`

- `y01-0015` *STATED* — Effort example: comparing two detailed plans and finding the problems in each one benefits from higher effort.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *example-of* `y01-0013`

### idea

- `g03-0009` *INFERRED* — Across this batch the limit-saving levers group into: shrink what always loads (CLAUDE.md, agent descriptions), stop pasting what is not needed (@ files, file-hunting), say less (Caveman), remove dead turns (rewind), compact helpers sooner, and run helpers on a cheaper model (Haiku).
  — [g-shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit](https://chen.media/guides/shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit) [g-stop-file-mentions-from-pasting-whole-files-into-your-claude-chat](https://chen.media/guides/stop-file-mentions-from-pasting-whole-files-into-your-claude-chat) [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files) [g-make-claude-answer-in-fewer-words-with-the-caveman-skill](https://chen.media/guides/make-claude-answer-in-fewer-words-with-the-caveman-skill) [g-rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it](https://chen.media/guides/rewind-claude-after-a-wrong-turn-instead-of-arguing-with-it) [g-shorten-your-claude-helper-agent-descriptions](https://chen.media/guides/shorten-your-claude-helper-agent-descriptions) [g-make-your-claude-helpers-summarize-themselves-sooner](https://chen.media/guides/make-your-claude-helpers-summarize-themselves-sooner) [g-run-every-claude-helper-agent-on-haiku](https://chen.media/guides/run-every-claude-helper-agent-on-haiku)

- `g03-0238` *INFERRED* — General lesson from Answer me with HTML: let Claude emit compact structured content and let a deterministic tool render it, instead of paying tokens for Claude to write boilerplate markup.
  — [g-answer-me-with-html-make-claude-answer-with-one-clean-page-not-a-wall-of-text](https://chen.media/guides/answer-me-with-html-make-claude-answer-with-one-clean-page-not-a-wall-of-text)
  ↳ *generalizes* `g03-0235`
  ↳ *qualifies* `g03-0099` — output tokens you pay for can be cut by rendering, not just brevity

- `g07-0221` *INFERRED* — Spending the monthly API credits on Haiku 5.5 ($0.10/M input under 100K-token prompts) through the Batch API (another 50% off) stretches them furthest.
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *part-of* `g07-0203`
  ↳ *example-of* `g07-0220`
  ↳ *depends-on* `g05-0189`

- `g11-0080` *INFERRED* — Running 100 Claudes on one question multiplies token use far beyond a single answer, so the 16-Claude quick mode is the cost lever for everyday questions.
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *because* `g11-0058`
  ↳ *example-of* `g13-0305`

- `g11-0097` *INFERRED* — Route detailed visual-rebuild work to Sonnet 5.5 before reaching for Opus 5.5: near-identical output at half the per-token price.
  — [g-turn-any-photo-into-a-painting-claude-draws-with-code](https://chen.media/guides/turn-any-photo-into-a-painting-claude-draws-with-code)
  ↳ *evidence-for* `g12-0026`

- `g11-0134` *INFERRED* — Because speed tiers only accelerate token output, they pay off on output-heavy work and barely help agent tasks dominated by thinking, test runs and tool waits.
  — [g-is-openais-500-ultrafast-plan-worth-it](https://chen.media/guides/is-openais-500-ultrafast-plan-worth-it)

- `g16-0009` *INFERRED* — Unifying idea across these guides: most Claude quality and cost problems are context problems — too much pasted, rules written for old models, no signal about what matters — and the fix is to change what enters the context (an index address, fewer stale rules, load-bearing prompts) rather than to prompt harder.
  — [g-15-claude-mistakes-that-are-quietly-costing-you-tokens](https://chen.media/guides/15-claude-mistakes-that-are-quietly-costing-you-tokens) [g-the-one-page-that-points-claude-at-the-right-notes](https://chen.media/guides/the-one-page-that-points-claude-at-the-right-notes) [g-why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it](https://chen.media/guides/why-your-claude-md-is-making-claude-worse-and-the-prompt-that-audits-it) [g-the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting](https://chen.media/guides/the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting)
  ↳ *generalizes* `g19-0016`

- `g16-0013` *INFERRED* — Model and provider routing recurs as a cost lever: send simple work away from the biggest model, let Ruflo's router decide which model each piece of work is worth, buy tokens from a cheaper source (deepclaude), use a free preview model (ox-alpha), or route past the usage limit (OmniRoute).
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert) [g-ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm](https://chen.media/guides/ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm) [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you) [g-the-anonymous-model-that-makes-claude-code-free-until-august-27](https://chen.media/guides/the-anonymous-model-that-makes-claude-code-free-until-august-27) [g-three-plugins-that-fix-claude-code-s-setup-limits-and-memory](https://chen.media/guides/three-plugins-that-fix-claude-code-s-setup-limits-and-memory)

- `g21-0118` *STATED* — Spend your last free Fable 5 night mining your whole backlog into build-ready blueprints, so cheaper models build them for months.
  — [g-turn-your-whole-backlog-into-finished-plans-in-one-night](https://chen.media/guides/turn-your-whole-backlog-into-finished-plans-in-one-night)
  ↳ *part-of* `g21-0117`
  ↳ *example-of* `g21-0121`
  ↳ *depends-on* `g21-0031` — same free-window deadline
  ↳ *evidence-for* `g23-0016`

- `g22-0064` *INFERRED* — The Sol/Terra/Luna line maps onto Claude tiers: a flagship (Fable 5 or Opus) writes the spec and inspects, Sonnet drafts, Haiku mass-produces.
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)
  ↳ *generalizes* `g22-0056`
  ↳ *generalizes* `g22-0282`
  ↳ *example-of* `g21-0158`

- `g23-0026` *INFERRED* — The clone method is cost routing: spend the strongest model once to author durable files (audit, skills, instructions) that cheaper models then execute on every later run.
  — [g-clone-the-smart-model-s-brain-into-the-cheap-one](https://chen.media/guides/clone-the-smart-model-s-brain-into-the-cheap-one)
  ↳ *generalizes* `g23-0012`
  ↳ *example-of* `g21-0158`

- `g23-0113` *INFERRED* — Because a skill loads only when relevant, installed skills cost little context until used, unlike always-loaded CLAUDE.md instructions.
  — [g-five-claude-skills-that-beat-99-of-users](https://chen.media/guides/five-claude-skills-that-beat-99-of-users)
  ↳ *because* `g23-0103`
  ↳ *evidence-for* `g09-0135`

### method

- `g02-0037` *STATED* — Context Mode runs Claude's reading work in a sandbox and sends back only the answer.
  > “runs that work in a sandbox and sends back only the answer”
  — [g-stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode)
  ↳ *part-of* `g02-0031`
  ↳ *example-of* `g17-0120`

- `g02-0038` *STATED* — Each Context Mode ctx_execute call runs in its own subprocess, and only what it prints comes back into the chat.
  — [g-stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode)
  ↳ *part-of* `g02-0037`

- `g02-0042` *STATED* — Context Mode indexes big output in a local SQLite search index, so Claude looks up the one part it needs later instead of re-reading it.
  > “Search instead of re-reading”
  — [g-stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode)
  ↳ *part-of* `g02-0031`
  ↳ *qualifies* `g02-0037` — lossy output stays searchable

- `g02-0043` *STATED* — Before Claude compacts the chat, Context Mode saves a small session snapshot (2 KB or less) and restores it afterwards, so you keep working from your last prompt.
  — [g-stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode)
  ↳ *part-of* `g02-0031`
  ↳ *qualifies* `g12-0176`

- `g02-0177` *STATED* — With Trail-code, Claude Code gets pointers to the matching files with each prompt, so it stops opening file after file to find its way.
  — [g-trail-code-stop-claude-getting-lost-in-your-code](https://chen.media/guides/trail-code-stop-claude-getting-lost-in-your-code)
  ↳ *part-of* `g02-0176`
  ↳ *contrast* `g02-0179`
  ↳ *contrast* `g02-0042` — map-then-point vs index-then-search to avoid re-reading
  ↳ *contrast* `g03-0120`

- `g02-0201` *STATED* — Run /usage and look at the Loops row: it shows your heaviest scheduled tasks and how often each fires.
  — [g-find-the-claude-code-loops-that-are-quietly-eating-your-limit](https://chen.media/guides/find-the-claude-code-loops-that-are-quietly-eating-your-limit)
  ↳ *leads-to* `g02-0204`
  ↳ *part-of* `g03-0073`

- `g02-0204` *STATED* — Step 2 of the loops guide (email-gated) is to cancel the loops you forgot.
  — [g-find-the-claude-code-loops-that-are-quietly-eating-your-limit](https://chen.media/guides/find-the-claude-code-loops-that-are-quietly-eating-your-limit)
  ↳ *leads-to* `g02-0205`
  ↳ *qualifies* `g02-0195`

- `g02-0205` *STATED* — Watch a build instead of polling it with a loop ('Step 3: watch, don't poll').
  > “watch, don't poll”
  — [g-find-the-claude-code-loops-that-are-quietly-eating-your-limit](https://chen.media/guides/find-the-claude-code-loops-that-are-quietly-eating-your-limit)
  ↳ *contrast* `g02-0196` — event watching instead of timer polling

- `g03-0022` *STATED* — Step 1 of shrinking CLAUDE.md: in Claude Code type /context, which shows what is using your context window.
  — [g-shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit](https://chen.media/guides/shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit)
  ↳ *part-of* `g03-0021`
  ↳ *contrast* `g03-0076` — /context = context window now; /usage = plan-limit attribution over 24h/7d

- `g03-0076` *STATED* — In Claude Code type /usage to open the usage breakdown; /cost and /stats open the same screen.
  — [g-find-what-is-draining-your-claude-limit-with-usage](https://chen.media/guides/find-what-is-draining-your-claude-limit-with-usage)
  ↳ *enables* `g03-0073`

- `g03-0078` *STATED* — In the /usage screen press d or w to switch between the last 24 hours and the last 7 days.
  — [g-find-what-is-draining-your-claude-limit-with-usage](https://chen.media/guides/find-what-is-draining-your-claude-limit-with-usage)
  ↳ *part-of* `g03-0077`

- `g03-0079` *STATED* — Step 2 of the /usage guide: read the flags it raises about the habits behind your usage.
  — [g-find-what-is-draining-your-claude-limit-with-usage](https://chen.media/guides/find-what-is-draining-your-claude-limit-with-usage)
  ↳ *part-of* `g03-0073`

- `g03-0080` *STATED* — Step 3 of the /usage guide: fix the top culprit first (the guide covers what to do about each culprit type).
  — [g-find-what-is-draining-your-claude-limit-with-usage](https://chen.media/guides/find-what-is-draining-your-claude-limit-with-usage)
  ↳ *depends-on* `g03-0079`
  ↳ *leads-to* `g03-0009`

- `g03-0170` *STATED* — Keep the session open when the usage limit hits so auto-continue can resume it.
  — [g-let-claude-code-wait-out-your-limit-and-carry-on](https://chen.media/guides/let-claude-code-wait-out-your-limit-and-carry-on)
  ↳ *depends-on* `g03-0166`

- `g03-0173` *STATED* — You can cancel the auto-continue wait (esc) or start it yourself (locked section "Cancel it or start it yourself").
  — [g-let-claude-code-wait-out-your-limit-and-carry-on](https://chen.media/guides/let-claude-code-wait-out-your-limit-and-carry-on)
  ↳ *qualifies* `g03-0171`

- `g03-0192` *STATED* — Open ~/.claude/settings.json and add CLAUDE_CODE_GOAL_CHECKIN_MINUTES set to 0 in the env block (or export it in your shell).
  > “"CLAUDE_CODE_GOAL_CHECKIN_MINUTES": "0"”
  — [g-stop-claude-goal-check-ins-from-eating-your-limit](https://chen.media/guides/stop-claude-goal-check-ins-from-eating-your-limit)
  ↳ *example-of* `g03-0004`
  ↳ *part-of* `g03-0010`
  ↳ *defines* `g03-0190`

- `g03-0215` *STATED* — In ~/.claude/settings.json add to the env block CLAUDE_CODE_SUBAGENT_MODEL set to haiku and CLAUDE_CODE_SUBAGENT_MODEL_FORCE set to 1.
  > “"CLAUDE_CODE_SUBAGENT_MODEL": "haiku", "CLAUDE_CODE_SUBAGENT_MODEL_FORCE": "1"”
  — [g-run-every-claude-helper-agent-on-haiku](https://chen.media/guides/run-every-claude-helper-agent-on-haiku)
  ↳ *example-of* `g03-0004`
  ↳ *defines* `g03-0213`

- `g04-0003` *STATED* — Alex Chen's triage for a draining Claude limit: run /usage, read which of the four habit warnings shows up, and fix that one first.
  > “Run /usage, read which one shows up, and fix that one first.”
  — [g-the-four-habits-eating-your-claude-limit-and-the-fix-for-each](https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each)
  ↳ *depends-on* `g04-0001`
  ↳ *leads-to* `g04-0004` — fix whichever warning appears
  ↳ *depends-on* `g03-0073`

- `g04-0004` *STATED* — Max effort is one of the four habits eating a Claude limit, and Alex's guide gives a dedicated fix for it (section 'Fix 1: max effort', body locked).
  — [g-the-four-habits-eating-your-claude-limit-and-the-fix-for-each](https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each)
  ↳ *part-of* `g04-0002`
  ↳ *example-of* `g10-0197`

- `g04-0005` *STATED* — Running workflows is one of the four habits eating a Claude limit, and Alex's guide gives a dedicated fix for it (section 'Fix 2: workflows', body locked).
  — [g-the-four-habits-eating-your-claude-limit-and-the-fix-for-each](https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each)
  ↳ *part-of* `g04-0002`
  ↳ *because* `g04-0011`

- `g04-0006` *STATED* — Always-on context is one of the four habits eating a Claude limit, and Alex's guide gives a dedicated fix for it (section 'Fix 3: always-on context', body locked).
  — [g-the-four-habits-eating-your-claude-limit-and-the-fix-for-each](https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each)
  ↳ *part-of* `g04-0002`
  ↳ *because* `g04-0009`

- `g04-0007` *STATED* — Large tool results are one of the four habits eating a Claude limit, and Alex's guide gives a dedicated fix for them (section 'Fix 4: large tool results', body locked).
  — [g-the-four-habits-eating-your-claude-limit-and-the-fix-for-each](https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each)
  ↳ *part-of* `g04-0002`
  ↳ *because* `g04-0010`

- `g04-0081` *STATED* — Alex recommends tokentab for when you keep hitting your Claude limit (section 'Why it helps when you keep hitting your limit').
  — [g-tokentab-see-where-every-claude-token-goes-as-a-monthly-statement](https://chen.media/guides/tokentab-see-where-every-claude-token-goes-as-a-monthly-statement)
  ↳ *depends-on* `g04-0076`

- `g04-0082` *STATED* — tokentab has several views; Alex's guide picks 'the views worth trying' and relays the repo's own tips on how to read the statement (bodies locked).
  — [g-tokentab-see-where-every-claude-token-goes-as-a-monthly-statement](https://chen.media/guides/tokentab-see-where-every-claude-token-goes-as-a-monthly-statement)
  ↳ *part-of* `g04-0084`

- `g04-0083` *INFERRED* — Pair tokentab (which project, model and kind of work ate tokens) with the /usage habit warnings (which habit is burning the plan) to decide what to fix first.
  — [g-tokentab-see-where-every-claude-token-goes-as-a-monthly-statement](https://chen.media/guides/tokentab-see-where-every-claude-token-goes-as-a-monthly-statement) [g-the-four-habits-eating-your-claude-limit-and-the-fix-for-each](https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each)
  ↳ *depends-on* `g04-0076`
  ↳ *depends-on* `g04-0003`

- `g04-0131` *STATED* — Claiming the monthly Claude API credits takes three steps.
  > “the three steps to claim them”
  — [g-how-to-claim-your-monthly-claude-credits-on-max-and-team-plans](https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans)
  ↳ *part-of* `g04-0122`

- `g04-0132` *STATED* — Step 1 to claim Max-plan API credits: open billing settings (body locked).
  — [g-how-to-claim-your-monthly-claude-credits-on-max-and-team-plans](https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans)
  ↳ *part-of* `g04-0131`
  ↳ *leads-to* `g04-0134`

- `g04-0133` *STATED* — Step 1 for a Team plan to claim its API credits: open Organization settings (body locked).
  — [g-how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets](https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets)
  ↳ *leads-to* `g04-0134`
  ↳ *contrast* `g04-0132` — Team claims in Organization settings, Max in billing settings

- `g04-0134` *STATED* — Step 2 to claim the monthly API credits: link a Console organization (body locked).
  — [g-how-to-claim-your-monthly-claude-credits-on-max-and-team-plans](https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans) [g-how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets](https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets)
  ↳ *part-of* `g04-0131`
  ↳ *leads-to* `g04-0135`

- `g04-0135` *STATED* — Step 3 after claiming the monthly API credits: start building on the Claude API (body locked).
  — [g-how-to-claim-your-monthly-claude-credits-on-max-and-team-plans](https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans) [g-how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets](https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets)
  ↳ *part-of* `g04-0131`

- `g04-0207` *STATED* — The early-compaction setting is one line added to the helper agent's own file (section 'Step 2: add the line to the helper's file', body locked).
  — [g-make-your-claude-helper-agents-compact-their-own-chat-early](https://chen.media/guides/make-your-claude-helper-agents-compact-their-own-chat-early)
  ↳ *part-of* `g04-0204`

- `g04-0208` *STATED* — Alex's guide gives a specific number to use for the subagent compaction threshold (body locked).
  > “the number to use”
  — [g-make-your-claude-helper-agents-compact-their-own-chat-early](https://chen.media/guides/make-your-claude-helper-agents-compact-their-own-chat-early)
  ↳ *part-of* `g04-0207`

- `g04-0232` *STATED* — Alex's advisor setup puts a cheaper main model (Sonnet) in the driver's seat and calls Opus only at the hard moments.
  > “put a cheaper main model in the driver's seat and call Opus only at the hard moments”
  — [g-let-opus-advise-while-sonnet-does-the-routine-work](https://chen.media/guides/let-opus-advise-while-sonnet-does-the-routine-work)
  ↳ *example-of* `g04-0231`

- `g04-0251` *INFERRED* — Alex's token-saving toolkit across these guides: read the /usage habit warnings, itemise spend with tokentab, filter test output with a PreToolUse hook, make subagents compact early, and let Sonnet drive with Opus as advisor.
  — [g-the-four-habits-eating-your-claude-limit-and-the-fix-for-each](https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each) [g-tokentab-see-where-every-claude-token-goes-as-a-monthly-statement](https://chen.media/guides/tokentab-see-where-every-claude-token-goes-as-a-monthly-statement) [g-the-claude-hook-that-cuts-test-output-down-to-just-the-failures](https://chen.media/guides/the-claude-hook-that-cuts-test-output-down-to-just-the-failures) [g-make-your-claude-helper-agents-compact-their-own-chat-early](https://chen.media/guides/make-your-claude-helper-agents-compact-their-own-chat-early) [g-let-opus-advise-while-sonnet-does-the-routine-work](https://chen.media/guides/let-opus-advise-while-sonnet-does-the-routine-work)
  ↳ *generalizes* `g04-0003`
  ↳ *generalizes* `g04-0071`
  ↳ *generalizes* `g04-0087`
  ↳ *generalizes* `g04-0204`
  ↳ *generalizes* `g04-0240`

- `g05-0099` *STATED* — Effortless reads each prompt with Haiku 5.5 and picks the reasoning effort for it.
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless)
  ↳ *part-of* `g05-0098`
  ↳ *depends-on* `g05-0180`

- `g05-0106` *STATED* — In Effortless setup, keep Haiku on its own: one click, no key, and it runs on your own Claude login.
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless)
  ↳ *part-of* `g05-0105`
  ↳ *example-of* `g05-0314`

- `g05-0149` *STATED* — Cache rule 1: pick your model and effort level at the top of a session.
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)
  ↳ *part-of* `g05-0157`
  ↳ *example-of* `g05-0316`

- `g05-0151` *STATED* — Cache rule 2: do not run /model in the middle of a task.
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)
  ↳ *part-of* `g05-0157`
  ↳ *because* `g05-0144`

- `g05-0153` *STATED* — Cache rule 3: save /compact for natural breaks between tasks, not the middle of one.
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)
  ↳ *part-of* `g05-0157`
  ↳ *qualifies* `g19-0003`

- `g05-0155` *STATED* — Cache rule 4: check your cache with /usage.
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)
  ↳ *part-of* `g05-0157`
  ↳ *part-of* `g03-0073`

- `g05-0161` *STATED* — Give each Claude Code subagent its own effort level so small jobs stop burning your limit on thinking.
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)
  ↳ *because* `g05-0166`

- `g05-0174` *CORE* — Keep max effort for hard problems: security reviews, tricky bugs, big refactors.
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)
  ↳ *part-of* `g05-0161`
  ↳ *qualifies* `g05-0164` — max is worth it only for hard problems
  ↳ *evidence-for* `y01-0150`

- `g05-0198` *STATED* — After 'You've hit your session limit' or 'weekly limit', /model changes nothing; wait for the reset time shown in the message.
  — [g-three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha](https://chen.media/guides/three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha)
  ↳ *because* `g05-0197`

- `g05-0201` *STATED* — Pick your model at the start of a task.
  — [g-three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha](https://chen.media/guides/three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha)
  ↳ *because* `g05-0200`
  ↳ *example-of* `g05-0316`

- `g05-0316` *CORE* — Choose model (and effort) at the start of a task and don't change them mid-task.
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup) [g-three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha](https://chen.media/guides/three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha)
  ↳ *because* `g05-0315`

- `g06-0064` *STATED* — Run /autocompact 200k in Claude Code and Claude summarizes the conversation once it reaches about 200,000 tokens.
  — [g-make-claude-compact-earlier-the-setting-and-the-claude-md-note](https://chen.media/guides/make-claude-compact-earlier-the-setting-and-the-claude-md-note)
  ↳ *part-of* `g06-0063`
  ↳ *leads-to* `g06-0073`

- `g06-0066` *STATED* — To return Claude Code to its default compaction point, run: /autocompact auto
  — [g-make-claude-compact-earlier-the-setting-and-the-claude-md-note](https://chen.media/guides/make-claude-compact-earlier-the-setting-and-the-claude-md-note)
  ↳ *contrast* `g06-0064`

- `g06-0091` *STATED* — Swarm control 1: use a smaller model for easy workflow stages.
  — [g-run-claude-agent-swarms-without-burning-your-limit](https://chen.media/guides/run-claude-agent-swarms-without-burning-your-limit)
  ↳ *because* `g06-0087`
  ↳ *part-of* `g06-0095`
  ↳ *example-of* `g06-0264`
  ↳ *example-of* `y02-0187`

- `g06-0092` *STATED* — Swarm control 2: set the workflow size to small.
  — [g-run-claude-agent-swarms-without-burning-your-limit](https://chen.media/guides/run-claude-agent-swarms-without-burning-your-limit)
  ↳ *part-of* `g06-0095`

- `g06-0093` *STATED* — Swarm control 3 (new): one model for every workflow agent; Alex says it is the one new setting to test before you trust it.
  — [g-run-claude-agent-swarms-without-burning-your-limit](https://chen.media/guides/run-claude-agent-swarms-without-burning-your-limit)
  ↳ *part-of* `g06-0095`
  ↳ *contrast* `g06-0087`

- `g06-0111` *STATED* — magpie step 3 keeps Claude Code going when a quota runs out by failing over to your next account.
  — [g-keep-claude-code-working-after-your-limit-runs-out](https://chen.media/guides/keep-claude-code-working-after-your-limit-runs-out)
  ↳ *part-of* `g06-0105`
  ↳ *evidence-for* `g15-0070`

- `g06-0207` *STATED* — To claim monthly API credits: on claude.ai go to Settings > Billing (Team: Organization settings > Billing).
  — [g-this-week-in-claude-ranked-by-what-it-does-for-you](https://chen.media/guides/this-week-in-claude-ranked-by-what-it-does-for-you)
  ↳ *part-of* `g06-0202`
  ↳ *leads-to* `g06-0208`
  ↳ *evidence-for* `g04-0132`

- `g06-0208` *STATED* — To claim monthly API credits, under API credits choose Link organization and pick or create a Claude Console organization.
  — [g-this-week-in-claude-ranked-by-what-it-does-for-you](https://chen.media/guides/this-week-in-claude-ranked-by-what-it-does-for-you)
  ↳ *leads-to* `g06-0209`
  ↳ *evidence-for* `g04-0134`

- `g06-0209` *STATED* — To finish claiming monthly API credits, review the Supplemental Credit Terms and link the Claude Console organization.
  — [g-this-week-in-claude-ranked-by-what-it-does-for-you](https://chen.media/guides/this-week-in-claude-ranked-by-what-it-does-for-you)

- `g06-0228` *STATED* — After making the helper file, you tell Claude when to use haiku-helper (wording in the gated 'Step 2: tell Claude when to use it').
  — [g-make-your-claude-limit-last-the-haiku-helper-and-3-habits](https://chen.media/guides/make-your-claude-limit-last-the-haiku-helper-and-3-habits)
  ↳ *part-of* `g06-0230`

- `g06-0229` *STATED* — The Haiku-helper guide adds three limit-saving habits taken from Anthropic's cost page (gated 'Step 3: three habits from Anthropic's cost page').
  — [g-make-your-claude-limit-last-the-haiku-helper-and-3-habits](https://chen.media/guides/make-your-claude-limit-last-the-haiku-helper-and-3-habits)
  ↳ *part-of* `g06-0230`

- `g06-0237` *STATED* — The Haiku 5.5 guide's fix is one helper file that makes Claude hand easy jobs to Haiku, plus a prompt that sets it up and a step telling Claude when to use it.
  — [g-send-claude-s-easy-jobs-to-haiku-5-5-with-one-helper-file](https://chen.media/guides/send-claude-s-easy-jobs-to-haiku-5-5-with-one-helper-file)
  ↳ *because* `g06-0232`
  ↳ *depends-on* `g06-0224` — same helper file
  ↳ *example-of* `y02-0187`

- `g07-0099` *STATED* — Switching to Haiku 5.5 is a one-line change ('Step 1: switch in one line'; the line is email-gated).
  — [g-set-up-claude-haiku-5-5-10x-cheaper-claude-model](https://chen.media/guides/set-up-claude-haiku-5-5-10x-cheaper-claude-model)
  ↳ *part-of* `g07-0090`

- `g07-0108` *STATED* — The Haiku helper skill sorts the work: easy jobs go to a Haiku 5.5 helper, and Opus only does the thinking.
  — [g-make-claude-code-limit-last-longer-haiku-5-5-helper](https://chen.media/guides/make-claude-code-limit-last-longer-haiku-5-5-helper)
  ↳ *part-of* `g07-0104`

- `g07-0216` *STATED* — Step 1 to use the API credits: claim them on claude.ai (exact clicks email-gated).
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *part-of* `g07-0203`
  ↳ *leads-to* `g07-0217`

- `g07-0217` *STATED* — Step 2 to use the API credits: find your credits and make an API key (email-gated).
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *part-of* `g07-0203`
  ↳ *leads-to* `g07-0218`

- `g07-0220` *STATED* — Alex's credits guide explains how to make the API credits go further ('Make them go further'; email-gated).
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *part-of* `g07-0203`

- `g09-0142` *STATED* — After running /skill-doctor, turn off the skills you never use.
  — [g-find-the-claude-skills-eating-your-limit-skill-doctor](https://chen.media/guides/find-the-claude-skills-eating-your-limit-skill-doctor)
  ↳ *evidence-for* `y02-0129`

- `g09-0143` *STATED* — Make /skill-doctor a habit: rerun it periodically rather than once.
  — [g-find-the-claude-skills-eating-your-limit-skill-doctor](https://chen.media/guides/find-the-claude-skills-eating-your-limit-skill-doctor)
  ↳ *qualifies* `g09-0142`

- `g12-0023` *STATED* — Guide section 'The cheat sheet' maps each kind of task to Sonnet 5.5 or Opus 5.5 (body email-gated).
  — [g-claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task](https://chen.media/guides/claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task)
  ↳ *part-of* `g12-0001`

- `g12-0025` *STATED* — Guide section 'Make your usage limit last longer' treats model choice as a lever for stretching the Claude usage limit (body email-gated).
  — [g-claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task](https://chen.media/guides/claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task)
  ↳ *part-of* `g12-0001`
  ↳ *part-of* `g12-0003`

- `g12-0026` *INFERRED* — Routing rule distilled from the Sonnet/Opus cheat sheet: default to Sonnet 5.5 for well-scoped everyday coding, bug fixes and documents, and escalate to Opus 5.5 only for the hardest judgment-heavy problems, halving per-token cost on most work.
  — [g-claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task](https://chen.media/guides/claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task)
  ↳ *generalizes* `g12-0023`
  ↳ *depends-on* `g12-0021`
  ↳ *depends-on* `g12-0022`
  ↳ *enables* `g12-0003`
  ↳ *evidence-for* `y02-0187`

- `g12-0125` *STATED* — Guide section 'Price your own usage' runs the free API-pricing tool on your own Claude Code history (body email-gated).
  — [g-what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything)
  ↳ *part-of* `g12-0111`
  ↳ *depends-on* `g12-0112`

- `g12-0126` *STATED* — Guide section 'The three habits' gives three habits that stop Claude re-reading everything (body email-gated).
  — [g-what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything)
  ↳ *part-of* `g12-0111`
  ↳ *enables* `g12-0118`

- `g12-0127` *STATED* — Guide section 'Check that it's working' verifies the habits are cutting re-read tokens (body email-gated).
  — [g-what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything)
  ↳ *part-of* `g12-0111`
  ↳ *qualifies* `g12-0126`

- `g12-0128` *INFERRED* — Since every turn re-sends the whole session, the biggest re-reading lever is short sessions: start fresh (/clear or a new session) per task instead of keeping one session open all day.
  — [g-what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything)
  ↳ *depends-on* `g12-0121`
  ↳ *part-of* `g12-0126` — inferred; actual habits are email-gated
  ↳ *evidence-for* `y01-0030`
  ↳ *depends-on* `g19-0021`

- `g12-0178` *CORE* — Fast-Jev Compaction replaces the /compact summary: it never rewrites anything, makes room by deleting old tool calls and tool results that are no longer needed, and hands Claude back the original messages.
  — [g-stop-claude-code-s-compact-from-summarizing-away-your-chat](https://chen.media/guides/stop-claude-code-s-compact-from-summarizing-away-your-chat)
  ↳ *part-of* `g12-0172`
  ↳ *contrast* `g12-0175`

- `g13-0116` *STATED* — Alex's credit guide has a section 'Use it after you hit your limit' on switching to cloud sessions once your local usage limit runs out.
  — [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)
  ↳ *part-of* `g13-0098`

- `g13-0117` *STATED* — Alex's credit guide has a section 'Make it last until November 4' on pacing the cloud credit before it expires.
  — [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)
  ↳ *depends-on* `g13-0103`

- `g13-0179` *CORE* — Let Jev make the small calls and spend Claude on the work that needs it.
  > “Let Jev make the small calls and spend Claude on the work that needs it.”
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *depends-on* `g13-0175`

- `g13-0186` *STATED* — Workflow 1 from Alex's JEV video: route every task, letting Jev decide which model handles it.
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *part-of* `g13-0184`
  ↳ *example-of* `g13-0177`
  ↳ *example-of* `y02-0187`

- `g13-0239` *STATED* — Darwin Loop guide section: 'Keep the token budget bounded'.
  — [g-darwin-loop-evolve-the-winner](https://chen.media/guides/darwin-loop-evolve-the-winner)
  ↳ *part-of* `g13-0236`

- `g13-0248` *STATED* — Get a basic draft before paying for multiple review passes.
  > “Get a basic draft before paying for multiple review passes.”
  — [g-swarm-loop-three-reviewers-guide](https://chen.media/guides/swarm-loop-three-reviewers-guide)
  ↳ *qualifies* `g13-0242`

- `g13-0253` *STATED* — SWARM Loop guide section 'Keep the loop worth its cost': the review loop is bounded.
  — [g-swarm-loop-three-reviewers-guide](https://chen.media/guides/swarm-loop-three-reviewers-guide)
  ↳ *generalizes* `g13-0248`

- `g13-0305` *CORE* — Alex's loop guides treat usage as a budget: draft once first, bound the number of passes, and make extra agents optional because each adds usage cost.
  — [g-darwin-loop-evolve-the-winner](https://chen.media/guides/darwin-loop-evolve-the-winner) [g-swarm-loop-three-reviewers-guide](https://chen.media/guides/swarm-loop-three-reviewers-guide) [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *generalizes* `g13-0236`
  ↳ *generalizes* `g13-0248`
  ↳ *generalizes* `g13-0230`
  ↳ *generalizes* `g13-0179`
  ↳ *generalizes* `g13-0253`

- `g14-0068` *STATED* — Try Headroom on a representative task before trusting its savings.
  > “Try Headroom on a representative task”
  — [g-headroom-claude-hud-aisa-setup](https://chen.media/guides/headroom-claude-hud-aisa-setup)
  ↳ *part-of* `g14-0056`
  ↳ *qualifies* `g14-0057`
  ↳ *evidence-for* `g17-0125`

- `g14-0132` *STATED* — AWS credits step 1: open aws.amazon.com/free and choose Create a free account.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *part-of* `g14-0129`

- `g14-0133` *STATED* — Review the AWS Free and Paid plan choices before continuing the sign-up.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *part-of* `g14-0132`

- `g14-0135` *STATED* — AWS credits step 2: in the AWS console, check the Cost and Usage widget and the Billing and Cost Management credit details.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *part-of* `g14-0129`

- `g14-0136` *STATED* — Confirm the AWS credit balance, expiration date and eligible services in your own account.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *part-of* `g14-0135`

- `g14-0144` *STATED* — For the first Bedrock test, enter a short prompt, keep the output limit small, and submit it.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *leads-to* `g14-0139`

- `g14-0146` *STATED* — After a Bedrock test call, confirm a response, then inspect your usage and credit balance.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *leads-to* `g14-0144`

- `g14-0148` *STATED* — Earn the remaining AWS credits from the Explore AWS widget on Console Home, which lists the activities available to your account worth up to another $100.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *part-of* `g14-0129`

- `g14-0151` *STATED* — Keep the AWS experiment under control: set an AWS Budget alert, check usage after testing, and remove resources created for other credit activities.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *part-of* `g14-0129`

- `g14-0153` *STATED* — Verify the remaining AWS credit balance rather than assuming every model call is covered.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *part-of* `g14-0151`

- `g14-0155` *STATED* — On Bedrock, choose the specific model shown in your catalog.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *depends-on* `g14-0154`

- `g14-0158` *STATED* — Check the Bedrock access screen, applicable terms and pricing before running a larger job.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *because* `g14-0157`

- `g14-0161` *STATED* — Bedrock quota error fix: inspect Service Quotas or contact AWS Support.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *contrast* `g14-0142`

- `g14-0162` *STATED* — If you have a Bedrock credit question, stop the experiment and check Billing and the offer terms before continuing.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *part-of* `g14-0153`

- `g14-0179` *STATED* — Start a local model with a short conversation and a modest context setting.
  — [g-spark-x-local-ai-setup-guide](https://chen.media/guides/spark-x-local-ai-setup-guide)
  ↳ *because* `g14-0177`

- `g14-0263` *STATED* — Read the outcome of a small Claude Octopus run before running a bigger job.
  > “Read the outcome before running a bigger job”
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *part-of* `g14-0241`
  ↳ *example-of* `g14-0349`
  ↳ *evidence-for* `g17-0125`

- `g15-0023` *STATED* — Measure the MarkItDown token saving on your own documents (about two minutes) instead of taking Alex Chen's number for it.
  — [g-why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix](https://chen.media/guides/why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix)
  ↳ *part-of* `g15-0016`
  ↳ *qualifies* `g15-0013` — measure your own number instead of trusting 70k
  ↳ *evidence-for* `g17-0125`

- `g15-0064` *STATED* — Use anydoc to feed Claude office files without breaking them.
  — [g-four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute](https://chen.media/guides/four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute)
  ↳ *part-of* `g15-0180`

- `g15-0172` *STATED* — A two-phase order stops a boss loop eating your whole token budget (section 'The cost, and the order that fixes it', locked).
  — [g-the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer](https://chen.media/guides/the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer)

- `g15-0180` *CORE* — Convert PDFs and office files to clean Markdown (Microsoft MarkItDown or firecrawl/anydoc) before giving them to Claude, so you stop paying tokens for layout and structure on every message.
  — [g-why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix](https://chen.media/guides/why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix) [g-four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute](https://chen.media/guides/four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute)

- `g16-0054` *STATED* — Install the three cost repos one per lever, in the order that pays back fastest.
  > “one repo per lever, in the order that pays back fastest”
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you)
  ↳ *part-of* `g16-0039`
  ↳ *example-of* `g16-0007`

- `g16-0085` *STATED* — Keep the notes where they are and hand Claude an ADDRESS instead of the contents.
  > “Keep the notes where they are, and hand over an ADDRESS instead of the contents.”
  — [g-the-one-page-that-points-claude-at-the-right-notes](https://chen.media/guides/the-one-page-that-points-claude-at-the-right-notes)
  ↳ *defines* `g16-0084`
  ↳ *example-of* `g16-0009`
  ↳ *generalizes* `g16-0115`
  ↳ *generalizes* `g16-0179`
  ↳ *evidence-for* `g18-0184`

- `g16-0123` *STATED* — His 15-mistakes guide ends with a five minute pass you can run over your setup.
  > “The five minute pass”
  — [g-15-claude-mistakes-that-are-quietly-costing-you-tokens](https://chen.media/guides/15-claude-mistakes-that-are-quietly-costing-you-tokens)
  ↳ *part-of* `g16-0099`

- `g16-0176` *STATED* — Tip 1 (beginner): stop sending simple work to the biggest model.
  > “1. Stop sending simple work to the biggest model”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *part-of* `g16-0175`
  ↳ *example-of* `g16-0013`
  ↳ *evidence-for* `y02-0187`

- `g16-0179` *STATED* — Tip 4 (beginner): search your own chat history instead of pasting it back in.
  > “4. Search your own history instead of pasting it back in”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *part-of* `g16-0175`

- `g17-0120` *STATED* — The fix for a coding agent's token bill is compressing the material before it leaves your machine.
  > “It is compressing the material before it leaves your machine.”
  — [g-cut-what-your-coding-agent-sends-to-the-model](https://chen.media/guides/cut-what-your-coding-agent-sends-to-the-model)
  ↳ *enables* `g17-0113`
  ↳ *qualifies* `g17-0114` — attacks the repetition

- `g17-0124` *STATED* — There are four ways to run the context-compression tool.
  > “The four ways to run it”
  — [g-cut-what-your-coding-agent-sends-to-the-model](https://chen.media/guides/cut-what-your-coding-agent-sends-to-the-model)
  ↳ *part-of* `g17-0121`

- `g17-0125` *CORE* — Evaluate context compression on your own work in one afternoon before adopting it.
  > “How to evaluate it on your own work in one afternoon”
  — [g-cut-what-your-coding-agent-sends-to-the-model](https://chen.media/guides/cut-what-your-coding-agent-sends-to-the-model)
  ↳ *qualifies* `g17-0120`

- `g17-0313` *INFERRED* — Alex Chen's zero-cost pattern: stack free tiers and bring-your-own-key tools (FreeLLMAPI, Open Generative AI, Arena, Google AI Studio) instead of paying for subscriptions.
  — [g-400-ai-image-and-video-models-in-one-free-desktop-app](https://chen.media/guides/400-ai-image-and-video-models-in-one-free-desktop-app) [g-pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint](https://chen.media/guides/pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint) [g-three-free-ai-sites-for-chat-video-and-images](https://chen.media/guides/three-free-ai-sites-for-chat-video-and-images) [g-ten-ai-tools-people-pay-for-and-the-free-version-of-each](https://chen.media/guides/ten-ai-tools-people-pay-for-and-the-free-version-of-each)

- `g18-0112` *STATED* — Install ONE of the four MCP servers tonight, not all four.
  > “Install ONE of these tonight, not all four.”
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again)
  ↳ *because* `g18-0113`
  ↳ *qualifies* `g18-0111`
  ↳ *example-of* `g18-0285`

- `g18-0184` *STATED* — Next session, instead of re-pasting your whole history, Claude reads back only the part of the NotebookLM memory it needs.
  — [g-give-claude-a-memory-that-survives-the-chat-window](https://chen.media/guides/give-claude-a-memory-that-survives-the-chat-window)
  ↳ *part-of* `g18-0183`
  ↳ *contrast* `g18-0182`

- `g18-0224` *STATED* — Pick a free LLM provider before you pick a model.
  — [g-134-free-llm-apis-and-how-to-point-your-editor-at-them](https://chen.media/guides/134-free-llm-apis-and-how-to-point-your-editor-at-them)
  ↳ *part-of* `g18-0225`

- `g18-0248` *STATED* — CUT 'Always explain your reasoning' from your setup: the model already reasons, so the line only pads your output.
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *part-of* `g18-0245`
  ↳ *contrast* `g18-0268` — both cut padded output
  ↳ *example-of* `g12-0103`
  ↳ *evidence-for* `g03-0099`

- `g18-0250` *STATED* — CUT skills you installed and never used: every one is context you pay for on every request.
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *part-of* `g18-0245`
  ↳ *example-of* `g18-0283`
  ↳ *evidence-for* `y02-0126`

- `g18-0251` *STATED* — CUT MCP servers for tools you dropped: dead connections still load their tool schemas.
  — [g-what-to-cut-from-your-claude-setup-and-what-to-keep](https://chen.media/guides/what-to-cut-from-your-claude-setup-and-what-to-keep)
  ↳ *evidence-for* `g18-0113` — dead MCP connections still load tool schemas
  ↳ *part-of* `g18-0245`

- `g19-0003` *STATED* — /compact makes Claude Code summarise the conversation so far and continue from that summary; it is one of the three Tier 1 usage-limit fixes from Alex's video.
  > “/compact summarise and continue”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *part-of* `g19-0002`
  ↳ *example-of* `g19-0020`

- `g19-0004` *STATED* — /compact takes focus instructions, e.g. '/compact focus on the auth', to steer what the summary keeps.
  > “/compact focus on the auth steer what the summary keeps”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *part-of* `g19-0002`
  ↳ *qualifies* `g19-0003` — focus instructions steer /compact

- `g19-0005` *STATED* — /model opusplan sets Claude Code so Opus does the planning and Sonnet does the building.
  > “/model opusplan Opus plans, Sonnet builds”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *part-of* `g19-0002`
  ↳ *example-of* `g19-0011`

- `g19-0006` *STATED* — /model sonnet switches Claude Code to Sonnet for everything.
  > “/model sonnet Sonnet for everything”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *part-of* `g19-0002`
  ↳ *example-of* `g19-0011`

- `g19-0007` *STATED* — Running /model in Claude Code shows which models are available to switch to.
  > “/model see what is available”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *part-of* `g19-0002`
  ↳ *enables* `g19-0005`

- `g19-0009` *STATED* — /context shows what is in Claude Code's context window right now.
  > “/context what is in the window right now”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *part-of* `g19-0008`
  ↳ *enables* `g19-0020` — see what you are dragging

- `g19-0010` *STATED* — /cost shows what the current Claude Code session has spent.
  > “/cost what this session has spent”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *part-of* `g19-0008`
  ↳ *evidence-for* `g19-0019`
  ↳ *qualifies* `g03-0076` — 28-ways guide: /cost shows session spend; /usage guide: /cost and /stats open the same /usage screen

- `g19-0015` *STATED* — The usage-limits guide ends with a shortlist titled 'If you only do three things'.
  > “If you only do three things”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *part-of* `g19-0001`

- `g19-0020` *STATED* — Almost every one of the 28 usage-limit tips is a way of dragging less context behind each message.
  > “Almost everything below is a way of dragging less.”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *part-of* `g19-0001`
  ↳ *because* `g19-0019`

- `g19-0168` *STATED* — Install and run Claude Code Router with: npm install -g @musistudio/claude-code-router, then ccr ui.
  > “npm install -g @musistudio/claude-code-router
ccr ui”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *part-of* `g19-0156`

- `g20-0004` *STATED* — If your Claude plan has extended thinking, turn it on for simulation steps 2 (play it out) and 4 (root cause and the one change) only.
  > “If your plan has extended thinking, turn it on for steps 2 and 4.”
  — [g-run-your-idea-as-a-simulation-and-find-what-breaks-it](https://chen.media/guides/run-your-idea-as-a-simulation-and-find-what-breaks-it)
  ↳ *part-of* `g20-0001`
  ↳ *qualifies* `g20-0006`
  ↳ *qualifies* `g20-0008`

- `g20-0084` *STATED* — On the Claude free plan, build one carousel deck per sitting.
  > “On free, build one deck per sitting.”
  — [g-the-one-prompt-that-makes-claude-design-real-carousels](https://chen.media/guides/the-one-prompt-that-makes-claude-design-real-carousels)

- `g20-0163` *STATED* — Memory Part 4 is 'The cheap model swap', routing work to a cheaper model.
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0141`
  ↳ *leads-to* `g20-0164`
  ↳ *example-of* `g20-0287`

- `g20-0211` *STATED* — Dev agent 2, the Coder, uses a cheaper model.
  > “The Coder (use a cheaper model)”
  — [g-four-claude-agents-that-work-like-a-dev-team](https://chen.media/guides/four-claude-agents-that-work-like-a-dev-team)
  ↳ *part-of* `g20-0198`
  ↳ *leads-to* `g20-0212`
  ↳ *example-of* `g20-0287`
  ↳ *example-of* `g21-0121`

- `g21-0091` *STATED* — Move 8 of the nine Fable 5 prompts: the effort dial.
  — [g-nine-prompts-worth-stealing-from-anthropic-s-own-guide](https://chen.media/guides/nine-prompts-worth-stealing-from-anthropic-s-own-guide)
  ↳ *part-of* `g21-0079`
  ↳ *example-of* `g21-0168` — effort dial = fix 4

- `g21-0121` *CORE* — Plan once with the expensive brain (Fable 5), then let cheap models (Sonnet, Haiku) 'cash the checks' for a long time.
  > “You plan once tonight with the expensive brain, then cheap models cash the checks for a long time.”
  — [g-turn-your-whole-backlog-into-finished-plans-in-one-night](https://chen.media/guides/turn-your-whole-backlog-into-finished-plans-in-one-night)
  ↳ *example-of* `g21-0158`

- `g21-0122` *STATED* — The backlog-to-blueprints system has three pieces: the mining prompt, the blueprint template, and the batch loop.
  — [g-turn-your-whole-backlog-into-finished-plans-in-one-night](https://chen.media/guides/turn-your-whole-backlog-into-finished-plans-in-one-night)
  ↳ *part-of* `g21-0117`

- `g21-0124` *STATED* — Backlog run order: paste the MINING PROMPT, then paste the TEMPLATE right after it, answer the questions it asks, then paste the BATCH LOOP; go to sleep and wake up to a vault of blueprints.
  — [g-turn-your-whole-backlog-into-finished-plans-in-one-night](https://chen.media/guides/turn-your-whole-backlog-into-finished-plans-in-one-night)
  ↳ *part-of* `g21-0123`
  ↳ *depends-on* `g21-0122`

- `g21-0149` *STATED* — Mining step 4: address each blueprint to the model that will build it, opening with one line such as 'BUILDER: Claude Sonnet, working alone, cold start, cannot ask questions.'
  > “BUILDER: Claude Sonnet, working alone, cold start, cannot ask questions.”
  — [g-turn-your-whole-backlog-into-finished-plans-in-one-night](https://chen.media/guides/turn-your-whole-backlog-into-finished-plans-in-one-night)
  ↳ *part-of* `g21-0125`

- `g21-0150` *STATED* — The planner uses Haiku for the simple blueprints, choosing per item and stating which model and why in one line.
  — [g-turn-your-whole-backlog-into-finished-plans-in-one-night](https://chen.media/guides/turn-your-whole-backlog-into-finished-plans-in-one-night)
  ↳ *qualifies* `g21-0149`

- `g21-0168` *CORE* — Fable 5 fix 4: turn the effort dial to match the task, instead of paying full price for everything.
  > “Turn the effort dial to match the task, instead of paying full price for everything.”
  — [g-the-fable-5-guide-effort-memory-and-self-verification](https://chen.media/guides/the-fable-5-guide-effort-memory-and-self-verification)
  ↳ *part-of* `g21-0164`
  ↳ *contrast* `g21-0162` — fix for token overspend
  ↳ *evidence-for* `g10-0197`

- `g21-0195` *STATED* — Sol workflow 2, the cost stack: let GPT-5.6 Sol PLAN, then hand the grunt work to Luna (about 5x cheaper) to EXECUTE.
  > “let Sol PLAN, then hand the grunt work to Luna (about 5x cheaper) to EXECUTE”
  — [g-three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team](https://chen.media/guides/three-workflows-that-turn-gpt-5-6-sol-into-a-whole-team)
  ↳ *part-of* `g21-0193`
  ↳ *example-of* `g21-0158`
  ↳ *evidence-for* `g22-0052`

- `g22-0009` *STATED* — Judgment Vault step 4 ('Wire the cheap-model harness'): wire a harness so any cheap model loads the vault file before it decides anything.
  — [g-bank-the-judgment-calls-not-just-the-output](https://chen.media/guides/bank-the-judgment-calls-not-just-the-output)
  ↳ *part-of* `g22-0003`

- `g22-0015` *STATED* — Judgment Vault upkeep: every month after, a cheap model re-runs the maintenance loop on the vault, for pennies.
  — [g-bank-the-judgment-calls-not-just-the-output](https://chen.media/guides/bank-the-judgment-calls-not-just-the-output)
  ↳ *part-of* `g22-0016`
  ↳ *example-of* `g22-0279`

- `g22-0061` *STATED* — Model-line rule of thumb: Sol touches the batch TWICE and only twice, once to write the spec and once to inspect it.
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)
  ↳ *part-of* `g22-0048`
  ↳ *because* `g22-0063`
  ↳ *example-of* `g22-0282`

- `g23-0012` *STATED* — Clone Fable 5's brain into the cheaper models before the free window closes, using three prompts: the audit prompt, the skill-file conversion, and the instructions file.
  — [g-clone-the-smart-model-s-brain-into-the-cheap-one](https://chen.media/guides/clone-the-smart-model-s-brain-into-the-cheap-one)
  ↳ *because* `g23-0014`
  ↳ *because* `g23-0015`
  ↳ *leads-to* `g23-0013`

- `g23-0016` *STATED* — Before Fable 5 goes pay per token, make it write its understanding of how you work DOWN into files.
  > “make it write that understanding DOWN”
  — [g-clone-the-smart-model-s-brain-into-the-cheap-one](https://chen.media/guides/clone-the-smart-model-s-brain-into-the-cheap-one)
  ↳ *part-of* `g23-0012`
  ↳ *because* `g23-0017`

- `g23-0018` *STATED* — Cloning Fable 5's brain takes one evening and three prompts, run in order.
  > “One evening, three prompts, in order.”
  — [g-clone-the-smart-model-s-brain-into-the-cheap-one](https://chen.media/guides/clone-the-smart-model-s-brain-into-the-cheap-one)
  ↳ *qualifies* `g23-0012`

- `g23-0131` *STATED* — Paste the retirement prompts one at a time and keep it all in the same chat so Claude remembers your numbers.
  — [g-three-numbers-you-know-one-chat-your-retirement-year](https://chen.media/guides/three-numbers-you-know-one-chat-your-retirement-year)
  ↳ *qualifies* `g23-0128`
  ↳ *enables* `g23-0144`

- `r01-0109` *STATED* — Before starting, the /agency night shift tells the user their computer must stay on and awake and that every job uses their Claude plan.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0048`
  ↳ *depends-on* `r01-0060`

- `r01-0179` *STATED* — /court flag '--quick' seats 6 jurors.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *qualifies* `r01-0178`

- `r01-0183` *STATED* — Every /court sub-agent counts toward your Claude plan's usage, so start with --quick if you are near your limit.
  > “start with `--quick` if you are near your limit”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0017`

- `r01-0184` *STATED* — Alex's tip in PROMPTS.md: short on usage? Add --quick for a jury of 6.
  > “Short on usage? Add `--quick` for a jury of 6.”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0183`

- `r01-0212` *CORE* — /court step 1: run 'COURT plan' with the same flags and tell the user in one line how big the trial is, e.g. '12 jurors, 17 sub-agent calls', then start.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0187`
  ↳ *example-of* `r01-0017` — disclose call count before starting

- `r01-0213` *STATED* — If /court fired on its own (the user never asked for a trial), it asks once first and offers --quick.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *qualifies* `r01-0204` — auto-invocation asks first
  ↳ *depends-on* `r01-0179`

- `r02-0145` *STATED* — `/launch --quick` polls only the first five stations: TESTS, SECURITY, DATABASE, SPEED and COST.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0143`
  ↳ *qualifies* `r02-0149` — 6 instead of 9 calls
  ↳ *evidence-for* `r01-0179`

- `r02-0147` *STATED* — `/launch --recheck` polls only the stations that said NO-GO last time, after you fixed things.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0143`
  ↳ *qualifies* `r02-0150` — reruns only failed stations

- `r02-0174` *STATED* — /launch step 1 (size it): run `LAUNCH plan` with the same flags and tell the user in one line how big the poll is, e.g. "8 stations + 1 flight director, 9 sub-agent calls", then start.
  > “8 stations + 1 flight director, 9 sub-agent calls”
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0171`
  ↳ *depends-on* `r02-0149`
  ↳ *evidence-for* `r01-0212`

- `r03-0081` *STATED* — /learn review step 1: if the inbox is empty, write no note, say 'Nothing to review.' and stop.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0080`

- `r04-0246` *STATED* — /shark Step 1, size it: run SHARK plan with the same flags and tell the user in one line how big the session is (e.g. '5 investors, 11 sub-agent calls'), then start.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0224`
  ↳ *example-of* `r04-0016`
  ↳ *evidence-for* `r01-0212`

- `y01-0018` *CORE* — Start with the default effort and raise it only when the problem needs much deeper reasoning, rather than assuming every task needs the highest setting.
  > “typically, start with a default effort and raise it only when the problem needs a lot deeper reasoning, rather than assuming every task needs the highest setting.”
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *because* `y01-0016`
  ↳ *evidence-for* `y01-0149` — effort is a cost lever in both tools

- `y01-0021` *STATED* — Leave Codex fast mode off unless a faster response is worth spending the extra usage allowance.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *because* `y01-0019`

- `y01-0023` *STATED* — The Codex /status command shows information about the current chat and your usage, so you can see your current limits.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *analogy-for* `g03-0076`
  ↳ *enables* `y01-0017` — see where you stand against the limit

- `y01-0028` *STATED* — Inside a Codex project, use separate chats for separate jobs - e.g. one chat about your website and another about a presentation.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *evidence-for* `g16-0119`
  ↳ *part-of* `y01-0024`

- `y01-0029` *STATED* — Keep related follow-up requests in the same chat so the agent can use the earlier discussion.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *qualifies* `y01-0028`

- `y01-0030` *CORE* — Start a new chat when you move to a different job that doesn't need the previous conversation's context.
  > “Start a new chat when you're moving to a different job that doesn't need that conversation context.”
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *contrast* `y01-0029`
  ↳ *depends-on* `y01-0031`

- `y01-0138` *CORE* — Sonnet is 'your reliable worker' and daily workhorse - start 90% of your tasks there; it handles most writing and coding.
  > “Sonnet is your reliable worker, so start 90% of your tasks here.”
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *example-of* `y01-0136`

- `y01-0139` *STATED* — Opus is 'your expert': save it for harder coding tasks or big choices where you need the smartest brain in the room.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *example-of* `y01-0136`
  ↳ *contrast* `y01-0140`

- `y01-0149` *STATED* — Don't waste max effort on basic summaries or simple reformatting.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *because* `y01-0148`

- `y01-0150` *STATED* — Save max effort for complicated problems, hard coding tasks, or situations where getting it wrong can cost real time and money.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *because* `y01-0147`

- `y02-0022` *STATED* — Routing split in Alex Chen's limit skill: searching files, reading logs and small edits go to Haiku; only the hard thinking goes to Opus.
  > “searching files, reading logs, and small edits go to Haiku, and only the hard thinking goes to Opus”
  — [9JtUYiRPQYc](https://youtu.be/9JtUYiRPQYc) [aSznLprottg](https://youtu.be/aSznLprottg) [EWbnYkyO5VM](https://youtu.be/EWbnYkyO5VM)
  ↳ *evidence-for* `g07-0111`
  ↳ *part-of* `y02-0021`

- `y02-0098` *CORE* — Fix for the Projects Opus default: switch the easy jobs to a cheaper model like Haiku first.
  > “switch the easy jobs to a cheaper model like Haiku first”
  — [GF2xgaEnQ0o](https://youtu.be/GF2xgaEnQ0o) [g6ZnVE4kQCk](https://youtu.be/g6ZnVE4kQCk)

- `y02-0129` *CORE* — Turn off the skills you never use and your Claude limit lasts way longer.
  — [Zy2NN8NydeA](https://youtu.be/Zy2NN8NydeA) [Eokwl898JUk](https://youtu.be/Eokwl898JUk)
  ↳ *defines* `y02-0124`

- `y02-0187` *CORE* — Model routing is Alex Chen's main limit lever: send easy jobs (search, logs, typos, small edits) to Haiku and save Opus for hard thinking, because Opus is the default for everything.
  — [9JtUYiRPQYc](https://youtu.be/9JtUYiRPQYc) [aSznLprottg](https://youtu.be/aSznLprottg) [EWbnYkyO5VM](https://youtu.be/EWbnYkyO5VM) [GF2xgaEnQ0o](https://youtu.be/GF2xgaEnQ0o) [g6ZnVE4kQCk](https://youtu.be/g6ZnVE4kQCk)
  ↳ *generalizes* `y02-0021`
  ↳ *generalizes* `y02-0098`

- `y03-0010` *INFERRED* — Model routing as a limit lever from Alex's numbers: send routine work to the cheaper models (Haiku about 15,000 messages per $1,000, Sonnet about 7,000) and reserve Opus or Fable for big, messy or hardest-problem work.
  — [FqOzuuip5iA](https://youtu.be/FqOzuuip5iA) [JifO6tUsSlA](https://youtu.be/JifO6tUsSlA)
  ↳ *evidence-for* `y02-0187`
  ↳ *generalizes* `y03-0186`
  ↳ *contrast* `y03-0045` — model choice and effort level are two separate limit levers

- `y03-0024` *STATED* — Alex packaged three habits that stop Claude from rereading everything, plus the tool to check your own Claude bill (comment 'costs').
  — [_I57Pc36DIg](https://youtu.be/_I57Pc36DIg)
  ↳ *evidence-for* `g12-0126`
  ↳ *qualifies* `y03-0023` — the habits target the rereading share

- `y03-0030` *STATED* — Fast-Jev Compaction makes room by clearing out only old stuff Claude already used, like files it opened earlier.
  — [20RWbPnejOE](https://youtu.be/20RWbPnejOE) [tq8Addr9brU](https://youtu.be/tq8Addr9brU) [kUH4J8VWe-I](https://youtu.be/kUH4J8VWe-I) [7eL_2dx0-bU](https://youtu.be/7eL_2dx0-bU)
  ↳ *evidence-for* `g12-0178`
  ↳ *part-of* `y03-0026`
  ↳ *leads-to* `y03-0034`
  ↳ *qualifies* `y03-0023` — dropping stale tool output shrinks what gets reread

- `y03-0032` *STATED* — Before Fast-Jev Compaction deletes anything, a second AI checks first whether it is still needed.
  — [20RWbPnejOE](https://youtu.be/20RWbPnejOE) [tq8Addr9brU](https://youtu.be/tq8Addr9brU) [kUH4J8VWe-I](https://youtu.be/kUH4J8VWe-I) [7eL_2dx0-bU](https://youtu.be/7eL_2dx0-bU)
  ↳ *qualifies* `y03-0030`

- `y04-0021` *STATED* — When you hit your usage limit locally, move the work to Claude Code cloud sessions and keep working until the credit runs out.
  > “So when you hit your limit locally, you move to the cloud and keep working until the credit runs out.”
  — [BgOlXwLlBrY](https://youtu.be/BgOlXwLlBrY) [QnzAaLZ70c0](https://youtu.be/QnzAaLZ70c0) [OyKQsxpeSLY](https://youtu.be/OyKQsxpeSLY)
  ↳ *evidence-for* `g13-0098`

- `y04-0044` *STATED* — Start with a basic first draft, then trigger the Darwin Loop only to improve the final result.
  > “you should start with a basic first draft and then trigger the Darwin Loop to improve the final result”
  — [gUOs9YjmZDo](https://youtu.be/gUOs9YjmZDo)
  ↳ *evidence-for* `g13-0236`
  ↳ *because* `y04-0043`

- `y04-0054` *STATED* — Start with a basic first draft, then trigger the Swarm Loop to improve the final result.
  > “you should start with a basic first draft and then trigger the Swarm Loop to improve the final result”
  — [kDh_gdXsJJU](https://youtu.be/kDh_gdXsJJU) [PG_HanOn_KE](https://youtu.be/PG_HanOn_KE) [jw25LS4GgUg](https://youtu.be/jw25LS4GgUg)
  ↳ *evidence-for* `g13-0248`
  ↳ *because* `y04-0053`

- `y04-0055` *CORE* — Rule for token-hungry multi-agent refinement loops (Darwin Loop, Swarm Loop): draft cheaply first and spend the loop only on polishing the final result.
  — [gUOs9YjmZDo](https://youtu.be/gUOs9YjmZDo) [kDh_gdXsJJU](https://youtu.be/kDh_gdXsJJU) [PG_HanOn_KE](https://youtu.be/PG_HanOn_KE) [jw25LS4GgUg](https://youtu.be/jw25LS4GgUg)
  ↳ *evidence-for* `g13-0305`
  ↳ *generalizes* `y04-0044`
  ↳ *generalizes* `y04-0054`

- `y04-0060` *STATED* — Instead of making your most expensive AI handle every little decision, connect Jev to your Claude Code workflow to make the small decisions.
  > “Instead of making your most expensive AI handle every little decision, just connect Jev to your Claude Code workflow.”
  — [Hdc86XqcDWM](https://youtu.be/Hdc86XqcDWM) [N8_l0apeaQE](https://youtu.be/N8_l0apeaQE) [1FXRIeZ2-lE](https://youtu.be/1FXRIeZ2-lE)
  ↳ *evidence-for* `g13-0179`
  ↳ *part-of* `y04-0057`

- `y04-0061` *STATED* — Jev use case 1 (router): give Jev your task and let it recommend whether a cheaper model can handle it or whether it needs your strongest model.
  > “giving Jev your task and letting it recommend whether a cheaper model can handle it or whether it needs your strongest one”
  — [Hdc86XqcDWM](https://youtu.be/Hdc86XqcDWM) [N8_l0apeaQE](https://youtu.be/N8_l0apeaQE) [1FXRIeZ2-lE](https://youtu.be/1FXRIeZ2-lE)
  ↳ *example-of* `y02-0187`
  ↳ *evidence-for* `g13-0186`
  ↳ *example-of* `y04-0060`
  ↳ *contrast* `y04-0021` — stretch limits by routing to cheaper models vs by moving to cloud credit

### number

- `g02-0035` *STATED* — Context Mode's README says that after 30 minutes, 40% of your Claude Code context is gone.
  > “after 30 minutes, 40% of your context is gone”
  — [g-stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode)
  ↳ *evidence-for* `g02-0034`
  ↳ *example-of* `g02-0236`

- `g02-0198` *STATED* — A Claude Code loop you forgot about can keep firing for a week.
  — [g-find-the-claude-code-loops-that-are-quietly-eating-your-limit](https://chen.media/guides/find-the-claude-code-loops-that-are-quietly-eating-your-limit)
  ↳ *qualifies* `g02-0195`

- `g03-0028` *STATED* — An @-mentioned file is inlined as long as it fits the Read tool's default limit of 25,000 tokens.
  — [g-stop-file-mentions-from-pasting-whole-files-into-your-claude-chat](https://chen.media/guides/stop-file-mentions-from-pasting-whole-files-into-your-claude-chat)

- `g03-0223` *STATED* — If your subagent descriptions together pass 15,000 tokens, Claude Code shows a warning with the total at the top of the screen when it starts.
  — [g-shorten-your-claude-helper-agent-descriptions](https://chen.media/guides/shorten-your-claude-helper-agent-descriptions)
  ↳ *evidence-for* `g03-0221`

- `g03-0237` *INFERRED* — From the README numbers, the Markdown-draft approach uses about 8x fewer output tokens (612 vs 4,893) and is about 2.6x faster (12 s vs 31 s) than hand-written HTML.
  — [g-answer-me-with-html-make-claude-answer-with-one-clean-page-not-a-wall-of-text](https://chen.media/guides/answer-me-with-html-make-claude-answer-with-one-clean-page-not-a-wall-of-text)
  ↳ *generalizes* `g03-0236`
  ↳ *evidence-for* `g16-0045`

- `g03-0241` *STATED* — In the terminal, Claude can run 200 web searches in one session.
  — [g-stop-claude-running-out-of-web-searches](https://chen.media/guides/stop-claude-running-out-of-web-searches)
  ↳ *leads-to* `g03-0243`

- `g03-0245` *STATED* — On Claude Code v2.1.290 or later, the web search limit refills on its own at about 100 searches an hour.
  — [g-stop-claude-running-out-of-web-searches](https://chen.media/guides/stop-claude-running-out-of-web-searches)
  ↳ *qualifies* `g03-0241`

- `g04-0088` *STATED* — Anthropic's cost docs say filtering test output to just the failures takes a 10,000-line log from tens of thousands of tokens down to hundreds.
  — [g-the-claude-hook-that-cuts-test-output-down-to-just-the-failures](https://chen.media/guides/the-claude-hook-that-cuts-test-output-down-to-just-the-failures)
  ↳ *evidence-for* `g04-0087`

- `g04-0124` *STATED* — Claude Max 5x includes $100 a month in Claude API credits.
  — [g-how-to-claim-your-monthly-claude-credits-on-max-and-team-plans](https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans)
  ↳ *part-of* `g04-0121`

- `g04-0125` *STATED* — Claude Max 20x includes $200 a month in Claude API credits.
  — [g-how-to-claim-your-monthly-claude-credits-on-max-and-team-plans](https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans)
  ↳ *part-of* `g04-0121`

- `g04-0126` *STATED* — On a Claude Team plan, each Standard seat adds $20 a month and each Premium seat adds $100 a month in Claude API credits.
  — [g-how-to-claim-your-monthly-claude-credits-on-max-and-team-plans](https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans) [g-how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets](https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets)
  ↳ *part-of* `g04-0121`

- `g04-0128` *CORE* — The pooled Team plan API credit balance is capped at $500 a month.
  — [g-how-to-claim-your-monthly-claude-credits-on-max-and-team-plans](https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans) [g-how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets](https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets)
  ↳ *qualifies* `g04-0127`

- `g04-0139` *STATED* — Anthropic's own example: a Team plan with three Standard seats plus two Premium seats gets $260 a month in API credits.
  — [g-how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets](https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets)
  ↳ *example-of* `g04-0126`

- `g04-0140` *STATED* — Adding one more Premium seat to a 3 Standard + 2 Premium Team plan makes the next month's API credit $360.
  — [g-how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets](https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets)
  ↳ *example-of* `g04-0126`
  ↳ *depends-on* `g04-0141`

- `g04-0142` *INFERRED* — By the per-seat rates, a team of five gets $100 a month in API credits if all five seats are Standard and $500 a month (the cap) if all five are Premium.
  — [g-how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets](https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets)
  ↳ *depends-on* `g04-0126`
  ↳ *depends-on* `g04-0128`

- `g04-0143` *INFERRED* — The $500 Team cap is reached at 5 Premium seats or 25 Standard seats; seats beyond that add no more credit.
  — [g-how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets](https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets)
  ↳ *depends-on* `g04-0128`

- `g05-0179` *STATED* — Claude Haiku 5.5 costs $0.10 per million input tokens, down from $1 on Haiku 4.5.
  — [g-claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command](https://chen.media/guides/claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command)
  ↳ *part-of* `g05-0180`
  ↳ *enables* `g05-0099` — a 10x cheaper Haiku makes a per-prompt classifier near-free
  ↳ *evidence-for* `g07-0092`

- `g05-0181` *STATED* — Haiku 5.5 costs $0.50 per million output tokens, at the listed price for prompts up to 100,000 tokens.
  — [g-claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command](https://chen.media/guides/claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command)
  ↳ *evidence-for* `g05-0183`
  ↳ *evidence-for* `g07-0093`

- `g05-0182` *STATED* — Haiku 4.5 costs $1 per million input tokens and $5 per million output tokens.
  — [g-claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command](https://chen.media/guides/claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command)
  ↳ *evidence-for* `g05-0183`

- `g05-0184` *STATED* — Haiku 5.5 reads up to 1 million tokens at once; Haiku 4.5 reads up to 200,000.
  — [g-claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command](https://chen.media/guides/claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command)
  ↳ *part-of* `g05-0180`
  ↳ *evidence-for* `g07-0095`

- `g05-0185` *STATED* — Haiku 5.5 writes up to 128,000 output tokens.
  — [g-claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command](https://chen.media/guides/claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command)
  ↳ *part-of* `g05-0180`
  ↳ *evidence-for* `g07-0096`

- `g05-0187` *STATED* — A $100 a month Haiku 4.5 bill becomes about $13 on Haiku 5.5, not $10, because of the tokenizer.
  — [g-claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command](https://chen.media/guides/claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command)
  ↳ *because* `g05-0186`
  ↳ *qualifies* `y02-0024` — 90% per-token cut, but new tokenizer means a $100 bill becomes ~$13 (87% saved), not $10

- `g05-0188` *INFERRED* — Haiku 4.5 -> 5.5 effective bill math: 1/10 the per-token price x ~1.3 tokens for the same text ≈ 0.13 of the old bill (about 87% saved).
  — [g-claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command](https://chen.media/guides/claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command)
  ↳ *evidence-for* `g05-0187`

- `g05-0189` *STATED* — Haiku 5.5 batch jobs are half price again: $0.05 in and $0.25 out per million tokens.
  — [g-claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command](https://chen.media/guides/claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command)
  ↳ *qualifies* `g05-0179`
  ↳ *evidence-for* `g07-0098`

- `g05-0190` *STATED* — Haiku 5.5 cache hits cost $0.01 per million tokens.
  — [g-claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command](https://chen.media/guides/claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command)
  ↳ *part-of* `g05-0179`
  ↳ *example-of* `g05-0146`

- `g05-0191` *STATED* — Haiku 5.5 can cache prompts from 512 tokens; Haiku 4.5 needed 4,096.
  — [g-claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command](https://chen.media/guides/claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command)
  ↳ *qualifies* `g05-0190`
  ↳ *qualifies* `g05-0146`

- `g05-0295` *STATED* — The Argon guide compares what Gemini 4 Argon costs next to Claude ('What it costs').
  — [g-gemini-4-argon-vs-claude-opus-5-5-the-full-table-and-which-model-to-use](https://chen.media/guides/gemini-4-argon-vs-claude-opus-5-5-the-full-table-and-which-model-to-use)
  ↳ *part-of* `g05-0294`

- `g06-0065` *STATED* — Valid /autocompact sizes run from 100K to 1M tokens.
  — [g-make-claude-compact-earlier-the-setting-and-the-claude-md-note](https://chen.media/guides/make-claude-compact-earlier-the-setting-and-the-claude-md-note)
  ↳ *qualifies* `g06-0064`

- `g06-0069` *STATED* — By default, on models with a native 1M window, Claude Code compacts at about 967K tokens, much later than a 200K setting.
  — [g-make-claude-compact-earlier-the-setting-and-the-claude-md-note](https://chen.media/guides/make-claude-compact-earlier-the-setting-and-the-claude-md-note)
  ↳ *contrast* `g06-0064`

- `g06-0203` *STATED* — Max 5x plans get $100 a month in API credits.
  — [g-this-week-in-claude-ranked-by-what-it-does-for-you](https://chen.media/guides/this-week-in-claude-ranked-by-what-it-does-for-you)
  ↳ *part-of* `g06-0202`
  ↳ *evidence-for* `g04-0124`

- `g06-0204` *STATED* — Max 20x plans get $200 a month in API credits.
  — [g-this-week-in-claude-ranked-by-what-it-does-for-you](https://chen.media/guides/this-week-in-claude-ranked-by-what-it-does-for-you)
  ↳ *part-of* `g06-0202`
  ↳ *evidence-for* `g04-0125`

- `g06-0205` *STATED* — Team Standard seats get $20 and Premium seats $100 a month in API credits, pooled and capped at $500.
  — [g-this-week-in-claude-ranked-by-what-it-does-for-you](https://chen.media/guides/this-week-in-claude-ranked-by-what-it-does-for-you)
  ↳ *part-of* `g06-0202`
  ↳ *evidence-for* `g04-0126`
  ↳ *evidence-for* `g04-0128`

- `g06-0234` *STATED* — Claude Code reported $0.347 (about $0.35) for Opus and $0.014 for Haiku 5.5 on the six-log-file job.
  — [g-send-claude-s-easy-jobs-to-haiku-5-5-with-one-helper-file](https://chen.media/guides/send-claude-s-easy-jobs-to-haiku-5-5-with-one-helper-file)
  ↳ *evidence-for* `g06-0232`

- `g07-0092` *STATED* — Claude Haiku 5.5 input costs $0.10 per million tokens, down from $1 on Haiku 4.5.
  — [g-set-up-claude-haiku-5-5-10x-cheaper-claude-model](https://chen.media/guides/set-up-claude-haiku-5-5-10x-cheaper-claude-model)
  ↳ *part-of* `g07-0090`
  ↳ *evidence-for* `g07-0090` — $0.10 vs $1 = 10x
  ↳ *enables* `g07-0221`

- `g07-0093` *STATED* — Claude Haiku 5.5 output costs $0.50 per million tokens, versus $5 on Haiku 4.5.
  — [g-set-up-claude-haiku-5-5-10x-cheaper-claude-model](https://chen.media/guides/set-up-claude-haiku-5-5-10x-cheaper-claude-model)
  ↳ *part-of* `g07-0090`
  ↳ *evidence-for* `g07-0090`

- `g07-0095` *STATED* — Claude Haiku 5.5 has a 1M-token context window, versus 200K tokens on Haiku 4.5.
  — [g-set-up-claude-haiku-5-5-10x-cheaper-claude-model](https://chen.media/guides/set-up-claude-haiku-5-5-10x-cheaper-claude-model)
  ↳ *part-of* `g07-0090`
  ↳ *evidence-for* `g07-0090` — million tokens at once
  ↳ *depends-on* `g07-0101`

- `g07-0096` *STATED* — Claude Haiku 5.5's max output is 128K tokens, versus 64K tokens on Haiku 4.5.
  — [g-set-up-claude-haiku-5-5-10x-cheaper-claude-model](https://chen.media/guides/set-up-claude-haiku-5-5-10x-cheaper-claude-model)
  ↳ *part-of* `g07-0090`

- `g07-0098` *STATED* — The Batch API takes another 50% off Haiku 5.5's prices.
  — [g-set-up-claude-haiku-5-5-10x-cheaper-claude-model](https://chen.media/guides/set-up-claude-haiku-5-5-10x-cheaper-claude-model)
  ↳ *part-of* `g07-0090`
  ↳ *enables* `g07-0221`

- `g07-0208` *STATED* — Claude Max 5x gets $100 of API credits every month.
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *part-of* `g07-0203`
  ↳ *evidence-for* `g07-0203`
  ↳ *evidence-for* `g04-0124`

- `g07-0209` *STATED* — Claude Max 20x gets $200 of API credits every month.
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *part-of* `g07-0203`
  ↳ *evidence-for* `g07-0203`
  ↳ *evidence-for* `g04-0125`

- `g07-0210` *STATED* — Claude Team gets $20 of API credits per Standard seat every month.
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *part-of* `g07-0203`
  ↳ *evidence-for* `g07-0213`
  ↳ *evidence-for* `g04-0126`

- `g07-0211` *STATED* — Claude Team gets $100 of API credits per Premium seat every month.
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *part-of* `g07-0203`
  ↳ *evidence-for* `g07-0213`
  ↳ *evidence-for* `g04-0126`

- `g10-0196` *STATED* — On Anthropic's hard benchmark tasks, a typical Fable 5.1 attempt at low effort used about 73k tokens and at max about 222k: three times as much for the same tasks.
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *evidence-for* `g10-0197`
  ↳ *evidence-for* `g10-0269`

- `g11-0037` *CORE* — Claude Opus 5.5 API pricing is $4 per 1M input tokens and $20 per 1M output tokens.
  — [g-gemini-4-argon-which-ai-to-use-for-what](https://chen.media/guides/gemini-4-argon-which-ai-to-use-for-what) [g-turn-any-photo-into-a-painting-claude-draws-with-code](https://chen.media/guides/turn-any-photo-into-a-painting-claude-draws-with-code) [g-gemini-4-pro-leak-one-prompt-to-test-it-against-claude](https://chen.media/guides/gemini-4-pro-leak-one-prompt-to-test-it-against-claude)
  ↳ *contrast* `g11-0038` — Astra costs 2.5x Opus per token
  ↳ *contrast* `g11-0093`
  ↳ *evidence-for* `g12-0016`

- `g11-0053` *STATED* — Gemini 4 Argon's cached input is 95% off.
  — [g-gemini-4-argon-which-ai-to-use-for-what](https://chen.media/guides/gemini-4-argon-which-ai-to-use-for-what)
  ↳ *qualifies* `g11-0048`

- `g11-0093` *STATED* — Claude Sonnet 5.5 costs $2 per million input tokens and $10 per million output tokens, half of Opus 5.5.
  — [g-turn-any-photo-into-a-painting-claude-draws-with-code](https://chen.media/guides/turn-any-photo-into-a-painting-claude-draws-with-code)
  ↳ *evidence-for* `g11-0096`
  ↳ *evidence-for* `g12-0016`

- `g11-0126` *STATED* — OpenAI's Pro 500 plan gives 25x the ChatGPT Plus allowance, with no 5-hour limit.
  — [g-is-openais-500-ultrafast-plan-worth-it](https://chen.media/guides/is-openais-500-ultrafast-plan-worth-it)
  ↳ *qualifies* `g11-0120` — what the $500 buys

- `g11-0218` *STATED* — Context windows per the leaked chart: Gemini 4 Pro 2M tokens, Claude Opus 5.5 1M tokens, GPT-6 Astra 1.1M tokens.
  — [g-gemini-4-pro-leak-one-prompt-to-test-it-against-claude](https://chen.media/guides/gemini-4-pro-leak-one-prompt-to-test-it-against-claude)
  ↳ *part-of* `g11-0211`

- `g12-0007` *CORE* — Claude Sonnet 5.5 costs half as much per token as Claude Opus 5.5.
  — [g-claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task](https://chen.media/guides/claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task)
  ↳ *evidence-for* `g12-0002`

- `g12-0016` *STATED* — API price per 1M tokens (input / output): Sonnet 5.5 $2 / $10, Opus 5.5 $4 / $20, Sonnet 5 $2 / $10.
  — [g-claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task](https://chen.media/guides/claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task)
  ↳ *evidence-for* `g12-0007`

- `g12-0096` *CORE* — Anthropic measured that on a customer-support benchmark moved from Opus 4.8 to Opus 5.5, removing old prompt patterns cut costs by a further 9%.
  — [g-clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit](https://chen.media/guides/clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit)
  ↳ *evidence-for* `g12-0092`
  ↳ *because* `g12-0105`

- `g12-0114` *CORE* — Alex Chen's $200 month of Claude Code usage would have cost about $4,500 at API prices, over 22 times what he paid.
  — [g-what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything)
  ↳ *depends-on* `g12-0113`

- `g12-0115` *STATED* — Alex Chen's most expensive single day of Claude Code usage came to about $500 at API prices.
  — [g-what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything)
  ↳ *part-of* `g12-0114`

- `g12-0116` *STATED* — Only about 11% of Alex Chen's API-priced Claude bill was Claude actually writing anything.
  — [g-what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything)
  ↳ *part-of* `g12-0114`
  ↳ *contrast* `g12-0117`

- `g12-0117` *STATED* — About two-thirds of Alex Chen's API-priced bill, roughly $3,000, was Claude re-reading the same conversation before every reply.
  — [g-what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything)
  ↳ *part-of* `g12-0114`
  ↳ *because* `g12-0119`
  ↳ *because* `g12-0124`

- `g13-0100` *CORE* — Pro subscribers get $100 of one-time Claude Code cloud session credit.
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it) [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)
  ↳ *part-of* `g13-0099`

- `g13-0101` *CORE* — Max subscribers get $250 of one-time Claude Code cloud session credit.
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it) [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)
  ↳ *part-of* `g13-0099`

- `g13-0102` *CORE* — The cloud session credit must be claimed by 11:59 PM PT (Pacific time) on October 7, 2026.
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it) [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)
  ↳ *qualifies* `g13-0099`

- `g13-0103` *CORE* — Unspent cloud session credit expires at 11:59 PM PT on November 4, 2026.
  — [g-claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it](https://chen.media/guides/claude-code-now-runs-with-your-laptop-closed-plus-up-to-250-free-to-try-it) [g-how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7](https://chen.media/guides/how-to-claim-up-to-250-of-free-claude-code-credit-before-october-7)
  ↳ *qualifies* `g13-0099`

- `g13-0180` *STATED* — TypeSafe publishes Jev response times of 70 to 500 milliseconds.
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *qualifies* `g13-0169`

- `g13-0181` *STATED* — TypeSafe publishes Jev input pricing of $0.042 per million tokens, with output tokens free.
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *qualifies* `g13-0169`
  ↳ *evidence-for* `y04-0058`

- `g14-0035` *STATED* — TypeSafe reports roughly $7 per hour for its Jev DOOM demo configuration.
  — [g-jev-doom-demo-explained](https://chen.media/guides/jev-doom-demo-explained)
  ↳ *part-of* `g14-0030`

- `g14-0130` *STATED* — AWS offers new customers up to $200 in credits: $100 at sign-up and up to $100 more from eligible activities.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *part-of* `g14-0129`
  ↳ *evidence-for* `g14-0148`

- `g14-0137` *STATED* — The AWS Free plan closes after six months or when its credits run out, whichever comes first.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *qualifies* `g14-0136`

- `g15-0013` *STATED* — Uploading a PDF to Claude can cost you about 70,000 tokens.
  — [g-why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix](https://chen.media/guides/why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix)
  ↳ *evidence-for* `y03-0012`

- `g16-0107` *STATED* — A single number starts the whole 15-mistakes argument.
  > “The number that starts all of this”
  — [g-15-claude-mistakes-that-are-quietly-costing-you-tokens](https://chen.media/guides/15-claude-mistakes-that-are-quietly-costing-you-tokens)
  ↳ *evidence-for* `g16-0100`

- `g16-0130` *STATED* — ox-alpha has a 1,048,576 token context window.
  — [g-the-anonymous-model-that-makes-claude-code-free-until-august-27](https://chen.media/guides/the-anonymous-model-that-makes-claude-code-free-until-august-27)
  ↳ *evidence-for* `g16-0129`
  ↳ *qualifies* `g16-0101` — a 1,048,576 window is still finite

- `g16-0131` *STATED* — ox-alpha produces up to 131,072 tokens of output in a single response.
  — [g-the-anonymous-model-that-makes-claude-code-free-until-august-27](https://chen.media/guides/the-anonymous-model-that-makes-claude-code-free-until-august-27)
  ↳ *evidence-for* `g16-0129`

- `g17-0020` *STATED* — Free Claude accounts get five Projects.
  > “Free accounts get five of them.”
  — [g-the-4-prompts-that-turn-a-claude-project-into-a-tutor](https://chen.media/guides/the-4-prompts-that-turn-a-claude-project-into-a-tutor)
  ↳ *qualifies* `g17-0019`
  ↳ *evidence-for* `g20-0290`

- `g17-0148` *STATED* — FreeLLMAPI lists roughly 4 billion tokens per month of free capacity.
  — [g-pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint](https://chen.media/guides/pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint)
  ↳ *evidence-for* `g17-0150`

- `g19-0169` *STATED* — The Claude Code Router management UI opens at http://127.0.0.1:3458 and the gateway runs at http://127.0.0.1:3456.
  > “The management UI opens at http://127.0.0.1:3458 and the gateway runs at http://127.0.0.1:3456.”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *leads-to* `g19-0168`

- `g19-0184` *STATED* — Shipping 2,000 lines into context to edit 20 means paying for 1,980 lines of noise.
  > “If you were shipping 2,000 lines into context to edit 20, you were paying for 1,980 lines of noise.”
  — [g-give-claude-code-an-ide-brain-so-it-stops-reading-everything](https://chen.media/guides/give-claude-code-an-ide-brain-so-it-stops-reading-everything)
  ↳ *evidence-for* `g19-0177`

- `g20-0046` *STATED* — Alex checked Claude plan prices on 18 July 2026.
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *qualifies* `g20-0047`
  ↳ *qualifies* `g20-0048`
  ↳ *qualifies* `g20-0049`

- `g20-0047` *STATED* — Claude Free costs $0.
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *qualifies* `g20-0050`

- `g20-0048` *STATED* — Claude Pro is $17 per month with the annual discount ($200 billed up front), or $20 billed monthly.
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *enables* `g20-0051`

- `g20-0049` *STATED* — Claude Max starts at $100 per month.
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)

- `g20-0082` *STATED* — The Claude Free plan caps you at 5 projects.
  — [g-the-one-prompt-that-makes-claude-design-real-carousels](https://chen.media/guides/the-one-prompt-that-makes-claude-design-real-carousels)
  ↳ *qualifies* `g20-0081`

- `g20-0083` *STATED* — The Claude Free plan resets usage on a rolling 5-hour window, and a 10-slide carousel build plus edits eats into that window.
  — [g-the-one-prompt-that-makes-claude-design-real-carousels](https://chen.media/guides/the-one-prompt-that-makes-claude-design-real-carousels)
  ↳ *qualifies* `g20-0081`
  ↳ *leads-to* `g20-0084`

- `g20-0166` *STATED* — The memory guide's 'What This Replaces: The math' section quantifies what the five-file system replaces.
  — [g-the-five-files-that-give-claude-a-real-memory](https://chen.media/guides/the-five-files-that-give-claude-a-real-memory)
  ↳ *part-of* `g20-0141`

- `g21-0214` *STATED* — The content-team setup is five files, five specialists, zero per-month cost beyond the Claude plan you already pay for.
  > “five files, five specialists, zero per-month cost beyond the Claude plan you already pay for.”
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *part-of* `g21-0210`
  ↳ *example-of* `g05-0314`

- `g22-0013` *STATED* — Judgment Vault cost table, this week: Fable 5 back-solves your rules (steps 1 to 3), free during the window.
  — [g-bank-the-judgment-calls-not-just-the-output](https://chen.media/guides/bank-the-judgment-calls-not-just-the-output)
  ↳ *evidence-for* `g22-0012`

- `g22-0014` *STATED* — Judgment Vault cost table, after the window: any cheap model reads the vault and decides like you (step 4), costing pennies per call.
  — [g-bank-the-judgment-calls-not-just-the-output](https://chen.media/guides/bank-the-judgment-calls-not-just-the-output)
  ↳ *evidence-for* `g22-0005`

- `g22-0052` *STATED* — GPT-5.6 Luna is about 5x cheaper than Sol.
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)
  ↳ *evidence-for* `g22-0049`

- `g22-0057` *STATED* — GPT-5.6 Sol costs $5 / $30 per 1M tokens (in / out) and takes the Architect + Inspector station: writes the master spec and quality bar, then QA-checks the batch.
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)
  ↳ *evidence-for* `g22-0052`
  ↳ *part-of* `g22-0055`

- `g22-0058` *STATED* — GPT-5.6 Terra costs $2.50 / $15 per 1M tokens (in / out) and is the Drafter: it turns the spec into structured drafts.
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)
  ↳ *part-of* `g22-0055`

- `g22-0060` *STATED* — GPT-5.6 Luna costs $1 / $6 per 1M tokens (in / out) and is the Line worker: it mass-produces, personalizes and formats all 50 units, fast and cheap.
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)
  ↳ *evidence-for* `g22-0052`
  ↳ *part-of* `g22-0055`

- `g22-0063` *STATED* — Everything between spec and inspection is Terra and Luna, and that is where the model line's 1/5 cost comes from.
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)

- `r01-0140` *STATED* — One /hiring-panel run is eight sub-agent calls and counts toward your Claude plan's usage.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *example-of* `r01-0017`

- `r01-0181` *STATED* — A full /court trial is 17 sub-agent calls: 2 openings, 2 rebuttals, 12 jurors, 1 judge.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *evidence-for* `r01-0183`

- `r01-0182` *STATED* — A /court --quick trial is 11 sub-agent calls.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *evidence-for* `r01-0183`
  ↳ *depends-on* `r01-0179`

- `r02-0075` *STATED* — /hunter keeps at most 15 postings to score per run; if more remain it keeps the best title matches and says how many were left.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0073`
  ↳ *qualifies* `r02-0038` — caps scorer calls per run

- `r02-0149` *STATED* — A full /launch poll is 9 sub-agent calls (8 stations and the flight director); `--quick` is 6.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r02-0150`
  ↳ *example-of* `r01-0017`

- `r04-0224` *STATED* — Five /shark investors is 11 sub-agent calls: 5 sets of questions, 1 founder, 5 decisions.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *evidence-for* `r04-0016`
  ↳ *qualifies* `r04-0210`
  ↳ *example-of* `r01-0017`

- `y01-0146` *STATED* — Alex says running Opus at max effort costs 50% more.
  > “It costs 50% more”
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *contradicts* `g10-0196` — Opus at max effort "costs 50% more" vs Anthropic benchmark: max ~222k vs low ~73k tokens, three times as much
  ↳ *evidence-for* `y01-0148`

- `y02-0024` *CORE* — Haiku 5.5 costs 90% less per token than the last Haiku.
  > “Haiku 5.5 costs 90% less per token than the last Haiku”
  — [9JtUYiRPQYc](https://youtu.be/9JtUYiRPQYc) [aSznLprottg](https://youtu.be/aSznLprottg) [EWbnYkyO5VM](https://youtu.be/EWbnYkyO5VM)
  ↳ *because* `y02-0026`
  ↳ *enables* `y02-0021`

- `y03-0002` *STATED* — $1,000 of Claude usage buys about 15,000 messages on Haiku.
  — [FqOzuuip5iA](https://youtu.be/FqOzuuip5iA)
  ↳ *evidence-for* `y03-0009`

- `y03-0003` *STATED* — $1,000 of Claude usage buys about 7,000 messages on Sonnet.
  — [FqOzuuip5iA](https://youtu.be/FqOzuuip5iA)
  ↳ *evidence-for* `y03-0010`
  ↳ *part-of* `y03-0009` — middle rungs of the same $1,000 ladder

- `y03-0005` *STATED* — $1,000 of Claude usage buys about 5,800 messages on Opus.
  — [FqOzuuip5iA](https://youtu.be/FqOzuuip5iA)
  ↳ *evidence-for* `y03-0010`
  ↳ *part-of* `y03-0009` — middle rungs of the same $1,000 ladder

- `y03-0007` *STATED* — $1,000 of Claude usage buys only about 3,200 messages on Claude Fable.
  — [FqOzuuip5iA](https://youtu.be/FqOzuuip5iA)
  ↳ *evidence-for* `y03-0009`

- `y03-0014` *STATED* — Opus costs double the price of Sonnet.
  — [Rgb7FFLwz60](https://youtu.be/Rgb7FFLwz60)
  ↳ *evidence-for* `g12-0007`
  ↳ *part-of* `y03-0012`
  ↳ *contradicts* `y03-0005` — if Opus cost 2x Sonnet, $1,000 should buy ~3,500 Opus messages, not 5,800 vs Sonnet's 7,000
  ↳ *evidence-for* `y03-0010`

- `y03-0018` *STATED* — Alex paid $200 for his Claude plan last month.
  — [_I57Pc36DIg](https://youtu.be/_I57Pc36DIg)
  ↳ *evidence-for* `y03-0020`

- `y03-0019` *STATED* — Alex's $200 month of Claude usage would have cost about $4,500 at API prices.
  — [_I57Pc36DIg](https://youtu.be/_I57Pc36DIg)
  ↳ *evidence-for* `g12-0114`
  ↳ *evidence-for* `y03-0020`

- `y03-0021` *STATED* — Alex's most expensive single day of Claude usage would have cost about $500 at API prices.
  — [_I57Pc36DIg](https://youtu.be/_I57Pc36DIg)
  ↳ *evidence-for* `g12-0115`
  ↳ *part-of* `y03-0019`

- `y03-0022` *STATED* — Only about 11% of Alex's $4,500 API-priced bill was Claude actually writing anything.
  — [_I57Pc36DIg](https://youtu.be/_I57Pc36DIg)
  ↳ *evidence-for* `g12-0116`
  ↳ *part-of* `y03-0019`
  ↳ *contrast* `y03-0023` — writing is a small slice; rereading dominates

- `y03-0023` *CORE* — Two thirds of Alex's $4,500 API-priced bill was Claude rereading the same conversation over and over before every single reply.
  — [_I57Pc36DIg](https://youtu.be/_I57Pc36DIg)
  ↳ *evidence-for* `g12-0117`
  ↳ *part-of* `y03-0019`
  ↳ *evidence-for* `y03-0025`

- `y03-0073` *STATED* — When Anthropic tested the legacy-prompt cleanup advice, costs dropped around 9%.
  — [q-cfyZWRwmU](https://youtu.be/q-cfyZWRwmU)
  ↳ *evidence-for* `g12-0096`
  ↳ *evidence-for* `y03-0065`
  ↳ *part-of* `y03-0074` — same Anthropic test

- `y03-0184` *STATED* — Sonnet 5.5 is up to 30% cheaper per job than the last Sonnet.
  — [JifO6tUsSlA](https://youtu.be/JifO6tUsSlA)
  ↳ *evidence-for* `g11-0095`
  ↳ *evidence-for* `y03-0186`

- `y04-0011` *STATED* — claude-mem claims 95% less token consumption per session.
  > “has 95% less token consumption per session”
  — [55RbHPThR8g](https://youtu.be/55RbHPThR8g) [EVTO2eM2DlQ](https://youtu.be/EVTO2eM2DlQ) [6zrQsxiYz1E](https://youtu.be/6zrQsxiYz1E)
  ↳ *evidence-for* `y04-0010` — headline token-savings claim
  ↳ *contrast* `y04-0020` — two different usage levers: fewer tokens vs credit outside limits

- `y04-0058` *STATED* — Jev costs 200 times less than Claude.
  > “it costs 200 times less than Claude”
  — [Hdc86XqcDWM](https://youtu.be/Hdc86XqcDWM) [N8_l0apeaQE](https://youtu.be/N8_l0apeaQE) [1FXRIeZ2-lE](https://youtu.be/1FXRIeZ2-lE)
  ↳ *evidence-for* `y04-0057`

- `y04-0062` *STATED* — Routing tasks through Jev to pick cheaper models 'will give you 80% more usage'.
  > “This will give you 80% more usage.”
  — [Hdc86XqcDWM](https://youtu.be/Hdc86XqcDWM) [N8_l0apeaQE](https://youtu.be/N8_l0apeaQE) [1FXRIeZ2-lE](https://youtu.be/1FXRIeZ2-lE)
  ↳ *evidence-for* `y04-0061`
  ↳ *contradicts* `y04-0059` — 80% more usage (1.8x) vs the '10x your Claude Code' headline

### opinion

- `g03-0075` *STATED* — Most people never open the /usage breakdown, so they guess at what is draining their limit.
  > “Most people never open it, so they guess.”
  — [g-find-what-is-draining-your-claude-limit-with-usage](https://chen.media/guides/find-what-is-draining-your-claude-limit-with-usage)
  ↳ *example-of* `g03-0008`
  ↳ *contrast* `g03-0073`

- `g04-0144` *STATED* — Alex's alternate headline frames claiming the monthly API credits as getting them 'back', since they are included in a plan you already pay for.
  > “How to Get Your Monthly Claude Credits Back”
  — [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans)
  ↳ *qualifies* `g04-0122`
  ↳ *example-of* `g04-0244`

- `g06-0220` *STATED* — You don't control your employer's AI budget, but you do control how fast your own Claude limit drains: stop spending it on easy jobs.
  > “You don't control that budget. You do control how fast your own Claude limit drains.”
  — [g-make-your-claude-limit-last-the-haiku-helper-and-3-habits](https://chen.media/guides/make-your-claude-limit-last-the-haiku-helper-and-3-habits)

- `g09-0133` *STATED* — The people who never hit their Claude limit aren't using it better than you; a lot of them simply don't carry skills they never use.
  > “The people who never hit their Claude limit aren't using it better than you. A lot of them simply don't carry skills they never use.”
  — [g-find-the-claude-skills-eating-your-limit-skill-doctor](https://chen.media/guides/find-the-claude-skills-eating-your-limit-skill-doctor)
  ↳ *because* `g09-0131`
  ↳ *evidence-for* `y02-0124`

- `g10-0183` *STATED* — Leaving effort untouched or pinned at max both waste something: time on easy jobs, or quality on hard ones, and a lot of your usage limit either way.
  — [g-claude-code-effort-levels-cheat-sheet](https://chen.media/guides/claude-code-effort-levels-cheat-sheet)
  ↳ *because* `g10-0182`
  ↳ *evidence-for* `y01-0018`

- `g11-0096` *STATED* — Alex: detailed visual work that used to need Opus is now within reach of the cheaper Sonnet 5.5.
  — [g-turn-any-photo-into-a-painting-claude-draws-with-code](https://chen.media/guides/turn-any-photo-into-a-painting-claude-draws-with-code)
  ↳ *leads-to* `g11-0097`

- `g11-0129` *STATED* — Alex: on Ultrafast your agent writes 8x faster, but it doesn't think, run your tests or wait on your tools 8x faster.
  > “Your agent writes 8x faster. It doesn't think, run your tests or wait on your tools 8x faster.”
  — [g-is-openais-500-ultrafast-plan-worth-it](https://chen.media/guides/is-openais-500-ultrafast-plan-worth-it)
  ↳ *qualifies* `g11-0118`
  ↳ *evidence-for* `g11-0134`

- `g12-0010` *STATED* — The useful question is not which Claude model is better but which one to pick for each job.
  > “So the question isn't which model is better. It's which one to pick for each job.”
  — [g-claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task](https://chen.media/guides/claude-sonnet-5-5-vs-opus-5-5-which-claude-for-every-task)
  ↳ *leads-to* `g12-0023`

- `g13-0178` *STATED* — You do not need your strongest, most expensive model for small workflow calls.
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)
  ↳ *because* `g13-0179`

- `g16-0041` *STATED* — Cheaper model, shorter prompts and clearing context are all fine, but they are all one lever.
  > “All fine, all one lever.”
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you)
  ↳ *qualifies* `g16-0040`
  ↳ *contrast* `g16-0042`

- `g17-0119` *STATED* — The fix for a coding agent's growing token bill is not a smaller model or a shorter prompt.
  > “The fix is not a smaller model or a shorter prompt.”
  — [g-cut-what-your-coding-agent-sends-to-the-model](https://chen.media/guides/cut-what-your-coding-agent-sends-to-the-model)
  ↳ *contrast* `g17-0120`

- `g17-0142` *STATED* — On its own each AI free tier is a toy, which is why most developers sign up for one, hit a wall, and go pay for a plan.
  > “On its own each one is a toy”
  — [g-pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint](https://chen.media/guides/pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint)

- `g19-0008` *STATED* — Context hygiene (Tier 2 of the 28 ways) is by far the biggest lever for staying under Claude Code usage limits.
  > “Context hygiene, the biggest lever by far”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)
  ↳ *part-of* `g19-0002`
  ↳ *because* `g19-0016` — context is the problem so context hygiene is the biggest lever

- `g22-0002` *STATED* — During the short free window with Claude Fable 5, Alex Chen says not to spend it building something new but to bank the one thing only you have: your judgment.
  > “You have a short free window with Fable 5. Do not spend it building something new. Spend it banking the one thing only you have: your judgment.”
  — [g-bank-the-judgment-calls-not-just-the-output](https://chen.media/guides/bank-the-judgment-calls-not-just-the-output)
  ↳ *part-of* `g22-0001`

- `g22-0012` *CORE* — Do the expensive thinking ONCE while the top model is free; the output, one small file, is readable by any model forever.
  > “So you do the expensive thinking ONCE while it is free, and the output (one small file) is readable by any model forever.”
  — [g-bank-the-judgment-calls-not-just-the-output](https://chen.media/guides/bank-the-judgment-calls-not-just-the-output)
  ↳ *because* `g22-0002`
  ↳ *evidence-for* `g23-0016`

- `g22-0045` *STATED* — Stop running all 50 tasks through GPT-5.6 Sol; build a Sol to Terra to Luna line and get flagship quality for a fraction of the cost.
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)
  ↳ *part-of* `g22-0044`

- `g22-0139` *STATED* — Brand setup step 1: open Claude with your best model, because the brief sets the ceiling for everything after it.
  > “use your best model, the brief sets the ceiling for everything after it”
  — [g-turn-claude-into-a-full-brand-studio-free](https://chen.media/guides/turn-claude-into-a-full-brand-studio-free)
  ↳ *part-of* `g22-0138`
  ↳ *leads-to* `g22-0140`
  ↳ *example-of* `g22-0282`
  ↳ *analogy-for* `g22-0050` — best model writes the spec that sets the ceiling
  ↳ *example-of* `g21-0158`

- `y02-0020` *STATED* — Everyone hitting their Claude limit is basically wasting it on jobs a way cheaper model could do.
  > “Everyone hitting their Claude limit is basically wasting it on jobs a way cheaper model could do.”
  — [9JtUYiRPQYc](https://youtu.be/9JtUYiRPQYc) [aSznLprottg](https://youtu.be/aSznLprottg) [EWbnYkyO5VM](https://youtu.be/EWbnYkyO5VM)
  ↳ *leads-to* `y02-0021` — problem -> his router skill

### product

- `g02-0031` *STATED* — Context Mode is a Claude Code plugin that keeps raw web pages, logs and GitHub issues out of Claude's context window.
  — [g-stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode)
  ↳ *because* `g02-0034`
  ↳ *example-of* `g02-0241`

- `g02-0176` *STATED* — Trail-code is a free, open-source tool (MIT license, over 10,000 GitHub stars) that builds a map of your code: every file, every function, and who calls what.
  — [g-trail-code-stop-claude-getting-lost-in-your-code](https://chen.media/guides/trail-code-stop-claude-getting-lost-in-your-code)
  ↳ *because* `g02-0178`
  ↳ *example-of* `g02-0235`

- `g04-0071` *STATED* — tokentab is a free, open-source tool (MIT licence) that reads the session logs Claude Code already writes to your computer and turns them into one monthly statement.
  — [g-tokentab-see-where-every-claude-token-goes-as-a-monthly-statement](https://chen.media/guides/tokentab-see-where-every-claude-token-goes-as-a-monthly-statement)
  ↳ *part-of* `g04-0084`
  ↳ *example-of* `g04-0252`

- `g05-0098` *STATED* — Effortless is a free, MIT-licensed Claude Code mod by HeyCubit that picks the reasoning effort for every prompt.
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless)
  ↳ *contradicts* `g05-0157` — Effortless changes effort per prompt; the cache guide says stay on one effort level for the whole task
  ↳ *contrast* `g05-0161` — automatic per-prompt effort vs manual per-subagent effort
  ↳ *enables* `y03-0044`

- `g07-0104` *CORE* — Alex's Haiku helper is a two-file skill that hands Claude Code's easy jobs (searching files, reading logs, small edits) to Haiku 5.5 and keeps Opus for the hard thinking.
  — [g-make-claude-code-limit-last-longer-haiku-5-5-helper](https://chen.media/guides/make-claude-code-limit-last-longer-haiku-5-5-helper)
  ↳ *example-of* `y02-0187`

- `g07-0169` *STATED* — token-weather is Anthropic's sample memory-meter mod: it forecasts how full Claude's memory (context) is.
  — [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *part-of* `g07-0181`
  ↳ *part-of* `g07-0160`
  ↳ *example-of* `g07-0163`
  ↳ *enables* `g07-0200` — context meter helps watch usage

- `g13-0169` *STATED* — Jev is TypeSafe AI's first 'System One' model: a fast, cheap decision model.
  — [g-jev-claude-code-workflows](https://chen.media/guides/jev-claude-code-workflows)

- `g14-0057` *STATED* — Headroom is a Claude Code tool that reduces supported input payloads (shrinking what is sent to the model).
  > “Headroom reduces supported input payloads”
  — [g-headroom-claude-hud-aisa-setup](https://chen.media/guides/headroom-claude-hud-aisa-setup)
  ↳ *part-of* `g14-0056`
  ↳ *example-of* `g17-0120`

- `g14-0061` *STATED* — Claude HUD displays context usage, active tools, agents and task progress beneath the Claude Code input.
  — [g-headroom-claude-hud-aisa-setup](https://chen.media/guides/headroom-claude-hud-aisa-setup)
  ↳ *defines* `g14-0058`
  ↳ *contrast* `g14-0180` — context usage visible vs advertised 1M context

- `g15-0069` *CORE* — diegosouzapw/OmniRoute (MIT, over 61,000 stars) is a free AI gateway that reroutes to another model when Claude runs out of credits or errors.
  — [g-four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute](https://chen.media/guides/four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute)
  ↳ *part-of* `g15-0061`
  ↳ *enables* `g15-0070`
  ↳ *contrast* `g15-0146` — both route across models: OmniRoute as fallback gateway, one tab as consolidated subscription
  ↳ *evidence-for* `g16-0284`

- `g16-0284` *STATED* — OmniRoute is the plugin that keeps you coding past the usage limit: the reason you stop hitting the wall.
  > “OmniRoute, the reason you stop hitting the wall”
  — [g-three-plugins-that-fix-claude-code-s-setup-limits-and-memory](https://chen.media/guides/three-plugins-that-fix-claude-code-s-setup-limits-and-memory)
  ↳ *part-of* `g16-0282`
  ↳ *example-of* `g16-0013`

- `g18-0268` *STATED* — Caveman (JuliusBrussee/caveman, 94.1k stars, MIT) makes Claude answer in short, blunt fragments instead of paragraphs.
  — [g-seven-free-repos-that-replace-paid-ai-tools](https://chen.media/guides/seven-free-repos-that-replace-paid-ai-tools)
  ↳ *part-of* `g18-0262`
  ↳ *example-of* `g16-0045`

- `g19-0156` *STATED* — Claude Code Router: musistudio/claude-code-router, 35.9k stars, MIT, https://github.com/musistudio/claude-code-router.
  > “Musistudio / Claude-code-router . 35.9k Stars . Mit”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *part-of* `g19-0155`

- `y02-0021` *STATED* — Alex Chen built a Claude skill (CTA keyword 'limit') that sorts each task first, automatically sends the easy ones to the new Haiku 5.5, and saves Opus for the hard thinking.
  > “I built a skill that sorts each task first and sends the easy ones to the new Haiku 5.5”
  — [9JtUYiRPQYc](https://youtu.be/9JtUYiRPQYc) [aSznLprottg](https://youtu.be/aSznLprottg) [EWbnYkyO5VM](https://youtu.be/EWbnYkyO5VM)
  ↳ *evidence-for* `g07-0104`

- `y02-0127` *STATED* — Claude has a 'hidden command' Alex Chen calls the Skill Doctor that shows exactly how many tokens your installed skills cost you (CTA keyword 'doctor').
  > “Claude has a hidden command called the Skill Doctor that shows you exactly how many tokens this costs you”
  — [Zy2NN8NydeA](https://youtu.be/Zy2NN8NydeA) [Eokwl898JUk](https://youtu.be/Eokwl898JUk)
  ↳ *enables* `y02-0129`

- `y03-0026` *STATED* — Fast-Jev Compaction is an open-sourced way to stop Claude from summarizing your conversation when it compacts (name heard as 'Fast Jet / fast chat compaction').
  — [20RWbPnejOE](https://youtu.be/20RWbPnejOE) [tq8Addr9brU](https://youtu.be/tq8Addr9brU) [kUH4J8VWe-I](https://youtu.be/kUH4J8VWe-I) [7eL_2dx0-bU](https://youtu.be/7eL_2dx0-bU)
  ↳ *evidence-for* `g12-0178`

### resource

- `g02-0184` *STATED* — The Trail-code guide has 1 prompt and 4 numbered steps, with email-gated 'Step 1: install it', 'Step 2: what changes' and 'The catch' sections.
  — [g-trail-code-stop-claude-getting-lost-in-your-code](https://chen.media/guides/trail-code-stop-claude-getting-lost-in-your-code)
  ↳ *part-of* `g02-0176`
  ↳ *example-of* `g02-0232`

- `g02-0206` *STATED* — The loops guide has 1 prompt and 6 numbered steps, with email-gated 'The catch' and 'Sources' sections.
  — [g-find-the-claude-code-loops-that-are-quietly-eating-your-limit](https://chen.media/guides/find-the-claude-code-loops-that-are-quietly-eating-your-limit)
  ↳ *part-of* `g02-0204`
  ↳ *example-of* `g02-0232`

- `g04-0013` *STATED* — Guide: 'The Four Habits Eating Your Claude Limit, and the Fix for Each' at https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each (1 prompt to copy, 10 numbered steps).
  — [g-the-four-habits-eating-your-claude-limit-and-the-fix-for-each](https://chen.media/guides/the-four-habits-eating-your-claude-limit-and-the-fix-for-each)
  ↳ *example-of* `g04-0243`

- `g04-0084` *STATED* — Guide: 'tokentab: See Where Every Claude Token Goes, as a Monthly Statement' at https://chen.media/guides/tokentab-see-where-every-claude-token-goes-as-a-monthly-statement (1 prompt, 4 steps; covers install, views, reading it and the catch).
  — [g-tokentab-see-where-every-claude-token-goes-as-a-monthly-statement](https://chen.media/guides/tokentab-see-where-every-claude-token-goes-as-a-monthly-statement)
  ↳ *example-of* `g04-0243`

- `g04-0145` *STATED* — Guides: 'How to Claim Your Monthly Claude Credits on Max and Team Plans' (https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) and its twin 'How to Get Your Monthly Claude Credits Back on Max and Team Plans' (https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans), 7 numbered steps each.
  — [g-how-to-claim-your-monthly-claude-credits-on-max-and-team-plans](https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans)
  ↳ *example-of* `g04-0243`

- `g04-0146` *STATED* — Guide: 'How a Claude Team Plan Claims Its Monthly Credits: What a Team of Five Gets' at https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets (7 numbered steps).
  — [g-how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets](https://chen.media/guides/how-a-claude-team-plan-claims-its-monthly-credits-what-a-team-of-five-gets)
  ↳ *example-of* `g04-0243`

- `g04-0241` *STATED* — Guide: 'Let Opus Advise While Sonnet Does the Routine Work' at https://chen.media/guides/let-opus-advise-while-sonnet-does-the-routine-work (1 prompt, 6 steps).
  — [g-let-opus-advise-while-sonnet-does-the-routine-work](https://chen.media/guides/let-opus-advise-while-sonnet-does-the-routine-work)
  ↳ *example-of* `g04-0243`

- `g05-0147` *STATED* — Claude Code docs: 'Each model has its own cache. Switching with /model means the next request reads the entire conversation history with no cache hits, even though the content is identical.'
  > “Each model has its own cache. Switching with /model means the next request reads the entire conversation history with no cache hits, even though the content is identical.”
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)
  ↳ *evidence-for* `g05-0144`
  ↳ *example-of* `g05-0323`
  ↳ *evidence-for* `g05-0315`

- `g05-0150` *STATED* — Claude Code docs: 'The fewer changes you make mid-task, the higher your cache hit rate.'
  > “The fewer changes you make mid-task, the higher your cache hit rate.”
  — [g-stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup](https://chen.media/guides/stop-wiping-your-claude-code-cache-the-model-switch-cost-and-a-four-rule-setup)
  ↳ *evidence-for* `g05-0149`

- `g05-0197` *STATED* — Claude Code docs: 'The session and weekly limits are shared across all models, so switching models doesn't restore access.'
  > “The session and weekly limits are shared across all models, so switching models doesn't restore access.”
  — [g-three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha](https://chen.media/guides/three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha)
  ↳ *evidence-for* `g05-0196`
  ↳ *example-of* `g05-0323`

- `g05-0205` *STATED* — The limit-myths guide includes a prompt that audits your setup and finds what's eating your limit (1 prompt to copy).
  — [g-three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha](https://chen.media/guides/three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha)
  ↳ *part-of* `g05-0195`

- `g06-0224` *CORE* — haiku-helper.md frontmatter: name: haiku-helper; description: Use for easy, low-risk jobs: reading logs, searching files, listing folders, renames, one-line edits.; model: haiku
  > “---
name: haiku-helper
description: Use for easy, low-risk jobs: reading logs, searching files, listing folders, renames, one-line edits.
model: haiku
---”
  — [g-make-your-claude-limit-last-the-haiku-helper-and-3-habits](https://chen.media/guides/make-your-claude-limit-last-the-haiku-helper-and-3-habits)
  ↳ *part-of* `g06-0222`

- `g09-0130` *STATED* — chen.media guide 'Find the Claude Skills Quietly Eating Your Limit: The Hidden /skill-doctor Command' (https://chen.media/guides/find-the-claude-skills-eating-your-limit-skill-doctor) has 5 prompts to copy and 7 numbered steps; sections: What /skill-doctor shows you; Run it; Turn off the ones you never use; Make it a habit.
  — [g-find-the-claude-skills-eating-your-limit-skill-doctor](https://chen.media/guides/find-the-claude-skills-eating-your-limit-skill-doctor)
  ↳ *example-of* `g09-0253`

- `g11-0078` *STATED* — Alex's tournament guide has a section on what running 100 Claudes costs.
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *leads-to* `g11-0080`
  ↳ *part-of* `g11-0057`

- `g11-0115` *STATED* — Alex's advisor guide covers what the advisor costs and when it's worth it, and when it isn't.
  — [g-put-fable-5-1-to-work-checking-opus-5-5](https://chen.media/guides/put-fable-5-1-to-work-checking-opus-5-5)
  ↳ *example-of* `g11-0003`
  ↳ *qualifies* `g11-0100`
  ↳ *evidence-for* `g04-0239`

- `g12-0099` *STATED* — Anthropic's post 'Reducing cost and improving performance with Claude Platform': https://claude.com/blog/reducing-cost-and-improving-performance-with-claude-platform
  — [g-clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit](https://chen.media/guides/clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit)
  ↳ *evidence-for* `g12-0096`
  ↳ *example-of* `g12-0300`

- `g12-0112` *STATED* — A free tool prices every token in your Claude Code history at the real API rate.
  — [g-what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything)
  ↳ *part-of* `g12-0111`
  ↳ *leads-to* `g12-0114`

- `g12-0120` *STATED* — Anthropic's Claude Code docs page 'Manage costs effectively': https://code.claude.com/docs/en/costs
  — [g-what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything](https://chen.media/guides/what-your-claude-plan-really-costs-and-3-habits-that-stop-claude-re-reading-everything)
  ↳ *evidence-for* `g12-0119`
  ↳ *example-of* `g12-0300`

- `g14-0129` *STATED* — Alex's guide 'How to Use AWS Free Tier Credits with Claude on Amazon Bedrock' (category: Claude Code) is the FREE reel setup guide for eligible new AWS customers.
  > “The FREE reel setup guide for eligible new AWS customers”
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *example-of* `g14-0346`

- `g14-0164` *STATED* — AWS offer and account plan details: https://aws.amazon.com/free/free-tier-faqs/
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *evidence-for* `g14-0130`

- `g14-0165` *STATED* — AWS credit-earning activities: https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/free-tier-plans-activities.html
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *evidence-for* `g14-0148`

- `g16-0039` *STATED* — Three free repos cut three different parts of what Claude Code costs: deepclaude (the RATE), caveman (the VOLUME) and super-token-saver (the WASTE).
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you)
  ↳ *example-of* `g16-0001`
  ↳ *example-of* `g16-0008`

- `g16-0099` *STATED* — 15 Claude mistakes quietly cost you tokens; his guide gives the setting path and the source for every one.
  > “The three from the video, plus twelve more, with the setting path and the source for every one”
  — [g-15-claude-mistakes-that-are-quietly-costing-you-tokens](https://chen.media/guides/15-claude-mistakes-that-are-quietly-costing-you-tokens)
  ↳ *example-of* `g16-0001`

- `g18-0220` *STATED* — github.com/open-free-llm-api/awesome-freellm-apis is a directory of 134+ free LLM APIs from 40+ providers, listing the rate limit, the context window and a direct link to get a key for each.
  — [g-134-free-llm-apis-and-how-to-point-your-editor-at-them](https://chen.media/guides/134-free-llm-apis-and-how-to-point-your-editor-at-them)
  ↳ *evidence-for* `g17-0141`

- `g19-0001` *STATED* — Alex Chen's chen.media guide '28 Ways to Stop Hitting Claude Code Usage Limits' (category: Claude Code) lists twenty-eight ways to make Claude Code do the same work for a fraction of the tokens, starting with the three from his video.
  > “Twenty-eight ways to make Claude Code do the same work for a fraction of the tokens, starting with the three from the video.”
  — [g-28-ways-to-stop-hitting-claude-code-usage-limits](https://chen.media/guides/28-ways-to-stop-hitting-claude-code-usage-limits)

- `g19-0091` *STATED* — Alex's chen.media guide 'Run Gemini Inside Claude Code, With Claude as the Boss' (category: Claude Code) gives the /route setup that makes Claude the boss and Gemini 3.6 the builder.
  > “The /route setup that makes Claude the boss and Gemini 3.6 the builder”
  — [g-run-gemini-inside-claude-code-with-claude-as-the-boss](https://chen.media/guides/run-gemini-inside-claude-code-with-claude-as-the-boss)
  ↳ *example-of* `g19-0011` — right model right job, across vendors
  ↳ *analogy-for* `g19-0005` — boss plans, cheaper model builds, like opusplan

- `g19-0100` *STATED* — The /route guide has a 'Why It Works: The math' section on the usage savings, plus Honest Notes.
  > “The math”
  — [g-run-gemini-inside-claude-code-with-claude-as-the-boss](https://chen.media/guides/run-gemini-inside-claude-code-with-claude-as-the-boss)
  ↳ *part-of* `g19-0091`
  ↳ *evidence-for* `g19-0092`

- `g19-0172` *STATED* — A prebuilt Claude Code Router desktop app is on the releases page for people who would rather not touch the terminal.
  > “A prebuilt desktop app is available on the releases page”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *contrast* `g19-0168` — no terminal needed

- `g19-0173` *STATED* — Full Claude Code Router docs live at ccrdesk.top.
  > “Full docs live at ccrdesk.top.”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *part-of* `g19-0156`

- `g21-0117` *STATED* — Alex's chen.media guide 'Turn Your Whole Backlog Into Finished Plans in One Night' (section: Prompting) gives the mining prompt, the blueprint template and the overnight batch loop to turn a backlog into build-ready blueprints.
  — [g-turn-your-whole-backlog-into-finished-plans-in-one-night](https://chen.media/guides/turn-your-whole-backlog-into-finished-plans-in-one-night)

- `g21-0169` *STATED* — The Fable 5 guide ends with a section 'Maxing everything vs using it well'.
  — [g-the-fable-5-guide-effort-memory-and-self-verification](https://chen.media/guides/the-fable-5-guide-effort-memory-and-self-verification)
  ↳ *part-of* `g21-0159`
  ↳ *qualifies* `g21-0168`

- `g22-0044` *STATED* — Alex Chen's chen.media guide 'Stop Running Every Task Through the Expensive Model' (section: Agent teams) gives 4 prompts for a Sol to Terra to Luna model line that gets flagship quality for a fraction of the cost.
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)

- `y03-0017` *STATED* — A free tool reads your Claude Code history and prices every token at the real API rate, showing what your subscription would cost if you paid per token.
  — [_I57Pc36DIg](https://youtu.be/_I57Pc36DIg)
  ↳ *evidence-for* `g12-0112`
  ↳ *leads-to* `y03-0019`
  ↳ *part-of* `y03-0024`

### result

- `g02-0039` *STATED* — On Context Mode's own README test, 315 KB of tool output becomes 5.4 KB, a 98% cut.
  — [g-stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode)
  ↳ *evidence-for* `g02-0037`

- `g03-0106` *STATED* — Caveman ships its own test of how much shorter its answers are, covered in the locked section "What its own test shows".
  — [g-make-claude-answer-in-fewer-words-with-the-caveman-skill](https://chen.media/guides/make-claude-answer-in-fewer-words-with-the-caveman-skill)
  ↳ *evidence-for* `g03-0100`

- `g03-0236` *STATED* — In the README's test (Claude Sonnet 5.5, 3 topics, 3 runs each) the skill's Markdown-draft approach took 612 tokens and 12 seconds versus 4,893 tokens and 31 seconds when Claude hand-writes the HTML.
  — [g-answer-me-with-html-make-claude-answer-with-one-clean-page-not-a-wall-of-text](https://chen.media/guides/answer-me-with-html-make-claude-answer-with-one-clean-page-not-a-wall-of-text)
  ↳ *evidence-for* `g03-0235`

- `g04-0078` *STATED* — In the tokentab repo's own sample statement, refactoring took 36% of a month's spend.
  — [g-tokentab-see-where-every-claude-token-goes-as-a-monthly-statement](https://chen.media/guides/tokentab-see-where-every-claude-token-goes-as-a-monthly-statement)
  ↳ *evidence-for* `g04-0080`
  ↳ *example-of* `g04-0077`

- `g04-0079` *STATED* — In the tokentab repo's sample statement, one model took most of the month's spend.
  — [g-tokentab-see-where-every-claude-token-goes-as-a-monthly-statement](https://chen.media/guides/tokentab-see-where-every-claude-token-goes-as-a-monthly-statement)
  ↳ *evidence-for* `g04-0080`

- `g05-0111` *STATED* — The Effortless guide reports what Effortless measured on Opus 5.5 (section 'What it measured').
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless)
  ↳ *part-of* `g05-0098`
  ↳ *evidence-for* `g05-0112`

- `g06-0232` *CORE* — In Alex's test, Opus and Haiku 5.5 were given the same job and both got every answer right, but Haiku 5.5 cost 96% less.
  — [g-send-claude-s-easy-jobs-to-haiku-5-5-with-one-helper-file](https://chen.media/guides/send-claude-s-easy-jobs-to-haiku-5-5-with-one-helper-file)
  ↳ *evidence-for* `g06-0264`
  ↳ *evidence-for* `g06-0212` — why Haiku 5.5 matters
  ↳ *evidence-for* `y02-0023`

- `g22-0049` *STATED* — The Sol-Terra-Luna factory gives Sol-level quality on the whole batch while you pay Luna prices for the labor.
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)

- `g23-0022` *STATED* — The audit prompt returns a ranked list of your repeated work, such as the weekly report, the outreach emails, and the invoices.
  — [g-clone-the-smart-model-s-brain-into-the-cheap-one](https://chen.media/guides/clone-the-smart-model-s-brain-into-the-cheap-one)
  ↳ *leads-to* `g23-0024`

- `r02-0253` *STATED* — COST watch: CaptionPal uses the most expensive-sounding model `"best-large"` with no max tokens and no cache, makes 3 separate calls instead of one asking for 3 captions, and allows unlimited description length.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0246`
  ↳ *leads-to* `r02-0292`

- `y03-0009` *STATED* — The same $1,000 gets about 5 times fewer messages on Fable than on Haiku (about 3,200 versus about 15,000).
  — [FqOzuuip5iA](https://youtu.be/FqOzuuip5iA)
  ↳ *evidence-for* `y03-0010`

- `y03-0020` *STATED* — Alex got over 20 times more Claude usage than he paid for by being on a plan instead of the API.
  — [_I57Pc36DIg](https://youtu.be/_I57Pc36DIg)
  ↳ *evidence-for* `g12-0114` — video says over 20x, guide says over 22x ($4,500/$200)

### style

- `g16-0104` *STATED* — Nothing in the 15-mistakes list is a prompt template; every item is a thing to stop doing or a setting to change.
  > “Nothing here is a prompt template.”
  — [g-15-claude-mistakes-that-are-quietly-costing-you-tokens](https://chen.media/guides/15-claude-mistakes-that-are-quietly-costing-you-tokens)
  ↳ *qualifies* `g16-0099`

- `r03-0169` *CORE* — Alex's skill READMEs disclose up front that runs count toward your Claude plan's usage (one Claude Code run per /learn review; five sub-agents per /linkedin-roast run).
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill) [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *evidence-for* `r01-0017`

### warning

- `g02-0195` *STATED* — A forgotten Claude Code /loop wakes up every few minutes and sends your whole chat again.
  > “A forgotten /loop wakes up every few minutes and sends your whole chat again.”
  — [g-find-the-claude-code-loops-that-are-quietly-eating-your-limit](https://chen.media/guides/find-the-claude-code-loops-that-are-quietly-eating-your-limit)

- `g03-0029` *STATED* — Tag a few big files with @ and a lot of your chat becomes files you may not have needed.
  — [g-stop-file-mentions-from-pasting-whole-files-into-your-claude-chat](https://chen.media/guides/stop-file-mentions-from-pasting-whole-files-into-your-claude-chat)
  ↳ *example-of* `g03-0001`

- `g03-0189` *STATED* — If you walk away, idle /goal check-ins can start by themselves and eat your limit.
  — [g-stop-claude-goal-check-ins-from-eating-your-limit](https://chen.media/guides/stop-claude-goal-check-ins-from-eating-your-limit)
  ↳ *example-of* `g03-0001`

- `g03-0212` *STATED* — If your session runs your priciest model, so do all its helper agents.
  — [g-run-every-claude-helper-agent-on-haiku](https://chen.media/guides/run-every-claude-helper-agent-on-haiku)
  ↳ *because* `g03-0213`

- `g03-0243` *STATED* — A big research job can use up all 200 web searches before it finishes.
  — [g-stop-claude-running-out-of-web-searches](https://chen.media/guides/stop-claude-running-out-of-web-searches)
  ↳ *leads-to* `g03-0244`

- `g04-0122` *CORE* — The monthly Claude API credits on Max and Team plans are not applied for you: you have to claim them yourself.
  > “you have to claim them yourself”
  — [g-how-to-claim-your-monthly-claude-credits-on-max-and-team-plans](https://chen.media/guides/how-to-claim-your-monthly-claude-credits-on-max-and-team-plans) [g-how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans](https://chen.media/guides/how-to-get-your-monthly-claude-credits-back-on-max-and-team-plans)
  ↳ *qualifies* `g04-0121`

- `g05-0164` *STATED* — Claude Code docs say max effort 'may show diminishing returns and is prone to overthinking.'
  > “may show diminishing returns and is prone to overthinking.”
  — [g-stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor](https://chen.media/guides/stop-burning-your-limit-on-thinking-give-each-claude-code-subagent-its-own-effor)
  ↳ *evidence-for* `g05-0166`
  ↳ *example-of* `g05-0323`
  ↳ *evidence-for* `y01-0149`

- `g05-0196` *STATED* — Limit myth 1 (false): switching to Sonnet brings you back when you hit your session limit.
  — [g-three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha](https://chen.media/guides/three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha)
  ↳ *part-of* `g05-0195`

- `g05-0202` *STATED* — Limit myth 2 (false): /compact saves your limit — /compact isn't free.
  — [g-three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha](https://chen.media/guides/three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha)
  ↳ *part-of* `g05-0195`
  ↳ *contradicts* `g19-0003` — 28-ways guide lists /compact as a Tier 1 usage-limit fix vs myths guide: "/compact saves your limit" is a myth, /compact is not free

- `g05-0203` *STATED* — Limit myth 3 (false): a quick question is cheap — a quick question in an old chat costs the whole chat.
  — [g-three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha](https://chen.media/guides/three-claude-limit-myths-busted-by-claude-s-own-docs-and-a-prompt-that-finds-wha)
  ↳ *part-of* `g05-0195`
  ↳ *because* `g05-0145` — a quick question in an old chat re-sends the whole chat
  ↳ *evidence-for* `g19-0019`

- `g07-0200` *STATED* — Claude Code Projects can eat your usage, so keep an eye on usage while it runs ('Step 6: keep an eye on usage'; tips email-gated).
  — [g-set-up-claude-code-projects](https://chen.media/guides/set-up-claude-code-projects)
  ↳ *part-of* `g07-0202`

- `g07-0206` *STATED* — Nothing happens with the Max/Team API credits until you claim them.
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *part-of* `g07-0203`
  ↳ *because* `g07-0216`
  ↳ *evidence-for* `g04-0122`

- `g07-0207` *STATED* — Whatever Max/Team API credit you don't use disappears at the end of each month.
  — [g-claim-claude-max-team-monthly-api-credits](https://chen.media/guides/claim-claude-max-team-monthly-api-credits)
  ↳ *part-of* `g07-0203`
  ↳ *because* `g07-0220`
  ↳ *evidence-for* `g06-0211`

- `g10-0211` *STATED* — Design work draws from the same pool as the rest of your Claude use, Claude Code included, so an afternoon of slides and landing pages can leave you rate limited when you sit down to code.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *qualifies* `g10-0199`
  ↳ *evidence-for* `g10-0269`

- `g11-0130` *STATED* — Ultrafast burns your allowance 8x as fast.
  — [g-is-openais-500-ultrafast-plan-worth-it](https://chen.media/guides/is-openais-500-ultrafast-plan-worth-it)
  ↳ *qualifies* `g11-0126`
  ↳ *qualifies* `g11-0120`

- `g12-0244` *STATED* — Lower-priority mode still counts toward your weekly limit, so it is for finishing work, not starting fresh.
  — [g-keep-using-claude-code-after-you-hit-your-usage-limit](https://chen.media/guides/keep-using-claude-code-after-you-hit-your-usage-limit)
  ↳ *qualifies* `g12-0241`
  ↳ *part-of* `g12-0249`

- `g12-0249` *STATED* — Guide section 'The catch: your weekly limit' covers how lower-priority use still drains the weekly limit (body email-gated).
  — [g-keep-using-claude-code-after-you-hit-your-usage-limit](https://chen.media/guides/keep-using-claude-code-after-you-hit-your-usage-limit)
  ↳ *part-of* `g12-0238`

- `g14-0134` *STATED* — Existing or previous AWS customers do not qualify for the new-customer Free Tier credits.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *qualifies* `g14-0130`

- `g14-0138` *STATED* — An AWS Paid plan can charge beyond the eligible credits.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *qualifies* `g14-0133`

- `g14-0143` *STATED* — If a Bedrock model requires a Paid plan, check its pricing and whether your credits cover it before deciding to upgrade.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *example-of* `g14-0138`

- `g14-0147` *STATED* — Claude calls on Amazon Bedrock are metered model usage, even when eligible credits pay for them.
  > “This is metered model usage, even when eligible credits pay for it.”
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *because* `g14-0146`
  ↳ *qualifies* `g14-0131`
  ↳ *evidence-for* `g14-0350`

- `g14-0150` *STATED* — Complete only the AWS credit activities you want to learn; some create resources that keep accruing charges until deleted.
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *qualifies* `g14-0148`
  ↳ *because* `g14-0151` — cleanup needed because resources accrue

- `g14-0152` *STATED* — An AWS Budget alert is a notification, not a hard spending stop.
  > “A budget alert is a notification, not a hard spending stop.”
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *qualifies* `g14-0151`

- `g14-0163` *STATED* — Do not create extra AWS accounts to bypass Free Tier eligibility rules.
  > “Do not create extra accounts to bypass eligibility rules.”
  — [g-aws-free-credits-claude-bedrock](https://chen.media/guides/aws-free-credits-claude-bedrock)
  ↳ *qualifies* `g14-0134`

- `g15-0171` *STATED* — The part almost nobody warns you about with the boss loop is the token cost: run naively it can eat your entire token budget in a single afternoon.
  — [g-the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer](https://chen.media/guides/the-boss-loop-run-a-team-of-claude-sub-agents-under-one-strict-reviewer)
  ↳ *qualifies* `g15-0167`
  ↳ *leads-to* `g15-0172`
  ↳ *contrast* `g15-0096` — both verification loops spend extra tokens; the boss loop fans out to a team
  ↳ *example-of* `g13-0305`

- `g16-0053` *STATED* — One setting undoes most of the saving from the three cost-cutting repos.
  > “the one setting that undoes most of the saving”
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you)
  ↳ *qualifies* `g16-0039`

- `g16-0110` *STATED* — Token mistake 3: leaving tool access on automatic.
  > “3. Leaving tool access on automatic”
  — [g-15-claude-mistakes-that-are-quietly-costing-you-tokens](https://chen.media/guides/15-claude-mistakes-that-are-quietly-costing-you-tokens)
  ↳ *part-of* `g16-0099`
  ↳ *example-of* `g18-0113`

- `g16-0115` *STATED* — Token mistake 8: re-uploading the same files every conversation.
  > “8. Re uploading the same files every conversation”
  — [g-15-claude-mistakes-that-are-quietly-costing-you-tokens](https://chen.media/guides/15-claude-mistakes-that-are-quietly-costing-you-tokens)
  ↳ *part-of* `g16-0099`
  ↳ *example-of* `g15-0015`

- `g16-0116` *STATED* — Token mistake 9: not caching a stable prefix.
  > “9. Not caching a stable prefix”
  — [g-15-claude-mistakes-that-are-quietly-costing-you-tokens](https://chen.media/guides/15-claude-mistakes-that-are-quietly-costing-you-tokens)
  ↳ *part-of* `g16-0099`
  ↳ *example-of* `g16-0046` — an uncached stable prefix is tokens paid for twice
  ↳ *example-of* `g05-0146`

- `g16-0117` *STATED* — Token mistake 10: never clearing a thread.
  > “10. Never clearing a thread”
  — [g-15-claude-mistakes-that-are-quietly-costing-you-tokens](https://chen.media/guides/15-claude-mistakes-that-are-quietly-costing-you-tokens)
  ↳ *part-of* `g16-0099`
  ↳ *example-of* `g16-0040` — clearing context is part of the one-lever advice
  ↳ *evidence-for* `g12-0128`

- `g16-0119` *STATED* — Token mistake 12: using one conversation for unrelated jobs.
  > “12. One conversation for unrelated jobs”
  — [g-15-claude-mistakes-that-are-quietly-costing-you-tokens](https://chen.media/guides/15-claude-mistakes-that-are-quietly-costing-you-tokens)
  ↳ *part-of* `g16-0099`
  ↳ *qualifies* `g16-0117`
  ↳ *evidence-for* `y01-0030`

- `g16-0122` *STATED* — Token mistake 15: treating extended thinking as free.
  > “15. Treating extended thinking as free”
  — [g-15-claude-mistakes-that-are-quietly-costing-you-tokens](https://chen.media/guides/15-claude-mistakes-that-are-quietly-costing-you-tokens)
  ↳ *part-of* `g16-0099`
  ↳ *example-of* `g10-0197`
  ↳ *evidence-for* `g05-0165`

- `g16-0166` *STATED* — Gauntlet Loops can burn your month of usage; run them with that in mind.
  > “Running it without burning your month”
  — [g-the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work](https://chen.media/guides/the-gauntlet-loop-the-three-line-prompt-where-claude-grades-its-own-work)
  ↳ *qualifies* `g16-0156`
  ↳ *qualifies* `g16-0122` — loops and extended thinking both quietly spend the limit
  ↳ *example-of* `g13-0305`

- `g17-0122` *STATED* — The savings number that videos quote for context compression is wrong, per Alex Chen.
  > “The number the videos get wrong”
  — [g-cut-what-your-coding-agent-sends-to-the-model](https://chen.media/guides/cut-what-your-coding-agent-sends-to-the-model)
  ↳ *qualifies* `g17-0120`
  ↳ *example-of* `g17-0308`

- `g21-0162` *CORE* — Fable 5 can quietly spend far more tokens than a task needs.
  > “it can quietly spend far more tokens than a task needs”
  — [g-the-fable-5-guide-effort-memory-and-self-verification](https://chen.media/guides/the-fable-5-guide-effort-memory-and-self-verification)
  ↳ *part-of* `g21-0161`

- `g22-0017` *STATED* — If you find yourself paying flagship prices to USE the Judgment Vault later, you wired step 4 (the cheap-model harness) wrong.
  — [g-bank-the-judgment-calls-not-just-the-output](https://chen.media/guides/bank-the-judgment-calls-not-just-the-output)
  ↳ *qualifies* `g22-0009`

- `g22-0062` *STATED* — In the model line, Sol never writes a single unit itself.
  — [g-stop-running-every-task-through-the-expensive-model](https://chen.media/guides/stop-running-every-task-through-the-expensive-model)
  ↳ *qualifies* `g22-0061`

- `r01-0017` *CORE* — Every sub-agent call and every queued job in Alex's skills counts toward your Claude plan's usage, and his READMEs state the call count up front.
  — [r-court-skill](https://github.com/alexyc9381/court-skill) [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill) [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *qualifies* `r01-0016` — independence costs one call per reviewer
  ↳ *example-of* `g14-0350`

- `r01-0061` *STATED* — Every /agency night-shift job counts toward your Claude plan's usage.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *qualifies* `r01-0048`
  ↳ *example-of* `r01-0017`

- `r04-0016` *CORE* — Alex's multi-agent skills warn up front that the agents spend your plan: every shark sub-agent counts toward your Claude plan's usage, and every night-crew routine run uses plan usage like a normal session.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill) [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *evidence-for* `r01-0017`

- `y01-0135` *CORE* — Picking the wrong Claude model for tasks burns through your usage limit, and you can run out of usage for hours.
  > “If you pick the wrong model for tasks, you will burn through your usage limit and run out of usage for hours.”
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *evidence-for* `y02-0187`
  ↳ *leads-to* `y01-0138` — default to the workhorse to avoid burning limits

- `y01-0148` *STATED* — Max effort burns through your message limits fast and responses take much longer.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *evidence-for* `g10-0197`
  ↳ *qualifies* `y01-0145`

- `y02-0097` *CORE* — Catch with the Projects team update: every Claude in the team runs Opus at full power by default, which eats your limit really quickly.
  > “they all run Opus at full power by default which eats your limit really quickly”
  — [GF2xgaEnQ0o](https://youtu.be/GF2xgaEnQ0o) [g6ZnVE4kQCk](https://youtu.be/g6ZnVE4kQCk)
  ↳ *example-of* `g03-0212`
  ↳ *part-of* `y02-0092`
  ↳ *leads-to* `y02-0098`

- `y03-0013` *STATED* — A big PDF uploaded to a Claude chat gets reread in every message after you upload it.
  — [Rgb7FFLwz60](https://youtu.be/Rgb7FFLwz60)
  ↳ *evidence-for* `g15-0015`
  ↳ *part-of* `y03-0012`
  ↳ *evidence-for* `y03-0025`

- `y03-0015` *STATED* — Claude plugins load into every chat even when you don't use them.
  — [Rgb7FFLwz60](https://youtu.be/Rgb7FFLwz60)
  ↳ *evidence-for* `g18-0283`
  ↳ *part-of* `y03-0012`
  ↳ *evidence-for* `y03-0107`

- `y04-0022` *STATED* — The free Claude Code cloud credit had to be claimed within two weeks.
  > “you have two weeks to claim it so you have to act fast”
  — [BgOlXwLlBrY](https://youtu.be/BgOlXwLlBrY) [QnzAaLZ70c0](https://youtu.be/QnzAaLZ70c0) [OyKQsxpeSLY](https://youtu.be/OyKQsxpeSLY)
  ↳ *evidence-for* `g13-0102` — two-week claim window ~ Sept 23 to Oct 7 2026
  ↳ *qualifies* `y04-0018`

- `y04-0043` *STATED* — The Darwin Loop burns through tokens fast.
  > “But this burns through tokens fast”
  — [gUOs9YjmZDo](https://youtu.be/gUOs9YjmZDo)
  ↳ *evidence-for* `g13-0239`
  ↳ *because* `y04-0042` — every round multiplies the candidates

- `y04-0053` *STATED* — The Swarm Loop burns through tokens fast.
  > “But this burns through tokens fast.”
  — [kDh_gdXsJJU](https://youtu.be/kDh_gdXsJJU) [PG_HanOn_KE](https://youtu.be/PG_HanOn_KE) [jw25LS4GgUg](https://youtu.be/jw25LS4GgUg)
  ↳ *evidence-for* `g13-0253`
  ↳ *because* `y04-0052` — re-checking loop until every flag is fixed

<!-- AUTO:atoms END -->
