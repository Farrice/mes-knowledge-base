#!/usr/bin/env python3
"""Verify the Codex-native Kimi swarm bridge."""

from __future__ import annotations

import json
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "execution"))

import kimi_swarm  # type: ignore  # noqa: E402
from native_floor import ingest_findings  # type: ignore  # noqa: E402


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def read(path: str) -> str:
    full = ROOT / path
    require(full.exists(), f"missing file: {path}")
    return full.read_text(encoding="utf-8", errors="ignore")


def main() -> int:
    for path in (
        "execution/kimi_swarm.py",
        "execution/convene.py",
        "execution/research.py",
        "execution/research_contract.py",
        "execution/native_floor.py",
        "execution/research_personas.py",
        ".agent/workflows/kimi-swarm.md",
        ".claude/commands/kimi-swarm.md",
        ".agents/cold-skills/source-command-wrappers/source-command-kimi-swarm/SKILL.md",
    ):
        read(path)

    workflow = read(".agent/workflows/kimi-swarm.md")
    require("/deep-research-os" in workflow, "kimi-swarm workflow must name deep-research-os owner")
    require("/convene" in workflow, "kimi-swarm workflow must name convene owner")
    require("does not spawn real Codex subagents" in workflow, "subagent boundary missing")

    research = kimi_swarm.build_plan(
        "research a market",
        mode="research",
        depth="standard",
        allow_subagents=True,
    )
    require(research["mode"] == "research", "research mode did not resolve")
    require(research["owner"] == "/deep-research-os", "research owner mismatch")
    require(research["delegation"]["allow_subagents_requested"] is True, "delegate intent not recorded")
    require(research["delegation"]["real_subagents_spawned"] is False, "verifier must not spawn subagents")
    require(research["worker_packets"], "research packets missing")
    require("source_url" in json.dumps(research["worker_packets"]), "source rule missing from packets")

    general = kimi_swarm.build_plan("design a launch strategy", mode="general", convene_mode="wide")
    require(general["mode"] == "general", "general mode did not resolve")
    require(general["owner"] == "/convene", "general owner mismatch")
    require(general["worker_packets"], "general packets missing")
    require("What We Would Have Missed" in json.dumps(general), "missed-insight contract missing")

    with tempfile.NamedTemporaryFile("w", suffix=".jsonl", delete=False) as tmp:
        tmp.write(
            json.dumps({
                "claim": "A sourced finding survives ingest.",
                "source_url": "https://example.com/source",
                "excerpt": "example excerpt",
            }) + "\n"
        )
        tmp.write(json.dumps({"claim": "This has no URL and must be quarantined."}) + "\n")
        tmp_path = Path(tmp.name)
    result = ingest_findings(tmp_path, "fixture query", depth="quick")
    require(len(result.findings) == 1, "sourced finding should survive")
    require(result.quarantined_count == 1, "unsourced finding should be quarantined")

    cli = subprocess.run(
        [
            sys.executable,
            "execution/kimi_swarm.py",
            "plan",
            "research a market",
            "--mode",
            "research",
            "--allow-subagents",
            "--json",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(cli.returncode == 0, f"kimi swarm research CLI failed: {cli.stderr}")
    require(json.loads(cli.stdout)["owner"] == "/deep-research-os", "CLI research owner mismatch")

    cli_general = subprocess.run(
        [
            sys.executable,
            "execution/kimi_swarm.py",
            "plan",
            "design a launch strategy",
            "--mode",
            "general",
            "--json",
        ],
        cwd=ROOT,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        check=False,
    )
    require(cli_general.returncode == 0, f"kimi swarm general CLI failed: {cli_general.stderr}")
    require(json.loads(cli_general.stdout)["owner"] == "/convene", "CLI general owner mismatch")

    hot = ROOT / ".agents" / "skills" / "source-command-kimi-swarm" / "SKILL.md"
    cold = ROOT / ".agents" / "cold-skills" / "source-command-wrappers" / "source-command-kimi-swarm" / "SKILL.md"
    require(not hot.exists(), "kimi-swarm should not be hot-promoted")
    require(cold.exists(), "kimi-swarm cold wrapper missing")

    print("Kimi swarm verification: PASS")
    print("- research packets route to /deep-research-os")
    print("- general packets route to /convene")
    print("- real subagents remain approval-gated")
    print("- unsourced findings are quarantined")
    print("- CLI JSON is valid")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
