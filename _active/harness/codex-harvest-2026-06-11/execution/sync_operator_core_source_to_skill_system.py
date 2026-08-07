#!/usr/bin/env python3
"""Check or align Source-to-skill-system Operator Core wrappers."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "source-to-skill-system.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-source-to-skill-system" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_SOURCE_TO_SKILL = Path.home() / ".codex" / "skills" / "source-to-skill-system" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-source-to-skill-system" / "SKILL.md"

CANONICAL_PATH = "/Users/farricecain/Codex Antigravity/.agent/workflows/source-to-skill-system.md"

COMMON_REQUIREMENTS = (
    "connected skill systems",
    "not isolated mega-skills",
    "evidence and existing-route fit",
    "Skill System Contract",
    "Agentic Engineering Packet",
    "Goal Packet",
    "companion OS layers",
    "no hot skill promotion",
    "global mirror",
    "external write",
    "new dependency",
    "real Codex subagents require explicit authorization",
    "thin compatibility wrapper",
    "no competing behavior contract",
)

PATH_REQUIREMENTS = {
    PROJECT_WORKFLOW: (
        "canonical source of truth for Source-to-skill-system behavior",
        "turns source material into connected skill systems, not isolated mega-skills",
        "Evidence and existing-route fit come before building",
        "Every build needs the Skill System Contract fields before implementation",
        "Agentic engineering changes require the Agentic Engineering Packet",
        "Self-improvement, maintenance, cleanup, or evolution changes require a Goal Packet",
        "Prefer companion OS layers over duplicate expert skills",
        "Do not create hot skills, global mirrors, external writes, new dependencies, or broad workflow mutations without explicit approval and validation",
        "Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`",
        "Real Codex subagents require explicit authorization",
    ),
    LOCAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        ".agent/workflows/source-to-skill-system.md",
        "canonical behavior source",
    ),
    GLOBAL_AGENTS: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Global Source-to-skill-system Builder",
    ),
    GLOBAL_SOURCE_TO_SKILL: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Project Source Of Truth",
    ),
    GLOBAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "/Users/farricecain/.codex/skills/source-to-skill-system/SKILL.md",
        "compatibility alias",
    ),
}

FORBIDDEN = (
    "giant all-purpose skill by default",
    "isolated mega-skill by default",
    "skip source grounding",
    "create hot skills by default",
    "global mirror by default",
    "external write by default",
    "new dependency by default",
    "broad workflow mutation by default",
)

GLOBAL_AGENTS_BLOCK = f"""## Global Source-to-skill-system Builder

Use the global `source-to-skill-system` skill at `/Users/farricecain/.codex/skills/source-to-skill-system/SKILL.md`
when the user invokes `/source-to-skill-system`,
`source-command-source-to-skill-system`, or asks to turn source material into a
connected Codex skill system, companion OS layer, workflow bridge, validation
loop, or reusable command surface.

The canonical Antigravity Source-to-skill-system workflow is `{CANONICAL_PATH}`.
Global Source-to-skill-system wrappers are thin compatibility wrappers with no
competing behavior contract.

Default behavior: source material becomes connected skill systems, not isolated
mega-skills. Evidence and existing-route fit come before building. Every build
requires the Skill System Contract before implementation. Agentic engineering
changes require an Agentic Engineering Packet; self-improvement, maintenance,
cleanup, or evolution changes require a Goal Packet. Prefer companion OS layers
over duplicate expert skills when improving existing control-plane behavior. Do
not create hot skills, global mirrors, external writes, new dependencies, or
broad workflow mutations without explicit approval and validation. Real Codex
subagents require explicit authorization.

In short: evidence and existing-route fit first, no hot skill promotion, no new
dependency, no competing behavior contract, and no real Codex subagents without
explicit authorization.
"""

GLOBAL_SOURCE_TO_SKILL_TEXT = f"""---
name: source-to-skill-system
description: Global thin compatibility wrapper for Antigravity Source-to-skill-system; delegates to the canonical project workflow.
---

# Source-to-skill-system

## Project Source Of Truth

The canonical Source-to-skill-system behavior source is:

`{CANONICAL_PATH}`

This global skill is a thin compatibility wrapper. It keeps source-to-system,
source material, skill-system, companion OS, workflow bridge, and validation
language discoverable anywhere in Codex, but it must not maintain a competing
behavior contract. When the Antigravity project workflow is available or
relevant, read and follow that workflow first.

