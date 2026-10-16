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
