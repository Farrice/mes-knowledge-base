#!/usr/bin/env python3
"""Verify Mission OS activation enforcement and fresh-session resume behavior."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(
    args: list[str],
    env: dict[str, str] | None = None,
    expect_ok: bool = True,
) -> subprocess.CompletedProcess[str]:
    run_env = os.environ.copy()
    if env:
        run_env.update(env)
    result = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        env=run_env,
        check=False,
    )
    if expect_ok and result.returncode != 0:
        raise AssertionError(f"{' '.join(args)} failed:\n{result.stdout}")
    if not expect_ok and result.returncode == 0:
        raise AssertionError(f"{' '.join(args)} unexpectedly passed:\n{result.stdout}")
    return result


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def test_empty_assertions_fail(tmp: Path, env: dict[str, str]) -> None:
    run(
        [
            sys.executable,
            "execution/mission_control.py",
            "create",
            "--name",
            "Empty Assertions Fixture",
            "--slug",
            "empty-assertions",
            "--goal",
            "Prove active missions cannot validate without assertions",
            "--mode",
            "system",
        ],
        env=env,
    )
    run(
        [
            sys.executable,
            "execution/mission_control.py",
            "set-status",
            "empty-assertions",
            "active",
        ],
        env=env,
    )
    result = run(
        [sys.executable, "execution/mission_control.py", "validate", "empty-assertions"],
        env=env,
        expect_ok=False,
    )
    if "FAIL validation assertions recorded for active mission" not in result.stdout:
        raise AssertionError("empty assertion fixture did not fail on missing assertions")


def test_partial_activation_fails(tmp: Path, env: dict[str, str]) -> None:
    evidence_one = tmp / "evidence" / "one.md"
    evidence_two = tmp / "evidence" / "two.md"
    evidence_one.parent.mkdir(parents=True, exist_ok=True)
    evidence_one.write_text("# Evidence One\n", encoding="utf-8")
    evidence_two.write_text("# Evidence Two\n", encoding="utf-8")

    run(
        [
            sys.executable,
            "execution/mission_control.py",
            "create",
            "--name",
            "Partial Activation Fixture",
            "--slug",
            "partial-activation",
            "--goal",
            "Prove unfinished activation items block validation",
            "--mode",
            "system",
            "--next-command",
            "/mission resume partial-activation",
        ],
        env=env,
    )
    run(
        [
            sys.executable,
            "execution/mission_control.py",
            "add-assertion",
            "partial-activation",
            "--id",
            "VA1",
            "--statement",
            "Every planned lane has evidence or a blocker",
            "--covered-by",
            "A1,A2,A3",
            "--validator",
            "mission activation verifier",
            "--pass-signal",
            "validation names unfinished lane",
        ],
        env=env,
    )
    for item_id, path in (("A1", evidence_one), ("A2", evidence_two)):
        run(
            [
                sys.executable,
                "execution/mission_control.py",
                "add-activation",
                "partial-activation",
                "--id",
                item_id,
                "--owner",
                f"Worker {item_id}",
                "--workflow",
                "/mission",
                "--expected-artifact",
                f"Artifact {item_id}",
                "--status",
                "complete",
                "--evidence-path",
                str(path),
                "--validation-assertion",
                "VA1",
            ],
            env=env,
        )
    run(
        [
            sys.executable,
            "execution/mission_control.py",
            "add-activation",
            "partial-activation",
            "--id",
            "A3",
            "--owner",
            "Worker A3",
            "--workflow",
            "/mission",
            "--expected-artifact",
            "Artifact A3",
            "--status",
            "active",
            "--validation-assertion",
            "VA1",
        ],
        env=env,
    )
    run(
        [
            sys.executable,
            "execution/mission_control.py",
            "set-resume-packet",
            "partial-activation",
            "--next-command",
            "/mission resume partial-activation",
        ],
        env=env,
    )
    run(
        [
            sys.executable,
            "execution/mission_control.py",
            "set-status",
            "partial-activation",
            "active",
        ],
        env=env,
    )
    result = run(
        [sys.executable, "execution/mission_control.py", "validate", "partial-activation"],
        env=env,
        expect_ok=False,
    )
    if "unfinished activation items: A3" not in result.stdout:
        raise AssertionError("partial activation fixture did not name unfinished lane A3")


def test_resume_prefers_structured_state(tmp: Path, env: dict[str, str]) -> None:
    run(
        [
            sys.executable,
            "execution/mission_control.py",
            "create",
            "--name",
            "Stale Resume Fixture",
            "--slug",
            "stale-resume",
            "--goal",
            "Prove resume prefers newer structured state",
            "--mode",
            "system",
            "--next-command",
            "/mission resume stale-resume",
        ],
        env=env,
    )
    session_state = tmp / ".agent" / "session-state.md"
    session_state.parent.mkdir(parents=True, exist_ok=True)
    session_state.write_text("# Session State\n\nActive Task: Old unrelated work\n", encoding="utf-8")
    os.utime(session_state, (1_700_000_000, 1_700_000_000))
    write_json(
        tmp / ".agent" / "intent-memory" / "current.json",
        {
            "mission": {"slug": "stale-resume"},
            "active_intent": {"goal": "structured resume"},
            "route": {"chosen_route": "mission"},
            "next_move": {"action": "/mission resume stale-resume"},
        },
    )
    write_json(
        tmp / ".agent" / "system-cohesion-state.json",
        {
            "mission": {"slug": "stale-resume"},
            "active_intent": {"goal": "structured resume"},
            "chosen_route": {"route": "mission"},
            "next_move": {"action": "/mission resume stale-resume"},
        },
    )
    result = run(
        [sys.executable, "execution/mission_control.py", "resume", "stale-resume"],
        env=env,
    )
    if "Preferred resume source: intent-memory + system-cohesion" not in result.stdout:
        raise AssertionError("resume did not prefer structured state")
    if "stale" not in result.stdout.lower():
        raise AssertionError("resume did not warn about stale session state")


def test_vibe_tax_deploy_routes_first() -> None:
    query = "vibe tax deployment post diagnostic daily"
    menu = run([sys.executable, "execution/command_menu.py", "search", query]).stdout
    router = run([sys.executable, "execution/workflow_router.py", "search", query]).stdout
    if "1. `/vibe-tax-deploy`" not in menu:
        raise AssertionError("/vibe-tax-deploy was not first in command menu:\n" + menu)
    first_router_line = next((line for line in router.splitlines() if line.strip().startswith("/")), "")
    if not first_router_line.strip().startswith("/vibe-tax-deploy"):
        raise AssertionError("/vibe-tax-deploy was not first in workflow router:\n" + router)


def main() -> int:
    failures: list[str] = []
    checks: list[str] = []
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        env = {"ANTIGRAVITY_ROOT": str(tmp)}
        for name, test in (
            ("empty assertions fail", test_empty_assertions_fail),
            ("partial activation fails", test_partial_activation_fails),
            ("resume prefers structured state", test_resume_prefers_structured_state),
        ):
            try:
                test(tmp, env)
                checks.append(name)
            except AssertionError as exc:
                failures.append(f"{name}: {exc}")

    try:
        test_vibe_tax_deploy_routes_first()
        checks.append("vibe tax deployment routes first")
    except AssertionError as exc:
        failures.append(f"vibe tax routing: {exc}")

    if failures:
        print("Mission Activation Contract verification: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Mission Activation Contract verification: PASS")
    for check in checks:
        print(f"- {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
