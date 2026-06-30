#!/usr/bin/env python3
"""Verify Codex-native authority (AGENTS.md + CODEX.md) is active.

Peer-constitution model (Farrice, 2026-06-30): CLAUDE.md is canon and GEMINI.md is the
Gemini constitution; both stay authoritative for their own platforms and are NOT demoted
to "LEGACY REFERENCE". Codex routes via AGENTS.md/CODEX.md; this verifier checks that
Codex authority is wired without forcing demotion of the sibling constitutions.
"""

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

    require("CODEX.md" in agents, "AGENTS.md does not point to CODEX.md", failures)
    require(
        "Read `GEMINI.md` as the primary harness specification" not in agents,
        "AGENTS.md still makes GEMINI.md primary authority",
        failures,
    )
    require(
        "Do not treat `GEMINI.md` or `CLAUDE.md` as primary routing authority" in codex,
        "CODEX.md lacks explicit legacy demotion rule",
        failures,
    )
    # Peer-constitution model (Farrice, 2026-06-30): CLAUDE.md and GEMINI.md stay
    # authoritative for their own platforms and are NOT demoted to "LEGACY REFERENCE".
    # Codex follows AGENTS.md/CODEX.md (asserted above); no legacy marker is required on
    # the sibling constitutions. CLAUDE.md is canon per the Platform Portability OS, so
    # this verifier must not force its demotion.

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
        print("Codex authority verification: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Codex authority verification: PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
