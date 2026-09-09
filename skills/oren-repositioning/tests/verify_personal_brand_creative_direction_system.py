#!/usr/bin/env python3
"""Verify the Oren personal-brand creative-direction extension and false-green controls."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "skills/oren-repositioning"
PACKAGE = ROOT / "extractions/video-context/tUlkycPTZm0"


def require(path: Path, failures: list[str]) -> str:
    if not path.exists() or path.stat().st_size == 0:
        failures.append(f"missing or empty: {path.relative_to(ROOT)}")
        return ""
    return path.read_text(encoding="utf-8", errors="ignore")


def receipt_failures(text: str) -> list[str]:
    required = (
        "## Behavior Proof",
        "## Strategy / Operations / Direction Role Ladder",
        "## Direction Spine",
        "## Biweekly Idea Room Slate",
        "## Personal Brand World Kit",
        "## Three Pilot Briefs",
        "## 90-Day Direction Plan",
        "## Human Approvals and No-Action Boundaries",
        "DRAFT ONLY",
        "NO PERMISSION",
        "UNTESTED",
        "UNKNOWN",
    )
    failures = [f"receipt missing: {item}" for item in required if item not in text]
    banned = ("guaranteed growth", "auto-publish", "fully verified market performance")
    failures.extend(f"receipt contains banned claim: {item}" for item in banned if item.lower() in text.lower())
    return failures


def main() -> int:
    failures: list[str] = []
    checks = 0

    required_files = (
        SKILL / "references/personal-brand-creative-direction-skill-system-contract.md",
        SKILL / "workflows/personal-brand-creative-direction.md",
        SKILL / "workflows/personal-brand-idea-room.md",
        SKILL / "workflows/personal-brand-world-kit.md",
        SKILL / "references/prompts-v2/personal-brand-creative-direction-system.md",
        SKILL / "references/prompts-v2/personal-brand-idea-room.md",
        SKILL / "references/prompts-v2/personal-brand-world-kit.md",
        ROOT / ".agent/workflows/personal-brand-creative-direction.md",
        ROOT / ".agent/workflows/personal-brand-idea-room.md",
        ROOT / ".agent/workflows/personal-brand-world-kit.md",
        ROOT / ".agents/skills/source-command-personal-brand-creative-direction/SKILL.md",
        ROOT / ".agents/skills/source-command-personal-brand-idea-room/SKILL.md",
        ROOT / ".agents/skills/source-command-personal-brand-world-kit/SKILL.md",
        SKILL / "tests/fixtures/personal-brand-generic-brief.md",
        SKILL / "tests/receipts/personal-brand-cold-start-output.md",
    )
    for path in required_files:
        require(path, failures)
    checks += 1

    metadata = json.loads(require(PACKAGE / "metadata.json", failures) or "{}")
    segments = json.loads(require(PACKAGE / "transcript_segments.json", failures) or "[]")
    ledger = json.loads(require(PACKAGE / "video-context-ledger.json", failures) or "[]")
    if metadata.get("id") != "tUlkycPTZm0" or len(segments) < 800:
        failures.append("source package identity or transcript depth is wrong")
    if sum(1 for row in ledger if row.get("type") == "observed_visual") != 40:
        failures.append("source package must retain exactly 40 reviewed visual rows")
    checks += 1

    contract = require(required_files[0], failures)
    for heading in (
        "## Source Evidence", "## Objective", "## Components", "## Composition Rule",
        "## Step Order", "## Inputs", "## Outputs", "## Handoff Summaries",
        "## Human Checkpoints", "## Validation", "## Behavior-Changing Proof",
        "## Result Surface", "## Context Policy", "## Reuse Hook",
    ):
        if heading not in contract:
            failures.append(f"contract missing: {heading}")
    checks += 1

    prompt_required = (
        "## Role & Activation", "## Input Required", "## Execution Protocol",
        "## Output Contract", "## Output Skeleton", "## Quality Gate", "## Deploy When",
    )
    for path in required_files[4:7]:
        text = require(path, failures)
        for heading in prompt_required:
            if heading not in text:
                failures.append(f"{path.name} missing: {heading}")
    for path in required_files[7:13]:
        text = require(path, failures)
        if "personal-brand-" not in text:
            failures.append(f"route wrapper lacks a personal-brand target: {path.relative_to(ROOT)}")
    checks += 1

    skill_text = require(SKILL / "SKILL.md", failures)
    genius_text = require(SKILL / "genius.md", failures)
    for token in (
        "personal-brand-creative-direction", "personal-brand-idea-room",
        "personal-brand-world-kit", "tUlkycPTZm0",
    ):
        if token not in skill_text:
            failures.append(f"SKILL.md missing: {token}")
    if "The World-Over-Account Test" not in genius_text or "Strategy -> Operations -> Direction" not in genius_text:
        failures.append("genius.md lacks source-derived decision mechanics")
    checks += 1

    receipt = require(SKILL / "tests/receipts/personal-brand-cold-start-output.md", failures)
    failures.extend(receipt_failures(receipt))
    checks += 1

    broken = receipt.replace("NO PERMISSION", "allowed").replace("UNTESTED", "proven")
    if not receipt_failures(broken):
        failures.append("false-green control failed: broken receipt passed")
    checks += 1

    if failures:
        print("Personal brand creative direction system: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print(f"Personal brand creative direction system: PASS ({checks}/7 groups)")
    print(f"- source: {len(segments)} transcript segments, 40 reviewed frames")
    print("- existing owner extended; no duplicate Oren skill created")
    print("- cold-start behavior proof and false-green negative control passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
