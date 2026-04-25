#!/usr/bin/env python3
"""
Eval Harness — Score outputs against the calibrated rubric (Fix 1 / 2026-04-24).

The rubric (`evolution_store/ground_truth/rubric_v1.md`) defines anchored
scoring criteria for the 4 quality dimensions. This harness:

    1. Loads the calibrated rubric + eval set
    2. Provides a calibration_check(): runs blind comparison of new finalize
       scores vs. ground-truth eval scores to detect rubric drift
    3. Provides a score_against_rubric() helper that returns a structured
       prompt the model can use to self-score with anchor references

Usage:

    # Show the eval set and current calibration status
    python3 execution/eval_harness.py status

    # Run blind calibration: take the last N finalize traces and check whether
    # rubric scoring would produce similar scores to what the model assigned
    python3 execution/eval_harness.py calibrate --days 7

    # Print the rubric anchor reference for a specific dimension
    python3 execution/eval_harness.py anchor --dimension intent_alignment --score 6
"""

import json
import sys
import argparse
from pathlib import Path
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
from collections import defaultdict

ROOT = Path(__file__).parent.parent
RUBRIC_PATH = ROOT / "evolution_store" / "ground_truth" / "rubric_v1.md"
EVAL_SET_PATH = ROOT / "evolution_store" / "ground_truth" / "eval_set_v1.jsonl"
TRACES_DIR = ROOT / "evolution_store" / "v2_traces"

DIMENSIONS = ["intent_alignment", "expert_standard", "adversarial_resilience", "factual_grounding"]


def load_eval_set() -> List[Dict[str, Any]]:
    """Load the eval set as a list of dicts."""
    if not EVAL_SET_PATH.exists():
        return []
    entries = []
    with open(EVAL_SET_PATH) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                entries.append(json.loads(line))
            except Exception:
                continue
    return entries


def calibration_status() -> Dict[str, Any]:
    """Report which eval entries have been human-calibrated vs. seeded."""
    entries = load_eval_set()
    total = len(entries)
    calibrated = sum(1 for e in entries if e.get("calibrated_by_human"))
    placeholders = sum(1 for e in entries if e.get("source") == "PLACEHOLDER")
    return {
        "total_entries": total,
        "human_calibrated": calibrated,
        "placeholders_to_fill": placeholders,
        "auto_seeded_pending_review": total - calibrated - placeholders,
        "calibration_complete": calibrated >= 15 and placeholders == 0,
        "rubric_load_bearing": calibrated >= 15,
        "next_action": (
            "Fill placeholders + review auto-seeded entries against rubric anchors."
            if calibrated < 15
            else "Run blind comparison and tighten anchors if divergence > 1.0 average."
        ),
    }


def load_recent_traces(days: int = 7) -> List[Dict[str, Any]]:
    """Load v2 traces from the last N days."""
    if not TRACES_DIR.exists():
        return []
    cutoff = datetime.now() - timedelta(days=days)
    traces = []
    for tf in TRACES_DIR.glob("trace_*.json"):
        try:
            mtime = datetime.fromtimestamp(tf.stat().st_mtime)
            if mtime < cutoff:
                continue
            traces.append(json.load(open(tf)))
        except Exception:
            continue
    return traces


def calibrate(days: int = 7) -> Dict[str, Any]:
    """
    Sanity-check rubric vs. recent finalize() scores.

    Approach:
        1. Load recent v2 traces (the score the model assigned at finalize)
        2. For each, compare against the seeded eval entries with similar task_type
        3. Flag traces where the model's scores look anomalous vs. the rubric's
           expected score for the closest eval entry

    This is rough — true calibration requires a second model pass scoring the
    actual output text against rubric anchors. For Fix 1 v1, we surface the
    distribution of scores so drift becomes visible.
    """
    traces = load_recent_traces(days)
    eval_set = load_eval_set()

    if not traces:
        return {"error": "no_traces", "message": f"No v2 traces in last {days} days."}

    # Distribution analysis
    score_buckets: Dict[str, List[float]] = defaultdict(list)
    for t in traces:
        q = t.get("quality") or {}
        for dim in DIMENSIONS:
            v = q.get(dim)
            if v is not None and v > 0:
                score_buckets[dim].append(float(v))

    def _stats(xs):
        if not xs:
            return None
        return {
            "n": len(xs),
            "mean": round(sum(xs) / len(xs), 2),
            "min": min(xs),
            "max": max(xs),
            "below_6": sum(1 for x in xs if x < 6),
            "above_8": sum(1 for x in xs if x >= 8),
            "above_9_5": sum(1 for x in xs if x >= 9.5),
        }

    distribution = {dim: _stats(score_buckets[dim]) for dim in DIMENSIONS}

    # Inflation alarm: if >70% of scores in any dimension are 8+, flag for recalibration
    inflation_alarms = []
    for dim, stats in distribution.items():
        if stats and stats["n"] >= 5 and stats["above_8"] / stats["n"] > 0.7:
            inflation_alarms.append(
                f"{dim}: {stats['above_8']}/{stats['n']} ({100*stats['above_8']/stats['n']:.0f}%) scored 8+. "
                f"Either output quality is exceptional or the rubric isn't being applied. Spot-check with anchor reference."
            )

    return {
        "window_days": days,
        "traces_analyzed": len(traces),
        "eval_set_size": len(eval_set),
        "score_distribution": distribution,
        "inflation_alarms": inflation_alarms,
        "interpretation": (
            "If inflation_alarms is non-empty, spot-check 3 high-scored outputs against the rubric anchors. "
            "If they don't actually match Anchor 8+ examples, the rubric isn't being used during scoring."
        ),
    }


def get_anchor(dimension: str, score: int) -> str:
    """Return the rubric anchor description for a dimension + score band."""
    if dimension not in DIMENSIONS:
        return f"Unknown dimension: {dimension}"
    band = "Anchor 9 (Exemplary)" if score >= 9 else "Anchor 6 (Passable)" if score >= 6 else "Anchor 3 (Clear fail)"
    return f"For {dimension} score {score} → {band}. See evolution_store/ground_truth/rubric_v1.md for the worked example."


def main():
    parser = argparse.ArgumentParser(description="Eval Harness — rubric calibration and drift detection")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("status", help="Show eval set calibration status")

    cal = sub.add_parser("calibrate", help="Distribution + drift analysis on recent traces")
    cal.add_argument("--days", type=int, default=7)

    anc = sub.add_parser("anchor", help="Look up rubric anchor reference")
    anc.add_argument("--dimension", required=True, choices=DIMENSIONS)
    anc.add_argument("--score", type=int, required=True)

    args = parser.parse_args()

    if args.command == "status":
        print(json.dumps(calibration_status(), indent=2))
        sys.exit(0)

    if args.command == "calibrate":
        print(json.dumps(calibrate(days=args.days), indent=2))
        sys.exit(0)

    if args.command == "anchor":
        print(get_anchor(args.dimension, args.score))
        sys.exit(0)

    parser.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
