#!/usr/bin/env python3
"""Verify Self-evolve Operator Core source truth, wrappers, and routing."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "self-evolve.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-self-evolve" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_SELF_EVOLVE = Path.home() / ".codex" / "skills" / "self-evolve" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-self-evolve" / "SKILL.md"

REQUIRED_TEXT = {
    PROJECT_WORKFLOW: [
        "canonical source of truth for Self-evolve behavior",
        "mutation-gated measured evolution",
        "Incomplete or vague goal packets produce a queue-only diagnosis",
        "Mutation requires a complete goal packet, Evolution Council Verdict, baseline, search set, measurable stop condition, turn cap, proof artifact, and no-regression check",
        "Permitted side effects must be local, reversible, and inside `/Users/farricecain/Codex Antigravity`",
        "Stop at a human checkpoint for global mirrors, external actions, broad archive/delete, destructive cleanup, new dependencies, failed validation, or scope expansion",
        "Do not mutate Mission unless `verify_mission_activation_contract.py` fails and the user explicitly approves Mission repair",
        "Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`",
        "Real Codex subagents require explicit authorization",
    ],
    LOCAL_WRAPPER: [
        ".agent/workflows/self-evolve.md",
        "canonical behavior source",
        "thin compatibility wrapper",
        "mutation-gated measured evolution",
        "queue-only diagnosis",
        "complete goal packet",
        "Evolution Council Verdict",
        "baseline",
        "search set",
        "measurable stop condition",
        "turn cap",
        "proof artifact",
        "no-regression check",
        "local, reversible",
        "human checkpoint",
        "verify_mission_activation_contract.py",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_AGENTS: [
        "Global Self-evolve Evolution",
        "/Users/farricecain/Codex Antigravity/.agent/workflows/self-evolve.md",
        "thin compatibility wrappers",
        "mutation-gated measured evolution",
        "queue-only diagnosis",
        "complete goal packet",
        "Evolution Council Verdict",
        "baseline",
        "search set",
        "measurable stop condition",
        "turn cap",
        "proof artifact",
        "no-regression check",
        "local, reversible",
        "human checkpoint",
        "verify_mission_activation_contract.py",
        "Codex subagents require explicit authorization",
    ],
    GLOBAL_SELF_EVOLVE: [
        "Project Source Of Truth",
        "/Users/farricecain/Codex Antigravity/.agent/workflows/self-evolve.md",
        "thin compatibility wrapper",
        "mutation-gated measured evolution",
        "queue-only diagnosis",
        "complete goal packet",
        "Evolution Council Verdict",
        "baseline",
        "search set",
        "measurable stop condition",
        "turn cap",
        "proof artifact",
        "no-regression check",
        "local, reversible",
        "human checkpoint",
        "verify_mission_activation_contract.py",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_WRAPPER: [
        "compatibility alias",
        "/Users/farricecain/.codex/skills/self-evolve/SKILL.md",
        "/Users/farricecain/Codex Antigravity/.agent/workflows/self-evolve.md",
        "thin compatibility wrapper",
        "mutation-gated measured evolution",
        "queue-only diagnosis",
        "complete goal packet",
        "Evolution Council Verdict",
        "baseline",
        "search set",
        "measurable stop condition",
        "turn cap",
        "proof artifact",
        "no-regression check",
        "local and reversible",
        "human checkpoint",
        "verify_mission_activation_contract.py",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
}

FORBIDDEN = (
    "improve this by editing immediately",
    "mutate by default",
    "global mirror by default",
    "external action by default",
    "delete without approval",
    "destructive cleanup by default",
    "mutate Mission by default",
    "repair Mission by default",
)

ROUTING_CASES = (
    ("source-command-self-evolve improve workflow with feedback", "self-evolve", "self-evolution"),
    ("self-evolve repeatable routing mistake with regression tests", "self-evolve", "self-evolution"),
    ("improve this workflow using performance logs", "self-evolve", "self-evolution"),
    ("audit self-evolve operator core drift", "system-audit", "system-failure"),
    ("self-evolve is broken and mutating without proof", "autopilot", "system-failure"),
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
                raise AssertionError(f"Stale Self-evolve text in {path}: {snippet}")
        results.append(f"self-evolve contract text present: {path}")
    return results


def verify_sync_helper() -> list[str]:
    run([sys.executable, "execution/sync_operator_core_self_evolve.py", "--check"])
    return ["self-evolve sync helper passes"]


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
    results.extend(verify_routes())
    print("SELF-EVOLVE OPERATOR CORE VERIFICATION PASS")
    for result in results:
        print(f"- {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
