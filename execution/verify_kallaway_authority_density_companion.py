#!/usr/bin/env python3
"""Verify the Kallaway Micro-Fame Authority Density companion and its negative controls."""

from __future__ import annotations

import copy
import json
from pathlib import Path

from verify_video_context_source_package import verify_package


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "kallaway-content-operating-system"
SOURCE = ROOT / "extractions" / "video-context" / "1ilMGCxJBQY"
WORKFLOW = SKILL / "workflows" / "micro-fame-authority-density.md"
PROOF = SKILL / "references" / "authority-density-behavior-proof.md"
FIXTURE = SKILL / "references" / "fixtures" / "authority-density-health-performance.json"

PROMPTS = (
    "authority-density-diagnostic.md",
    "positioning-contrast-brief.md",
    "authority-321-batch-plan.md",
    "four-rep-authority-review.md",
)

PROMPT_SECTIONS = (
    "## Role & Activation",
    "## Input Required",
    "## Execution Protocol",
    "## Output Contract",
    "## Output Skeleton",
    "## Quality Gate",
    "## Deploy When",
)


def require_text(path: Path, phrases: tuple[str, ...], failures: list[str]) -> None:
    if not path.exists():
        failures.append(f"missing file: {path.relative_to(ROOT)}")
        return
    text = path.read_text(encoding="utf-8", errors="ignore")
    for phrase in phrases:
        if phrase not in text:
            failures.append(f"{path.relative_to(ROOT)} missing phrase: {phrase}")


def validate_fixture(data: dict) -> list[str]:
    failures: list[str] = []
    posts = data.get("posts")
    if not isinstance(posts, list):
        return ["fixture posts must be a list"]

    groups: dict[str, list[dict]] = {}
    for post in posts:
        groups.setdefault(str(post.get("bucket")), []).append(post)

    required_counts = {
        "broad": 4,
        "narrow_proof_to_promise": 4,
        "narrow_decision_room": 4,
        "chaos_claim_memo": 2,
    }
    for bucket, count in required_counts.items():
        if len(groups.get(bucket, [])) != count:
            failures.append(f"{bucket} expected {count} reps")

    expected = data.get("expected_decisions", {})
    required_decisions = {
        "broad": "MODIFY",
        "narrow_proof_to_promise": "KEEP",
        "narrow_decision_room": "KEEP",
        "chaos_claim_memo": "INCONCLUSIVE_CONTINUE_TO_FOUR_REPS",
    }
    if expected != required_decisions:
        failures.append("expected decisions do not preserve the four negative controls")

    broad = groups.get("broad", [])
    narrow = groups.get("narrow_proof_to_promise", []) + groups.get("narrow_decision_room", [])
    if broad and narrow:
        broad_avg = sum(int(row["views"]) for row in broad) / len(broad)
        narrow_avg = sum(int(row["views"]) for row in narrow) / len(narrow)
        if broad_avg <= narrow_avg * 8:
            failures.append("fixture no longer creates a strong vanity-reach false winner")
        if sum(int(row["qualified_replies"]) for row in broad) != 0:
            failures.append("broad negative control must have zero qualified replies")
        if sum(int(row["qualified_replies"]) for row in narrow) <= 0:
            failures.append("narrow positive controls need qualified replies")
        if sum(int(row["deposits"]) for row in narrow) != 1:
            failures.append("narrow commercial control must contain one synthetic deposit")

    if data.get("synthetic") is not True:
        failures.append("fixture must remain explicitly synthetic")
    return failures


def main() -> int:
    failures: list[str] = []

    package_ok, package_failures, _ = verify_package(SOURCE)
    if not package_ok:
        failures.extend(f"source package: {failure}" for failure in package_failures)

    require_text(
        WORKFLOW,
        (
            "search lenses",
            "not fields to complete or score",
            "minimum evidence floor",
            "KEEP",
            "MODIFY",
            "KILL",
            "INCONCLUSIVE",
            "Do not collapse these into one authority-density number",
        ),
        failures,
    )
    require_text(
        PROOF,
        (
            "The claim boundary is the creative brief",
            "Broad: modify",
            "Proof to Promise: keep",
            "Campaign Decision Room: keep",
            "inconclusive; continue to four reps",
            "synthetic",
        ),
        failures,
    )

    require_text(
        SKILL / "references" / "source-evidence-map.md",
        ("1ilMGCxJBQY", "Authority density", "four-rep evidence floor"),
        failures,
    )
    require_text(
        SKILL / "references" / "skill-system-contract.md",
        ("Behavior-changing proof", "authority-density-behavior-proof.md"),
        failures,
    )
    require_text(
        SKILL / "SKILL.md",
        ("Micro-Fame Authority Density Companion", "smallest decisive contrast"),
        failures,
    )

    for filename in PROMPTS:
        path = SKILL / "references" / "prompts-v2" / filename
        require_text(
            path,
            (
                "source_prompt: born-v2",
                "skill: kallaway-content-operating-system",
                "standard: structure-pure-v2",
                "forged: born-v2",
                *PROMPT_SECTIONS,
            ),
            failures,
        )

    if not FIXTURE.exists():
        failures.append(f"missing file: {FIXTURE.relative_to(ROOT)}")
    else:
        try:
            fixture = json.loads(FIXTURE.read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            failures.append(f"fixture JSON invalid: {exc}")
        else:
            failures.extend(validate_fixture(fixture))

            broken = copy.deepcopy(fixture)
            broken["expected_decisions"]["broad"] = "KEEP"
            if not validate_fixture(broken):
                failures.append("false-green control failed: a vanity-reach KEEP was not rejected")

            broken = copy.deepcopy(fixture)
            broken["posts"] = [row for row in broken["posts"] if row["id"] != "N1-4"]
            if not validate_fixture(broken):
                failures.append("false-green control failed: a missing fourth rep was not rejected")

    if failures:
        print("Kallaway Authority Density companion: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("Kallaway Authority Density companion: PASS")
    print("- source package complete")
    print("- contrast diagnosis rejects checkbox positioning")
    print("- four prompts satisfy born-v2 structure")
    print("- vanity-reach, narrow-value, four-rep, and synthetic-proof controls pass")
    print("- corrupted decision and missing-rep controls fail as expected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
