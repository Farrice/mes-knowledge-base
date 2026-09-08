#!/usr/bin/env python3
"""Verify System-audit Operator Core source truth, wrappers, and routing."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "system-audit.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-system-audit" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_SYSTEM_AUDIT = Path.home() / ".codex" / "skills" / "system-audit" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-system-audit" / "SKILL.md"
AGENTIC_CONTRACT = ROOT / "semantic_libraries" / "antigravity" / "primitives" / "agentic-engineering-loop-contract.md"
GOAL_LOOP_CONTRACT = ROOT / "semantic_libraries" / "antigravity" / "primitives" / "goal-loop-maintenance-contract.md"
SOURCE_TO_SKILL = ROOT / ".agent" / "workflows" / "source-to-skill-system.md"

REQUIRED_TEXT = {
    PROJECT_WORKFLOW: [
        "canonical source of truth for System-audit behavior",
        "control-plane audit and repair route",
        "Run read-only proof first",
        "Distinguish structural health from firing behavior",
        "Repairs must be severity-ranked, verifier-backed, and workspace-local by default",
        "Global `~/.codex` edits require explicit approval",
        "Mission remains untouched unless `verify_mission_activation_contract.py` fails and Farrice explicitly approves Mission repair",
        "Route normal status reads to `/health-check`, routing analytics to `/routing-intelligence`, and raw intent or broad broken-harness triage to `/autopilot`",
        "Real Codex subagents require explicit authorization",
    ],
    LOCAL_WRAPPER: [
        ".agent/workflows/system-audit.md",
        "canonical behavior source",
        "thin compatibility wrapper",
        "control-plane audit and repair",
        "read-only proof first",
        "structural health",
        "firing behavior",
        "severity-ranked",
        "verifier-backed",
        "workspace-local by default",
        "global `~/.codex` edits require explicit approval",
        "verify_mission_activation_contract.py",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_AGENTS: [
        "Global System-audit Control Plane",
        "/Users/farricecain/Google Antigravity/.agent/workflows/system-audit.md",
        "thin compatibility wrappers",
        "control-plane audit and repair",
        "read-only proof first",
        "structural health",
        "firing behavior",
        "severity-ranked",
        "verifier-backed",
        "workspace-local by default",
        "global `~/.codex` edits require explicit approval",
        "verify_mission_activation_contract.py",
        "Codex subagents require explicit authorization",
    ],
    GLOBAL_SYSTEM_AUDIT: [
        "Project Source Of Truth",
        "/Users/farricecain/Google Antigravity/.agent/workflows/system-audit.md",
        "thin compatibility wrapper",
        "control-plane audit and repair",
        "read-only proof first",
        "structural health",
        "firing behavior",
        "severity-ranked",
        "verifier-backed",
        "workspace-local by default",
        "global `~/.codex` edits require explicit approval",
        "verify_mission_activation_contract.py",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_WRAPPER: [
        "compatibility alias",
        "/Users/farricecain/.codex/skills/system-audit/SKILL.md",
        "/Users/farricecain/Google Antigravity/.agent/workflows/system-audit.md",
        "thin compatibility wrapper",
        "control-plane audit and repair",
        "read-only proof first",
        "structural health",
        "firing behavior",
        "severity-ranked",
        "verifier-backed",
        "workspace-local by default",
        "global `~/.codex` edits",
        "verify_mission_activation_contract.py",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
}

FORBIDDEN = (
    "delete by default",
    "destructive cleanup by default",
    "global edit by default",
    "connector write by default",
    "publish by default",
    "mutate Mission by default",
    "repair Mission by default",
)

ROUTING_CASES = (
    ("source-command-system-audit control plane drift audit", "system-audit", "system-failure"),
    ("audit autopilot control-plane routing drift", "system-audit", "system-failure"),
    ("system audit not firing proof path", "system-audit", "system-failure"),
    ("health check harness status", "health-check", "health-check-status"),
    ("routing intelligence dashboard", "routing-intelligence", "routing-intelligence-analytics"),
)

STALE_LIVE_VERIFIER_COMMANDS = (
    "python3 execution/verify_agentic_engineering_loop_contract.py",
    "python3 execution/verify_goal_loop_maintenance_contract.py",
)

ACTIVE_PROOF_SURFACES = (
    ROOT / "CODEX.md",
    PROJECT_WORKFLOW,
    AGENTIC_CONTRACT,
    GOAL_LOOP_CONTRACT,
    SOURCE_TO_SKILL,
)


def run(args: list[str]) -> str:
    completed = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if completed.returncode != 0:
        raise AssertionError(f"Command failed: {' '.join(args)}\n{completed.stdout}")
    return completed.stdout


def first_command_line(output: str) -> str:
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("1. `/") or stripped.startswith("/"):
            return stripped
    return ""


def first_workflow_line(output: str) -> str:
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("/"):
            return stripped
    return ""


def chosen_route(output: str) -> str:
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("- **Chosen route**: /"):
            return stripped.rsplit("/", 1)[-1]
    return ""


def detected_lane(output: str) -> str:
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("- **Detected lane**:"):
            return stripped.split(":", 1)[-1].strip()
    return ""


def verify_text() -> list[str]:
    results = []
    for path, snippets in REQUIRED_TEXT.items():
        if not path.exists():
            raise AssertionError(f"Missing file: {path}")
        text = path.read_text(encoding="utf-8", errors="ignore")
        normalized = " ".join(text.split())
        for snippet in snippets:
            if " ".join(snippet.split()) not in normalized:
                raise AssertionError(f"Missing snippet in {path}: {snippet}")
        for snippet in FORBIDDEN:
            if snippet.lower() in text.lower():
                raise AssertionError(f"Stale System-audit text in {path}: {snippet}")
        results.append(f"system-audit contract text present: {path}")
    return results


def verify_sync_helper() -> list[str]:
    run([sys.executable, "execution/sync_operator_core_system_audit.py", "--check"])
    return ["system-audit sync helper passes"]


def stale_live_verifier_commands(content: str) -> list[str]:
    return [command for command in STALE_LIVE_VERIFIER_COMMANDS if command in content]


def verify_live_proof_paths() -> list[str]:
    archived = ROOT / "execution" / "_archived_verifiers"
    if not archived.is_dir():
        raise AssertionError("Missing approved archived-verifier directory")
    for path in ACTIVE_PROOF_SURFACES:
        if not path.exists():
            raise AssertionError(f"Missing proof surface: {path}")
        content = path.read_text(encoding="utf-8", errors="ignore")
        stale = stale_live_verifier_commands(content)
        if stale:
            raise AssertionError(f"Stale live verifier command in {path}: {stale[0]}")
    for command in STALE_LIVE_VERIFIER_COMMANDS:
        if stale_live_verifier_commands(f"Run next:\n{command}\n") != [command]:
            raise AssertionError(f"Negative control failed to catch stale command: {command}")
    return [
        "active proof surfaces do not advertise intentionally archived verifiers",
        "negative controls catch both retired live command paths",
    ]


def verify_validator_truthfulness() -> list[str]:
    valid = subprocess.run(
        [sys.executable, "execution/validate_skill.py", "source-command-system-audit"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if valid.returncode != 0 or "critical" not in valid.stdout or "0 critical" not in valid.stdout:
        raise AssertionError(f"Valid Codex wrapper did not validate cleanly:\n{valid.stdout}")

    invalid = subprocess.run(
        [sys.executable, "execution/validate_skill.py", "source-command-definitely-missing"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if invalid.returncode == 0 or "critical" not in invalid.stdout:
        raise AssertionError("Validator false-green negative control did not fail")
    return ["skill validator returns nonzero for critical wrapper failures"]


def verify_routes() -> list[str]:
    results = []
    for query, expected, expected_lane in ROUTING_CASES:
        menu = run([sys.executable, "execution/command_menu.py", "search", query])
        first_menu = first_command_line(menu)
        if f"`/{expected}`" not in first_menu:
            raise AssertionError(f"command_menu expected /{expected} first for {query!r}; got {first_menu}")
        router = run([sys.executable, "execution/workflow_router.py", "search", query])
        first_router = first_workflow_line(router)
        if f"/{expected}" not in first_router:
            raise AssertionError(f"workflow_router expected /{expected} first for {query!r}; got {first_router}")
        governor = run([sys.executable, "execution/routing_governor.py", "evaluate", query])
        chosen = chosen_route(governor)
        lane = detected_lane(governor)
        if chosen != expected:
            raise AssertionError(f"routing_governor expected /{expected} for {query!r}; got /{chosen}")
        if lane != expected_lane:
            raise AssertionError(f"routing_governor expected lane {expected_lane} for {query!r}; got {lane}")
        results.append(f"routing guard: {query!r} -> /{expected} ({lane})")
    return results


def main() -> int:
    results = []
    results.extend(verify_text())
    results.extend(verify_sync_helper())
    results.extend(verify_live_proof_paths())
    results.extend(verify_validator_truthfulness())
    results.extend(verify_routes())
    print("SYSTEM-AUDIT OPERATOR CORE VERIFICATION PASS")
    for result in results:
        print(f"- {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
