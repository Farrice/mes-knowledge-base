#!/usr/bin/env python3
"""Verify Activation Governor scan, dry-run, approval, and safety behavior."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


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


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def check_scan_and_dry_run(tmp: Path) -> str:
    queue = tmp / "queue.jsonl"
    reports = tmp / "reports"
    scan = run([
        sys.executable,
        "execution/activation_governor.py",
        "scan",
        "--queue-path",
        str(queue),
        "--report-dir",
        str(reports),
    ])
    if "No files were written." not in scan or "Local Signals" not in scan:
        raise AssertionError(f"scan output missing read-only proof:\n{scan}")
    if queue.exists() or reports.exists():
        raise AssertionError("scan wrote queue/report outputs")

    dry = run([
        sys.executable,
        "execution/activation_governor.py",
        "plan",
        "--dry-run",
        "--queue-path",
        str(queue),
        "--report-dir",
        str(reports),
    ])
    if "Queue would be appended" not in dry or "Report would be written" not in dry:
        raise AssertionError(f"plan dry-run did not show write plan:\n{dry}")
    if queue.exists() or reports.exists():
        raise AssertionError("plan --dry-run wrote queue/report outputs")
    return "scan and plan dry-run are read-only"


def check_plan_write_and_apply(tmp: Path) -> str:
    queue = tmp / "queue.jsonl"
    applied = tmp / "applied.jsonl"
    reports = tmp / "reports"
    run([
        sys.executable,
        "execution/activation_governor.py",
        "plan",
        "--queue-path",
        str(queue),
        "--report-dir",
        str(reports),
    ])
    rows = read_jsonl(queue)
    if not rows:
        rows = [{
            "id": "ag_test_fixture",
            "priority": "LOW",
            "title": "Fixture approval handoff",
            "source": "verify_activation_governor",
            "signal": "fixture",
            "evidence": "no live queue items were generated",
            "proposed_action": "Record a fixture handoff only. Do not activate anything.",
            "risk": "low",
            "approval_required": True,
            "status": "queued",
        }]
        queue.write_text(json.dumps(rows[0], sort_keys=True) + "\n", encoding="utf-8")

    approval_id = rows[0]["id"]
    dry = run([
        sys.executable,
        "execution/activation_governor.py",
        "apply-approved",
        "--dry-run",
        "--approval-id",
        approval_id,
        "--queue-path",
        str(queue),
        "--applied-path",
        str(applied),
        "--report-dir",
        str(reports),
    ])
    if "would-apply" not in dry or "No protocols, agents, routing logs, or performance entries" not in dry:
        raise AssertionError(f"apply-approved dry-run missing safety boundary:\n{dry}")
    if applied.exists():
        raise AssertionError("apply-approved --dry-run wrote applied log")

    write = run([
        sys.executable,
        "execution/activation_governor.py",
        "apply-approved",
        "--approval-id",
        approval_id,
        "--queue-path",
        str(queue),
        "--applied-path",
        str(applied),
        "--report-dir",
        str(reports),
    ])
    if "applied" not in write:
        raise AssertionError(f"apply-approved did not record approved handoff:\n{write}")
    applied_rows = read_jsonl(applied)
    if not applied_rows or applied_rows[0].get("id") != approval_id:
        raise AssertionError("approved handoff log missing expected ID")
    return "plan write and apply-approved handoff"


def check_verify_mode(tmp: Path) -> str:
    verify = run([
        sys.executable,
        "execution/activation_governor.py",
        "verify",
        "--queue-path",
        str(tmp / "queue.jsonl"),
        "--report-dir",
        str(tmp / "reports"),
    ])
    if "ACTIVATION GOVERNOR VERIFICATION PASS" not in verify:
        raise AssertionError(f"verify mode did not pass:\n{verify}")
    return "verify mode"


def main() -> int:
    with tempfile.TemporaryDirectory() as temp:
        tmp = Path(temp)
        checks = [
            check_scan_and_dry_run(tmp / "dry"),
            check_plan_write_and_apply(tmp / "write"),
            check_verify_mode(tmp / "verify"),
        ]
    print("ACTIVATION GOVERNOR CLI VERIFICATION PASS")
    for check in checks:
        print(f"- ok: {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
