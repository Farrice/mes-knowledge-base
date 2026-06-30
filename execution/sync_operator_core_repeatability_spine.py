#!/usr/bin/env python3
"""Check or align Repeatability-spine Operator Core wrappers."""

from __future__ import annotations

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
PROJECT_WORKFLOW = ROOT / ".agent" / "workflows" / "repeatability-spine.md"
LOCAL_WRAPPER = ROOT / ".agents" / "skills" / "source-command-repeatability-spine" / "SKILL.md"
GLOBAL_AGENTS = Path.home() / ".codex" / "AGENTS.md"
GLOBAL_REPEATABILITY = Path.home() / ".codex" / "skills" / "repeatability-spine" / "SKILL.md"
GLOBAL_WRAPPER = Path.home() / ".codex" / "skills" / "source-command-repeatability-spine" / "SKILL.md"

CANONICAL_PATH = "/Users/farricecain/Codex Antigravity/.agent/workflows/repeatability-spine.md"

COMMON_REQUIREMENTS = (
    "preserve the good example",
    "grounded evidence",
    "primary failure class",
    "Preservation Lock",
    "repair route",
    "validation",
    "regression guard",
    "replay prompt",
    "pending evidence",
    "verifier query or routing feedback log",
    "Goal Packet",
    "workspace proof and explicit approval",
    "real Codex subagents require explicit authorization",
    "thin compatibility wrapper",
    "no competing behavior contract",
)

PATH_REQUIREMENTS = {
    PROJECT_WORKFLOW: (
        "canonical source of truth for Repeatability-spine behavior",
        "preserves the good example before repair",
        "Every run needs grounded evidence, one primary failure class, Preservation Lock, repair route, validation, regression guard, and replay prompt",
        "Inaccessible conversations are pending evidence, not invented findings",
        "Routing failures require a verifier query or routing feedback log before being called repaired",
        "Mutation-capable repair routes (`/self-evolve`, `/skill-anneal`, `/skill-evolution`) require a Goal Packet before edits",
        "Global `~/.codex` behavior changes require workspace proof and explicit approval",
        "Route broad broken-harness triage to `/autopilot` or `/system-audit`",
        "Real Codex subagents require explicit authorization",
    ),
    LOCAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        ".agent/workflows/repeatability-spine.md",
        "canonical behavior source",
    ),
    GLOBAL_AGENTS: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Global Repeatability-spine Regression Repair",
    ),
    GLOBAL_REPEATABILITY: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "Project Source Of Truth",
    ),
    GLOBAL_WRAPPER: COMMON_REQUIREMENTS
    + (
        CANONICAL_PATH,
        "/Users/farricecain/.codex/skills/repeatability-spine/SKILL.md",
        "compatibility alias",
    ),
}

FORBIDDEN = (
    "revise without a Preservation Lock",
    "invent findings by default",
    "global behavior changes by default",
    "mutate by default",
)

GLOBAL_AGENTS_BLOCK = f"""## Global Repeatability-spine Regression Repair

Use the global `repeatability-spine` skill at `/Users/farricecain/.codex/skills/repeatability-spine/SKILL.md`
when the user invokes `/repeatability-spine`,
`source-command-repeatability-spine`, says a revision got worse, cannot repeat
the magic, lost the good part, route picked the wrong workflow, or a patch
introduced a regression.

The canonical Antigravity Repeatability-spine workflow is `{CANONICAL_PATH}`.
Global Repeatability-spine wrappers are thin compatibility wrappers with no
competing behavior contract.

Default behavior: preserve the good example before repair. Every run needs
grounded evidence, one primary failure class, Preservation Lock, repair route,
validation, regression guard, and replay prompt. Inaccessible conversations are
pending evidence, not invented findings. Routing failures require a verifier
query or routing feedback log before being called repaired. Mutation-capable
repair routes require a Goal Packet before edits. Global `~/.codex` behavior
changes require workspace proof and explicit approval. Real Codex subagents
require explicit authorization.
"""

