"""
Cross-Platform Contract Matcher — AI + Rules hybrid matching engine.

Matches prediction market contracts across Polymarket and Kalshi to detect
cross-platform arbitrage opportunities. This is the hardest problem in the
system: only ~15-20% of similar-looking cross-platform pairs are true 1:1
matches suitable for risk-free arbitrage. The rest have material differences.

Documented false-match disasters:
  - Bitcoin Reserve (2025): Kalshi "before Jan 1 2026" vs Polymarket "during 2025"
    → Same event, different time boundaries, opposite resolutions possible
  - Government Shutdown: Polymarket resolved Yes (OPM announcement), Kalshi No
    (didn't exceed 24h) → Same event, different outcome definitions
  - Super Bowl Halftime: $47.3M in disputed settlement on Kalshi

3-Stage Matching Pipeline:
  Stage 1: CANDIDATE GENERATION (rules-based, fast)
    Text similarity + category + date overlap → candidate pairs
  Stage 2: STRUCTURED COMPARISON (rules-based, medium)
    Resolution source, time boundaries, outcome definitions
  Stage 3: LLM VERIFICATION (AI, slow, only for candidates)
    Claude analyzes both contracts for functional equivalence

Confidence Scoring (5 dimensions):
  Text similarity (20%) + Resolution source (25%) + Time window (20%)
  + Outcome structure (20%) + Category match (15%)

Hard gate: Resolution source mismatch caps confidence at 0.75 regardless
of other dimensions. This is where the disasters happened.
"""

import json
import logging
import os
import re
from datetime import datetime, timezone
from difflib import SequenceMatcher
from typing import Optional

from projects.prediction_market_arb.models import (
    CrossPlatformMatch, KalshiMarket, Market, Opportunity,
    StrategyType, EdgeType, Platform,
)
from projects.prediction_market_arb.constants import CROSS_PLATFORM_FEE_DRAG

logger = logging.getLogger("polymarket.matcher")


# =============================================================================
# STAGE 1: CANDIDATE GENERATION (fast, rules-based)
# =============================================================================

def _normalize_text(text: str) -> str:
    """Normalize market question/title for comparison."""
    text = text.lower().strip()
    # Remove common prefixes
    for prefix in ["will ", "will the ", "is ", "does "]:
        if text.startswith(prefix):
            text = text[len(prefix):]
    # Remove punctuation
    text = re.sub(r'[?!.,;:\'"()]', '', text)
    # Normalize whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    return text


def _text_similarity(text_a: str, text_b: str) -> float:
    """Calculate text similarity between two market questions."""
    norm_a = _normalize_text(text_a)
    norm_b = _normalize_text(text_b)

    # SequenceMatcher for overall similarity
    seq_ratio = SequenceMatcher(None, norm_a, norm_b).ratio()

    # Keyword overlap (important words only, >3 chars)
    words_a = {w for w in norm_a.split() if len(w) > 3}
    words_b = {w for w in norm_b.split() if len(w) > 3}
    if words_a and words_b:
        jaccard = len(words_a & words_b) / len(words_a | words_b)
    else:
        jaccard = 0.0

    # Weighted blend
    return 0.6 * seq_ratio + 0.4 * jaccard


def generate_candidates(poly_markets: list, kalshi_markets: list[KalshiMarket],
                        min_similarity: float = 0.45) -> list[tuple]:
    """
    Stage 1: Fast candidate generation via text similarity.

    Compares every Polymarket market against every Kalshi market.
    Returns list of (poly_market, kalshi_market, text_similarity) tuples
    that exceed the minimum similarity threshold.
    """
    candidates = []

    for pm in poly_markets:
        pm_question = pm.question if hasattr(pm, 'question') else pm.get("question", "")
        pm_id = pm.id if hasattr(pm, 'id') else pm.get("id", "")
        if not pm_question:
            continue

        for km in kalshi_markets:
            if not km.title:
                continue

            sim = _text_similarity(pm_question, km.title)

            # Also check subtitle if available
            if km.subtitle:
                sub_sim = _text_similarity(pm_question, km.subtitle)
                sim = max(sim, sub_sim)

            if sim >= min_similarity:
                candidates.append((pm, km, sim))

    # Sort by similarity (highest first)
    candidates.sort(key=lambda x: x[2], reverse=True)

    logger.info(f"Stage 1: {len(candidates)} candidates from "
                f"{len(poly_markets)} Poly x {len(kalshi_markets)} Kalshi markets "
                f"(threshold: {min_similarity})")
    return candidates


