#!/usr/bin/env python3
"""Deterministic helper for auditing attention-hijack hook candidates."""

from __future__ import annotations

import argparse
import json
import math
import re
import sys
from dataclasses import asdict, dataclass
from pathlib import Path


PLATFORM_WIDTH = {
    "linkedin": 110.0,
    "x": 130.0,
    "threads": 130.0,
    "newsletter": 150.0,
    "script": 120.0,
    "ad": 120.0,
    "carousel": 95.0,
    "landing": 160.0,
}


THROAT_CLEARING = re.compile(
    r"\b(i('ve| have)? been thinking|here'?s (what|why|how|the thing)|in today'?s|"
    r"let'?s talk about|quick reminder|friendly reminder|in this post)\b",
    re.IGNORECASE,
)


CONTRAST_MARKERS = {
    "but",
    "however",
    "instead",
    "versus",
    "vs",
    "while",
    "actually",
    "changed",
    "shifted",
    "before",
    "after",
    "wrong",
    "mistake",
    "problem",
    "kills",
    "dies",
    "cost",
    "risk",
    "gap",
}


@dataclass
class HookAudit:
    hook: str
    platform: str
    format: str
    word_count: int
    first_50_words: str
    estimated_width: float
    estimated_mobile_lines: int
    topical_terms_found: list[str]
    gap_score: int
    specificity_score: int
    throat_clearing: bool
    verdict: str
    recommendations: list[str]


def load_text(args: argparse.Namespace) -> str:
    if args.hook:
        return args.hook
    if args.draft:
        return Path(args.draft).read_text(encoding="utf-8", errors="ignore")
    return sys.stdin.read()


def words(text: str) -> list[str]:
    return re.findall(r"[A-Za-z0-9][A-Za-z0-9'%-]*", text)


def char_width(ch: str) -> float:
    if ch in "ilI.,'!|":
        return 0.35
    if ch in "mwMW@#%&":
        return 1.7
    if ch in " ":
        return 0.45
    if ch.isupper():
        return 1.15
    if ch.isdigit():
        return 0.95
    return 0.85


def estimate_width(text: str) -> float:
    return sum(char_width(ch) for ch in text)


def nonempty_lines(text: str) -> list[str]:
    return [line.strip() for line in text.splitlines() if line.strip()]


def has_blank_break(text: str) -> bool:
    return bool(re.search(r"\n\s*\n", text))


def classify_format(text: str) -> str:
    lines = nonempty_lines(text)
    word_count = len(words(text))
    if len(lines) == 1:
        if word_count <= 12:
            return "single-line-bomb"
        return "dense"
    if has_blank_break(text) and len(lines) == 2:
        return "punchy-plus-context"
    if len(lines) >= 3:
        starts = [re.sub(r"[^A-Za-z0-9]+.*", "", line).lower() for line in lines[:4]]
        repeated_start = len(starts) != len(set(starts))
        similar_lengths = max(len(line) for line in lines[:4]) - min(len(line) for line in lines[:4]) <= 24
        if repeated_start or similar_lengths:
            return "stacked"
    return "hybrid"


def score_gap(text: str) -> int:
    lower = text.lower()
    score = 0
    markers = sum(1 for marker in CONTRAST_MARKERS if re.search(rf"\b{re.escape(marker)}\b", lower))
    score += min(4, markers)
    if "?" in text:
        score += 1
    if re.search(r"\b\d+([,.]\d+)?(%|x|k|m)?\b", lower):
        score += 1
    if re.search(r"\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b", text):
        score += 1
    if re.search(r"\byou|your|reader|client|customer|founder|team|buyer\b", lower):
        score += 1
    if re.search(r"\b(no one|most people|everyone|nobody|nothing|never|always)\b", lower):
        score += 1
    if re.search(r"\b(because|so|which means|that means)\b", lower):
        score += 1
    return min(10, score)


def score_specificity(text: str, term_hits: list[str]) -> int:
    score = 0
    if re.search(r"\b\d+([,.]\d+)?(%|x|k|m)?\b", text.lower()):
        score += 2
    if re.search(r"\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b", text):
        score += 2
    score += min(3, len(term_hits))
    if re.search(r"\b(algorithm|platform|reader|mobile|hook|brand|news|draft|offer|proof|client)\b", text.lower()):
        score += 1
    if len(words(text)) <= 50:
        score += 1
    if not THROAT_CLEARING.search(text):
        score += 1
    return min(10, score)


