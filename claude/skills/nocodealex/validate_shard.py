"""Validate one mining shard before it is merged:   python -I validate_shard.py <shard-id>

Checks shards/atoms/<id>.jsonl and shards/edges/<id>.jsonl: valid JSON lines, unique ids with
the shard prefix, legal type/topic/confidence, sources present in the manifest, every edge
endpoint resolving (to this shard or to an already-merged atom), connectivity, and density per
assigned source. Prints SHARD OK only when everything passes.
"""
import collections
import json
import pathlib
import sys

sys.stdout.reconfigure(encoding="utf-8")
HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from build_brain import (GATE_DEFAULT, GATE_LONGFORM, LONGFORM_WORDS, VALID_CONF,  # noqa: E402
                         VALID_REL, VALID_TOPICS, VALID_TYPES)


def lines(path: pathlib.Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for n, l in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if l.strip():
            try:
                out.append(json.loads(l))
            except json.JSONDecodeError as e:
                sys.exit(f"FAIL {path.name}:{n} invalid JSON — {e}")
    return out


def main_crosslink(shard: str) -> None:
    """x-* shards add only edges between already-merged atoms, plus confidence overrides."""
    merged = {json.loads(l)["id"] for l in (HERE / "atoms.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()}
    edges = lines(HERE / "shards" / "edges" / f"{shard}.jsonl")
    overrides = lines(HERE / "shards" / "overrides" / f"{shard}.jsonl")
    errs = []
    for e in edges:
        if e.get("rel") not in VALID_REL:
            errs.append(f"edge {e.get('from')}->{e.get('to')}: bad rel {e.get('rel')!r}")
        for end in (e.get("from"), e.get("to")):
            if end not in merged:
                errs.append(f"edge endpoint {end!r} resolves to no merged atom")
        if e.get("from") == e.get("to"):
            errs.append(f"self-loop on {e.get('from')}")
    for o in overrides:
        if o.get("id") not in merged:
            errs.append(f"override for unknown atom {o.get('id')!r}")
        if o.get("confidence") not in VALID_CONF:
            errs.append(f"override {o.get('id')}: bad confidence {o.get('confidence')!r}")
    print(f"crosslink {shard}: {len(edges)} edges, {len(overrides)} confidence overrides")
    if not edges:
        errs.append("no edges written")
    if errs:
        print(f"FAIL {len(errs)} problem(s):")
        for e in errs[:40]:
            print("  " + e)
        sys.exit(1)
    print("SHARD OK")


def main(shard: str) -> None:
    if shard.startswith("x-"):
        return main_crosslink(shard)
    atoms = lines(HERE / "shards" / "atoms" / f"{shard}.jsonl")
    edges = lines(HERE / "shards" / "edges" / f"{shard}.jsonl")
    plan = json.loads((HERE / "shards" / "plan.json").read_text(encoding="utf-8"))
    assigned = plan["batches"][shard]["sources"]
    manifest = {it["id"]: it for it in json.loads((HERE / "sources" / "manifest.json").read_text(encoding="utf-8"))["items"]}
    merged = {json.loads(l)["id"] for l in (HERE / "atoms.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()} \
        if (HERE / "atoms.jsonl").exists() else set()
    errs, ids = [], set()
    for a in atoms:
        aid = a.get("id", "")
        if not aid.startswith(f"{shard}-"):
            errs.append(f"{aid!r}: id must start with '{shard}-'")
        if aid in ids:
            errs.append(f"duplicate id {aid}")
        ids.add(aid)
        for field, legal in (("type", VALID_TYPES), ("topic", VALID_TOPICS), ("confidence", VALID_CONF)):
            if a.get(field) not in legal:
                errs.append(f"{aid}: bad {field} {a.get(field)!r}")
        if not a.get("text"):
            errs.append(f"{aid}: empty text")
        if not a.get("sources"):
            errs.append(f"{aid}: no sources")
        for s in a.get("sources", []):
            if s not in manifest:
                errs.append(f"{aid}: unknown source {s!r}")
    touched = set()
    for e in edges:
        if e.get("rel") not in VALID_REL:
            errs.append(f"edge {e.get('from')}->{e.get('to')}: bad rel {e.get('rel')!r}")
        for end in (e.get("from"), e.get("to")):
            if end not in ids and end not in merged:
                errs.append(f"edge endpoint {end!r} resolves to no atom")
        touched.update((e.get("from"), e.get("to")))
    conn = len(touched & ids) / max(1, len(ids))
    per = collections.Counter(s for a in atoms for s in a.get("sources", []))
    for s in assigned:
        w, c = manifest[s]["words"], per.get(s, 0)
        gate = GATE_LONGFORM if w >= LONGFORM_WORDS else GATE_DEFAULT
        if w >= 20 and (c == 0 or w / c > gate):
            errs.append(f"source {s}: {c} atoms for {w} words (gate 1/{gate})")
    if conn < 0.9:
        errs.append(f"connectivity {conn:.0%} < 90% — link isolated atoms")
    mined_words = sum(manifest[s]["words"] for s in assigned)
    print(f"shard {shard}: {len(atoms)} atoms, {len(edges)} edges, connectivity {conn:.0%}, "
          f"density 1/{mined_words / max(1, len(atoms)):.1f} words over {len(assigned)} sources")
    if errs:
        print(f"FAIL {len(errs)} problem(s):")
        for e in errs[:40]:
            print("  " + e)
        sys.exit(1)
    print("SHARD OK")


if __name__ == "__main__":
    main(sys.argv[1])
