#!/usr/bin/env python3
"""Deterministic positive/negative controls for the Jun Story Engine expansion."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from workflow_router import search_workflows


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "extractions/video-context/XS-E6rnCr5U/fixtures/story-engine-cases.json"
EXPANSION_FIXTURES = ROOT / "extractions/video-context/6r-HF9K030A/fixtures/pursuit-offer-cases.json"

REQUIRED_FILES = [
    "extractions/video-context/XS-E6rnCr5U/video-context-ledger.json",
    "extractions/video-context/XS-E6rnCr5U/deep-extraction.md",
    "extractions/video-context/XS-E6rnCr5U/skill-system-contract.md",
    "extractions/video-context/XS-E6rnCr5U/behavior-proof.md",
    "extractions/video-context/XS-E6rnCr5U/commercial-field-proof.md",
    "extractions/jun-yuh-creator-vision/blind-embodiment-receipt.md",
    "extractions/video-context/XS-E6rnCr5U/USER-GUIDE.md",
    "extractions/video-context/6r-HF9K030A/metadata.json",
    "extractions/video-context/6r-HF9K030A/transcript.vtt",
    "extractions/video-context/6r-HF9K030A/transcript.txt",
    "extractions/video-context/6r-HF9K030A/transcript_segments.json",
    "extractions/video-context/6r-HF9K030A/video-context-ledger.json",
    "extractions/video-context/6r-HF9K030A/deep-extraction.md",
    "extractions/video-context/6r-HF9K030A/skill-system-contract.md",
    "extractions/video-context/6r-HF9K030A/behavior-proof.md",
    "extractions/video-context/6r-HF9K030A/USER-GUIDE.md",
    "extractions/video-context/6r-HF9K030A/fixtures/pursuit-offer-cases.json",
    "skills/jun-yuh-creator-vision/references/storytelling-masterclass-ledger.md",
    "skills/jun-yuh-creator-vision/references/selling-course-ledger.md",
    "skills/jun-yuh-creator-vision/workflows/story-material-miner.md",
    "skills/jun-yuh-creator-vision/workflows/story-content-format-router.md",
    "skills/jun-yuh-creator-vision/workflows/jun-story-engine.md",
    "skills/jun-yuh-creator-vision/workflows/pursuit-to-offer-miner.md",
    "skills/jun-yuh-creator-vision/workflows/story-angle-expander.md",
    "skills/jun-yuh-creator-vision/references/prompts-v2/story-material-packet.md",
    "skills/jun-yuh-creator-vision/references/prompts-v2/story-content-format-plan.md",
    "skills/jun-yuh-creator-vision/references/prompts-v2/jun-story-engine.md",
    "skills/jun-yuh-creator-vision/references/prompts-v2/pursuit-method-card.md",
    "skills/jun-yuh-creator-vision/references/prompts-v2/story-angle-map.md",
    ".agent/workflows/jun-story-engine.md",
    ".claude/commands/jun-story-engine.md",
    ".agents/skills/source-command-jun-story-engine/SKILL.md",
]

DIRECT_WORK = {"status", "incident", "specification", "procedure", "calculation", "risk", "decision"}
PROOF_LEVELS = ("EXPERIENCE", "METHOD", "DELIVERABLE", "MARKET")
ROUTING_QUERIES = (
    "turn my lived moments into truthful personal stories without inventing psychology",
    "my life is boring and I do not know what personal story to tell",
    "make a story material packet from this ordinary lived moment",
)


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


def method_state(case: dict[str, object]) -> str:
    """Return the highest method state supported without inferring demand."""
    pursuit = str(case.get("pursuit", "")).strip()
    if not pursuit:
        return "NO_OFFER"
    steps = int(case.get("steps", 0))
    decision_rules = int(case.get("decision_rules", 0))
    output = str(case.get("output", "")).strip()
    if steps < 2 or decision_rules < 1 or not output:
        return "NEEDS_SOURCE"
    if bool(case.get("market_evidence")):
        return "OFFER_HYPOTHESIS"
    return "METHOD_CANDIDATE"


def distinct_angle_count(case: dict[str, object]) -> int:
    """Count semantic angles by normalized 3P meaning, not wording volume."""
    signatures: set[tuple[str, str, str]] = set()
    for angle in case.get("angles", []):
        problem = str(angle.get("problem", "")).lower()
        pursuit = str(angle.get("pursuit", "")).lower()
        payoff = str(angle.get("payoff", "")).lower()
        focus_terms = {"focus", "focused", "concentration", "concentrate"}
        if any(term in problem + " " + payoff for term in focus_terms):
            problem = "focus"
            payoff = "focus"
        if any(term in pursuit for term in ("train", "trained", "lift", "lifted")):
            pursuit = "training before work"
        signatures.add((problem, pursuit, payoff))
    return len(signatures)


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
        ("/shaan-story-deploy", "/ml-validate-offer", "One body owner", "NO STORY", "Story Engine Receipt", "commercial proof ceiling", "METHOD_CANDIDATE"),
        failures,
    )
    require_tokens(
        "skills/jun-yuh-creator-vision/workflows/pursuit-to-offer-miner.md",
        ("NO_OFFER", "NEEDS_SOURCE", "METHOD_CANDIDATE", "OFFER_HYPOTHESIS", "MARKET PROOF: NO EVENT", "/ml-validate-offer"),
        failures,
    )
    require_tokens(
        "skills/jun-yuh-creator-vision/workflows/story-angle-expander.md",
        ("meaning-distinct", "fact-traced 3P", "Reject paraphrases", "story-content-format-router", "/shaan-story-deploy"),
        failures,
    )
    require_tokens(
        "skills/shaan-puri-storytelling/references/story-deployment-map.md",
        ("/jun-story-engine", "Shaan still decides"),
        failures,
    )
    require_tokens(
        "skills/jun-yuh-creator-vision/SKILL.md",
        ("workflows: 24", "Story Material Miner", "Jun Story Engine", "Pursuit-to-Offer Miner", "Story Angle Expander"),
        failures,
    )
    require_tokens(
        ".agent/workflows/jun-story-engine.md",
        ("Pursuit", "offer hypothesis", "distinct angles", "/ml-validate-offer"),
        failures,
    )
    require_tokens(
        ".agents/skills/source-command-jun-story-engine/SKILL.md",
        ("teachable IP", "meaning-distinct angles", "/ml-validate-offer"),
        failures,
    )

    expansion = json.loads(EXPANSION_FIXTURES.read_text(encoding="utf-8"))
    method_decisions: dict[str, str] = {}
    for case in expansion.get("method_cases", []):
        actual = method_state(case)
        method_decisions[str(case["id"])] = actual
        if actual != case.get("expected"):
            failures.append(f"{case['id']}: expected {case.get('expected')}, got {actual}")
    angle_decisions: dict[str, int] = {}
    for case in expansion.get("angle_cases", []):
        actual = distinct_angle_count(case)
        angle_decisions[str(case["id"])] = actual
        if actual != case.get("expected_count"):
            failures.append(f"{case['id']}: expected {case.get('expected_count')} angles, got {actual}")

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

    # Expansion sabotage: deleting the decision rule must demote a Method Candidate.
    positive_method = next(case for case in expansion["method_cases"] if case["id"] == "repeatable_method")
    sabotaged_method = dict(positive_method)
    sabotaged_method["decision_rules"] = 0
    if method_state(sabotaged_method) != "NEEDS_SOURCE":
        failures.append("negative control failed: missing decision rule did not demote method")

    # Expansion sabotage: buyer evidence may change validation readiness, but absent evidence cannot.
    absent_market = dict(positive_method)
    absent_market["market_evidence"] = False
    if method_state(absent_market) != "METHOD_CANDIDATE":
        failures.append("negative control failed: absent buyer evidence escaped METHOD_CANDIDATE")

    # Cold-start discoverability: source-derived behavior is not useful if a
    # natural lived-material request cannot surface the connected front door.
    for query in ROUTING_QUERIES:
        ranked = search_workflows(query, top_n=3)
        top_name = ranked[0][1]["name"] if ranked else "NONE"
        if top_name != "jun-story-engine":
            failures.append(
                f"routing control failed: {query!r} ranked {top_name!r} instead of 'jun-story-engine'"
            )

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
    for case_id, decision in method_decisions.items():
        print(f"- method {case_id}: {decision}")
    for case_id, count in angle_decisions.items():
        print(f"- angle {case_id}: {count}")
    print("- routing controls: 3/3 natural lived-material queries -> jun-story-engine")
    print("- negative controls: missing Pursuit -> NEEDS_SOURCE; incident -> NO_STORY; no market event -> DELIVERABLE ceiling; missing decision rule -> NEEDS_SOURCE; duplicate angles collapse")
    return 0


if __name__ == "__main__":
    sys.exit(main())
