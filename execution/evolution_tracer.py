#!/usr/bin/env python3
"""
Evolution Tracer — Execution trace logging for Antigravity evolution loops.

Captures prompt→response traces, quality signals, token usage, and state
mutations. Feeds the evolution loop's diagnostic layer (GP-7: Trace > Score).

This script is ADDITIVE — it logs data but never modifies production code,
skills, workflows, or harness files.

Usage:
    # Log an execution trace
    python execution/evolution_tracer.py log \
        --component "skills/lara-acosta-linkedin-ghostwriting/SKILL.md" \
        --operation "chain_finalize" \
        --expert "lara-acosta" \
        --workflow "high-dwell" \
        --quality-score 8.3 \
        --intent 9 --expert-score 8 --adversarial 8 \
        --token-estimate 4500 \
        --notes "Strong hook but weak CTA"

    # Query traces for a component
    python execution/evolution_tracer.py query --component "AGENTS.md" --limit 10

    # Build search set from failures
    python execution/evolution_tracer.py search-set --threshold 7.0

    # Get evolution coverage report
    python execution/evolution_tracer.py coverage
"""

import os
import sys
import json
import argparse
from datetime import datetime
from pathlib import Path

# Trace storage
TRACE_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) / "evolution_store" / "v2_traces"
SEARCH_SET_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) / "evolution_store" / "v2_search_sets"
GROUND_TRUTH_DIR = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) / "evolution_store" / "ground_truth"

# Ensure directories exist
TRACE_DIR.mkdir(parents=True, exist_ok=True)
SEARCH_SET_DIR.mkdir(parents=True, exist_ok=True)
GROUND_TRUTH_DIR.mkdir(parents=True, exist_ok=True)


def log_trace(
    component: str,
    operation: str,
    expert: str = "",
    workflow: str = "",
    quality_score: float = 0.0,
    intent: float = 0.0,
    expert_score: float = 0.0,
    adversarial: float = 0.0,
    token_estimate: int = 0,
    notes: str = "",
    context: dict = None,
) -> dict:
    """Log an execution trace to the v2 trace store."""
    timestamp = datetime.now().isoformat()
    trace_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    trace = {
        "trace_id": trace_id,
        "timestamp": timestamp,
        "component": component,
        "operation": operation,
        "expert": expert,
        "workflow": workflow,
        "quality": {
            "composite": quality_score,
            "intent_alignment": intent,
            "expert_standard": expert_score,
            "adversarial_resilience": adversarial,
        },
        "token_estimate": token_estimate,
        "notes": notes,
        "context": context or {},
    }

    # Determine if this is a failure (search set candidate)
    is_failure = quality_score < 7.0 or any(
        s < 6.0 for s in [intent, expert_score, adversarial] if s > 0
    )
    trace["is_failure"] = is_failure

    # Write trace file
    safe_component = component.replace("/", "_").replace(".", "_")
    filename = f"trace_{trace_id}_{safe_component}.json"
    filepath = TRACE_DIR / filename

    with open(filepath, "w") as f:
        json.dump(trace, f, indent=2)

    # Auto-add to search set if failure
    if is_failure:
        add_to_search_set(trace)

    print(f"{'🔴' if is_failure else '✅'} Trace logged: {filepath.name}")
    print(f"   Component: {component}")
    print(f"   Quality:   {quality_score}/10")
    if is_failure:
        print(f"   ⚠️  Added to search set (quality < 7.0 or dimension < 6.0)")

    return trace


def add_to_search_set(trace: dict):
    """Add a failure trace to the search set for evolution targeting."""
    search_set_file = SEARCH_SET_DIR / "active_search_set.json"

    # Load existing search set or create new
    if search_set_file.exists():
        with open(search_set_file) as f:
            search_set = json.load(f)
    else:
        search_set = {
            "created": datetime.now().isoformat(),
            "description": "Auto-populated from chain finalize failures (composite < 7 or any dimension < 6)",
            "cases": [],
        }

    # Add case
    search_set["cases"].append({
        "trace_id": trace["trace_id"],
        "timestamp": trace["timestamp"],
        "component": trace["component"],
        "expert": trace["expert"],
        "workflow": trace["workflow"],
        "quality": trace["quality"],
        "notes": trace["notes"],
    })
    search_set["last_updated"] = datetime.now().isoformat()
    search_set["total_cases"] = len(search_set["cases"])

    with open(search_set_file, "w") as f:
        json.dump(search_set, f, indent=2)


