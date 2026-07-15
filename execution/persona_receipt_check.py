#!/usr/bin/env python3
"""
Persona Receipt Check — the deterministic half of the Mastery Floor.

A GROUNDED bespoke persona must ship with a research receipt sidecar proving it
was distilled from live practitioner research, not latent knowledge alone
(Farrice 2026-07-15: "grounded in truth and grounded in real mastery... there
has to be some type of standard so I can move with confidence").

Checks the receipt STRUCTURE deterministically (the adversarial mastery-verify
agent judges currency separately — this script is the part that cannot drift):

  1. Receipt file exists next to the persona: <persona>.receipt.md
  2. >= 3 sources with real URLs
  3. A recency line: `As-of:` or `Current practice (as of ...)` marker
  4. The persona's named methodology traces to the receipt (any receipt line
     mentions it, so the framework isn't invented after the research)
  5. Verdict from the mastery-verify agent recorded: `Mastery-Verify: CURRENT`
     (STALE/UNSUPPORTED = FLAG — seat only with a visible flag)

Usage:
    python3 execution/persona_receipt_check.py <persona.md> [<persona.md> ...]
Exit 0 = all PASS, 1 = any FLAG. Prints per-file verdicts + reasons.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Dict, List

_URL_RE = re.compile(r"https?://[^\s\)\"'>\]]+")
_RECENCY_RE = re.compile(r"(?:as-of|as of|current practice|last (?:12|18|24) months|202[5-9])", re.I)
_VERIFY_RE = re.compile(r"mastery-verify:\s*(CURRENT|STALE|UNSUPPORTED)", re.I)
_METHOD_RE = re.compile(r'"signature_methodology"\s*:\s*"([^"\\]{4,80})', re.I)
MIN_SOURCES = 3


def check_persona(persona_path: Path) -> Dict:
    reasons: List[str] = []
    receipt_path = persona_path.with_suffix(".receipt.md")

    if not receipt_path.exists():
        return {"verdict": "FLAG", "reasons": [f"missing receipt sidecar: {receipt_path.name}"],
                "receipt": str(receipt_path)}

    receipt = receipt_path.read_text(encoding="utf-8", errors="ignore")
    persona = persona_path.read_text(encoding="utf-8", errors="ignore")

    urls = set(_URL_RE.findall(receipt))
    if len(urls) < MIN_SOURCES:
        reasons.append(f"only {len(urls)} source URL(s) in receipt — floor is {MIN_SOURCES}")

    if not _RECENCY_RE.search(receipt):
        reasons.append("no recency marker (As-of / current practice / recent-window line)")

    m = _METHOD_RE.search(persona)
    if m:
        # First distinctive word of the named methodology must appear in the receipt.
        words = [w for w in re.findall(r"[A-Za-z][A-Za-z\-]{3,}", m.group(1))
                 if w.lower() not in {"the", "method", "framework", "protocol", "system", "approach"}]
        if words and not any(w.lower() in receipt.lower() for w in words[:3]):
            reasons.append(f"named methodology '{m.group(1)}' not traceable to any receipt line")

    v = _VERIFY_RE.search(receipt)
    if not v:
        reasons.append("no Mastery-Verify verdict recorded in receipt")
    elif v.group(1).upper() != "CURRENT":
        reasons.append(f"Mastery-Verify verdict is {v.group(1).upper()} — seat only with visible flag")

    return {"verdict": "FLAG" if reasons else "PASS", "reasons": reasons,
            "receipt": str(receipt_path), "sources": len(urls)}


def main(paths: List[str]) -> int:
    rc = 0
    for p in paths:
        f = Path(p)
        if not f.exists():
            print(f"{p}: MISSING PERSONA FILE")
            rc = 1
            continue
        r = check_persona(f)
        print(f"{p}: {r['verdict']}" + (f" ({r.get('sources', 0)} sources)" if r["verdict"] == "PASS" else ""))
        for reason in r["reasons"]:
            print(f"  • {reason}")
        if r["verdict"] == "FLAG":
            rc = 1
    return rc


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(2)
    sys.exit(main(sys.argv[1:]))
