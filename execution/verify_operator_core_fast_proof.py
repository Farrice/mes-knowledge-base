#!/usr/bin/env python3
"""Verify the fast Operator Core proof layer."""

from __future__ import annotations

import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

import harness_status  # type: ignore  # noqa: E402


ROOT = Path(__file__).resolve().parent.parent


def run(args: list[str]) -> str:
    completed = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if completed.returncode != 0:
        raise AssertionError(f"Command failed: {' '.join(args)}\n{completed.stdout}")
    return completed.stdout


def main() -> int:
    stale_working, stale_findings = harness_status.current_state_findings(
        {"updated_at": "2000-01-01T00:00:00+00:00"},
        {"updated_at": "2000-01-01T00:00:00+00:00"},
        {"slug": "finished-example", "status": "complete"},
    )
    if stale_working or len(stale_findings) != 3:
        raise AssertionError(f"stale-state negative control failed: {stale_working}, {stale_findings}")

    fresh = datetime.now(timezone.utc).isoformat()
    fresh_working, fresh_stale = harness_status.current_state_findings(
        {"updated_at": fresh},
        {"updated_at": fresh},
        {"slug": "active-example", "status": "active"},
    )
    if fresh_stale or len(fresh_working) != 3:
        raise AssertionError(f"fresh-state control failed: {fresh_working}, {fresh_stale}")

    raw = run([sys.executable, "execution/operator_core_fast_proof.py", "--json", "--strict"])
    data = json.loads(raw)
    if data["summary"]["status"] not in {"PASS", "STALE"}:
        raise AssertionError(f"fast proof status was {data['summary']['status']}")
    if not data["summary"]["safe_to_use"]:
        raise AssertionError("fast proof says the harness is not safe to use")
    names = {check["name"] for check in data["checks"]}
    required = {
        "harness_has_no_broken_items",
        "routing_probes",
        "live_surface_strict",
        "run_receipt_schema",
        "ai_employee_os_operator_core",
        "friction_ledger_readable",
    }
    missing = required - names
    if missing:
        raise AssertionError(f"fast proof missing checks: {sorted(missing)}")
    if any(check["status"] == "FAIL" for check in data["checks"]):
        raise AssertionError(f"fast proof has failures: {data['checks']}")

    plain = run([sys.executable, "execution/operator_core_fast_proof.py", "--plain"])
    for snippet in (
        "# Operator Core Fast Proof",
        "Safe to use: yes",
        "ai_employee_os_operator_core",
        "Global mirror: requires explicit approval",
    ):
        if snippet not in plain:
            raise AssertionError(f"plain fast proof missing: {snippet}")

    print("OPERATOR CORE FAST PROOF VERIFICATION PASS")
    print("- fast proof JSON is parseable")
    print("- all required proof checks are present")
    print("- no failing fast-proof checks")
    print("- stale intent and completed-mission controls cannot report fresh")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
