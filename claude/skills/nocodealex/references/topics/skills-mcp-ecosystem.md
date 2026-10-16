# Skills, plugins, MCP servers and open-source tools

Alex Chen covers this ecosystem as a shopping list you vet before you install. He does not treat it as a catalogue to hoard. Most of his guides here follow one template: a tool, the reason it matters, a numbered install order, and an honest "the catch" section.

## What he believes (CORE first)

- **A skill is a folder with a SKILL.md.** It holds YAML frontmatter (name and description) followed by markdown instructions, and that is the whole format (`g18-0100`, `g15-0044`). "Skills are not prompts": you install one once and Claude keeps the capability (`g18-0084`, `y01-0180`). Project instructions (AGENTS.md) hold rules for a whole project, while a skill holds the process for one job (`y01-0070`).
- **The description is the routing surface.** Claude reads each description and turns the matching skill on by itself; you never pick from a menu (`g15-0045`, `g17-0228`). A vague description means the skill never fires (`g17-0229`). INFERRED: this is why The Agency guide says routing decides whether the pack is any use (`g15-0189`).
- **The file is the product, so read it.** Skills and agents are plain markdown, so read them before you trust them (`g17-0311`). His guides open with "Read this before you install anything" (`g15-0185`).
- **Free usually means a free tier, not unlimited** (`g18-0126`). Free-for-paid swaps always carry a caveat about where the paid tool still wins (`g18-0287`, `g16-0008`).
- **Local-first ownership.** No telemetry, state kept in local folders, "your domain, your server, your files" (`g02-0240`, `y03-0208` INFERRED, `g11-0029`).
- **Installable tools beat prompt packs.** He says it repeatedly: "not a prompt pack", "not prompt templates" (`g15-0179`).

## Frameworks and methods

**Start small, sequence everything.** One job, one skill, one clear test of the result (`g13-0281`). Begin with one MCP server, a smaller ECC profile, and a one-week trial of any free tool, and don't install all five animation skills at once (`g18-0285`, `g18-0011`). Every tool guide has an "order to install them in" section (`g16-0007`). Order matters more than the list itself: if you install outbound-acting marketing skills before your brand system exists, you get an agent running outbound against nothing (`g17-0010`, `g17-0008`).

**Vet, then install.**
1. Check the author, install count and stars. Find Skills prefers 1K+ installs, is wary of anything under 100 installs or from repos under 100 stars, and ranks Vercel, Anthropic and Microsoft first (`g10-0261`, `g10-0263`, `g10-0262`).
2. Scan the skill with NVIDIA's SkillSpector. It checks 71 attack patterns in 17 categories and returns a 0-100 risk score with SAFE, CAUTION or DO NOT INSTALL (`g03-0040`, `g03-0046`). The reason: in NVIDIA's set of 31,132 skills, 26.1% had a vulnerability and 5.2% showed likely malicious intent (`g03-0038`, `g03-0039`).
3. Prefer human-gated tools. github-triage changes nothing until you say yes (`g02-0162`), Atticus never sends the email replies it writes (`g02-0137`), and the Meta Ads connector creates everything PAUSED (`g22-0152`).

**Alex's own skill template** (INFERRED, `r01-0021`): one slash command, a hidden output folder (`.court/`, `.shark/`) that touches nothing else (`r01-0014`, `r04-0010`), and a Python helper called as `python3 "${CLAUDE_SKILL_DIR}/<tool>.py" <command>` so state lives in code (`r04-0009`). The frontmatter has a long description ending in "Use when the user ..." triggers, plus `license: MIT` and `version "1.0.0"` (`r04-0006`). Tests run with `python3 -m unittest discover -s tests` (`r01-0007`). Every skill is free, MIT, no signup and no key (`r01-0001`).

## Exact commands

- **Plugins:** `/plugin marketplace add owner/repo` → `/plugin install name@marketplace` → `/reload-plugins` (`g18-0160`).
- **Alex's skills:** paste `https://github.com/alexyc9381/<repo>` plus "Install this skill, then confirm /<name> works." (`r01-0003`, `r04-0004`). Each repo is also its own marketplace: `/plugin install court-skill@court-skill` (`r01-0004`). Other routes: `npx skills add alexyc9381/<repo>`, or `cp -r <repo>/skills/<name> ~/.claude/skills/` (`r04-0005`, `g05-0311`).
- **Anthropic:** `/plugin marketplace add anthropics/skills`, then `/plugin install document-skills@anthropic-agent-skills` (`g18-0105`, `g18-0106`).
- **Superpowers:** `/plugin marketplace add obra/superpowers-marketplace`, then `/plugin install superpowers@superpowers-marketplace` (`g21-0009`).
- **MCP:** `claude mcp add context7 -- npx -y @upstash/context7-mcp` (no key) (`g20-0276`, `g20-0277`). Other servers: `claude mcp add playwright npx @playwright/mcp@latest` (`g21-0015`) and `claude mcp add exa -- npx -y exa-mcp-server` (`g20-0260`). Keys go in `-e KEY=value` (INFERRED, `g20-0279`). MCP is "what gives Claude hands" (`g16-0190`).
- **Hub tools:** Find Skills (Vercel Labs, MIT) (`g10-0247`). claude-mem runs capture → compress → inject on its own and never saves anything marked private (`g13-0139`–`g13-0145`). ECC needs Node 18+, and a marketplace install updates differently from a clone (`g14-0229`, `g18-0010`).
- **Connectors:** a plugin bundles skills, connectors, commands and agents, and a connector is an MCP server (`g12-0162`, `g12-0164`). The Free plan allows one custom connector (`g22-0155`). A `127.0.0.1` URL fails because connectors must be reachable from Anthropic's IP ranges (`g20-0038`, `g20-0039`). On Windows, mcp-remote hangs for 60s (issue 296) (`g20-0045`).
- **Long skill files:** Claude may read only the first 100 lines of a reference file, so rules near the bottom can be skipped (`g05-0207`, `g05-0211`).

## Contradictions and caveats

- **Find Skills installs:** 3.8M (`g07-0033`) vs 3.6M (`g10-0248`).
- **How many other agents skills reach:** 75+ (`y03-0104`) vs about 40 for `npx skills` (`g18-0086`).
- **Skill counts:** 50,000 (`g23-0099`), 90,000 (`y04-0113`), a million (`g07-0025`) and 1,499,600 (`g10-0256`).
- **The Agency:** 230+ agents (`g08-0096`) at 158,347 stars (`g08-0104`).
- **claude-mem stars:** 94K (`g13-0137`) vs 90,651 (`g17-0088`).
- **Star counts in general:** syndicated counts go stale, and for a harness like ECC coverage matters more than stars (`g17-0088`, `g18-0012`).
- **Tool swaps:** Higgsfield vs Runway, and v0 ranked top (`g19-0214`) vs "replace v0 with Bolt.new" (`g23-0189`).
- **Gated material:** many "catch" and install sections are email-gated or locked, so the store records only their headings (toc-only), e.g. `g07-0027`, `g10-0255`.

## What to load next

Hooks, settings and mods → the Claude Code optimisation topic. His multi-Claude panels (/court, /shark, /agency) → the panels topic. Paid-to-free swap tables → `atoms.jsonl` filtered on this topic, type `opinion`.

---

## Atom index

<!-- AUTO:atoms BEGIN -- regenerated by build_topics.py, do not edit below -->

*1688 atoms.*

### analogy

- `g18-0157` *STATED* — Adding a plugin marketplace and then installing plugins is like adding an app store, then choosing apps.
  > “Think of it as adding an app store, then choosing apps.”
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *analogy-for* `g18-0156`

### bio

- `g02-0186` *STATED* — Chrome Relay is by Alexey Indeev.
  — [g-let-claude-use-your-signed-in-chrome-in-the-background](https://chen.media/guides/let-claude-use-your-signed-in-chrome-in-the-background)
  ↳ *part-of* `g02-0185`

- `g08-0050` *STATED* — The Craft apps were released by developer Brandon Thomas, of ArtCraft, as a suite of free open-source apps made to copy Adobe's.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *part-of* `g08-0049`

- `g11-0060` *STATED* — The 100-Claude tournament skill was built by an outside developer; Alex covers it as a free tool rather than one of his own.
  > “A developer built a free skill”
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *qualifies* `g11-0057`

### caveat

- `g01-0068` *STATED* — khan-explainer renders the MP4 on your Mac.
  — [g-make-khan-academy-style-videos-with-claude](https://chen.media/guides/make-khan-academy-style-videos-with-claude)
  ↳ *qualifies* `g01-0066`
  ↳ *example-of* `g01-0189`
  ↳ *example-of* `g01-0196`

- `g01-0085` *INFERRED* — Show Your Work's QuickTime option suggests it is aimed at macOS users.
  — [g-show-your-work-see-every-screenshot-and-video-claude-makes-right-in-your-termina](https://chen.media/guides/show-your-work-see-every-screenshot-and-video-claude-makes-right-in-your-termina)
  ↳ *qualifies* `g01-0082`

- `g01-0180` *STATED* — The Scientific Agent Skills guide flags a catch about keys and tools (its 'The catch' section is gated).
  — [g-give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills](https://chen.media/guides/give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills)
  ↳ *qualifies* `g01-0177`
  ↳ *qualifies* `g01-0182`
  ↳ *example-of* `g01-0189`

- `g02-0033` *STATED* — Context Mode comes with a catch about its licence, covered in the email-gated 'The catch' section of the guide.
  > “the catch about its licence”
  — [g-stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode)
  ↳ *qualifies* `g02-0031`
  ↳ *example-of* `g02-0233`

- `g02-0193` *STATED* — The Chrome Relay vs agent-browser scores are the author's own numbers on the author's own test page.
  > “(the author's numbers)”
  — [g-let-claude-use-your-signed-in-chrome-in-the-background](https://chen.media/guides/let-claude-use-your-signed-in-chrome-in-the-background)
  ↳ *qualifies* `g02-0192`
  ↳ *example-of* `g02-0236`

- `g03-0123` *STATED* — The code intelligence plugin does not include the language server: install the binary first and make sure it is on the PATH of the shell you start claude from.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *qualifies* `g03-0122`
  ↳ *part-of* `g03-0138`

- `g04-0015` *STATED* — Academic Research Skills is free for non-commercial use only.
  > “(free for non-commercial use)”
  — [g-academic-research-skills-make-claude-check-every-source-in-your-paper-is-real](https://chen.media/guides/academic-research-skills-make-claude-check-every-source-in-your-paper-is-real)
  ↳ *qualifies* `g04-0014`
  ↳ *example-of* `g04-0252`

- `g04-0196` *STATED* — Anthropic's study did not test Vibewise; Alex says to treat it as the reason the plugin exists, not as a result for the plugin.
  > “Treat it as the reason the plugin exists, not as a result for the plugin.”
  — [g-ai-coders-scored-17-lower-on-a-quiz-make-claude-teach-you-with-the-free-vibewise](https://chen.media/guides/ai-coders-scored-17-lower-on-a-quiz-make-claude-teach-you-with-the-free-vibewise)
  ↳ *qualifies* `g04-0176`
  ↳ *example-of* `g04-0242`
  ↳ *evidence-for* `g05-0026`

- `g05-0025` *STATED* — Anthropic's study did not test Vibewise itself.
  — [g-turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin](https://chen.media/guides/turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin)
  ↳ *qualifies* `g05-0001`

- `g05-0030` *STATED* — The Vibewise guide has a section 'What to know before you rely on it' — caveats about depending on the plugin.
  — [g-turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin](https://chen.media/guides/turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin)
  ↳ *qualifies* `g05-0001`

- `g05-0040` *INFERRED* — The Chrome Relay guide frames setup as 'once per Mac', so the documented path targets macOS; Windows users should check the repo first.
  — [g-let-claude-use-your-real-chrome-signed-in-in-background-tabs](https://chen.media/guides/let-claude-use-your-real-chrome-signed-in-in-background-tabs)
  ↳ *qualifies* `g05-0039`

- `g05-0042` *STATED* — The Chrome Relay guide flags catches of letting Claude drive your signed-in Chrome (section 'The catch').
  — [g-let-claude-use-your-real-chrome-signed-in-in-background-tabs](https://chen.media/guides/let-claude-use-your-real-chrome-signed-in-in-background-tabs)
  ↳ *qualifies* `g05-0031`
  ↳ *example-of* `g05-0320`

- `g05-0054` *STATED* — The promo-video guide lists several catches (section 'The catches').
  — [g-make-a-full-promo-video-with-claude-from-one-sentence](https://chen.media/guides/make-a-full-promo-video-with-claude-from-one-sentence)
  ↳ *qualifies* `g05-0043`

- `g05-0097` *STATED* — The motion-design guide has a catch about Claude-coded films (section 'The catch').
  — [g-15-motion-design-styles-claude-can-make-from-one-prompt](https://chen.media/guides/15-motion-design-styles-claude-can-make-from-one-prompt)
  ↳ *qualifies* `g05-0074`

- `g05-0127` *STATED* — The ReelMimic guide has a catch section qualifying the app.
  — [g-reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style)
  ↳ *qualifies* `g05-0114`

- `g05-0143` *STATED* — The Mortiflix guide has a catch section qualifying the app.
  — [g-mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer](https://chen.media/guides/mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer)
  ↳ *qualifies* `g05-0128`

- `g05-0222` *STATED* — The head -100 skill guide has a catch qualifying the fix (1 prompt to copy, 4 numbered steps).
  — [g-claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix](https://chen.media/guides/claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix)
  ↳ *qualifies* `g05-0217`

- `g05-0228` *STATED* — Over the public 3D Asset Server, Claude gets direct file URLs and a one-click zip for each asset; it does not write to your disk.
  — [g-3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once](https://chen.media/guides/3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once)
  ↳ *qualifies* `g05-0227`

- `g05-0237` *STATED* — The 3D Asset Server guide has a catch section qualifying the tool.
  — [g-3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once](https://chen.media/guides/3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once)
  ↳ *qualifies* `g05-0223`

- `g05-0255` *STATED* — OpenQodex needs Node 22 or newer, git, macOS or Linux, and Claude Code installed and logged in.
  — [g-install-openqodex-a-second-claude-reviews-your-code-before-you-push](https://chen.media/guides/install-openqodex-a-second-claude-reviews-your-code-before-you-push)
  ↳ *part-of* `g05-0250`

- `g05-0261` *INFERRED* — OpenQodex lists only macOS or Linux, so on Windows it likely needs WSL.
  — [g-install-openqodex-a-second-claude-reviews-your-code-before-you-push](https://chen.media/guides/install-openqodex-a-second-claude-reviews-your-code-before-you-push)
  ↳ *qualifies* `g05-0255`

- `g05-0309` *STATED* — The logo-design guide has a catch section qualifying the skill (1 prompt to copy, 4 numbered steps).
  — [g-install-the-logo-design-skill](https://chen.media/guides/install-the-logo-design-skill)
  ↳ *qualifies* `g05-0299`

- `g06-0008` *STATED* — The /iq skill's output is a fun estimate, not an IQ test.
  > “A fun estimate, not a test.”
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *qualifies* `g06-0001`

- `g07-0011` *STATED* — Alex flags a catch to understand before you trust Claude to triage your Gmail ('The catch'; details email-gated).
  — [g-sort-your-inbox-with-claude-instead-of-superhuman](https://chen.media/guides/sort-your-inbox-with-claude-instead-of-superhuman)
  ↳ *part-of* `g07-0001`
  ↳ *qualifies* `g07-0010`

- `g07-0027` *STATED* — Alex says one habit keeps you safe when letting Find Skills pick and install skills ('The catch'; the habit is email-gated).
  — [g-let-claude-find-and-install-the-right-skill-for-any-job](https://chen.media/guides/let-claude-find-and-install-the-right-skill-for-any-job)
  ↳ *part-of* `g07-0024`
  ↳ *qualifies* `g07-0030`
  ↳ *evidence-for* `g10-0255`

- `g07-0049` *STATED* — Alex flags a catch with REA ('The catch'; details email-gated).
  — [g-see-how-an-apps-feature-works-with-claude-code-and-rea-free](https://chen.media/guides/see-how-an-apps-feature-works-with-claude-code-and-rea-free)
  ↳ *part-of* `g07-0038`
  ↳ *qualifies* `g07-0038`

- `g08-0006` *STATED* — Alex lists things to know before you rely on Vibewise (section 'What to know before you rely on it', body locked).
  — [g-vibe-code-and-still-learn-set-up-the-free-vibewise-plugin-for-claude-code](https://chen.media/guides/vibe-code-and-still-learn-set-up-the-free-vibewise-plugin-for-claude-code)
  ↳ *qualifies* `g08-0001`
  ↳ *evidence-for* `g05-0030`

- `g08-0026` *STATED* — Anthropic's study did not test Vibewise; treat it as the reason the plugin exists, not as a result for the plugin.
  > “Treat it as the reason the plugin exists, not as a result for the plugin.”
  — [g-vibe-code-and-still-learn-set-up-the-free-vibewise-plugin-for-claude-code](https://chen.media/guides/vibe-code-and-still-learn-set-up-the-free-vibewise-plugin-for-claude-code)
  ↳ *qualifies* `g08-0003`
  ↳ *example-of* `g08-0258`
  ↳ *evidence-for* `g05-0026`

- `g08-0048` *STATED* — Check adobe.com for today's price; Adobe's all-apps Creative Cloud plan is a different, bigger plan than the three single-app subscriptions.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *qualifies* `g08-0047`

- `g08-0052` *STATED* — PhotoCraft, FilmCraft and EffectCraft are very new and still rough.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *qualifies* `g08-0049`
  ↳ *leads-to* `g08-0058`

- `g08-0056` *STATED* — The Craft apps are not made or approved by Adobe.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *qualifies* `g08-0049`
  ↳ *example-of* `g08-0258`

- `g08-0057` *STATED* — The Craft apps' own pages call them "early alpha", "in development" and "young and moving fast".
  > “"early alpha", "in development" and "young and moving fast"”
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *evidence-for* `g08-0052`
  ↳ *qualifies* `g08-0049`

- `g08-0061` *STATED* — PhotoCraft's own page says it is not yet a Photoshop replacement for daily professional work.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *qualifies* `g08-0059`
  ↳ *evidence-for* `g08-0058`
  ↳ *contrast* `g10-0152`

- `g08-0065` *STATED* — EffectCraft can't open After Effects project files.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *qualifies* `g08-0064`
  ↳ *contrast* `g08-0060` — PhotoCraft reads .psd; EffectCraft cannot read AE projects

- `g08-0070` *STATED* — Swapping Adobe for the Craft apps costs features you will honestly miss; Alex lists them in a locked section ('What you will honestly miss').
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *qualifies* `g08-0058`

- `g08-0093` *STATED* — Alex flags things to know before you load all 230+ of The Agency's agents (guide lede; 'Good to know' body locked).
  — [g-run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents](https://chen.media/guides/run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents)
  ↳ *qualifies* `g08-0089`
  ↳ *evidence-for* `g18-0285`

- `g08-0160` *STATED* — Replica has one rule it won't break (section 'The one rule it won't break', body locked).
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *qualifies* `g08-0156`

- `g09-0242` *STATED* — No notch: on an iMac, a Mac mini, or a MacBook with its lid closed on an external display, Mochi sits in a small bar at the top of the screen instead.
  — [g-coucou-free-notch-pet-that-watches-claude-code](https://chen.media/guides/coucou-free-notch-pet-that-watches-claude-code)
  ↳ *qualifies* `g09-0232`

- `g10-0157` *STATED* — Alex Chen's Photon Studio guide has a section 'Where it falls short (for now)' (body locked).
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *qualifies* `g10-0152`
  ↳ *example-of* `g10-0270`

- `g10-0210` *STATED* — Alex Chen's Open Design guide has a section 'Before you switch: the honest part' (body locked).
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *qualifies* `g10-0198`
  ↳ *example-of* `g10-0270`

- `g10-0233` *STATED* — Alex Chen's Dyad guide has a section 'Before you switch: the honest part' (body locked).
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *qualifies* `g10-0224`
  ↳ *example-of* `g10-0270`

- `g10-0246` *STATED* — Dyad is a desktop app for Mac and Windows (with Linux builds on the releases page), and it needs Node.js installed.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *qualifies* `g10-0226`
  ↳ *qualifies* `g10-0223`

- `g10-0255` *STATED* — Alex Chen's Find Skills guide has a section 'Before you install: the honest part' (body locked).
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)
  ↳ *qualifies* `g10-0247`
  ↳ *example-of* `g10-0270`

- `g11-0031` *STATED* — Instatic is early software and you run it yourself, so hosting and your Claude usage cost a little.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *qualifies* `g11-0014`
  ↳ *example-of* `g11-0003`
  ↳ *example-of* `g11-0005`
  ↳ *evidence-for* `g18-0126`

- `g11-0194` *STATED* — FluidVoice is Mac only for now and needs macOS 15 or later.
  — [g-fluidvoice-the-free-open-source-wispr-flow](https://chen.media/guides/fluidvoice-the-free-open-source-wispr-flow)
  ↳ *qualifies* `g11-0181`
  ↳ *example-of* `g11-0005`

- `g12-0198` *INFERRED* — AGPL-3.0 means that if you modify SupoClip and offer it to others as a network service, you must publish your modified source.
  — [g-supoclip-open-source-opusclip-alternative](https://chen.media/guides/supoclip-open-source-opusclip-alternative)
  ↳ *qualifies* `g12-0192`

- `g13-0012` *STATED* — Alex's Bot Crossing guide has a section 'What it can see' covering which local data the game can read.
  — [g-watch-every-claude-code-session-as-a-bot-in-bot-crossing](https://chen.media/guides/watch-every-claude-code-session-as-a-bot-in-bot-crossing)
  ↳ *qualifies* `g13-0007`

- `g13-0069` *STATED* — What you can collect with Scrapling is determined by the available data, site rules, request limits and your machine.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *qualifies* `g13-0068`

- `g13-0070` *STATED* — Alex's Scrapling guide does not establish a fastest-crawler ranking.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *qualifies* `g13-0067`

- `g13-0078` *STATED* — Alex's Scrapling guide ends with a 'What was verified' section separating tested results from claims.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *part-of* `g13-0063`

- `g13-0133` *STATED* — Alex's /watch guide has a section 'What it can't see (and the fixes)' on /watch's blind spots and workarounds.
  — [g-let-claude-code-watch-any-video-with-watch](https://chen.media/guides/let-claude-code-watch-any-video-with-watch)
  ↳ *qualifies* `g13-0126`

- `g13-0151` *STATED* — Alex's claude-mem guide has a 'Good to know' section of caveats.
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *qualifies* `g13-0136`

- `g13-0191` *STATED* — The examples in Alex's HackingTool guide are original planning templates, not results from a scan he ran.
  — [g-hackingtool-secure-your-own-apps](https://chen.media/guides/hackingtool-secure-your-own-apps)
  ↳ *qualifies* `g13-0190`

- `g13-0285` *STATED* — Free skills can still cost money through model plans, APIs, hosting and third-party services.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *qualifies* `g13-0284`
  ↳ *evidence-for* `g18-0126`

- `g13-0286` *STATED* — Skill licences differ, including source-available document skills.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *qualifies* `g13-0284`

- `g13-0288` *STATED* — The 100-skill list is a curated starting shelf, not a certification that every workflow has been tested in your environment.
  > “This is a curated starting shelf, not a certification that every workflow has been tested in your environment.”
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *qualifies* `g13-0282`
  ↳ *qualifies* `g13-0281`

- `g14-0052` *STATED* — OpenCut has more than one official repository, so choose the right one before cloning.
  > “Choose the right repository”
  — [g-opencut-repo-and-setup-guide](https://chen.media/guides/opencut-repo-and-setup-guide)
  ↳ *part-of* `g14-0043`

- `g14-0103` *STATED* — Agent Reach connects existing readers and search tools rather than removing every platform restriction.
  > “It connects existing readers and search tools rather than removing every platform restriction.”
  — [g-agent-reach-web-research-setup](https://chen.media/guides/agent-reach-web-research-setup)
  ↳ *qualifies* `g14-0101`
  ↳ *qualifies* `y04-0140`

- `g14-0105` *STATED* — An ordinary ChatGPT conversation is not a local terminal, so it cannot run terminal-based tools like Agent Reach.
  > “An ordinary ChatGPT conversation is not a local terminal.”
  — [g-agent-reach-web-research-setup](https://chen.media/guides/agent-reach-web-research-setup)
  ↳ *contrast* `g14-0104`

- `g14-0224` *STATED* — With ECC installed you still need the coding agent, its model access, and human review of the result.
  > “You still need the coding agent, its model access, and human review of the result.”
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *qualifies* `g14-0223`

- `g14-0231` *STATED* — Alex's ECC install examples follow the repository documentation checked on September 12, 2026.
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *part-of* `g14-0220`
  ↳ *example-of* `g14-0347`

- `g14-0240` *STATED* — Know what ECC's advertised numbers (counts of skills, agents and hooks) actually mean before treating them as quality.
  > “Know what the numbers mean”
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *part-of* `g14-0220`
  ↳ *example-of* `g14-0348`
  ↳ *evidence-for* `g18-0012`

- `g14-0294` *STATED* — A Claude skill does not create an autonomous employee or make model usage free.
  > “it does not create an autonomous employee or make model usage free”
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *qualifies* `g14-0289`
  ↳ *evidence-for* `g14-0350`
  ↳ *evidence-for* `g18-0126`

- `g15-0002` *STATED* — "Free-to-start" is deliberate wording: of Skiper UI, Vengeance UI, Animmaster Lib and React Bits, at least one actually costs money, and the guide's locked honest notes say which.
  — [g-four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed](https://chen.media/guides/four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed)
  ↳ *qualifies* `g15-0001`
  ↳ *example-of* `g15-0177`

- `g15-0022` *STATED* — MarkItDown handles some files badly, and there are two ways round it (guide Part 5, locked).
  — [g-why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix](https://chen.media/guides/why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix)
  ↳ *qualifies* `g15-0016`
  ↳ *example-of* `g15-0177`

- `g15-0052` *STATED* — There are two popular Claude Code skills with ADHD in the name and neither is a verifier; install the wrong one and you get something genuinely good that does a completely different job.
  — [g-claude-code-says-done-before-it-has-proved-anything-this-fixes-it](https://chen.media/guides/claude-code-says-done-before-it-has-proved-anything-this-fixes-it)
  ↳ *leads-to* `g15-0056`
  ↳ *leads-to* `g15-0058`

- `g16-0050` *STATED* — caveman carries a caveat that he quotes in the repo's own words.
  > “The caveat on caveman, in the repo's own words”
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you)
  ↳ *qualifies* `g16-0049`
  ↳ *part-of* `g03-0100`

- `g16-0155` *STATED* — There are tasks where you should not use unlazy.
  > “When not to use it”
  — [g-the-free-skill-that-stops-claude-saying-done-when-it-is-not](https://chen.media/guides/the-free-skill-that-stops-claude-saying-done-when-it-is-not)
  ↳ *qualifies* `g16-0141`

- `g17-0093` *STATED* — One claim from Alex Chen's three-plugins video is not supported by the tools themselves, and the guide says which.
  > “the one claim from the video that the tools themselves do not support”
  — [g-the-three-claude-code-plugins-worth-installing](https://chen.media/guides/the-three-claude-code-plugins-worth-installing)
  ↳ *qualifies* `g17-0086`
  ↳ *example-of* `g17-0308`

- `g17-0095` *STATED* — The Awesome APIs section explains what the free tier really is.
  > “Awesome APIs, and what the free tier really is”
  — [g-the-three-claude-code-plugins-worth-installing](https://chen.media/guides/the-three-claude-code-plugins-worth-installing)
  ↳ *qualifies* `g17-0089`

- `g17-0108` *STATED* — Alex Chen lists three things to be clear about before you start with Claude SEO.
  > “Three things to be clear about before you start”
  — [g-install-25-seo-skills-and-18-specialist-agents-into-claude-code](https://chen.media/guides/install-25-seo-skills-and-18-specialist-agents-into-claude-code)
  ↳ *qualifies* `g17-0099`

- `g17-0112` *STATED* — Claude SEO has places where it struggles, listed in the guide.
  > “Where it struggles”
  — [g-install-25-seo-skills-and-18-specialist-agents-into-claude-code](https://chen.media/guides/install-25-seo-skills-and-18-specialist-agents-into-claude-code)
  ↳ *qualifies* `g17-0099`
  ↳ *example-of* `g17-0306`

- `g17-0154` *STATED* — There are two things to be clear about before you set up FreeLLMAPI.
  > “Two things to be clear about before you start”
  — [g-pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint](https://chen.media/guides/pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint)
  ↳ *qualifies* `g17-0143`

- `g17-0165` *STATED* — Alex Chen gives an honest take on the hardware Project NOMAD needs.
  > “Hardware, honestly”
  — [g-a-knowledge-server-that-keeps-answering-with-the-internet-off](https://chen.media/guides/a-knowledge-server-that-keeps-answering-with-the-internet-off)
  ↳ *qualifies* `g17-0160`
  ↳ *example-of* `g17-0306`

- `g18-0010` *STATED* — Installing ECC as a marketplace is not the same as cloning it, and the difference is how updates reach you.
  > “A marketplace is not a clone, and the difference is updates”
  — [g-67-agents-281-skills-and-94-commands-in-one-install](https://chen.media/guides/67-agents-281-skills-and-94-commands-in-one-install)
  ↳ *qualifies* `g18-0009`
  ↳ *qualifies* `g18-0156`

- `g18-0027` *STATED* — If you are on a lower tier your saving from a free swap is smaller, but the swap still works.
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *qualifies* `g18-0025`
  ↳ *evidence-for* `g18-0126`

- `g18-0030` *STATED* — Prices in the 15-replacements guide were checked the week it went out; prices move, the tool links do not.
  > “They move. The tool links do not.”
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *qualifies* `g18-0024`

- `g18-0036` *STATED* — Figma is one to keep paying for unless you are working solo; Penpot suits solo designers.
  > “This is one to keep paying for unless you are working solo”
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *qualifies* `g18-0035`
  ↳ *example-of* `g18-0028`
  ↳ *qualifies* `g18-0148` — 15-more guide says keep Figma unless solo

- `g18-0088` *STATED* — Genjutsu is the exception among the five animation skills: it installs as a Claude Code plugin, not through npx skills.
  — [g-five-animation-skills-for-claude-code-with-install-commands](https://chen.media/guides/five-animation-skills-for-claude-code-with-install-commands)
  ↳ *qualifies* `g18-0086`
  ↳ *qualifies* `g18-0082`
  ↳ *example-of* `g18-0160`

- `g18-0126` *CORE* — Free almost always means a free tier, not unlimited.
  > “free almost always means a free tier, not unlimited”
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *qualifies* `g18-0125`
  ↳ *qualifies* `g16-0008`

- `g18-0185` *STATED* — NotebookLM has no public write API, so nothing can push a file into a notebook for you automatically.
  — [g-give-claude-a-memory-that-survives-the-chat-window](https://chen.media/guides/give-claude-a-memory-that-survives-the-chat-window)
  ↳ *qualifies* `g18-0183`
  ↳ *qualifies* `g18-0187`

- `g18-0195` *STATED* — G0DM0D3 is not fully offline: model calls still go out to whichever provider you point it at.
  — [g-one-html-file-that-runs-chatgpt-claude-gemini-and-grok-side-by-side](https://chen.media/guides/one-html-file-that-runs-chatgpt-claude-gemini-and-grok-side-by-side)
  ↳ *qualifies* `g18-0194`

- `g18-0267` *INFERRED* — The seven-repos guide's own table lists rohitg00/agentmemory as Apache-2.0, so five of the seven are MIT, not six.
  — [g-seven-free-repos-that-replace-paid-ai-tools](https://chen.media/guides/seven-free-repos-that-replace-paid-ai-tools)
  ↳ *contradicts* `g18-0266` — guide table: agentmemory is Apache-2.0, so only five MIT
  ↳ *qualifies* `g18-0272`
  ↳ *qualifies* `g18-0262`

- `g19-0154` *INFERRED* — The @observe() decorator traces Python agent code you write yourself; it does not by itself instrument the Claude Code CLI's internal calls.
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *qualifies* `g19-0151`

- `g20-0139` *INFERRED* — The free table of contents of the design-stack guide skips items 9, 12 and 17, so those three sites are not identifiable without the gated part.
  — [g-why-every-ai-built-site-looks-the-same-and-how-to-fix-it](https://chen.media/guides/why-every-ai-built-site-looks-the-same-and-how-to-fix-it)
  ↳ *qualifies* `g20-0129`

- `g22-0125` *INFERRED* — The 'skills' in the Five Claude Skills guide are paste-in chat prompts, not installed SKILL.md skills or plugins.
  — [g-five-claude-skills-that-feel-like-cheating](https://chen.media/guides/five-claude-skills-that-feel-like-cheating)
  ↳ *qualifies* `g22-0114`
  ↳ *contrast* `g22-0070`
  ↳ *contrast* `g15-0179`

- `y01-0046` *STATED* — After installing a Codex plugin, start a new chat so the plugin's tools are available.
  > “After installation, start a new chat so its tools are available.”
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *evidence-for* `g07-0008`
  ↳ *qualifies* `y01-0045`

- `y01-0129` *INFERRED* — The 'completely free' framing covers the open-source ai-agency-claude repo; running it still requires Claude Code, which needs a paid Claude plan or API usage.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *evidence-for* `g18-0126`
  ↳ *qualifies* `y01-0128`

- `y01-0195` *INFERRED* — The video promises an exact fix for runaway fal.ai spend but only shows a per-request budget ('maximum $1') given to the skill; no account-level spending cap on fal.ai is demonstrated.
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *qualifies* `y01-0194`

- `y01-0222` *STATED* — Video description caveat: Alex's fal skill and setup guide are free, but video generation through fal.ai is paid, with costs depending on the model and settings - the 10c example isn't a flat price for every generation.
  > “The 10¢ example isn't a flat price for every generation.”
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *evidence-for* `g18-0126`
  ↳ *contradicts* `y01-0182` — title/hook '10c' vs description: not a flat price per generation
  ↳ *qualifies* `y01-0189`

- `y04-0096` *INFERRED* — A single HTML file cannot itself grant free use of paid models; hubs like this usually embed or link each provider's own web interface, so each provider's login and limits still apply - verify before relying on it.
  — [OD7UTDYiTYI](https://youtu.be/OD7UTDYiTYI) [voaf6bOrHgc](https://youtu.be/voaf6bOrHgc)
  ↳ *qualifies* `y04-0091`
  ↳ *qualifies* `y04-0094`

### claim

- `g01-0072` *STATED* — In khan-explainer the voice drives the clock, so the pen never runs ahead of the words.
  > “The voice drives the clock, so the pen never runs ahead of the words.”
  — [g-make-khan-academy-style-videos-with-claude](https://chen.media/guides/make-khan-academy-style-videos-with-claude)
  ↳ *part-of* `g01-0067`

- `g01-0073` *STATED* — khan-explainer offers chalk on a blackboard or marker on a whiteboard, in landscape or vertical.
  — [g-make-khan-academy-style-videos-with-claude](https://chen.media/guides/make-khan-academy-style-videos-with-claude)
  ↳ *part-of* `g01-0066`

- `g01-0079` *STATED* — With Show Your Work, screenshots, designs, charts and generated images appear right in the Claude Code chat.
  — [g-show-your-work-see-every-screenshot-and-video-claude-makes-right-in-your-termina](https://chen.media/guides/show-your-work-see-every-screenshot-and-video-claude-makes-right-in-your-termina)
  ↳ *part-of* `g01-0075`

- `g01-0082` *STATED* — Show Your Work's video player has playback controls, timestamped steps and version comparison, and can open in QuickTime or save to Downloads.
  — [g-show-your-work-see-every-screenshot-and-video-claude-makes-right-in-your-termina](https://chen.media/guides/show-your-work-see-every-screenshot-and-video-claude-makes-right-in-your-termina)
  ↳ *part-of* `g01-0075`

- `g01-0088` *STATED* — With Graphicle, Claude asks it first and gets cited excerpts: the exact files and lines.
  — [g-give-claude-a-map-and-a-memory-of-your-whole-project](https://chen.media/guides/give-claude-a-map-and-a-memory-of-your-whole-project)
  ↳ *defines* `g01-0087`

- `g01-0090` *STATED* — Graphicle's project memory holds your docs (Markdown, PDF, Office, HTML), reviewed decisions and past Claude Code sessions, searchable next to the code.
  — [g-give-claude-a-map-and-a-memory-of-your-whole-project](https://chen.media/guides/give-claude-a-map-and-a-memory-of-your-whole-project)
  ↳ *part-of* `g01-0087`
  ↳ *contrast* `g01-0039` — project-wide memory vs a per-tool corrections log

- `g01-0094` *STATED* — Graphicle is local: no account, no telemetry, and nothing leaves your machine unless you ask.
  — [g-give-claude-a-map-and-a-memory-of-your-whole-project](https://chen.media/guides/give-claude-a-map-and-a-memory-of-your-whole-project)
  ↳ *part-of* `g01-0087`
  ↳ *example-of* `g01-0196`
  ↳ *example-of* `g02-0240`

- `g01-0100` *STATED* — Claudemy makes a one-page card for every lesson: key ideas, how much the sources agree, a practice task and further reading.
  — [g-turn-any-topic-into-a-12-lesson-audio-course-with-claude](https://chen.media/guides/turn-any-topic-into-a-12-lesson-audio-course-with-claude)
  ↳ *part-of* `g01-0097`

- `g01-0101` *STATED* — Claudemy produces a playbook with one rule per lesson.
  — [g-turn-any-topic-into-a-12-lesson-audio-course-with-claude](https://chen.media/guides/turn-any-topic-into-a-12-lesson-audio-course-with-claude)
  ↳ *part-of* `g01-0097`

- `g01-0178` *STATED* — Scientific Agent Skills covers biology, chemistry, medicine, physics and engineering.
  — [g-give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills](https://chen.media/guides/give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills)
  ↳ *part-of* `g01-0177`

- `g01-0181` *STATED* — Scientific Agent Skills' 177 skills follow the open Agent Skills standard, so Claude loads the right one when your request matches it.
  — [g-give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills](https://chen.media/guides/give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills)
  ↳ *part-of* `g01-0177`
  ↳ *enables* `g01-0185`
  ↳ *evidence-for* `g15-0045`
  ↳ *because* `g15-0184`

- `g02-0082` *STATED* — GoLive is free and MIT-licensed, and does the go-live work with you one approved step at a time.
  > “one approved step at a time”
  — [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive)
  ↳ *qualifies* `g02-0080`
  ↳ *evidence-for* `g12-0051`
  ↳ *example-of* `g12-0303`

- `g02-0132` *STATED* — Atticus moves your windows, finds your files, reads your screen and gets it done.
  — [g-control-your-whole-mac-with-your-voice-powered-by-claude](https://chen.media/guides/control-your-whole-mac-with-your-voice-powered-by-claude)
  ↳ *part-of* `g02-0129`

- `g02-0158` *STATED* — claude-seo needs no API keys.
  — [g-have-claude-audit-your-whole-website-for-google](https://chen.media/guides/have-claude-audit-your-whole-website-for-google)
  ↳ *qualifies* `g02-0151`
  ↳ *evidence-for* `g17-0100`
  ↳ *part-of* `g17-0099`

- `g02-0165` *STATED* — github-triage works through the repo's open pull requests and issues with the gh command line tool.
  — [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say)

- `g02-0170` *STATED* — Each github-triage review is saved to a local file and never posted to GitHub.
  — [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say)
  ↳ *qualifies* `g02-0169`
  ↳ *example-of* `g02-0237`
  ↳ *example-of* `g02-0240`

- `g02-0174` *STATED* — github-triage priorities and sizes stay on your machine and are never posted.
  — [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say)
  ↳ *qualifies* `g02-0173`
  ↳ *example-of* `g02-0240`

- `g02-0187` *STATED* — Most browser agents start in a blank browser with none of your logins.
  — [g-let-claude-use-your-signed-in-chrome-in-the-background](https://chen.media/guides/let-claude-use-your-signed-in-chrome-in-the-background)

- `g02-0188` *STATED* — With Chrome Relay, Claude works in background tabs, so your own window stays yours.
  — [g-let-claude-use-your-signed-in-chrome-in-the-background](https://chen.media/guides/let-claude-use-your-signed-in-chrome-in-the-background)
  ↳ *part-of* `g02-0185`

- `g02-0191` *STATED* — Chrome Relay offers optional 1Password sign-ins, iPhone approvals and an audit trail.
  — [g-let-claude-use-your-signed-in-chrome-in-the-background](https://chen.media/guides/let-claude-use-your-signed-in-chrome-in-the-background)
  ↳ *part-of* `g02-0185`

- `g02-0220` *STATED* — AI Homepage has Claude read the sites you actually visit and write a fresh front page into every new tab, in any look you describe.
  — [g-ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper](https://chen.media/guides/ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper)
  ↳ *defines* `g02-0219`

- `g02-0221` *STATED* — AI Homepage replaces Chrome's new-tab page with one that's written for you.
  — [g-ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper](https://chen.media/guides/ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper)
  ↳ *part-of* `g02-0219`

- `g02-0228` *STATED* — AI Homepage auto-rebuild is on by default, after your first build by hand.
  — [g-ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper](https://chen.media/guides/ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper)
  ↳ *qualifies* `g02-0227`

- `g02-0230` *STATED* — AI Homepage skips search engines, webmail, banking and logged-out marketing pages, plus any site you add to its block list.
  — [g-ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper](https://chen.media/guides/ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper)
  ↳ *qualifies* `g02-0224`

- `g02-0240` *CORE* — Local-first is a recurring selling point: /hunter writes only to .hunter, career-ops has no telemetry or backend, github-triage keeps rankings local, Trail-code builds its map with no model or API key, Time Machine uses its own hidden git store.
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill) [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi) [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say) [g-trail-code-stop-claude-getting-lost-in-your-code](https://chen.media/guides/trail-code-stop-claude-getting-lost-in-your-code) [g-rewind-claude-code-to-the-step-that-broke-your-code](https://chen.media/guides/rewind-claude-code-to-the-step-that-broke-your-code)

- `g02-0244` *INFERRED* — Two featured tools solve the logged-out browser problem by running inside your own signed-in Chrome: Chrome Relay drives background tabs and AI Homepage opens the sites you follow signed in as you.
  — [g-let-claude-use-your-signed-in-chrome-in-the-background](https://chen.media/guides/let-claude-use-your-signed-in-chrome-in-the-background) [g-ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper](https://chen.media/guides/ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper)
  ↳ *because* `g02-0187`

- `g03-0037` *STATED* — SkillSpector reads a skill folder before you install it and tells you whether anything inside looks dangerous.
  — [g-skillspector-scan-any-claude-skill-for-malware-before-you-install-it](https://chen.media/guides/skillspector-scan-any-claude-skill-for-malware-before-you-install-it)
  ↳ *defines* `g03-0035`

- `g03-0045` *STATED* — SkillSpector can scan a skill folder, a single SKILL.md, a zip file or a GitHub link.
  — [g-skillspector-scan-any-claude-skill-for-malware-before-you-install-it](https://chen.media/guides/skillspector-scan-any-claude-skill-for-malware-before-you-install-it)
  ↳ *part-of* `g03-0035`

- `g03-0046` *STATED* — SkillSpector outputs a risk score from 0 to 100 and a recommendation of SAFE, CAUTION or DO NOT INSTALL.
  — [g-skillspector-scan-any-claude-skill-for-malware-before-you-install-it](https://chen.media/guides/skillspector-scan-any-claude-skill-for-malware-before-you-install-it)
  ↳ *part-of* `g03-0035`

- `g03-0047` *STATED* — SkillSpector rates severity from LOW to CRITICAL and reports the file and line of each finding.
  — [g-skillspector-scan-any-claude-skill-for-malware-before-you-install-it](https://chen.media/guides/skillspector-scan-any-claude-skill-for-malware-before-you-install-it)
  ↳ *part-of* `g03-0046`

- `g03-0090` *STATED* — Diagram Design matches diagrams to your own website's colors and fonts: point it at your website once and every diagram after uses your palette and fonts.
  — [g-diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe](https://chen.media/guides/diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe)
  ↳ *part-of* `g03-0089`

- `g03-0094` *STATED* — Every Diagram Design type comes in three styles: minimal light, minimal dark and full-editorial.
  — [g-diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe](https://chen.media/guides/diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe)
  ↳ *part-of* `g03-0089`

- `g03-0096` *STATED* — Diagram Design can import and redraw your existing Mermaid, draw.io and Excalidraw diagrams in the same clean style.
  — [g-diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe](https://chen.media/guides/diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe)
  ↳ *part-of* `g03-0089`

- `g03-0097` *STATED* — Diagram Design exports to SVG or PNG.
  — [g-diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe](https://chen.media/guides/diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe)
  ↳ *part-of* `g03-0089`

- `g03-0139` *STATED* — The code intelligence guide has locked sections "What it adds" and "The catch" (6 numbered steps total).
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *example-of* `g03-0005`
  ↳ *qualifies* `g03-0122`

- `g03-0141` *STATED* — Minutes is pitched as an open-source alternative to Otter and Granola.
  — [g-minutes-the-free-open-source-meeting-recorder-that-claude-can-search](https://chen.media/guides/minutes-the-free-open-source-meeting-recorder-that-claude-can-search)
  ↳ *qualifies* `g03-0140`
  ↳ *contrast* `g18-0038` — Minutes pitched as alternative to Granola; 15-replacements lists Granola itself as the free swap

- `g03-0142` *STATED* — Minutes lets Claude Code (or Codex, Cursor, any MCP client) search the meeting history you choose to share and answer what got decided.
  — [g-minutes-the-free-open-source-meeting-recorder-that-claude-can-search](https://chen.media/guides/minutes-the-free-open-source-meeting-recorder-that-claude-can-search)
  ↳ *part-of* `g03-0140`
  ↳ *evidence-for* `g15-0184`

- `g03-0144` *STATED* — In Minutes, capture, transcription and storage run locally and audio stays on your machine.
  — [g-minutes-the-free-open-source-meeting-recorder-that-claude-can-search](https://chen.media/guides/minutes-the-free-open-source-meeting-recorder-that-claude-can-search)
  ↳ *example-of* `g03-0012`
  ↳ *part-of* `g03-0140`
  ↳ *example-of* `g02-0240`

- `g03-0145` *STATED* — Minutes saves every meeting as a plain Markdown file in ~/meetings/ with YAML at the top: title, date, duration, action items, decisions.
  > “~/meetings/”
  — [g-minutes-the-free-open-source-meeting-recorder-that-claude-can-search](https://chen.media/guides/minutes-the-free-open-source-meeting-recorder-that-claude-can-search)
  ↳ *part-of* `g03-0140`
  ↳ *enables* `g03-0146` — plain Markdown files are what the MCP server searches

- `g03-0149` *STATED* — Minutes has a desktop app with menu bar capture, dictation and Recall.
  — [g-minutes-the-free-open-source-meeting-recorder-that-claude-can-search](https://chen.media/guides/minutes-the-free-open-source-meeting-recorder-that-claude-can-search)
  ↳ *part-of* `g03-0140`

- `g03-0150` *STATED* — Minutes imports meetings from Granola.
  — [g-minutes-the-free-open-source-meeting-recorder-that-claude-can-search](https://chen.media/guides/minutes-the-free-open-source-meeting-recorder-that-claude-can-search)
  ↳ *evidence-for* `g03-0141`

- `g03-0151` *STATED* — Minutes has no paid tier for anything in the repo, and the author says it stays MIT.
  — [g-minutes-the-free-open-source-meeting-recorder-that-claude-can-search](https://chen.media/guides/minutes-the-free-open-source-meeting-recorder-that-claude-can-search)
  ↳ *qualifies* `g03-0140`

- `g04-0037` *STATED* — Harvey requires Python 3.11 or newer.
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)

- `g04-0039` *STATED* — Harvey requires an active Claude Pro or Max plan with the Claude Code CLI logged in (run: claude login).
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *enables* `g04-0035`

- `g04-0115` *STATED* — /hiring-panel writes everything to a .hiring-panel folder where you run it and never touches your other files.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *qualifies* `g04-0099`
  ↳ *example-of* `g04-0248`
  ↳ *evidence-for* `r01-0142`

- `g04-0169` *STATED* — /linkedin-roast writes everything to a linkedin-roast-output folder where you run it.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *qualifies* `g04-0149`
  ↳ *example-of* `g04-0248`

- `g04-0170` *STATED* — /linkedin-roast never logs in to LinkedIn and never touches your other files.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *qualifies* `g04-0149`
  ↳ *qualifies* `g04-0248`

- `g04-0248` *STATED* — Alex's career skills write all output to their own folder in the directory where you run them (.hiring-panel, linkedin-roast-output) and never touch your other files.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free) [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *evidence-for* `r01-0014`

- `g05-0027` *STATED* — Vibewise tries to give you back 'the other way of using AI' — the explain-and-ask habits instead of full delegation.
  > “Vibewise is a free plugin that tries to give you the other way of using AI back.”
  — [g-turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin](https://chen.media/guides/turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin)
  ↳ *defines* `g05-0001`

- `g05-0028` *STATED* — Installing the Vibewise plugin takes about 2 minutes (guide section 'Install it (about 2 minutes)').
  — [g-turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin](https://chen.media/guides/turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin)
  ↳ *part-of* `g05-0001`

- `g05-0032` *STATED* — Chrome Relay opens its tabs in the background, so nothing steals focus while you keep working.
  — [g-let-claude-use-your-real-chrome-signed-in-in-background-tabs](https://chen.media/guides/let-claude-use-your-real-chrome-signed-in-in-background-tabs)
  ↳ *part-of* `g05-0031`
  ↳ *evidence-for* `g02-0188`

- `g05-0039` *STATED* — Chrome Relay setup takes about 2 minutes and is done once per Mac (guide 'Step 1: set it up (about 2 minutes, once per Mac)').
  — [g-let-claude-use-your-real-chrome-signed-in-in-background-tabs](https://chen.media/guides/let-claude-use-your-real-chrome-signed-in-in-background-tabs)
  ↳ *part-of* `g05-0041`

- `g05-0045` *STATED* — From that one sentence AI Promo Video Maker does the research, the screenshots, the edit and the render.
  — [g-make-a-full-promo-video-with-claude-from-one-sentence](https://chen.media/guides/make-a-full-promo-video-with-claude-from-one-sentence)
  ↳ *part-of* `g05-0043`
  ↳ *leads-to* `g05-0049`

- `g05-0051` *STATED* — Without narration, AI Promo Video Maker gives you royalty-free music and big subtitles.
  — [g-make-a-full-promo-video-with-claude-from-one-sentence](https://chen.media/guides/make-a-full-promo-video-with-claude-from-one-sentence)

- `g05-0075` *STATED* — In the 15 motion films, Claude wrote code for the picture, the animation, the music and the sound effects.
  — [g-15-motion-design-styles-claude-can-make-from-one-prompt](https://chen.media/guides/15-motion-design-styles-claude-can-make-from-one-prompt)
  ↳ *part-of* `g05-0074`

- `g05-0076` *STATED* — No image or video generator is used in the 15 motion-design films.
  — [g-15-motion-design-styles-claude-can-make-from-one-prompt](https://chen.media/guides/15-motion-design-styles-claude-can-make-from-one-prompt)
  ↳ *qualifies* `g05-0075`
  ↳ *evidence-for* `g05-0318`

- `g05-0105` *STATED* — After reloading, a short Effortless setup opens above the prompt.
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless)
  ↳ *depends-on* `g05-0104`

- `g05-0115` *STATED* — ReelMimic accepts the reference as a file, a phone recording or a YouTube link.
  — [g-reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style)
  ↳ *part-of* `g05-0114`

- `g05-0118` *STATED* — ReelMimic learns how the reference was made and never reuses its footage, characters, logos or assets.
  — [g-reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style)
  ↳ *part-of* `g05-0114`
  ↳ *qualifies* `g05-0116`

- `g05-0133` *STATED* — Mortiflix makes four kinds of video today: an explainer, a social short, a logo sting and a song.
  — [g-mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer](https://chen.media/guides/mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer)
  ↳ *part-of* `g05-0128`

- `g05-0208` *STATED* — When a skill points Claude to another file, Claude does not always read the whole thing.
  — [g-claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix](https://chen.media/guides/claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix)
  ↳ *generalizes* `g05-0207`

- `g05-0215` *STATED* — Skill reference files that are only reachable through another file are the ones Claude previews partially.
  — [g-claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix](https://chen.media/guides/claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix)
  ↳ *because* `g05-0214`

- `g05-0219` *INFERRED* — A '## Contents' list at the top means even a head -100 preview reveals every section the file holds, so Claude knows to read further.
  — [g-claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix](https://chen.media/guides/claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix)
  ↳ *because* `g05-0213`
  ↳ *qualifies* `g05-0211`

- `g05-0240` *STATED* — Founder needs no signup, no API key and nothing to connect.
  — [g-the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar](https://chen.media/guides/the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar)
  ↳ *part-of* `g05-0238`
  ↳ *example-of* `g05-0314`

- `g05-0245` *STATED* — The four Founder helper tools need Python 3.8 or newer; nothing to pip install, and they never touch the network.
  — [g-the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar](https://chen.media/guides/the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar)
  ↳ *part-of* `g05-0238`
  ↳ *example-of* `g02-0240`

- `g05-0257` *STATED* — npx openqodex init finds Claude Code, lists the files it will write, asks once, and downloads the scanners.
  — [g-install-openqodex-a-second-claude-reviews-your-code-before-you-push](https://chen.media/guides/install-openqodex-a-second-claude-reviews-your-code-before-you-push)
  ↳ *defines* `g05-0256`
  ↳ *example-of* `g12-0303`

- `g06-0004` *STATED* — The /iq skill gives you a number instead of a dodge and shows its working: what you actually wrote to an AI over weeks of chats.
  > “This skill gives you a number instead, and shows its working”
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *part-of* `g06-0001`

- `g06-0013` *STATED* — The /iq skill reads only what YOU wrote, never Claude's replies.
  > “only what YOU wrote (never Claude's replies)”
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *part-of* `g06-0012`

- `g06-0015` *STATED* — The /iq skill masks passwords, tokens, emails and phone numbers in your messages.
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *part-of* `g06-0012`

- `g06-0016` *STATED* — The /iq skill saves its data only in a .iq folder in the directory where you run it.
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *part-of* `g06-0012`
  ↳ *example-of* `r01-0014`

- `g06-0018` *STATED* — The /iq skill can read a ChatGPT export or a folder of your own writing instead of Claude Code chats, if you point it at one.
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *qualifies* `g06-0017`

- `g06-0028` *STATED* — The /iq report is saved as .iq/<date>/REPORT.md.
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)

- `g06-0029` *STATED* — The /iq skill never touches your other files.
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *qualifies* `g06-0016`
  ↳ *example-of* `r01-0014`

- `g06-0034` *STATED* — Oil UI works for websites, apps, dashboards and components.
  — [g-oil-ui-make-claude-design-your-app-three-really-different-ways-then-pick-one](https://chen.media/guides/oil-ui-make-claude-design-your-app-three-really-different-ways-then-pick-one)
  ↳ *qualifies* `g06-0031`

- `g06-0075` *STATED* — anatomy is a free, MIT-licensed Agent Skill repo.
  — [g-set-up-the-anatomy-skill-the-free-repo-that-turns-any-idea-into-a-working-machin](https://chen.media/guides/set-up-the-anatomy-skill-the-free-repo-that-turns-any-idea-into-a-working-machin)
  ↳ *part-of* `g06-0074`

- `g06-0077` *STATED* — anatomy draws the idea as an isometric SVG machine, with optional WebGL shaders.
  — [g-set-up-the-anatomy-skill-the-free-repo-that-turns-any-idea-into-a-working-machin](https://chen.media/guides/set-up-the-anatomy-skill-the-free-repo-that-turns-any-idea-into-a-working-machin)
  ↳ *part-of* `g06-0074`

- `g06-0078` *STATED* — anatomy builds a figure as a standalone HTML page, a lone SVG, or a React or Next.js component, in light or dark.
  — [g-set-up-the-anatomy-skill-the-free-repo-that-turns-any-idea-into-a-working-machin](https://chen.media/guides/set-up-the-anatomy-skill-the-free-repo-that-turns-any-idea-into-a-working-machin)
  ↳ *qualifies* `g06-0077`

- `g06-0079` *STATED* — anatomy adds moving parts and live numbers to the figure.
  — [g-set-up-the-anatomy-skill-the-free-repo-that-turns-any-idea-into-a-working-machin](https://chen.media/guides/set-up-the-anatomy-skill-the-free-repo-that-turns-any-idea-into-a-working-machin)
  ↳ *part-of* `g06-0074`
  ↳ *leads-to* `g06-0080`

- `g06-0081` *STATED* — The anatomy skill also runs in OpenCode and Codex, not only Claude Code.
  — [g-set-up-the-anatomy-skill-the-free-repo-that-turns-any-idea-into-a-working-machin](https://chen.media/guides/set-up-the-anatomy-skill-the-free-repo-that-turns-any-idea-into-a-working-machin)
  ↳ *qualifies* `g06-0074`
  ↳ *evidence-for* `g15-0184`

- `g06-0106` *STATED* — magpie is MIT-licensed and runs a small gateway on your computer; your coding agents talk to it, and you choose which model answers each one.
  — [g-keep-claude-code-working-after-your-limit-runs-out](https://chen.media/guides/keep-claude-code-working-after-your-limit-runs-out)
  ↳ *defines* `g06-0105`

- `g06-0114` *STATED* — Coucou shows what your AI coding agents are doing in your Mac's notch; Claude Code is one of the agents it supports.
  — [g-approve-claude-s-permission-requests-from-your-iphone-with-coucou](https://chen.media/guides/approve-claude-s-permission-requests-from-your-iphone-with-coucou)
  ↳ *part-of* `g06-0113`
  ↳ *evidence-for* `g09-0232`

- `g06-0120` *STATED* — Coucou needs no account and no server: the Mac and the iPhone link through the same Apple Account in iCloud.
  — [g-approve-claude-s-permission-requests-from-your-iphone-with-coucou](https://chen.media/guides/approve-claude-s-permission-requests-from-your-iphone-with-coucou)
  ↳ *enables* `g06-0115`
  ↳ *example-of* `g02-0240`
  ↳ *part-of* `g09-0232`

- `g06-0121` *STATED* — Coucou's code is MIT-licensed, and its site says it has no analytics and no tracking.
  — [g-approve-claude-s-permission-requests-from-your-iphone-with-coucou](https://chen.media/guides/approve-claude-s-permission-requests-from-your-iphone-with-coucou)
  ↳ *part-of* `g06-0113`
  ↳ *part-of* `g09-0232`

- `g06-0125` *STATED* — universal-modder is a free, MIT-licensed toolkit made of Claude skills, a command line tool called um, and an MCP server for generating game art.
  — [g-set-up-universal-modder-the-free-repo-that-lets-claude-mod-your-pc-games](https://chen.media/guides/set-up-universal-modder-the-free-repo-that-lets-claude-mod-your-pc-games)
  ↳ *defines* `g06-0124`

- `g06-0127` *STATED* — universal-modder's mod-any-game skill carries playbooks for 12 engines, including Unity, Unreal, Godot, Source, Bethesda and Minecraft.
  — [g-set-up-universal-modder-the-free-repo-that-lets-claude-mod-your-pc-games](https://chen.media/guides/set-up-universal-modder-the-free-repo-that-lets-claude-mod-your-pc-games)
  ↳ *part-of* `g06-0125`

- `g06-0132` *STATED* — universal-modder can generate sprites, 3D models and audio for a mod.
  — [g-set-up-universal-modder-the-free-repo-that-lets-claude-mod-your-pc-games](https://chen.media/guides/set-up-universal-modder-the-free-repo-that-lets-claude-mod-your-pc-games)
  ↳ *depends-on* `g06-0125` — MCP server for game art

- `g06-0133` *STATED* — universal-modder can package the finished mod.
  — [g-set-up-universal-modder-the-free-repo-that-lets-claude-mod-your-pc-games](https://chen.media/guides/set-up-universal-modder-the-free-repo-that-lets-claude-mod-your-pc-games)
  ↳ *part-of* `g06-0124`

- `g06-0155` *STATED* — bigarrow has no account, no telemetry and no background process, and it is MIT licensed.
  — [g-make-claude-point-at-the-button-you-need-to-click](https://chen.media/guides/make-claude-point-at-the-button-you-need-to-click)
  ↳ *part-of* `g06-0149`
  ↳ *example-of* `g02-0240`

- `g07-0001` *STATED* — Alex's guide 'Sort Your Inbox With Claude Instead of Superhuman' says connecting Gmail to Claude lets it search, summarize, label and draft email for you.
  — [g-sort-your-inbox-with-claude-instead-of-superhuman](https://chen.media/guides/sort-your-inbox-with-claude-instead-of-superhuman)

- `g07-0004` *STATED* — Claude's Gmail connector is made by Google.
  — [g-sort-your-inbox-with-claude-instead-of-superhuman](https://chen.media/guides/sort-your-inbox-with-claude-instead-of-superhuman)
  ↳ *part-of* `g07-0001`

- `g07-0005` *STATED* — Claude's Gmail connector lets Claude search your inbox, summarize long threads, draft replies and label mail inside a normal chat.
  — [g-sort-your-inbox-with-claude-instead-of-superhuman](https://chen.media/guides/sort-your-inbox-with-claude-instead-of-superhuman)
  ↳ *part-of* `g07-0001`
  ↳ *because* `g07-0012`

- `g07-0009` *STATED* — Claude connectors work on every Claude plan, Free included.
  — [g-sort-your-inbox-with-claude-instead-of-superhuman](https://chen.media/guides/sort-your-inbox-with-claude-instead-of-superhuman)
  ↳ *part-of* `g07-0001`
  ↳ *evidence-for* `g07-0012`
  ↳ *generalizes* `g07-0116` — connectors and Design both reach the Free plan

- `g07-0023` *STATED* — Find Skills is the most installed skill on skills.sh.
  — [g-let-claude-find-and-install-the-right-skill-for-any-job](https://chen.media/guides/let-claude-find-and-install-the-right-skill-for-any-job)
  ↳ *part-of* `g07-0024`
  ↳ *evidence-for* `g10-0257`

- `g07-0031` *STATED* — Find Skills tells you each recommended skill's install count and source.
  — [g-let-claude-find-and-install-the-right-skill-for-any-job](https://chen.media/guides/let-claude-find-and-install-the-right-skill-for-any-job)
  ↳ *part-of* `g07-0024`
  ↳ *leads-to* `g07-0032`
  ↳ *part-of* `g10-0247`

- `g07-0034` *STATED* — Find Skills is free and open source under the MIT license.
  — [g-let-claude-find-and-install-the-right-skill-for-any-job](https://chen.media/guides/let-claude-find-and-install-the-right-skill-for-any-job)
  ↳ *part-of* `g07-0024`
  ↳ *evidence-for* `g10-0259`
  ↳ *example-of* `g06-0262`

- `g07-0037` *STATED* — REA was the top repo on GitHub the week Alex wrote his guide on it.
  — [g-see-how-an-apps-feature-works-with-claude-code-and-rea-free](https://chen.media/guides/see-how-an-apps-feature-works-with-claude-code-and-rea-free)
  ↳ *part-of* `g07-0038`

- `g07-0040` *STATED* — REA gives Claude Code the tools to find out how an app's feature works without the app's source code.
  — [g-see-how-an-apps-feature-works-with-claude-code-and-rea-free](https://chen.media/guides/see-how-an-apps-feature-works-with-claude-code-and-rea-free)
  ↳ *part-of* `g07-0038`

- `g07-0041` *STATED* — REA connects Claude Code to inspection tools for desktop apps, JavaScript and Electron apps, .NET programs, Android apps and websites.
  — [g-see-how-an-apps-feature-works-with-claude-code-and-rea-free](https://chen.media/guides/see-how-an-apps-feature-works-with-claude-code-and-rea-free)
  ↳ *part-of* `g07-0038`
  ↳ *enables* `g07-0040`

- `g07-0045` *STATED* — Everything REA does runs on your own machine.
  — [g-see-how-an-apps-feature-works-with-claude-code-and-rea-free](https://chen.media/guides/see-how-an-apps-feature-works-with-claude-code-and-rea-free)
  ↳ *part-of* `g07-0038`
  ↳ *example-of* `g02-0240`

- `g08-0002` *STATED* — Vibewise exists so you can vibe code and still learn: it tries to give back the way of using AI that keeps you understanding the code.
  > “Vibewise is a free plugin that tries to give you the other way of using AI back.”
  — [g-vibe-code-and-still-learn-set-up-the-free-vibewise-plugin-for-claude-code](https://chen.media/guides/vibe-code-and-still-learn-set-up-the-free-vibewise-plugin-for-claude-code)
  ↳ *evidence-for* `g05-0027`

- `g08-0060` *STATED* — PhotoCraft opens and saves Photoshop .psd files with their layers.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *qualifies* `g08-0059`

- `g08-0066` *STATED* — PhotoCraft, FilmCraft and EffectCraft are all free, with no subscription and no account.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *part-of* `g08-0049`
  ↳ *contrast* `g08-0046`

- `g08-0068` *STATED* — The Craft apps run on Mac, Windows and Linux.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *part-of* `g08-0049`

- `g08-0102` *STATED* — The Agency README describes its agents as not generic prompt templates.
  > “not generic prompt templates”
  — [g-run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents](https://chen.media/guides/run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents)
  ↳ *qualifies* `g08-0101`
  ↳ *evidence-for* `g15-0179`

- `g08-0127` *STATED* — The 21 design sites work with Claude Code, Cursor, Codex, Lovable and v0.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *qualifies* `g08-0123`

- `g08-0157` *STATED* — Replica maps an app's screens and flows, rebuilds it screen by screen, clicks through every feature to find bugs, and reads the app's real reviews so your version skips what people hate.
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *defines* `g08-0156`

- `g09-0057` *STATED* — Jarvis requires Node 20 or newer.
  — [g-run-a-jarvis-on-your-own-claude-code](https://chen.media/guides/run-a-jarvis-on-your-own-claude-code)

- `g09-0058` *STATED* — Jarvis requires Chrome or Edge in a real window, because it listens through the browser.
  > “Chrome or Edge in a real window, because it listens through the browser.”
  — [g-run-a-jarvis-on-your-own-claude-code](https://chen.media/guides/run-a-jarvis-on-your-own-claude-code)

- `g09-0059` *STATED* — You wake Jarvis by saying its name.
  > “you wake it by saying its name”
  — [g-run-a-jarvis-on-your-own-claude-code](https://chen.media/guides/run-a-jarvis-on-your-own-claude-code)
  ↳ *part-of* `g09-0050`

- `g09-0060` *STATED* — Alex pitches Jarvis setup as worth about ten minutes ('Why it's worth ten minutes').
  — [g-run-a-jarvis-on-your-own-claude-code](https://chen.media/guides/run-a-jarvis-on-your-own-claude-code)
  ↳ *qualifies* `g09-0053`

- `g09-0182` *STATED* — When you pick a logo concept, the skill builds the whole kit, and every file is yours.
  — [g-free-claude-logo-design-skill](https://chen.media/guides/free-claude-logo-design-skill)
  ↳ *part-of* `g09-0177`
  ↳ *contrast* `g09-0178` — every file is yours

- `g09-0183` *STATED* — Logo skill concepts: three logo directions built as real SVG files, shown on one overview sheet with a recommendation.
  — [g-free-claude-logo-design-skill](https://chen.media/guides/free-claude-logo-design-skill)
  ↳ *part-of* `g09-0181`
  ↳ *part-of* `g09-0177`

- `g09-0186` *STATED* — Logo skill final logo: production-ready SVG files, plus PNGs at the sizes you need.
  — [g-free-claude-logo-design-skill](https://chen.media/guides/free-claude-logo-design-skill)
  ↳ *part-of* `g09-0182`
  ↳ *part-of* `g09-0177`

- `g09-0187` *STATED* — Logo skill colour palette: your brand colours, checked for contrast.
  — [g-free-claude-logo-design-skill](https://chen.media/guides/free-claude-logo-design-skill)
  ↳ *part-of* `g09-0182`

- `g09-0188` *STATED* — Logo skill icons: favicon, app icons and the full web-manifest set, exported in one go.
  — [g-free-claude-logo-design-skill](https://chen.media/guides/free-claude-logo-design-skill)
  ↳ *part-of* `g09-0182`

- `g09-0189` *STATED* — Logo skill guidelines: a presentation board with mockups for your industry and a brand-guidelines page.
  — [g-free-claude-logo-design-skill](https://chen.media/guides/free-claude-logo-design-skill)
  ↳ *part-of* `g09-0182`

- `g09-0190` *STATED* — The logo skill works in Claude Code, in the Claude app (Claude.ai and Claude Desktop), and in other agents that support skills, such as Gemini CLI, Codex CLI, Cursor and GitHub Copilot.
  — [g-free-claude-logo-design-skill](https://chen.media/guides/free-claude-logo-design-skill)
  ↳ *qualifies* `g09-0177`
  ↳ *evidence-for* `g15-0184`

- `g09-0198` *STATED* — MiroFish builds a small world of simulated people, each with their own personality, memory and reasons.
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)
  ↳ *part-of* `g09-0195`

- `g09-0199` *STATED* — MiroFish's simulated people post about your launch, reply to each other, like and pile on, across a Twitter-style feed and a Reddit-style one.
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)
  ↳ *part-of* `g09-0195`

- `g09-0200` *STATED* — MiroFish writes you a report, and you can ask any one simulated person why they did or didn't buy.
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)
  ↳ *part-of* `g09-0195`

- `g09-0234` *STATED* — Coucou shows live activity in the notch: every file Claude reads, edits and runs, step by step.
  — [g-coucou-free-notch-pet-that-watches-claude-code](https://chen.media/guides/coucou-free-notch-pet-that-watches-claude-code)
  ↳ *part-of* `g09-0232`

- `g09-0235` *STATED* — Coucou shows each edit with the file name and how many lines were added and removed, and a tap opens the full diff.
  — [g-coucou-free-notch-pet-that-watches-claude-code](https://chen.media/guides/coucou-free-notch-pet-that-watches-claude-code)
  ↳ *qualifies* `g09-0234`
  ↳ *part-of* `g09-0232`

- `g09-0236` *STATED* — Coucou shows every agent in one place (Claude Code, Codex, Cursor, Gemini CLI, Antigravity and more), each in a pill of its own.
  — [g-coucou-free-notch-pet-that-watches-claude-code](https://chen.media/guides/coucou-free-notch-pet-that-watches-claude-code)
  ↳ *part-of* `g09-0232`
  ↳ *evidence-for* `g15-0184`

- `g09-0239` *STATED* — Mochi jumps when a Claude Code task finishes, so you can stay in your email or your feed until then.
  — [g-coucou-free-notch-pet-that-watches-claude-code](https://chen.media/guides/coucou-free-notch-pet-that-watches-claude-code)
  ↳ *part-of* `g09-0232`

- `g09-0240` *STATED* — One click in Coucou opens the exact terminal window of that Claude Code session.
  — [g-coucou-free-notch-pet-that-watches-claude-code](https://chen.media/guides/coucou-free-notch-pet-that-watches-claude-code)
  ↳ *part-of* `g09-0232`

- `g09-0241` *STATED* — Coucou hides when nothing is running and peeks out when you hover over the notch.
  — [g-coucou-free-notch-pet-that-watches-claude-code](https://chen.media/guides/coucou-free-notch-pet-that-watches-claude-code)
  ↳ *part-of* `g09-0232`

- `g10-0116` *STATED* — Each of the 14 AI sites worth bookmarking does one job better than a general chatbot does.
  > “each one does one job better than a general chatbot does”
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)
  ↳ *qualifies* `g10-0114`

- `g10-0117` *STATED* — Most of the 14 bookmark-worthy AI sites have a free plan, so you can try every one of them today.
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)
  ↳ *qualifies* `g10-0114`

- `g10-0153` *STATED* — In Photon Studio even subject selection and background removal run offline.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *part-of* `g10-0152`

- `g10-0154` *STATED* — Photon Studio runs on Mac, Windows and Linux.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *qualifies* `g10-0152`
  ↳ *contradicts* `y03-0141` — Photon Studio platforms: 'Mac, Windows and Linux' (guide) vs 'macOS and Windows' (video)

- `g10-0163` *STATED* — Photon Studio was released by a small studio and covers most of what people pay Photoshop for, opening Photoshop's own PSD files with their layers intact.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *defines* `g10-0152`

- `g10-0164` *STATED* — Photon Studio has no account to create and nothing to upload: every edit happens on your own computer.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *part-of* `g10-0152`
  ↳ *example-of* `g02-0240`

- `g10-0165` *STATED* — Photon Studio layers, groups and masks: stack, group and mask the parts of a design, with adjustment layers, smart objects and layer effects.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *part-of* `g10-0152`

- `g10-0166` *STATED* — Photon Studio retouching: curves and levels with a live preview, healing brushes, the clone stamp, content-aware fill and Liquify.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *part-of* `g10-0152`

- `g10-0167` *STATED* — Photon Studio design tools: editable text, vector shapes and Pen paths, brushes, colours and gradients.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *part-of* `g10-0152`

- `g10-0168` *STATED* — Photon Studio subject selection selects the subject of a photo in one click.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *depends-on* `g10-0172`

- `g10-0169` *STATED* — Photon Studio background removal cuts the background away in one click.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *depends-on* `g10-0172`
  ↳ *contrast* `g10-0127` — free offline bg removal vs watermarked Photoroom free plan

- `g10-0170` *STATED* — Photon Studio opens Photoshop documents with their layers intact and saves back to PSD.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *evidence-for* `g10-0163`
  ↳ *part-of* `g10-0152`

- `g10-0171` *STATED* — Photon Studio keeps the familiar Photoshop shortcuts, plus a search box that finds any command by name.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *part-of* `g10-0152`

- `g10-0172` *STATED* — The AI behind Photon Studio's subject selection and background removal runs on your machine, so your photos never leave it, and both still work with the Wi-Fi off.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *because* `g10-0153`

- `g10-0202` *STATED* — Open Design runs on the model you choose, DeepSeek included.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *part-of* `g10-0198`
  ↳ *example-of* `g16-0013`

- `g10-0212` *STATED* — Open Design is licensed Apache 2.0.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *part-of* `g10-0198`

- `g10-0213` *STATED* — In Open Design you describe what you want and it builds the website, the app screen or the slide deck in front of you, in the style of a real brand if you like.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *defines* `g10-0198`

- `g10-0214` *STATED* — Open Design's model can be DeepSeek, a model running on your own computer, or any provider you already pay for.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *qualifies* `g10-0202`

- `g10-0215` *STATED* — Open Design websites and landing pages: a working single-page site you can click through, for desktop or mobile.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *part-of* `g10-0213`
  ↳ *part-of* `g10-0198`

- `g10-0216` *STATED* — Open Design app screens: mobile and desktop app screens as live, clickable prototypes.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *part-of* `g10-0213`
  ↳ *part-of* `g10-0198`

- `g10-0218` *STATED* — Open Design makes live dashboards and email marketing templates.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *part-of* `g10-0213`

- `g10-0220` *STATED* — Open Design turns your idea into an animated motion-graphics MP4, in 16:9 or vertical 9:16 for reels and TikTok.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *defines* `g10-0209`

- `g10-0222` *STATED* — Everything Open Design makes comes out as real files you keep: HTML, PDF, PowerPoint, ZIP, Markdown and MP4.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *part-of* `g10-0209`
  ↳ *part-of* `g10-0198`

- `g10-0224` *STATED* — Dyad does what Lovable does for free, with no sign-up and no credits running out, so it can replace a Lovable subscription.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *qualifies* `g10-0223`
  ↳ *example-of* `g10-0267`
  ↳ *example-of* `g18-0287`

- `g10-0236` *STATED* — In Dyad you describe the app and the AI writes it while a live preview updates next to the chat.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *defines* `g10-0223`

- `g10-0239` *STATED* — Dyad's code is plain files on your disk, and they're yours.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *enables* `g10-0244`
  ↳ *example-of* `g02-0240`
  ↳ *part-of* `g10-0223`

- `g10-0240` *STATED* — Dyad's free version is the whole builder.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *evidence-for* `g10-0224`
  ↳ *part-of* `g10-0223`

- `g10-0242` *STATED* — With your own API key in Dyad you build as many apps as you want and pay only the AI provider's own usage price.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *part-of* `g10-0238`
  ↳ *analogy-for* `g17-0270`
  ↳ *part-of* `g10-0223`

- `g10-0243` *STATED* — One click in Dyad connects Supabase or Neon, so your app gets a real database and working user logins, not a login page that logs no one in.
  > “not a login page that logs no one in”
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *defines* `g10-0229`

- `g10-0245` *STATED* — Dyad needs no sign-up: download it and go.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *evidence-for* `g10-0224`
  ↳ *part-of* `g10-0223`

- `g10-0257` *STATED* — The most installed agent skill isn't a design skill or a coding skill; it's the skill that finds the others, Find Skills.
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)

- `g10-0259` *STATED* — Find Skills is free and open source.
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)
  ↳ *part-of* `g10-0247`

- `g10-0260` *STATED* — Find Skills checks the skills.sh leaderboard first, which ranks every skill by total installs, then searches the whole catalogue if the leaderboard doesn't cover your job.
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)
  ↳ *part-of* `g10-0252`
  ↳ *part-of* `g10-0247`

- `g10-0262` *STATED* — Find Skills ranks official sources like Vercel, Anthropic and Microsoft above unknown authors.
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)
  ↳ *part-of* `g10-0252`
  ↳ *evidence-for* `g10-0266`

- `g10-0264` *STATED* — Say yes and Find Skills runs the install itself, so the new skill is in your setup right away.
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)
  ↳ *part-of* `g10-0247`

- `g10-0265` *STATED* — The skills Find Skills installs work in Claude Code, Codex, Cursor, GitHub Copilot, Gemini CLI and 75 more coding agents.
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)
  ↳ *qualifies* `g10-0247`
  ↳ *contradicts* `g18-0086` — skills CLI reach: Find Skills skills work in Claude Code + '75 more coding agents' vs npx skills works with '40 or so other agents'
  ↳ *evidence-for* `g15-0184`

- `g11-0012` *STATED* — In Instatic you describe a page and Claude builds it on a visual canvas as real buttons, text and pictures you can drag around.
  > “Describe a page, and Claude builds it on a visual canvas as real buttons, text and pictures you can drag around.”
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *part-of* `g11-0011`

- `g11-0013` *STATED* — Every page Instatic publishes is plain HTML on a server you pick, so you own the pages.
  > “every page it publishes is plain HTML you own”
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *part-of* `g11-0011`
  ↳ *example-of* `g02-0240`

- `g11-0018` *STATED* — Instatic has an AI agent built into the editor that works with your own Claude key.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *enables* `g11-0012`
  ↳ *part-of* `g11-0011`

- `g11-0019` *STATED* — Instatic is free under the MIT license.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *evidence-for* `g11-0014`
  ↳ *example-of* `g06-0262`

- `g11-0021` *STATED* — With Instatic you pay for your own small server instead of a per-site plan.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *qualifies* `g11-0019` — free licence but you still pay a small server

- `g11-0022` *STATED* — Claude builds on Instatic's canvas, not in a code box: everything it adds is a normal element on the page.
  > “Claude builds on the canvas, not in a code box”
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *defines* `g11-0012`

- `g11-0023` *STATED* — An element Claude adds in Instatic can be clicked, moved, re-texted and restyled exactly as if you had placed it yourself.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *example-of* `g11-0022`

- `g11-0024` *STATED* — Instatic's agent runs on your Claude API key, or on OpenAI, OpenRouter, or a local model through Ollama.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *qualifies* `g11-0018`
  ↳ *example-of* `g17-0270`

- `g11-0026` *STATED* — Instatic publishes plain HTML and compact CSS, with no framework and no editor code left in the page.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *evidence-for* `g11-0013`
  ↳ *part-of* `g11-0011`

- `g11-0027` *STATED* — You can export a whole Instatic site as one ZIP file at any time.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *evidence-for* `g11-0013`

- `g11-0028` *STATED* — Instatic hosting: one-click deploy to Railway, or run it on Render, or on your own server with Docker.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *enables* `g11-0013`
  ↳ *part-of* `g11-0011`

- `g11-0030` *STATED* — Instatic is also a full CMS: blog posts, custom collections, forms that save to your own database, and user roles.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *qualifies* `g11-0011` — more than a page builder

- `g11-0182` *STATED* — FluidVoice's speech model runs on your own Mac, so it works with no internet.
  — [g-fluidvoice-the-free-open-source-wispr-flow](https://chen.media/guides/fluidvoice-the-free-open-source-wispr-flow)
  ↳ *part-of* `g11-0181`
  ↳ *enables* `g11-0190`

- `g11-0189` *STATED* — Wispr's own docs say an internet connection is required for transcription.
  — [g-fluidvoice-the-free-open-source-wispr-flow](https://chen.media/guides/fluidvoice-the-free-open-source-wispr-flow)
  ↳ *contrast* `g11-0190`

- `g11-0190` *STATED* — FluidVoice turns speech into text on your Mac, so it types on a plane, on a train or on bad hotel Wi-Fi.
  — [g-fluidvoice-the-free-open-source-wispr-flow](https://chen.media/guides/fluidvoice-the-free-open-source-wispr-flow)
  ↳ *part-of* `g11-0181`

- `g11-0191` *STATED* — Wispr says its transcription always happens in the cloud.
  — [g-fluidvoice-the-free-open-source-wispr-flow](https://chen.media/guides/fluidvoice-the-free-open-source-wispr-flow)
  ↳ *contrast* `g11-0192`

- `g11-0192` *STATED* — FluidVoice keeps your voice and text on your Mac unless you choose to plug in a cloud AI provider.
  — [g-fluidvoice-the-free-open-source-wispr-flow](https://chen.media/guides/fluidvoice-the-free-open-source-wispr-flow)
  ↳ *example-of* `g02-0240`
  ↳ *part-of* `g11-0181`

- `g11-0193` *STATED* — FluidVoice types straight into the app you're in: email, Slack, Notes, the Claude app or your terminal.
  — [g-fluidvoice-the-free-open-source-wispr-flow](https://chen.media/guides/fluidvoice-the-free-open-source-wispr-flow)
  ↳ *qualifies* `g11-0181`

- `g11-0199` *STATED* — Cloning your voice on ElevenLabs means a paid plan every month, because cloning isn't on its free tier.
  — [g-the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer](https://chen.media/guides/the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer)
  ↳ *contrast* `g11-0198`

- `g11-0200` *STATED* — One developer wrote almost all of VoiceStudio.
  — [g-the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer](https://chen.media/guides/the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer)
  ↳ *qualifies* `g11-0198`

- `g11-0203` *STATED* — VoiceStudio needs no account, no cloud and no API key, so your voice never leaves your machine and there's nothing to cancel.
  — [g-the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer](https://chen.media/guides/the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer)
  ↳ *qualifies* `g11-0198`
  ↳ *analogy-for* `g11-0192` — local-first privacy
  ↳ *example-of* `g02-0240`

- `g11-0204` *STATED* — VoiceStudio's Audiobooks tool turns a whole book or a long script into audio in your voice, with a queue for long jobs.
  — [g-the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer](https://chen.media/guides/the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer)
  ↳ *part-of* `g11-0198`

- `g11-0205` *STATED* — VoiceStudio's Dictation tool is a floating button: talk, and it types out what you said.
  — [g-the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer](https://chen.media/guides/the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer)
  ↳ *part-of* `g11-0198`
  ↳ *contrast* `g11-0181` — both offer local dictation

- `g11-0206` *STATED* — VoiceStudio's Transcripts tool writes out any recording and splits it by who said what.
  — [g-the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer](https://chen.media/guides/the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer)
  ↳ *part-of* `g11-0198`

- `g11-0207` *STATED* — VoiceStudio's Video dubbing re-voices your video in another language, in your own voice, timed to the original.
  — [g-the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer](https://chen.media/guides/the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer)
  ↳ *part-of* `g11-0198`

- `g11-0208` *STATED* — VoiceStudio's Voice design lets you describe a voice in words and makes one that doesn't belong to anyone.
  — [g-the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer](https://chen.media/guides/the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer)
  ↳ *part-of* `g11-0198`

- `g11-0209` *STATED* — Every clip VoiceStudio makes gets an AI watermark so it can be told apart from a real recording.
  — [g-the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer](https://chen.media/guides/the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer)
  ↳ *qualifies* `g11-0198`

- `g12-0056` *STATED* — Nothing touches your accounts until you approve the go-live skill's plan.
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *qualifies* `g12-0055`

- `g12-0064` *STATED* — For a provider not on the go-live skill's built-in list, it walks you through setup with that provider's own tools on a best-effort basis.
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *qualifies* `g12-0051`

- `g12-0069` *STATED* — Guide section 'Why it's safe to hand it your accounts' argues the go-live skill is safe to give account access (body email-gated).
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *part-of* `g12-0050`
  ↳ *depends-on* `g12-0056`
  ↳ *depends-on* `g12-0063`
  ↳ *part-of* `g12-0051`

- `g12-0133` *STATED* — The SEO skill checks a site the way Google does and scores what holds it back: pages that load too slowly, pages Google can't find, missing local-search info, and whether Google's AI answers would ever mention you.
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *part-of* `g12-0131`
  ↳ *part-of* `g17-0099`

- `g12-0134` *STATED* — The SEO skill outputs a health score out of 100 and a ranked action plan with the most important fix first.
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *part-of* `g12-0131`
  ↳ *evidence-for* `g17-0102`

- `g12-0155` *STATED* — Two days after launch Anthropic opened Claude Marketplace to everyone: any developer on a paid Claude plan can now submit their own plugin.
  — [g-claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed](https://chen.media/guides/claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed)

- `g12-0156` *STATED* — Once a Claude Marketplace plugin is live, people add it in one click on claude.ai, the desktop and mobile apps, Cowork and Claude Code.
  — [g-claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed](https://chen.media/guides/claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed)
  ↳ *depends-on* `g12-0155`
  ↳ *part-of* `g12-0154`

- `g12-0165` *STATED* — A plugin with only skills is complete, so you don't need to build a server to have a plugin in the Claude Marketplace.
  — [g-claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed](https://chen.media/guides/claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed)
  ↳ *because* `g12-0163`
  ↳ *depends-on* `g12-0162`

- `g12-0187` *STATED* — SupoClip does the same job as OpusClip, is open source, and runs on your own computer instead of costing $29 a month.
  — [g-supoclip-open-source-opusclip-alternative](https://chen.media/guides/supoclip-open-source-opusclip-alternative)
  ↳ *part-of* `g12-0184`

- `g12-0189` *STATED* — SupoClip describes itself as an open-source OpusClip alternative.
  — [g-supoclip-open-source-opusclip-alternative](https://chen.media/guides/supoclip-open-source-opusclip-alternative)
  ↳ *evidence-for* `g12-0187`

- `g12-0280` *STATED* — NVIDIA hosts four open coding models for free, and the key plugs into Claude Code, Codex, Cursor and Cline.
  — [g-free-kimi-k3-glm-and-deepseek-on-one-nvidia-key](https://chen.media/guides/free-kimi-k3-glm-and-deepseek-on-one-nvidia-key)
  ↳ *part-of* `g12-0279`
  ↳ *example-of* `g16-0013`

- `g12-0290` *STATED* — NVIDIA's free model key needs no credit card and no separate subscription for each model.
  — [g-free-kimi-k3-glm-and-deepseek-on-one-nvidia-key](https://chen.media/guides/free-kimi-k3-glm-and-deepseek-on-one-nvidia-key)
  ↳ *part-of* `g12-0281`

- `g12-0292` *STATED* — NVIDIA's model API speaks the OpenAI-style API, so most coding tools can use it.
  — [g-free-kimi-k3-glm-and-deepseek-on-one-nvidia-key](https://chen.media/guides/free-kimi-k3-glm-and-deepseek-on-one-nvidia-key)
  ↳ *enables* `g12-0280`

- `g13-0007` *STATED* — Bot Crossing needs no account and uploads nothing: it only reads the Claude Code session files already on your computer.
  > “No account and nothing uploaded: it only reads the session files already on your computer”
  — [g-watch-every-claude-code-session-as-a-bot-in-bot-crossing](https://chen.media/guides/watch-every-claude-code-session-as-a-bot-in-bot-crossing)
  ↳ *qualifies* `g13-0001` — privacy model
  ↳ *example-of* `g02-0240`

- `g13-0008` *STATED* — Bot Crossing works with Claude Code, Codex, Cursor, OpenCode, Antigravity CLI, Hermes and Kilo Code.
  — [g-watch-every-claude-code-session-as-a-bot-in-bot-crossing](https://chen.media/guides/watch-every-claude-code-session-as-a-bot-in-bot-crossing)
  ↳ *part-of* `g13-0001`
  ↳ *evidence-for* `g15-0184`

- `g13-0065` *STATED* — Scraping retrieves only what a source actually contains.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *because* `g13-0066`

- `g13-0068` *STATED* — Scrapling includes stealth-oriented browser features, but websites can still block requests.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *evidence-for* `g13-0067`
  ↳ *qualifies* `g13-0061`

- `g13-0127` *STATED* — /watch works with YouTube, Loom, TikTok, Instagram, X, Vimeo and many more sites, plus video files on your computer.
  — [g-let-claude-code-watch-any-video-with-watch](https://chen.media/guides/let-claude-code-watch-any-video-with-watch)
  ↳ *qualifies* `g13-0119`

- `g13-0128` *STATED* — /watch uses the video's own captions first, so most public videos need no extra API keys.
  — [g-let-claude-code-watch-any-video-with-watch](https://chen.media/guides/let-claude-code-watch-any-video-with-watch)
  ↳ *qualifies* `g13-0125`
  ↳ *part-of* `g13-0119`
  ↳ *enables* `g13-0127`

- `g13-0129` *STATED* — Every /watch answer comes with timestamps, so you can jump straight to the moment in the video.
  — [g-let-claude-code-watch-any-video-with-watch](https://chen.media/guides/let-claude-code-watch-any-video-with-watch)
  ↳ *depends-on* `g13-0125`
  ↳ *part-of* `g13-0119`

- `g13-0130` *STATED* — /watch is free and open source under the MIT licence.
  — [g-let-claude-code-watch-any-video-with-watch](https://chen.media/guides/let-claude-code-watch-any-video-with-watch)
  ↳ *qualifies* `g13-0119`
  ↳ *example-of* `g06-0262`

- `g13-0144` *STATED* — Anything you mark private is never saved by claude-mem.
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *qualifies* `g13-0136`

- `g13-0145` *STATED* — claude-mem runs on its own in the background once it's installed.
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *qualifies* `g13-0136`

- `g13-0157` *STATED* — The Public APIs directory covers areas such as weather, food, news and cryptocurrency.
  — [g-public-apis-claude-code-build-guide](https://chen.media/guides/public-apis-claude-code-build-guide)
  ↳ *part-of* `g13-0153`

- `g13-0158` *STATED* — Public APIs directory tables list each API's description, authentication, HTTPS and CORS.
  — [g-public-apis-claude-code-build-guide](https://chen.media/guides/public-apis-claude-code-build-guide)
  ↳ *part-of* `g13-0153`

- `g13-0159` *STATED* — You do not need to clone or install the whole Public APIs repository to use an API in the list.
  — [g-public-apis-claude-code-build-guide](https://chen.media/guides/public-apis-claude-code-build-guide)
  ↳ *qualifies* `g13-0156`
  ↳ *part-of* `g13-0153`

- `g13-0196` *STATED* — HackingTool's documented interface is a terminal app; Alex's guide does not rely on a native Claude Code integration or a one-click desktop installer.
  — [g-hackingtool-secure-your-own-apps](https://chen.media/guides/hackingtool-secure-your-own-apps)
  ↳ *qualifies* `g13-0189`

- `g13-0283` *STATED* — You do not need to install the whole list of 100 skills.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *because* `g13-0281`

- `g13-0284` *STATED* — The 100 linked skill instruction files are publicly accessible without buying the skill itself.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *qualifies* `g13-0282`

- `g14-0075` *STATED* — The Antigravity VS Code extension requires an eligible Google account, and a free Antigravity plan qualifies.
  > “A free Antigravity plan qualifies.”
  — [g-antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you](https://chen.media/guides/antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you)
  ↳ *qualifies* `g14-0082`

- `g14-0076` *STATED* — The Antigravity VS Code extension installs the local 'agy' backend service on its first launch.
  > “The extension installs the local agy backend service on its first launch.”
  — [g-antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you](https://chen.media/guides/antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you)
  ↳ *part-of* `g14-0073`

- `g14-0104` *STATED* — Agent Reach's intended environment is Claude Code and other agents that can execute terminal commands.
  — [g-agent-reach-web-research-setup](https://chen.media/guides/agent-reach-web-research-setup)
  ↳ *qualifies* `g14-0101`
  ↳ *contrast* `g14-0223` — terminal-capable agents

- `g14-0223` *STATED* — ECC adds reusable instructions and tooling to a coding agent and can be used with Claude Code or Codex.
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *qualifies* `g14-0222`
  ↳ *evidence-for* `g15-0184`

- `g14-0289` *STATED* — Reusable Claude skills can help a solo founder organize marketing, social media, design, finance and legal jobs.
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *part-of* `g14-0287`
  ↳ *because* `g14-0288`

- `g14-0291` *STATED* — The department skill libraries in the AI-team video are free to download.
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *part-of* `g14-0287`

- `g15-0008` *STATED* — Skiper UI is the library for the blocks you always need anyway.
  — [g-four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed](https://chen.media/guides/four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed)
  ↳ *part-of* `g15-0001`

- `g15-0009` *STATED* — Vengeance UI is the library for the cinematic half of a site.
  — [g-four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed](https://chen.media/guides/four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed)
  ↳ *part-of* `g15-0001`

- `g15-0010` *STATED* — Animmaster Lib is the UI library to reach for when you want volume.
  — [g-four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed](https://chen.media/guides/four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed)
  ↳ *part-of* `g15-0001`

- `g15-0011` *STATED* — React Bits is the UI library for the finish.
  — [g-four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed](https://chen.media/guides/four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed)
  ↳ *part-of* `g15-0001`

- `g15-0043` *STATED* — sergebulaev/linkedin-skills' main branch was pushed the day before the guide was written, so it is under active development.
  — [g-linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes](https://chen.media/guides/linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes)
  ↳ *qualifies* `g15-0041`

- `g15-0045` *CORE* — Claude reads each skill's description and turns the right skill on by itself when your request matches it; you do not pick skills from a menu.
  — [g-linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes](https://chen.media/guides/linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes)
  ↳ *because* `g15-0189`
  ↳ *evidence-for* `g17-0228`

- `g15-0056` *STATED* — Treat 'the ADHD skill' as a description of a behaviour, not as a package name.
  — [g-claude-code-says-done-before-it-has-proved-anything-this-fixes-it](https://chen.media/guides/claude-code-says-done-before-it-has-proved-anything-this-fixes-it)

- `g15-0061` *STATED* — anydoc, herdr, DeepSeek Harness and OmniRoute are four open-source GitHub repos that each fix one specific thing that goes wrong when you use Claude for real work; none is a prompt pack, each is a tool you install once.
  — [g-four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute](https://chen.media/guides/four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute)
  ↳ *example-of* `g15-0179`

- `g15-0062` *STATED* — The four problems anydoc, herdr, DeepSeek Harness and OmniRoute fix: office files that turn to mush, a terminal full of tangled agents, a model you cannot swap, and a usage limit that stops you mid task.
  — [g-four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute](https://chen.media/guides/four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute)
  ↳ *defines* `g15-0061`

- `g15-0110` *STATED* — wshobson/agents runs in Claude Code and also Codex, Cursor, OpenCode, GitHub Copilot and Antigravity.
  — [g-the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build](https://chen.media/guides/the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build)
  ↳ *example-of* `g15-0184`

- `g15-0118` *STATED* — The Agency installs into Claude Code, Cursor, Codex, Gemini CLI, GitHub Copilot, Windsurf, Qwen, OpenCode and Osaurus.
  — [g-the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install](https://chen.media/guides/the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install)
  ↳ *example-of* `g15-0184`
  ↳ *qualifies* `g15-0113`
  ↳ *part-of* `g08-0089`

- `g15-0147` *STATED* — The one-tab guide is not a list of coupons: it covers how a one-tab route works mechanically, what you give up, and the checks that separate a real aggregator from a wrapper.
  — [g-every-premium-ai-model-in-one-place-how-the-one-tab-route-actually-works](https://chen.media/guides/every-premium-ai-model-in-one-place-how-the-one-tab-route-actually-works)
  ↳ *qualifies* `g15-0146`

- `g15-0184` *CORE* — Agent and skill bundles now install across many harnesses, not just Claude Code: linkedin-skills (Claude Code, Codex), wshobson/agents (Codex, Cursor, OpenCode, Copilot, Antigravity), The Agency (nine harnesses incl. Gemini CLI, Windsurf, Qwen, Osaurus).
  — [g-linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes](https://chen.media/guides/linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes) [g-the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build](https://chen.media/guides/the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build) [g-the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install](https://chen.media/guides/the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install)

- `g16-0145` *STATED* — Leon Lin also ships taste-skill, at 79,304 stars, which is most of the reason unlazy spread as fast as it did.
  — [g-the-free-skill-that-stops-claude-saying-done-when-it-is-not](https://chen.media/guides/the-free-skill-that-stops-claude-saying-done-when-it-is-not)
  ↳ *part-of* `g16-0006`

- `g16-0218` *STATED* — Five free Google AI tools replace paid subscriptions most people are still buying; his guide gives the exact point where each one stops being free.
  > “the exact point where each one stops being free”
  — [g-five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for](https://chen.media/guides/five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for)
  ↳ *example-of* `g16-0001`
  ↳ *example-of* `g16-0008`

- `g16-0221` *STATED* — Five Google AI products replace something you are probably paying for right now, which is a different claim and a much smaller list.
  > “which is a different claim and a much smaller list”
  — [g-five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for](https://chen.media/guides/five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for)
  ↳ *contrast* `g16-0220`
  ↳ *evidence-for* `g16-0218`

- `g16-0232` *STATED* — Five public GitHub repositories, 945,792 stars between them, replace software most people pay a monthly fee for.
  — [g-five-free-github-repos-that-replace-software-you-pay-for](https://chen.media/guides/five-free-github-repos-that-replace-software-you-pay-for)
  ↳ *example-of* `g16-0001`
  ↳ *part-of* `g16-0006`
  ↳ *example-of* `g18-0287`

- `g16-0233` *STATED* — This is not a list of cheap alternatives: every one of the five repos is free, public and open.
  > “This is not a list of cheap alternatives.”
  — [g-five-free-github-repos-that-replace-software-you-pay-for](https://chen.media/guides/five-free-github-repos-that-replace-software-you-pay-for)
  ↳ *qualifies* `g16-0232`
  ↳ *because* `g16-0234`

- `g16-0277` *STATED* — Prompt Master is not a Claude only tool: it works with Claude, Claude Code, ChatGPT, Gemini, Cursor, Windsurf, Copilot, Midjourney and about thirty more.
  > “It is not a Claude only tool”
  — [g-the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting](https://chen.media/guides/the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting)
  ↳ *qualifies* `g16-0270`
  ↳ *evidence-for* `g15-0184`

- `g16-0282` *STATED* — Three plugins fix Claude Code's setup, limits and memory: Claude Code Setup, OmniRoute and Claude Mem.
  — [g-three-plugins-that-fix-claude-code-s-setup-limits-and-memory](https://chen.media/guides/three-plugins-that-fix-claude-code-s-setup-limits-and-memory)
  ↳ *because* `g16-0287`
  ↳ *example-of* `g16-0001`

- `g16-0286` *STATED* — There are hundreds of Claude Code plugins now and almost all of them make Claude better at a task you already knew you wanted done.
  — [g-three-plugins-that-fix-claude-code-s-setup-limits-and-memory](https://chen.media/guides/three-plugins-that-fix-claude-code-s-setup-limits-and-memory)
  ↳ *contrast* `g16-0287`

- `g16-0293` *STATED* — Ruflo is the repo you may know as claude-flow; it renamed itself, and the README says so in its own words.
  — [g-ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm](https://chen.media/guides/ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm)
  ↳ *qualifies* `g16-0292`

- `g16-0305` *STATED* — Seven free Claude Code repos each take over a job you are currently doing by hand.
  > “Seven free repos that each take over a job you are currently doing by hand”
  — [g-seven-free-claude-code-repos-that-fix-what-claude-gets-wrong](https://chen.media/guides/seven-free-claude-code-repos-that-fix-what-claude-gets-wrong)
  ↳ *example-of* `g16-0001`
  ↳ *part-of* `g16-0015`

- `g16-0307` *STATED* — There are thousands of Claude Code repos on GitHub and almost all of them are wrappers, demos or abandoned experiments.
  — [g-seven-free-claude-code-repos-that-fix-what-claude-gets-wrong](https://chen.media/guides/seven-free-claude-code-repos-that-fix-what-claude-gets-wrong)
  ↳ *contrast* `g16-0308`
  ↳ *evidence-for* `g15-0179`

- `g16-0311` *STATED* — Every one of the seven repos is free and open source.
  — [g-seven-free-claude-code-repos-that-fix-what-claude-gets-wrong](https://chen.media/guides/seven-free-claude-code-repos-that-fix-what-claude-gets-wrong)
  ↳ *qualifies* `g16-0305`
  ↳ *example-of* `g16-0008`

- `g17-0002` *STATED* — All seven Claude skills in Alex Chen's marketing-department stack are free and public.
  > “All seven of these are free and public right now.”
  — [g-seven-free-claude-skills-that-cover-a-marketing-department](https://chen.media/guides/seven-free-claude-skills-that-cover-a-marketing-department)
  ↳ *contrast* `g17-0003`

- `g17-0004` *STATED* — Of the seven free marketing Claude skills, three change what you produce, two change how you decide, and two go out and act.
  > “three of them change what you produce, two change how you decide, and two go out and act”
  — [g-seven-free-claude-skills-that-cover-a-marketing-department](https://chen.media/guides/seven-free-claude-skills-that-cover-a-marketing-department)
  ↳ *part-of* `g17-0001`

- `g17-0097` *STATED* — Claude Mem fixes one specific Claude Code problem, named in the plugins guide.
  > “Claude Mem, and the thing it fixes”
  — [g-the-three-claude-code-plugins-worth-installing](https://chen.media/guides/the-three-claude-code-plugins-worth-installing)
  ↳ *qualifies* `g17-0091`
  ↳ *part-of* `g13-0136`

- `g17-0102` *STATED* — Claude SEO returns a prioritised action plan rather than a list of complaints, sequenced so the thing you fix first is the thing everything else depends on.
  > “What comes back is not a list of complaints. It is a prioritised action plan”
  — [g-install-25-seo-skills-and-18-specialist-agents-into-claude-code](https://chen.media/guides/install-25-seo-skills-and-18-specialist-agents-into-claude-code)
  ↳ *part-of* `g17-0099`
  ↳ *example-of* `g17-0312`

- `g17-0149` *STATED* — FreeLLMAPI keeps provider keys AES-256-GCM encrypted at rest and decrypts them in memory per request.
  — [g-pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint](https://chen.media/guides/pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint)
  ↳ *part-of* `g17-0143`

- `g17-0152` *STATED* — Alex Chen's guide explains why FreeLLMAPI does not fall over when a provider's limit is hit.
  > “Why it does not fall over”
  — [g-pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint](https://chen.media/guides/pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint)
  ↳ *qualifies* `g17-0150`

- `g17-0158` *STATED* — With Project NOMAD you install one thing and it handles the rest.
  > “You install one thing; it handles the rest.”
  — [g-a-knowledge-server-that-keeps-answering-with-the-internet-off](https://chen.media/guides/a-knowledge-server-that-keeps-answering-with-the-internet-off)
  ↳ *qualifies* `g17-0157`

- `g17-0160` *STATED* — Project NOMAD needs no desktop environment, so a NOMAD box can sit headless in a cupboard and be used from a laptop or phone on the same network.
  > “a NOMAD box can sit headless in a cupboard”
  — [g-a-knowledge-server-that-keeps-answering-with-the-internet-off](https://chen.media/guides/a-knowledge-server-that-keeps-answering-with-the-internet-off)
  ↳ *because* `g17-0159`

- `g17-0162` *STATED* — Project NOMAD needs internet only while you install it and while you choose to download more content; after that it runs with nothing plugged in.
  > “After that it runs with nothing plugged in.”
  — [g-a-knowledge-server-that-keeps-answering-with-the-internet-off](https://chen.media/guides/a-knowledge-server-that-keeps-answering-with-the-internet-off)
  ↳ *because* `g17-0161`
  ↳ *example-of* `g02-0240`

- `g17-0227` *STATED* — A Claude skill can bundle scripts, reference documents and assets alongside SKILL.md, but none of that is required.
  > “It can bundle scripts, reference documents and assets alongside it, but none of that is required.”
  — [g-164-claude-skills-in-one-repo-which-to-take-first](https://chen.media/guides/164-claude-skills-in-one-repo-which-to-take-first)
  ↳ *qualifies* `g17-0225`
  ↳ *qualifies* `g18-0100`

- `g17-0228` *CORE* — A skill's description is the important part: it is what Claude reads when deciding whether the skill is relevant to what you just asked.
  > “The description is the important part.”
  — [g-164-claude-skills-in-one-repo-which-to-take-first](https://chen.media/guides/164-claude-skills-in-one-repo-which-to-take-first)
  ↳ *qualifies* `g17-0226`

- `g17-0230` *STATED* — A precise skill description means the skill fires when it should.
  > “A precise one means it fires when it should.”
  — [g-164-claude-skills-in-one-repo-which-to-take-first](https://chen.media/guides/164-claude-skills-in-one-repo-which-to-take-first)
  ↳ *because* `g17-0228`

- `g17-0231` *STATED* — The simple SKILL.md format is why a 164-skill list can exist at all: a skill is portable text.
  > “A skill is portable text”
  — [g-164-claude-skills-in-one-repo-which-to-take-first](https://chen.media/guides/164-claude-skills-in-one-repo-which-to-take-first)
  ↳ *because* `g17-0223`
  ↳ *because* `g18-0100`

- `g17-0235` *STATED* — Branding skills in the ComposioHQ repo do not live where you would expect; the guide says where they actually live.
  > “Where "branding" actually lives”
  — [g-164-claude-skills-in-one-repo-which-to-take-first](https://chen.media/guides/164-claude-skills-in-one-repo-which-to-take-first)
  ↳ *qualifies* `g17-0233`

- `g17-0270` *STATED* — Open Generative AI has no subscription because you supply the API key.
  > “There is no subscription, because you supply the key.”
  — [g-400-ai-image-and-video-models-in-one-free-desktop-app](https://chen.media/guides/400-ai-image-and-video-models-in-one-free-desktop-app)
  ↳ *qualifies* `g17-0268`
  ↳ *example-of* `g17-0313`
  ↳ *evidence-for* `g18-0126`

- `g18-0005` *STATED* — The ECC project itself names Claude Code, Codex, Opencode and Cursor as the tools it runs inside.
  — [g-67-agents-281-skills-and-94-commands-in-one-install](https://chen.media/guides/67-agents-281-skills-and-94-commands-in-one-install)
  ↳ *qualifies* `g18-0001`
  ↳ *evidence-for* `g14-0223`
  ↳ *evidence-for* `g15-0184`

- `g18-0028` *STATED* — Four of the fifteen tools are marked KEEP, because the paid tool genuinely wins and swapping would cost more in time than it saves in money.
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *qualifies* `g18-0024`
  ↳ *because* `g18-0029`
  ↳ *evidence-for* `g18-0126`

- `g18-0043` *STATED* — Self-host PostHog and there is no event cap at all.
  > “Self host it and there is no event cap at all”
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *qualifies* `g18-0042`

- `g18-0087` *STATED* — The `npx skills` CLI auto-detects whichever agent you have installed.
  — [g-five-animation-skills-for-claude-code-with-install-commands](https://chen.media/guides/five-animation-skills-for-claude-code-with-install-commands)
  ↳ *part-of* `g18-0086`

- `g18-0099` *CORE* — One command installs Anthropic's own skill library into Claude Code.
  — [g-one-command-installs-anthropic-s-own-skill-library](https://chen.media/guides/one-command-installs-anthropic-s-own-skill-library)
  ↳ *defines* `g18-0165` — same official Anthropic skill library

- `g18-0110` *STATED* — Out of the box Claude cannot search the live web, open a page and click through it, read a site it was not handed, or check the current docs for a library.
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again)
  ↳ *contrast* `g18-0109`
  ↳ *evidence-for* `g16-0014`

- `g18-0115` *STATED* — Most search tools hand back ten links and leave the model to fetch each one.
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again)
  ↳ *contrast* `g18-0114`

- `g18-0125` *STATED* — Every paid tool in Alex's list of 25 has a free alternative that does the same job for most people: the 15 from his post first, then 10 that did not fit.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *example-of* `g18-0287`

- `g18-0155` *STATED* — Claude Code plugin installs are a two-step process, and nearly every 'it did not work' is one of those two steps missing.
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *part-of* `g18-0154`

- `g18-0158` *STATED* — Anthropic's own marketplace, claude-plugins-official, is added automatically when Claude Code starts, so its plugins (such as code-review) need only the install line.
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *qualifies* `g18-0155`
  ↳ *qualifies* `g18-0160`
  ↳ *contrast* `g18-0159`

- `g18-0159` *STATED* — The other four of Alex's five plugins live in other catalogs, so each needs both the marketplace-add line and the install line.
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *qualifies* `g18-0155`

- `g18-0171` *STATED* — code-review has two sibling plugins in the same marketplace.
  > “Two siblings in the same marketplace”
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *part-of* `g18-0158`

- `g18-0194` *STATED* — G0DM0D3 runs entirely client side, keeping chat history in the browser's localStorage, so nothing is stored on somebody else's server.
  — [g-one-html-file-that-runs-chatgpt-claude-gemini-and-grok-side-by-side](https://chen.media/guides/one-html-file-that-runs-chatgpt-claude-gemini-and-grok-side-by-side)
  ↳ *part-of* `g18-0191`
  ↳ *example-of* `g02-0240`

- `g18-0198` *STATED* — Five subscriptions you probably pay for have full open source replacements: not free tiers with the good parts removed, but the whole application on your machine with the source in the open.
  — [g-five-paid-apps-with-full-open-source-replacements](https://chen.media/guides/five-paid-apps-with-full-open-source-replacements)
  ↳ *contrast* `g18-0126` — full open source app vs free tier
  ↳ *example-of* `g18-0287`

- `g19-0094` *STATED* — The Google AI Studio API key is free to start and is what lets Gemini run inside the /route setup.
  > “This is free to start and is what lets Gemini run.”
  — [g-run-gemini-inside-claude-code-with-claude-as-the-boss](https://chen.media/guides/run-gemini-inside-claude-code-with-claude-as-the-boss)
  ↳ *qualifies* `g19-0093`
  ↳ *evidence-for* `g16-0224`

- `g19-0110` *STATED* — All five 'hands' repos (ComfyUI, Duix-Avatar, Presenton, whisper.cpp, Activepieces) are free and open source.
  > “Five free, open-source repos”
  — [g-five-free-repos-that-give-claude-actual-hands](https://chen.media/guides/five-free-repos-that-give-claude-actual-hands)
  ↳ *part-of* `g19-0101`
  ↳ *generalizes* `g19-0103`

- `g19-0137` *STATED* — Langfuse turns a black-box AI agent into a full x-ray: every call, every cost, every step, on one screen.
  > “Turn your black-box AI agent into a full x-ray: every call, every cost, every step, on one screen.”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *part-of* `g19-0136`

- `g19-0138` *STATED* — Langfuse is free and open source.
  > “Free and open source.”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *part-of* `g19-0136`

- `g19-0139` *STATED* — Your agent is a black box; Langfuse makes it glass.
  > “Your agent is a black box. This makes it glass.”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *analogy-for* `g19-0137`

- `g19-0152` *STATED* — In Langfuse the top-level @observe() run, e.g. def agent(task), becomes one trace.
  > “@observe() # the top-level run = one trace”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *part-of* `g19-0151`

- `g19-0153` *STATED* — With @observe() applied, every nested call such as plan(task) or read_file('app.py') shows up as its own span inside the trace.
  > “# every nested call now shows up as its own span”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *part-of* `g19-0152`

- `g19-0162` *STATED* — Install Repomix second because it changes how every later prompt behaves.
  > “Then Repomix, because it changes how every later prompt behaves.”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *part-of* `g19-0160`

- `g19-0181` *STATED* — Serena plugs language servers, the same tech your IDE uses, into your coding agent.
  > “It plugs language servers, the same tech your IDE uses, into your coding agent.”
  — [g-give-claude-code-an-ide-brain-so-it-stops-reading-everything](https://chen.media/guides/give-claude-code-an-ide-brain-so-it-stops-reading-everything)
  ↳ *defines* `g19-0178`

- `g20-0024` *STATED* — After the Day 1 setup Claude can search your Obsidian vault, pull up what was actually said in your meetings, read the emails you have sent, and write back in your voice instead of generic assistant voice.
  > “this is the part almost everyone skips”
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *part-of* `g20-0023`
  ↳ *depends-on* `g20-0025`

- `g20-0036` *STATED* — The Obsidian step runs a small server on your own machine at an address like 127.0.0.1; Anthropic's servers cannot reach your machine, so a browser tab can never connect to your vault.
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *because* `g20-0035`
  ↳ *because* `g20-0038`

- `g20-0038` *STATED* — Anthropic states that a custom connector 'must be reachable over the public internet from Anthropic's IP ranges' and that servers behind a firewall 'won't connect, even if you can reach them from your own machine.'
  > “must be reachable over the public internet from Anthropic's IP ranges”
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *evidence-for* `g20-0037`
  ↳ *qualifies* `g22-0161`

- `g20-0041` *STATED* — Three of the four Day 1 steps are pure clicking; only the Obsidian step asks more of you.
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *part-of* `g20-0034`
  ↳ *leads-to* `g20-0042`

- `g20-0226` *STATED* — Out of the box, Claude stalls the second it needs a tool it does not have.
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *evidence-for* `g20-0224`
  ↳ *leads-to* `g20-0255`
  ↳ *evidence-for* `g16-0014`

- `g20-0257` *STATED* — Each of the five free MCPs is added with a single line; a couple of them need a free API key.
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *part-of* `g20-0255`
  ↳ *generalizes* `g20-0260`

- `g20-0258` *STATED* — With the five MCPs installed, 'search it, scrape it, structure it, build it, ship it' becomes one sentence.
  > “search it, scrape it, structure it, build it, ship it”
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *part-of* `g20-0255`
  ↳ *depends-on* `g20-0256`

- `g20-0277` *STATED* — Context7 needs no API key: it is free with no key needed.
  > “Key: none. Free, no key needed”
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *qualifies* `g20-0275`
  ↳ *part-of* `g18-0123`

- `g21-0002` *STATED* — Alex claims five specific Claude Code skills make Claude Code about 10x more powerful.
  > “5 Claude Code skills that make it about 10x more powerful”
  — [g-five-claude-code-skills-with-the-install-command-for-each](https://chen.media/guides/five-claude-code-skills-with-the-install-command-for-each)
  ↳ *part-of* `g21-0001`
  ↳ *qualifies* `g21-0005`

- `g21-0004` *STATED* — Each of Alex's five must-have skills bolts one real capability onto Claude Code: design, planning, security, restraint, and self-testing.
  — [g-five-claude-code-skills-with-the-install-command-for-each](https://chen.media/guides/five-claude-code-skills-with-the-install-command-for-each)
  ↳ *part-of* `g21-0001`
  ↳ *leads-to* `g21-0005`

- `g22-0150` *STATED* — The official Meta Ads connector means no third-party app and no ban risk, because Meta built it themselves.
  — [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)
  ↳ *qualifies* `g22-0149`

- `g22-0152` *STATED* — Everything Claude changes through the Meta Ads connector is created PAUSED by default, so nothing spends a cent until you approve it.
  > “Everything Claude changes is created PAUSED by default, so nothing spends a cent until you approve it.”
  — [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)
  ↳ *qualifies* `g22-0151`
  ↳ *example-of* `g22-0278`
  ↳ *example-of* `g12-0303`

- `g23-0066` *STATED* — Why n8n wins Automations in his tier list: n8n lets you self host it, branch it, and wire AI agents in without per task fees.
  — [g-the-2026-ai-tool-tier-list-with-the-reason-for-each-pick](https://chen.media/guides/the-2026-ai-tool-tier-list-with-the-reason-for-each-pick)
  ↳ *evidence-for* `g23-0205`

- `g23-0100` *STATED* — Alex Chen's five Claude skills worth installing today: stop-slop, ClaudeMem, UI-UX Pro Max, Task Observer, and Find Skills.
  — [g-five-claude-skills-that-beat-99-of-users](https://chen.media/guides/five-claude-skills-that-beat-99-of-users)
  ↳ *qualifies* `g23-0099`
  ↳ *contrast* `y04-0113`

- `g23-0101` *STATED* — Those five skills are the highest leverage ones to start with.
  — [g-five-claude-skills-that-beat-99-of-users](https://chen.media/guides/five-claude-skills-that-beat-99-of-users)
  ↳ *qualifies* `g23-0100`

- `g23-0103` *STATED* — A skill loads only when it is relevant: Claude loads the folder on demand.
  > “A skill is a folder Claude loads on demand”
  — [g-five-claude-skills-that-beat-99-of-users](https://chen.media/guides/five-claude-skills-that-beat-99-of-users)
  ↳ *qualifies* `g23-0102`
  ↳ *evidence-for* `g15-0045`

- `g23-0150` *STATED* — For each MCP plugin the cheat sheet gives what it does, the one line that installs it, and a starter prompt.
  — [g-the-claude-plugins-cheat-sheet-add-once-then-just-ask](https://chen.media/guides/the-claude-plugins-cheat-sheet-add-once-then-just-ask)
  ↳ *qualifies* `g23-0151`

- `g23-0151` *STATED* — His five MCP plugins to install once: Chrome DevTools, Firecrawl, Figma, Blender, and ElevenLabs.
  — [g-the-claude-plugins-cheat-sheet-add-once-then-just-ask](https://chen.media/guides/the-claude-plugins-cheat-sheet-add-once-then-just-ask)
  ↳ *example-of* `g23-0148`

- `g23-0188` *STATED* — There are six swaps worth making: tools that quietly do the same job as the hyped ones for less.
  — [g-six-hyped-ai-tools-and-what-quietly-does-the-same-job](https://chen.media/guides/six-hyped-ai-tools-and-what-quietly-does-the-same-job)
  ↳ *because* `g23-0187`

- `r01-0001` *CORE* — Every Alex Chen skill repo (/agency, /court, /hiring-panel, /shark, /night-crew, /launch, /learn) is free, MIT-licensed, needs no signup and no API key.
  > “Free, MIT, no signup, no API key.”
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill) [r-alexyc9381](https://github.com/alexyc9381/alexyc9381) [r-court-skill](https://github.com/alexyc9381/court-skill) [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *example-of* `g18-0288`
  ↳ *evidence-for* `g06-0262`

- `r01-0054` *STATED* — Everything /agency produces lives in .agency/ in the folder you run it in.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *example-of* `r01-0014`

- `r01-0158` *STATED* — /court is one Claude Code skill with nothing to connect (no MCP, no API key).
  > “nothing to connect”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *qualifies* `r01-0157`
  ↳ *example-of* `r01-0001`

- `r01-0171` *STATED* — /court never touches your files: everything is written inside .court/ in the folder you run it in.
  > “It never touches your files.”
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0014`

- `r03-0023` *STATED* — Installed as a plugin, the learn skill shows up namespaced as '/learn-skill:learn' instead of '/learn'.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *qualifies* `r03-0022`
  ↳ *qualifies* `r01-0004`

- `r03-0040` *STATED* — When /learn is installed as a plugin, the headless nightly prompt is "/learn-skill:learn review" instead of "/learn review".
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *qualifies* `r03-0038`
  ↳ *depends-on* `r03-0023`

- `r03-0044` *STATED* — skills/learn/learn.py does all the /learn bookkeeping using Python's standard library only.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0001`

- `r03-0063` *STATED* — The learn SKILL.md description triggers on 'learn', 'remember this', 'don't do that again', 'add that to the rules', 'you keep making this mistake', a request for a review of today's mistakes, or wanting Claude to stop repeating itself.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0001`

- `r03-0064` *STATED* — The learn SKILL.md frontmatter sets argument-hint: "[a lesson in your words | review | list | setup | nightly | status]".
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0072`

- `r03-0065` *STATED* — The learn SKILL.md frontmatter carries license: MIT and metadata author 'Alex Chen (@nocodealex)', homepage https://chen.media, source https://github.com/alexyc9381/learn-skill, version 1.0.0.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *part-of* `r03-0001`

- `r03-0146` *STATED* — /linkedin-roast also accepts pasted profile text or a screenshot instead of a PDF.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *qualifies* `r03-0145`

- `r03-0180` *STATED* — The linkedin-roast SKILL.md description triggers on '/linkedin-roast' followed by a profile (a PDF path, pasted text or a screenshot), or requests to 'roast my LinkedIn', 'review my LinkedIn profile' or 'fix my LinkedIn'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0134`

- `r04-0002` *CORE* — Alex Chen's mentor, night-crew and shark skills are each free, MIT-licensed, need no signup and no API key.
  > “Free, MIT, no signup, no API key.”
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill) [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill) [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *generalizes* `r04-0207`
  ↳ *qualifies* `r04-0023`
  ↳ *qualifies* `r04-0087`
  ↳ *qualifies* `r04-0206`
  ↳ *evidence-for* `r01-0001`

- `r04-0010` *CORE* — Alex's skills keep all their state in a dot-folder in the folder you run them in (.mentor/, .shark/) and never touch your other files.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill) [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *evidence-for* `r01-0014`

- `r04-0022` *STATED* — The /mentor plugin's tagline: 'Claude writes the code. You make the calls.'
  > “Claude writes the code. You make the calls.”
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *defines* `r04-0023`

- `r04-0036` *STATED* — Everything you decided and learned in a /mentor session goes into .mentor/RECAP.md.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)

- `r04-0037` *STATED* — /mentor never touches anything outside your project: its notes live in .mentor/ in the folder you run it in.
  > “It never touches anything outside your project.”
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *example-of* `r04-0010`
  ↳ *qualifies* `r04-0023`

- `r04-0049` *STATED* — Python 3 is the only requirement of the /mentor plugin.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *enables* `r04-0011`
  ↳ *qualifies* `r04-0023`

- `r04-0052` *STATED* — /mentor is a separate build from VibeWise with its own take: a hard lock on code until you've answered, and an explain-back at the end of every feature.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *contrast* `r04-0051`
  ↳ *depends-on* `r04-0033`
  ↳ *depends-on* `r04-0035`
  ↳ *contrast* `g05-0002`

- `r04-0207` *STATED* — /shark has nothing to connect, on top of being free, MIT, no signup, no API key.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r01-0001`

- `r04-0216` *STATED* — /shark never touches your files: everything is written inside .shark/ in the folder you run it in.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0010`
  ↳ *qualifies* `r04-0206`

- `r04-0245` *STATED* — /shark state lives in .shark/<run>/state.json in the current directory, and every command after init finds it through .shark/LATEST.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0010`
  ↳ *depends-on* `r04-0254`

- `y01-0064` *STATED* — A preference like 'use plain English' doesn't describe all the steps needed to make a weekly report - that's when you use a skill.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *example-of* `y01-0070`
  ↳ *leads-to* `y01-0065`

- `y01-0098` *STATED* — If you connect Claude to apps like Canva or Adobe, the agency can also make visuals for the marketing.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *depends-on* `y01-0174`
  ↳ *qualifies* `y01-0095`
  ↳ *example-of* `y01-0168`

- `y01-0128` *STATED* — Alex says you do all of the agency work inside Claude 'for completely free'.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *qualifies* `y01-0079`

- `y01-0173` *STATED* — The Drive connector reads the live files directly from your Google Workspace, so you get answers without opening another tab.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *qualifies* `y01-0172`

- `y01-0174` *STATED* — There are hundreds of other Claude connectors across marketing, finance and more.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *qualifies* `y01-0168`

- `y01-0180` *CORE* — Tell the AI once, save it as a skill, and it follows those instructions every single time.
  > “all you need to do is just tell AI once, save it as a skill, and it follows those instructions as the skill every single time.”
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *qualifies* `y01-0176`

- `y01-0185` *STATED* — With Alex's fal skill, every video you create is saved on your own computer.
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *example-of* `y03-0208`
  ↳ *part-of* `y01-0184`

- `y01-0187` *STATED* — You can use Seedance 2.5 and Nano Banana directly without paying Higgsfield's $100-a-month fee.
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *depends-on* `y01-0186`

- `y01-0189` *STATED* — Alex: spending the same $100 a month directly at the source models generates hundreds of videos, much cheaper.
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *qualifies* `y01-0187`

- `y01-0192` *STATED* — Through fal.ai you get Seedance 2.5 and Nano Banana inside Claude just as on Higgsfield, without the markups and with full access to your videos.
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *part-of* `y01-0191`

- `y02-0031` *STATED* — Claude Motion doesn't use any video model — it animates everything with code.
  > “it doesn't use any video model and it animates everything with code”
  — [HWioULsQJWM](https://youtu.be/HWioULsQJWM)
  ↳ *evidence-for* `g05-0318`
  ↳ *part-of* `y02-0029`
  ↳ *enables* `y02-0032` — code-driven animation

- `y02-0032` *STATED* — With /motion you can make in minutes, with zero experience, videos that would take an After Effects expert hours.
  — [HWioULsQJWM](https://youtu.be/HWioULsQJWM)
  ↳ *part-of* `y02-0029`

- `y02-0036` *STATED* — The Agency plugs straight into Claude Code.
  — [SChgKT-vXHk](https://youtu.be/SChgKT-vXHk) [GaXO0ZKN4WI](https://youtu.be/GaXO0ZKN4WI) [Di7KzYJ7NwA](https://youtu.be/Di7KzYJ7NwA)
  ↳ *evidence-for* `g08-0089`
  ↳ *part-of* `y02-0033`

- `y02-0048` *STATED* — Agent Office gives each Claude its own desk and its own screen, so you can run multiple Claudes at once and watch what each one is typing.
  — [qPP2IR9Dw3E](https://youtu.be/qPP2IR9Dw3E)
  ↳ *part-of* `y02-0047`

- `y02-0049` *STATED* — In Agent Office, when one Claude needs you to reply, a red light turns on over its desk.
  — [qPP2IR9Dw3E](https://youtu.be/qPP2IR9Dw3E)
  ↳ *part-of* `y02-0047`
  ↳ *qualifies* `y02-0051` — the alert prevents the wasted hour

- `y02-0050` *STATED* — Agent Office can also sound an alarm and show a banner on your screen telling you which Claude chat needs you.
  — [qPP2IR9Dw3E](https://youtu.be/qPP2IR9Dw3E)
  ↳ *part-of* `y02-0047`
  ↳ *qualifies* `y02-0051`

- `y02-0052` *STATED* — You can replace Photoshop, Premiere, After Effects and more with free apps and never pay Adobe again (CTA keyword 'Adobe').
  > “You can replace Photoshop, Premiere, After Effects, and more with free apps and never pay Adobe again.”
  — [lhx8M2JPLPE](https://youtu.be/lhx8M2JPLPE)
  ↳ *evidence-for* `g08-0049`

- `y02-0054` *STATED* — Each Adobe app now has an 'official open-source copy' you can try right now.
  > “each one now has an official open-source copy”
  — [lhx8M2JPLPE](https://youtu.be/lhx8M2JPLPE)
  ↳ *contradicts* `g08-0056` — Craft apps: 'official open-source copy' of each Adobe app (video) vs 'not made or approved by Adobe' (guide)
  ↳ *part-of* `y02-0052`
  ↳ *because* `y02-0052`

- `y02-0144` *STATED* — Cuckoo shows every file Claude reads, edits and runs, live.
  — [4iwKLOxgvZQ](https://youtu.be/4iwKLOxgvZQ) [DIJprXkxmIs](https://youtu.be/DIJprXkxmIs)
  ↳ *evidence-for* `g09-0234`
  ↳ *part-of* `y02-0142`

- `y02-0145` *STATED* — Cuckoo watches Claude, Cursor, Codex and Gemini at the exact same time.
  — [4iwKLOxgvZQ](https://youtu.be/4iwKLOxgvZQ) [DIJprXkxmIs](https://youtu.be/DIJprXkxmIs)
  ↳ *evidence-for* `g09-0236`
  ↳ *part-of* `y02-0142`

- `y02-0146` *STATED* — When Claude asks you a question, you can just say yes right from the Mac notch with Cuckoo.
  — [4iwKLOxgvZQ](https://youtu.be/4iwKLOxgvZQ) [DIJprXkxmIs](https://youtu.be/DIJprXkxmIs)
  ↳ *evidence-for* `g06-0114`
  ↳ *part-of* `y02-0142`

- `y02-0155` *STATED* — MiroFish runs on Claude.
  — [tQRaHRjRROk](https://youtu.be/tQRaHRjRROk) [fYrca_-P1NI](https://youtu.be/fYrca_-P1NI)
  ↳ *evidence-for* `g09-0201`
  ↳ *part-of* `g09-0195`
  ↳ *part-of* `y02-0148`

- `y02-0178` *STATED* — The Logo Design Skill also hands over a color palette and app icons.
  — [J8g3EZwZx20](https://youtu.be/J8g3EZwZx20)
  ↳ *evidence-for* `g09-0188`
  ↳ *part-of* `y02-0172`

- `y03-0103` *STATED* — Find Skills downloads the skills it picks and puts them straight into your setup so Claude uses them right away.
  — [wfwnTNtnomk](https://youtu.be/wfwnTNtnomk) [1j9mmXDW8Qw](https://youtu.be/1j9mmXDW8Qw)
  ↳ *evidence-for* `g10-0264`
  ↳ *part-of* `y03-0100`
  ↳ *leads-to* `y03-0105`
  ↳ *qualifies* `y03-0107`

- `y03-0105` *STATED* — With Find Skills you stop hunting for skills yourself and Claude always grabs the right one.
  — [wfwnTNtnomk](https://youtu.be/wfwnTNtnomk) [1j9mmXDW8Qw](https://youtu.be/1j9mmXDW8Qw)

- `y03-0111` *STATED* — Open Design runs on top-tier free AI models like DeepSeek.
  — [NrJa3MCde-I](https://youtu.be/NrJa3MCde-I) [vdLceKphMoQ](https://youtu.be/vdLceKphMoQ)
  ↳ *evidence-for* `g10-0202`
  ↳ *part-of* `y03-0110`
  ↳ *qualifies* `y03-0108` — free models do not touch the Claude limit

- `y03-0115` *STATED* — Open Design also turns your idea into an animated video ready to post.
  — [NrJa3MCde-I](https://youtu.be/NrJa3MCde-I) [vdLceKphMoQ](https://youtu.be/vdLceKphMoQ)
  ↳ *evidence-for* `g10-0220`
  ↳ *part-of* `g10-0198`
  ↳ *part-of* `y03-0110`

- `y03-0119` *STATED* — Dyad doesn't stop at the basic screens any AI can build: it even sets up your app's database and user logins.
  — [cxLfDm8_Yx4](https://youtu.be/cxLfDm8_Yx4) [a8nVKYxwcjo](https://youtu.be/a8nVKYxwcjo) [udcHbDvy7o4](https://youtu.be/udcHbDvy7o4)
  ↳ *evidence-for* `g10-0243`
  ↳ *qualifies* `y03-0118`

- `y03-0120` *STATED* — With Dyad you can build as many apps as you want with no credits running out.
  — [cxLfDm8_Yx4](https://youtu.be/cxLfDm8_Yx4) [a8nVKYxwcjo](https://youtu.be/a8nVKYxwcjo) [udcHbDvy7o4](https://youtu.be/udcHbDvy7o4)
  ↳ *evidence-for* `g10-0224`
  ↳ *part-of* `g10-0223`
  ↳ *part-of* `y03-0116`

- `y03-0125` *STATED* — Instatic doesn't just spit out code: it builds real buttons, text and pictures you can drag around.
  — [N8BCMjq3wPE](https://youtu.be/N8BCMjq3wPE) [23JOjnkdikY](https://youtu.be/23JOjnkdikY)
  ↳ *evidence-for* `g11-0023`
  ↳ *part-of* `g11-0011`
  ↳ *qualifies* `y03-0124`

- `y03-0131` *STATED* — FluidVoice types into any app on your Mac, from email to Slack.
  — [OtRSHXUQxAQ](https://youtu.be/OtRSHXUQxAQ) [4xBCskEhIfE](https://youtu.be/4xBCskEhIfE)
  ↳ *evidence-for* `g11-0193`
  ↳ *part-of* `g11-0181`
  ↳ *part-of* `y03-0128`

- `y03-0132` *STATED* — FluidVoice even works with no internet because everything runs right on your Mac locally.
  — [OtRSHXUQxAQ](https://youtu.be/OtRSHXUQxAQ) [4xBCskEhIfE](https://youtu.be/4xBCskEhIfE)
  ↳ *evidence-for* `g11-0182`
  ↳ *part-of* `y03-0128`
  ↳ *enables* `y03-0133`

- `y03-0135` *STATED* — Photon Studio lets you edit photos, retouch images and create designs right on your computer.
  — [WB8w3FTYCnw](https://youtu.be/WB8w3FTYCnw) [kasTR80Lvjo](https://youtu.be/kasTR80Lvjo)
  ↳ *part-of* `g10-0152`
  ↳ *part-of* `y03-0134`

- `y03-0136` *STATED* — Photon Studio works without uploading your files to the cloud.
  — [WB8w3FTYCnw](https://youtu.be/WB8w3FTYCnw) [kasTR80Lvjo](https://youtu.be/kasTR80Lvjo)
  ↳ *evidence-for* `g10-0164`
  ↳ *part-of* `y03-0134`
  ↳ *leads-to* `y03-0140`

- `y03-0137` *STATED* — Photon Studio needs no account to start editing.
  — [WB8w3FTYCnw](https://youtu.be/WB8w3FTYCnw) [kasTR80Lvjo](https://youtu.be/kasTR80Lvjo)
  ↳ *evidence-for* `g10-0164`
  ↳ *part-of* `y03-0134`

- `y03-0138` *STATED* — Photon Studio comes with the Photoshop tools you'll recognize, like layers, groups and masks.
  — [WB8w3FTYCnw](https://youtu.be/WB8w3FTYCnw) [kasTR80Lvjo](https://youtu.be/kasTR80Lvjo)
  ↳ *evidence-for* `g10-0165`
  ↳ *part-of* `y03-0134`

- `y03-0139` *STATED* — In Photon Studio even subject selection and background removal run on your own computer.
  — [WB8w3FTYCnw](https://youtu.be/WB8w3FTYCnw) [kasTR80Lvjo](https://youtu.be/kasTR80Lvjo)
  ↳ *evidence-for* `g10-0172`
  ↳ *part-of* `y03-0134`
  ↳ *leads-to* `y03-0140`

- `y03-0140` *STATED* — Because Photon Studio runs locally, you own your files 100%.
  — [WB8w3FTYCnw](https://youtu.be/WB8w3FTYCnw) [kasTR80Lvjo](https://youtu.be/kasTR80Lvjo)
  ↳ *example-of* `y03-0208`

- `y03-0141` *STATED* — Photon Studio is available for macOS and Windows.
  — [WB8w3FTYCnw](https://youtu.be/WB8w3FTYCnw) [kasTR80Lvjo](https://youtu.be/kasTR80Lvjo)
  ↳ *part-of* `g10-0152`
  ↳ *part-of* `y03-0134`

- `y03-0151` *STATED* — SupoClip crops every clip to vertical.
  — [fm0bvQE5IW8](https://youtu.be/fm0bvQE5IW8)
  ↳ *part-of* `g12-0187`
  ↳ *part-of* `y03-0144`

- `y03-0152` *STATED* — SupoClip follows the speaker's face when it crops.
  — [fm0bvQE5IW8](https://youtu.be/fm0bvQE5IW8)
  ↳ *part-of* `g12-0187`
  ↳ *qualifies* `y03-0151`

- `y03-0153` *STATED* — SupoClip adds captions that line up word by word.
  — [fm0bvQE5IW8](https://youtu.be/fm0bvQE5IW8)
  ↳ *part-of* `g12-0187`
  ↳ *part-of* `y03-0144`

- `y03-0195` *STATED* — Alex says the NVIDIA key works like the Claude API, so one key runs every model and plugs straight into the coding tools you already use.
  > “It works just like the Claude API, so one key runs every model and it plugs straight into all of the coding tools you already use.”
  — [0KN0eTZcoqI](https://youtu.be/0KN0eTZcoqI)
  ↳ *contradicts* `g12-0292` — NVIDIA free key: 'works like the Claude API' (video) vs 'speaks the OpenAI-style API' (guide)
  ↳ *evidence-for* `g12-0280`
  ↳ *enables* `y03-0192`

- `y04-0007` *STATED* — Bot Crossing requires no account creation.
  > “You don't need to create an account”
  — [Hfgfyi4-xOI](https://youtu.be/Hfgfyi4-xOI)
  ↳ *evidence-for* `g13-0007`
  ↳ *qualifies* `y04-0001`

- `y04-0008` *STATED* — Bot Crossing only reads what's already on your computer (your local Claude Code session data).
  > “it only reads what's already on your computer”
  — [Hfgfyi4-xOI](https://youtu.be/Hfgfyi4-xOI)
  ↳ *evidence-for* `g13-0007`
  ↳ *qualifies* `y04-0001`

- `y04-0013` *STATED* — claude-mem includes a Claude Desktop skill (transcribed as 'cloud desktop scale'), extending the memory beyond Claude Code.
  > “It has a Claude Desktop skill”
  — [55RbHPThR8g](https://youtu.be/55RbHPThR8g) [EVTO2eM2DlQ](https://youtu.be/EVTO2eM2DlQ) [6zrQsxiYz1E](https://youtu.be/6zrQsxiYz1E)
  ↳ *part-of* `g13-0136`
  ↳ *part-of* `y04-0010`

- `y04-0014` *STATED* — claude-mem has a privacy control feature.
  > “privacy control”
  — [55RbHPThR8g](https://youtu.be/55RbHPThR8g) [EVTO2eM2DlQ](https://youtu.be/EVTO2eM2DlQ) [6zrQsxiYz1E](https://youtu.be/6zrQsxiYz1E)
  ↳ *evidence-for* `g13-0144`
  ↳ *part-of* `y04-0010`

- `y04-0015` *STATED* — claude-mem has a context configuration feature.
  > “context configuration”
  — [55RbHPThR8g](https://youtu.be/55RbHPThR8g) [EVTO2eM2DlQ](https://youtu.be/EVTO2eM2DlQ) [6zrQsxiYz1E](https://youtu.be/6zrQsxiYz1E)
  ↳ *part-of* `g13-0136`
  ↳ *part-of* `y04-0010`

- `y04-0016` *STATED* — claude-mem has automatic operation: memory capture runs on its own without manual commands.
  > “and even automatic operation”
  — [55RbHPThR8g](https://youtu.be/55RbHPThR8g) [EVTO2eM2DlQ](https://youtu.be/EVTO2eM2DlQ) [6zrQsxiYz1E](https://youtu.be/6zrQsxiYz1E)
  ↳ *evidence-for* `g13-0145`
  ↳ *part-of* `y04-0010`

- `y04-0026` *STATED* — /watch works with YouTube, Loom, TikTok, Instagram and many more video sources.
  > “YouTube, Loom, TikTok, Instagram, and many more”
  — [dXOq_pNqeFA](https://youtu.be/dXOq_pNqeFA) [bmUJ_ifeXIE](https://youtu.be/bmUJ_ifeXIE) [9DM6ZdHEWls](https://youtu.be/9DM6ZdHEWls)
  ↳ *evidence-for* `g13-0127`
  ↳ *qualifies* `y04-0025`

- `y04-0028` *STATED* — /watch breaks a video down frame by frame and extracts the audio, so Claude understands literally every aspect of it.
  > “It'll break down the video frame by frame and extract the audio so it understands literally every aspect.”
  — [dXOq_pNqeFA](https://youtu.be/dXOq_pNqeFA) [bmUJ_ifeXIE](https://youtu.be/bmUJ_ifeXIE) [9DM6ZdHEWls](https://youtu.be/9DM6ZdHEWls)
  ↳ *evidence-for* `g13-0124`
  ↳ *part-of* `y04-0025`
  ↳ *enables* `y04-0029`

- `y04-0082` *STATED* — The free-API list covers email, entertainment, healthcare, crypto, weather, news, finance and a lot more.
  > “There's email, entertainment, healthcare, crypto, weather, news, finance, and a lot more.”
  — [-U14AktLSiM](https://youtu.be/-U14AktLSiM)
  ↳ *evidence-for* `g13-0157`
  ↳ *qualifies* `y04-0080`

- `y04-0093` *STATED* — The single file puts ChatGPT, Claude, Gemini, Grok and 50 other AI tools in one place.
  > “you get access to ChatGPT, Claude, Gemini, Grok, and 50 other AI tools in one place”
  — [OD7UTDYiTYI](https://youtu.be/OD7UTDYiTYI) [voaf6bOrHgc](https://youtu.be/voaf6bOrHgc)
  ↳ *contradicts* `g18-0193` — Single-file AI hub reach: 'ChatGPT, Claude, Gemini, Grok and 50 other AI tools' vs G0DM0D3 'more than 60 models'
  ↳ *part-of* `y04-0091`

- `y04-0094` *STATED* — The single-file AI hub needs no login, no subscription and no cloud.
  > “No login, no subscription, no cloud.”
  — [OD7UTDYiTYI](https://youtu.be/OD7UTDYiTYI) [voaf6bOrHgc](https://youtu.be/voaf6bOrHgc)
  ↳ *contradicts* `g18-0195` — Single-file AI hub: 'no login, no subscription and no cloud' vs G0DM0D3 'not fully offline: model calls still go out to the provider'
  ↳ *qualifies* `y04-0091`

### concept

- `g01-0196` *INFERRED* — Recurring local-first criterion: Alex favours tools that run on your own machine with no backend or telemetry, keeping files and data local.
  — [g-the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops](https://chen.media/guides/the-open-source-claude-job-hunter-behind-a-head-of-ai-offer-set-up-career-ops) [g-pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud](https://chen.media/guides/pan-740-job-posts-down-to-your-shortlist-set-up-career-ops-the-open-source-claud) [g-score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s](https://chen.media/guides/score-one-job-post-against-your-cv-before-you-apply-set-up-career-ops-the-open-s) [g-740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j](https://chen.media/guides/740-job-posts-68-applications-1-offer-set-up-career-ops-the-open-source-claude-j) [g-stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t](https://chen.media/guides/stop-applying-to-every-job-set-up-career-ops-the-open-source-claude-job-hunter-t) [g-give-claude-a-map-and-a-memory-of-your-whole-project](https://chen.media/guides/give-claude-a-map-and-a-memory-of-your-whole-project) [g-reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style) [g-let-claude-tailor-your-resume-to-every-job-without-inventing-anything](https://chen.media/guides/let-claude-tailor-your-resume-to-every-job-without-inventing-anything) [g-find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free](https://chen.media/guides/find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free) [g-make-khan-academy-style-videos-with-claude](https://chen.media/guides/make-khan-academy-style-videos-with-claude)
  ↳ *evidence-for* `g02-0240`

- `g03-0012` *INFERRED* — Privacy is a selling point in the open-source tools he features: career-ops has no telemetry and no backend, and Minutes keeps audio and transcripts on your machine.
  — [g-career-ops-let-claude-score-every-job-against-your-cv-before-you-apply](https://chen.media/guides/career-ops-let-claude-score-every-job-against-your-cv-before-you-apply) [g-minutes-the-free-open-source-meeting-recorder-that-claude-can-search](https://chen.media/guides/minutes-the-free-open-source-meeting-recorder-that-claude-can-search)
  ↳ *evidence-for* `g02-0240`

- `g03-0041` *STATED* — SkillSpector's attack categories include prompt injection and hidden instructions inside skill files.
  — [g-skillspector-scan-any-claude-skill-for-malware-before-you-install-it](https://chen.media/guides/skillspector-scan-any-claude-skill-for-malware-before-you-install-it)
  ↳ *part-of* `g03-0040`

- `g03-0042` *STATED* — SkillSpector's attack categories include data exfiltration, stealing environment variables (API keys) and privilege escalation.
  — [g-skillspector-scan-any-claude-skill-for-malware-before-you-install-it](https://chen.media/guides/skillspector-scan-any-claude-skill-for-malware-before-you-install-it)
  ↳ *part-of* `g03-0040`

- `g03-0043` *STATED* — SkillSpector's attack categories include supply-chain risks and MCP tool poisoning.
  — [g-skillspector-scan-any-claude-skill-for-malware-before-you-install-it](https://chen.media/guides/skillspector-scan-any-claude-skill-for-malware-before-you-install-it)
  ↳ *part-of* `g03-0040`
  ↳ *qualifies* `g03-0146` — MCP servers you add are a tool-poisoning surface
  ↳ *qualifies* `g16-0014`

- `g03-0107` *CORE* — Claude Code skills/plugins like Caveman can be installed three ways: claude plugin CLI commands, npx skills add <repo> -g for the skill alone, or /plugin slash commands inside a session.
  — [g-make-claude-answer-in-fewer-words-with-the-caveman-skill](https://chen.media/guides/make-claude-answer-in-fewer-words-with-the-caveman-skill)
  ↳ *enables* `g03-0100`

- `g03-0122` *STATED* — A code intelligence plugin is an official Claude Code plugin type that connects Claude to a language server so it can look up a function's definition by symbol in one step.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *part-of* `g03-0009`
  ↳ *contrast* `g03-0120`
  ↳ *example-of* `g02-0241`

- `g05-0231` *STATED* — The ASSET_DOWNLOAD_DIR environment variable tells the local 3D Asset Server where to save downloaded files.
  — [g-3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once](https://chen.media/guides/3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once)
  ↳ *part-of* `g05-0230`

- `g05-0311` *CORE* — Personal Claude skills live in ~/.claude/skills/ (project skills in .claude/skills); copying a skill folder there installs it without the plugin system.
  — [g-the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar](https://chen.media/guides/the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar) [g-install-the-logo-design-skill](https://chen.media/guides/install-the-logo-design-skill) [g-claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix](https://chen.media/guides/claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix)

- `g05-0318` *CORE* — Claude makes video by writing code (Remotion, code-drawn picture, music and sound) and capturing real screenshots, rather than calling image or video generators.
  — [g-15-motion-design-styles-claude-can-make-from-one-prompt](https://chen.media/guides/15-motion-design-styles-claude-can-make-from-one-prompt) [g-mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer](https://chen.media/guides/mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer) [g-make-a-full-promo-video-with-claude-from-one-sentence](https://chen.media/guides/make-a-full-promo-video-with-claude-from-one-sentence)

- `g13-0002` *STATED* — In Bot Crossing, each Claude Code session walks out of a landing ship, claims a plot for its project and starts building.
  — [g-watch-every-claude-code-session-as-a-bot-in-bot-crossing](https://chen.media/guides/watch-every-claude-code-session-as-a-bot-in-bot-crossing)
  ↳ *part-of* `g13-0001`

- `g13-0005` *STATED* — Bot Crossing maps one bot per session and one hex plot per project folder.
  — [g-watch-every-claude-code-session-as-a-bot-in-bot-crossing](https://chen.media/guides/watch-every-claude-code-session-as-a-bot-in-bot-crossing)
  ↳ *part-of* `g13-0001`

- `g13-0006` *STATED* — In Bot Crossing, bigger conversations grow bigger buildings, so building size reflects how long a session's conversation is.
  — [g-watch-every-claude-code-session-as-a-bot-in-bot-crossing](https://chen.media/guides/watch-every-claude-code-session-as-a-bot-in-bot-crossing)
  ↳ *part-of* `g13-0001`
  ↳ *part-of* `g13-0005` — visual mapping rules

- `g13-0010` *STATED* — Alex's Bot Crossing guide has a section 'What you're looking at' on reading the colony view.
  — [g-watch-every-claude-code-session-as-a-bot-in-bot-crossing](https://chen.media/guides/watch-every-claude-code-session-as-a-bot-in-bot-crossing)
  ↳ *part-of* `g13-0001`

- `g13-0148` *STATED* — Alex's claude-mem guide has a 'How it works' section on the capture, compress and inject cycle.
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *part-of* `g13-0139`

- `g14-0354` *INFERRED* — LM Studio and Ollama are the two local runtimes Alex's guides use for running open models (Qwen, Spark-X2.5-4B) on your own computer.
  — [g-run-qwen3-8-locally-with-lm-studio](https://chen.media/guides/run-qwen3-8-locally-with-lm-studio) [g-spark-x-local-ai-setup-guide](https://chen.media/guides/spark-x-local-ai-setup-guide)

- `g15-0068` *STATED* — DeepSeek Harness lets you replace the brain and keep the agent.
  — [g-four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute](https://chen.media/guides/four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute)
  ↳ *contrast* `g15-0070` — swap the model by design vs reroute when Claude runs out

- `g15-0146` *STATED* — A 'one tab route' is an aggregator platform that puts every premium AI model in one place instead of separate subscriptions.
  — [g-every-premium-ai-model-in-one-place-how-the-one-tab-route-actually-works](https://chen.media/guides/every-premium-ai-model-in-one-place-how-the-one-tab-route-actually-works)

- `g15-0189` *INFERRED* — Because Claude switches skills and agents on from their descriptions, the description is the routing surface, which is why The Agency guide says routing decides whether it is useful.
  — [g-linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes](https://chen.media/guides/linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes) [g-the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install](https://chen.media/guides/the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install)
  ↳ *qualifies* `g15-0120`
  ↳ *generalizes* `g17-0228`

- `g16-0008` *CORE* — A core theme across the batch: free, open-source (mostly MIT) tools and free tiers that remove a cost meter — free repos that cut Claude Code costs, free GitHub repos and free Google tools that replace subscriptions, free MIT skills (unlazy, Prompt Master), and a free preview model.
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you) [g-five-free-github-repos-that-replace-software-you-pay-for](https://chen.media/guides/five-free-github-repos-that-replace-software-you-pay-for) [g-five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for](https://chen.media/guides/five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for) [g-seven-free-claude-code-repos-that-fix-what-claude-gets-wrong](https://chen.media/guides/seven-free-claude-code-repos-that-fix-what-claude-gets-wrong) [g-the-free-skill-that-stops-claude-saying-done-when-it-is-not](https://chen.media/guides/the-free-skill-that-stops-claude-saying-done-when-it-is-not) [g-the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting](https://chen.media/guides/the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting) [g-the-anonymous-model-that-makes-claude-code-free-until-august-27](https://chen.media/guides/the-anonymous-model-that-makes-claude-code-free-until-august-27)

- `g16-0014` *CORE* — MCP servers appear across three guides as the way Claude gets real-world reach: tip 15 says connecting MCP servers is what gives Claude hands, awesome-mcp-servers is the connectors directory, and prompt 7 wires up an MCP server.
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert) [g-five-free-github-repos-that-replace-software-you-pay-for](https://chen.media/guides/five-free-github-repos-that-replace-software-you-pay-for) [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)

- `g16-0287` *STATED* — These three plugins are different: each one removes a wall you hit whether you asked for it or not.
  > “each one removes a wall you hit whether you asked for it or not”
  — [g-three-plugins-that-fix-claude-code-s-setup-limits-and-memory](https://chen.media/guides/three-plugins-that-fix-claude-code-s-setup-limits-and-memory)

- `g16-0313` *STATED* — The seven repos have one thing in common.
  > “The thing they have in common”
  — [g-seven-free-claude-code-repos-that-fix-what-claude-gets-wrong](https://chen.media/guides/seven-free-claude-code-repos-that-fix-what-claude-gets-wrong)
  ↳ *qualifies* `g16-0309` — inferred: the shared trait is likely the step-proof process

- `g17-0005` *STATED* — Stage one of Alex Chen's marketing skill install order is 'what you produce': the skills that change your output are installed first.
  > “Stage one: what you produce”
  — [g-seven-free-claude-skills-that-cover-a-marketing-department](https://chen.media/guides/seven-free-claude-skills-that-cover-a-marketing-department)
  ↳ *part-of* `g17-0004`
  ↳ *leads-to* `g17-0006`

- `g17-0006` *STATED* — Stage two of Alex Chen's marketing skill install order is 'how you decide': the decision skills come after the production skills.
  > “Stage two: how you decide”
  — [g-seven-free-claude-skills-that-cover-a-marketing-department](https://chen.media/guides/seven-free-claude-skills-that-cover-a-marketing-department)
  ↳ *part-of* `g17-0004`
  ↳ *leads-to* `g17-0007`

- `g17-0007` *STATED* — Stage three of Alex Chen's marketing skill install order is 'what goes out the door': the two skills that take outbound action are installed last.
  > “Stage three: what goes out the door”
  — [g-seven-free-claude-skills-that-cover-a-marketing-department](https://chen.media/guides/seven-free-claude-skills-that-cover-a-marketing-department)
  ↳ *part-of* `g17-0004`

- `g17-0161` *STATED* — Project NOMAD's design point is that everything it knows is already on the disk.
  > “The point of the design is that everything it knows is already on the disk.”
  — [g-a-knowledge-server-that-keeps-answering-with-the-internet-off](https://chen.media/guides/a-knowledge-server-that-keeps-answering-with-the-internet-off)
  ↳ *enables* `g17-0155`

- `g17-0163` *STATED* — Alex Chen's NOMAD guide breaks down what is inside it and what actually powers each part.
  > “What is inside it, and what actually powers each part”
  — [g-a-knowledge-server-that-keeps-answering-with-the-internet-off](https://chen.media/guides/a-knowledge-server-that-keeps-answering-with-the-internet-off)
  ↳ *qualifies* `g17-0157`

- `g17-0233` *STATED* — Alex Chen's guide lists the ComposioHQ repo's 11 skill categories verbatim.
  > “The 11 categories, verbatim”
  — [g-164-claude-skills-in-one-repo-which-to-take-first](https://chen.media/guides/164-claude-skills-in-one-repo-which-to-take-first)
  ↳ *part-of* `g17-0223`

- `g17-0277` *STATED* — Open Generative AI organises its models into 14 studios, listed in the guide.
  > “The 14 studios”
  — [g-400-ai-image-and-video-models-in-one-free-desktop-app](https://chen.media/guides/400-ai-image-and-video-models-in-one-free-desktop-app)
  ↳ *qualifies* `g17-0269`
  ↳ *part-of* `g17-0268`

- `g18-0287` *CORE* — Free replacements for paid AI tools is a recurring Alex Chen guide format, always paired with a caveat on where the paid tool still wins.
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools) [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools) [g-five-paid-apps-with-full-open-source-replacements](https://chen.media/guides/five-paid-apps-with-full-open-source-replacements) [g-seven-free-repos-that-replace-paid-ai-tools](https://chen.media/guides/seven-free-repos-that-replace-paid-ai-tools) [g-the-open-source-ai-studio-that-replaces-a-video-subscription](https://chen.media/guides/the-open-source-ai-studio-that-replaces-a-video-subscription)
  ↳ *qualifies* `g18-0288`
  ↳ *evidence-for* `g16-0008`

- `g21-0017` *INFERRED* — The five-skills guide uses three distinct install mechanisms: npx skills add <owner/repo> for skills, /plugin marketplace add + /plugin install <name>@<marketplace> for plugins, and claude mcp add <name> <command> for MCP servers.
  — [g-five-claude-code-skills-with-the-install-command-for-each](https://chen.media/guides/five-claude-code-skills-with-the-install-command-for-each)
  ↳ *qualifies* `g21-0016`
  ↳ *generalizes* `g03-0107`

- `g22-0161` *INFERRED* — A Claude 'custom connector' is a remote MCP server added by URL; the Meta Ads connector is Meta's first-party MCP server.
  — [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)
  ↳ *generalizes* `g22-0153`
  ↳ *example-of* `g12-0164`

- `g23-0205` *INFERRED* — Cost structure is a recurring reason in his tool picks: n8n without per task fees, Bolt.new free tier and self-host, Leonardo's permanent free tier, Comet free, ChatGPT Agent bundled in the $20 plan.
  — [g-the-2026-ai-tool-tier-list-with-the-reason-for-each-pick](https://chen.media/guides/the-2026-ai-tool-tier-list-with-the-reason-for-each-pick) [g-six-hyped-ai-tools-and-what-quietly-does-the-same-job](https://chen.media/guides/six-hyped-ai-tools-and-what-quietly-does-the-same-job)
  ↳ *evidence-for* `g16-0008`

- `y01-0003` *STATED* — Saving your preferences and saving an entire process solve different problems; knowing which one to use saves you from repeating yourself over and over again.
  > “They solve different problems, and knowing which one to use saves you from repeating yourself over and over again.”
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)

- `y01-0070` *CORE* — Project instructions (AGENTS.md / Project custom instructions) save the rules that guide work across the whole project, while a skill saves a process for a specific job.
  > “Project instructions save the rules that should guide work across the project, while a skill saves a process for a specific job.”
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8) [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *defines* `y01-0003`

- `y01-0071` *STATED* — A plugin supplies tools (such as a Google Drive connection) while a skill explains how to use those tools for a particular job.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *evidence-for* `g12-0162`
  ↳ *qualifies* `y01-0065`
  ↳ *qualifies* `y01-0043`

### definition

- `g05-0210` *STATED* — head -100 shows only the first 100 lines of a file.
  — [g-claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix](https://chen.media/guides/claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix)
  ↳ *defines* `g05-0209`

- `g08-0096` *STATED* — The Agency is a folder of more than 230 agent files grouped into divisions like Engineering, Design, Paid Media, Marketing, Product, Testing and Security.
  — [g-run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents](https://chen.media/guides/run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents)
  ↳ *defines* `g08-0089`

- `g08-0097` *STATED* — Each Agency file is one specialist: who they are, how they think, what they deliver and how they talk.
  — [g-run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents](https://chen.media/guides/run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents)
  ↳ *part-of* `g08-0096`

- `g08-0100` *STATED* — The Agency's divisions are Engineering, Design, Paid Media, Sales, Marketing, Product, Project Management, Testing, Security, Support, Spatial Computing, Game Development, Finance, Academic, GIS, Healthcare and Research, plus a Specialized division.
  — [g-run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents](https://chen.media/guides/run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents)
  ↳ *part-of* `g08-0096`
  ↳ *part-of* `g08-0089`

- `g08-0101` *STATED* — Each Agency agent file holds an identity and personality, a mission and workflow, deliverables with code examples, success metrics and a communication style.
  — [g-run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents](https://chen.media/guides/run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents)
  ↳ *defines* `g08-0097`
  ↳ *part-of* `g08-0089`

- `g12-0162` *CORE* — A Claude plugin is a folder people add once; it can hold skills, a connector, commands and agents, in any combination.
  — [g-claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed](https://chen.media/guides/claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed)
  ↳ *part-of* `g12-0153`

- `g12-0163` *STATED* — Skills are instructions that teach Claude a workflow: the steps, the defaults, and what good output looks like.
  — [g-claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed](https://chen.media/guides/claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed)
  ↳ *part-of* `g12-0162`
  ↳ *evidence-for* `g18-0100`

- `g12-0164` *CORE* — A connector is an MCP server that lets Claude reach a product's data.
  — [g-claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed](https://chen.media/guides/claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed)
  ↳ *part-of* `g12-0162`

- `g13-0121` *CORE* — A skill is an add-on that teaches Claude a new job.
  > “A skill is an add-on that teaches Claude a new job.”
  — [g-let-claude-code-watch-any-video-with-watch](https://chen.media/guides/let-claude-code-watch-any-video-with-watch)
  ↳ *defines* `g13-0119`
  ↳ *defines* `g13-0282`
  ↳ *evidence-for* `g18-0100`

- `g13-0138` *STATED* — A plugin is an add-on you install into Claude Code.
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *defines* `g13-0136`
  ↳ *contrast* `g13-0121` — plugin vs skill definitions
  ↳ *evidence-for* `g12-0162`

- `g14-0221` *STATED* — ECC stands for Everything Claude Code.
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *defines* `g14-0222`

- `g14-0293` *STATED* — A Claude skill supplies instructions and sometimes supporting scripts.
  > “A skill supplies instructions and sometimes supporting scripts”
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *contrast* `g14-0294`
  ↳ *evidence-for* `g18-0100`

- `g15-0006` *STATED* — None of Skiper UI, Vengeance UI, Animmaster Lib or React Bits is a template or a site builder; they are component libraries.
  — [g-four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed](https://chen.media/guides/four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed)
  ↳ *defines* `g15-0001`
  ↳ *enables* `g15-0007`
  ↳ *example-of* `g15-0179`

- `g15-0044` *CORE* — A Claude skill is a folder with a SKILL.md file in it.
  > “A skill is a folder with a SKILL.md file in it.”
  — [g-linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes](https://chen.media/guides/linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes)
  ↳ *enables* `g15-0045`
  ↳ *evidence-for* `g18-0100`

- `g17-0100` *STATED* — Claude SEO is an open-source SEO analysis plugin for Claude Code.
  > “Claude SEO is an open source SEO analysis plugin for Claude Code.”
  — [g-install-25-seo-skills-and-18-specialist-agents-into-claude-code](https://chen.media/guides/install-25-seo-skills-and-18-specialist-agents-into-claude-code)
  ↳ *defines* `g17-0099`

- `g17-0134` *CORE* — A Claude skill is just a markdown file of rules that Claude loads and then follows without being reminded.
  > “That is all a skill is: a markdown file of rules that Claude loads and then follows without being reminded.”
  — [g-apple-s-real-design-tokens-packaged-as-a-claude-skill](https://chen.media/guides/apple-s-real-design-tokens-packaged-as-a-claude-skill)
  ↳ *enables* `g17-0127`
  ↳ *generalizes* `g17-0225`
  ↳ *evidence-for* `g17-0311`
  ↳ *evidence-for* `g18-0100`

- `g17-0157` *STATED* — Project NOMAD is not a chatbot: it is a management application called the Command Center, plus an API that installs and runs a set of containerised tools for you through Docker.
  > “NOMAD is not a chatbot. It is a management application, which the project calls the Command Center”
  — [g-a-knowledge-server-that-keeps-answering-with-the-internet-off](https://chen.media/guides/a-knowledge-server-that-keeps-answering-with-the-internet-off)
  ↳ *defines* `g17-0155`

- `g17-0225` *CORE* — A Claude skill is a folder with a SKILL.md file in it.
  > “A skill is a folder with a SKILL.md file in it.”
  — [g-164-claude-skills-in-one-repo-which-to-take-first](https://chen.media/guides/164-claude-skills-in-one-repo-which-to-take-first)
  ↳ *enables* `g17-0231`
  ↳ *evidence-for* `g18-0100`

- `g17-0226` *STATED* — A SKILL.md file has a name, a description, and a set of instructions in plain Markdown.
  > “That file has a name, a description, and a set of instructions in plain Markdown.”
  — [g-164-claude-skills-in-one-repo-which-to-take-first](https://chen.media/guides/164-claude-skills-in-one-repo-which-to-take-first)
  ↳ *part-of* `g17-0225`
  ↳ *qualifies* `g17-0134` — folder + SKILL.md structure vs 'just a markdown file of rules'
  ↳ *evidence-for* `g18-0100`

- `g18-0004` *STATED* — ECC registers as a plugin marketplace inside Claude Code, and brings a set of specialist agents, reusable skills and commands with it.
  — [g-67-agents-281-skills-and-94-commands-in-one-install](https://chen.media/guides/67-agents-281-skills-and-94-commands-in-one-install)
  ↳ *defines* `g18-0001`
  ↳ *example-of* `g18-0156`
  ↳ *evidence-for* `g14-0222`

- `g18-0084` *CORE* — Skills are not prompts: you install a skill once and Claude keeps the capability.
  > “You install a skill once and Claude keeps the capability. That is the whole point.”
  — [g-five-animation-skills-for-claude-code-with-install-commands](https://chen.media/guides/five-animation-skills-for-claude-code-with-install-commands)
  ↳ *contrast* `g18-0103` — persistent capability vs loaded only on description match
  ↳ *evidence-for* `y01-0180`

- `g18-0100` *CORE* — A Claude Skill is a folder with a SKILL.md in it; that is the entire format: YAML frontmatter with a name and a description, then markdown instructions.
  — [g-one-command-installs-anthropic-s-own-skill-library](https://chen.media/guides/one-command-installs-anthropic-s-own-skill-library)
  ↳ *defines* `g18-0099`

- `g18-0108` *INFERRED* — The anthropics/skills repo registers under the marketplace name anthropic-agent-skills, which is the part after @ in its install lines.
  — [g-one-command-installs-anthropic-s-own-skill-library](https://chen.media/guides/one-command-installs-anthropic-s-own-skill-library)
  ↳ *defines* `g18-0106`

- `g18-0116` *STATED* — Exa MCP has two tools on by default, web_search_exa and web_fetch_exa, plus two more that can be enabled for advanced filtering and multi-step research.
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again)
  ↳ *part-of* `g18-0114`

- `g18-0156` *STATED* — A plugin marketplace is a catalog: adding one lets you browse it and installs nothing; you then install individual plugins out of it.
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *defines* `g18-0155`
  ↳ *defines* `g18-0160`

- `g18-0192` *STATED* — G0DM0D3 is not an app, not an install and not an account: the whole interface is a single index.html of about 774 KB that you open like any web page.
  — [g-one-html-file-that-runs-chatgpt-claude-gemini-and-grok-side-by-side](https://chen.media/guides/one-html-file-that-runs-chatgpt-claude-gemini-and-grok-side-by-side)
  ↳ *defines* `g18-0191`

- `g19-0141` *STATED* — Langfuse grabs every hidden agent call and lays them out in order on one screen.
  > “grabs every one of those hidden calls and lays them out in order on one screen”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *defines* `g19-0137`

- `g19-0148` *STATED* — A Langfuse key pair is a Public key starting pk-lf- and a Secret key starting sk-lf-.
  > “a Public key that starts with pk-lf- and a Secret key that starts with sk-lf-”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *defines* `g19-0147`

- `g19-0178` *STATED* — Serena plugs real language servers into Claude so it asks for code by name instead of opening whole files.
  > “Serena plugs real language servers into Claude so it asks for code by name instead.”
  — [g-give-claude-code-an-ide-brain-so-it-stops-reading-everything](https://chen.media/guides/give-claude-code-an-ide-brain-so-it-stops-reading-everything)
  ↳ *part-of* `g19-0176`
  ↳ *analogy-for* `g03-0122`
  ↳ *example-of* `g02-0241`

- `g19-0182` *STATED* — Serena gives Claude symbol-level tools: find_symbol, get_symbols_overview, find_referencing_symbols, replace_symbol_body, rename_symbol.
  > “find_symbol, get_symbols_overview, find_referencing_symbols, replace_symbol_body, rename_symbol”
  — [g-give-claude-code-an-ide-brain-so-it-stops-reading-everything](https://chen.media/guides/give-claude-code-an-ide-brain-so-it-stops-reading-everything)
  ↳ *enables* `g19-0178`

- `g20-0256` *CORE* — An MCP connects a live service to Claude once, and it stays connected in every chat after.
  > “An MCP connects a live service to Claude once, and it stays connected in every chat after.”
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *part-of* `g20-0255`
  ↳ *evidence-for* `g12-0164`

- `g23-0102` *CORE* — A skill is a small folder (a SKILL.md file plus any helper files) that teaches Claude one job.
  > “A skill is a small folder (a SKILL.md file plus any helper files) that teaches Claude one job”
  — [g-five-claude-skills-that-beat-99-of-users](https://chen.media/guides/five-claude-skills-that-beat-99-of-users)
  ↳ *evidence-for* `g18-0100`

- `g23-0148` *STATED* — His plugin cheat sheet covers MCP plugins for Claude (Claude Code / desktop); each plugs a real app or service into Claude so it can actually do the work, not just describe it.
  — [g-the-claude-plugins-cheat-sheet-add-once-then-just-ask](https://chen.media/guides/the-claude-plugins-cheat-sheet-add-once-then-just-ask)
  ↳ *evidence-for* `g20-0256`

- `y01-0043` *STATED* — Codex plugins add capabilities, including connections to other services, so information in Google Drive or Gmail doesn't have to be copied into your project first.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *analogy-for* `g12-0162`
  ↳ *analogy-for* `y01-0168` — Codex plugins ~ Claude connectors

- `y01-0065` *CORE* — A skill saves instructions for a particular type of job.
  > “A skill saves instructions for a particular type of job.”
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *evidence-for* `g18-0100`
  ↳ *part-of* `y01-0070`
  ↳ *evidence-for* `y01-0176` — same skill definition in Codex and Claude tutorials

- `y01-0168` *STATED* — Claude connectors give Claude direct access to apps like Gmail, Google Drive and Notion instead of you searching them manually.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *evidence-for* `g12-0164`
  ↳ *because* `y01-0167`

- `y01-0176` *CORE* — A Claude skill is basically a saved set of instructions that tells Claude how to handle a task step by step.
  > “a skill is basically just a saved set of instructions that tells Claude how to handle a task step-by-step.”
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *evidence-for* `g18-0100`

- `y01-0200` *STATED* — Alex's beginner definition of a skill: basically a setup file that gives Claude brand new knowledge.
  > “a skill is basically just a setup file that gives Claude brand new knowledge.”
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *evidence-for* `g18-0100`
  ↳ *defines* `y01-0199`
  ↳ *qualifies* `y01-0176` — 'gives Claude new knowledge' vs 'saved step-by-step instructions'

### example

- `g01-0183` *STATED* — Databases reachable via Scientific Agent Skills include PubChem, ChEMBL, UniProt, AlphaFold, and PubMed through Paper Lookup.
  — [g-give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills](https://chen.media/guides/give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills)
  ↳ *example-of* `g01-0182`

- `g01-0184` *STATED* — Scientific Agent Skills wraps science libraries as skills: RDKit for chemistry, Scanpy for single-cell data, DiffDock for molecular docking, PyDESeq2 for gene expression.
  — [g-give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills](https://chen.media/guides/give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills)
  ↳ *part-of* `g01-0177`

- `g02-0133` *STATED* — Atticus example: 'Code on my big screen, Chrome and Terminal on the laptop.' arranges the windows across both displays.
  — [g-control-your-whole-mac-with-your-voice-powered-by-claude](https://chen.media/guides/control-your-whole-mac-with-your-voice-powered-by-claude)
  ↳ *example-of* `g02-0132`

- `g02-0134` *STATED* — Atticus example: 'Find my notes about the Tokyo trip.' searches your files by what's inside them and opens the match.
  — [g-control-your-whole-mac-with-your-voice-powered-by-claude](https://chen.media/guides/control-your-whole-mac-with-your-voice-powered-by-claude)
  ↳ *example-of* `g02-0132`

- `g02-0135` *STATED* — Atticus example: 'What's wrong with this code?' looks at your screen and answers in a line.
  — [g-control-your-whole-mac-with-your-voice-powered-by-claude](https://chen.media/guides/control-your-whole-mac-with-your-voice-powered-by-claude)
  ↳ *example-of* `g02-0132`

- `g02-0136` *STATED* — Atticus example: 'Reply to this. Thursday works, send me a time.' reads the email on screen and writes the reply.
  — [g-control-your-whole-mac-with-your-voice-powered-by-claude](https://chen.media/guides/control-your-whole-mac-with-your-voice-powered-by-claude)
  ↳ *example-of* `g02-0132`

- `g05-0221` *STATED* — The skill guide shows what Anthropic's own skill-guide example looks like ('What the guide's own example looks like').
  — [g-claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix](https://chen.media/guides/claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix)
  ↳ *example-of* `g05-0207`

- `g05-0236` *STATED* — The 3D Asset Server guide shows what a real search returns ('What a real search returns'; 1 prompt to copy, 5 numbered steps).
  — [g-3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once](https://chen.media/guides/3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once)
  ↳ *part-of* `g05-0223`

- `g07-0039` *STATED* — REA use case: you see a feature you love in an app, like how its search finds the right note instantly, and want the same thing in your own project.
  — [g-see-how-an-apps-feature-works-with-claude-code-and-rea-free](https://chen.media/guides/see-how-an-apps-feature-works-with-claude-code-and-rea-free)
  ↳ *example-of* `g07-0038`

- `g09-0192` *STATED* — The logo-skill example from Alex's video is a brand called Zestly.
  — [g-free-claude-logo-design-skill](https://chen.media/guides/free-claude-logo-design-skill)
  ↳ *example-of* `g09-0177`

- `g10-0258` *STATED* — With Find Skills installed, tell Claude "I need tests for my app" and it looks for a skill that already does it, checks that people actually trust it, and installs it for you.
  > “I need tests for my app”
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)
  ↳ *example-of* `g10-0251`
  ↳ *part-of* `g10-0247`

- `g13-0143` *STATED* — With claude-mem you can ask about old work, like 'what did we decide about auth?'
  > “You can ask about old work, like "what did we decide about auth?"”
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *example-of* `g13-0142`
  ↳ *part-of* `g13-0136`

- `g15-0046` *STATED* — In linkedin-skills, you ask for a post and the post-writer skill answers; you paste a comment URL and the reply-handler skill answers.
  — [g-linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes](https://chen.media/guides/linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes)
  ↳ *example-of* `g15-0045`

- `g17-0234` *STATED* — Alex Chen picks ten real skills from the ComposioHQ repo and says what each is for.
  > “Ten real ones, and what each is for”
  — [g-164-claude-skills-in-one-repo-which-to-take-first](https://chen.media/guides/164-claude-skills-in-one-repo-which-to-take-first)
  ↳ *part-of* `g17-0224`
  ↳ *qualifies* `g17-0309`

- `g18-0101` *STATED* — Minimal SKILL.md template: '---', 'name: my-skill-name', 'description: What this does and when to use it', '---', '# My Skill Name', then '[instructions Claude follows when this skill is active]'.
  — [g-one-command-installs-anthropic-s-own-skill-library](https://chen.media/guides/one-command-installs-anthropic-s-own-skill-library)
  ↳ *example-of* `g18-0100`

- `g19-0183` *STATED* — With Serena, 'Show me the body of handleCheckout' pulls the function, not the 2,000-line file it lives in.
  > “"Show me the body of handleCheckout" pulls the function, not the 2,000 line file it lives in.”
  — [g-give-claude-code-an-ide-brain-so-it-stops-reading-everything](https://chen.media/guides/give-claude-code-an-ide-brain-so-it-stops-reading-everything)
  ↳ *example-of* `g19-0182`

- `g20-0262` *STATED* — Exa MCP prompt: 'Use Exa to research <topic>. Read the top sources and give me the 5 key facts with links.'
  > “Use Exa to research <topic>. Read the top sources and give me the 5 key facts with links.”
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *example-of* `g20-0259`
  ↳ *part-of* `g18-0114`

- `g20-0266` *STATED* — Apify MCP prompt: 'Use Apify to scrape <site> and return the listings as clean JSON.'
  > “Use Apify to scrape <site> and return the listings as clean JSON.”
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *example-of* `g20-0263`

- `g20-0270` *STATED* — Unstructured MCP prompt: 'Run this PDF through Unstructured and give me the tables as structured data.'
  > “Run this PDF through Unstructured and give me the tables as structured data.”
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *example-of* `g20-0267`

- `g20-0274` *STATED* — Magic MCP prompt: '/ui a pricing card with three tiers and a highlighted middle plan.'
  > “/ui a pricing card with three tiers and a highlighted middle plan.”
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *example-of* `g20-0271`
  ↳ *example-of* `g20-0124` — pricing card component

- `g22-0071` *STATED* — Connectors a Claude Code Routine can use include Google Drive, Slack, GitHub, and more.
  — [g-put-a-recurring-job-on-autopilot-with-claude-code](https://chen.media/guides/put-a-recurring-job-on-autopilot-with-claude-code)
  ↳ *example-of* `g22-0070`
  ↳ *contrast* `g22-0153` — Routine connectors vs custom MCP connector

- `g23-0154` *STATED* — Chrome DevTools MCP starter prompt: 'Open localhost:3000, reproduce the checkout bug, read the console, and tell me the exact line that’s failing.'
  > “Open localhost:3000, reproduce the checkout bug, read the console, and tell me the exact line that’s failing.”
  — [g-the-claude-plugins-cheat-sheet-add-once-then-just-ask](https://chen.media/guides/the-claude-plugins-cheat-sheet-add-once-then-just-ask)
  ↳ *example-of* `g23-0152`

- `r04-0044` *STATED* — Example /mentor invocation: /mentor a Notion clone
  > “/mentor a Notion clone”
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *example-of* `r04-0045`

- `y01-0044` *STATED* — A Codex Google Drive plugin helps it find documents in your account; a Gmail plugin helps it work with email.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *example-of* `y01-0043`

- `y01-0048` *STATED* — Plugin example: 'find the latest proposal from a vendor' - the connection gives Codex a way to search the account that contains it.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *example-of* `y01-0043`
  ↳ *evidence-for* `y01-0170` — same 'latest proposal from a vendor' connector example

- `y01-0066` *STATED* — Weekly report skill example: it explains which notes to read, how to separate finished work from next steps, and how to format the final document.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *example-of* `y01-0065`
  ↳ *evidence-for* `y01-0179` — weekly report skill used as the example in both tutorials

- `y01-0067` *STATED* — Script-writing skill example: it describes the audience, the intro structure, and the writing style you want.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *example-of* `y01-0065`

- `y01-0170` *STATED* — Gmail connector example: tell Claude to find the latest pricing proposal from a vendor - it scans your inbox, finds the exact thread and summarizes the deal.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *evidence-for* `g07-0005`
  ↳ *example-of* `y01-0168`

- `y01-0171` *STATED* — Gmail connector example: ask Claude to write an email pushing back on the timeline - it puts the email in your Gmail drafts so you can one-click send it.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *evidence-for* `g07-0005`
  ↳ *example-of* `y01-0168`

- `y01-0172` *STATED* — Google Drive connector example: ask Claude to pull from your last meeting's notes or summarize all of last quarter's planning docs.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *example-of* `y01-0168`

- `y01-0178` *STATED* — Alex uploads his weekly report skill as a zip; instead of writing a massive prompt every Friday he types one sentence telling Claude to run the report skill, and the skill triggers automatically.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *example-of* `y01-0180`
  ↳ *example-of* `y01-0177`

- `y01-0179` *STATED* — Alex's weekly report skill collects completed tasks from his work folders, lists new client emails, and formats everything into a clean document.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *part-of* `y01-0178`

- `y01-0203` *STATED* — For the demo Alex chose option 1, a clip from scratch (text-to-video).
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *example-of* `y01-0202`

- `y01-0207` *STATED* — Alex answered the fal skill: maximum 10 seconds, widescreen, maximum $1.
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *example-of* `y01-0206`
  ↳ *evidence-for* `y01-0194`
  ↳ *leads-to* `y01-0208`

- `y02-0177` *STATED* — Logo Design Skill example: for a food delivery app it turned a citrus slice into a winking grin.
  — [J8g3EZwZx20](https://youtu.be/J8g3EZwZx20)
  ↳ *part-of* `g09-0177`
  ↳ *example-of* `y02-0174`

- `y04-0143` *STATED* — Agent Reach uses: scrape jobs on LinkedIn, analyse YouTube videos, or check what's trending on Instagram - all through one tool for free.
  > “scrape jobs on LinkedIn, analyze YouTube videos or check what's trending on Instagram”
  — [VRRK9REgdaA](https://youtu.be/VRRK9REgdaA)
  ↳ *part-of* `g14-0101`
  ↳ *contrast* `y04-0028` — both let Claude analyse YouTube videos: scraping tool vs frame+audio skill
  ↳ *example-of* `y04-0140`

### idea

- `g06-0262` *CORE* — Most tools Alex picks for Claude Code are free and MIT-licensed: anatomy, magpie, Coucou, universal-modder, bigarrow and VibeWise.
  — [g-set-up-the-anatomy-skill-the-free-repo-that-turns-any-idea-into-a-working-machin](https://chen.media/guides/set-up-the-anatomy-skill-the-free-repo-that-turns-any-idea-into-a-working-machin) [g-keep-claude-code-working-after-your-limit-runs-out](https://chen.media/guides/keep-claude-code-working-after-your-limit-runs-out) [g-approve-claude-s-permission-requests-from-your-iphone-with-coucou](https://chen.media/guides/approve-claude-s-permission-requests-from-your-iphone-with-coucou) [g-set-up-universal-modder-the-free-repo-that-lets-claude-mod-your-pc-games](https://chen.media/guides/set-up-universal-modder-the-free-repo-that-lets-claude-mod-your-pc-games) [g-make-claude-point-at-the-button-you-need-to-click](https://chen.media/guides/make-claude-point-at-the-button-you-need-to-click) [g-make-claude-teach-you-while-it-writes-your-code](https://chen.media/guides/make-claude-teach-you-while-it-writes-your-code)
  ↳ *generalizes* `g06-0075`
  ↳ *generalizes* `g06-0106`
  ↳ *generalizes* `g06-0121`
  ↳ *generalizes* `g06-0125`
  ↳ *generalizes* `g06-0155`
  ↳ *generalizes* `g06-0252`
  ↳ *evidence-for* `g09-0252`

- `g17-0011` *STATED* — Alex Chen's marketing-skills guide names the two skills to install if you install only two of the seven.
  > “If you install only two”
  — [g-seven-free-claude-skills-that-cover-a-marketing-department](https://chen.media/guides/seven-free-claude-skills-that-cover-a-marketing-department)
  ↳ *part-of* `g17-0001`

- `r01-0021` *INFERRED* — Alex's skill template: one slash command, a hidden output folder, a deterministic artifact (VERDICT.md, PANEL.md, AGENCY.md), a credit footer, an honest disclaimer, and three install paths (paste link, plugin, copy folder).
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill) [r-court-skill](https://github.com/alexyc9381/court-skill) [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *generalizes* `r01-0014`
  ↳ *generalizes* `r01-0010`
  ↳ *generalizes* `r01-0003`
  ↳ *generalizes* `r01-0012`
  ↳ *generalizes* `r01-0018`

- `r01-0068` *INFERRED* — /agency is a single SKILL.md that routes eight subcommands from $ARGUMENTS into five agent roles — a multi-mode skill without separate files per agent.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *depends-on* `r01-0013`
  ↳ *part-of* `r01-0037`

- `y03-0208` *CORE* — Ownership is Alex's core pitch for open-source alternatives: work runs on your own computer or server (Photon Studio, Dyad, FluidVoice, SupoClip) and you keep the files, code or pages (Instatic).
  — [WB8w3FTYCnw](https://youtu.be/WB8w3FTYCnw) [kasTR80Lvjo](https://youtu.be/kasTR80Lvjo) [cxLfDm8_Yx4](https://youtu.be/cxLfDm8_Yx4) [a8nVKYxwcjo](https://youtu.be/a8nVKYxwcjo) [udcHbDvy7o4](https://youtu.be/udcHbDvy7o4) [OtRSHXUQxAQ](https://youtu.be/OtRSHXUQxAQ) [4xBCskEhIfE](https://youtu.be/4xBCskEhIfE) [N8BCMjq3wPE](https://youtu.be/N8BCMjq3wPE) [23JOjnkdikY](https://youtu.be/23JOjnkdikY) [fm0bvQE5IW8](https://youtu.be/fm0bvQE5IW8)
  ↳ *evidence-for* `g02-0240`
  ↳ *generalizes* `y03-0198`

- `y04-0029` *STATED* — /watch can turn any video link into a custom skill you can use in Claude or ChatGPT (transcribed 'Chat Tributee').
  > “you can turn any of those video links into a custom skill”
  — [dXOq_pNqeFA](https://youtu.be/dXOq_pNqeFA) [bmUJ_ifeXIE](https://youtu.be/bmUJ_ifeXIE) [9DM6ZdHEWls](https://youtu.be/9DM6ZdHEWls)
  ↳ *part-of* `g13-0119`
  ↳ *part-of* `y04-0025`

### method

- `g01-0003` *STATED* — The /hiring-panel skill is installed by pasting one link into Claude.
  — [g-find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free](https://chen.media/guides/find-out-why-companies-reject-your-resume-7-claudes-tell-you-first-with-the-free)
  ↳ *part-of* `g01-0001`
  ↳ *example-of* `r01-0003`

- `g01-0032` *STATED* — The AirLLM guide includes ready-made prompts so Claude Code sets AirLLM up for you (section: Let Claude Code set it up for you).
  — [g-read-a-giant-ai-model-one-page-at-a-time-run-70b-models-on-4gb-with-the-free-air](https://chen.media/guides/read-a-giant-ai-model-one-page-at-a-time-run-70b-models-on-4gb-with-the-free-air)
  ↳ *part-of* `g01-0033`
  ↳ *evidence-for* `g02-0078`

- `g01-0078` *STATED* — Show Your Work installs with 2 commands.
  — [g-show-your-work-see-every-screenshot-and-video-claude-makes-right-in-your-termina](https://chen.media/guides/show-your-work-see-every-screenshot-and-video-claude-makes-right-in-your-termina)
  ↳ *part-of* `g01-0075`

- `g01-0089` *STATED* — Graphicle's code graph covers files, functions, classes, calls and imports, parsed with tree-sitter and no model.
  — [g-give-claude-a-map-and-a-memory-of-your-whole-project](https://chen.media/guides/give-claude-a-map-and-a-memory-of-your-whole-project)
  ↳ *part-of* `g01-0087`
  ↳ *enables* `g01-0088`

- `g01-0092` *STATED* — Graphicle runs as one MCP server (graphicle mcp) that Claude Code connects to.
  > “graphicle mcp”
  — [g-give-claude-a-map-and-a-memory-of-your-whole-project](https://chen.media/guides/give-claude-a-map-and-a-memory-of-your-whole-project)
  ↳ *part-of* `g01-0087`
  ↳ *example-of* `g16-0014`

- `g01-0093` *STATED* — In Graphicle, memories an agent proposes wait for your approval.
  — [g-give-claude-a-map-and-a-memory-of-your-whole-project](https://chen.media/guides/give-claude-a-map-and-a-memory-of-your-whole-project)
  ↳ *part-of* `g01-0087`
  ↳ *example-of* `g01-0194`
  ↳ *example-of* `g12-0303`

- `g01-0098` *STATED* — With Claudemy you ask for a topic, Claude researches the web, and you get about twelve two-minute lessons with two hosts talking.
  — [g-turn-any-topic-into-a-12-lesson-audio-course-with-claude](https://chen.media/guides/turn-any-topic-into-a-12-lesson-audio-course-with-claude)
  ↳ *defines* `g01-0097`

- `g01-0109` *STATED* — The I Have ADHD skill installs in Claude Code with 2 commands.
  — [g-i-have-adhd-make-claude-lead-with-the-answer-instead-of-burying-it](https://chen.media/guides/i-have-adhd-make-claude-lead-with-the-answer-instead-of-burying-it)
  ↳ *part-of* `g01-0105`

- `g01-0179` *STATED* — Scientific Agent Skills installs in one line.
  — [g-give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills](https://chen.media/guides/give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills)
  ↳ *part-of* `g01-0177`

- `g02-0006` *STATED* — /hunter installs by pasting one link into Claude.
  > “How to install it by pasting one link into Claude”
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *enables* `g02-0001`
  ↳ *example-of* `r01-0003`

- `g02-0032` *STATED* — Context Mode installs in two lines.
  > “the two-line install”
  — [g-stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode)
  ↳ *enables* `g02-0031`

- `g02-0048` *STATED* — cc-stretch has a two-line setup.
  — [g-make-claude-s-long-answers-6x-shorter-to-read](https://chen.media/guides/make-claude-s-long-answers-6x-shorter-to-read)
  ↳ *enables* `g02-0046`

- `g02-0078` *STATED* — The AirLLM guide has a section 'Let Claude Code set it up for you': AirLLM's install and first run can be handed to Claude Code with ready-made prompts.
  — [g-run-a-235-billion-parameter-ai-model-on-a-3gb-graphics-card-set-up-the-free-airl](https://chen.media/guides/run-a-235-billion-parameter-ai-model-on-a-3gb-graphics-card-set-up-the-free-airl) [g-run-a-2-8-trillion-parameter-ai-model-on-your-gaming-graphics-card-set-up-the-fr](https://chen.media/guides/run-a-2-8-trillion-parameter-ai-model-on-your-gaming-graphics-card-set-up-the-fr)
  ↳ *part-of* `g02-0063`

- `g02-0131` *STATED* — To use Atticus you hold three keys (Control, Option and Space), say what you need, and let go.
  — [g-control-your-whole-mac-with-your-voice-powered-by-claude](https://chen.media/guides/control-your-whole-mac-with-your-voice-powered-by-claude)
  ↳ *part-of* `g02-0129`

- `g02-0164` *STATED* — You run github-triage with /github-triage inside a project.
  — [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say)
  ↳ *enables* `g02-0161`

- `g02-0166` *STATED* — github-triage handles pull requests first, before issues.
  — [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say)
  ↳ *part-of* `g02-0161`
  ↳ *leads-to* `g02-0171`

- `g02-0167` *STATED* — github-triage can merge passing bot PRs (like Dependabot) one at a time, in order.
  — [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say)
  ↳ *part-of* `g02-0166`

- `g02-0168` *STATED* — github-triage gives PRs that are approved, green and mergeable a merge prompt.
  — [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say)
  ↳ *part-of* `g02-0166`
  ↳ *evidence-for* `g02-0162`

- `g02-0171` *STATED* — If a merged PR or a commit on the default branch resolved an issue, github-triage closes it with a comment that cites the fix.
  — [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say)
  ↳ *part-of* `g02-0161`
  ↳ *leads-to* `g02-0173`

- `g02-0172` *STATED* — github-triage cross-links open PRs with the issues they would fix, so nobody works the same thing twice.
  — [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say)
  ↳ *part-of* `g02-0161`

- `g02-0173` *STATED* — github-triage gives everything left a priority (Critical, High, Medium, Low) and a size from XS to XXL.
  — [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say)
  ↳ *part-of* `g02-0161`

- `g02-0189` *STATED* — The command chrome-relay do "<goal>" runs a multi-step browser goal in one command.
  — [g-let-claude-use-your-signed-in-chrome-in-the-background](https://chen.media/guides/let-claude-use-your-signed-in-chrome-in-the-background)
  ↳ *part-of* `g02-0185`

- `g02-0190` *STATED* — Chrome Relay's open, snapshot, click and fill commands give step-by-step browser control.
  — [g-let-claude-use-your-signed-in-chrome-in-the-background](https://chen.media/guides/let-claude-use-your-signed-in-chrome-in-the-background)
  ↳ *part-of* `g02-0185`
  ↳ *contrast* `g02-0189` — step-by-step vs one-shot goal

- `g02-0222` *STATED* — AI Homepage looks at what you've been browsing and opens the pages you follow signed in as you.
  — [g-ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper](https://chen.media/guides/ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper)
  ↳ *part-of* `g02-0220`
  ↳ *example-of* `g02-0244`

- `g02-0223` *STATED* — AI Homepage rebuilds itself in the background, so each new tab is up to date.
  — [g-ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper](https://chen.media/guides/ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper)
  ↳ *part-of* `g02-0219`

- `g02-0225` *STATED* — AI Homepage writes one page from what it read: headlines, posts and links.
  — [g-ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper](https://chen.media/guides/ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper)
  ↳ *part-of* `g02-0220`

- `g03-0024` *STATED* — Step 2 of shrinking CLAUDE.md: move the rarely used steps out of CLAUDE.md and into skills.
  — [g-shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit](https://chen.media/guides/shrink-a-bloated-claude-md-so-it-stops-eating-your-claude-limit)
  ↳ *part-of* `g03-0021`
  ↳ *evidence-for* `g05-0216`

- `g03-0044` *STATED* — SkillSpector runs in two stages: a fast static scan, then an optional AI review of what the code and instructions actually do.
  — [g-skillspector-scan-any-claude-skill-for-malware-before-you-install-it](https://chen.media/guides/skillspector-scan-any-claude-skill-for-malware-before-you-install-it)
  ↳ *part-of* `g03-0035`

- `g03-0048` *STATED* — The SkillSpector guide's locked sections are "Set it up", "The catch" and "Sources"; it ships 1 prompt to copy and 5 numbered steps.
  — [g-skillspector-scan-any-claude-skill-for-malware-before-you-install-it](https://chen.media/guides/skillspector-scan-any-claude-skill-for-malware-before-you-install-it)
  ↳ *example-of* `g03-0005`
  ↳ *part-of* `g03-0035`

- `g03-0049` *STATED* — Scan any third-party Claude skill (folder or GitHub link) with SkillSpector before installing it.
  — [g-skillspector-scan-any-claude-skill-for-malware-before-you-install-it](https://chen.media/guides/skillspector-scan-any-claude-skill-for-malware-before-you-install-it)
  ↳ *depends-on* `g03-0035`
  ↳ *evidence-for* `g17-0311`

- `g03-0091` *STATED* — With Diagram Design you describe the diagram in plain words; Claude picks the type, states its plan, and writes one .html file you can open by double-clicking.
  — [g-diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe](https://chen.media/guides/diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe)
  ↳ *defines* `g03-0089`
  ↳ *analogy-for* `g03-0156` — Claude states its plan before drawing, like plan mode before editing

- `g03-0098` *STATED* — The Diagram Design guide's locked sections are "Set it up in Claude Code", "The catch" and "Sources" (1 prompt to copy, 4 numbered steps).
  — [g-diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe](https://chen.media/guides/diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe)
  ↳ *example-of* `g03-0005`
  ↳ *part-of* `g03-0089`

- `g03-0102` *STATED* — Install Caveman as a plugin from the terminal: claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman.
  > “claude plugin marketplace add JuliusBrussee/caveman && claude plugin install caveman@caveman”
  — [g-make-claude-answer-in-fewer-words-with-the-caveman-skill](https://chen.media/guides/make-claude-answer-in-fewer-words-with-the-caveman-skill)
  ↳ *example-of* `g03-0107`
  ↳ *evidence-for* `g14-0252`
  ↳ *part-of* `g03-0100`

- `g03-0103` *STATED* — Install only the Caveman skill (global) with: npx skills add JuliusBrussee/caveman -g.
  > “npx skills add JuliusBrussee/caveman -g”
  — [g-make-claude-answer-in-fewer-words-with-the-caveman-skill](https://chen.media/guides/make-claude-answer-in-fewer-words-with-the-caveman-skill)
  ↳ *example-of* `g03-0107`
  ↳ *example-of* `g18-0086`
  ↳ *part-of* `g03-0100`

- `g03-0104` *STATED* — Install Caveman from inside Claude Code: /plugin marketplace add JuliusBrussee/caveman, then /plugin install caveman@caveman.
  > “/plugin marketplace add JuliusBrussee/caveman”
  — [g-make-claude-answer-in-fewer-words-with-the-caveman-skill](https://chen.media/guides/make-claude-answer-in-fewer-words-with-the-caveman-skill)
  ↳ *example-of* `g03-0107`
  ↳ *example-of* `g18-0160`
  ↳ *part-of* `g03-0100`

- `g03-0105` *STATED* — Step 2 of the Caveman guide: switch it on and off.
  — [g-make-claude-answer-in-fewer-words-with-the-caveman-skill](https://chen.media/guides/make-claude-answer-in-fewer-words-with-the-caveman-skill)
  ↳ *part-of* `g03-0100`

- `g03-0125` *STATED* — Install the TypeScript language server with: npm install -g typescript-language-server typescript.
  > “npm install -g typescript-language-server typescript”
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *example-of* `g03-0124`
  ↳ *example-of* `g03-0123`

- `g03-0138` *STATED* — Code intelligence setup order: Step 1 install the language server for your language, Step 2 install the plugin, Step 3 check that it works.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)

- `g03-0152` *STATED* — The Minutes guide's locked sections are "Set it up", "The catch" and "Sources"; the lede promises what to ask Claude about your meetings.
  — [g-minutes-the-free-open-source-meeting-recorder-that-claude-can-search](https://chen.media/guides/minutes-the-free-open-source-meeting-recorder-that-claude-can-search)
  ↳ *example-of* `g03-0005`
  ↳ *part-of* `g03-0140`

- `g03-0178` *STATED* — Anthropic's security skills run as a pipeline: map where an attacker gets in, scan those spots, double-check every finding, and write the fixes.
  — [g-hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills](https://chen.media/guides/hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills)
  ↳ *defines* `g03-0176`

- `g03-0179` *STATED* — /threat-model maps where an attacker could get in, so the scan aims at the risky spots first.
  — [g-hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills](https://chen.media/guides/hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills)
  ↳ *part-of* `g03-0178`
  ↳ *leads-to* `g03-0180`

- `g03-0180` *STATED* — /vuln-scan reads your source and lists each security hole with its file and line.
  — [g-hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills](https://chen.media/guides/hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills)
  ↳ *part-of* `g03-0178`
  ↳ *leads-to* `g03-0181`

- `g03-0182` *STATED* — /patch writes a candidate fix for each confirmed hole as a diff you review; it is never applied for you.
  > “never applied for you”
  — [g-hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills](https://chen.media/guides/hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills)
  ↳ *example-of* `g03-0011`
  ↳ *part-of* `g03-0178`
  ↳ *example-of* `g12-0303`

- `g03-0184` *STATED* — Step 1 with Anthropic's security skills: try them on the built-in test target before your own code.
  — [g-hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills](https://chen.media/guides/hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills)
  ↳ *leads-to* `g03-0185`
  ↳ *qualifies* `g03-0183` — the example run is on a small test program

- `g03-0185` *STATED* — Step 2 with Anthropic's security skills: run them on your own code.
  — [g-hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills](https://chen.media/guides/hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills)

- `g03-0239` *STATED* — Answer me with HTML setup: Step 1 install it in Claude Code, Step 2 ask the way you always do.
  — [g-answer-me-with-html-make-claude-answer-with-one-clean-page-not-a-wall-of-text](https://chen.media/guides/answer-me-with-html-make-claude-answer-with-one-clean-page-not-a-wall-of-text)
  ↳ *part-of* `g03-0228`

- `g03-0240` *STATED* — Answer me with HTML has an optional always-on mode (Step 3) that gives you a page with every answer.
  — [g-answer-me-with-html-make-claude-answer-with-one-clean-page-not-a-wall-of-text](https://chen.media/guides/answer-me-with-html-make-claude-answer-with-one-clean-page-not-a-wall-of-text)
  ↳ *qualifies* `g03-0239`

- `g04-0027` *STATED* — Alex's Academic Research Skills guide is a 4-step walk-through with 1 copyable prompt: 'Step 1: install it', 'Step 2: what to ask', then 'The catch' and 'Sources' (bodies locked).
  — [g-academic-research-skills-make-claude-check-every-source-in-your-paper-is-real](https://chen.media/guides/academic-research-skills-make-claude-check-every-source-in-your-paper-is-real)
  ↳ *part-of* `g04-0028`

- `g04-0042` *STATED* — Harvey setup step 2: git clone https://github.com/ethanplusai/harvey.git
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *leads-to* `g04-0043`

- `g04-0043` *STATED* — Harvey setup step 3: cd harvey, then start Claude Code in the folder with: claude
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *leads-to* `g04-0044`

- `g04-0102` *STATED* — /hiring-panel installs by pasting one link into Claude.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free)
  ↳ *leads-to* `g04-0103`
  ↳ *example-of* `g04-0247`
  ↳ *example-of* `r01-0003`

- `g04-0151` *STATED* — /linkedin-roast installs by pasting one link into Claude.
  — [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *leads-to* `g04-0152`
  ↳ *example-of* `g04-0247`
  ↳ *example-of* `r01-0003`

- `g04-0247` *CORE* — Alex's own skills (/hiring-panel, /linkedin-roast) install by pasting one link into Claude.
  — [g-get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri](https://chen.media/guides/get-your-resume-past-the-robot-screen-7-claudes-try-to-reject-it-first-free-hiri) [g-practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free](https://chen.media/guides/practice-rejection-before-it-counts-run-your-resume-past-7-claudes-with-the-free) [g-5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li](https://chen.media/guides/5-claudes-roast-your-linkedin-profile-then-rewrite-every-line-set-up-the-free-li) [g-roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked](https://chen.media/guides/roast-night-for-your-linkedin-5-claudes-tear-it-apart-and-rebuild-it-free-linked)
  ↳ *evidence-for* `r01-0003`

- `g05-0002` *STATED* — Vibewise makes Claude ask how you would build something first, before it writes the code.
  — [g-turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin](https://chen.media/guides/turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin)
  ↳ *part-of* `g05-0001`
  ↳ *enables* `g05-0019` — pushes you to think conceptually before Claude writes

- `g05-0003` *STATED* — Vibewise has Claude walk you through the trade-offs of an implementation.
  — [g-turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin](https://chen.media/guides/turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin)
  ↳ *part-of* `g05-0001`

- `g05-0004` *STATED* — Vibewise has Claude explain what it changed after it edits your code.
  — [g-turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin](https://chen.media/guides/turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin)
  ↳ *part-of* `g05-0001`
  ↳ *enables* `g05-0017` — automates the high-scoring 'ask it to explain' habit

- `g05-0033` *STATED* — Chrome Relay agent tabs open inactive, in a collapsed 'Agents' tab group, in the Chrome you already use.
  — [g-let-claude-use-your-real-chrome-signed-in-in-background-tabs](https://chen.media/guides/let-claude-use-your-real-chrome-signed-in-in-background-tabs)
  ↳ *part-of* `g05-0031`
  ↳ *enables* `g05-0032`
  ↳ *part-of* `g02-0185`

- `g05-0035` *STATED* — One Chrome Relay command carries out a whole browser goal and checks every step.
  — [g-let-claude-use-your-real-chrome-signed-in-in-background-tabs](https://chen.media/guides/let-claude-use-your-real-chrome-signed-in-in-background-tabs)
  ↳ *part-of* `g05-0031`
  ↳ *evidence-for* `g02-0189`

- `g05-0041` *STATED* — The Chrome Relay workflow is two steps: set it up once, then give Claude a whole goal in one command (1 prompt to copy, 8 numbered steps).
  — [g-let-claude-use-your-real-chrome-signed-in-in-background-tabs](https://chen.media/guides/let-claude-use-your-real-chrome-signed-in-in-background-tabs)
  ↳ *part-of* `g05-0031`
  ↳ *part-of* `g02-0185`

- `g05-0044` *STATED* — AI Promo Video Maker takes one sentence as input, like a product name or a GitHub repo.
  — [g-make-a-full-promo-video-with-claude-from-one-sentence](https://chen.media/guides/make-a-full-promo-video-with-claude-from-one-sentence)
  ↳ *part-of* `g05-0043`
  ↳ *leads-to* `g05-0045`

- `g05-0047` *STATED* — AI Promo Video Maker takes 4K screenshots of the real product pages.
  — [g-make-a-full-promo-video-with-claude-from-one-sentence](https://chen.media/guides/make-a-full-promo-video-with-claude-from-one-sentence)
  ↳ *part-of* `g05-0045`
  ↳ *part-of* `g05-0318`

- `g05-0048` *STATED* — AI Promo Video Maker cuts the video to the music beat.
  — [g-make-a-full-promo-video-with-claude-from-one-sentence](https://chen.media/guides/make-a-full-promo-video-with-claude-from-one-sentence)
  ↳ *part-of* `g05-0045`

- `g05-0052` *STATED* — The promo-video guide gives what you need and a single install line for AI Promo Video Maker ('Step 1: install it').
  — [g-make-a-full-promo-video-with-claude-from-one-sentence](https://chen.media/guides/make-a-full-promo-video-with-claude-from-one-sentence)
  ↳ *part-of* `g05-0043`

- `g05-0053` *STATED* — Step 2 of the promo-video guide is to ask Claude Code for the video with one copyable prompt (6 numbered steps in all).
  — [g-make-a-full-promo-video-with-claude-from-one-sentence](https://chen.media/guides/make-a-full-promo-video-with-claude-from-one-sentence)
  ↳ *part-of* `g05-0043`

- `g05-0095` *STATED* — Making your own motion film needs software installed first ('Step 1: install what it needs').
  — [g-15-motion-design-styles-claude-can-make-from-one-prompt](https://chen.media/guides/15-motion-design-styles-claude-can-make-from-one-prompt)
  ↳ *part-of* `g05-0074`
  ↳ *leads-to* `g05-0096`

- `g05-0096` *STATED* — 'Step 2: make a film' walks you through making your own motion film from one prompt (8 numbered steps).
  — [g-15-motion-design-styles-claude-can-make-from-one-prompt](https://chen.media/guides/15-motion-design-styles-claude-can-make-from-one-prompt)
  ↳ *part-of* `g05-0074`

- `g05-0102` *STATED* — Install Effortless, step 1 — in Claude Code's chat box type: /plugin marketplace add HeyCubit/effortless
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless)
  ↳ *part-of* `g05-0098`
  ↳ *example-of* `g05-0310`
  ↳ *example-of* `g18-0160`

- `g05-0103` *STATED* — Install Effortless, step 2 — type: /plugin install effortless@effortless
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless)
  ↳ *depends-on* `g05-0102`
  ↳ *example-of* `g18-0160`

- `g05-0116` *STATED* — ReelMimic takes the reference apart: shot count, shot lengths, tempo, transitions, colours, framing and camera moves.
  — [g-reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style)
  ↳ *part-of* `g05-0114`
  ↳ *leads-to* `g05-0117`

- `g05-0125` *STATED* — ReelMimic needs some software installed before first use ('Step 1: install what it needs'; 8 numbered steps).
  — [g-reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style)
  ↳ *part-of* `g05-0114`

- `g05-0126` *STATED* — The ReelMimic guide walks through making your first video ('Step 2: make your first video').
  — [g-reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style)
  ↳ *part-of* `g05-0114`

- `g05-0129` *STATED* — In Mortiflix you write a brief and Claude builds the video in stages: the script, style frames, transitions, an animatic, music and the final.
  — [g-mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer](https://chen.media/guides/mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer)
  ↳ *part-of* `g05-0128`

- `g05-0134` *STATED* — The Mortiflix explainer pipeline runs brief, script, style frames, transitions, animatic, music, final.
  — [g-mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer](https://chen.media/guides/mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer)
  ↳ *part-of* `g05-0133`
  ↳ *example-of* `g05-0129`

- `g05-0141` *STATED* — The Mortiflix guide covers installing the app ('Step 1: install it'; 7 numbered steps).
  — [g-mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer](https://chen.media/guides/mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer)
  ↳ *part-of* `g05-0128`
  ↳ *leads-to* `g05-0142`

- `g05-0142` *STATED* — The Mortiflix guide walks through making your first video ('Step 2: make your first video').
  — [g-mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer](https://chen.media/guides/mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer)
  ↳ *part-of* `g05-0128`

- `g05-0194` *STATED* — The Haiku 5.5 guide gives one Claude Code prompt that switches your app to Haiku 5.5 and shows your new monthly cost ('Switch your app (Claude Code)'; 4 numbered steps).
  — [g-claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command](https://chen.media/guides/claude-haiku-5-5-is-ten-times-cheaper-switch-your-app-in-one-command)
  ↳ *leads-to* `g05-0179`

- `g05-0212` *STATED* — Skill fix 1: find every skill reference file over 100 lines — on Mac or Linux: wc -l ~/.claude/skills/*/*.md
  — [g-claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix](https://chen.media/guides/claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix)
  ↳ *part-of* `g05-0217`
  ↳ *depends-on* `g05-0311`

- `g05-0213` *STATED* — Skill fix 2: at the very top of each long reference file add a short contents list matching its headings — '## Contents', then one line per section.
  — [g-claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix](https://chen.media/guides/claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix)
  ↳ *part-of* `g05-0217`
  ↳ *contrast* `g05-0211` — the contents list counters bottom-of-file skipping

- `g05-0214` *STATED* — Skill fix 3: link every reference file straight from SKILL.md (one level deep).
  — [g-claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix](https://chen.media/guides/claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix)
  ↳ *part-of* `g05-0217`

- `g05-0216` *STATED* — Skill fix 4: keep the SKILL.md body itself under 500 lines and split the rest into reference files.
  — [g-claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix](https://chen.media/guides/claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix)
  ↳ *part-of* `g05-0217`
  ↳ *contrast* `g05-0175`

- `g05-0226` *STATED* — Claude drives 3D Asset Server over MCP: it searches, shows you the options with their licences, and saves the files into your project's assets/ folder.
  — [g-3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once](https://chen.media/guides/3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once)
  ↳ *part-of* `g05-0223`
  ↳ *example-of* `g16-0014`

- `g05-0227` *STATED* — Fastest 3D Asset Server setup, no key — run in your terminal: claude mcp add --transport http 3d-assets https://3d.shep.bot/mcp
  — [g-3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once](https://chen.media/guides/3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once)
  ↳ *part-of* `g05-0223`
  ↳ *contrast* `g20-0279`

- `g05-0229` *STATED* — To have Claude save 3D assets straight into your project: git clone https://github.com/arielshad/3d-asset-server.git, then npm install and npm run build (Node.js 20 or newer).
  — [g-3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once](https://chen.media/guides/3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once)
  ↳ *part-of* `g05-0223`
  ↳ *contrast* `g05-0228` — local install writes to disk; public server does not

- `g05-0230` *STATED* — Then add 3D Asset Server locally: claude mcp add 3d-assets -e ASSET_DOWNLOAD_DIR="$PWD/assets" -- node /path/to/3d-asset-server/dist/cli.js mcp
  — [g-3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once](https://chen.media/guides/3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once)
  ↳ *depends-on* `g05-0229`

- `g05-0242` *STATED* — Easiest Founder install: paste https://github.com/Jakeschincariol/founder-skill into Claude and say: install skill
  — [g-the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar](https://chen.media/guides/the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar)
  ↳ *part-of* `g05-0238`

- `g05-0243` *STATED* — Founder in Claude Code: /plugin marketplace add Jakeschincariol/founder-skill, then /plugin install founder-skill@founder-skill
  — [g-the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar](https://chen.media/guides/the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar)
  ↳ *part-of* `g05-0238`
  ↳ *contrast* `g05-0242`
  ↳ *example-of* `g05-0310`
  ↳ *example-of* `g18-0160`

- `g05-0244` *STATED* — Founder by copying folders: git clone the repo, then cp -r founder-skill/skills/founder-* ~/.claude/skills/
  — [g-the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar](https://chen.media/guides/the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar)
  ↳ *part-of* `g05-0238`
  ↳ *contrast* `g05-0243`
  ↳ *example-of* `g05-0311`

- `g05-0256` *STATED* — Install OpenQodex: in your project folder run npx openqodex init
  — [g-install-openqodex-a-second-claude-reviews-your-code-before-you-push](https://chen.media/guides/install-openqodex-a-second-claude-reviews-your-code-before-you-push)
  ↳ *part-of* `g05-0250`

- `g05-0258` *STATED* — Want only the OpenQodex skill, with no push gate and no scanner downloads? Run: npx skills add openqodex/openqodex -g
  — [g-install-openqodex-a-second-claude-reviews-your-code-before-you-push](https://chen.media/guides/install-openqodex-a-second-claude-reviews-your-code-before-you-push)
  ↳ *part-of* `g05-0250`
  ↳ *contrast* `g05-0256`
  ↳ *example-of* `g05-0311`
  ↳ *example-of* `g18-0086`

- `g05-0301` *STATED* — Install logo-design, step 1 — in Claude Code run: /plugin marketplace add kaankiziltug/logo-design-skill
  — [g-install-the-logo-design-skill](https://chen.media/guides/install-the-logo-design-skill)
  ↳ *part-of* `g05-0299`
  ↳ *example-of* `g05-0310`
  ↳ *example-of* `g18-0160`
  ↳ *part-of* `g09-0177`

- `g05-0302` *STATED* — Install logo-design, step 2 — run: /plugin install logo-design@logo-design-skill
  — [g-install-the-logo-design-skill](https://chen.media/guides/install-the-logo-design-skill)
  ↳ *depends-on* `g05-0301`
  ↳ *example-of* `g18-0160`
  ↳ *part-of* `g09-0177`

- `g05-0303` *STATED* — Without Claude Code, copy the repo's skills/logo-design folder into ~/.claude/skills/
  — [g-install-the-logo-design-skill](https://chen.media/guides/install-the-logo-design-skill)
  ↳ *part-of* `g05-0299`
  ↳ *example-of* `g05-0311`
  ↳ *part-of* `g09-0177`

- `g05-0304` *STATED* — On Claude.ai or Desktop, download logo-design.zip from the repo's Releases and upload it under Settings, Capabilities, Skills.
  — [g-install-the-logo-design-skill](https://chen.media/guides/install-the-logo-design-skill)
  ↳ *part-of* `g05-0299`
  ↳ *contrast* `g05-0303`
  ↳ *evidence-for* `g09-0190`
  ↳ *part-of* `g09-0177`

- `g05-0310` *CORE* — Alex's standard Claude Code plugin install is two commands: /plugin marketplace add <owner>/<repo>, then /plugin install <plugin>@<marketplace>.
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless) [g-the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar](https://chen.media/guides/the-founder-skill-test-a-business-idea-with-claude-before-you-spend-a-dollar) [g-install-the-logo-design-skill](https://chen.media/guides/install-the-logo-design-skill)
  ↳ *evidence-for* `g18-0160`

- `g06-0006` *STATED* — In the /iq skill a small calculator (a script, not the model) turns the two reader scores into one IQ number plus where it sits among everyone else.
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *part-of* `g06-0001`

- `g06-0012` *STATED* — Step 1 of /iq: you type /iq, it tells you what it is about to read, and it asks for your go-ahead once.
  > “You type /iq. It tells you what it is about to read, and asks once”
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *part-of* `g06-0001`
  ↳ *leads-to* `g06-0017`
  ↳ *example-of* `g12-0303`

- `g06-0017` *STATED* — Step 2 of /iq: a small script collects your messages from your past Claude Code chats into one evidence file.
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *part-of* `g06-0001`
  ↳ *leads-to* `g06-0019`

- `g06-0026` *STATED* — Step 5 of /iq: the calculator turns the two scores into ONE IQ estimate with a range and says where it sits among everyone else.
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *part-of* `g06-0001`
  ↳ *defines* `g06-0006`
  ↳ *leads-to* `g06-0028`

- `g06-0052` *STATED* — To run MiniCPM-V 4.7 on a laptop, first install Ollama from ollama.com; it is free.
  — [g-run-minicpm-v-4-7-a-free-35b-ai-on-your-laptop-or-iphone](https://chen.media/guides/run-minicpm-v-4-7-a-free-35b-ai-on-your-laptop-or-iphone)
  ↳ *part-of* `g06-0051`
  ↳ *leads-to* `g06-0053`

- `g06-0053` *STATED* — Run MiniCPM-V 4.7 by opening a terminal and typing: ollama run openbmb/minicpm-v4.7
  — [g-run-minicpm-v-4-7-a-free-35b-ai-on-your-laptop-or-iphone](https://chen.media/guides/run-minicpm-v-4-7-a-free-35b-ai-on-your-laptop-or-iphone)
  ↳ *leads-to* `g06-0056`

- `g06-0055` *STATED* — Short on disk space, run the small 1B MiniCPM-V 4.7 model (about 1.8 GB) instead: ollama run openbmb/minicpm-v4.7:1b
  — [g-run-minicpm-v-4-7-a-free-35b-ai-on-your-laptop-or-iphone](https://chen.media/guides/run-minicpm-v-4-7-a-free-35b-ai-on-your-laptop-or-iphone)
  ↳ *contrast* `g06-0054`

- `g06-0056` *STATED* — When the Ollama prompt appears, you chat with MiniCPM-V 4.7 directly in the terminal.
  — [g-run-minicpm-v-4-7-a-free-35b-ai-on-your-laptop-or-iphone](https://chen.media/guides/run-minicpm-v-4-7-a-free-35b-ai-on-your-laptop-or-iphone)

- `g06-0107` *STATED* — Install magpie by downloading the app from usemagpie.ai, or run: curl -fsSL https://usemagpie.ai/install.sh | sh
  — [g-keep-claude-code-working-after-your-limit-runs-out](https://chen.media/guides/keep-claude-code-working-after-your-limit-runs-out)
  ↳ *part-of* `g06-0105`
  ↳ *leads-to* `g06-0108`

- `g06-0108` *STATED* — In magpie, go to Providers, then Add provider, pick a preset (DeepSeek, Kimi, GLM, OpenRouter and more) and paste your API key.
  — [g-keep-claude-code-working-after-your-limit-runs-out](https://chen.media/guides/keep-claude-code-working-after-your-limit-runs-out)
  ↳ *leads-to* `g06-0110`
  ↳ *part-of* `g06-0105`

- `g06-0109` *STATED* — Add a magpie provider from the terminal with: magpie provider add deepseek <your key>
  — [g-keep-claude-code-working-after-your-limit-runs-out](https://chen.media/guides/keep-claude-code-working-after-your-limit-runs-out)
  ↳ *contrast* `g06-0108` — terminal alternative to the app

- `g06-0122` *STATED* — Coucou setup has two stages: install it on your Mac, then add your iPhone (steps in the gated part of the guide).
  — [g-approve-claude-s-permission-requests-from-your-iphone-with-coucou](https://chen.media/guides/approve-claude-s-permission-requests-from-your-iphone-with-coucou)
  ↳ *part-of* `g06-0113`
  ↳ *part-of* `g09-0232`

- `g06-0156` *STATED* — bigarrow installs with two commands (in the gated 'Step 1: install it' section).
  — [g-make-claude-point-at-the-button-you-need-to-click](https://chen.media/guides/make-claude-point-at-the-button-you-need-to-click)
  ↳ *part-of* `g06-0157`

- `g06-0168` *STATED* — Pair setup takes four steps, and the full skill is meant to be copied into SKILL.md ('The skill (copy into SKILL.md)').
  — [g-pair-make-claude-and-codex-check-each-other-s-work](https://chen.media/guides/pair-make-claude-and-codex-check-each-other-s-work)
  ↳ *part-of* `g06-0169`

- `g06-0254` *STATED* — Install VibeWise: in Claude Code run /plugin install vibe-wise@anthropic-plugin-directory, then choose a scope and confirm.
  — [g-make-claude-teach-you-while-it-writes-your-code](https://chen.media/guides/make-claude-teach-you-while-it-writes-your-code)
  ↳ *part-of* `g06-0250`
  ↳ *leads-to* `g06-0255`
  ↳ *example-of* `g18-0158`
  ↳ *part-of* `g05-0001`

- `g06-0255` *STATED* — After installing VibeWise, restart Claude Code in your project, then run /vibe-wise:learn.
  — [g-make-claude-teach-you-while-it-writes-your-code](https://chen.media/guides/make-claude-teach-you-while-it-writes-your-code)
  ↳ *part-of* `g05-0001`

- `g06-0256` *STATED* — VibeWise fallback install if the directory install is not available: /plugin marketplace add nykooi1/vibe-wise, then /plugin install vibe-wise@vibe-wise.
  — [g-make-claude-teach-you-while-it-writes-your-code](https://chen.media/guides/make-claude-teach-you-while-it-writes-your-code)
  ↳ *contrast* `g06-0254`
  ↳ *example-of* `g18-0160`
  ↳ *part-of* `g05-0001`

- `g07-0006` *STATED* — To connect Gmail to Claude, open claude.com/connectors/gmail and press 'Add to Claude', or open Connectors in Claude's settings.
  — [g-sort-your-inbox-with-claude-instead-of-superhuman](https://chen.media/guides/sort-your-inbox-with-claude-instead-of-superhuman)
  ↳ *part-of* `g07-0001` — Step 1: connect Gmail
  ↳ *leads-to* `g07-0007`
  ↳ *contrast* `g07-0293` — connector via settings vs skill via pasted link

- `g07-0007` *STATED* — When connecting the Gmail connector, sign in to the Google account you want Claude to read.
  — [g-sort-your-inbox-with-claude-instead-of-superhuman](https://chen.media/guides/sort-your-inbox-with-claude-instead-of-superhuman)
  ↳ *part-of* `g07-0001` — Step 1: connect Gmail
  ↳ *leads-to* `g07-0008`

- `g07-0008` *STATED* — After connecting Gmail, start a new chat so Claude can use the connector.
  — [g-sort-your-inbox-with-claude-instead-of-superhuman](https://chen.media/guides/sort-your-inbox-with-claude-instead-of-superhuman)
  ↳ *part-of* `g07-0001` — Step 1: connect Gmail
  ↳ *enables* `g07-0010`

- `g07-0010` *STATED* — Alex's inbox guide gives one prompt to run every morning that triages your morning inbox through the Gmail connector ('Step 2: run the morning triage'; prompt body email-gated).
  — [g-sort-your-inbox-with-claude-instead-of-superhuman](https://chen.media/guides/sort-your-inbox-with-claude-instead-of-superhuman)
  ↳ *part-of* `g07-0001`

- `g07-0026` *STATED* — Find Skills sets up in one command ('Step 1: install it'; the command is email-gated).
  — [g-let-claude-find-and-install-the-right-skill-for-any-job](https://chen.media/guides/let-claude-find-and-install-the-right-skill-for-any-job)
  ↳ *part-of* `g07-0024`
  ↳ *leads-to* `g07-0035`

- `g07-0028` *STATED* — Find Skills checks the skills.sh leaderboard first, where skills are ranked by total installs.
  — [g-let-claude-find-and-install-the-right-skill-for-any-job](https://chen.media/guides/let-claude-find-and-install-the-right-skill-for-any-job)
  ↳ *part-of* `g07-0024`
  ↳ *leads-to* `g07-0029` — fallback when leaderboard has no fit
  ↳ *evidence-for* `g10-0260`

- `g07-0029` *STATED* — If nothing on the skills.sh leaderboard fits, Find Skills searches the whole skills library by keyword.
  — [g-let-claude-find-and-install-the-right-skill-for-any-job](https://chen.media/guides/let-claude-find-and-install-the-right-skill-for-any-job)
  ↳ *part-of* `g07-0024`
  ↳ *leads-to* `g07-0030`
  ↳ *evidence-for* `g10-0260`

- `g07-0030` *STATED* — Find Skills prefers skills with 1,000+ installs from known sources (like Vercel, Anthropic or Microsoft) and well-starred repos.
  — [g-let-claude-find-and-install-the-right-skill-for-any-job](https://chen.media/guides/let-claude-find-and-install-the-right-skill-for-any-job)
  ↳ *part-of* `g07-0024`
  ↳ *leads-to* `g07-0031`
  ↳ *example-of* `g07-0298`
  ↳ *evidence-for* `g10-0261`
  ↳ *evidence-for* `g10-0262`

- `g07-0032` *STATED* — Find Skills offers to install the skill you pick rather than installing silently.
  — [g-let-claude-find-and-install-the-right-skill-for-any-job](https://chen.media/guides/let-claude-find-and-install-the-right-skill-for-any-job)
  ↳ *part-of* `g07-0024`
  ↳ *example-of* `g07-0297`
  ↳ *evidence-for* `g10-0264`
  ↳ *example-of* `g12-0303`

- `g07-0035` *STATED* — Once Find Skills is installed, you use it by telling Claude what you're working on ('Step 2: ask for what you're working on'; prompts email-gated).
  — [g-let-claude-find-and-install-the-right-skill-for-any-job](https://chen.media/guides/let-claude-find-and-install-the-right-skill-for-any-job)
  ↳ *part-of* `g07-0024`
  ↳ *part-of* `g10-0247`

- `g07-0042` *STATED* — With REA, Claude traces the feature you asked about and explains how it works.
  — [g-see-how-an-apps-feature-works-with-claude-code-and-rea-free](https://chen.media/guides/see-how-an-apps-feature-works-with-claude-code-and-rea-free)
  ↳ *part-of* `g07-0038`
  ↳ *leads-to* `g07-0043`

- `g07-0044` *STATED* — After tracing a feature, REA can have Claude write and test your own version of that feature for your project.
  — [g-see-how-an-apps-feature-works-with-claude-code-and-rea-free](https://chen.media/guides/see-how-an-apps-feature-works-with-claude-code-and-rea-free)
  ↳ *part-of* `g07-0038`

- `g07-0047` *STATED* — REA sets up in one command ('Step 1: set it up in one command'; the command is email-gated).
  — [g-see-how-an-apps-feature-works-with-claude-code-and-rea-free](https://chen.media/guides/see-how-an-apps-feature-works-with-claude-code-and-rea-free)
  ↳ *part-of* `g07-0038`
  ↳ *leads-to* `g07-0048`

- `g07-0053` *STATED* — Alex's AI-agency skill installs by pasting one link into Claude.
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents)
  ↳ *part-of* `g07-0073`
  ↳ *example-of* `g07-0293`
  ↳ *example-of* `r01-0003`

- `g07-0240` *STATED* — Alex's AirLLM guide gives the install command and the code to paste to run a model ('Step 1: install it', 'Step 2: run a model'; email-gated).
  — [g-run-a-70b-ai-model-on-a-4gb-graphics-card-set-up-the-free-airllm-library](https://chen.media/guides/run-a-70b-ai-model-on-a-4gb-graphics-card-set-up-the-free-airllm-library)
  ↳ *part-of* `g07-0224`
  ↳ *evidence-for* `g02-0063`

- `g07-0249` *STATED* — /linkedin-roast installs by pasting one link into Claude.
  — [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill)
  ↳ *part-of* `g07-0246`
  ↳ *example-of* `g07-0293`
  ↳ *example-of* `r01-0003`

- `g07-0293` *CORE* — Alex's own Claude Code skills (the AI agency, /linkedin-roast, /brain-grade) are installed by pasting one link into Claude ('Get the skill').
  — [g-run-an-ai-agency-inside-claude-five-agents](https://chen.media/guides/run-an-ai-agency-inside-claude-five-agents) [g-get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill](https://chen.media/guides/get-5-claudes-to-roast-your-linkedin-profile-then-fix-it-set-up-the-free-linkedin-roast-skill) [g-get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill](https://chen.media/guides/get-6-claudes-to-grade-how-smart-you-actually-are-from-your-own-chats-set-up-the-free-brain-grade-skill)
  ↳ *contrast* `g07-0297` — one-paste install, but every action gated
  ↳ *evidence-for* `r01-0003`

- `g08-0031` *STATED* — You install the /hiring-panel skill by pasting one link into Claude.
  > “How to install it by pasting one link into Claude”
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill)
  ↳ *enables* `g08-0028`
  ↳ *example-of* `g08-0261`
  ↳ *example-of* `r01-0003`

- `g08-0053` *STATED* — One Homebrew line installs two of the three Craft apps (exact command in the locked install section).
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *enables* `g08-0049`

- `g08-0091` *STATED* — Option 1 for installing The Agency uses the desktop app and needs no terminal.
  — [g-run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents](https://chen.media/guides/run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents)
  ↳ *enables* `g08-0089`
  ↳ *contrast* `g08-0092`
  ↳ *evidence-for* `g15-0117`

- `g08-0092` *STATED* — Option 2 installs The Agency from its repo and takes about 2 minutes.
  — [g-run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents](https://chen.media/guides/run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents)
  ↳ *enables* `g08-0089`

- `g08-0159` *STATED* — Replica's skills are meant to be run in a set order (section 'Run it in order', body locked).
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *qualifies* `g08-0156`

- `g08-0168` *STATED* — Replica's seven remaining skills plan the stack, rebuild the design system, add login and payments, score your copy against the original, rebrand it, write the landing page and put it live on your own domain.
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *part-of* `g08-0156`

- `g08-0169` *STATED* — One Replica skill plans the tech stack for your clone.
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *part-of* `g08-0168`

- `g08-0170` *STATED* — One Replica skill rebuilds the original app's design system.
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *part-of* `g08-0168`

- `g08-0171` *STATED* — One Replica skill adds login and payments to your clone.
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *part-of* `g08-0168`

- `g08-0172` *STATED* — One Replica skill scores your copy against the original app's.
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *part-of* `g08-0168`

- `g08-0173` *STATED* — One Replica skill rebrands the clone as your own.
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *part-of* `g08-0168`

- `g08-0174` *STATED* — One Replica skill writes the landing page for your version.
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *part-of* `g08-0168`

- `g08-0175` *STATED* — One Replica skill puts your version live on your own domain.
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *part-of* `g08-0168`

- `g08-0221` *STATED* — The /rival guide gives the whole skill to paste in, so you install it by pasting the skill text into Claude.
  > “The whole skill to paste in”
  — [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill)
  ↳ *enables* `g08-0220`
  ↳ *example-of* `g08-0261`

- `g08-0261` *STATED* — Alex's skills install by pasting into Claude: /hiring-panel via one pasted link, /rival by pasting the whole skill.
  — [g-run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill](https://chen.media/guides/run-your-resume-past-7-claudes-that-try-to-reject-it-set-up-the-free-hiring-panel-skill) [g-have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill](https://chen.media/guides/have-five-claudes-plan-how-to-beat-your-idea-set-up-the-free-rival-skill)
  ↳ *example-of* `r01-0003`

- `g09-0053` *STATED* — Jarvis is a free open-source repo you install in four commands.
  — [g-run-a-jarvis-on-your-own-claude-code](https://chen.media/guides/run-a-jarvis-on-your-own-claude-code)
  ↳ *part-of* `g09-0049`
  ↳ *depends-on* `g09-0057`

- `g09-0055` *STATED* — Jarvis guide order: 'Keep it safe first', and only then 'Give it more to work with'.
  — [g-run-a-jarvis-on-your-own-claude-code](https://chen.media/guides/run-a-jarvis-on-your-own-claude-code)
  ↳ *qualifies* `g09-0054`

- `g09-0180` *STATED* — To use the logo skill, add it to Claude and describe your business in a sentence or two.
  — [g-free-claude-logo-design-skill](https://chen.media/guides/free-claude-logo-design-skill)
  ↳ *part-of* `g09-0191`
  ↳ *leads-to* `g09-0181`

- `g09-0191` *STATED* — Logo skill workflow: Step 1 install it, Step 2 brief it, Step 3 pick a direction, Step 4 get the kit.
  — [g-free-claude-logo-design-skill](https://chen.media/guides/free-claude-logo-design-skill)
  ↳ *part-of* `g09-0175`

- `g09-0201` *STATED* — Point MiroFish at Claude and Claude plays every one of the simulated people.
  > “Point it at Claude, and Claude plays every one of them.”
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)
  ↳ *enables* `g09-0198`

- `g09-0207` *STATED* — Run MiroFish small first before a full-size simulation ('Step 4: run it, small first').
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)
  ↳ *qualifies* `g09-0201`
  ↳ *because* `g09-0210`
  ↳ *evidence-for* `g13-0281`

- `g09-0243` *STATED* — Coucou setup: install Coucou, connect it to Claude Code, then start a job and go do something else; extras are worth turning on after.
  — [g-coucou-free-notch-pet-that-watches-claude-code](https://chen.media/guides/coucou-free-notch-pet-that-watches-claude-code)
  ↳ *part-of* `g09-0229`

- `g10-0132` *STATED* — Alex Chen's 14 AI sites guide ends with 'Where to start' (body locked).
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)
  ↳ *part-of* `g10-0114`

- `g10-0156` *STATED* — Alex Chen's Photon Studio guide has a 'Photon Studio vs Photoshop' comparison section (body locked).
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *part-of* `g10-0152`

- `g10-0158` *STATED* — Photon Studio step 1: download Photon Studio.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *part-of* `g10-0152`

- `g10-0159` *STATED* — Photon Studio step 2: open your PSD files.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *leads-to* `g10-0158`
  ↳ *depends-on* `g10-0170`

- `g10-0160` *STATED* — Photon Studio step 3: remove a background in one click.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *leads-to* `g10-0159`
  ↳ *depends-on* `g10-0169`

- `g10-0161` *STATED* — Photon Studio step 4: retouch and design.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *leads-to* `g10-0160`

- `g10-0204` *STATED* — Alex Chen's Open Design guide has an 'Open Design vs Claude Design' comparison section (body locked).
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *part-of* `g10-0198`

- `g10-0205` *STATED* — Open Design step 1: install it (install commands locked).
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *leads-to* `g10-0206`
  ↳ *part-of* `g10-0198`

- `g10-0206` *STATED* — Open Design step 2: pick the model that does the work.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *leads-to* `g10-0207`
  ↳ *depends-on* `g10-0214`

- `g10-0207` *STATED* — Open Design step 3: choose a brand's style.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *leads-to* `g10-0208`
  ↳ *depends-on* `g10-0221`

- `g10-0208` *STATED* — Open Design step 4: make the website, the app screen or the deck.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *leads-to* `g10-0209`

- `g10-0209` *STATED* — Open Design step 5: export it, or turn it into a video.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)

- `g10-0226` *STATED* — Dyad step 1: download and install Dyad.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *part-of* `g10-0223`
  ↳ *leads-to* `g10-0227`

- `g10-0227` *STATED* — Dyad step 2: add your AI key.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *part-of* `g10-0223`
  ↳ *leads-to* `g10-0228`
  ↳ *depends-on* `g10-0238`

- `g10-0228` *STATED* — Dyad step 3: describe your first app.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *part-of* `g10-0223`
  ↳ *leads-to* `g10-0229`

- `g10-0229` *STATED* — Dyad step 4: a real database and logins, which Alex calls the part other AI builders skip.
  > “the part other AI builders skip”
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *part-of* `g10-0223`
  ↳ *leads-to* `g10-0230`

- `g10-0231` *STATED* — Alex Chen's Dyad guide has a 'Tips that make it better' section (body locked).
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *part-of* `g10-0223`

- `g10-0232` *STATED* — Alex Chen's Dyad guide has a 'Dyad vs Lovable Pro' comparison section (body locked).
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *part-of* `g10-0223`
  ↳ *part-of* `g10-0241`

- `g10-0250` *STATED* — Find Skills step 1: install it with one line (install line locked in the guide).
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)
  ↳ *part-of* `g10-0247`
  ↳ *leads-to* `g10-0251`

- `g10-0251` *STATED* — Find Skills step 2: just ask Claude for what you need.
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)
  ↳ *part-of* `g10-0247`

- `g10-0252` *STATED* — Alex Chen's Find Skills guide has a section 'What it checks before it recommends anything'.
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)
  ↳ *part-of* `g10-0247`

- `g10-0253` *STATED* — Alex Chen's Find Skills guide has a section 'Where the skills land' (install locations locked).
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)
  ↳ *part-of* `g10-0247`

- `g10-0254` *STATED* — Alex Chen's Find Skills guide has a section 'Commands worth knowing' (commands locked).
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)
  ↳ *part-of* `g10-0247`

- `g10-0266` *INFERRED* — Across his guides Alex applies one rule to third-party Claude extensions: check who made it and how many people trust it before installing (mods from trusted authors only; Find Skills wants 1K+ installs, 100+ GitHub stars, official sources), because extensions run with Claude Code's own access.
  — [g-claude-code-mods-install-commands](https://chen.media/guides/claude-code-mods-install-commands) [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill) [g-openai-agents-hacked-hugging-face-5-login-rules](https://chen.media/guides/openai-agents-hacked-hugging-face-5-login-rules)
  ↳ *evidence-for* `g17-0311`

- `g11-0032` *STATED* — Step 1 of Alex's Instatic setup is getting Instatic live, which takes about two minutes.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *part-of* `g11-0011` — Instatic setup
  ↳ *leads-to* `g11-0033`

- `g11-0033` *STATED* — Step 2 of the Instatic setup is plugging in your Claude key.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *part-of* `g11-0011` — Instatic setup
  ↳ *leads-to* `g11-0034`
  ↳ *depends-on* `g11-0018`

- `g11-0034` *STATED* — Step 3 of the Instatic setup is describing your first page to Claude.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *part-of* `g11-0011` — Instatic setup
  ↳ *leads-to* `g11-0035`

- `g11-0035` *STATED* — Step 4 of the Instatic setup is to publish, and keep the files.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *part-of* `g11-0011` — Instatic setup

- `g11-0079` *STATED* — Using the tournament skill is two steps: install it, then run it.
  — [g-make-100-claudes-fight-over-your-question](https://chen.media/guides/make-100-claudes-fight-over-your-question)
  ↳ *part-of* `g11-0057`

- `g11-0195` *STATED* — FluidVoice setup step 1 is installing it; step 2 grants permissions and picks a hotkey and a voice model.
  — [g-fluidvoice-the-free-open-source-wispr-flow](https://chen.media/guides/fluidvoice-the-free-open-source-wispr-flow)
  ↳ *leads-to* `g11-0196`
  ↳ *part-of* `g11-0181`

- `g11-0210` *STATED* — Alex's VoiceStudio guide lists what you need, then three steps: install VoiceStudio, clone your voice, then use the other tools.
  — [g-the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer](https://chen.media/guides/the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer)
  ↳ *part-of* `g11-0198`

- `g12-0055` *STATED* — The go-live skill reads your app, works out what it needs, and shows you a plan with the exact accounts and changes.
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *part-of* `g12-0051`

- `g12-0067` *STATED* — Guide section 'Step 1: install the skill' gives the go-live skill's install step (body email-gated).
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *part-of* `g12-0050`
  ↳ *leads-to* `g12-0068`

- `g12-0147` *STATED* — Guide section 'Set it up' installs the SEO skill in Claude Code (body email-gated).
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *part-of* `g12-0129`
  ↳ *leads-to* `g12-0148`
  ↳ *part-of* `g17-0099`

- `g12-0151` *STATED* — Guide section 'Optional: plug in your real Google data' covers optionally connecting your real Google data to the SEO audit (body email-gated).
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *part-of* `g12-0129`
  ↳ *qualifies* `g12-0131`

- `g12-0167` *STATED* — Guide section 'Build it: the exact steps' takes a plugin from an empty folder to a working plugin (body email-gated).
  — [g-claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed](https://chen.media/guides/claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed)
  ↳ *part-of* `g12-0153`
  ↳ *leads-to* `g12-0168`

- `g12-0168` *STATED* — Guide section 'Test and validate it' covers testing and validating a plugin before submission (body email-gated).
  — [g-claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed](https://chen.media/guides/claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed)
  ↳ *part-of* `g12-0153`
  ↳ *leads-to* `g12-0169`

- `g12-0181` *STATED* — Guide section 'Set it up' installs Fast-Jev Compaction in Claude Code (body email-gated; 6 numbered steps).
  — [g-stop-claude-code-s-compact-from-summarizing-away-your-chat](https://chen.media/guides/stop-claude-code-s-compact-from-summarizing-away-your-chat)
  ↳ *part-of* `g12-0171`
  ↳ *enables* `g12-0172`

- `g12-0196` *STATED* — Guide section 'Run it on your own computer' sets SupoClip up locally (body email-gated; 1 prompt to copy).
  — [g-supoclip-open-source-opusclip-alternative](https://chen.media/guides/supoclip-open-source-opusclip-alternative)
  ↳ *part-of* `g12-0184`
  ↳ *depends-on* `g12-0188`

- `g12-0214` *STATED* — Guide section 'Turn your own check into a skill' packages your own project-specific check as a Claude Code skill (body email-gated).
  — [g-how-to-make-claude-test-its-own-work-the-verification-loop](https://chen.media/guides/how-to-make-claude-test-its-own-work-the-verification-loop)
  ↳ *part-of* `g12-0199`

- `g12-0235` *STATED* — Guide section 'Install it in Claude Code' installs the Straight Talk skill in Claude Code (body email-gated).
  — [g-make-claude-write-like-a-human-with-the-straight-talk-skill](https://chen.media/guides/make-claude-write-like-a-human-with-the-straight-talk-skill)
  ↳ *part-of* `g12-0216`
  ↳ *enables* `g12-0217`

- `g12-0264` *STATED* — Guide section 'Check your own app with the FIX skill' runs the FIX skill on your own app (body email-gated; 1 prompt to copy).
  — [g-how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill](https://chen.media/guides/how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill)
  ↳ *part-of* `g12-0250`
  ↳ *defines* `g12-0251`

- `g12-0294` *STATED* — NVIDIA guide step 1: get your free key (body email-gated).
  — [g-free-kimi-k3-glm-and-deepseek-on-one-nvidia-key](https://chen.media/guides/free-kimi-k3-glm-and-deepseek-on-one-nvidia-key)
  ↳ *part-of* `g12-0279`
  ↳ *leads-to* `g12-0295`

- `g12-0295` *STATED* — NVIDIA guide step 2: test the key in ten seconds (body email-gated).
  — [g-free-kimi-k3-glm-and-deepseek-on-one-nvidia-key](https://chen.media/guides/free-kimi-k3-glm-and-deepseek-on-one-nvidia-key)
  ↳ *part-of* `g12-0279`
  ↳ *leads-to* `g12-0296`

- `g12-0296` *STATED* — NVIDIA guide step 3: plug the key into your coding tool (Claude Code, Codex, Cursor, Cline) (body email-gated; 8 prompts and 14 steps in the full guide).
  — [g-free-kimi-k3-glm-and-deepseek-on-one-nvidia-key](https://chen.media/guides/free-kimi-k3-glm-and-deepseek-on-one-nvidia-key)
  ↳ *part-of* `g12-0279`

- `g13-0009` *STATED* — Alex's Bot Crossing guide has a 'Set it up' section with 4 numbered steps and 3 copyable prompts.
  — [g-watch-every-claude-code-session-as-a-bot-in-bot-crossing](https://chen.media/guides/watch-every-claude-code-session-as-a-bot-in-bot-crossing)
  ↳ *part-of* `g13-0001`

- `g13-0063` *STATED* — Use Scrapling to retrieve pages, select the information you need, and turn that information into a file Claude can work with.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *part-of* `g13-0061`

- `g13-0071` *STATED* — Step 2 of Alex's Scrapling guide: install a small local workspace.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *part-of* `g13-0063`

- `g13-0072` *STATED* — Step 3 of Alex's Scrapling guide: run your first page-to-CSV export; the guide ships a tested CSV export.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *part-of* `g13-0063`

- `g13-0073` *STATED* — Alex's Scrapling guide has a step 'Choose the fetcher for the page': Scrapling's fetcher is picked per page.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *part-of* `g13-0063`

- `g13-0074` *STATED* — Alex's Scrapling guide has a step 'Connect Scrapling to Claude Code'.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *part-of* `g13-0063`

- `g13-0077` *STATED* — Alex's Scrapling guide has a step 'Clean the output before you use it'.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *part-of* `g13-0063`

- `g13-0123` *STATED* — With /watch you paste a video link, ask a question, and Claude answers from what is actually on screen and what is actually said.
  — [g-let-claude-code-watch-any-video-with-watch](https://chen.media/guides/let-claude-code-watch-any-video-with-watch)
  ↳ *part-of* `g13-0119`

- `g13-0124` *STATED* — /watch grabs a picture every time the scene changes.
  — [g-let-claude-code-watch-any-video-with-watch](https://chen.media/guides/let-claude-code-watch-any-video-with-watch)
  ↳ *part-of* `g13-0123`
  ↳ *part-of* `g13-0119`

- `g13-0125` *STATED* — /watch pulls a transcript with a timestamp on every line.
  — [g-let-claude-code-watch-any-video-with-watch](https://chen.media/guides/let-claude-code-watch-any-video-with-watch)
  ↳ *part-of* `g13-0123`
  ↳ *part-of* `g13-0119`

- `g13-0126` *STATED* — After capturing scene-change frames and a transcript, /watch has Claude look at every one of those pictures itself.
  — [g-let-claude-code-watch-any-video-with-watch](https://chen.media/guides/let-claude-code-watch-any-video-with-watch)
  ↳ *depends-on* `g13-0124`
  ↳ *part-of* `g13-0123`

- `g13-0131` *STATED* — Alex's /watch guide has a 'Set it up' section with 4 numbered steps for installing /watch in Claude Code.
  — [g-let-claude-code-watch-any-video-with-watch](https://chen.media/guides/let-claude-code-watch-any-video-with-watch)
  ↳ *part-of* `g13-0119`

- `g13-0132` *STATED* — Alex's /watch guide has a 'How to use it' section; the guide carries 7 copyable prompts for getting the most out of /watch.
  — [g-let-claude-code-watch-any-video-with-watch](https://chen.media/guides/let-claude-code-watch-any-video-with-watch)
  ↳ *part-of* `g13-0123`

- `g13-0139` *STATED* — While you work, claude-mem takes notes on what Claude does.
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *part-of* `g13-0136`

- `g13-0140` *STATED* — claude-mem shrinks its session notes down with AI.
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *leads-to* `g13-0139`
  ↳ *part-of* `g13-0136`

- `g13-0141` *STATED* — claude-mem hands the useful parts of its notes to Claude at the start of your next session.
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *leads-to* `g13-0140`
  ↳ *part-of* `g13-0136`

- `g13-0147` *STATED* — Alex's claude-mem guide has a 'Set it up' section with 3 numbered steps.
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *part-of* `g13-0136`

- `g13-0149` *STATED* — Alex's claude-mem guide has a 'Search your past work' section; the guide carries 7 copyable prompts.
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *part-of* `g13-0143`

- `g13-0150` *STATED* — Alex's claude-mem guide has a 'Keep things private' section on excluding content from memory.
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *part-of* `g13-0144`

- `g13-0156` *STATED* — To use the Public APIs directory, browse its category index, then open an entry's provider documentation.
  — [g-public-apis-claude-code-build-guide](https://chen.media/guides/public-apis-claude-code-build-guide)
  ↳ *part-of* `g13-0153`

- `g13-0199` *STATED* — HackingTool guide step 1: install the HackingTool console in an isolated environment.
  — [g-hackingtool-secure-your-own-apps](https://chen.media/guides/hackingtool-secure-your-own-apps)
  ↳ *leads-to* `g13-0200`
  ↳ *part-of* `g13-0190`

- `g13-0200` *STATED* — HackingTool guide step 2: browse the tools before running a test.
  — [g-hackingtool-secure-your-own-apps](https://chen.media/guides/hackingtool-secure-your-own-apps)
  ↳ *leads-to* `g13-0201`

- `g13-0201` *STATED* — HackingTool guide step 3: match mobile tools to the type of review.
  — [g-hackingtool-secure-your-own-apps](https://chen.media/guides/hackingtool-secure-your-own-apps)
  ↳ *leads-to* `g13-0202`

- `g13-0276` *STATED* — Claudex Loop guide step: 'Install the full workflow'.
  — [g-split-claude-and-codex-with-claudex-loop](https://chen.media/guides/split-claude-and-codex-with-claudex-loop)
  ↳ *leads-to* `g13-0277`
  ↳ *part-of* `g13-0268`

- `g13-0281` *CORE* — Start skills with one job, one relevant skill and a clear test of the result.
  > “Start with one job, one relevant skill and a clear test of the result.”
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *part-of* `g13-0282`

- `g13-0287` *STATED* — Read the licence beside the specific skill folder before redistributing it.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *leads-to* `g13-0286`

- `g13-0296` *STATED* — 100-skills guide section: 'Choose the first useful skill'.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *part-of* `g13-0281`

- `g13-0298` *STATED* — 100-skills guide section: 'How to use the catalogue'.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *part-of* `g13-0282`

- `g13-0299` *STATED* — 100-skills guide section: 'A small repeatable workflow' for trying skills.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *part-of* `g13-0281`

- `g14-0046` *STATED* — With OpenCut, start by editing and exporting a short clip, then decide whether you need a local development setup.
  — [g-opencut-repo-and-setup-guide](https://chen.media/guides/opencut-repo-and-setup-guide)
  ↳ *leads-to* `g14-0053`
  ↳ *example-of* `g14-0349`
  ↳ *evidence-for* `g13-0281`

- `g14-0048` *STATED* — OpenCut first test: make a small project with a copy of a clip, trim it, add a title and export.
  — [g-opencut-repo-and-setup-guide](https://chen.media/guides/opencut-repo-and-setup-guide)
  ↳ *part-of* `g14-0046`

- `g14-0053` *STATED* — Run the 'classic' OpenCut web source locally for development.
  > “Run the classic web source locally”
  — [g-opencut-repo-and-setup-guide](https://chen.media/guides/opencut-repo-and-setup-guide)
  ↳ *part-of* `g14-0043`

- `g14-0064` *STATED* — Claude HUD install step 1, inside Claude Code: /plugin marketplace add jarrodwatts/claude-hud
  > “/plugin marketplace add jarrodwatts/claude-hud”
  — [g-headroom-claude-hud-aisa-setup](https://chen.media/guides/headroom-claude-hud-aisa-setup)
  ↳ *part-of* `g14-0063`
  ↳ *leads-to* `g14-0065`
  ↳ *example-of* `g14-0351`
  ↳ *example-of* `g18-0160`

- `g14-0065` *STATED* — Claude HUD install step 2, inside Claude Code: /plugin install claude-hud
  > “/plugin install claude-hud”
  — [g-headroom-claude-hud-aisa-setup](https://chen.media/guides/headroom-claude-hud-aisa-setup)
  ↳ *part-of* `g14-0063`
  ↳ *leads-to* `g14-0066`

- `g14-0069` *STATED* — With AIsa, connect only the data you actually need.
  > “Connect the data you actually need”
  — [g-headroom-claude-hud-aisa-setup](https://chen.media/guides/headroom-claude-hud-aisa-setup)
  ↳ *part-of* `g14-0056`
  ↳ *qualifies* `g14-0059`
  ↳ *example-of* `g13-0281`

- `g14-0077` *STATED* — Antigravity install step 1: open the Extensions sidebar in VS Code and search for 'Google Antigravity'.
  — [g-antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you](https://chen.media/guides/antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you)
  ↳ *leads-to* `g14-0079`
  ↳ *part-of* `g14-0073`

- `g14-0079` *STATED* — Antigravity install step 2: install the extension, open its Activity Bar entry, and complete the Google sign-in and setup.
  — [g-antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you](https://chen.media/guides/antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you)
  ↳ *leads-to* `g14-0080`

- `g14-0080` *STATED* — Antigravity install step 3: open a small project you can safely experiment with.
  — [g-antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you](https://chen.media/guides/antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you)

- `g14-0084` *STATED* — Decide whether to keep Antigravity only after the small test, before adopting it for daily work.
  > “Decide whether to keep it”
  — [g-antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you](https://chen.media/guides/antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you)
  ↳ *part-of* `g14-0072`
  ↳ *evidence-for* `g13-0281`

- `g14-0106` *STATED* — Install Agent Reach by starting from the official installer instructions.
  > “Start with the official installer instructions”
  — [g-agent-reach-web-research-setup](https://chen.media/guides/agent-reach-web-research-setup)
  ↳ *part-of* `g14-0100`
  ↳ *part-of* `g14-0101`

- `g14-0112` *STATED* — With Agent Reach, choose a first research task, check the channels you need, and build a result you can verify.
  — [g-agent-reach-web-research-setup](https://chen.media/guides/agent-reach-web-research-setup)
  ↳ *part-of* `g14-0100`
  ↳ *example-of* `g14-0349`
  ↳ *evidence-for* `g13-0281`

- `g14-0232` *STATED* — ECC has separate installation paths for Claude Code and for Codex.
  > “Install in Claude Code”
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *part-of* `g14-0220`
  ↳ *depends-on* `g14-0229`
  ↳ *depends-on* `g14-0230`
  ↳ *part-of* `g14-0222`

- `g14-0233` *STATED* — ECC also offers a guided installer as an alternative to the manual Claude Code or Codex install.
  > “Use the guided installer instead”
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *part-of* `g14-0220`
  ↳ *part-of* `g14-0222`

- `g14-0252` *STATED* — Claude Octopus install command 1 (terminal): claude plugin marketplace add https://github.com/nyldn/plugins.git
  > “claude plugin marketplace add https://github.com/nyldn/plugins.git”
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *part-of* `g14-0251`
  ↳ *leads-to* `g14-0253`
  ↳ *example-of* `g14-0351`
  ↳ *example-of* `g03-0107`

- `g14-0253` *STATED* — Claude Octopus install command 2 (terminal): claude plugin install octo@nyldn-plugins
  > “claude plugin install octo@nyldn-plugins”
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *part-of* `g14-0251`
  ↳ *leads-to* `g14-0254`

- `g14-0295` *STATED* — AI-team step 1: open Claude Code in the project folder where you keep your business materials.
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *part-of* `g14-0287`
  ↳ *leads-to* `g14-0297`

- `g14-0297` *STATED* — AI-team step 2: pick one recurring task with an output you can check, such as a landing page draft or a weekly content plan.
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *leads-to* `g14-0298`
  ↳ *evidence-for* `g13-0281`

- `g14-0298` *STATED* — AI-team step 3: open the skill repository, read its installation instructions, then install that pack.
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *leads-to* `g14-0300`

- `g14-0300` *STATED* — AI-team step 4: give the agent a short business brief and ask it to adapt one skill.
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *example-of* `g14-0290`

- `g14-0301` *STATED* — Run a small example with one skill before adding more departments to your AI team.
  > “Run a small example before adding more departments.”
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *leads-to* `g14-0300`
  ↳ *example-of* `g14-0349`
  ↳ *evidence-for* `g13-0281`

- `g14-0303` *STATED* — Confirm the skill installation before using it.
  > “Confirm the installation”
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *part-of* `g14-0287`

- `g14-0304` *STATED* — Customize each Claude skill around your business, then test before expanding the team.
  > “Customize the skill around your business”
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *part-of* `g14-0287`
  ↳ *example-of* `g14-0290`
  ↳ *evidence-for* `g13-0281`

- `g14-0325` *STATED* — Make the Human Scope skill fit your own work.
  > “Make the skill fit your work”
  — [g-human-scope-storyscope-claude-writing-skill](https://chen.media/guides/human-scope-storyscope-claude-writing-skill)
  ↳ *part-of* `g14-0306`

- `g14-0326` *STATED* — Keep the StoryScope source paper and the Human Scope skill together.
  > “Keep the source and the skill together”
  — [g-human-scope-storyscope-claude-writing-skill](https://chen.media/guides/human-scope-storyscope-claude-writing-skill)
  ↳ *part-of* `g14-0306`
  ↳ *depends-on* `g14-0320`

- `g14-0328` *STATED* — Download and install the Human Scope Claude skill from the guide.
  > “Download and install Human Scope”
  — [g-human-scope-storyscope-claude-writing-skill](https://chen.media/guides/human-scope-storyscope-claude-writing-skill)
  ↳ *part-of* `g14-0306`

- `g15-0018` *STATED* — MarkItDown installs in one line (guide Part 2, 'Install it, in one line').
  — [g-why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix](https://chen.media/guides/why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix)
  ↳ *part-of* `g15-0016`

- `g15-0019` *STATED* — There are three MarkItDown commands you will actually use (guide Part 3; the commands are locked).
  — [g-why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix](https://chen.media/guides/why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix)
  ↳ *part-of* `g15-0016`

- `g15-0020` *STATED* — MarkItDown ships an MCP server; adding it to Claude Desktop is 'the one setting that makes it automatic', so you never think about converting files again.
  — [g-why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix](https://chen.media/guides/why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix)
  ↳ *part-of* `g15-0016`
  ↳ *example-of* `g20-0256`

- `g15-0058` *STATED* — Before installing a so-called verifier skill, open its SKILL.md and search for the word 'verify'; if the file never describes running a command and comparing its output, it is not a real verifier.
  — [g-claude-code-says-done-before-it-has-proved-anything-this-fixes-it](https://chen.media/guides/claude-code-says-done-before-it-has-proved-anything-this-fixes-it)
  ↳ *qualifies* `g15-0055` — test that a skill really implements the mechanism
  ↳ *depends-on* `g15-0056`
  ↳ *example-of* `g15-0185`
  ↳ *evidence-for* `g17-0311`

- `g15-0071` *STATED* — The four-repos guide names which of anydoc, herdr, DeepSeek Harness and OmniRoute to install first, plus honest limits and a first-hour plan (locked).
  — [g-four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute](https://chen.media/guides/four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute)
  ↳ *qualifies* `g15-0061`
  ↳ *example-of* `g15-0177`
  ↳ *example-of* `g16-0007`

- `g15-0119` *STATED* — There are two ways to install The Agency, the fast way and the honest way (section locked).
  — [g-the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install](https://chen.media/guides/the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install)
  ↳ *part-of* `g15-0113`
  ↳ *part-of* `g08-0089`

- `g15-0149` *STATED* — Ask eight questions before you paste anything real into an AI aggregator (questions locked).
  — [g-every-premium-ai-model-in-one-place-how-the-one-tab-route-actually-works](https://chen.media/guides/every-premium-ai-model-in-one-place-how-the-one-tab-route-actually-works)
  ↳ *part-of* `g15-0147`

- `g16-0007` *CORE* — A recurring section in his tool guides is the install (or run/try) order: "The order to install them in", "The order I would install them in", "The order to run them in", "The order to try them in" — he always sequences tools rather than dumping a list.
  > “The order to install them in”
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you) [g-five-free-github-repos-that-replace-software-you-pay-for](https://chen.media/guides/five-free-github-repos-that-replace-software-you-pay-for) [g-three-plugins-that-fix-claude-code-s-setup-limits-and-memory](https://chen.media/guides/three-plugins-that-fix-claude-code-s-setup-limits-and-memory) [g-ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm](https://chen.media/guides/ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm) [g-seven-free-claude-code-repos-that-fix-what-claude-gets-wrong](https://chen.media/guides/seven-free-claude-code-repos-that-fix-what-claude-gets-wrong) [g-the-design-command-claude-code-now-publishes-an-editable-canvas](https://chen.media/guides/the-design-command-claude-code-now-publishes-an-editable-canvas) [g-five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for](https://chen.media/guides/five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for)

- `g16-0189` *STATED* — Tip 14 (expert): install plugins from the Customize menu.
  > “14. Install plugins from the Customize menu”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *part-of* `g16-0175`
  ↳ *evidence-for* `g12-0156`

- `g16-0190` *STATED* — Tip 15 (expert): connect MCP servers, which is what actually gives Claude hands.
  > “15. Connect MCP servers, which is what actually gives it hands”
  — [g-fifteen-claude-tips-beginner-to-expert](https://chen.media/guides/fifteen-claude-tips-beginner-to-expert)
  ↳ *part-of* `g16-0175`
  ↳ *contrast* `g16-0189` — plugins add features; MCP servers give Claude hands
  ↳ *part-of* `g16-0014`

- `g16-0208` *STATED* — Build prompt 7: wire up an MCP server.
  > “Wire Up an MCP Server”
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0197`
  ↳ *part-of* `g16-0014`

- `g16-0216` *STATED* — Build prompt 15: turn a task into a skill.
  > “Turn a Task Into a Skill”
  — [g-15-claude-code-prompts-one-for-every-stage-of-the-build](https://chen.media/guides/15-claude-code-prompts-one-for-every-stage-of-the-build)
  ↳ *part-of* `g16-0199`

- `g16-0223` *STATED* — Where a free tool has a meter or a limit, he writes the limit next to it, because the limit usually decides whether it can actually replace what you pay for.
  > “the limit is usually the thing that decides whether it can actually replace what you pay for”
  — [g-five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for](https://chen.media/guides/five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for)
  ↳ *qualifies* `g16-0218`
  ↳ *evidence-for* `g18-0126`

- `g16-0230` *STATED* — Try the five free Google AI tools in a specific order.
  > “The order to try them in”
  — [g-five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for](https://chen.media/guides/five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for)
  ↳ *part-of* `g16-0218`
  ↳ *example-of* `g16-0007`

- `g16-0243` *STATED* — Install the five free repos in a specific order.
  > “The order to install them in”
  — [g-five-free-github-repos-that-replace-software-you-pay-for](https://chen.media/guides/five-free-github-repos-that-replace-software-you-pay-for)
  ↳ *part-of* `g16-0232`
  ↳ *example-of* `g16-0007`

- `g16-0272` *STATED* — Prompt Master installs from a browser in about a minute with no terminal.
  — [g-the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting](https://chen.media/guides/the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting)
  ↳ *part-of* `g16-0270`

- `g16-0289` *STATED* — The order he lists the three plugins in (Setup, OmniRoute, Claude Mem) is also the order you should install them in.
  — [g-three-plugins-that-fix-claude-code-s-setup-limits-and-memory](https://chen.media/guides/three-plugins-that-fix-claude-code-s-setup-limits-and-memory)
  ↳ *part-of* `g16-0282`
  ↳ *example-of* `g16-0007`

- `g16-0306` *STATED* — A single block you paste into Claude Code sets up all seven repos in one go.
  > “the one paste that installs all of them”
  — [g-seven-free-claude-code-repos-that-fix-what-claude-gets-wrong](https://chen.media/guides/seven-free-claude-code-repos-that-fix-what-claude-gets-wrong)
  ↳ *part-of* `g16-0305`

- `g16-0315` *STATED* — Install the seven repos in the order they are worth installing.
  > “The seven, in the order they are worth installing”
  — [g-seven-free-claude-code-repos-that-fix-what-claude-gets-wrong](https://chen.media/guides/seven-free-claude-code-repos-that-fix-what-claude-gets-wrong)
  ↳ *leads-to* `g16-0306`
  ↳ *example-of* `g16-0007`

- `g17-0009` *STATED* — Alex Chen lists the seven marketing skills in dependency order, which is also the order they appear in his video.
  > “So this is the list in dependency order, which is also the order they appear in the video.”
  — [g-seven-free-claude-skills-that-cover-a-marketing-department](https://chen.media/guides/seven-free-claude-skills-that-cover-a-marketing-department)
  ↳ *example-of* `g17-0010`
  ↳ *example-of* `g17-0312`
  ↳ *example-of* `g16-0007`

- `g17-0087` *STATED* — Alex Chen checked all three plugins' numbers against the GitHub API on the day he wrote the guide rather than taking them from a blog.
  > “all three were checked against the GitHub API on the day this was written rather than taken from a blog”
  — [g-the-three-claude-code-plugins-worth-installing](https://chen.media/guides/the-three-claude-code-plugins-worth-installing)
  ↳ *evidence-for* `g17-0092`
  ↳ *evidence-for* `g17-0303`

- `g17-0096` *STATED* — There is a proper way to use Find Skills, which the plugins guide spells out.
  > “Find Skills, used properly”
  — [g-the-three-claude-code-plugins-worth-installing](https://chen.media/guides/the-three-claude-code-plugins-worth-installing)
  ↳ *qualifies* `g17-0090`
  ↳ *part-of* `g17-0309`

- `g17-0111` *STATED* — Alex Chen's Claude SEO guide gives a first run that produces something useful.
  > “A first run that gives you something useful”
  — [g-install-25-seo-skills-and-18-specialist-agents-into-claude-code](https://chen.media/guides/install-25-seo-skills-and-18-specialist-agents-into-claude-code)
  ↳ *leads-to* `g17-0102`

- `g17-0139` *STATED* — Alex Chen's Apple guide shows how to turn the design numbers into a Claude skill.
  > “Making it a skill”
  — [g-apple-s-real-design-tokens-packaged-as-a-claude-skill](https://chen.media/guides/apple-s-real-design-tokens-packaged-as-a-claude-skill)
  ↳ *example-of* `g17-0134`

- `g17-0144` *STATED* — With FreeLLMAPI you add the free keys you already qualify for and it serves all of them behind a single OpenAI-compatible endpoint.
  > “it serves all of them behind a single OpenAI compatible endpoint”
  — [g-pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint](https://chen.media/guides/pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint)
  ↳ *part-of* `g17-0143`

- `g17-0145` *STATED* — Point any OpenAI client at your local FreeLLMAPI server and it routes transparently across whichever providers you have added.
  > “Point any OpenAI client at your local server and it routes transparently”
  — [g-pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint](https://chen.media/guides/pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint)
  ↳ *part-of* `g17-0143`

- `g17-0164` *STATED* — Alex Chen's NOMAD guide walks the install from start to finish.
  > “The install, start to finish”
  — [g-a-knowledge-server-that-keeps-answering-with-the-internet-off](https://chen.media/guides/a-knowledge-server-that-keeps-answering-with-the-internet-off)
  ↳ *qualifies* `g17-0158`

- `g17-0232` *STATED* — Because a skill is portable text, anyone can publish one and anyone can read one before they run it.
  > “anyone can publish one and anyone can read one before they run it”
  — [g-164-claude-skills-in-one-repo-which-to-take-first](https://chen.media/guides/164-claude-skills-in-one-repo-which-to-take-first)
  ↳ *because* `g17-0231`
  ↳ *evidence-for* `g17-0311`

- `g17-0236` *STATED* — Alex Chen's ComposioHQ guide shows how to install one Claude skill.
  > “How to install one”
  — [g-164-claude-skills-in-one-repo-which-to-take-first](https://chen.media/guides/164-claude-skills-in-one-repo-which-to-take-first)
  ↳ *qualifies* `g17-0225`

- `g17-0263` *STATED* — There are three ways to install The Agency into Claude Code.
  > “Install it, three ways”
  — [g-286-specialist-ai-agents-free-inside-claude-code](https://chen.media/guides/286-specialist-ai-agents-free-inside-claude-code)
  ↳ *part-of* `g17-0258`
  ↳ *part-of* `g08-0089`

- `g17-0273` *STATED* — There are three ways to run Open Generative AI.
  > “The three ways to run it”
  — [g-400-ai-image-and-video-models-in-one-free-desktop-app](https://chen.media/guides/400-ai-image-and-video-models-in-one-free-desktop-app)
  ↳ *part-of* `g17-0268`

- `g17-0276` *STATED* — Alex Chen shares a Claude Code plus Open Generative AI workflow worth stealing.
  > “A workflow worth stealing”
  — [g-400-ai-image-and-video-models-in-one-free-desktop-app](https://chen.media/guides/400-ai-image-and-video-models-in-one-free-desktop-app)
  ↳ *example-of* `g17-0272`

- `g18-0002` *STATED* — ECC installs in two lines, is MIT licensed, and is free.
  — [g-67-agents-281-skills-and-94-commands-in-one-install](https://chen.media/guides/67-agents-281-skills-and-94-commands-in-one-install)
  ↳ *part-of* `g18-0001`
  ↳ *example-of* `g18-0288`
  ↳ *part-of* `g14-0222`

- `g18-0008` *STATED* — ECC can also be installed into Codex (gated section 'If you want it in Codex as well').
  — [g-67-agents-281-skills-and-94-commands-in-one-install](https://chen.media/guides/67-agents-281-skills-and-94-commands-in-one-install)
  ↳ *part-of* `g18-0001`
  ↳ *qualifies* `g18-0005`
  ↳ *evidence-for* `g14-0232`

- `g18-0009` *STATED* — ECC can be installed from a git clone instead of through the plugin marketplace (gated section 'If you would rather install from a clone').
  — [g-67-agents-281-skills-and-94-commands-in-one-install](https://chen.media/guides/67-agents-281-skills-and-94-commands-in-one-install)
  ↳ *part-of* `g18-0001`
  ↳ *contrast* `g18-0004`
  ↳ *part-of* `g14-0222`

- `g18-0011` *STATED* — ECC has install profiles, and Alex's honest advice is to start with a smaller one rather than installing everything.
  > “Profiles exist, and starting smaller is the honest advice”
  — [g-67-agents-281-skills-and-94-commands-in-one-install](https://chen.media/guides/67-agents-281-skills-and-94-commands-in-one-install)
  ↳ *qualifies* `g18-0002`
  ↳ *example-of* `g18-0285`
  ↳ *evidence-for* `g13-0281`
  ↳ *part-of* `g14-0222`

- `g18-0022` *STATED* — Alex teaches a method for judging any open source tool in about five minutes.
  — [g-the-open-source-agent-tool-two-yc-founders-gave-away](https://chen.media/guides/the-open-source-agent-tool-two-yc-founders-gave-away)
  ↳ *generalizes* `g18-0015`
  ↳ *depends-on* `g18-0017` — licence check is part of judging a tool

- `g18-0025` *STATED* — Each price in the 15-replacements guide is the highest self-serve plan on that tool's pricing page, not the cheapest.
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *qualifies* `g18-0024`
  ↳ *because* `g18-0026`

- `g18-0051` *STATED* — The 15-replacements guide ends with an 'If you only do three' shortlist of the swaps to make first.
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0024`

- `g18-0055` *STATED* — Graphify installs with two commands: the first installs the tool, the second wires it into Claude Code as a skill.
  — [g-stop-claude-code-re-reading-your-repo-every-session](https://chen.media/guides/stop-claude-code-re-reading-your-repo-every-session)
  ↳ *part-of* `g18-0054`

- `g18-0056` *STATED* — Graphify's tool install command is `uv tool install graphifyy` (the package name has a double y).
  > “uv tool install graphifyy”
  — [g-stop-claude-code-re-reading-your-repo-every-session](https://chen.media/guides/stop-claude-code-re-reading-your-repo-every-session)
  ↳ *part-of* `g18-0055`

- `g18-0057` *STATED* — `graphify install` is the second command, which wires Graphify into Claude Code as a skill.
  > “graphify install”
  — [g-stop-claude-code-re-reading-your-repo-every-session](https://chen.media/guides/stop-claude-code-re-reading-your-repo-every-session)
  ↳ *part-of* `g18-0055`

- `g18-0096` *STATED* — Open Generative AI sets up in four steps.
  — [g-the-open-source-ai-studio-that-replaces-a-video-subscription](https://chen.media/guides/the-open-source-ai-studio-that-replaces-a-video-subscription)
  ↳ *part-of* `g18-0092`
  ↳ *evidence-for* `g17-0273`
  ↳ *part-of* `g17-0268`

- `g18-0105` *STATED* — Add Anthropic's skill marketplace in Claude Code with `/plugin marketplace add anthropics/skills`.
  > “/plugin marketplace add anthropics/skills”
  — [g-one-command-installs-anthropic-s-own-skill-library](https://chen.media/guides/one-command-installs-anthropic-s-own-skill-library)
  ↳ *part-of* `g18-0099`
  ↳ *example-of* `g18-0160`

- `g18-0106` *STATED* — Install Anthropic's document skills with `/plugin install document-skills@anthropic-agent-skills`.
  > “/plugin install document-skills@anthropic-agent-skills”
  — [g-one-command-installs-anthropic-s-own-skill-library](https://chen.media/guides/one-command-installs-anthropic-s-own-skill-library)
  ↳ *depends-on* `g18-0105`
  ↳ *part-of* `g18-0099`

- `g18-0107` *STATED* — Install Anthropic's example skills with `/plugin install example-skills@anthropic-agent-skills`.
  > “/plugin install example-skills@anthropic-agent-skills”
  — [g-one-command-installs-anthropic-s-own-skill-library](https://chen.media/guides/one-command-installs-anthropic-s-own-skill-library)
  ↳ *depends-on* `g18-0105`
  ↳ *part-of* `g18-0099`

- `g18-0118` *STATED* — Claude Desktop config for Exa MCP: {"mcpServers": {"exa": {"command": "npx", "args": ["-y", "mcp-remote", "https://mcp.exa.ai/mcp"]}}}.
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again)
  ↳ *part-of* `g18-0114`
  ↳ *contrast* `g20-0260`

- `g18-0119` *STATED* — In Claude Desktop you can add Exa without touching the config file: Settings, then Connectors, search for Exa, click the plus.
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again)
  ↳ *contrast* `g18-0118` — connector UI vs config file
  ↳ *evidence-for* `g22-0153`
  ↳ *part-of* `g18-0114`

- `g18-0124` *STATED* — The MCP guide maps which server solves which problem, so you install only the one that matches your gap.
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again)
  ↳ *enables* `g18-0112`
  ↳ *example-of* `g18-0280`
  ↳ *example-of* `g18-0285`

- `g18-0127` *STATED* — Before cancelling a paid tool, run the free replacement for a week on real work first.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *qualifies* `g18-0125`
  ↳ *qualifies* `g18-0052`
  ↳ *example-of* `g18-0285`
  ↳ *evidence-for* `g13-0281`

- `g18-0160` *CORE* — The shape of every Claude Code plugin install: `/plugin marketplace add owner/repo`, then `/plugin install plugin-name@marketplace-name`, then `/reload-plugins`.
  > “/plugin marketplace add owner/repo
/plugin install plugin-name@marketplace-name
/reload-plugins”
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *defines* `g18-0155`

- `g18-0173` *STATED* — Do the whole five-plugin setup in one sitting, in the guide's order.
  > “Do It in One Sitting”
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *part-of* `g18-0154`
  ↳ *example-of* `g16-0007`

- `g18-0175` *STATED* — The video-watching skill needs two files saved and three things installed.
  — [g-the-skill-that-makes-claude-watch-a-video-not-read-about-it](https://chen.media/guides/the-skill-that-makes-claude-watch-a-video-not-read-about-it)
  ↳ *part-of* `g18-0174`

- `g18-0180` *STATED* — Video skill setup: install three things, save the script, make it a skill, use it; the guide also flags 'the one decision that matters' and a 'Before you Trust It' check.
  — [g-the-skill-that-makes-claude-watch-a-video-not-read-about-it](https://chen.media/guides/the-skill-that-makes-claude-watch-a-video-not-read-about-it)
  ↳ *defines* `g18-0175`
  ↳ *example-of* `g18-0279`

- `g18-0187` *STATED* — Getting the memory folder into NotebookLM is a one-time setup; after that it is automatic through Google Drive or a five-second upload.
  — [g-give-claude-a-memory-that-survives-the-chat-window](https://chen.media/guides/give-claude-a-memory-that-survives-the-chat-window)
  ↳ *depends-on* `g18-0186`

- `g18-0197` *STATED* — G0DM0D3 sets up in four steps, and the guide adds 'What it costs' and a 'Read this before you use it' warning.
  — [g-one-html-file-that-runs-chatgpt-claude-gemini-and-grok-side-by-side](https://chen.media/guides/one-html-file-that-runs-chatgpt-claude-gemini-and-grok-side-by-side)
  ↳ *part-of* `g18-0191`
  ↳ *example-of* `g18-0279`

- `g18-0222` *STATED* — The awesome-freellm-apis list is updated continuously, so treat it as the source of truth rather than anything you copy out of it once.
  — [g-134-free-llm-apis-and-how-to-point-your-editor-at-them](https://chen.media/guides/134-free-llm-apis-and-how-to-point-your-editor-at-them)
  ↳ *qualifies* `g18-0220`
  ↳ *qualifies* `g17-0089`

- `g18-0277` *STATED* — Alex gives an install order for the seven repos ('Install in this order').
  — [g-seven-free-repos-that-replace-paid-ai-tools](https://chen.media/guides/seven-free-repos-that-replace-paid-ai-tools)
  ↳ *part-of* `g18-0262`
  ↳ *example-of* `g16-0007`

- `g18-0285` *CORE* — Alex's install advice is to start small: one MCP server, a smaller ECC profile, not all five animation skills, a one-week trial of any free tool.
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again) [g-67-agents-281-skills-and-94-commands-in-one-install](https://chen.media/guides/67-agents-281-skills-and-94-commands-in-one-install) [g-five-animation-skills-for-claude-code-with-install-commands](https://chen.media/guides/five-animation-skills-for-claude-code-with-install-commands) [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *because* `g18-0283`
  ↳ *evidence-for* `g13-0281`

- `g19-0093` *STATED* — /route step 1: go to aistudio.google.com/apikey, click Create API key, and copy it.
  > “Go to aistudio.google.com/apikey, click Create API key, and copy it.”
  — [g-run-gemini-inside-claude-code-with-claude-as-the-boss](https://chen.media/guides/run-gemini-inside-claude-code-with-claude-as-the-boss)
  ↳ *part-of* `g19-0091`
  ↳ *leads-to* `g19-0095`

- `g19-0095` *STATED* — /route step 2: install the Gemini CLI.
  > “Install the Gemini CLI”
  — [g-run-gemini-inside-claude-code-with-claude-as-the-boss](https://chen.media/guides/run-gemini-inside-claude-code-with-claude-as-the-boss)
  ↳ *part-of* `g19-0091`
  ↳ *leads-to* `g19-0096`

- `g19-0096` *STATED* — /route step 3: add the Gemini plugin to Claude Code.
  > “Add the Gemini plugin to Claude Code”
  — [g-run-gemini-inside-claude-code-with-claude-as-the-boss](https://chen.media/guides/run-gemini-inside-claude-code-with-claude-as-the-boss)
  ↳ *part-of* `g19-0091`
  ↳ *leads-to* `g19-0097`

- `g19-0097` *STATED* — /route step 4: paste Prompt 1 into Claude Code to connect Gemini 3.6.
  > “Paste Prompt 1, connect Gemini”
  — [g-run-gemini-inside-claude-code-with-claude-as-the-boss](https://chen.media/guides/run-gemini-inside-claude-code-with-claude-as-the-boss)
  ↳ *part-of* `g19-0091`
  ↳ *leads-to* `g19-0098`

- `g19-0098` *STATED* — /route step 5: paste Prompt 2 to have Claude build the /route skill.
  > “Paste Prompt 2, build the /route skill”
  — [g-run-gemini-inside-claude-code-with-claude-as-the-boss](https://chen.media/guides/run-gemini-inside-claude-code-with-claude-as-the-boss)
  ↳ *part-of* `g19-0091`
  ↳ *enables* `g19-0099`

- `g19-0103` *STATED* — Claude wires up the ComfyUI node graph, so you get any image or a whole video with zero subscription.
  > “Claude wires up the node graph and you get any image, or a whole video, with zero subscription.”
  — [g-five-free-repos-that-give-claude-actual-hands](https://chen.media/guides/five-free-repos-that-give-claude-actual-hands)
  ↳ *qualifies* `g19-0102`

- `g19-0104` *STATED* — With ComfyUI, start from a ready-made text-to-image workflow, then ask Claude to add a video node.
  > “Start from a ready-made text-to-image workflow, then ask Claude to add a video node.”
  — [g-five-free-repos-that-give-claude-actual-hands](https://chen.media/guides/five-free-repos-that-give-claude-actual-hands)
  ↳ *part-of* `g19-0103`

- `g19-0109` *STATED* — A bonus section not in the video gives the install order that keeps the five-repo setup simple.
  > “The install order that keeps it simple”
  — [g-five-free-repos-that-give-claude-actual-hands](https://chen.media/guides/five-free-repos-that-give-claude-actual-hands)
  ↳ *part-of* `g19-0101`
  ↳ *example-of* `g16-0007`

- `g19-0143` *STATED* — In Langfuse you can click into any run, see the exact steps it took, and scroll straight to the moment something went wrong.
  > “scroll straight to the moment something went wrong”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *enables* `g19-0141`

- `g19-0144` *STATED* — Langfuse runs two free ways: cloud or self-hosted.
  > “Two ways to run it, both free.”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *part-of* `g19-0136`

- `g19-0145` *STATED* — Langfuse cloud: go to cloud.langfuse.com, sign up, and create a project.
  > “Cloud: go to cloud.langfuse.com, sign up, and create a project.”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *part-of* `g19-0144`
  ↳ *leads-to* `g19-0147`

- `g19-0146` *STATED* — Self-host Langfuse on your own machine with Docker if you want your data to stay local.
  > “Self-host: run it on your own machine with Docker if you want your data to stay local.”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *part-of* `g19-0144`
  ↳ *example-of* `g02-0240`

- `g19-0147` *STATED* — In Langfuse open Settings, then API Keys, and create a new key pair.
  > “open Settings and then API Keys, and create a new key pair”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *part-of* `g19-0136`

- `g19-0149` *STATED* — Self-host Langfuse in one command: git clone https://github.com/langfuse/langfuse.git, cd langfuse, docker compose up.
  > “git clone https://github.com/langfuse/langfuse.git
cd langfuse
docker compose up”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *part-of* `g19-0136`
  ↳ *example-of* `g19-0146`

- `g19-0150` *STATED* — After docker compose up, open self-hosted Langfuse at http://localhost:3000.
  > “# then open http://localhost:3000”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *leads-to* `g19-0149`

- `g19-0151` *STATED* — Instrument a Python agent for Langfuse with 'from langfuse import observe' and the @observe() decorator on each function, e.g. def plan(task) and def read_file(path).
  > “from langfuse import observe
@observe()
def plan(task):”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)
  ↳ *part-of* `g19-0136`
  ↳ *leads-to* `g19-0153`

- `g19-0160` *STATED* — Install the four repos in this order: Claude Code Router, then Repomix, then Graphiti and Task Master.
  > “Install them in this order”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *part-of* `g19-0155`
  ↳ *example-of* `g16-0007`

- `g19-0179` *STATED* — Install Serena once, add one config step, done.
  > “Install it once, add one config step, done.”
  — [g-give-claude-code-an-ide-brain-so-it-stops-reading-everything](https://chen.media/guides/give-claude-code-an-ide-brain-so-it-stops-reading-everything)
  ↳ *part-of* `g19-0176`

- `g19-0190` *STATED* — The Serena guide's 'The Part Everyone Misses' and 'The one config that makes it click' cover the single config step after installing.
  > “The one config that makes it click”
  — [g-give-claude-code-an-ide-brain-so-it-stops-reading-everything](https://chen.media/guides/give-claude-code-an-ide-brain-so-it-stops-reading-everything)
  ↳ *part-of* `g19-0176`
  ↳ *part-of* `g19-0179`

- `g19-0191` *STATED* — The Serena guide includes 'How to tell it is working', '3 quick wins to try' and Troubleshooting.
  > “How to tell it is working”
  — [g-give-claude-code-an-ide-brain-so-it-stops-reading-everything](https://chen.media/guides/give-claude-code-an-ide-brain-so-it-stops-reading-everything)
  ↳ *part-of* `g19-0176`
  ↳ *qualifies* `g19-0179`

- `g20-0025` *STATED* — Day 1 STEP 1 connects Obsidian as your vault, so Claude can search your notes.
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *part-of* `g20-0023`
  ↳ *leads-to* `g20-0026`
  ↳ *example-of* `g20-0256` — Obsidian as local MCP

- `g20-0026` *STATED* — Day 1 STEP 2 connects Fireflies, your meeting recorder, so Claude can pull up what was actually said in meetings.
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *part-of* `g20-0023`
  ↳ *leads-to* `g20-0027`

- `g20-0027` *STATED* — Day 1 STEP 3 connects Gmail, and specifically your sent folder, because your sent emails are what show how you write.
  > “STEP 3: Gmail, and specifically your sent folder”
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *part-of* `g20-0023`
  ↳ *enables* `g20-0028` — sent folder feeds the voice profile
  ↳ *evidence-for* `g07-0005`

- `g20-0040` *STATED* — Obsidian is connected to Claude as a Desktop extension or via the config file instead of the Connectors screen.
  > “Obsidian is installed as a Desktop extension or via the config file instead.”
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *contrast* `g20-0037`
  ↳ *part-of* `g20-0025`
  ↳ *because* `g20-0038`

- `g20-0042` *STATED* — For Obsidian the guide gives the three-click version first and the fallback second.
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)

- `g20-0053` *STATED* — On a Mac, clicking Obsidian's red button often quits the app entirely, so use Command+H to hide it instead.
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *part-of* `g20-0052`

- `g20-0232` *STATED* — Upgrade 2 of 4 is MCP, which gives Claude hands.
  > “MCP: give it hands”
  — [g-four-upgrades-that-make-claude-code-run-like-a-newer-model](https://chen.media/guides/four-upgrades-that-make-claude-code-run-like-a-newer-model)
  ↳ *part-of* `g20-0229`
  ↳ *leads-to* `g20-0233`
  ↳ *contrast* `g20-0226` — fixes missing tools
  ↳ *defines* `g20-0256`
  ↳ *evidence-for* `g16-0014`

- `g20-0260` *STATED* — Install the Exa MCP in Claude Code with: claude mcp add exa -- npx -y exa-mcp-server
  > “claude mcp add exa -- npx -y exa-mcp-server”
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *part-of* `g20-0259`
  ↳ *part-of* `g18-0114`

- `g20-0261` *STATED* — The Exa MCP needs a free EXA_API_KEY from exa.ai, set as EXA_API_KEY in the command's env.
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *depends-on* `g20-0260`
  ↳ *evidence-for* `g18-0117`

- `g20-0264` *STATED* — Install the Apify MCP in Claude Code with: claude mcp add apify -- npx -y @apify/actors-mcp-server
  > “claude mcp add apify -- npx -y @apify/actors-mcp-server”
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *part-of* `g20-0263`

- `g20-0265` *STATED* — The Apify MCP needs a free APIFY_TOKEN from apify.com, set as APIFY_TOKEN in env.
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *depends-on* `g20-0264`

- `g20-0268` *STATED* — Install the Unstructured MCP in Claude Code with: claude mcp add unstructured -- uvx uns-mcp
  > “claude mcp add unstructured -- uvx uns-mcp”
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *part-of* `g20-0267`

- `g20-0269` *STATED* — The Unstructured MCP needs a free UNSTRUCTURED_API_KEY from unstructured.io, set in env.
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *depends-on* `g20-0268`

- `g20-0272` *STATED* — Install the 21st.dev Magic MCP in Claude Code with: claude mcp add magic -- npx -y @21st-dev/magic@latest
  > “claude mcp add magic -- npx -y @21st-dev/magic@latest”
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *part-of* `g20-0271`

- `g20-0273` *STATED* — The 21st.dev Magic MCP needs a free API key from 21st.dev/magic, set in env.
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *depends-on* `g20-0272`

- `g20-0276` *STATED* — Install the Context7 MCP in Claude Code with: claude mcp add context7 -- npx -y @upstash/context7-mcp
  > “claude mcp add context7 -- npx -y @upstash/context7-mcp”
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *part-of* `g20-0275`
  ↳ *part-of* `g18-0123`

- `g20-0278` *STATED* — The five-MCP guide closes with 'Keep them on': leave the MCPs connected.
  > “Keep them on”
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *part-of* `g20-0255`
  ↳ *because* `g20-0256`

- `g20-0279` *INFERRED* — In Claude Code an MCP server's API key is passed with the -e flag on claude mcp add, for example: claude mcp add -e EXA_API_KEY=your-key exa -- npx -y exa-mcp-server; the -- separates Claude's flags from the server launch command.
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *qualifies* `g20-0261`

- `g21-0007` *STATED* — Install the Superdesign skill with one line: npx skills add superdesigndev/superdesign-skill
  > “npx skills add superdesigndev/superdesign-skill”
  — [g-five-claude-code-skills-with-the-install-command-for-each](https://chen.media/guides/five-claude-code-skills-with-the-install-command-for-each)
  ↳ *enables* `g21-0006`
  ↳ *part-of* `g21-0018`
  ↳ *example-of* `g21-0017`
  ↳ *example-of* `g18-0086`

- `g21-0009` *STATED* — Install Superpowers in Claude Code with two commands: /plugin marketplace add obra/superpowers-marketplace then /plugin install superpowers@superpowers-marketplace
  > “/plugin marketplace add obra/superpowers-marketplace → /plugin install superpowers@superpowers-marketplace”
  — [g-five-claude-code-skills-with-the-install-command-for-each](https://chen.media/guides/five-claude-code-skills-with-the-install-command-for-each)
  ↳ *enables* `g21-0008`
  ↳ *part-of* `g21-0018`
  ↳ *example-of* `g21-0017`
  ↳ *example-of* `g18-0160`

- `g21-0011` *STATED* — Install the Trail of Bits audit by running /plugin marketplace add trailofbits/skills and then installing the "static-analysis" plugin from it.
  > “/plugin marketplace add trailofbits/skills → install "static-analysis"”
  — [g-five-claude-code-skills-with-the-install-command-for-each](https://chen.media/guides/five-claude-code-skills-with-the-install-command-for-each)
  ↳ *enables* `g21-0010`
  ↳ *part-of* `g21-0018`
  ↳ *example-of* `g18-0160`

- `g21-0013` *STATED* — Install the Karpathy skill with: /plugin marketplace add forrestchang/andrej-karpathy-skills then /plugin install andrej-karpathy-skills@karpathy-skills
  > “/plugin marketplace add forrestchang/andrej-karpathy-skills → /plugin install andrej-karpathy-skills@karpathy-skills”
  — [g-five-claude-code-skills-with-the-install-command-for-each](https://chen.media/guides/five-claude-code-skills-with-the-install-command-for-each)
  ↳ *enables* `g21-0012`
  ↳ *part-of* `g21-0018`
  ↳ *example-of* `g18-0160`

- `g21-0015` *STATED* — Add the Playwright MCP server to Claude Code with: claude mcp add playwright npx @playwright/mcp@latest
  > “claude mcp add playwright npx @playwright/mcp@latest”
  — [g-five-claude-code-skills-with-the-install-command-for-each](https://chen.media/guides/five-claude-code-skills-with-the-install-command-for-each)
  ↳ *enables* `g21-0014`
  ↳ *part-of* `g21-0018`
  ↳ *example-of* `g21-0017`
  ↳ *part-of* `g18-0121`

- `g22-0101` *STATED* — PURGE step 1 FIND: Claude digs through years of your inbox and builds one master list of every account, subscription and login tied to you, sorted riskiest first.
  — [g-make-claude-hunt-down-every-forgotten-account-you-have](https://chen.media/guides/make-claude-hunt-down-every-forgotten-account-you-have)
  ↳ *part-of* `g22-0099`
  ↳ *leads-to* `g22-0103`

- `g22-0103` *STATED* — PURGE step 2 DELETE: Claude opens each unused account, logs in, exports your data, requests deletion and closes it, one by one.
  — [g-make-claude-hunt-down-every-forgotten-account-you-have](https://chen.media/guides/make-claude-hunt-down-every-forgotten-account-you-have)
  ↳ *part-of* `g22-0099`
  ↳ *leads-to* `g22-0106`

- `g22-0104` *STATED* — During PURGE DELETE, Claude pauses for your OK before each account.
  > “pausing for your OK”
  — [g-make-claude-hunt-down-every-forgotten-account-you-have](https://chen.media/guides/make-claude-hunt-down-every-forgotten-account-you-have)
  ↳ *qualifies* `g22-0103`
  ↳ *example-of* `g22-0278`
  ↳ *example-of* `g12-0303`

- `g22-0153` *STATED* — Meta Ads connector setup: open Claude (claude.ai or the Mac / Windows app), go to Settings, then Connectors, add a custom connector, paste the connector URL, and authorize with the Meta account that manages your ads.
  — [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)
  ↳ *part-of* `g22-0145`

- `g22-0154` *STATED* — Confirm the Meta Ads connector by starting a NEW chat and typing 'List my ad accounts'; if it names your account, you are connected.
  — [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)
  ↳ *part-of* `g22-0153`
  ↳ *example-of* `g22-0158`
  ↳ *evidence-for* `g07-0008`

- `g22-0157` *STATED* — When authorizing the Meta Ads connector, click Connect / Authorize, log in with the Facebook account that has access to your ad account, and grant the ads permissions it asks for.
  — [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)
  ↳ *part-of* `g22-0153`

- `g22-0158` *STATED* — Confirm the Meta Ads connector can see your ad account before you do anything else with it.
  — [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)
  ↳ *part-of* `g22-0153`

- `g22-0159` *STATED* — If Meta has moved the connector URL since launch, search 'Meta Ads MCP connector' or find it in Meta's Business Help Center under connectors.
  — [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)
  ↳ *qualifies* `g22-0156`

- `g23-0024` *STATED* — Step 2 of cloning Fable 5 is 'The skill-file conversion' prompt, turning what the audit found into skill files.
  — [g-clone-the-smart-model-s-brain-into-the-cheap-one](https://chen.media/guides/clone-the-smart-model-s-brain-into-the-cheap-one)
  ↳ *part-of* `g23-0012`
  ↳ *depends-on* `g23-0102`

- `g23-0104` *STATED* — Install a skill by dropping its folder into your skills directory.
  — [g-five-claude-skills-that-beat-99-of-users](https://chen.media/guides/five-claude-skills-that-beat-99-of-users)
  ↳ *depends-on* `g23-0102`
  ↳ *contrast* `g23-0105`
  ↳ *evidence-for* `g05-0311`

- `g23-0105` *STATED* — Or install a skill by asking Claude to fetch and install it for you.
  — [g-five-claude-skills-that-beat-99-of-users](https://chen.media/guides/five-claude-skills-that-beat-99-of-users)
  ↳ *depends-on* `g23-0102`
  ↳ *evidence-for* `r01-0003`

- `g23-0107` *STATED* — The skill install prompt ends by making Claude confirm the skill is active and show one example of it working.
  — [g-five-claude-skills-that-beat-99-of-users](https://chen.media/guides/five-claude-skills-that-beat-99-of-users)
  ↳ *part-of* `g23-0106`
  ↳ *example-of* `g23-0200`
  ↳ *evidence-for* `g14-0303`

- `g23-0149` *STATED* — Add each MCP plugin once, then just ask Claude in plain English and it drives the tool for you.
  > “Add each one once. Then just ask Claude in plain English and it drives the tool for you.”
  — [g-the-claude-plugins-cheat-sheet-add-once-then-just-ask](https://chen.media/guides/the-claude-plugins-cheat-sheet-add-once-then-just-ask)
  ↳ *qualifies* `g23-0148`
  ↳ *evidence-for* `g16-0014`

- `r01-0003` *CORE* — Alex's standard install for any of his skills: paste the GitHub repo link into Claude Code followed by one instruction line, e.g. 'https://github.com/alexyc9381/court-skill' + 'Install this skill, then confirm /court works.'
  > “Install any of them by pasting the repo link into Claude Code.”
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill) [r-alexyc9381](https://github.com/alexyc9381/alexyc9381) [r-court-skill](https://github.com/alexyc9381/court-skill) [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *contrast* `r01-0004` — one-link paste vs plugin marketplace

- `r01-0004` *CORE* — Each Alex Chen skill repo doubles as its own plugin marketplace: '/plugin marketplace add alexyc9381/<repo>' then '/plugin install <repo>@<repo>' (e.g. /plugin install court-skill@court-skill).
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill) [r-court-skill](https://github.com/alexyc9381/court-skill) [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *example-of* `g18-0160`

- `r01-0005` *CORE* — Manual install of an Alex Chen skill: copy the repo's skills/<name> folder into ~/.claude/skills/.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill) [r-court-skill](https://github.com/alexyc9381/court-skill) [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *leads-to* `r01-0006`
  ↳ *contrast* `r01-0004`
  ↳ *example-of* `g05-0311`

- `r01-0007` *CORE* — Alex's skill repos ship Python unit tests run with: python3 -m unittest discover -s tests
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill) [r-court-skill](https://github.com/alexyc9381/court-skill) [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *part-of* `r01-0021`

- `r01-0014` *CORE* — Alex's skills write all their output into one hidden folder in the current directory (.agency/, .court/, .hiring-panel/) and touch nothing else.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill) [r-court-skill](https://github.com/alexyc9381/court-skill) [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)

- `r01-0055` *STATED* — Install /agency by pasting into Claude Code: 'https://github.com/alexyc9381/agency-skill' followed by 'Install this skill, then run /agency setup.'
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *example-of* `r01-0003`

- `r01-0056` *STATED* — Install /agency as a plugin: '/plugin marketplace add alexyc9381/agency-skill' then '/plugin install agency-skill@agency-skill'.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *example-of* `r01-0004`

- `r01-0057` *STATED* — Install /agency manually by copying skills/agency into ~/.claude/skills/.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *example-of* `r01-0005`

- `r01-0066` *STATED* — The /agency SKILL.md description triggers when the user types /agency, wants to start or run an AI agency, wants clients for automation work, or asks for help with outreach, sales calls, proposals, building a client automation or client emails.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *example-of* `r01-0012`

- `r01-0078` *STATED* — /agency setup creates .agency/queue.md (empty list), .agency/outbox/, .agency/clients/ and .agency/support/, then shows the five commands in one line each.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0042`

- `r01-0087` *STATED* — If a Gmail or other email connector is available, /agency offers to put the emails in your Drafts.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *contrast* `r01-0086` — connector drafts vs mail-merge CSV
  ↳ *qualifies* `r01-0088`
  ↳ *contrast* `r01-0102` — connector used for both drafts and reading
  ↳ *depends-on* `g07-0005`

- `r01-0102` *STATED* — The /agency support agent reads new client emails from an email connector if available, or from files dropped in .agency/support/inbox/.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *part-of* `r01-0047`
  ↳ *depends-on* `g07-0005`

- `r01-0142` *STATED* — /hiring-panel writes .hiring-panel/<date>-<name>/ with PANEL.md (the seven verdicts and the numbered mistakes) and RESUME-IMPROVED.md (the new resume), and touches no other files.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *example-of* `r01-0014`

- `r01-0145` *STATED* — Install /hiring-panel by pasting 'https://github.com/alexyc9381/hiring-panel-skill' + 'Install this skill, then confirm /hiring-panel works.' into Claude Code.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *example-of* `r01-0003`

- `r01-0146` *STATED* — Install /hiring-panel as a plugin: '/plugin marketplace add alexyc9381/hiring-panel-skill' then '/plugin install hiring-panel-skill@hiring-panel-skill'.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *example-of* `r01-0004`

- `r01-0172` *STATED* — Install /court by pasting 'https://github.com/alexyc9381/court-skill' + 'Install this skill, then confirm /court works.' into Claude.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0003`

- `r01-0173` *STATED* — Install /court by hand: 'git clone https://github.com/alexyc9381/court-skill' then 'cp -r court-skill/skills/court ~/.claude/skills/'.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0005`

- `r01-0174` *STATED* — Install /court with the skills CLI: 'npx skills add alexyc9381/court-skill'.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *contrast* `r01-0173` — skills CLI vs manual clone
  ↳ *example-of* `r04-0005`

- `r01-0175` *STATED* — Install /court as a plugin: '/plugin marketplace add alexyc9381/court-skill' then '/plugin install court-skill@court-skill'.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0004`

- `r01-0191` *STATED* — Uninstall /court with: rm -rf ~/.claude/skills/court
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *contrast* `r01-0173`

- `r01-0204` *STATED* — The /court description triggers when the user wants honest pushback instead of agreement, says Claude just agrees with everything, asks 'is this a good idea', wants an idea, plan, pitch or claim stress-tested, or says 'court' or 'put it on trial'.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0012`
  ↳ *because* `r01-0160`

- `r02-0031` *STATED* — Install /hunter by pasting into Claude Code: `https://github.com/alexyc9381/hunter-skill` followed by `Install this skill, then confirm /hunter works.`
  > “https://github.com/alexyc9381/hunter-skill
Install this skill, then confirm /hunter works.”
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *example-of* `r02-0309`
  ↳ *example-of* `r01-0003`

- `r02-0032` *STATED* — Install /hunter as a plugin with `/plugin marketplace add alexyc9381/hunter-skill` then `/plugin install hunter-skill@hunter-skill`.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *example-of* `r02-0310`
  ↳ *example-of* `r01-0004`

- `r02-0033` *STATED* — Install /hunter manually by copying the repo's `skills/hunter` folder into `~/.claude/skills/`.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *contrast* `r02-0032`
  ↳ *example-of* `r01-0005`

- `r02-0046` *STATED* — The hunter-skill repo's tests run with `python3 -m unittest discover -s tests`.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *example-of* `r02-0316`

- `r02-0050` *STATED* — The /hunter SKILL.md description tells Claude to use it when the user types /hunter, wants Claude to find jobs, score jobs against their resume, tailor a resume and cover letter per job, or prepare job applications.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *defines* `r02-0001`

- `r02-0138` *STATED* — Install /launch by pasting into Claude: `https://github.com/alexyc9381/launch-skill` followed by `Install this skill, then confirm /launch works.`
  > “https://github.com/alexyc9381/launch-skill
Install this skill, then confirm /launch works.”
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0309`
  ↳ *example-of* `r01-0003`

- `r02-0139` *STATED* — Install /launch manually with `git clone https://github.com/alexyc9381/launch-skill` then `cp -r launch-skill/skills/launch ~/.claude/skills/`.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *contrast* `r02-0140`
  ↳ *example-of* `r01-0005`

- `r02-0140` *STATED* — Install /launch with the skills CLI: `npx skills add alexyc9381/launch-skill`.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *contrast* `r02-0141`
  ↳ *example-of* `r04-0005`

- `r02-0141` *STATED* — Install /launch as a plugin with `/plugin marketplace add alexyc9381/launch-skill` then `/plugin install launch-skill@launch-skill`.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0310`
  ↳ *example-of* `r01-0004`

- `r02-0159` *STATED* — The launch-skill repo's tests run with `python3 -m unittest discover -s tests`.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *example-of* `r02-0316`

- `r02-0161` *STATED* — Uninstall /launch with `rm -rf ~/.claude/skills/launch`.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *contrast* `r02-0139`

- `r02-0164` *STATED* — The /launch SKILL.md description fires when the user is about to launch, ship, deploy or go live, asks "is my app ready" or "can I ship this", wants a pre-launch or production-readiness check, says Claude told them it's done but they aren't sure, or says "launch" or "go/no-go".
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *defines* `r02-0118`

- `r02-0175` *STATED* — If /launch fired on its own (the user never asked for a launch check), it asks once first and offers `--quick`.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0164`
  ↳ *depends-on* `r02-0145`

- `r02-0309` *CORE* — Alex's standard skill install is to paste the GitHub repo URL into Claude Code with the line "Install this skill, then confirm /<name> works."
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill) [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *contrast* `r02-0310`
  ↳ *evidence-for* `r01-0003`

- `r02-0310` *CORE* — Alex's repos double as plugin marketplaces: `/plugin marketplace add alexyc9381/<repo>` then `/plugin install <repo>@<repo>`.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill) [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *evidence-for* `r01-0004`
  ↳ *example-of* `g05-0310`

- `r02-0316` *INFERRED* — Alex ships Python unittest suites with his skill repos (`python3 -m unittest discover -s tests`).
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill) [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0155`
  ↳ *evidence-for* `r01-0007`

- `r03-0019` *STATED* — Install /learn by pasting into Claude: 'https://github.com/alexyc9381/learn-skill' followed by 'Install this skill, then run /learn setup in this project.'
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *example-of* `r03-0024`
  ↳ *leads-to* `r03-0025`
  ↳ *example-of* `r01-0003`

- `r03-0020` *STATED* — Manual /learn install in Claude Code: 'git clone https://github.com/alexyc9381/learn-skill' then 'cp -r learn-skill/skills/learn ~/.claude/skills/'.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *example-of* `r03-0024`
  ↳ *example-of* `r01-0005`

- `r03-0021` *STATED* — Install /learn with the skills CLI: 'npx skills add alexyc9381/learn-skill'.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *example-of* `r03-0024`
  ↳ *example-of* `r04-0005`

- `r03-0022` *STATED* — Install /learn as a plugin: '/plugin marketplace add alexyc9381/learn-skill' then '/plugin install learn-skill@learn-skill'.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *example-of* `r03-0024`
  ↳ *example-of* `r01-0004`

- `r03-0052` *STATED* — Both learn-skill and linkedin-roast-skill ship unit tests, run with 'python3 -m unittest discover -s tests'.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill) [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *part-of* `r03-0044`
  ↳ *part-of* `r03-0134`
  ↳ *evidence-for* `r01-0007`

- `r03-0057` *STATED* — Uninstall the /learn skill with 'rm -rf ~/.claude/skills/learn'.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *contrast* `r03-0020`

- `r03-0139` *STATED* — Install /linkedin-roast by pasting into Claude Code: 'https://github.com/alexyc9381/linkedin-roast-skill' followed by 'Install this skill, then confirm /linkedin-roast works.'
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0024`
  ↳ *example-of* `r01-0003`

- `r03-0140` *STATED* — Install /linkedin-roast as a plugin: '/plugin marketplace add alexyc9381/linkedin-roast-skill' then '/plugin install linkedin-roast-skill@linkedin-roast-skill'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0024`
  ↳ *example-of* `r01-0004`

- `r03-0141` *STATED* — Manual /linkedin-roast install: copy the folder into your skills folder with 'cp -r skills/linkedin-roast ~/.claude/skills/'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *example-of* `r03-0024`
  ↳ *example-of* `r01-0005`

- `r03-0145` *STATED* — Put the profile PDF in the folder you opened Claude Code in, then run '/linkedin-roast my-profile.pdf'.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *leads-to* `r03-0147`

- `r04-0004` *CORE* — Alex's universal install route for every skill: paste the repo URL into Claude followed by 'Install this skill, then confirm /<name> works.' and let Claude do the install.
  > “Paste this into Claude: https://github.com/alexyc9381/shark-skill Install this skill, then confirm /shark works.”
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill) [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill) [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0005`
  ↳ *evidence-for* `r01-0003`

- `r04-0005` *CORE* — Alex's skill repos offer four install routes: paste the URL into Claude; git clone + cp -r <repo>/skills/<name> ~/.claude/skills/; the skills CLI (npx skills add alexyc9381/<repo>); or as a plugin (/plugin marketplace add alexyc9381/<repo> then /plugin install <repo>@<repo>).
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill) [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `g21-0017`

- `r04-0006` *CORE* — Alex's SKILL.md frontmatter pattern: name, a long description ending in a 'Use when the user ...' trigger list, argument-hint, license: MIT, and metadata with author "Alex Chen (@nocodealex)", homepage https://chen.media, source (the GitHub URL) and version "1.0.0".
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill) [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill) [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *evidence-for* `r01-0012`
  ↳ *example-of* `g15-0045`

- `r04-0009` *CORE* — Alex's interactive skills put all bookkeeping in a Python helper inside the skill folder (mentor.py, shark.py), called as python3 "${CLAUDE_SKILL_DIR}/<tool>.py" <command>, so state and rules live in code rather than in Claude's memory.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill) [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r01-0021`

- `r04-0054` *STATED* — The mentor SKILL.md triggers when the user wants to learn to code while building with Claude, says they are a beginner or a student, says vibe coding is teaching them nothing, asks Claude to teach instead of just doing it, or says 'mentor'.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *part-of* `r04-0006`
  ↳ *part-of* `r04-0023`

- `r04-0061` *STATED* — If the /mentor arguments are status, recap or stop, Claude runs that command, shows the result, and stops.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *example-of* `r04-0007`
  ↳ *generalizes* `r04-0046`

- `r04-0070` *STATED* — /mentor records each answer word for word: MENTOR answer <checkpoint> --text "<exactly what they typed>".
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *depends-on* `r04-0071`
  ↳ *enables* `r04-0078`

- `r04-0077` *STATED* — If MENTOR answer reports the answer is too short, Claude asks the learner to say a bit more, in their words; mentor.py enforces a minimum answer length.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *qualifies* `r04-0070`

- `r04-0078` *STATED* — /mentor Step 3: MENTOR unlock refuses until all three answers exist.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *part-of* `r04-0062`
  ↳ *depends-on* `r04-0058`

- `r04-0084` *STATED* — /mentor picks the two or three concepts a feature taught (e.g. 'local storage vs a database', 'foreign keys') and logs them: MENTOR explain --text "<their explanation, word for word>" --concept "..." --concept "...".
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *part-of* `r04-0062`
  ↳ *leads-to* `r04-0036`

- `r04-0157` *STATED* — The night-crew skill triggers when the user wants Claude to work overnight, while they sleep, on a schedule, 'a night shift', 'a night crew', or to wake up to finished work; argument-hint "[setup | morning]".
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0006`
  ↳ *part-of* `r04-0087`

- `r04-0159` *STATED* — The night-crew skill routes on $ARGUMENTS: blank, 'setup', or anything about setting it up runs Setup; 'morning', 'what did the crew do' or 'briefing' runs Morning.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *example-of* `r04-0007`
  ↳ *enables* `r04-0107`

- `r04-0227` *STATED* — skills/shark/shark.py does the /shark bookkeeping: it opens the session, writes one brief per sub-agent, checks every output exists, counts the deals and renders the board.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0009`
  ↳ *enables* `r04-0228`

- `r04-0241` *STATED* — The shark skill triggers when the user wants honest feedback on a business, product or side-hustle idea, says Claude thinks every idea is great, asks 'would investors fund this', wants to practice a pitch, or says 'pitch' or 'shark tank'; argument-hint "[--investors N] [--seed S] <the business idea>".
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0006`
  ↳ *part-of* `r04-0206`

- `r04-0243` *STATED* — If /shark's $ARGUMENTS is blank, or still reads like a placeholder, the skill takes the idea from the conversation.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0007`

- `r04-0247` *STATED* — If the shark skill fired on its own (auto-triggered rather than typed), it asks the user once before spending the sub-agent calls.
  > “If this skill fired on its own, ask once first.”
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *qualifies* `r04-0246`
  ↳ *evidence-for* `r02-0175`

- `y01-0045` *STATED* — Install a Codex plugin from Plugins: open the plugin's details, install it, and connect it to your account when prompted.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *part-of* `y01-0043`

- `y01-0047` *STATED* — In Codex, describe what you need in normal language or type the @ sign to choose a particular plugin.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *part-of* `y01-0043`

- `y01-0068` *STATED* — You can ask Codex to create a skill from a process you've described; the built-in skill creator helps do this.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *enables* `y01-0065`

- `y01-0069` *STATED* — In Codex, type a dollar sign ($) in the message box to choose a saved skill directly from a list.
  — [lq-pBM_8vF8](https://youtu.be/lq-pBM_8vF8)
  ↳ *contrast* `g15-0045`
  ↳ *part-of* `y01-0065`

- `y01-0083` *STATED* — Prerequisite for ai-agency-claude: download and install Claude Code first.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)

- `y01-0085` *STATED* — Install ai-agency-claude: on the GitHub repo scroll to the one-command install, copy it, paste it into the Claude Code chat window and hit enter - the main agency system is then running.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *depends-on* `y01-0083`
  ↳ *part-of* `y01-0079`

- `y01-0087` *STATED* — After the core install, install the ai-agency-claude marketing, sales, legal and SEO teams.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *leads-to* `y01-0085`

- `y01-0088` *STATED* — Type /agency stack (spoken 'slash agency stack') to see every installed ai-agency-claude department ready to go.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *depends-on* `y01-0087`

- `y01-0169` *STATED* — Set up Claude connectors in Settings; Alex starts by connecting both Gmail and Google Drive.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *evidence-for* `g07-0006`
  ↳ *part-of* `y01-0168`

- `y01-0177` *STATED* — Upload a custom skill in the Claude app: Settings -> Customize -> Skills tab -> upload the skill as a zip file.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *evidence-for* `g05-0304`
  ↳ *part-of* `y01-0176`

- `y01-0194` *STATED* — Alex's spend guard in the demo: state a maximum budget in the request - he told the fal skill 'maximum $1' for the clip.
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *qualifies* `y01-0193` — the mitigation actually shown

- `y01-0196` *STATED* — fal.ai setup step 1: search 'Fal AI' on Google, open fal.ai and create an account.
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *leads-to* `y01-0198`
  ↳ *part-of* `y01-0223`

- `y01-0198` *STATED* — Get a fal.ai API key: Settings -> API keys -> add key -> create key, then copy the key and keep it safe.
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *part-of* `y01-0223`
  ↳ *leads-to* `y01-0199`

- `y01-0199` *STATED* — Download Alex's fal video skill from the video description (via https://school.chen.media/fal) and upload it into Claude - there is no additional code to write.
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *leads-to* `y01-0201`
  ↳ *example-of* `y01-0225`
  ↳ *depends-on* `y01-0177` — upload via Settings -> Customize -> Skills

- `y01-0201` *STATED* — Run Alex's fal skill by typing /fal/video (spoken 'slash Fal slash video').
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *leads-to* `y01-0202`

- `y01-0202` *STATED* — The fal skill first asks what you're making: a clip from scratch, a clip from a picture, or a picture first.
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *leads-to* `y01-0204`

- `y01-0206` *STATED* — The fal skill asks how long the video should be and its dimensions - e.g. for iPhones (vertical) or computers (widescreen).
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)

- `y01-0216` *STATED* — The fal skill can run the exact same prompt through multiple AI video models at the same time to compare outputs.
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *part-of* `y01-0184`

- `y01-0223` *STATED* — Alex's fal workflow in three steps: 1) set up (fal.ai account, API key, load the skill), 2) generate your video, 3) review the results.
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *generalizes* `y01-0199`

- `y02-0030` *STATED* — To make a video with Claude Motion you type /motion and explain the video you want to create.
  > “just type slash motion and explain the video you want to create”
  — [HWioULsQJWM](https://youtu.be/HWioULsQJWM)
  ↳ *part-of* `y02-0029`

- `y02-0174` *STATED* — With the Logo Design Skill you describe your business and Claude designs the logo.
  — [J8g3EZwZx20](https://youtu.be/J8g3EZwZx20)
  ↳ *evidence-for* `g09-0180`
  ↳ *part-of* `y02-0172`

- `y03-0086` *INFERRED* — Reusable pattern from Straight Talk: turn a measurement study into a skill by converting each finding into a never-break rule, then invoke the skill before every task of that kind.
  — [mw5TnnOoHek](https://youtu.be/mw5TnnOoHek)

- `y03-0102` *STATED* — With Find Skills you tell Claude what you need and it hunts down the best skills for that exact job.
  — [wfwnTNtnomk](https://youtu.be/wfwnTNtnomk) [1j9mmXDW8Qw](https://youtu.be/1j9mmXDW8Qw)
  ↳ *evidence-for* `g10-0258`
  ↳ *part-of* `y03-0100`
  ↳ *leads-to* `y03-0105`

- `y03-0113` *STATED* — In Open Design you type what you want and it builds the website, app screen or slide deck right in front of you.
  — [NrJa3MCde-I](https://youtu.be/NrJa3MCde-I) [vdLceKphMoQ](https://youtu.be/vdLceKphMoQ)
  ↳ *evidence-for* `g10-0213`
  ↳ *part-of* `y03-0110`

- `y03-0118` *STATED* — In Dyad you describe the app you want and Claude builds it right on your computer.
  — [cxLfDm8_Yx4](https://youtu.be/cxLfDm8_Yx4) [a8nVKYxwcjo](https://youtu.be/a8nVKYxwcjo) [udcHbDvy7o4](https://youtu.be/udcHbDvy7o4)
  ↳ *evidence-for* `g10-0236`
  ↳ *part-of* `y03-0116`

- `y03-0124` *STATED* — In Instatic you describe the page you want and Claude builds it right there in the editor.
  — [N8BCMjq3wPE](https://youtu.be/N8BCMjq3wPE) [23JOjnkdikY](https://youtu.be/23JOjnkdikY)
  ↳ *evidence-for* `g11-0012`
  ↳ *part-of* `y03-0122`

- `y04-0092` *STATED* — Setup for the single-file AI hub: download the one file and open it in your browser.
  > “open it in your browser”
  — [OD7UTDYiTYI](https://youtu.be/OD7UTDYiTYI) [voaf6bOrHgc](https://youtu.be/voaf6bOrHgc)
  ↳ *part-of* `y04-0091`

- `y04-0107` *STATED* — Install the split skill by dropping it inside Claude Code or Codex; it then automatically routes everything to Fable 5 and Astro 6.
  > “Just drop this free skill inside your Claude Code or Codex and it'll automatically route everything to Fable 5 and Astro 6.”
  — [_gYzRT-j_ls](https://youtu.be/_gYzRT-j_ls)
  ↳ *part-of* `y04-0106`

- `y04-0142` *STATED* — Install Agent Reach by running one command in Claude (transcribed 'plot') or ChatGPT, which then gets full internet access.
  > “All you do is run this one command in Claude or ChatGPT and it gets full internet access.”
  — [VRRK9REgdaA](https://youtu.be/VRRK9REgdaA)
  ↳ *contradicts* `g14-0105` — Agent Reach: install 'in Claude or ChatGPT' (video) vs 'an ordinary ChatGPT conversation cannot run terminal-based tools like Agent Reach' (guide)
  ↳ *part-of* `y04-0140`

### number

- `g01-0099` *STATED* — A Claudemy course is about 12 audio lessons of around two minutes each, roughly 25 minutes of audio, as MP3 files.
  — [g-turn-any-topic-into-a-12-lesson-audio-course-with-claude](https://chen.media/guides/turn-any-topic-into-a-12-lesson-audio-course-with-claude)
  ↳ *evidence-for* `g01-0098`

- `g01-0166` *STATED* — Matt Pocock's skills pack has 27 skills and is past 290,000 stars.
  — [g-grill-me-make-claude-interview-you-before-it-writes-a-line-of-code](https://chen.media/guides/grill-me-make-claude-interview-you-before-it-writes-a-line-of-code)
  ↳ *qualifies* `g01-0165`

- `g01-0182` *STATED* — Scientific Agent Skills gives Claude access to more than 100 scientific and financial databases, 80 of them documented in its Database Lookup skill.
  — [g-give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills](https://chen.media/guides/give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills)
  ↳ *part-of* `g01-0177`

- `g02-0036` *STATED* — Context Mode has over 29,000 stars on GitHub.
  — [g-stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode)
  ↳ *evidence-for* `g02-0031`
  ↳ *example-of* `g02-0235`

- `g02-0066` *STATED* — AirLLM is Apache-2.0 licensed and has over 38,000 stars on GitHub.
  — [g-run-a-235-billion-parameter-ai-model-on-a-3gb-graphics-card-set-up-the-free-airl](https://chen.media/guides/run-a-235-billion-parameter-ai-model-on-a-3gb-graphics-card-set-up-the-free-airl) [g-run-a-2-8-trillion-parameter-ai-model-on-your-gaming-graphics-card-set-up-the-fr](https://chen.media/guides/run-a-2-8-trillion-parameter-ai-model-on-your-gaming-graphics-card-set-up-the-fr)
  ↳ *evidence-for* `g02-0062`
  ↳ *example-of* `g02-0235`
  ↳ *contradicts* `g07-0227` — AirLLM stars: 'over 38,000' (235B/2.8T guides) vs 'over 35,000' (70B guide)

- `g02-0102` *STATED* — santifer open-sourced career-ops after his search, and it is past 74,000 stars on GitHub.
  — [g-know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a](https://chen.media/guides/know-if-a-job-is-worth-applying-before-you-start-career-ops-scores-it-out-of-5-a) [g-200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi](https://chen.media/guides/200-applications-zero-replies-career-ops-shows-which-jobs-were-never-worth-sendi)
  ↳ *evidence-for* `g02-0098`
  ↳ *example-of* `g02-0235`
  ↳ *evidence-for* `g03-0064`

- `g02-0163` *STATED* — github-triage is one skill in Trail of Bits' open-source skills repo for Claude Code, which has 7,500+ stars across the repo.
  — [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say)
  ↳ *example-of* `g02-0235`

- `g02-0224` *STATED* — AI Homepage ranks the sites in your history and opens up to 8 of them per build, in your signed-in browser.
  — [g-ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper](https://chen.media/guides/ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper)
  ↳ *qualifies* `g02-0222`

- `g02-0227` *STATED* — AI Homepage rebuilds automatically once your page is older than 6, 12, 24 or 48 hours.
  — [g-ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper](https://chen.media/guides/ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper)
  ↳ *qualifies* `g02-0223`

- `g03-0013` *STATED* — GitHub star counts he quotes for featured repos: career-ops past 74,000, Diagram Design past 54,000, Anthropic's security skills past 7,500, Minutes past 1,500.
  — [g-career-ops-let-claude-score-every-job-against-your-cv-before-you-apply](https://chen.media/guides/career-ops-let-claude-score-every-job-against-your-cv-before-you-apply) [g-diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe](https://chen.media/guides/diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe) [g-hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills](https://chen.media/guides/hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills) [g-minutes-the-free-open-source-meeting-recorder-that-claude-can-search](https://chen.media/guides/minutes-the-free-open-source-meeting-recorder-that-claude-can-search)
  ↳ *evidence-for* `g02-0235`

- `g03-0038` *STATED* — In NVIDIA's research set of 31,132 skills, 26.1% had a vulnerability.
  — [g-skillspector-scan-any-claude-skill-for-malware-before-you-install-it](https://chen.media/guides/skillspector-scan-any-claude-skill-for-malware-before-you-install-it)
  ↳ *evidence-for* `g03-0036`

- `g03-0039` *STATED* — In NVIDIA's research set of 31,132 skills, 5.2% showed likely malicious intent.
  — [g-skillspector-scan-any-claude-skill-for-malware-before-you-install-it](https://chen.media/guides/skillspector-scan-any-claude-skill-for-malware-before-you-install-it)
  ↳ *evidence-for* `g03-0036`

- `g03-0040` *STATED* — SkillSpector checks every file against 71 known attack patterns grouped in 17 categories.
  — [g-skillspector-scan-any-claude-skill-for-malware-before-you-install-it](https://chen.media/guides/skillspector-scan-any-claude-skill-for-malware-before-you-install-it)
  ↳ *part-of* `g03-0035`

- `g03-0064` *STATED* — career-ops was open-sourced and is past 74,000 stars on GitHub.
  — [g-career-ops-let-claude-score-every-job-against-your-cv-before-you-apply](https://chen.media/guides/career-ops-let-claude-score-every-job-against-your-cv-before-you-apply)
  ↳ *part-of* `g03-0013`
  ↳ *evidence-for* `g03-0059`

- `g03-0092` *STATED* — Diagram Design is past 54,000 stars on GitHub.
  — [g-diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe](https://chen.media/guides/diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe)
  ↳ *part-of* `g03-0013`
  ↳ *evidence-for* `g03-0089`

- `g03-0093` *STATED* — Diagram Design supports 45 diagram types, including architecture, flowchart, sequence, state machine, timeline, org chart, quadrant, swimlane, Gantt, Venn, pyramid, Sankey, Kanban and user journey.
  — [g-diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe](https://chen.media/guides/diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe)
  ↳ *part-of* `g03-0089`

- `g03-0137` *STATED* — His code intelligence table covers 12 language plugins: TypeScript/JavaScript, Python, Go, Rust, Java, C/C++, C#, Ruby, PHP, Swift, Kotlin and Lua.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *part-of* `g03-0138`

- `g03-0143` *STATED* — Minutes is MIT licensed and past 1,500 stars on GitHub.
  — [g-minutes-the-free-open-source-meeting-recorder-that-claude-can-search](https://chen.media/guides/minutes-the-free-open-source-meeting-recorder-that-claude-can-search)
  ↳ *part-of* `g03-0013`
  ↳ *evidence-for* `g03-0151`

- `g03-0146` *STATED* — Minutes includes an MCP server with 34 tools that lets Claude search every meeting at once and answer questions that span several calls.
  — [g-minutes-the-free-open-source-meeting-recorder-that-claude-can-search](https://chen.media/guides/minutes-the-free-open-source-meeting-recorder-that-claude-can-search)
  ↳ *enables* `g03-0142`
  ↳ *example-of* `g16-0014`

- `g03-0147` *STATED* — Minutes includes a Claude Code plugin with 23 skills: prep before a call, capture, live help, debrief after, and memory workflows.
  — [g-minutes-the-free-open-source-meeting-recorder-that-claude-can-search](https://chen.media/guides/minutes-the-free-open-source-meeting-recorder-that-claude-can-search)
  ↳ *part-of* `g03-0140`

- `g03-0148` *STATED* — Minutes ships a CLI with 58 commands.
  — [g-minutes-the-free-open-source-meeting-recorder-that-claude-can-search](https://chen.media/guides/minutes-the-free-open-source-meeting-recorder-that-claude-can-search)
  ↳ *part-of* `g03-0140`

- `g03-0177` *STATED* — Anthropic's security skills repo is past 7,500 stars on GitHub.
  — [g-hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills](https://chen.media/guides/hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills)
  ↳ *part-of* `g03-0013`
  ↳ *evidence-for* `g03-0176`

- `g04-0197` *STATED* — Installing the Vibewise plugin takes about 2 minutes (section 'Install it (about 2 minutes)', body locked).
  — [g-ai-coders-scored-17-lower-on-a-quiz-make-claude-teach-you-with-the-free-vibewise](https://chen.media/guides/ai-coders-scored-17-lower-on-a-quiz-make-claude-teach-you-with-the-free-vibewise)
  ↳ *part-of* `g04-0200`
  ↳ *evidence-for* `g05-0028`

- `g05-0037` *STATED* — In the Chrome Relay author's test, a 7-step form took 2.5 seconds.
  — [g-let-claude-use-your-real-chrome-signed-in-in-background-tabs](https://chen.media/guides/let-claude-use-your-real-chrome-signed-in-in-background-tabs)
  ↳ *evidence-for* `g05-0036`
  ↳ *part-of* `g02-0185`

- `g05-0038` *STATED* — Replayed from a saved flow, the same 7-step form took 1.2 seconds in Chrome Relay.
  — [g-let-claude-use-your-real-chrome-signed-in-in-background-tabs](https://chen.media/guides/let-claude-use-your-real-chrome-signed-in-in-background-tabs)
  ↳ *contrast* `g05-0037` — saved-flow replay halves the time
  ↳ *part-of* `g02-0185`

- `g06-0014` *STATED* — The /iq skill reads up to 320 of your messages.
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *part-of* `g06-0012`

- `g06-0054` *STATED* — The first run of ollama run openbmb/minicpm-v4.7 downloads about 22 GB (the 35B-A3B default), so check your free disk space before you press Enter.
  — [g-run-minicpm-v-4-7-a-free-35b-ai-on-your-laptop-or-iphone](https://chen.media/guides/run-minicpm-v-4-7-a-free-35b-ai-on-your-laptop-or-iphone)
  ↳ *qualifies* `g06-0053`

- `g07-0003` *STATED* — Superhuman Mail costs about $30 a month and has no free plan.
  — [g-sort-your-inbox-with-claude-instead-of-superhuman](https://chen.media/guides/sort-your-inbox-with-claude-instead-of-superhuman)
  ↳ *evidence-for* `g07-0012`

- `g07-0025` *STATED* — There are over a million agent skills out there now, and nobody can search that by hand.
  — [g-let-claude-find-and-install-the-right-skill-for-any-job](https://chen.media/guides/let-claude-find-and-install-the-right-skill-for-any-job)
  ↳ *because* `g07-0024` — too many skills to search by hand
  ↳ *contradicts* `g23-0099` — Skill count: 'over a million agent skills' vs 'over 50,000 skills'
  ↳ *evidence-for* `g10-0256`

- `g07-0033` *STATED* — Find Skills is the #1 skill on skills.sh, with 3.8 million installs.
  — [g-let-claude-find-and-install-the-right-skill-for-any-job](https://chen.media/guides/let-claude-find-and-install-the-right-skill-for-any-job)
  ↳ *evidence-for* `g07-0023`
  ↳ *contradicts* `g10-0248` — Find Skills installs: 3.8 million (find-and-install guide) vs 3.6 million (most-installed guide)
  ↳ *contradicts* `y03-0101` — Find Skills installs: 3.8 million (guide) vs 3.6 million (short video)

- `g07-0046` *STATED* — REA is free and open source (MIT), with over 100,000 GitHub stars.
  — [g-see-how-an-apps-feature-works-with-claude-code-and-rea-free](https://chen.media/guides/see-how-an-apps-feature-works-with-claude-code-and-rea-free)
  ↳ *part-of* `g07-0038`
  ↳ *contrast* `g07-0034` — both MIT, very different scale (100K stars vs 3.8M installs)

- `g07-0227` *STATED* — AirLLM is Apache-2.0 licensed and has over 35,000 stars on GitHub.
  — [g-run-a-70b-ai-model-on-a-4gb-graphics-card-set-up-the-free-airllm-library](https://chen.media/guides/run-a-70b-ai-model-on-a-4gb-graphics-card-set-up-the-free-airllm-library)
  ↳ *part-of* `g07-0224`

- `g08-0005` *STATED* — Installing the Vibewise plugin into Claude Code takes about 2 minutes (guide section 'Install it (about 2 minutes)', steps locked).
  — [g-vibe-code-and-still-learn-set-up-the-free-vibewise-plugin-for-claude-code](https://chen.media/guides/vibe-code-and-still-learn-set-up-the-free-vibewise-plugin-for-claude-code)
  ↳ *part-of* `g08-0001`
  ↳ *evidence-for* `g05-0028`

- `g08-0046` *STATED* — Photoshop, Premiere Pro and After Effects, each on its own Adobe plan, add up to $68.97 a month.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *leads-to* `g08-0049` — the bill is why you'd swap

- `g08-0047` *STATED* — Adobe sells Photoshop, Premiere Pro and After Effects as separate subscriptions at about $22.99 a month each, according to third-party price trackers in mid-2026.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *evidence-for* `g08-0046`
  ↳ *evidence-for* `g10-0162`

- `g08-0063` *STATED* — FilmCraft's makers estimate it is about half to 60% ready for real work.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *qualifies* `g08-0062`
  ↳ *evidence-for* `g08-0058`

- `g08-0074` *STATED* — Setting up the /heist skill takes about 2 minutes.
  — [g-give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes](https://chen.media/guides/give-claude-a-heist-crew-that-hacks-your-app-before-a-real-hacker-does-set-up-heist-in-2-minutes)
  ↳ *part-of* `g08-0073`
  ↳ *example-of* `g08-0254`

- `g08-0104` *STATED* — The Agency had 158,347 stars on GitHub when Alex's guide was written (Oct 8 2026).
  — [g-run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents](https://chen.media/guides/run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents)
  ↳ *evidence-for* `g08-0089` — popularity
  ↳ *contradicts* `g18-0271` — The Agency stars: 158,347 (Oct 8 2026) vs 137.4k (seven-repos guide)
  ↳ *contradicts* `y02-0033` — The Agency stars: 158,347 vs 'over 124,000' (short video)

- `g08-0178` *STATED* — Setting up the /jester skill takes about 2 minutes.
  — [g-give-claude-a-jester-that-tells-you-the-brutal-truth-set-up-jester-in-2-minutes](https://chen.media/guides/give-claude-a-jester-that-tells-you-the-brutal-truth-set-up-jester-in-2-minutes)
  ↳ *part-of* `g08-0177`
  ↳ *example-of* `g08-0254`

- `g08-0192` *STATED* — Setting up the /bouncer skill takes about 2 minutes.
  — [g-stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes](https://chen.media/guides/stop-claude-code-from-changing-things-you-never-asked-for-set-up-the-bouncer-skill-in-2-minutes)
  ↳ *part-of* `g08-0191`
  ↳ *example-of* `g08-0254`

- `g08-0238` *STATED* — Setting up the /trojan detector takes about 2 minutes.
  — [g-stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes](https://chen.media/guides/stop-hidden-orders-in-your-files-from-tricking-claude-set-up-the-free-trojan-detector-in-2-minutes)
  ↳ *part-of* `g08-0237`
  ↳ *example-of* `g08-0254`

- `g09-0179` *STATED* — The logo design skill is MIT-licensed and passed 1,500 GitHub stars in its first week.
  — [g-free-claude-logo-design-skill](https://chen.media/guides/free-claude-logo-design-skill)
  ↳ *qualifies* `g09-0177`
  ↳ *example-of* `g09-0252`
  ↳ *evidence-for* `g09-0251`

- `g09-0196` *STATED* — MiroFish passed 75,000 stars on GitHub in ten months.
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)
  ↳ *evidence-for* `g09-0195`
  ↳ *evidence-for* `g09-0251`

- `g09-0233` *STATED* — Coucou passed 3,000 stars on GitHub in its first week.
  — [g-coucou-free-notch-pet-that-watches-claude-code](https://chen.media/guides/coucou-free-notch-pet-that-watches-claude-code)
  ↳ *evidence-for* `g09-0232`
  ↳ *evidence-for* `g09-0251`

- `g10-0115` *STATED* — Alex Chen's 14 AI sites guide contains 7 prompts to copy and 5 numbered steps.
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)
  ↳ *part-of* `g10-0114`

- `g10-0155` *STATED* — Alex Chen's Photon Studio guide contains 9 numbered steps.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *part-of* `g10-0152`

- `g10-0162` *STATED* — Photoshop costs $22.99 a month on Adobe's annual plan, whether you open it that month or not.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *evidence-for* `g10-0152` — price saved
  ↳ *evidence-for* `g10-0267`

- `g10-0201` *STATED* — Open Design has passed 99,000 stars on GitHub.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *evidence-for* `g10-0198`

- `g10-0203` *STATED* — Alex Chen's Open Design guide contains 7 prompts to copy and 9 numbered steps.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *part-of* `g10-0198`

- `g10-0217` *STATED* — Open Design slide decks: 15 deck templates and 36 themes, exported to PowerPoint, PDF or HTML.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *part-of* `g10-0213`
  ↳ *part-of* `g10-0198`

- `g10-0219` *STATED* — Open Design ships 93 prompt templates for marketing images.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *part-of* `g10-0213`

- `g10-0221` *STATED* — Open Design ships 151 design systems from real brands, including Apple, Nike, Airbnb, Stripe and Spotify.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *enables* `g10-0213`

- `g10-0225` *STATED* — Alex Chen's Dyad guide contains 1 prompt to copy and 17 numbered steps.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *part-of* `g10-0223`

- `g10-0237` *STATED* — Dyad has passed 21,000 stars on GitHub.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)
  ↳ *evidence-for* `g10-0223`

- `g10-0248` *STATED* — Find Skills is the most installed skill of all time, at 3.6 million installs.
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)
  ↳ *evidence-for* `g10-0247`
  ↳ *evidence-for* `g10-0257`

- `g10-0249` *STATED* — Alex Chen's Find Skills guide contains 2 prompts to copy and 4 numbered steps.
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)
  ↳ *part-of* `g10-0247`

- `g10-0256` *STATED* — There are 1,499,600 agent skills on the skills.sh leaderboard.
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)
  ↳ *qualifies* `g10-0257`
  ↳ *enables* `g10-0260` — leaderboard is what it searches

- `g10-0261` *STATED* — Find Skills prefers skills with 1K+ installs and is wary of anything under 100, so a skill with 12 installs never makes the list.
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)
  ↳ *part-of* `g10-0252`
  ↳ *evidence-for* `g10-0266`

- `g10-0263` *STATED* — Find Skills treats a skill from a repo with under 100 GitHub stars with suspicion.
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)
  ↳ *part-of* `g10-0252`
  ↳ *evidence-for* `g10-0266`

- `g11-0015` *STATED* — Framer's Pro plan costs $45 a month on monthly billing, or $30 a month if you pay for the year, and you pay it for each site.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *evidence-for* `g11-0014`
  ↳ *leads-to* `g11-0016`

- `g11-0016` *STATED* — Framer Pro on monthly billing comes to $540 a year for one site.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *evidence-for* `g11-0014`
  ↳ *example-of* `g11-0009`

- `g11-0017` *STATED* — Instatic passed 8,800 stars on GitHub in five months.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *example-of* `g11-0004`

- `g11-0020` *STATED* — Framer's paid plans are bought site by site: Basic is $15 a month and Pro is $45 a month on monthly billing.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *evidence-for* `g11-0014`

- `g11-0183` *STATED* — Wispr Flow Pro costs $15 a month, or $12 a month if you pay for the year.
  — [g-fluidvoice-the-free-open-source-wispr-flow](https://chen.media/guides/fluidvoice-the-free-open-source-wispr-flow)
  ↳ *leads-to* `g11-0188`
  ↳ *contrast* `g11-0181`

- `g11-0184` *STATED* — Wispr Flow's free plan stops at 2,000 words a week on desktop.
  — [g-fluidvoice-the-free-open-source-wispr-flow](https://chen.media/guides/fluidvoice-the-free-open-source-wispr-flow)
  ↳ *because* `g11-0188` — free cap forces Pro

- `g11-0185` *STATED* — FluidVoice has passed 11,800 stars on GitHub.
  — [g-fluidvoice-the-free-open-source-wispr-flow](https://chen.media/guides/fluidvoice-the-free-open-source-wispr-flow)
  ↳ *evidence-for* `g11-0004`

- `g11-0188` *STATED* — Unlimited Wispr Flow means Pro: $180 a year paid monthly, or $144 paid yearly.
  — [g-fluidvoice-the-free-open-source-wispr-flow](https://chen.media/guides/fluidvoice-the-free-open-source-wispr-flow)
  ↳ *example-of* `g11-0009`

- `g11-0201` *STATED* — VoiceStudio has passed 43,000 stars on GitHub.
  — [g-the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer](https://chen.media/guides/the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer)
  ↳ *evidence-for* `g11-0004`

- `g11-0202` *STATED* — VoiceStudio needs 5 to 15 seconds of you talking to read any text back in your voice.
  — [g-the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer](https://chen.media/guides/the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer)
  ↳ *part-of* `g11-0198`

- `g12-0054` *STATED* — The go-live skill passed 1,000 stars on GitHub in its first five days.
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *evidence-for* `g12-0051`

- `g12-0132` *STATED* — The Claude Code SEO audit skill has almost 18,000 stars on GitHub.
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *evidence-for* `g12-0131`
  ↳ *contradicts* `g17-0103` — Claude SEO stars: 'almost 18,000' vs 14,028 (AgriciDaniel/claude-seo)

- `g12-0154` *STATED* — On September 23 (2026) Anthropic launched Claude Marketplace, one catalog inside Claude with more than 2,000 plugins and connectors from companies like Atlassian, Google, Microsoft, Notion and Salesforce.
  — [g-claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed](https://chen.media/guides/claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed)
  ↳ *part-of* `g12-0153`
  ↳ *leads-to* `g12-0155`

- `g12-0192` *STATED* — SupoClip is released under AGPL-3.0 and has about 1,200 stars on GitHub.
  — [g-supoclip-open-source-opusclip-alternative](https://chen.media/guides/supoclip-open-source-opusclip-alternative)
  ↳ *qualifies* `g12-0187`

- `g12-0291` *STATED* — One NVIDIA key runs all four coding models plus about 80 other models in NVIDIA's catalog.
  — [g-free-kimi-k3-glm-and-deepseek-on-one-nvidia-key](https://chen.media/guides/free-kimi-k3-glm-and-deepseek-on-one-nvidia-key)
  ↳ *part-of* `g12-0281`

- `g13-0079` *STATED* — Alex's Scrapling guide has 8 copyable Claude prompts for business research and website analysis.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *part-of* `g13-0063`

- `g13-0120` *STATED* — The /watch skill has over 17,000 GitHub stars.
  — [g-let-claude-code-watch-any-video-with-watch](https://chen.media/guides/let-claude-code-watch-any-video-with-watch)
  ↳ *evidence-for* `g13-0119`

- `g13-0137` *STATED* — claude-mem has over 94,000 stars on GitHub.
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *evidence-for* `g13-0136`
  ↳ *contradicts* `g17-0091` — claude-mem stars: 'over 94,000' vs 90,651 from the GitHub API

- `g13-0193` *STATED* — HackingTool lists 215 tools in 21 categories, including web, mobile and password testing.
  — [g-hackingtool-secure-your-own-apps](https://chen.media/guides/hackingtool-secure-your-own-apps)
  ↳ *part-of* `g13-0189`

- `g13-0194` *STATED* — HackingTool's repository showed about 79,700 GitHub stars when checked on September 23, 2026.
  — [g-hackingtool-secure-your-own-apps](https://chen.media/guides/hackingtool-secure-your-own-apps)
  ↳ *evidence-for* `g13-0189`

- `g13-0301` *STATED* — Alex's '100 Free Claude Skills' guide has 6 copyable setup prompts, 1 numbered step and 13 listed sections.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *part-of* `g13-0282`

- `g14-0074` *STATED* — Google's Antigravity setup guide requires VS Code 1.90 or later on macOS, Windows or Linux.
  — [g-antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you](https://chen.media/guides/antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you)
  ↳ *depends-on* `g14-0073` — requirement

- `g14-0229` *STATED* — The current ECC universal package requires Node.js 18 or newer.
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *part-of* `g14-0222`

- `g15-0017` *STATED* — Read on the GitHub API on 9 September 2026, Microsoft's MarkItDown had 182,033 stars and 13,371 forks.
  — [g-why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix](https://chen.media/guides/why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix)
  ↳ *evidence-for* `g15-0016`
  ↳ *example-of* `g15-0176`

- `g15-0042` *STATED* — Verified 2026-09-06 on the GitHub API, sergebulaev/linkedin-skills had 1,126 stars and 171 forks, MIT licence, written in Python.
  — [g-linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes](https://chen.media/guides/linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes)
  ↳ *evidence-for* `g15-0041`
  ↳ *example-of* `g15-0176`

- `g15-0109` *STATED* — wshobson/agents also ships 94 plugins, 183 skills, 105 commands and 16 orchestrators.
  — [g-the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build](https://chen.media/guides/the-202-agent-dev-team-how-to-put-four-claude-agents-on-one-build)
  ↳ *part-of* `g15-0105`

- `g16-0006` *STATED* — GitHub star counts quoted in this batch: public-apis 466,531; ollama 179,017; free-for-dev 132,255; awesome-mcp-servers 92,592; taste-skill 79,304; Scrapling 75,397; ruflo 68,132; prompt-master 11,415; unlazy 973; seven Claude Code repos 579,600 combined; five replacement repos 945,792 combined.
  — [g-the-free-skill-that-stops-claude-saying-done-when-it-is-not](https://chen.media/guides/the-free-skill-that-stops-claude-saying-done-when-it-is-not) [g-the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting](https://chen.media/guides/the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting) [g-ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm](https://chen.media/guides/ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm) [g-five-free-github-repos-that-replace-software-you-pay-for](https://chen.media/guides/five-free-github-repos-that-replace-software-you-pay-for) [g-seven-free-claude-code-repos-that-fix-what-claude-gets-wrong](https://chen.media/guides/seven-free-claude-code-repos-that-fix-what-claude-gets-wrong)
  ↳ *evidence-for* `g02-0235`

- `g16-0144` *STATED* — Unlazy reached 973 GitHub stars in under two weeks.
  — [g-the-free-skill-that-stops-claude-saying-done-when-it-is-not](https://chen.media/guides/the-free-skill-that-stops-claude-saying-done-when-it-is-not)
  ↳ *qualifies* `g16-0143`
  ↳ *because* `g16-0145`
  ↳ *part-of* `g16-0006`
  ↳ *part-of* `g16-0141`

- `g16-0295` *STATED* — ruvnet/ruflo has 68,132 stars, is MIT licensed, and was pushed the morning the guide was written.
  — [g-ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm](https://chen.media/guides/ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm)
  ↳ *qualifies* `g16-0294`
  ↳ *part-of* `g16-0006`
  ↳ *part-of* `g16-0293`

- `g16-0310` *STATED* — The seven Claude Code repos have 579,600 stars combined.
  — [g-seven-free-claude-code-repos-that-fix-what-claude-gets-wrong](https://chen.media/guides/seven-free-claude-code-repos-that-fix-what-claude-gets-wrong)
  ↳ *qualifies* `g16-0305`
  ↳ *part-of* `g16-0006`

- `g17-0092` *STATED* — The three Claude Code plugins total 121,174 combined GitHub stars, with nothing to pay and nothing to sign up for.
  — [g-the-three-claude-code-plugins-worth-installing](https://chen.media/guides/the-three-claude-code-plugins-worth-installing)
  ↳ *evidence-for* `g17-0086`

- `g17-0104` *STATED* — Claude SEO ships 25 sub-skills, 18 specialist agents and 32 user-facing commands.
  — [g-install-25-seo-skills-and-18-specialist-agents-into-claude-code](https://chen.media/guides/install-25-seo-skills-and-18-specialist-agents-into-claude-code)
  ↳ *evidence-for* `g17-0099`

- `g17-0105` *STATED* — Claude SEO has 410 tests passing.
  — [g-install-25-seo-skills-and-18-specialist-agents-into-claude-code](https://chen.media/guides/install-25-seo-skills-and-18-specialist-agents-into-claude-code)
  ↳ *qualifies* `g17-0103`
  ↳ *part-of* `g17-0099`

- `g17-0147` *STATED* — FreeLLMAPI covers 29 free providers, 251 model families and 358 free model endpoints.
  — [g-pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint](https://chen.media/guides/pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint)
  ↳ *evidence-for* `g17-0150`

- `g17-0159` *STATED* — Project NOMAD is reached through a browser at localhost:8080.
  — [g-a-knowledge-server-that-keeps-answering-with-the-internet-off](https://chen.media/guides/a-knowledge-server-that-keeps-answering-with-the-internet-off)
  ↳ *part-of* `g17-0157`

- `g17-0269` *STATED* — Open Generative AI, verified 2026-08-07: 25,757 stars, 4,527 forks, 400+ models across 14 studios.
  — [g-400-ai-image-and-video-models-in-one-free-desktop-app](https://chen.media/guides/400-ai-image-and-video-models-in-one-free-desktop-app)
  ↳ *evidence-for* `g17-0268`
  ↳ *evidence-for* `g17-0303`

- `g18-0024` *STATED* — Alex's 15 more free replacements for paid AI tools add up to $747 a month at their top tier, of which $569 a month is switchable.
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *example-of* `g18-0287`

- `g18-0050` *INFERRED* — The four KEEP tools in the 15-replacements list sum to $178/month ($747 - $569); Figma $90, DeepL $58 and Todoist $6 make $154, so the fourth KEEP is a $24 tool (Dropbox or Loom).
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *evidence-for* `g18-0028`

- `g18-0094` *STATED* — The Open Generative AI README describes 400 plus models across 14 studios, more than most people realise when they first open it.
  — [g-the-open-source-ai-studio-that-replaces-a-video-subscription](https://chen.media/guides/the-open-source-ai-studio-that-replaces-a-video-subscription)
  ↳ *part-of* `g18-0092`
  ↳ *evidence-for* `g17-0269`
  ↳ *part-of* `g17-0268`

- `g18-0193` *STATED* — G0DM0D3 talks to more than 60 models.
  — [g-one-html-file-that-runs-chatgpt-claude-gemini-and-grok-side-by-side](https://chen.media/guides/one-html-file-that-runs-chatgpt-claude-gemini-and-grok-side-by-side)
  ↳ *part-of* `g18-0191`

- `g18-0199` *STATED* — Between them the five open source replacements have 176,656 stars on GitHub; the guide ranks them by stars and gives the install command for each.
  — [g-five-paid-apps-with-full-open-source-replacements](https://chen.media/guides/five-paid-apps-with-full-open-source-replacements)
  ↳ *evidence-for* `g18-0198`

- `g18-0264` *INFERRED* — The seven listed star counts sum to 499.3k (94.1 + 111.3 + 137.4 + 25.9 + 54.8 + 43.6 + 32.2), matching the 'over 499,000' headline.
  — [g-seven-free-repos-that-replace-paid-ai-tools](https://chen.media/guides/seven-free-repos-that-replace-paid-ai-tools)
  ↳ *evidence-for* `g18-0262`

- `g19-0188` *STATED* — Serena works across over 40 programming languages on its language-server backend.
  > “It works across over 40 programming languages”
  — [g-give-claude-code-an-ide-brain-so-it-stops-reading-everything](https://chen.media/guides/give-claude-code-an-ide-brain-so-it-stops-reading-everything)
  ↳ *qualifies* `g19-0181`

- `g22-0155` *STATED* — Custom connectors work on every Claude plan: the free plan allows one custom connector, while Pro and Max allow more.
  — [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)
  ↳ *qualifies* `g22-0153`
  ↳ *evidence-for* `g07-0009`

- `g23-0099` *STATED* — Claude has over 50,000 skills and most people have never used one.
  — [g-five-claude-skills-that-beat-99-of-users](https://chen.media/guides/five-claude-skills-that-beat-99-of-users)
  ↳ *contradicts* `g10-0256` — Skill count: 'Claude has over 50,000 skills' vs 1,499,600 agent skills on the skills.sh leaderboard
  ↳ *contradicts* `y04-0113` — Skill count: 'over 50,000 skills' vs 'over 90,000 skills'

- `y02-0053` *STATED* — Adobe costs $68.97 a month (the figure in Alex Chen's video title 'Stop paying Adobe $68.97 a month').
  — [lhx8M2JPLPE](https://youtu.be/lhx8M2JPLPE)
  ↳ *evidence-for* `g08-0046`
  ↳ *part-of* `y02-0052`

- `y02-0175` *STATED* — The Logo Design Skill got over 1,500 stars on GitHub in one week.
  — [J8g3EZwZx20](https://youtu.be/J8g3EZwZx20)
  ↳ *evidence-for* `g09-0179`
  ↳ *part-of* `y02-0172`
  ↳ *because* `y02-0176` — traction attributed to studying real logos

- `y03-0028` *STATED* — Fast-Jev Compaction is already at almost 7,000 GitHub stars.
  — [20RWbPnejOE](https://youtu.be/20RWbPnejOE) [tq8Addr9brU](https://youtu.be/tq8Addr9brU) [kUH4J8VWe-I](https://youtu.be/kUH4J8VWe-I) [7eL_2dx0-bU](https://youtu.be/7eL_2dx0-bU)
  ↳ *evidence-for* `g12-0172`
  ↳ *evidence-for* `y03-0026`

- `y03-0101` *STATED* — The Find Skills skill has been installed 3.6 million times.
  — [wfwnTNtnomk](https://youtu.be/wfwnTNtnomk) [1j9mmXDW8Qw](https://youtu.be/1j9mmXDW8Qw)
  ↳ *evidence-for* `g10-0248`
  ↳ *evidence-for* `y03-0100`

- `y03-0104` *STATED* — Find Skills also works in over 75 other AI coding tools.
  — [wfwnTNtnomk](https://youtu.be/wfwnTNtnomk) [1j9mmXDW8Qw](https://youtu.be/1j9mmXDW8Qw)
  ↳ *contradicts* `g18-0086` — skills reach: 'over 75 other AI coding tools' vs npx skills '40 or so other agents'
  ↳ *evidence-for* `g10-0265`
  ↳ *qualifies* `y03-0100`

- `y03-0112` *STATED* — Open Design has already passed 99,000 stars on GitHub.
  — [NrJa3MCde-I](https://youtu.be/NrJa3MCde-I) [vdLceKphMoQ](https://youtu.be/vdLceKphMoQ)
  ↳ *evidence-for* `g10-0201`
  ↳ *evidence-for* `y03-0110`
  ↳ *example-of* `y03-0207`

- `y03-0114` *STATED* — Open Design comes with the design styles of 151 real brands like Apple, Nike and Airbnb.
  — [NrJa3MCde-I](https://youtu.be/NrJa3MCde-I) [vdLceKphMoQ](https://youtu.be/vdLceKphMoQ)
  ↳ *evidence-for* `g10-0221`
  ↳ *qualifies* `y03-0113`

- `y03-0117` *STATED* — Dyad already has over 21,000 stars on GitHub.
  — [cxLfDm8_Yx4](https://youtu.be/cxLfDm8_Yx4) [a8nVKYxwcjo](https://youtu.be/a8nVKYxwcjo) [udcHbDvy7o4](https://youtu.be/udcHbDvy7o4)
  ↳ *evidence-for* `g10-0237`
  ↳ *evidence-for* `y03-0116`

- `y03-0123` *STATED* — Instatic already has over 8,000 stars on GitHub.
  — [N8BCMjq3wPE](https://youtu.be/N8BCMjq3wPE) [23JOjnkdikY](https://youtu.be/23JOjnkdikY)
  ↳ *evidence-for* `g11-0017`
  ↳ *evidence-for* `y03-0122`

- `y03-0129` *STATED* — FluidVoice already has over 11,000 stars on GitHub.
  — [OtRSHXUQxAQ](https://youtu.be/OtRSHXUQxAQ) [4xBCskEhIfE](https://youtu.be/4xBCskEhIfE)
  ↳ *evidence-for* `g11-0185`
  ↳ *evidence-for* `y03-0128`

- `y04-0141` *STATED* — Agent Reach has over 78,000 stars on GitHub.
  > “with over 78,000 stars on GitHub”
  — [VRRK9REgdaA](https://youtu.be/VRRK9REgdaA)
  ↳ *part-of* `g14-0101`
  ↳ *evidence-for* `y04-0140`

### opinion

- `g05-0026` *STATED* — Treat Anthropic's learning study as the reason Vibewise exists, not as a result for the plugin.
  > “Treat it as the reason the plugin exists, not as a result for the plugin.”
  — [g-turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin](https://chen.media/guides/turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin)
  ↳ *because* `g05-0025`

- `g07-0012` *STATED* — Alex positions Claude's Gmail connector as a free replacement for Superhuman Mail for searching, summarizing, labelling and drafting email.
  — [g-sort-your-inbox-with-claude-instead-of-superhuman](https://chen.media/guides/sort-your-inbox-with-claude-instead-of-superhuman)
  ↳ *example-of* `g07-0292`

- `g08-0058` *STATED* — The Craft apps are worth trying next to your Adobe apps today, but not yet worth cancelling Adobe for.
  > “They are worth trying next to your Adobe apps today, and not yet worth cancelling for.”
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *example-of* `g08-0258`
  ↳ *example-of* `g18-0287`

- `g09-0056` *STATED* — Every voice assistant you've tried either does very little or costs a monthly fee on top of what you already pay.
  > “Every voice assistant you've tried either does very little or costs a monthly fee on top of what you already pay.”
  — [g-run-a-jarvis-on-your-own-claude-code](https://chen.media/guides/run-a-jarvis-on-your-own-claude-code)
  ↳ *contrast* `g09-0050`

- `g11-0014` *STATED* — Alex says Instatic can replace a $45-a-month Framer plan.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *example-of* `g18-0287`

- `g11-0029` *STATED* — Alex's ownership pitch for Instatic: your domain, your server, your files.
  > “Your domain, your server, your files.”
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *generalizes* `g11-0013`
  ↳ *example-of* `y03-0208`

- `g14-0290` *STATED* — The part that makes Claude skill packs useful is adapting one workflow to your actual business.
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *qualifies* `g14-0289`

- `g15-0179` *CORE* — Alex Chen separates installable tools from prompt packs: the four repos are 'none of them a prompt pack', Munder Difflin is 'a desktop app, not a prompt pack', The Agency is 'not prompt templates, not a starter pack', and the UI libraries are 'not a template or a site builder'.
  — [g-four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute](https://chen.media/guides/four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute) [g-munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents](https://chen.media/guides/munder-difflin-the-free-app-that-turns-claude-code-into-an-office-of-agents) [g-the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install](https://chen.media/guides/the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install) [g-four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed](https://chen.media/guides/four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed)

- `g16-0308` *STATED* — Only seven Claude Code repos are worth the disk space.
  > “Seven are worth the disk space.”
  — [g-seven-free-claude-code-repos-that-fix-what-claude-gets-wrong](https://chen.media/guides/seven-free-claude-code-repos-that-fix-what-claude-gets-wrong)
  ↳ *qualifies* `g16-0305`

- `g17-0003` *STATED* — Alex Chen says being free is not the interesting part of the seven marketing skills; the interesting part is that they do not compose in an arbitrary order.
  > “That is not the interesting part. The interesting part is that they do not compose in an arbitrary order”
  — [g-seven-free-claude-skills-that-cover-a-marketing-department](https://chen.media/guides/seven-free-claude-skills-that-cover-a-marketing-department)
  ↳ *leads-to* `g17-0010`

- `g17-0010` *STATED* — For a stack of Claude skills, the order you install them in matters more than which ones are on the list.
  > “Why the order matters more than the list”
  — [g-seven-free-claude-skills-that-cover-a-marketing-department](https://chen.media/guides/seven-free-claude-skills-that-cover-a-marketing-department)
  ↳ *example-of* `g16-0007`

- `g17-0136` *STATED* — Several Apple style skills exist; chaos-xxl/apple-design-skill is the closest to a web design system rather than an iOS one, which is what you want for a website.
  > “That one is the closest to a web design system rather than an iOS one”
  — [g-apple-s-real-design-tokens-packaged-as-a-claude-skill](https://chen.media/guides/apple-s-real-design-tokens-packaged-as-a-claude-skill)
  ↳ *qualifies* `g17-0135`

- `g17-0271` *STATED* — Bring-your-own-key is the whole reason Open Generative AI is free, and it is the part the video does not have time to explain.
  > “it is the whole reason the thing is free”
  — [g-400-ai-image-and-video-models-in-one-free-desktop-app](https://chen.media/guides/400-ai-image-and-video-models-in-one-free-desktop-app)
  ↳ *qualifies* `g17-0270`
  ↳ *example-of* `g17-0305`

- `g17-0311` *CORE* — Claude skills and agents are plain markdown files, so read the file before you trust or run it: the file is the product.
  > “The file is the product, so you can read it before you trust it.”
  — [g-164-claude-skills-in-one-repo-which-to-take-first](https://chen.media/guides/164-claude-skills-in-one-repo-which-to-take-first) [g-286-specialist-ai-agents-free-inside-claude-code](https://chen.media/guides/286-specialist-ai-agents-free-inside-claude-code) [g-apple-s-real-design-tokens-packaged-as-a-claude-skill](https://chen.media/guides/apple-s-real-design-tokens-packaged-as-a-claude-skill)

- `g18-0012` *STATED* — For judging a harness like ECC, coverage is the number that matters, not GitHub stars.
  > “Coverage is the number that matters, not stars”
  — [g-67-agents-281-skills-and-94-commands-in-one-install](https://chen.media/guides/67-agents-281-skills-and-94-commands-in-one-install)
  ↳ *qualifies* `g18-0001`
  ↳ *qualifies* `g02-0235`

- `g18-0049` *STATED* — Todoist to Vikunja is the one swap on the list that is probably not worth the effort.
  > “This is the one swap that is probably not worth the effort”
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *qualifies* `g18-0048`
  ↳ *example-of* `g18-0028`

- `g18-0097` *STATED* — Cinema Studio is the part of Open Generative AI worth the install.
  > “Cinema Studio, the part worth the install”
  — [g-the-open-source-ai-studio-that-replaces-a-video-subscription](https://chen.media/guides/the-open-source-ai-studio-that-replaces-a-video-subscription)
  ↳ *part-of* `g18-0092`
  ↳ *evidence-for* `g17-0274`

- `g18-0196` *STATED* — Classic Mode is the part of G0DM0D3 worth the download.
  > “Classic Mode, the part worth the download”
  — [g-one-html-file-that-runs-chatgpt-claude-gemini-and-grok-side-by-side](https://chen.media/guides/one-html-file-that-runs-chatgpt-claude-gemini-and-grok-side-by-side)
  ↳ *part-of* `g18-0191`

- `g19-0163` *STATED* — Graphiti and Task Master are the heavier lifts, so set them up once Claude Code Router and Repomix are earning their keep.
  > “Graphiti and Task Master are the heavier lifts, so do them once the first two are earning their keep.”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *part-of* `g19-0160`
  ↳ *qualifies* `g19-0158`
  ↳ *qualifies* `g19-0159`

- `g23-0065` *STATED* — 2026 tier list, Automations (in the video): bad Zapier, mid Make, great pick n8n.
  — [g-the-2026-ai-tool-tier-list-with-the-reason-for-each-pick](https://chen.media/guides/the-2026-ai-tool-tier-list-with-the-reason-for-each-pick)
  ↳ *part-of* `g23-0051`
  ↳ *because* `g23-0066`
  ↳ *contradicts* `g23-0180` — tier list rates Zapier bad and n8n great; pro stack calls Zapier the pro upgrade over Make
  ↳ *evidence-for* `g18-0034`

- `g23-0189` *STATED* — Hype swap, Design: replace v0 with Bolt.new: comparable UI plus full-stack code, with a free tier and an open-source self-host option.
  — [g-six-hyped-ai-tools-and-what-quietly-does-the-same-job](https://chen.media/guides/six-hyped-ai-tools-and-what-quietly-does-the-same-job)
  ↳ *evidence-for* `g23-0205`
  ↳ *example-of* `g23-0188`

- `g23-0190` *STATED* — Hype swap, Video: replace Runway with Higgsfield: cinematic AI video and motion for a fraction of Runway's monthly spend.
  — [g-six-hyped-ai-tools-and-what-quietly-does-the-same-job](https://chen.media/guides/six-hyped-ai-tools-and-what-quietly-does-the-same-job)
  ↳ *evidence-for* `g23-0201`
  ↳ *example-of* `g23-0188`
  ↳ *contradicts* `y01-0186` — Higgsfield: recommended swap 'for a fraction of Runway's monthly spend' vs 'literally just a wrapper' charging $100/month
  ↳ *contradicts* `g18-0135` — Higgsfield: swap Runway FOR Higgsfield vs replace Higgsfield WITH Hailuo
  ↳ *contradicts* `g18-0201` — Higgsfield: hype-swap pick vs OpenMontage as open-source replacement 'instead of HiggsField'

- `g23-0191` *STATED* — Hype swap, Images: replace Midjourney with Leonardo: comparable image quality on a permanent free tier; Midjourney has none.
  — [g-six-hyped-ai-tools-and-what-quietly-does-the-same-job](https://chen.media/guides/six-hyped-ai-tools-and-what-quietly-does-the-same-job)
  ↳ *evidence-for* `g23-0205`
  ↳ *example-of* `g23-0188`

- `g23-0192` *STATED* — Hype swap, Coding: replace GitHub Copilot with Cursor: it edits your whole project agentically instead of just autocompleting lines.
  — [g-six-hyped-ai-tools-and-what-quietly-does-the-same-job](https://chen.media/guides/six-hyped-ai-tools-and-what-quietly-does-the-same-job)
  ↳ *evidence-for* `g23-0202`
  ↳ *example-of* `g23-0188`
  ↳ *evidence-for* `g18-0132`

- `g23-0193` *STATED* — Hype swap, Agents: replace Manus with ChatGPT Agent: the same browse, click and build workflows, bundled in the $20 plan you already pay.
  — [g-six-hyped-ai-tools-and-what-quietly-does-the-same-job](https://chen.media/guides/six-hyped-ai-tools-and-what-quietly-does-the-same-job)
  ↳ *evidence-for* `g23-0205`
  ↳ *example-of* `g23-0188`

- `g23-0194` *STATED* — Hype swap, Browser: replace Dia with Comet: the same agentic browsing, free, and on every platform instead of macOS only.
  — [g-six-hyped-ai-tools-and-what-quietly-does-the-same-job](https://chen.media/guides/six-hyped-ai-tools-and-what-quietly-does-the-same-job)
  ↳ *evidence-for* `g23-0205`
  ↳ *example-of* `g23-0188`

- `y01-0126` *STATED* — Alex prefers ai-agency-claude over downloading 50 random AI agents because its teams connect through one business workflow.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)
  ↳ *because* `y01-0127`

- `y01-0175` *STATED* — Telling Claude what to do every single day by re-prompting it is inefficient - to fully automate a repetitive workflow, use Claude skills.
  — [pIED4nGZL6E](https://youtu.be/pIED4nGZL6E)
  ↳ *leads-to* `y01-0180`
  ↳ *leads-to* `y01-0176`

- `y03-0142` *STATED* — Alex: if you're looking for a free alternative to Photoshop, Photon Studio is worth a try.
  — [WB8w3FTYCnw](https://youtu.be/WB8w3FTYCnw) [kasTR80Lvjo](https://youtu.be/kasTR80Lvjo)
  ↳ *part-of* `g10-0152`
  ↳ *qualifies* `y03-0134`

- `y04-0113` *STATED* — Claude has over 90,000 skills, but you only need three of them.
  > “Claude has over 90,000 skills, but you only need three of them.”
  — [Gqm7-viLo_E](https://youtu.be/Gqm7-viLo_E)
  ↳ *contradicts* `g10-0256` — Skill count: 'over 90,000 skills' vs 1,499,600 on skills.sh
  ↳ *example-of* `y04-0153`

- `y04-0144` *STATED* — Agent Reach is 'better than paid alternatives' for giving AI web and social-platform access.
  > “Agent Reach: Better than paid alternatives”
  — [VRRK9REgdaA](https://youtu.be/VRRK9REgdaA)
  ↳ *part-of* `g14-0101`
  ↳ *qualifies* `y04-0140`

### product

- `g01-0066` *STATED* — khan-explainer is a free, open-source (MIT) Claude Code skill that makes Khan Academy style videos.
  — [g-make-khan-academy-style-videos-with-claude](https://chen.media/guides/make-khan-academy-style-videos-with-claude)
  ↳ *contrast* `g01-0097` — video lesson vs audio course from one prompt

- `g01-0075` *STATED* — Show Your Work is a free, open-source Claude Code plugin that puts the real images, test recordings and design versions your agent made straight into the chat.
  — [g-show-your-work-see-every-screenshot-and-video-claude-makes-right-in-your-termina](https://chen.media/guides/show-your-work-see-every-screenshot-and-video-claude-makes-right-in-your-termina)

- `g01-0087` *STATED* — Graphicle is a free, open-source (Apache-2.0) program that gives your coding agent a code graph of your repo and a memory of your project.
  — [g-give-claude-a-map-and-a-memory-of-your-whole-project](https://chen.media/guides/give-claude-a-map-and-a-memory-of-your-whole-project)
  ↳ *example-of* `g02-0241`

- `g01-0097` *STATED* — Claudemy is a free, open-source (MIT) Claude Code skill that turns a topic into a short audio course.
  — [g-turn-any-topic-into-a-12-lesson-audio-course-with-claude](https://chen.media/guides/turn-any-topic-into-a-12-lesson-audio-course-with-claude)

- `g01-0152` *STATED* — ReelMimic is a free, open-source app that runs on your own computer with your own Claude Code and makes a new video in the style of one you love.
  — [g-reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-get-a-new-one-in-the-same-style)
  ↳ *example-of* `g01-0196`
  ↳ *evidence-for* `g05-0114`

- `g01-0165` *STATED* — Grill Me is a free Claude Code skill from Matt Pocock's skills pack.
  — [g-grill-me-make-claude-interview-you-before-it-writes-a-line-of-code](https://chen.media/guides/grill-me-make-claude-interview-you-before-it-writes-a-line-of-code)

- `g01-0177` *STATED* — Scientific Agent Skills is a free, open-source collection of 177 science and research skills for Claude, made by K-Dense (MIT licence, over 50,000 stars on GitHub).
  — [g-give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills](https://chen.media/guides/give-claude-a-full-science-lab-set-up-the-free-scientific-agent-skills)

- `g02-0129` *STATED* — Atticus is a free, open-source (MIT) Mac app that lets you control your whole Mac with your voice, powered by Claude.
  — [g-control-your-whole-mac-with-your-voice-powered-by-claude](https://chen.media/guides/control-your-whole-mac-with-your-voice-powered-by-claude)

- `g02-0161` *STATED* — github-triage is an open-source Claude Code skill from Trail of Bits that goes through every open issue and pull request in your repo, offers to merge the ready ones, closes the issues already fixed, and ranks what is left.
  — [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say)
  ↳ *part-of* `g02-0163`
  ↳ *depends-on* `g02-0165`

- `g02-0185` *CORE* — Chrome Relay is a free, MIT-licensed Mac program that lets Claude Code drive the Chrome you already use, signed in as you, in background tabs.
  — [g-let-claude-use-your-signed-in-chrome-in-the-background](https://chen.media/guides/let-claude-use-your-signed-in-chrome-in-the-background)
  ↳ *contrast* `g02-0187`
  ↳ *example-of* `g02-0244`

- `g02-0219` *STATED* — AI Homepage is a free, open-source Chrome extension from an engineer on the Claude Code team.
  — [g-ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper](https://chen.media/guides/ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper)

- `g03-0035` *STATED* — SkillSpector is a free, open-source scanner from NVIDIA that scans a Claude skill for malware before you install it.
  — [g-skillspector-scan-any-claude-skill-for-malware-before-you-install-it](https://chen.media/guides/skillspector-scan-any-claude-skill-for-malware-before-you-install-it)
  ↳ *contrast* `g03-0176` — SkillSpector scans skills you install; Anthropic's skills scan your own code

- `g03-0089` *STATED* — Diagram Design is a free, open-source agent skill for Claude Code by Cathryn Lavery that turns a plain-words request into a finished, designed diagram in one HTML file.
  — [g-diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe](https://chen.media/guides/diagram-design-the-free-claude-skill-that-draws-any-diagram-you-describe)
  ↳ *example-of* `g03-0014`

- `g03-0100` *STATED* — Caveman is a popular open-source skill (JuliusBrussee/caveman) that makes Claude drop the filler and answer in short, blunt phrases while code stays exact.
  — [g-make-claude-answer-in-fewer-words-with-the-caveman-skill](https://chen.media/guides/make-claude-answer-in-fewer-words-with-the-caveman-skill)
  ↳ *part-of* `g03-0009`

- `g03-0140` *STATED* — Minutes is a free, open-source conversation memory app by Mat Silverstein that records and transcribes meetings, calls, voice memos and dictation on your device.
  — [g-minutes-the-free-open-source-meeting-recorder-that-claude-can-search](https://chen.media/guides/minutes-the-free-open-source-meeting-recorder-that-claude-can-search)

- `g03-0176` *STATED* — Anthropic open-sourced four Claude Code skills, built from what it learned working with security teams, that find security holes in source code.
  — [g-hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills](https://chen.media/guides/hunt-the-security-holes-in-your-code-with-anthropic-s-free-claude-skills)

- `g03-0228` *STATED* — Answer me with HTML is a free, open-source (MIT) Claude skill that turns a hard answer into one readable page with diagrams, tables, code and warnings in view at once.
  — [g-answer-me-with-html-make-claude-answer-with-one-clean-page-not-a-wall-of-text](https://chen.media/guides/answer-me-with-html-make-claude-answer-with-one-clean-page-not-a-wall-of-text)
  ↳ *example-of* `g03-0014`

- `g04-0014` *STATED* — Academic Research Skills is a free set of Claude Code skills for research papers.
  — [g-academic-research-skills-make-claude-check-every-source-in-your-paper-is-real](https://chen.media/guides/academic-research-skills-make-claude-check-every-source-in-your-paper-is-real)
  ↳ *part-of* `g04-0028`

- `g04-0176` *STATED* — Vibewise is a free Claude Code plugin that tries to give you back the learning way of using AI.
  > “Vibewise is a free plugin that tries to give you the other way of using AI back.”
  — [g-ai-coders-scored-17-lower-on-a-quiz-make-claude-teach-you-with-the-free-vibewise](https://chen.media/guides/ai-coders-scored-17-lower-on-a-quiz-make-claude-teach-you-with-the-free-vibewise)
  ↳ *because* `g04-0186`
  ↳ *part-of* `g04-0200`
  ↳ *example-of* `g04-0252`
  ↳ *evidence-for* `g05-0001`

- `g05-0001` *CORE* — Vibewise is a free Claude Code plugin that turns Claude into a coding tutor instead of a code-writer you hand everything to.
  — [g-turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin](https://chen.media/guides/turn-claude-into-a-coding-tutor-set-up-the-free-vibewise-plugin)
  ↳ *because* `g05-0005` — the plugin exists because of the learning gap

- `g05-0031` *STATED* — Chrome Relay is a free, open-source (MIT) tool that lets Claude Code work inside your everyday Chrome, already signed in to your apps.
  — [g-let-claude-use-your-real-chrome-signed-in-in-background-tabs](https://chen.media/guides/let-claude-use-your-real-chrome-signed-in-in-background-tabs)
  ↳ *example-of* `g05-0322`
  ↳ *evidence-for* `g02-0185`
  ↳ *contrast* `g22-0105`

- `g05-0043` *STATED* — AI Promo Video Maker is a free, MIT-licensed repo that teaches Claude Code a ten-step workflow for making a product promo video.
  — [g-make-a-full-promo-video-with-claude-from-one-sentence](https://chen.media/guides/make-a-full-promo-video-with-claude-from-one-sentence)
  ↳ *enables* `g05-0055`

- `g05-0050` *STATED* — Narration in AI Promo Video Maker is optional and uses ElevenLabs.
  — [g-make-a-full-promo-video-with-claude-from-one-sentence](https://chen.media/guides/make-a-full-promo-video-with-claude-from-one-sentence)
  ↳ *part-of* `g05-0043`
  ↳ *contrast* `g05-0051`

- `g05-0074` *STATED* — An open-source repo holds fifteen 10-second motion-design films, one style each, all made by Claude Opus 5.5 writing code from one prompt.
  — [g-15-motion-design-styles-claude-can-make-from-one-prompt](https://chen.media/guides/15-motion-design-styles-claude-can-make-from-one-prompt)
  ↳ *example-of* `g05-0318`

- `g05-0114` *STATED* — ReelMimic is a free, open-source (MIT) app: drop in a reference video, say what you want to make, and it builds a new video in that style.
  — [g-reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style](https://chen.media/guides/reelmimic-show-claude-a-video-you-love-and-get-a-new-one-in-the-same-style)

- `g05-0128` *STATED* — Mortiflix is a free, open-source app (AGPL-3.0) that works like a small motion design studio, with Claude making the video one stage at a time on your own computer.
  — [g-mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer](https://chen.media/guides/mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer)

- `g05-0138` *STATED* — Mortiflix videos are built in Remotion.
  — [g-mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer](https://chen.media/guides/mortiflix-let-claude-run-a-motion-design-studio-on-your-own-computer)
  ↳ *part-of* `g05-0128`
  ↳ *evidence-for* `g05-0318`

- `g05-0223` *STATED* — 3D Asset Server is a free, open-source (Apache-2.0) MCP tool that lets Claude search 23 sites of 3D models, textures and HDRI skies at once and download what you pick.
  — [g-3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once](https://chen.media/guides/3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once)
  ↳ *example-of* `g05-0322`

- `g05-0299` *STATED* — The logo-design skill is an open-source skill that makes Claude work like a step-by-step identity designer.
  — [g-install-the-logo-design-skill](https://chen.media/guides/install-the-logo-design-skill)
  ↳ *evidence-for* `g09-0177`

- `g06-0001` *STATED* — The free /iq Claude Code skill estimates your IQ from your own past Claude Code chats instead of from a test.
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *contrast* `g06-0002`

- `g06-0031` *STATED* — Oil UI is a free, open-source design skill for Claude Code that explores a few genuinely different design directions side by side, lets you pick one, then refines it against real laptop and phone screenshots.
  — [g-oil-ui-make-claude-design-your-app-three-really-different-ways-then-pick-one](https://chen.media/guides/oil-ui-make-claude-design-your-app-three-really-different-ways-then-pick-one)

- `g06-0074` *STATED* — anatomy is a Claude Code skill that explains an idea by building it as a detailed isometric figure you can click and watch run.
  — [g-set-up-the-anatomy-skill-the-free-repo-that-turns-any-idea-into-a-working-machin](https://chen.media/guides/set-up-the-anatomy-skill-the-free-repo-that-turns-any-idea-into-a-working-machin)

- `g06-0105` *STATED* — magpie is an open source app that lets you pick the model behind Claude Code and moves on to your next account when one runs out.
  — [g-keep-claude-code-working-after-your-limit-runs-out](https://chen.media/guides/keep-claude-code-working-after-your-limit-runs-out)
  ↳ *contrast* `g06-0220` — route around the limit vs make it last
  ↳ *example-of* `g16-0013`

- `g06-0124` *STATED* — universal-modder gives Claude Code skills for twelve game engines, so one sentence can add a weapon, a unit or a whole new mechanic to a PC game you own.
  — [g-set-up-universal-modder-the-free-repo-that-lets-claude-mod-your-pc-games](https://chen.media/guides/set-up-universal-modder-the-free-repo-that-lets-claude-mod-your-pc-games)

- `g06-0250` *STATED* — VibeWise is an open-source Claude Code plugin that asks for your plan first, lets you approve each step, then explains what it built, so Claude teaches you while it writes your code.
  — [g-make-claude-teach-you-while-it-writes-your-code](https://chen.media/guides/make-claude-teach-you-while-it-writes-your-code)
  ↳ *evidence-for* `g05-0001`
  ↳ *example-of* `g05-0312`

- `g07-0024` *STATED* — Find Skills: tell Claude what you're working on and it searches over a million skills, checks which ones are trusted, and installs the best match.
  — [g-let-claude-find-and-install-the-right-skill-for-any-job](https://chen.media/guides/let-claude-find-and-install-the-right-skill-for-any-job)
  ↳ *evidence-for* `g10-0247`

- `g07-0038` *STATED* — REA lets Claude Code look inside an app on your own machine and explain how a feature works, with the evidence, then build your own version.
  — [g-see-how-an-apps-feature-works-with-claude-code-and-rea-free](https://chen.media/guides/see-how-an-apps-feature-works-with-claude-code-and-rea-free)

- `g08-0001` *STATED* — Vibewise is a free plugin for Claude Code that makes Claude ask how you would build it first, walk you through the trade-offs and explain what it changed.
  > “Vibewise is a free plugin that makes Claude ask how you'd build it first, walk you through the trade-offs and explain what it changed.”
  — [g-vibe-code-and-still-learn-set-up-the-free-vibewise-plugin-for-claude-code](https://chen.media/guides/vibe-code-and-still-learn-set-up-the-free-vibewise-plugin-for-claude-code)
  ↳ *leads-to* `g08-0002`
  ↳ *because* `g08-0008` — the plugin answers the vibe-coding catch
  ↳ *evidence-for* `g05-0001`

- `g08-0049` *STATED* — PhotoCraft, FilmCraft and EffectCraft are free, open-source copies of Photoshop, Premiere Pro and After Effects, released by a developer who says he built them with Claude.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *example-of* `g18-0287`

- `g08-0059` *STATED* — PhotoCraft (the Photoshop swap) is an image editor with layers, masks, adjustment layers, layer styles, type, vectors and brushes.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *part-of* `g08-0049`

- `g08-0062` *STATED* — FilmCraft (the Premiere Pro swap) is a video editor with a timeline, colour, effects, audio, titles and captions, and export.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *part-of* `g08-0049`

- `g08-0064` *STATED* — EffectCraft (the After Effects swap) is a motion graphics and effects app with compositions, layers, keyframes, hundreds of effects, 3D cameras and lights, and a render queue.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *part-of* `g08-0049`

- `g08-0069` *STATED* — The ArtCraft suite has more apps beyond PhotoCraft, FilmCraft and EffectCraft (section 'And more from the same suite', body locked).
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *part-of* `g08-0049`

- `g08-0089` *CORE* — The Agency is a free, open-source repo of more than 230 specialist agents for Claude Code, each a separate expert with its own personality and process.
  — [g-run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents](https://chen.media/guides/run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents)
  ↳ *evidence-for* `g15-0113`
  ↳ *contradicts* `g15-0116` — The Agency size: 'more than 230' agents vs 273 agents
  ↳ *contradicts* `g17-0258` — The Agency size: 'more than 230' agents vs 286 agents

- `g08-0156` *STATED* — Replica is a free set of 11 Claude skills that clone an app you pay for, test it and fix what its users hate.
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *contrast* `g08-0089` — 11 pipeline skills for one job vs 230+ standalone specialists

- `g09-0050` *STATED* — Jarvis is a free, open-source (MIT) voice assistant: say 'Hey Jarvis' and it wakes up in your browser, powered by the Claude Code you already pay for.
  > “Say "Hey Jarvis" and a voice assistant wakes up in your browser, powered by the Claude Code you already pay for.”
  — [g-run-a-jarvis-on-your-own-claude-code](https://chen.media/guides/run-a-jarvis-on-your-own-claude-code)
  ↳ *part-of* `g09-0049`
  ↳ *depends-on* `g09-0058`
  ↳ *example-of* `g09-0252`

- `g09-0073` *STATED* — Impeccable is a free, open-source Claude design skill (76,000+ GitHub stars) that gives Claude a real design language and catches 61 AI design tells before anyone sees them.
  — [g-stop-your-site-looking-ai-made-impeccable](https://chen.media/guides/stop-your-site-looking-ai-made-impeccable)
  ↳ *part-of* `g09-0062`
  ↳ *because* `g09-0063`
  ↳ *example-of* `g09-0252`
  ↳ *evidence-for* `g09-0251`

- `g09-0177` *CORE* — The free, open-source logo design skill turns Claude into a logo designer: it checks your idea against more than 1,400 real logos, tests the mark down to 16 pixels, and hands you the SVG, a colour palette and a full set of app icons and favicons.
  — [g-free-claude-logo-design-skill](https://chen.media/guides/free-claude-logo-design-skill)
  ↳ *part-of* `g09-0175`

- `g09-0195` *STATED* — MiroFish is a free, open-source swarm simulator (75,000 GitHub stars) that builds a crowd of simulated customers from your page, price or ad and tells you who bites, who swims off and why.
  — [g-mirofish-test-your-launch-on-fake-customers](https://chen.media/guides/mirofish-test-your-launch-on-fake-customers)
  ↳ *part-of* `g09-0193`
  ↳ *because* `g09-0194`

- `g09-0232` *CORE* — Coucou is a free, open-source Mac app that puts a little pet called Mochi in your MacBook's notch to show what Claude Code is doing, live, and let you answer it without opening the terminal.
  — [g-coucou-free-notch-pet-that-watches-claude-code](https://chen.media/guides/coucou-free-notch-pet-that-watches-claude-code)
  ↳ *part-of* `g09-0229`
  ↳ *because* `g09-0230`

- `g10-0152` *STATED* — Photon Studio is a free desktop image editor that does most of what people pay Photoshop $22.99 a month for: layers and masks, retouching, design tools, and opening and saving PSD files.
  — [g-photon-studio-the-free-photoshop-alternative](https://chen.media/guides/photon-studio-the-free-photoshop-alternative)
  ↳ *example-of* `g10-0267`

- `g10-0198` *STATED* — Open Design is a free, open-source alternative to Claude Design for websites, app screens and decks without burning your Claude limit.
  — [g-open-design-the-free-claude-design-alternative](https://chen.media/guides/open-design-the-free-claude-design-alternative)
  ↳ *example-of* `g10-0267`

- `g10-0223` *STATED* — Dyad is a free, open-source app builder: type what you want and Claude builds a real web app on your own computer, with a live preview, a database and user logins.
  — [g-dyad-the-free-open-source-lovable](https://chen.media/guides/dyad-the-free-open-source-lovable)

- `g10-0247` *CORE* — Find Skills (from Vercel Labs) is a Claude skill where you tell Claude what you need and it checks the skills leaderboard, skips the skills nobody trusts, and installs the best one for the job.
  — [g-find-skills-the-most-installed-claude-skill](https://chen.media/guides/find-skills-the-most-installed-claude-skill)

- `g11-0011` *STATED* — Instatic is a free, open-source visual site builder that does Framer's job: you design pages on a canvas and it publishes them.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *example-of* `g11-0004`

- `g11-0181` *STATED* — FluidVoice is a free, open-source Mac app: press one key, talk, and a cleaned-up version of what you said is typed into any app, from Claude to Slack.
  — [g-fluidvoice-the-free-open-source-wispr-flow](https://chen.media/guides/fluidvoice-the-free-open-source-wispr-flow)
  ↳ *example-of* `g11-0004`

- `g11-0198` *STATED* — VoiceStudio is a free, open-source app that clones your voice from a few seconds of audio, reads books aloud, types what you say and dubs your videos into other languages, all on your own machine.
  — [g-the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer](https://chen.media/guides/the-free-open-source-elevenlabs-clone-your-voice-on-your-own-computer)
  ↳ *example-of* `g11-0004`

- `g12-0051` *STATED* — A free, open-source go-live skill for Claude Code looks at your app, works out everything it needs to go live, shows you the plan, and only then sets it up on your own accounts.
  — [g-take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments](https://chen.media/guides/take-your-claude-built-app-live-the-free-skill-that-sets-up-hosting-database-domain-email-and-payments)
  ↳ *part-of* `g12-0050`
  ↳ *example-of* `g12-0163`
  ↳ *evidence-for* `g02-0080`

- `g12-0098` *STATED* — Anthropic has built a prompt-audit command into its own Claude Code skill that finds legacy prompt patterns in your files and proposes the fix.
  — [g-clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit](https://chen.media/guides/clean-up-your-claude-md-for-opus-5-5-with-anthropic-s-prompt-audit)
  ↳ *part-of* `g12-0091`
  ↳ *part-of* `g12-0107`

- `g12-0131` *STATED* — A free, open-source SEO skill for Claude Code runs an agency-style website audit with one command, on your own site or a client's.
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *part-of* `g12-0129`
  ↳ *example-of* `g12-0163`
  ↳ *evidence-for* `g17-0099`

- `g12-0172` *STATED* — Fast-Jev Compaction is an open-source Claude Code plugin that frees up context by dropping only old tool output and keeps every word you and Claude wrote.
  — [g-stop-claude-code-s-compact-from-summarizing-away-your-chat](https://chen.media/guides/stop-claude-code-s-compact-from-summarizing-away-your-chat)
  ↳ *example-of* `g12-0162`
  ↳ *part-of* `g12-0171`
  ↳ *example-of* `g02-0241`

- `g12-0193` *STATED* — SupoClip also has a hosted version at supoclip.com and an iOS app for people who'd rather not run anything themselves.
  — [g-supoclip-open-source-opusclip-alternative](https://chen.media/guides/supoclip-open-source-opusclip-alternative)
  ↳ *qualifies* `g12-0187`

- `g12-0251` *STATED* — The FIX skill is a Claude skill that checks your own app for the same bugs Anthropic found slowing claude.ai, such as an em dash that froze the page and a reload nobody could see.
  — [g-how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill](https://chen.media/guides/how-anthropic-made-claude-ai-3x-faster-and-the-fix-skill)
  ↳ *example-of* `g12-0163`
  ↳ *part-of* `g12-0250`

- `g13-0001` *STATED* — Bot Crossing is a free, open-source game by Jarren Rocks that shows every coding-agent session on your computer as a little bot in a 3D colony.
  > “Bot Crossing is a free, open-source game by Jarren Rocks that shows every coding-agent session on your computer as a little bot in a 3D colony.”
  — [g-watch-every-claude-code-session-as-a-bot-in-bot-crossing](https://chen.media/guides/watch-every-claude-code-session-as-a-bot-in-bot-crossing)

- `g13-0061` *STATED* — Scrapling is the open-source scraping framework behind Alex's SCRAPE reel.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)

- `g13-0119` *STATED* — /watch is a free, open-source Claude Code skill made by bradautomates on GitHub that teaches Claude to watch videos.
  — [g-let-claude-code-watch-any-video-with-watch](https://chen.media/guides/let-claude-code-watch-any-video-with-watch)

- `g13-0136` *CORE* — claude-mem is a free, open-source memory plugin for Claude Code that lets Claude remember your past sessions.
  — [g-give-claude-code-a-memory-with-claude-mem](https://chen.media/guides/give-claude-code-a-memory-with-claude-mem)
  ↳ *contrast* `g13-0134` — the fix
  ↳ *example-of* `g13-0291` — claude-mem is the Claude Mem system in the SKILL reel

- `g13-0189` *STATED* — HackingTool brings security utilities into one terminal workspace.
  — [g-hackingtool-secure-your-own-apps](https://chen.media/guides/hackingtool-secure-your-own-apps)

- `g14-0044` *STATED* — OpenCut is an independent open-source video editor.
  — [g-opencut-repo-and-setup-guide](https://chen.media/guides/opencut-repo-and-setup-guide)
  ↳ *part-of* `g14-0043`

- `g14-0047` *STATED* — The official OpenCut site offers an early-beta browser editor.
  > “Open the OpenCut early beta”
  — [g-opencut-repo-and-setup-guide](https://chen.media/guides/opencut-repo-and-setup-guide)
  ↳ *part-of* `g14-0043`
  ↳ *enables* `g14-0048`

- `g14-0059` *STATED* — AIsa connects a coding agent to external data services.
  > “AIsa connects an agent to external data services”
  — [g-headroom-claude-hud-aisa-setup](https://chen.media/guides/headroom-claude-hud-aisa-setup)
  ↳ *part-of* `g14-0056`

- `g14-0073` *STATED* — Google Antigravity can be used from inside VS Code through Google's official extension.
  — [g-antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you](https://chen.media/guides/antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you)
  ↳ *part-of* `g14-0072`
  ↳ *depends-on* `g14-0075`
  ↳ *evidence-for* `g16-0228`

- `g14-0101` *STATED* — Agent Reach helps a command-capable AI agent gather information from supported websites.
  — [g-agent-reach-web-research-setup](https://chen.media/guides/agent-reach-web-research-setup)
  ↳ *part-of* `g14-0100`

- `g14-0222` *STATED* — ECC is an open-source collection of skills, agents, hooks and workflow patterns by Affaan Mustafa.
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *part-of* `g14-0220`

- `g14-0307` *STATED* — Human Scope is a downloadable Claude editorial skill Alex made from the StoryScope research for improving Claude-written fiction.
  > “The editorial tool I made from it”
  — [g-human-scope-storyscope-claude-writing-skill](https://chen.media/guides/human-scope-storyscope-claude-writing-skill)
  ↳ *part-of* `g14-0306`
  ↳ *depends-on* `g14-0309`

- `g15-0001` *STATED* — Four free-to-start UI component libraries make an AI-built site look designed: Skiper UI, Vengeance UI, Animmaster Lib and React Bits.
  — [g-four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed](https://chen.media/guides/four-free-to-start-ui-libraries-that-make-an-ai-built-site-look-designed)

- `g15-0016` *STATED* — MarkItDown is Microsoft's free, open-source (MIT) converter that does one job: it takes almost any file and hands back clean Markdown text.
  — [g-why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix](https://chen.media/guides/why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix)
  ↳ *example-of* `g15-0180`
  ↳ *example-of* `g02-0241`

- `g15-0041` *STATED* — sergebulaev/linkedin-skills is an open-source bundle of eleven skills for Claude Code and Codex that write, comment, reply, plan and scrub your LinkedIn.
  — [g-linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes](https://chen.media/guides/linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes)
  ↳ *example-of* `g15-0184`

- `g15-0053` *STATED* — The Claude Code skill named adhd does parallel divergent ideation: it splits a question into five isolated agent branches under different framings, scores them, prunes, and deepens the best three. It is for thinking wider, not verifying work (around 4,000 stars, MIT).
  — [g-claude-code-says-done-before-it-has-proved-anything-this-fixes-it](https://chen.media/guides/claude-code-says-done-before-it-has-proved-anything-this-fixes-it)
  ↳ *example-of* `g15-0052`
  ↳ *contrast* `g15-0055` — ideation, not verification

- `g15-0054` *STATED* — The Claude Code skill named i-have-adhd fixes output formatting so the agent stops burying the answer under preamble; it is very widely starred and is also not a verifier.
  — [g-claude-code-says-done-before-it-has-proved-anything-this-fixes-it](https://chen.media/guides/claude-code-says-done-before-it-has-proved-anything-this-fixes-it)
  ↳ *example-of* `g15-0052`
  ↳ *contrast* `g15-0055` — formatting, not verification

- `g15-0063` *STATED* — firecrawl/anydoc (MIT, over 20,000 stars on 5 September 2026) converts Word, PowerPoint, Excel, PDF and more into clean Markdown.
  — [g-four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute](https://chen.media/guides/four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute)
  ↳ *part-of* `g15-0061`
  ↳ *enables* `g15-0064`
  ↳ *example-of* `g15-0180`
  ↳ *example-of* `g15-0176`
  ↳ *contrast* `g15-0016` — two free to-Markdown converters: anydoc (firecrawl) vs MarkItDown (Microsoft)

- `g15-0067` *STATED* — deepseek-ai/deepseek-harness (MIT, over 212,000 stars) is an agent runtime where every part, including the model, is a plugin you can swap.
  — [g-four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute](https://chen.media/guides/four-repos-that-upgrade-your-claude-setup-anydoc-herdr-deepseek-harness-and-omniroute)
  ↳ *part-of* `g15-0061`
  ↳ *enables* `g15-0068`
  ↳ *example-of* `g16-0013`

- `g15-0117` *STATED* — The Agency has a native desktop app for macOS, Windows and Linux that installs the agents for you.
  — [g-the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install](https://chen.media/guides/the-free-ai-agency-273-specialist-claude-code-agents-and-which-ones-to-install)
  ↳ *part-of* `g15-0113`
  ↳ *enables* `g15-0119`
  ↳ *part-of* `g08-0089`

- `g16-0047` *STATED* — deepclaude is his lever-one repo for the RATE: it changes who you buy Claude Code's tokens from.
  > “Lever one, the RATE. deepclaude”
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you)
  ↳ *example-of* `g16-0044`
  ↳ *example-of* `g16-0013`

- `g16-0049` *STATED* — caveman is his lever-two repo for the VOLUME: it cuts the prose the model writes around the code.
  > “Lever two, the VOLUME. caveman”
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you)
  ↳ *example-of* `g16-0045`
  ↳ *evidence-for* `g03-0100`
  ↳ *example-of* `g02-0241`

- `g16-0051` *STATED* — super-token-saver is his lever-three repo for the WASTE: tokens you pay for twice because of the cache clock.
  > “Lever three, the WASTE. super-token-saver”
  — [g-three-free-repos-that-cut-what-claude-code-costs-you](https://chen.media/guides/three-free-repos-that-cut-what-claude-code-costs-you)
  ↳ *example-of* `g16-0046`

- `g16-0141` *STATED* — Unlazy is a free, MIT licensed Claude skill by Leon Lin that stops Claude saying it is done when it is not.
  > “Unlazy is a free, MIT licensed skill by Leon Lin.”
  — [g-the-free-skill-that-stops-claude-saying-done-when-it-is-not](https://chen.media/guides/the-free-skill-that-stops-claude-saying-done-when-it-is-not)
  ↳ *example-of* `g16-0001`
  ↳ *example-of* `g16-0008`

- `g16-0224` *STATED* — Google AI Studio, at aistudio.google.com, replaces paying for a chat window.
  > “AI Studio, instead of paying for a chat window”
  — [g-five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for](https://chen.media/guides/five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for)
  ↳ *example-of* `g16-0218`

- `g16-0225` *STATED* — NotebookLM, at notebooklm.google.com, replaces trusting a general model with your own material.
  > “NotebookLM, instead of trusting a general model with your own material”
  — [g-five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for](https://chen.media/guides/five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for)
  ↳ *example-of* `g16-0218`

- `g16-0226` *STATED* — Google Flow, at labs.google/fx/tools/flow, replaces a monthly video generation subscription.
  > “Flow, instead of a monthly video generation subscription”
  — [g-five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for](https://chen.media/guides/five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for)
  ↳ *example-of* `g16-0218`

- `g16-0227` *STATED* — Google Opal, at opal.google, replaces building a small internal tool from scratch.
  > “Opal, instead of building a small internal tool from scratch”
  — [g-five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for](https://chen.media/guides/five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for)
  ↳ *example-of* `g16-0218`

- `g16-0228` *STATED* — Google Antigravity, at antigravity.google, replaces a paid agentic IDE seat.
  > “Antigravity, instead of a paid agentic IDE seat”
  — [g-five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for](https://chen.media/guides/five-free-google-ai-tools-that-replace-the-subscriptions-you-are-still-paying-for)
  ↳ *example-of* `g16-0218`
  ↳ *contrast* `g16-0253` — Antigravity as a free agentic IDE vs his coding pick Claude Code (Cursor 2nd)

- `g16-0270` *STATED* — Prompt Master is a free, MIT licensed Claude skill: you describe what you want in whatever shape it comes out of your head, and it hands back a single clean prompt you can paste into any AI tool.
  — [g-the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting](https://chen.media/guides/the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting)
  ↳ *because* `g16-0278`
  ↳ *example-of* `g16-0001`
  ↳ *example-of* `g16-0008`

- `g16-0283` *STATED* — Claude Code Setup is the official Anthropic plugin: it scans your repo and tells you what to install.
  > “Claude Code Setup, the official Anthropic one”
  — [g-three-plugins-that-fix-claude-code-s-setup-limits-and-memory](https://chen.media/guides/three-plugins-that-fix-claude-code-s-setup-limits-and-memory)
  ↳ *part-of* `g16-0282`
  ↳ *example-of* `g16-0288` — fixes: you do not know what to configure

- `g16-0285` *STATED* — Claude Mem is the plugin that stops you re-explaining your project every session, so you stop starting from zero.
  > “Claude Mem, so you stop starting from zero”
  — [g-three-plugins-that-fix-claude-code-s-setup-limits-and-memory](https://chen.media/guides/three-plugins-that-fix-claude-code-s-setup-limits-and-memory)
  ↳ *part-of* `g16-0282`
  ↳ *part-of* `g16-0012`
  ↳ *evidence-for* `g13-0136`

- `g17-0001` *STATED* — Alex Chen's chen.media guide 'Seven Free Claude Skills That Cover a Marketing Department' maps every job a marketing retainer covers to a free Claude skill, listed in the order you should install them.
  > “Every job a retainer covers, mapped to a free Claude skill, in the order you should install them”
  — [g-seven-free-claude-skills-that-cover-a-marketing-department](https://chen.media/guides/seven-free-claude-skills-that-cover-a-marketing-department)

- `g17-0069` *STATED* — Alex Chen's 'Three Free AI Sites for Chat, Video and Images' guide gives the exact links, what each site actually gives you, and where its free tier stops.
  > “The exact links, what each one actually gives you, and where the free tier stops”
  — [g-three-free-ai-sites-for-chat-video-and-images](https://chen.media/guides/three-free-ai-sites-for-chat-video-and-images)
  ↳ *example-of* `g17-0305`

- `g17-0070` *STATED* — Arena (arena.ai): every frontier model in one chat box, free.
  > “Arena (arena.ai): every frontier model, one chat box, free”
  — [g-three-free-ai-sites-for-chat-video-and-images](https://chen.media/guides/three-free-ai-sites-for-chat-video-and-images)
  ↳ *part-of* `g17-0069`
  ↳ *example-of* `g17-0313`

- `g17-0071` *STATED* — Magnific, formerly Freepik (magnific.com): Kling, Sora and Seedance video models in one generator.
  > “Magnific, formerly Freepik (magnific.com): Kling, Sora and Seedance in one generator”
  — [g-three-free-ai-sites-for-chat-video-and-images](https://chen.media/guides/three-free-ai-sites-for-chat-video-and-images)
  ↳ *part-of* `g17-0069`

- `g17-0072` *STATED* — Google AI Studio (aistudio.google.com): free Nano Banana image generation.
  > “Google AI Studio (aistudio.google.com): Nano Banana image generation”
  — [g-three-free-ai-sites-for-chat-video-and-images](https://chen.media/guides/three-free-ai-sites-for-chat-video-and-images)
  ↳ *part-of* `g17-0069`
  ↳ *evidence-for* `g16-0224`

- `g17-0086` *STATED* — Alex Chen's three Claude Code plugins worth installing are Awesome APIs, Find Skills and Claude Mem, all free and open source.
  — [g-the-three-claude-code-plugins-worth-installing](https://chen.media/guides/the-three-claude-code-plugins-worth-installing)
  ↳ *contrast* `g18-0154`

- `g17-0099` *STATED* — Claude SEO installs 25 SEO skills and 18 specialist agents into Claude Code and produces a prioritised action plan for any site in about fifteen minutes.
  — [g-install-25-seo-skills-and-18-specialist-agents-into-claude-code](https://chen.media/guides/install-25-seo-skills-and-18-specialist-agents-into-claude-code)

- `g17-0143` *STATED* — FreeLLMAPI is an MIT-licensed proxy that stacks the free tiers of many AI providers.
  > “FreeLLMAPI is an MIT licensed proxy that stacks them.”
  — [g-pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint](https://chen.media/guides/pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint)
  ↳ *contrast* `g17-0142` — stacking turns toys into capacity
  ↳ *enables* `g17-0150`
  ↳ *example-of* `g17-0313`
  ↳ *example-of* `g16-0013`

- `g17-0155` *STATED* — Project NOMAD is a knowledge server that keeps answering after the internet stops.
  > “Project NOMAD: a knowledge server that keeps answering after the internet stops.”
  — [g-a-knowledge-server-that-keeps-answering-with-the-internet-off](https://chen.media/guides/a-knowledge-server-that-keeps-answering-with-the-internet-off)

- `g17-0224` *STATED* — Alex Chen's guide to the 164-skill ComposioHQ repo says which skills to take first and which to leave.
  > “Which ones to take first, and which to leave.”
  — [g-164-claude-skills-in-one-repo-which-to-take-first](https://chen.media/guides/164-claude-skills-in-one-repo-which-to-take-first)
  ↳ *qualifies* `g17-0223`

- `g17-0268` *STATED* — Anil Matcha's Open Generative AI is an MIT-licensed desktop app that puts 400+ image and video models behind one interface.
  — [g-400-ai-image-and-video-models-in-one-free-desktop-app](https://chen.media/guides/400-ai-image-and-video-models-in-one-free-desktop-app)

- `g17-0274` *STATED* — Open Generative AI's Cinema Studio is the part most people miss.
  > “Cinema Studio, the part most people miss”
  — [g-400-ai-image-and-video-models-in-one-free-desktop-app](https://chen.media/guides/400-ai-image-and-video-models-in-one-free-desktop-app)
  ↳ *part-of* `g17-0277`
  ↳ *part-of* `g17-0268`

- `g18-0031` *STATED* — Notes: replace Notion ($20/month) with Obsidian ($0).
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0024`

- `g18-0032` *STATED* — Scheduling: replace Calendly ($16/month) with Cal.com ($0).
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0024`

- `g18-0033` *STATED* — Cloud storage: replace Dropbox ($24/month) with Nextcloud ($0).
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0024`

- `g18-0034` *STATED* — Automation: replace Zapier ($69/month) with n8n ($0).
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0024`
  ↳ *evidence-for* `g18-0150` — same swap in both lists

- `g18-0035` *STATED* — Design: replace Figma ($90/month) with Penpot ($0).
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0024`
  ↳ *evidence-for* `g18-0148` — same swap in both lists
  ↳ *contrast* `g18-0204` — Figma replacement: Penpot vs OpenPencil

- `g18-0037` *STATED* — Whiteboard: replace Miro ($20/month) with Excalidraw ($0).
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0024`

- `g18-0038` *STATED* — Meeting notes: replace Otter.ai ($30/month) with Granola ($0).
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0024`
  ↳ *contrast* `g18-0144` — Otter replaced by Granola in one list, Whisper in the other

- `g18-0039` *STATED* — Databases: replace Airtable ($45/month) with Baserow ($0).
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0024`

- `g18-0040` *STATED* — Screen recording: replace Loom ($24/month) with OBS Studio ($0).
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0024`
  ↳ *evidence-for* `g18-0149` — same swap in both lists

- `g18-0041` *STATED* — Forms: replace Typeform ($99/month) with Google Forms ($0).
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0024`

- `g18-0042` *STATED* — Analytics: replace Mixpanel ($99/month) with PostHog ($0).
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0024`

- `g18-0044` *STATED* — Translation: replace DeepL ($58/month) with LibreTranslate ($0).
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0024`

- `g18-0046` *STATED* — Passwords: replace 1Password ($8/month) with Bitwarden ($0).
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0024`

- `g18-0047` *STATED* — Support chat: replace Intercom ($139/month) with Chatwoot ($0); the most expensive tool on the list.
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0024`

- `g18-0048` *STATED* — Tasks: replace Todoist ($6/month) with Vikunja ($0).
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0024`

- `g18-0054` *STATED* — Graphify parses a repository once into a graph that Claude Code can query, instead of re-reading the repo every session.
  — [g-stop-claude-code-re-reading-your-repo-every-session](https://chen.media/guides/stop-claude-code-re-reading-your-repo-every-session)
  ↳ *example-of* `g18-0289`
  ↳ *example-of* `g18-0278`
  ↳ *analogy-for* `g01-0087`
  ↳ *example-of* `g02-0241`

- `g18-0078` *STATED* — Animation skill 1 of 5: Three.js, repo CloudAI-X/threejs-skills.
  — [g-five-animation-skills-for-claude-code-with-install-commands](https://chen.media/guides/five-animation-skills-for-claude-code-with-install-commands)
  ↳ *part-of* `g18-0077`

- `g18-0079` *STATED* — Animation skill 2 of 5: GSAP, repo greensock/gsap-skills.
  — [g-five-animation-skills-for-claude-code-with-install-commands](https://chen.media/guides/five-animation-skills-for-claude-code-with-install-commands)
  ↳ *part-of* `g18-0077`

- `g18-0081` *STATED* — Animation skill 4 of 5: Motion Design, repo LottieFiles/motion-design-skill.
  — [g-five-animation-skills-for-claude-code-with-install-commands](https://chen.media/guides/five-animation-skills-for-claude-code-with-install-commands)
  ↳ *part-of* `g18-0077`

- `g18-0082` *STATED* — Animation skill 5 of 5: Genjutsu, repo AThevon/genjutsu.
  — [g-five-animation-skills-for-claude-code-with-install-commands](https://chen.media/guides/five-animation-skills-for-claude-code-with-install-commands)
  ↳ *part-of* `g18-0077`

- `g18-0086` *CORE* — Most of the animation skills install through `npx skills`, a third-party CLI that works with Claude Code, Cursor, Codex, Copilot and 40 or so other agents.
  — [g-five-animation-skills-for-claude-code-with-install-commands](https://chen.media/guides/five-animation-skills-for-claude-code-with-install-commands)
  ↳ *enables* `g18-0077`
  ↳ *part-of* `g17-0090`

- `g18-0092` *STATED* — Open Generative AI is a free, MIT-licensed app by Anil Matcha that puts image generation, video generation, lip sync and a cinema camera studio into one interface.
  — [g-the-open-source-ai-studio-that-replaces-a-video-subscription](https://chen.media/guides/the-open-source-ai-studio-that-replaces-a-video-subscription)
  ↳ *example-of* `g18-0287`
  ↳ *example-of* `g18-0288`
  ↳ *contrast* `g18-0201` — both pitched against paid AI video subscriptions
  ↳ *evidence-for* `g17-0268`

- `g18-0114` *STATED* — Exa is a search MCP server that returns clean, ready-to-use content directly instead of links, and matches on meaning rather than keywords.
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again)
  ↳ *part-of* `g18-0111`

- `g18-0121` *STATED* — Playwright MCP drives a real browser, which is what lets Claude open a page and click through it; the guide explains the reason it works.
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again)
  ↳ *part-of* `g18-0111`

- `g18-0122` *STATED* — Firecrawl MCP reads one page, or the whole site.
  > “Firecrawl: one page, or the whole site”
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again)
  ↳ *part-of* `g18-0111`

- `g18-0123` *STATED* — Context7 MCP gives Claude version-specific library docs straight from the source.
  > “Context7: version specific docs, straight from the source”
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again)
  ↳ *part-of* `g18-0111`

- `g18-0129` *STATED* — Free swap 01 of 25 (Alex's 25 free replacements): Image creation: replace Midjourney with Nano Banana.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`
  ↳ *contradicts* `g23-0191` — Midjourney replacement: Nano Banana (25 free replacements) vs Leonardo (hype swaps)

- `g18-0130` *STATED* — Free swap 02 of 25 (Alex's 25 free replacements): Replace Perplexity with Consensus.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`
  ↳ *evidence-for* `g17-0200`

- `g18-0131` *STATED* — Free swap 03 of 25 (Alex's 25 free replacements): Replace HeyGen with Hedra.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`

- `g18-0132` *STATED* — Free swap 04 of 25 (Alex's 25 free replacements): Replace GitHub Copilot with Cursor.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`
  ↳ *evidence-for* `g17-0204`

- `g18-0133` *STATED* — Free swap 05 of 25 (Alex's 25 free replacements): Replace Runway ML with Stable Diffusion.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`
  ↳ *contradicts* `g23-0190` — Runway replacement: Stable Diffusion (25 free replacements) vs Higgsfield (hype swaps)

- `g18-0134` *STATED* — Free swap 06 of 25 (Alex's 25 free replacements): Replace Adobe Firefly with Photoroom.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`

- `g18-0135` *STATED* — Free swap 07 of 25 (Alex's 25 free replacements): Replace Higgsfield with Hailuo.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`
  ↳ *evidence-for* `g17-0206`

- `g18-0136` *STATED* — Free swap 08 of 25 (Alex's 25 free replacements): Replace Buffer with Publer.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`

- `g18-0137` *STATED* — Free swap 09 of 25 (Alex's 25 free replacements): Replace Canva with Lovart.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`

- `g18-0138` *STATED* — Free swap 10 of 25 (Alex's 25 free replacements): Replace Framer AI with Durable.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`
  ↳ *contradicts* `g17-0212` — free Framer swap: 25-replacements guide says Durable; ten-tools guide says Lovable
  ↳ *contrast* `g11-0014` — Framer replacement: Durable vs Instatic

- `g18-0139` *STATED* — Free swap 11 of 25 (Alex's 25 free replacements): Replace CapCut with Edits.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`
  ↳ *evidence-for* `g17-0214`

- `g18-0140` *STATED* — Free swap 12 of 25 (Alex's 25 free replacements): Replace Suno with Udio.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`

- `g18-0141` *STATED* — Free swap 13 of 25 (Alex's 25 free replacements): Replace ElevenLabs with MiniMax.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`
  ↳ *contrast* `g11-0198` — ElevenLabs replacement: MiniMax vs VoiceStudio

- `g18-0142` *STATED* — Free swap 14 of 25 (Alex's 25 free replacements): Replace Surfer SEO with Ubersuggest.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`

- `g18-0143` *STATED* — Free swap 15 of 25 (Alex's 25 free replacements): Replace Jasper AI with Copy.ai.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`

- `g18-0144` *STATED* — Free swap 16 of 25 (Alex's 25 free replacements): Replace Otter with Whisper.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`

- `g18-0145` *STATED* — Free swap 17 of 25 (Alex's 25 free replacements): Replace Fireflies with Tactiq.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`

- `g18-0146` *STATED* — Free swap 18 of 25 (Alex's 25 free replacements): Replace Grammarly with LanguageTool.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`

- `g18-0147` *STATED* — Free swap 19 of 25 (Alex's 25 free replacements): Replace Topaz with Upscayl.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`

- `g18-0148` *STATED* — Free swap 20 of 25 (Alex's 25 free replacements): Replace Figma with Penpot.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`

- `g18-0149` *STATED* — Free swap 21 of 25 (Alex's 25 free replacements): Replace Loom with OBS Studio.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`

- `g18-0150` *STATED* — Free swap 22 of 25 (Alex's 25 free replacements): Replace Zapier with n8n.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`

- `g18-0151` *STATED* — Free swap 23 of 25 (Alex's 25 free replacements): Replace ChatPDF with NotebookLM.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`
  ↳ *contrast* `g18-0183` — NotebookLM as ChatPDF replacement vs as Claude memory store
  ↳ *evidence-for* `g16-0225`

- `g18-0152` *STATED* — Free swap 24 of 25 (Alex's 25 free replacements): Replace ChatGPT Plus with Ollama.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`

- `g18-0153` *STATED* — Free swap 25 of 25 (Alex's 25 free replacements): Replace remove.bg with Rembg.
  — [g-25-free-replacements-for-paid-ai-tools](https://chen.media/guides/25-free-replacements-for-paid-ai-tools)
  ↳ *part-of* `g18-0125`

- `g18-0165` *STATED* — Plugin 1 of 5: the official Anthropic skills, with a section on what comes in the box.
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *part-of* `g18-0154`

- `g18-0168` *STATED* — Plugin 3 of 5: claude-obsidian, the second brain; the guide singles out the skills in it that matter.
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *part-of* `g18-0154`
  ↳ *contrast* `g18-0183` — Obsidian second brain vs NotebookLM second brain

- `g18-0174` *STATED* — Alex's video skill makes Claude watch a video instead of reading about it.
  — [g-the-skill-that-makes-claude-watch-a-video-not-read-about-it](https://chen.media/guides/the-skill-that-makes-claude-watch-a-video-not-read-about-it)
  ↳ *part-of* `g13-0119`

- `g18-0191` *STATED* — G0DM0D3 is a single HTML file that runs ChatGPT, Claude, Gemini and Grok side by side in your browser.
  — [g-one-html-file-that-runs-chatgpt-claude-gemini-and-grok-side-by-side](https://chen.media/guides/one-html-file-that-runs-chatgpt-claude-gemini-and-grok-side-by-side)
  ↳ *evidence-for* `y04-0091`

- `g18-0200` *STATED* — Open source replacement 1 (most stars): AppFlowy instead of Notion.
  — [g-five-paid-apps-with-full-open-source-replacements](https://chen.media/guides/five-paid-apps-with-full-open-source-replacements)
  ↳ *contrast* `g18-0031` — Notion replaced by AppFlowy vs Obsidian
  ↳ *part-of* `g18-0198`

- `g18-0201` *STATED* — Open source replacement 2: OpenMontage instead of HiggsField.
  — [g-five-paid-apps-with-full-open-source-replacements](https://chen.media/guides/five-paid-apps-with-full-open-source-replacements)
  ↳ *contrast* `g18-0135` — Higgsfield replaced by OpenMontage vs Hailuo
  ↳ *part-of* `g18-0198`

- `g18-0202` *STATED* — Open source replacement 3: Jan instead of ChatGPT Plus.
  — [g-five-paid-apps-with-full-open-source-replacements](https://chen.media/guides/five-paid-apps-with-full-open-source-replacements)
  ↳ *contrast* `g18-0152` — ChatGPT Plus replaced by Jan vs Ollama
  ↳ *part-of* `g18-0198`

- `g18-0203` *STATED* — Open source replacement 4: Presenton instead of Canva.
  — [g-five-paid-apps-with-full-open-source-replacements](https://chen.media/guides/five-paid-apps-with-full-open-source-replacements)
  ↳ *contrast* `g18-0137` — Canva replaced by Presenton vs Lovart
  ↳ *part-of* `g18-0198`

- `g18-0204` *STATED* — Open source replacement 5: OpenPencil instead of Figma.
  — [g-five-paid-apps-with-full-open-source-replacements](https://chen.media/guides/five-paid-apps-with-full-open-source-replacements)
  ↳ *contrast* `g18-0148` — Figma replaced by OpenPencil vs Penpot
  ↳ *part-of* `g18-0198`

- `g18-0273` *STATED* — Last 30 Days: mvanhorn/last30days-skill, 54.8k stars, MIT.
  — [g-seven-free-repos-that-replace-paid-ai-tools](https://chen.media/guides/seven-free-repos-that-replace-paid-ai-tools)
  ↳ *part-of* `g18-0262`

- `g18-0274` *STATED* — Open Montage: calesthio/OpenMontage, 43.6k stars, AGPL-3.0.
  — [g-seven-free-repos-that-replace-paid-ai-tools](https://chen.media/guides/seven-free-repos-that-replace-paid-ai-tools)
  ↳ *defines* `g18-0201` — OpenMontage repo is calesthio/OpenMontage, AGPL-3.0
  ↳ *part-of* `g18-0262`

- `g19-0102` *STATED* — ComfyUI (github.com/comfyanonymous/ComfyUI, 122k stars) is tool 1 of 5: the free studio behind most of the AI images and video you have seen.
  > “The free studio behind most of the AI images and video you have seen.”
  — [g-five-free-repos-that-give-claude-actual-hands](https://chen.media/guides/five-free-repos-that-give-claude-actual-hands)
  ↳ *part-of* `g19-0101`

- `g19-0105` *STATED* — Duix-Avatar (14k stars) is tool 2 of 5, the repo that puts a real face and voice on camera.
  > “Duix-Avatar · 14k stars”
  — [g-five-free-repos-that-give-claude-actual-hands](https://chen.media/guides/five-free-repos-that-give-claude-actual-hands)
  ↳ *part-of* `g19-0101`

- `g19-0106` *STATED* — Presenton (9k stars), which Alex calls 'the sleeper', is tool 3 of 5, the repo that builds a full slide deck.
  > “Presenton · 9k stars (the sleeper)”
  — [g-five-free-repos-that-give-claude-actual-hands](https://chen.media/guides/five-free-repos-that-give-claude-actual-hands)
  ↳ *part-of* `g19-0101`
  ↳ *evidence-for* `g18-0203`

- `g19-0107` *STATED* — whisper.cpp (52k stars) is tool 4 of 5, the repo that gives Claude ears.
  > “whisper.cpp · 52k stars”
  — [g-five-free-repos-that-give-claude-actual-hands](https://chen.media/guides/five-free-repos-that-give-claude-actual-hands)
  ↳ *part-of* `g19-0101`
  ↳ *evidence-for* `g18-0144`

- `g19-0157` *STATED* — Repomix: yamadashy/repomix, 27.2k stars, MIT, https://github.com/yamadashy/repomix.
  > “Yamadashy / Repomix . 27.2k Stars . Mit”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *part-of* `g19-0155`
  ↳ *qualifies* `g19-0162`

- `g19-0158` *STATED* — Graphiti: getzep/graphiti, 28.9k stars, open source, https://github.com/getzep/graphiti.
  > “Getzep / Graphiti . 28.9k Stars . Open Source”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *part-of* `g19-0155`

- `g19-0180` *STATED* — Serena (github.com/oraios/serena, over 26,000 stars) is a free, MIT-licensed, open-source MCP server.
  > “a free, MIT licensed, open source MCP server”
  — [g-give-claude-code-an-ide-brain-so-it-stops-reading-everything](https://chen.media/guides/give-claude-code-an-ide-brain-so-it-stops-reading-everything)
  ↳ *qualifies* `g19-0178`
  ↳ *example-of* `g16-0014`

- `g20-0259` *STATED* — MCP 1, Exa: AI search that reads pages; it replaces a paid research/search tool.
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *part-of* `g20-0255`
  ↳ *evidence-for* `g18-0114`

- `g20-0263` *STATED* — MCP 2, Apify: 5,000 ready-made scrapers; it replaces your web-scraping subscription.
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *part-of* `g20-0255`

- `g20-0267` *STATED* — MCP 3, Unstructured: turns ugly docs into clean data; it replaces a $100s/mo document-parsing service.
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *part-of* `g20-0255`
  ↳ *analogy-for* `g15-0016`

- `g20-0271` *STATED* — MCP 4, Magic by 21st.dev: describe UI and get real React; it replaces a paid UI component kit.
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *part-of* `g20-0255`
  ↳ *part-of* `g20-0124` — 21st.dev Magic MCP
  ↳ *part-of* `g08-0143`

- `g20-0275` *STATED* — MCP 5, Context7: current docs for any library; it replaces debugging against dead APIs.
  > “Replaces: debugging against dead APIs”
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)
  ↳ *part-of* `g20-0255`
  ↳ *evidence-for* `g18-0123`

- `g21-0006` *STATED* — Superdesign is a Claude Code skill that gives Claude a real design canvas: it mocks up UI directions and hands back React + Tailwind code.
  — [g-five-claude-code-skills-with-the-install-command-for-each](https://chen.media/guides/five-claude-code-skills-with-the-install-command-for-each)
  ↳ *example-of* `g21-0004`

- `g21-0008` *CORE* — Superpowers (obra) is a plan-first Claude Code plugin team that writes a spec, spins up subagents, and refuses to write code before tests exist.
  — [g-five-claude-code-skills-with-the-install-command-for-each](https://chen.media/guides/five-claude-code-skills-with-the-install-command-for-each)
  ↳ *example-of* `g21-0004`

- `g21-0010` *STATED* — The Trail of Bits security audit skill runs professional static analysis (CodeQL, Semgrep) and flags real, reachable vulnerabilities.
  — [g-five-claude-code-skills-with-the-install-command-for-each](https://chen.media/guides/five-claude-code-skills-with-the-install-command-for-each)
  ↳ *example-of* `g21-0004`

- `g21-0012` *STATED* — The Karpathy skill (forrestchang/andrej-karpathy-skills) makes Claude touch only what the task needs, which stops it rewriting working code.
  > “Touch only what the task needs: stops Claude rewriting working code.”
  — [g-five-claude-code-skills-with-the-install-command-for-each](https://chen.media/guides/five-claude-code-skills-with-the-install-command-for-each)
  ↳ *example-of* `g21-0004`

- `g21-0014` *STATED* — The Playwright MCP server lets Claude drive a real browser, click through what it built, and fix what breaks (self-testing).
  — [g-five-claude-code-skills-with-the-install-command-for-each](https://chen.media/guides/five-claude-code-skills-with-the-install-command-for-each)
  ↳ *example-of* `g21-0004`
  ↳ *evidence-for* `g18-0121`

- `g22-0149` *STATED* — Meta released an official, native connector that plugs your Meta ad account straight into Claude.
  — [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)
  ↳ *defines* `g22-0146`
  ↳ *enables* `g22-0151`

- `g23-0108` *STATED* — Skill 1 of 5 on his must-install list is stop-slop.
  — [g-five-claude-skills-that-beat-99-of-users](https://chen.media/guides/five-claude-skills-that-beat-99-of-users)
  ↳ *part-of* `g23-0100`

- `g23-0109` *STATED* — Skill 2 of 5 on his must-install list is ClaudeMem.
  — [g-five-claude-skills-that-beat-99-of-users](https://chen.media/guides/five-claude-skills-that-beat-99-of-users)
  ↳ *part-of* `g23-0100`
  ↳ *evidence-for* `g13-0136`

- `g23-0110` *STATED* — Skill 3 of 5 on his must-install list is UI-UX Pro Max.
  — [g-five-claude-skills-that-beat-99-of-users](https://chen.media/guides/five-claude-skills-that-beat-99-of-users)
  ↳ *part-of* `g23-0100`

- `g23-0111` *STATED* — Skill 4 of 5 on his must-install list is Task Observer.
  — [g-five-claude-skills-that-beat-99-of-users](https://chen.media/guides/five-claude-skills-that-beat-99-of-users)
  ↳ *part-of* `g23-0100`

- `g23-0112` *STATED* — Skill 5 of 5 on his must-install list is Find Skills.
  — [g-five-claude-skills-that-beat-99-of-users](https://chen.media/guides/five-claude-skills-that-beat-99-of-users)
  ↳ *part-of* `g23-0100`
  ↳ *analogy-for* `g23-0106` — Find Skills searches the library like the install prompt does
  ↳ *evidence-for* `g10-0247`

- `g23-0152` *STATED* — The Chrome DevTools MCP lets Claude drive a live Chrome tab: click, fill forms, read the console and network, and find the exact error that broke your page.
  — [g-the-claude-plugins-cheat-sheet-add-once-then-just-ask](https://chen.media/guides/the-claude-plugins-cheat-sheet-add-once-then-just-ask)
  ↳ *part-of* `g23-0151`
  ↳ *enables* `g23-0068` — DevTools MCP lets Claude Code debug the live page
  ↳ *contrast* `g21-0014`

- `g23-0156` *STATED* — Plugin 02 on his MCP cheat sheet is Firecrawl.
  — [g-the-claude-plugins-cheat-sheet-add-once-then-just-ask](https://chen.media/guides/the-claude-plugins-cheat-sheet-add-once-then-just-ask)
  ↳ *part-of* `g23-0151`
  ↳ *evidence-for* `g18-0122`

- `g23-0157` *STATED* — Plugin 03 on his MCP cheat sheet is Figma.
  — [g-the-claude-plugins-cheat-sheet-add-once-then-just-ask](https://chen.media/guides/the-claude-plugins-cheat-sheet-add-once-then-just-ask)
  ↳ *part-of* `g23-0151`

- `g23-0158` *STATED* — Plugin 04 on his MCP cheat sheet is Blender.
  — [g-the-claude-plugins-cheat-sheet-add-once-then-just-ask](https://chen.media/guides/the-claude-plugins-cheat-sheet-add-once-then-just-ask)
  ↳ *part-of* `g23-0151`

- `g23-0159` *STATED* — Plugin 05 on his MCP cheat sheet is ElevenLabs.
  — [g-the-claude-plugins-cheat-sheet-add-once-then-just-ask](https://chen.media/guides/the-claude-plugins-cheat-sheet-add-once-then-just-ask)
  ↳ *part-of* `g23-0151`

- `r02-0004` *STATED* — The /hunter skill is free, MIT licensed, and needs no signup and no API key.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *qualifies* `r02-0001`
  ↳ *example-of* `r01-0001`

- `r02-0119` *STATED* — /launch is one Claude Code skill: free, MIT, no signup, no API key, nothing to connect.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *qualifies* `r02-0118`
  ↳ *example-of* `r01-0001`

- `r03-0001` *STATED* — The /learn skill (github.com/alexyc9381/learn-skill) is 'a Claude setup that stops making the same mistake twice, and runs on its own'.
  > “A Claude setup that stops making the same mistake twice, and runs on its own.”
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *depends-on* `r03-0003` — made by

- `r03-0002` *STATED* — The /learn skill is one Claude Code skill: free, MIT-licensed, no signup, no API key, nothing to connect.
  > “One Claude Code skill. Free, MIT, no signup, no API key, nothing to connect.”
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill)
  ↳ *qualifies* `r03-0001`
  ↳ *example-of* `r01-0001`

- `r03-0137` *STATED* — /linkedin-roast is free, MIT-licensed, with no signup and no API key.
  — [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *qualifies* `r03-0134`
  ↳ *example-of* `r01-0001`

- `r04-0023` *STATED* — /mentor (github.com/alexyc9381/mentor-skill) is one Claude Code plugin that makes you learn while you build.
  > “One Claude Code plugin that makes you learn while you build.”
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)

- `y01-0184` *STATED* — Alex replaced Higgsfield's whole platform with one Claude skill that routes the exact same prompts to the exact same models (via fal.ai).
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *evidence-for* `g18-0135`
  ↳ *contradicts* `g23-0201` — Higgsfield: recommended pick vs replaced with one fal.ai Claude skill to avoid the $100/month fee
  ↳ *depends-on* `y01-0191`

- `y02-0029` *STATED* — Breaking news per Alex Chen: 'Atomic' announced 'CloudMotion' (likely Claude Motion; transcript spelling uncertain), which turns any prompt into an animated explainer video.
  > “Atomic just announced CloudMotion, which turns any prompt into an animated explainer video”
  — [HWioULsQJWM](https://youtu.be/HWioULsQJWM)

- `y02-0033` *STATED* — 'The Agency' is an open-source GitHub project with over 124,000 stars that lets you run an entire AI agency inside Claude without spending a single dollar.
  > “It's called the agency and it's over 124,000 stars on GitHub.”
  — [SChgKT-vXHk](https://youtu.be/SChgKT-vXHk) [GaXO0ZKN4WI](https://youtu.be/GaXO0ZKN4WI) [Di7KzYJ7NwA](https://youtu.be/Di7KzYJ7NwA)
  ↳ *evidence-for* `g08-0089`

- `y02-0037` *STATED* — The Agency has a desktop app that installs your 'dream team' of agents in one click.
  > “there's even a desktop app that installs your dream team in one click”
  — [SChgKT-vXHk](https://youtu.be/SChgKT-vXHk) [GaXO0ZKN4WI](https://youtu.be/GaXO0ZKN4WI) [Di7KzYJ7NwA](https://youtu.be/Di7KzYJ7NwA)
  ↳ *evidence-for* `g15-0117`
  ↳ *part-of* `y02-0033`

- `y02-0047` *STATED* — Agent Office is a free 3D office where every worker at a desk is one of your Claude chat windows (CTA keyword 'desks').
  > “Someone built a 3D office where every worker at a desk is one of your chat windows. It's called Agent Office”
  — [qPP2IR9Dw3E](https://youtu.be/qPP2IR9Dw3E)
  ↳ *evidence-for* `g08-0205`

- `y02-0121` *STATED* — Someone open-sourced a free design skill (past 70,000 stars) that fixes the generic AI look (CTA keyword 'polish').
  > “someone open-sourced a design skill that fixes exactly this in its past 70,000 stars”
  — [c0r70JFGd3s](https://youtu.be/c0r70JFGd3s)

- `y02-0142` *STATED* — Cuckoo is a free, open-source cute tiny pet that lives in your Mac's notch and watches Claude for you (CTA keyword 'notch').
  > “Someone built a cute tiny pet that lives in your Mac's notch and watches Claude for you.”
  — [4iwKLOxgvZQ](https://youtu.be/4iwKLOxgvZQ) [DIJprXkxmIs](https://youtu.be/DIJprXkxmIs)
  ↳ *evidence-for* `g09-0232`

- `y02-0172` *STATED* — The free 'Logo Design Skill' gets you a finished logo from Claude (CTA keyword 'logo').
  > “You can now get a finished logo from Claude with this one free skill.”
  — [J8g3EZwZx20](https://youtu.be/J8g3EZwZx20)
  ↳ *evidence-for* `g09-0177`

- `y03-0084` *STATED* — Alex turned the writing-study rules into a permanent Claude skill called Straight Talk.
  — [mw5TnnOoHek](https://youtu.be/mw5TnnOoHek)
  ↳ *enables* `y03-0085`
  ↳ *example-of* `y03-0086`

- `y03-0100` *STATED* — Find Skills is one Claude skill that finds every other skill you need; Alex calls it the most powerful Claude skill on the planet that most people don't know exists.
  — [wfwnTNtnomk](https://youtu.be/wfwnTNtnomk) [1j9mmXDW8Qw](https://youtu.be/1j9mmXDW8Qw)
  ↳ *evidence-for* `g10-0247`

- `y03-0110` *STATED* — Open Design is a free, open-source version of Claude Design.
  — [NrJa3MCde-I](https://youtu.be/NrJa3MCde-I) [vdLceKphMoQ](https://youtu.be/vdLceKphMoQ)
  ↳ *evidence-for* `g10-0198`
  ↳ *contrast* `y03-0108` — the free way out

- `y03-0116` *STATED* — Dyad is one open-source GitHub repo that gives you Lovable without paying for it (name heard as 'the ad').
  — [cxLfDm8_Yx4](https://youtu.be/cxLfDm8_Yx4) [a8nVKYxwcjo](https://youtu.be/a8nVKYxwcjo) [udcHbDvy7o4](https://youtu.be/udcHbDvy7o4)
  ↳ *evidence-for* `g10-0223`
  ↳ *example-of* `y03-0198`

- `y03-0122` *STATED* — Instatic is one open-source GitHub repo that gives you Framer without paying for it.
  — [N8BCMjq3wPE](https://youtu.be/N8BCMjq3wPE) [23JOjnkdikY](https://youtu.be/23JOjnkdikY)
  ↳ *evidence-for* `g11-0011`
  ↳ *example-of* `y03-0198`

- `y03-0128` *STATED* — FluidVoice is one open-source GitHub repo that gives you Wispr Flow without paying for it.
  — [OtRSHXUQxAQ](https://youtu.be/OtRSHXUQxAQ) [4xBCskEhIfE](https://youtu.be/4xBCskEhIfE)
  ↳ *evidence-for* `g11-0181`
  ↳ *example-of* `y03-0198`

- `y03-0134` *STATED* — Photon Studio is a 100% free recreation of Photoshop that runs on your computer.
  > “They've recreated Photoshop 100% for free and Adobe is so pissed right now.”
  — [WB8w3FTYCnw](https://youtu.be/WB8w3FTYCnw) [kasTR80Lvjo](https://youtu.be/kasTR80Lvjo)
  ↳ *evidence-for* `g10-0152`
  ↳ *example-of* `y03-0208`

- `y03-0143` *STATED* — SupoClip is one open-source GitHub repo that gives you Opus Clip without paying for it.
  — [fm0bvQE5IW8](https://youtu.be/fm0bvQE5IW8)
  ↳ *evidence-for* `g12-0187`
  ↳ *example-of* `y03-0198`

- `y04-0001` *STATED* — Bot Crossing is a game that visualises your Claude chats: every character walking around its little colony is one of your real Claude Code sessions doing actual work.
  > “every bot walking around is a real Claude Code session doing actual work”
  — [Hfgfyi4-xOI](https://youtu.be/Hfgfyi4-xOI)
  ↳ *evidence-for* `g13-0001`

- `y04-0010` *STATED* — claude-mem (Claude Mem) was trending number 1 on GitHub with over 90,000 stars when he featured it as Claude's 'permanent memory upgrade'.
  > “This is trending number 1 right now on GitHub with over 90,000 stars”
  — [55RbHPThR8g](https://youtu.be/55RbHPThR8g) [EVTO2eM2DlQ](https://youtu.be/EVTO2eM2DlQ) [6zrQsxiYz1E](https://youtu.be/6zrQsxiYz1E)
  ↳ *evidence-for* `g13-0136`
  ↳ *evidence-for* `g17-0091`
  ↳ *example-of* `y04-0153`

- `y04-0025` *STATED* — The /watch skill gives Claude Code the ability to watch any video.
  > “You can now give Claude Code the ability to watch any video with this one skill.”
  — [dXOq_pNqeFA](https://youtu.be/dXOq_pNqeFA) [bmUJ_ifeXIE](https://youtu.be/bmUJ_ifeXIE) [9DM6ZdHEWls](https://youtu.be/9DM6ZdHEWls)
  ↳ *evidence-for* `g13-0119`
  ↳ *enables* `y04-0030`

- `y04-0091` *STATED* — A single file posted to GitHub (pitched as 'leaked') claims to give free access to over 50 AI tools with zero subscription.
  > “Someone just leaked a single file to GitHub that gives you free access to over 50 AI tools with zero subscription.”
  — [OD7UTDYiTYI](https://youtu.be/OD7UTDYiTYI) [voaf6bOrHgc](https://youtu.be/voaf6bOrHgc)
  ↳ *example-of* `y04-0151`

- `y04-0114` *STATED* — Must-have skill #1, the Anthropic Skills Library: say what you're building and it searches its entire skills library, finds the best-matching skills, and even installs them for you.
  > “You just say what you're building, and it will look through its entire skills library, find the best-matching ones, and even install them for you.”
  — [Gqm7-viLo_E](https://youtu.be/Gqm7-viLo_E)
  ↳ *contrast* `g18-0099`
  ↳ *part-of* `y04-0113`

- `y04-0115` *STATED* — Must-have skill #2, Superpowers: give it one task and it forces Claude to slow down, plan properly, and check its own work.
  > “You just give it one task, and it forces Claude to slow down, properly plan, and check its own work”
  — [Gqm7-viLo_E](https://youtu.be/Gqm7-viLo_E)
  ↳ *evidence-for* `g21-0008`
  ↳ *contrast* `y04-0046` — Superpowers makes one Claude check itself; Swarm adds outside critics
  ↳ *part-of* `y04-0113`

- `y04-0117` *STATED* — Must-have skill #3, Claude Memory (claude-mem): gives Claude memory across every session so it remembers your chats and files.
  > “This gives Claude memory across every session, so it remembers your chats and files”
  — [Gqm7-viLo_E](https://youtu.be/Gqm7-viLo_E)
  ↳ *evidence-for* `g13-0136`
  ↳ *example-of* `y04-0012` — claude-mem appears again as must-have skill #3
  ↳ *part-of* `y04-0113`

- `y04-0140` *STATED* — Agent Reach is a free, open-source tool that lets your AI scrape the entire internet, including LinkedIn, YouTube, Instagram and Twitter, without any subscription.
  > “This completely free AI tool lets you scrape the entire internet, even platforms like LinkedIn, YouTube, Instagram and Twitter”
  — [VRRK9REgdaA](https://youtu.be/VRRK9REgdaA)
  ↳ *evidence-for* `g14-0101`
  ↳ *example-of* `y04-0153`

### resource

- `g02-0007` *STATED* — The chen.media /hunter guide ships 6 prompts to copy, 6 numbered steps, and an example of what a /hunter answer looks like.
  — [g-let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill](https://chen.media/guides/let-5-claudes-find-jobs-and-fill-out-your-applications-set-up-the-free-hunter-skill)
  ↳ *part-of* `g02-0001`
  ↳ *example-of* `g02-0232`

- `g02-0045` *STATED* — The Context Mode guide has 1 prompt to copy and 5 numbered steps, with sections What it does, Step 1: install it, The catch, and Sources.
  — [g-stop-junk-from-eating-claude-s-memory-set-up-context-mode](https://chen.media/guides/stop-junk-from-eating-claude-s-memory-set-up-context-mode)
  ↳ *part-of* `g02-0031`
  ↳ *example-of* `g02-0232`

- `g02-0063` *STATED* — The AirLLM guide gives the install command, the code to paste in, 4 ready-made prompts for Claude Code, 4 numbered steps and the model sizes from AirLLM's README.
  — [g-run-a-235-billion-parameter-ai-model-on-a-3gb-graphics-card-set-up-the-free-airl](https://chen.media/guides/run-a-235-billion-parameter-ai-model-on-a-3gb-graphics-card-set-up-the-free-airl) [g-run-a-2-8-trillion-parameter-ai-model-on-your-gaming-graphics-card-set-up-the-fr](https://chen.media/guides/run-a-2-8-trillion-parameter-ai-model-on-your-gaming-graphics-card-set-up-the-fr)
  ↳ *part-of* `g02-0062`
  ↳ *example-of* `g02-0232`

- `g02-0095` *STATED* — The GoLive guide has 1 prompt and 4 numbered steps, with email-gated 'Step 1: install it' and 'The catches' sections.
  — [g-put-your-claude-built-app-online-with-golive](https://chen.media/guides/put-your-claude-built-app-online-with-golive)
  ↳ *part-of* `g02-0080`
  ↳ *example-of* `g02-0232`
  ↳ *example-of* `g02-0233`
  ↳ *part-of* `g12-0051`

- `g02-0139` *STATED* — The Atticus guide has 1 prompt and 4 numbered steps, with an email-gated 'What it costs' section alongside 'Step 1: set it up' and 'The catch'.
  — [g-control-your-whole-mac-with-your-voice-powered-by-claude](https://chen.media/guides/control-your-whole-mac-with-your-voice-powered-by-claude)
  ↳ *part-of* `g02-0129`
  ↳ *qualifies* `g02-0130`
  ↳ *example-of* `g02-0232`

- `g02-0175` *STATED* — The github-triage guide has 1 prompt and 4 numbered steps, with email-gated 'Set it up' and 'The catch' sections.
  — [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say)
  ↳ *part-of* `g02-0161`
  ↳ *example-of* `g02-0232`

- `g02-0194` *STATED* — The Chrome Relay guide has a first prompt to try, 5 numbered steps, and email-gated 'Step 1: install it' and 'The catches' sections.
  — [g-let-claude-use-your-signed-in-chrome-in-the-background](https://chen.media/guides/let-claude-use-your-signed-in-chrome-in-the-background)
  ↳ *part-of* `g02-0185`
  ↳ *example-of* `g02-0232`
  ↳ *example-of* `g02-0233`

- `g02-0231` *STATED* — The AI Homepage guide has 2 prompts and 5 numbered steps, with email-gated 'How it works', 'Set it up' and 'The catch' sections.
  — [g-ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper](https://chen.media/guides/ai-homepage-claude-writes-your-new-tab-like-a-morning-newspaper)
  ↳ *part-of* `g02-0219`
  ↳ *example-of* `g02-0232`

- `g03-0124` *STATED* — TypeScript and JavaScript: plugin typescript-lsp, language server binary typescript-language-server.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *part-of* `g03-0137`

- `g03-0126` *STATED* — Python: plugin pyright-lsp, language server binary pyright-langserver.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *part-of* `g03-0137`

- `g03-0127` *STATED* — Go: plugin gopls-lsp, language server binary gopls.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *part-of* `g03-0137`

- `g03-0128` *STATED* — Rust: plugin rust-analyzer-lsp, language server binary rust-analyzer.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *part-of* `g03-0137`

- `g03-0129` *STATED* — Java: plugin jdtls-lsp, language server binary jdtls.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *part-of* `g03-0137`

- `g03-0130` *STATED* — C and C++: plugin clangd-lsp, language server binary clangd.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *part-of* `g03-0137`

- `g03-0131` *STATED* — C#: plugin csharp-lsp, language server binary csharp-ls.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *part-of* `g03-0137`

- `g03-0132` *STATED* — Ruby: plugin ruby-lsp, language server binary ruby-lsp.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *part-of* `g03-0137`

- `g03-0133` *STATED* — PHP: plugin php-lsp, language server binary intelephense.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *part-of* `g03-0137`

- `g03-0134` *STATED* — Swift: plugin swift-lsp, language server binary sourcekit-lsp.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *part-of* `g03-0137`

- `g03-0135` *STATED* — Kotlin: plugin kotlin-lsp, language server binary kotlin-lsp.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *part-of* `g03-0137`

- `g03-0136` *STATED* — Lua: plugin lua-lsp, language server binary lua-language-server.
  — [g-install-a-code-intelligence-plugin-so-claude-reads-fewer-files](https://chen.media/guides/install-a-code-intelligence-plugin-so-claude-reads-fewer-files)
  ↳ *part-of* `g03-0137`

- `g04-0028` *STATED* — Guide: 'Academic Research Skills: Make Claude Check Every Source in Your Paper Is Real' at https://chen.media/guides/academic-research-skills-make-claude-check-every-source-in-your-paper-is-real.
  — [g-academic-research-skills-make-claude-check-every-source-in-your-paper-is-real](https://chen.media/guides/academic-research-skills-make-claude-check-every-source-in-your-paper-is-real)
  ↳ *example-of* `g04-0243`

- `g04-0200` *STATED* — Guide: 'AI Coders Scored 17% Lower on a Quiz: Make Claude Teach You With the Free Vibewise Plugin' at https://chen.media/guides/ai-coders-scored-17-lower-on-a-quiz-make-claude-teach-you-with-the-free-vibewise (10 prompts, 5 steps; locked: 'What Vibewise does', 'Ready-made prompts', 'What to know before you rely on it').
  — [g-ai-coders-scored-17-lower-on-a-quiz-make-claude-teach-you-with-the-free-vibewise](https://chen.media/guides/ai-coders-scored-17-lower-on-a-quiz-make-claude-teach-you-with-the-free-vibewise)
  ↳ *example-of* `g04-0243`

- `g05-0077` *STATED* — For every style the motion repo contains the film, the style notes, the full prompt and the complete source.
  — [g-15-motion-design-styles-claude-can-make-from-one-prompt](https://chen.media/guides/15-motion-design-styles-claude-can-make-from-one-prompt)
  ↳ *part-of* `g05-0074`

- `g05-0108` *STATED* — Paste-in install for Effortless: 'Install the effortless plugin for me: run `claude plugin marketplace add HeyCubit/effortless` and then `claude plugin install effortless@effortless`. When both succeed, tell me to run /reload-plugins.'
  > “Install the effortless plugin for me: run `claude plugin marketplace add HeyCubit/effortless` and then `claude plugin install effortless@effortless`. When both succeed, tell me to run /reload-plugins.”
  — [g-cut-your-claude-code-costs-with-effortless](https://chen.media/guides/cut-your-claude-code-costs-with-effortless)
  ↳ *part-of* `g05-0098`

- `g05-0209` *STATED* — Claude's skill guide says Claude 'might use commands like head -100 to preview content rather than reading entire files, resulting in incomplete information.'
  > “might use commands like head -100 to preview content rather than reading entire files, resulting in incomplete information.”
  — [g-claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix](https://chen.media/guides/claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix)
  ↳ *evidence-for* `g05-0207`
  ↳ *example-of* `g05-0323`

- `g05-0217` *STATED* — Skill audit prompt: 'Audit every skill in ~/.claude/skills (and .claude/skills in this project if it exists). For each one: 1) List every file SKILL.md links to, and any file that is only linked from another reference file. 2) For every reference file over 100 lines, write a ## Contents list at the very top that matches its headings, one line per section. 3) For every file that is only reachable through another file, add a direct link to it from SKILL.md. 4) Flag any SKILL.md body over 500 lines and suggest what to move into a reference file. Show me a table of the changes per skill and wait for my yes before you edit anything. Do not change any rule's wording.'
  > “Audit every skill in ~/.claude/skills (and .claude/skills in this project if it exists).”
  — [g-claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix](https://chen.media/guides/claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix)
  ↳ *qualifies* `g05-0207` — the one-minute fix

- `g05-0224` *STATED* — 3D Asset Server's 23 sites include Poly Haven, ambientCG, BlenderKit, Kenney, Quaternius, Sketchfab and itch.io.
  — [g-3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once](https://chen.media/guides/3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once)
  ↳ *part-of* `g05-0223`

- `g05-0232` *STATED* — No Claude handy? The same 3D asset search runs in the browser at https://3d.shep.bot
  — [g-3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once](https://chen.media/guides/3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once)
  ↳ *part-of* `g05-0223`

- `g05-0233` *STATED* — 3D Asset Server prompt: 'I need a low-poly tree pack, a mossy rock material and a sunset HDRI for my Three.js scene. Use the 3d-assets tools: show me the free options with their licences, then download the ones I pick into ./assets and tell me if any need a credit line.'
  > “I need a low-poly tree pack, a mossy rock material and a sunset HDRI for my Three.js scene. Use the 3d-assets tools: show me the free options with their licences, then download the ones I pick into ./assets and tell me if any need a credit line.”
  — [g-3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once](https://chen.media/guides/3d-asset-server-let-claude-find-and-download-3d-models-from-23-sites-at-once)
  ↳ *example-of* `g05-0226`
  ↳ *example-of* `g05-0312`

- `g06-0010` *STATED* — The /iq skill is delivered as a whole skill file you paste in yourself (section 'Get the skill').
  — [g-get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill](https://chen.media/guides/get-claude-to-estimate-your-iq-from-your-own-chats-set-up-the-free-iq-skill)
  ↳ *part-of* `g06-0009`

- `g06-0045` *STATED* — Oil UI installs with a single line (the command sits in the gated 'Install (one line)' section).
  — [g-oil-ui-make-claude-design-your-app-three-really-different-ways-then-pick-one](https://chen.media/guides/oil-ui-make-claude-design-your-app-three-really-different-ways-then-pick-one)
  ↳ *part-of* `g06-0044`

- `g06-0082` *STATED* — The anatomy repo has eight worked examples in its examples folder.
  — [g-set-up-the-anatomy-skill-the-free-repo-that-turns-any-idea-into-a-working-machin](https://chen.media/guides/set-up-the-anatomy-skill-the-free-repo-that-turns-any-idea-into-a-working-machin)
  ↳ *part-of* `g06-0074`

- `g07-0241` *INFERRED* — AirLLM is published on PyPI, so the standard install is `pip install airllm` (GitHub repo lyogavin/airllm); not shown in the free part of Alex's guide.
  — [g-run-a-70b-ai-model-on-a-4gb-graphics-card-set-up-the-free-airllm-library](https://chen.media/guides/run-a-70b-ai-model-on-a-4gb-graphics-card-set-up-the-free-airllm-library)
  ↳ *part-of* `g07-0224`
  ↳ *example-of* `g07-0240`

- `g08-0067` *STATED* — The Craft apps' code is public on GitHub under the MIT or Apache-2.0 licence.
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *part-of* `g08-0049`

- `g08-0071` *STATED* — If you need something proven today, Alex points to older free apps as Adobe alternatives (section 'If you need something proven today', names locked).
  — [g-stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft](https://chen.media/guides/stop-paying-adobe-68-97-a-month-try-the-new-free-open-source-photocraft-filmcraft-and-effectcraft)
  ↳ *contrast* `g08-0052`

- `g08-0103` *STATED* — The Agency is free and MIT licensed.
  — [g-run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents](https://chen.media/guides/run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents)
  ↳ *part-of* `g08-0089`
  ↳ *example-of* `g06-0262`

- `g08-0105` *STATED* — The Agency is a community project by GitHub user msitarzewski, not made or endorsed by Anthropic.
  — [g-run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents](https://chen.media/guides/run-a-whole-ai-agency-inside-claude-code-set-up-230-free-specialist-agents)
  ↳ *qualifies* `g08-0089`
  ↳ *example-of* `g08-0258`

- `g08-0123` *STATED* — Alex's guide '21 Sites for Every Serious Vibe Coder' covers the places vibe coders keep bookmarked: real designs to copy, design files your AI reads, ready-made components, animations, effects and art, with the first thing to try on each.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)

- `g08-0135` *STATED* — Minimal Gallery (minimal.gallery) offers hand-picked website designs, with new ones added daily.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0128`

- `g08-0136` *STATED* — Kage (kage.design) lets you pick a design and copy it as a prompt.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0128` — category inferred from table order

- `g08-0137` *STATED* — AppShot Gallery (appshot.gallery) has 821 hand-picked real mobile apps.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0128`

- `g08-0138` *STATED* — Component Gallery (component.gallery) has 2,671 examples of every UI part, from real design systems.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0128`

- `g08-0139` *STATED* — DESIGN.md (designmd.ai) offers free design systems as a file your AI reads.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0129`

- `g08-0140` *STATED* — Refero Styles (styles.refero.design) offers 2,000+ real site styles as DESIGN.md files.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0129`

- `g08-0141` *STATED* — Jiro (jiro.build) lets you browse a design and copy the prompt.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0129` — category inferred from table order

- `g08-0142` *STATED* — VibePrompt (vibeprompts.dev) has 286 ready prompts and Tailwind code for page sections.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0129` — category inferred from table order

- `g08-0143` *STATED* — 21st.dev has 12,000+ components your agent can install.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0130`

- `g08-0144` *STATED* — shadcn/ui (ui.shadcn.com) offers clean components you copy in and own.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0130`

- `g08-0145` *STATED* — Aceternity UI (ui.aceternity.com) has 200+ animated parts for landing pages.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0130` — category inferred from table order

- `g08-0146` *STATED* — Magic UI (magicui.design) has 150+ free animated components.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0130` — category inferred from table order

- `g08-0147` *STATED* — Motion Primitives (motion-primitives.com) offers animated parts you copy and paste.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0131`

- `g08-0148` *STATED* — Kinetics (kinetics.colorion.co) has 153 spring effects, each as CSS, React and a prompt.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0131`

- `g08-0149` *STATED* — MicroKit UI (microkit.co) has 49 tiny hover and click effects.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0131`

- `g08-0150` *STATED* — Anime.js (animejs.com) is one light library for any animation.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0131`

- `g08-0151` *STATED* — Uiverse (uiverse.io) has community-made UI elements to copy.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0132` — category inferred from table order

- `g08-0152` *STATED* — mapcn (mapcn.dev) offers drop-in maps with markers and routes.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0132` — category inferred from table order

- `g08-0153` *STATED* — Liquid Glass (glass.samasante.com) brings Apple's glass look to any website.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0132`

- `g08-0154` *STATED* — Kitbitz (kitbitz.art) has 2,000+ hand-drawn illustrations.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0133`

- `g08-0155` *STATED* — 3dicons (3dicons.co) has 1,440+ 3D icons.
  — [g-21-sites-for-every-serious-vibe-coder](https://chen.media/guides/21-sites-for-every-serious-vibe-coder)
  ↳ *part-of* `g08-0123`
  ↳ *part-of* `g08-0133`

- `g08-0163` *STATED* — Replica is made by Jake Schincariol: eleven skills, free and MIT licensed, with no signup, no API key and nothing to connect.
  — [g-rebuild-any-app-you-pay-for](https://chen.media/guides/rebuild-any-app-you-pay-for)
  ↳ *part-of* `g08-0156`
  ↳ *evidence-for* `g05-0240`

- `g08-0205` *STATED* — agent-office by alminisl is a free open-source Agent Office that runs on any computer with Node.
  — [g-see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office](https://chen.media/guides/see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office)
  ↳ *example-of* `g08-0204`
  ↳ *contrast* `g08-0206`

- `g08-0206` *STATED* — agent-office by kys42 is a free open-source Agent Office packaged as a Mac desktop app.
  — [g-see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office](https://chen.media/guides/see-every-claude-code-session-as-a-worker-at-a-desk-set-up-a-free-agent-office)
  ↳ *example-of* `g08-0204`

- `g09-0049` *STATED* — chen.media guide 'Run a Jarvis on Your Own Claude Code: The Free Voice Assistant That Needs No API Key' (https://chen.media/guides/run-a-jarvis-on-your-own-claude-code) has 2 prompts to copy and 3 numbered steps; sections: What you need; Set it up; Keep it safe first; Give it more to work with; Why it's worth ten minutes.
  — [g-run-a-jarvis-on-your-own-claude-code](https://chen.media/guides/run-a-jarvis-on-your-own-claude-code)
  ↳ *example-of* `g09-0253`

- `g09-0074` *STATED* — Impeccable's repo is github.com/pbakaus/impeccable.
  — [g-stop-your-site-looking-ai-made-impeccable](https://chen.media/guides/stop-your-site-looking-ai-made-impeccable)
  ↳ *part-of* `g09-0073`

- `g09-0175` *STATED* — chen.media guide 'The Free Claude Skill That Designs Your Whole Logo: How to Install It, Brief It and Get the Files' (https://chen.media/guides/free-claude-logo-design-skill) has 8 prompts to copy and 9 numbered steps; sections: What you get; How it works; Step 1: install it; Step 2: brief it; Step 3: pick a direction; Step 4: get the kit; The example from the video: Zestly; Before you start: the honest part.
  — [g-free-claude-logo-design-skill](https://chen.media/guides/free-claude-logo-design-skill)
  ↳ *example-of* `g09-0253`

- `g09-0229` *STATED* — chen.media guide 'Coucou, the Free Pet That Lives in Your Mac's Notch and Watches Claude Code for You' (https://chen.media/guides/coucou-free-notch-pet-that-watches-claude-code) has 6 numbered steps and no prompts; sections: What it does; Step 1: install Coucou; Step 2: connect it to Claude Code; Step 3: start a job, then go do something else; Extras worth turning on; The honest part.
  — [g-coucou-free-notch-pet-that-watches-claude-code](https://chen.media/guides/coucou-free-notch-pet-that-watches-claude-code)
  ↳ *example-of* `g09-0253`

- `g10-0114` *STATED* — Alex Chen's list of 14 AI sites worth bookmarking covers what each one does, what is free, and the first thing to try on each, from NVIDIA's photo-to-3D-world model to an AI co-founder that runs your business.
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)

- `g10-0118` *STATED* — NVIDIA Lyra 2.0: one photo becomes a 3D world you can walk through; open source, but needs a big GPU.
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)
  ↳ *part-of* `g10-0114`
  ↳ *qualifies* `g10-0117` — free but needs a big GPU

- `g10-0119` *STATED* — Google Stitch: describe an app in a sentence and get its screens and the code; free.
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)
  ↳ *part-of* `g10-0114`
  ↳ *example-of* `g10-0116`

- `g10-0120` *STATED* — Polsia: an AI co-founder that builds and runs your business; free to start.
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)
  ↳ *part-of* `g10-0114`

- `g10-0121` *STATED* — Napkin: turns your notes into clean diagrams; free plan.
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)
  ↳ *part-of* `g10-0114`

- `g10-0122` *STATED* — Gamma: a full slide deck from one prompt; free plan.
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)
  ↳ *part-of* `g10-0114`

- `g10-0123` *STATED* — Suno: a full song from one sentence; free plan.
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)
  ↳ *part-of* `g10-0114`

- `g10-0124` *STATED* — Krea: AI images that update live as you sketch; free plan.
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)
  ↳ *part-of* `g10-0114`

- `g10-0125` *STATED* — Ideogram: AI images with words spelled right; free plan.
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)
  ↳ *part-of* `g10-0114`

- `g10-0126` *STATED* — Recraft: logos and icons as real vector files; free plan.
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)
  ↳ *part-of* `g10-0114`

- `g10-0127` *STATED* — Photoroom: background removal and product photos without a studio; free plan, but watermarked.
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)
  ↳ *part-of* `g10-0114`
  ↳ *qualifies* `g10-0117` — free plan is watermarked

- `g10-0128` *STATED* — Hugging Face Spaces: thousands of free AI apps in your browser; free.
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)
  ↳ *part-of* `g10-0114`
  ↳ *contrast* `g10-0078` — same Hugging Face platform: free apps vs leaked tokens

- `g10-0130` *STATED* — Meshy: a picture becomes a 3D model you can print; free plan.
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)
  ↳ *part-of* `g10-0114`

- `g10-0131` *STATED* — Kling: AI video clips, with free credits every day.
  — [g-14-ai-sites-worth-bookmarking](https://chen.media/guides/14-ai-sites-worth-bookmarking)
  ↳ *part-of* `g10-0114`

- `g11-0036` *STATED* — Alex's Instatic guide compares Instatic against Framer Pro head to head.
  — [g-instatic-the-free-open-source-framer](https://chen.media/guides/instatic-the-free-open-source-framer)
  ↳ *example-of* `g11-0004`

- `g12-0146` *STATED* — Guide section 'The skill' identifies the open-source Claude Code SEO skill (body email-gated).
  — [g-how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code](https://chen.media/guides/how-to-get-an-agency-level-seo-audit-of-any-website-free-inside-claude-code)
  ↳ *part-of* `g12-0129`
  ↳ *defines* `g12-0131`

- `g12-0173` *STATED* — Fast-Jev Compaction on GitHub: https://github.com/tamaratran/fast-jev-compaction (MIT licence).
  — [g-stop-claude-code-s-compact-from-summarizing-away-your-chat](https://chen.media/guides/stop-claude-code-s-compact-from-summarizing-away-your-chat)
  ↳ *part-of* `g12-0172`
  ↳ *example-of* `g12-0300`

- `g12-0188` *STATED* — SupoClip on GitHub: FujiwaraChoki/supoclip.
  — [g-supoclip-open-source-opusclip-alternative](https://chen.media/guides/supoclip-open-source-opusclip-alternative)
  ↳ *part-of* `g12-0187`
  ↳ *example-of* `g12-0300`

- `g13-0062` *STATED* — Scrapling's GitHub repository is D4Vinci/Scrapling.
  — [g-scrapling-claude-code-setup-guide](https://chen.media/guides/scrapling-claude-code-setup-guide)
  ↳ *part-of* `g13-0061`

- `g13-0153` *STATED* — The Public APIs directory on GitHub, the repo from Alex's PUB reel, is a place to find real data for an app.
  — [g-public-apis-claude-code-build-guide](https://chen.media/guides/public-apis-claude-code-build-guide)
  ↳ *enables* `g13-0152`

- `g13-0198` *STATED* — Alex's HackingTool guide links the official HackingTool repository and its current tool catalog.
  — [g-hackingtool-secure-your-own-apps](https://chen.media/guides/hackingtool-secure-your-own-apps)
  ↳ *part-of* `g13-0189`

- `g13-0282` *STATED* — Alex's '100 Free Claude Skills' guide gives the three systems from his SKILL reel, a repeatable way to try them, and 100 direct links to published skill files.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)

- `g13-0289` *STATED* — System 1 in Alex's SKILL reel: the Anthropic Skills Library.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *part-of* `g13-0282`
  ↳ *evidence-for* `g18-0099`

- `g13-0290` *STATED* — System 2 in Alex's SKILL reel: Superpowers.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *part-of* `g13-0282`
  ↳ *evidence-for* `g21-0008`

- `g13-0291` *STATED* — System 3 in Alex's SKILL reel: Claude Mem.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *part-of* `g13-0282`
  ↳ *evidence-for* `y04-0117`
  ↳ *evidence-for* `g17-0086`

- `g13-0292` *STATED* — Alex's 100-skill catalogue group: Anthropic skills.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *part-of* `g13-0298`
  ↳ *part-of* `g18-0099`

- `g13-0293` *STATED* — Alex's 100-skill catalogue group: Superpowers workflow skills.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *part-of* `g13-0298`
  ↳ *part-of* `g21-0008`

- `g13-0294` *STATED* — Alex's 100-skill catalogue group: Marketing skills.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *part-of* `g13-0298`

- `g13-0295` *STATED* — Alex's 100-skill catalogue group: Review and development skills.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *part-of* `g13-0298`

- `g13-0300` *STATED* — 100-skills guide section: 'Sources and attribution' for the linked skills.
  — [g-100-free-claude-skills-and-setup](https://chen.media/guides/100-free-claude-skills-and-setup)
  ↳ *qualifies* `g13-0286`

- `g14-0043` *STATED* — Alex's guide 'OpenCut: Try the Editor and Run the Classic Source' covers the OP reel's browser editor, official repositories, local development commands and a small export test.
  — [g-opencut-repo-and-setup-guide](https://chen.media/guides/opencut-repo-and-setup-guide)
  ↳ *example-of* `g14-0346`

- `g14-0062` *STATED* — Claude HUD lives at the GitHub repository jarrodwatts/claude-hud, which has a maintained installation guide.
  — [g-headroom-claude-hud-aisa-setup](https://chen.media/guides/headroom-claude-hud-aisa-setup)
  ↳ *part-of* `g14-0058`

- `g14-0072` *STATED* — Alex's guide 'Antigravity Inside VS Code: Setup and Free-Tier Limits' shows how to install Google's official extension, understand the account requirements, and test a small change before adopting it for daily work.
  — [g-antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you](https://chen.media/guides/antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you)

- `g14-0100` *STATED* — Alex's guide 'Agent Reach: Web Research Setup and Three Useful Workflows' shows how to connect supported research channels, verify your setup and produce useful job, video and content research.
  — [g-agent-reach-web-research-setup](https://chen.media/guides/agent-reach-web-research-setup)

- `g14-0102` *STATED* — Agent Reach is an open-source project on GitHub under the MIT license.
  — [g-agent-reach-web-research-setup](https://chen.media/guides/agent-reach-web-research-setup)
  ↳ *part-of* `g14-0100`

- `g14-0220` *STATED* — Alex's guide 'How to install ECC in Claude Code or Codex' gives the official repository, a clear installation path, and prompts for planning, building, reviewing and testing one small feature.
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)

- `g14-0225` *STATED* — ECC official repository: https://github.com/affaan-m/ECC
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *part-of* `g14-0220`
  ↳ *part-of* `g14-0222`

- `g14-0234` *STATED* — The ECC guide includes the setup prompt from Alex's ECC video.
  > “The setup prompt from the video”
  — [g-ecc-installation-guide](https://chen.media/guides/ecc-installation-guide)
  ↳ *part-of* `g14-0220`

- `g14-0247` *STATED* — Claude Octopus is an independent MIT-licensed project (published via the nyldn plugins marketplace).
  — [g-claude-octopus-setup-guide](https://chen.media/guides/claude-octopus-setup-guide)
  ↳ *part-of* `g14-0241`

- `g14-0287` *STATED* — Alex's guide 'Build Your AI Team with Claude Skills' collects the marketing, social media, design, finance and legal skill links from his video, plus prompts to adapt them to your business.
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *example-of* `g14-0353`

- `g14-0302` *STATED* — The AI-team guide has one section of skill links per department: Marketing, Social media, Design, Finance and Legal.
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *part-of* `g14-0287`

- `g14-0305` *STATED* — The AI-team guide includes a section to fix common skill setup problems.
  > “Fix common setup problems”
  — [g-build-your-ai-team-with-claude-skills](https://chen.media/guides/build-your-ai-team-with-claude-skills)
  ↳ *part-of* `g14-0287`

- `g15-0021` *STATED* — The full MarkItDown guide gives the MCP server config for Claude Desktop word for word plus a supported-formats table (locked part).
  — [g-why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix](https://chen.media/guides/why-uploading-a-pdf-to-claude-costs-you-70-000-tokens-and-the-free-microsoft-fix)
  ↳ *part-of* `g15-0020`
  ↳ *example-of* `g15-0175`

- `g16-0143` *STATED* — Unlazy's repo is github.com/Leonxlnx/unlazy.
  — [g-the-free-skill-that-stops-claude-saying-done-when-it-is-not](https://chen.media/guides/the-free-skill-that-stops-claude-saying-done-when-it-is-not)
  ↳ *part-of* `g16-0141`

- `g16-0153` *STATED* — His unlazy guide includes a GATES.md you can copy.
  > “A GATES.md you can copy”
  — [g-the-free-skill-that-stops-claude-saying-done-when-it-is-not](https://chen.media/guides/the-free-skill-that-stops-claude-saying-done-when-it-is-not)
  ↳ *part-of* `g16-0151`
  ↳ *part-of* `g16-0141`

- `g16-0237` *STATED* — ripienaar/free-for-dev (132,255 stars) is the directory of free tiers.
  — [g-five-free-github-repos-that-replace-software-you-pay-for](https://chen.media/guides/five-free-github-repos-that-replace-software-you-pay-for)
  ↳ *part-of* `g16-0232`

- `g16-0238` *STATED* — public-apis/public-apis (466,531 stars, MIT) is the switchboard of free public APIs.
  — [g-five-free-github-repos-that-replace-software-you-pay-for](https://chen.media/guides/five-free-github-repos-that-replace-software-you-pay-for)
  ↳ *part-of* `g16-0232`
  ↳ *evidence-for* `g13-0153`

- `g16-0239` *STATED* — D4Vinci/Scrapling (75,397 stars, BSD-3-Clause) is the scraper that gets the page.
  > “Scrapling, the one that gets the page”
  — [g-five-free-github-repos-that-replace-software-you-pay-for](https://chen.media/guides/five-free-github-repos-that-replace-software-you-pay-for)
  ↳ *part-of* `g16-0232`
  ↳ *evidence-for* `g13-0061`

- `g16-0240` *STATED* — ollama/ollama (179,017 stars, MIT) is the model on your own machine.
  > “Ollama, the model on your own machine”
  — [g-five-free-github-repos-that-replace-software-you-pay-for](https://chen.media/guides/five-free-github-repos-that-replace-software-you-pay-for)
  ↳ *part-of* `g16-0232`
  ↳ *contrast* `g16-0086` — free Ollama runs small local models; matching Claude-class quality locally (Kimi K3) costs $112,000 and runs at 1 token / 10 s
  ↳ *evidence-for* `g18-0152`

- `g16-0241` *STATED* — punkpeye/awesome-mcp-servers (92,592 stars, MIT) is the directory of connectors (MCP servers).
  > “awesome-mcp-servers, the connectors”
  — [g-five-free-github-repos-that-replace-software-you-pay-for](https://chen.media/guides/five-free-github-repos-that-replace-software-you-pay-for)
  ↳ *part-of* `g16-0232`
  ↳ *part-of* `g16-0014`

- `g16-0276` *STATED* — Prompt Master's repo is github.com/nidhinjs/prompt-master: 11,415 stars, MIT licensed, verified 19 August 2026.
  — [g-the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting](https://chen.media/guides/the-free-claude-skill-that-writes-the-prompt-so-you-stop-re-prompting)
  ↳ *part-of* `g16-0270`
  ↳ *example-of* `g16-0005`
  ↳ *part-of* `g16-0006`

- `g16-0294` *STATED* — Searching for "claude flow" on GitHub now lands you on ruvnet/ruflo: same project, same maintainer.
  — [g-ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm](https://chen.media/guides/ruflo-the-agent-harness-that-runs-claude-code-as-a-swarm)
  ↳ *evidence-for* `g16-0293`

- `g17-0079` *STATED* — Anthropic's finance agents repo is github.com/anthropics/financial-services: 34,211 stars, Apache 2.0 licence, Python.
  — [g-anthropic-s-ten-finance-agents-for-equity-research-and-modelling](https://chen.media/guides/anthropic-s-ten-finance-agents-for-equity-research-and-modelling)
  ↳ *evidence-for* `g17-0074`
  ↳ *example-of* `g17-0310`

- `g17-0089` *STATED* — Awesome APIs plugin: github.com/open-free-llm-api/awesome-freellm-apis, 1,697 stars, MIT.
  — [g-the-three-claude-code-plugins-worth-installing](https://chen.media/guides/the-three-claude-code-plugins-worth-installing)
  ↳ *part-of* `g17-0086`
  ↳ *contrast* `g17-0143` — a list of free LLM APIs vs a proxy that pools them

- `g17-0090` *STATED* — Find Skills plugin: github.com/vercel-labs/skills, 28,826 stars, MIT.
  — [g-the-three-claude-code-plugins-worth-installing](https://chen.media/guides/the-three-claude-code-plugins-worth-installing)
  ↳ *part-of* `g17-0086`
  ↳ *enables* `g17-0236` — Find Skills installs skills from repos like ComposioHQ
  ↳ *evidence-for* `g10-0247`

- `g17-0091` *STATED* — Claude Mem plugin: github.com/thedotmack/claude-mem, 90,651 stars, Apache 2.0.
  — [g-the-three-claude-code-plugins-worth-installing](https://chen.media/guides/the-three-claude-code-plugins-worth-installing)
  ↳ *part-of* `g17-0086`

- `g17-0103` *STATED* — Claude SEO repo: github.com/AgriciDaniel/claude-seo, 14,028 stars, MIT licence, Python.
  — [g-install-25-seo-skills-and-18-specialist-agents-into-claude-code](https://chen.media/guides/install-25-seo-skills-and-18-specialist-agents-into-claude-code)
  ↳ *evidence-for* `g17-0100`

- `g17-0106` *STATED* — Claude SEO has a Codex port at github.com/AgriciDaniel/codex-seo.
  — [g-install-25-seo-skills-and-18-specialist-agents-into-claude-code](https://chen.media/guides/install-25-seo-skills-and-18-specialist-agents-into-claude-code)
  ↳ *part-of* `g17-0103`
  ↳ *part-of* `g17-0099`

- `g17-0121` *STATED* — Alex Chen's context-compression guide is built on one specific tool, named in the gated section.
  > “The tool this is built on”
  — [g-cut-what-your-coding-agent-sends-to-the-model](https://chen.media/guides/cut-what-your-coding-agent-sends-to-the-model)
  ↳ *enables* `g17-0120`

- `g17-0135` *STATED* — The Apple design tokens come from an open-source MIT-licensed Apple style skill at github.com/chaos-xxl/apple-design-skill.
  — [g-apple-s-real-design-tokens-packaged-as-a-claude-skill](https://chen.media/guides/apple-s-real-design-tokens-packaged-as-a-claude-skill)
  ↳ *evidence-for* `g17-0127`

- `g17-0146` *STATED* — FreeLLMAPI repo: github.com/tashfeenahmed/freellmapi, 18,265 stars, MIT licence, TypeScript.
  — [g-pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint](https://chen.media/guides/pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint)
  ↳ *evidence-for* `g17-0143`

- `g17-0156` *STATED* — Project NOMAD repo, checked 11 August 2026: github.com/Crosstalk-Solutions/project-nomad, Apache-2.0, 35,694 stars, 3,579 forks, TypeScript, last pushed 11 August 2026.
  — [g-a-knowledge-server-that-keeps-answering-with-the-internet-off](https://chen.media/guides/a-knowledge-server-that-keeps-answering-with-the-internet-off)
  ↳ *evidence-for* `g17-0155`
  ↳ *evidence-for* `g17-0303`
  ↳ *example-of* `g17-0304`

- `g17-0223` *STATED* — github.com/ComposioHQ/awesome-claude-skills, checked 9 August 2026: Apache-2.0, 72,138 stars, 8,183 forks, 164 linked skills across 11 category sections.
  — [g-164-claude-skills-in-one-repo-which-to-take-first](https://chen.media/guides/164-claude-skills-in-one-repo-which-to-take-first)
  ↳ *evidence-for* `g17-0303`
  ↳ *example-of* `g17-0304`

- `g17-0275` *STATED* — A second repo is the real unlock for Open Generative AI.
  > “The second repo, and the real unlock”
  — [g-400-ai-image-and-video-models-in-one-free-desktop-app](https://chen.media/guides/400-ai-image-and-video-models-in-one-free-desktop-app)
  ↳ *enables* `g17-0272`

- `g18-0077` *STATED* — Alex lists five animation skills for Claude Code, all public repos, none paid or sponsored, with every install command and what to prompt once each is in.
  — [g-five-animation-skills-for-claude-code-with-install-commands](https://chen.media/guides/five-animation-skills-for-claude-code-with-install-commands)

- `g18-0093` *STATED* — The Open Generative AI repo is github.com/Anil-matcha/Open-Generative-AI and has passed 25,000 stars.
  — [g-the-open-source-ai-studio-that-replaces-a-video-subscription](https://chen.media/guides/the-open-source-ai-studio-that-replaces-a-video-subscription)
  ↳ *part-of* `g18-0092`
  ↳ *evidence-for* `g17-0269`

- `g18-0111` *STATED* — Four MCP servers close Claude's four gaps: Exa (live search), Playwright (real browser), Firecrawl (reading a page or a whole site) and Context7 (current library docs).
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again)
  ↳ *because* `g18-0110`

- `g18-0117` *STATED* — The Exa MCP server is exa-labs/exa-mcp-server (4,800 stars) and needs an API key from the Exa dashboard.
  — [g-the-four-mcp-servers-to-install-before-you-open-claude-again](https://chen.media/guides/the-four-mcp-servers-to-install-before-you-open-claude-again)
  ↳ *part-of* `g18-0114`

- `g18-0154` *STATED* — Alex's five Claude Code plugins to install before you build anything: the official Anthropic skills, claude-mem, claude-obsidian, code-review and ponytail.
  — [g-the-5-claude-code-plugins-to-install-before-you-build-anything](https://chen.media/guides/the-5-claude-code-plugins-to-install-before-you-build-anything)
  ↳ *example-of* `g18-0279`

- `g18-0262` *STATED* — Alex's seven open source repos that replace paid AI tools are all free and public, with over 499,000 GitHub stars between them.
  — [g-seven-free-repos-that-replace-paid-ai-tools](https://chen.media/guides/seven-free-repos-that-replace-paid-ai-tools)
  ↳ *example-of* `g18-0287`

- `g18-0276` *STATED* — Three more tools worth your time that did not make Alex's seven: a skills marketplace, an observability layer and a local model router.
  — [g-seven-free-repos-that-replace-paid-ai-tools](https://chen.media/guides/seven-free-repos-that-replace-paid-ai-tools)
  ↳ *part-of* `g18-0262`

- `g19-0101` *STATED* — Alex's chen.media guide 'Five Free Repos That Give Claude Actual Hands' (category: Tools & repos) covers five open-source repos that let Claude make images and video, put a real face and voice on camera, build a slide deck, hear audio, and run your week while you sleep.
  > “make images and video, put a real face and voice on camera, build a full slide deck, give it ears, and let it run your week while you sleep”
  — [g-five-free-repos-that-give-claude-actual-hands](https://chen.media/guides/five-free-repos-that-give-claude-actual-hands)

- `g19-0136` *STATED* — Alex's gated guide 'The Langfuse Setup Kit' ('Turn a Black-Box AI Agent Into an X-Ray of Every Call', category: Tools & repos) sets up Langfuse in about ten minutes.
  > “The Langfuse Setup Kit”
  — [g-turn-a-black-box-ai-agent-into-an-x-ray-of-every-call](https://chen.media/guides/turn-a-black-box-ai-agent-into-an-x-ray-of-every-call)

- `g19-0155` *STATED* — Alex's chen.media guide 'Four Free Repos That Upgrade Claude, and What Each One Fixes' (category: Tools & repos) gives what each fixes, the exact install command and the honest catches; every tool is free and open source.
  > “What each one fixes, the exact install command, and the honest catches.”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)

- `g19-0174` *STATED* — The four-repos guide closes with 'What each one actually fixes' and Honest notes.
  > “What each one actually fixes”
  — [g-four-free-repos-that-upgrade-claude-and-what-each-one-fixes](https://chen.media/guides/four-free-repos-that-upgrade-claude-and-what-each-one-fixes)
  ↳ *part-of* `g19-0155`

- `g19-0176` *STATED* — Alex's chen.media guide 'Give Claude Code an IDE Brain So It Stops Reading Everything' (category: Tools & repos) sets up Serena so Claude Code stops reading your whole codebase to change one function.
  > “Give Claude Code an IDE brain so it stops reading your whole codebase to change one function.”
  — [g-give-claude-code-an-ide-brain-so-it-stops-reading-everything](https://chen.media/guides/give-claude-code-an-ide-brain-so-it-stops-reading-everything)

- `g20-0023` *STATED* — Alex Chen's chen.media guide 'Give Claude Your Notes, Meetings and Email: the Day 1 Setup' (category: Claude Code) is Part 1 of 2, 'building the brain', with 12 prompts to copy and 10 numbered steps.
  > “Part 1 of 2: building the brain. Your notes, your meetings, your email, and the step that makes it answer like you.”
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)

- `g20-0123` *STATED* — The five design sites from Alex's video are 21st.dev, Aceternity UI, Magic UI, Mobbin and tweakcn.
  — [g-why-every-ai-built-site-looks-the-same-and-how-to-fix-it](https://chen.media/guides/why-every-ai-built-site-looks-the-same-and-how-to-fix-it)
  ↳ *part-of* `g20-0114`
  ↳ *example-of* `g20-0281`

- `g20-0124` *STATED* — 21st.dev (5,347 GitHub stars) is a marketplace of beautiful UI components built by real designers: find a hero, a pricing card or a bento grid you like, copy it and paste it straight into your site.
  — [g-why-every-ai-built-site-looks-the-same-and-how-to-fix-it](https://chen.media/guides/why-every-ai-built-site-looks-the-same-and-how-to-fix-it)
  ↳ *part-of* `g20-0123`
  ↳ *example-of* `g20-0122` — grab a component
  ↳ *evidence-for* `g08-0143`

- `g20-0125` *STATED* — Aceternity UI (ui.aceternity.com) is design-stack site #2 from the video.
  — [g-why-every-ai-built-site-looks-the-same-and-how-to-fix-it](https://chen.media/guides/why-every-ai-built-site-looks-the-same-and-how-to-fix-it)
  ↳ *part-of* `g20-0123`
  ↳ *evidence-for* `g08-0145`

- `g20-0126` *STATED* — Magic UI (magicui.design, 21,565 GitHub stars) is design-stack site #3 from the video.
  — [g-why-every-ai-built-site-looks-the-same-and-how-to-fix-it](https://chen.media/guides/why-every-ai-built-site-looks-the-same-and-how-to-fix-it)
  ↳ *part-of* `g20-0123`
  ↳ *evidence-for* `g08-0146`

- `g20-0127` *STATED* — Mobbin (mobbin.com) is design-stack site #4 from the video, a source of real app screens to match.
  — [g-why-every-ai-built-site-looks-the-same-and-how-to-fix-it](https://chen.media/guides/why-every-ai-built-site-looks-the-same-and-how-to-fix-it)
  ↳ *part-of* `g20-0123`
  ↳ *example-of* `g20-0122` — match a screenshot

- `g20-0128` *STATED* — tweakcn (tweakcn.com, 10,171 GitHub stars) is design-stack site #5 from the video, a theme source.
  — [g-why-every-ai-built-site-looks-the-same-and-how-to-fix-it](https://chen.media/guides/why-every-ai-built-site-looks-the-same-and-how-to-fix-it)
  ↳ *part-of* `g20-0123`
  ↳ *example-of* `g20-0122` — apply a theme

- `g20-0129` *STATED* — Beyond the video's five, the guide adds 'A dozen more (the full stack)', numbered 6 to 17.
  — [g-why-every-ai-built-site-looks-the-same-and-how-to-fix-it](https://chen.media/guides/why-every-ai-built-site-looks-the-same-and-how-to-fix-it)
  ↳ *part-of* `g20-0114`

- `g20-0130` *STATED* — shadcn/ui (ui.shadcn.com) is #6 in Alex's design stack.
  — [g-why-every-ai-built-site-looks-the-same-and-how-to-fix-it](https://chen.media/guides/why-every-ai-built-site-looks-the-same-and-how-to-fix-it)
  ↳ *part-of* `g20-0129`
  ↳ *evidence-for* `g08-0144`

- `g20-0131` *STATED* — Tailwind CSS (tailwindcss.com) is #7 in Alex's design stack.
  — [g-why-every-ai-built-site-looks-the-same-and-how-to-fix-it](https://chen.media/guides/why-every-ai-built-site-looks-the-same-and-how-to-fix-it)
  ↳ *part-of* `g20-0129`

- `g20-0132` *STATED* — Radix UI (radix-ui.com) is #8 in Alex's design stack.
  — [g-why-every-ai-built-site-looks-the-same-and-how-to-fix-it](https://chen.media/guides/why-every-ai-built-site-looks-the-same-and-how-to-fix-it)
  ↳ *part-of* `g20-0129`

- `g20-0133` *STATED* — Lucide (lucide.dev) icons are #10 in Alex's design stack.
  — [g-why-every-ai-built-site-looks-the-same-and-how-to-fix-it](https://chen.media/guides/why-every-ai-built-site-looks-the-same-and-how-to-fix-it)
  ↳ *part-of* `g20-0129`

- `g20-0134` *STATED* — Fontshare (fontshare.com) fonts are #11 in Alex's design stack, an alternative to the default Inter font.
  — [g-why-every-ai-built-site-looks-the-same-and-how-to-fix-it](https://chen.media/guides/why-every-ai-built-site-looks-the-same-and-how-to-fix-it)
  ↳ *part-of* `g20-0129`
  ↳ *contrast* `g20-0115` — Inter default

- `g20-0135` *STATED* — Godly (godly.website) is #13 in Alex's design stack, a gallery of standout websites.
  — [g-why-every-ai-built-site-looks-the-same-and-how-to-fix-it](https://chen.media/guides/why-every-ai-built-site-looks-the-same-and-how-to-fix-it)
  ↳ *part-of* `g20-0129`

- `g20-0136` *STATED* — Land-book (land-book.com) is #14 in Alex's design stack, a landing-page gallery.
  — [g-why-every-ai-built-site-looks-the-same-and-how-to-fix-it](https://chen.media/guides/why-every-ai-built-site-looks-the-same-and-how-to-fix-it)
  ↳ *part-of* `g20-0129`

- `g20-0137` *STATED* — Cult UI (cult-ui.com) is #15 in Alex's design stack.
  — [g-why-every-ai-built-site-looks-the-same-and-how-to-fix-it](https://chen.media/guides/why-every-ai-built-site-looks-the-same-and-how-to-fix-it)
  ↳ *part-of* `g20-0129`

- `g20-0138` *STATED* — Haikei (haikei.app) is #16 in Alex's design stack, a generator for SVG backgrounds and shapes.
  — [g-why-every-ai-built-site-looks-the-same-and-how-to-fix-it](https://chen.media/guides/why-every-ai-built-site-looks-the-same-and-how-to-fix-it)
  ↳ *part-of* `g20-0129`

- `g20-0255` *STATED* — Alex Chen's chen.media guide 'Five Free MCPs That Plug Real Tools Into Claude' (category: Tools & repos) claims the five MCPs replace thousands of dollars a month of software.
  > “replace thousands of dollars a month of software.”
  — [g-five-free-mcps-that-plug-real-tools-into-claude](https://chen.media/guides/five-free-mcps-that-plug-real-tools-into-claude)

- `g21-0001` *STATED* — Alex Chen's chen.media guide 'Five Claude Code Skills, With the Install Command for Each' (section: Tools & repos, funnel keyword POWERS) lists 5 Claude Code skills with what each does, why it matters and the exact install command.
  — [g-five-claude-code-skills-with-the-install-command-for-each](https://chen.media/guides/five-claude-code-skills-with-the-install-command-for-each)
  ↳ *part-of* `g21-0243`

- `g21-0016` *STATED* — The five-skills guide has a section 'How skills, plugins & MCP servers install (the 30-second version)'.
  — [g-five-claude-code-skills-with-the-install-command-for-each](https://chen.media/guides/five-claude-code-skills-with-the-install-command-for-each)
  ↳ *part-of* `g21-0001`

- `g21-0018` *STATED* — The five-skills guide opens with a one-page summary table: skill, what it does, and a one-line install for each.
  — [g-five-claude-code-skills-with-the-install-command-for-each](https://chen.media/guides/five-claude-code-skills-with-the-install-command-for-each)
  ↳ *part-of* `g21-0001`

- `g21-0210` *STATED* — Alex's chen.media guide 'Five Skills That Run a Whole Content Team' (section: Agent teams) gives five custom Claude skills you install once: a strategist, a copywriter, an editor, a planner, and a repurposer, for the price of your Claude plan.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)

- `g21-0218` *STATED* — hooks.md frontmatter: description 'Writes scroll-stopping hooks for any topic', argument-hint '[topic or video idea]'.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *part-of* `g21-0215`
  ↳ *example-of* `g21-0217`

- `g21-0221` *STATED* — repurpose.md frontmatter: description 'Turns one long piece into a week of content', argument-hint '[paste a transcript or @file]'.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *part-of* `g21-0215`
  ↳ *example-of* `g21-0217`

- `g21-0226` *STATED* — grade.md frontmatter: description 'Grades a post before you publish it', argument-hint '[paste your draft caption or script]'.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *part-of* `g21-0215`
  ↳ *example-of* `g21-0217`

- `g21-0230` *STATED* — trends.md frontmatter: argument-hint '[your niche]' and allowed-tools: WebSearch, letting the trend scout search the web.
  > “allowed-tools: WebSearch”
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *part-of* `g21-0215`
  ↳ *example-of* `g21-0217`

- `g21-0234` *STATED* — calendar.md frontmatter: argument-hint '[your goal + content pillars]'; body opens 'You are my content planner. Goal and pillars: $ARGUMENTS'.
  — [g-five-skills-that-run-a-whole-content-team](https://chen.media/guides/five-skills-that-run-a-whole-content-team)
  ↳ *part-of* `g21-0215`
  ↳ *example-of* `g21-0217`

- `g22-0097` *STATED* — Alex Chen's chen.media guide 'Make Claude Hunt Down Every Forgotten Account You Have' (section: Tools & repos; comment keyword PURGE) gives 3 exact prompts, the setup for each, and a safety checklist.
  — [g-make-claude-hunt-down-every-forgotten-account-you-have](https://chen.media/guides/make-claude-hunt-down-every-forgotten-account-you-have)
  ↳ *example-of* `g22-0283`

- `g22-0102` *STATED* — PURGE FIND needs your email connected to Claude through the Gmail / Outlook connector or an MCP.
  — [g-make-claude-hunt-down-every-forgotten-account-you-have](https://chen.media/guides/make-claude-hunt-down-every-forgotten-account-you-have)
  ↳ *enables* `g22-0101`
  ↳ *evidence-for* `g07-0005`

- `g22-0105` *STATED* — PURGE DELETE needs a browser Claude can drive: Claude for Chrome or the Playwright MCP.
  — [g-make-claude-hunt-down-every-forgotten-account-you-have](https://chen.media/guides/make-claude-hunt-down-every-forgotten-account-you-have)
  ↳ *enables* `g22-0103`
  ↳ *enables* `g22-0278`
  ↳ *evidence-for* `g21-0014`

- `g22-0145` *STATED* — Alex Chen's chen.media guide 'Run Your Meta Ads From Claude With the Official Connector' (section: Build & sell) gives the connector, a 60-second setup and 6 prompts.
  — [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)

- `g22-0156` *STATED* — The Meta Ads connector URL is https://mcp.facebook.com/ads (Settings > Connectors > Add custom connector > paste).
  — [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)
  ↳ *part-of* `g22-0153`

- `g23-0106` *STATED* — The install-any-skill prompt: 'Find and install the [skill name] skill for me. Search the skills library, pick the best match, and add it to my setup. Then confirm it is active and show me one example of it working.'
  > “Find and install the [skill name] skill for me. Search the skills library, pick the best match, and add it to my setup. Then confirm it is active and show me one example of it working.”
  — [g-five-claude-skills-that-beat-99-of-users](https://chen.media/guides/five-claude-skills-that-beat-99-of-users)
  ↳ *example-of* `g23-0105`

- `g23-0153` *STATED* — Install the Chrome DevTools MCP in Claude Code with: claude mcp add chrome-devtools -- npx chrome-devtools-mcp@latest
  > “claude mcp add chrome-devtools -- npx chrome-devtools-mcp@latest”
  — [g-the-claude-plugins-cheat-sheet-add-once-then-just-ask](https://chen.media/guides/the-claude-plugins-cheat-sheet-add-once-then-just-ask)
  ↳ *part-of* `g23-0152`

- `r01-0025` *STATED* — Alex Chen's GitHub account is github.com/alexyc9381; skill repos are named <name>-skill (shark-skill, court-skill, night-crew-skill, launch-skill, learn-skill).
  — [r-alexyc9381](https://github.com/alexyc9381/alexyc9381)
  ↳ *part-of* `r01-0002`

- `r01-0067` *STATED* — The /agency argument-hint is 'setup | outbound <leads file> | sales prep <client> | sales live <transcript file> | build <client> | support | night | status'.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill)
  ↳ *defines* `r01-0068`
  ↳ *example-of* `r01-0012`

- `r01-0155` *STATED* — The /hiring-panel argument-hint is '<resume file or pasted text> [job posting or role]'.
  — [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *example-of* `r01-0012`

- `r01-0205` *STATED* — The /court argument-hint is '[--jury N | --quick] [--seed S] <the idea, plan or claim>'.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *example-of* `r01-0012`
  ↳ *defines* `r01-0178`

- `r01-0206` *STATED* — The /court SKILL.md metadata also carries source: https://github.com/alexyc9381/court-skill.
  — [r-court-skill](https://github.com/alexyc9381/court-skill)
  ↳ *part-of* `r01-0012`

- `r02-0051` *STATED* — The /hunter SKILL.md frontmatter sets `license: MIT` and metadata author "Alex Chen (@nocodealex)", homepage "https://chen.media", version "1.0.0".
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *part-of* `r02-0001`

- `r02-0068` *STATED* — Greenhouse boards list jobs as JSON at `https://boards-api.greenhouse.io/v1/boards/<company>/jobs?content=true`.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *enables* `r02-0071`

- `r02-0069` *STATED* — Lever boards list jobs at `https://api.lever.co/v0/postings/<company>?mode=json`.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *enables* `r02-0071`

- `r02-0070` *STATED* — Ashby boards list jobs at `https://api.ashbyhq.com/posting-api/job-board/<company>`.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *enables* `r02-0071`

- `r02-0095` *STATED* — The Greenhouse API can list a job's real application questions with `?questions=true` on the job.
  — [r-hunter-skill](https://github.com/alexyc9381/hunter-skill)
  ↳ *enables* `r02-0094`

- `r02-0158` *STATED* — The /launch stations are defined in `skills/launch/stations.json`.
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0155`

- `r02-0167` *STATED* — The /launch SKILL.md frontmatter sets `license: MIT` and metadata author "Alex Chen (@nocodealex)", homepage "https://chen.media", source "https://github.com/alexyc9381/launch-skill", version "1.0.0".
  — [r-launch-skill](https://github.com/alexyc9381/launch-skill)
  ↳ *part-of* `r02-0118`

- `r04-0003` *CORE* — Alex Chen's skill repos live under the GitHub account alexyc9381 (github.com/alexyc9381/mentor-skill, /night-crew-skill, /shark-skill).
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill) [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill) [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *enables* `r04-0005`

- `r04-0011` *CORE* — Alex's mentor and shark repos ship unit tests, run with: python3 -m unittest discover -s tests.
  > “python3 -m unittest discover -s tests”
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill) [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *qualifies* `r04-0009` — the helpers are unit-tested
  ↳ *evidence-for* `r01-0007`

- `r04-0038` *STATED* — /mentor install by paste: give Claude 'https://github.com/alexyc9381/mentor-skill' plus 'Install this plugin, then confirm /mentor works.'
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *example-of* `r04-0004`
  ↳ *part-of* `r04-0023`
  ↳ *example-of* `r01-0003`

- `r04-0039` *STATED* — /mentor plugin install in Claude Code: /plugin marketplace add alexyc9381/mentor-skill then /plugin install mentor-skill@mentor-skill.
  > “/plugin marketplace add alexyc9381/mentor-skill
/plugin install mentor-skill@mentor-skill”
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *part-of* `r04-0005`
  ↳ *leads-to* `r04-0040`
  ↳ *example-of* `r01-0004`

- `r04-0045` *STATED* — /mentor <what you want to build> starts a session and asks the first question.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *part-of* `r04-0023`

- `r04-0046` *STATED* — /mentor status shows what's answered, and whether code is locked.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *part-of* `r04-0023`
  ↳ *depends-on* `r04-0033`

- `r04-0047` *STATED* — /mentor recap writes .mentor/RECAP.md: every call you made and what you learned.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *part-of* `r04-0023`
  ↳ *defines* `r04-0036`

- `r04-0048` *STATED* — /mentor stop turns the lock off; Claude can write freely again.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *part-of* `r04-0023`
  ↳ *qualifies* `r04-0033`

- `r04-0051` *STATED* — The idea of a plugin that keeps you in the loop comes from Noah Kim's VibeWise (github.com/nykooi1/vibe-wise, MIT).
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *leads-to* `r04-0023` — inspiration
  ↳ *part-of* `g06-0250`

- `r04-0053` *STATED* — /mentor uninstall: /plugin uninstall mentor-skill@mentor-skill
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *contrast* `r04-0039`

- `r04-0055` *STATED* — The mentor skill's argument-hint is "[what you want to build] | status | recap | stop".
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *part-of* `r04-0006`

- `r04-0057` *STATED* — All /mentor bookkeeping goes through mentor.py: python3 "${CLAUDE_SKILL_DIR}/mentor.py" <command> (called MENTOR in the skill).
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *example-of* `r04-0009`
  ↳ *part-of* `r04-0023`

- `r04-0064` *STATED* — /mentor session start command: MENTOR start --goal "<what they want to build>" --level <level>.
  — [r-mentor-skill](https://github.com/alexyc9381/mentor-skill)
  ↳ *part-of* `r04-0062`

- `r04-0102` *STATED* — /night-crew install by paste: give Claude 'https://github.com/alexyc9381/night-crew-skill' plus 'Install this skill, then confirm /night-crew works.'
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *example-of* `r04-0004`
  ↳ *example-of* `r01-0003`

- `r04-0103` *STATED* — /night-crew manual install: git clone https://github.com/alexyc9381/night-crew-skill then cp -r night-crew-skill/skills/night-crew ~/.claude/skills/
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0005`
  ↳ *example-of* `r01-0005`

- `r04-0104` *STATED* — /night-crew install with the skills CLI: npx skills add alexyc9381/night-crew-skill
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0005`

- `r04-0105` *STATED* — /night-crew plugin install: /plugin marketplace add alexyc9381/night-crew-skill then /plugin install night-crew-skill@night-crew-skill
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *part-of* `r04-0005`
  ↳ *example-of* `r01-0004`

- `r04-0114` *STATED* — /night-crew uninstall: rm -rf ~/.claude/skills/night-crew, then delete the three routines at claude.ai/code/routines and, if you like, NIGHT-CREW.md from your repo.
  — [r-night-crew-skill](https://github.com/alexyc9381/night-crew-skill)
  ↳ *depends-on* `r04-0111`
  ↳ *contrast* `r04-0103`

- `r04-0217` *STATED* — /shark install by paste: give Claude 'https://github.com/alexyc9381/shark-skill' plus 'Install this skill, then confirm /shark works.'
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0004`
  ↳ *example-of* `r01-0003`

- `r04-0218` *STATED* — /shark manual install: git clone https://github.com/alexyc9381/shark-skill then cp -r shark-skill/skills/shark ~/.claude/skills/
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0005`
  ↳ *example-of* `r01-0005`

- `r04-0219` *STATED* — /shark install with the skills CLI: npx skills add alexyc9381/shark-skill
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0005`

- `r04-0220` *STATED* — /shark plugin install: /plugin marketplace add alexyc9381/shark-skill then /plugin install shark-skill@shark-skill
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *part-of* `r04-0005`
  ↳ *example-of* `r01-0004`

- `r04-0229` *STATED* — The /shark investor personas are defined in skills/shark/investors.json.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *defines* `r04-0211`

- `r04-0231` *STATED* — /shark uninstall: rm -rf ~/.claude/skills/shark
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *contrast* `r04-0218`

- `r04-0244` *STATED* — All /shark bookkeeping goes through python3 "${CLAUDE_SKILL_DIR}/shark.py" <command> (called SHARK in the skill).
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *example-of* `r04-0009`
  ↳ *defines* `r04-0227`

- `r04-0254` *STATED* — /shark Step 3: SHARK init --pitch-file .shark/pitch.md [--investors N] [--seed S].
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *leads-to* `r04-0255`

- `r04-0262` *STATED* — /shark Step 5: SHARK render counts the deals, writes BOARD.md into the run folder and prints it.
  — [r-shark-skill](https://github.com/alexyc9381/shark-skill)
  ↳ *defines* `r04-0215`

- `y01-0079` *STATED* — github.com/zubair-trabzada/ai-agency-claude ('AI agency Claude') is a free GitHub repo that turns Claude Code into an AI agency of teams - marketing, sales, SEO, legal and content - all running inside Claude.
  — [mAZKEu8Akkg](https://youtu.be/mAZKEu8Akkg)

- `y01-0191` *STATED* — fal.ai (Fal AI) cuts out the middleman and gives direct API access to generative video/image models, which you can then use directly inside Claude.
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)

- `y01-0197` *STATED* — After sign-up, fal.ai's page lists the latest models such as GPT Image 2.5, ElevenLabs and MiniMax.
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *part-of* `y01-0196`

- `y01-0221` *STATED* — Setup uses a 'prompting routing file' Alex dropped in the description: copy and paste it into Claude to get set up in minutes.
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *part-of* `y01-0199`

- `y03-0106` *STATED* — Alex made a one-line install for Find Skills so you can add it tonight (comment 'find').
  — [wfwnTNtnomk](https://youtu.be/wfwnTNtnomk) [1j9mmXDW8Qw](https://youtu.be/1j9mmXDW8Qw)
  ↳ *part-of* `g10-0247`
  ↳ *enables* `y03-0100`

- `y04-0017` *INFERRED* — The claude-mem project he features is the GitHub repo thedotmack/claude-mem, a Claude Code plugin.
  — [55RbHPThR8g](https://youtu.be/55RbHPThR8g) [EVTO2eM2DlQ](https://youtu.be/EVTO2eM2DlQ) [6zrQsxiYz1E](https://youtu.be/6zrQsxiYz1E)
  ↳ *evidence-for* `g17-0091`
  ↳ *defines* `y04-0010`

- `y04-0080` *STATED* — One GitHub repo lists over 1000 free APIs that Claude Code can use to build anything you want.
  > “This is how you get 1000 free APIs for Claude Code to build anything you want.”
  — [-U14AktLSiM](https://youtu.be/-U14AktLSiM)
  ↳ *evidence-for* `g13-0153`
  ↳ *enables* `y04-0081`

- `y04-0090` *INFERRED* — The 1000+ free-API repo is most likely public-apis/public-apis on GitHub.
  — [-U14AktLSiM](https://youtu.be/-U14AktLSiM)
  ↳ *evidence-for* `g16-0238`
  ↳ *defines* `y04-0080`

- `y04-0145` *INFERRED* — Agent Reach is most likely the GitHub repo Panniantong/Agent-Reach.
  — [VRRK9REgdaA](https://youtu.be/VRRK9REgdaA)
  ↳ *evidence-for* `g14-0102`
  ↳ *defines* `y04-0140`

### result

- `g02-0192` *STATED* — On Chrome Relay's own test page it passed 23 of 23 checks while agent-browser passed 21 of 23.
  — [g-let-claude-use-your-signed-in-chrome-in-the-background](https://chen.media/guides/let-claude-use-your-signed-in-chrome-in-the-background)
  ↳ *evidence-for* `g02-0185`

- `g04-0023` *STATED* — On the Academic Research Skills repo's own sample paper, the integrity check flagged 15 bad references out of 71.
  — [g-academic-research-skills-make-claude-check-every-source-in-your-paper-is-real](https://chen.media/guides/academic-research-skills-make-claude-check-every-source-in-your-paper-is-real)
  ↳ *evidence-for* `g04-0016`

- `g05-0049` *STATED* — AI Promo Video Maker delivers a 4K video plus a web player.
  — [g-make-a-full-promo-video-with-claude-from-one-sentence](https://chen.media/guides/make-a-full-promo-video-with-claude-from-one-sentence)

- `g19-0214` *STATED* — V0 wins Alex's ranking of the five hyped AI design tools.
  > “Why V0 wins”
  — [g-five-hyped-ai-design-tools-judged-the-way-a-client-would](https://chen.media/guides/five-hyped-ai-design-tools-judged-the-way-a-client-would)
  ↳ *part-of* `g19-0212`
  ↳ *evidence-for* `g19-0216`
  ↳ *contradicts* `g23-0189` — v0: 'V0 wins' his ranking of five hyped AI design tools vs 'replace v0 with Bolt.new'

- `y02-0147` *STATED* — With Cuckoo you can doomscroll or answer emails and never miss the moment Claude needs you.
  — [4iwKLOxgvZQ](https://youtu.be/4iwKLOxgvZQ) [DIJprXkxmIs](https://youtu.be/DIJprXkxmIs)
  ↳ *part-of* `g09-0232`
  ↳ *part-of* `y02-0142`

### style

- `g15-0185` *CORE* — His tool guides open with a 'Read this before you install anything' warning (LinkedIn skills, MetaGPT, and the ADHD-name ambiguity in the verifier guide): vet before installing.
  — [g-linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes](https://chen.media/guides/linkedin-skills-for-claude-eleven-free-skills-that-run-your-linkedin-and-wait-for-your-yes) [g-metagpt-one-line-in-a-whole-software-company-out](https://chen.media/guides/metagpt-one-line-in-a-whole-software-company-out) [g-claude-code-says-done-before-it-has-proved-anything-this-fixes-it](https://chen.media/guides/claude-code-says-done-before-it-has-proved-anything-this-fixes-it)
  ↳ *qualifies* `g15-0041`
  ↳ *evidence-for* `g17-0311`

- `r01-0012` *CORE* — Alex's SKILL.md frontmatter pattern: name, a long 'description' with explicit 'Use when the user types /<name>...' triggers, an argument-hint, license: MIT, and metadata author 'Alex Chen (@nocodealex)', homepage 'https://chen.media', version '1.0.0'.
  — [r-agency-skill](https://github.com/alexyc9381/agency-skill) [r-court-skill](https://github.com/alexyc9381/court-skill) [r-hiring-panel-skill](https://github.com/alexyc9381/hiring-panel-skill)
  ↳ *part-of* `r01-0021`
  ↳ *example-of* `g17-0228`

- `r03-0024` *CORE* — Alex's skill READMEs offer several install routes side by side: paste the GitHub URL into Claude with a one-line instruction, copy the skill folder into ~/.claude/skills/, or add the repo as a plugin marketplace and install from it.
  — [r-learn-skill](https://github.com/alexyc9381/learn-skill) [r-linkedin-roast-skill](https://github.com/alexyc9381/linkedin-roast-skill)
  ↳ *evidence-for* `r04-0005`

### warning

- `g02-0137` *STATED* — Atticus never sends the email replies it writes.
  > “It never sends it.”
  — [g-control-your-whole-mac-with-your-voice-powered-by-claude](https://chen.media/guides/control-your-whole-mac-with-your-voice-powered-by-claude)
  ↳ *qualifies* `g02-0136`
  ↳ *example-of* `g02-0237`
  ↳ *example-of* `g12-0303`

- `g02-0162` *STATED* — With github-triage nothing changes in your repo until you say yes.
  > “Nothing Changes Until You Say Yes”
  — [g-github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say](https://chen.media/guides/github-triage-let-claude-sort-your-github-backlog-nothing-changes-until-you-say)
  ↳ *qualifies* `g02-0161`
  ↳ *example-of* `g02-0237`
  ↳ *example-of* `g12-0303`

- `g03-0036` *STATED* — Claude skills run with a lot of trust: a skill is a folder of instructions and scripts that Claude follows and runs.
  > “Claude skills run with a lot of trust”
  — [g-skillspector-scan-any-claude-skill-for-malware-before-you-install-it](https://chen.media/guides/skillspector-scan-any-claude-skill-for-malware-before-you-install-it)
  ↳ *because* `g03-0035`
  ↳ *leads-to* `g03-0049`
  ↳ *because* `g17-0311`

- `g04-0038` *STATED* — macOS ships Python 3.9, which is too old for Harvey, so on a Mac first run: brew install python@3.13
  — [g-harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies](https://chen.media/guides/harvey-a-free-claude-sales-agent-that-finds-customers-emails-them-and-answers-the-replies)
  ↳ *qualifies* `g04-0037`

- `g05-0207` *STATED* — Claude may only read the first 100 lines of a long skill reference file.
  — [g-claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix](https://chen.media/guides/claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix)
  ↳ *qualifies* `g05-0311`

- `g05-0211` *STATED* — In a long reference file, rules near the bottom can be skipped unless Claude decides the rest is worth reading.
  — [g-claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix](https://chen.media/guides/claude-may-only-read-the-first-100-lines-of-your-skill-files-the-one-minute-fix)
  ↳ *leads-to* `g05-0207`

- `g06-0257` *STATED* — Run the VibeWise install commands one at a time and use one install method only (directory or marketplace, not both).
  > “one at a time, one method only”
  — [g-make-claude-teach-you-while-it-writes-your-code](https://chen.media/guides/make-claude-teach-you-while-it-writes-your-code)
  ↳ *qualifies* `g06-0256`
  ↳ *qualifies* `g18-0155`

- `g07-0298` *INFERRED* — Across his guides Alex treats third-party extensions as a trust decision: Find Skills prefers 1,000+-install skills from known sources, and mods run unsandboxed with your permissions so only trusted authors should be installed.
  — [g-let-claude-find-and-install-the-right-skill-for-any-job](https://chen.media/guides/let-claude-find-and-install-the-right-skill-for-any-job) [g-claude-code-sample-mods-setup-commands](https://chen.media/guides/claude-code-sample-mods-setup-commands)
  ↳ *evidence-for* `g17-0311`

- `g09-0054` *STATED* — Jarvis has a safety switch you should know about before you let it act for you.
  > “the safety switch you should know about before you let it act for you”
  — [g-run-a-jarvis-on-your-own-claude-code](https://chen.media/guides/run-a-jarvis-on-your-own-claude-code)
  ↳ *qualifies* `g09-0050`
  ↳ *example-of* `g09-0247`

- `g12-0170` *STATED* — Guide section 'What gets a plugin held or blocked' covers the reasons Claude Marketplace holds or blocks a submission (body email-gated).
  — [g-claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed](https://chen.media/guides/claude-plugin-store-5-plugins-you-can-build-and-how-to-get-listed)
  ↳ *part-of* `g12-0153`
  ↳ *qualifies* `g12-0169`
  ↳ *part-of* `g12-0154`

- `g14-0045` *STATED* — OpenCut is not CapCut's released source code.
  > “It is not CapCut's released source code.”
  — [g-opencut-repo-and-setup-guide](https://chen.media/guides/opencut-repo-and-setup-guide)
  ↳ *qualifies* `g14-0044`
  ↳ *example-of* `g14-0348`

- `g14-0051` *STATED* — Keep the original media until OpenCut has produced a result you can use.
  > “Keep the original media until you have a result you can use.”
  — [g-opencut-repo-and-setup-guide](https://chen.media/guides/opencut-repo-and-setup-guide)
  ↳ *qualifies* `g14-0048`

- `g14-0078` *STATED* — When installing the Google Antigravity extension, check that the publisher is Google.
  > “check that the publisher is Google”
  — [g-antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you](https://chen.media/guides/antigravity-inside-vs-code-google-s-official-extension-and-what-the-free-tier-actually-gives-you)
  ↳ *qualifies* `g14-0077`
  ↳ *evidence-for* `g17-0311`

- `g14-0107` *STATED* — Check that the Agent Reach channels you need are working before promising a research result.
  > “Check the channels before promising a result”
  — [g-agent-reach-web-research-setup](https://chen.media/guides/agent-reach-web-research-setup)
  ↳ *part-of* `g14-0100`
  ↳ *part-of* `g14-0112`

- `g15-0148` *STATED* — Some AI aggregators are wrappers you should not paste your work into.
  — [g-every-premium-ai-model-in-one-place-how-the-one-tab-route-actually-works](https://chen.media/guides/every-premium-ai-model-in-one-place-how-the-one-tab-route-actually-works)
  ↳ *leads-to* `g15-0149`
  ↳ *evidence-for* `g17-0311`

- `g16-0314` *STATED* — There are known places where people get stuck installing the seven repos.
  > “Where people get stuck”
  — [g-seven-free-claude-code-repos-that-fix-what-claude-gets-wrong](https://chen.media/guides/seven-free-claude-code-repos-that-fix-what-claude-gets-wrong)
  ↳ *qualifies* `g16-0306`

- `g17-0008` *STATED* — If you install the outbound-acting marketing skills first, you get an agent running outbound against a brand system that does not exist yet.
  > “Install the acting ones first and you get an agent running outbound against a brand system that does not exist yet.”
  — [g-seven-free-claude-skills-that-cover-a-marketing-department](https://chen.media/guides/seven-free-claude-skills-that-cover-a-marketing-department)
  ↳ *evidence-for* `g17-0010`
  ↳ *qualifies* `g17-0007` — why acting skills go last
  ↳ *example-of* `g17-0306`

- `g17-0088` *STATED* — A widely syndicated article listed claude-mem at 46.1K stars while the GitHub API returned 90,651, so syndicated star counts can be badly stale.
  > “a widely syndicated article this month lists claude-mem at 46.1K stars and the API returns 90,651”
  — [g-the-three-claude-code-plugins-worth-installing](https://chen.media/guides/the-three-claude-code-plugins-worth-installing)
  ↳ *because* `g17-0087`
  ↳ *qualifies* `g17-0091`
  ↳ *because* `g17-0303`
  ↳ *qualifies* `g02-0235`

- `g17-0094` *STATED* — Read Alex Chen's caveat before installing the second plugin, Find Skills.
  > “Read this before you install the second one”
  — [g-the-three-claude-code-plugins-worth-installing](https://chen.media/guides/the-three-claude-code-plugins-worth-installing)
  ↳ *qualifies* `g17-0090`
  ↳ *example-of* `g17-0307`
  ↳ *evidence-for* `g10-0255`

- `g17-0151` *STATED* — FreeLLMAPI has a failure mode you need to plan for.
  > “The failure mode to plan for”
  — [g-pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint](https://chen.media/guides/pool-the-free-tiers-of-29-ai-providers-behind-one-endpoint)
  ↳ *qualifies* `g17-0150`
  ↳ *qualifies* `g17-0314`

- `g17-0166` *STATED* — There are two things to know before you trust Project NOMAD.
  > “Two things to know before you trust it”
  — [g-a-knowledge-server-that-keeps-answering-with-the-internet-off](https://chen.media/guides/a-knowledge-server-that-keeps-answering-with-the-internet-off)
  ↳ *qualifies* `g17-0155`

- `g17-0229` *CORE* — A vague skill description means the skill never fires.
  > “A vague description means the skill never fires.”
  — [g-164-claude-skills-in-one-repo-which-to-take-first](https://chen.media/guides/164-claude-skills-in-one-repo-which-to-take-first)
  ↳ *because* `g17-0228`
  ↳ *contrast* `g17-0230`

- `g17-0237` *STATED* — There is a mistake almost everyone makes with a big Claude skills repo, named in the guide.
  > “The mistake almost everyone makes”
  — [g-164-claude-skills-in-one-repo-which-to-take-first](https://chen.media/guides/164-claude-skills-in-one-repo-which-to-take-first)
  ↳ *qualifies* `g17-0224`
  ↳ *example-of* `g17-0307`
  ↳ *qualifies* `g13-0281`

- `g18-0052` *STATED* — The 15-replacements guide carries a 'Before you cancel anything' check before you drop a paid subscription.
  — [g-15-more-free-replacements-for-paid-ai-tools](https://chen.media/guides/15-more-free-replacements-for-paid-ai-tools)
  ↳ *qualifies* `g18-0024`

- `g18-0091` *STATED* — Alex's animation guide carries a 'Before you install all five' caveat against installing every skill at once.
  — [g-five-animation-skills-for-claude-code-with-install-commands](https://chen.media/guides/five-animation-skills-for-claude-code-with-install-commands)
  ↳ *qualifies* `g18-0077`
  ↳ *example-of* `g18-0285`
  ↳ *evidence-for* `g13-0281`

- `g18-0205` *STATED* — The five-apps guide adds 'The thing the video did not have time for' and a 'Before you switch anything' check.
  — [g-five-paid-apps-with-full-open-source-replacements](https://chen.media/guides/five-paid-apps-with-full-open-source-replacements)
  ↳ *qualifies* `g18-0198`
  ↳ *example-of* `g18-0280`
  ↳ *evidence-for* `g18-0127`

- `g20-0037` *STATED* — The Obsidian step cannot be done through Claude's Connectors screen.
  > “The Obsidian step cannot be done through the Connectors screen.”
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *part-of* `g20-0034`
  ↳ *qualifies* `g07-0009`

- `g20-0039` *STATED* — Pasting a 127.0.0.1 address into Claude's 'Add custom connector' will fail, and it is not your fault.
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *example-of* `g20-0037`
  ↳ *because* `g20-0038`

- `g20-0045` *STATED* — On Windows the mcp-remote bridge used by the Obsidian step has an open defect: a 60 second hang, then 'Could not attach to MCP server', tracked publicly as geelen/mcp-remote issue 296; the workaround is in the guide's Step 1.
  > “60 second hang, then "Could not attach to MCP server"”
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *because* `g20-0044`
  ↳ *qualifies* `g20-0040`

- `g20-0052` *STATED* — Leave Obsidian open: both Obsidian routes run the server inside Obsidian itself, so closing Obsidian kills the connection mid conversation.
  > “Close Obsidian and the connection dies mid conversation.”
  — [g-give-claude-your-notes-meetings-and-email-the-day-1-setup](https://chen.media/guides/give-claude-your-notes-meetings-and-email-the-day-1-setup)
  ↳ *qualifies* `g20-0040`
  ↳ *qualifies* `g20-0256` — local MCP dies when host app closes
  ↳ *qualifies* `g20-0036`

- `g22-0160` *STATED* — The native Meta Ads connector will always live on a Meta / Facebook domain, never a random third-party site.
  — [g-run-your-meta-ads-from-claude-with-the-official-connector](https://chen.media/guides/run-your-meta-ads-from-claude-with-the-official-connector)
  ↳ *qualifies* `g22-0159`
  ↳ *evidence-for* `g17-0311`

- `y01-0193` *STATED* — Running these models yourself has one danger: no platform holds you accountable for spending, so one mistake can accidentally spend lots of money you didn't intend to.
  — [u0uwzSnPshM](https://youtu.be/u0uwzSnPshM)
  ↳ *qualifies* `y01-0187`
  ↳ *qualifies* `y01-0191`

<!-- AUTO:atoms END -->
