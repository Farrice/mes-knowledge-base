#!/usr/bin/env python3
"""Savant Control Room for the Codex Antigravity harness."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent.parent
EXECUTION = ROOT / "execution"
sys.path.insert(0, str(EXECUTION))

import capability_graph  # type: ignore  # noqa: E402
import harness_status  # type: ignore  # noqa: E402
import plugin_readiness_audit  # type: ignore  # noqa: E402
import routing_intelligence  # type: ignore  # noqa: E402
from operator_core_fast_proof import build_proof  # noqa: E402


OPERATOR_CORE_CANDIDATES = (
    "mission",
    "knowledge-librarian",
    "extraction-governor-agent",
    "routing-intelligence",
    "health-check",
    "self-evolve",
    "ai-employee-os",
)


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def routing_summary() -> dict[str, Any]:
    data = routing_intelligence._read_data()  # Local read-only analytics helper.
    summary = routing_intelligence._get_current_summary(data)
    feedback = data.get("feedback_log", [])
    decisions = data.get("routing_decisions", [])
    by_id = {item.get("routing_id"): item for item in decisions}
    negative = [item for item in feedback if item.get("rating") == "negative"]
    underperforming = []
    for item in negative[-5:]:
        decision = by_id.get(item.get("routing_id"), {})
        underperforming.append(
            {
                "workflow": decision.get("workflow_used", ""),
                "correction": item.get("correction", ""),
                "notes": item.get("notes", ""),
            }
        )

    total_feedback = int(summary.get("total_feedback", 0) or 0)
    positive = int(summary.get("positive_count", 0) or 0)
    total_routings = int(summary.get("total_routings", 0) or len(decisions))
    ensemble = int(summary.get("ensemble_count", 0) or 0)

    return {
        "total_routings": total_routings,
        "total_feedback": total_feedback,
        "positive_rate": round((positive / total_feedback) * 100) if total_feedback else 0,
        "negative_count": int(summary.get("negative_count", 0) or len(negative)),
        "ensemble_rate": round((ensemble / total_routings) * 100) if total_routings else 0,
        "underperforming": underperforming,
    }


def plugin_summary() -> dict[str, Any]:
    route_counts = plugin_readiness_audit.routing_counts()
    scores = [plugin_readiness_audit.score_candidate(name, route_counts) for name in OPERATOR_CORE_CANDIDATES]
    return {
        "average": round(sum(score.total for score in scores) / len(scores), 1) if scores else 0,
        "package_now": [score.name for score in scores if score.total >= 80],
        "improve_first": [score.name for score in scores if 65 <= score.total < 80],
        "keep_as_workflow": [score.name for score in scores if 45 <= score.total < 65],
        "scores": {score.name: score.total for score in scores},
    }


def next_sequence(status: dict[str, Any], proof: dict[str, Any], routing: dict[str, Any]) -> dict[str, Any]:
    broken = status["summary"].get("broken", [])
    stale = status["summary"].get("stale", [])
    if proof["summary"]["status"] == "FAIL" or broken:
        use_now = "Run Operator Cockpit V2 for the raw request, then /system-audit against the failing fast-proof check before building more capability."
        harden = "Repair the failed verifier, then rerun `python3 execution/operator_core_fast_proof.py --strict`."
        expand = "Do not expand until the fast proof is PASS or STALE-with-no-failures."
    elif stale:
        use_now = "Use `python3 execution/operator_cockpit.py --intent '[raw request]' --plain` before meaningful work; use Savant Control Room for status-only reads."
        harden = "Refresh stale anchors only when they block the chosen route; do not treat stale Mission absence as breakage."
        expand = "Build the Excellence Evaluation Lab after one clean fast-proof pass."
    elif routing.get("ensemble_rate", 0) == 0:
        use_now = "Keep using the Control Room and collect one more routing sample before changing routers."
        harden = "Add golden-task regression tests before activating more dormant experts."
        expand = "Prototype controlled ensemble activation through /expert-composition-governor."
    else:
        use_now = "Proceed with the next highest-leverage roadmap item from the Control Room."
        harden = "Compare fast-proof and full control-plane verification after every harness mutation."
        expand = "Package stable Operator Core routes only after repeated fresh-thread proof."

    return {
        "use_now": use_now,
        "harden": harden,
        "expand": expand,
    }


def build_control_room() -> dict[str, Any]:
    status = harness_status.build_status()
    proof = build_proof()
    graph = capability_graph.build_graph()
    routing = routing_summary()
    plugins = plugin_summary()
    sequence = next_sequence(status, proof, routing)

    return {
        "summary": {
            "generated_at": now_iso(),
            "overall": proof["summary"]["status"],
            "safe_to_use": proof["summary"]["safe_to_use"],
            "harness_status": status["summary"]["status"].upper(),
            "broken": status["summary"].get("broken", []),
            "stale": status["summary"].get("stale", []),
            "next_move": status["summary"].get("next_move", ""),
        },
        "fast_proof": proof["summary"],
        "harness": status,
        "routing_intelligence": routing,
        "capability_graph": graph["summary"],
        "plugin_readiness": plugins,
        "recommended_sequence": sequence,
        "boundaries": {
            "mission": "read_only_unless_explicitly_approved",
            "global_mirror": "requires_explicit_approval",
            "external_writes": "not_allowed",
            "real_subagents": "requires_explicit_authorization",
        },
    }


def render_plain(room: dict[str, Any]) -> str:
    summary = room["summary"]
    routing = room["routing_intelligence"]
    plugins = room["plugin_readiness"]
    sequence = room["recommended_sequence"]
    proof = room["fast_proof"]

    lines = [
        "# Savant Control Room",
        "",
        f"Overall: {summary['overall']}",
        f"Safe to use: {'yes' if summary['safe_to_use'] else 'no'}",
        f"Harness: {summary['harness_status']}",
        f"Generated: {summary['generated_at']}",
        f"Broken: {', '.join(summary['broken']) or 'none'}",
        f"Stale: {', '.join(summary['stale']) or 'none'}",
        f"Recorded next move: {summary['next_move'] or 'none'}",
        "",
        "## Fast Proof",
        f"- Checks: {proof['checks']} total; {proof['failures']} failing; {proof['stale']} stale",
        f"- Safe to use: {'yes' if proof['safe_to_use'] else 'no'}",
        "",
        "## Routing Intelligence",
        f"- Routings: {routing['total_routings']}",
        f"- Feedback: {routing['total_feedback']} ({routing['positive_rate']}% positive)",
        f"- Ensemble rate: {routing['ensemble_rate']}%",
        f"- Negative feedback: {routing['negative_count']}",
        "",
        "## Capability And Packaging",
        f"- Workflows indexed: {room['capability_graph']['workflow_count']}",
        f"- Outcome recipes: {room['capability_graph']['recipe_count']}",
        f"- Operator Core bundle average: {plugins['average']}/100",
        f"- Package-now candidates: {', '.join('/' + item for item in plugins['package_now']) or 'none'}",
        f"- Keep as workflow: {', '.join('/' + item for item in plugins['keep_as_workflow']) or 'none'}",
        "",
        "## Recommended Sequence",
        f"- Use Now: {sequence['use_now']}",
        f"- Harden: {sequence['harden']}",
        f"- Expand: {sequence['expand']}",
        "",
        "## Boundaries",
        "- Mission: read-only unless explicitly approved",
        "- Global mirror: requires explicit approval",
        "- External writes: not allowed",
        "- Real subagents: require explicit authorization",
    ]

    if routing["underperforming"]:
        lines.extend(["", "## Latest Underperforming Routes"])
        for item in routing["underperforming"]:
            workflow = item.get("workflow") or "unknown"
            correction = item.get("correction") or "none"
            lines.append(f"- /{workflow} -> correction: /{correction}")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Show the Savant Control Room cockpit.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument("--plain", action="store_true", help="Print readable cockpit output.")
    args = parser.parse_args()

    room = build_control_room()
    if args.json:
        print(json.dumps(room, indent=2, sort_keys=True))
    else:
        print(render_plain(room))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
