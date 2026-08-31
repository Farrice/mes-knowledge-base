#!/usr/bin/env python3
"""
Memory Distill — Weekly clustering + Gemini-as-judge proposal pipeline.

Sprint 6 (2026-05-25): cluster recent episodic decisions by cosine similarity,
ask Gemini to propose a semantic rule per cluster, judge it with a second
Gemini call, and insert into `flagged_review` if judge_score >= threshold.

Never auto-promotes. Human-in-loop via `memory_review.py`.

Usage:
    python3 execution/memory_distill.py --dry-run            # preview clusters + proposals
    python3 execution/memory_distill.py run                  # commit to flagged_review
    python3 execution/memory_distill.py run --week current   # default
    python3 execution/memory_distill.py run --days 14        # custom window
    python3 execution/memory_distill.py run --min-cluster 3  # default
    python3 execution/memory_distill.py run --judge-threshold 7.0  # default

Scheduled via ~/Library/LaunchAgents/com.antigravity.distill-weekly.plist (Sun 04:00).
"""
from __future__ import annotations

import argparse
import asyncio
import hashlib
import json
import math
import os
import sqlite3
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))

from memory_store import DB_PATH  # noqa: E402

JUDGE_MODEL = "lite"  # gemini-3.1-flash-lite-preview per gemini_client MODEL_TIERS

# Defaults
DEFAULT_DAYS = 7
DEFAULT_MIN_CLUSTER = 3
DEFAULT_JUDGE_THRESHOLD = 7.0
DEFAULT_COSINE_THRESHOLD = 0.45  # CENTERED-cosine scale (2026-08-21): vectors are
# mean-centered before clustering, which drops the median pairwise sim from
# ~0.80 (raw, anisotropic) to ~-0.03; 0.45 ≈ p99 of the centered distribution,
# so only genuinely topical pairs cluster. The old raw-scale 0.72 sat BELOW
# the raw p10 and collapsed everything into one cluster.


# ─────────────────────────────────────────────────────────
# CLUSTERING
# ─────────────────────────────────────────────────────────

def cosine(a: List[float], b: List[float]) -> float:
    if not a or not b or len(a) != len(b):
        return 0.0
    dot = sum(x * y for x, y in zip(a, b))
    na = math.sqrt(sum(x * x for x in a))
    nb = math.sqrt(sum(y * y for y in b))
    if na == 0 or nb == 0:
        return 0.0
    return dot / (na * nb)


