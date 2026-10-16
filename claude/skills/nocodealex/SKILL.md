---
name: nocodealex
description: The distilled brain of Alex Chen (@nocodealex on Instagram, @alexchenbuildsai on YouTube, chen.media guides, github.com/alexyc9381) — Claude and Claude Code optimisation (usage limits, /compact, /context, model routing, effort levels, hooks, mods, settings, fixes for Claude stopping or repeating mistakes), Claude skills/plugins/MCP and free open-source tool alternatives, multi-Claude panels (/court, /shark, /launch, /hiring-panel, /hunter, /linkedin-roast, /mentor, /learn, /night-crew, /agency), prompting and output quality, and building/selling with AI. Trigger generously — invoke on /nocodealex, on any mention of Alex Chen, nocodealex, chen.media or his skills, and whenever the user asks how to make Claude better, cheaper, longer-lasting or less annoying, or wants his methods applied.
---

# nocodealex brain — Alex Chen

Distilled from his public output: YouTube (long-form + shorts, cross-posted from his Instagram reels),
the free part of every chen.media guide (one guide per reel), and the prose of his GitHub skill repos.
Facts here are HIS claims and methods, not validated results.

## How to use it

1. **Always read `references/knowledge.md` first** — the core distillation plus the Topic Map.
2. **Route by the Topic Map** — load only the `references/topics/*.md` files the question needs.
3. **Run a checklist from `references/protocols.md`** when the user brings a session, a setup, an
   idea or an app his method applies to. Do the steps; do not just recall them.
4. **Grep `atoms.jsonl`** for targeted lookups by `type`, `topic`, `tags` or `confidence`
   (e.g. every `method` tagged `compact`). Traverse `edges.jsonl` to follow his reasoning.
5. **Drop to the raw source** via `sources/manifest.json` (`text_path`, `url`) for exact wording:
   `sources/transcripts/{id}.txt`, `sources/guide_text/g-*.txt`, `sources/repo_text/r-*.txt`,
   and the cloned repos in `sources/repos/`.
6. **Apply his frameworks**, not generic advice. Where he differs from the docs, say both and
   prefer the official docs for exact command/setting syntax (Claude Code changes fast).
7. **Respect confidence.** Lean on `CORE`; qualify `STATED`; flag `INFERRED` as synthesis.
   Atoms tagged `toc-only` come from a guide's section title whose body is email-gated — they
   name the technique but not his full explanation.
8. **Surface contradictions** (`rel: "contradicts"` edges); never smooth them over.

## Limits

Public teaching only — NOT validated, and only as current as `sources/manifest.json`'s fetch
date. chen.media guide bodies past section 1 are email-gated, so guides are `free_only`.
Instagram itself is login-walled; its reels are covered through their YouTube cross-posts and
guides (see `sources/instagram/status.json`). The user's own rule outranks any tip here: Claude
models via the Max plan only — skip any of his tips that route work to other model providers.

Rebuild after new mining: `python -I build_manifest.py` then `python -I build_brain.py`
(validates, gates density + connectivity, regenerates topic indexes and `graph.html`).
