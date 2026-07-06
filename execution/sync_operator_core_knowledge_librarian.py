#!/usr/bin/env python3
"""Check or align Knowledge-librarian Operator Core wrappers."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "knowledge-librarian.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-knowledge-librarian" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_KNOWLEDGE_LIBRARIAN = Path.home() / ".codex" / "skills" / "knowledge-librarian" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-knowledge-librarian" / "SKILL.md"

CANONICAL_PATH = "/Users/farricecain/Google Antigravity/.agent/workflows/knowledge-librarian.md"

COMMON_REQUIREMENTS = (
    "compact session-start knowledge pulse",
    "read-only default scans",
    "knowledge_compiler.py stats",
    "knowledge_compiler.py solutions",
    "--stdout",
    "existing compiled briefing",
    "local evidence",
    "no state snapshot",
    "Mission mutation",
    "cleanup",
    "real Codex subagents require explicit authorization",
    "thin compatibility wrapper",
    "no competing behavior contract",
)

PATH_REQUIREMENTS = {
    PROJECT_WORKFLOW: (
        "canonical source of truth for Knowledge-librarian behavior",
        "compact session-start knowledge pulse by default",
        "python3 execution/knowledge_compiler.py stats",
        'python3 execution/knowledge_compiler.py solutions "[focus]" --top 8 --stdout',
        "Read `knowledge/compiled/briefing.md` if it exists",
        "do not generate or refresh the briefing by default",
        "Do not write `.agent/knowledge-librarian-state.md`, refresh compiled knowledge, create solution docs, mutate Mission, perform cleanup, or mirror global files unless explicitly requested",
        "Route repair, drift-audit, and broken-system language to `/system-audit` or `/autopilot`",
        "Real Codex subagents require explicit authorization",
    ),
    LOCAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        ".agent/workflows/knowledge-librarian.md",
        "canonical behavior source",
    ),
    GLOBAL_AGENTS: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Global Knowledge-librarian Pulse",
    ),
    GLOBAL_KNOWLEDGE_LIBRARIAN: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Project Source Of Truth",
    ),
    GLOBAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "/Users/farricecain/.codex/skills/knowledge-librarian/SKILL.md",
        "compatibility alias",
    ),
}

FORBIDDEN = (
    "python execution/knowledge_compiler.py",
    "python3 execution/knowledge_compiler.py briefing\n",
    "python3 execution/knowledge_compiler.py solutions \"[focus]\" --top 8\n",
    "After producing the Library Pulse, update `.agent/knowledge-librarian-state.md`",
    "write state by default",
    "refresh compiled knowledge by default",
    "create solution docs by default",
    "mutate Mission by default",
    "repair Mission by default",
)

GLOBAL_AGENTS_BLOCK = f"""## Global Knowledge-librarian Pulse

Use the global `knowledge-librarian` skill at `/Users/farricecain/.codex/skills/knowledge-librarian/SKILL.md`
when the user invokes `/knowledge-librarian`, `source-command-knowledge-librarian`,
`library pulse`, `session start pulse`, asks for prior decisions, reusable
solution docs, underused workflows, sleeping giants, or one grounded start
command from the library.

The canonical Antigravity Knowledge-librarian workflow is `{CANONICAL_PATH}`.
Global Knowledge-librarian wrappers are thin compatibility wrappers with no
competing behavior contract.

Default behavior: produce a compact session-start knowledge pulse using
read-only default scans: `knowledge_compiler.py stats` and
`knowledge_compiler.py solutions ... --stdout`. Read the existing compiled
briefing when available; do not refresh compiled knowledge, write a state
snapshot, create solution docs, mutate Mission, perform cleanup, or use real
Codex subagents without explicit authorization. Route repair, drift-audit, and
broken-system language to `/system-audit` or `/autopilot`.

In short: every named capability must be grounded in local evidence, with no
state snapshot, no competing behavior contract, and no real Codex subagents
without explicit authorization.
"""

GLOBAL_KNOWLEDGE_LIBRARIAN_TEXT = f"""---
name: knowledge-librarian
description: Global thin compatibility wrapper for Antigravity Knowledge-librarian pulses; delegates to the canonical project workflow.
---

# Knowledge-librarian

## Project Source Of Truth

The canonical Knowledge-librarian behavior source is:

`{CANONICAL_PATH}`

This global skill is a thin compatibility wrapper. It keeps
`/knowledge-librarian`, library pulse, reusable-context, prior-decision,
solution-doc, and underused-workflow language discoverable anywhere in Codex,
but it must not maintain a competing behavior contract. When the Antigravity
project workflow is available or relevant, read and follow that workflow first.

## Operator Core Alignment

Preserve the current Knowledge-librarian contract:

