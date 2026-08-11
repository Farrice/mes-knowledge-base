#!/usr/bin/env python3
"""Verify /end-session automatic intelligence capture."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
FIXTURES = ROOT / "execution" / "fixtures" / "end_session_intelligence"


def run(args: list[str], cwd: Path = ROOT) -> str:
    completed = subprocess.run(
        args,
        cwd=cwd,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if completed.returncode != 0:
        raise AssertionError(f"Command failed: {' '.join(args)}\n{completed.stdout}")
    return completed.stdout


def read_json(path: Path) -> dict:
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.strip():
            rows.append(json.loads(line))
    return rows


def base_args(tmp: Path, state: str) -> list[str]:
    return [
        "--state-file",
        str(FIXTURES / state),
        "--autopilot-state-file",
        str(FIXTURES / "autopilot-state.md"),
        "--routing-data-file",
        str(tmp / "routing-intelligence.json"),
        "--feedback-inbox",
        str(tmp / "routing-feedback-inbox.jsonl"),
        "--report-dir",
        str(tmp / "reports"),
        "--skip-registrar",
        "--skip-snapshots",
        "--guard-file",
        str(tmp / "closeout-intelligence-guard.jsonl"),
    ]


def check_workflow_wiring() -> str:
    # Closeout side-effects live in the deterministic spine
    # (execution/end_session_closeout.py), not workflow prose (End-Session
    # Closeout Spine decision). The workflow must invoke the spine; the spine
    # must wire intelligence capture; the capture script must keep the
    # routing-feedback inbox default. Pins are script paths, not sentences.
    workflow = (ROOT / ".agent" / "workflows" / "end-session.md").read_text(encoding="utf-8")
    required = [
        "end_session_closeout.py run",
        "session_closeout_intelligence.py run --source end-session",
        "conversation_index.py stats",
        "codex_end_session.py run --manifest",
        "--handoff \"<exact-stored-handoff-path>\"",
    ]
    missing = [item for item in required if item not in workflow]
    if missing:
        raise AssertionError("end-session workflow missing: " + ", ".join(missing))
    spine = (ROOT / "execution" / "end_session_closeout.py").read_text(encoding="utf-8")
    if "session_closeout_intelligence.py" not in spine:
        raise AssertionError("closeout spine does not invoke session_closeout_intelligence.py")
    intelligence = (ROOT / "execution" / "session_closeout_intelligence.py").read_text(encoding="utf-8")
    if "routing-feedback-inbox.jsonl" not in intelligence:
        raise AssertionError("session_closeout_intelligence.py lost the routing-feedback-inbox.jsonl default")
    if "conversation_index.py update <current-conversation-id>" in workflow:
        raise AssertionError("end-session still uses fragile targeted conversation index update")
    return "workflow wiring (closeout spine)"


def check_scan_and_dry_run(tmp: Path) -> str:
    scan = run([
        sys.executable,
        "execution/session_closeout_intelligence.py",
        "scan",
        *base_args(tmp, "success-session-state.md"),
    ])
    if "/autopilot" not in scan or "/system-audit" not in scan:
        raise AssertionError(f"scan did not find expected route candidates:\n{scan}")

    dry = run([
        sys.executable,
        "execution/session_closeout_intelligence.py",
        "run",
        *base_args(tmp, "success-session-state.md"),
        "--dry-run",
    ])
    if "would-commit" not in dry or "Report would be written" not in dry:
        raise AssertionError(f"dry-run did not show write plan:\n{dry}")
    if (tmp / "routing-intelligence.json").exists():
        raise AssertionError("dry-run wrote routing data")
    return "scan and dry-run"


def check_missing_optional_autopilot(tmp: Path) -> str:
    degradation_log = ROOT / ".agent" / "health" / "degradations.jsonl"
    before = degradation_log.read_bytes() if degradation_log.exists() else b""
    args = base_args(tmp, "success-session-state.md")
    marker = args.index("--autopilot-state-file")
    args[marker + 1] = str(tmp / "missing-autopilot-state.md")
    scan = run([
        sys.executable,
        "execution/session_closeout_intelligence.py",
        "scan",
        *args,
    ])
    after = degradation_log.read_bytes() if degradation_log.exists() else b""
    if "/autopilot" not in scan or before != after:
        raise AssertionError("missing optional autopilot state degraded or changed closeout scanning")
    return "missing optional autopilot state stays quiet"


def check_duplicate_protection(tmp: Path) -> str:
    command = [
        sys.executable,
        "execution/session_closeout_intelligence.py",
        "run",
        *base_args(tmp, "success-session-state.md"),
    ]
    run(command)
    run(command)
    data = read_json(tmp / "routing-intelligence.json")
    decisions = data.get("routing_decisions", [])
    feedback = data.get("feedback_log", [])
    if len(decisions) != 2:
        raise AssertionError(f"expected 2 routing decisions after duplicate run, got {len(decisions)}")
    if len(feedback) != 2:
        raise AssertionError(f"expected 2 positive feedback entries after duplicate run, got {len(feedback)}")
    return "duplicate protection"


def check_explicit_misroute(tmp: Path) -> str:
    run([
        sys.executable,
        "execution/session_closeout_intelligence.py",
        "run",
        *base_args(tmp, "misroute-session-state.md"),
    ])
    data = read_json(tmp / "routing-intelligence.json")
    feedback = data.get("feedback_log", [])
    if not feedback:
        raise AssertionError("explicit misroute did not create feedback")
    latest = feedback[-1]
    if latest.get("rating") != "negative" or latest.get("correction") != "first-10k":
        raise AssertionError(f"misroute feedback incorrect: {latest}")
    return "explicit misroute feedback"


def check_ambiguous_inbox(tmp: Path) -> str:
    run([
        sys.executable,
        "execution/session_closeout_intelligence.py",
        "run",
        *base_args(tmp, "ambiguous-session-state.md"),
    ])
    inbox = read_jsonl(tmp / "routing-feedback-inbox.jsonl")
    data = read_json(tmp / "routing-intelligence.json")
    if not inbox:
        raise AssertionError("ambiguous failure signal did not create inbox item")
    if data.get("feedback_log"):
        raise AssertionError("ambiguous failure signal should not commit routing feedback")
    return "ambiguous feedback inbox"


def check_meta_language_not_inboxed(tmp: Path) -> str:
    run([
        sys.executable,
        "execution/session_closeout_intelligence.py",
        "run",
        *base_args(tmp, "meta-session-state.md"),
    ])
    inbox = read_jsonl(tmp / "routing-feedback-inbox.jsonl")
    if inbox:
        raise AssertionError(f"meta implementation language should not create inbox items: {inbox}")
    return "meta language ignored"


def check_status(tmp: Path) -> str:
    status = run([
        sys.executable,
        "execution/session_closeout_intelligence.py",
        "status",
        "--routing-data-file",
        str(tmp / "routing-intelligence.json"),
        "--feedback-inbox",
        str(tmp / "routing-feedback-inbox.jsonl"),
        "--report-dir",
        str(tmp / "reports"),
    ])
    if "Routing decisions:" not in status or "Routing feedback inbox:" not in status:
        raise AssertionError(f"status missing expected counts:\n{status}")
    return "status surface"


def check_no_prune(tmp: Path) -> str:
    report_dir = tmp / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    originals = []
    for index in range(12):
        path = report_dir / f"2026-07-{index + 1:02d}T000000-session-closeout-intelligence.md"
        path.write_text(f"report {index}\n", encoding="utf-8")
        originals.append(path)
    run([
        sys.executable,
        "execution/session_closeout_intelligence.py",
        "run",
        *base_args(tmp, "success-session-state.md"),
        "--no-prune",
    ])
    missing = [path.name for path in originals if not path.exists()]
    if missing or (report_dir / "archive").exists():
        raise AssertionError(f"--no-prune moved existing reports: {missing}")
    return "manifest-scoped no-prune retention"


def main() -> int:
    checks = [check_workflow_wiring()]
    with tempfile.TemporaryDirectory() as temp:
        tmp = Path(temp)
        checks.append(check_scan_and_dry_run(tmp / "dry"))
        checks.append(check_missing_optional_autopilot(tmp / "optional"))
        checks.append(check_duplicate_protection(tmp / "dupes"))
        checks.append(check_explicit_misroute(tmp / "misroute"))
        checks.append(check_ambiguous_inbox(tmp / "ambiguous"))
        checks.append(check_meta_language_not_inboxed(tmp / "meta"))
        checks.append(check_status(tmp / "ambiguous"))
        checks.append(check_no_prune(tmp / "no-prune"))

    print("END SESSION INTELLIGENCE VERIFICATION PASS")
    for check in checks:
        print(f"- ok: {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
