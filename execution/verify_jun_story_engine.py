#!/usr/bin/env python3
"""Deterministic positive/negative controls for the Jun Story Engine expansion."""

from __future__ import annotations

import json
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "extractions/video-context/XS-E6rnCr5U/fixtures/story-engine-cases.json"

REQUIRED_FILES = [
    "extractions/video-context/XS-E6rnCr5U/video-context-ledger.json",
    "extractions/video-context/XS-E6rnCr5U/deep-extraction.md",
    "extractions/video-context/XS-E6rnCr5U/skill-system-contract.md",
    "extractions/video-context/XS-E6rnCr5U/behavior-proof.md",
    "extractions/video-context/XS-E6rnCr5U/commercial-field-proof.md",
    "extractions/jun-yuh-creator-vision/blind-embodiment-receipt.md",
    "extractions/video-context/XS-E6rnCr5U/USER-GUIDE.md",
    "skills/jun-yuh-creator-vision/references/storytelling-masterclass-ledger.md",
    "skills/jun-yuh-creator-vision/workflows/story-material-miner.md",
    "skills/jun-yuh-creator-vision/workflows/story-content-format-router.md",
    "skills/jun-yuh-creator-vision/workflows/jun-story-engine.md",
    "skills/jun-yuh-creator-vision/references/prompts-v2/story-material-packet.md",
    "skills/jun-yuh-creator-vision/references/prompts-v2/story-content-format-plan.md",
    "skills/jun-yuh-creator-vision/references/prompts-v2/jun-story-engine.md",
    ".agent/workflows/jun-story-engine.md",
    ".claude/commands/jun-story-engine.md",
    ".agents/skills/source-command-jun-story-engine/SKILL.md",
]

DIRECT_WORK = {"status", "incident", "specification", "procedure", "calculation", "risk", "decision"}
PROOF_LEVELS = ("EXPERIENCE", "METHOD", "DELIVERABLE", "MARKET")


def decide(case: dict[str, object]) -> str:
    """Return the smallest narrative state supported by the fixture."""
    if str(case.get("work_type", "")).lower() in DIRECT_WORK:
        return "NO_STORY"
    if not str(case.get("pursuit", "")).strip():
        return "NEEDS_SOURCE"
    if bool(case.get("privacy_sensitive")):
        return "STORY_FRAGMENT_CANDIDATE"
    full_fields = ("problem", "pursuit", "payoff", "want", "obstacle", "turn", "change")
    if all(str(case.get(field, "")).strip() for field in full_fields):
        return "FULL_STORY_CANDIDATE"
    if any(str(case.get(field, "")).strip() for field in ("problem", "pursuit", "payoff")):
        return "STORY_FRAGMENT_CANDIDATE"
    return "NO_STORY"


def proof_ceiling(case: dict[str, object]) -> str:
    """Return the highest evidence-backed commercial proof level."""
    flags = {
        "EXPERIENCE": "experience_evidence",
        "METHOD": "method_evidence",
        "DELIVERABLE": "deliverable_evidence",
        "MARKET": "market_evidence",
    }
    ceiling = "NONE"
    for level in PROOF_LEVELS:
        if bool(case.get(flags[level])):
            ceiling = level
    return ceiling


def require_tokens(path: str, tokens: tuple[str, ...], failures: list[str]) -> None:
    text = (ROOT / path).read_text(encoding="utf-8")
    for token in tokens:
        if token not in text:
            failures.append(f"{path}: missing token {token!r}")


def main() -> int:
    failures: list[str] = []
    for relative in REQUIRED_FILES:
        if not (ROOT / relative).is_file():
            failures.append(f"missing required file: {relative}")

    if failures:
        print("JUN STORY ENGINE VERIFY: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    payload = json.loads(FIXTURES.read_text(encoding="utf-8"))
    cases = payload.get("cases", [])
    if len(cases) < 5:
        failures.append("fixture suite must contain at least five cases")

    decisions: dict[str, str] = {}
    for case in cases:
        actual = decide(case)
        decisions[str(case["id"])] = actual
        if actual != case.get("expected"):
            failures.append(f"{case['id']}: expected {case.get('expected')}, got {actual}")
        expected_ceiling = case.get("expected_proof_ceiling")
        if expected_ceiling and proof_ceiling(case) != expected_ceiling:
            failures.append(
                f"{case['id']}: expected proof ceiling {expected_ceiling}, got {proof_ceiling(case)}"
            )

    require_tokens(
        "skills/jun-yuh-creator-vision/workflows/story-material-miner.md",
        ("LIFE", "Safe", "Real", "Raw", "[NEEDS SOURCE]", "NO STORY CANDIDATE", "Pursuit", "DOCUMENTED CONTRAST", "MARKET PROOF: NO EVENT"),
        failures,
    )
    require_tokens(
        "skills/jun-yuh-creator-vision/workflows/story-content-format-router.md",
        ("EMOTION-MATCHED ILLUSTRATIVE FOOTAGE", "CONTEMPORANEOUS EVIDENCE", "ATTRACT", "CONVERT"),
        failures,
    )
    require_tokens(
        "skills/jun-yuh-creator-vision/workflows/jun-story-engine.md",
        ("/shaan-story-deploy", "One body owner", "NO STORY", "Story Engine Receipt", "commercial proof ceiling"),
        failures,
    )
    require_tokens(
        "skills/shaan-puri-storytelling/references/story-deployment-map.md",
        ("/jun-story-engine", "Shaan still decides"),
        failures,
    )
    require_tokens(
        "skills/jun-yuh-creator-vision/SKILL.md",
        ("workflows: 16", "Story Material Miner", "Jun Story Engine"),
        failures,
    )

    # Negative control: removing Pursuit from a valid full candidate must change the decision.
    positive = next(case for case in cases if case["id"] == "positive_full_social")
    sabotaged = dict(positive)
    sabotaged["pursuit"] = ""
    if decide(sabotaged) != "NEEDS_SOURCE":
        failures.append("negative control failed: removing Pursuit did not trigger NEEDS_SOURCE")

    # Negative control: relabeling a full candidate as an incident must force direct communication.
    incident = dict(positive)
    incident["work_type"] = "incident"
    if decide(incident) != "NO_STORY":
        failures.append("negative control failed: incident did not trigger NO_STORY")

    # Negative control: a sample deliverable cannot silently become market proof.
    contrast = next(case for case in cases if case["id"] == "documented_contrast_unknown_turn")
    if proof_ceiling(contrast) != "DELIVERABLE":
        failures.append("negative control failed: absent market evidence did not cap proof at DELIVERABLE")

    if failures:
        print("JUN STORY ENGINE VERIFY: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("JUN STORY ENGINE VERIFY: PASS")
    print(f"- required files: {len(REQUIRED_FILES)}/{len(REQUIRED_FILES)}")
    print(f"- fixtures: {len(cases)}/{len(cases)}")
    for case_id, decision in decisions.items():
        print(f"- {case_id}: {decision}")
    print("- negative controls: missing Pursuit -> NEEDS_SOURCE; incident -> NO_STORY; no market event -> DELIVERABLE ceiling")
    return 0


if __name__ == "__main__":
    sys.exit(main())
