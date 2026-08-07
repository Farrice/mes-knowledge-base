#!/usr/bin/env python3
"""Check or align Extraction-governor-agent Operator Core wrappers."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "extraction-governor-agent.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-extraction-governor-agent" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_EXTRACTION = Path.home() / ".codex" / "skills" / "extraction-governor-agent" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-extraction-governor-agent" / "SKILL.md"

CANONICAL_PATH = "/Users/farricecain/Codex Antigravity/.agent/workflows/extraction-governor-agent.md"

COMMON_REQUIREMENTS = (
    "source-to-capability triage",
    "read-only triage",
    "source grounding before synthesis",
    "existing-route and duplicate-system checks",
    "no state writes",
    "hot skill promotion",
    "global mirrors",
    "paid/quota-heavy tools",
    "external source fetches",
    "workflow mutation",
    "/source-to-skill-system",
    "/knowledge-librarian",
    "/plugin-readiness-audit",
    "real Codex subagents require explicit authorization",
    "thin compatibility wrapper",
    "no competing behavior contract",
)

PATH_REQUIREMENTS = {
    PROJECT_WORKFLOW: (
        "canonical source of truth for Extraction-governor-agent behavior",
        "owns source-to-capability triage and routing, not isolated summarization or collection",
        "Default mode is read-only triage",
        "Preserve source grounding before synthesis",
        "Run existing-route and duplicate-system checks before recommending a new skill, workflow, agent, command bridge, or knowledge artifact",
        "Do not write `.agent/extraction-governor-agent-state.md`, create artifacts, promote hot skills, mirror global files, use paid/quota-heavy tools, fetch external sources, or mutate workflows unless explicitly requested and validated",
        "Hand off connected skill-system or orchestration builds to `/source-to-skill-system`",
        "overlap or prior-decision questions to `/knowledge-librarian`",
        "travel/plugin packaging decisions to `/plugin-readiness-audit`",
        "Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`",
        "Real Codex subagents require explicit authorization",
    ),
    LOCAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        ".agent/workflows/extraction-governor-agent.md",
        "canonical behavior source",
    ),
    GLOBAL_AGENTS: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Global Extraction-governor-agent Source Triage",
    ),
    GLOBAL_EXTRACTION: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Project Source Of Truth",
    ),
    GLOBAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "/Users/farricecain/.codex/skills/extraction-governor-agent/SKILL.md",
        "compatibility alias",
    ),
}

FORBIDDEN = (
    "knowledge_compiler.py briefing",
    "automatically update lightweight state",
    "automatically write state",
    "create artifacts by default",
    "promote hot skills by default",
    "global mirror by default",
    "external source fetch by default",
    "paid tool by default",
    "workflow mutation by default",
    "spawn subagents by default",
)

GLOBAL_AGENTS_BLOCK = f"""## Global Extraction-governor-agent Source Triage

Use the global `extraction-governor-agent` skill at `/Users/farricecain/.codex/skills/extraction-governor-agent/SKILL.md`
when the user invokes `/extraction-governor-agent`,
`source-command-extraction-governor-agent`, asks for extraction governance,
source triage, hidden mechanics, duplicate-system avoidance, source-to-capability
routing, or a decision about whether source material should become a reference,
workflow, companion skill, command bridge, agent, knowledge artifact, or business
asset.

The canonical Antigravity Extraction-governor-agent workflow is
`{CANONICAL_PATH}`. Global Extraction-governor-agent wrappers are thin
compatibility wrappers with no competing behavior contract.

Default behavior: read-only triage for source-to-capability triage. Preserve
source grounding before synthesis, run existing-route and duplicate-system
checks, classify build shape, expose risks, and recommend the next executable
path. no state writes, artifact creation, hot skill promotion, global mirrors,
paid/quota-heavy tools, external source fetches, or workflow mutation unless
explicitly requested and validated. Hand off connected skill-system or orchestration builds to
`/source-to-skill-system`, overlap or prior-decision questions to
`/knowledge-librarian`, and travel/plugin packaging decisions to
`/plugin-readiness-audit`. Route repair, drift-audit, and broken-system language
to `/system-audit` or `/autopilot`. Real Codex subagents require explicit
authorization.
"""

GLOBAL_EXTRACTION_TEXT = f"""---
name: extraction-governor-agent
description: Global thin compatibility wrapper for Antigravity Extraction-governor-agent; delegates to the canonical project workflow.
---

# Extraction-governor-agent

## Project Source Of Truth

The canonical Extraction-governor-agent behavior source is:

`{CANONICAL_PATH}`

