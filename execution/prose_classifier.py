#!/usr/bin/env python3
"""
Prose Classifier — Automated AI-prose detection for Antigravity.

The quality gate caps Expert Standard at 6 if prose reads AI-generated.
This script automates that check using pattern-based detection.

Detection signals:
    1. Banned vocabulary (delve, tapestry, landscape, leverage, robust, etc.)
    2. Sentence rhythm uniformity (AI tends toward uniform length)
    3. Hedging density (AI over-qualifies with "arguably", "potentially", etc.)
    4. Parallel structure overuse (AI loves lists of 3 with identical grammar)
    5. Transition phrase density (AI uses "furthermore", "moreover" excessively)
    6. Adjective stacking (AI loves compound modifiers: "comprehensive, strategic")
    7. Empty opener patterns ("In the world of...", "When it comes to...")

Scoring:
    0-2 signals: CLEAN — passes prose check
    3-4 signals: WARNING — review for AI patterns
    5+ signals:  FLAGGED — prose reads AI-generated, Expert Standard capped at 6

Usage:
    from execution.prose_classifier import classify_prose, quick_check

CLI:
    python execution/prose_classifier.py check <file_path>
    python execution/prose_classifier.py check --text "paste text here"
    python execution/prose_classifier.py scan <directory>
"""

import re
import math
import argparse
from pathlib import Path
from typing import Dict, List, Any, Tuple
from collections import Counter


# ── Detection Patterns ───────────────────────────────────────

# Tier 1: Banned vocabulary (from quality_gate.md)
BANNED_WORDS = [
    "delve", "tapestry", "landscape", "leverage", "robust",
    "multifaceted", "comprehensive", "nuanced", "paradigm",
    "synergy", "holistic", "transformative", "groundbreaking",
    "cutting-edge", "game-changing", "unparalleled", "myriad",
    "plethora", "foster", "cultivate", "harness", "spearhead",
    "streamline", "embark", "navigate", "unlock", "elevate",
    "empower", "reimagine", "revolutionize",
]

# Tier 2: AI hedging phrases
HEDGING_PHRASES = [
    r"\bargually\b", r"\bpotentially\b", r"\bit'?s worth noting\b",
    r"\bit'?s important to\b", r"\bit should be noted\b",
    r"\bin many ways\b", r"\bto some extent\b", r"\bvarious\b",
    r"\bnumerous\b", r"\bsignificant\b", r"\bsubstantial\b",
    r"\bfundamentally\b", r"\binherently\b", r"\bultimately\b",
    r"\bessentially\b", r"\bin essence\b",
]

# Tier 3: AI transition phrases
AI_TRANSITIONS = [
    r"\bfurthermore\b", r"\bmoreover\b", r"\badditionally\b",
    r"\bin addition\b", r"\bthat being said\b", r"\bthat said\b",
    r"\bwith that in mind\b", r"\bhaving said that\b",
    r"\bin this regard\b", r"\bin conclusion\b", r"\bto summarize\b",
    r"\bin summary\b", r"\ball in all\b",
]

# Tier 4: Empty openers
EMPTY_OPENERS = [
    r"^in the (?:world|realm|landscape|arena) of\b",
    r"^when it comes to\b",
    r"^in today'?s (?:fast-paced|digital|modern|ever-changing)\b",
    r"^(?:as we all know|it goes without saying)\b",
    r"^the (?:importance|significance|value|power) of\b",
    r"^(?:have you ever wondered|imagine a world)\b",
]

# Tier 5: Adjective stacking (AI loves "comprehensive, strategic, data-driven")
ADJECTIVE_STACK_PATTERN = r'\b\w+(?:ive|ful|ous|ent|ant|tic|al),\s+\w+(?:ive|ful|ous|ent|ant|tic|al)\b'


def _split_sentences(text: str) -> List[str]:
    """Split text into sentences."""
    # Simple sentence splitting
    sentences = re.split(r'(?<=[.!?])\s+', text)
    return [s.strip() for s in sentences if s.strip() and len(s.strip()) > 5]


