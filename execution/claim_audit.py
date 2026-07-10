#!/usr/bin/env python3
"""
Claim Audit — deterministic anti-fabrication net for Antigravity.

Wave 2 (Harness Apex Plan): turns jw-engine's Gate-0 assumption-label audit
and Chain Step 5.5's confidence-labeling discipline into an exit code a
mid-tier model cannot silently skip.

This is a NET, not a judge. Its job is "no unlabeled factual-claim carrier
escapes" — it does NOT adjudicate whether a claim is true. Truth adjudication
stays with Step 5.5 / fact-verifier. What this catches deterministically:
a number, date, named-entity claim, or superlative-with-stats that carries
NO grounding marker at all.

A carrier line passes if the line itself, the line above, or the line below
carries any of:
    - a bracketed grounding tag:  [VERIFIED] [LIKELY] [UNCONFIRMED]
      [ASSUMED] / [ASSUMED: ...] [MODELED]
    - a bare UPPERCASE verdict marker: VERIFIED / LIKELY / UNCONFIRMED /
      ASSUMED / MODELED / GROUNDED / REFUTED (case-sensitive — matches the
      house style of heavy reports and jw-engine grounding summaries)
    - a source URL (http/https)
    - a `Source:` / `Sources:` field

False-positive controls: fenced code blocks, YAML frontmatter, markdown
table separator rows, inline code spans, file paths, `file.md:123` line
refs, markdown link URLs, and version strings (v1.2 / 1.2.3) are all
excluded before carrier detection.

CLI:
    python3 execution/claim_audit.py check <file> [--json] [--strict]
    python3 execution/claim_audit.py tag-help

Exit codes (check):
    0  no untagged carriers (and, with --strict, UNCONFIRMED density <= 30%)
    1  untagged carriers found (or --strict density breach)
    2  usage / file error
"""

import argparse
import json
import re
import sys
from pathlib import Path

# ── Grounding markers ────────────────────────────────────────

GROUNDING_TAGS = ["VERIFIED", "LIKELY", "UNCONFIRMED", "ASSUMED", "MODELED"]

BRACKET_TAG_RE = re.compile(
    r"\[(VERIFIED|LIKELY|UNCONFIRMED|ASSUMED|MODELED)\b[^\]]*\]"
)
# Bare uppercase verdict markers (house style: **UNCONFIRMED**, 🟢 GROUNDED, REFUTED)
BARE_TAG_RE = re.compile(
    r"\b(VERIFIED|LIKELY|UNCONFIRMED|ASSUMED|MODELED|GROUNDED|REFUTED)\b"
)
URL_RE = re.compile(r"https?://\S+")
SOURCE_FIELD_RE = re.compile(r"\bSources?\s*:", re.IGNORECASE)

# ── Carrier patterns (run against SANITIZED line text) ───────

MONTHS = (
    r"Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
    r"Jul(?:y)?|Aug(?:ust)?|Sep(?:t(?:ember)?)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?"
)

CLAIM_VERBS = (
    r"said|says|reported|reports|found|finds|grew|grows|costs?|charged?|charges|"
    r"raised|launched|announced|confirmed|showed|shows|increased|decreased|"
    r"published|acquired|hit|reached|earn(?:s|ed)?|generat(?:es|ed)|sold|"
    r"pays?|paid|closed|converted"
)

PROPER_NOUN_SEQ_RE = re.compile(r"\b[A-Z][a-zA-Z&.]+(?:\s+[A-Z][a-zA-Z&.]+)+\b")
CLAIM_VERB_RE = re.compile(r"\b(?:%s)\b" % CLAIM_VERBS, re.IGNORECASE)