GLOBAL_REPEATABILITY_TEXT = f"""---
name: repeatability-spine
description: Global thin compatibility wrapper for Antigravity Repeatability-spine; delegates to the canonical project workflow.
---

# Repeatability-spine

## Project Source Of Truth

The canonical Repeatability-spine behavior source is:

`{CANONICAL_PATH}`

This global skill is a thin compatibility wrapper. It keeps repeatability,
failed revision, lost magic, preservation lock, wrong route, and regression
repair language discoverable anywhere in Codex, but it must not maintain a
competing behavior contract. When the Antigravity project workflow is available
or relevant, read and follow that workflow first.

## Operator Core Alignment

Preserve the current Repeatability-spine contract:

- preserve the good example before repair
- every run needs grounded evidence, one primary failure class, Preservation Lock, repair route, validation, regression guard, and replay prompt
- inaccessible conversations are pending evidence, not invented findings
- routing failures require a verifier query or routing feedback log before being called repaired
- mutation-capable repair routes require a Goal Packet before edits
- global `~/.codex` behavior changes require workspace proof and explicit approval
- broad broken-harness triage routes to `/autopilot` or `/system-audit`
- real Codex subagents require explicit authorization
- this global skill stays a thin compatibility wrapper with no competing behavior contract
"""

GLOBAL_WRAPPER_TEXT = f"""---
name: source-command-repeatability-spine
description: Global compatibility alias for /repeatability-spine; follows the Antigravity regression-repair source of truth.
---

# source-command-repeatability-spine

This is a compatibility alias for the global Repeatability-spine wrapper. When
invoked, load and follow:

`/Users/farricecain/.codex/skills/repeatability-spine/SKILL.md`

If the current work is inside Antigravity or the user is discussing the
Antigravity harness, also load the canonical project workflow:

`{CANONICAL_PATH}`

## Operator Core Alignment

This wrapper is intentionally a thin compatibility wrapper. It must preserve the
current Repeatability-spine contract: preserve the good example, grounded
evidence, primary failure class, Preservation Lock, repair route, validation,
regression guard, replay prompt, pending evidence for inaccessible
conversations, verifier query or routing feedback log for routing failures,
Goal Packet before mutation-capable repair, workspace proof and explicit
approval for global behavior changes, real Codex subagents require explicit
authorization, and no competing behavior contract.
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
    if "## Global Repeatability-spine Regression Repair" in text:
        return re.sub(
            r"## Global Repeatability-spine Regression Repair\n.*?(?=\n## Global System-audit Control Plane|\n## Global Source-to-skill-system Builder|\n## Native Codex Artifact Default)",
            GLOBAL_AGENTS_BLOCK.rstrip() + "\n\n",
            text,
            count=1,
            flags=re.DOTALL,
        )
    anchor = "## Global System-audit Control Plane"
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
    if not GLOBAL_REPEATABILITY.exists() or read(GLOBAL_REPEATABILITY) != GLOBAL_REPEATABILITY_TEXT.rstrip() + "\n":
        write(GLOBAL_REPEATABILITY, GLOBAL_REPEATABILITY_TEXT)
        changed.append(str(GLOBAL_REPEATABILITY))
    if not GLOBAL_WRAPPER.exists() or read(GLOBAL_WRAPPER) != GLOBAL_WRAPPER_TEXT.rstrip() + "\n":
        write(GLOBAL_WRAPPER, GLOBAL_WRAPPER_TEXT)
        changed.append(str(GLOBAL_WRAPPER))
    return changed


def check_alignment() -> list[str]:
    failures: list[str] = []
    for label, path in (
        ("project workflow", PROJECT_WORKFLOW),
        ("local source-command-repeatability-spine", LOCAL_WRAPPER),
        ("global AGENTS", GLOBAL_AGENTS),
        ("global repeatability-spine", GLOBAL_REPEATABILITY),
        ("global source-command-repeatability-spine", GLOBAL_WRAPPER),
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
                failures.append(f"{label} contains stale Repeatability-spine contract: {snippet}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description="Check or align Repeatability-spine Operator Core wrappers.")
    parser.add_argument("--apply", action="store_true", help="Update global Repeatability-spine surfaces.")
    parser.add_argument("--check", action="store_true", help="Check alignment only.")
    args = parser.parse_args()
    if args.apply:
        changed = apply_alignment()
        print("REPEATABILITY-SPINE OPERATOR CORE ALIGNMENT APPLIED")
        print("- changed: " + (", ".join(changed) if changed else "none"))
    failures = check_alignment()
    if failures:
        print("REPEATABILITY-SPINE OPERATOR CORE ALIGNMENT FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("REPEATABILITY-SPINE OPERATOR CORE ALIGNMENT PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
