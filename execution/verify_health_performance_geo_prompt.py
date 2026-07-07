#!/usr/bin/env python3
"""Verify the Health Performance GEO automation prompt keeps broad market focus.

This guard exists because the daily brief drifted into a narrow GLP-1 lane even
though the intended job is broad health-performance market-domain creative
strategy. It checks for the explicit anti-capture contract in the local
automation prompt.
"""

from __future__ import annotations

import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
PROMPT = ROOT / "_active" / "health-performance-ip-library" / "AUTOMATION_PROMPT.md"


REQUIRED_PHRASES = {
    "version": "Version: 3.4 Market-Domain Creative Intelligence",
    "market_domain_mandate": "### Market-Domain Mandate",
    "not_glp1_monitor": "The engine is not a GLP-1 monitor",
    "ten_candidate_signals": "at least ten candidate signals",
    "eight_non_glp1": "At least eight must be non-GLP-1-specific",
    "glp1_one_signal": "GLP-1 is one category signal",
    "repetition_penalty": "Apply a repetition penalty before picking",
    "market_intelligence_read": "Market Intelligence Read",
    "creative_depth_gate": "### Creative Strategist Depth Gate",
    "market_lane_first": "1. **Market Domain And Avatar Pressure Lane**",
    "source_truth_later": "5. **Source Truth Lane**",
    "non_glp1_acceptance": "at least eight angle candidates were non-GLP-1-specific",
}


def main() -> int:
    if not PROMPT.exists():
        print(f"FAIL: missing prompt: {PROMPT}")
        return 1

    text = PROMPT.read_text(encoding="utf-8")
    missing = [name for name, phrase in REQUIRED_PHRASES.items() if phrase not in text]

    glp1_count = text.lower().count("glp-1")
    market_count = text.lower().count("market")

    if missing:
        print("FAIL: Health Performance GEO prompt missing broad-market guard clauses:")
        for name in missing:
            print(f"- {name}: {REQUIRED_PHRASES[name]}")
        return 1

    if market_count <= glp1_count:
        print(
            "FAIL: prompt still appears GLP-1-heavy; "
            f"market_count={market_count}, glp1_count={glp1_count}"
        )
        return 1

    print("PASS: Health Performance GEO prompt has broad market-domain guardrails.")
    print(f"Prompt: {PROMPT}")
    print(f"market_count={market_count}; glp1_count={glp1_count}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
