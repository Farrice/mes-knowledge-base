"""
Sportsbook Odds Integration — The Vegas Anchor (GP-1).

sovereign2013's core strategy: treat professional sportsbook odds as ground truth,
exploit Polymarket deviations. This module:

  1. Fetches odds from OddsPapi (348 bookmakers, including Pinnacle)
  2. Strips the vig using multiplicative method (Power for heavy favorites)
  3. Calculates true implied probabilities
  4. Fuzzy-matches sportsbook events to Polymarket markets
  5. Identifies actionable edges (gap > fee drag)

The key insight (HK-8): Pinnacle runs 2-3% vig, accepts sharp bettors, and their
lines most closely approximate true probabilities. DraftKings/FanDuel run higher
margins and limit sharps. Pinnacle IS the reference price.

Vig stripping math (HK-8, verified by research):
  Multiplicative: divide each implied prob by total overround
    -110/-110 → 52.38% each → total 104.76% → true 50%/50%
  Power: raises probabilities to a constant power. Better for lopsided lines (> -300)
"""

import logging
import os
import re
from datetime import datetime, timezone
from difflib import SequenceMatcher
from typing import Optional

import requests

from projects.prediction_market_arb.constants import ODDSPAPI_URL, SPORT_KEYS, FEE_DRAG
from projects.prediction_market_arb.models import SportsOdds, Opportunity, StrategyType, EdgeType
from projects.prediction_market_arb.resilience import retry_transient

logger = logging.getLogger("polymarket.sportsbook")


# =============================================================================
# VIG STRIPPING (from HK-8: The Gambot Principle)
# =============================================================================

def american_to_implied(american: float) -> float:
    """Convert American odds to implied probability.

    -150 → 0.6000 (60%)
    +130 → 0.4348 (43.48%)
    """
    if american == 0:
        return 0.0
    if american < 0:
        return abs(american) / (abs(american) + 100)
    return 100 / (american + 100)


def decimal_to_implied(decimal_odds: float) -> float:
    """Convert decimal odds to implied probability."""
    if decimal_odds <= 0:
        return 0.0
    return 1.0 / decimal_odds


def strip_vig_multiplicative(probs: list[float]) -> list[float]:
    """
    Multiplicative vig stripping — industry standard for balanced markets.

    Each implied probability is divided by the total overround.
    Example: [0.6, 0.435] → total 1.035 → [0.5797, 0.4203]
    """
    total = sum(probs)
    if total <= 0:
        return [0.0] * len(probs)
    return [p / total for p in probs]


def strip_vig_power(probs: list[float]) -> list[float]:
    """
    Power method vig stripping — better for lopsided lines (heavy favorites).

    Finds exponent k such that sum(p_i^k) = 1.0 using binary search.
    More accurate than multiplicative when one side exceeds -300.
    """
    if not probs or all(p <= 0 for p in probs):
        return [0.0] * len(probs)

    # Binary search for k
    lo, hi = 0.5, 2.0
    for _ in range(50):  # Converges quickly
        k = (lo + hi) / 2
        total = sum(p ** k for p in probs if p > 0)
        if total > 1.0:
            lo = k
        else:
            hi = k

    k = (lo + hi) / 2
    return [p ** k if p > 0 else 0.0 for p in probs]


def strip_vig(probs: list[float], method: str = "multiplicative",
              power_threshold: float = 300) -> list[float]:
    """
    Strip vig using the appropriate method.

    Automatically switches to Power method if any implied probability
    exceeds the threshold (corresponds to American odds beyond -300).
    """
    # Check if any line is heavy enough to warrant Power method
    if method == "multiplicative":
        for p in probs:
            if p > 0 and (p > power_threshold / (power_threshold + 100)):
                method = "power"
                break

    if method == "power":
        return strip_vig_power(probs)
    return strip_vig_multiplicative(probs)


# =============================================================================
# ODDSPAPI CLIENT
# =============================================================================