def _check_banned_vocab(text: str) -> Tuple[int, List[str]]:
    """Check for banned AI vocabulary."""
    text_lower = text.lower()
    found = []
    for word in BANNED_WORDS:
        pattern = r'\b' + re.escape(word) + r'\b'
        matches = re.findall(pattern, text_lower)
        if matches:
            found.extend([word] * len(matches))
    return len(found), found


def _check_hedging(text: str) -> Tuple[int, List[str]]:
    """Check for AI hedging phrases."""
    text_lower = text.lower()
    found = []
    for pattern in HEDGING_PHRASES:
        matches = re.findall(pattern, text_lower)
        if matches:
            found.extend(matches)
    return len(found), found


def _check_transitions(text: str) -> Tuple[int, List[str]]:
    """Check for AI transition overuse."""
    text_lower = text.lower()
    found = []
    for pattern in AI_TRANSITIONS:
        matches = re.findall(pattern, text_lower)
        if matches:
            found.extend(matches)
    return len(found), found


def _check_empty_openers(text: str) -> Tuple[int, List[str]]:
    """Check for empty opener patterns."""
    lines = text.split('\n')
    found = []
    for line in lines:
        line_lower = line.strip().lower()
        for pattern in EMPTY_OPENERS:
            if re.match(pattern, line_lower):
                found.append(line.strip()[:60])
    return len(found), found


def _check_rhythm_uniformity(text: str) -> Tuple[float, str]:
    """
    Check sentence length uniformity.
    AI tends to write sentences of similar length.
    Human writing has more variance.

    Returns coefficient of variation (lower = more uniform = more AI-like)
    """
    sentences = _split_sentences(text)
    if len(sentences) < 5:
        return 0.5, "insufficient_data"

    lengths = [len(s.split()) for s in sentences]
    mean = sum(lengths) / len(lengths)
    if mean == 0:
        return 0.5, "empty"

    variance = sum((l - mean) ** 2 for l in lengths) / len(lengths)
    std_dev = math.sqrt(variance)
    cv = std_dev / mean  # Coefficient of variation

    # CV < 0.3 = very uniform (AI-like)
    # CV 0.3-0.5 = moderate (could be either)
    # CV > 0.5 = varied (more human-like)
    if cv < 0.3:
        return cv, "uniform_ai_pattern"
    elif cv < 0.5:
        return cv, "moderate"
    else:
        return cv, "varied_human_pattern"


def _check_adjective_stacking(text: str) -> Tuple[int, List[str]]:
    """Check for AI-typical adjective stacking."""
    matches = re.findall(ADJECTIVE_STACK_PATTERN, text, re.IGNORECASE)
    return len(matches), matches


def _check_parallel_structure(text: str) -> Tuple[int, str]:
    """
    Check for excessive parallel structure in lists.
    AI loves starting consecutive items with the same pattern.
    """
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    parallel_count = 0

    for i in range(len(lines) - 2):
        # Check if 3+ consecutive lines start with the same word/pattern
        first_words = [lines[j].split()[0].lower() if lines[j].split() else "" for j in range(i, min(i+3, len(lines)))]
        if len(set(first_words)) == 1 and first_words[0]:
            parallel_count += 1

    detail = f"{parallel_count} parallel blocks found"
    return parallel_count, detail


