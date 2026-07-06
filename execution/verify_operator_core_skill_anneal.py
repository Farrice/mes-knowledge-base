#!/usr/bin/env python3
"""Verify Skill-anneal Operator Core source truth, wrappers, and routing."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "skill-anneal.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-skill-anneal" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_SKILL_ANNEAL = Path.home() / ".codex" / "skills" / "skill-anneal" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-skill-anneal" / "SKILL.md"

REQUIRED_TEXT = {
    PROJECT_WORKFLOW: [
        "canonical source of truth for Skill-anneal behavior",
        "prompt-level skill/component annealing",
        "Incomplete or vague goal packets produce a queue-only diagnosis",
        "Annealing requires a target skill directory, failure examples, rubric/test-input set, proof artifact, measurable stop condition, turn cap, and explicit no-regression clause",
        "preserve upstream input, downstream output, and validation contract",
        "Limit edits to the single weakest criterion unless the user approves a broader rewrite",
        "Side effects must be local, reversible, and inside `/Users/farricecain/Google Antigravity`",
        "Stop at a human checkpoint for broader workflow evolution, global mirrors, external actions, broad archive/delete, destructive cleanup, new dependencies, failed validation, or Mission repair",
        "Route broad workflow evolution to `/self-evolve`",
        "Real Codex subagents require explicit authorization",
    ],
    LOCAL_WRAPPER: [
        ".agent/workflows/skill-anneal.md",
        "canonical behavior source",
        "thin compatibility wrapper",
        "prompt-level skill/component annealing",
        "queue-only diagnosis",
        "target skill directory",
        "failure examples",
        "rubric/test-input set",
        "proof artifact",
        "measurable stop condition",
        "turn cap",
        "explicit no-regression clause",
        "single weakest criterion",
        "local, reversible",
        "human checkpoint",
        "/self-evolve",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_AGENTS: [
        "Global Skill-anneal Prompt Repair",
        "/Users/farricecain/Google Antigravity/.agent/workflows/skill-anneal.md",
        "thin compatibility wrappers",
        "prompt-level skill/component annealing",
        "queue-only diagnosis",
        "target skill directory",
        "failure examples",
        "rubric/test-input set",
        "proof artifact",
        "measurable stop condition",
        "turn cap",
        "explicit no-regression clause",
        "single weakest criterion",
        "local, reversible",
        "human checkpoint",
        "/self-evolve",
        "Codex subagents require explicit authorization",
    ],
    GLOBAL_SKILL_ANNEAL: [
        "Project Source Of Truth",
        "/Users/farricecain/Google Antigravity/.agent/workflows/skill-anneal.md",
        "thin compatibility wrapper",
        "prompt-level skill/component annealing",
        "queue-only diagnosis",
        "target skill directory",
        "failure examples",
        "rubric/test-input set",
        "proof artifact",
        "measurable stop condition",
        "turn cap",
        "explicit no-regression clause",
        "single weakest criterion",
        "local, reversible",
        "human checkpoint",
        "/self-evolve",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
    GLOBAL_WRAPPER: [
        "compatibility alias",
        "/Users/farricecain/.codex/skills/skill-anneal/SKILL.md",
        "/Users/farricecain/Google Antigravity/.agent/workflows/skill-anneal.md",
        "thin compatibility wrapper",
        "prompt-level skill/component annealing",
        "queue-only diagnosis",
        "target skill",
        "failure examples",
        "rubric/test-input set",
        "proof artifact",
        "measurable stop condition",
        "turn cap",
        "explicit no-regression clause",
        "single weakest criterion",
        "local, reversible",
        "human checkpoint",
        "/self-evolve",
        "real Codex subagents require explicit authorization",
        "no competing behavior contract",
    ],
}

FORBIDDEN = (
    "rewrite the whole workflow by default",
    "edit without rubric",
    "edit without failure examples",
    "mutate by default",
    "global mirror by default",
    "external action by default",
    "destructive cleanup by default",
    "mutate Mission by default",
    "repair Mission by default",
)

ROUTING_CASES = (
    ("source-command-skill-anneal improve this skill prompt", "skill-anneal", "skill-anneal"),
    ("skill-anneal SKILL.md with rubric.md and test_inputs.md", "skill-anneal", "skill-anneal"),
    ("anneal this skill using failure examples", "skill-anneal", "skill-anneal"),
    ("audit skill-anneal operator core drift", "system-audit", "system-failure"),
    ("skill-anneal is broken and rewriting everything", "autopilot", "system-failure"),
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
                raise AssertionError(f"Stale Skill-anneal text in {path}: {snippet}")
        results.append(f"skill-anneal contract text present: {path}")
    return results


def verify_sync_helper() -> list[str]:
    run([sys.executable, "execution/sync_operator_core_skill_anneal.py", "--check"])
    return ["skill-anneal sync helper passes"]


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
    print("SKILL-ANNEAL OPERATOR CORE VERIFICATION PASS")
    for result in results:
        print(f"- {result}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
