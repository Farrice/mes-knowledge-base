#!/usr/bin/env python3
"""
Grounding Guard — the systemic, deterministic backstop for the research-integrity
bug class. Catches ungrounded factual output at finalize REGARDLESS of which
workflow produced it, so the false-PASS era cannot recur even from a workflow
that bypasses the unified research engine.

It detects the exact signature the 2026 audit surfaced:
  - factual claims (stats: $, %, CAGR, "billion"; named-source attributions) with
    ZERO source URLs — the "confident but unverifiable" dossier,
  - [MODELED] placeholder data presented as fact (outside a fenced modeled section),
  - hardcoded "GROUNDED" labels asserted with no URLs to back them.

Returns PASS | WARN | FLAG + the signals. Wired into chain_runner.finalize
(Cap 4) and runnable standalone:
    python3 execution/grounding_guard.py <file> [--task-type Research] [--strict]
"""

from __future__ import annotations

import re
import sys
from typing import Dict, List

# Factual-claim signals — the presence of hard numbers / sized markets / named
# authorities is what *demands* sourcing.
_STAT_PATTERNS = [
    r"\$\s?\d",
    r"\d+(?:\.\d+)?\s?%",
    r"\b\d+(?:\.\d+)?\s?(?:billion|million|thousand|bn|mn|k)\b",
    r"\bCAGR\b",
    r"\bmarket size\b",
    r"\b(?:valued at|projected to|grew by|growth rate|revenue of)\b",
]
_ATTRIBUTION_PATTERNS = [
    r"\baccording to\b",
    r"\b(?:Forbes|McKinsey|Gartner|Statista|Nielsen|Pew|Reddit|NSCA|NYT|Bloomberg)\b",
    r"\(20\d\d\)",
    r"\bsources?:\s",
    r"\bstudy (?:found|shows|reports)\b",
    r"\b\d+\s+(?:quotes|sources|searches|extractions)\b",  # "47 quotes", "9 searches" provenance claims
]
_URL_RE = r"https?://[^\s\)\"'>\]]+"

# Task types where factual grounding matters. Pure Creative/System excluded.
GROUNDING_TASK_TYPES = {"Research", "Strategy", "Analysis", "Content", "Client Work"}


def scan(text: str, task_type: str = "") -> Dict:
    """Scan output for the ungrounded-factual signature. Returns a verdict dict."""
    if not text:
        return {"verdict": "PASS", "risk": "none", "signals": [],
                "stat_hits": 0, "attr_hits": 0, "url_count": 0, "modeled": 0}

    url_count = len(set(re.findall(_URL_RE, text)))
    stat_hits = sum(len(re.findall(p, text, re.I)) for p in _STAT_PATTERNS)
    attr_hits = sum(len(re.findall(p, text, re.I)) for p in _ATTRIBUTION_PATTERNS)
    factual_load = stat_hits + attr_hits
    modeled = len(re.findall(r"\[MODELED", text, re.I))
    # "GROUNDED" asserted as a status label (not the word "grounded" in prose).
    hardcoded_grounded = len(re.findall(r"(?:research|grounding|status)\s*[:=]\s*[`\"']?GROUNDED", text, re.I))

    signals: List[str] = []
    verdict = "PASS"

    def _raise(level):
        nonlocal verdict
        order = {"PASS": 0, "WARN": 1, "FLAG": 2}
        if order[level] > order[verdict]:
            verdict = level

    # [MODELED] presented as fact (not inside the explicit fenced modeled section).
    if modeled > 0 and "MODELED-SECTION" not in text:
        signals.append(f"{modeled} [MODELED] placeholder(s) presented outside a fenced modeled section")
        _raise("FLAG")

    # Heavy factual load with no sources at all — the core false-PASS signature.
    if factual_load >= 5 and url_count == 0:
        signals.append(f"{factual_load} factual claims (stats/attributions) with ZERO source URLs")
        _raise("FLAG")
    elif factual_load >= 3 and url_count == 0:
        signals.append(f"{factual_load} factual claims with no source URLs")
        _raise("WARN")
    elif factual_load >= 8 and url_count < factual_load * 0.3:
        signals.append(f"low provenance: {factual_load} factual claims, only {url_count} source URLs")
        _raise("WARN")

    # A "GROUNDED" status asserted with no URLs behind it.
    if hardcoded_grounded and url_count == 0 and factual_load >= 2:
        signals.append("'GROUNDED' status asserted with no source URLs to back it")
        _raise("FLAG")

    risk = {"PASS": "none", "WARN": "medium", "FLAG": "high"}[verdict]
    return {"verdict": verdict, "risk": risk, "signals": signals,
            "stat_hits": stat_hits, "attr_hits": attr_hits,
            "url_count": url_count, "modeled": modeled, "factual_load": factual_load}


def _cli() -> int:
    import argparse
    import json
    p = argparse.ArgumentParser(prog="grounding_guard.py")
    p.add_argument("file", nargs="?", help="file to scan (default: stdin)")
    p.add_argument("--task-type", default="")
    p.add_argument("--strict", action="store_true", help="exit 1 on FLAG")
    a = p.parse_args()
    text = open(a.file, encoding="utf-8", errors="ignore").read() if a.file else sys.stdin.read()
    r = scan(text, a.task_type)
    print(json.dumps(r, indent=2))
    return 1 if (a.strict and r["verdict"] == "FLAG") else 0


if __name__ == "__main__":
    raise SystemExit(_cli())