## Operator Core Alignment

Preserve the current Source-to-skill-system contract:

- source material becomes connected skill systems, not isolated mega-skills
- evidence and existing-route fit come before building
- every build fills the Skill System Contract before implementation
- Agentic Engineering Packet is required for agentic engineering changes
- Goal Packet is required for self-improvement, maintenance, cleanup, or evolution changes
- companion OS layers are preferred over duplicate expert skills when improving existing control-plane behavior
- no hot skill promotion, global mirror, external write, new dependency, or broad workflow mutation without explicit approval and validation
- repair, drift-audit, and broken-system language routes to `/system-audit` or `/autopilot`
- real Codex subagents require explicit authorization
- this global skill stays a thin compatibility wrapper with no competing behavior contract
"""

GLOBAL_WRAPPER_TEXT = f"""---
name: source-command-source-to-skill-system
description: Global compatibility alias for /source-to-skill-system; follows the Antigravity source-to-system source of truth.
---

# source-command-source-to-skill-system

This is a compatibility alias for the global Source-to-skill-system wrapper.
When invoked, load and follow:

`/Users/farricecain/.codex/skills/source-to-skill-system/SKILL.md`

If the current work is inside Antigravity or the user is discussing the
Antigravity harness, also load the canonical project workflow:

`{CANONICAL_PATH}`

## Operator Core Alignment

This wrapper is intentionally a thin compatibility wrapper. It must preserve the
current Source-to-skill-system contract: connected skill systems, not isolated
mega-skills, evidence and existing-route fit first, Skill System Contract,
Agentic Engineering Packet, Goal Packet, companion OS layers, no hot skill
promotion, global mirror, external write, new dependency, or broad workflow
mutation without explicit approval and validation, real Codex subagents require
explicit authorization, and no competing behavior contract.
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
    if "## Global Source-to-skill-system Builder" in text:
        return re.sub(
            r"## Global Source-to-skill-system Builder\n.*?(?=\n## Global Skill-anneal Prompt Repair|\n## Global Self-evolve Evolution|\n## Native Codex Artifact Default)",
            GLOBAL_AGENTS_BLOCK.rstrip() + "\n\n",
            text,
            count=1,
            flags=re.DOTALL,
        )
    anchor = "## Global Skill-anneal Prompt Repair"
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
    if not GLOBAL_SOURCE_TO_SKILL.exists() or read(GLOBAL_SOURCE_TO_SKILL) != GLOBAL_SOURCE_TO_SKILL_TEXT.rstrip() + "\n":
        write(GLOBAL_SOURCE_TO_SKILL, GLOBAL_SOURCE_TO_SKILL_TEXT)
        changed.append(str(GLOBAL_SOURCE_TO_SKILL))
    if not GLOBAL_WRAPPER.exists() or read(GLOBAL_WRAPPER) != GLOBAL_WRAPPER_TEXT.rstrip() + "\n":
        write(GLOBAL_WRAPPER, GLOBAL_WRAPPER_TEXT)
        changed.append(str(GLOBAL_WRAPPER))
    return changed


def check_alignment() -> list[str]:
    failures: list[str] = []
    for label, path in (
        ("project workflow", PROJECT_WORKFLOW),
        ("local source-command-source-to-skill-system", LOCAL_WRAPPER),
        ("global AGENTS", GLOBAL_AGENTS),
        ("global source-to-skill-system", GLOBAL_SOURCE_TO_SKILL),
        ("global source-command-source-to-skill-system", GLOBAL_WRAPPER),
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
                failures.append(f"{label} contains stale Source-to-skill-system contract: {snippet}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Check or align Source-to-skill-system Operator Core wrappers.")
    parser.add_argument("--apply", action="store_true", help="Update global Source-to-skill-system surfaces.")
    parser.add_argument("--check", action="store_true", help="Check alignment only.")
    args = parser.parse_args()
    if args.apply:
        changed = apply_alignment()
        print("SOURCE-TO-SKILL-SYSTEM OPERATOR CORE ALIGNMENT APPLIED")
        print("- changed: " + (", ".join(changed) if changed else "none"))
    failures = check_alignment()
    if failures:
        print("SOURCE-TO-SKILL-SYSTEM OPERATOR CORE ALIGNMENT FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("SOURCE-TO-SKILL-SYSTEM OPERATOR CORE ALIGNMENT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