def term_hits(text: str, terms: str) -> list[str]:
    hits: list[str] = []
    for raw in terms.split(","):
        term = raw.strip()
        if not term:
            continue
        if re.search(rf"\b{re.escape(term)}\b", text, re.IGNORECASE):
            hits.append(term)
    return hits


def recommendations(audit: HookAudit) -> list[str]:
    recs: list[str] = []
    if audit.throat_clearing:
        recs.append("Cut throat-clearing before the first claim.")
    if audit.gap_score < 5:
        recs.append("Make the expectation-versus-claim gap explicit.")
    if audit.specificity_score < 5:
        recs.append("Add a concrete name, number, proof object, reader, or consequence.")
    if audit.platform == "linkedin" and audit.estimated_mobile_lines > 3 and audit.format in {"dense", "hybrid"}:
        recs.append("Compress for the LinkedIn mobile fold or switch to Punchy plus Context.")
    if audit.platform == "linkedin" and audit.word_count > 50:
        recs.append("Move semantic signal and curiosity into the first 40 to 50 words.")
    if audit.format == "single-line-bomb" and audit.gap_score < 8:
        recs.append("Do not spend the whole first screen on one sentence unless the line is unusually strong.")
    if not audit.topical_terms_found:
        recs.append("Add at least one platform/topic term so the hook is not generic.")
    return recs


def audit_hook(text: str, platform: str, terms: str) -> HookAudit:
    clean = text.strip()
    platform_key = platform.lower()
    width_budget = PLATFORM_WIDTH.get(platform_key, PLATFORM_WIDTH["linkedin"])
    first_words = words(clean)[:50]
    first_50 = " ".join(first_words)
    width = estimate_width(first_50 or clean)
    lines = max(1, math.ceil(width / width_budget))
    hits = term_hits(clean, terms)
    fmt = classify_format(clean)
    gap = score_gap(clean)
    spec = score_specificity(clean, hits)
    throat = bool(THROAT_CLEARING.search(clean))

    provisional = HookAudit(
        hook=clean,
        platform=platform_key,
        format=fmt,
        word_count=len(words(clean)),
        first_50_words=first_50,
        estimated_width=round(width, 1),
        estimated_mobile_lines=lines,
        topical_terms_found=hits,
        gap_score=gap,
        specificity_score=spec,
        throat_clearing=throat,
        verdict="PASS",
        recommendations=[],
    )
    recs = recommendations(provisional)
    verdict = "PASS" if not recs else "REVISE"
    provisional.verdict = verdict
    provisional.recommendations = recs
    return provisional


def render_markdown(audit: HookAudit) -> str:
    lines = [
        "# Attention Hijack Hook Audit",
        "",
        f"- **Verdict**: {audit.verdict}",
        f"- **Platform**: {audit.platform}",
        f"- **Detected format**: {audit.format}",
        f"- **Words**: {audit.word_count}",
        f"- **Estimated first-window width**: {audit.estimated_width}",
        f"- **Estimated mobile lines**: {audit.estimated_mobile_lines}",
        f"- **Gap score**: {audit.gap_score}/10",
        f"- **Specificity score**: {audit.specificity_score}/10",
        f"- **Topical terms found**: {', '.join(audit.topical_terms_found) or 'none'}",
        f"- **Throat clearing**: {'yes' if audit.throat_clearing else 'no'}",
        "",
        "## First 50 Words",
        audit.first_50_words or "(none)",
        "",
        "## Recommendations",
    ]
    if audit.recommendations:
        lines.extend(f"- {item}" for item in audit.recommendations)
    else:
        lines.append("- Keep. The hook has enough signal, gap, and first-window fit for the selected platform.")
    return "\n".join(lines) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit attention-hijack hook candidates.")
    parser.add_argument("--hook", help="Hook text to audit.")
    parser.add_argument("--draft", help="Path to a draft file. The full text will be audited as the opening.")
    parser.add_argument("--platform", default="linkedin", help="Platform: linkedin, x, threads, newsletter, script, ad, carousel, landing.")
    parser.add_argument("--terms", default="", help="Comma-separated topical terms expected in the hook.")
    parser.add_argument("--json", action="store_true", help="Emit JSON instead of Markdown.")
    args = parser.parse_args()

    text = load_text(args)
    if not text.strip():
        parser.error("provide --hook, --draft, or stdin text")

    audit = audit_hook(text, args.platform, args.terms)
    if args.json:
        print(json.dumps(asdict(audit), indent=2))
    else:
        print(render_markdown(audit), end="")
    return 0 if audit.verdict == "PASS" else 2


if __name__ == "__main__":
    raise SystemExit(main())
