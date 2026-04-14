"""
Strategy Orchestrator — Routes market opportunities to the correct pipeline.

This is the brain of Phase 2. It connects:
  - Market discovery (Polymarket client → pre-filter → categorize)
  - Weather pipeline (existing Phase 1, for weather markets)
  - Sports arbitrage pipeline (sportsbook odds → vig strip → edge detection)
  - Ensemble pipeline (3-model LLM → Bayesian integration, for politics/econ/tech)
  - Market selection (cross-strategy scoring → portfolio allocation)
  - Risk validation (8-check chain → Kelly sizing)

Data flow:
  Polymarket markets → Pre-filter by category → Route to strategy pipelines →
  Collect Opportunity objects → Market selector ranks → Risk manager validates →
  Paper/Live execution

The Two-Layer Rule is absolute: LLM handles analysis (this module and ensemble.py).
Deterministic code handles execution (polymarket_client.py, risk_manager.py).
The LLM NEVER touches the order book.
"""

import logging
import os
from datetime import datetime, timezone

from projects.prediction_market_arb.config import load_config
from projects.prediction_market_arb.state import StateManager
from projects.prediction_market_arb.polymarket_client import create_client
from projects.prediction_market_arb.weather_data import WeatherPipeline
from projects.prediction_market_arb.sportsbook import (
    SportsbookClient, match_events_to_polymarket, find_sports_edges,
)
from projects.prediction_market_arb.ensemble import EnsembleEngine
from projects.prediction_market_arb.kalshi_client import KalshiClient
from projects.prediction_market_arb.contract_matcher import ContractMatcher
from projects.prediction_market_arb.market_selector import (
    pre_filter_markets, rank_opportunities, allocate_capital,
)
from projects.prediction_market_arb.risk_manager import RiskManager
from projects.prediction_market_arb.models import (
    Opportunity, StrategyType, OrderRequest, OrderSide,
)

logger = logging.getLogger("polymarket.orchestrator")


# =============================================================================
# TERMINAL COLORS
# =============================================================================

class C:
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    CYAN   = "\033[96m"
    GRAY   = "\033[90m"
    MAGENTA = "\033[95m"
    RESET  = "\033[0m"
    BOLD   = "\033[1m"


STRATEGY_COLORS = {
    StrategyType.WEATHER.value: C.CYAN,
    StrategyType.SPORTS_ARB.value: C.GREEN,
    StrategyType.ENSEMBLE.value: C.MAGENTA,
    StrategyType.MARKET_MAKING.value: C.YELLOW,
}


# =============================================================================
# STRATEGY ORCHESTRATOR
# =============================================================================