- `/knowledge-librarian` is a compact session-start knowledge pulse by default
- use read-only default scans with `knowledge_compiler.py stats` and `knowledge_compiler.py solutions ... --stdout`
- read existing compiled briefing when available; do not refresh it by default
- every named capability must be grounded in local evidence
- no state snapshot, compiled knowledge refresh, solution-doc creation, Mission mutation, cleanup, destructive action, or global mirror unless explicitly requested
- repair, drift-audit, and broken-system language routes to `/system-audit` or `/autopilot`
- real Codex subagents require explicit authorization
- this global skill stays a thin compatibility wrapper with no competing behavior contract

## Output Contract

Produce a compact Library Pulse: current arsenal status, most relevant
capabilities, reusable solutions, sleeping giants, gaps, and exactly one start
command. Do not persist the pulse from this wrapper.
"""

GLOBAL_WRAPPER_TEXT = f"""---
name: source-command-knowledge-librarian
description: Global compatibility alias for /knowledge-librarian; follows the Antigravity library-pulse source of truth.
---

# source-command-knowledge-librarian

This is a compatibility alias for the global Knowledge-librarian wrapper. When
invoked, load and follow:

`/Users/farricecain/.codex/skills/knowledge-librarian/SKILL.md`

If the current work is inside Antigravity or the user is discussing the
Antigravity harness, also load the canonical project workflow:

`{CANONICAL_PATH}`

## Operator Core Alignment

This wrapper is intentionally a thin compatibility wrapper. It must preserve the
current Knowledge-librarian contract: compact session-start knowledge pulse by
default, read-only default scans with `knowledge_compiler.py stats` and
`knowledge_compiler.py solutions ... --stdout`, existing compiled briefing may
be read but not refreshed by default, every named capability grounded in local
evidence, no state snapshot, compiled knowledge refresh, solution-doc creation,
Mission mutation, cleanup, destructive action, or global mirror unless
explicitly requested, real Codex subagents require explicit authorization, and
no competing behavior contract.

Route repair, drift-audit, and broken-system language to `/system-audit` or
`/autopilot`; keep explicit library-pulse and reusable-context questions on
`/knowledge-librarian`.
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
    if "## Global Knowledge-librarian Pulse" in text:
        return re.sub(
            r"## Global Knowledge-librarian Pulse\n.*?(?=\n## Global Routing-intelligence Analytics|\n## Global Health-check Status|\n## Native Codex Artifact Default)",
            GLOBAL_AGENTS_BLOCK.rstrip() + "\n\n",
            text,
            count=1,
            flags=re.DOTALL,
        )
    anchor = "## Global Routing-intelligence Analytics"
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

    if not GLOBAL_KNOWLEDGE_LIBRARIAN.exists() or read(GLOBAL_KNOWLEDGE_LIBRARIAN) != GLOBAL_KNOWLEDGE_LIBRARIAN_TEXT.rstrip() + "\n":
        write(GLOBAL_KNOWLEDGE_LIBRARIAN, GLOBAL_KNOWLEDGE_LIBRARIAN_TEXT)
        changed.append(str(GLOBAL_KNOWLEDGE_LIBRARIAN))

    if not GLOBAL_WRAPPER.exists() or read(GLOBAL_WRAPPER) != GLOBAL_WRAPPER_TEXT.rstrip() + "\n":
        write(GLOBAL_WRAPPER, GLOBAL_WRAPPER_TEXT)
        changed.append(str(GLOBAL_WRAPPER))

    return changed


def check_alignment() -> list[str]:
    failures: list[str] = []
    for label, path in (
        ("project workflow", PROJECT_WORKFLOW),
        ("local source-command-knowledge-librarian", LOCAL_WRAPPER),
        ("global AGENTS", GLOBAL_AGENTS),
        ("global knowledge-librarian", GLOBAL_KNOWLEDGE_LIBRARIAN),
        ("global source-command-knowledge-librarian", GLOBAL_WRAPPER),
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
                failures.append(f"{label} contains stale Knowledge-librarian contract: {snippet}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Check or align Knowledge-librarian Operator Core wrappers.")
    parser.add_argument("--apply", action="store_true", help="Update global Knowledge-librarian surfaces.")
    parser.add_argument("--check", action="store_true", help="Check alignment only.")
    args = parser.parse_args()

    if args.apply:
        changed = apply_alignment()
        print("KNOWLEDGE-LIBRARIAN OPERATOR CORE ALIGNMENT APPLIED")
        print("- changed: " + (", ".join(changed) if changed else "none"))

    failures = check_alignment()
    if failures:
        print("KNOWLEDGE-LIBRARIAN OPERATOR CORE ALIGNMENT FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("KNOWLEDGE-LIBRARIAN OPERATOR CORE ALIGNMENT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
