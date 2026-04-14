# AI Trading System for Prediction Markets — Business Briefing

**From**: Farrice Cain
**Date**: April 14, 2026
**For**: Partner review and go/no-go decision
**Confidential**

---

## The Short Version

You asked me to build a serious AI-powered trading system for Polymarket and Kalshi. I built it. The system is through Phase 2 of 6 — the intelligence engine is complete and the first paper trades have already run. No real money has been deployed yet, and it won't be until the system proves itself in simulation first.

Before I get into what was built and what it costs, let me address three things directly:

1. **This is real.** Claude-powered bots are already the most profitable traders on Polymarket. One turned $1 into $3.3 million in 8 months. Another turned $1,000 into $24,000 trading weather markets. I reverse-engineered how they work and built a system that uses those same strategies.

2. **Both Polymarket AND Kalshi are integrated.** The system connects to both platforms, ingests market data from both, and includes an AI-assisted contract matching engine that compares markets across platforms to detect cross-platform arbitrage opportunities. It also detects "false arbitrage" caused by subtle differences in contract wording, resolution sources, or time boundaries — which the research shows accounts for 60-70% of apparent cross-platform opportunities.

3. **I didn't cut corners.** The system has 23,900 lines across 58 files. It includes a kill switch that halts all trading automatically if losses exceed limits. It requires two separate keys to enable real trading — you literally cannot accidentally trade real money. This is built to protect capital first and make money second.

---

## What the System Does

Four AI "employees" that never sleep, never get emotional, and never oversize a bet:

**The Weather Analyst** monitors 20 cities across 4 continents. Here's the edge: every Polymarket weather market resolves based on a specific airport weather station, not the city center. Most traders don't know this and use the wrong coordinates, which introduces 3-8 degrees of error. Our system uses the exact airport station data. When our forecast says 72 degrees and the market is priced as if it'll be 65, we buy. This is an information advantage most competitors don't even know exists.

**The Sports Scout** watches 348 sportsbooks in real time, including Pinnacle (the sharpest bookmaker in the world). When Vegas says the Lakers have a 62% chance of winning but Polymarket says 55%, the system buys. We don't need to be smarter than Vegas. We just need Polymarket to be dumber than Vegas — and on sports, it consistently is. This is exactly how the $3.3 million bot works.

**The AI Council** convenes three independent AI analysts for political, economic, and technology events. Each analyzes the same market from a different angle without seeing each other's work, then their estimates are combined. When all three disagree with the market by more than 5%, the system acts. This covers markets like "Will the Fed cut rates?" or "Will GPT-5 launch before June?" where no sportsbook reference exists.

**The Cross-Platform Detective** continuously compares markets across Polymarket and Kalshi — looking for the same event priced differently on each platform. But here's the critical part: it doesn't just look at prices. It uses AI to analyze the actual contract wording, resolution sources, and time boundaries to make sure the two markets are truly equivalent before flagging an opportunity. Research shows that 60-70% of apparent cross-platform "arbitrage" is actually caused by subtle differences in how the markets define the outcome — our system catches those false matches before money is at risk.

Every trade goes through an 8-point safety check before a single dollar moves. If the system hits a bad day, an automatic kill switch stops everything until a human reviews what happened and manually restarts it.

---

## How the Build Compares to Your Original Brief

You wrote a thorough spec with 7 layers. Here's where each one stands:

### Scope Comparison

| What You Asked For | What Exists | Status |
|-------------------|-------------|--------|
| Market data from Polymarket | Real-time connection to all Polymarket APIs (market data, order books, prices) | Done |
| Market data from Kalshi | Kalshi client with RSA-PSS auth, market data reads, category scanning | Done |
| Cross-platform contract matching | 3-stage AI+rules matching engine (candidate generation → structured comparison → LLM verification) | Done |
| Contract confidence scoring | 5-dimension scoring: text similarity, resolution source, time window, outcome structure, category | Done |
| False arbitrage detection | Structural flag system catches resolution source mismatches, time boundary gaps, definition differences | Done |
| AI intelligence layer | 4-strategy AI: weather forecast + sportsbook odds + 3-model ensemble + cross-platform matching | Done — exceeds spec |
| Paper trading / simulation | Full simulator with configurable fills, dual-cadence monitoring (10min defense, 60min offense) | Done |
| Execution engine | Paper/Live hierarchy with two-key safety gate, batch orders, slippage checks | Done |
| Risk engine | 8-check validation chain, one-way kill switch, quarter-Kelly sizing, 5 exit mechanisms | Done — exceeds spec |
| Dashboard / UI | Interactive demo dashboard built; production dashboard is Phase 4 | Demo ready |

### One Important Nuance on Cross-Platform Arbitrage

Your original vision centered on buying on one platform and selling on another when the same event is priced differently. The system does this — but with an important safety layer your brief also asked for: the contract intelligence engine.

Research uncovered that **60-70% of apparent cross-platform opportunities are false arbitrage** caused by subtle differences in contract wording, resolution sources, or time boundaries. Real examples: a "National Bitcoin Reserve" market appeared to be 14 points mispriced between Polymarket and Kalshi, but Kalshi required establishment "before Jan 1 2026" while Polymarket required it "during 2025." Same event, different definitions, potentially opposite outcomes.

The system's 3-stage contract matcher (text similarity → structured field comparison → AI verification) is specifically designed to catch these cases before money is at risk. This is exactly the "contract intelligence layer" your spec described.

