"""Group manifest sources into mining batches → shards/plan.json.

Usage: python -I plan_batches.py <kind> <prefix> <target_words>
Packs sources of one kind (youtube | guide | repo) into batches of ~target_words, in manifest
order, skipping sources already assigned to a batch. Existing batches are never renumbered,
so re-running for a new kind only appends.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent


def main(kind: str, prefix: str, target: int) -> None:
    plan_path = HERE / "shards" / "plan.json"
    plan_path.parent.mkdir(parents=True, exist_ok=True)
    plan = json.loads(plan_path.read_text(encoding="utf-8")) if plan_path.exists() else {"batches": {}}
    taken = {s for b in plan["batches"].values() for s in b["sources"]}
    items = [it for it in json.loads((HERE / "sources" / "manifest.json").read_text(encoding="utf-8"))["items"]
             if it["kind"] == kind and it.get("text_path") and it["words"] >= 20 and it["id"] not in taken]
    n = 1 + sum(1 for k in plan["batches"] if k.startswith(prefix))
    batch, words = [], 0
    for it in items:
        batch.append(it["id"])
        words += it["words"]
        if words >= target:
            plan["batches"][f"{prefix}{n:02d}"] = {"kind": kind, "sources": batch, "words": words}
            n, batch, words = n + 1, [], 0
    if batch:
        plan["batches"][f"{prefix}{n:02d}"] = {"kind": kind, "sources": batch, "words": words}
    plan_path.write_text(json.dumps(plan, indent=1), encoding="utf-8")
    mine = {k: v for k, v in plan["batches"].items() if k.startswith(prefix)}
    print(f"{kind}: {len(mine)} batches, {sum(len(v['sources']) for v in mine.values())} sources, "
          f"{sum(v['words'] for v in mine.values())} words")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[3]))
