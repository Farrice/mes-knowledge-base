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
    r"\barguably\b", r"\bpotentially\b", r"\bit'?s worth noting\b",
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

# Tier 6: Manufactured-reveal / gatekept-knowledge lead-ins (the "the part nobody..." family).
# These ANNOUNCE the writing instead of doing it. High-confidence formulaic tells — fire on any hit.
# Calibrated on Farrice's rejections (the "Here is the part that should keep you up" / "the quiet part is" tells).
REVEAL_LEADINS = [
    r"\bhere'?s (?:what|why|how)\b",
    r"\bhere'?s the thing\b",
    r"\bhere'?s how \w+ this is\b",
    r"\bthe part (?:nobody|no one) (?:warns|tells|talks)\b",
    r"\bthe (?:quiet|hard|real|scary|uncomfortable) part is\b",
    r"\bthe thing (?:nobody|no one) (?:tells|warns|talks)\b",
    r"\bthe part that should keep you up\b",
    r"\bwhat (?:nobody|no one) (?:tells|warns) you\b",
    r"\bhere'?s what (?:happens when|they don'?t|nobody)\b",
    r"\blet me explain\b",
    r"\bbuckle up\b",
    r"\bplot twist\b",
]

# Tier 7: LinkedIn / creator-genre cliches (formulaic engagement gestures).
LINKEDIN_TROPES = [
    r"\blet that sink in\b",
    r"\bread that again\b",
    r"\bi'?ll wait\b",
    r"\bthis changes everything\b",
    r"\bgame[- ]chang(?:er|ing)\b",
    r"\bwon'?t replace you[,.]? but\b",
    r"\bno longer optional\b",
    r"\bis dead\.?\s+long live\b",
    r"\bmic drop\b",
    r"\bunpopular opinion\b",
    r"\bwe need to talk about\b",
]

# Tier 8: Generic question sign-offs (cheap engagement-bait closers) — checked on the LAST line only.
GENERIC_QUESTION_CLOSE = [
    r"^(?:agree|thoughts|right|yes|no)\?+$",
    r"^what (?:would you add|do you think|are your thoughts|say you)\??$",
    r"^(?:am i wrong|change my mind|who'?s with me|sound familiar)\??$",
    r"\bdrop .{0,30}in the comments\b",
]

# Tier 11: Mascot reveals (the novelty-protect kill-list) — admitting the new frame is the old thing.
MASCOT_REVEALS = [
    r"\bthis is really just\b",
    r"\bas you (?:probably|already) know\b",
    r"\b(?:this )?has been around (?:forever|for decades|for years)\b",
    r"\bto be fair,? this (?:isn'?t|is not) new\b",
    r"\bi'?m no expert,? but\b",
    r"\b(?:this )?might be obvious,? but\b",
    r"\bgrain of salt\b",
    r"\bnothing (?:new|groundbreaking) (?:here|about)\b",
]

# Tier 12: Manufactured-stakes / thriller-cadence lines (unambiguous clichés only — "should scare you"
# in natural relative-clause usage is fine, so it is deliberately excluded).
MANUFACTURED_STAKES = [
    r"\bkeep you up at night\b",
    r"\bsay it louder for the people\b",
]

# Tier 13: Hinge / scene-transition seams.
HINGE_PHRASES = [
    r"\bthat'?s where \w+ comes? in\b",
    r"\blet me break it down\b",
    r"\bwhat does this mean for you\b",
    r"\bare you ready to (?:embrace|adopt|unlock)\b",
    r"\bso,? what does (?:this|that) mean\b",
]

# Tier 14: Current-era (GPT-4o) vocab cluster — fires on OVERUSE (>1), low severity each.
CURRENT_ERA_VOCAB = [
    r"\bensuring\b", r"\bshowcasing\b", r"\bhighlighting\b",
    r"\balign(?:ing|ed)? with\b", r"\bunderscoring\b", r"\bseamless(?:ly)?\b",
]

# Tier 15: Doubled-adjective hedge ("quieter and harder", "stranger and deeper").
DOUBLED_ADJ_HEDGE = r'\b\w+er and (?:harder|deeper|wider|stranger|quieter|colder|darker|softer|sharper)\b'


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


def _check_reveal_leadins(text: str) -> Tuple[int, List[str]]:
    """Manufactured-reveal / gatekept-knowledge lead-ins ('the part nobody warns you about',
    'here's how new this is'). They announce the writing instead of doing it. High-confidence tell."""
    text_lower = text.lower()
    found = []
    for pattern in REVEAL_LEADINS:
        for m in re.findall(pattern, text_lower):
            found.append(m if isinstance(m, str) and m else pattern)
    return len(found), found


