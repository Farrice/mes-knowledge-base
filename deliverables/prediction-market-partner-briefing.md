# Prediction Market AI Trading System — Partner Briefing

**Prepared by**: Farrice Cain (System Architect)
**Date**: April 14, 2026
**Status**: System built through Phase 2 of 6. Ready for funded testing.
**Classification**: Confidential — for partner decision-making only.

---

## What This Is

An AI-powered multi-strategy trading system for Polymarket, the largest prediction market platform (~$9.5B/month volume, CFTC-regulated since December 2025). The system uses Claude AI and multiple data sources to identify mispriced markets and execute trades automatically.

This is not theoretical. Claude-powered bots are already the most profitable traders on Polymarket:

- **sovereign2013**: $1 → $3.3 million in 8 months (37,247 trades, sports arbitrage, Claude-powered)
- **Weather bots**: $1K → $24K, another at $65K profit (temperature market arbitrage)
- **Only 7.6% of Polymarket wallets are profitable** — nearly all of them are automated bots

The system I built reverse-engineered HOW these bots work by extracting 3,947 lines of expert intelligence from their source code, academic papers, and on-chain wallet analysis.

---

## What Was Built (Phases 0-2 Complete)

### Phase 0: Intelligence Extraction (Complete)
Deep analysis of every successful Polymarket bot strategy:
- 4 extraction reports (weather trading, sports arbitrage, market making, risk management)
- Source material: 7,281 lines of production bot code, academic papers, wallet analytics
- Encoded into 4 deployable AI skills with 12 specialized workflows

### Phase 1: Data Infrastructure (Complete)
A 9-module Python trading platform:
- Real-time connection to Polymarket APIs (market data, order books, prices)
- Weather forecast pipeline (ECMWF, HRRR, METAR — 20 cities, 4 continents)
- Risk management engine (8-check validation chain, automatic kill switch)
- Paper trading simulator (tests strategies against real market data without risking money)
- **Two-key safety gate**: Live trading requires BOTH a config change AND an environment variable. Impossible to accidentally trade real money.
- **First paper trade already executed**: London weather market

### Phase 2: Intelligence Layer (Complete)
4 new modules connecting the AI intelligence to the trading pipeline:
- **Sports Arbitrage Engine**: Fetches odds from 348 sportsbooks (including Pinnacle — the sharpest book), strips the house edge to get true probabilities, compares against Polymarket prices, identifies gaps
- **AI Ensemble Engine**: 3 independent AI models analyze political, economic, and tech markets from different angles, then combine estimates using the same Bayesian method proven in academic research
- **Market Selection Engine**: Scores and ranks opportunities across ALL strategies on a unified scale, allocates capital according to risk-adjusted portfolio rules
- **Strategy Orchestrator**: The brain — routes each market to the right analysis pipeline, collects the best opportunities, feeds them through risk validation

### Current System Status
```
Strategy Pipelines:
  Weather:       Active (20 cities, 3 forecast sources)
  Sports Arb:    Built — needs API key to activate ($49/mo)
  AI Ensemble:   Built — needs API keys to activate (~$10/mo)
  Market Making: Intelligence built, execution deferred to Phase 4

Paper Trading:   1 position open (London weather, $20 deployed)
Balance:         $980 of $1,000 paper money
Kill Switch:     Normal (not triggered)
```

---

## What's Left to Build (Phases 3-6)

| Phase | What | Duration | Capital Needed | Purpose |
|-------|------|----------|----------------|---------|
| **3** | Paper Trading Accumulation | 30-60 days | $0 (simulated) | Prove the system works: 200+ trades, measure real edge, calibrate parameters |
| **4** | Dashboard + Monitoring | 1-2 weeks | $0 | Visual performance tracking, alerts, daily reports |
| **5** | Live Testing | 30-60 days | $500-$5,000 | Real money, small positions, graduated deployment ($50 → $500 → $5K) |
| **6** | Scale | Ongoing | $5,000-$100,000+ | Full multi-strategy deployment, continuous optimization |

---

## Cost Model — What It Takes to Run This

### Tier 1: Paper Trading (Phase 3) — Prove It Works

No trading capital required. Just infrastructure to run the system against real market data in simulation mode.

| Item | Monthly Cost | Notes |
|------|-------------|-------|
| Sportsbook odds API | $30-49 | The Odds API ($30) or OddsPapi ($49) for Pinnacle access |
| AI ensemble (3 cheap models) | $8-15 | Claude Haiku + GPT-4o-mini + Gemini Flash |
| Bot hosting | $0 | Can run on any home computer during paper phase |
| Polygon RPC | $0 | Alchemy free tier (30M compute units/mo) |
| Polygon gas fees | $0 | Paper trading doesn't touch the blockchain |
| **Total** | **$38-64/mo** | |

