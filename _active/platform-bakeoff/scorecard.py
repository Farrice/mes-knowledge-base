#!/usr/bin/env python3
"""Aggregate bakeoff scores and apply the pre-committed decision rule.

Reads scores.jsonl (one JSON object per task x platform), prints per-platform
composites and the mechanical verdict. The rule lives in PROTOCOL.md and is
mirrored here; do not edit after the first run is recorded.
"""

import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
MIN_COMPOSITE = 7.5
MIN_TASK = 6.5
LANE_KEEP = 7.0
TIEBREAK_TASK = 3
N_TASKS = 6


def composite(row):
    dims = [row.get(k) for k in ("intent", "expert", "adversarial", "grounding")]
    dims = [d for d in dims if d is not None]
    return sum(dims) / len(dims)


def main():
    path = HERE / "scores.jsonl"
    if not path.exists():
        print("No scores.jsonl yet — run tasks per PROTOCOL.md first.")
        return
    rows = [json.loads(l) for l in path.read_text().splitlines() if l.strip()]
    by_platform = defaultdict(dict)
    for r in rows:
        by_platform[r["platform"]][r["task"]] = composite(r)

    print(f"{'platform':<18}{'tasks':>6}{'avg':>7}{'min':>7}  task scores")
    results = {}
    for plat, tasks in sorted(by_platform.items()):
        scores = [tasks[t] for t in sorted(tasks)]
        avg = sum(scores) / len(scores)
        results[plat] = {"avg": avg, "min": min(scores), "n": len(tasks), "tasks": tasks}
        detail = " ".join(f"T{t}:{tasks[t]:.1f}" for t in sorted(tasks))
        print(f"{plat:<18}{len(tasks):>6}{avg:>7.2f}{min(scores):>7.2f}  {detail}")

    complete = {p: r for p, r in results.items() if r["n"] == N_TASKS}
    qualified = {p: r for p, r in complete.items() if r["avg"] >= MIN_COMPOSITE and r["min"] >= MIN_TASK}

    print()
    if not complete:
        print(f"VERDICT: incomplete — no platform has all {N_TASKS} tasks scored.")
        return
    if not qualified:
        print("VERDICT: no platform clears the bar (>=7.5 avg, no task <6.5).")
        print("  -> Claude Code remains daily driver BY DATA. Satellites: re-test after next packaging fix.")
    else:
        ranked = sorted(qualified.items(), key=lambda kv: (-kv[1]["avg"], -kv[1]["tasks"].get(TIEBREAK_TASK, 0)))
        top_avg = ranked[0][1]["avg"]
        tied = [p for p, r in ranked if abs(r["avg"] - top_avg) < 0.05]
        winner = ranked[0][0]
        if len(tied) > 1:
            winner = max(tied, key=lambda p: qualified[p]["tasks"].get(TIEBREAK_TASK, 0))
            print(f"Tie among {tied} -> broken by task {TIEBREAK_TASK} (research).")
        print(f"VERDICT: daily driver = {winner} (avg {qualified[winner]['avg']:.2f})")

    print("\nLane assignments (>=7.0 on a task keeps that lane):")
    for plat, r in sorted(complete.items()):
        lanes = [f"T{t}" for t, s in sorted(r["tasks"].items()) if s >= LANE_KEEP]
        print(f"  {plat}: {', '.join(lanes) if lanes else 'experimental only'}")


if __name__ == "__main__":
    main()
