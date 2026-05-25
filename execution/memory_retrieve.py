#!/usr/bin/env python3
"""
Memory Retrieve — Chain Step 4 LOAD cascade.

Sprint 4: pure-Python vector retrieval over sovereign memory. Returns the
top-K most relevant memories for a task intent, blending:
  1. Pinned semantic rules (always included, ranked by cosine)
  2. Vector-similarity semantic memories (workspace-filtered)
  3. Vector-similarity procedural memories (workspace-filtered)
  4. BM25 episodic recent decisions (workspace-filtered)

Then dedup, rank by combined (cosine × freshness), and return.

Usage (agents invoke this at Step 4 LOAD per directives/agent-loading-protocol.md):
    python3 execution/memory_retrieve.py "task intent goes here"
    python3 execution/memory_retrieve.py "ghostwriting voice rules" --workspace farrice-brand
    python3 execution/memory_retrieve.py "fal poster cost" --top 5 --json

Library use:
    from memory_retrieve import retrieve_context
    results = retrieve_context("voice rules for Substack", workspace=None, top_k=10)
"""
from __future__ import annotations

import argparse
import json
import math
import sqlite3
import sys
from pathlib import Path
from typing import Dict, List, Optional

# Add execution/ to sys.path
sys.path.insert(0, str(Path(__file__).resolve().parent))

from memory_store import DB_PATH, FRESHNESS_COLD, _detect_workspace, search_memories  # noqa: E402
from memory_embed import embed_text  # noqa: E402


