#!/usr/bin/env python3
"""Verify the Expert Composition Standard bridge and integrations."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]

FILES = {
    "primitive": ROOT / "semantic_libraries" / "antigravity" / "primitives" / "expert-composition-contract.md",
    "workflow": ROOT / ".agent" / "workflows" / "expert-composition-governor.md",
    "codex_skill": ROOT / ".agents" / "skills" / "source-command-expert-composition-governor" / "SKILL.md",
    "source_command": ROOT / ".claude" / "commands" / "expert-composition-governor.md",
    "solution": ROOT / "docs" / "solutions" / "expert-composition-standard.md",
    "codex": ROOT / "CODEX.md",
    "mission": ROOT / ".agent" / "workflows" / "mission.md",
    "autopilot": ROOT / ".agent" / "workflows" / "autopilot.md",
    "orchestrate": ROOT / ".agent" / "workflows" / "orchestrate.md",
    "routing_governor": ROOT / "execution" / "routing_governor.py",
    "arsenal": ROOT / "semantic_libraries" / "antigravity" / "primitives" / "agent-arsenal-routing-contract.md",
    "skill_system": ROOT / "semantic_libraries" / "antigravity" / "primitives" / "skill-system-contract.md",
}

REQUIRED_PRIMITIVE_TERMS = [
    "Expert Soup Signals",
    "One owner, bounded experts, explicit handoffs",
    "Contribution Slots",
    "Specialist Handoff",
    "Integration Pass",
    "Composition Ledger",
    "Score Discipline",
    "Fail Conditions",
]

INTEGRATION_TERMS = [
    "/expert-composition-governor",
    "expert-composition-contract.md",
]

ROUTING_QUERIES = [
    "expert soup too many agents not interwoven",
    "compose experts full arsenal end to end",
    "hammer instead of scalpel many skills workflows",
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


def main() -> int:
    failures: list[str] = []

    for label, path in FILES.items():
        if not path.exists():
            failures.append(f"missing {label}: {path.relative_to(ROOT)}")

    if FILES["primitive"].exists():
        content = read(FILES["primitive"])
        for term in REQUIRED_PRIMITIVE_TERMS:
            if term not in content:
                failures.append(f"primitive missing term: {term}")

    if FILES["workflow"].exists():
        workflow = read(FILES["workflow"])
        for term in ["Function Owner", "Fill Contribution Slots", "Composition Ledger", "expert soup"]:
            if term not in workflow:
                failures.append(f"workflow missing term: {term}")

    for label in ["codex", "mission", "autopilot", "orchestrate", "arsenal", "skill_system"]:
        if not FILES[label].exists():
            continue
        content = read(FILES[label])
        if not any(term in content for term in INTEGRATION_TERMS):
            failures.append(f"{label} missing expert composition integration")

    if FILES["routing_governor"].exists():
        governor = read(FILES["routing_governor"])
        for term in [
            "EXPERT_COMPOSITION_STACK",
            "EXPERT_COMPOSITION_SIGNALS",
            "is_expert_composition_intent",
            "expert_composition_route_bonus",
        ]:
            if term not in governor:
                failures.append(f"routing governor missing term: {term}")

    skill_text = read(FILES["codex_skill"]) if FILES["codex_skill"].exists() else ""
    for trigger in ["expert soup", "too many agents", "not interwoven", "full arsenal"]:
        if trigger not in skill_text:
            failures.append(f"codex skill missing trigger: {trigger}")

    for query in ROUTING_QUERIES:
        menu = run([sys.executable, "execution/command_menu.py", "search", query])
        router = run([sys.executable, "execution/workflow_router.py", "search", query])
        combined = menu + "\n" + router
        if "/expert-composition-governor" not in combined:
            failures.append(f"routing query did not surface /expert-composition-governor: {query}")

    governor_eval = run([
        sys.executable,
        "execution/routing_governor.py",
        "evaluate",
        "hammer instead of scalpel many skills workflows",
    ])
    if "Detected lane**: expert-composition" not in governor_eval:
        failures.append("routing governor did not detect expert-composition lane")
    if "Chosen route**: /expert-composition-governor" not in governor_eval:
        failures.append("routing governor did not choose /expert-composition-governor")

    if failures:
        print("Expert Composition Standard verification: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Expert Composition Standard verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
