#!/usr/bin/env python3
"""Verify the Performance Evidence gate fails closed."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import performance_evidence_audit as gate  # type: ignore  # noqa: E402


def write_jsonl(path: Path, rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(row) + "\n" for row in rows), encoding="utf-8")


def check_synthetic_gate(tmp: Path) -> str:
    tmp.mkdir(parents=True, exist_ok=True)
    proof = tmp / "proof.md"
    proof.write_text("Implemented verifier-backed repair. Validation passed.", encoding="utf-8")
    rows = [
        {
            "draft_id": "draft_promotable",
            "title": "Protocol lifecycle classifier repair",
            "workflow": "protocol-lifecycle",
            "quality_score": 8.5,
            "intent_alignment": 9,
            "expert_standard": 8,
            "adversarial_resilience": 8,
            "notes": "Implemented lifecycle buckets and verifier passed.",
            "source_artifact": str(proof),
        },
        {
            "draft_id": "draft_needs_rating",
            "title": "Tiered routing verifier",
            "workflow": "tiered-agent-routing",
            "notes": "Implemented routing verifier and proof passed.",
            "source_artifact": str(proof),
        },
        {
            "draft_id": "draft_closeout",
            "title": "Session Closeout Intelligence",
            "workflow": "autopilot",
            "quality_score": None,
            "notes": "Recurring report wrapper.",
            "source_artifact": ".agent/recurring-reports/example.md",
        },
        {
            "draft_id": "draft_no_proof",
            "title": "Mystery repair",
            "workflow": "unknown",
            "quality_score": 9,
            "intent_alignment": 9,
            "expert_standard": 9,
            "adversarial_resilience": 9,
            "notes": "Implemented something.",
            "source_artifact": str(tmp / "missing.md"),
        },
    ]
    verdicts = gate.audit_rows(rows, [], root=ROOT)
    by_id = {verdict.draft_id: verdict.classification for verdict in verdicts}
    expected = {
        "draft_promotable": gate.PROMOTABLE,
        "draft_needs_rating": gate.NEEDS_HUMAN_RATING,
        "draft_closeout": gate.DUPLICATE_CLOSEOUT_ONLY,
        "draft_no_proof": gate.INSUFFICIENT_PROOF,
    }
    if by_id != expected:
        raise AssertionError(f"unexpected synthetic classifications: {by_id}")
    return "synthetic classifications"


def check_live_inbox_not_auto_promotable() -> str:
    inbox = gate.read_jsonl(gate.DEFAULT_INBOX)
    committed = gate.read_jsonl(gate.DEFAULT_LOG)
    verdicts = gate.audit_rows(inbox, committed)
    bad = [
        verdict
        for verdict in verdicts
        if verdict.classification == gate.PROMOTABLE
        and verdict.title in {"Session Closeout Intelligence", "Weekly System Pulse", "Activation Governor Plan"}
    ]
    if bad:
        raise AssertionError("closeout/report drafts classified promotable: " + ", ".join(v.draft_id for v in bad))
    if inbox and not verdicts:
        raise AssertionError("live inbox had rows but no verdicts")
    return f"live inbox audited ({len(verdicts)} drafts)"


def check_cli(tmp: Path) -> str:
    tmp.mkdir(parents=True, exist_ok=True)
    proof = tmp / "proof.md"
    proof.write_text("Implemented and verified.", encoding="utf-8")
    inbox = tmp / "inbox.jsonl"
    log = tmp / "performance-log.jsonl"
    write_jsonl(inbox, [{
        "draft_id": "draft_cli",
        "title": "CLI proof repair",
        "workflow": "performance-evidence",
        "quality_score": 8,
        "intent_alignment": 8,
        "expert_standard": 8,
        "adversarial_resilience": 8,
        "notes": "Implemented and verifier passed.",
        "source_artifact": str(proof),
    }])
    write_jsonl(log, [])
    result = subprocess.run(
        [
            sys.executable,
            "execution/performance_evidence_audit.py",
            "--inbox",
            str(inbox),
            "--performance-log",
            str(log),
            "--json",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(result.stdout)
    data = json.loads(result.stdout)
    if data["counts"].get(gate.PROMOTABLE) != 1:
        raise AssertionError(f"CLI did not classify promotable fixture:\n{result.stdout}")
    return "CLI JSON audit"


def check_promote_block(tmp: Path) -> str:
    tmp.mkdir(parents=True, exist_ok=True)
    inbox = tmp / "inbox.jsonl"
    skipped = tmp / "skipped.jsonl"
    write_jsonl(inbox, [{
        "draft_id": "draft_blocked_closeout",
        "title": "Session Closeout Intelligence",
        "workflow": "autopilot",
        "task_type": "System",
        "lane": "System",
        "quality_score": None,
        "intent_alignment": None,
        "expert_standard": None,
        "adversarial_resilience": None,
        "status": "Baseline",
        "notes": "Recurring closeout wrapper.",
        "source_artifact": ".agent/recurring-reports/example.md",
        "registration_source": "end-session",
        "auto_confidence": 0.62,
        "review_state": "inbox",
        "reason": "recurring report needs review before becoming performance evidence",
        "fingerprint": "blocked",
    }])
    script = (
        "import sys; "
        "from pathlib import Path; "
        "sys.path.insert(0, 'execution'); "
        "import session_log_registrar as r; "
        f"r.INBOX_PATH=Path({str(inbox)!r}); "
        f"r.SKIPPED_PATH=Path({str(skipped)!r}); "
        "raise SystemExit(r.main())"
    )
    result = subprocess.run(
        [sys.executable, "-c", script, "promote", "draft_blocked_closeout", "--dry-run"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode == 0 or "Promotion blocked" not in result.stdout:
        raise AssertionError(f"registrar promote did not fail closed:\n{result.stdout}")
    return "registrar promote fails closed"


def main() -> int:
    with tempfile.TemporaryDirectory() as temp:
        tmp = Path(temp)
        checks = [
            check_synthetic_gate(tmp / "synthetic"),
            check_live_inbox_not_auto_promotable(),
            check_cli(tmp / "cli"),
            check_promote_block(tmp / "promote"),
        ]
    print("PERFORMANCE EVIDENCE GATE VERIFICATION PASS")
    for check in checks:
        print(f"- ok: {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
