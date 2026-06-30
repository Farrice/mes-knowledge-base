#!/usr/bin/env python3
"""Check or align Expert-composition-governor Operator Core wrappers."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "expert-composition-governor.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-expert-composition-governor" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_EXPERT_COMPOSITION = Path.home() / ".codex" / "skills" / "expert-composition-governor" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-expert-composition-governor" / "SKILL.md"

CANONICAL_PATH = "/Users/farricecain/Codex Antigravity/.agent/workflows/expert-composition-governor.md"

COMMON_REQUIREMENTS = (
    "prevent expert soup",
    "full-arsenal sprawl",
    "more than three experts/routes",
    "one function owner",
    "bounded slots",
    "Composition Ledger",
    "evidence of change",
    "expert names are not proof",
    "no real Codex subagents unless explicitly authorized",
    "thin compatibility wrapper",
    "no competing behavior contract",
)

PATH_REQUIREMENTS = {
    PROJECT_WORKFLOW: (
        "canonical source of truth for Expert-composition-governor behavior",
        "prevents expert soup and full-arsenal sprawl",
        "more than three experts/routes are plausible",
        "One function owner must integrate the final result",
        "Specialists must occupy bounded slots",
        "The Composition Ledger must show accepted, skipped, or rejected contributions with evidence of change",
        "Expert names are not proof; integration evidence is proof",
        "Do not spawn real Codex subagents unless explicitly authorized",
        "Route broad broken-harness triage to `/autopilot` or `/system-audit`",
    ),
    LOCAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        ".agent/workflows/expert-composition-governor.md",
        "canonical behavior source",
    ),
    GLOBAL_AGENTS: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Global Expert-composition Governor",
    ),
    GLOBAL_EXPERT_COMPOSITION: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Project Source Of Truth",
    ),
    GLOBAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "/Users/farricecain/.codex/skills/expert-composition-governor/SKILL.md",
        "compatibility alias",
    ),
}

FORBIDDEN = (
    "spawn subagents by default",
    "full arsenal by default",
    "experts are proof",
)

GLOBAL_AGENTS_BLOCK = f"""## Global Expert-composition Governor

Use the global `expert-composition-governor` skill at `/Users/farricecain/.codex/skills/expert-composition-governor/SKILL.md`
when the user invokes `/expert-composition-governor`,
`source-command-expert-composition-governor`, says expert soup, too many agents,
not interwoven, full arsenal, one-man army, or when more than three
experts/routes are plausible.

The canonical Antigravity Expert-composition-governor workflow is
`{CANONICAL_PATH}`. Global Expert-composition-governor wrappers are thin
compatibility wrappers with no competing behavior contract.

Default behavior: prevent expert soup and full-arsenal sprawl. Choose one
function owner, assign bounded slots, require a Composition Ledger, and prove
integration with evidence of change. expert names are not proof; integration
evidence is proof. no real Codex subagents unless explicitly authorized. Route
broad broken-harness triage to `/autopilot` or `/system-audit`; route reusable
source-to-system builds to `/source-to-skill-system`.
"""

GLOBAL_EXPERT_COMPOSITION_TEXT = f"""---
name: expert-composition-governor
description: Global thin compatibility wrapper for Antigravity Expert-composition-governor; delegates to the canonical project workflow.
---

# Expert-composition-governor

## Project Source Of Truth

The canonical Expert-composition-governor behavior source is:

`{CANONICAL_PATH}`

This global skill is a thin compatibility wrapper. It keeps expert soup,
full-arsenal, one-man army, multi-expert composition, and bounded specialist
slot language discoverable anywhere in Codex, but it must not maintain a
competing behavior contract. When the Antigravity project workflow is available
or relevant, read and follow that workflow first.

## Operator Core Alignment

Preserve the current Expert-composition-governor contract:

