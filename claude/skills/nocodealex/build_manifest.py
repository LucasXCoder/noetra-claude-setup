"""Build sources/manifest.json — every nocodealex source, its coverage, and its text file.

Run after any fetch:  python -I build_manifest.py
Sources: YouTube (sources/yt_meta.jsonl + transcripts/), chen.media guides
(sources/guides_index.jsonl + guides/), GitHub skill repos (sources/repos/*), and the
Instagram record (sources/instagram/status.json). Repo prose (.md) is flattened into
sources/repo_text/r-{name}.txt so every source kind is gated the same way.
"""
import json
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
SRC = HERE / "sources"
FETCHED = "2026-10-16"


def jsonl(path: pathlib.Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def words(path: pathlib.Path) -> int:
    return len(path.read_text(encoding="utf-8", errors="ignore").split()) if path.exists() else 0


def youtube() -> list[dict]:
    items = []
    for m in jsonl(SRC / "yt_meta.jsonl"):
        vid = m["id"]
        t = SRC / "transcripts" / f"{vid}.txt"
        items.append({
            "id": vid, "kind": "youtube", "title": m.get("title") or m.get("flat_title", ""),
            "url": f"https://youtu.be/{vid}", "date": m.get("upload_date", ""),
            "duration": m.get("duration"), "views": m.get("view_count"),
            "coverage": "transcript" if t.exists() else ("description_only" if m.get("description") else "missed"),
            "words": words(t), "text_path": f"sources/transcripts/{vid}.txt" if t.exists() else None,
            "description": (m.get("description") or "")[:2000], "fetched": FETCHED,
        })
    return items


GATE_BLOCK = re.compile(r"\nKeep reading\s*\n.*?(?:Unsubscribe in one click\.|$)", re.S)
BOILERPLATE = [
    re.compile(r"Alex Chen\s*@nocodealex\s*·\s*[\d,]+\+?\s*follow on Instagram"),
    re.compile(r"^\d+\s*min read\s*$", re.M), re.compile(r"^\d+\s*sections\s*$", re.M),
    re.compile(r"^In this guide · \d+ sections▾\s*$", re.M), re.compile(r"^Contents · \d+ sections\s*$", re.M),
    re.compile(r"^\d{2}\s*$", re.M), re.compile(r"\(locked\)"),
]


def clean_guide(raw: str) -> str:
    """Drop the site chrome (byline, read-time, email gate, TOC counters) so word counts are honest."""
    # Drop the fetcher's own header ("# title" + url/section/date/locked lines); the page
    # repeats the title as its own H1 below.
    body = re.sub(r"\A# .*?\n\nurl: .*?\nlocked: \w+\n\n", "", raw, flags=re.S)
    body = GATE_BLOCK.sub("\n", body)
    for rx in BOILERPLATE:
        body = rx.sub("", body)
    return re.sub(r"\n\s*\n\s*\n+", "\n\n", body).strip() + "\n"


def guides() -> list[dict]:
    out_dir = SRC / "guide_text"
    out_dir.mkdir(exist_ok=True)
    items = []
    for g in jsonl(SRC / "guides_index.jsonl"):
        p = SRC / "guides" / f"{g['id']}.md"
        raw = p.read_text(encoding="utf-8") if p.exists() else ""
        locked = "(locked)" in raw or "Free, for an email" in raw
        cov = "missed" if g.get("error") or not raw else ("free_only" if locked else "full_text")
        target = out_dir / f"{g['id']}.txt"
        if raw:
            target.write_text(clean_guide(raw), encoding="utf-8")
        items.append({
            "id": g["id"], "kind": "guide", "title": g.get("title", g["id"]), "url": g["url"],
            "date": g.get("date", ""), "section": g.get("section", ""), "coverage": cov,
            "locked_sections": raw.count("(locked)"), "words": words(target),
            "text_path": f"sources/guide_text/{g['id']}.txt" if raw else None,
            "raw_path": f"sources/guides/{g['id']}.md" if raw else None, "fetched": FETCHED,
        })
    return items


def repos() -> list[dict]:
    out_dir = SRC / "repo_text"
    out_dir.mkdir(exist_ok=True)
    items = []
    for repo in sorted(p for p in (SRC / "repos").iterdir() if p.is_dir()):
        prose = []
        for f in sorted(repo.rglob("*.md")):
            if ".git" in f.parts:
                continue
            prose.append(f"\n\n===== {f.relative_to(repo).as_posix()} =====\n\n" + f.read_text(encoding="utf-8", errors="ignore"))
        rid = f"r-{repo.name}"
        target = out_dir / f"{rid}.txt"
        target.write_text("".join(prose).strip() + "\n", encoding="utf-8")
        items.append({
            "id": rid, "kind": "repo", "title": repo.name, "url": f"https://github.com/alexyc9381/{repo.name}",
            "coverage": "full_text", "words": words(target), "text_path": f"sources/repo_text/{rid}.txt",
            "fetched": FETCHED,
        })
    return items


def main() -> None:
    ig = json.loads((SRC / "instagram" / "status.json").read_text(encoding="utf-8")) if (SRC / "instagram" / "status.json").exists() else {}
    items = youtube() + guides() + repos()
    summary = {}
    for it in items:
        summary.setdefault(it["kind"], {}).setdefault(it["coverage"], 0)
        summary[it["kind"]][it["coverage"]] += 1
    methods = {m["id"]: m["method"] for m in jsonl(SRC / "transcripts_method.jsonl")}
    for it in items:
        if it["kind"] == "youtube" and it["coverage"] == "transcript":
            it["transcript_method"] = methods.get(it["id"], "youtube captions")
    no_speech_path = SRC / "no_speech.json"
    no_speech = json.loads(no_speech_path.read_text(encoding="utf-8")) if no_speech_path.exists() else []
    manifest = {
        "creator": "Alex Chen (@nocodealex)", "fetched": FETCHED, "no_speech": no_speech,
        "channels": {
            "instagram": "https://www.instagram.com/nocodealex", "youtube": "https://www.youtube.com/@alexchenbuildsai",
            "guides": "https://chen.media/guides", "github": "https://github.com/alexyc9381",
        },
        "instagram": ig, "summary": summary, "total": len(items), "items": items,
    }
    (SRC / "manifest.json").write_text(json.dumps(manifest, ensure_ascii=False, indent=1), encoding="utf-8")
    print(json.dumps(summary), f"total={len(items)}")


if __name__ == "__main__":
    main()
