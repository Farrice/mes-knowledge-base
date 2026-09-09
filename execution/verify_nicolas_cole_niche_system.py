#!/usr/bin/env python3
"""Deterministic verifier for the Nicolas Cole niche discovery skill system."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "nicolas-cole-niche-positioning"
WORKFLOWS = [
    "00-niche-discovery-system.md",
    "01-niche-evidence-research.md",
    "02-thirty-in-thirty-discovery.md",
    "03-service-industry-specialization.md",
    "04-niche-constellation-map.md",
    "05-niche-brief.md",
    "06-content-constellation-plan.md",
    "07-commit-or-pivot-audit.md",
]
PROMPTS = [name.removeprefix("00-").removeprefix("01-").removeprefix("02-").removeprefix("03-").removeprefix("04-").removeprefix("05-").removeprefix("06-").removeprefix("07-") for name in WORKFLOWS]


def require(condition: bool, message: str, failures: list[str]) -> None:
    if condition:
        print(f"PASS: {message}")
    else:
        print(f"FAIL: {message}")
        failures.append(message)


def main() -> int:
    failures: list[str] = []
    skill_text = (SKILL / "SKILL.md").read_text()
    genius_text = (SKILL / "genius.md").read_text()
    source_text = (SKILL / "references" / "source-ledger.md").read_text()

    require("version: 2.0" in skill_text, "skill upgraded to v2", failures)
    require("No meaningful evidence + creator path" in skill_text, "creator cold-start route exists", failures)
    require("choose the service before the industry" in skill_text, "service cold-start route exists", failures)
    require("## When Not to Use" in skill_text, "negative routing boundary exists", failures)
    require("not the universal entry route" in genius_text, "old specificity rule is demoted", failures)
    require("Niche clarity must never be described as market validation" in genius_text, "false-demand control exists", failures)
    require("Corrected Boundaries" in source_text and "UNCONFIRMED as literal Cole" in source_text, "source-derived boundary is explicit", failures)

    for workflow in WORKFLOWS:
        path = SKILL / "workflows" / workflow
        require(path.exists(), f"workflow exists: {workflow}", failures)
        if path.exists():
            require("Execution prompt:" in path.read_text(), f"workflow is wired: {workflow}", failures)

    for prompt in PROMPTS:
        path = SKILL / "references" / "prompts-v2" / prompt
        require(path.exists(), f"prompt exists: {prompt}", failures)
        if path.exists():
            text = path.read_text()
            require("source_prompt: born-v2" in text and "## Quality Gate" in text, f"prompt contract passes: {prompt}", failures)

    for video_id, minimum_rows in (("tOOVzQlSgCI", 9), ("0f-RLuOCTbg", 7)):
        package = ROOT / "extractions" / "video-context" / video_id
        required = ["transcript.txt", "transcript_segments.json", "metadata.json", "video-context-ledger.json", "analysis.md", "uncertainty-report.md"]
        require(all((package / item).exists() for item in required), f"source package complete: {video_id}", failures)
        ledger = json.loads((package / "video-context-ledger.json").read_text())
        spoken = [row for row in ledger if row.get("type") == "observed_spoken" and row.get("status") == "VERIFIED"]
        require(len(spoken) >= minimum_rows, f"spoken evidence rows present: {video_id}", failures)

    proof = (ROOT / "extractions" / "nicolas-cole-niche-system" / "behavior-proof.md").read_text()
    for control in ("False demand", "Forced specificity", "Permanent identity", "Premature service industry", "Pivot anxiety"):
        require(control in proof and "PASS" in proof, f"negative control recorded: {control}", failures)

    require(not (ROOT / "skills" / "nicolas-cole-niche-system").exists(), "no competing skill created", failures)
    print(f"RESULT: {'FAIL' if failures else 'PASS'} ({len(failures)} failures)")
    return 1 if failures else 0


if __name__ == "__main__":
    raise SystemExit(main())