def load_recent_episodic(days: int, include_export: bool = False) -> List[Dict]:
    """Pull recent episodic decisions with embeddings.

    By default the large `claude-export` corpus (thousands of imported claude.ai
    conversations) is EXCLUDED so the unattended weekly cron never floods the O(n^2)
    clustering / human-review queue with it. Distill that corpus deliberately, in small
    batches, via `--include-export` (or ANTIGRAVITY_DISTILL_INCLUDE_EXPORT=1)."""
    cutoff = (datetime.now(timezone.utc) - timedelta(days=days)).isoformat()
    if os.environ.get("ANTIGRAVITY_DISTILL_INCLUDE_EXPORT") == "1":
        include_export = True
    conn = sqlite3.connect(str(DB_PATH))
    conn.row_factory = sqlite3.Row
    where_export = "" if include_export else \
        "AND (workspace IS NULL OR workspace != 'claude-export')"
    rows = conn.execute(f"""
        SELECT id, category, content, embedding, metadata, created_at, workspace
        FROM memories
        WHERE tier = 'episodic'
          AND created_at >= ?
          AND embedding IS NOT NULL
          {where_export}
        ORDER BY created_at ASC
    """, (cutoff,)).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def cluster_by_cosine(rows: List[Dict], threshold: float = DEFAULT_COSINE_THRESHOLD,
                     min_cluster: int = DEFAULT_MIN_CLUSTER) -> List[List[Dict]]:
    """Mean-centered centroid (leader) clustering by cosine similarity.

    Rebuilt 2026-08-21 — two compounding failures in the original:
    (1) single-linkage connected-components CHAINS (A~B, B~C merges A with C);
    (2) raw Gemini embeddings are anisotropic — measured on the live corpus,
    the MEDIAN pairwise cosine was 0.801 (p10 = 0.764), so the 0.72 threshold
    matched virtually every pair and 348 rows collapsed into ONE cluster →
    one generic rule per weekly run, the reason the semantic tier crawled
    even when the cron was green.

    Fix: subtract the corpus mean from every vector first. Centering spreads
    the band (measured after: median −0.035, p95 0.304, p99 0.458), so only
    genuinely related pairs stay high. Then leader clustering against running
    cluster CENTROIDS (no chaining — membership is judged against the
    cluster's mean, never its nearest edge). `threshold` is on the CENTERED
    cosine scale (see DEFAULT_COSINE_THRESHOLD). Returns clusters with
    >= min_cluster members, largest first.
    """
    if not rows:
        return []
    # Parse embeddings once
    parsed: List[Tuple[Dict, List[float]]] = []
    for r in rows:
        try:
            vec = json.loads(r["embedding"])
            parsed.append((r, vec))
        except (json.JSONDecodeError, TypeError):
            continue
    if not parsed:
        return []

    dim = len(parsed[0][1])
    n = len(parsed)
    mean = [sum(v[d] for _, v in parsed) / n for d in range(dim)]
    centered: List[Tuple[Dict, List[float]]] = [
        (row, [v[d] - mean[d] for d in range(dim)]) for row, v in parsed
    ]

    # clusters: list of [member_rows, member_vecs, centroid]
    clusters: List[List] = []
    for row, vec in centered:
        best_i, best_sim = -1, -1.0
        for ci, (_, _, centroid) in enumerate(clusters):
            sim = cosine(vec, centroid)
            if sim > best_sim:
                best_i, best_sim = ci, sim
        if best_i >= 0 and best_sim >= threshold:
            members, vecs, _ = clusters[best_i]
            members.append(row)
            vecs.append(vec)
            clusters[best_i][2] = [sum(v[d] for v in vecs) / len(vecs) for d in range(dim)]
        else:
            clusters.append([[row], [vec], list(vec)])

    out = [members for members, _, _ in clusters if len(members) >= min_cluster]
    out.sort(key=len, reverse=True)
    return out


# ─────────────────────────────────────────────────────────
# GEMINI PROPOSALS + JUDGING
# ─────────────────────────────────────────────────────────

PROPOSE_SYSTEM = """You are a pattern-extraction assistant for the Antigravity memory system.

You receive a CLUSTER of related recent episodic decisions (routing choices, cost gates, content production events).
Your job: propose a single SEMANTIC RULE that captures the underlying pattern.

A good semantic rule:
- Names the rule (single sentence, imperative or declarative)
- Explains WHY (1-2 sentences — what motivates the rule)
- Explains HOW TO APPLY (1-2 sentences — when/where the rule triggers)

Output JSON only, no preamble. Schema:
{
  "rule": "<one-sentence rule>",
  "why": "<1-2 sentences>",
  "how_to_apply": "<1-2 sentences>",
  "proposed_category": "<one of: rule, pattern, principle>"
}

If the cluster does NOT reveal a generalizable pattern (just coincidental co-occurrence),
return: {"rule": null, "why": "no pattern", "how_to_apply": "", "proposed_category": "rule"}
"""

JUDGE_SYSTEM = """You are an evaluator for the Antigravity memory system.

You receive a proposed SEMANTIC RULE that was distilled from recent decisions.
Score it from 0-10 on this question:
"Would adding this rule to long-term memory be VALUABLE for future content, strategy,
or routing work — beyond what's already obvious from system documentation?"

Scoring anchors:
- 0-3: trivial, restates obvious system behavior, or too vague to apply
- 4-6: real but narrow — only useful in a specific edge case
- 7-8: load-bearing pattern that would meaningfully reduce future friction
- 9-10: signature insight, immediately changes how to approach a class of decisions

Output JSON only:
{
  "score": <0-10 float>,
  "rationale": "<one sentence explaining the score>"
}
"""


