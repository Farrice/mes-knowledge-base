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
import log_performance  # noqa: E402


def _fixture_skill() -> str:
    """Pick a fixture skill that genuinely has local performance history.

    The local mirror (.agent/performance-log.jsonl) started fresh on
    2026-07-15; skills that were only ever logged to Notion (e.g. the old
    luke-iha-client-mastery fixture) have zero local rows. The contract
    under test is local-first behavior, not any one skill, so the fixture
    is the most-logged skill with >=2 rows and a real skills/ directory.
    """
    counts: dict[str, int] = {}
    for row in log_performance.get_local_performance_entries():
        name = str(row.get("skill") or row.get("Skill") or "")
        if name and (ROOT / "skills" / name).is_dir():
            counts[name] = counts.get(name, 0) + 1
    eligible = {k: v for k, v in counts.items() if v >= 2}
    if not eligible:
        raise AssertionError(
            "no skill has >=2 rows in the local performance mirror "
            "(.agent/performance-log.jsonl) — local-first evidence is broken"
        )
    return max(eligible, key=lambda k: (eligible[k], k))


FIXTURE_SKILL = _fixture_skill()


def check_local_history() -> str:
    os.environ.pop("ANTIGRAVITY_ALLOW_NOTION_BENCHMARK", None)
    history = skill_benchmark.get_performance_history(FIXTURE_SKILL)
    if len(history) < 2:
        raise AssertionError(f"expected local history for {FIXTURE_SKILL}, got {len(history)}")
    if any(not str(row.get("url", "")).startswith(("local://", "https://")) for row in history):
        raise AssertionError("local history rows missing local/remote URL markers")
    return f"local benchmark history available for {FIXTURE_SKILL} ({len(history)} rows)"


def check_report_no_network() -> str:
    result = subprocess.run(
        [sys.executable, "execution/skill_benchmark.py", "report", FIXTURE_SKILL],
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
