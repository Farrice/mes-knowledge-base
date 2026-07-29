# Prediction Market Strategist — Context Memory

## Project Status
- **Phase 0**: Extraction COMPLETE. 4 MES 3.0 deep extractions finalized. 4 skills + 1 compound agent built.
- **Phase 1**: Data infrastructure COMPLETE. 9 modules built, tested, and verified against live Polymarket data.
  - Package: `_active/prediction-market-arb/` (9 Python modules)
  - CLI wrappers: `execution/polymarket_paper.py`, `execution/polymarket_client.py`, `execution/weather_data.py`, `execution/risk_manager.py`, `execution/polymarket_ws.py`
  - First paper trade executed: London weather market, $20 @ $0.002 (99.8% edge from METAR ground truth)
  - HRRR + ECMWF + METAR all operational. 20 cities across 4 continents.
  - 5-layer paper-only safety architecture verified (two-key gate tested)
- **Phase 2**: Intelligence Layer COMPLETE. 4 new modules + orchestrator built.
  - Package: `_active/prediction-market-arb/` (13 Python modules, up from 9)
  - New modules: `sportsbook.py`, `ensemble.py`, `market_selector.py`, `strategy_orchestrator.py`
  - CLI wrapper: `execution/strategy_orchestrator.py` (scan, scan-weather, scan-sports, status, run, run-weather)
  - Sportsbook: OddsPapi ($49/mo) with Pinnacle vig stripping (multiplicative + Power auto-switch)
  - Ensemble: 3-model independent calls (Haiku 4.5 + GPT-4o-mini + Gemini Flash), 70/30 Bayesian integration
  - Market selector: 5-dimension scoring (edge 40%, confidence 25%, liquidity 15%, time 10%, strategy 10%)
  - Strategy routing: Weather → forecast pipeline, Sports → sportsbook odds, Politics/Econ/Tech → ensemble
  - Market making: Scoring/selection built, quoting engine deferred to Phase 4
  - Paper trader extended: `scan_and_trade_multi()` runs all strategies, `run(multi_strategy=True)` for continuous mode
  - All imports verified, vig stripping math tested, scoring validated
- **Phase 3 next**: Paper Trading Accumulation (30+ days, 200+ trades)
- Built for Farrice Cain and his brother-in-law
- Goal: Multi-strategy AI trading platform on Polymarket (+ eventually Kalshi)
- Financial context: Starting small ($20-50 weather), scaling up per graduated deployment plan
- Plan file: `.claude/plans/twinkly-juggling-coral.md`
- Feasibility doc: `_active/prediction-market-arb/02-research/polymarket-kalshi-arbitrage-feasibility.md`

## Extraction Reports — Complete Inventory

### 1. Weather Trading (`extractions/prediction-market-trading/weatherbot-extraction.md`)
- **Lines**: 676
- **Source**: alteregoeth-ai/weatherbot GitHub repo — README + config.json + bot_v1.py (17.5KB) + bot_v2.py (43.8KB) + sim_dashboard (17.9KB). ~1,700 lines of production trading logic.
- **Genius Patterns**: 11 | **Hidden Knowledge**: 8
- **Key findings**:
  - The #1 edge is ICAO station coordinates, not city names. NYC = KLGA (LaGuardia), not Manhattan. 3-8 degrees F systematic error eliminated.
  - Three-layer forecast source selection: HRRR for US D+0/D+1, ECMWF for everything else, METAR for same-day ground truth only
  - Self-calibrating sigma per (city, source) pair via MAE after 30+ resolved markets. Default sigma 2.0F/1.2C is intentionally conservative.
  - Fractional Kelly (0.25) with hard $20 cap AND $0.45 max price filter. Three layers of position sizing defense.
  - Five exit mechanisms: stop-loss (20% below entry), trailing stop (breakeven at +20%), time-horizon take-profit (0.75/0.85/hold by hours), forecast-change exit (2-degree buffer), resolution
  - Dual-cadence monitoring: defense every 10 min, offense every 60 min
  - Data collection decoupled from trading: forecast snapshots recorded for ALL markets regardless of trade — builds calibration dataset
  - Per-market JSON storage, not database — deliberate choice for debuggability and resilience
  - v2 bot is paper-only. No live execution mode. Simulation-first deployment philosophy.

