#!/usr/bin/env python3
"""Verify Farrice's first real Content Signal Loop deployment."""

from __future__ import annotations

import json
import re
import sys
from datetime import date
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "_active/farrice-brand/content/signal-loop"
FILES = {
    "readme": STATE / "README.md",
    "audience": STATE / "audience-profile.md",
    "sources": STATE / "evidence/source-inventory.md",
    "profile": STATE / "profiles/winning-content-linkedin.md",
    "ideas": STATE / "runs/ideas-2026-07-30-linkedin.md",
    "queue": STATE / "queues/content-queue.md",
}
METADATA = (
    STATE / "audience-profile.md.metadata.json",
    STATE / "profiles/winning-content-linkedin.md.metadata.json",
    STATE / "runs/ideas-2026-07-30-linkedin.md.metadata.json",
    STATE / "queues/content-queue.md.metadata.json",
)


def contains_all(text: str, fragments: list[str]) -> bool:
    folded = text.casefold()
    return all(fragment.casefold() in folded for fragment in fragments)


def idea_sections(text: str) -> dict[str, str]:
    matches = list(re.finditer(r"^### `(IDEA-[A-Z]\d{2})`", text, re.MULTILINE))
    sections: dict[str, str] = {}
    for index, match in enumerate(matches):
        next_idea = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        next_major = text.find("\n## ", match.end())
        end = min(next_idea, next_major) if next_major != -1 else next_idea
        sections[match.group(1)] = text[match.start():end]
    return sections


def record(name: str, passed: bool, failures: list[str]) -> None:
    print(f"[{'PASS' if passed else 'FAIL'}] {name}")
    if not passed:
        failures.append(name)


def main() -> int:
    failures: list[str] = []
    missing = [path.relative_to(ROOT) for path in FILES.values() if not path.exists()]
    record("deployment_files_exist", not missing, failures)
    if missing:
        for path in missing:
            print(f"  missing: {path}")
        return 1

    content = {name: path.read_text(encoding="utf-8") for name, path in FILES.items()}
    ideas = idea_sections(content["ideas"])

    record(
        "audience_profile_grounded",
        contains_all(
            content["audience"],
            [
                "founders and authorized marketing leads",
                "one belief shift",
                "reactive triggers",
                "evidence boundary",
            ],
        ),
        failures,
    )
    record(
        "profile_is_provisional",
        contains_all(
            content["profile"],
            [
                "status | **provisional**",
                "available metrics | none",
                "does not call any formula a performance winner",
                "coverage gaps",
            ],
        ),
        failures,
    )
    formula_sections = re.findall(r"^### `WCF-LI-\d+`", content["profile"], re.MULTILINE)
    record("five_transferable_formulas", len(formula_sections) == 5, failures)
    record(
        "negative_taste_evidence_preserved",
        contains_all(content["profile"], ["WCF-LI-X1", "2/10", "detached craft lecture"]),
        failures,
    )

    record("eight_idea_cards", len(ideas) == 8, failures)
    card_contract = all(
        contains_all(
            section,
            [
                "recommended platform:",
                "linkedin",
                "audience reason:",
                "creator bridge:",
                "confidence:",
                "risks or unknowns:",
                "recommended queue action:",
                "selection marker:",
            ],
        )
        for section in ideas.values()
    )
    record("idea_card_contract", card_contract, failures)

    selected = {
        idea_id
        for idea_id, section in ideas.items()
        if "`SELECTED_BY_DIRECTIVE`" in section
    }
    expected_selected = {"IDEA-P01", "IDEA-P02", "IDEA-T01", "IDEA-T02", "IDEA-C01"}
    record("five_directive_selected_ideas", selected == expected_selected, failures)

    queue_idea_ids = set(
        re.findall(r"^- \*\*Idea ID:\*\* `(IDEA-[A-Z]\d{2})`", content["queue"], re.MULTILINE)
    )
    record("queue_matches_selection", queue_idea_ids == selected, failures)
    queue_items = re.findall(r"^### `Q-\d{3}`", content["queue"], re.MULTILINE)
    record("five_active_queue_items", len(queue_items) == 5, failures)
    record(
        "queue_selection_boundary",
        contains_all(
            content["queue"],
            [
                "selection authority",
                "direct instruction",
                "item-level felt verdicts remain pending",
                "only one operation was performed",
            ],
        ),
        failures,
    )
    queue_sections = re.split(r"^### `Q-\d{3}`", content["queue"], flags=re.MULTILINE)[1:]
    record(
        "queue_state_contract",
        len(queue_sections) == 5
        and all(
            contains_all(
                section,
                [
                    "**Platform:** LinkedIn",
                    "**Creator bridge:**",
                    "**Next action:**",
                    "**Stale after:**",
                ],
            )
            for section in queue_sections
        ),
        failures,
    )

    source_dates = {
        match.group(1): date.fromisoformat(match.group(2))
        for match in re.finditer(
            r"\| `(EXT-\d{2})` \| (\d{4}-\d{2}-\d{2}) \|",
            content["sources"],
        )
    }
    window_start = date(2026, 7, 1)
    window_end = date(2026, 7, 30)
    record(
        "fresh_sources_in_window",
        len(source_dates) == 4
        and all(window_start <= source_date <= window_end for source_date in source_dates.values()),
        failures,
    )
    record(
        "source_provenance_retained",
        content["sources"].count("https://") == 4
        and all(source_id in content["ideas"] for source_id in source_dates),
        failures,
    )
    record(
        "finished_content_veto",
        not re.search(
            r"^## (Finished Post|Draft Post|Carousel Copy|Publishable Copy)\b",
            content["ideas"] + content["queue"],
            re.MULTILINE | re.IGNORECASE,
        ),
        failures,
    )

    metadata_valid = True
    for path in METADATA:
        try:
            payload = json.loads(path.read_text(encoding="utf-8"))
            metadata_valid = metadata_valid and bool(payload.get("artifact_type"))
        except (OSError, json.JSONDecodeError):
            metadata_valid = False
    record("artifact_metadata_valid", metadata_valid, failures)

    if failures:
        print(f"\nFarrice deployment verification: FAIL ({len(failures)} failure(s))")
        return 1

    print(
        "\nFarrice deployment verification: PASS "
        "(provisional profile + 8 ideas + 5-item queue + 4 fresh sources)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