# =============================================================================
# STAGE 2: STRUCTURED COMPARISON (medium, rules-based)
# =============================================================================

def _parse_datetime(date_str: str) -> Optional[datetime]:
    """Parse ISO datetime string, handling various formats."""
    if not date_str:
        return None
    try:
        # Handle Z suffix
        date_str = date_str.replace("Z", "+00:00")
        return datetime.fromisoformat(date_str)
    except (ValueError, TypeError):
        return None


def _time_window_overlap(poly_end: str, kalshi_end: str) -> tuple[float, float]:
    """
    Compare close/expiration times.
    Returns (overlap_score 0-1, delta_hours).
    """
    dt_poly = _parse_datetime(poly_end)
    dt_kalshi = _parse_datetime(kalshi_end)

    if not dt_poly or not dt_kalshi:
        return 0.5, 0.0  # Unknown — neutral score

    delta = abs((dt_poly - dt_kalshi).total_seconds()) / 3600

    if delta < 1:
        return 1.0, delta        # Within 1 hour — excellent
    elif delta < 6:
        return 0.8, delta        # Within 6 hours — good
    elif delta < 24:
        return 0.5, delta        # Within 24 hours — risky
    else:
        return 0.2, delta        # More than 24 hours — likely different events


def _extract_resolution_hints(text: str) -> set[str]:
    """Extract resolution source hints from market description/rules."""
    text = text.lower()
    sources = set()

    source_patterns = {
        "associated press": "ap",
        " ap ": "ap",
        "ap call": "ap",
        "new york times": "nyt",
        "nyt ": "nyt",
        "official results": "official",
        "official government": "official",
        "federal reserve": "fed",
        "bureau of labor": "bls",
        "bls report": "bls",
        "white house": "whitehouse",
        "coinmarketcap": "cmc",
        "coingecko": "coingecko",
        "uma oracle": "uma",
        "optimistic oracle": "uma",
    }

    for pattern, label in source_patterns.items():
        if pattern in text:
            sources.add(label)

    return sources


