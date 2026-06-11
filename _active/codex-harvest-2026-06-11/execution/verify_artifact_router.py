#!/usr/bin/env python3
"""Verify the global artifact router and command bridge."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def run(args: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        args,
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=60,
    )


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def command_output(args: list[str], failures: list[str], label: str) -> str:
    proc = run(args)
    if proc.returncode != 0:
        failures.append(f"{label} failed: {(proc.stderr or proc.stdout).strip()[:240]}")
    return proc.stdout


def main() -> int:
    failures: list[str] = []

    for path in [
        ROOT / "execution" / "artifact_router.py",
        ROOT / ".agent" / "workflows" / "artifact-router.md",
        ROOT / ".claude" / "commands" / "artifact-router.md",
        ROOT / ".agents" / "skills" / "source-command-artifact-router" / "SKILL.md",
    ]:
        require(path.exists(), f"missing bridge file: {path}", failures)

    inventory_out = command_output(
        [sys.executable, "execution/artifact_router.py", "inventory", "--json"],
        failures,
        "inventory",
    )
    if inventory_out:
        manifest = json.loads(inventory_out)
        require(manifest.get("total_files", 0) > 0, "inventory has no files", failures)
        roots = manifest.get("counts", {}).get("by_root", {})
        for expected in ["brain", "_active", "deliverables", "research_outputs", "strategy_briefs"]:
            require(expected in roots, f"manifest missing root: {expected}", failures)

    classify_out = command_output(
        [
            sys.executable,
            "execution/artifact_router.py",
            "classify",
            "deliverables/hybrid-morning-signal-radar-2026-05-11.md",
            "--json",
        ],
        failures,
        "classify sample",
    )
    if classify_out:
        sample = json.loads(classify_out)
        require(sample.get("project") == "farrice-content-os", "hybrid morning route should map to farrice-content-os", failures)
        require(sample.get("domain") == "Content", "hybrid morning route should carry Content domain", failures)

    plan_path = ROOT / ".tmp" / "artifact-router-verify-plan.json"
    plan_out = command_output(
        [sys.executable, "execution/artifact_router.py", "plan", "--output", str(plan_path), "--json"],
        failures,
        "plan",
    )
    if plan_out:
        plan = json.loads(plan_out)
        for bucket in ["safe", "ambiguous", "blocked", "skipped"]:
            require(bucket in plan, f"plan missing bucket: {bucket}", failures)

    backlog_out = command_output(
        [sys.executable, "execution/artifact_router.py", "backlog-map", "--json"],
        failures,
        "backlog map",
    )
    if backlog_out:
        backlog = json.loads(backlog_out)
        require(Path(backlog.get("map_path", "")).exists(), "backlog map file was not created", failures)
        require(Path(backlog.get("plan_path", "")).exists(), "backlog move plan was not created", failures)

    duplicate_dir = ROOT / ".tmp" / "artifact-router-overwrite"
    duplicate_dir.mkdir(parents=True, exist_ok=True)
    duplicate_source = duplicate_dir / "source.md"
    duplicate_destination = duplicate_dir / "destination.md"
    duplicate_plan = duplicate_dir / "duplicate-plan.json"
    duplicate_source.write_text("# Source\n", encoding="utf-8")
    duplicate_destination.write_text("# Destination\n", encoding="utf-8")
    duplicate_plan.write_text(
        json.dumps(
            {
                "version": 1,
                "safe": [
                    {
                        "path": str(duplicate_source),
                        "destination": str(duplicate_destination),
                        "domain": "System",
                        "project": "system-audit",
                        "lifecycle": "deliverable",
                    }
                ],
            },
            indent=2,
        ),
        encoding="utf-8",
    )
    duplicate_apply = run(
        [
            sys.executable,
            "execution/artifact_router.py",
            "apply",
            "--plan",
            str(duplicate_plan),
            "--json",
        ]
    )
    require(duplicate_apply.returncode == 0, "duplicate-destination apply should skip without failing", failures)
    if duplicate_apply.stdout:
        duplicate_result = json.loads(duplicate_apply.stdout)
        require(not duplicate_result.get("moved"), "duplicate-destination apply should not move", failures)
        require(duplicate_result.get("skipped"), "duplicate-destination apply should report skipped item", failures)
    require(duplicate_destination.read_text(encoding="utf-8") == "# Destination\n", "duplicate destination was overwritten", failures)

    enforce_pass = run(
        [
            sys.executable,
            "execution/artifact_router.py",
            "enforce",
            "_system/organization/ORG_INDEX.md",
            "--json",
        ]
    )
    require(enforce_pass.returncode == 0, "enforce should pass for organization control-plane index", failures)

    loose_candidates = sorted((ROOT / "deliverables").glob("*"))
    if loose_candidates:
        enforce_fail = run(
            [
                sys.executable,
                "execution/artifact_router.py",
                "enforce",
                str(loose_candidates[0]),
                "--json",
            ]
        )
        require(enforce_fail.returncode != 0, "enforce should fail for loose deliverables backlog item", failures)

    menu_show = command_output(
        [sys.executable, "execution/command_menu.py", "show", "artifact-router"],
        failures,
        "command menu show",
    )
    require("/artifact-router" in menu_show, "command menu show does not resolve /artifact-router", failures)

    menu_search = command_output(
        [sys.executable, "execution/command_menu.py", "search", "organize files artifacts projects router"],
        failures,
        "command menu search",
    )
    require("/artifact-router" in menu_search, "command menu search does not surface /artifact-router", failures)

    workflow_search = command_output(
        [sys.executable, "execution/workflow_router.py", "search", "organize files artifacts projects router"],
        failures,
        "workflow router search",
    )
    require("/artifact-router" in workflow_search, "workflow router search does not surface /artifact-router", failures)

    find_context = command_output(
        [sys.executable, "execution/context_search.py", "hybrid morning signal radar", "--max", "3"],
        failures,
        "context search organization",
    )
    require("Organization matches" in find_context, "context search did not include organization manifest matches", failures)

    if failures:
        print("Artifact router verification FAILED")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Artifact router verification PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
