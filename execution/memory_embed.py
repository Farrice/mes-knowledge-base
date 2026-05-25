#!/usr/bin/env python3
"""
Memory Embed — Generate Gemini embeddings for sovereign memory rows.

Sprint 4: pure-Python vector store (sqlite-vec extension loading is disabled
on this Python build). Embeddings stored as JSON-serialized float arrays in
the `embedding` column. Brute-force cosine similarity at query time
(see memory_retrieve.py).

Model: gemini-embedding-001 (768 dims, $0.15/1M tokens)
Task type: SEMANTIC_SIMILARITY (best for retrieval cascade)

Usage:
    python3 execution/memory_embed.py backfill                # embed all rows missing embeddings
    python3 execution/memory_embed.py backfill --dry-run      # count + cost estimate
    python3 execution/memory_embed.py backfill --batch 20     # smaller batches for slow connections
    python3 execution/memory_embed.py embed <memory_id>       # single row (test)
    python3 execution/memory_embed.py stats                   # coverage report
    python3 execution/memory_embed.py rebuild                 # re-embed ALL rows (after model change)
"""
from __future__ import annotations

import argparse
import json
import sqlite3
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import List, Optional

# Add execution/ to sys.path for imports
sys.path.insert(0, str(Path(__file__).resolve().parent))

from memory_store import DB_PATH, get_db  # noqa: E402

EMBED_MODEL = "gemini-embedding-001"
EMBED_DIM = 768  # gemini-embedding-001 default output dim
COST_PER_1M_TOKENS = 0.15  # USD


def _load_genai():
    """Lazy import google.genai + load env."""
    try:
        from google import genai  # noqa: F401
    except ImportError as e:
        raise SystemExit(f"google.genai not installed: {e}")

    # Load .env into os.environ
    import os
    env_path = Path(__file__).resolve().parent.parent / ".env"
    if env_path.exists():
        for line in env_path.read_text().splitlines():
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                os.environ.setdefault(k.strip(), v.strip())

    if not os.environ.get("GEMINI_API_KEY"):
        raise SystemExit("GEMINI_API_KEY not set in .env or environment")

    from google import genai
    return genai


def embed_text(text: str, task_type: str = "SEMANTIC_SIMILARITY") -> Optional[List[float]]:
    """Generate a Gemini embedding for the given text. Returns None on failure."""
    if not text or not text.strip():
        return None
    genai = _load_genai()
    import os
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    try:
        resp = client.models.embed_content(
            model=EMBED_MODEL,
            contents=text[:8000],  # gemini embed limit ~8K tokens
            config={"task_type": task_type, "output_dimensionality": EMBED_DIM},
        )
        # Response shape: resp.embeddings[0].values
        if hasattr(resp, "embeddings") and resp.embeddings:
            return list(resp.embeddings[0].values)
        return None
    except Exception as e:
        print(f"  embed failed: {e}", file=sys.stderr)
        return None


def embed_batch(texts: List[str], task_type: str = "SEMANTIC_SIMILARITY") -> List[Optional[List[float]]]:
    """Batch-embed multiple texts. Returns list parallel to inputs (None for failures)."""
    if not texts:
        return []
    genai = _load_genai()
    import os
    client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
    out: List[Optional[List[float]]] = []
    # Gemini batch endpoint accepts a list of contents. For safety + retry, embed individually here.
    # (Batch endpoint exists but single-item is more robust for our scale.)
    for t in texts:
        if not t or not t.strip():
            out.append(None)
            continue
        try:
            resp = client.models.embed_content(
                model=EMBED_MODEL,
                contents=t[:8000],
                config={"task_type": task_type, "output_dimensionality": EMBED_DIM},
            )
            if hasattr(resp, "embeddings") and resp.embeddings:
                out.append(list(resp.embeddings[0].values))
            else:
                out.append(None)
        except Exception as e:
            print(f"  embed failed for text[:40]={t[:40]!r}: {e}", file=sys.stderr)
            out.append(None)
    return out


