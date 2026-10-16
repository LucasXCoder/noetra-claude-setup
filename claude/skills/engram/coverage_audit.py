"""ENGRAM coverage audit — catches under-extracted sources.

Usage:  python coverage_audit.py <path-to-brain>      e.g.  python coverage_audit.py ../delta

Reads the brain's NODE store — atoms.jsonl (current standard), falling back to the legacy
claims.jsonl — and its source texts, then reports words vs records per source. Source texts
come from sources/manifest.json items that carry a `text_path` (so guides, docs and repo
prose are gated the same way as video transcripts); without such a manifest it falls back to
sources/transcripts/*.txt. Flags any source below the density gate or with ZERO records —
those must be re-mined before a build is considered done. Sources under MIN_WORDS carry no
teaching and are listed as trivial, not flagged.

Density reference (from SKILL.md Step 3b) — enforces UNIFORM detail across every creator:
  - target FLOOR (all sources)           ~ 1 record / 120 words
  - hard GATE, long-form (>=1500 words)  ~ 1 record / 150 words  (re-mine if below)
  - hard GATE, shorter sources           ~ 1 record / 170 words  (re-mine if below)
Also reports edge connectivity (share of atoms touched by >=1 edge in edges.jsonl).
"""
import collections
import json
import os
import sys

# Windows consoles default to cp1252 and crash on non-ASCII; force UTF-8 where possible.
try:
    sys.stdout.reconfigure(encoding="utf-8")
except Exception:
    pass

GATE_LONGFORM = 150             # long-form (>=1500w): FAIL above this words/record
GATE_DEFAULT = 170              # shorter sources: FAIL above this words/record
FLOOR_WORDS_PER_RECORD = 120    # aspirational floor; passing-but-above is reported "thin"
LONGFORM_WORDS = 1500           # sources at/above this are held to the stricter long-form gate
MIN_WORDS = 20                  # below this a source carries no teaching (e.g. a music-only short)


def read_records(brain):
    for name in ("atoms.jsonl", "claims.jsonl"):
        path = os.path.join(brain, name)
        if os.path.exists(path):
            with open(path, encoding="utf-8") as f:
                return name, [json.loads(l) for l in f if l.strip()]
    sys.exit(f"no atoms.jsonl or claims.jsonl in {brain}")


def word_count(path):
    with open(path, encoding="utf-8", errors="ignore") as f:
        return len(f.read().split())


def read_sources(brain):
    manifest = os.path.join(brain, "sources", "manifest.json")
    if os.path.exists(manifest):
        with open(manifest, encoding="utf-8") as f:
            items = json.load(f).get("items", [])
        paths = {it["id"]: it["text_path"] for it in items if isinstance(it, dict) and it.get("text_path")}
        if paths:
            return {sid: word_count(os.path.join(brain, p)) for sid, p in paths.items()
                    if os.path.exists(os.path.join(brain, p))}
    tdir = os.path.join(brain, "sources", "transcripts")
    if not os.path.isdir(tdir):
        return {}
    return {fn[:-4]: word_count(os.path.join(tdir, fn)) for fn in os.listdir(tdir) if fn.endswith(".txt")}


def main(brain):
    brain = os.path.abspath(brain)
    store, records = read_records(brain)
    per_src = collections.Counter(s for d in records for s in d.get("sources", []))
    words = read_sources(brain)

    rows, trivial = [], []
    for sid, w in words.items():
        if w < MIN_WORDS:
            trivial.append(sid)
            continue
        c = per_src.get(sid, 0)
        wpc = (w / c) if c else float("inf")
        gate = GATE_LONGFORM if w >= LONGFORM_WORDS else GATE_DEFAULT
        rows.append(((c == 0) or (wpc > gate), w, c, wpc, sid))
    rows.sort(key=lambda r: (-r[0], -r[1]))  # flagged first, then biggest

    print(f"\nBRAIN: {brain}  (store: {store})")
    print(f"total records: {len(records)} | sources: {len(words)} ({len(trivial)} trivial <{MIN_WORDS}w) | "
          f"source words: {sum(words.values()):,}")
    if records and words:
        print(f"overall density: 1 record / {sum(words.values()) / len(records):.0f} words "
              f"(floor target <= {FLOOR_WORDS_PER_RECORD})")
    edges_path = os.path.join(brain, "edges.jsonl")
    if store == "atoms.jsonl" and os.path.exists(edges_path):
        with open(edges_path, encoding="utf-8") as f:
            edges = [json.loads(l) for l in f if l.strip()]
        ids = {d.get("id") for d in records}
        touched = {e.get(k) for e in edges for k in ("from", "to")} & ids
        print(f"edges: {len(edges)} | connectivity: {100 * len(touched) / max(1, len(ids)):.0f}% of atoms touched")
    print()
    print(f"{'FLAG':<16}{'WORDS':>7}{'RECS':>7}{'W/REC':>9}  SOURCE")
    print("-" * 56)
    flagged = []
    for flag, w, c, wpc, sid in rows:
        tag = ("ZERO-RECORDS" if c == 0 else "UNDER-EXTRACTED") if flag else "ok"
        if tag == "ok" and wpc > FLOOR_WORDS_PER_RECORD:
            tag = "thin"  # passes gate but below aspirational floor
        print(f"{tag:<16}{w:>7}{c:>7}{'inf' if c == 0 else f'{wpc:.0f}':>9}  {sid}")
        if flag:
            flagged.append(sid)

    print()
    if flagged:
        print(f"[FAIL] {len(flagged)} source(s) UNDER-EXTRACTED -- re-mine before finishing:")
        for sid in flagged:
            print(f"   {sid}")
        sys.exit(1)
    if not rows:
        print("[FAIL] no substantive sources found -- nothing was audited.")
        sys.exit(1)
    print("[OK] all sources clear the density gate.")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else ".")