def _check_linkedin_tropes(text: str) -> Tuple[int, List[str]]:
    """LinkedIn/creator-genre engagement cliches ('let that sink in', 'game-changer', 'I'll wait')."""
    text_lower = text.lower()
    found = []
    for pattern in LINKEDIN_TROPES:
        if re.search(pattern, text_lower):
            found.append(pattern.strip("\\b").replace("\\", ""))
    return len(found), found


def _check_question_close(text: str) -> Tuple[int, List[str]]:
    """Generic question sign-off on the final non-blank line (the cheap engagement-bait close)."""
    lines = [l.strip() for l in text.split('\n') if l.strip()]
    if not lines:
        return 0, []
    last = lines[-1].lower()
    for pattern in GENERIC_QUESTION_CLOSE:
        if re.search(pattern, last):
            return 1, [lines[-1][:60]]
    # A bare short interrogative as the closer (<=8 words ending in ?) is the generic-question tell.
    if last.endswith('?') and len(last.split()) <= 8:
        return 1, [lines[-1][:60]]
    return 0, []


def _check_em_dashes(text: str) -> Tuple[int, str]:
    """Count em-dashes. Farrice's #1 personal tell; the standard is a hard ceiling of 1-2 per piece."""
    count = len(re.findall(r'—', text))
    return count, f"{count} em-dashes (ceiling is 1-2)"


def _check_contrast_reveal(text: str) -> Tuple[int, List[str]]:
    """The 'It's not X. It's Y.' / 'no longer X; what wins is Y' antithesis MOVE — the banned
    contrast-reveal that survives word-level scans. Detects a negation-claim sentence followed by a
    short counter-assertion, plus the single-sentence semicolon reframe."""
    sentences = _split_sentences(text)
    found = []
    neg = re.compile(r"\b(?:it'?s not|it was not|isn'?t|wasn'?t|no longer)\b", re.IGNORECASE)
    counter = re.compile(r"^(?:it'?s|it was|that'?s|what (?:wins|matters|counts)|the real|instead)\b", re.IGNORECASE)
    for i in range(len(sentences) - 1):
        if neg.search(sentences[i]) and counter.match(sentences[i + 1].strip()):
            found.append(sentences[i][:35] + " || " + sentences[i + 1][:35])
    for s in sentences:
        if re.search(r"\bno longer\b.{0,60};\s*what (?:wins|matters|counts)\b", s, re.IGNORECASE):
            found.append(s[:70])
    return len(found), found


def _split_paragraphs(text: str) -> List[str]:
    """Split into paragraphs on blank lines (fall back to single newlines if there are none)."""
    paras = re.split(r'\n\s*\n', text)
    if len(paras) < 2:
        paras = [p for p in text.split('\n') if p.strip()]
    return [p.strip() for p in paras if p.strip()]


def _scan_patterns(text: str, patterns: List[str]) -> Tuple[int, List[str]]:
    """Generic case-insensitive whole-text scan; returns total match count + matched strings."""
    text_lower = text.lower()
    found = []
    for pattern in patterns:
        for m in re.findall(pattern, text_lower):
            found.append(m if isinstance(m, str) and m.strip() else pattern)
    return len(found), found


def _check_internal_anaphora(text: str) -> Tuple[int, List[str]]:
    """>=3 sentences WITHIN one paragraph sharing the same first word (semantic anaphora the
    line-based _check_parallel_structure misses, e.g. 'She doesn't... She doesn't... She doesn't...')."""
    # Function words are meaningless as anaphora (everyone starts sentences with "the"/"it").
    # The tell is a meaningful repeated SUBJECT ("She doesn't... She doesn't...", "They want...").
    stop = {
        "the", "a", "an", "and", "but", "so", "or", "nor", "yet", "in", "on", "at",
        "of", "to", "for", "as", "if", "then", "there", "here", "it", "this", "that",
        "these", "those", "with", "by", "from", "no", "not", "now", "when",
    }
    found = []
    for para in _split_paragraphs(text):
        sents = _split_sentences(para)
        if len(sents) < 3:
            continue
        firsts = [s.split()[0].lower().strip('.,;:"\'') for s in sents if s.split()]
        for word, n in Counter(firsts).items():
            if n >= 3 and len(word) > 1 and word not in stop:
                found.append(f"'{word}' x{n}")
    return len(found), found


