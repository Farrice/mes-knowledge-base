#!/usr/bin/env python3
"""Verify tiered agent routing coverage."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import routing_audit  # type: ignore  # noqa: E402


def check_tiered_summary() -> str:
    rows, summary = routing_audit.build_tiered_routing_report()
    if summary["total"] != 169:
        raise AssertionError(f"expected 169 agents, got {summary['total']}")
    if summary["legacy_fully_routed"] < 15:
        raise AssertionError("legacy all-layer metric unexpectedly regressed below 15")
    if summary["legacy_unrouted"] < 1:
        raise AssertionError("expected legacy unrouted agents to remain visible")
    if summary["tier_noncompliant"] != 0:
        offenders = [row["slug"] for row in rows if not row["tier_compliant"]]
        raise AssertionError("tiered noncompliant agents: " + ", ".join(offenders[:20]))
    return f"tiered compliant {summary['tier_compliant']}/{summary['total']} with legacy unrouted {summary['legacy_unrouted']}"


def check_control_plane_operators() -> str:
    rows, _ = routing_audit.build_tiered_routing_report()
    by_slug = {row["slug"]: row for row in rows}
    expected_routes = {
        "operator-autopilot": "autopilot",
        "antigravity-orchestrator": "orchestrate",
        "knowledge-librarian": "knowledge-librarian",
        "quality-judge": "quality-judge",
    }
    for slug, route in expected_routes.items():
        row = by_slug.get(slug)
        if not row:
            raise AssertionError(f"missing control-plane operator: {slug}")
        if row["tier"] != "control-plane-operator":
            raise AssertionError(f"{slug} wrong tier: {row['tier']}")
        if row["route"] != route:
            raise AssertionError(f"{slug} wrong route: {row['route']}")
        if not row["tier_compliant"]:
            raise AssertionError(f"{slug} not tier compliant: {row['tier_reason']}")
        if not row["workflow_exists"] or not row["bridge_exists"] or not row["has_routing_interop"]:
            raise AssertionError(f"{slug} lacks full operator route surfaces")
    return "control-plane operators have full route surfaces"


def check_primary_execution_agents() -> str:
    rows, _ = routing_audit.build_tiered_routing_report()
    primary = [row for row in rows if row["tier"] == "primary-execution"]
    if len(primary) != len(routing_audit.PRIMARY_EXECUTION_AGENTS):
        raise AssertionError("primary execution agent count mismatch")
    missing = [
        row["slug"]
        for row in primary
        if not (row["in_registry"] or row["in_cards"])
    ]
    if missing:
        raise AssertionError("primary agents lack registry/card coverage: " + ", ".join(missing))
    return f"primary execution agents covered ({len(primary)})"


def check_cold_source_only_classification() -> str:
    rows, summary = routing_audit.build_tiered_routing_report()
    cold = [row for row in rows if row["tier"] == "cold/source-only"]
    if not cold:
        raise AssertionError("expected some cold/source-only agents")
    bad = [row["slug"] for row in cold if not row["has_routing_interop"]]
    if bad:
        raise AssertionError("cold/source-only without Routing Interop: " + ", ".join(bad))
    if summary["unclassified_cold"] != 0:
        raise AssertionError("unclassified cold agents remain")
    return f"cold/source-only classified ({len(cold)})"


def check_cli_report() -> str:
    result = subprocess.run(
        [sys.executable, "execution/routing_audit.py"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(result.stdout)
    report = ROOT / ".tmp" / "routing-audit.md"
    text = report.read_text(encoding="utf-8")
    required = [
        "Legacy All-Layers Coverage",
        "Tiered Routing Standard",
        "Tiered Coverage Matrix",
        "cold/source-only",
    ]
    missing = [snippet for snippet in required if snippet not in text]
    if missing:
        raise AssertionError("routing report missing: " + ", ".join(missing))
    return "routing_audit CLI writes tiered report"


def main() -> int:
    checks = [
        check_tiered_summary(),
        check_control_plane_operators(),
        check_primary_execution_agents(),
        check_cold_source_only_classification(),
        check_cli_report(),
    ]
    print("TIERED AGENT ROUTING VERIFICATION PASS")
    for check in checks:
        print(f"- ok: {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
