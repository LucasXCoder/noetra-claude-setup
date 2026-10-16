---
name: engram
description: Factory skill that builds callable knowledge-base "brain" skills from a creator's entire public channel plus optional documents. Trigger whenever the user invokes /engram, asks to "build a brain," "make a knowledge base," ingest a YouTube channel / IG / TikTok profile, or add reports to an existing brain. Trigger generously.
---

# ENGRAM — Brain Factory

Engram holds no knowledge itself. Each run builds (or updates) ONE callable "brain" skill
distilled from a creator's entire public output. One brain per creator/source. Brains are
**tiered**: core distillation → topic deep-files → preserved raw sources → an atom/edge graph.
Follow every step below when /engram runs.

## Inputs (from the user)

- A YouTube **CHANNEL** link — the whole channel, not single videos
- Optional Instagram / TikTok **PROFILE** link
- Optional extra material: reports, PDFs, articles, pasted notes
- A short name for the new brain (e.g. `delta`)

If the name is missing, derive one from the creator's handle and state the choice in the
final report.

## Step 1 — ENUMERATE + FETCH the whole channel

1. Use **yt-dlp** to list every video AND check the `/shorts` tab:
   `yt-dlp --flat-playlist --print "%(id)s|%(view_count)s|%(upload_date)s|%(title)s" <channel-url>/videos`
   Install tooling as needed (`pip install yt-dlp youtube-transcript-api`).
   **Never ask the user to paste transcripts.**
2. Pull transcripts / auto-captions for each video — `youtube-transcript-api` first (faster),
   falling back to `yt-dlp --write-auto-subs --skip-download --sub-format json3` per video.
   Expect IP rate-limits (HTTP 429 / IpBlocked) on large channels; they persist for hours —
   don't spin retrying.
3. **Process EVERY video that has a fetchable transcript — never subset or "prioritize" down to
   a sample.** The whole point is the COMPLETE brain. For a huge channel, work through it in
   batches across multiple passes (views + recency is only the *order* you take batches in,
   never a stopping point). The only videos left out are those with no captions at all — list
   those explicitly. Report progress as "N of M done" and keep going until N = every captioned
   video.
4. IG / TikTok profiles: pull post captions and on-screen/spoken text where accessible.
5. Fallbacks — if captions are disabled, rate-limited, or a source is blocked (IG/TikTok
   without login are usually fully blocked): fetch metadata instead —
   `yt-dlp --skip-download --print "%(.{id,title,description})j"` — descriptions often carry
   the video's core claim. Note exactly what was missed, and continue. Never stall the whole
   build on one blocked source.

## Step 2 — INGEST EXTRA MATERIAL

Read every provided report / PDF / article / pasted note and fold it into the same brain,
tagged by source.

## Step 3 — DISTILL (EXHAUSTIVE — this is the whole point of a brain)

> ⚠️ **You are cloning the creator's brain into a skill — that is the entire point of
> ENGRAM.** The job is to capture **EVERYTHING of value** from their content, not a tidy set
> of teachable claims. Results they got, ideas they floated, things they're building, products
> and tools they use, who they criticize, how they work, what they believe, their personality
> and recurring phrases — all of it. Someone querying this brain should get answers as if the
> creator were sitting there. The #1 failure mode is summarizing: a holistic "pull the key
> points" pass collapses a 5,900-word video into a handful of records and throws away ~95% of
> the person. That is a broken build. Mine like you are reconstructing a mind, not reviewing a
> lecture.

### 3a. Mine window-by-window, never whole-video-at-once

Process every transcript in **tiny windows of ~2–4 sentences** (not 500-word chunks). For EACH
window, capture every distinct valuable thing before moving on. Do not read the whole
transcript and then write a summary — that is exactly what loses the person.

