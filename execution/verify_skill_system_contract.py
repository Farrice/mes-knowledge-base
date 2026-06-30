#!/usr/bin/env python3
"""Verify the Codex skill-system contract and pilot command bridge."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMITIVE = ROOT / "semantic_libraries" / "antigravity" / "primitives" / "skill-system-contract.md"
WORKFLOW = ROOT / ".agent" / "workflows" / "source-to-skill-system.md"
SOURCE_COMMAND = ROOT / ".claude" / "commands" / "source-to-skill-system.md"
CODEX_SKILL = ROOT / ".agents" / "skills" / "source-command-source-to-skill-system" / "SKILL.md"
SOURCE_PACKAGE = ROOT / "extractions" / "video-context" / "FD53kEpLh9c"


REQUIRED_TERMS = [
    "Source evidence",
    "Components",
    "Step order",
    "Inputs",
    "Outputs",
    "Handoff summary",
    "Human checkpoint",
    "Validation",
    "Behavior-changing proof",
    "Result surface",
    "Context policy",
    "Reuse hook",
]

ROUTING_QUERIES = [
    "make skills make sense 10x better",
    "turn this video into a reusable skill system",
    "improve Codex orchestration",
    "build an end-to-end source extraction system",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def run(args: list[str]) -> str:
    result = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(f"{' '.join(args)} failed:\n{result.stdout}")
    return result.stdout


def assert_terms(label: str, content: str, failures: list[str]) -> None:
    for term in REQUIRED_TERMS:
        if term not in content:
            failures.append(f"{label} missing contract term: {term}")


def assert_route(query: str, failures: list[str]) -> None:
    menu = run([sys.executable, "execution/command_menu.py", "search", query])
    router = run([sys.executable, "execution/workflow_router.py", "search", query])
    allowed = ["/source-to-skill-system", "/extraction-governor-agent", "/autopilot", "/mission", "/self-evolve", "/skill-anneal"]
    combined = menu + "\n" + router
    if not any(route in combined for route in allowed):
        failures.append(f"routing query did not surface a skill-system route: {query}")


def main() -> int:
    failures: list[str] = []

    for path in [PRIMITIVE, WORKFLOW, SOURCE_COMMAND, CODEX_SKILL]:
        if not path.exists():
            failures.append(f"missing file: {path.relative_to(ROOT)}")

    if PRIMITIVE.exists():
        assert_terms("skill-system-contract.md", read(PRIMITIVE), failures)
    if WORKFLOW.exists():
        assert_terms("source-to-skill-system.md", read(WORKFLOW), failures)

    transcript = SOURCE_PACKAGE / "transcript.txt"
    ledger = SOURCE_PACKAGE / "video-context-ledger.md"
    uncertainty = SOURCE_PACKAGE / "uncertainty-report.md"
    for path in [transcript, ledger, uncertainty]:
        if not path.exists():
            failures.append(f"source package missing: {path.relative_to(ROOT)}")
    if transcript.exists() and transcript.stat().st_size < 1000:
        failures.append("source transcript is too small to be a grounded package")

    for query in ROUTING_QUERIES:
        assert_route(query, failures)

    if failures:
        print("Skill-system contract verification: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Skill-system contract verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