def _check_aphoristic_endings(text: str) -> Tuple[int, List[str]]:
    """Uniform aphoristic-ending rhythm: paragraphs that close on a short punch (<=6 words) after a
    longer sentence. Fires only when >=3 paragraphs do it (the rhythm, not one good punch)."""
    count = 0
    examples = []
    for para in _split_paragraphs(text):
        sents = _split_sentences(para)
        if len(sents) < 2:
            continue
        last, prev = sents[-1], sents[-2]
        if len(last.split()) <= 6 and len(prev.split()) >= 12:
            count += 1
            examples.append(last[:40])
    return count, examples


def _check_gerund_tails(text: str) -> Tuple[int, List[str]]:
    """Sentences ending in a comma + '-ing' significance clause ('..., underscoring its significance')."""
    found = []
    for s in _split_sentences(text):
        if re.search(r',\s+\w+ing\b[^.!?]{0,45}[.!?]?$', s):
            found.append(s[-45:])
    return len(found), found


def _check_micdrop_deflation(text: str) -> Tuple[int, List[str]]:
    """A 1-3 word final paragraph (typographic mic-drop), in a multi-paragraph piece."""
    paras = _split_paragraphs(text)
    if len(paras) > 2 and 1 <= len(paras[-1].split()) <= 3:
        return 1, [paras[-1][:30]]
    return 0, []


def _check_town_crier(text: str) -> Tuple[int, List[str]]:
    """Billboard register: ALL-CAPS runs, hype words, exclamation density (acronyms excluded)."""
    hits = []
    hits += re.findall(r'\b[A-Z]{2,}(?:\s+[A-Z]{2,}){2,}\b', text)
    hits += re.findall(r'\b(?:HUGE|MASSIVE|INSANE|BREAKING)\b', text)
    if re.search(r'\byou NEED to\b', text):
        hits.append('you NEED to')
    excl = text.count('!')
    if excl / max(len(text.split()), 1) * 100 > 1.0:
        hits.append(f'{excl} exclamation marks')
    return len(hits), hits[:5]


