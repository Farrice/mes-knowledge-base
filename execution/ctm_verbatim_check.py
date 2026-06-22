#!/usr/bin/env python3
"""
ctm_verbatim_check.py — the deterministic backstop for the Customer Truth Map
Verbatim-Integrity gate (Phase 2 / /ctm-clean).

The skill's #1 promise is "organize real customer language, never invent it." This
script makes that gate REAL instead of an LLM eyeballing it (which the project bans as
"AI-memory-dependent observability"). It checks that every extracted quote actually
appears, word-for-word, in the source text it was supposedly pulled from.

What counts as verbatim here:
  - Whitespace is normalized (newlines/tabs/multi-space collapse to one space).
  - Smart quotes/dashes are normalized to ASCII.
  - A leading markdown quote marker ("> ") and a trailing source tag
    (" — [source]" / " (source: ...)") are stripped before checking.
  - Bracketed insertions "[added for sense]" are ALLOWED: the gate removes them and
    requires every remaining contiguous segment to be a substring of the source.
  - Comparison is case-insensitive by default (people quote with varied capitalization);
    pass --case-sensitive to tighten.

Exit code 0 = all quotes verbatim. Exit code 1 = one or more offenders (the gate fails).

Usage:
  python3 execution/ctm_verbatim_check.py --source raw_chunk.txt --quotes extracted.txt
  python3 execution/ctm_verbatim_check.py --source raw_chunk.txt --quotes extracted.txt --json
  cat extracted.txt | python3 execution/ctm_verbatim_check.py --source raw_chunk.txt
"""
import argparse
import json
import re
import sys

_SMART = {
    "‘": "'", "’": "'", "“": '"', "”": '"',
    "–": "-", "—": "-", "…": "...", " ": " ",
}


def normalize(text: str, case_sensitive: bool) -> str:
    for a, b in _SMART.items():
        text = text.replace(a, b)
    text = re.sub(r"\s+", " ", text).strip()
    return text if case_sensitive else text.lower()


def clean_quote(line: str) -> str:
    """Strip markdown quote markers and a trailing source/permalink tag."""
    s = line.strip()
    s = re.sub(r"^[>\-\*\d\.\)\s]+", "", s)          # leading "> ", "- ", "1. "
    s = s.strip().strip('"').strip("'")
    # trailing source tag forms: " — [r/x, date]" / " (source: ...)" / " — https://..."
    s = re.sub(r"\s+[—-]\s*\[[^\]]*\]\s*$", "", s)
    s = re.sub(r"\s+\((?:source|src|via)[^)]*\)\s*$", "", s, flags=re.I)
    s = re.sub(r"\s+[—-]\s*https?://\S+\s*$", "", s)
    return s.strip().strip('"').strip("'").strip()


def segments_outside_brackets(quote: str):
    """Return the contiguous text segments with [bracketed insertions] removed."""
    parts = re.split(r"\[[^\]]*\]", quote)
    return [p.strip() for p in parts if len(p.strip()) >= 3]


def is_verbatim(quote: str, source_norm: str, case_sensitive: bool) -> bool:
    q = clean_quote(quote)
    if not q:
        return True  # empty / header line — not a quote, skip
    qn = normalize(q, case_sensitive)
    if qn and qn in source_norm:
        return True
    # allow bracketed insertions: every non-bracket segment must be in source
    segs = segments_outside_brackets(q)
    if segs and all(normalize(s, case_sensitive) in source_norm for s in segs):
        return True
    return False


def main():
    ap = argparse.ArgumentParser(description="Verbatim-Integrity gate for Customer Truth Map")
    ap.add_argument("--source", required=True, help="path to the raw source chunk text")
    ap.add_argument("--quotes", help="path to extracted quotes (one per line); omit to read stdin")
    ap.add_argument("--case-sensitive", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    with open(args.source, encoding="utf-8") as f:
        source_norm = normalize(f.read(), args.case_sensitive)

    raw = open(args.quotes, encoding="utf-8").read() if args.quotes else sys.stdin.read()
    lines = [ln for ln in raw.splitlines() if clean_quote(ln)]

    offenders = [ln.strip() for ln in lines
                 if not is_verbatim(ln, source_norm, args.case_sensitive)]
    checked = len(lines)
    passed = checked - len(offenders)

    if args.json:
        print(json.dumps({
            "checked": checked, "passed": passed,
            "offenders": offenders, "ok": not offenders,
        }, indent=2))
    else:
        print(f"Verbatim-Integrity: {passed}/{checked} quotes verified.")
        if offenders:
            print(f"\n❌ {len(offenders)} NON-VERBATIM line(s) — discard these and re-issue the "
                  f"rule (\"Return these sentences word for word. Do not paraphrase. Do not fix "
                  f"the grammar. Do not summarize.\"):")
            for o in offenders:
                print(f"   • {o}")
        else:
            print("✅ Every quote is verbatim. Gate PASSED.")

    sys.exit(1 if offenders else 0)


if __name__ == "__main__":
    main()