def query_traces(component: str = None, limit: int = 20) -> list:
    """Query traces, optionally filtered by component."""
    traces = []
    for trace_file in sorted(TRACE_DIR.glob("trace_*.json"), reverse=True):
        with open(trace_file) as f:
            trace = json.load(f)
        if component and component not in trace.get("component", ""):
            continue
        traces.append(trace)
        if len(traces) >= limit:
            break

    if not traces:
        print(f"No traces found" + (f" for component '{component}'" if component else ""))
        return []

    print(f"\n{'='*60}")
    print(f"  TRACE QUERY — {len(traces)} results")
    print(f"{'='*60}")
    for t in traces:
        status = "🔴" if t.get("is_failure") else "✅"
        print(f"  {status} {t['trace_id']} | {t['component'][:40]} | {t['quality']['composite']}/10 | {t.get('expert', 'n/a')}")
    print(f"{'='*60}\n")
    return traces


def build_search_set(threshold: float = 7.0) -> dict:
    """Rebuild search set from all traces below threshold."""
    search_set = {
        "created": datetime.now().isoformat(),
        "threshold": threshold,
        "description": f"All traces with composite < {threshold} or any dimension < 6.0",
        "cases": [],
    }

    for trace_file in sorted(TRACE_DIR.glob("trace_*.json")):
        with open(trace_file) as f:
            trace = json.load(f)
        quality = trace.get("quality", {})
        composite = quality.get("composite", 10)
        dims = [quality.get("intent_alignment", 10), quality.get("expert_standard", 10), quality.get("adversarial_resilience", 10)]

        if composite < threshold or any(d < 6.0 for d in dims if d > 0):
            search_set["cases"].append({
                "trace_id": trace["trace_id"],
                "timestamp": trace["timestamp"],
                "component": trace["component"],
                "expert": trace.get("expert", ""),
                "workflow": trace.get("workflow", ""),
                "quality": quality,
                "notes": trace.get("notes", ""),
            })

    search_set["total_cases"] = len(search_set["cases"])
    search_set["last_updated"] = datetime.now().isoformat()

    output_file = SEARCH_SET_DIR / "active_search_set.json"
    with open(output_file, "w") as f:
        json.dump(search_set, f, indent=2)

    print(f"\n{'='*60}")
    print(f"  SEARCH SET REBUILT — {search_set['total_cases']} cases below {threshold}")
    print(f"{'='*60}")
    for case in search_set["cases"]:
        print(f"  🔴 {case['component'][:40]} | {case['quality']['composite']}/10 | {case.get('expert', 'n/a')}")
    if not search_set["cases"]:
        print(f"  ✅ No failures found. All traces above threshold.")
    print(f"{'='*60}\n")
    return search_set