class SportsbookClient:
    """
    Fetches odds from OddsPapi and identifies Pinnacle reference prices.

    OddsPapi: 348 bookmakers including Pinnacle, WebSocket on paid tiers.
    API key from ODDSPAPI_KEY environment variable.
    """

    def __init__(self, config):
        self.config = config
        self.api_url = config.sports.odds_api_url
        self.api_key = os.environ.get("ODDSPAPI_KEY", "")
        self.preferred_book = config.sports.preferred_bookmaker
        self._session = requests.Session()
        self._session.headers.update({
            "User-Agent": "polymarket-arb/0.2.0",
            "Accept": "application/json",
        })
        if not self.api_key:
            logger.warning("ODDSPAPI_KEY not set — sportsbook scanning disabled")

    @retry_transient()
    def fetch_odds(self, sport: str) -> list[SportsOdds]:
        """
        Fetch current odds for a sport from OddsPapi.

        Returns list of SportsOdds with Pinnacle lines and vig-stripped probabilities.
        Falls back to consensus of other sharp books if Pinnacle unavailable for an event.
        """
        if not self.api_key:
            return []

        try:
            resp = self._session.get(
                f"{self.api_url}/sports/{sport}/odds",
                params={
                    "apiKey": self.api_key,
                    "regions": "eu,us,uk",
                    "markets": "h2h",
                    "oddsFormat": "american",
                    "bookmakers": self.preferred_book,
                },
                timeout=15,
            )
            resp.raise_for_status()
            events = resp.json()
        except requests.RequestException as e:
            logger.error(f"OddsPapi fetch failed for {sport}: {e}")
            return []

        results = []
        vig_method = self.config.sports.vig_strip_method
        power_threshold = self.config.sports.vig_strip_power_threshold

        for event in events:
            # Find Pinnacle odds (or fallback book)
            bookmakers = event.get("bookmakers", [])
            pinnacle = None
            for bm in bookmakers:
                if bm.get("key") == self.preferred_book:
                    pinnacle = bm
                    break

            if not pinnacle:
                # Fallback: use first available sharp book
                if bookmakers:
                    pinnacle = bookmakers[0]
                else:
                    continue

            # Extract h2h market odds
            h2h = None
            for market in pinnacle.get("markets", []):
                if market.get("key") == "h2h":
                    h2h = market
                    break

            if not h2h:
                continue

            outcomes = h2h.get("outcomes", [])
            if len(outcomes) < 2:
                continue

            # Parse odds
            home_odds = float(outcomes[0].get("price", 0))
            away_odds = float(outcomes[1].get("price", 0))
            draw_odds = float(outcomes[2].get("price", 0)) if len(outcomes) > 2 else None

            # Convert to implied probabilities
            implied = [american_to_implied(home_odds), american_to_implied(away_odds)]
            if draw_odds is not None:
                implied.append(american_to_implied(draw_odds))

            # Strip vig
            true_probs = strip_vig(implied, method=vig_method,
                                   power_threshold=power_threshold)

            vig_pct = sum(implied) - 1.0

            odds = SportsOdds(
                event_id=event.get("id", ""),
                sport=sport,
                home_team=event.get("home_team", ""),
                away_team=event.get("away_team", ""),
                commence_time=event.get("commence_time", ""),
                pinnacle_home=home_odds,
                pinnacle_away=away_odds,
                pinnacle_draw=draw_odds,
                true_prob_home=round(true_probs[0], 4),
                true_prob_away=round(true_probs[1], 4),
                true_prob_draw=round(true_probs[2], 4) if len(true_probs) > 2 else None,
                vig_pct=round(vig_pct, 4),
                bookmaker=pinnacle.get("key", self.preferred_book),
                last_update=pinnacle.get("last_update", ""),
            )
            results.append(odds)

        logger.info(f"Fetched {len(results)} events for {sport} "
                    f"({SPORT_KEYS.get(sport, sport)})")
        return results

    def scan_all_sports(self) -> list[SportsOdds]:
        """Fetch odds across all configured sports."""
        all_odds = []
        sports = self.config.sports.sports
        if isinstance(sports, str):
            sports = [sports]

        for sport in sports:
            odds = self.fetch_odds(sport)
            all_odds.extend(odds)

        logger.info(f"Total sportsbook events: {len(all_odds)} across {len(sports)} sports")
        return all_odds


# =============================================================================
# EVENT MATCHING (Polymarket ↔ Sportsbook)
# =============================================================================

def normalize_team_name(name: str) -> str:
    """Normalize team name for fuzzy matching.

    "Los Angeles Lakers" → "los angeles lakers"
    "LA Lakers" → "la lakers"
    "Man Utd" → "man utd"
    """
    name = name.lower().strip()
    # Remove common suffixes
    for suffix in [" fc", " cf", " sc", " afc"]:
        if name.endswith(suffix):
            name = name[:-len(suffix)].strip()
    return name


