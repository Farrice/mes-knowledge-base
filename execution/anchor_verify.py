#!/usr/bin/env python3
"""
Anchor Verify — anchor-propagation checker for Supercomputer missions.

Wave 2 (Harness Apex Plan): closes the open question named in
`skills/supercomputer/genius.md` ("Anchor-memory propagation enforcement …
eventually: a finalize-time check that grep-detects anchor path references
in dependent deliverables, scores propagation 1-10"). This is that check.

How it scores: key terms are extracted from the anchor file (headings,
bolded phrases, proper-noun sequences, numbers with units/currency/percent
— plus any explicit `--terms`), each term carries a weight, and every
target is grepped for coverage. Propagation score per target =
1 + 9 x (covered weight / total weight), rounded. Overall = weighted mean
across targets. Missing terms are printed per target so a low score is
always explainable and fixable (re-inject exactly those terms, regenerate).

CLI:
    python3 execution/anchor_verify.py check \
        --anchor projects/<slug>/path/to/anchor.md \
        --targets deliverable1.md deliverable2.md [dir/ ...] \
        [--terms "term a,term b"] [--min-score 7] [--json]

Targets may be files or directories (directories scan *.md/*.txt recursively).

Exit codes:
    0  overall score >= min-score (default 7)
    1  overall score below min-score — fix propagation before finalizing
    2  usage / file error
"""

import argparse
import json
import re
import sys
from pathlib import Path

# ── Term extraction ──────────────────────────────────────────

HEADING_RE = re.compile(r"^#{1,6}\s+(.*)$", re.MULTILINE)
BOLD_RE = re.compile(r"\*\*([^*\n]{3,80})\*\*|__([^_\n]{3,80})__")
PROPER_NOUN_RE = re.compile(r"\b[A-Z][a-zA-Z&.]+(?:\s+[A-Z][a-zA-Z&.]+)+\b")
NUMBER_RE = re.compile(
    r"[$€£]\s?\d[\d,]*(?:\.\d+)?[KkMmBb]?"
    r"|\b\d[\d,]*(?:\.\d+)?\s?%"
    r"|\b\d[\d,]*(?:\.\d+)?\s?(?:million|billion|thousand|USD)\b")
FENCE_RE = re.compile(r"^(?:```|~~~).*?^(?:```|~~~)\s*$", re.MULTILINE | re.DOTALL)

STOPWORDS = {
    "the", "and", "for", "with", "that", "this", "from", "your", "you",
    "are", "not", "was", "were", "will", "have", "has", "had", "but",
    "all", "any", "can", "how", "what", "when", "where", "why", "who",
    "one", "two", "into", "out", "our", "their", "its", "it's", "them",
    "than", "then", "these", "those", "over", "under", "about", "after",
    "before", "between", "does", "did", "done", "being", "been", "each",
    "every", "more", "most", "other", "some", "such", "only", "own",
    "same", "too", "very", "just", "should", "would", "could", "may",
    "might", "must", "shall", "also", "per", "via", "use", "used",
    "using", "see", "part", "phase", "step", "section", "notes", "note",
    "overview", "summary", "intro", "introduction", "conclusion",
}

MAX_TERMS = 60

WEIGHTS = {"explicit": 3, "heading": 3, "bold": 2, "proper-noun": 2, "number": 2}


def clean_phrase(phrase: str) -> str:
    phrase = re.sub(r"[`*_#>\[\]()|]", " ", phrase)
    phrase = re.sub(r"\s+", " ", phrase).strip(" .,:;—–-")
    return phrase


def content_words(phrase: str) -> list:
    return [w for w in re.findall(r"[A-Za-z][A-Za-z'&.-]{2,}", phrase)
            if w.lower() not in STOPWORDS]


def extract_terms(anchor_text: str, explicit_terms: list) -> list:
    """Return list of {term, kind, weight}, deduped by lowercase term."""
    body = FENCE_RE.sub(" ", anchor_text)
    # strip frontmatter
    if body.startswith("---"):
        end = body.find("\n---", 3)
        if end != -1:
            body = body[end + 4:]

    candidates = []  # (phrase, kind) in priority order
    for t in explicit_terms:
        candidates.append((t, "explicit"))
    for m in HEADING_RE.finditer(body):
        candidates.append((m.group(1), "heading"))
    for m in BOLD_RE.finditer(body):
        candidates.append((m.group(1) or m.group(2), "bold"))
    for line in body.splitlines():  # per-line so sequences never span lines
        for m in PROPER_NOUN_RE.finditer(line):
            candidates.append((m.group(0), "proper-noun"))
    for m in NUMBER_RE.finditer(body):
        candidates.append((m.group(0), "number"))

    seen = set()
    terms = []
    for phrase, kind in candidates:
        phrase = clean_phrase(phrase)
        if kind != "number" and not content_words(phrase):
            continue
        if len(phrase) < 3:
            continue
        key = phrase.lower()
        if key in seen:
            continue
        seen.add(key)
        terms.append({"term": phrase, "kind": kind, "weight": WEIGHTS[kind]})
        if len(terms) >= MAX_TERMS:
            break
    return terms


