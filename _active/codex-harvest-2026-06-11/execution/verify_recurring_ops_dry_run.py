#!/usr/bin/env python3
"""Verify recurring_ops dry-run mode does not write local ops artifacts."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
REPORT_DIR = ROOT / ".agent" / "recurring-reports"
GOVERNOR_QUEUE = ROOT / ".agent" / "system-governor-queue.md"
ROUTING_LOG = ROOT / ".agent" / "routing-intelligence.json"


def snapshot() -> dict[str, object]:
    reports = sorted(str(path.relative_to(ROOT)) for path in REPORT_DIR.glob("*.md")) if REPORT_DIR.exists() else []
    return {
        "reports": reports,
        "queue_exists": GOVERNOR_QUEUE.exists(),
        "queue_size": GOVERNOR_QUEUE.stat().st_size if GOVERNOR_QUEUE.exists() else 0,
        "routing_exists": ROUTING_LOG.exists(),
        "routing_size": ROUTING_LOG.stat().st_size if ROUTING_LOG.exists() else 0,
    }


def run_case(args: list[str], expected_text: str) -> str:
    result = subprocess.run(
        [sys.executable, "execution/recurring_ops.py", *args],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        timeout=180,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(f"recurring_ops {' '.join(args)} failed:\n{result.stdout}")
    if expected_text not in result.stdout:
        raise AssertionError(f"recurring_ops {' '.join(args)} missing {expected_text!r}")
    return result.stdout


def assert_unchanged(before: dict[str, object], after: dict[str, object], label: str) -> None:
    if before != after:
        raise AssertionError(f"{label} changed dry-run artifacts:\nbefore={before}\nafter={after}")


def main() -> int:
    before = snapshot()
    run_case(["--dry-run", "monthly-hygiene-review"], "Report would be written")
    after_monthly = snapshot()
    assert_unchanged(before, after_monthly, "top-level monthly dry-run")

    run_case(["system-governor", "--dry-run"], "Queue would be appended")
    after_governor = snapshot()
    assert_unchanged(after_monthly, after_governor, "subcommand system-governor dry-run")

    print("Recurring ops dry-run verification: PASS")
    print("- top-level --dry-run created no recurring report")
    print("- subcommand --dry-run appended no governor queue entry")
    print("- routing log size was unchanged")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