def classify_prose(text: str) -> Dict[str, Any]:
    """
    Classify text for AI-prose patterns.

    Returns:
        Dict with:
            - verdict: CLEAN | WARNING | FLAGGED
            - score: 0-10 (higher = more AI-like)
            - signals: List of detected patterns
            - recommendation: What to fix
    """
    word_count = len(text.split())
    signals = []

    # Run all checks
    banned_count, banned_words = _check_banned_vocab(text)
    hedge_count, hedge_words = _check_hedging(text)
    transition_count, transition_words = _check_transitions(text)
    opener_count, opener_words = _check_empty_openers(text)
    rhythm_cv, rhythm_verdict = _check_rhythm_uniformity(text)
    adj_count, adj_stacks = _check_adjective_stacking(text)
    parallel_count, parallel_detail = _check_parallel_structure(text)

    # Score each signal (normalized by text length)
    words_per_signal = max(word_count / 100, 1)  # Normalize per 100 words

    if banned_count > 0:
        severity = min(banned_count / words_per_signal, 3)
        signals.append({
            "type": "banned_vocabulary",
            "severity": round(severity, 1),
            "count": banned_count,
            "examples": list(set(banned_words))[:5],
        })

    if hedge_count > 2:
        severity = min(hedge_count / words_per_signal, 3)
        signals.append({
            "type": "hedging_phrases",
            "severity": round(severity, 1),
            "count": hedge_count,
            "examples": list(set(hedge_words))[:5],
        })

    if transition_count > 2:
        severity = min(transition_count / words_per_signal, 3)
        signals.append({
            "type": "ai_transitions",
            "severity": round(severity, 1),
            "count": transition_count,
            "examples": list(set(transition_words))[:5],
        })

    if opener_count > 0:
        signals.append({
            "type": "empty_openers",
            "severity": min(opener_count * 1.5, 3),
            "count": opener_count,
            "examples": opener_words[:3],
        })

    if rhythm_verdict == "uniform_ai_pattern":
        signals.append({
            "type": "rhythm_uniformity",
            "severity": 2.0,
            "detail": f"CV={rhythm_cv:.2f} — sentences are suspiciously similar length",
        })

    if adj_count > 1:
        severity = min(adj_count / words_per_signal, 2)
        signals.append({
            "type": "adjective_stacking",
            "severity": round(severity, 1),
            "count": adj_count,
            "examples": adj_stacks[:3],
        })

    if parallel_count > 2:
        signals.append({
            "type": "parallel_structure_overuse",
            "severity": min(parallel_count * 0.5, 2),
            "detail": parallel_detail,
        })

    # Calculate overall score
    total_severity = sum(s.get("severity", 0) for s in signals)
    ai_score = min(round(total_severity, 1), 10)

    # Determine verdict
    if ai_score < 2:
        verdict = "CLEAN"
        recommendation = "Prose passes the AI-detection check. Expert Standard scoring is uncapped."
    elif ai_score < 4:
        verdict = "WARNING"
        fixes = []
        for s in signals:
            if s["type"] == "banned_vocabulary":
                fixes.append(f"Replace banned words: {', '.join(s['examples'])}")
            elif s["type"] == "hedging_phrases":
                fixes.append("Remove hedging — state claims directly")
            elif s["type"] == "ai_transitions":
                fixes.append("Cut transition phrases — let ideas flow naturally")
            elif s["type"] == "empty_openers":
                fixes.append("Delete empty openers — start with the point")
            elif s["type"] == "rhythm_uniformity":
                fixes.append("Vary sentence length — mix short punches with longer builds")
        recommendation = "Review these before finalizing: " + "; ".join(fixes)
    else:
        verdict = "FLAGGED"
        recommendation = (
            "This prose reads AI-generated. Expert Standard capped at 6. "
            "Rewrite with: shorter sentences, active voice, specific details over abstractions, "
            "and the expert's actual vocabulary (not AI vocabulary)."
        )

    return {
        "verdict": verdict,
        "ai_score": ai_score,
        "word_count": word_count,
        "signal_count": len(signals),
        "signals": signals,
        "recommendation": recommendation,
        "rhythm_cv": round(rhythm_cv, 2),
    }


def quick_check(text: str) -> str:
    """Quick one-line verdict for inline use."""
    result = classify_prose(text)
    return f"[{result['verdict']}] AI Score: {result['ai_score']}/10 — {result['signal_count']} signals"


