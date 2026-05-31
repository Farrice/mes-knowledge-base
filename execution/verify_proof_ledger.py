#!/usr/bin/env python3
"""
verify_proof_ledger.py — Deterministic proof-claim gate for /copy-engine.

The problem this closes: `chain_runner.py finalize` enforces a Factual Grounding
veto, but (a) it only fires if `--factual` is passed honestly, and (b) the CLI
exits 0 even when it BLOCKS. So it cannot be an exit-code gate. This script is
the deterministic, exit-code-enforceable check the orchestrator needs.

What it does (pure regex + set membership — NO AI judgment):
    1. Regex-extracts "Freshness-Tax" claims from a finished draft:
         - statistics  (percentages, multipliers, "N times", significant counts)
         - prices      ($ amounts)
         - dates       (4-digit years, explicit month-year)
         - superlatives (best / #1 / only / first / proven / guaranteed / world's ...)
         - attributions (according to X / X study / research by X)
    2. Loads the claim ledger (proof-claims.md): rows carrying a label of
         VERIFIED | LIKELY | UNCONFIRMED.
    3. Asserts every extracted draft claim is PRESENT + LABELED in the ledger.
    4. Exits nonzero on ANY unlabeled claim (or a missing ledger when claims exist).

Label VALUE policy (e.g. "UNCONFIRMED presented as fact") is a judgment left to
the verification sub-agent + finalize --factual. This script enforces the
mechanical floor: every factual claim must appear in the ledger with a label.

Ledger row schema (proof-claims.md) — any of these forms is accepted:
    claim text | source_url | VERIFIED
    - "470% average ROI" | https://... | LIKELY
    | claim | source | UNCONFIRMED |        (markdown table row)
A row counts as "labeled" if it contains one of the three label tokens.

Usage:
    python3 execution/verify_proof_ledger.py --draft .tmp/copy-engine/draft.md \
        --ledger .tmp/copy-engine/proof-claims.md
    python3 execution/verify_proof_ledger.py --draft d.md --ledger l.md --json
    python3 execution/verify_proof_ledger.py --draft d.md --ledger l.md --quiet

Exit codes:
    0  PASS  — every Freshness-Tax claim is present + labeled (or no claims found)
    1  FAIL  — one or more claims unlabeled / missing, or ledger missing w/ claims
    2  ERROR — bad arguments / draft unreadable
"""

import argparse
import json
import re
import sys
from pathlib import Path

LABELS = ("VERIFIED", "LIKELY", "UNCONFIRMED")

# Superlative / authority words that signal an unverifiable-by-default claim.
SUPERLATIVES = [
    r"\bthe only\b", r"\bworld'?s\b", r"\b#1\b", r"\bnumber one\b", r"\bbest\b",
    r"\bfastest\b", r"\blargest\b", r"\bgreatest\b", r"\bproven\b", r"\bguaranteed\b",
    r"\bleading\b", r"\bmost (?:effective|powerful|advanced|trusted)\b", r"\bfirst-ever\b",
    r"\bonly (?:system|method|product|solution)\b",
]

# Attribution patterns — a claim leans on an external authority/source.
# Entity = a proper-noun sequence (Capitalized tokens, max 4), never spanning
# lowercase connectors or sentence punctuation (prevents greedy cross-sentence grabs).
_ENT = r"([A-Z][A-Za-z&.\-]*(?:\s+[A-Z][A-Za-z&.\-]*){0,3})"
ATTRIBUTIONS = [
    rf"\baccording to {_ENT}",
    rf"\b{_ENT}\s+(?:study|studies|research|trial|report)\b",
    rf"\bresearch by {_ENT}",
    r"\b(Harvard|Stanford|MIT|FDA|NASA|Forbes|Mayo Clinic|Johns Hopkins|Oxford|Cambridge)\b",
]


def _norm(s: str) -> str:
    """Normalize a token for matching: lowercase, strip commas/spaces."""
    return re.sub(r"[,\s]", "", s.lower())