def coverage_report() -> dict:
    """Generate evolution coverage report."""
    # Collect unique components from traces
    traced_components = set()
    total_traces = 0
    failures = 0
    scores = []

    for trace_file in TRACE_DIR.glob("trace_*.json"):
        with open(trace_file) as f:
            trace = json.load(f)
        traced_components.add(trace.get("component", "unknown"))
        total_traces += 1
        if trace.get("is_failure"):
            failures += 1
        score = trace.get("quality", {}).get("composite", 0)
        if score > 0:
            scores.append(score)

    # Count system components
    project_root = Path(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    skills = len(list((project_root / "skills").glob("*"))) if (project_root / "skills").exists() else 0
    agents = len(list((project_root / "agents").glob("*"))) if (project_root / "agents").exists() else 0
    workflows = len(list((project_root / ".agent" / "workflows").glob("*.md"))) if (project_root / ".agent" / "workflows").exists() else 0
    scripts = len(list((project_root / "execution").glob("*.py"))) if (project_root / "execution").exists() else 0
    total = skills + agents + workflows + scripts + 2  # +2 for AGENTS.md and GEMINI.md

    # Check ground truth
    gt_files = list(GROUND_TRUTH_DIR.glob("*.json"))

    avg_score = sum(scores) / len(scores) if scores else 0

    report = {
        "timestamp": datetime.now().isoformat(),
        "system": {
            "skills": skills,
            "agents": agents,
            "workflows": workflows,
            "execution_scripts": scripts,
            "harness_files": 2,
            "total_components": total,
        },
        "evolution": {
            "traced_components": len(traced_components),
            "coverage_pct": round(len(traced_components) / max(total, 1) * 100, 2),
            "total_traces": total_traces,
            "failures": failures,
            "failure_rate_pct": round(failures / max(total_traces, 1) * 100, 2),
            "avg_quality_score": round(avg_score, 2),
            "ground_truth_samples": len(gt_files),
        },
    }

    print(f"\n{'='*60}")
    print(f"  EVOLUTION COVERAGE REPORT")
    print(f"{'='*60}")
    print(f"  System Components:     {total}")
    print(f"  Traced Components:     {len(traced_components)}")
    print(f"  Coverage:              {report['evolution']['coverage_pct']}%")
    print(f"  Total Traces:          {total_traces}")
    print(f"  Failures:              {failures} ({report['evolution']['failure_rate_pct']}%)")
    print(f"  Avg Quality Score:     {avg_score:.1f}/10")
    print(f"  Ground Truth Samples:  {len(gt_files)}")
    print(f"{'='*60}\n")

    return report


def main():
    parser = argparse.ArgumentParser(description="Evolution Tracer for Antigravity")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Log command
    log_parser = subparsers.add_parser("log", help="Log an execution trace")
    log_parser.add_argument("--component", required=True, help="Component being traced")
    log_parser.add_argument("--operation", required=True, help="Operation type (chain_finalize, skill_load, etc.)")
    log_parser.add_argument("--expert", default="", help="Expert name")
    log_parser.add_argument("--workflow", default="", help="Workflow name")
    log_parser.add_argument("--quality-score", type=float, default=0.0, help="Composite quality score")
    log_parser.add_argument("--intent", type=float, default=0.0, help="Intent alignment score")
    log_parser.add_argument("--expert-score", type=float, default=0.0, help="Expert standard score")
    log_parser.add_argument("--adversarial", type=float, default=0.0, help="Adversarial resilience score")
    log_parser.add_argument("--token-estimate", type=int, default=0, help="Estimated token usage")
    log_parser.add_argument("--notes", default="", help="Additional notes")

    # Query command
    query_parser = subparsers.add_parser("query", help="Query execution traces")
    query_parser.add_argument("--component", default=None, help="Filter by component")
    query_parser.add_argument("--limit", type=int, default=20, help="Max results")

    # Search set command
    ss_parser = subparsers.add_parser("search-set", help="Build search set from failures")
    ss_parser.add_argument("--threshold", type=float, default=7.0, help="Quality threshold")

    # Coverage command
    subparsers.add_parser("coverage", help="Evolution coverage report")

    args = parser.parse_args()

    if args.command == "log":
        log_trace(
            component=args.component,
            operation=args.operation,
            expert=args.expert,
            workflow=args.workflow,
            quality_score=args.quality_score,
            intent=args.intent,
            expert_score=args.expert_score,
            adversarial=args.adversarial,
            token_estimate=args.token_estimate,
            notes=args.notes,
        )
    elif args.command == "query":
        query_traces(component=args.component, limit=args.limit)
    elif args.command == "search-set":
        build_search_set(threshold=args.threshold)
    elif args.command == "coverage":
        coverage_report()
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
