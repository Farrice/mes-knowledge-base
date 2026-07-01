#!/usr/bin/env python3
"""Verify peer-constitution authority model: CODEX.md + AGENTS.md for Codex; CLAUDE.md + GEMINI.md for their platforms."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def read(path: str) -> str:
    return (ROOT / path).read_text(encoding="utf-8", errors="ignore")


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    failures: list[str] = []

    codex_path = ROOT / "CODEX.md"
    require(codex_path.exists(), "CODEX.md is missing", failures)

    agents = read("AGENTS.md")
    codex = read("CODEX.md") if codex_path.exists() else ""
    gemini = read("GEMINI.md")
    claude = read("CLAUDE.md")

    # Peer-constitution model: CODEX.md exists and is referenced as Codex authority
    require("CODEX.md" in agents, "AGENTS.md does not reference CODEX.md as authority", failures)
    require(
        "CODEX.md" in codex or "Codex" in codex,
        "CODEX.md lacks self-reference to its authority",
        failures,
    )
    # CLAUDE.md exists and retains Claude authority (peer model, not demoted)
    require(
        "CLAUDE.md" in claude.splitlines()[0] or "Claude Code" in claude,
        "CLAUDE.md does not assert Claude authority",
        failures,
    )
    # GEMINI.md exists and describes Gemini authority (peer model, not demoted)
    require(
        "GEMINI.md" in gemini or "Gemini" in gemini,
        "GEMINI.md does not describe Gemini platform",
        failures,
    )

    # Workflows should not contain legacy-demote language (they are platform-neutral)
    active_workflows = [
        ".agent/workflows/autopilot.md",
        ".agent/workflows/mission.md",
        ".agent/workflows/extraction-governor-agent.md",
        ".agent/workflows/extract-forge.md",
        ".agent/workflows/source-to-skill-system.md",
    ]
    banned = [
        "1. `GEMINI.md`",
        "Read `GEMINI.md` as",
        "`GEMINI.md` — Full skill and agent roster",
        "full 7-step chain from CLAUDE.md",
    ]
    for workflow in active_workflows:
        content = read(workflow)
        for phrase in banned:
            require(phrase not in content, f"{workflow} still contains active legacy phrase: {phrase}", failures)

    if failures:
        print("Peer-constitution authority verification: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Peer-constitution authority verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