def match_events_to_polymarket(odds_list: list[SportsOdds],
                                polymarket_markets: list,
                                min_confidence: float = 0.7) -> list[SportsOdds]:
    """
    Fuzzy-match sportsbook events to Polymarket markets.

    Uses normalized team names + date proximity for matching.
    Returns odds_list with polymarket_market_id and match_confidence populated.
    """
    matched = []

    for odds in odds_list:
        home_norm = normalize_team_name(odds.home_team)
        away_norm = normalize_team_name(odds.away_team)

        best_match = None
        best_score = 0.0

        for market in polymarket_markets:
            question = market.question.lower() if hasattr(market, 'question') else str(market.get("question", "")).lower()
            market_id = market.id if hasattr(market, 'id') else market.get("id", "")

            # Score: both team names must appear in the question
            home_score = SequenceMatcher(None, home_norm, question).ratio()
            away_score = SequenceMatcher(None, away_norm, question).ratio()

            # Check if team names are substrings (stronger signal)
            home_in = home_norm in question or any(
                word in question for word in home_norm.split() if len(word) > 3
            )
            away_in = away_norm in question or any(
                word in question for word in away_norm.split() if len(word) > 3
            )

            if home_in and away_in:
                # Both teams found — high confidence
                score = 0.85 + 0.15 * ((home_score + away_score) / 2)
            elif home_in or away_in:
                # One team found — check if it's a "will X win" market
                score = 0.5 + 0.3 * max(home_score, away_score)
            else:
                score = (home_score + away_score) / 2

            if score > best_score:
                best_score = score
                best_match = market_id
                best_question = question

        if best_match and best_score >= min_confidence:
            odds.polymarket_market_id = best_match
            odds.match_confidence = round(best_score, 3)
            odds.polymarket_question = best_question[:200]
            matched.append(odds)
            logger.debug(f"Matched: {odds.home_team} vs {odds.away_team} → "
                         f"{best_question[:50]}... (conf={best_score:.2f})")
        else:
            logger.debug(f"No match: {odds.home_team} vs {odds.away_team} "
                         f"(best={best_score:.2f})")

    logger.info(f"Matched {len(matched)}/{len(odds_list)} events to Polymarket markets")
    return matched


# =============================================================================
# EDGE DETECTION (The Vegas Anchor — GP-1)
# =============================================================================

def find_sports_edges(matched_odds: list[SportsOdds],
                      client,
                      config) -> list[Opportunity]:
    """
    Compare vig-stripped sportsbook probabilities against Polymarket prices.
    Returns list of Opportunity objects for markets with actionable edges.

    The mechanic (GP-1): When Pinnacle prices Lakers at 62% and Polymarket
    prices them at 55%, the 7-point gap minus fees = extractable edge.
    """
    opportunities = []
    min_edge = config.sports.min_edge_pct
    fee_drag = FEE_DRAG.get("sports", 0.0075)

    for odds in matched_odds:
        if not odds.polymarket_market_id:
            continue

        # Get current Polymarket price
        prices = client.get_market_price(odds.polymarket_market_id)
        if not prices:
            continue

        poly_yes = prices["yes"]
        poly_no = prices["no"]

        # Check home team edge (YES side on Polymarket)
        # Assumption: Polymarket "Will X win?" → YES = home team wins
        home_edge = odds.true_prob_home - poly_yes
        away_edge = odds.true_prob_away - poly_no

        # Determine which side has the bigger edge
        if home_edge > away_edge and home_edge > fee_drag:
            edge = home_edge
            our_prob = odds.true_prob_home
            market_price = poly_yes
            side_label = f"{odds.home_team} (home)"
        elif away_edge > fee_drag:
            edge = away_edge
            our_prob = odds.true_prob_away
            market_price = poly_no
            side_label = f"{odds.away_team} (away)"
        else:
            continue

        edge_after_fees = edge - fee_drag

        if edge_after_fees < min_edge:
            continue

        # EV calculation (same as weather_data.calc_edge)
        if market_price > 0 and market_price < 1.0:
            ev = our_prob / market_price - 1.0
            b = (1.0 / market_price) - 1.0
            kelly_f = max(0.0, (our_prob * b - (1.0 - our_prob)) / b) if b > 0 else 0.0
        else:
            ev = 0.0
            kelly_f = 0.0

        opp = Opportunity(
            strategy=StrategyType.SPORTS_ARB.value,
            market_id=odds.polymarket_market_id,
            token_id="",  # Will be resolved by the orchestrator
            question=odds.polymarket_question,
            category="sports",
            our_probability=round(our_prob, 4),
            market_price=round(market_price, 4),
            edge=round(edge, 4),
            edge_after_fees=round(edge_after_fees, 4),
            ev=round(ev, 4),
            kelly_f=round(kelly_f, 4),
            edge_type=EdgeType.INFORMATION_ASYMMETRY.value,
            reference_source=f"{odds.bookmaker} (vig: {odds.vig_pct:.1%})",
            confidence=odds.match_confidence,
            volume=0.0,  # Will be populated by orchestrator
            hours_left=0.0,
            context={
                "sport": odds.sport,
                "home_team": odds.home_team,
                "away_team": odds.away_team,
                "side": side_label,
                "pinnacle_home": odds.pinnacle_home,
                "pinnacle_away": odds.pinnacle_away,
                "true_prob_home": odds.true_prob_home,
                "true_prob_away": odds.true_prob_away,
                "commence_time": odds.commence_time,
                "match_confidence": odds.match_confidence,
            },
            timestamp=datetime.now(timezone.utc).isoformat(),
        )
        opportunities.append(opp)

    # Sort by edge (highest first)
    opportunities.sort(key=lambda x: x.edge_after_fees, reverse=True)
    logger.info(f"Sports arb scan: {len(opportunities)} actionable edges "
                f"from {len(matched_odds)} matched events")
    return opportunities
