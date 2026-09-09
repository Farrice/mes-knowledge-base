#!/usr/bin/env python3
"""Deterministic verifier for the shared creative-strategy intelligence layer."""

from __future__ import annotations

import json
import importlib.util
import shutil
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import creative_intelligence as ci  # noqa: E402
from review_miner import score_trigger_event  # noqa: E402


REQUIRED = [
    "semantic_libraries/antigravity/primitives/creative-strategy-intelligence-layer.md",
    "execution/creative_intelligence.py",
    "skills/trigger-event-creative-strategy/SKILL.md",
    "skills/trigger-event-creative-strategy/genius.md",
    ".agent/workflows/trigger-event-creative-strategy.md",
    ".agents/skills/source-command-trigger-event-creative-strategy/SKILL.md",
    ".claude/commands/trigger-event-creative-strategy.md",
    "extractions/alex-cooper-compounding-creative-intelligence/skill-system-contract.md",
]


def check(condition: bool, label: str, failures: list[str]) -> None:
    print(f"{'PASS' if condition else 'FAIL'} {label}")
    if not condition:
        failures.append(label)


def main() -> int:
    failures: list[str] = []
    for rel in REQUIRED:
        check((ROOT / rel).exists(), f"required file: {rel}", failures)

    chain = (ROOT / "execution" / "chain_runner.py").read_text(encoding="utf-8")
    review = (ROOT / "execution" / "memory_review.py").read_text(encoding="utf-8")
    revenue = (ROOT / "execution" / "revenue_tracker.py").read_text(encoding="utf-8")
    check("capture_finalize_event" in chain, "Creative/Strategy finalize capture wired", failures)
    check("auto_promotion_allowed" in review, "explicit-review veto survives high score", failures)
    check("attach_outcome_by_deliverable" in revenue, "revenue resolution attaches descriptive evidence", failures)

    claude_hooks = (ROOT / ".claude" / "settings.json").read_text(encoding="utf-8")
    codex_hooks = (ROOT / ".codex" / "hooks.json").read_text(encoding="utf-8")
    check("skill_router_hook.py" in claude_hooks, "approved recall hook present: .claude/settings.json", failures)
    check("skill-router" in codex_hooks and "codex_hook_runner.py" in codex_hooks,
          "approved recall bridge present: .codex/hooks.json", failures)

    trigger_score, _ = score_trigger_event(
        "At 2:00 one night I woke up because my dog was chewing his paws until they bled."
    )
    benefit_score, _ = score_trigger_event("Healthy ingredients support better skin and a shiny coat.")
    check(trigger_score >= 45, "specific intolerable moment detected", failures)
    check(benefit_score < 45, "generic benefit rejected", failures)

    with tempfile.TemporaryDirectory(prefix="creative-intelligence-verify-") as tmp:
        base = Path(tmp)
        ledger = base / "events.jsonl"
        db = base / "memory.db"
        lesson = "Mine the intolerable moment before writing the benefit"
        event_ids = []
        for project in ("acme", "beacon", "cobalt"):
            event_id = ci.capture_event(
                project_scope=project,
                hypothesis="controlled trigger test",
                event_key=project,
                ledger_path=ledger,
            )["event_id"]
            event_ids.append(event_id)
            ci.attach_outcome(
                event_id,
                metric="hold_rate",
                value="0.31",
                baseline="0.22",
                test_design="controlled",
                candidate_lesson=lesson,
                ledger_path=ledger,
            )
        preview = ci.synthesize(ledger_path=ledger)
        check(len(preview["candidates"]) == 1, "three projects yield one shared proposal", failures)
        check(preview["candidates"][0].get("scope") == "shared", "proposal scope is shared", failures)
        committed = ci.synthesize(commit=True, ledger_path=ledger, db_path=db)
        check(committed["candidates"][0].get("inserted") is True, "proposal queued", failures)
        conn = sqlite3.connect(str(db))
        row = conn.execute("SELECT status, proposed_metadata FROM flagged_review").fetchone()
        conn.close()
        metadata = json.loads(row[1])
        check(row[0] == "pending", "candidate remains pending human review", failures)
        check(metadata.get("auto_promotion_allowed") is False, "candidate forbids auto-promotion", failures)

        opposite = ci.capture_event(
            project_scope="acme",
            hypothesis="contradictory result",
            event_key="contradiction",
            ledger_path=ledger,
        )["event_id"]
        ci.attach_outcome(
            opposite,
            metric="hold_rate",
            value="0.18",
            baseline="0.22",
            test_design="comparative",
            candidate_lesson=lesson,
            contradicts=event_ids[0],
            ledger_path=ledger,
        )
        remaining = ci.synthesize(ledger_path=ledger)["candidates"]
        check(not any(event_ids[0] in row.get("event_ids", []) for row in remaining), "contradicted evidence cannot promote", failures)

    if importlib.util.find_spec("pytest") is not None:
        pytest_command = [sys.executable, "-m", "pytest"]
    else:
        pytest_executable = shutil.which("pytest")
        pytest_command = [pytest_executable] if pytest_executable else []
    check(bool(pytest_command), "pytest runner available", failures)
    tests = subprocess.run(
        [*pytest_command, "tests/test_creative_intelligence.py", "tests/test_review_miner_trigger_events.py", "-q"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    ) if pytest_command else None
    if tests is not None:
        print(tests.stdout.strip())
        check(tests.returncode == 0, "focused test suite", failures)

    print(f"\nVERDICT: {'PASS' if not failures else 'FAIL'} ({len(failures)} failure(s))")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
