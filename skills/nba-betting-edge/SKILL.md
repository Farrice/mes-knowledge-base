---
name: "NBA Betting Edge: Player Prop & Parlay Prediction System"
description: "Systematic NBA player prop analysis using behavioral finance principles and statistical edge detection. Research-driven predictions with honest confidence scoring, correlation-aware parlay construction, and Kelly criterion bankroll discipline."
version: "2.0"
format: "completion-engine"
workflows: 3
---

# NBA Betting Edge: Player Prop & Parlay Prediction System

A research-driven prediction system that finds exploitable edges in NBA player prop betting markets. Built on Jim O'Shaughnessy's behavioral finance framework — the core insight is that betting markets, like financial markets, are distorted by predictable human biases (recency bias, name recognition, emotional betting). The system identifies where posted lines diverge from statistical reality, scores confidence based on contextual alignment, and constructs correlation-aware parlays with disciplined bankroll sizing.

**Core Genius**: Edge detection through the Context Stack (5-variable analysis) + Recency Bias Arbitrage (weighted averaging that exploits the market's overreaction to recent games) + behavioral bias auditing (Four Horsemen Defense adapted for sports betting).

**Honest caveat**: This is a research-informed decision tool, not a guaranteed edge. Sports betting markets are efficient. The system helps make *better* decisions — it does not promise profitability.

## Available Workflows

| # | Workflow | Produces | Use When |
|---|---------|----------|----------|
| research | [Game Day Research & Picks](workflows/game-day-research-picks.md) | Pick slate with confidence scores, parlay suggestions, and bankroll sizing for tonight's NBA games | Running daily analysis before game time — pull stats, detect edges, build picks |
| review | [Performance Review & Calibration](workflows/performance-review-calibration.md) | Win/loss report with ROI calculation, confidence calibration analysis, and pattern effectiveness review | After results are in — log outcomes, calibrate the confidence model, track what's working |
| bankroll | [Bankroll Strategy & Position Sizing](workflows/bankroll-strategy-position-sizing.md) | Bankroll setup, Kelly criterion sizing guide, exposure limits, and drawdown protocols | Setting up initial bankroll, reviewing position sizing strategy, or after a significant drawdown |

## Quick Reference
- **Genius Context**: [genius.md](genius.md) — load before any workflow
- **Entry Point**: `.agent/workflows/betting-edge.md` — invoke via `/betting-edge`
- **Bet Tracker**: `execution/bet_tracker.py` — CLI for logging bets and results
- **Tracking Data**: `.agent/bet-tracking.json` — prediction history and bankroll
