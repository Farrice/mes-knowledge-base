#!/usr/bin/env python3
"""Install or verify global Codex and Claude bridges for belief-community routes."""

from __future__ import annotations

import argparse
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = Path("/Users/farricecain/Google Antigravity")
GLOBAL_CODEX_SKILLS = Path.home() / ".codex" / "skills"
GLOBAL_AGENT_SKILLS = Path.home() / ".agents" / "skills"
GLOBAL_CLAUDE_SKILLS = Path.home() / ".claude" / "skills"
GLOBAL_CLAUDE_COMMANDS = Path.home() / ".claude" / "commands"

ROUTES = {
    "joanna-wiebe": {
        "description": "Deploy Joanna Wiebe's complete extracted expertise adaptively or in explicit full-stack mode across copy, persuasion, authority, belief communities, messaging, funnels, and writing-business architecture.",
        "workflow": "joanna-wiebe.md",
        "kind": "expert-front-door",
    },
    "belief-community-architecture": {
        "description": "Build the full Joanna Wiebe belief-community system across worldview, ethical contrast, symbols, voluntary rituals, language, conviction, and channel deployment.",
        "workflow": "belief-community-architecture.md",
    },
    "worldview-contrast-system": {
        "description": "Turn generic positioning into an evidence-backed worldview and ethical contrast without attacking people.",
        "workflow": "worldview-contrast-system.md",
    },
    "participation-language-system": {
        "description": "Create a belief-carrying symbol, voluntary value-producing ritual, shared language, and adoption instrumentation.",
        "workflow": "participation-language-system.md",
    },
    "earned-conviction-deployment": {
        "description": "Turn an established belief system into proof-bounded conviction and finished cross-channel expressions.",
        "workflow": "earned-conviction-deployment.md",
    },
}


def direct_skill_text(route: str, data: dict[str, str]) -> str:
    workflow = PROJECT_ROOT / ".agent" / "workflows" / data["workflow"]
    if data.get("kind") == "expert-front-door":
        return f"""---
name: {route}
description: Global named front door for Antigravity /{route}. {data['description']}
---

# {route}

## Canonical source

Read and execute:

`{workflow}`

The canonical Joanna owner and capability maps remain in:

- `{PROJECT_ROOT / 'agents/joanna-wiebe/AGENT.md'}`
- `{PROJECT_ROOT / 'skills/joanna-wiebe-persuasion-mastery/SKILL.md'}`
- `{PROJECT_ROOT / 'skills/joanna-wiebe-writing-careers/SKILL.md'}`

Use Adaptive Joanna by default. When the user explicitly asks for full Joanna,
full deployment, all extracted genius, or complete expertise, use the workflow's
Full Joanna Deployment mode. This global skill is a thin bridge and must not
duplicate or replace the project-owned expert system.
"""
    return f"""---
name: {route}
description: Global thin wrapper for Antigravity /{route}. {data['description']}
---

# {route}

## Canonical source

Read and execute:

`{workflow}`

Load the existing Joanna Wiebe owner before execution:

- `{PROJECT_ROOT / 'skills/joanna-wiebe-persuasion-mastery/genius.md'}`
- `{PROJECT_ROOT / 'skills/joanna-wiebe-persuasion-mastery/references/belief-community-architecture.md'}`

This global skill is a thin compatibility wrapper. The project workflow and
`joanna-wiebe-persuasion-mastery` remain the behavior source of truth. Do not
create a duplicate expert, standalone methodology, or competing behavior
contract. Preserve the evidence ladder, ethical enemy boundary, voluntary
ritual safeguards, and NO EVENT limits.
"""


def alias_skill_text(route: str, data: dict[str, str]) -> str:
    return f"""---
name: source-command-{route}
description: Global compatibility alias for /{route}. {data['description']}
---

# source-command-{route}

Load and follow:

`{GLOBAL_CODEX_SKILLS / route / 'SKILL.md'}`

When running in Claude Code, the equivalent canonical skill lives at:

`{GLOBAL_AGENT_SKILLS / route / 'SKILL.md'}`

This alias is intentionally thin and must not maintain a competing behavior
contract.
"""


def claude_command_text(route: str, data: dict[str, str]) -> str:
    workflow = PROJECT_ROOT / ".agent" / "workflows" / data["workflow"]
    return f"""---
description: {data['description']}
---

Read and execute the canonical workflow at `{workflow}`.
"""