CARRIER_PATTERNS = [
    ("currency", re.compile(
        r"[$€£]\s?\d[\d,]*(?:\.\d+)?\s?[KkMmBb]?\b"
        r"|\b\d[\d,]*(?:\.\d+)?\s?(?:USD|dollars)\b")),
    ("percent", re.compile(
        r"\b\d[\d,]*(?:\.\d+)?\s?(?:%|percent)")),
    ("number+unit", re.compile(
        r"\b\d[\d,]*(?:\.\d+)?\s?(?:million|billion|thousand)\b"
        r"|\b\d[\d,]*(?:\.\d+)?[KMB]\+?\b"
        r"|\b\d[\d,]*\s(?:users|customers|clients|leads|subscribers|followers|"
        r"views|impressions|downloads|employees|companies|agencies|studies|"
        r"sources|deals|calls|bookings|sales|reviews|members)\b")),
    ("date", re.compile(
        r"\b(?:" + MONTHS + r")\.?\s+\d{1,2}(?:st|nd|rd|th)?"
        r"(?:,?\s*(?:19|20)\d{2})?\b"
        r"|\b(?:19|20)\d{2}-\d{2}-\d{2}\b")),
    ("year", re.compile(r"\b(?:19|20)\d{2}\b")),
]

SUPERLATIVE_RE = re.compile(
    r"\b(?:largest|biggest|fastest|fastest-growing|leading|best-selling|"
    r"most\s+\w+|#1|top\s+\d+|first(?:-ever)?|only\s+\w+)\b", re.IGNORECASE)

# ── Sanitizers (strip before carrier detection) ──────────────

INLINE_CODE_RE = re.compile(r"`[^`]*`")
MD_LINK_URL_RE = re.compile(r"\]\([^)]*\)")            # [text](url) → keep text
PATH_TOKEN_RE = re.compile(r"\S*/\S+")                 # anything with a slash
LINE_REF_RE = re.compile(r"\S+\.\w{1,4}:\d+")          # file.md:84
VERSION_RE = re.compile(r"\bv\d+(?:\.\d+)+\b|\b\d+\.\d+\.\d+\b")
TABLE_SEP_RE = re.compile(r"^\s*\|?[\s:|-]+\|?\s*$")


def sanitize(line: str) -> str:
    line = INLINE_CODE_RE.sub(" ", line)
    line = MD_LINK_URL_RE.sub("]", line)
    line = URL_RE.sub(" ", line)
    line = LINE_REF_RE.sub(" ", line)
    line = PATH_TOKEN_RE.sub(" ", line)
    line = VERSION_RE.sub(" ", line)
    return line


def line_has_grounding(raw_line: str) -> "str | None":
    """Return the grounding kind found on a RAW line, else None."""
    m = BRACKET_TAG_RE.search(raw_line)
    if m:
        return m.group(1)
    m = BARE_TAG_RE.search(raw_line)
    if m:
        return m.group(1)
    if URL_RE.search(raw_line):
        return "URL"
    if SOURCE_FIELD_RE.search(raw_line):
        return "SOURCE-FIELD"
    return None


def detect_carriers(sanitized: str) -> list:
    """Return list of (kind, excerpt) carriers on a sanitized line."""
    found = []
    matched_spans = []

    def overlaps(span):
        return any(not (span[1] <= s or span[0] >= e) for s, e in matched_spans)

    for kind, pat in CARRIER_PATTERNS:
        for m in pat.finditer(sanitized):
            if kind == "year" and overlaps(m.span()):
                continue  # year already inside a currency/date/number match
            matched_spans.append(m.span())
            found.append((kind, m.group(0).strip()))

    # proper-noun sequence near a claim verb
    if CLAIM_VERB_RE.search(sanitized):
        pn = PROPER_NOUN_SEQ_RE.search(sanitized)
        if pn:
            found.append(("entity+claim-verb", pn.group(0)))

    # superlative with a stat on the same line
    sup = SUPERLATIVE_RE.search(sanitized)
    if sup and re.search(r"\d", sanitized):
        found.append(("superlative+stat", sup.group(0)))

    return found