def structured_compare(poly_market, kalshi_market: KalshiMarket,
                       text_sim: float) -> CrossPlatformMatch:
    """
    Stage 2: Compare structured fields between matched candidates.

    Checks resolution sources, time windows, outcome structures.
    Returns a CrossPlatformMatch with dimensional scoring.
    """
    pm_question = poly_market.question if hasattr(poly_market, 'question') else poly_market.get("question", "")
    pm_id = poly_market.id if hasattr(poly_market, 'id') else poly_market.get("id", "")
    pm_end = poly_market.end_date if hasattr(poly_market, 'end_date') else poly_market.get("endDate", "")
    pm_volume = poly_market.volume if hasattr(poly_market, 'volume') else float(poly_market.get("volume", 0) or 0)

    # Get prices
    try:
        pm_prices = poly_market.get("outcomePrices", "[0.5,0.5]") if isinstance(poly_market, dict) else "[0.5,0.5]"
        if isinstance(pm_prices, str):
            prices = json.loads(pm_prices)
        else:
            prices = pm_prices
        pm_yes = float(prices[0]) if prices else 0.5
        pm_no = float(prices[1]) if len(prices) > 1 else 1.0 - pm_yes
    except (json.JSONDecodeError, IndexError, TypeError):
        pm_yes = 0.5
        pm_no = 0.5

    # Kalshi prices (normalize cents to 0-1)
    k_yes = kalshi_market.yes_price_normalized
    k_no = kalshi_market.no_price_normalized

    # --- Dimension scores ---

    # 1. Text similarity (from Stage 1)
    text_score = text_sim

    # 2. Resolution source comparison
    poly_sources = _extract_resolution_hints(pm_question)
    kalshi_sources = _extract_resolution_hints(kalshi_market.title + " " + kalshi_market.subtitle)
    resolution_match = bool(poly_sources & kalshi_sources) if poly_sources and kalshi_sources else False
    # If both have identified sources that overlap, high score
    # If sources identified but different, low score (hard gate)
    # If sources unknown, neutral
    if poly_sources and kalshi_sources:
        if poly_sources & kalshi_sources:
            resolution_score = 1.0
        else:
            resolution_score = 0.3  # Known different sources
    else:
        resolution_score = 0.6  # Unknown — neutral but cautious

    # 3. Time window overlap
    time_score, time_delta = _time_window_overlap(pm_end, kalshi_market.end_date)

    # 4. Outcome structure match (both binary = 1.0)
    # Polymarket is always binary yes/no; Kalshi is also binary
    outcome_score = 1.0

    # 5. Category match
    pm_category = ""
    if hasattr(poly_market, 'category'):
        pm_category = poly_market.category
    elif isinstance(poly_market, dict):
        pm_category = poly_market.get("groupItemTitle", "")
    k_category = kalshi_market.category.lower() if kalshi_market.category else ""
    category_score = 0.8 if pm_category.lower() == k_category else 0.4

    # --- Weighted confidence ---
    confidence = (
        0.20 * text_score +
        0.25 * resolution_score +
        0.20 * time_score +
        0.20 * outcome_score +
        0.15 * category_score
    )

    # Hard gate: resolution source mismatch caps at 0.75
    if poly_sources and kalshi_sources and not (poly_sources & kalshi_sources):
        confidence = min(confidence, 0.75)

    # --- Structural flags ---
    flags = []
    if poly_sources and kalshi_sources and not (poly_sources & kalshi_sources):
        flags.append("different_resolution_source")
    if time_delta > 6:
        flags.append(f"time_gap_{time_delta:.0f}h")
    if time_delta > 24:
        flags.append("different_event_timing")

    # --- Price gap ---
    price_gap = pm_yes - k_yes
    price_gap_pct = price_gap / max(k_yes, 0.01)

    # --- Combined fee drag ---
    # Default to politics fee drag (most common cross-platform category)
    combined_fees = CROSS_PLATFORM_FEE_DRAG.get("politics", 0.0275)
    net_edge = abs(price_gap) - combined_fees
    is_actionable = (net_edge > 0 and confidence >= 0.75 and len(flags) == 0)

    match = CrossPlatformMatch(
        poly_market_id=pm_id,
        poly_question=pm_question,
        poly_price_yes=round(pm_yes, 4),
        poly_price_no=round(pm_no, 4),
        poly_volume=pm_volume,
        poly_end_date=pm_end,
        kalshi_ticker=kalshi_market.ticker,
        kalshi_title=kalshi_market.title,
        kalshi_price_yes=round(k_yes, 4),
        kalshi_price_no=round(k_no, 4),
        kalshi_volume=kalshi_market.volume,
        kalshi_end_date=kalshi_market.end_date,
        match_confidence=round(confidence, 4),
        text_similarity=round(text_sim, 4),
        resolution_match=resolution_match,
        time_window_match=(time_delta < 6),
        structural_flags=flags,
        price_gap=round(price_gap, 4),
        price_gap_pct=round(price_gap_pct, 4),
        combined_fee_drag=round(combined_fees, 4),
        net_edge=round(net_edge, 4),
        is_actionable=is_actionable,
        timestamp=datetime.now(timezone.utc).isoformat(),
    )

    return match


