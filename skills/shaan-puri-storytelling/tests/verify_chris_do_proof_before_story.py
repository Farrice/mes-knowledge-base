#!/usr/bin/env python3
"""Verify the bounded Chris Do proof-before-story integration."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[3]
REFERENCE = ROOT / "skills/shaan-puri-storytelling/references/chris-do-proof-before-story.md"
MAP = ROOT / "skills/shaan-puri-storytelling/references/story-deployment-map.md"
WORKFLOW = ROOT / "skills/shaan-puri-storytelling/workflows/shaan-story-deploy.md"
PROMPT = ROOT / "skills/shaan-puri-storytelling/references/prompts-v2/shaan-story-deploy.md"
CONTRACT = ROOT / "extractions/video-context/FFPaVFBEIhI/skill-system-contract.md"
PROOF = ROOT / "extractions/video-context/FFPaVFBEIhI/behavior-proof.md"


def require(path: Path, needles: tuple[str, ...], failures: list[str]) -> None:
    if not path.is_file():
        failures.append(f"missing file: {path.relative_to(ROOT)}")
        return
    text = " ".join(path.read_text(encoding="utf-8").split())
    for needle in needles:
        normalized_needle = " ".join(needle.split())
        if normalized_needle not in text:
            failures.append(f"{path.relative_to(ROOT)} missing: {needle}")


def main() -> int:
    failures: list[str] = []
    require(
        REFERENCE,
        (
            "current publishable asset is `NO STORY`",
            "`/proof-portfolio-builder`",
            "Return to `/shaan-story-deploy` only when",
            "## Negative Controls",
            "status, incident, procedure, specification, calculation",
        ),
        failures,
    )
    require(
        MAP,
        (
            "CHRIS-DO-DERIVED",
            "claims but no seeable proof",
            "`/proof-portfolio-builder`",
            "Missing proof is different from missing presentation context.",
        ),
        failures,
    )
    require(
        WORKFLOW,
        (
            "separate a claim from seeable proof",
            "The current publishable asset remains `NO STORY`",
            "Do not use this recovery route for incidents",
            "irrelevant proof-capture ritual",
        ),
        failures,
    )
    require(
        PROMPT,
        (
            "distinguish the transformation claim from a seeable proof object",
            "keep the current asset at `NO STORY`",
            "do not send direct, technical, incident, status, or evidence-sensitive",
            "negative-control `NO STORY` cases avoid proof capture",
        ),
        failures,
    )
    require(
        CONTRACT,
        (
            "Shaan owns dosage. Luke owns proof acquisition.",
            "Do not add a new command or expert.",
            "Skill System Handoff: Shaan Diagnosis -> Luke Proof Capture",
        ),
        failures,
    )
    require(
        PROOF,
        (
            "Narrative decision: NO STORY",
            "Technical incident",
            "Health research explainer",
            "Verified customer case",
            "DOCUMENTED CONTRAST",
            "Live usefulness remains `UNTESTED`",
        ),
        failures,
    )

    if failures:
        print("CHRIS DO PROOF-BEFORE-STORY: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("CHRIS DO PROOF-BEFORE-STORY: PASS")
    print("- claim-only brand/sales case stays NO STORY and routes to proof acquisition")
    print("- direct and evidence-sensitive negative controls stay out of proof capture")
    print("- existing Shaan/Luke ownership preserved; no new command or expert")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