class StrategyOrchestrator:
    """
    Multi-strategy trading orchestrator. Routes markets to the correct
    analysis pipeline, collects opportunities, and feeds them through
    the market selector and risk manager.
    """

    def __init__(self, config=None, config_path=None):
        self.config = config or load_config(config_path)
        self.state = StateManager(self.config.paper.data_dir)
        self.client = create_client(self.config, self.state)
        self.risk = RiskManager(self.config, self.state)

        # Strategy pipelines
        self.weather = WeatherPipeline(self.config, self.state)
        self.sportsbook = SportsbookClient(self.config)
        self.ensemble = EnsembleEngine(self.config)
        # Cross-platform (Kalshi)
        self.kalshi = KalshiClient(self.config)
        self.matcher = ContractMatcher(self.config)

    # -------------------------------------------------------------------------
    # FULL SCAN — runs all strategy pipelines
    # -------------------------------------------------------------------------

    def scan_all(self) -> list[Opportunity]:
        """
        Full multi-strategy scan:
          1. Discover Polymarket markets
          2. Pre-filter and categorize
          3. Route to strategy pipelines (weather, sports, ensemble)
          4. Collect all opportunities
          5. Rank via market selector
          6. Return scored, ranked opportunities

        This does NOT execute trades — that's the paper_trader's job.
        """
        print(f"\n{C.BOLD}{C.CYAN}=== MULTI-STRATEGY SCAN ==={C.RESET}")
        print(f"  Time: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M UTC')}")

        # Check kill switch first
        ks = self.risk.get_kill_switch_status()
        if ks["triggered"]:
            print(f"  {C.RED}KILL SWITCH TRIGGERED: {ks['reason']}{C.RESET}")
            return []

        all_opportunities = []

        # --- WEATHER PIPELINE (existing Phase 1) ---
        print(f"\n{C.BOLD}{C.CYAN}[1/3] Weather Markets{C.RESET}")
        weather_opps = self._scan_weather()
        all_opportunities.extend(weather_opps)
        print(f"  {C.CYAN}Found {len(weather_opps)} weather opportunities{C.RESET}")

        # --- SPORTS ARBITRAGE PIPELINE (Phase 2 new) ---
        print(f"\n{C.BOLD}{C.GREEN}[2/3] Sports Arbitrage{C.RESET}")
        sports_opps = self._scan_sports()
        all_opportunities.extend(sports_opps)
        print(f"  {C.GREEN}Found {len(sports_opps)} sports arb opportunities{C.RESET}")

        # --- ENSEMBLE PIPELINE (Phase 2 new) ---
        print(f"\n{C.BOLD}{C.MAGENTA}[3/4] AI Ensemble{C.RESET}")
        ensemble_opps = self._scan_ensemble()
        all_opportunities.extend(ensemble_opps)
        print(f"  {C.MAGENTA}Found {len(ensemble_opps)} ensemble opportunities{C.RESET}")

        # --- CROSS-PLATFORM PIPELINE (Phase 2.5 — Kalshi) ---
        print(f"\n{C.BOLD}{C.YELLOW}[4/4] Cross-Platform (Polymarket ↔ Kalshi){C.RESET}")
        cross_opps = self._scan_cross_platform()
        all_opportunities.extend(cross_opps)
        print(f"  {C.YELLOW}Found {len(cross_opps)} cross-platform opportunities{C.RESET}")

        # --- RANK AND SELECT ---
        print(f"\n{C.BOLD}Ranking {len(all_opportunities)} total opportunities...{C.RESET}")
        ranked = rank_opportunities(all_opportunities, self.config)

        # Apply capital allocation
        balance = self.state.load_balance()
        ranked = allocate_capital(ranked, balance.current, self.config)

        # Print top opportunities
        if ranked:
            print(f"\n{C.BOLD}Top Opportunities:{C.RESET}")
            for i, opp in enumerate(ranked[:5]):
                color = STRATEGY_COLORS.get(opp.strategy, C.GRAY)
                print(f"  {i+1}. {color}[{opp.strategy:12s}]{C.RESET} "
                      f"{opp.question[:50]}...")
                print(f"     Edge: {opp.edge_after_fees:+.1%} | "
                      f"Score: {opp.composite_score:.3f} | "
                      f"Ref: {opp.reference_source}")
        else:
            print(f"  {C.GRAY}No opportunities above threshold{C.RESET}")

        return ranked

    # -------------------------------------------------------------------------
    # STRATEGY PIPELINES
    # -------------------------------------------------------------------------

    def _scan_weather(self) -> list[Opportunity]:
        """
        Run the weather pipeline (Phase 1 — already built).
        Converts weather results to Opportunity format for unified ranking.
        """
        try:
            raw = self.weather.scan_weather_markets(self.client)
        except Exception as e:
            logger.error(f"Weather scan failed: {e}")
            return []

        # Convert weather results to Opportunity objects
        opportunities = []
        for r in raw:
            opp = Opportunity(
                strategy=StrategyType.WEATHER.value,
                market_id=r["market_id"],
                token_id=r["token_id"],
                question=r["question"],
                category="weather",
                our_probability=r["probability"],
                market_price=r["market_price"],
                edge=r["edge"],
                edge_after_fees=r["edge"] - 0.0125,  # Weather fee drag
                ev=r["ev"],
                kelly_f=r["kelly_f"],
                edge_type="information_asymmetry",
                reference_source=r["forecast_source"],
                confidence=0.85,  # Weather forecasts are reliable at D+0/D+1
                volume=r["volume"],
                hours_left=r["hours_left"],
                neg_risk=r["neg_risk"],
                context={
                    "city": r["city"],
                    "city_name": r["city_name"],
                    "date": r["date"],
                    "forecast_temp": r["forecast_temp"],
                    "sigma": r["sigma"],
                    "unit": r["unit"],
                    "bucket": r["bucket"],
                },
                timestamp=datetime.now(timezone.utc).isoformat(),
            )
            opportunities.append(opp)

        return opportunities

    def _scan_sports(self) -> list[Opportunity]:
        """
        Run the sports arbitrage pipeline (Phase 2 — new).
        Fetches sportsbook odds, matches to Polymarket, finds edges.
        """
        # Step 1: Fetch odds from OddsPapi across all configured sports
        try:
            all_odds = self.sportsbook.scan_all_sports()
        except Exception as e:
            logger.error(f"Sportsbook scan failed: {e}")
            return []

        if not all_odds:
            logger.info("No sportsbook odds available (API key may not be set)")
            return []

        # Step 2: Get Polymarket sports markets for matching
        try:
            sports_markets = self.client.get_markets(
                active=True, limit=200, category="sports"
            )
        except Exception as e:
            logger.error(f"Failed to fetch Polymarket sports markets: {e}")
            return []

        if not sports_markets:
            return []

        # Step 3: Match events to Polymarket
        min_conf = self.config.sports.match_confidence_min
        matched = match_events_to_polymarket(all_odds, sports_markets, min_conf)

        # Step 4: Find edges
        opportunities = find_sports_edges(matched, self.client, self.config)
        return opportunities

    def _scan_ensemble(self) -> list[Opportunity]:
        """
        Run the ensemble pipeline (Phase 2 — new).
        Pre-filters markets, runs 3-model ensemble on candidates.
        """
        if not self.config.ensemble.enabled:
            return []

        # Step 1: Get all active markets
        try:
            all_markets = self.client.get_markets(active=True, limit=200)
        except Exception as e:
            logger.error(f"Failed to fetch markets for ensemble: {e}")
            return []

        # Step 2: Pre-filter and categorize
        categorized = pre_filter_markets(all_markets, self.config)

        # Step 3: Select ensemble-eligible markets
        ensemble_categories = self.config.ensemble.categories
        if isinstance(ensemble_categories, str):
            ensemble_categories = [ensemble_categories]

        candidates = []
        for cat in ensemble_categories:
            if cat in categorized:
                candidates.extend(categorized[cat])

        if not candidates:
            logger.info("No ensemble-eligible markets found")
            return []

        logger.info(f"Ensemble candidates: {len(candidates)} markets in "
                     f"{', '.join(ensemble_categories)}")

        # Step 4: Run ensemble analysis on candidates
        try:
            opportunities = self.ensemble.scan_markets(candidates, self.client)
        except Exception as e:
            logger.error(f"Ensemble scan failed: {e}")
            return []

        return opportunities

    def _scan_cross_platform(self) -> list[Opportunity]:
        """
        Run the cross-platform matching pipeline (Phase 2.5 — Kalshi integration).
        Compares Polymarket and Kalshi markets to find cross-platform arbitrage.
        """
        if not self.config.cross_platform.enabled:
            return []

        # Step 1: Get Polymarket markets
        try:
            poly_markets = self.client.get_markets(active=True, limit=200)
        except Exception as e:
            logger.error(f"Failed to fetch Polymarket markets for cross-platform: {e}")
            return []

        # Step 2: Get Kalshi markets
        try:
            kalshi_markets = self.kalshi.scan_categories()
        except Exception as e:
            logger.error(f"Failed to fetch Kalshi markets: {e}")
            return []

        if not poly_markets or not kalshi_markets:
            logger.info("Cross-platform scan: insufficient markets on one or both platforms")
            return []

        logger.info(f"Cross-platform: comparing {len(poly_markets)} Polymarket "
                    f"x {len(kalshi_markets)} Kalshi markets")

        # Step 3: Run 3-stage matching pipeline
        try:
            use_llm = bool(os.environ.get("ANTHROPIC_API_KEY"))
            matches = self.matcher.find_matches(poly_markets, kalshi_markets, use_llm=use_llm)
        except Exception as e:
            logger.error(f"Contract matching failed: {e}")
            return []

        # Step 4: Convert matches to opportunities
        opportunities = self.matcher.matches_to_opportunities(matches)
        return opportunities

    # -------------------------------------------------------------------------
    # STATUS
    # -------------------------------------------------------------------------

    def status(self):
        """Print current orchestrator status."""
        balance = self.state.load_balance()
        risk = self.risk.get_status()
        positions = self.state.load_positions()

        print(f"\n{C.BOLD}{'=' * 60}{C.RESET}")
        print(f"{C.BOLD}  STRATEGY ORCHESTRATOR — STATUS{C.RESET}")
        print(f"{'=' * 60}")

        print(f"\n  Mode: {C.YELLOW}{'LIVE' if self.config.is_live else 'PAPER'}{C.RESET}")
        print(f"  Balance: {C.BOLD}${balance.current:.2f}{C.RESET}")
        print(f"  Kill switch: "
              f"{'🔴 TRIGGERED' if risk['kill_switch']['triggered'] else '🟢 Normal'}")

        # Strategy pipeline status
        print(f"\n  {C.BOLD}Strategy Pipelines:{C.RESET}")
        print(f"    {C.CYAN}Weather{C.RESET}:     Active (20 cities, 3 sources)")

        has_sports_key = bool(self.sportsbook.api_key)
        print(f"    {C.GREEN}Sports Arb{C.RESET}:  "
              f"{'Active' if has_sports_key else 'Disabled (ODDSPAPI_KEY not set)'}")

        has_api_keys = any([
            bool(__import__("os").environ.get("OPENAI_API_KEY")),
            bool(__import__("os").environ.get("ANTHROPIC_API_KEY")),
            bool(__import__("os").environ.get("GOOGLE_API_KEY")),
        ])
        print(f"    {C.MAGENTA}Ensemble{C.RESET}:    "
              f"{'Active' if has_api_keys and self.config.ensemble.enabled else 'Disabled'}")

        has_kalshi = self.kalshi._authenticated
        print(f"    {C.YELLOW}Cross-Platform{C.RESET}: "
              f"{'Active (Polymarket ↔ Kalshi)' if has_kalshi else 'Ready — Awaiting Kalshi API credentials'}")
        print(f"    {C.GRAY}Market Making{C.RESET}:  Deferred (Phase 4)")

        # Current positions by strategy
        if positions:
            by_strategy = {}
            for p in positions:
                # Infer strategy from context (stored in position)
                strategy = "unknown"
                if p.city:
                    strategy = "weather"
                by_strategy.setdefault(strategy, []).append(p)

            print(f"\n  {C.BOLD}Open Positions ({len(positions)}):{C.RESET}")
            for strategy, pos_list in by_strategy.items():
                total_cost = sum(p.cost for p in pos_list)
                print(f"    {strategy}: {len(pos_list)} positions, "
                      f"${total_cost:.2f} deployed")
