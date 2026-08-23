#!/usr/bin/env python3
"""Verify project and global runtime availability for all belief-community routes."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

from sync_belief_community_global import ROUTES, global_failures, project_failures


ROOT = Path(__file__).resolve().parents[1]


def run(args: list[str]) -> str:
    result = subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    if result.returncode != 0:
        raise AssertionError(f"command failed: {' '.join(args)}\n{result.stdout}")
    return result.stdout


def first_route(output: str) -> str:
    for line in output.splitlines():
        stripped = line.strip()
        if stripped.startswith("1. `/"):
            return stripped.split("`/", 1)[1].split("`", 1)[0]
        if stripped.startswith("/"):
            return stripped.split()[0].removeprefix("/")
    return ""


def main() -> int:
    failures = project_failures() + global_failures()
    if failures:
        print("BELIEF COMMUNITY RUNTIME VERIFICATION: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    run([sys.executable, "execution/verify_joanna_belief_community.py", "--json"])
    run([sys.executable, "execution/skill_auditor.py", "check", "--skill", "joanna-wiebe-persuasion-mastery"])

    receipts: list[str] = []
    for route in ROUTES:
        menu = run([sys.executable, "execution/command_menu.py", "search", route, "-n", "5"])
        workflow = run([sys.executable, "execution/workflow_router.py", "search", route, "--top", "5"])
        menu_route = first_route(menu)
        workflow_route = first_route(workflow)
        if menu_route != route:
            raise AssertionError(f"command menu expected /{route}, got /{menu_route or 'none'}")
        if workflow_route != route:
            raise AssertionError(f"workflow router expected /{route}, got /{workflow_route or 'none'}")
        receipts.append(f"/{route}: project menu + workflow router + global Codex + global Claude")

    print("BELIEF COMMUNITY RUNTIME VERIFICATION: PASS")
    for receipt in receipts:
        print(f"- {receipt}")
    print("- source package, behavior proof, and unsafe negative controls passed")
    print("- fresh Codex/Claude sessions will discover the new global skills at startup")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
