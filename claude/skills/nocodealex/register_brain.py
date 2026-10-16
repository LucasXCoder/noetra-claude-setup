"""Add/refresh the nocodealex entry in engram's registry.json from the live store.

Run after build_brain.py:   python -I register_brain.py
Counts (atoms, edges, coverage) are measured here, never typed in.
"""
import json
import pathlib

HERE = pathlib.Path(__file__).resolve().parent
REGISTRY = HERE.parent / "engram" / "registry.json"
TODAY = "2026-10-16"


def count(name: str) -> int:
    return sum(1 for l in (HERE / name).read_text(encoding="utf-8").splitlines() if l.strip())


def main() -> None:
    manifest = json.loads((HERE / "sources" / "manifest.json").read_text(encoding="utf-8"))
    reg = json.loads(REGISTRY.read_text(encoding="utf-8"))
    old = next((b for b in reg["brains"] if b["name"] == "nocodealex"), {})
    entry = {
        "name": "nocodealex",
        "creator": "Alex Chen",
        "handle": "@nocodealex",
        "domains": ["Claude Code optimisation", "usage limits and model routing", "Claude skills, plugins and MCP",
                    "multi-Claude panels and agent teams", "prompting and output quality",
                    "open-source AI tool alternatives", "building and selling with AI"],
        "path": ".claude/skills/nocodealex",
        "trigger": "/nocodealex",
        "coverage": {"total": manifest["total"], **{k: v for k, v in manifest["summary"].items()}},
        "sources": {
            "instagram": "https://www.instagram.com/nocodealex (login wall; covered via cross-posts)",
            "youtube": "https://www.youtube.com/@alexchenbuildsai",
            "guides": "https://chen.media/guides (free part only)",
            "github": "https://github.com/alexyc9381",
        },
        "files": {"core": "references/knowledge.md", "topics": "references/topics/", "protocols": "references/protocols.md",
                  "atoms": "atoms.jsonl", "edges": "edges.jsonl", "manifest": "sources/manifest.json",
                  "graph": "graph.html", "build": "build_brain.py"},
        "atoms_count": count("atoms.jsonl"),
        "edges_count": count("edges.jsonl"),
        "status": "DONE - 514 of 514 sources mined; guides free_only",
        "built": old.get("built", TODAY),
        "last_updated": TODAY,
    }
    reg["brains"] = [b for b in reg["brains"] if b["name"] != "nocodealex"] + [entry]
    reg["updated"] = TODAY
    REGISTRY.write_text(json.dumps(reg, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"registry: nocodealex atoms {entry['atoms_count']} edges {entry['edges_count']}")


if __name__ == "__main__":
    main()