def should_cap_expert_standard(text: str) -> Tuple[bool, Dict[str, Any]]:
    """Public interface for chain_runner._enforce_caps.

    Returns (cap_required, details). cap_required is True iff classifier
    verdict is FLAGGED (ai_score >= 4, per the existing threshold). WARNING
    tier stays advisory — precision over recall, because false positives
    would cap legitimate human-edited prose. Cap fires only when the
    classifier is confident the prose reads AI-generated.

    Details dict carries the full classify_prose return so callers can
    populate audit trails without re-running the classifier.
    """
    if not text or len(text.split()) < 50:
        return False, {
            "reason": "text_too_short",
            "word_count": len(text.split()) if text else 0,
        }
    try:
        result = classify_prose(text)
    except Exception as e:
        return False, {"reason": "classifier_error", "error": str(e)}
    cap_required = result["verdict"] == "FLAGGED"
    return cap_required, result


# ── CLI ─────────────────────────────────────────────────────
def main():
    parser = argparse.ArgumentParser(description="Prose Classifier — AI-prose detection")
    sub = parser.add_subparsers(dest="command")

    # check
    check_cmd = sub.add_parser("check", help="Check a file or text for AI patterns")
    check_cmd.add_argument("file_path", nargs="?", help="Path to file to check")
    check_cmd.add_argument("--text", default="", help="Text to check directly")

    # scan
    scan_cmd = sub.add_parser("scan", help="Scan a directory of files")
    scan_cmd.add_argument("directory", help="Directory to scan")
    scan_cmd.add_argument("--ext", default=".md", help="File extension filter")

    args = parser.parse_args()

    if args.command == "check":
        if args.text:
            text = args.text
        elif args.file_path:
            text = Path(args.file_path).read_text()
        else:
            parser.error("Provide either a file path or --text")
            return

        result = classify_prose(text)

        print(f"\n{'='*60}")
        print(f"  PROSE CLASSIFICATION")
        print(f"{'='*60}")
        print(f"  Verdict:    {result['verdict']}")
        print(f"  AI Score:   {result['ai_score']}/10")
        print(f"  Words:      {result['word_count']}")
        print(f"  Signals:    {result['signal_count']}")
        print(f"  Rhythm CV:  {result['rhythm_cv']} ({'uniform' if result['rhythm_cv'] < 0.3 else 'varied'})")

        if result['signals']:
            print(f"\n  DETECTED PATTERNS:")
            for s in result['signals']:
                examples = s.get('examples', [])
                detail = s.get('detail', '')
                info = f" — {', '.join(examples)}" if examples else f" — {detail}" if detail else ""
                print(f"    [{s['severity']:.1f}] {s['type']}{info}")

        print(f"\n  {result['recommendation']}")
        print(f"{'='*60}\n")

    elif args.command == "scan":
        directory = Path(args.directory)
        files = list(directory.rglob(f"*{args.ext}"))

        print(f"\n{'='*60}")
        print(f"  PROSE SCAN — {len(files)} files")
        print(f"{'='*60}\n")

        flagged = []
        warnings = []

        for f in files:
            try:
                text = f.read_text()
                if len(text.split()) < 50:
                    continue
                result = classify_prose(text)
                if result['verdict'] == 'FLAGGED':
                    flagged.append((f.name, result['ai_score']))
                elif result['verdict'] == 'WARNING':
                    warnings.append((f.name, result['ai_score']))
            except Exception:
                continue

        if flagged:
            print(f"  FLAGGED ({len(flagged)}):")
            for name, score in sorted(flagged, key=lambda x: -x[1]):
                print(f"    {name}: AI Score {score}/10")

        if warnings:
            print(f"\n  WARNINGS ({len(warnings)}):")
            for name, score in sorted(warnings, key=lambda x: -x[1]):
                print(f"    {name}: AI Score {score}/10")

        if not flagged and not warnings:
            print("  All files CLEAN.")

        print(f"\n{'='*60}\n")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
