---
name: "Prediction Market Risk Management"
description: "Capital protection across all prediction market strategies — the system that keeps you alive while edges rotate. Position sizing, portfolio risk, kill switches, and the paper-to-live gap."
version: "1.0"
format: "completion-engine"
workflows: 3
source: "MES 3.0 Deep Extraction — all 6 source files (weatherbot + sovereign + Polymarket docs + arbitrage bot + poly-maker + agents, 7,281 lines)"
---

# Prediction Market Risk Management

> Cross-cutting risk management skill that protects capital across all prediction market trading strategies. This skill does not generate trades — it validates, sizes, monitors, and kills them.

**Core truth: 92.4% of Polymarket wallets are unprofitable. The 7.6% that survive share one trait: they treat risk management as the product, not an afterthought bolted onto strategy.** Every edge decays — arbitrage windows compressed from 12.3 seconds (2024) to 2.7 seconds (2026) to dead. Strategies that printed money in February fail by March. The ONLY durable asset is the system that keeps you alive while edges rotate.

---

## The Paper-to-Live Gap (Centerpiece Finding)

Simulation showed 522x returns. Live v2 lost 49.5%. Live v3 lost 13%. Same signal logic. Every backtest lies because it cannot capture execution fees, slippage on thin order books, market impact, latency, and adversarial competition. The question is not "will my strategy work?" but "will I survive when it doesn't?"

**Expect 80-95% degradation from paper to live. If your strategy is not profitable at 90% degradation, do not deploy.**

---

## The Three-Layer Defense

1. **Per-Trade Risk** — Kelly fraction (0.25) + hard caps (MAX_BET, MAX_PRICE, MIN_VOLUME, MIN_EV, MAX_SLIPPAGE) + 8-check sequential validation chain
2. **Per-Strategy Risk** — Strategy-specific envelopes: weather calibration per city/source, AI uncertainty filter (swarm std dev < 30%), market-making inventory caps + compound stop-loss, arb fee-adjusted edge thresholds
3. **Portfolio Risk** — 10% max per market, 5% daily circuit breaker, 30% correlation limit, global exposure ceiling, kill switch as one-way emergency brake

## The Two-Layer Security Architecture

From the Polymarket Agents framework: "LLM proposes, code validates." The AI identifies opportunities and suggests trades. Deterministic code validates every parameter before execution. The RiskManager.check_order() method gates every API call. This prevents hallucinated edges, size errors, invalid orders, and stale signals. LLMs hallucinate. When an LLM hallucinates in a trading context, the result is real money lost.

---

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| 1 | [Position Sizing Calculator](workflows/position-sizing.md) | Kelly-optimal position size with all risk limits and fee impact applied | Before any trade — calculates exact dollar amount and validates against the 8-check chain |
| 2 | [Portfolio Risk Audit](workflows/portfolio-risk-audit.md) | Full risk assessment across all active positions with dashboard + recommendations | Daily review, after significant market events, or when portfolio composition changes |
| 3 | [Kill Switch Protocol](workflows/kill-switch-protocol.md) | 3-level emergency shutdown with triggers, recovery procedures, and test protocol | System setup, emergency situations, monthly testing, and post-mortem analysis |

---

## Key Parameters Quick Reference

### Position Sizing (WeatherBot `bot_v2.py`)
| Parameter | Value | Function |
|-----------|-------|----------|
| `KELLY_FRACTION` | 0.25 | Quarter-Kelly cap on all positions |
| `MAX_BET` | $20 | Hard ceiling regardless of Kelly output |
| `MIN_EV` | 0.10 | Minimum 10% expected value to enter |
| `MAX_PRICE` | 0.45 | Never buy contracts above 45 cents |
| `MAX_SLIPPAGE` | 0.03 | Maximum bid-ask spread tolerance |
| `MIN_VOLUME` | 500 | Minimum market volume for liquidity |

### Arbitrage Bot Risk Parameters (`config.yaml`)
| Parameter | Conservative | Default |
|-----------|-------------|---------|
| `max_position_per_market` | $15 | $200 |
| `max_global_exposure` | $50 | $5,000 |
| `max_daily_loss` | $10 | $500 |
| `max_drawdown_pct` | 15% | 10% |
| `min_edge` | 1% (bundle) | 2% (cross-platform) |

### Portfolio-Level Controls
| Control | Value | Source |
|---------|-------|--------|
| Max capital per market | 10% | Sovereign analysis |
| Daily drawdown circuit breaker | 5% | Sovereign + PolySwarm |
| Correlation rebalance threshold | 30% | Portfolio construction |
| Human underperformance vs bots | ~18% | 50K wallet analysis |

### Platform Risk
| Risk | Detail |
|------|--------|
| Heartbeat timeout | 10s window (5s buffer) — miss = ALL orders cancelled |
| Matching engine restart | Tuesdays 7 AM ET, ~90s downtime |
| Fee peak | At 50% probability: crypto 0.072, sports 0.03, geopolitical 0 |
| Rate limits | 3,500 orders/10s, cancel-all 250/10s |

---

## What Separates the 7.6% from the 92.4%

**Losers:** Full Kelly sizing (overleveraged), no stop-losses (hold losers hoping), paper results = live expectations, single strategy (no fallback when edge decays), emotional interference with sizing and exits (18% worse than bots).

**Survivors:** Quarter-Kelly with hard caps, automated exits that execute without human interference, paper-to-live graduation (test with real tiny money before scaling), multi-strategy rotation (when arbitrage dies, rotate to market making or AI probability), bot-assisted execution that doesn't panic, revenge-trade, or override stops.

---

## Domain Context
- **Extraction**: `extractions/prediction-market-trading/risk-management-extraction.md`
- **Genius Context**: [genius.md](genius.md) — full deep knowledge including Kelly math, 8-check chain, all exit mechanisms, platform risk, compound stop-loss architecture
- **Related Skills**: Weather trading, AI ensemble probability, market making, cross-platform arbitrage (this skill applies across all)
- **Scaling Protocol**: Paper (2-4 weeks) -> Micro-live $50-$100 (50+ trades) -> Small-live $500-$1K (100+ trades) -> Full deployment
