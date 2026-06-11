#!/usr/bin/env python3
"""Verify /skill-evolution uses local-first evidence in sandboxed runs."""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import skill_benchmark  # noqa: E402


def check_local_history() -> str:
    os.environ.pop("ANTIGRAVITY_ALLOW_NOTION_BENCHMARK", None)
    history = skill_benchmark.get_performance_history("luke-iha-client-mastery")
    if len(history) < 2:
        raise AssertionError(f"expected local history for luke-iha-client-mastery, got {len(history)}")
    if any(not str(row.get("url", "")).startswith(("local://", "https://")) for row in history):
        raise AssertionError("local history rows missing local/remote URL markers")
    return f"local benchmark history available ({len(history)} rows)"


def check_report_no_network() -> str:
    result = subprocess.run(
        [sys.executable, "execution/skill_benchmark.py", "report", "luke-iha-client-mastery"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    combined = result.stdout + result.stderr
    if result.returncode != 0:
        raise AssertionError(f"skill benchmark report failed:\n{combined}")
    if "api.notion.com" in combined or "HTTPSConnection" in combined:
        raise AssertionError("skill benchmark attempted Notion network access")
    if "averaging 0/10" in combined:
        raise AssertionError("weak dimension recommendation used a missing metric key")
    if 'WEAK_WORKFLOW: "linkedin-cs-outreach"' in combined:
        raise AssertionError("benchmark proposed a non-existent workflow file from route metadata")
    return "report runs local-first without bogus weak-target recommendations"


def check_orchestrator_idempotent() -> str:
    result = subprocess.run(
        [sys.executable, "execution/evolution_orchestrator.py", "auto"],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    combined = result.stdout + result.stderr
    if result.returncode != 0:
        raise AssertionError(f"evolution orchestrator auto failed:\n{combined}")
    if "SyntaxWarning" in combined:
        raise AssertionError("evolution orchestrator emitted SyntaxWarning")
    if '"skipped"' not in result.stdout:
        raise AssertionError(f"unexpected orchestrator auto output:\n{result.stdout}")
    return "orchestrator auto is idempotent after first run"


def main() -> int:
    checks = [check_local_history, check_report_no_network, check_orchestrator_idempotent]
    passed: list[str] = []
    for check in checks:
        passed.append(check())
    print("SKILL EVOLUTION LOCAL-FIRST VERIFICATION PASS")
    for item in passed:
        print(f"- ok: {item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
