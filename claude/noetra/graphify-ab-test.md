# Graphify Token A/B Test — MasterQuantLabs

Goal: measure real tokens-per-session to answer the SAME architecture question
**without** the graph (Claude reads files) vs **with** the graph (Claude queries it).

Test bed: `~\Downloads\MasterQuantLabs` (95 files, ~101K words)
Graph already built (zero-token): `graphify-out/` — 779 nodes, 1318 edges, 75 communities.

### The question (use verbatim in both runs)
> Trace how `MCResult` is produced and consumed across the backend: which modules
> create it, which modules consume it, and what entry point kicks off the Monte
> Carlo run. Cite the files involved.

---

## RUN A — Baseline (NO graph, Claude reads files)
1. In PowerShell:
   ```powershell
   Rename-Item "~\Downloads\MasterQuantLabs\graphify-out" graphify-out.bak
   ```
2. Open a **fresh** Claude Code session in `MasterQuantLabs`.
3. Paste the question above. Let Claude answer (it will read/grep files).
4. Run `/cost` → record **total tokens** (input+output) as **A**.

## RUN B — With graph (Claude queries graphify)
1. Restore the graph:
   ```powershell
   Rename-Item "~\Downloads\MasterQuantLabs\graphify-out.bak" graphify-out
   ```
2. Open a **fresh** Claude Code session in `MasterQuantLabs`.
3. Paste the SAME question. Claude should answer via the graph (`graphify explain` /
   `graphify path` / GRAPH_REPORT.md) instead of reading every file.
4. Run `/cost` → record **total tokens** as **B**.

## Result
- Savings % = (A − B) / A × 100
- Record A, B, and % below for the Checkpoint 1 record.

---

## Pre-measured estimate (from actual file sizes — to sanity-check your live numbers)
- **Baseline read cost** for this question (Monte Carlo + propfirm + analysis modules
  + entry points): ~131,867 bytes ≈ **~33,000 tokens** just to read the relevant files.
  (A broader grep-and-read exploration could approach the full corpus ≈ ~135K tokens.)
- **Graph cost**: `GRAPH_REPORT.md` ≈ ~4,000 tokens (often only a slice needed) +
  a few `explain`/`path` queries at a few hundred tokens each ≈ **~1,000–4,000 tokens**.
- **Estimated reduction on this task: ~88–94%.** Build cost to get there: **0 tokens.**

Note: savings scale with codebase size and how much file-reading the question would
otherwise require. Small, localized questions save less; broad architecture questions
on large repos save the most.