**Capture EVERYTHING valuable — each as its own typed ATOM.** Do not restrict to "claims";
these types all belong in the brain (an atom's `type`):

| `type` | capture… |
|---|---|
| `claim` | a factual assertion, rule, heuristic, definition, framework (and each component) |
| `concept` | a named idea/structure other atoms hang off of |
| `definition` | what a term means |
| `number` | a statistic, threshold, price, or measured value — with its exact setup |
| `result` | a backtest/experiment outcome or P&L — with its exact setup |
| `example` | a worked example or anecdote — its setup AND its result/lesson |
| `analogy` | an analogy or intuition pump they use to teach |
| `method` | how they actually DO something — a workflow/technique, step by step |
| `caveat` | a qualification, condition, or edge case |
| `idea` | a proposal, hypothesis, future plan, "I might try…", what they want to build next |
| `product` | something they built or use — tool, app, course, service — and what it does |
| `opinion` | a take, stance, value judgment, or who/what they criticize |
| `warning` | an anti-pattern, trap, or thing they reject |
| `prediction` | a forecast or expectation they state |
| `bio` | identity / background facts (school, history, affiliations) |
| `resource` | a book, person, paper, dataset, or tool they cite |
| `style` | recurring phrases, personality, how they communicate |

If something is valuable and fits none cleanly, capture it with the closest `type` —
**never drop it because it isn't a "claim."** When in doubt, keep it.

### 3b. One ATOM per assertion (the unit is a single fact, not a paragraph)

- **An atom is a single irreducible fact you could cite on its own.** Split every compound
  sentence: "it's traded by retail, HFT, and institutions" → 3 atoms; "tight stop, wide TP, low
  win rate" → 3 atoms. Each atom stands alone as true.
- **Density target ≈ 1 atom per ~18–25 words** of substantive teaching — every distinct
  assertion, number, definition, example beat, caveat, and aside, at the grain of a careful
  human note-taker. A 2,000-word video yields **~80–110 atoms, not ~15**.
- **The bar is EXHAUSTION** — mine each window until re-reading surfaces nothing new — but
  **quality gates quantity.** A finer grain is right ONLY when each piece is independently
  meaningful; **never split one idea into hollow fragments to hit a number** — that drowns
  signal just as badly as summarizing. When unsure whether two fragments are really one idea,
  keep them as one atom and join related atoms with an *edge* (3d), don't emit noise.
- Pure filler (greetings, "smash like", bare self-promo) is the only thing you skip.
- **This atom + edge model is the standard from the FIRST pass.** There is no coarse "claims"
  draft to upgrade later — build at full atom density, with reasoning edges, from atom one. A
  brain's very first version is already the everything-quality version.

### 3c. Tag, cite, preserve

- Tag confidence: `CORE` (foundational, repeated across sources) / `STATED` (said explicitly,
  once or twice) / `INFERRED` (implied, your synthesis).
- **Cite the source ID** on every atom (`sources[]`). Preserve ALL numbers, thresholds, and
  conditions exactly. Optionally keep the creator's exact words in `verbatim`.
- Record contradictions via a `contradicts` edge — **never smooth them over**.

### 3d. CONNECT atoms into a reasoning graph (`edges.jsonl`)

Atoms alone are a bag of facts; the **edges are what make it a brain.** After a window's atoms
are written, link them with **typed edges** — `{from, to, rel, note?}` where `rel` ∈ `because` /
`defines` / `part-of` / `example-of` / `analogy-for` / `evidence-for` / `qualifies` /
`contrast` / `contradicts` / `leads-to` / `enables` / `depends-on` / `generalizes`. Capture the
creator's ARGUMENT, not just their facts: which number is evidence for which claim, which
example illustrates which concept, what causes / qualifies / contradicts what. **Most atoms
should be touched by ≥1 edge** — isolated atoms usually mean you missed a connection. This graph
is what lets the brain answer "walk me through his reasoning," not just "quote a fact."

### 3e. COVERAGE GATE — verify density + connectivity before you finish (mandatory)

After writing `atoms.jsonl` + `edges.jsonl`, run the bundled audit and re-mine anything thin:

```
python coverage_audit.py ../{name}
```

It flags any source below the atom-density gate (calibrated to honest exhaustion at the atom
grain) and reports edge connectivity. For every flagged source, re-mine window-by-window until
it clears; if a source has atoms but almost no edges, it was captured as a *list*, not a brain —
go back and link it. The audit **exits non-zero while anything is flagged — treat that as "build
NOT done."** Report the final density + connectivity in the build summary.

## Step 4 — WRITE THE BRAIN SKILL (tiered layout)

Write to `./{name}/` **under the skills directory** (i.e. `.claude/skills/{name}/`, sibling
of this engram folder) so it registers as a callable skill:

```
{name}/
├── SKILL.md                      ← trigger + routing instructions
├── atoms.jsonl                   ← NODES: one typed atom (irreducible fact) per line
├── edges.jsonl                   ← EDGES: typed links between atoms (the reasoning graph)
├── build_brain.py                ← validate + density/connectivity gate; calls build_graph at the end
├── build_graph.py                ← renders graph.html FROM atoms.jsonl + edges.jsonl (source of truth)
├── graph.html                    ← interactive visualization (always regenerated, never hand-edited)
├── references/
│   ├── knowledge.md              ← CORE distillation (always read) + Topic Map table
│   ├── protocols.md              ← the creator's METHODS as executable checklists
│   └── topics/                   ← 3–7 deep files split by domain, full numbers,
│       └── <topic>.md               per-atom source-ID citations
└── sources/                      ← GROUND TRUTH (never distilled away)
    ├── manifest.json             ← every item: id, type, title, url, coverage
    │                                (transcript | description_only | missed) + fetch date
    ├── transcripts/{id}.txt      ← all raw transcripts
    └── <docs, descs.jsonl, …>    ← any extra ingested material, raw
```

**Layer rules:**
- `knowledge.md` = the 12-section schema below, kept lean enough to always load, with a
  **Topic Map** table routing each question type to its topic file.
- `topics/*.md` = the depth: complete numbers, worked examples, per-atom citations of source
  IDs. Split by domain so a question loads one or two files, never all. **Keep them in sync
  with `atoms.jsonl` — the atom/edge graph is the source of truth.** The robust pattern is a
  small generator that (re)writes a marked, regenerable index block (every atom for that topic +
  its source-video link, grouped by type) into each topic file, so the conversational layer
  `/{name}` reads first can never drift below the graph. Run it whenever atoms change, and
  create a new topic file for any genuinely new domain (e.g. the creator's product/bio).
- `protocols.md` = what the creator would DO: 3–6 step-by-step checklists distilled from
  their demonstrated workflow (with decision gates and required outputs), so the brain can
  run the method against user inputs, not just recall facts.
- `atoms.jsonl` = the NODES — one irreducible fact per line:
  `{id, type, topic, confidence, sources[], text, verbatim?, numbers[]?, tags[]}`
  — `type` is one of the Step 3a kinds. `text` is the atom; `verbatim` optionally holds the
  creator's exact words.
- `edges.jsonl` = the typed reasoning graph between atoms:
  `{from, to, rel, note?}`, `rel` ∈ because/defines/part-of/example-of/analogy-for/evidence-for/
  qualifies/contrast/contradicts/leads-to/enables/depends-on/generalizes. Validate after writing:
  atom ids unique, every edge endpoint resolves, most atoms touched by ≥1 edge. This graph
  enables grep/jq lookups, reasoning traversal, cross-brain comparison, and visualization.
- `graph.html` = the visualization, and it is **generated, never authored**. `build_graph.py`
  reads `atoms.jsonl` + `edges.jsonl` (nodes colored by topic, sized by edge degree, hover =
  atom text/type/confidence + a `youtu.be/<sourceid>` link) and `build_brain.py` calls it at the
  end of EVERY run — so the graph can never go stale relative to the store. Never hand-edit the
  HTML and never build the graph from any legacy/flat file; the atom/edge store is the only source.
- `sources/` = raw fidelity. Copy fetched transcripts/docs here BEFORE temp dirs get cleaned.
  The distillation is lossy; the sources are not.

The brain's `SKILL.md` frontmatter:
- `name: {name}`
- `description:` triggers (user invokes `/{name}`, references the creator by name/handle, or
  asks to apply their knowledge/strategies — list the creator's main domains as trigger
  keywords) + what the brain does + an explicit push to **trigger generously**.

The brain's `SKILL.md` body must instruct Claude to:
1. Read `references/knowledge.md` first, always.
2. Route deeper via the Topic Map — load only matching `topics/*.md` files.
3. RUN the matching `protocols.md` checklist when the user brings inputs the creator's
   method applies to (compute and simulate where the protocol calls for it).
4. Grep `atoms.jsonl` for targeted lookups by type/tag/topic/confidence, and traverse
   `edges.jsonl` to follow the creator's reasoning.
5. Drop to `sources/transcripts/{id}.txt` (via manifest.json) for exact wording or disputed
   claims.
6. **APPLY** the creator's frameworks, not generic knowledge.
7. Respect confidence tags: lean on `CORE`, qualify `STATED`, flag `INFERRED`.
8. Honor the limits: distilled public teaching — NOT validated, NOT financial advice, only as
   current as the manifest's fetch date.
9. Surface recorded contradictions; never smooth them.

## Step 5 — REGISTER the brain

Update `registry.json` (sibling of this file): add or update the brain's entry — name,
creator, handle, domains, path, trigger, coverage counts, source URLs, file map,
atom/edge counts, built/last_updated dates. The registry is the fleet index: it answers "which
brain knows about X?" and feeds future fleet visualization. Bump its top-level `updated` date.

## Knowledge file schema (`references/knowledge.md`)

```markdown
# KNOWLEDGE BASE: [Creator]
**Domain:** …  **Sources:** [channel + docs]  **Videos processed:** X of Y
**Last updated:** [date]

## Topic Map — deep files (load on demand)   ← table: topic file → when to load it

## 1. Identity & Bio         — who they are, background, affiliations, what they're known for
## 2. Core Philosophy        — 3–7 foundational beliefs, CORE only
## 3. Mental Models & Frameworks — name, when it applies, step by step
## 4. Methods & Workflows     — how they actually DO things, step by step
## 5. Rules & Heuristics     — concrete if-then rules, all numbers preserved
## 6. Key Concepts Explained — distilled enough to apply without rewatching
## 7. Results & Data Points  — their stats/backtests/outcomes, dated, with exact setup
## 8. Products, Tools & Things They've Built — what each is and does, how it's used
## 9. Ideas & Things They're Exploring — proposals, plans, open hypotheses, "I might build…"
## 10. Opinions & What They Reject — takes, who/what they criticize, anti-patterns, traps
## 11. Open Questions / Contradictions / Gaps
## 12. How To Apply This Base — what it's good for, what NOT to trust it for
```

## Merge behavior

If `./{name}/` already exists: **MERGE** — never overwrite.
- Add newly fetched transcripts/docs to `sources/` and update `manifest.json` (coverage
  upgrades: missed → description_only → transcript) and its fetch date.
- Append new items into the right sections of `knowledge.md` and the right `topics/*.md`
  files; **never drop existing items**. Create a new topic file only if a genuinely new
  domain appears.
- Update **Videos processed** and **Last updated**; new contradictions with old items go in
  section 11.
- Append new atoms to `atoms.jsonl` and new links to `edges.jsonl` (never drop or renumber
  existing ids); extend `protocols.md` if the creator's method evolved; update the brain's
  `registry.json` entry (coverage, atom/edge counts, last_updated).

## Finishing & resuming (multi-pass builds)

A build is **NOT done** until `python coverage_audit.py {name}` exits 0 — every captioned
source has atoms + edges and clears the density gate. Never report a brain as finished while
any source is flagged; re-mine it first. This is the hard guarantee that every brain hits the
same depth.

**A full channel usually cannot be mined in one sitting** (turn/size limits) — mining every
video at the atom grain is many batches. Handle that honestly:

- The state lives in the brain itself: `sources/manifest.json` lists ALL videos; `atoms.jsonl`
  records which are DONE. The remaining set = manifest videos with no atoms yet. `coverage_audit.py`
  (or the brain's build tool) prints `N of M done`.
- Each run, **process remaining videos in batches until the run is full**, then run the audit.
- **If the gate is not yet green when the run ends, do NOT pretend it's finished.** End with
  exactly: **"PARTIAL — N of M videos done. Run `/engram {name}` again to continue."**
- A re-run **resumes automatically**: it reads the existing `atoms.jsonl`, skips videos already
  mined (the MERGE path), and continues only the remaining ones. Repeat until the gate exits 0.
- Only when `coverage_audit.py` exits 0 do you report **DONE** with the full summary.

## Final report (when DONE)

After building (or updating) a brain, show the user:
1. The `coverage_audit.py` density + connectivity output proving every source passes (exit 0).
2. The full file tree of `{name}/` (including topics/ and sources/ counts).
3. The **full** `knowledge.md` contents.
4. Coverage stats: transcript / description-only / missed, and what to re-run later to fill gaps.