### 2. AI Event Analysis (`extractions/prediction-market-trading/ai-event-analysis-extraction.md`)
- **Lines**: 1,088
- **Sources**: 11 sources — Finbold, Yahoo Finance, Finance Magnates, arXiv PolySwarm paper, Jung-Hua Liu live trading analysis, 5 GitHub repos, wallet analytics
- **Genius Patterns**: 12 | **Hidden Knowledge**: 10
- **Key findings**:
  - **sovereign2013**: $1 to $3.3M, 37,247 bets, almost exclusively sports, Claude-powered. Multiple bets per minute implies capital rotation, not hold-to-resolution. Utah State vs Arizona bet: $1.73M volume, $179K profit.
  - **The Vegas Anchor**: Sports have the best reference price. Pinnacle odds stripped of vig = true probabilities. Edge = Polymarket price - Pinnacle true probability.
  - **Ensemble weights**: GPT-4o 40% (statistical), Claude 35% (source credibility), Gemini 25% (contrarian). Independence is mandatory — models forecast separately, aggregate after.
  - **PolySwarm 70/30**: 25 of 50 agents per evaluation, confidence-weighted average → 0.70 swarm + 0.30 market. Trade trigger: combined > market by 5% AND std dev < 30%.
  - **Paper-to-live gap**: Simulation 522x. Live v2: -49.5%. Live v3: -13%. Five degradation causes identified. The 0.5x-0.7x haircut rule.
  - **92.4% failure taxonomy**: Oversized positions, late entries, inconsistent risk management. Humans underperform bots by ~18% on identical strategies.
  - **Latency arbitrage is dead**: Windows compressed 12.3s (2024) → 2.7s (2026). 73% of profits to sub-100ms bots. Infrastructure arms race.
  - **$40M extracted**: Arbitrage traders extracted ~$40M from Polymarket Apr 2024-Apr 2025. Zero-sum before fees, negative-sum after.
  - **API cost trap**: Brute-force multi-agent approaches can cost $1-5K/day in inference. sovereign2013's sports arb uses FREE sportsbook odds — structurally superior.
  - **Front-running risk**: Some bots trade against OTHER bots via mempool monitoring. Use private RPC nodes, batch transactions, never large market orders.

### 3. Market Making (`extractions/prediction-market-trading/market-making-extraction.md`)
- **Lines**: 1,191
- **Sources**: Polymarket official docs (14 pages), ImMike/polymarket-arbitrage codebase, warproxxx/poly-maker (2,101 lines — THE production MM bot), Polymarket/agents framework
- **Genius Patterns**: 21 | **Hidden Knowledge**: 13
- **Key findings**:
  - **Quadratic reward cliff**: S(v,s) = ((v-s)/v)^2 * b. 1-cent spread earns 3.24x the reward of 5-cent spread. Two-sided quoting gets 3x boost.
  - **$5M+/month reward pools**: NBA $7,700/game, Champions League QF $24,000/game, EPL $10,000/game. This is the real money — not spread capture.
  - **Post-Only = zero fees**: Makers pay 0%. Combined with GTC/GTD orders, this is the structural moat.
  - **Heartbeat kill switch**: Miss 10-second window = ALL open orders cancelled. Infrastructure priority #1.
  - **Tuesday restart**: Every Tues 7 AM ET, ~90s downtime, HTTP 425. Calendar-aware bots pre-cancel and probe.
  - **poly-maker author verdict**: "In today's market, this bot is not profitable and will lose money." Stop-losses trigger too frequently, reducing active quoting time below reward breakeven.
  - **ImMike config**: `mm_enabled: false` with comment "markets too efficient." Confirms pure spread capture not viable without rewards.
  - **8-check validation chain**: kill switch → blacklist → whitelist → volume → per-market exposure → global exposure → daily loss → drawdown. Sequential, cheapest first, state-changing checks last.
  - **Smart order cancellation**: Only cancel/replace when price diff > $0.005 OR size diff > 10%. Prevents rate limit burn and reward scoring gaps.
  - **Position merging**: YES+NO pairs on-chain → merge to recover USDC. Most bots miss this capital efficiency.
  - **Neg risk capital efficiency**: In multi-outcome markets, No shares convertible to Yes shares in complementary set. Quote across all outcomes with single collateral post.
  - **4 WebSocket channels**: Market (book), User (orders/fills), Sports (scores), RTDS (real-time data). User channel heartbeat is existential; others are operationally important but recoverable.
  - **Batch orders**: 15 per request, effective 15,000/10s vs 3,500/10s individual. 4.3x throughput multiplier. All MM bots should batch.

