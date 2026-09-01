#!/usr/bin/env python3
"""Verify the connected Brand Direction Decision Spine and sabotage controls."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
RESULTS: list[tuple[str, bool, str]] = []


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8", errors="ignore")


def check(name: str, condition: bool, detail: str = "") -> None:
    RESULTS.append((name, bool(condition), detail))


def evaluate_fixture(text: str) -> list[str]:
    """Return missing behavior markers for a direction-decision artifact."""
    required = {
        "design challenge": "design challenge",
        "reference role": "reference role",
        "borrowed quality": "borrowed quality",
        "attraction-only rejection": "attraction-only",
        "proving surface": "proving surface",
        "application revision": "mobile hero failure",
        "source boundary": "commercial impact remain untested",
    }
    lowered = text.lower()
    return [label for label, marker in required.items() if marker not in lowered]


source_packages = ("xJEYViuQifg", "ZvxpaklnMXI")
required_source_files = (
    "metadata.json",
    "transcript.txt",
    "transcript_segments.json",
    "video-context-ledger.md",
    "uncertainty-report.md",
    "frame-notes.md",
    "analysis.md",
)
missing_sources: list[str] = []
for video_id in source_packages:
    for filename in required_source_files:
        relative = f"extractions/video-context/{video_id}/{filename}"
        if not (ROOT / relative).is_file():
            missing_sources.append(relative)
check("both source packages are decision-complete", not missing_sources, ", ".join(missing_sources))

reference_path = "skills/andrew-lane-design-systems/references/brand-direction-decision-spine.md"
andrew_workflow_path = "skills/andrew-lane-design-systems/workflows/01-build-vibe-foundation.md"
bos_discover_path = "skills/brand-operating-system/workflows/01-discover.md"
bos_visual_path = "skills/brand-operating-system/workflows/03-visual.md"
contract_path = "extractions/brand-direction-decision-spine/skill-system-contract.md"
proof_path = "extractions/brand-direction-decision-spine/behavior-proof.md"
mastery_path = "extractions/brand-direction-decision-spine/mastery-extraction.md"
reconciliation_path = "extractions/brand-direction-decision-spine/reconciliation.md"

required_files = (
    reference_path,
    andrew_workflow_path,
    bos_discover_path,
    bos_visual_path,
    contract_path,
    proof_path,
    mastery_path,
    reconciliation_path,
)
missing_build = [relative for relative in required_files if not (ROOT / relative).is_file()]
check("connected build files exist", not missing_build, ", ".join(missing_build))

reference = read(reference_path)
reference_terms = (
    "internal exploration board",
    "Client direction board / stylescape",
    "Reference Role Card",
    "Borrowed quality",
    "Cost / rights",
    "Proving surface",
    "Direction Decision Ledger",
    "Taste-owned",
    "UNTESTED",
)
reference_lower = reference.lower()
check(
    "cold reference preserves the source mechanics",
    all(term.lower() in reference_lower for term in reference_terms),
)

andrew = read(andrew_workflow_path)
check(
    "Andrew Lane remains the direction function owner",
    all(term in andrew for term in ("internal exploration board", "client direction boards / stylescapes", "first proving surface")),
)

discover = read(bos_discover_path)
visual = read(bos_visual_path)
check(
    "Brand OS discovery produces evidence-backed design challenges",
    all(term in discover for term in ("A4 — Design challenge ledger", "proof surface", "falsify")),
)
check(
    "Brand OS visual phase consumes and carries the decision spine",
    all(term in visual for term in ("C0 — Direction decision spine", "A4-design-challenge-ledger", "direction-decision-ledger", "proving-surface")),
)

contract = read(contract_path)
contract_fields = (
    "| Source evidence |",
    "| Objective |",
    "| Components |",
    "| Step order |",
    "| Inputs |",
    "| Outputs |",
    "| Handoff summary |",
    "| Composition rule |",
    "| Human checkpoint |",
    "| Validation |",
    "| Behavior-changing proof |",
    "| Result surface |",
    "| Context policy |",
    "| Reuse hook |",
)
check("skill-system contract is complete", all(field in contract for field in contract_fields))
check(
    "duplicate-system rejection is explicit",
    all(term in read(reconciliation_path) for term in ("No new skill or command", "New mega-skill", "Skipped")),
)

mastery = read(mastery_path)
check(
    "mastery extraction includes method, hidden knowledge, and implementation",
    all(term in mastery for term in ("## Hidden knowledge revealed", "## Full methodology", "## Implementation pathway", "## Transcendence opportunities")),
)

proof = read(proof_path)
positive_failures = evaluate_fixture(proof)
check("positive fixture changes real decision behavior", not positive_failures, ", ".join(positive_failures))

negative_fixture = """
Three attractive boards were created. The client chose Quiet Assembly.
The palette and typography were converted into guidelines.
"""
negative_failures = evaluate_fixture(negative_fixture)
check(
    "negative control rejects plausible but untraceable moodboards",
    len(negative_failures) == 7,
    f"missing={len(negative_failures)}/7",
)

failed = [row for row in RESULTS if not row[1]]
for name, ok, detail in RESULTS:
    suffix = f"  [{detail}]" if detail else ""
    print(f"{'PASS' if ok else 'FAIL'}  {name}{suffix}")
print(f"\n{len(RESULTS) - len(failed)}/{len(RESULTS)} completion checks passed")
raise SystemExit(1 if failed else 0)
