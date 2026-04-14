"""
Prediction Market Arb Platform — Phase 2: Intelligence Layer

Multi-strategy AI trading platform for Polymarket.
Paper mode by default. Real money requires explicit two-key activation.

Phase 1 (Data Infrastructure): constants, models, config, state, polymarket_client,
    weather_data, polymarket_ws, risk_manager, paper_trader
Phase 2 (Intelligence Layer): sportsbook, ensemble, market_selector,
    strategy_orchestrator
Phase 2.5 (Kalshi Integration): kalshi_client, contract_matcher

Architecture: LLM reasons, deterministic code executes.
The LLM never holds private keys or places orders.
"""

__version__ = "0.3.0"
