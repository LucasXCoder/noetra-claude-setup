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
