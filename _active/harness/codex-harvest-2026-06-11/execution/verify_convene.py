#!/usr/bin/env python3
"""Verify the Codex-native /convene family."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import council_cast  # type: ignore  # noqa: E402
import grounding_guard  # type: ignore  # noqa: E402


PRESETS = {
    "convene": "wide",
    "council": "tight",
    "roundtable": "tight",
    "strike": "strike",
    "deploy-council": "deploy",
    "jcc-deploy": "deploy",
    "campaign": "wide",
}


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(path: str) -> str:
    full = ROOT / path
    require(full.exists(), f"missing file: {path}")
    return full.read_text(encoding="utf-8", errors="ignore")


def main() -> int:
    for path in (
        "execution/convene.py",
        "execution/kimi_swarm.py",
        "execution/council_cast.py",
        "execution/grounding_guard.py",
        "knowledge/council-rubric.md",
        "knowledge/council-sessions",
        ".agent/workflows/collective-genius-council.workflow.js",
    ):
        full = ROOT / path
        require(full.exists(), f"missing file: {path}")

    for command, mode in PRESETS.items():
        workflow = read(f".agent/workflows/{command}.md")
        source = read(f".claude/commands/{command}.md")
        wrapper = read(f".agents/cold-skills/source-command-wrappers/source-command-{command}/SKILL.md")
        require(".agent/workflows" in source, f"{command} source bridge missing workflow pointer")
        require("cold" in wrapper.lower(), f"{command} wrapper should stay cold")
        if command != "kimi-swarm":
            require("convene" in workflow.lower() or command == "campaign", f"{command} workflow must map to convene")
        require(mode in workflow or command in {"convene", "campaign"}, f"{command} workflow missing mode {mode}")

    plan = council_cast.build_council_plan("design a premium offer", "tight")
    require(plan["mode"] == "tight", "council cast mode mismatch")
    require(plan["roster"], "council roster missing")
    require(any(member.get("is_user") for member in plan["roster"]), "Farrice lens must be seated")
    require(plan["inner_council_size"] == 4, "tight mode inner council size mismatch")

    fixture = (
        "The market is projected to reach $12 billion by 2027 according to McKinsey. "
        "Growth rate is 18% CAGR. No URLs are present."
    )
    scan = grounding_guard.scan(fixture, "Strategy")
    require(scan["verdict"] in {"WARN", "FLAG"}, "grounding guard should catch unsourced factual load")

    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False) as tmp:
        tmp.write(fixture)
        tmp_path = tmp.name
    guard_cli = subprocess.run(
        [sys.executable, "execution/grounding_guard.py", tmp_path, "--task-type", "Strategy"],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(guard_cli.returncode == 0, f"grounding guard CLI failed: {guard_cli.stderr}")
    require(json.loads(guard_cli.stdout)["verdict"] in {"WARN", "FLAG"}, "grounding guard CLI weak")

    convene_cli = subprocess.run(
        [
            sys.executable,
            "execution/convene.py",
            "plan",
            "design a premium offer",
            "--mode",
            "tight",
            "--json",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(convene_cli.returncode == 0, f"convene CLI failed: {convene_cli.stderr}")
    parsed = json.loads(convene_cli.stdout)
    require(parsed["owner"] == "/convene", "convene CLI owner mismatch")
    require(parsed["delegation"]["real_subagents_spawned"] is False, "convene must not spawn subagents")

    for command in PRESETS:
        hot = ROOT / ".agents" / "skills" / f"source-command-{command}" / "SKILL.md"
        require(not hot.exists(), f"{command} should not be hot-promoted")

    print("Convene verification: PASS")
    print("- /convene and presets map to council packet plans")
    print("- council_cast seats Farrice and diverse roster")
    print("- grounding_guard catches unsourced factual load")
    print("- cold wrappers exist without hot promotion")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
