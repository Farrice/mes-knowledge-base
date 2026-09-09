#!/usr/bin/env python3
"""Verify the source-grounded Brock Say–Do–Need bridge and sabotage paths."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "extractions/video-context/MX-Emk6vkE4/fixtures/say-do-need-cases.json"
REQUIRED_FILES = (
    "extractions/video-context/MX-Emk6vkE4/metadata.json",
    "extractions/video-context/MX-Emk6vkE4/transcript.txt",
    "extractions/video-context/MX-Emk6vkE4/transcript_segments.json",
    "extractions/video-context/MX-Emk6vkE4/video-context-ledger.json",
    "extractions/video-context/MX-Emk6vkE4/uncertainty-report.md",
    "extractions/video-context/MX-Emk6vkE4/analysis.md",
    "extractions/video-context/MX-Emk6vkE4/deep-extraction.md",
    "extractions/video-context/MX-Emk6vkE4/skill-system-contract.md",
    "extractions/video-context/MX-Emk6vkE4/behavior-proof.md",
    "extractions/video-context/MX-Emk6vkE4/blind-pass-receipt.md",
    "skills/brock-johnson-shareworthy-content/workflows/say-do-need-message-bridge.md",
    "skills/brock-johnson-shareworthy-content/references/prompts-v2/say-do-need-message-bridge.md",
)


def decide(case: dict[str, object]) -> str:
    """Return the nearest safe continuation for a bridge evidence packet."""
    if not case.get("say_evidence") or not case.get("do_evidence"):
        return "NEEDS_EVIDENCE"
    if case.get("regulated_claim"):
        return "HUMAN_REVIEW"
    if not case.get("promise_delivered"):
        return "REJECT_BAIT_SWITCH"
    if case.get("need_support") in (None, "", "untested"):
        return "UNTESTED_BRIDGE"
    return "READY_TO_TEST"


def require_tokens(path: str, tokens: tuple[str, ...], failures: list[str]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for token in tokens:
        if token not in text:
            failures.append(f"{path}: missing token {token!r}")


def main() -> int:
    failures: list[str] = []
    for relative in REQUIRED_FILES:
        path = ROOT / relative
        if not path.is_file() or path.stat().st_size == 0:
            failures.append(f"missing or empty required file: {relative}")

    if failures:
        print("BROCK SAY-DO-NEED VERIFY: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    require_tokens(
        "skills/brock-johnson-shareworthy-content/workflows/say-do-need-message-bridge.md",
        ("SAY", "DO", "NEED", "Promise Integrity", "UNTESTED", "Execution prompt:"),
        failures,
    )
    require_tokens(
        "skills/brock-johnson-shareworthy-content/references/prompts-v2/say-do-need-message-bridge.md",
        ("source_prompt: born-v2", "## Output Contract", "## Output Skeleton", "## Quality Gate", "## Deploy When"),
        failures,
    )
    require_tokens(
        "skills/brock-johnson-shareworthy-content/SKILL.md",
        ("workflows: 4", "Say–Do–Need Message Bridge", "MX-Emk6vkE4"),
        failures,
    )
    require_tokens(
        "extractions/video-context/MX-Emk6vkE4/behavior-proof.md",
        ("REJECT_BAIT_SWITCH", "NO EVENT", "UNTESTED", "Promise-to-payload audit"),
        failures,
    )
    require_tokens(
        "extractions/video-context/MX-Emk6vkE4/blind-pass-receipt.md",
        ("NOT RUN", "B-tier", "0 of the required 2", "Market performance"),
        failures,
    )

    payload = json.loads(FIXTURES.read_text(encoding="utf-8"))
    cases = payload.get("cases", [])
    if len(cases) < 6:
        failures.append("fixture suite must contain at least six cases")

    decisions: dict[str, str] = {}
    for case in cases:
        actual = decide(case)
        case_id = str(case.get("id"))
        decisions[case_id] = actual
        if actual != case.get("expected"):
            failures.append(f"{case_id}: expected {case.get('expected')}, got {actual}")

    positive = next(case for case in cases if case.get("id") == "ready_bridge")
    sabotage = dict(positive)
    sabotage["promise_delivered"] = False
    if decide(sabotage) != "REJECT_BAIT_SWITCH":
        failures.append("negative control failed: broken promise was not rejected")

    sabotage = dict(positive)
    sabotage["do_evidence"] = False
    if decide(sabotage) != "NEEDS_EVIDENCE":
        failures.append("negative control failed: missing behavior evidence was not caught")

    sabotage = dict(positive)
    sabotage["need_support"] = "untested"
    if decide(sabotage) != "UNTESTED_BRIDGE":
        failures.append("negative control failed: unsupported Need was promoted")

    if failures:
        print("BROCK SAY-DO-NEED VERIFY: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("BROCK SAY-DO-NEED VERIFY: PASS")
    print(f"- required files: {len(REQUIRED_FILES)}/{len(REQUIRED_FILES)}")
    print(f"- fixtures: {len(cases)}/{len(cases)}")
    for case_id, decision in decisions.items():
        print(f"- {case_id}: {decision}")
    print("- negative controls: broken promise, missing behavior evidence, unsupported Need")
    return 0


if __name__ == "__main__":
    sys.exit(main())
