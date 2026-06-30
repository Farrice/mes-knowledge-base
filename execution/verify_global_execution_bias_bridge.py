#!/usr/bin/env python3
"""Verify the thin global Codex execution-bias bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
CODEX_HOME = Path("/Users/farricecain/.codex")
GLOBAL_FILES = {
    "agents": CODEX_HOME / "AGENTS.md",
    "system_audit": CODEX_HOME / "skills/system-audit/SKILL.md",
    "autopilot": CODEX_HOME / "skills/autopilot/SKILL.md",
    "source_autopilot": CODEX_HOME / "skills/source-command-autopilot/SKILL.md",
    "source_system_audit": CODEX_HOME / "skills/source-command-system-audit/SKILL.md",
}


def run(args: list[str], cwd: Path = ROOT) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, cwd=cwd, text=True, capture_output=True)


def fail(message: str) -> None:
    raise AssertionError(message)


def read(path: Path) -> str:
    if not path.exists():
        fail(f"Missing global bridge file: {path}")
    return path.read_text(encoding="utf-8")


def require_text(label: str, path: Path, needles: list[str]) -> None:
    text = read(path).lower()
    missing = [needle for needle in needles if needle.lower() not in text]
    if missing:
        fail(f"{label} missing: {', '.join(missing)}")


def check_global_contract() -> None:
    require_text(
        "global AGENTS",
        GLOBAL_FILES["agents"],
        [
            "global execution bias contract",
            "patch + verify",
            "local_next_action",
            "current workspace",
            "non-current-workspace harness edits",
            "real codex subagents",
        ],
    )
    require_text(
        "global system-audit",
        GLOBAL_FILES["system_audit"],
        [
            "execution bias global bridge",
            "patch + verify",
            "local_next_action",
            "current-workspace work",
            "copy-paste prompts",
            "non-current-workspace harness edits",
        ],
    )
    require_text(
        "global autopilot",
        GLOBAL_FILES["autopilot"],
        [
            "execution bias bridge",
            "local_next_action",
            "prompt is for blocked",
            "not for safe local work",
            "current workspace",
            "non-current-workspace harness",
        ],
    )
    require_text(
        "source-command-autopilot",
        GLOBAL_FILES["source_autopilot"],
        ["execution bias alias rule", "local_next_action when runnable", "run prompt when blocked"],
    )
    require_text(
        "source-command-system-audit",
        GLOBAL_FILES["source_system_audit"],
        ["execution bias alias rule", "safe local next actions", "non-current-workspace harness edits"],
    )


def check_no_conflicting_google_block() -> None:
    combined = "\n".join(read(path).lower() for path in GLOBAL_FILES.values())
    forbidden = [
        "edit google antigravity",
        "google antigravity edits",
        "no-google-antigravity",
    ]
    found = [term for term in forbidden if term in combined]
    if found:
        fail("Global bridge still contains blanket Google-blocking language: " + ", ".join(found))


def check_google_preflight_fresh_intent() -> None:
    proc = run(
        [
            sys.executable,
            "execution/codex_operator_preflight.py",
            "Codex is planning instead of acting; run the safe local next action and prove it",
            "--json",
        ]
    )
    if proc.returncode != 0:
        fail(f"Google preflight failed: {proc.stderr.strip()}")
    data = json.loads(proc.stdout)
    if data["chosen_path"].get("owner") != "system-audit":
        fail(f"Fresh-session intent should route to /system-audit, got /{data['chosen_path'].get('owner')}")
    if data["execution_decision"].get("status") != "Run Locally":
        fail(f"Fresh-session intent should Run Locally, got {data['execution_decision'].get('status')}")
    if not data["execution_decision"].get("can_execute_now"):
        fail("Fresh-session intent should be executable now")
    next_action = data.get("local_next_action") or {}
    if next_action.get("mode") != "patch_and_verify":
        fail("Fresh-session intent should emit local_next_action.mode patch_and_verify")
    if next_action.get("owner") != "system-audit":
        fail("Fresh-session local_next_action should stay /system-audit owned")


def check_outside_workspace_readiness() -> None:
    # Simulate the surface a new Codex session can read before entering Google.
    proc = run(
        [
            "rg",
            "-n",
            "Global Execution Bias Contract|Execution Bias Bridge|Execution Bias Global Bridge|local_next_action",
            str(GLOBAL_FILES["agents"]),
            str(GLOBAL_FILES["autopilot"]),
            str(GLOBAL_FILES["system_audit"]),
        ],
        cwd=Path("/private/tmp"),
    )
    if proc.returncode != 0:
        fail(f"Global bridge is not discoverable from outside Google: {proc.stderr or proc.stdout}")


def main() -> int:
    checks = [
        check_global_contract,
        check_no_conflicting_google_block,
        check_google_preflight_fresh_intent,
        check_outside_workspace_readiness,
    ]
    failures: list[str] = []
    for check in checks:
        try:
            check()
        except Exception as exc:  # noqa: BLE001 - verifier should report all failures.
            failures.append(f"{check.__name__}: {exc}")
    if failures:
        print("GLOBAL EXECUTION BIAS BRIDGE VERIFICATION FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("GLOBAL EXECUTION BIAS BRIDGE VERIFICATION PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
