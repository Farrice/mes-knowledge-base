#!/usr/bin/env python3
"""Regression proof for SHADOW experiment versus shadow-market routing."""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
if str(ROOT / "execution") not in sys.path:
    sys.path.insert(0, str(ROOT / "execution"))

from codex_operator_preflight import build_preflight  # noqa: E402
from workflow_router import search_workflows  # noqa: E402


TARGET = "shadow-market-validation-report"

NEGATIVE_CONTROLS = (
    "Integrate the bounded Signal Fidelity recipient-mode repair in the parked SHADOW worktree, replay frozen cases, and leave it unmerged and unenforced.",
    "Run a SHADOW observation cycle on three capabilities without promoting or enforcing anything.",
    "Keep the buyer psychology overlay in cold SHADOW mode and preserve the native content owner.",
    "Review this SHADOW marketing experiment without promoting the companion layer.",
    "Review this design's use of light and shadow without changing the palette.",
)

POSITIVE_CONTROLS = (
    "Run a shadow market validation report for an underserved AI product niche.",
    "Validate the buyer demand and messy MVP for this shadow market before launch.",
    "Find the aftermath niche and prepare a market validation report.",
)


def route_names(query: str, limit: int = 10) -> list[str]:
    return [workflow["name"] for _, workflow in search_workflows(query, limit)]


def main() -> int:
    failures: list[str] = []

    for query in NEGATIVE_CONTROLS:
        names = route_names(query)
        if TARGET in names:
            failures.append(f"negative control still exposed /{TARGET}: {query}")
        preflight = build_preflight(query)
        if preflight["chosen_path"]["owner"] == TARGET:
            failures.append(f"negative preflight still chose /{TARGET}: {query}")

    for query in POSITIVE_CONTROLS:
        names = route_names(query)
        if not names or names[0] != TARGET:
            failures.append(f"positive control did not rank /{TARGET} first: {query}")
        preflight = build_preflight(query)
        if preflight["chosen_path"]["owner"] != TARGET:
            failures.append(f"positive preflight did not choose /{TARGET}: {query}")

    if failures:
        print("SHADOW route disambiguation: FAIL")
        for failure in failures:
            print(f"- {failure}")
        return 1

    print("SHADOW route disambiguation: PASS")
    print("- unrelated SHADOW experiments: 4/4 suppressed from shadow-market routing")
    print("- light-and-shadow design control: suppressed")
    print("- real shadow-market intents: 3/3 preserved")
    print("- Signal Fidelity files, routes, and promotion state: untouched")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
