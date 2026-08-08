#!/usr/bin/env python3
"""Verify the Elizabeth Stone systems-thinking overlay and its SHADOW wiring."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PRIMITIVE = ROOT / "semantic_libraries/antigravity/primitives/systems-thinking-expertise-intelligence-overlay.md"
SOURCE = ROOT / "extractions/video-context/t0GiTyz4syY"


REQUIRED_MARKERS = {
    PRIMITIVE: (
        "Status: `SHADOW`",
        "### Zoom",
        "### Craft",
        "### Pave",
        "### Own",
        "### Learn",
        "## SHADOW Rules",
        "behavior-proof.md",
    ),
    ROOT / "semantic_libraries/antigravity/primitives/operating-alignment-contract.md": (
        "## One-Click Systems Zoom (SHADOW)",
        "systems-thinking-expertise-intelligence-overlay.md",
    ),
    ROOT / "semantic_libraries/antigravity/primitives/expert-composition-contract.md": (
        "### 2.5 Craft Depth And Adjacent Fluency (SHADOW)",
        "systems-thinking-expertise-intelligence-overlay.md",
    ),
    ROOT / "semantic_libraries/antigravity/primitives/skill-system-contract.md": (
        "## Paved-Path Design (SHADOW)",
        "systems-thinking-expertise-intelligence-overlay.md",
    ),
    ROOT / "semantic_libraries/antigravity/primitives/agentic-engineering-loop-contract.md": (
        "## Outcome Ownership And Explain-Or-Recover (SHADOW)",
        "systems-thinking-expertise-intelligence-overlay.md",
    ),
    ROOT / "semantic_libraries/antigravity/primitives/goal-loop-maintenance-contract.md": (
        "## Retro Before Rule (SHADOW)",
        "systems-thinking-expertise-intelligence-overlay.md",
    ),
    ROOT / ".agent/workflows/operator-school.md": (
        "## The six operator deltas",
        "**One-click systems drill.**",
        "systems-thinking-expertise-intelligence-overlay.md",
    ),
    SOURCE / "behavior-proof.md": (
        "## Case 1: Source Extraction Becomes a Companion Layer",
        "## Case 2: Full-Arsenal Content Work Preserves One Craft Owner",
        "## Case 3: Repeated Engineering Failure Produces an Upstream Repair, Not Another Checklist",
        "Production promotion remains `UNTESTED`",
    ),
}

SOURCE_FILES = (
    "metadata.json",
    "transcript.txt",
    "transcript_segments.json",
    "video-context-ledger.json",
    "uncertainty-report.md",
    "analysis.md",
    "vision.md",
    "deep-extraction.md",
    "architecture.md",
    "behavior-proof.md",
)


def main() -> int:
    failures: list[str] = []

    for path, markers in REQUIRED_MARKERS.items():
        if not path.exists():
            failures.append(f"missing file: {path.relative_to(ROOT)}")
            continue
        text = path.read_text(encoding="utf-8")
        for marker in markers:
            if marker not in text:
                failures.append(f"missing marker in {path.relative_to(ROOT)}: {marker}")

    for filename in SOURCE_FILES:
        path = SOURCE / filename
        if not path.exists() or path.stat().st_size == 0:
            failures.append(f"missing or empty source artifact: {path.relative_to(ROOT)}")

    if PRIMITIVE.exists():
        primitive_text = PRIMITIVE.read_text(encoding="utf-8")
        banned_enforcement = ("Status: `ENFORCED`", "HARD BLOCK", "mandatory score")
        for marker in banned_enforcement:
            if marker in primitive_text:
                failures.append(f"SHADOW primitive contains enforcement marker: {marker}")

    if failures:
        print("Systems Thinking Expertise Overlay: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Systems Thinking Expertise Overlay: PASS")
    print(f"- integrations: {len(REQUIRED_MARKERS) - 2}")
    print("- cold-start behavior cases: 3")
    print("- mode: SHADOW, non-blocking")
    print("- source boundary: transcript-backed, visual/OCR unavailable")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
