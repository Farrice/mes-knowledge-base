#!/usr/bin/env python3
"""Verify the workspace-local intent memory contract."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FILES = {
    "intent_memory": ROOT / "execution" / "intent_memory.py",
    "cohesion_state": ROOT / "execution" / "system_cohesion_state.py",
    "autopilot": ROOT / ".agent" / "workflows" / "autopilot.md",
    "mission": ROOT / ".agent" / "workflows" / "mission.md",
}

REQUIRED_WORKFLOW_TERMS = (
    ".agent/intent-memory/current.json",
    ".agent/system-cohesion-state.json",
    "execution/intent_memory.py capture",
    "execution/intent_memory.py update",
    "execution/intent_memory.py verify",
)


def run(args: list[str], env: dict[str, str] | None = None) -> str:
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
    if result.returncode != 0:
        raise AssertionError(f"{' '.join(args)} failed:\n{result.stdout}")
    return result.stdout


def check_files_and_workflows() -> list[str]:
    failures: list[str] = []
    for label, path in FILES.items():
        if not path.exists():
            failures.append(f"missing {label}: {path.relative_to(ROOT)}")
    for workflow_label in ("autopilot", "mission"):
        path = FILES[workflow_label]
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8", errors="ignore")
        for term in REQUIRED_WORKFLOW_TERMS:
            if term not in text:
                failures.append(f"{path.relative_to(ROOT)} missing term: {term}")
    return failures


def check_cli_contract() -> list[str]:
    with tempfile.TemporaryDirectory() as tmpdir:
        env = {"ANTIGRAVITY_ROOT": tmpdir}
        agent_dir = Path(tmpdir) / ".agent"
        agent_dir.mkdir(parents=True, exist_ok=True)

        capture_output = run(
            [
                sys.executable,
                "execution/intent_memory.py",
                "capture",
                "--goal",
                "Verify intent memory contract",
                "--deliverable",
                "temporary verifier state",
                "--audience",
                "Codex harness",
                "--success",
                "capture command writes current intent",
                "--constraint",
                "workspace local",
                "--clarity-score",
                "96",
                "--confidence",
                "High",
                "--ambiguity-map",
                "non-blocking",
                "--source",
                "verifier",
                "--mode",
                "Direct Execute",
                "--chosen-route",
                "autopilot",
                "--support-gate",
                "system-cohesion-state",
                "--expert",
                "none",
                "--next-move",
                "run verifier",
                "--next-owner",
                "validator",
                "--next-verification",
                "intent_memory.py verify",
            ],
            env=env,
        )
        if "Captured intent memory" not in capture_output:
            raise AssertionError("capture command did not report capture")

        current = agent_dir / "intent-memory" / "current.json"
        cohesion = agent_dir / "system-cohesion-state.json"
        if not current.exists():
            raise AssertionError("capture did not create .agent/intent-memory/current.json")
        if not cohesion.exists():
            raise AssertionError("capture did not sync .agent/system-cohesion-state.json")

        show_output = run([sys.executable, "execution/intent_memory.py", "show"], env=env)
        if "Verify intent memory contract" not in show_output:
            raise AssertionError("show command did not print captured goal")

        run(
            [
                sys.executable,
                "execution/intent_memory.py",
                "update",
                "--next-move",
                "confirm contract",
                "--support-gate",
                "intent-memory-contract",
            ],
            env=env,
        )
        verify_output = run([sys.executable, "execution/intent_memory.py", "verify"], env=env)
        if "PASS" not in verify_output:
            raise AssertionError("verify command did not pass")

        intent_payload = json.loads(current.read_text(encoding="utf-8"))
        cohesion_payload = json.loads(cohesion.read_text(encoding="utf-8"))
        if intent_payload["schema_version"] != "intent-memory/v1":
            raise AssertionError("intent memory schema version mismatch")
        if cohesion_payload["active_intent"]["goal"] != intent_payload["active_intent"]["goal"]:
            raise AssertionError("cohesion state did not mirror active intent")
        if cohesion_payload["chosen_route"]["route"] != intent_payload["route"]["chosen_route"]:
            raise AssertionError("cohesion state did not mirror chosen route")
    return ["capture/show/update/verify commands work in isolated workspace"]


def main() -> int:
    failures = check_files_and_workflows()
    checks: list[str] = []
    if not failures:
        try:
            checks.extend(check_cli_contract())
        except AssertionError as exc:
            failures.append(str(exc))

    if failures:
        print("Intent Memory Contract verification: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Intent Memory Contract verification: PASS")
    for check in checks:
        print(f"- {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
