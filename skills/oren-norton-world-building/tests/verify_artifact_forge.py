#!/usr/bin/env python3
"""Verify the Oren-Norton artifact forge in positive and negative directions."""

from __future__ import annotations

import re
from pathlib import Path


SKILL = Path(__file__).resolve().parents[1]
REPO = SKILL.parents[1]
SAMPLE = REPO / "extractions/oren-norton-world-building/artifact-forge-sample-night-shift-coffee.md"


def validate_pack(text: str) -> list[str]:
    failures: list[str] = []
    required = (
        "## Provenance Reservoir",
        "## Derivation Spine",
        "## Portfolio Matrix",
        "## Prop-Grade Briefs",
        "## Artifact-vs-Merch Verdicts",
        "## Craft Calibration",
        "## Commit Harder",
        "## Prototype Plan",
    )
    for heading in required:
        if heading not in text:
            failures.append(f"missing heading: {heading}")

    briefs = re.split(r"^### \d+\. ", text, flags=re.MULTILINE)[1:]
    if len(briefs) < 8:
        failures.append(f"expected >=8 artifact briefs, found {len(briefs)}")
    for index, brief in enumerate(briefs, start=1):
        for field in ("**Derivation:**", "**Functional job:**", "**Predicted behavior:**", "**Artifact-vs-merch:**"):
            if field not in brief:
                failures.append(f"brief {index} missing {field}")
    return failures


def main() -> int:
    required_paths = (
        SKILL / "workflows/artifact-forge.md",
        SKILL / "references/prompts-v2/artifact-forge-pack.md",
        SKILL / "references/artifact-pattern-library.md",
        SKILL / "references/source-mechanics-ledger.md",
        REPO / ".agent/workflows/artifact-forge.md",
        REPO / ".agents/skills/source-command-artifact-forge/SKILL.md",
        REPO / ".claude/commands/artifact-forge.md",
        SAMPLE,
    )
    failures = [f"missing: {path.relative_to(REPO)}" for path in required_paths if not path.is_file()]
    skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    if "workflows: 11" not in skill_text or "workflows/artifact-forge.md" not in skill_text:
        failures.append("SKILL.md does not register the 11th artifact workflow")

    if SAMPLE.is_file():
        failures.extend(validate_pack(SAMPLE.read_text(encoding="utf-8")))

    negative = """# Logo Tote\n## Prop-Grade Briefs\n### 1. Tote\n**Artifact-vs-merch:** logo on a generic tote\n"""
    if not validate_pack(negative):
        failures.append("negative control incorrectly passed")

    if failures:
        print("Artifact forge verifier: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Artifact forge verifier: PASS")
    print("- hot command surfaces present")
    print("- 9-brief cold-start pack passes")
    print("- generic logo-merch negative control fails")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