def audit_file(path: Path) -> dict:
    text = path.read_text(encoding="utf-8", errors="replace")
    lines = text.splitlines()

    # frontmatter bounds
    fm_end = -1
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                fm_end = i
                break

    findings = []
    in_fence = False
    for i, raw in enumerate(lines):
        stripped = raw.strip()
        if stripped.startswith("```") or stripped.startswith("~~~"):
            in_fence = not in_fence
            continue
        if in_fence or i <= fm_end:
            continue
        if TABLE_SEP_RE.match(raw) or not stripped:
            continue

        carriers = detect_carriers(sanitize(raw))
        if not carriers:
            continue

        # grounding on same line or adjacent lines
        tag = line_has_grounding(raw)
        if tag is None and i > 0:
            tag = line_has_grounding(lines[i - 1])
        if tag is None and i + 1 < len(lines):
            tag = line_has_grounding(lines[i + 1])

        for kind, excerpt in carriers:
            findings.append({
                "line": i + 1,
                "kind": kind,
                "excerpt": excerpt,
                "context": stripped[:110],
                "tag": tag,   # None = untagged
            })

    tagged = [f for f in findings if f["tag"]]
    untagged = [f for f in findings if not f["tag"]]
    unconfirmed = [f for f in tagged if f["tag"] == "UNCONFIRMED"]
    density = (len(unconfirmed) / len(tagged) * 100.0) if tagged else 0.0

    return {
        "file": str(path),
        "carriers": len(findings),
        "tagged": len(tagged),
        "untagged": len(untagged),
        "unconfirmed_density_pct": round(density, 1),
        "findings": findings,
    }


TAG_HELP = """\
CLAIM GROUNDING TAGS — every factual-claim carrier (number with units/
currency/percent, date or 4-digit year, named entity + claim verb,
superlative with a stat) must carry one of these on the SAME or an
ADJACENT line, or a source:

  [VERIFIED]      confirmed against 2+ independent sources
  [LIKELY]        one credible source or strong inference — say which
  [UNCONFIRMED]   could not verify — reader must check before relying on it
  [ASSUMED: ...]  inferred by the model, no source — state the basis
  [MODELED]       produced by estimation/projection, not observation

Also accepted as grounding:
  - a source URL (http/https) on the same or adjacent line
  - a `Source:` / `Sources:` field

Rule of thumb: if you state a number, a date, or "X did/said/costs Y"
and you cannot cite where it came from, tag it [ASSUMED: ...] or cut it.
An unlabeled claim is a gate failure (`python3 execution/claim_audit.py
check <file>` exits 1), not a style issue."""


def cmd_check(args) -> int:
    path = Path(args.file)
    if not path.is_file():
        print(f"claim_audit: file not found: {path}", file=sys.stderr)
        return 2

    result = audit_file(path)
    strict_breach = args.strict and result["tagged"] > 0 and \
        result["unconfirmed_density_pct"] > 30.0
    passed = result["untagged"] == 0 and not strict_breach
    result["strict"] = bool(args.strict)
    result["strict_breach"] = bool(strict_breach)
    result["result"] = "PASS" if passed else "FAIL"

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(f"CLAIM AUDIT — {result['file']}")
        for f in result["findings"]:
            status = f"tagged: {f['tag']}" if f["tag"] else "UNTAGGED"
            print(f"  L{f['line']:<5} [{status}] {f['kind']}: "
                  f"\"{f['excerpt']}\"  |  {f['context']}")
        if not result["findings"]:
            print("  (no factual-claim carriers detected)")
        print(f"Counts: carriers={result['carriers']} "
              f"tagged={result['tagged']} untagged={result['untagged']} "
              f"unconfirmed-density={result['unconfirmed_density_pct']}%")
        if strict_breach:
            print("STRICT: UNCONFIRMED density exceeds 30% — "
                  "verify or cut before shipping.")
        print(f"RESULT: {result['result']}")

    return 0 if passed else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Deterministic anti-fabrication net: every factual-claim "
                    "carrier must carry a grounding tag or source.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_check = sub.add_parser("check", help="Audit a file for untagged claims.")
    p_check.add_argument("file")
    p_check.add_argument("--json", action="store_true")
    p_check.add_argument("--strict", action="store_true",
                         help="Also fail on [UNCONFIRMED] density > 30%%.")

    sub.add_parser("tag-help",
                   help="Print the tag vocabulary for worker-prompt injection.")

    args = parser.parse_args()
    if args.command == "check":
        return cmd_check(args)
    if args.command == "tag-help":
        print(TAG_HELP)
        return 0
    return 2


if __name__ == "__main__":
    sys.exit(main())
