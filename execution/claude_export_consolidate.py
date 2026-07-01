#!/usr/bin/env python3
"""claude_export_consolidate.py — collapse the 112 exported Project prompts into unique systems.

The export holds heavy duplication: exact dupes, and long version-families ("Enhanced
Collaborative Prompt Engineering v1..v18", "MES 3.0" ×8, "KACE" ×5). Building a skill per
project would flood the system with junk. This stage collapses them FIRST, deterministically
(no LLM, $0), so the downstream routing workflow only judges unique survivors.

Three dedup signals, merged by union-find (anything transitively connected collapses):
    1. exact content hash of the custom-instructions section (identical dupes)
    2. name-family Jaccard on version-stripped name tokens (the version drift chains)
    3. content Jaccard on instruction word-sets (near-identical under different names)

The largest-instruction variant becomes the canonical (most-evolved) representative.

Usage:
    python3 execution/claude_export_consolidate.py hash      # exact-dup report
    python3 execution/claude_export_consolidate.py cluster   # → canonical-systems.json
    python3 execution/claude_export_consolidate.py plan      # → consolidation-plan.md (ranked)
    python3 execution/claude_export_consolidate.py all       # hash + cluster + plan
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Tuple

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import claude_export_state as st  # noqa: E402
from memory_store import _jaccard  # noqa: E402  (reuse the proven text-overlap primitive)

CANON_PATH = st.EXPORT_DIR / "canonical-systems.json"
PLAN_PATH = st.REPORTS_DIR / "consolidation-plan.md"

# ── thresholds (tuning surface) ──
NAME_JACCARD = 0.60       # version-family grouping
CONTENT_JACCARD = 0.70    # near-duplicate instruction bodies

# tokens stripped from names before family comparison (versioning / filler noise)
_NAME_NOISE = re.compile(
    r"\b(v\d+|\d+(\.\d+)?|version|final|enhanced|complete|comprehensive|fully|new|ultimate|"
    r"advanced|supreme|system|systems|instructions?|custom|claude|openai|o1|gpt|sonnet|poe|ai|"
    r"test|testing|trial|for|the|of|and|with|hub|assistant|v)\b", re.I)

# theme → keyword markers (first match wins, order matters)
THEMES: List[Tuple[str, List[str]]] = [
    ("test-experiment", ["test", "testing", "trial", "experiment", "scratch", "draft"]),
    ("extraction-mes", ["mes", "mastery extraction", "expert replication", "skill download", "extract"]),
    ("knowledge-arch", ["kace", "ohkif", "knowledge architecture", "knowledge acquisition"]),
    ("context-architect", ["context profile", "context architect"]),
    ("prompt-engineering", ["prompt engineer", "collaborative prompt", "expert panel", "meta-prompt",
                            "prompt intelligence", "pier", "enhanced instructions", "deep reasoning"]),
    ("coaching", ["coach", "prosperity", "transformation"]),
    ("copywriting", ["copywriting", "copywriter", "copy ", "marketing maestro", "clemens"]),
    ("ghostwriting-content", ["ghostwriter", "ghostwriting", "linkedin", "content", "brand"]),
    ("business-offer", ["business plan", "offer", "revenue", "$", "funnel", "sales", "maria", "dwa"]),
    ("assistant-jarvis", ["jarvis", "executive ai", "assistant", "omniflow"]),
]


def _load_projects() -> List[Dict[str, Any]]:
    idx = json.loads(st.INDEX_PATH.read_text())
    return [p for p in idx["projects"] if p.get("has_instructions")]


def _instructions_of(md_path: str) -> str:
    """Extract the '## Custom Instructions' body from a project md (defensive)."""
    p = ROOT / md_path
    if not p.exists():
        return ""
    text = p.read_text()
    m = re.search(r"## Custom Instructions\s*\n(.*?)(?:\n## |\Z)", text, re.S)
    return (m.group(1).strip() if m else text).strip()


def _name_tokens(name: str) -> set:
    cleaned = _NAME_NOISE.sub(" ", name.lower())
    cleaned = re.sub(r"[^a-z0-9 ]+", " ", cleaned)
    return {t for t in cleaned.split() if len(t) > 2}


def _theme(name: str, body: str) -> str:
    hay = (name + " " + body[:400]).lower()
    for theme, markers in THEMES:
        if any(m in hay for m in markers):
            return theme
    return "misc"


def _load_all() -> List[Dict[str, Any]]:
    """Enrich each project with instructions body, hash, name tokens, theme."""
    out = []
    for p in _load_projects():
        body = _instructions_of(p["md_path"])
        out.append({
            "id": p["id"], "name": p["name"], "chars": p.get("instruction_chars", len(body)),
            "md_path": p["md_path"], "body": body,
            "hash": hashlib.md5(body.encode("utf-8")).hexdigest(),
            "tokens": _name_tokens(p["name"]),
            "words": set(body.lower().split()),
        })
    return out


# ── union-find ──
class _UF:
    def __init__(self, n): self.p = list(range(n))
    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]; x = self.p[x]
        return x
    def union(self, a, b): self.p[self.find(a)] = self.find(b)


def _cluster(items: List[Dict[str, Any]]) -> List[List[int]]:
    n = len(items)
    uf = _UF(n)
    # signal 1: exact content hash
    by_hash: Dict[str, int] = {}
    for i, it in enumerate(items):
        if it["body"]:
            if it["hash"] in by_hash:
                uf.union(i, by_hash[it["hash"]])
            else:
                by_hash[it["hash"]] = i
    # signals 2 & 3: name-family + content jaccard (O(n^2), n≈112 — trivial)
    for i in range(n):
        for j in range(i + 1, n):
            if uf.find(i) == uf.find(j):
                continue
            ti, tj = items[i]["tokens"], items[j]["tokens"]
            if ti and tj:
                nj = len(ti & tj) / len(ti | tj)
                if nj >= NAME_JACCARD:
                    uf.union(i, j); continue
            if items[i]["body"] and items[j]["body"]:
                if _jaccard(items[i]["body"], items[j]["body"]) >= CONTENT_JACCARD:
                    uf.union(i, j)
    groups: Dict[int, List[int]] = {}
    for i in range(n):
        groups.setdefault(uf.find(i), []).append(i)
    return list(groups.values())


def cluster() -> Dict[str, Any]:
    items = _load_all()
    groups = _cluster(items)
    systems = []
    for g in groups:
        members = [items[i] for i in g]
        best = max(members, key=lambda m: m["chars"])
        exact = len({m["hash"] for m in members if m["body"]}) < len([m for m in members if m["body"]])
        systems.append({
            "canonical_id": best["id"], "name": best["name"], "chars": best["chars"],
            "md_path": best["md_path"], "theme": _theme(best["name"], best["body"]),
            "variant_count": len(members), "has_exact_dupes": exact,
            "variants": [{"id": m["id"], "name": m["name"], "chars": m["chars"]}
                         for m in sorted(members, key=lambda m: -m["chars"])],
        })
    systems.sort(key=lambda s: -s["chars"])
    out = {"generated_at": st._now(), "total_projects": len(items),
           "unique_systems": len(systems), "systems": systems}
    st.EXPORT_DIR.mkdir(parents=True, exist_ok=True)
    CANON_PATH.write_text(json.dumps(out, indent=2))
    print(f"─── CLUSTER ───\n  {len(items)} projects → {len(systems)} unique systems")
    from collections import Counter
    for theme, c in Counter(s["theme"] for s in systems).most_common():
        print(f"    {theme:<20} {c}")
    print(f"  → {CANON_PATH.relative_to(ROOT)}\n  next: consolidate.py plan")
    return out


def hash_report() -> None:
    items = _load_all()
    by_hash: Dict[str, List[Dict]] = {}
    for it in items:
        if it["body"]:
            by_hash.setdefault(it["hash"], []).append(it)
    dupes = {h: v for h, v in by_hash.items() if len(v) > 1}
    print(f"─── EXACT-DUP REPORT ───\n  {len(dupes)} exact-duplicate clusters "
          f"({sum(len(v) for v in dupes.values())} projects, "
          f"{sum(len(v) - 1 for v in dupes.values())} droppable)")
    for h, v in sorted(dupes.items(), key=lambda kv: -kv[1][0]["chars"]):
        print(f"    [{v[0]['chars']} chars] " + "  ·  ".join(m["name"][:32] for m in v))


# heuristic proposed route (the B1 workflow refines against existing skills)
def _proposed_route(sys_: Dict[str, Any]) -> str:
    t = sys_["theme"]
    if t == "test-experiment":
        return "SKIP (experiment/test)"
    if t in ("prompt-engineering", "extraction-mes"):
        return "COLLAPSE→flagship (biggest of family; fold rest into existing extraction skills)"
    return "BUILD-NEW? (route vs existing skills in B1)"


def plan() -> int:
    if not CANON_PATH.exists():
        cluster()
    data = json.loads(CANON_PATH.read_text())
    systems = data["systems"]
    from collections import defaultdict
    by_theme: Dict[str, List[Dict]] = defaultdict(list)
    for s in systems:
        by_theme[s["theme"]].append(s)

    lines = ["# Claude Export — Consolidation Plan", "",
             f"_generated {data['generated_at']}_", "",
             f"**{data['total_projects']} project prompts → {data['unique_systems']} unique systems.** "
             "Proposed routes are heuristic; the routing workflow (B1) refines each against the "
             "existing ~260 skills (SKIP / MERGE→skill / BUILD-NEW / COLLAPSE→flagship).", ""]
    # theme order: value-first
    order = ["context-architect", "extraction-mes", "knowledge-arch", "prompt-engineering",
             "copywriting", "coaching", "ghostwriting-content", "business-offer",
             "assistant-jarvis", "misc", "test-experiment"]
    for theme in order + [t for t in by_theme if t not in order]:
        rows = by_theme.get(theme)
        if not rows:
            continue
        lines += [f"## {theme}  ({len(rows)} systems)", "",
                  "| # | System (canonical) | chars | variants | proposed route | md_path |",
                  "|---|--------------------|-------|----------|----------------|---------|"]
        for i, s in enumerate(rows, 1):
            lines.append(f"| {i} | {s['name'][:48]} | {s['chars']} | {s['variant_count']} | "
                         f"{_proposed_route(s)} | `{s['md_path']}` |")
        lines.append("")
    st.REPORTS_DIR.mkdir(parents=True, exist_ok=True)
    PLAN_PATH.write_text("\n".join(lines) + "\n")
    print(f"─── PLAN ───\n  → {PLAN_PATH.relative_to(ROOT)}  ({data['unique_systems']} systems)")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="Consolidate exported project prompts into unique systems")
    ap.add_argument("command", choices=["hash", "cluster", "plan", "all"])
    args = ap.parse_args()
    if args.command in ("hash", "all"):
        hash_report()
    if args.command in ("cluster", "all"):
        cluster()
    if args.command in ("plan", "all"):
        plan()
    return 0


if __name__ == "__main__":
    sys.exit(main())
