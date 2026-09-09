#!/usr/bin/env python3
"""Verify the skill-local Seth Godin AI Creative Practice extension."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
PACKAGE = ROOT / "extractions/video-context/DHTgH34inHY"
SKILL = ROOT / "skills/seth-godin-philosophy"


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str, failures: list[str]) -> None:
    if not condition:
        failures.append(message)


def main() -> int:
    failures: list[str] = []
    required = [
        PACKAGE / "metadata.json",
        PACKAGE / "transcript.vtt",
        PACKAGE / "transcript.txt",
        PACKAGE / "transcript_segments.json",
        PACKAGE / "video-context-ledger.md",
        PACKAGE / "video-context-ledger.json",
        PACKAGE / "evidence-ledger.md",
        PACKAGE / "uncertainty-report.md",
        PACKAGE / "visual-references.md",
        PACKAGE / "analysis.md",
        PACKAGE / "overlap-build-shape.md",
        PACKAGE / "behavior-proof.md",
        PACKAGE / "recognition-review.md",
        PACKAGE / "production-receipt-01-linkedin-cash-launch.md",
        PACKAGE / "manifest.json",
        SKILL / "workflows/10-ai-creative-practice.md",
        SKILL / "references/prompts-v2/ai-creative-practice-design.md",
        SKILL / "references/prompts-v2/ai-creative-practice-traction-review.md",
        ROOT / ".agent/workflows/godin-ai-creative-practice.md",
    ]
    for path in required:
        require(path.is_file() and path.stat().st_size > 0, f"missing or empty: {path.relative_to(ROOT)}", failures)

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1

    metadata = json.loads((PACKAGE / "metadata.json").read_text())
    segments = json.loads((PACKAGE / "transcript_segments.json").read_text())
    ledger = json.loads((PACKAGE / "video-context-ledger.json").read_text())
    manifest = json.loads((PACKAGE / "manifest.json").read_text())
    require(metadata.get("id") == "DHTgH34inHY", "metadata video id drift", failures)
    require(metadata.get("duration") == 3729, "source duration must be 3729 seconds", failures)
    require(metadata.get("source_scope") == "whole video", "source scope is not whole video", failures)
    require(len(segments) == 1574, f"caption count must be 1574, found {len(segments)}", failures)
    require(all(row.get("start") and row.get("end") and row.get("text") for row in segments), "caption rows lack timestamp/text", failures)
    require(sum(row.get("type") == "observed_spoken" for row in ledger) == 1574, "spoken ledger count drift", failures)
    require(sum(row.get("type") == "observed_visual" for row in ledger) == 7, "visual ledger count drift", failures)

    manifest_rows = {row["path"]: row for row in manifest.get("files", [])}
    for relative, row in manifest_rows.items():
        path = PACKAGE / relative
        require(path.is_file(), f"manifest path missing: {relative}", failures)
        if path.is_file():
            require(row.get("sha256") == sha256(path), f"checksum drift: {relative}", failures)

    workflow = (SKILL / "workflows/10-ai-creative-practice.md").read_text()
    for token in (
        "[DESIRED_CHANGE]", "[SMALLEST_VIABLE_AUDIENCE]", "[CONSTRAINTS]",
        "[HUMAN_ONLY_DECISIONS]", "[CANDIDATE_AI_TASKS]", "[FAILURE_BUDGET]",
        "[EVIDENCE]", "[PUBLISHING_BOUNDARY]", "Project Ownership Lock",
        "System Gap Map", "Proud Artifact Spec", "Bounded AI Task Packets",
        "Three-Step Cheap Failure Ladder", "Traction Measures", "STOP:",
        "ITERATE:", "SCALE:", "KILL:", "draft five posts", "seth-godin-brand",
    ):
        require(token in workflow, f"workflow contract missing token: {token}", failures)
    require("Do not delegate the desired change" in workflow, "objective delegation prohibition missing", failures)
    require("exactly three" in workflow.lower(), "three-rung constraint missing", failures)

    for prompt_name in ("ai-creative-practice-design.md", "ai-creative-practice-traction-review.md"):
        prompt = (SKILL / "references/prompts-v2" / prompt_name).read_text()
        for heading in (
            "## Role & Activation", "## Input Required", "## Execution Protocol",
            "## Output Contract", "## Output Skeleton", "## Quality Gate", "## Deploy When",
        ):
            require(heading in prompt, f"{prompt_name} missing {heading}", failures)
        require("source_prompt: born-v2" in prompt, f"{prompt_name} is not born-v2", failures)

    skill_manifest = (SKILL / "SKILL.md").read_text()
    agent = (ROOT / "agents/seth-godin/AGENT.md").read_text()
    bridge = (ROOT / ".agent/workflows/godin-ai-creative-practice.md").read_text()
    slash_index = (ROOT / "SLASH_COMMANDS.md").read_text()
    skill_index = (ROOT / "SKILL_INDEX.md").read_text()
    proof = (PACKAGE / "behavior-proof.md").read_text()
    production_receipt = (PACKAGE / "production-receipt-01-linkedin-cash-launch.md").read_text()
    require("workflows: 10" in skill_manifest, "skill workflow count not updated", failures)
    require("ai-creative-practice-design.md" in skill_manifest, "design prompt not wired", failures)
    require("ai-creative-practice-traction-review.md" in skill_manifest, "review prompt not wired", failures)
    require("/godin-ai-creative-practice" in agent, "existing Seth Godin agent not extended", failures)
    require("description:" in bridge and "worth shipping" in bridge, "searchable command description missing", failures)
    require("/godin-ai-creative-practice" in slash_index, "slash index lacks command", failures)
    require("| 10 | 0 |" in skill_index, "skill index workflow count not regenerated", failures)
    for criterion in (
        "Human owns objective", "AI receives bounded tasks", "Audience and system gap",
        "Capped inexpensive experiments", "Usable proud artifact", "Real traction measures",
        "Explicit decision",
    ):
        require(criterion in proof and "PASS" in proof, f"behavior proof missing criterion: {criterion}", failures)
    for token in (
        "Project Ownership Lock", "System Gap Map", "Proud Artifact Spec",
        "Bounded AI Task Packets", "Cheap Failure Ladder", "Traction Contract",
        "**STOP**", "traction `NO EVENT`", "Publishing: OFF",
    ):
        require(token in production_receipt, f"production receipt missing token: {token}", failures)

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        return 1
    print("Seth Godin AI Creative Practice verifier: PASS")
    print("- source: 3729 seconds, 1574 caption cues, 7 inspected frames")
    print("- skill: workflow 10, 2 born-v2 prompts, generated registry presence")
    print("- behavior: ownership, bounded tasks, gap, artifact, 3 experiments, traction, verdict")
    print("- production: first current-project receipt exists; external traction remains NO EVENT")
    print("- recognition: fresh blind FAIL, honest tier B; A-tier remains unearned")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
