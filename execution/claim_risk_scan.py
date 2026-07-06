#!/usr/bin/env python3
"""
Claim Risk Scan — deterministic FTC/FDA disease-claim scanner for Path A
(claim-safe content for funded health/supplement brands). A missed disease
claim is a real liability, and the "never ship infra that depends on the
model REMEMBERING" rule means this cannot live as a workflow the model has
to recall to run — it has to be code wired into the finalize path. This
module is the scanner; chain_runner.finalize() is the deterministic trigger.

Compass-not-cage: this NEVER blocks delivery. It flags, loudly for
DISEASE_CLAIM hits, quietly for RISKY/WATCH — same posture as
grounding_guard.py and content_finish_gate.py, which cap scores but never
hard-veto (the only hard veto in this system is chain_runner's Factual
Grounding veto, which this module does not touch).

SOURCE OF TRUTH
----------------
skills/claim-safe-health-marketing/references/red-flag-word-bank.md is the
canonical word bank (Farrice/genius.md maintained). This script PARSES that
markdown at scan time via load_bank(); if the md is missing or unparseable,
it falls back to a small embedded bank so scanning never crashes finalize.
Because live-parsing a hand-maintained markdown file is inherently a little
brittle, `--rebuild` compiles a snapshot to .agent/claim-risk-bank.json —
run it after editing the word bank md to pin the compiled version; load_bank()
prefers the JSON snapshot when present (faster, and immune to markdown
formatting drift) and only re-parses the md live if the snapshot is absent.

DETECTION
---------
  (a) DISEASE_CLAIM — a treatment/cure verb (treats/cures/prevents/reverses/…)
      and a disease-name token in the SAME sentence. The hard FTC/FDA line.
  (b) RISKY — red-flag words/phrases with a compliant swap available but no
      disease pairing: a treatment verb used alone, a disease token appearing
      without a verb (still trips Amazon-style scanners per the word bank),
      outcome-guarantee language ("guaranteed results"), unsubstantiated
      evidence-strength language ("clinically proven"), or comparison/
      substitution framing ("alternative to [drug]").
  (c) WATCH — category-specific high-risk terms (inflammation, blood sugar,
      etc. — Dougherty's "especially sensitive" list) and unqualified
      numeric+timeframe "typical results" claims with no disclaimer nearby.

CLI
---
  python3 execution/claim_risk_scan.py scan <file> [--json]
  python3 execution/claim_risk_scan.py --rebuild
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

_ROOT = Path(__file__).resolve().parent.parent
_MD_PATH = _ROOT / "skills" / "claim-safe-health-marketing" / "references" / "red-flag-word-bank.md"
_BANK_JSON_PATH = _ROOT / ".agent" / "claim-risk-bank.json"

# Acronym/short disease tokens where a case-insensitive match would collide
# with common English words ("aids" the verb, "adhd" as a substring is rare
# but "hiv"/"aids" lowercase are common enough in casual copy to false-positive).
_CASE_SENSITIVE_TOKENS = {"aids", "hiv", "adhd"}

# Minimal embedded fallback so a missing/corrupt md never breaks finalize.
_FALLBACK_BANK: Dict[str, Any] = {
    "disease_tokens": [
        "cancer", "diabetes", "arthritis", "depression", "herpes", "lupus",
        "heart disease", "autism",
    ],
    "treatment_verbs": [
        {"tokens": ["cures", "cure"], "compliant": "Supports [normal function]", "notes": "Never pair with any disease token"},
        {"tokens": ["treats", "treatment"], "compliant": "Supports / promotes", "notes": ""},
        {"tokens": ["prevents", "prevention"], "compliant": "Supports [immune/metabolic/etc.] health", "notes": "\"Prevents\" is a disease-claim verb even with a vague object"},
        {"tokens": ["heals", "healing"], "compliant": "Soothes / supports comfort", "notes": ""},
        {"tokens": ["reverses"], "compliant": "Supports healthy [function] as part of a balanced routine", "notes": "\"Reverses\" implies existing pathology"},
        {"tokens": ["remedy", "remedies"], "compliant": "Supports", "notes": ""},
        {"tokens": ["eliminates"], "compliant": "Supports a healthy response to [trigger]", "notes": ""},
    ],
    "outcome_guarantee": [
        {"phrase": "Guaranteed results", "compliant": "[N]% of customers report [specific, typical, disclosed result] within [timeframe]"},
        {"phrase": "Works instantly", "compliant": "Formulated for [mechanism]; many customers notice [typical, non-disease effect] within [realistic timeframe]"},
        {"phrase": "Melts fat away", "compliant": "Supports healthy weight management as part of a balanced diet and exercise routine"},
    ],
    "evidence_strength": [
        {"phrase": "Clinically proven", "compliant": "Formulated with clinically studied ingredients"},
        {"phrase": "Scientifically proven", "compliant": "Backed by research on [specific ingredient/mechanism]"},
        {"phrase": "Doctors recommend", "compliant": "Formulated by [credentialed role, named and verifiable]"},
    ],
    "category_terms": [
        "inflammation", "immune-boosting", "cholesterol", "blood pressure",
        "weight loss", "blood sugar",
    ],
    "comparison_phrases": ["Alternative to [named drug]", "Works like [prescription name]", "Skip the prescription"],
    "source_md": None,
    "generated_at": None,
}

_TIER_ORDER = {"CLEAN": 0, "WATCH": 1, "RISKY": 2, "DISEASE_CLAIM": 3}


# ─────────────────────────────────────────────────────────────────
# Markdown bank parsing
# ─────────────────────────────────────────────────────────────────

def _sections(md_text: str) -> Dict[str, str]:
    """Split a markdown doc into {heading_line: body} at each '## ' heading."""
    parts = re.split(r"^## ", md_text, flags=re.MULTILINE)
    out: Dict[str, str] = {}
    for part in parts[1:]:
        heading, _, body = part.partition("\n")
        out[heading.strip()] = body
    return out


def _parse_table(block: str) -> List[List[str]]:
    """Parse a markdown pipe-table block into rows of cells (row 0 = header)."""
    rows: List[List[str]] = []
    for line in block.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        if re.match(r"^\|[\s:|-]+\|$", line):
            continue  # separator row
        cells = [c.strip() for c in line.strip("|").split("|")]
        rows.append(cells)
    return rows


def _split_slash_tokens(cell: str) -> List[str]:
    """'Cures / cure' -> ['cures', 'cure']; strips bracket placeholders first."""
    cleaned = re.sub(r"\[[^\]]*\]", "", cell)
    tokens = []
    for part in cleaned.split("/"):
        part = part.strip().strip(".").strip()
        if part:
            tokens.append(part.lower())
    return tokens


def _extract_quoted_or_raw(cell: str) -> str:
    m = re.search(r'"([^"]+)"', cell)
    return m.group(1).strip() if m else cell.strip()


def _extract_disease_tokens(body: str) -> List[str]:
    first_chunk = body.split("**Rule**")[0]
    tokens: List[str] = []
    for chunk in first_chunk.split(","):
        chunk = re.sub(r"\([^)]*\)", "", chunk)  # drop parentheticals
        chunk = chunk.strip().rstrip(".").strip()
        if not chunk:
            continue
        for sub in chunk.split("/"):
            sub = sub.strip()
            if sub:
                tokens.append(sub)
    return tokens


def _extract_category_terms(body: str) -> List[str]:
    first_sentence = body.split(".")[0]
    tokens: List[str] = []
    for chunk in first_sentence.split(","):
        chunk = chunk.strip()
        if not chunk:
            continue
        for sub in chunk.split("/"):
            sub = sub.strip()
            if sub:
                tokens.append(sub)
    return tokens


def _extract_bullet_phrases(body: str) -> List[str]:
    phrases = []
    for line in body.splitlines():
        line = line.strip()
        if not line.startswith("-"):
            continue
        m = re.search(r'"([^"]+)"', line)
        if m:
            phrases.append(m.group(1).strip())
    return phrases


def build_bank_from_md(md_path: Path = _MD_PATH) -> Dict[str, Any]:
    """Parse the red-flag word bank markdown into the compiled bank structure.
    Raises on any hard failure — callers should catch and fall back."""
    text = md_path.read_text(encoding="utf-8")
    sections = _sections(text)

    disease_tokens: List[str] = []
    treatment_verbs: List[Dict[str, Any]] = []
    outcome_guarantee: List[Dict[str, str]] = []
    evidence_strength: List[Dict[str, str]] = []
    category_terms: List[str] = []
    comparison_phrases: List[str] = []

    for heading, body in sections.items():
        if heading.startswith("Disease-Name Tokens"):
            disease_tokens = _extract_disease_tokens(body)
        elif heading.startswith("Treatment/Cure Verbs"):
            rows = _parse_table(body)
            for row in rows[1:]:
                if len(row) < 2:
                    continue
                banned_tokens = _split_slash_tokens(row[0])
                compliant = row[1].strip()
                notes = row[2].strip() if len(row) > 2 else ""
                if banned_tokens:
                    treatment_verbs.append({"tokens": banned_tokens, "compliant": compliant, "notes": notes})
        elif heading.startswith("Outcome-Guarantee Language"):
            rows = _parse_table(body)
            for row in rows[1:]:
                if len(row) < 2:
                    continue
                phrase = _extract_quoted_or_raw(row[0])
                compliant = _extract_quoted_or_raw(row[1])
                if phrase:
                    outcome_guarantee.append({"phrase": phrase, "compliant": compliant})
        elif heading.startswith("Evidence-Strength Language"):
            rows = _parse_table(body)
            for row in rows[1:]:
                if len(row) < 2:
                    continue
                phrase = _extract_quoted_or_raw(row[0])
                compliant = _extract_quoted_or_raw(row[1])
                if phrase:
                    evidence_strength.append({"phrase": phrase, "compliant": compliant})
        elif heading.startswith("Category-Specific High-Risk Terms"):
            category_terms = _extract_category_terms(body)
        elif heading.startswith("Comparison/Substitution Language"):
            comparison_phrases = _extract_bullet_phrases(body)

    if not disease_tokens or not treatment_verbs:
        raise ValueError("red-flag-word-bank.md parsed but core sections came back empty — treat as parse failure")

    return {
        "disease_tokens": disease_tokens,
        "treatment_verbs": treatment_verbs,
        "outcome_guarantee": outcome_guarantee,
        "evidence_strength": evidence_strength,
        "category_terms": category_terms,
        "comparison_phrases": comparison_phrases,
        "source_md": str(md_path),
        "generated_at": datetime.now().isoformat(),
    }


def save_bank(bank: Dict[str, Any], path: Path = _BANK_JSON_PATH) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(bank, f, indent=2)


def load_bank(rebuild: bool = False) -> Dict[str, Any]:
    """Load the compiled bank. Prefers the .agent/ JSON snapshot; parses the
    md live if no snapshot exists yet; falls back to the embedded minimal
    bank if both the snapshot and the live parse fail (never raises)."""
    if rebuild:
        try:
            bank = build_bank_from_md()
            save_bank(bank)
            return bank
        except Exception:
            pass  # fall through to snapshot/fallback below

    if _BANK_JSON_PATH.exists():
        try:
            with open(_BANK_JSON_PATH, encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass

    try:
        bank = build_bank_from_md()
        try:
            save_bank(bank)
        except Exception:
            pass
        return bank
    except Exception:
        return dict(_FALLBACK_BANK)


# ─────────────────────────────────────────────────────────────────
# Scanning
# ─────────────────────────────────────────────────────────────────

def _token_pattern(token: str) -> re.Pattern:
    escaped = r"\s+".join(re.escape(w) for w in token.split())
    flags = 0 if token.lower() in _CASE_SENSITIVE_TOKENS else re.IGNORECASE
    return re.compile(rf"\b{escaped}\b", flags)


def _phrase_pattern(phrase: str) -> re.Pattern:
    """Bracket placeholders (e.g. '[named drug]') become a bounded wildcard so
    'Alternative to [named drug]' matches 'alternative to Ozempic'."""
    parts = re.split(r"(\[[^\]]+\])", phrase)
    out = []
    for part in parts:
        if part.startswith("[") and part.endswith("]"):
            out.append(r"[\w][\w\s/'-]{0,40}")
        elif part:
            out.append(re.escape(part))
    pattern = "".join(out) if out else re.escape(phrase)
    return re.compile(pattern, re.IGNORECASE)


def _split_sentences(text: str) -> List[Tuple[int, int, str]]:
    spans = []
    for m in re.finditer(r"[^.!?\n]+[.!?]?", text):
        s = m.group().strip()
        if s:
            spans.append((m.start(), m.end(), s))
    return spans


_RESULT_CLAIM_RE = re.compile(
    r"\b\d{1,3}\s?(?:%|lbs?|pounds?|kg|inches?)\b[^.\n]{0,60}?\b(?:in|within)\b[^.\n]{0,20}?"
    r"\b(?:hours?|days?|weeks?|months?)\b",
    re.IGNORECASE,
)
_DISCLAIMER_RE = re.compile(
    r"results?\s+may\s+vary|individual\s+results?|not\s+typical|"
    r"your\s+results?\s+may\s+differ|not\s+been\s+evaluated\s+by\s+the\s+food\s+and\s+drug",
    re.IGNORECASE,
)


def scan(text: str, bank: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Scan text for claim risk. Returns {"verdict","counts","hits"}.
    Never raises on well-formed input; empty/short text returns CLEAN."""
    bank = bank or load_bank()
    hits: Dict[str, List[Dict[str, str]]] = {"DISEASE_CLAIM": [], "RISKY": [], "WATCH": []}

    if not text or len(text) < 20:
        return {"verdict": "CLEAN", "counts": {k: 0 for k in hits}, "hits": hits}

    disease_patterns = [(tok, _token_pattern(tok)) for tok in bank.get("disease_tokens", [])]
    verb_entries = []
    for entry in bank.get("treatment_verbs", []):
        for tok in entry.get("tokens", []):
            verb_entries.append((tok, _token_pattern(tok), entry.get("compliant", ""), entry.get("notes", "")))

    sentences = _split_sentences(text)
    disease_hit_spans = set()

    # (a) DISEASE_CLAIM: verb + disease token, same sentence.
    for start, end, sent in sentences:
        matched_diseases = [tok for tok, pat in disease_patterns if pat.search(sent)]
        matched_verbs = [(tok, c, n) for tok, pat, c, n in verb_entries if pat.search(sent)]
        if matched_diseases and matched_verbs:
            for vtok, compliant, vnotes in matched_verbs:
                for dtok in matched_diseases:
                    hits["DISEASE_CLAIM"].append({
                        "pattern": f"{vtok} + {dtok}",
                        "context": sent[:220],
                        "swap": compliant,
                        "note": vnotes or "treatment verb paired with a disease-name token in the same sentence",
                    })
            disease_hit_spans.add((start, end))

    # (b) RISKY, part 1: disease token alone (no verb in that sentence) —
    # still trips platform scanners (Amazon) per the word bank.
    for start, end, sent in sentences:
        if (start, end) in disease_hit_spans:
            continue
        for tok, pat in disease_patterns:
            if pat.search(sent):
                hits["RISKY"].append({
                    "pattern": tok,
                    "context": sent[:220],
                    "swap": "Remove the disease-name token or route through legal review — platform scanners (e.g. Amazon) flag disease tokens regardless of surrounding context.",
                    "note": "disease-name token present without a same-sentence treatment verb",
                })

    # (b) RISKY, part 2: treatment/cure verb used without disease pairing —
    # still a structure/function compliance risk with a documented swap.
    for start, end, sent in sentences:
        if (start, end) in disease_hit_spans:
            continue
        for tok, pat, compliant, vnotes in verb_entries:
            if pat.search(sent):
                hits["RISKY"].append({
                    "pattern": tok,
                    "context": sent[:220],
                    "swap": compliant,
                    "note": vnotes or "treatment/cure verb used without disease pairing",
                })

    # (b) RISKY, part 3: outcome-guarantee + evidence-strength phrases.
    for entry in bank.get("outcome_guarantee", []) + bank.get("evidence_strength", []):
        phrase = entry.get("phrase", "")
        if not phrase:
            continue
        pat = _phrase_pattern(phrase)
        for m in pat.finditer(text):
            hits["RISKY"].append({
                "pattern": phrase,
                "context": text[max(0, m.start() - 40): m.end() + 40].strip(),
                "swap": entry.get("compliant", ""),
                "note": "outcome-guarantee / evidence-strength language from the red-flag word bank",
            })

    # (b) RISKY, part 4: comparison/substitution framing — never permitted
    # regardless of evidence tier.
    for phrase in bank.get("comparison_phrases", []):
        pat = _phrase_pattern(phrase)
        for m in pat.finditer(text):
            hits["RISKY"].append({
                "pattern": phrase,
                "context": text[max(0, m.start() - 40): m.end() + 40].strip(),
                "swap": "Remove entirely — comparison/substitution framing vs. a named drug/prescription is never permitted regardless of evidence.",
                "note": "comparison/substitution language",
            })

    # (c) WATCH, part 1: category-specific high-risk terms.
    for term in bank.get("category_terms", []):
        pat = _token_pattern(term)
        for m in pat.finditer(text):
            hits["WATCH"].append({
                "pattern": term,
                "context": text[max(0, m.start() - 40): m.end() + 40].strip(),
                "swap": "Confirm Tier 4-5 evidence exists for this category before shipping (Dougherty's 'especially sensitive' list).",
                "note": "category-specific high-risk term",
            })

    # (c) WATCH, part 2: unqualified numeric + timeframe "typical results"
    # claims with no disclaimer language nearby.
    for m in _RESULT_CLAIM_RE.finditer(text):
        window = text[max(0, m.start() - 200): m.end() + 200]
        if not _DISCLAIMER_RE.search(window):
            hits["WATCH"].append({
                "pattern": m.group(0).strip(),
                "context": text[max(0, m.start() - 40): m.end() + 40].strip(),
                "swap": "Add a proximate disclaimer (e.g. 'individual results may vary') or reframe as a disclosed, typical-result statement per genius.md GP-07.",
                "note": "unqualified numeric+timeframe result claim, no nearby disclaimer",
            })

    verdict = "CLEAN"
    for tier in ("WATCH", "RISKY", "DISEASE_CLAIM"):
        if hits[tier]:
            verdict = tier

    return {
        "verdict": verdict,
        "counts": {k: len(v) for k, v in hits.items()},
        "hits": hits,
    }