**Duration**: 30-60 days to accumulate 200+ paper trades
**Total Phase 3 cost**: $75-130
**What you get**: Statistical proof of whether the system's edge is real before risking a single dollar

### Tier 2: Small Live Testing (Phase 5) — First Real Money

| Item | Monthly Cost | Notes |
|------|-------------|-------|
| Sportsbook odds API | $30-49 | Same as above |
| AI inference (Claude + ensemble) | $15-40 | With prompt caching, 50-100 decisions/day |
| VPS (24/7 hosting) | $6-60 | $6 budget (Hostinger) to $60 trading-optimized (QuantVPS) |
| Polygon RPC | $0 | Free tier sufficient at this volume |
| Polygon gas per trade | ~$0.007 | Negligible — $2-4/mo at 10-50 trades/day |
| **Total operational** | **$55-150/mo** | |
| **Trading capital (one-time)** | **$2,000-$5,000** | Deployed on Polymarket as USDC |

**Why home computer works**: Our strategies exploit 2-15 minute windows (sports arb) and multi-hour windows (weather). The 50-150ms latency of a home connection is irrelevant when the edge window is measured in minutes. A dedicated low-latency VPS ($60-100/mo) only matters for cross-platform arbitrage where windows are 2.7 seconds. We don't do that.

**Expected returns at $5K capital (conservative, with 0.5x-0.7x live haircut applied)**:
- Weather strategy alone: $100-$500/mo (2-10% monthly)
- Weather + Sports arb: $200-$1,250/mo (4-25% monthly)
- Note: Documented weather bots turned $1K into $24K. Our system uses the same ICAO station precision edge.

### Tier 3: Full Scale (Phase 6) — Real Operation

| Item | Monthly Cost | Notes |
|------|-------------|-------|
| Trading-optimized VPS | $60-100 | QuantVPS Pro, US-East (near Polymarket servers) |
| Private Polygon RPC | $49 | Chainstack Growth — prevents front-running |
| AI inference (full models) | $40-80 | Claude Sonnet + GPT-4o + Gemini Pro, cached |
| Sportsbook odds | $49 | OddsPapi with Pinnacle + WebSocket streaming |
| **Total operational** | **$200-280/mo** | |
| **Trading capital** | **$25,000-$100,000** | |

**Expected returns (conservative, with 0.5x haircut applied)**:

| Capital | Strategy Mix | Monthly Return (Conservative) | Monthly Return (Balanced) |
|---------|-------------|-------------------------------|---------------------------|
| $25,000 | 80% arb / 20% reserve | $1,050 (4.2%) | $2,925 (11.7%) |
| $50,000 | 80% arb / 20% reserve | $2,100 (4.2%) | $5,850 (11.7%) |
| $100,000 | 50% arb / 30% AI / 20% reserve | $4,200 (4.2%) | $11,700 (11.7%) |

These numbers come from academic research and on-chain analysis of profitable wallets. The conservative allocation (80% arbitrage / 20% reserve) has a documented Sharpe ratio of 2.1 with max drawdown of 0.8%.

**Profit margins are extreme**: Documented profitable bots spend $80-150/mo on infrastructure while generating $24K-$3.3M. Infrastructure is less than 0.1% of gross at scale. The constraint is edge quality, not overhead.

**Important caveat**: sovereign2013's $3.3M run involved 37,247 trades over 8 months with capital rotation (each dollar deployed dozens of times). Returns scale with both capital AND trading velocity.

---

## What the System Actually Does (Non-Technical)

Think of it as three employees who never sleep:

1. **The Weather Analyst** watches 20 cities worldwide and knows the exact airport weather station each market resolves on. When the forecast says 72°F and the market is priced as if it'll be 68°F, the system buys.

2. **The Sports Scout** watches every sportsbook in real time. When Vegas says the Lakers have a 62% chance of winning but Polymarket is priced at 55%, the system buys. The sportsbooks have billion-dollar incentives to be accurate. Polymarket participants are mostly retail guessers.