def cosine(a: List[float], b: List[float]) -> float:
    """Cosine similarity between two equal-length vectors."""
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def _load_vec_candidates(tier: str, workspace: Optional[str], min_freshness: float = 0.0) -> List[Dict]:
    """Load all memories of a tier with embeddings, optionally workspace-filtered."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row

    sql = """
        SELECT id, tier, category, content, freshness, pinned, metadata, embedding, workspace
        FROM memories
        WHERE tier = ? AND embedding IS NOT NULL AND freshness >= ?
    """
    params: List = [tier, min_freshness]

    if workspace:
        sql += " AND (workspace = ? OR workspace IS NULL)"
        params.append(workspace)

    rows = conn.execute(sql, params).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def _load_pinned_semantic() -> List[Dict]:
    """Always-included pinned semantic memories (voice rules, banned moves)."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    rows = conn.execute("""
        SELECT id, tier, category, content, freshness, pinned, metadata, embedding, workspace
        FROM memories
        WHERE tier = 'semantic' AND pinned = 1 AND embedding IS NOT NULL
    """).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def _score_vec(qvec: List[float], rows: List[Dict]) -> List[tuple]:
    """Score rows by cosine × freshness. Returns sorted list of (score, row, cosine)."""
    scored = []
    for row in rows:
        try:
            vec = json.loads(row["embedding"])
        except (json.JSONDecodeError, TypeError):
            continue
        cos = cosine(qvec, vec)
        # Combined score: cosine weighted by freshness (active memories favored slightly)
        score = cos * (0.7 + 0.3 * (row["freshness"] / 10.0))
        scored.append((score, row, cos))
    scored.sort(key=lambda x: -x[0])
    return scored


def retrieve_context(query: str, workspace: Optional[str] = None,
                     top_k: int = 10) -> Dict:
    """Main retrieval cascade. Returns structured result."""
    if not query or not query.strip():
        return {"query": query, "results": [], "error": "empty query"}

    if workspace is None:
        workspace = _detect_workspace()

    qvec = embed_text(query)
    if qvec is None:
        return {"query": query, "results": [], "error": "embed failed (rate limit?)"}

    # Tier 1: pinned semantic (always include, ranked by cosine)
    pinned_rows = _load_pinned_semantic()
    pinned_scored = _score_vec(qvec, pinned_rows)
    pinned_top = pinned_scored[: min(5, top_k)]

    # Tier 2: vec-semantic (non-pinned, workspace-filtered)
    sem_rows = [r for r in _load_vec_candidates("semantic", workspace, min_freshness=FRESHNESS_COLD)
                if not r.get("pinned")]
    sem_scored = _score_vec(qvec, sem_rows)
    sem_top = sem_scored[: max(0, top_k - len(pinned_top))]

    # Tier 3: vec-procedural (workspace-filtered)
    proc_rows = _load_vec_candidates("procedural", workspace, min_freshness=FRESHNESS_COLD)
    proc_scored = _score_vec(qvec, proc_rows)
    proc_top = proc_scored[:3]

    # Tier 4: BM25 episodic (recent decisions, workspace-filtered)
    # search_memories already handles freshness floor + BM25 ranking
    ep_results = search_memories(query, top_k=3, tier="episodic")
    # Reshape for consistency
    ep_top = []
    for fts_score, row in ep_results:
        if workspace and row.get("workspace") and row["workspace"] != workspace:
            continue
        # Synthesize a comparable score (cosine 0-1 range)
        cos_proxy = min(1.0, fts_score / 20.0)
        ep_top.append((cos_proxy * 0.5, row, cos_proxy))  # downweight episodic

    # Combine + dedup by id
    all_results = []
    seen = set()
    for label, scored in [
        ("pinned_semantic", pinned_top),
        ("vec_semantic", sem_top),
        ("vec_procedural", proc_top),
        ("bm25_episodic", ep_top),
    ]:
        for score, row, cos in scored:
            if row["id"] in seen:
                continue
            seen.add(row["id"])
            all_results.append({
                "source_tier": label,
                "score": round(score, 4),
                "cosine": round(cos, 4),
                "id": row["id"],
                "tier": row["tier"],
                "category": row["category"],
                "pinned": bool(row.get("pinned")),
                "freshness": round(row["freshness"], 2),
                "workspace": row.get("workspace"),
                "content": row["content"][:300] + ("..." if len(row["content"]) > 300 else ""),
                "metadata": json.loads(row["metadata"]) if row.get("metadata") else {},
            })

    # Final sort by score (pinned items already prioritized by source ordering)
    all_results.sort(key=lambda r: -r["score"])
    final = all_results[:top_k]

    return {
        "query": query,
        "workspace": workspace,
        "model": "gemini-embedding-001",
        "result_count": len(final),
        "results": final,
    }


def format_result(result: Dict) -> str:
    """Pretty-print a retrieval result for CLI use."""
    out = []
    out.append("─" * 70)
    out.append(f"QUERY: {result['query']}")
    if result.get("workspace"):
        out.append(f"WORKSPACE: {result['workspace']}")
    if result.get("error"):
        out.append(f"❌ ERROR: {result['error']}")
        return "\n".join(out)
    out.append(f"RESULTS: {result['result_count']}")
    out.append("─" * 70)
    for i, r in enumerate(result["results"], 1):
        pin = " 📌" if r["pinned"] else ""
        ws = f" [ws={r['workspace']}]" if r.get("workspace") else ""
        out.append(
            f"\n[{i}] score={r['score']} cos={r['cosine']} "
            f"({r['source_tier']}) {r['tier']}/{r['category']}{pin}{ws}"
        )
        out.append(f"    id={r['id']} fresh={r['freshness']}")
        out.append(f"    {r['content']}")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description="Memory Retrieve — Step 4 LOAD cascade")
    parser.add_argument("query", help="Task intent or query text")
    parser.add_argument("--workspace", "-w", help="Workspace filter (auto-detect if omitted)")
    parser.add_argument("--top", "-n", type=int, default=10, help="Top K (default 10)")
    parser.add_argument("--json", action="store_true", help="JSON output for programmatic use")
    args = parser.parse_args()

    result = retrieve_context(args.query, workspace=args.workspace, top_k=args.top)
    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(format_result(result))
    return 0 if not result.get("error") else 1


if __name__ == "__main__":
    sys.exit(main())
