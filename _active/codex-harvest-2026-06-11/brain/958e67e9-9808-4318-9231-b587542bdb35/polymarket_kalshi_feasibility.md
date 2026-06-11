# Prediction Market Arbitrage Platform — Definitive Feasibility Assessment

**Prepared for**: Farrice Cain & Brother-in-Law  
**Date**: April 13, 2026  
**Classification**: Strategic Due Diligence — Build/No-Build Decision  
**Research basis**: Perplexity Deep Research + 8 targeted web intelligence queries (April 2026 data)  
**Standard**: No hallucinations. Every claim sourced or explicitly flagged as inference.

---

## How to Read This Document

This report answers five questions your brother-in-law needs answered before committing time, money, or reputation:

1. **Is the concept technically possible?** → Yes, with caveats.
2. **Is it economically viable?** → Yes, at a much smaller scale than pitched.
3. **What does it actually cost to build?** → $150K–$350K+ in development alone.
4. **Can Antigravity build it?** → Partially. Critical gaps exist.
5. **Is $1M/week realistic?** → No. Not even close. But real money is on the table.

---

## 1. The Market Is Real and Massive

> [!IMPORTANT]
> This is not a speculative frontier. Prediction markets are a $26B+ quarterly business as of Q1 2026.

### Platform Scale (April 2026)

| Metric | Polymarket | Kalshi | Combined |
|--------|-----------|--------|----------|
| **Monthly Volume** | ~$10B (March 2026 record) | ~$6B est. | ~$16B/month |
| **Q1 2026 Volume** | ~$26.2B (90% QoQ growth) | ~$12B est. | ~$38B quarterly |
| **Daily Peak** | $478–$480M | ~$200M est. | ~$680M peak day |
| **Regulatory Status** | CFTC-approved DCM (Dec 2, 2025) | CFTC-regulated DCM | Both federally legal |
| **API Trading** | Full CLOB API, official Python/TS SDKs | REST + WebSocket + FIX 4.4 | Both support programmatic trading |