# ── Coverage check ───────────────────────────────────────────

def load_target_text(path: Path) -> str:
    if path.is_dir():
        parts = []
        for f in sorted(path.rglob("*")):
            if f.is_file() and f.suffix.lower() in {".md", ".txt", ".yaml", ".yml", ".html"}:
                parts.append(f.read_text(encoding="utf-8", errors="replace"))
        return "\n".join(parts)
    return path.read_text(encoding="utf-8", errors="replace")


def term_covered(term: str, kind: str, haystack_lower: str) -> bool:
    t = term.lower()
    if t in haystack_lower:
        return True
    if kind == "number":
        return False
    words = [w.lower() for w in content_words(term)]
    if not words:
        return False
    # partial credit rule: a multi-word term counts if all its content
    # words appear somewhere in the target (propagated but rephrased)
    return all(w in haystack_lower for w in words)


def score_target(path: Path, terms: list) -> dict:
    text_lower = load_target_text(path).lower()
    total_w = sum(t["weight"] for t in terms) or 1
    covered_w = 0
    missing = []
    for t in terms:
        if term_covered(t["term"], t["kind"], text_lower):
            covered_w += t["weight"]
        else:
            missing.append(f"{t['term']} ({t['kind']})")
    coverage = covered_w / total_w
    score = max(1, min(10, round(1 + 9 * coverage)))
    return {
        "target": str(path),
        "score": score,
        "coverage_pct": round(coverage * 100, 1),
        "missing_terms": missing,
    }


def cmd_check(args) -> int:
    anchor = Path(args.anchor)
    if not anchor.is_file():
        print(f"anchor_verify: anchor not found: {anchor}", file=sys.stderr)
        return 2

    explicit = [t.strip() for t in (args.terms or "").split(",") if t.strip()]
    terms = extract_terms(anchor.read_text(encoding="utf-8", errors="replace"),
                          explicit)
    if not terms:
        print("anchor_verify: no key terms extractable from anchor "
              "(add --terms \"a,b,c\")", file=sys.stderr)
        return 2

    targets = []
    for t in args.targets:
        p = Path(t)
        if not p.exists():
            print(f"anchor_verify: target not found: {p}", file=sys.stderr)
            return 2
        targets.append(p)

    results = [score_target(p, terms) for p in targets]
    overall = max(1, min(10, round(sum(r["score"] for r in results) / len(results))))
    passed = overall >= args.min_score

    report = {
        "anchor": str(anchor),
        "terms_extracted": len(terms),
        "terms": [t["term"] for t in terms],
        "targets": results,
        "overall_score": overall,
        "min_score": args.min_score,
        "result": "PASS" if passed else "FAIL",
    }

    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print(f"ANCHOR VERIFY — anchor: {anchor}")
        print(f"  key terms extracted: {len(terms)}")
        for r in results:
            print(f"\n  target: {r['target']}")
            print(f"    propagation score: {r['score']}/10 "
                  f"(coverage {r['coverage_pct']}%)")
            if r["missing_terms"]:
                print(f"    missing anchor terms ({len(r['missing_terms'])}):")
                for m in r["missing_terms"][:15]:
                    print(f"      - {m}")
                if len(r["missing_terms"]) > 15:
                    print(f"      … +{len(r['missing_terms']) - 15} more")
        print(f"\nOVERALL: {overall}/10 (gate: >= {args.min_score})")
        print(f"RESULT: {report['result']}")
        if not passed:
            print("Fix: re-inject the missing anchor terms into the dependent "
                  "phase's prompt verbatim and regenerate, then re-run.")

    return 0 if passed else 1


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Grep dependent deliverables for anchor key-term coverage; "
                    "return a propagation score 1-10 per target.")
    sub = parser.add_subparsers(dest="command", required=True)

    p_check = sub.add_parser("check", help="Score anchor propagation.")
    p_check.add_argument("--anchor", required=True,
                         help="Path to the anchor file (source of key terms).")
    p_check.add_argument("--targets", required=True, nargs="+",
                         help="Dependent deliverable files or directories.")
    p_check.add_argument("--terms", default="",
                         help="Explicit extra key terms, comma-separated.")
    p_check.add_argument("--min-score", type=int, default=7,
                         help="Gate threshold for overall score (default 7).")
    p_check.add_argument("--json", action="store_true")

    args = parser.parse_args()
    if args.command == "check":
        return cmd_check(args)
    return 2


if __name__ == "__main__":
    sys.exit(main())
