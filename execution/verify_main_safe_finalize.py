#!/usr/bin/env python3
"""Negative controls for integration-main-safe finalize telemetry."""
from __future__ import annotations

import json
import subprocess
import tempfile
from pathlib import Path

import chain_runner as cr


TRACKED_TELEMETRY = (
    "evolution_store/sub_agent_misses.jsonl",
    "evolution_store/blind_pass_overrides.jsonl",
    "evolution_store/learning_latch_overrides.jsonl",
    "evolution_store/verification_misses.jsonl",
    "evolution_store/verdict_advisory.jsonl",
)


def run(root: Path, *args: str) -> None:
    subprocess.run(["git", "-C", str(root), *args], check=True,
                   capture_output=True, text=True)


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)
    print(f"PASS: {message}")


def main() -> int:
    source_root = cr.PROJECT_ROOT
    with tempfile.TemporaryDirectory() as temp:
        root = Path(temp)
        run(root, "init", "-b", "main")
        run(root, "config", "user.email", "verify@local")
        run(root, "config", "user.name", "Verifier")
        (root / "README.md").write_text("fixture\n")
        for relative in TRACKED_TELEMETRY:
            path = root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text("baseline\n")
        run(root, "add", ".")
        run(root, "commit", "-m", "fixture")

        old_root, old_log = cr.PROJECT_ROOT, cr.FINALIZE_RUNTIME_LOG
        try:
            cr.PROJECT_ROOT = root
            cr.FINALIZE_RUNTIME_LOG = root / ".agent" / "finalize-runtime.jsonl"
            check(cr._on_integration_main(), "canonical main checkout selects runtime-only telemetry")
            cr._record_main_runtime_event("test", {"proof": "main stays clean"})
            event = json.loads(cr.FINALIZE_RUNTIME_LOG.read_text().splitlines()[-1])
            check(event["kind"] == "test" and event["proof"] == "main stays clean",
                  "runtime event remains observable in the local ledger")

            for relative in TRACKED_TELEMETRY:
                cr._append_runtime_safe_event(
                    root / relative,
                    Path(relative).stem,
                    {"proof": "tracked main stays unchanged"},
                )
            check(
                all((root / relative).read_text() == "baseline\n"
                    for relative in TRACKED_TELEMETRY),
                "all finalize telemetry ledgers remain unchanged on main",
            )
            runtime_kinds = {
                json.loads(line)["kind"]
                for line in cr.FINALIZE_RUNTIME_LOG.read_text().splitlines()
            }
            check(
                {Path(relative).stem for relative in TRACKED_TELEMETRY}
                <= runtime_kinds,
                "all redirected telemetry remains observable at runtime",
            )

            run(root, "checkout", "-b", "codex/test-lane")
            check(not cr._on_integration_main(), "authoring lane retains document-update behavior")
            lane_ledger = root / TRACKED_TELEMETRY[0]
            destination = cr._append_runtime_safe_event(
                lane_ledger, "lane-proof", {"proof": "lane retains evidence"}
            )
            check(
                destination == "tracked" and len(lane_ledger.read_text().splitlines()) == 2,
                "authoring lane retains tracked telemetry behavior",
            )
        finally:
            cr.PROJECT_ROOT, cr.FINALIZE_RUNTIME_LOG = old_root, old_log

    ignore_text = (source_root / ".gitignore").read_text(encoding="utf-8")
    scheduled_patterns = (
        ".agent/mission-queue/pending/card-harness-evals-*.md",
        ".agent/mission-queue/pending/card-verdict-to-diff-*.md",
        ".agent/recurring-reports/*-session-closeout-intelligence.md",
    )
    check(
        all(pattern in ignore_text for pattern in scheduled_patterns),
        "scheduled queue and closeout outputs stay outside Git status",
    )

    print("PASS: main-safe finalize suite")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
