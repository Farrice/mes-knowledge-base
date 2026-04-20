#!/usr/bin/env python3
"""
Evolution Tracer v3 — Reasoning-trajectory trace logging for Antigravity loops.

Captures prompt→response traces, quality signals, reasoning chains, failure
signals by type, hypothesis, variant diffs, held-out scores, and gaming flags.
Feeds the evolution loop's diagnostic layer (Nate B Jones GP-6: Traces > Scores).

v3 upgrade (2026-04-20) per Karpathy Loop audit — adds reasoning fields so
meta-agents and human diagnosticians can ask "where did this variant lose
direction?" rather than only seeing outcome scores.

This script is ADDITIVE — it logs data but never modifies production code,
skills, workflows, or harness files.

Usage:
    # Log an execution trace (v3 — with reasoning trajectory)
    python execution/evolution_tracer.py log \\
        --component "skills/lara-acosta-linkedin-ghostwriting/SKILL.md" \\
        --operation "evolution_cycle" \\
        --expert "lara-acosta" \\
        --workflow "high-dwell" \\
        --quality-score 8.3 \\
        --intent 9 --expert-score 8 --adversarial 8 --factual 9 \\
        --hypothesis "Add Proof Layer Audit to improve adversarial resilience" \\
        --variant-diff "Added Phase 4b with 5 proof checks before quality gate" \\
        --held-out-score 7.8 --held-out-delta 0.5 \\
        --notes "Strong hook but weak CTA"

    # Query traces for a component
    python execution/evolution_tracer.py query --component "AGENTS.md" --limit 10

    # Diagnose a specific trace (v3 — reads reasoning chain + failure signals)
    python execution/evolution_tracer.py diagnose --trace-id 20260420_123839

    # Gaming check — scan recent traces for held_out_delta > threshold
    python execution/evolution_tracer.py gaming-check --threshold 1.5 --limit 30

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
    factual: float = 0.0,
    token_estimate: int = 0,
    notes: str = "",
    context: dict = None,
    # ─── v3 reasoning-trajectory fields (Nate GP-6 Traces Over Scores) ───
    hypothesis: str = "",
    variant_diff: str = "",
    reasoning_chain: list = None,
    failure_signals: list = None,
    benchmark_tasks: list = None,
    held_out_score: float = 0.0,
    held_out_delta: float = 0.0,
    gaming_flag: bool = False,
    schema_version: str = "v3",
) -> dict:
    """Log an execution trace to the v3 trace store.

    v3 additions (per Karpathy Loop audit 2026-04-20):
      hypothesis:      what was tested (plain-English)
      variant_diff:    what changed in the workflow (git diff or prose summary)
      reasoning_chain: list of {step, thought, decision, alternatives_considered}
      failure_signals: list of {step, signal_type, severity, description}
      benchmark_tasks: list of task IDs actually run this cycle
      held_out_score:  score on rotating held-out task (Upgrade 2 integration)
      held_out_delta:  seen_avg - held_out_score (gaming signal >1.5)
      gaming_flag:     True if held_out_delta exceeds threshold
      schema_version:  trace schema version for future migration

    Backwards-compatible: all v3 fields are optional. v2 traces remain readable.
    """
    timestamp = datetime.now().isoformat()
    trace_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    trace = {
        "trace_id": trace_id,
        "timestamp": timestamp,
        "schema_version": schema_version,
        "component": component,
        "operation": operation,
        "expert": expert,
        "workflow": workflow,
        "quality": {
            "composite": quality_score,
            "intent_alignment": intent,
            "expert_standard": expert_score,
            "adversarial_resilience": adversarial,
            "factual_grounding": factual,
        },
        "reasoning": {
            "hypothesis": hypothesis,
            "variant_diff": variant_diff,
            "reasoning_chain": reasoning_chain or [],
            "failure_signals": failure_signals or [],
        },
        "evaluation": {
            "benchmark_tasks": benchmark_tasks or [],
            "held_out_score": held_out_score,
            "held_out_delta": held_out_delta,
            "gaming_flag": gaming_flag,
        },
        "token_estimate": token_estimate,
        "notes": notes,
        "context": context or {},
    }

    # Determine if this is a failure (search set candidate)
    # v3: also flag on gaming, factual <6, or any reasoning-chain failure signal of severity "blocker"
    dim_scores = [intent, expert_score, adversarial]
    if factual > 0:
        dim_scores.append(factual)
    has_blocker_signal = any(
        s.get("severity") == "blocker" for s in (failure_signals or [])
    )
    is_failure = (
        quality_score < 7.0
        or any(s < 6.0 for s in dim_scores if s > 0)
        or gaming_flag
        or has_blocker_signal
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

    # Add case — v3 includes reasoning trajectory for meta-agent diagnosis
    search_set["cases"].append({
        "trace_id": trace["trace_id"],
        "timestamp": trace["timestamp"],
        "schema_version": trace.get("schema_version", "v2"),
        "component": trace["component"],
        "expert": trace["expert"],
        "workflow": trace["workflow"],
        "quality": trace["quality"],
        "reasoning": trace.get("reasoning", {}),
        "evaluation": trace.get("evaluation", {}),
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


def diagnose_trace(trace_id: str = None, component: str = None) -> dict:
    """v3 — Read a trace's reasoning chain + failure signals for targeted diagnosis.

    Answers "where did this variant lose direction?" — the core Nate GP-6 question
    that score-only traces cannot address.
    """
    # Find the trace
    target = None
    for trace_file in sorted(TRACE_DIR.glob("trace_*.json"), reverse=True):
        with open(trace_file) as f:
            t = json.load(f)
        if trace_id and trace_id in t.get("trace_id", ""):
            target = t
            break
        if component and not trace_id and component in t.get("component", ""):
            target = t
            break

    if not target:
        print(f"No trace found matching trace_id={trace_id} component={component}")
        return {}

    print(f"\n{'='*60}")
    print(f"  DIAGNOSE — {target['trace_id']}")
    print(f"{'='*60}")
    print(f"  Component:       {target['component']}")
    print(f"  Schema version:  {target.get('schema_version', 'v2 (legacy)')}")
    print(f"  Expert/workflow: {target.get('expert', 'n/a')} / {target.get('workflow', 'n/a')}")
    print(f"  Composite:       {target['quality']['composite']}/10")

    if target.get("schema_version") != "v3":
        print(f"\n  ⚠️  Legacy v2 trace — no reasoning chain captured.")
        print(f"  Notes: {target.get('notes', '(none)')}")
        print(f"{'='*60}\n")
        return target

    reasoning = target.get("reasoning", {})
    evaluation = target.get("evaluation", {})

    print(f"\n  ── Hypothesis ──")
    print(f"  {reasoning.get('hypothesis') or '(not recorded)'}")

    print(f"\n  ── Variant diff ──")
    print(f"  {reasoning.get('variant_diff') or '(not recorded)'}")

    chain = reasoning.get("reasoning_chain", [])
    if chain:
        print(f"\n  ── Reasoning chain ({len(chain)} steps) ──")
        for step in chain:
            print(f"  [{step.get('step', '?')}] {step.get('thought', '')[:120]}")
            if step.get("decision"):
                print(f"      → decision: {step['decision'][:120]}")

    signals = reasoning.get("failure_signals", [])
    if signals:
        print(f"\n  ── Failure signals ({len(signals)}) ──")
        for sig in signals:
            sev = sig.get("severity", "unknown")
            marker = "🔴" if sev == "blocker" else "🟠" if sev == "major" else "🟡"
            print(f"  {marker} step {sig.get('step', '?')} | {sig.get('signal_type', '')} | {sig.get('description', '')[:80]}")

    if evaluation.get("held_out_score"):
        delta = evaluation.get("held_out_delta", 0)
        flag = "🚨 GAMING" if evaluation.get("gaming_flag") else "✅"
        print(f"\n  ── Held-out evaluation ──")
        print(f"  Held-out score: {evaluation['held_out_score']}/10")
        print(f"  Seen-vs-held-out delta: {delta:.2f} {flag}")

    print(f"\n  Notes: {target.get('notes', '(none)')}")
    print(f"{'='*60}\n")
    return target


def gaming_check(threshold: float = 1.5, limit: int = 30) -> list:
    """v3 — Scan recent traces for held_out_delta exceeding threshold.

    Metric-gaming detection per Nate GP-12. A variant that scores high on seen
    tasks but low on held-out tasks is gaming the rubric.
    """
    flagged = []
    for trace_file in sorted(TRACE_DIR.glob("trace_*.json"), reverse=True)[:limit]:
        with open(trace_file) as f:
            t = json.load(f)
        evaluation = t.get("evaluation", {})
        delta = evaluation.get("held_out_delta", 0)
        if delta > threshold or evaluation.get("gaming_flag"):
            flagged.append({
                "trace_id": t["trace_id"],
                "component": t["component"],
                "composite": t["quality"]["composite"],
                "held_out": evaluation.get("held_out_score"),
                "delta": delta,
                "flag": evaluation.get("gaming_flag"),
            })

    print(f"\n{'='*60}")
    print(f"  GAMING CHECK — threshold {threshold}, last {limit} traces")
    print(f"{'='*60}")
    if not flagged:
        print(f"  ✅ No gaming signals detected.")
    else:
        for f in flagged:
            print(f"  🚨 {f['trace_id']} | {f['component'][:40]} | composite {f['composite']}, held_out {f['held_out']}, delta {f['delta']:.2f}")
    print(f"{'='*60}\n")
    return flagged


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
    log_parser.add_argument("--factual", type=float, default=0.0, help="Factual grounding score (0 = N/A)")
    log_parser.add_argument("--token-estimate", type=int, default=0, help="Estimated token usage")
    log_parser.add_argument("--notes", default="", help="Additional notes")
    # ─── v3 reasoning-trajectory fields ───
    log_parser.add_argument("--hypothesis", default="", help="Plain-English statement of what the variant tested")
    log_parser.add_argument("--variant-diff", default="", help="What changed (git diff summary or prose)")
    log_parser.add_argument("--reasoning-chain", default="", help="JSON array of {step, thought, decision, alternatives_considered}")
    log_parser.add_argument("--failure-signals", default="", help="JSON array of {step, signal_type, severity, description}")
    log_parser.add_argument("--benchmark-tasks", default="", help="Comma-separated list of task IDs run this cycle")
    log_parser.add_argument("--held-out-score", type=float, default=0.0, help="Score on rotating held-out task (Upgrade 2)")
    log_parser.add_argument("--held-out-delta", type=float, default=0.0, help="seen_avg - held_out_score; gaming signal >1.5")
    log_parser.add_argument("--gaming-flag", action="store_true", help="Flag variant as potentially gaming the metric")

    # Query command
    query_parser = subparsers.add_parser("query", help="Query execution traces")
    query_parser.add_argument("--component", default=None, help="Filter by component")
    query_parser.add_argument("--limit", type=int, default=20, help="Max results")

    # Search set command
    ss_parser = subparsers.add_parser("search-set", help="Build search set from failures")
    ss_parser.add_argument("--threshold", type=float, default=7.0, help="Quality threshold")

    # Coverage command
    subparsers.add_parser("coverage", help="Evolution coverage report")

    # v3 — Diagnose command (reasoning-chain read)
    diag_parser = subparsers.add_parser("diagnose", help="v3 — Read reasoning chain + failure signals for a trace")
    diag_parser.add_argument("--trace-id", default=None, help="Trace ID to diagnose (partial match OK)")
    diag_parser.add_argument("--component", default=None, help="Find most recent trace matching component")

    # v3 — Gaming check
    gc_parser = subparsers.add_parser("gaming-check", help="v3 — Scan recent traces for held-out delta > threshold")
    gc_parser.add_argument("--threshold", type=float, default=1.5, help="Gaming delta threshold (default 1.5)")
    gc_parser.add_argument("--limit", type=int, default=30, help="Most recent N traces to scan")

    args = parser.parse_args()

    if args.command == "log":
        # Parse JSON fields if provided
        reasoning_chain = json.loads(args.reasoning_chain) if args.reasoning_chain else None
        failure_signals = json.loads(args.failure_signals) if args.failure_signals else None
        benchmark_tasks = [t.strip() for t in args.benchmark_tasks.split(",") if t.strip()] if args.benchmark_tasks else None

        log_trace(
            component=args.component,
            operation=args.operation,
            expert=args.expert,
            workflow=args.workflow,
            quality_score=args.quality_score,
            intent=args.intent,
            expert_score=args.expert_score,
            adversarial=args.adversarial,
            factual=args.factual,
            token_estimate=args.token_estimate,
            notes=args.notes,
            hypothesis=args.hypothesis,
            variant_diff=args.variant_diff,
            reasoning_chain=reasoning_chain,
            failure_signals=failure_signals,
            benchmark_tasks=benchmark_tasks,
            held_out_score=args.held_out_score,
            held_out_delta=args.held_out_delta,
            gaming_flag=args.gaming_flag,
        )
    elif args.command == "query":
        query_traces(component=args.component, limit=args.limit)
    elif args.command == "search-set":
        build_search_set(threshold=args.threshold)
    elif args.command == "coverage":
        coverage_report()
    elif args.command == "diagnose":
        diagnose_trace(trace_id=args.trace_id, component=args.component)
    elif args.command == "gaming-check":
        gaming_check(threshold=args.threshold, limit=args.limit)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
