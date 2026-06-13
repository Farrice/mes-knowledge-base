#!/usr/bin/env python3
"""memory_facade.py — one retrieval interface over every memory store.

Audit 2026-04-24 Fix 7 (deferred then; shipped 2026-06-12). The system had
five memory silos, each queried (or not) by a different code path — the
textbook "5 memories, none load at the right moment" failure. This facade
gives The Chain ONE call at Tier 1.5b:

    python3 execution/memory_facade.py "<task intent>" --top 10
    python3 execution/memory_facade.py "<task intent>" --json --sources sovereign,automem

Stores unified (in rank order):
    sovereign   .memory/sovereign.db — vector retrieval via memory_retrieve
                (pinned voice rules first), with a deterministic FTS5/LIKE
                fallback when embeddings are unavailable (no network/key)
    automem     Claude Code user auto-memory (~/.claude/projects/.../memory/)
                — frontmatter descriptions + MEMORY.md index, keyword-scored
    wiki        knowledge/ — via knowledge/compiled/manifest.json (filename/
                domain/expert match); pointers, not full documents
    agents      agents/*/memory/context.md — matched when the query names an
                agent; pointers + first lines

Design rules:
    - Read-only. The facade never writes to any store.
    - Degrade store-by-store: a broken store yields zero results and a note
      in `degraded`, never an exception. (Silent-skip is the banned pattern;
      every skip is REPORTED in the payload.)
    - Existing single-store entry points (memory_retrieve.py etc.) remain
      valid; this wraps, it does not replace.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sqlite3
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

ROOT = Path(__file__).resolve().parents[1]
SOVEREIGN_DB = ROOT / ".memory" / "sovereign.db"
WIKI_MANIFEST = ROOT / "knowledge" / "compiled" / "manifest.json"
AGENTS_DIR = ROOT / "agents"
AUTOMEM_DIR = Path(os.environ.get(
    "ANTIGRAVITY_AUTOMEM_DIR",
    str(Path.home() / ".claude" / "projects" / "-Users-farricecain-Google-Antigravity" / "memory"),
))

ALL_SOURCES = ("sovereign", "automem", "wiki", "agents")

_STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "how",
    "in", "is", "it", "of", "on", "or", "that", "the", "this", "to", "what",
    "when", "with", "i", "my", "we", "our", "you", "your", "do", "does",
}


def _tokens(text: str) -> List[str]:
    return [t for t in re.findall(r"[a-z0-9]+", (text or "").lower())
            if len(t) > 2 and t not in _STOPWORDS]


def _overlap_score(query_tokens: List[str], text: str) -> float:
    """Fraction of query tokens present in text (0..1). Cheap, deterministic."""
    if not query_tokens:
        return 0.0
    hay = set(_tokens(text))
    hits = sum(1 for t in query_tokens if t in hay)
    return round(hits / len(query_tokens), 3)


# ──────────────────────────────────────────────────────────────────
# sovereign — vector path with deterministic FTS5 fallback
# ──────────────────────────────────────────────────────────────────
def _query_sovereign(query: str, workspace: Optional[str], top_k: int) -> Dict[str, Any]:
    # Primary: the existing vector retrieval (pinned rules + cosine ranking).
    try:
        sys.path.insert(0, str(ROOT / "execution"))
        from memory_retrieve import retrieve_context
        ctx = retrieve_context(query, workspace=workspace, top_k=top_k)
        results = [{
            "source": "sovereign",
            "via": r.get("source_tier", "vector"),
            "score": float(r.get("score", 0.0)),
            "id": r.get("id", ""),
            "pinned": bool(r.get("pinned")),
            "snippet": (r.get("content") or "")[:300],
            "path": str(SOVEREIGN_DB),
        } for r in ctx.get("results", [])]
        if results:
            return {"results": results, "degraded": None}
    # memory_embed raises SystemExit (not Exception) on a missing API key —
    # catch both so a keyless environment degrades to FTS instead of dying.
    except (Exception, SystemExit) as exc:
        vec_error = str(exc)[:120]
    else:
        vec_error = "vector path returned 0 results"

    # Fallback: FTS5 (then LIKE) directly against sovereign.db — no network.
    try:
        q_tokens = _tokens(query)
        if not SOVEREIGN_DB.exists() or not q_tokens:
            return {"results": [], "degraded": f"sovereign: {vec_error}; no db/tokens for fallback"}
        con = sqlite3.connect(f"file:{SOVEREIGN_DB}?mode=ro", uri=True)
        rows: List[tuple] = []
        try:
            match = " OR ".join(q_tokens[:8])
            rows = con.execute(
                "SELECT m.id, m.content, m.pinned, m.freshness FROM memories_fts f "
                "JOIN memories m ON m.rowid = f.rowid WHERE memories_fts MATCH ? LIMIT ?",
                (match, top_k * 2),
            ).fetchall()
        except sqlite3.Error:
            like = f"%{q_tokens[0]}%"
            rows = con.execute(
                "SELECT id, content, pinned, freshness FROM memories "
                "WHERE content LIKE ? ORDER BY freshness DESC LIMIT ?",
                (like, top_k * 2),
            ).fetchall()
        finally:
            con.close()
        results = []
        for rid, content, pinned, freshness in rows:
            results.append({
                "source": "sovereign",
                "via": "fts_fallback",
                "score": _overlap_score(q_tokens, content) * (1.2 if pinned else 1.0),
                "id": rid,
                "pinned": bool(pinned),
                "snippet": (content or "")[:300],
                "path": str(SOVEREIGN_DB),
            })
        results.sort(key=lambda r: r["score"], reverse=True)
        return {"results": results[:top_k],
                "degraded": f"sovereign vector path unavailable ({vec_error}); used FTS fallback"}
    except Exception as exc:
        return {"results": [], "degraded": f"sovereign: {str(exc)[:120]}"}


# ──────────────────────────────────────────────────────────────────
# automem — Claude Code user auto-memory (frontmatter descriptions)
# ──────────────────────────────────────────────────────────────────
def _query_automem(query: str, top_k: int) -> Dict[str, Any]:
    try:
        if not AUTOMEM_DIR.is_dir():
            return {"results": [], "degraded": f"automem dir missing: {AUTOMEM_DIR}"}
        q_tokens = _tokens(query)
        results = []
        for f in AUTOMEM_DIR.glob("*.md"):
            if f.name == "MEMORY.md":
                continue
            try:
                head = f.read_text(errors="ignore")[:1200]
            except OSError:
                continue
            desc = ""
            m = re.search(r"^description:\s*(.+)$", head, re.MULTILINE)
            if m:
                desc = m.group(1).strip()
            score = _overlap_score(q_tokens, f.stem.replace("-", " ").replace("_", " ") + " " + desc + " " + head)
            if score > 0:
                results.append({
                    "source": "automem",
                    "via": "frontmatter",
                    "score": score,
                    "id": f.stem,
                    "pinned": False,
                    "snippet": desc[:300] if desc else head.split("---")[-1].strip()[:300],
                    "path": str(f),
                })
        results.sort(key=lambda r: r["score"], reverse=True)
        return {"results": results[:top_k], "degraded": None}
    except Exception as exc:
        return {"results": [], "degraded": f"automem: {str(exc)[:120]}"}


# ──────────────────────────────────────────────────────────────────
# wiki — knowledge/ manifest pointers
# ──────────────────────────────────────────────────────────────────
def _query_wiki(query: str, top_k: int) -> Dict[str, Any]:
    try:
        if not WIKI_MANIFEST.exists():
            return {"results": [], "degraded": "wiki manifest missing — run knowledge_compiler.py inventory"}
        manifest = json.loads(WIKI_MANIFEST.read_text())
        q_tokens = _tokens(query)
        results = []
        for entry in manifest.get("files", []):
            path = entry.get("path", "")
            hay = " ".join([
                Path(path).stem.replace("-", " ").replace("_", " "),
                str(entry.get("domain") or ""), str(entry.get("expert") or ""),
                str(entry.get("title") or ""),
            ])
            score = _overlap_score(q_tokens, hay)
            if score > 0:
                results.append({
                    "source": "wiki",
                    "via": "manifest",
                    "score": score,
                    "id": Path(path).stem,
                    "pinned": False,
                    "snippet": f"[{entry.get('domain', '?')} / {entry.get('expert', '?')}] "
                               f"{entry.get('words', '?')} words",
                    "path": path,
                })
        results.sort(key=lambda r: r["score"], reverse=True)
        return {"results": results[:top_k], "degraded": None}
    except Exception as exc:
        return {"results": [], "degraded": f"wiki: {str(exc)[:120]}"}


# ──────────────────────────────────────────────────────────────────
# agents — per-agent memory/context.md, matched when query names the agent
# ──────────────────────────────────────────────────────────────────
def _query_agents(query: str, top_k: int) -> Dict[str, Any]:
    try:
        if not AGENTS_DIR.is_dir():
            return {"results": [], "degraded": "agents dir missing"}
        q_tokens = set(_tokens(query))
        results = []
        for ctx_file in AGENTS_DIR.glob("*/memory/context.md"):
            agent = ctx_file.parts[-3]
            name_tokens = set(_tokens(agent.replace("-", " ")))
            if not (name_tokens & q_tokens):
                continue
            try:
                head = ctx_file.read_text(errors="ignore")[:400]
            except OSError:
                continue
            results.append({
                "source": "agents",
                "via": "name_match",
                "score": round(len(name_tokens & q_tokens) / max(len(name_tokens), 1), 3),
                "id": agent,
                "pinned": False,
                "snippet": head.strip()[:300],
                "path": str(ctx_file),
            })
        results.sort(key=lambda r: r["score"], reverse=True)
        return {"results": results[:top_k], "degraded": None}
    except Exception as exc:
        return {"results": [], "degraded": f"agents: {str(exc)[:120]}"}


# ──────────────────────────────────────────────────────────────────
# facade
# ──────────────────────────────────────────────────────────────────
def recall(
    query: str,
    top_k: int = 10,
    workspace: Optional[str] = None,
    sources: Optional[List[str]] = None,
) -> Dict[str, Any]:
    """Unified recall across all memory stores.

    Returns {query, results, degraded, by_source}. Ordering: sovereign
    pinned rules first (voice rules / banned moves must always surface),
    then everything else by score. Dedup by (source, id).
    """
    use = [s for s in (sources or ALL_SOURCES) if s in ALL_SOURCES]
    per_store = max(3, top_k)
    merged: List[Dict[str, Any]] = []
    degraded: List[str] = []
    by_source: Dict[str, int] = {}

    for name, fn in (
        ("sovereign", lambda: _query_sovereign(query, workspace, per_store)),
        ("automem", lambda: _query_automem(query, per_store)),
        ("wiki", lambda: _query_wiki(query, per_store)),
        ("agents", lambda: _query_agents(query, per_store)),
    ):
        if name not in use:
            continue
        out = fn()
        if out.get("degraded"):
            degraded.append(out["degraded"])
        by_source[name] = len(out.get("results", []))
        merged.extend(out.get("results", []))

    seen = set()
    deduped = []
    for r in merged:
        key = (r["source"], r["id"])
        if key in seen:
            continue
        seen.add(key)
        deduped.append(r)

    pinned = [r for r in deduped if r.get("pinned")]
    rest = sorted([r for r in deduped if not r.get("pinned")],
                  key=lambda r: r["score"], reverse=True)
    final = (pinned + rest)[:top_k]

    return {
        "query": query,
        "workspace": workspace,
        "result_count": len(final),
        "results": final,
        "by_source": by_source,
        "degraded": degraded or None,
    }


def _print_human(payload: Dict[str, Any]) -> None:
    print(f"\n{'=' * 64}")
    print(f"  MEMORY FACADE — {payload['result_count']} results for: {payload['query'][:60]}")
    print(f"  sources: {payload['by_source']}")
    if payload.get("degraded"):
        for d in payload["degraded"]:
            print(f"  ⚠ degraded: {d}")
    print(f"{'=' * 64}")
    for r in payload["results"]:
        pin = " [PINNED]" if r.get("pinned") else ""
        print(f"\n  [{r['source']}/{r['via']}] {r['id']}{pin}  (score {r['score']})")
        print(f"    {r['snippet'][:200]}")
        print(f"    -> {r['path']}")
    print()


def main() -> int:
    ap = argparse.ArgumentParser(description="Unified memory recall (audit Fix 7)")
    ap.add_argument("query", help="Task intent / search query")
    ap.add_argument("--top", type=int, default=10, help="Max results (default 10)")
    ap.add_argument("--workspace", default=None, help="Sovereign workspace filter")
    ap.add_argument("--sources", default=None,
                    help=f"Comma-separated subset of {','.join(ALL_SOURCES)} (default: all)")
    ap.add_argument("--json", action="store_true", help="JSON output")
    args = ap.parse_args()

    sources = args.sources.split(",") if args.sources else None
    payload = recall(args.query, top_k=args.top, workspace=args.workspace, sources=sources)
    if args.json:
        print(json.dumps(payload, indent=2))
    else:
        _print_human(payload)
    return 0


if __name__ == "__main__":
    sys.exit(main())