async def propose_rule(client, cluster: List[Dict]) -> Dict:
    """Ask Gemini to propose a semantic rule for one cluster."""
    examples = "\n".join(
        f"- ({i+1}) [{r['category']}] {r['content']}"
        for i, r in enumerate(cluster[:12])  # cap at 12 to keep prompt small
    )
    prompt = f"CLUSTER ({len(cluster)} decisions):\n\n{examples}\n\nPropose the rule."

    text, meta = await client.generate(
        prompt,
        system_instruction=PROPOSE_SYSTEM,
        model=JUDGE_MODEL,
        temperature=0.4,
        max_output_tokens=400,
        response_mime_type="application/json",
    )
    try:
        parsed = json.loads(text)
    except json.JSONDecodeError:
        return {"rule": None, "why": "parse_error", "how_to_apply": "",
                "proposed_category": "rule", "_raw": text}
    parsed["_meta"] = {"tokens": meta.total_tokens, "cost": meta.estimated_cost_usd}
    return parsed


async def judge_rule(client, proposal: Dict) -> Dict:
    """Score a proposed rule. Returns {score, rationale}."""
    if not proposal.get("rule"):
        return {"score": 0.0, "rationale": "no rule proposed"}
    prompt = (
        f"Rule: {proposal['rule']}\n"
        f"Why: {proposal.get('why', '')}\n"
        f"How to apply: {proposal.get('how_to_apply', '')}\n\n"
        f"Score it."
    )
    text, meta = await client.generate(
        prompt,
        system_instruction=JUDGE_SYSTEM,
        model=JUDGE_MODEL,
        temperature=0.2,
        max_output_tokens=200,
        response_mime_type="application/json",
    )
    try:
        parsed = json.loads(text)
        parsed["_meta"] = {"tokens": meta.total_tokens, "cost": meta.estimated_cost_usd}
        return parsed
    except json.JSONDecodeError:
        return {"score": 0.0, "rationale": f"parse_error: {text[:80]}"}


# ─────────────────────────────────────────────────────────
# FLAGGED REVIEW PERSISTENCE
# ─────────────────────────────────────────────────────────

def make_flagged_id(rule_text: str, source_ids: List[str]) -> str:
    """Stable ID so re-runs deduplicate."""
    h = hashlib.sha256(
        (rule_text + "|" + ",".join(sorted(source_ids))).encode("utf-8")
    ).hexdigest()[:16]
    return f"fr_{h}"


def insert_flagged(proposal: Dict, judge: Dict, cluster: List[Dict]) -> Optional[str]:
    """Insert into flagged_review. Returns ID or None if dup."""
    rule = proposal.get("rule")
    if not rule:
        return None
    source_ids = [r["id"] for r in cluster]
    fid = make_flagged_id(rule, source_ids)
    now = datetime.now(timezone.utc).isoformat()
    body = (
        f"{rule}\n\n"
        f"**Why:** {proposal.get('why', '')}\n"
        f"**How to apply:** {proposal.get('how_to_apply', '')}"
    )
    proposed_metadata = {
        "source": "memory_distill",
        "proposal_meta": proposal.get("_meta", {}),
        "judge_meta": judge.get("_meta", {}),
        "cluster_size": len(cluster),
    }

    conn = sqlite3.connect(str(DB_PATH))
    existing = conn.execute(
        "SELECT id FROM flagged_review WHERE id = ?", (fid,)
    ).fetchone()
    if existing:
        conn.close()
        return None

    conn.execute("""
        INSERT INTO flagged_review
            (id, proposed_tier, proposed_category, proposed_content, proposed_metadata,
             source_memory_ids, judge_score, judge_rationale, status, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, 'pending', ?)
    """, (
        fid, "semantic", proposal.get("proposed_category", "rule"),
        body, json.dumps(proposed_metadata),
        json.dumps(source_ids), float(judge.get("score", 0.0)),
        judge.get("rationale", ""), now,
    ))
    conn.commit()
    conn.close()
    return fid


# ─────────────────────────────────────────────────────────
# ORCHESTRATION
# ─────────────────────────────────────────────────────────

