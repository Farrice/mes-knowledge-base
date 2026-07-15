#!/usr/bin/env python3
"""
Persona Stat Lint — gate for synthetic personas to prevent fabricated credentials.

Scans a composite persona document for:
  1. Fabricated statistics (% claims, $-dollar figures, "billion/million" markets, growth rates)
  2. False attributions (cites to real orgs without grounding)
  3. Real company names in credentials (only composites allowed)
  4. Missing composite label (must be clearly marked as synthesized)

Returns: PASS (safe to use) | FLAG (rewrite required; specific lines listed)

CLI: python3 execution/persona_stat_lint.py <persona_file> [--verbose]
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List

# Patterns stolen from grounding_guard.py — same definitions so we use the same lens.
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
]

# Real company names that must NOT appear in credentials
_FORBIDDEN_COMPANIES = {
    "apple", "google", "microsoft", "amazon", "meta", "tesla",
    "netflix", "uber", "airbnb", "spotify", "slack", "github",
    "stripe", "figma", "notion", "notion labs",
    "mckenzie", "bcg", "bain", "deloitte", "kpmg",
    "goldman sachs", "jpmorgan", "morgan stanley", "goldman",
    "salesforce", "adobe", "oracle", "ibm", "cisco"
}

_URL_RE = r"https?://[^\s\)\"'>\]]+"
_COMPOSITE_LABEL_RE = r"(?:composite|synthesized|bespoke|generated|assembled)"


def lint(text: str, verbose: bool = False) -> Dict:
    """
    Scan persona text for fabricated credentials.
    Returns {verdict: 'PASS'|'FLAG', issues: [...], lines_flagged: [line_nums]}
    """
    if not text:
        return {"verdict": "PASS", "issues": [], "lines_flagged": []}

    lines = text.split("\n")
    issues: List[str] = []
    lines_flagged: List[int] = []
    urls = set(re.findall(_URL_RE, text))

    # 1. Check for composite label (required).
    composite_label_found = False
    for i, line in enumerate(lines, 1):
        if re.search(_COMPOSITE_LABEL_RE, line, re.I):
            composite_label_found = True
            break

    if not composite_label_found:
        issues.append("No composite/synthesized/bespoke label found in persona. Must declare synthetic origin.")

    # 2. Scan each line for stat + attribution patterns without grounding.
    for i, line in enumerate(lines, 1):
        if not line.strip():
            continue

        # Skip fenced code blocks or explicit caveats.
        if "note:" in line.lower() or "caveat:" in line.lower() or "[modeled]" in line.lower():
            continue

        stat_matches = sum(len(re.findall(p, line, re.I)) for p in _STAT_PATTERNS)
        attr_matches = sum(len(re.findall(p, line, re.I)) for p in _ATTRIBUTION_PATTERNS)
        has_url = bool(re.search(_URL_RE, line))

        # Any stat without a URL or qualifier = FLAG.
        if stat_matches > 0 and not has_url:
            # Check if line has a disclaimer (e.g., "approximately", "roughly", "estimated").
            disclaimer_words = ["approximately", "roughly", "estimated", "assumed", "hypothetically", "notional"]
            has_disclaimer = any(w in line.lower() for w in disclaimer_words)
            if not has_disclaimer:
                issues.append(f"Line {i}: stats without source URL: {line.strip()[:80]}")
                lines_flagged.append(i)

        # Attribution without URL = FLAG.
        if attr_matches > 0 and not has_url:
            issues.append(f"Line {i}: attribution without source URL: {line.strip()[:80]}")
            lines_flagged.append(i)

    # 3. Check for real company names (credential fraud).
    full_lower = text.lower()
    for company in _FORBIDDEN_COMPANIES:
        if company in full_lower:
            # Only flag if it looks like a credential (near "worked at", "led", "founded", etc.).
            context_patterns = [
                rf"worked at.*{re.escape(company)}",
                rf"led.*{re.escape(company)}",
                rf"founded.*{re.escape(company)}",
                rf"cto at.*{re.escape(company)}",
                rf"ceo at.*{re.escape(company)}",
                rf"partner at.*{re.escape(company)}",
                rf"\b{re.escape(company)}\b.*(?:executive|leadership|team|director|manager)",
            ]
            for pattern in context_patterns:
                matches = re.finditer(pattern, full_lower)
                for match in matches:
                    # Find line number.
                    match_pos = match.start()
                    line_num = text[:match_pos].count("\n") + 1
                    issues.append(f"Line {line_num}: real company name detected in credential: {company}")
                    if line_num not in lines_flagged:
                        lines_flagged.append(line_num)

    verdict = "FLAG" if issues else "PASS"
    return {
        "verdict": verdict,
        "issues": issues,
        "lines_flagged": sorted(set(lines_flagged)),
        "composite_label_found": composite_label_found,
        "urls_detected": len(urls),
    }


def _cli() -> int:
    import argparse

    p = argparse.ArgumentParser(prog="persona_stat_lint.py")
    p.add_argument("persona_file", help="Path to persona .md file")
    p.add_argument("--verbose", action="store_true", help="Verbose output")
    a = p.parse_args()

    path = Path(a.persona_file)
    if not path.exists():
        print(f"ERROR: File not found: {a.persona_file}", file=sys.stderr)
        return 1

    text = path.read_text(encoding="utf-8")
    result = lint(text, verbose=a.verbose)

    print(f"Verdict: {result['verdict']}")
    if result["verdict"] == "FLAG":
        print(f"\nIssues ({len(result['issues'])}):")
        for issue in result["issues"]:
            print(f"  • {issue}")
        if result["lines_flagged"]:
            print(f"\nLines flagged: {', '.join(map(str, result['lines_flagged']))}")
    else:
        print(f"✓ Persona is clean. Composite label present: {result['composite_label_found']}")
        if a.verbose:
            print(f"  URLs detected: {result['urls_detected']}")

    return 0 if result["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(_cli())