- prevent expert soup and full-arsenal sprawl
- use when more than three experts/routes are plausible or the user asks for the full arsenal
- one function owner integrates the final result
- specialists occupy bounded slots and return specific contributions, preservation notes, and downstream risk
- Composition Ledger shows accepted, skipped, or rejected contributions with evidence of change
- expert names are not proof; integration evidence is proof
- no real Codex subagents unless explicitly authorized
- broad broken-harness triage routes to `/autopilot` or `/system-audit`
- reusable source-to-system builds route to `/source-to-skill-system`
- this global skill stays a thin compatibility wrapper with no competing behavior contract
"""

GLOBAL_WRAPPER_TEXT = f"""---
name: source-command-expert-composition-governor
description: Global compatibility alias for /expert-composition-governor; follows the Antigravity composition source of truth.
---

# source-command-expert-composition-governor

This is a compatibility alias for the global Expert-composition-governor wrapper.
When invoked, load and follow:

`/Users/farricecain/.codex/skills/expert-composition-governor/SKILL.md`

If the current work is inside Antigravity or the user is discussing the
Antigravity harness, also load the canonical project workflow:

`{CANONICAL_PATH}`

## Operator Core Alignment

This wrapper is intentionally a thin compatibility wrapper. It must preserve the
current Expert-composition-governor contract: prevent expert soup and
full-arsenal sprawl, more than three experts/routes triggers composition, one
function owner, bounded slots, Composition Ledger, evidence of change, expert
names are not proof, no real Codex subagents unless explicitly authorized, and
no competing behavior contract.
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
    if "## Global Expert-composition Governor" in text:
        return re.sub(
            r"## Global Expert-composition Governor\n.*?(?=\n## Global Repeatability-spine Regression Repair|\n## Global System-audit Control Plane|\n## Native Codex Artifact Default)",
            GLOBAL_AGENTS_BLOCK.rstrip() + "\n\n",
            text,
            count=1,
            flags=re.DOTALL,
        )
    anchor = "## Global Repeatability-spine Regression Repair"
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
    if not GLOBAL_EXPERT_COMPOSITION.exists() or read(GLOBAL_EXPERT_COMPOSITION) != GLOBAL_EXPERT_COMPOSITION_TEXT.rstrip() + "\n":
        write(GLOBAL_EXPERT_COMPOSITION, GLOBAL_EXPERT_COMPOSITION_TEXT)
        changed.append(str(GLOBAL_EXPERT_COMPOSITION))
    if not GLOBAL_WRAPPER.exists() or read(GLOBAL_WRAPPER) != GLOBAL_WRAPPER_TEXT.rstrip() + "\n":
        write(GLOBAL_WRAPPER, GLOBAL_WRAPPER_TEXT)
        changed.append(str(GLOBAL_WRAPPER))
    return changed


def check_alignment() -> list[str]:
    failures: list[str] = []
    for label, path in (
        ("project workflow", PROJECT_WORKFLOW),
        ("local source-command-expert-composition-governor", LOCAL_WRAPPER),
        ("global AGENTS", GLOBAL_AGENTS),
        ("global expert-composition-governor", GLOBAL_EXPERT_COMPOSITION),
        ("global source-command-expert-composition-governor", GLOBAL_WRAPPER),
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
                failures.append(f"{label} contains stale Expert-composition-governor contract: {snippet}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Check or align Expert-composition-governor Operator Core wrappers.")
    parser.add_argument("--apply", action="store_true", help="Update global Expert-composition-governor surfaces.")
    parser.add_argument("--check", action="store_true", help="Check alignment only.")
    args = parser.parse_args()
    if args.apply:
        changed = apply_alignment()
        print("EXPERT-COMPOSITION-GOVERNOR OPERATOR CORE ALIGNMENT APPLIED")
        print("- changed: " + (", ".join(changed) if changed else "none"))
    failures = check_alignment()
    if failures:
        print("EXPERT-COMPOSITION-GOVERNOR OPERATOR CORE ALIGNMENT FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("EXPERT-COMPOSITION-GOVERNOR OPERATOR CORE ALIGNMENT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
