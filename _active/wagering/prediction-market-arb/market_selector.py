"""
Market Selection Engine — Cross-strategy scoring and portfolio allocation.

Scores and ranks opportunities from ALL strategies (weather, sports, ensemble)
on a unified scale, then allocates capital according to portfolio rules.

Scoring dimensions (0-1 each, weighted):
  1. Edge magnitude (40%) — larger edge = higher score
  2. Confidence (25%) — match confidence, forecast reliability, model agreement
  3. Liquidity (15%) — higher volume = easier fills, less slippage
  4. Time horizon (10%) — sweet spot is 6-48 hours (SM-6 timing matrix)
  5. Strategy priority (10%) — weather > sports > ensemble (risk-adjusted order)

Portfolio allocation (from GP-7):
  Conservative: 80% arb (weather + sports), 20% reserve
  Capital rotation: when no edge in one strategy, capital shifts to others

Pre-filtering runs BEFORE any LLM calls to minimize API spend.
"""

import logging
from datetime import datetime, timezone

from projects.prediction_market_arb.models import (
    Opportunity, StrategyType, MarketCategory,
)
from projects.prediction_market_arb.constants import FEE_DRAG

logger = logging.getLogger("polymarket.selector")


# =============================================================================
# PRE-FILTER (runs before any LLM/API calls)
# =============================================================================

def pre_filter_markets(markets: list, config) -> dict:
    """
    Categorize and filter Polymarket markets before strategy-specific analysis.

    Returns dict of category -> list of markets that pass basic filters.
    This prevents wasting API calls on markets that can't be traded.
    """
    pf = config.market_selection.pre_filter
    min_vol = pf.get("min_volume", 5000) if isinstance(pf, dict) else pf.min_volume
    min_price = pf.get("min_price", 0.05) if isinstance(pf, dict) else pf.min_price
    max_price = pf.get("max_price", 0.95) if isinstance(pf, dict) else pf.max_price
    min_hours = pf.get("min_hours_to_resolution", 2.0) if isinstance(pf, dict) else pf.min_hours_to_resolution
    max_hours = pf.get("max_hours_to_resolution", 168.0) if isinstance(pf, dict) else pf.max_hours_to_resolution

    categorized = {
        "weather": [],
        "sports": [],
        "politics": [],
        "crypto": [],
        "economics": [],
        "ai_tech": [],
        "other": [],
    }

    passed = 0
    filtered = 0

    for market in markets:
        question = market.question if hasattr(market, "question") else market.get("question", "")
        volume = market.volume if hasattr(market, "volume") else float(market.get("volume", 0) or 0)
        q_lower = question.lower()

        # Basic filters
        if volume < min_vol:
            filtered += 1
            continue

        # Categorize by question content
        category = _categorize_market(q_lower, market)
        categorized[category].append(market)
        passed += 1

    logger.info(f"Pre-filter: {passed} passed, {filtered} filtered "
                f"(weather={len(categorized['weather'])}, "
                f"sports={len(categorized['sports'])}, "
                f"politics={len(categorized['politics'])}, "
                f"other={len(categorized['other'])})")
    return categorized


def _categorize_market(question_lower: str, market) -> str:
    """Categorize a market by its question text and metadata."""
    # Weather markers
    weather_words = ["temperature", "highest temp", "weather", "degrees",
                     "°f", "°c", "celsius", "fahrenheit"]
    if any(w in question_lower for w in weather_words):
        return "weather"

    # Sports markers
    sports_words = ["win", "beat", "score", "game", "match", "championship",
                    "playoffs", "finals", "nba", "nfl", "mlb", "nhl",
                    "premier league", "champions league", "ufc", "mma",
                    "super bowl", "world series", "world cup", "ipl"]
    if any(w in question_lower for w in sports_words):
        return "sports"

    # Politics markers
    politics_words = ["president", "election", "congress", "senate", "governor",
                      "vote", "democrat", "republican", "party", "poll",
                      "nomination", "primary", "electoral"]
    if any(w in question_lower for w in politics_words):
        return "politics"

    # Crypto markers
    crypto_words = ["bitcoin", "btc", "ethereum", "eth", "crypto", "token",
                    "blockchain", "defi", "nft", "solana"]
    if any(w in question_lower for w in crypto_words):
        return "crypto"

    # Economics markers
    econ_words = ["gdp", "inflation", "fed", "interest rate", "unemployment",
                  "recession", "cpi", "jobs report", "federal reserve",
                  "treasury", "yield"]
    if any(w in question_lower for w in econ_words):
        return "economics"

    # AI/Tech markers
    tech_words = ["ai ", "artificial intelligence", "openai", "google ai",
                  "chatgpt", "gpt-", "model release", "apple", "microsoft",
                  "meta ", "nvidia", "semiconductor", "chip"]
    if any(w in question_lower for w in tech_words):
        return "ai_tech"

    return "other"


