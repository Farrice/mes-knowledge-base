# Prediction Market Trading — Knowledge Index

**Domain**: Prediction market trading (Polymarket)
**Created**: 2026-04-13
**Phase**: 0 (Knowledge Foundation) — COMPLETE
**Pipeline**: Research → Source Collection → MES 3.0 Extractions → Skill Conversion → Agent Creation

---

## Source Materials (6 files, 336KB)

| Source | Lines | Type | Key Content |
|--------|-------|------|-------------|
| [weatherbot-source.md](raw-sources/weatherbot-source.md) | 2,009 | Python codebase | Production weather trading bot — Kelly, calibration, 20 cities |
| [sovereign-trader-analysis-source.md](raw-sources/sovereign-trader-analysis-source.md) | 607 | Research compilation | 11 sources — sovereign2013, PolySwarm paper, live trading failures |
| [polymarket-docs-source.md](raw-sources/polymarket-docs-source.md) | 634 | Official docs | API architecture, fees, WebSocket, rewards, contracts |
| [polymarket-arbitrage-source.md](raw-sources/polymarket-arbitrage-source.md) | 608 | Python codebase | Risk manager, 8-check validation, cross-platform arb |
| [poly-maker-source.md](raw-sources/poly-maker-source.md) | 2,101 | Python codebase | Production market making bot (author: "not profitable") |
| [polymarket-agents-source.md](raw-sources/polymarket-agents-source.md) | 1,322 | Python framework | Official Polymarket AI agent framework — LLM + RAG + trading |

## MES 3.0 Extractions (4 reports, 252KB)

| Extraction | Lines | Genius Patterns | Hidden Knowledge | Crown Jewels |
|-----------|-------|----------------|-----------------|-------------|
| [weatherbot-extraction.md](weatherbot-extraction.md) | 676 | 11 | 8 | 5 |
| [ai-event-analysis-extraction.md](ai-event-analysis-extraction.md) | 1,088 | 12 | 10 | 5 |
| [market-making-extraction.md](market-making-extraction.md) | 1,191 | 21 | 13 | 5 |
| [risk-management-extraction.md](risk-management-extraction.md) | 992 | 10+ | 8+ | 5 |

## Skills (4 skills, 20 files)

| Skill | SKILL.md | genius.md | Workflows |
|-------|----------|-----------|-----------|
| `prediction-market-weather-trading` | ✅ | ✅ (249 lines) | market-forecast-edge, trade-execution-plan, calibration-review |
| `prediction-market-ai-event-analysis` | ✅ | ✅ (392 lines) | odds-discrepancy-scanner, edge-validation-sizing, multi-model-ensemble |
| `prediction-market-making` | ✅ | ✅ (409 lines) | market-selection-spread, adverse-selection-defense, reward-optimization |
| `prediction-market-risk-management` | ✅ | ✅ (448 lines) | position-sizing, portfolio-risk-audit, kill-switch-protocol |

## Agent

| Agent | Skills | Source |
|-------|--------|--------|
| `prediction-market-strategist` | 4 skills above | All 4 MES 3.0 extractions |

## Critical Findings

1. **Prediction market trading is information-transfer arbitrage, not forecasting.** The 7.6% that profit detect when market price deviates from a superior reference price.
2. **Paper-to-live gap is the #1 risk.** Simulation: 522x returns. Live v2: -49.5%. Live v3: -13%. Apply 0.5-0.7x haircut to all backtests.
3. **92.4% of Polymarket wallets are unprofitable.** 14 of 20 top wallets are bots.
4. **Latency arb is DEAD.** Dynamic fees killed it. Windows compressed from 12.3s → 2.7s → dead.
5. **Weather is the quiet alpha.** Airport ICAO codes (not city centers) + multi-source forecasting + self-calibration = persistent edge.
6. **Quarter-Kelly (0.25) is consensus** across every successful implementation studied.
7. **The poly-maker author says his production bot is "not profitable."** Pure spread capture without rewards is not viable.
8. **Execution is 70% of success, strategy is 30%.** Slippage + fees + latency + liquidity destroy paper edges.
