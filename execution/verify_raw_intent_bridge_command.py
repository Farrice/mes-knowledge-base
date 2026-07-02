#!/usr/bin/env python3
"""Verify the /raw-intent-bridge command surface."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import command_menu  # type: ignore  # noqa: E402
import workflow_router  # type: ignore  # noqa: E402


COMMAND = "raw-intent-bridge"
FILES = {
    "workflow": ROOT / ".agent" / "workflows" / f"{COMMAND}.md",
    "claude_command": ROOT / ".claude" / "commands" / f"{COMMAND}.md",
    "codex_skill": ROOT / ".agents" / "skills" / f"source-command-{COMMAND}" / "SKILL.md",
    "compiler": ROOT / "execution" / "raw_intent_run_packet.py",
    "contract": ROOT / "semantic_libraries" / "antigravity" / "primitives" / "raw-intent-virtuoso-bridge-contract.md",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="ignore")


def verify_files() -> None:
    for label, path in FILES.items():
        require(path.exists(), f"missing {label}: {path.relative_to(ROOT)}")

    workflow = read(FILES["workflow"])
    skill = read(FILES["codex_skill"])
    command = read(FILES["claude_command"])
    for label, content in {
        "workflow": workflow,
        "codex skill": skill,
        "claude command": command,
    }.items():
        require("raw_intent_run_packet.py" in content, f"{label} does not point to packet compiler")
        require("plugin" in content.lower(), f"{label} must preserve plugin boundary")

    require('name: "source-command-raw-intent-bridge"' in skill, "Codex skill frontmatter name mismatch")
    require("/raw-intent-bridge" in skill, "Codex skill missing command trigger")


def verify_discovery() -> None:
    workflows = command_menu.build_index()
    menu_hits = [workflow.name for _, workflow in command_menu.search(workflows, "/raw-intent-bridge messy Codex run packet", 5)]
    require(menu_hits and menu_hits[0] == COMMAND, f"command_menu did not rank /{COMMAND} first: {menu_hits}")

    router_hits = [workflow["name"] for _, workflow in workflow_router.search_workflows("/raw-intent-bridge messy Codex run packet", 5)]
    require(COMMAND in router_hits[:3], f"workflow_router did not surface /{COMMAND}: {router_hits}")


def verify_packet_cli() -> None:
    result = subprocess.run(
        [
            sys.executable,
            "execution/raw_intent_run_packet.py",
            "/raw-intent-bridge I do not know how to ask Codex for an entrepreneurial run packet",
            "--plain",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(result.returncode == 0, f"packet CLI failed: {result.stderr}")
    require("## Raw Intent Run Packet" in result.stdout, "packet CLI did not render packet")
    require("Plugin Packaging" in result.stdout, "packet CLI missing plugin-packaging verdict")
    first_action_line = next((line for line in result.stdout.splitlines() if "First safe action" in line), "")
    require("/raw-intent-bridge" not in first_action_line, "packet should strip command prefix before building first safe action")


def main() -> int:
    verify_files()
    verify_discovery()
    verify_packet_cli()
    print("Raw Intent Bridge command verification: PASS")
    print("- /raw-intent-bridge workflow, slash shim, and Codex skill wrapper exist")
    print("- command_menu ranks /raw-intent-bridge first for explicit command usage")
    print("- workflow_router surfaces /raw-intent-bridge for explicit command usage")
    print("- packet compiler renders a run packet with plugin packaging deferred")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
