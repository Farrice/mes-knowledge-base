#!/usr/bin/env python3
"""Verify protocol lifecycle classification does not fake activations."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import protocol_tracker  # type: ignore  # noqa: E402


def check_report_shape() -> str:
    report = protocol_tracker.audit_protocols()
    required = {
        "active_protocols",
        "healthy_protocols",
        "dormant_protocols",
        "cold_source_only_protocols",
        "overdue_protocols",
        "deprecated_protocols",
        "lifecycle_counts",
    }
    missing = sorted(required - set(report))
    if missing:
        raise AssertionError("missing lifecycle fields: " + ", ".join(missing))

    total = report["total_protocols"]
    counted = sum(report["lifecycle_counts"].values())
    if counted != total:
        raise AssertionError(f"lifecycle counts do not sum to total: {counted} != {total}")
    return f"lifecycle fields present ({total} protocols)"


def check_never_activated_not_zombie() -> str:
    report = protocol_tracker.audit_protocols()
    bad = [
        row["file"]
        for row in report["protocols"]
        if row.get("never_activated") and row.get("is_zombie")
    ]
    if bad:
        raise AssertionError("never-activated protocols still marked zombie: " + ", ".join(bad[:10]))
    never = [row for row in report["protocols"] if row.get("never_activated")]
    if not never:
        raise AssertionError("expected at least one never-activated protocol fixture in live directives")
    allowed = {"dormant", "cold/source-only", "deprecated"}
    wrong = [row["file"] for row in never if row.get("lifecycle") not in allowed]
    if wrong:
        raise AssertionError("never-activated protocols have wrong lifecycle: " + ", ".join(wrong[:10]))
    return f"never-activated classified without zombie state ({len(never)} protocols)"


def check_overdue_semantics() -> str:
    report = protocol_tracker.audit_protocols()
    overdue = [row for row in report["protocols"] if row.get("lifecycle") == "overdue"]
    stale_never = [row for row in overdue if row.get("never_activated")]
    if stale_never:
        raise AssertionError("overdue includes never-activated protocols: " + ", ".join(row["file"] for row in stale_never[:10]))
    if report["zombie_protocols"] != report["overdue_protocols"]:
        raise AssertionError("backward-compatible zombie count should equal overdue count")
    return f"overdue means activated and review-late ({len(overdue)} protocols)"


def check_cli_output() -> str:
    result = subprocess.run(
        [sys.executable, "execution/protocol_tracker.py", "audit"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(result.stdout)
    required = ["Active Recent", "Cold/Source-Only", "Overdue", "DORMANT"]
    missing = [term for term in required if term not in result.stdout]
    if missing:
        raise AssertionError("CLI output missing lifecycle terms: " + ", ".join(missing))
    if "ZOMBIES" in result.stdout:
        raise AssertionError("CLI still presents zombie bucket language")
    return "CLI lifecycle output"


def main() -> int:
    checks = [
        check_report_shape(),
        check_never_activated_not_zombie(),
        check_overdue_semantics(),
        check_cli_output(),
    ]
    print("PROTOCOL LIFECYCLE VERIFICATION PASS")
    for check in checks:
        print(f"- ok: {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