def _check_structural_emoji(text: str) -> Tuple[int, List[str]]:
    """Emoji on a markdown header line or at a line-end (structure-as-decoration)."""
    emoji = re.compile(r'[\U0001F000-\U0001FAFF☀-➿←-⇿]')
    found = []
    for line in text.split('\n'):
        ls = line.strip()
        if not ls:
            continue
        if (ls.startswith('#') or ls.startswith('-') or ls.startswith('*')) and emoji.search(ls):
            found.append(ls[:30])
        elif emoji.search(ls[-3:]):
            found.append(ls[-15:])
    return len(found), found


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
    reveal_count, reveal_found = _check_reveal_leadins(text)
    li_count, li_found = _check_linkedin_tropes(text)
    qclose_count, qclose_found = _check_question_close(text)
    emdash_count, emdash_detail = _check_em_dashes(text)
    contrast_count, contrast_found = _check_contrast_reveal(text)
    mascot_count, mascot_found = _scan_patterns(text, MASCOT_REVEALS)
    stakes_count, stakes_found = _scan_patterns(text, MANUFACTURED_STAKES)
    hinge_count, hinge_found = _scan_patterns(text, HINGE_PHRASES)
    era_count, era_found = _scan_patterns(text, CURRENT_ERA_VOCAB)
    dbladj_count = len(re.findall(DOUBLED_ADJ_HEDGE, text, re.IGNORECASE))
    anaphora_count, anaphora_found = _check_internal_anaphora(text)
    aphoristic_count, aphoristic_found = _check_aphoristic_endings(text)
    gerund_count, gerund_found = _check_gerund_tails(text)
    micdrop_count, micdrop_found = _check_micdrop_deflation(text)
    towncrier_count, towncrier_found = _check_town_crier(text)
    semoji_count, semoji_found = _check_structural_emoji(text)

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

    # Tier 6 — manufactured-reveal lead-ins. High-confidence: one is a WARNING, two FLAG.
    if reveal_count > 0:
        signals.append({
            "type": "manufactured_reveal_leadin",
            "severity": min(reveal_count * 2.0, 4),
            "count": reveal_count,
            "examples": list(dict.fromkeys(reveal_found))[:3],
        })

    # Tier 7 — LinkedIn-genre cliches.
    if li_count > 0:
        signals.append({
            "type": "linkedin_genre_cliche",
            "severity": min(li_count * 1.5, 3),
            "count": li_count,
            "examples": li_found[:3],
        })

    # Tier 8 — generic question sign-off (the cheap close).
    if qclose_count > 0:
        signals.append({
            "type": "generic_question_signoff",
            "severity": 1.5,
            "count": qclose_count,
            "examples": qclose_found,
        })

    # Tier 9 — em-dash overuse (ceiling 1-2; fire at 3+).
    if emdash_count > 2:
        signals.append({
            "type": "em_dash_overuse",
            "severity": min((emdash_count - 1) * 0.7, 3),
            "count": emdash_count,
            "detail": emdash_detail,
        })

    # Tier 10 — the "It's not X. It's Y." contrast-reveal antithesis MOVE.
    if contrast_count > 0:
        signals.append({
            "type": "contrast_reveal_antithesis",
            "severity": min(contrast_count * 2.0, 3),
            "count": contrast_count,
            "examples": contrast_found[:2],
        })

    # Tier 11 — mascot reveals (hedge-to-old / false modesty). Near-binary; one is a strong WARNING.
    if mascot_count > 0:
        signals.append({
            "type": "mascot_reveal",
            "severity": min(mascot_count * 3.0, 6),
            "count": mascot_count,
            "examples": mascot_found[:3],
        })

    # Tier 12 — manufactured-stakes thriller cadence.
    if stakes_count > 0:
        signals.append({
            "type": "manufactured_stakes",
            "severity": min(stakes_count * 2.0, 4),
            "count": stakes_count,
            "examples": stakes_found[:3],
        })

    # Tier 13 — hinge / scene-transition seams.
    if hinge_count > 0:
        signals.append({
            "type": "hinge_seam",
            "severity": min(hinge_count * 1.5, 3),
            "count": hinge_count,
            "examples": hinge_found[:3],
        })

    # Tier 14 — current-era vocab cluster (fires only on overuse).
    if era_count > 1:
        signals.append({
            "type": "current_era_vocab",
            "severity": min((era_count - 1) * 1.0, 3),
            "count": era_count,
            "examples": list(dict.fromkeys(era_found))[:4],
        })

    # Tier 15 — doubled-adjective hedge.
    if dbladj_count > 0:
        signals.append({
            "type": "doubled_adjective_hedge",
            "severity": min(dbladj_count * 1.5, 3),
            "count": dbladj_count,
        })

    # Tier 16 — internal anaphora (3+ same-first-word sentences in one paragraph).
    if anaphora_count > 0:
        signals.append({
            "type": "internal_anaphora",
            "severity": min(anaphora_count * 2.0, 3),
            "count": anaphora_count,
            "examples": anaphora_found[:3],
        })

    # Tier 17 — uniform aphoristic paragraph endings (>=3 short punches after long sentences).
    if aphoristic_count >= 3:
        signals.append({
            "type": "aphoristic_endings",
            "severity": min((aphoristic_count - 2) * 1.5, 3),
            "count": aphoristic_count,
            "examples": aphoristic_found[:3],
        })

    # Tier 18 — gerund significance tails.
    if gerund_count > 1:
        signals.append({
            "type": "gerund_significance_tails",
            "severity": min((gerund_count - 1) * 1.5, 3),
            "count": gerund_count,
            "examples": gerund_found[:3],
        })

    # Tier 19 — mic-drop deflation (1-3 word final paragraph).
    if micdrop_count > 0:
        signals.append({
            "type": "micdrop_deflation",
            "severity": 2.0,
            "count": micdrop_count,
            "examples": micdrop_found,
        })

    # Tier 20 — town-crier register.
    if towncrier_count > 0:
        signals.append({
            "type": "town_crier_register",
            "severity": min(towncrier_count * 1.5, 3),
            "count": towncrier_count,
            "examples": towncrier_found[:3],
        })

    # Tier 21 — structural emoji (decoration on headers / line-ends).
    if semoji_count > 0:
        signals.append({
            "type": "structural_emoji",
            "severity": min(semoji_count * 1.5, 3),
            "count": semoji_count,
            "examples": semoji_found[:3],
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
            elif s["type"] == "manufactured_reveal_leadin":
                fixes.append("Cut the reveal lead-in ('the part nobody...', 'here's what/why/how') — state the insight directly")
            elif s["type"] == "contrast_reveal_antithesis":
                fixes.append("Rewrite the 'It's not X. It's Y.' antithesis as one direct claim")
            elif s["type"] == "generic_question_signoff":
                fixes.append("Replace the question sign-off with an image, declaration, or bookend close")
            elif s["type"] == "em_dash_overuse":
                fixes.append("Reduce em-dashes to at most 1-2 per piece")
            elif s["type"] == "linkedin_genre_cliche":
                fixes.append("Cut the LinkedIn cliche ('let that sink in', 'game-changer', 'I'll wait')")
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