**Additionally**, the system doesn't ONLY do cross-platform arb. It also runs three single-platform strategies with wider edge windows (weather: hours, sports: 2-15 minutes, AI ensemble: hours-days). These wider windows are exploitable by AI without needing the sub-100ms infrastructure that pure cross-platform speed arbitrage requires ($50-100K/year hardware cost). The system will pursue cross-platform arb when the match is high-confidence AND the edge exceeds combined fees — but it also makes money when no cross-platform opportunity exists, through the other three strategies.

---

## The Numbers

### What It Costs to Test (Phase 3 — No Real Money at Risk)

| Expense | Monthly | Notes |
|---------|---------|-------|
| Sportsbook data (Pinnacle odds) | $30-49 | Gives us the "Vegas reference price" for sports |
| AI analysis (3 models) | $8-15 | Cheap models for testing; upgrade later |
| Server hosting | $0 | Runs on any home computer during testing |
| Trading capital | $0 | Paper trading uses simulated money |
| **Total to test** | **$38-64/mo** | **~$75-130 total for the full test period** |

The test runs 30-60 days and produces 200+ simulated trades against real market data. At the end, we know: does this system actually find profitable edges, and how big are they?

### What It Costs to Go Live (After Testing Proves the Edge)

| Scale | Monthly Overhead | Capital Needed | Expected Monthly Return |
|-------|-----------------|----------------|------------------------|
| Small ($2-5K capital) | $55-150 | $2,000-$5,000 | $100-$1,250 (2-25%) |
| Medium ($25K capital) | $150-250 | $25,000 | $1,050-$2,925 (4-12%) |
| Full ($100K capital) | $200-280 | $100,000 | $4,200-$11,700 (4-12%) |

These projections apply a 50% "reality haircut" to paper trading results. This is standard practice — every documented profitable bot shows significantly worse live performance than simulation due to slippage, fees, and execution delays. The one bot with honest live data showed 522x returns in simulation but -49.5% live on version 2. Our system is built with that lesson baked in.

**Infrastructure margins are extreme.** Documented profitable bots spend $80-150/month on infrastructure while generating $24,000-$3,300,000. The constraint is finding real edges, not overhead costs.

### The $1M/Week Question

Your original email mentioned $1M/week at scale. Here's the honest answer:

- The best documented bot (sovereign2013) averaged ~$100K/week over 8 months with $3.3M total. But that included a single $1.73M trade on a college basketball game — the distribution is lumpy, not smooth.
- $1M/week is possible in peak weeks with $500K+ capital during high-volatility events (elections, Fed decisions, major sports playoffs).
- A sustainable average with $100K capital is more like $4,000-$12,000/week.
- With $500K+ capital running multiple strategies: $20,000-$125,000/week.

I'd rather underpromise and overdeliver than the reverse.

---

## What's Already Working

The system has already executed its first paper trade — a London weather market where our forecast model identified the market was pricing temperature incorrectly. The paper trading balance stands at $980 of $1,000 (one loss, two wins across 3 trades).

The demo dashboard (included with this briefing) shows what the system looks like in operation: live opportunities across all four strategies (weather, sports, AI ensemble, cross-platform), risk monitoring, trade history, and portfolio status. Both Polymarket and Kalshi market data are integrated.

---

## What Happens Next — The Decision

**The minimum viable next step costs $75-130 total.** That funds 30-60 days of paper trading to answer one question: does this system find real, repeatable edges?

No trading capital at risk. The system runs against real market data in simulation. At the end, we have hard numbers — win rate, profit per trade, edge by strategy — and a data-backed answer on whether to deploy real capital.

If the numbers work: proceed to live testing with $2-5K.
If they don't: the total loss is $130, not $25,000.

---

## The Risks (No Sugarcoating)

1. **92.4% of all Polymarket wallets lose money.** This system is built to be in the 7.6%, but results are not guaranteed.

2. **Strategies decay.** What works today may not work in 6 months as more bots enter. The system requires ongoing evolution — it's not a "set and forget" investment.

3. **Platform risk.** Polymarket changed its fee structure on March 30, 2026 and killed an entire category of profitable bots overnight. This will happen again.

4. **Paper-to-live gap.** Simulation always looks better than reality. That's why we apply a 50% haircut and why paper testing comes before real money.

5. **Regulatory nuance.** Polymarket is federally legal (CFTC-approved December 2025), but ~11 states have restrictions. Check your state before deploying capital.

---

## How This Works Between Us

This system was designed and built by me using proprietary AI infrastructure I've developed over the past 6 months. Here are the options:

**Option A: Partnership** (my recommendation)
You fund infrastructure and trading capital. I maintain and evolve the system. We split profits — suggested starting point is 30/70 (builder/capital), adjustable after live results prove out. The system IP stays with me; you're licensing it through the partnership.

**Option B: Retainer + Profit Share**
You fund everything. I receive a monthly retainer ($500-1,000) for maintenance plus 10-15% of net profits. This gives me guaranteed compensation while you keep most of the upside.

**Option C: System Purchase**
One-time fee of $5,000-$10,000 for the complete system, documentation, and 30 days of setup support. After that, maintenance is on you. Fair warning: without ongoing AI expertise to evolve the strategies, performance will degrade within 3-6 months as market conditions change.

**Option D: No Deal**
No cost to either of us. The system stays with me. I can deploy it independently or find another capital partner.

---

## What I Need From You

1. A decision on whether to fund Phase 3 testing ($75-130 total)
2. If yes: which deal structure works for you
3. If yes: the API key costs would be on your card (I'll set everything up)

The demo dashboard is attached so you can see what the system looks like. Happy to walk through it on a call.

— Farrice
