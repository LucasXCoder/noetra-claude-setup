---
name: noetra-librarian
description: >
  The Noetra second-brain librarian. Distills raw sources into an organized, cited, cross-linked
  wiki, and answers questions from it with citations. Use when the user wants to process or ingest
  raw-sources, organize/distill notes, build or update the wiki / second brain, turn
  articles/transcripts/books/videos into knowledge, brief me on a topic from my own notes, find
  gaps in my knowledge, check the brain for contradictions or stale info, or ask the vault a
  question. Operates on ~/noetra-vault (raw-sources/ → wiki/).
---

# Noetra Librarian — second-brain engine

Runs entirely on Claude via the Max plan (no external providers). Vault root: `~/noetra-vault/`.
`raw-sources/` = inbox (dump zone). `wiki/topics/` = atomic distilled notes. `wiki/briefings/` =
saved answers. Be **selective** — distill what earns it; don't bloat the brain or burn quota on noise.

## Mode A — DISTILL (raw-sources → wiki)
Trigger: "process raw-sources", "update my second brain", "organize these notes", "distill X".
1. **Scan** `raw-sources/` for unprocessed material (track processed files in `wiki/.processed.json`
   by path + mtime; skip unchanged).
2. **Read & extract** the durable ideas — claims, frameworks, data, decisions, open questions.
   Ignore filler. One source can yield several atomic notes; trivial sources yield none.
3. **Dedupe first:** search existing `wiki/topics/` (and the Graphify graph) for the concept.
   If it exists, **update/merge** that note instead of creating a duplicate.
4. **Write atomic notes** to `wiki/topics/<kebab-title>.md`, one idea per note, in this format:
   ```
   ---
   title: <clear title>
   tags: [<topic>, <project-if-any>]
   sources: ["raw-sources/<file>"]      # citation anchor — never invent sources
   created: <YYYY-MM-DD>
   updated: <YYYY-MM-DD>
   ---
   <2–6 sentence distilled summary in plain language.>

   ## Key points
   - <atomic claim>  (cite: raw-sources/<file>)

   ## Links
   [[related-note]] · [[another-note]]      # backlinks to related wiki notes
   ```
5. **Citations are mandatory and real** — every claim traces to a file in `raw-sources/`. Never
   fabricate a source. If you inferred/synthesized something, label it `(synthesis)` not a citation.
6. **Backlink** generously to related `wiki/topics/` notes (create the `[[link]]` even if the target
   doesn't exist yet — it marks a note worth writing).
7. **Update the graph:** after writing, run `graphify update ~/noetra-vault` (code/structural, no key).
8. Leave source files in `raw-sources/` (they're the citation anchor). Record what you processed.

## Mode B — ASK THE WIKI (query → cited answer → saved back)
Trigger: "brief me on X", "gaps in my knowledge on X", "what do I know about X", "what changed about X".
1. Pull from `wiki/topics/` + `raw-sources/` + the Graphify graph (query the graph first, then read
   only the notes it points to — token-efficient).
2. Answer with **inline citations** to the wiki/source notes. Be honest about gaps: explicitly list
   what's missing or thin ("you have nothing on …").
3. **Save the answer back** to `wiki/briefings/<YYYY-MM-DD>-<topic>.md` with frontmatter + the notes
   it drew on in `sources:`. This is what makes the brain compound — answers become reusable knowledge.
4. Backlink the briefing to the topic notes it used.

## Mode C — HEALTH CHECK (contradictions + staleness)
Trigger: "brain health check", or run as the Phase 4 morning-standup "brain hygiene" job.
1. Scan `wiki/` for **contradictions** (notes asserting conflicting things) and **stale** notes
   (old `updated:` dates, superseded claims, dead [[links]]).
2. Write findings to `wiki/briefings/<YYYY-MM-DD>-health-check.md`; propose merges/fixes.
3. Apply only safe fixes (dead-link cleanup, merging exact dupes); flag judgment calls for the user.

## Rules
- **Claude/Max only** — never call OpenAI/Gemini/OpenRouter. Local files + Claude reasoning only.
- **Selective & terse** — atomic notes, no padding; quality over volume. Don't distill noise.
- **Never invent citations.** Real source file or `(synthesis)`.
- **Dedupe before create.** Merge into existing notes; the wiki should converge, not sprawl.
- Cross-references with claude-mem are fine — but the wiki is the durable, human-readable brain;
  claude-mem is session recall. Keep them complementary.
