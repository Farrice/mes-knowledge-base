# Prediction Market Arbitrage Platform: Feasibility Assessment v2

**Prepared for**: Farrice Cain & Brother-in-Law
**Date**: April 13, 2026
**Classification**: Strategic Due Diligence — Go/No-Go Decision
**Research basis**: 4 parallel research workstreams + 6 targeted web searches with 2026 data
**Version**: 2.1 — Corrected legal status + strategy viability update (latency arb dead)

---

## Executive Summary

The concept is not just technically sound — it's already being done profitably by Claude-powered AI bots on Polymarket right now. Polymarket is federally legal in the US as of December 2, 2025 (CFTC-approved Designated Contract Market). The $1M/week claim is still aggressive but no longer fantasy-territory given documented bot performance. A well-designed multi-strategy system is a legitimate, buildable business.

**Verdict**: Buildable — yes. Profitable — high probability with the right strategies. The question isn't "is this possible" — it's "can we execute fast enough and smart enough to compete in a market where bots already dominate."

---

## Correction: Polymarket IS Legal in the US

The initial feasibility report (v1) was based on outdated information. Here's the current reality:

- **December 2, 2025**: Polymarket officially relaunched for US users after receiving CFTC Amended Order of Designation
- **Status**: Fully regulated Designated Contract Market (DCM), same classification as Kalshi
- **US access**: Via KYC verification on iOS app, API keys through developer portal
- **API trading**: Explicitly supported — application process + sandbox testing required
- **Automated trading**: Not prohibited. Polymarket's CLOB API is designed for programmatic access. They even maintain an official open-source AI agent framework (`Polymarket/agents` on GitHub)

### State-Level Nuance
- Federally legal, but ~11 states have issued cease-and-desist orders (Nevada, Tennessee, Massachusetts, Connecticut most aggressive)
- California appears available under federal derivatives law
- The core legal question — whether federal CFTC approval preempts state gambling laws — is unresolved in courts
- **Action item**: Verify your specific state's current status before deploying capital