### 4. Risk Management (`extractions/prediction-market-trading/risk-management-extraction.md`)
- **Lines**: 992
- **Sources**: Cross-strategy synthesis of all 4 extraction source sets
- **Key findings**:
  - **Three-tier risk model**: Per-trade (Kelly + caps + filters + validation chain + exit plan), per-strategy (weather caps, ensemble uncertainty filter, MM inventory caps, cross-platform fee gates), portfolio-level (10% max per market, 5% daily circuit breaker, 30% correlation limit, kill switch)
  - **Kill switch is one-way**: Once triggered, NO automatic recovery. Every subsequent order rejected at Check 1. Manual root cause analysis + parameter review + 2 days paper trading required before reset.
  - **Compound stop-loss (poly-maker)**: Fires when PnL below threshold AND spread narrow enough to exit cleanly, OR when 3-hour volatility exceeds threshold. Prevents selling into wide spreads.
  - **Risk-off cooldown**: After stop-loss, no new buys for configurable hours. Persisted to JSON — survives bot restarts. Per-market, not global.
  - **Calibration-driven adjustment**: Weatherbot sigma updates from actual forecast errors. Risk parameters are alive, not static.
  - **The v2→v3 insight**: ONE change (longer lookback windows) reduced losses by 7x. Signal quality IS risk management — bad signals with perfect stops still lose money, just slower.
  - **Cross-platform fee accounting**: Polymarket taker 1.5% + Kalshi ~1% + $0.04 gas round-trip = minimum ~5.5% gross discrepancy needed. Explains why cross-platform arb is "rare and fleeting."
  - **Integration map**: Portfolio level wraps all strategies → strategies feed through 8-check validation → platform layer (heartbeat, rate limits, fees, slippage) sits underneath everything.

## Source Material Inventory

| File | Size | Type | Status |
|------|------|------|--------|
| alteregoeth-ai/weatherbot (GitHub) | ~86KB, ~1,700 lines trading logic | Production codebase | Fully extracted |
| Multi-source research compilation (11 sources) | 607 lines | News + academic + live trading + wallet analytics | Fully extracted |
| Polymarket official docs | 14 pages | Platform documentation | Fully extracted |
| ImMike/polymarket-arbitrage (GitHub) | Production risk manager + arb engine | Codebase | Fully extracted |
| warproxxx/poly-maker (GitHub) | 2,101 lines | Production MM bot (author confirms unprofitable) | Fully extracted |
| Polymarket/agents (GitHub) | Official AI agent framework | Codebase | Fully extracted |

## Decisions Made
- Quarter-Kelly (0.25 fraction) for all position sizing — non-negotiable, consensus across all sources
- LLM reasons, deterministic code executes — the LLM never holds private keys
- Paper mode required before any live deployment (paper → micro-live $50-100 → small-live $500-1K → full)
- Weather markets first, sports second, market making third
- Kalshi integration deferred until Polymarket strategies are validated
- Portfolio allocation starts conservative (80% arb / 20% MM), migrates to balanced after demonstrated live profitability
- Front-running defense: batch transactions, private RPC nodes, no large market orders

## Open Questions for Phase 1
- Exact starting capital allocation (waiting on brother-in-law discussion)
- Sportsbook odds API selection (Odds API vs The Odds API vs direct Pinnacle scraping)
- Hosting infrastructure: local vs cloud for always-on bot (heartbeat requires 24/7 uptime)
- Kalshi API access, fee structure, and liquidity depth (deferred but relevant for cross-platform)
- USDC.e acquisition path and Polygon wallet setup (Gnosis Safe vs EOA)
- Gas cost optimization strategy ($0.02/order adds up at scale)
- Whether to pursue market making given poly-maker author's unprofitability verdict — may depend on reward pool competition levels at time of entry
- Ensemble cost management: how to keep multi-model inference under $100/day while maintaining prediction quality