3. **The AI Council** convenes three independent AI analysts for political, economic, and tech events. Each analyzes separately (so they don't influence each other), then their estimates are combined. When they collectively disagree with the market by more than 5%, the system acts.

Every trade goes through an 8-point safety check before execution. If the system hits a bad streak, the automatic kill switch halts ALL trading until a human reviews what happened.

---

## Risk Disclosure (Honest)

1. **92.4% of Polymarket wallets lose money.** We built this system to be in the 7.6%, but past bot performance doesn't guarantee our results.

2. **The paper-to-live gap is real.** Backtests always look better than live trading. Our system applies a 0.5x-0.7x haircut to account for slippage, fees, and latency.

3. **Strategies decay.** What works today may not work in 6 months as more bots enter. The system must continuously evolve.

4. **Platform risk.** Polymarket changed its fee structure on March 30, 2026 and killed an entire category of profitable bots overnight. This can happen again.

5. **Regulatory risk.** Polymarket is federally legal (CFTC-approved) but ~11 states have restrictions. Verify your state before deploying capital.

6. **Capital risk.** Only invest what you can afford to lose entirely. The graduated deployment plan ($50 → $500 → $5K) exists to limit early losses while the system calibrates.

---

## The Decision Points

### For Phase 3 (Paper Trading): ~$75-130 total
No trading capital at risk. This proves whether the edge is real before any money goes on the line. Can run from a home computer. **This is the minimum investment to get a data-backed answer on whether to proceed.**

### For Phase 5 (Live Testing): $2,000-$5,000 trading capital + ~$55-150/mo infrastructure
Real money, small positions. The system graduates through increasingly larger positions only after proving profitability at each level.

### For Phase 6 (Scale): $25,000-$100,000+ capital + ~$200-280/mo infrastructure
Full multi-strategy deployment. This is where the numbers get meaningful.

---

## Deal Structure Options

This system was designed and built by Farrice Cain using proprietary AI orchestration infrastructure. The following options are available:

### Option A: Partnership (Recommended)
- **Partner funds**: All infrastructure costs + trading capital
- **Farrice provides**: The system, ongoing maintenance, strategy evolution, monitoring
- **Profit split**: Negotiable (suggested starting point: 30% builder / 70% capital, adjustable after Phase 5 results)
- **IP ownership**: Remains with Farrice. System is licensed to the partnership.
- **Maintenance commitment**: Weekly system checks, monthly strategy review, quarterly evolution cycle
- **Exit terms**: Either party can exit with 30-day notice. System returns to Farrice. Partner retains any profits earned.

### Option B: Monthly Retainer + Smaller Split
- **Partner funds**: All infrastructure costs + trading capital
- **Farrice receives**: $500-$1,000/mo retainer for maintenance + 10-15% of net profits
- **Advantage**: Guaranteed income for Farrice regardless of trading performance
- **IP ownership**: Remains with Farrice

### Option C: Turnkey Handoff
- **One-time fee**: $5,000-$10,000 for the complete system
- **Partner receives**: Full codebase, documentation, deployment guide
- **Farrice provides**: 30 days of setup support, then done
- **Ongoing maintenance**: Partner's responsibility (or separate maintenance contract)
- **IP ownership**: License to use; Farrice retains right to use the system himself
- **Risk for partner**: System requires AI expertise to maintain and evolve. Without ongoing optimization, strategies will decay.

### Option D: Walk Away
- **Cost**: $0
- **What happens**: System sits idle. No money made, no money lost.
- **The system remains**: Farrice retains everything built. Can deploy independently or find another partner.

---

## Recommended Next Step

**Fund Phase 3 (~$75-130 total) and let the system prove itself.**

This is the lowest-risk path. No trading capital at risk. The system runs against real market data in simulation mode for 30-60 days. The only costs are API keys for sportsbook data and AI inference.

At the end of Phase 3, we have hard numbers:
- Win rate by strategy (weather, sports, AI ensemble)
- Profit factor (how much we win vs how much we lose)
- Edge distribution (are we finding 5% edges or 15% edges?)
- Data-backed projection for live returns with the 0.5x haircut applied

If the numbers are good → proceed to Phase 5 with confidence and $2-5K capital.
If the numbers disappoint → total investment lost is $130, not $25,000.

---

## Technical Appendix: What's Under the Hood

For reference, the complete system inventory:

| Component | Count | Description |
|-----------|-------|-------------|
| Python modules | 13 | Core trading platform |
| AI skill files | 4 skills, 12 workflows | Encoded expert intelligence |
| Extraction reports | 4 reports, 3,947 lines | Reverse-engineered bot strategies |
| CLI commands | 6 | Operational control interface |
| Lines of code | ~6,500 | Production Python |
| Lines of intelligence | ~17,400 | Skills, workflows, extractions |
| Total system | ~23,900 lines | |

**Technology stack**: Python 3.11+, Polymarket CLOB/Gamma APIs, OddsPapi, Open-Meteo (weather), Claude/GPT-4o/Gemini (ensemble), JSON state persistence with atomic writes.

**Safety architecture**: Two-key live trading gate, 8-check order validation chain, one-way kill switch, quarter-Kelly position sizing, 5 exit mechanisms per position, dual-cadence monitoring (defense every 10 min, offense every 60 min).