def scan_file(path: str, bank: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    text = Path(path).read_text(encoding="utf-8", errors="ignore")
    result = scan(text, bank)
    result["file"] = path
    return result


def format_summary(result: Dict[str, Any]) -> str:
    lines = []
    lines.append(f"CLAIM RISK SCAN — verdict: {result['verdict']}")
    counts = result.get("counts", {})
    lines.append(f"  DISEASE_CLAIM: {counts.get('DISEASE_CLAIM', 0)}  RISKY: {counts.get('RISKY', 0)}  WATCH: {counts.get('WATCH', 0)}")
    for tier in ("DISEASE_CLAIM", "RISKY", "WATCH"):
        tier_hits = result.get("hits", {}).get(tier, [])
        if not tier_hits:
            continue
        lines.append(f"\n[{tier}]")
        for h in tier_hits:
            lines.append(f"  • {h['pattern']} — \"{h['context']}\"")
            lines.append(f"      swap → {h['swap']}")
    return "\n".join(lines)


# ─────────────────────────────────────────────────────────────────
# CLI
# ─────────────────────────────────────────────────────────────────

def _cli() -> int:
    parser = argparse.ArgumentParser(prog="claim_risk_scan.py")
    parser.add_argument("--rebuild", action="store_true",
                         help="Rebuild .agent/claim-risk-bank.json from the red-flag word bank md")
    sub = parser.add_subparsers(dest="command")
    scan_p = sub.add_parser("scan", help="Scan a text/markdown file for claim risk")
    scan_p.add_argument("file")
    scan_p.add_argument("--json", action="store_true")
    args = parser.parse_args()

    if args.rebuild:
        bank = build_bank_from_md() if _MD_PATH.exists() else dict(_FALLBACK_BANK)
        save_bank(bank)
        print(
            f"Rebuilt {_BANK_JSON_PATH} — disease_tokens={len(bank['disease_tokens'])} "
            f"treatment_verbs={len(bank['treatment_verbs'])} "
            f"outcome_guarantee={len(bank.get('outcome_guarantee', []))} "
            f"evidence_strength={len(bank.get('evidence_strength', []))} "
            f"category_terms={len(bank.get('category_terms', []))} "
            f"comparison_phrases={len(bank.get('comparison_phrases', []))}"
        )
        if args.command != "scan":
            return 0

    if args.command == "scan":
        result = scan_file(args.file)
        if args.json:
            print(json.dumps(result, indent=2))
        else:
            print(format_summary(result))
        return 0

    if not args.rebuild:
        parser.print_help()
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(_cli())