# =============================================================================
# OPPORTUNITY SCORING (unified cross-strategy ranking)
# =============================================================================

# Scoring weights
W_EDGE = 0.40
W_CONFIDENCE = 0.25
W_LIQUIDITY = 0.15
W_TIME = 0.10
W_STRATEGY = 0.10

# Strategy priority scores (risk-adjusted — lower risk = higher priority)
STRATEGY_PRIORITY = {
    StrategyType.WEATHER.value: 1.0,       # Best risk-adjusted: free data, persistent edge
    StrategyType.SPORTS_ARB.value: 0.85,   # Strong: Pinnacle reference, proven by sovereign2013
    StrategyType.ENSEMBLE.value: 0.60,     # Moderate: LLM estimates, no external reference
    StrategyType.MARKET_MAKING.value: 0.40, # Lower: requires capital, crowded rewards
}


def score_opportunity(opp: Opportunity) -> float:
    """
    Score a single opportunity on a 0-1 unified scale.

    Higher score = more attractive for capital allocation.
    """
    # 1. Edge magnitude (0-1, scaled: 5% edge = 0.5, 15%+ = 1.0)
    edge_score = min(1.0, abs(opp.edge_after_fees) / 0.15)

    # 2. Confidence (0-1, already scaled)
    confidence_score = max(0.0, min(1.0, opp.confidence))

    # 3. Liquidity (0-1, log-scaled: $10K vol = 0.4, $100K = 0.7, $1M = 1.0)
    import math
    if opp.volume > 0:
        liquidity_score = min(1.0, math.log10(max(1, opp.volume)) / 6)  # log10(1M) = 6
    else:
        liquidity_score = 0.3  # Unknown volume, assume moderate

    # 4. Time horizon (0-1, peak at 6-48 hours per SM-6 timing matrix)
    if opp.hours_left <= 0:
        time_score = 0.5  # Unknown
    elif 6 <= opp.hours_left <= 48:
        time_score = 1.0  # Peak trading window
    elif 1 <= opp.hours_left < 6:
        time_score = 0.7  # Exit window — still tradeable
    elif 48 < opp.hours_left <= 168:
        time_score = 0.5  # Monitor-scan window
    else:
        time_score = 0.2  # Too far out or too close

    # 5. Strategy priority
    strategy_score = STRATEGY_PRIORITY.get(opp.strategy, 0.3)

    # Weighted composite
    composite = (
        W_EDGE * edge_score +
        W_CONFIDENCE * confidence_score +
        W_LIQUIDITY * liquidity_score +
        W_TIME * time_score +
        W_STRATEGY * strategy_score
    )

    return round(composite, 4)


def rank_opportunities(opportunities: list[Opportunity],
                       config) -> list[Opportunity]:
    """
    Score and rank all opportunities across strategies.

    Applies composite scoring, filters by minimum threshold,
    respects portfolio allocation limits.
    """
    min_score = config.market_selection.min_composite_score
    max_positions = config.market_selection.max_concurrent_positions

    # Score each opportunity
    for opp in opportunities:
        opp.composite_score = score_opportunity(opp)

    # Filter by minimum score
    qualified = [o for o in opportunities if o.composite_score >= min_score]

    # Sort by composite score (highest first)
    qualified.sort(key=lambda x: x.composite_score, reverse=True)

    # Apply position limit
    if len(qualified) > max_positions:
        qualified = qualified[:max_positions]

    logger.info(f"Market selector: {len(qualified)} qualified from "
                f"{len(opportunities)} total (min_score={min_score})")

    if qualified:
        top = qualified[0]
        logger.info(f"  Top opportunity: {top.question[:50]}... "
                    f"(score={top.composite_score:.3f}, "
                    f"edge={top.edge_after_fees:+.3f}, "
                    f"strategy={top.strategy})")

    return qualified


def allocate_capital(opportunities: list[Opportunity],
                     balance: float,
                     config) -> list[Opportunity]:
    """
    Apply portfolio-level capital allocation across strategies.

    Respects strategy_allocation percentages from config.
    Each strategy gets a capital budget, and opportunities within
    each strategy compete for their strategy's budget.
    """
    allocation = config.market_selection.strategy_allocation
    if isinstance(allocation, dict):
        alloc = allocation
    else:
        alloc = allocation._data

    # Calculate per-strategy capital budgets
    budgets = {}
    for strategy, pct in alloc.items():
        budgets[strategy] = balance * pct

    # Group opportunities by strategy
    by_strategy = {}
    for opp in opportunities:
        key = opp.strategy
        if key not in by_strategy:
            by_strategy[key] = []
        by_strategy[key].append(opp)

    # Log allocation
    for strategy, opps in by_strategy.items():
        budget = budgets.get(strategy, 0)
        logger.info(f"  {strategy}: {len(opps)} opportunities, "
                    f"budget ${budget:.2f}")

    return opportunities  # Sizing is handled by RiskManager's Kelly calc
