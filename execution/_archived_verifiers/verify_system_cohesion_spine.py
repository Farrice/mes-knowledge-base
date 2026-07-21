#!/usr/bin/env python3
"""Verify the shared system cohesion spine."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
STATE_SCRIPT = ROOT / "execution" / "system_cohesion_state.py"
INTENT_SCRIPT = ROOT / "execution" / "intent_memory.py"
AUTOPILOT = ROOT / ".agent" / "workflows" / "autopilot.md"
MISSION = ROOT / ".agent" / "workflows" / "mission.md"

REQUIRED_STATE_KEYS = (
    "active_intent",
    "mission",
    "chosen_route",
    "support_gates",
    "expert_stack",
    "activation_queue",
    "verifier_status",
    "weekly_platter",
    "next_move",
)

REQUIRED_WORKFLOW_TERMS = (
    ".agent/system-cohesion-state.json",
    "execution/system_cohesion_state.py update",
    "active intent",
    "chosen route",
    "support gates",
    "expert stack",
    "activation queue",
    "verifier status",
    "weekly platter",
    "next move",
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


def check_workflows() -> list[str]:
    failures: list[str] = []
    for path in (AUTOPILOT, MISSION):
        if not path.exists():
            failures.append(f"missing workflow: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8", errors="ignore").lower()
        for term in REQUIRED_WORKFLOW_TERMS:
            if term.lower() not in text:
                failures.append(f"{path.relative_to(ROOT)} missing term: {term}")
    return failures


def check_state_contract() -> list[str]:
    if not STATE_SCRIPT.exists():
        raise AssertionError("missing execution/system_cohesion_state.py")
    if not INTENT_SCRIPT.exists():
        raise AssertionError("missing execution/intent_memory.py")

    with tempfile.TemporaryDirectory() as tmpdir:
        env = {"ANTIGRAVITY_ROOT": tmpdir}
        agent_dir = Path(tmpdir) / ".agent"
        agent_dir.mkdir(parents=True, exist_ok=True)

        run(
            [
                sys.executable,
                "execution/system_cohesion_state.py",
                "update",
                "--intent-goal",
                "Verify cohesion spine",
                "--intent-deliverable",
                "state contract proof",
                "--intent-audience",
                "Codex harness",
                "--success",
                "state tracks current operating picture",
                "--constraint",
                "workspace local",
                "--clarity-score",
                "94",
                "--confidence",
                "High",
                "--ambiguity-map",
                "non-blocking",
                "--source",
                "verifier",
                "--mission-slug",
                "system-cohesion-spine",
                "--mission-state-path",
                ".agent/missions/system-cohesion-spine/mission.json",
                "--mission-status",
                "validating",
                "--route",
                "mission",
                "--mode",
                "Mission Mode",
                "--route-reason",
                "system-changing durable state",
                "--support-gate",
                "intent-memory-contract",
                "--support-gate",
                "system-cohesion-spine",
                "--expert",
                "operator-autopilot",
                "--activation",
                "run new verifiers",
                "--verifier",
                "intent_memory_contract=pass",
                "--verifier",
                "system_cohesion_spine=pass",
                "--weekly-platter-status",
                "queued",
                "--weekly-platter-path",
                ".agent/recurring-reports/weekly-system-cohesion.md",
                "--next-move",
                "finish Worker 2 verification",
                "--next-owner",
                "Worker 2",
                "--next-verification",
                "python3 execution/verify_system_cohesion_spine.py",
            ],
            env=env,
        )
        show_output = run([sys.executable, "execution/system_cohesion_state.py", "show"], env=env)
        if "Verify cohesion spine" not in show_output:
            raise AssertionError("cohesion show did not include active intent")
        verify_output = run([sys.executable, "execution/system_cohesion_state.py", "verify"], env=env)
        if "PASS" not in verify_output:
            raise AssertionError("cohesion verify did not pass")

        state_path = agent_dir / "system-cohesion-state.json"
        payload = json.loads(state_path.read_text(encoding="utf-8"))
        missing = [key for key in REQUIRED_STATE_KEYS if key not in payload]
        if missing:
            raise AssertionError("state missing required keys: " + ", ".join(missing))
        if payload["chosen_route"]["route"] != "mission":
            raise AssertionError("state did not store chosen route")
        if payload["weekly_platter"]["status"] != "queued":
            raise AssertionError("state did not store weekly platter status")
        if "run new verifiers" not in payload["activation_queue"]:
            raise AssertionError("state did not store activation queue")

        run(
            [
                sys.executable,
                "execution/intent_memory.py",
                "capture",
                "--goal",
                "Sync intent into cohesion",
                "--chosen-route",
                "autopilot",
            ],
            env=env,
        )
        synced = json.loads(state_path.read_text(encoding="utf-8"))
        if synced["active_intent"]["goal"] != "Sync intent into cohesion":
            raise AssertionError("intent capture did not update cohesion active intent")
        if synced["chosen_route"]["route"] != "autopilot":
            raise AssertionError("intent capture did not update cohesion chosen route")
    return ["shared cohesion keys, update/show/verify, and intent sync work"]


def main() -> int:
    failures = check_workflows()
    checks: list[str] = []
    if not failures:
        try:
            checks.extend(check_state_contract())
        except AssertionError as exc:
            failures.append(str(exc))

    if failures:
        print("System Cohesion Spine verification: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("System Cohesion Spine verification: PASS")
    for check in checks:
        print(f"- {check}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
