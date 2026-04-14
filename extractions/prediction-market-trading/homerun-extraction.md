# Homerun Extraction — braedonsaunders/homerun

**Source**: github.com/braedonsaunders/homerun (MIT, Python/FastAPI + React/TS)
**Date**: 2026-04-13
**Purpose**: Delta analysis vs our prediction_market_arb system

---

## What Homerun Has That We Don't — 6 Actionable Patterns

### 1. Token Circuit Breaker (ADOPT — HIGH PRIORITY)

**What**: Per-token isolation that blocks individual misbehaving tokens without halting all trading. Trips on 2+ large trades (1500+ shares) within 30 seconds on the same token, or 5 consecutive API errors per token. Auto-expires after 120s.

**Why it matters**: Our kill switch is binary — one bad market kills everything. A flash crash on one weather market shouldn't freeze our sports arb pipeline.

**Implementation**: Add `TokenCircuitBreaker` class to `risk_manager.py`. Dict of `{token_id: TripState}` with timestamps. Check between validation step 4 (volume) and step 5 (per-market exposure). ~50 lines. Our kill switch stays as the nuclear option; circuit breaker handles per-token isolation below it.

### 2. Execution Tiers with Price Chasing (ADOPT — HIGH PRIORITY)

**What**: 4-tier system classifies opportunities by ROI + liquidity into conviction levels. Each tier gets different price buffers, position size multipliers, retry counts, and order types. Price chaser retries up to 6 times with +0.005/retry price improvement (capped at 2% slippage), switching to GTD on final attempt.

**Why it matters**: We currently treat all orders identically. A 12% edge on a liquid market should get more aggressive fills than a 3% edge on a thin one. The price chaser alone could recover 30-50% of missed fills from limit order timeouts.

**Implementation**: Add `ExecutionTier` enum + `classify_opportunity()` to `market_selector.py`. Add `PriceChaser` to execution layer. Tier thresholds: T1 (ROI>=5%, liq>=20K), T2 (3%/5K), T3 (2%/1K), T4 (remainder). ~120 lines total.

### 3. Market Prioritizer — HOT/WARM/COLD Scanning (ADOPT — MEDIUM)

**What**: Instead of polling all markets at the same interval, classifies markets into HOT (15s), WARM (60s), COLD (180s) based on 7 signals: age, price stability, liquidity, alerts, recent changes, volume, stagnation. Uses price fingerprinting (hash of rounded prices) to skip unchanged markets entirely.

**Why it matters**: Our dual-cadence (10min/60min) is coarse. New markets and volatile ones need sub-minute polling. The fingerprint optimization alone could cut API calls 60%+ during quiet periods.

**Implementation**: Add `MarketPrioritizer` to `strategy_orchestrator.py`. Replace fixed intervals with tier-based scheduling. Price fingerprinting is ~15 lines (round to 3 decimals, hash). ~80 lines total.

### 4. Comprehensive Fee Model (ADOPT — MEDIUM)

**What**: Four-component fee calculation: entry/taker fees (platform-specific), gas costs ($0.005/tx on Polygon + NegRisk conversion surcharge), spread costs (bid-ask in bps), and multi-leg slippage (quadratic scaling when position >5% of market liquidity). Distinguishes maker (0% fee) vs taker modes.

**Why it matters**: Our system accounts for fees but doesn't model gas, spread, or the nonlinear slippage on large positions. This means our edge calculations overstate actual profitability, especially on multi-leg arbs.

**Implementation**: Add `FeeModel` class with `calculate()` returning `FeeBreakdown` dataclass. Feed into `rank_opportunities()` so edge = gross_edge - total_fees. ~60 lines.

### 5. Event-Driven Strategy Triggering (CONSIDER — LOW)

**What**: Async event bus with pub/sub. Strategies subscribe to event types (MARKET_DATA_REFRESH, DATA_SOURCE_UPDATE). Data sources publish events that trigger immediate strategy evaluation instead of poll-based cycles.

**Why it matters**: Our system is poll-based (scan → analyze → trade). Event-driven would let us react to weather forecast updates or odds movements within seconds instead of waiting for the next scan cycle. However, this is an architectural shift — not a drop-in.

**Status**: Park for Phase 3. Our poll cadence works for current volume. Worth revisiting when we add real-time WebSocket feeds.

### 6. Walk-Forward Parameter Optimization (CONSIDER — LOW)

**What**: Grid/random search over strategy parameters with time-series train/test splits. Top-K configurations validated on held-out data. Composite scoring by `total_roi * quality_pass_rate`.

**Why it matters**: We don't have parameter optimization. Our Kelly fraction (0.25) and thresholds are static. But our strategy count is low (4 pipelines) — optimization matters more at 38 strategies.

**Status**: Build when we have 30+ days of paper trading data to optimize against.

---

## What We Have That Homerun Doesn't

- **Two-key safety gate** (paper/live hierarchy with manual promotion) — Homerun has paper/live toggle but no deliberate friction
- **Kill switch as one-way state machine** with manual recovery — Homerun's circuit breakers auto-expire
- **ICAO-station-precision weather pipeline** — Homerun has weather workers but no documented station-level precision
- **Sportsbook vig stripping** — Homerun has sports strategies but no documented odds normalization
- **3-model ensemble with Bayesian integration** — Homerun uses single LLM scoring, not multi-model consensus
- **3-stage AI+rules contract matcher** — Homerun doesn't document cross-platform contract matching

---

## Architecture Comparison

| Layer | Our System | Homerun |
|-------|-----------|---------|
| Strategies | 4 pipelines (weather, sports, ensemble, MM) | 38 plugin strategies with BaseStrategy pattern |
| Data | Weather API + sportsbook + Polymarket | 39 data source plugins (RSS, REST, Twitter, Chainlink, Binance) |
| Execution | Single-path paper/live | 4-tier execution with price chasing |
| Risk | 8-check chain + quarter-Kelly | Exposure caps + loss limits + circuit breakers + Kelly |
| Monitoring | Dual-cadence (10/60 min) | 16 concurrent workers + HOT/WARM/COLD prioritization |
| Backtesting | None built | Code validation + walk-forward (no slippage sim) |
| UI | Terminal dashboard | 97-component React dashboard |

---

## Priority Integration Order

1. **Token circuit breaker** → `risk_manager.py` (1 hour, high ROI)
2. **Execution tiers + price chaser** → new `execution_tiers.py` (2 hours, recovers missed fills)
3. **Fee model upgrade** → `market_selector.py` (1 hour, fixes edge overstatement)
4. **Market prioritizer** → `strategy_orchestrator.py` (2 hours, better scanning efficiency)
