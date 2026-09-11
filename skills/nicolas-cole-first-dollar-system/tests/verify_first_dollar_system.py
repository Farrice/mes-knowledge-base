#!/usr/bin/env python3
"""Verify the Nicolas Cole first-dollar connected skill system."""

from __future__ import annotations

import json
from pathlib import Path


SKILL_ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = SKILL_ROOT.parents[1]
SOURCE_ROOT = REPO_ROOT / "extractions" / "video-context" / "sfABlt-pTd0"

WORKFLOWS = (
    "01-first-dollar-roadmap.md",
    "02-information-advantage-audit.md",
    "03-congruence-supply-chain.md",
    "04-offer-time-horizon-router.md",
    "05-customer-improvement-loop.md",
)

PROMPTS = (
    "first-dollar-roadmap.md",
    "information-advantage-audit.md",
    "congruence-supply-chain.md",
    "offer-time-horizon-router.md",
    "customer-improvement-loop.md",
)

WORKFLOW_HEADINGS = (
    "## Input Required",
    "## Protocol",
    "## Output Contract",
    "## Quality Gate",
    "Execution prompt:",
)

PROMPT_HEADINGS = (
    "## Role & Activation",
    "## Input Required",
    "## Execution Protocol",
    "## Output Contract",
    "## Output Skeleton",
    "## Quality Gate",
    "## Deploy When",
)


def require(path: Path, failures: list[str]) -> str:
    if not path.exists():
        failures.append(f"missing file: {path.relative_to(REPO_ROOT)}")
        return ""
    text = path.read_text(encoding="utf-8", errors="replace")
    if not text.strip():
        failures.append(f"empty file: {path.relative_to(REPO_ROOT)}")
    return text


def main() -> int:
    failures: list[str] = []

    skill_text = require(SKILL_ROOT / "SKILL.md", failures)
    genius_text = require(SKILL_ROOT / "genius.md", failures)
    source_ledger = require(SOURCE_ROOT / "video-context-ledger.md", failures)
    contract = require(SOURCE_ROOT / "skill-system-contract.md", failures)
    behavior = require(SOURCE_ROOT / "behavior-proof.md", failures)
    negative = require(SKILL_ROOT / "tests" / "receipts" / "urgent-cash-no-audience-output.md", failures)
    workflow_wrapper = require(REPO_ROOT / ".agent" / "workflows" / "nicolas-cole-first-dollar.md", failures)
    claude_wrapper = require(REPO_ROOT / ".claude" / "commands" / "nicolas-cole-first-dollar.md", failures)
    codex_wrapper = require(
        REPO_ROOT / ".agents" / "skills" / "source-command-nicolas-cole-first-dollar" / "SKILL.md",
        failures,
    )

    for filename in WORKFLOWS:
        text = require(SKILL_ROOT / "workflows" / filename, failures)
        for heading in WORKFLOW_HEADINGS:
            if heading not in text:
                failures.append(f"{filename}: missing {heading}")

    for filename in PROMPTS:
        text = require(SKILL_ROOT / "references" / "prompts-v2" / filename, failures)
        for heading in PROMPT_HEADINGS:
            if heading not in text:
                failures.append(f"{filename}: missing {heading}")

    for required in (
        "nicolas-cole-niche-positioning",
        "nicolas-cole-library-first-writing",
        "nicolas-cole-newsletter-flywheel",
        "nicolas-cole-digital-products",
        "nicolas-cole-client-acquisition",
        "/first-10k",
        "NO EVENT",
    ):
        if required not in skill_text:
            failures.append(f"SKILL.md missing connected owner or proof state: {required}")

    for timestamp in ("05:32", "10:35", "20:30", "35:47", "42:31", "47:17", "50:34", "56:40"):
        if timestamp not in source_ledger:
            failures.append(f"source ledger missing anchor: {timestamp}")

    for field in (
        "Source evidence",
        "Objective",
        "Components",
        "Step order",
        "Handoff summary",
        "Composition rule",
        "Human checkpoint",
        "Validation",
        "Behavior-changing proof",
        "Context policy",
        "Reuse hook",
    ):
        if f"| {field} |" not in contract:
            failures.append(f"skill-system contract missing field: {field}")

    for field in (
        "## Input Tested",
        "## Weakness Diagnosed",
        "## Source Mechanics Used",
        "## Output Produced",
        "## Behavior Delta",
        "## Validation Run",
        "## Remaining Risk",
    ):
        if field not in behavior:
            failures.append(f"behavior proof missing field: {field}")

    # Negative control: urgent cash plus no audience must not become a
    # newsletter/course prerequisite or a false revenue claim.
    for required in ("Service-first", "/first-10k", "Newsletter-first: parked", "Course-first: parked", "NO EVENT"):
        if required not in negative:
            failures.append(f"negative-control receipt missing: {required}")
    if "guaranteed" in negative.lower():
        failures.append("negative-control receipt contains a guaranteed-outcome claim")

    segments_path = SOURCE_ROOT / "transcript_segments.json"
    if segments_path.exists():
        try:
            segments = json.loads(segments_path.read_text(encoding="utf-8"))
            if len(segments) < 1000:
                failures.append("source transcript has fewer than 1000 timestamped segments")
        except json.JSONDecodeError as exc:
            failures.append(f"source transcript segments invalid JSON: {exc}")

    if "Information-Advantage Load Reduction" not in genius_text:
        failures.append("genius.md missing source-derived information-advantage mechanic")

    for name, text in (
        ("workflow wrapper", workflow_wrapper),
        ("Claude wrapper", claude_wrapper),
        ("Codex wrapper", codex_wrapper),
    ):
        if "nicolas-cole-first-dollar-system" not in text:
            failures.append(f"{name} does not point to the canonical skill")

    if failures:
        print("Nicolas Cole first-dollar system: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Nicolas Cole first-dollar system: PASS")
    print(f"- workflows: {len(WORKFLOWS)}/{len(WORKFLOWS)}")
    print(f"- structure-pure prompts: {len(PROMPTS)}/{len(PROMPTS)}")
    print("- source anchors: 8/8")
    print("- command surfaces: workflow + Claude + Codex wrappers")
    print("- negative control: urgent cash routes service-first; newsletter/course parked")
    print("- commercial proof boundary: NO EVENT preserved")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