def candidates_for_backfill(rebuild: bool = False) -> List[dict]:
    """Rows that need embeddings. Returns list of dicts."""
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    if rebuild:
        rows = conn.execute(
            "SELECT id, tier, category, content FROM memories ORDER BY freshness DESC"
        ).fetchall()
    else:
        rows = conn.execute(
            "SELECT id, tier, category, content FROM memories WHERE embedding IS NULL ORDER BY freshness DESC"
        ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def estimate_cost(candidates: List[dict]) -> dict:
    """Rough token + cost estimate for the embedding job."""
    total_chars = sum(len(c["content"]) for c in candidates)
    total_tokens = total_chars // 4  # rough rule
    cost_usd = (total_tokens / 1_000_000.0) * COST_PER_1M_TOKENS
    return {
        "rows": len(candidates),
        "total_chars": total_chars,
        "est_tokens": total_tokens,
        "est_cost_usd": round(cost_usd, 4),
    }


def backfill(dry_run: bool = False, batch_size: int = 20, rebuild: bool = False,
             max_rows: Optional[int] = None) -> int:
    """Backfill embeddings. Returns count embedded."""
    candidates = candidates_for_backfill(rebuild=rebuild)
    if max_rows:
        candidates = candidates[:max_rows]

    est = estimate_cost(candidates)
    print(f"Candidates: {est['rows']} rows, ~{est['est_tokens']:,} tokens, ~${est['est_cost_usd']} estimated cost")

    if not candidates:
        print("Nothing to embed.")
        return 0

    if dry_run:
        print("(dry run — no API calls)")
        return 0

    now_iso = datetime.now(timezone.utc).isoformat()
    conn = sqlite3.connect(str(DB_PATH))

    embedded = 0
    failed = 0

    for i in range(0, len(candidates), batch_size):
        batch = candidates[i : i + batch_size]
        texts = [c["content"] for c in batch]
        vectors = embed_batch(texts)
        for c, vec in zip(batch, vectors):
            if vec is None:
                failed += 1
                continue
            conn.execute(
                """UPDATE memories
                   SET embedding = ?, embedding_model = ?, embedded_at = ?
                   WHERE id = ?""",
                (json.dumps(vec), EMBED_MODEL, now_iso, c["id"]),
            )
            embedded += 1
        conn.commit()
        print(f"  batch {i // batch_size + 1}: {embedded}/{len(candidates)} embedded so far")
        # Be polite — slight pause between batches
        if i + batch_size < len(candidates):
            time.sleep(0.5)

    conn.close()
    print(f"\nDone: embedded={embedded}, failed={failed}")
    return embedded


def show_stats() -> None:
    """Report embedding coverage."""
    conn = sqlite3.connect(str(DB_PATH))
    total = conn.execute("SELECT count(*) FROM memories").fetchone()[0]
    with_emb = conn.execute("SELECT count(*) FROM memories WHERE embedding IS NOT NULL").fetchone()[0]
    by_tier = dict(conn.execute(
        "SELECT tier, count(*) FROM memories WHERE embedding IS NOT NULL GROUP BY tier"
    ).fetchall())
    models = dict(conn.execute(
        "SELECT embedding_model, count(*) FROM memories WHERE embedding IS NOT NULL GROUP BY embedding_model"
    ).fetchall())
    conn.close()

    print(f"Embedding coverage:")
    print(f"  Total memories: {total}")
    print(f"  Embedded:       {with_emb} ({100*with_emb/total:.1f}%)" if total else "  Embedded:       0")
    print(f"  Missing:        {total - with_emb}")
    print(f"\nBy tier (embedded):")
    for tier in ["episodic", "semantic", "procedural"]:
        print(f"  {tier:12s}  {by_tier.get(tier, 0)}")
    print(f"\nBy model:")
    for model, count in models.items():
        print(f"  {model}  {count}")


def main() -> int:
    parser = argparse.ArgumentParser(description="Memory Embed — Gemini embeddings for sovereign memory")
    sub = parser.add_subparsers(dest="command")

    bf = sub.add_parser("backfill", help="Embed rows missing embeddings")
    bf.add_argument("--dry-run", action="store_true", help="Count + cost estimate only")
    bf.add_argument("--batch", type=int, default=20, help="Batch size (default 20)")
    bf.add_argument("--rebuild", action="store_true", help="Re-embed ALL rows (overwrite existing)")
    bf.add_argument("--max-rows", type=int, help="Cap rows processed (testing)")

    one = sub.add_parser("embed", help="Embed a single memory by ID")
    one.add_argument("memory_id")

    sub.add_parser("stats", help="Coverage report")

    args = parser.parse_args()

    if args.command == "backfill":
        backfill(dry_run=args.dry_run, batch_size=args.batch,
                 rebuild=args.rebuild, max_rows=args.max_rows)
        return 0
    elif args.command == "embed":
        conn = sqlite3.connect(str(DB_PATH))
        row = conn.execute("SELECT content FROM memories WHERE id = ?", (args.memory_id,)).fetchone()
        if not row:
            print(f"Memory {args.memory_id} not found", file=sys.stderr)
            return 1
        vec = embed_text(row[0])
        if vec is None:
            print(f"Embed failed", file=sys.stderr)
            return 1
        now_iso = datetime.now(timezone.utc).isoformat()
        conn.execute(
            "UPDATE memories SET embedding = ?, embedding_model = ?, embedded_at = ? WHERE id = ?",
            (json.dumps(vec), EMBED_MODEL, now_iso, args.memory_id),
        )
        conn.commit()
        conn.close()
        print(f"Embedded {args.memory_id} (dim={len(vec)})")
        return 0
    elif args.command == "stats":
        show_stats()
        return 0
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