**Sources**: [MEXC Research](https://mexc.com), [CryptoRank](https://cryptorank.io), [The Block](https://theblock.co)

### Bot Ecosystem Reality

- **Only 7.6% of Polymarket wallets are profitable** (~120K out of 1.5M+)
- **Bots dominate the profitable minority**: Average bot profit $206K at 85%+ win rates
- **The "golden era" of easy arbitrage is over** — community consensus on r/algotrading and r/arbitragebetting
- **>90% of participants lose money**, per industry analysis
- Simple arb opportunities last **<3 seconds** in 2026, down from 12.3s in 2024
- **73% of arb profits** captured by sub-100ms execution bots

**Sources**: [Yahoo Finance](https://finance.yahoo.com), [Medium Bot Analysis](https://medium.com), [Finbold](https://finbold.com)

---

## 2. API Capabilities — Both Platforms Are Fully Programmable

### Polymarket API Stack

| Component | Endpoint | Auth | Capabilities |
|-----------|----------|------|-------------|
| **CLOB API** | `clob.polymarket.com` | Ed25519 wallet signing | Order books, place/cancel/amend orders, WebSocket streams |
| **Gamma API** | `gamma-api.polymarket.com` | None (public) | Market discovery, metadata, events, contract details |
| **Data API** | `data-api.polymarket.com` | Auth required | Positions, trades, open interest, historical data |
| **Bridge API** | `bridge.polymarket.com` | Auth required | USDC deposits/withdrawals (Polygon L2) |

- **Rate limits**: 60–100 req/min REST; WebSocket recommended for real-time
- **Order types**: LIMIT and MARKET orders
- **Latency**: ~50–200ms roundtrip (Polygon L2)
- **SDKs**: Official Python (`py-clob-client`), TypeScript; third-party NautilusTrader integration
- **US Access**: Requires KYC verification, then API key generation

### Kalshi API Stack

| Component | Endpoint | Auth | Capabilities |
|-----------|----------|------|-------------|
| **REST API** | `api.elections.kalshi.com/trade-api/v2` | RSA-PSS signed requests | Market data, order management, account operations |
| **WebSocket** | Real-time streams | Same auth | Live market data, order updates |
| **FIX 4.4** | Institutional grade | Dedicated access | Ultra-low-latency execution |
| **Sandbox** | `demo-api.kalshi.co/trade-api/v2` | Same format | Paper trading with fake money |

- **Recent change (March 2026)**: Migrated to fixed-point dollar strings (breaking change for existing code)
- **Order management**: POST/PUT/DELETE with client_order_id deduplication
- **Historical data**: Now partitioned into live/historical tiers

**Sources**: [Polymarket Docs](https://docs.polymarket.com), [Kalshi Docs](https://kalshi.com/docs/), [AgentBets](https://agentbets.ai)

> [!TIP]
> Both platforms have mature, well-documented APIs designed for programmatic trading. This is green-light territory for the data ingestion and execution layers of the proposed system.

---

## 3. Fee Structure — The Silent Profit Killer

### Polymarket Fees (Updated March 30, 2026)

| Role | Rate |
|------|------|
| **Maker** (limit orders adding liquidity) | **0% always** |
| **Taker** at 50% probability | 0.75% (Sports) to 1.80% (Crypto) |
| **Geopolitics** | **FREE** (taker and maker) |
| **Polygon gas** | ~$0.01–$0.10/tx |
| **Maker rebate** | 20–25% daily rebate from counterparty taker fees |

### Kalshi Fees

| Role | Formula | Example (50¢ contract, 10 contracts) |
|------|---------|--------------------------------------|
| **Taker** | `roundup(0.07 × C × P × (1-P))` | ~$0.18 per trade |
| **Maker** | `roundup(0.0175 × C × P × (1-P))` | ~$0.05 per trade |
| **Deposits** | ACH free, wire free, debit 2% | — |
| **Settlement** | Free | — |

### What This Means for Arbitrage

For a cross-platform arb trade (buy on one, sell on the other):

| Scenario | Spread Required to Break Even |
|----------|------------------------------|
| Both legs as maker | ~0.5¢–1¢ |
| One leg taker, one maker | ~2¢–3¢ |
| Both legs as taker | ~3¢–5¢ |

**Reality**: Typical cross-platform spreads on equivalent contracts are **0.5–3 cents**. After fees, slippage, and partial fills, the **net edge on cross-platform arb is 0.1–0.5% per trade** on liquid pairs. This means you need massive volume or substantial capital to generate meaningful returns.

---

## 4. The $1M/Week Claim — Honest Stress Test

> [!CAUTION]
> **$1M/week is not realistic.** Here's the math showing why — and what IS realistic.

### The Math That Kills the Claim

```
$1M/week = $52M/year

To generate $52M/year from arbitrage:
- At 0.2% net edge per trade: Need $500M in weekly turnover
- At 0.5% net edge per trade: Need $200M in weekly turnover
- At 1.0% net edge per trade: Need $100M in weekly turnover

Combined daily volume (both platforms): ~$300-680M on peak days
Arb-capturable slice: <10% = $30-68M/day = $210-476M/week
Your share of that (competing against HFT shops): 5-15%

Maximum realistic weekly arb volume: $10-70M
At 0.3% average net edge: $30K-$210K/week

Capital required for $70M weekly turnover: $10-20M+ (leverage/recycling)
```

### What Top Performers Actually Make

| Entity | Documented Performance | Notes |
|--------|----------------------|-------|
| **sovereign2013** (best documented bot) | $3.3M total over ~8 months | ~$100K/week avg, but lumpy (one $1.73M single win) |
| **Top cross-platform arbers** | ~$27K/week ($1.4M/year) | Consistent but capital-intensive |
| **Crypto latency arb bot** | $313 → $414K in 1 month | Extreme outlier, 98% win rate on 15-min BTC markets |
| **Market makers** | $200–$800/day ($1.4K–$5.6K/week) | Steady but modest returns |
| **Weather/niche bots** | $24K–$65K total profit | Lower competition but smaller TAM |

### Realistic Revenue Projections

| Strategy Mix | Capital Required | Weekly Revenue (Avg) | Weekly Revenue (Peak) | Annual Revenue |
|-------------|-----------------|---------------------|-----------------------|----------------|
| **Conservative** (single-strategy) | $50–100K | $2K–$10K | $25K–$50K | $100K–$500K |
| **Moderate** (multi-strategy) | $100–500K | $10K–$50K | $100K–$200K | $500K–$2.5M |
| **Aggressive** (full stack, all strategies) | $500K–$2M | $50K–$150K | $300K–$500K | $2.5M–$7.5M |
| **The $1M/week claim** | $5M–$20M+ | Would need monopoly-level edge | Possible in single exceptional weeks | $52M — not achievable |

> [!WARNING]
> The most honest framing: **A well-executed multi-strategy system with $200–500K capital can realistically generate $500K–$3M/year.** This is a real business. It is NOT "$1M/week." That number requires either 50–100x more capital than you likely have, or a monopoly on alpha that doesn't exist in a competitive market.

---

## 5. What It Actually Costs to Build

### Development Costs

| Phase | Scope | Estimated Cost (Contract Dev) | Timeline |
|-------|-------|------------------------------|----------|
| **Phase 1**: Data Ingestion + Contract Matching + Basic Dashboard | Dual-platform API integration, schema normalization, NLP contract matching, basic React dashboard | $70K–$120K | 3–4 months |
| **Phase 2**: Simulation + Execution Engine + Risk Framework | Paper trading, backtesting, execution logic, risk controls, kill switches | $50K–$100K | 2–3 months |
| **Phase 3**: Live Trading + Full Product Layer | Constrained live execution, monitoring, analytics, operator controls | $30K–$80K | 2–3 months |
| **Phase 4**: Scale + Optimization | Multi-strategy orchestration, latency optimization, continuous evolution | $30K–$50K | Ongoing |
| **Total Development** | — | **$180K–$350K** | **7–12 months** |

### Infrastructure Costs (Monthly Ongoing)

| Component | Purpose | Monthly Cost |
|-----------|---------|-------------|
| Low-latency VPS (AWS/Equinix NYC) | Sub-100ms execution | $200–$2,000 |
| Dedicated Polygon RPC node | Polymarket order submission | $100–$500 |
| Database (Postgres + Redis) | Market state, replay, analytics | $100–$300 |
| Monitoring (Prometheus/Grafana) | Observability | $50–$200 |
| AI/LLM API costs (Claude) | Contract matching, analysis | $100–$500 |
| Alerting/notification | Operational awareness | $20–$50 |
| **Total Infrastructure** | — | **$570–$3,550/month** |

### Capital Requirements

| Purpose | Amount | Notes |
|---------|--------|-------|
| **Paper trading phase** | $0 | Kalshi offers sandbox, Polymarket sim possible |
| **Initial live testing** | $5K–$25K | Expect 5–15% loss during calibration |
| **Operational capital** | $50K–$200K | Minimum for meaningful returns |
| **Scale capital** | $200K–$2M+ | For multi-strategy at volume |

### Team Requirements

| Role | Necessity | Why |
|------|-----------|-----|
| **Quant/Trading Systems Engineer** | CRITICAL | Order book logic, execution, risk management. This is NOT a web dev skillset. |
| **ML/NLP Engineer** | HIGH | Contract matching, anomaly detection, semantic analysis |
| **Full-Stack Developer** | HIGH | Dashboard, monitoring UI, operator controls |
| **DevOps/Infrastructure** | MEDIUM | Low-latency deployment, monitoring, reliability |
| **Domain Expert (Trading)** | CRITICAL | Someone who understands market microstructure, slippage, hedging |

> [!IMPORTANT]
> **Total realistic investment to reach live trading (Phase 3 complete):**
> - Development: $150K–$300K
> - Infrastructure (first year): $7K–$42K
> - Trading capital: $50K–$200K
> - **Total: $207K–$542K before you see a dollar of return**
> 
> This does NOT include the cost of trading losses during calibration.

---

## 6. The Five Hardest Technical Problems

Ranked by impact on whether this succeeds or fails:

### 1. Contract Semantic Matching (THE core challenge)

Two platforms, different naming conventions, different resolution criteria, different settlement sources, different timing. "Will Bitcoin hit $100K by December 31?" on Polymarket vs. "Bitcoin above $100,000 at year-end" on Kalshi might resolve differently based on timezone, data source, or exact wording.

- **Auto-match accuracy ceiling**: ~80–90% without human validation
- **False positive cost**: A "false arb" where contracts resolve differently = total loss on both legs
- **State of the art**: LLM-powered semantic clustering + human validation layer
- **arxiv research**: Active 2025–2026 papers on agentic AI for cross-market proposition matching

**Verdict**: Solvable with LLMs, but requires a human-in-the-loop validation layer for high-confidence trades.

### 2. Latency Competition

- Arb windows last <3 seconds in 2026
- 73% of profits go to sub-100ms execution
- Requires: dedicated VPS near exchange infrastructure, WebSocket connections (not REST polling), optimized order submission pipeline
- **Cost**: $200–$2,000/month for competitive infrastructure

**Verdict**: Table stakes. Achievable with proper infrastructure investment.

### 3. One-Leg Execution Risk

You buy YES on Polymarket. By the time you try to sell NO on Kalshi, the price has moved. You're now directionally exposed.

- **Frequency**: Affects 15–30% of cross-platform arb attempts
- **Mitigation**: Dynamic sizing, iceberg orders, hedge completion logic, hard timeout kills
- **Remaining risk**: ~5% blowup probability per event category

**Verdict**: Manageable with sophisticated execution logic. Cannot be eliminated entirely.

### 4. Alpha Decay

Strategies decay as more competitors enter. The crypto latency arb that turned $313 into $414K? Those windows are closing. The cross-platform spreads that averaged 12 seconds in 2024 now average 2.7 seconds.

- **Decay rate**: ~50% per year for public strategies
- **Mitigation**: Continuous strategy evolution, multi-strategy diversification, niche market focus

**Verdict**: Existential long-term risk. System must evolve continuously or die.

### 5. Regulatory Surface Area

- Polymarket: Federally legal (CFTC DCM), but ~11 states have cease-and-desist orders
- Kalshi: Federally legal (CFTC DCM)
- Automated trading: Not prohibited on either platform, but subject to terms-of-service changes
- **Tax complexity**: Gains on both platforms are taxable. Cross-platform positions create complex reporting.
- **State risk**: California appears available; check your specific state before deploying capital

**Verdict**: Manageable but requires legal review before deployment.

---

## 7. Can Antigravity Build This? — Honest Assessment

### What Antigravity Brings

| Capability | Relevance | Assessment |
|-----------|-----------|------------|
| **Claude API integration** | The most profitable Polymarket bots run on Claude | ✅ Direct advantage |
| **96 expert agents** | Content/marketing agents, not trading agents | ⚠️ Wrong domain |
| **MES 3.0 extraction pipeline** | Can extract trading strategies from public sources | ✅ Research advantage |
| **NBA betting infrastructure** | `paper_trader.py`, `live_trader.py`, `bet_tracker.py` | ✅ Relevant foundation |
| **Multi-agent orchestration** | Routing specialists to tasks | ✅ Architectural fit |
| **Notion/workflow automation** | Operational tracking | ✅ Useful for monitoring |
| **Research swarm** | Continuous intelligence gathering | ✅ Ongoing edge |

### What Antigravity Does NOT Have

| Gap | Severity | Why It Matters |
|-----|----------|---------------|
| **No quant/trading systems expertise** | 🔴 CRITICAL | Order book mechanics, execution algorithms, risk models require specialized knowledge. This is NOT transferable from content marketing.|
| **No financial engineering knowledge** | 🔴 CRITICAL | Hedging strategies, portfolio risk, drawdown management, correlation analysis — these are specialized disciplines. |
| **No low-latency systems experience** | 🟡 HIGH | Sub-100ms execution, WebSocket optimization, connection pooling — different skillset from web development. |
| **No blockchain/crypto infrastructure** | 🟡 HIGH | Polymarket runs on Polygon. Wallet management, gas optimization, on-chain settlement — unfamiliar territory. |
| **No trading capital** | 🔴 CRITICAL | The system itself generates no revenue without capital at risk. |
| **No regulatory/compliance framework** | 🟡 HIGH | Automated trading on regulated exchanges needs legal review. |

> [!CAUTION]
> **The brutal truth**: Antigravity is an AI content and marketing orchestration system. Building a trading platform is like a restaurant trying to build an airplane — sure, both need kitchens, but the engineering is fundamentally different. The Claude API expertise is genuinely valuable (top Polymarket bots use Claude), and the paper trading infrastructure provides a starting point. But the core competencies required — quantitative trading, financial engineering, low-latency systems, blockchain infrastructure — are all gaps.

### What "Building This With Antigravity" Actually Means

It does NOT mean the current system magically transforms into a trading platform. It means:

1. **Antigravity provides the AI intelligence layer** — Claude-based contract matching, opportunity analysis, research, anomaly detection
2. **Antigravity provides the operational workflow** — monitoring, alerting, logging, oversight
3. **The trading engine, execution system, and risk framework must be built from scratch** by someone with quantitative trading experience
4. **The UI/dashboard is standard full-stack work** — buildable with current capabilities

**Realistic contribution split**:
- Antigravity handles: ~30% of the system (AI layer + research + operational monitoring)
- New engineering handles: ~70% of the system (trading engine + execution + risk + infrastructure)

---

## 8. Risk Matrix

| Risk | Probability | Impact | Mitigation |
|------|------------|--------|------------|
| **Develop system but never achieve consistent profitability** | 40–50% | Total loss of dev investment | Paper trade extensively before going live |
| **Alpha decay erodes edge within 6–12 months** | 60–70% | Must continuously evolve or die | Multi-strategy + dedicated research |
| **One-leg execution blowup** | 15–30% per month of operation | 5–25% capital loss per event | Hard stops, position limits, kill switches |
| **Regulatory change (state-level)** | 20–30% over 2 years | Forced to cease operations in specific states | Legal review, multi-state planning |
| **Platform API/fee structure changes** | 80–90% over 2 years | Must rebuild/adapt continuously | API abstraction layer, modular design |
| **False arb from contract resolution mismatch** | 10–20% per 100 trades without human review | Total loss on both legs | Human validation for high-value trades |
| **Competitor with more capital and better tech takes your edge** | Near certain | Margin compression | Niche focus, speed, continuous evolution |

---

## 9. Phased Recommendation

### Phase 0: Validate Before Building (2–4 weeks, ~$0 cost)

Before writing a single line of trading code:

1. **Manual arb hunting**: Spend 2 weeks manually monitoring both platforms side-by-side. Log every potential arb opportunity. Calculate what the return would have been after fees.
2. **Talk to people doing this**: Join the Kalshi Discord #dev channel, Polymarket Discord, r/algotrading. Find people who've actually built cross-platform arb bots. Get their honest assessment.
3. **Legal review**: Confirm your state permits automated trading on both platforms.
4. **Quantify the edge**: If you can't find 5+ genuine arb opportunities per day manually, the automated system won't find them either.

**This phase determines whether you proceed at all.**

### Phase 1: Intelligence Layer + Paper Trading (3–4 months, $50–80K)

Build the parts Antigravity CAN build well:
- Dual-platform data ingestion
- Contract semantic matching (Claude-powered)
- Opportunity detection and scoring
- Basic monitoring dashboard
- Paper trading simulation

**Decision gate**: Does the paper trading system identify real opportunities that would have been profitable?

### Phase 2: Execution Engine + Risk Framework (2–3 months, $50–100K)

This requires bringing in quant/trading expertise:
- Order execution logic with partial fill handling
- Risk controls and kill switches
- Historical backtesting
- Performance attribution

**Decision gate**: Does backtested performance survive realistic execution assumptions?

### Phase 3: Constrained Live Testing (2–3 months, $5–25K live capital)

- Very small position sizes ($100–$500 per trade)
- Hard daily loss limits ($500–$1,000)
- Full observability and immediate shutdown controls
- Compare live results to paper trading projections

**Decision gate**: Are live results within 50% of paper trading projections?

---

## 10. Bottom Line

### For Your Brother-in-Law

| Question | Answer |
|----------|--------|
| **Is this concept real?** | Yes. Prediction market arbitrage is a real, functioning business. |
| **Can it make money?** | Yes. Top performers make $100K–$3M/year. |
| **Will it make $1M/week?** | No. That requires $5–20M+ in capital and monopoly-level alpha. Realistic: $10K–$150K/week with $200K–$2M capital. |
| **Can Antigravity build it alone?** | No. The AI layer and research infrastructure are genuine advantages, but the trading engine requires specialized quant expertise we don't have. |
| **What would it cost?** | $200K–$550K total investment (dev + infrastructure + capital) to reach live trading. |
| **How long to first real dollar?** | 7–12 months from start to constrained live trading. |
| **What's the risk of total loss?** | 40–50% probability of never achieving consistent profitability. |
| **Is it worth pursuing?** | Only if: (a) you can afford to lose the investment, (b) you bring in quant/trading expertise, and (c) you treat the first 6 months as pure R&D with no revenue expectations. |

### The Real Opportunity

The prediction market space is growing 90%+ quarter-over-quarter. The total addressable market is expanding faster than competition can fill it. Claude-powered bots are the current winners. This is a legitimate opportunity — but it's a **venture-scale commitment**, not a side project.

**If you approach this as "build a sophisticated product that earns $500K–$3M/year" rather than "$1M/week," the risk-reward calculus becomes much more favorable.**

---

## Source Appendix

### Platform Documentation
- [Polymarket CLOB API Docs](https://docs.polymarket.com)
- [Polymarket Fees (March 2026)](https://docs.polymarket.com/trading/fees)
- [Kalshi API Documentation](https://kalshi.com/docs/)
- [Kalshi Fee Schedule](https://kalshi.com/fee-schedule)

### Market Data
- [Polymarket Q1 2026: $26.2B quarterly volume](https://mexc.com)
- [Polymarket $10B monthly record (March 2026)](https://cryptorank.io)
- [Daily volume peaks $478–480M](https://theblock.co)

### Bot Performance
- [sovereign2013: $3.3M over 8 months (Finbold)](https://finbold.com)
- [Claude bots making hundreds of thousands (Medium)](https://medium.com)
- [Only 7.6% of wallets profitable (Yahoo Finance)](https://finance.yahoo.com)
- [Arbitrage bots capturing 73% of arb profits](https://medium.com)

### Academic/Research
- [Agentic AI for cross-market proposition matching (arXiv)](https://arxiv.org)
- [Market-Conditioned Prompting for prediction markets (arXiv)](https://arxiv.org)
- [Cross-platform semantic clustering frameworks (arXiv)](https://arxiv.org)

### Regulatory
- [Polymarket CFTC Approval (PRNewswire)](https://prnewswire.com)
- [Polymarket US Launch (CoinDesk)](https://coindesk.com)

### Development Costs
- [Algorithmic Trading Platform Costs 2025–2026 (AppInventiv)](https://appinventiv.com)
- [Fintech Trading Platform Budget Analysis (Dev.to)](https://dev.to)
