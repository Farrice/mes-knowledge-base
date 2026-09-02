#!/usr/bin/env python3
"""Deterministic verification for bulk_closeout_control.py."""
from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "execution" / "bulk_closeout_control.py"


def invoke(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, str(SCRIPT), *args],
        cwd=str(ROOT),
        text=True,
        capture_output=True,
    )


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def parse(result: subprocess.CompletedProcess[str]) -> dict:
    return json.loads(result.stdout)


def main() -> int:
    ready = invoke("interpret", "close ready")
    require(ready.returncode == 0, ready.stderr)
    ready_data = parse(ready)
    require(ready_data["requested_status"] == "ready", "close ready status drift")
    require(ready_data["archive"] is False, "close ready must never archive")
    require(ready_data["merge_main"] is False, "close ready must never merge main")

    done = invoke("interpret", "close done")
    require(done.returncode == 0, done.stderr)
    done_data = parse(done)
    require(done_data["require_integration_proof"] is True, "close done lost integration proof")
    require(done_data["archive"] == "only when task_actions.archive is true", "close done archive gate drift")
    require(done_data["fail_closed_status"] != "done", "close done must fail closed")

    audit = invoke("interpret", "bulk closeout audit")
    require(audit.returncode == 0, audit.stderr)
    audit_data = parse(audit)
    require(audit_data["read_only"] is True, "bulk audit must be read-only")
    for key in ("messages", "commits", "merges", "pushes", "archives", "deletions"):
        require(audit_data[key] == 0, f"bulk audit side effect drift: {key}")

    for raw in ("ready", "done", "close everything", "close ready and merge main"):
        rejected = invoke("interpret", raw)
        require(rejected.returncode == 2, f"unsafe phrase accepted: {raw}")
        require(parse(rejected)["recognized"] is False, f"unsafe phrase recognized: {raw}")

    with tempfile.TemporaryDirectory(prefix="bulk-closeout-verify-") as raw:
        tmp = Path(raw)
        snapshot = {
            "schema_version": "codex-task-snapshot/v1",
            "tasks": [{
                "id": "task-1",
                "title": "System: Bulk Closeout Control - Verified",
                "cwd": str(ROOT),
                "summary": "fixture remains intentionally unmatched",
                "branch_mentions": [],
                "status_mentions": [],
                "end_session_invoked": False,
                "closeout_receipt_seen": False,
            }],
        }
        snapshot_path = tmp / "tasks.json"
        snapshot_path.write_text(json.dumps(snapshot), encoding="utf-8")
        audit_path = tmp / "audit.json"
        report_path = tmp / "audit.md"
        result = invoke(
            "audit", "--tasks", str(snapshot_path), "--main", str(ROOT),
            "--output-json", str(audit_path), "--output-md", str(report_path),
        )
        require(result.returncode == 0, result.stderr)
        payload = json.loads(audit_path.read_text(encoding="utf-8"))
        require(payload["schema_version"] == "bulk-closeout-audit/v1", "audit schema drift")
        require(payload["safety"]["archives"] == 0, "audit claims archive side effect")
        require(report_path.exists(), "markdown report missing")
        report = report_path.read_text(encoding="utf-8")
        require("Bare `ready` and `done`" in report, "report lost bare-word safety rule")

    print("BULK CLOSEOUT CONTROL VERIFICATION PASS")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except AssertionError as exc:
        print(f"BULK CLOSEOUT CONTROL VERIFICATION FAIL\n- {exc}")
        raise SystemExit(1)