# =============================================================================
# STAGE 3: LLM VERIFICATION (slow, AI-assisted, only for top candidates)
# =============================================================================

VERIFICATION_PROMPT = """You are a prediction market contract analyst. Compare these two contracts and determine if they are FUNCTIONALLY IDENTICAL for arbitrage purposes.

CONTRACT A (Polymarket):
Question: {poly_question}
Close time: {poly_end}

CONTRACT B (Kalshi):
Title: {kalshi_title}
Subtitle: {kalshi_subtitle}
Close time: {kalshi_end}

Analyze these dimensions:
1. OUTCOME EQUIVALENCE: Do "Yes" on both platforms mean the same thing?
2. RESOLUTION SOURCE: Do both use the same authority/source to determine outcome?
3. TIME BOUNDARY: Could one resolve Yes while the other hasn't closed yet?
4. EDGE CASES: Is there ANY scenario where these resolve differently?

Output JSON only:
{{"functionally_identical": true/false, "confidence": 0.0-1.0, "differences": ["list"], "risk_scenario": "worst case", "recommendation": "TRADE|REVIEW|REJECT"}}"""


def llm_verify(match: CrossPlatformMatch, kalshi_market: KalshiMarket) -> CrossPlatformMatch:
    """
    Stage 3: Use Claude to verify whether two contracts are functionally identical.

    Only called for high-confidence candidates from Stage 2.
    Updates the match's confidence, flags, and actionability based on LLM analysis.
    """
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key:
        logger.warning("ANTHROPIC_API_KEY not set — skipping LLM verification")
        return match

    prompt = VERIFICATION_PROMPT.format(
        poly_question=match.poly_question,
        poly_end=match.poly_end_date,
        kalshi_title=match.kalshi_title,
        kalshi_subtitle=kalshi_market.subtitle,
        kalshi_end=match.kalshi_end_date,
    )

    try:
        import requests
        resp = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers={
                "x-api-key": api_key,
                "anthropic-version": "2023-06-01",
                "Content-Type": "application/json",
            },
            json={
                "model": "claude-haiku-4-5-20251001",
                "system": "You are a prediction market contract analyst. Respond in JSON only.",
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.1,
                "max_tokens": 500,
            },
            timeout=30,
        )
        resp.raise_for_status()
        content = resp.json()["content"][0]["text"]

        # Parse JSON from response
        if "```" in content:
            content = content.split("```")[1]
            if content.startswith("json"):
                content = content[4:]
        result = json.loads(content.strip())

        # Update match based on LLM analysis
        if not result.get("functionally_identical", False):
            match.structural_flags.append("llm_not_identical")
            if result.get("differences"):
                for diff in result["differences"][:3]:
                    match.structural_flags.append(f"llm: {diff[:50]}")
            match.is_actionable = False

        # Adjust confidence based on LLM
        llm_conf = float(result.get("confidence", 0.5))
        # Blend: 70% structured analysis, 30% LLM
        match.match_confidence = round(
            0.70 * match.match_confidence + 0.30 * llm_conf, 4
        )

        rec = result.get("recommendation", "REVIEW")
        if rec == "REJECT":
            match.is_actionable = False
            match.structural_flags.append("llm_rejected")
        elif rec == "REVIEW":
            match.structural_flags.append("llm_needs_review")

        logger.info(f"LLM verify: {match.poly_question[:40]}... ↔ {match.kalshi_title[:40]}... "
                    f"→ {rec} (conf={llm_conf:.2f})")

    except Exception as e:
        logger.error(f"LLM verification failed: {e}")

    return match


# =============================================================================
# FULL MATCHING PIPELINE
# =============================================================================

