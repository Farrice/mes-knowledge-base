#!/usr/bin/env python3
"""Check or align Skill-anneal Operator Core wrappers."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "skill-anneal.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-skill-anneal" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_SKILL_ANNEAL = Path.home() / ".codex" / "skills" / "skill-anneal" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-skill-anneal" / "SKILL.md"

CANONICAL_PATH = "/Users/farricecain/Codex Antigravity/.agent/workflows/skill-anneal.md"

COMMON_REQUIREMENTS = (
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
    "thin compatibility wrapper",
    "no competing behavior contract",
)

PATH_REQUIREMENTS = {
    PROJECT_WORKFLOW: (
        "canonical source of truth for Skill-anneal behavior",
        "prompt-level skill/component annealing",
        "Incomplete or vague goal packets produce a queue-only diagnosis",
        "Annealing requires a target skill directory, failure examples, rubric/test-input set, proof artifact, measurable stop condition, turn cap, and explicit no-regression clause",
        "preserve upstream input, downstream output, and validation contract",
        "Limit edits to the single weakest criterion unless the user approves a broader rewrite",
        "Side effects must be local, reversible, and inside `/Users/farricecain/Codex Antigravity`",
        "Stop at a human checkpoint for broader workflow evolution, global mirrors, external actions, broad archive/delete, destructive cleanup, new dependencies, failed validation, or Mission repair",
        "Route broad workflow evolution to `/self-evolve`",
        "Real Codex subagents require explicit authorization",
    ),
    LOCAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        ".agent/workflows/skill-anneal.md",
        "canonical behavior source",
    ),
    GLOBAL_AGENTS: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Global Skill-anneal Prompt Repair",
    ),
    GLOBAL_SKILL_ANNEAL: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Project Source Of Truth",
    ),
    GLOBAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "/Users/farricecain/.codex/skills/skill-anneal/SKILL.md",
        "compatibility alias",
    ),
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

GLOBAL_AGENTS_BLOCK = f"""## Global Skill-anneal Prompt Repair

Use the global `skill-anneal` skill at `/Users/farricecain/.codex/skills/skill-anneal/SKILL.md`
when the user invokes `/skill-anneal`, `source-command-skill-anneal`, or asks to
anneal a specific skill prompt, repair a SKILL.md component with failure
examples, or tune one skill-system component without rewriting the whole
workflow.

The canonical Antigravity Skill-anneal workflow is `{CANONICAL_PATH}`. Global
Skill-anneal wrappers are thin compatibility wrappers with no competing
behavior contract.

Default behavior: prompt-level skill/component annealing. Incomplete or vague
goal packets produce queue-only diagnosis and missing fields. Annealing requires
target skill directory, failure examples, rubric/test-input set, proof artifact,
measurable stop condition, turn cap, and explicit no-regression clause. Limit
edits to the single weakest criterion unless Farrice approves broader rewrite.
Side effects must be local, reversible, and inside
`/Users/farricecain/Codex Antigravity`. Use `/self-evolve` for broad workflow
evolution. Stop at a human checkpoint for global mirrors, external actions,
broad archive/delete, destructive cleanup, new dependencies, failed validation,
or Mission repair. Real Codex subagents require explicit authorization.
"""

GLOBAL_SKILL_ANNEAL_TEXT = f"""---
name: skill-anneal
description: Global thin compatibility wrapper for Antigravity Skill-anneal; delegates to the canonical project workflow.
---

# Skill-anneal

## Project Source Of Truth

The canonical Skill-anneal behavior source is:

`{CANONICAL_PATH}`

This global skill is a thin compatibility wrapper. It keeps `/skill-anneal`,
prompt annealing, SKILL.md component repair, and rubric/test-input language
discoverable anywhere in Codex, but it must not maintain a competing behavior
contract. When the Antigravity project workflow is available or relevant, read
and follow that workflow first.

## Operator Core Alignment

Preserve the current Skill-anneal contract:

- prompt-level skill/component annealing, not broad workflow evolution
- incomplete or vague goal packets produce queue-only diagnosis and missing fields
- annealing requires target skill directory, failure examples, rubric/test-input set, proof artifact, measurable stop condition, turn cap, and explicit no-regression clause
- preserve upstream input, downstream output, and validation contract for larger skill systems
- limit edits to the single weakest criterion unless Farrice approves broader rewrite
- side effects must be local, reversible, and inside `/Users/farricecain/Codex Antigravity`
- human checkpoint for broader workflow evolution, global mirrors, external actions, broad archive/delete, destructive cleanup, new dependencies, failed validation, or Mission repair
- broad workflow evolution routes to `/self-evolve`; repair, drift-audit, and broken-system language routes to `/system-audit` or `/autopilot`
- real Codex subagents require explicit authorization
- this global skill stays a thin compatibility wrapper with no competing behavior contract
"""

GLOBAL_WRAPPER_TEXT = f"""---
name: source-command-skill-anneal
description: Global compatibility alias for /skill-anneal; follows the Antigravity prompt-annealing source of truth.
---

