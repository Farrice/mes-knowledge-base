#!/usr/bin/env python3
"""Deterministic positive and negative controls for Jun Format Intelligence."""

from __future__ import annotations

import json
import sys
from pathlib import Path

from workflow_router import search_workflows


ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "extractions/jun-yuh-story-marketing-system/fixtures/format-intelligence-cases.json"
REQUIRED = (
    "skills/jun-yuh-creator-vision/workflows/format-intelligence-lab.md",
    "skills/jun-yuh-creator-vision/references/prompts-v2/format-intelligence-lab.md",
    "extractions/video-context/TY9OrhsUsjM/analysis.md",
    "extractions/video-context/-f1XbEJ9sTs/analysis.md",
    "extractions/jun-yuh-story-marketing-system/format-intelligence-capability-proof.md",
    "extractions/jun-yuh-story-marketing-system/farrice-autonomous-campaign-proof.md",
    "extractions/jun-yuh-story-marketing-system/client-story-marketing-os-install.md",
)


def format_state(case: dict[str, object]) -> str:
    if bool(case.get("direct_work")):
        return "NO_FORMAT"
    if not bool(case.get("concept_source_traced")):
        return "NEEDS_SOURCE"
    if int(case.get("reference_count", 0)) == 0 and not bool(case.get("research_authorized")):
        return "NEEDS_REFERENCE_SET"
    if int(case.get("candidate_count", 0)) < 3:
        return "NEEDS_COMPARISON"
    if bool(case.get("selected_requires_unsupported_proof")):
        return "NO_FIT"
    if not bool(case.get("message_locked")):
        return "NEEDS_MESSAGE"
    return "FORMAT_READY"


def require_tokens(relative: str, tokens: tuple[str, ...], failures: list[str]) -> None:
    body = (ROOT / relative).read_text(encoding="utf-8")
    for token in tokens:
        if token not in body:
            failures.append(f"{relative}: missing {token!r}")


def main() -> int:
    failures: list[str] = []
    for relative in REQUIRED:
        if not (ROOT / relative).is_file():
            failures.append(f"missing required file: {relative}")
    if failures:
        print("JUN FORMAT INTELLIGENCE VERIFY: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    results: dict[str, str] = {}
    for case in json.loads(FIXTURES.read_text(encoding="utf-8"))["cases"]:
        actual = format_state(case)
        results[str(case["id"])] = actual
        if actual != case["expected"]:
            failures.append(f"{case['id']}: expected {case['expected']}, got {actual}")

    require_tokens("skills/jun-yuh-creator-vision/workflows/format-intelligence-lab.md", ("7x7", "VISUALS / EDITING", "read-aloud test", "MARKET PROOF: NO EVENT", "NO FIT"), failures)
    require_tokens("skills/jun-yuh-creator-vision/references/source-ledger.md", ("Universal 5-7 word overlay limit", "REJECTED AS UNIVERSAL RULE", "Trial Reel derivatives pass algorithmic detection", "UNCONFIRMED / REMOVED"), failures)
    require_tokens("extractions/jun-yuh-story-marketing-system/farrice-autonomous-campaign-proof.md", ("Five Meaning-Distinct Concepts", "Winning Concept Brief", "NO EVENT", "NEEDS SOURCE"), failures)
    require_tokens("extractions/jun-yuh-story-marketing-system/client-story-marketing-os-install.md", ("synthetic test business", "Before/after sleep transformation reel", "REJECT", "NO OFFER"), failures)

    queries = (
        "help me study winning formats before turning my story into content",
        "use Jun Yuh 7x7 to match my message to a proven content format",
        "build a story marketing system for a health brand without inventing claims",
    )
    routing: dict[str, list[str]] = {}
    for query in queries:
        names = [match[1]["name"] for match in search_workflows(query, top_n=5)]
        routing[query] = names[:3]
        if not any(name in {"junyuh-marketing", "jun-story-engine"} for name in names[:3]):
            failures.append(f"routing miss for {query!r}: {names[:3]}")

    if failures:
        print("JUN FORMAT INTELLIGENCE VERIFY: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1
    print("JUN FORMAT INTELLIGENCE VERIFY: PASS")
    print(f"- required files: {len(REQUIRED)}/{len(REQUIRED)}")
    print(f"- state controls: {results}")
    print(f"- routing controls: {routing}")
    print("- outcome boundary: structural capability PASS; reach, demand, and revenue remain NO EVENT")
    return 0


if __name__ == "__main__":
    sys.exit(main())

