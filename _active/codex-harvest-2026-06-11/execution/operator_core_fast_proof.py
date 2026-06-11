#!/usr/bin/env python3
"""Fast read-only proof layer for daily Operator Core confidence."""

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

import codex_live_surface_audit  # type: ignore  # noqa: E402
import friction_ledger  # type: ignore  # noqa: E402
import harness_status  # type: ignore  # noqa: E402
import run_receipt  # type: ignore  # noqa: E402
from verify_operator_core_ai_employee_os import inspect_ai_employee_os  # noqa: E402


def now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat()


def pass_fail(name: str, passed: bool, detail: str, stale: bool = False) -> dict[str, Any]:
    if not passed:
        status = "FAIL"
    elif stale:
        status = "STALE"
    else:
        status = "PASS"
    return {"name": name, "status": status, "detail": detail}


def build_proof() -> dict[str, Any]:
    status = harness_status.build_status()
    live_surface = codex_live_surface_audit.build_report()
    live_failures = codex_live_surface_audit.strict_failures(live_surface)
    ai_employee = inspect_ai_employee_os(run_skill_validation=False)
    friction = friction_ledger.summarize(friction_ledger.read_events())

    receipt_ok = True
    receipt_detail = "latest receipt schema ok"
    try:
        run_receipt.verify()
    except Exception as exc:  # pragma: no cover - defensive CLI surface
        receipt_ok = False
        receipt_detail = str(exc)

    routing_pass = all(item["pass"] for item in status["routing_health"].values())
    stale_items = status["summary"].get("stale", [])
    broken_items = status["summary"].get("broken", [])

    checks = [
        pass_fail(
            "harness_has_no_broken_items",
            not broken_items,
            ", ".join(broken_items) if broken_items else "no broken harness items",
            stale=bool(stale_items),
        ),
        pass_fail(
            "routing_probes",
            routing_pass,
            "all routing probes pass" if routing_pass else "one or more routing probes failed",
        ),
        pass_fail(
            "live_surface_strict",
            not live_failures,
            "strict live surface clean" if not live_failures else "; ".join(live_failures),
        ),
        pass_fail("run_receipt_schema", receipt_ok, receipt_detail),
        pass_fail(
            "ai_employee_os_operator_core",
            ai_employee["summary"]["status"] == "PASS",
            f"{ai_employee['summary']['checks']} local checks; {ai_employee['summary']['failures']} failing",
        ),
        pass_fail(
            "friction_ledger_readable",
            isinstance(friction.get("events"), int),
            f"{friction.get('events', 0)} recorded friction events",
        ),
    ]

    failures = [check for check in checks if check["status"] == "FAIL"]
    stale = [check for check in checks if check["status"] == "STALE"]
    overall = "FAIL" if failures else "STALE" if stale else "PASS"

    return {
        "summary": {
            "status": overall,
            "generated_at": now_iso(),
            "checks": len(checks),
            "failures": len(failures),
            "stale": len(stale),
            "safe_to_use": not failures,
            "next_move": status["summary"].get("next_move", ""),
        },
        "checks": checks,
        "harness_summary": status["summary"],
        "latest_run_receipt": status["latest_run_receipt"],
        "friction_ledger": friction,
        "ai_employee_os": ai_employee["summary"],
        "boundary": {
            "mission_mutation": "not_allowed",
            "global_mirror": "requires_explicit_approval",
            "external_writes": "not_allowed",
            "real_subagents": "requires_explicit_authorization",
        },
    }


def render_plain(proof: dict[str, Any]) -> str:
    summary = proof["summary"]
    lines = [
        "# Operator Core Fast Proof",
        "",
        f"Overall: {summary['status']}",
        f"Safe to use: {'yes' if summary['safe_to_use'] else 'no'}",
        f"Generated: {summary['generated_at']}",
        f"Checks: {summary['checks']} total; {summary['failures']} failing; {summary['stale']} stale",
        f"Next move: {summary['next_move'] or 'none recorded'}",
        "",
        "## Checks",
    ]
    for check in proof["checks"]:
        lines.append(f"- {check['status']}: {check['name']} - {check['detail']}")
    lines.extend(
        [
            "",
            "## Boundaries",
            "- Mission mutation: not allowed",
            "- Global mirror: requires explicit approval",
            "- External writes: not allowed",
            "- Real subagents: require explicit authorization",
        ]
    )
    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the fast Operator Core proof layer.")
    parser.add_argument("--json", action="store_true", help="Print machine-readable JSON.")
    parser.add_argument("--plain", action="store_true", help="Print readable proof output.")
    parser.add_argument("--strict", action="store_true", help="Exit nonzero when the proof fails.")
    args = parser.parse_args()

    proof = build_proof()
    if args.json:
        print(json.dumps(proof, indent=2, sort_keys=True))
    else:
        print(render_plain(proof))
    return 1 if args.strict and proof["summary"]["status"] == "FAIL" else 0


if __name__ == "__main__":
    raise SystemExit(main())