# source-command-skill-anneal

This is a compatibility alias for the global Skill-anneal wrapper. When invoked,
load and follow:

`/Users/farricecain/.codex/skills/skill-anneal/SKILL.md`

If the current work is inside Antigravity or the user is discussing the
Antigravity harness, also load the canonical project workflow:

`{CANONICAL_PATH}`

## Operator Core Alignment

This wrapper is intentionally a thin compatibility wrapper. It must preserve the
current Skill-anneal contract: prompt-level skill/component annealing,
queue-only diagnosis for incomplete or vague goal packets, target skill
directory, failure examples, rubric/test-input set, proof artifact, measurable
stop condition, turn cap, explicit no-regression clause, single weakest
criterion, local and reversible side effects, human checkpoint for risky
changes, broad workflow evolution routes to `/self-evolve`, real Codex
subagents require explicit authorization, and no competing behavior contract.

In short: side effects must be local, reversible, and bounded by the canonical
workflow.
"""


def read(path: Path) -> str:
    if not path.exists():
        raise AssertionError(f"Missing required file: {path}")
    return path.read_text(encoding="utf-8")


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def normalize(text: str) -> str:
    return re.sub(r"\s+", " ", text)


def align_global_agents(text: str) -> str:
    if "## Global Skill-anneal Prompt Repair" in text:
        return re.sub(
            r"## Global Skill-anneal Prompt Repair\n.*?(?=\n## Global Self-evolve Evolution|\n## Global Knowledge-librarian Pulse|\n## Native Codex Artifact Default)",
            GLOBAL_AGENTS_BLOCK.rstrip() + "\n\n",
            text,
            count=1,
            flags=re.DOTALL,
        )
    anchor = "## Global Self-evolve Evolution"
    if anchor in text:
        return text.replace(anchor, GLOBAL_AGENTS_BLOCK.rstrip() + "\n\n" + anchor, 1)
    return text.rstrip() + "\n\n" + GLOBAL_AGENTS_BLOCK.rstrip() + "\n"


def apply_alignment() -> list[str]:
    changed: list[str] = []

    original_agents = read(GLOBAL_AGENTS)
    updated_agents = align_global_agents(original_agents)
    if updated_agents != original_agents:
        write(GLOBAL_AGENTS, updated_agents)
        changed.append(str(GLOBAL_AGENTS))

    if not GLOBAL_SKILL_ANNEAL.exists() or read(GLOBAL_SKILL_ANNEAL) != GLOBAL_SKILL_ANNEAL_TEXT.rstrip() + "\n":
        write(GLOBAL_SKILL_ANNEAL, GLOBAL_SKILL_ANNEAL_TEXT)
        changed.append(str(GLOBAL_SKILL_ANNEAL))

    if not GLOBAL_WRAPPER.exists() or read(GLOBAL_WRAPPER) != GLOBAL_WRAPPER_TEXT.rstrip() + "\n":
        write(GLOBAL_WRAPPER, GLOBAL_WRAPPER_TEXT)
        changed.append(str(GLOBAL_WRAPPER))

    return changed


def check_alignment() -> list[str]:
    failures: list[str] = []
    for label, path in (
        ("project workflow", PROJECT_WORKFLOW),
        ("local source-command-skill-anneal", LOCAL_WRAPPER),
        ("global AGENTS", GLOBAL_AGENTS),
        ("global skill-anneal", GLOBAL_SKILL_ANNEAL),
        ("global source-command-skill-anneal", GLOBAL_WRAPPER),
    ):
        if not path.exists():
            failures.append(f"{label} missing: {path}")
            continue
        text = read(path)
        normalized = normalize(text)
        for snippet in PATH_REQUIREMENTS[path]:
            if normalize(snippet) not in normalized:
                failures.append(f"{label} missing: {snippet}")
        for snippet in FORBIDDEN:
            if snippet.lower() in text.lower():
                failures.append(f"{label} contains stale Skill-anneal contract: {snippet}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Check or align Skill-anneal Operator Core wrappers.")
    parser.add_argument("--apply", action="store_true", help="Update global Skill-anneal surfaces.")
    parser.add_argument("--check", action="store_true", help="Check alignment only.")
    args = parser.parse_args()

    if args.apply:
        changed = apply_alignment()
        print("SKILL-ANNEAL OPERATOR CORE ALIGNMENT APPLIED")
        print("- changed: " + (", ".join(changed) if changed else "none"))

    failures = check_alignment()
    if failures:
        print("SKILL-ANNEAL OPERATOR CORE ALIGNMENT FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("SKILL-ANNEAL OPERATOR CORE ALIGNMENT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