class ContractMatcher:
    """
    Cross-platform contract matching engine.

    Runs the 3-stage pipeline: candidate generation → structured comparison
    → LLM verification. Returns scored CrossPlatformMatch objects.
    """

    def __init__(self, config):
        self.config = config
        self.min_confidence = config.cross_platform.min_match_confidence
        self.min_net_edge = config.cross_platform.min_net_edge
        self.max_flags = config.cross_platform.max_structural_flags

    def find_matches(self, poly_markets: list,
                     kalshi_markets: list[KalshiMarket],
                     use_llm: bool = True) -> list[CrossPlatformMatch]:
        """
        Run the full 3-stage matching pipeline.

        Returns list of CrossPlatformMatch objects, sorted by net_edge.
        Only includes matches that pass all filters.
        """
        # Stage 1: Candidate generation
        candidates = generate_candidates(poly_markets, kalshi_markets)
        logger.info(f"Stage 1 complete: {len(candidates)} candidates")

        if not candidates:
            return []

        # Stage 2: Structured comparison
        matches = []
        for pm, km, text_sim in candidates:
            match = structured_compare(pm, km, text_sim)
            matches.append((match, km))

        logger.info(f"Stage 2 complete: {len(matches)} comparisons")

        # Stage 3: LLM verification (only for promising candidates)
        verified = []
        llm_count = 0
        for match, km in matches:
            if match.match_confidence >= 0.60 and use_llm and llm_count < 20:
                match = llm_verify(match, km)
                llm_count += 1
            verified.append(match)

        logger.info(f"Stage 3 complete: {llm_count} LLM verifications")

        # Filter
        results = []
        for match in verified:
            if match.match_confidence < self.min_confidence:
                continue
            if len(match.structural_flags) > self.max_flags:
                continue
            if match.net_edge < self.min_net_edge:
                continue
            results.append(match)

        # Sort by net edge
        results.sort(key=lambda m: m.net_edge, reverse=True)

        logger.info(f"Matching complete: {len(results)} actionable matches "
                    f"from {len(candidates)} candidates")
        return results

    def matches_to_opportunities(self, matches: list[CrossPlatformMatch]) -> list[Opportunity]:
        """Convert CrossPlatformMatch objects to Opportunity format for the market selector."""
        opportunities = []

        for match in matches:
            if not match.is_actionable:
                continue

            # Determine which side to trade
            if match.price_gap > 0:
                # Poly overpriced vs Kalshi → buy on Kalshi, sell on Poly
                our_prob = match.kalshi_price_yes
                market_price = match.poly_price_yes
                platform = Platform.KALSHI.value
            else:
                # Kalshi overpriced → buy on Poly, sell on Kalshi
                our_prob = match.poly_price_yes
                market_price = match.kalshi_price_yes
                platform = Platform.POLYMARKET.value

            opp = Opportunity(
                strategy=StrategyType.CROSS_PLATFORM.value,
                market_id=match.poly_market_id,
                token_id="",
                platform=platform,
                question=f"{match.poly_question} ↔ {match.kalshi_ticker}",
                category=match.category,
                our_probability=round(our_prob, 4),
                market_price=round(market_price, 4),
                edge=round(abs(match.price_gap), 4),
                edge_after_fees=round(match.net_edge, 4),
                ev=round(match.net_edge, 4),
                kelly_f=0.0,  # Cross-platform arb uses fixed sizing, not Kelly
                edge_type=EdgeType.INFORMATION_ASYMMETRY.value,
                reference_source=f"kalshi:{match.kalshi_ticker}",
                confidence=match.match_confidence,
                volume=min(match.poly_volume, match.kalshi_volume),
                context={
                    "poly_market_id": match.poly_market_id,
                    "poly_price": match.poly_price_yes,
                    "kalshi_ticker": match.kalshi_ticker,
                    "kalshi_price": match.kalshi_price_yes,
                    "price_gap": match.price_gap,
                    "match_confidence": match.match_confidence,
                    "structural_flags": match.structural_flags,
                    "combined_fees": match.combined_fee_drag,
                },
                timestamp=datetime.now(timezone.utc).isoformat(),
            )
            opportunities.append(opp)

        return opportunities