def extract_claims(text: str) -> list[dict]:
    """Return a list of {type, key, snippet} Freshness-Tax claims from the draft."""
    claims: list[dict] = []
    seen: set[tuple] = set()
    occupied: list[tuple[int, int]] = []  # char spans already claimed by a higher-priority numeric match

    def _overlaps(a: int, b: int) -> bool:
        return any(a < e and s < b for s, e in occupied)

    def add(ctype: str, key: str, start: int, end: int | None = None, occupy: bool = False):
        k = _norm(key)
        if not k or (ctype, k) in seen:
            return
        seen.add((ctype, k))
        if occupy and end is not None:
            occupied.append((start, end))
        snippet = text[max(0, start - 45): start + len(key) + 45].replace("\n", " ").strip()
        claims.append({"type": ctype, "key": key.strip(), "match_key": k, "snippet": snippet})

    # 1. Percentages and multipliers (470%, 3x, 10X, "3 times") — highest priority, occupy span
    for m in re.finditer(r"\b\d[\d,]*\.?\d*\s?%", text):
        add("stat", m.group(0), m.start(), m.end(), occupy=True)
    for m in re.finditer(r"\b\d[\d,]*\.?\d*\s?[xX]\b", text):
        add("stat", m.group(0), m.start(), m.end(), occupy=True)
    for m in re.finditer(r"\b\d[\d,]*\.?\d*\s+times\b", text, re.I):
        add("stat", m.group(0), m.start(), m.end(), occupy=True)

    # 2. Prices / money — occupy span (so "2,000" inside "$2,000" isn't re-caught as a count)
    for m in re.finditer(r"\$\s?\d[\d,]*\.?\d*\s?(?:k|m|million|billion|/mo|/month|per month)?", text, re.I):
        add("price", m.group(0), m.start(), m.end(), occupy=True)

    # 3. Dates — 4-digit years and Month-Year — occupy span (so a year isn't re-caught as a count)
    for m in re.finditer(r"\b(?:19|20)\d{2}\b", text):
        add("date", m.group(0), m.start(), m.end(), occupy=True)
    for m in re.finditer(
        r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\.?\s+(?:19|20)?\d{2}\b", text):
        add("date", m.group(0), m.start(), m.end(), occupy=True)

    # 4. Significant standalone counts (full number w/ optional commas; e.g. "47 clients",
    #    "10,000 ads"). Skip any match overlapping a %/$/x/year span already captured.
    for m in re.finditer(r"(?<![\d,.\$])\d{1,3}(?:,\d{3})+(?![\d%])|(?<![\d,.\$%])\d{2,}(?![\d%]|\s?[xX]\b)", text):
        if not _overlaps(m.start(), m.end()):
            add("stat", m.group(0), m.start())

    # 5. Superlatives
    for pat in SUPERLATIVES:
        for m in re.finditer(pat, text, re.I):
            add("superlative", m.group(0), m.start())

    # 6. Attributions
    for pat in ATTRIBUTIONS:
        for m in re.finditer(pat, text):
            grp = m.group(1) if m.groups() else m.group(0)
            add("attribution", grp, m.start(m.lastindex or 0))

    return claims


def load_labeled_rows(ledger_text: str) -> list[str]:
    """Return ledger lines that carry one of the three label tokens (case-insensitive)."""
    rows = []
    for line in ledger_text.splitlines():
        up = line.upper()
        if any(lbl in up for lbl in LABELS):
            rows.append(line)
    return rows


def is_covered(claim: dict, labeled_rows: list[str]) -> bool:
    """A claim is covered if its key (numeric/price/date) or a content word
    (superlative/attribution) appears in some labeled ledger row."""
    key = claim["match_key"]
    if claim["type"] in ("stat", "price", "date"):
        # numeric-ish: the normalized number must appear in a labeled row
        digits = re.sub(r"[^\d]", "", key)
        for row in labeled_rows:
            rn = _norm(row)
            if key and key in rn:
                return True
            if digits and len(digits) >= 2 and digits in re.sub(r"[^\d]", "", rn):
                return True
        return False
    else:
        # superlative / attribution: require a shared significant word (>=4 chars)
        words = [w for w in re.findall(r"[a-z]{4,}", claim["snippet"].lower())]
        for row in labeled_rows:
            rl = row.lower()
            if any(w in rl for w in words):
                return True
        # attribution: the entity name itself
        ent_words = [w for w in re.findall(r"[a-z]{3,}", key.lower())]
        for row in labeled_rows:
            rl = row.lower()
            if ent_words and all(w in rl for w in ent_words):
                return True
        return False


def main() -> int:
    ap = argparse.ArgumentParser(description="Deterministic proof-claim ledger gate")
    ap.add_argument("--draft", required=True, help="Path to the finished draft")
    ap.add_argument("--ledger", required=True, help="Path to proof-claims.md")
    ap.add_argument("--json", action="store_true", help="Machine-readable output")
    ap.add_argument("--quiet", action="store_true", help="Only print on FAIL")
    args = ap.parse_args()

    draft_path = Path(args.draft)
    if not draft_path.exists():
        print(f"❌ ERROR: draft not found: {args.draft}", file=sys.stderr)
        return 2
    draft_text = draft_path.read_text(encoding="utf-8", errors="replace")

    claims = extract_claims(draft_text)

    ledger_path = Path(args.ledger)
    labeled_rows = []
    if ledger_path.exists():
        labeled_rows = load_labeled_rows(ledger_path.read_text(encoding="utf-8", errors="replace"))

    if not claims:
        if not args.quiet and not args.json:
            print("✅ PASS — no Freshness-Tax claims detected in draft (nothing to verify).")
        if args.json:
            print(json.dumps({"status": "PASS", "claims": 0, "uncovered": []}))
        return 0

    if not ledger_path.exists():
        msg = (f"🚫 FAIL — {len(claims)} factual claim(s) in draft but ledger missing: "
               f"{args.ledger}. Cannot verify. Build the proof-claims ledger first.")
        if args.json:
            print(json.dumps({"status": "FAIL", "claims": len(claims),
                              "reason": "ledger_missing",
                              "uncovered": [c["snippet"] for c in claims]}))
        else:
            print(msg, file=sys.stderr)
        return 1

    uncovered = [c for c in claims if not is_covered(c, labeled_rows)]

    if args.json:
        print(json.dumps({
            "status": "FAIL" if uncovered else "PASS",
            "claims": len(claims),
            "labeled_rows": len(labeled_rows),
            "uncovered": [{"type": c["type"], "key": c["key"], "snippet": c["snippet"]}
                          for c in uncovered],
        }, indent=2))
        return 1 if uncovered else 0

    if uncovered:
        print(f"🚫 PROOF-LEDGER GATE: FAIL — {len(uncovered)} of {len(claims)} "
              f"factual claim(s) are NOT present+labeled in the ledger:\n", file=sys.stderr)
        for c in uncovered:
            print(f"  [{c['type']}] {c['key']}", file=sys.stderr)
            print(f"      …{c['snippet']}…", file=sys.stderr)
        print(f"\nLabel each in {args.ledger} as VERIFIED|LIKELY|UNCONFIRMED "
              f"(with a source), or cut/caveat the claim. Delivery blocked.", file=sys.stderr)
        return 1

    if not args.quiet:
        print(f"✅ PROOF-LEDGER GATE: PASS — all {len(claims)} factual claim(s) "
              f"present + labeled across {len(labeled_rows)} ledger row(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