Sources:
- [Polymarket Receives CFTC Approval](https://www.prnewswire.com/news-releases/polymarket-receives-cftc-approval-of-amended-order-of-designation-enabling-intermediated-us-market-access-302625833.html)
- [Polymarket CFTC Approval - CoinDesk](https://www.coindesk.com/business/2025/11/25/polymarket-secures-cftc-approval-for-regulated-u-s-return)
- [Polymarket Returns to US - Reason](https://reason.com/2026/01/04/the-return-of-polymarket/)
- [Polymarket US API Access - QuantVPS](https://www.quantvps.com/blog/polymarket-us-api-available)

---

## The Market Right Now (April 2026)

### Scale
- **Polymarket**: ~$9.55B/month volume, $800K-$1M/day in fee revenue
- **Kalshi**: ~$6B/month volume
- **Combined**: ~$15B+/month, ~$4B/week

### The Bot Ecosystem
This is no longer a niche — bots dominate Polymarket:
- **Only 7.6% of Polymarket wallets are profitable** — ~120,000 traders making money out of 1.5M+
- **Bots**: Average $206K profit at 85%+ win rates
- **Humans**: ~$100K with similar strategies
- The profitable minority is overwhelmingly automated

### Fee Structure (Updated March 30, 2026)
- **Makers**: 0% always (limit orders that add liquidity are free)
- **Takers**: Dynamic by category at 50% probability:
  - Crypto: 1.80% | Sports: 0.75% | Politics: 1.00%
  - Finance: 1.00% | Weather: 1.25% | Geopolitics: FREE
- **Maker rebate**: 20-25% daily rebate of taker fees from counterparty trades

Sources:
- [Polymarket Fees Documentation](https://docs.polymarket.com/trading/fees)
- [Polymarket $1M Daily Fee Flow](https://www.ainvest.com/news/polymarket-1m-daily-fee-flow-bots-arbitrage-liquidity-engine-2604/)
- [Arbitrage Bots Dominate Polymarket - Yahoo Finance](https://finance.yahoo.com/news/arbitrage-bots-dominate-polymarket-millions-100000888.html)

---

## Proven Profitable Strategies (With Real Numbers)

### ~~Strategy 1: Latency Arbitrage (Crypto Short-Term Markets)~~ — DEAD
**UPDATE (April 2026)**: Polymarket introduced dynamic taker fees (~3.15% at 50-cent contracts) that exceed the typical latency arb margin. The documented $515K/month bot went to zero overnight. The 500ms execution delay was also removed. **Do not pursue this strategy.**

Historical context: One bot turned $313 into $414,000 in a single month (15-min BTC markets, 98% win rate). This was real — but the window closed when Polymarket changed its fee structure. This is an important lesson: **platform fee changes can kill strategies overnight.**

### Strategy 2: AI-Powered Sports/Event Arbitrage
Claude-powered bots analyzing event probabilities faster than the market can price them.

**Documented results**:
- **sovereign2013**: $1 → $3.3 million since August 2025 (37,247 predictions, sports arbitrage)
- Largest single win: $1.73M on a college basketball game ($179K pure profit)
- Another Claude bot: $600 → $10,000 in 48 hours
- Another: $2,000 → $12,000 overnight
- **This is our wheelhouse** — Claude API is a core Google Antigravity capability

### Strategy 3: Cross-Platform Arbitrage (Polymarket ↔ Kalshi)
Same event priced differently on two platforms = mathematical profit opportunity.

**Current reality**:
- Average arb window: 2.7 seconds (down from 12.3s in 2024)
- 73% of arb profits captured by sub-100ms execution bots
- Top documented arbers: ~$27K/week ($1.4M/year)
- Still the "most consistent edge" per multiple 2026 guides, but competitive

### Strategy 4: Market Making
Provide liquidity to both sides of a market, earn the spread + Polymarket's liquidity rewards.

**Documented results**:
- One operator: started $10K → earning $200/day, scaled to $700-800/day at peak
- Win rates: 78-85%
- Monthly returns: 1-3%
- Requires $5K+ capital minimum
- Polymarket pays daily USDC rebates for 2-sided liquidity

### Strategy 5: Weather/Niche Trading — BEST CURRENT OPPORTUNITY (Updated)
AI-powered probability assessment in niche markets with the least bot competition.

**Why this is now #1**: Free, publicly available weather data (NOAA forecasts are 85-90% accurate at 1-2 day horizon) vs. Polymarket participants who are retail guessers. The hidden edge: every Polymarket weather market resolves on a specific airport weather station, NOT city center coordinates. Most competing bots use city centers and get 3-8 degrees F error — fatal on tight bucket markets.

**Documented results**:
- Weather bot: $1K → $24K trading London weather markets
- Another: $65K profit across NYC, London, Seoul temperature markets
- Open-source implementation available (`alteregoeth-ai/weatherbot` on GitHub)
- Single weather markets clear $300K-$400K in 24-hour volume
- Starting capital as low as $20-50 USDC for live testing
- Kelly fraction 0.25 with self-calibrating per-city accuracy tracking

Sources:
- [Claude Bot $3.3M - Finbold](https://finbold.com/claude-ai-powered-trading-bot-turns-1-into-3-3-million-on-polymarket/)
- [Claude Bots Making Hundreds of Thousands - Medium](https://medium.com/@weare1010/claude-ai-trading-bots-are-making-hundreds-of-thousands-on-polymarket-2840efb9f2cd)
- [Claude Bot $600 to $10K - Finbold](https://finbold.com/claude-ai-powered-arbitrage-bot-turns-600-into-10000-in-48-hours/)
- [Weather Trading Bots $24K - Dev Genius](https://blog.devgenius.io/found-the-weather-trading-bots-quietly-making-24-000-on-polymarket-and-built-one-myself-for-free-120bd34d6f09)
- [Beyond Simple Arbitrage - Medium](https://medium.com/illumination/beyond-simple-arbitrage-4-polymarket-strategies-bots-actually-profit-from-in-2026-ddacc92c5b4f)
- [How AI Helps Retail Traders - CoinDesk](https://www.coindesk.com/markets/2026/02/21/how-ai-is-helping-retail-traders-exploit-prediction-market-glitches-to-make-easy-money)
- [Best Polymarket Bots 2026 - AgentBets](https://agentbets.ai/guides/best-polymarket-bots-2026/)

---

## The $1M/Week Claim — Revised Assessment

With the corrected data, here's how the math changes:

### What the best documented bot has done
- sovereign2013 (Claude-powered): $3.3M over ~8 months = ~$100K/week average
- But with a single $1.73M win, the distribution is lumpy — not $100K/week steady

### What's realistic at different capital levels

| Strategy | Capital | Monthly Range | Weekly Avg |
|---------|---------|--------------|------------|
| Latency arb (crypto) | $50-100K | $50K-$400K+ | $12K-$100K |
| AI sports/event arb | $10-50K | $10K-$100K+ | $2.5K-$25K+ |
| Cross-platform arb | $100-500K | $20K-$60K | $5K-$15K |
| Market making | $10-50K | $3K-$15K | $750-$3.75K |
| Multi-strategy combined | $100-500K | $80K-$500K+ | $20K-$125K+ |

### Can $1M/week happen?
With $500K+ capital, a multi-strategy system running latency arb + AI-powered event trading + cross-platform arb simultaneously, plus occasional large wins — **$1M/week is possible in peak weeks but not a sustainable average**. A more honest framing: **$50K-$200K/week average with $500K+ capital** is the realistic ceiling for a well-executed system, with occasional $500K+ weeks during high-volatility events (elections, Fed decisions, major sports).

The sovereign2013 bot proves seven-figure months are possible. But it also proves you need thousands of trades to get there — it made 37,247 predictions over 8 months.

---

## What Google Antigravity Brings to This Fight

### Why this is different from a random dev team building a bot

1. **Claude API is already our core tool** — The most successful prediction market bots in 2026 run on Claude. We don't need to figure out how to use it. We use it every day for complex reasoning, NLP, and decision-making. This is our home turf.

2. **MES 3.0 Extraction Pipeline** — We can extract the tacit knowledge from every YouTube walkthrough, blog post, and academic paper about prediction market strategies and encode it into deployable agents. A normal team reads these. We operationalize them.

3. **NBA Betting Infrastructure** — `paper_trader.py`, `live_trader.py`, `bet_tracker.py`, `backtest.py` are battle-tested paper-to-live trading infrastructure. Same workflow, different market.

4. **Polymarket's own AI agent framework is open-source** — `Polymarket/agents` on GitHub. This is the foundation we'd build on.

5. **Multi-strategy orchestration** — Our system is literally designed to route tasks to specialist agents. A multi-strategy trading system (latency arb agent + event analysis agent + cross-platform arb agent + market making agent) is architecturally identical to what we already do with content agents.

6. **Parallel research** — Our research swarm can continuously scan for new strategies, market structure changes, and competitor intelligence. This is an ongoing edge, not a one-time advantage.

---

## Risk Assessment (Honest)

### What could go wrong
1. **Speed competition**: 73% of arb profits go to sub-100ms bots. We'd need low-latency infrastructure (dedicated VPS, Polygon RPC node). Cost: ~$50-200/month.
2. **Strategy alpha decay**: Strategies that work today may not work in 3 months as more bots enter. Must continuously evolve.
3. **State regulatory risk**: If your state issues a cease-and-desist, operations must pause. Check state status first.
4. **Capital risk**: Only 7.6% of wallets are profitable. The 92.4% that lose money thought they had a strategy too.
5. **One-leg execution risk**: In cross-platform arb, filling one side but not the other creates directional exposure.
6. **Fee structure changes**: Polymarket just changed fees March 30, 2026. This will happen again.

### What mitigates the risk
1. **Paper trading before real money** — Our existing paper_trader.py pattern proves strategies work before capital is at risk
2. **Multi-strategy diversification** — Not dependent on any single edge
3. **AI-powered adaptation** — Claude can analyze why trades fail and adjust strategy
4. **Conservative position sizing** — Existing live_trader.py LIMITS pattern prevents catastrophic losses
5. **Kill switches** — Hard stops on daily loss, per-trade loss, and anomaly detection

---

## Recommendation

This is a **strong go** — with the following conditions:

1. **Verify state legal status** before deploying any capital
2. **Start with paper trading** to prove the edge before risking real money
3. **Budget $5-25K for initial live testing capital** (expect to lose 5-15% during calibration)
4. **Multi-strategy from day one** — don't bet everything on a single edge
5. **Infrastructure matters** — low-latency VPS and dedicated RPC node are table stakes, not nice-to-haves
6. **Continuous evolution** — the market changes fast. The system must learn and adapt weekly.

The Claude-powered bot ecosystem on Polymarket is real, documented, and profitable. Google Antigravity is literally an AI orchestration system built on Claude. This is the best-aligned opportunity this system has ever faced.
