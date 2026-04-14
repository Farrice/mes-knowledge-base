---
name: "Prediction Market Weather Trading"
description: "Production weather market trading system extracted from alteregoeth-ai/weatherbot — airport station resolution matching eliminates 3-8F systematic error, multi-source forecast selection (HRRR/ECMWF/METAR) weighted by geography and time horizon, self-calibrating per-city sigma replaces static probability assumptions after 30+ samples, quarter-Kelly with hard cap sizes every position defensively, and a three-exit framework (stop-loss + trailing + forecast-change) manages risk on price, profit, and information dimensions simultaneously."
version: "1.0"
format: "completion-engine"
workflows: 3
source: "MES 3.0 Deep Extraction — alteregoeth-ai/weatherbot (2,009 lines production Python)"
---

# Prediction Market Weather Trading

> The bot wins because it solves a coordination problem most traders ignore — weather markets resolve on specific airport stations, not cities. Using KLGA coordinates instead of "New York City" coordinates eliminates 3-8 degrees F of systematic error on markets with 1-2 degree F buckets. Combined with multi-source forecast cross-validation and learned per-city sigma calibration, this creates persistent informational edge against traders using generic weather data.

**Core Principle**: More accurate data at the resolution point beats better trading at the wrong location.

---

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| forecast | [Market Forecast & Edge Detection](workflows/market-forecast-edge.md) | Ranked opportunity table with probability, EV, Kelly sizing, and top-3 actionable edges | Scanning active Polymarket weather markets for mispriced positions |
| execution | [Trade Execution Plan](workflows/trade-execution-plan.md) | Complete trade ticket with entry, position size, all five exit scenarios, and decision tree | You have an identified edge and need the full lifecycle plan before placing a trade |
| calibration | [Self-Calibration Review](workflows/calibration-review.md) | Per-city sigma report, parameter optimization recommendations, and updated config.json | After 30+ resolved markets, reviewing model accuracy and tuning parameters |

## Quick Reference
- **Genius Context**: [genius.md](genius.md) — load before any workflow
- **Source Extraction**: [weatherbot-extraction.md](../../extractions/prediction-market-trading/weatherbot-extraction.md)
- **Reference Implementation**: alteregoeth-ai/weatherbot (GitHub) — bot_v1.py (450 lines) + bot_v2.py (1,050 lines)
- **Key Constraint**: ALWAYS map markets to airport ICAO codes before forecasting. Never use city-center coordinates.
- **Architecture**: LLM reasons, deterministic code executes. Separation is absolute and non-negotiable.
