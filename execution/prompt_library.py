#!/usr/bin/env python3
"""prompt_library.py — make the ~1,860 Crown Jewel / practitioner prompts routable assets.

The system holds battle-tested prompts in three populations:
    skills/*/references/prompts/*.md          (crown-jewel prompts per skill)
    skills/*/references/_legacy-prompts/*.md  (archived atomic prompts)
    extractions/*/prompts/*.md                (raw extraction-era prompts)

They were indexed by COUNT in SKILL_INDEX.md but not by CONTENT — you couldn't ask
"which prompt builds a proof ladder?" This registry fixes that deterministically:
one JSON index + a keyword search CLI, $0, no LLM.

Usage:
    python3 execution/prompt_library.py build            # (re)build .agent/prompt-index.json
    python3 execution/prompt_library.py search "<query>" [--top 10]
    python3 execution/prompt_library.py stats
    python3 execution/prompt_library.py orphans          # prompt dirs not mentioned by their SKILL.md
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / ".agent" / "prompt-index.json"

STOP = {"the", "a", "an", "and", "or", "of", "to", "for", "in", "on", "with", "your",
        "you", "this", "that", "prompt", "md"}


def _title_and_gist(path: Path) -> tuple[str, str]:
    """First heading (or filename) + a short gist from the opening lines."""
    try:
        text = path.read_text(errors="ignore")
    except OSError:
        return path.stem, ""
    title = ""
    m = re.search(r"^#\s+(.+)$", text, re.M)
    if m:
        title = m.group(1).strip()
    else:
        fm = re.search(r"^---\n.*?name:\s*\"?([^\"\n]+)\"?.*?\n---", text, re.S)
        if fm:
            title = fm.group(1).strip()
    if not title:
        title = path.stem.replace("-", " ").replace("_", " ")
    # gist: first non-heading, non-frontmatter paragraph line
    body = re.sub(r"^---\n.*?\n---", "", text, flags=re.S)
    gist = ""
    for ln in body.splitlines():
        ln = ln.strip()
        if ln and not ln.startswith(("#", "-", "|", ">", "```", "*")):
            gist = ln[:220]
            break
    return title[:140], gist


def build() -> dict:
    entries = []
    pops = [
        ("skill-prompt", ROOT / "skills", "*/references/prompts/*.md"),
        ("legacy-prompt", ROOT / "skills", "*/references/_legacy-prompts/*.md"),
        ("extraction-prompt", ROOT / "extractions", "*/prompts/*.md"),
    ]
    seen = set()
    for kind, base, pat in pops:
        for p in sorted(base.glob(pat)):
            rel = str(p.relative_to(ROOT))
            if rel in seen:
                continue
            seen.add(rel)
            skill = p.relative_to(base).parts[0]
            title, gist = _title_and_gist(p)
            entries.append({"kind": kind, "skill": skill, "title": title,
                            "gist": gist, "path": rel})
    INDEX.parent.mkdir(parents=True, exist_ok=True)
    data = {"generated_from": "prompt_library.py build", "count": len(entries),
            "entries": entries}
    INDEX.write_text(json.dumps(data, indent=1))
    by_kind = {}
    for e in entries:
        by_kind[e["kind"]] = by_kind.get(e["kind"], 0) + 1
    print(f"prompt index built: {len(entries)} prompts → {INDEX.relative_to(ROOT)}")
    for k, v in sorted(by_kind.items()):
        print(f"  {k:<18} {v}")
    return data


def _load() -> dict:
    if not INDEX.exists():
        return build()
    return json.loads(INDEX.read_text())


def search(query: str, top: int = 10) -> None:
    data = _load()
    q = [t for t in re.sub(r"[^a-z0-9 ]", " ", query.lower()).split() if t not in STOP]
    scored = []
    for e in data["entries"]:
        hay_t = e["title"].lower()
        hay_s = e["skill"].lower()
        hay_g = e["gist"].lower()
        score = sum(3 for t in q if t in hay_t) + sum(2 for t in q if t in hay_s) \
              + sum(1 for t in q if t in hay_g)
        if score:
            scored.append((score, e))
    scored.sort(key=lambda x: -x[0])
    if not scored:
        print(f"no prompts matched: {query}")
        return
    print(f"top {min(top, len(scored))} of {len(scored)} matches for: {query}\n")
    for score, e in scored[:top]:
        print(f"[{score:>2}] {e['title']}")
        print(f"     {e['skill']} · {e['kind']} · {e['path']}")
        if e["gist"]:
            print(f"     {e['gist'][:110]}")
        print()


def stats() -> None:
    data = _load()
    by_skill = {}
    for e in data["entries"]:
        by_skill[e["skill"]] = by_skill.get(e["skill"], 0) + 1
    print(f"prompts indexed: {data['count']} across {len(by_skill)} skills/extractions")
    for s, n in sorted(by_skill.items(), key=lambda kv: -kv[1])[:15]:
        print(f"  {s:<46} {n}")


def orphans() -> None:
    bad = []
    for d in ROOT.glob("skills/*/references/*prompts*"):
        if not d.is_dir():
            continue
        sk = d.relative_to(ROOT / "skills").parts[0]
        skill_md = ROOT / "skills" / sk / "SKILL.md"
        if skill_md.exists() and "prompt" not in skill_md.read_text(errors="ignore").lower():
            bad.append(sk)
    for s in sorted(set(bad)):
        print(f"  ORPHAN: {s} (prompt dir exists; SKILL.md never mentions prompts)")
    print(f"orphan skills: {len(set(bad))}")


def main() -> int:
    ap = argparse.ArgumentParser(description="Prompt-asset registry + search")
    ap.add_argument("command", choices=["build", "search", "stats", "orphans"])
    ap.add_argument("query", nargs="?", default="")
    ap.add_argument("--top", type=int, default=10)
    args = ap.parse_args()
    if args.command == "build":
        build()
    elif args.command == "search":
        if not args.query:
            print("usage: prompt_library.py search \"<query>\""); return 1
        search(args.query, args.top)
    elif args.command == "stats":
        stats()
    elif args.command == "orphans":
        orphans()
    return 0


if __name__ == "__main__":
    sys.exit(main())
