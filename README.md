# Noetra Claude setup

A tuned [Claude Code](https://code.claude.com) setup, packaged so a second machine (a Mac) can reach the same
level with one command: a lean `CLAUDE.md` with a mandatory verify-before-done workflow, 86 skills, 32 agents,
safety hooks, a status line, a cost-aware `settings.json`, and a knowledge brain built from
[Alex Chen's (@nocodealex)](https://github.com/alexyc9381) public Claude content.

Built on a Windows PC on Claude's Max plan, with a hard rule: **Claude models only, no third-party providers, $0 autonomous spend.**

## Put it on a Mac (pick one)

**A. One command** (fresh Mac, nothing installed):
```bash
curl -fsSL https://raw.githubusercontent.com/LucasXCoder/noetra-claude-setup/main/bootstrap.sh | bash
```
It installs Xcode tools, Homebrew, Node and Claude Code, clones this repo to `~/noetra-claude-setup`, installs everything,
then verifies. Read [`bootstrap.sh`](bootstrap.sh) first if you like. Preview without changing anything:
`curl -fsSL …/bootstrap.sh | bash -s -- --dry-run`.

**B. Let the Mac's Claude do it** (Claude Code already installed and logged in). Paste this into Claude Code on the Mac:
> Set up this Mac's Claude Code from https://github.com/LucasXCoder/noetra-claude-setup — clone it, read INSTALL-FOR-CLAUDE.md, and follow it exactly. Run install.sh --dry-run first and tell me the plan, then install, then run verify.sh and show me its output. Don't touch permissions or auto-mode settings, and don't print any secrets.

**C. By hand:** `git clone https://github.com/LucasXCoder/noetra-claude-setup.git && cd noetra-claude-setup && ./install.sh && ./verify.sh`

`install.sh` is idempotent and backs up anything it replaces to `~/.claude/backups/pre-noetra-<time>/`.
Flags: `--dry-run`, `--no-network` (files only), `--home DIR`.

## After installing (by hand, 3 minutes)
1. `claude` → log in with your Max account.
2. claude.ai → Settings → Usage: **Usage credits OFF**.
3. Re-add MCP servers that need secrets (names are in `manifest.json`; secrets are never in this repo).
4. Restart Claude Code, then `/doctor` and `/usage`.

## What is in it
| Path | What |
|---|---|
| `claude/CLAUDE.md` | Master memory file: mission, money gate, **Mandatory workflow** (done = a check exits 0; superpowers in order; unlazy gates for big work), memory design |
| `claude/settings.template.json` | Per-model effort (`high` on Sonnet/Opus 5.5), 400K auto-compact, fast mode off, claude-mem seal, status line, guard hooks |
| `claude/skills/` | 86 skills incl. `nocodealex` (the brain), `unlazy` (completion gates), `engram` (brain factory), design skills |
| `claude/agents/` | 32 subagents (`Explore` runs on Haiku) |
| `claude/hooks/` + `statusline.mjs` | `guard-shell` (blocks destructive commands), `protect-files` (blocks edits to `.env`, keys, rule files), usage status line |
| `claude-mem/` | Scripts that keep claude-mem's AI note-taker off (it spends your allowance) and stream sessions into memory with no LLM |
| `claude/noetra/claude-optimize/research/REPORT.md` | The research behind every setting: 210 sources, 150 official, each claim fact-checked |
| `verify.sh` | Checks the install: tools, settings, skills, hook behavior (it really tries `git reset --hard`), brain, memory |

## Using this as someone else
Anyone can use it (MIT licence). It installs a ready-made Claude Code setup: skills, agents, hooks, plugins and a memory system.

- **Your own login.** It never copies logins or keys. You sign in with your own Claude account; usage comes out of your own plan.
- **Make CLAUDE.md yours.** `claude/CLAUDE.md` is the author's personal file. Its Trading Research rules, the Noetra projects and the priorities are specific to him. Read it and delete or rewrite what is not yours before or right after installing.
- **Your memory starts empty.** The author's memories, vault and private notes are not included.
- **Check before you trust.** Run `./install.sh --dry-run` first; it prints every change. Hooks run code on your machine, so read them.

## Not in this repo (on purpose)
Other creators' brains (`delta`, `tradexlabs`), raw scraped transcripts and guide text, the owner's private task list,
the 600 MB+ memory database, and every secret. `manifest.json → private_items` lists them. `master-todo.md` is a stub.

## Attribution and licence
The `nocodealex` skill is an index of public content by **Alex Chen (@nocodealex)** — [YouTube](https://www.youtube.com/@alexchenbuildsai),
[chen.media](https://chen.media/guides), [GitHub](https://github.com/alexyc9381) — with links back to each source; it is not affiliated with him.
Third-party skills in `claude/skills/` keep their original licences. Original work in this repo is MIT ([LICENSE](LICENSE)).
