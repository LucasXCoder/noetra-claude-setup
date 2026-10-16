# PLAN — Claude re-optimization (nocodealex brain + research + apply + Mac transfer)

Started 2026-10-16. Ledger: `GATES.md` (this folder). Verifier: `tools/verify.mjs`.

## Request inventory (every independently omittable outcome)

| # | Outcome the user asked for | Gate(s) |
|---|---|---|
| R1 | Engram brain of **nocodealex** (Alex Chen) built from ALL reachable content | G1, G2, G3, G4 |
| R2 | Find a way to get his links / content (Instagram blocked) | G1 (manifest records every route tried) |
| R3 | "Fair share" of research beyond nocodealex — best quality, usage limits, function, fixes | G5 |
| R4 | Apply the optimization to this Windows Claude (skills, MCP, settings, other programs) | G6, G7 |
| R5 | Fix Claude problems (broken MCP, tooling mismatches, known failure modes) | G6 |
| R6 | Transfer the optimization to the Mac | G8 |

## Constraints (acceptance-changing)
- Claude / Max plan ONLY — no third-party model providers or paid keys in any recommendation (CLAUDE.md hard rule).
- $0 spend. Every config change is backed up first and listed in `CHANGELOG.md` with its revert.
- Never break the running setup: claude-mem capture/recall, unlazy Stop hook, superpowers.
- No account creation on Instagram (ToS + phone verification + identity). No bypassing chen.media's email gate.
- User email is never submitted to a third party without explicit consent.
- Native `~/.claude/projects/.../memory/` is FROZEN — do not write there.

## Source map (discovered 2026-10-16)
- Instagram `@nocodealex` — login wall, HTTP 429 on API, yt-dlp extractor broken. Reels are cross-posted.
- YouTube `@alexchenbuildsai` — 4 long-form + 114 shorts (the IG reels' cross-posts).
- chen.media — 385 guides (one per reel: "comment X and I'll DM you the guide"); free part = lede +
  section 1 + every section title; remainder email-gated → coverage `free_only`.
- GitHub `alexyc9381` — 11 original skill repos (+8 forks of awesome-lists = resources, not his work).

## Tree
1. **acquire** — fetch YT transcripts+meta, guides, repos → `sources/manifest.json`  → G1
2. **mine** — atom/edge extraction per source batch (workflow, shards) → merge → G2, G3
3. **write** — SKILL.md, knowledge.md, topics/, protocols.md, graph.html, registry → G4
4. **research** — outside sweep + adversarial verification against official docs → `research/REPORT.md` → G5
5. **apply** — optimization plan from brain + research → `~/.claude` changes + CHANGELOG → G6, G7
6. **mac** — portable bundle + `install.sh` + dry-run test → G8

## Status log
- 2026-10-16 acquire: running (YT fetch, guides fetch); repos cloned (11).
- 2026-10-16 acquire: guides 385/385 fetched (all email-gated → free_only, 105.7k clean words).
  YouTube caption endpoints IP-blocked after 20 videos → local faster-whisper (small.en) on
  audio-only downloads (PyAV 15+ incompatibility worked around by decoding in-script).
  chen.media unlock not attempted: email gate is the site's access control (auto-mode
  classifier also blocked JS inspection) — offered to the user as an opt-in upgrade.
- 2026-10-16 mine: 27 batches (g01-g23 guides, r01-r04 repos) dispatched as workflow
  wf_3abeb3dc-d33 (first launch wf_f5a0149e-d37 stopped: bad args, no files written).
- 2026-10-16 research: workflow wf_02db8e0a-775 (7 areas → adversarial verify → REPORT.md).
- 2026-10-16 fix: engram coverage_audit.py now reads atoms.jsonl + manifest text_paths
  (backup in backups/2026-10-16/skills/engram/).
- 2026-10-16 FOUND+FIXED: claude-mem 13.39.0 exec-form hooks bypassed noetra-patch-hooks.py →
  AI observer silently re-enabled. Patcher fixed (command+args, PostToolUseFailure, python3 on
  Mac); 9 hooks.json re-patched; `--check` → NOETRA HOOKS OK. Durable self-heal hook pending (apply).
- 2026-10-16 acquire DONE: YouTube 118/118 transcribed (20 captions + 98 whisper; last one needed
  `--js-runtimes node`). G1 SOURCES OK.
- 2026-10-16 mine: y01-y04 dispatched (wf_f753b8dc-822). Early shards: density 1/14-1/24, 100% connected.
- 2026-10-16 MERGED: 8,291 atoms / 10,772 edges, 514/514 sources, 1 atom/14.9 words, 100% connected.
  G0-G3 met. magic MCP removed (fix-mcp-magic). Mac bundle builder + install.sh written, trial-built.
- 2026-10-16 PAUSED (usage limit). Both workflows stopped; finished agents are cached.
  RESUME: research → Workflow({scriptPath: workflows/scripts/claude-optimize-research-wf_02db8e0a-775.js,
  resumeFromRunId: "wf_02db8e0a-775"}) (13/15 agents cached). Brain write → resume
  wf_f61acd78-30c (script nocodealex-brain-write-wf_f61acd78-30c.js, args {atoms:8291, edges:10772}).
  Then: build_brain.py → registry entry → G4; apply phase (skillOverrides name-only for niche
  unused skills, self-heal SessionStart hook, research items) → G6/G7; bundle: exempt
  unlazy/tests + noetra Windows records from the path check → G8.