This global skill is a thin compatibility wrapper. It keeps extraction
governance, source-to-capability triage, hidden mechanics, duplicate-system
avoidance, and build-shape decision language discoverable anywhere in Codex,
but it must not maintain a competing behavior contract. When the Antigravity
project workflow is available or relevant, read and follow that workflow first.

## Operator Core Alignment

Preserve the current Extraction-governor-agent contract:

- source-to-capability triage and routing, not isolated summarization or collection
- read-only triage by default: source pointer, arsenal route, build-shape decision, risks, and next executable path
- source grounding before synthesis; unavailable source evidence is marked, not invented
- existing-route and duplicate-system checks before recommending a new skill, workflow, agent, command bridge, or knowledge artifact
- no state writes, artifact creation, hot skill promotion, global mirrors, paid/quota-heavy tools, external source fetches, or workflow mutation unless explicitly requested and validated
- connected skill-system or orchestration builds route to `/source-to-skill-system`
- overlap or prior-decision questions route to `/knowledge-librarian`
- travel/plugin packaging decisions route to `/plugin-readiness-audit`
- repair, drift-audit, and broken-system language routes to `/system-audit` or `/autopilot`
- real Codex subagents require explicit authorization
- this global skill stays a thin compatibility wrapper with no competing behavior contract
"""

GLOBAL_WRAPPER_TEXT = f"""---
name: source-command-extraction-governor-agent
description: Global compatibility alias for /extraction-governor-agent; follows the Antigravity extraction source of truth.
---

# source-command-extraction-governor-agent

This is a compatibility alias for the global Extraction-governor-agent wrapper.
When invoked, load and follow:

`/Users/farricecain/.codex/skills/extraction-governor-agent/SKILL.md`

If the current work is inside Antigravity or the user is discussing the
Antigravity harness, also load the canonical project workflow:

`{CANONICAL_PATH}`

## Operator Core Alignment

This wrapper is intentionally a thin compatibility wrapper. It must preserve the
current Extraction-governor-agent contract: source-to-capability triage,
read-only triage, source grounding before synthesis, existing-route and
duplicate-system checks, no state writes, no hot skill promotion, no global
mirrors, no paid/quota-heavy tools, no external source fetches, no workflow
mutation unless explicitly requested and validated, `/source-to-skill-system`,
`/knowledge-librarian`, `/plugin-readiness-audit`, real Codex subagents require
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
    if "## Global Extraction-governor-agent Source Triage" in text:
        return re.sub(
            r"## Global Extraction-governor-agent Source Triage\n.*?(?=\n## Global Source-to-skill-system Builder|\n## Global Skill-anneal Prompt Repair|\n## Native Codex Artifact Default)",
            GLOBAL_AGENTS_BLOCK.rstrip() + "\n\n",
            text,
            count=1,
            flags=re.DOTALL,
        )
    anchor = "## Global Source-to-skill-system Builder"
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
    if not GLOBAL_EXTRACTION.exists() or read(GLOBAL_EXTRACTION) != GLOBAL_EXTRACTION_TEXT.rstrip() + "\n":
        write(GLOBAL_EXTRACTION, GLOBAL_EXTRACTION_TEXT)
        changed.append(str(GLOBAL_EXTRACTION))
    if not GLOBAL_WRAPPER.exists() or read(GLOBAL_WRAPPER) != GLOBAL_WRAPPER_TEXT.rstrip() + "\n":
        write(GLOBAL_WRAPPER, GLOBAL_WRAPPER_TEXT)
        changed.append(str(GLOBAL_WRAPPER))
    return changed


def check_alignment() -> list[str]:
    failures: list[str] = []
    for label, path in (
        ("project workflow", PROJECT_WORKFLOW),
        ("local source-command-extraction-governor-agent", LOCAL_WRAPPER),
        ("global AGENTS", GLOBAL_AGENTS),
        ("global extraction-governor-agent", GLOBAL_EXTRACTION),
        ("global source-command-extraction-governor-agent", GLOBAL_WRAPPER),
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
                failures.append(f"{label} contains stale Extraction-governor-agent contract: {snippet}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Check or align Extraction-governor-agent Operator Core wrappers.")
    parser.add_argument("--apply", action="store_true", help="Update global Extraction-governor-agent surfaces.")
    parser.add_argument("--check", action="store_true", help="Check alignment only.")
    args = parser.parse_args()
    if args.apply:
        changed = apply_alignment()
        print("EXTRACTION-GOVERNOR-AGENT OPERATOR CORE ALIGNMENT APPLIED")
        print("- changed: " + (", ".join(changed) if changed else "none"))
    failures = check_alignment()
    if failures:
        print("EXTRACTION-GOVERNOR-AGENT OPERATOR CORE ALIGNMENT FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("EXTRACTION-GOVERNOR-AGENT OPERATOR CORE ALIGNMENT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