def expected_files() -> dict[Path, str]:
    files: dict[Path, str] = {}
    for route, data in ROUTES.items():
        direct = direct_skill_text(route, data).rstrip() + "\n"
        alias = alias_skill_text(route, data).rstrip() + "\n"
        files[GLOBAL_CODEX_SKILLS / route / "SKILL.md"] = direct
        files[GLOBAL_CODEX_SKILLS / f"source-command-{route}" / "SKILL.md"] = alias
        files[GLOBAL_AGENT_SKILLS / route / "SKILL.md"] = direct
        files[GLOBAL_AGENT_SKILLS / f"source-command-{route}" / "SKILL.md"] = alias
        files[GLOBAL_CLAUDE_COMMANDS / f"{route}.md"] = claude_command_text(route, data).rstrip() + "\n"
    return files


def expected_links() -> dict[Path, Path]:
    links: dict[Path, Path] = {}
    for route in ROUTES:
        links[GLOBAL_CLAUDE_SKILLS / route] = GLOBAL_AGENT_SKILLS / route
        links[GLOBAL_CLAUDE_SKILLS / f"source-command-{route}"] = (
            GLOBAL_AGENT_SKILLS / f"source-command-{route}"
        )
    return links


def project_failures() -> list[str]:
    failures: list[str] = []
    for route, data in ROUTES.items():
        paths = (
            ROOT / ".agent" / "workflows" / data["workflow"],
            ROOT / ".claude" / "commands" / f"{route}.md",
            ROOT / ".agents" / "skills" / f"source-command-{route}" / "SKILL.md",
        )
        for path in paths:
            if not path.is_file() or path.stat().st_size == 0:
                failures.append(f"missing project bridge: {path.relative_to(ROOT)}")
        command = paths[1]
        if command.is_file() and f".agent/workflows/{data['workflow']}" not in command.read_text(encoding="utf-8"):
            failures.append(f"Claude command does not point to canonical workflow: {command.relative_to(ROOT)}")
    return failures


def apply_global() -> list[str]:
    changed: list[str] = []
    for path, content in expected_files().items():
        path.parent.mkdir(parents=True, exist_ok=True)
        current = path.read_text(encoding="utf-8") if path.is_file() else None
        if current != content:
            path.write_text(content, encoding="utf-8")
            changed.append(str(path))

    GLOBAL_CLAUDE_SKILLS.mkdir(parents=True, exist_ok=True)
    for link, target in expected_links().items():
        if link.is_symlink():
            if link.resolve() == target.resolve():
                continue
            link.unlink()
        elif link.exists():
            raise AssertionError(f"refusing to replace non-symlink Claude skill path: {link}")
        link.symlink_to(target, target_is_directory=True)
        changed.append(str(link))
    return changed


def global_failures() -> list[str]:
    failures: list[str] = []
    for path, expected in expected_files().items():
        if not path.is_file():
            failures.append(f"missing global file: {path}")
            continue
        if path.read_text(encoding="utf-8") != expected:
            failures.append(f"global file drift: {path}")
    for link, target in expected_links().items():
        if not link.is_symlink():
            failures.append(f"missing Claude skill symlink: {link}")
        elif link.resolve() != target.resolve():
            failures.append(f"Claude skill symlink drift: {link} -> {link.resolve()}")
    return failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("--plan", action="store_true", help="Show exact global targets without writing.")
    group.add_argument("--apply", action="store_true", help="Write authorized global Codex and Claude bridges.")
    group.add_argument("--check", action="store_true", help="Verify project and global bridge parity.")
    args = parser.parse_args()

    failures = project_failures()
    if args.plan:
        print("BELIEF COMMUNITY GLOBAL DEPLOYMENT PLAN")
        for path in expected_files():
            print(f"- file: {path}")
        for link, target in expected_links().items():
            print(f"- symlink: {link} -> {target}")
    elif args.apply:
        changed = apply_global()
        print("BELIEF COMMUNITY GLOBAL DEPLOYMENT APPLIED")
        print(f"- changed: {len(changed)}")
        for path in changed:
            print(f"  - {path}")
        failures.extend(global_failures())
    else:
        failures.extend(global_failures())

    if failures:
        print("BELIEF COMMUNITY GLOBAL DEPLOYMENT: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("BELIEF COMMUNITY GLOBAL DEPLOYMENT: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
