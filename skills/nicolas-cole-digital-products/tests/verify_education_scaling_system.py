#!/usr/bin/env python3
"""Verify the Nicolas Cole education-business scaling extension."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
SKILL = ROOT / "skills" / "nicolas-cole-digital-products"
SOURCE = ROOT / "extractions" / "video-context" / "sIZnPcCt7BM"


def require(path: Path, needles: tuple[str, ...]) -> None:
    if not path.is_file():
        raise AssertionError(f"missing file: {path.relative_to(ROOT)}")
    text = path.read_text(encoding="utf-8")
    missing = [needle for needle in needles if needle not in text]
    if missing:
        raise AssertionError(
            f"{path.relative_to(ROOT)} missing required markers: {missing}"
        )


def main() -> None:
    verdicts = (
        "STAY SMALL",
        "STABILIZE",
        "SCALE VERTICALLY",
        "SCALE HORIZONTALLY",
        "SCALE CAPACITY FIRST",
    )
    require(
        SKILL / "workflows" / "education-business-scaling-decision.md",
        verdicts
        + (
            "Remove Subjectivity Before Multiplying It",
            "Match Expansion to Traffic Topology",
            "More → Better → New",
            "trailing-12-month",
            "accepted atrophy",
            "UNVERIFIED / NO EVENT",
        ),
    )
    require(
        SKILL
        / "references"
        / "prompts-v2"
        / "education-business-scaling-decision.md",
        (
            "## Role & Activation",
            "## Input Required",
            "## Execution Protocol",
            "## Output Contract",
            "## Output Skeleton",
            "## Quality Gate",
            "## Creative Latitude",
            "## Deploy When",
        ),
    )
    require(
        SKILL / "references" / "source-ledger.md",
        (
            "20 Lessons Selling",
            "speaker-reported",
            "sIZnPcCt7BM",
        ),
    )
    require(
        SOURCE / "behavior-proof.md",
        (
            "STABILIZE, THEN SCALE VERTICALLY",
            "Concentrated traffic",
            "subjective delivery prevents automation and hiring",
            "NO EVENT",
            "peak month cannot support fixed commitments",
        ),
    )
    require(
        SOURCE / "skill-system-contract.md",
        (
            "nicolas-cole-digital-products",
            "education-business-scaling-decision",
            "no duplicate skill or command",
            "No contributor may expand the skill surface",
            "No external export requested",
        ),
    )
    print("PASS: education-business scaling extension and negative controls are wired")


if __name__ == "__main__":
    main()