async def distill(days: int, min_cluster: int, judge_threshold: float,
                  dry_run: bool, max_clusters: Optional[int] = None,
                  include_export: bool = False) -> Dict:
    """Main distillation pass."""
    from gemini_client import GeminiClient, load_env
    load_env()
    client = GeminiClient()

    rows = load_recent_episodic(days, include_export=include_export)
    print(f"Loaded {len(rows)} recent episodic memories from last {days}d")
    clusters = cluster_by_cosine(rows, min_cluster=min_cluster)
    print(f"Found {len(clusters)} clusters with >= {min_cluster} members")

    if max_clusters:
        clusters = clusters[:max_clusters]

    summary = {
        "days": days, "rows": len(rows), "clusters": len(clusters),
        "proposed": 0, "flagged": 0, "skipped_below_threshold": 0,
        "skipped_no_rule": 0, "skipped_dup": 0,
        "total_cost_usd": 0.0,
        "proposals": [],
    }

    for i, cluster in enumerate(clusters, 1):
        print(f"\n[{i}/{len(clusters)}] cluster size={len(cluster)}")
        sample = cluster[0]["content"][:100]
        print(f"  sample: {sample}…")

        proposal = await propose_rule(client, cluster)
        summary["proposed"] += 1
        prop_cost = proposal.get("_meta", {}).get("cost", 0.0)

        if not proposal.get("rule"):
            print(f"  → no rule (judge skipped)")
            summary["skipped_no_rule"] += 1
            summary["total_cost_usd"] += prop_cost
            continue

        print(f"  rule: {proposal['rule']}")
        judge = await judge_rule(client, proposal)
        judge_cost = judge.get("_meta", {}).get("cost", 0.0)
        summary["total_cost_usd"] += prop_cost + judge_cost

        print(f"  judge_score: {judge.get('score')}/10 — {judge.get('rationale', '')[:80]}")

        proposal_record = {
            "cluster_size": len(cluster),
            "rule": proposal["rule"],
            "why": proposal.get("why"),
            "how_to_apply": proposal.get("how_to_apply"),
            "score": judge.get("score"),
            "rationale": judge.get("rationale"),
        }
        summary["proposals"].append(proposal_record)

        if float(judge.get("score", 0.0)) < judge_threshold:
            summary["skipped_below_threshold"] += 1
            print(f"  → below threshold ({judge_threshold}), skipped")
            continue

        if dry_run:
            print(f"  → would flag (dry-run)")
            summary["flagged"] += 1
        else:
            fid = insert_flagged(proposal, judge, cluster)
            if fid:
                print(f"  → FLAGGED: {fid}")
                summary["flagged"] += 1
            else:
                print(f"  → dup, skipped")
                summary["skipped_dup"] += 1

    print(f"\n─── DISTILL SUMMARY ───")
    print(f"  clusters processed: {summary['clusters']}")
    print(f"  proposed: {summary['proposed']}")
    print(f"  flagged: {summary['flagged']}")
    print(f"  skipped (below threshold): {summary['skipped_below_threshold']}")
    print(f"  skipped (no rule): {summary['skipped_no_rule']}")
    print(f"  skipped (duplicate): {summary['skipped_dup']}")
    print(f"  total cost: ${summary['total_cost_usd']:.4f}")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description="Memory Distill — weekly Gemini-judged proposal pipeline")
    parser.add_argument("command", nargs="?", default="run", choices=["run", "preview"],
                       help="run = execute (default); preview = same as --dry-run")
    parser.add_argument("--days", type=int, default=DEFAULT_DAYS,
                       help=f"Look back N days (default {DEFAULT_DAYS})")
    parser.add_argument("--min-cluster", type=int, default=DEFAULT_MIN_CLUSTER,
                       help=f"Minimum cluster size (default {DEFAULT_MIN_CLUSTER})")
    parser.add_argument("--judge-threshold", type=float, default=DEFAULT_JUDGE_THRESHOLD,
                       help=f"Min judge score to flag (default {DEFAULT_JUDGE_THRESHOLD})")
    parser.add_argument("--max-clusters", type=int, help="Cap clusters processed (testing)")
    parser.add_argument("--dry-run", action="store_true", help="Don't write to flagged_review")
    parser.add_argument("--include-export", action="store_true",
                        help="Include the claude-export workspace (excluded by default to protect "
                             "the weekly cron; use for deliberate, small, batched enrichment)")
    parser.add_argument("--json", action="store_true", help="JSON summary output")
    args = parser.parse_args()

    dry_run = args.dry_run or args.command == "preview"

    summary = asyncio.run(distill(
        days=args.days,
        include_export=args.include_export,
        min_cluster=args.min_cluster,
        judge_threshold=args.judge_threshold,
        dry_run=dry_run,
        max_clusters=args.max_clusters,
    ))

    if args.json:
        print(json.dumps(summary, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
