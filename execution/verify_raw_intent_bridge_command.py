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
INVOCATION_FORMS = (
    "/raw-intent-bridge [payload]",
    "raw-intent-bridge: [payload]",
    "source-command-raw-intent-bridge: [payload]",
)
PREFIX_LEAKS = ("/raw-intent-bridge", "raw-intent-bridge:", "source-command-raw-intent-bridge:")
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
        require("Invocation Contract" in content, f"{label} missing invocation contract")
        require("Packet + Run" in content, f"{label} missing Packet + Run default")
        require("everything after the prefix" in content, f"{label} must define payload stripping")
        for form in INVOCATION_FORMS:
            require(form in content, f"{label} missing invocation form: {form}")

    require('name: "source-command-raw-intent-bridge"' in skill, "Codex skill frontmatter name mismatch")
    require("/raw-intent-bridge" in skill, "Codex skill missing command trigger")

    contract = read(FILES["contract"])
    require("Invocation" in contract or "Prefix invocation" in contract, "contract missing invocation language")
    require("Packet + Run" in contract, "contract missing Packet + Run default")
    for form in INVOCATION_FORMS:
        require(form in contract, f"contract missing invocation form: {form}")


def verify_discovery() -> None:
    workflows = command_menu.build_index()
    menu_hits = [workflow.name for _, workflow in command_menu.search(workflows, "/raw-intent-bridge messy Codex run packet", 5)]
    require(menu_hits and menu_hits[0] == COMMAND, f"command_menu did not rank /{COMMAND} first: {menu_hits}")

    router_hits = [workflow["name"] for _, workflow in workflow_router.search_workflows("/raw-intent-bridge messy Codex run packet", 5)]
    require(COMMAND in router_hits[:3], f"workflow_router did not surface /{COMMAND}: {router_hits}")


def verify_packet_cli() -> None:
    cases = [
        "/raw-intent-bridge I have a messy business idea and need the right execution path",
        "raw-intent-bridge: I have a rough offer idea but do not know how to ask Codex",
        "source-command-raw-intent-bridge: audit this raw task and give me the first safe action",
    ]
    for case in cases:
        result = subprocess.run(
            [
                sys.executable,
                "execution/raw_intent_run_packet.py",
                case,
                "--plain",
                "--no-log",
            ],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )
        require(result.returncode == 0, f"packet CLI failed for {case!r}: {result.stderr}")
        require("## Raw Intent Run Packet" in result.stdout, "packet CLI did not render packet")
        require("Plugin Packaging" in result.stdout, "packet CLI missing plugin-packaging verdict")
        first_action_line = next((line for line in result.stdout.splitlines() if "First safe action" in line), "")
        require(first_action_line, f"packet missing first safe action for {case!r}")
        for prefix in PREFIX_LEAKS:
            require(prefix.lower() not in first_action_line.lower(), f"first safe action leaked {prefix}: {first_action_line}")
        require("**First safe action**: /" in first_action_line, f"first safe action is not executable: {first_action_line}")


def main() -> int:
    verify_files()
    verify_discovery()
    verify_packet_cli()
    print("Raw Intent Bridge command verification: PASS")
    print("- /raw-intent-bridge workflow, slash shim, and Codex skill wrapper exist")
    print("- command_menu ranks /raw-intent-bridge first for explicit command usage")
    print("- workflow_router surfaces /raw-intent-bridge for explicit command usage")
    print("- slash, colon, and source-command forms render packets without prefix leakage")
    print("- packet compiler renders a run packet with plugin packaging deferred")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
