#!/usr/bin/env python3
"""Verify core extraction slash-command bridges are live in Codex."""

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
COMMANDS = (
    "extract",
    "extract-forge",
    "extract-vision",
    "extract-amplify",
    "video-source-extract",
    "video-transcript-ledger",
)


def command_paths(command: str) -> dict[str, Path]:
    return {
        "workflow": ROOT / ".agent" / "workflows" / f"{command}.md",
        "source": ROOT / ".claude" / "commands" / f"{command}.md",
        "live": ROOT / ".agents" / "skills" / f"source-command-{command}" / "SKILL.md",
    }


def command_menu_status(command: str) -> tuple[bool, str]:
    result = subprocess.run(
        [sys.executable, str(ROOT / "execution" / "command_menu.py"), "show", command],
        cwd=ROOT,
        text=True,
        capture_output=True,
        check=False,
    )
    output = (result.stdout or "") + (result.stderr or "")
    return result.returncode == 0 and "Execution status: hot-bridge" in output, output.strip()


def verify(commands: tuple[str, ...]) -> tuple[bool, list[str]]:
    failures: list[str] = []
    for command in commands:
        for label, path in command_paths(command).items():
            if not path.exists():
                failures.append(f"/{command}: missing {label} bridge at {path.relative_to(ROOT)}")
        ok, output = command_menu_status(command)
        if not ok:
            failures.append(f"/{command}: command menu does not report hot-bridge ({output})")
    return not failures, failures


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("commands", nargs="*", help="Optional command names without leading slash")
    args = parser.parse_args()

    commands = tuple(args.commands) or COMMANDS
    ok, failures = verify(commands)
    if ok:
        print("Extraction command surface: PASS")
        for command in commands:
            print(f"- /{command}: hot-bridge")
        return 0

    print("Extraction command surface: FAIL")
    for failure in failures:
        print(f"- {failure}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
