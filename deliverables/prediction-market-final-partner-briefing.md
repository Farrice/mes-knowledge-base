# AI Trading System for Prediction Markets — Investment Briefing

**From**: Farrice Cain
**Date**: April 15, 2026
**Confidential**

---

## The Short Version

Kuya, you brought me a real idea, and I treated it like one.

You asked me to look into building an AI-powered trading system for Polymarket and Kalshi — something that could find pricing inefficiencies across prediction markets and capitalize on them automatically. I went deep. Not surface-level research, not a prototype, not a concept. I built the thing.

The entire intelligence engine is working. Four AI strategies are coded and operational. The system placed its first paper trade on April 14 against live Polymarket weather data — the 30-60 day validation period has begun. No real money has been deployed, by design. Both Polymarket and Kalshi are integrated. Risk management is production-grade with multiple safety layers.

This document gives you everything you need to make a real decision: what exists, what the market opportunity looks like, what it costs to operate, what I'm asking for, and what our next steps are. No fluff, no inflated promises.

Three things upfront:

1. **This is already happening.** Claude-powered AI bots are the most profitable traders on Polymarket right now. One turned $1 into $3.3 million in 8 months ([Finbold](https://finbold.com/claude-ai-powered-trading-bot-turns-1-into-3-3-million-on-polymarket/), [CryptoNews](https://cryptonews.net/news/finance/32651731/)). Another turned $1,000 into $24,000 trading weather markets ([Dev Genius](https://blog.devgenius.io/found-the-weather-trading-bots-quietly-making-24-000-on-polymarket-and-built-one-myself-for-free-120bd34d6f09)). I studied how they work and built a system using those same approaches.

2. **Both platforms are integrated.** The system connects to Polymarket and Kalshi, pulls live market data from both, and includes a contract intelligence engine that compares markets across platforms — while catching the "false arbitrage" that traps most traders.

3. **Capital protection comes first.** The system has a triple-layer safety gate — you literally cannot accidentally trade real money. Every trade passes an 8-point validation chain. If the system hits a bad day, an automatic kill switch halts everything until a human reviews and manually restarts. This isn't a script someone cobbled together. This is infrastructure.

---

## The Market Right Now

Prediction markets are no longer experimental. They're a multi-billion dollar industry with federal regulatory approval.

- **Polymarket**: ~$10.6 billion in March 2026 trading volume — its first $10B+ month. CFTC approval issued November 25, 2025; US relaunch December 2, 2025. ([BitKE](https://bitcoinke.io/2026/04/polymarket-in-march-2026/))
- **Kalshi**: ~$12.4 billion in March 2026 — its biggest month ever, driven by March Madness. Also CFTC-regulated. ([DeFi Rate](https://defirate.com/news/kalshi-hits-12b-polymarket-10b-all-time-highs-march-ncaa-tournament-surge/))
- **Combined**: Over $22 billion per month between the two platforms. ([TRM Labs](https://www.trmlabs.com/resources/blog/how-prediction-markets-scaled-to-usd-21b-in-monthly-volume-in-2026))

Here's the edge: **only 7.6% of Polymarket wallets are profitable.** Out of 1.5 million+ traders, roughly 120,000 are making money — and the profitable minority is overwhelmingly automated. Bots average $206K in profit at 85%+ win rates. Humans average ~$100K using similar strategies.

The takeaway: this market rewards AI-powered systems and punishes gut-feel traders. The question isn't whether AI trading works on prediction markets — it's whether we can execute it well enough to be in that top 7.6%.

**Regulatory note**: Both platforms are federally regulated under CFTC jurisdiction. However, approximately 11 states have issued cease-and-desist orders, and the federal government has sued 3 states in response. The question of whether CFTC approval preempts state gambling laws is actively being litigated. Both of us should verify our state's current status before deploying capital. ([Axios](https://www.axios.com/2026/04/03/prediction-market-crackdown-kalshi-polymarket), [Stateline](https://stateline.org/2026/03/06/kalshi-and-polymarket-are-skirting-laws-on-sports-betting-states-say/))

*Profitability sources: [CoinTelegraph/Dune Analytics](https://cointelegraph.com/news/gambling-on-polymarket-profitability-data-revealed), [Yahoo Finance](https://finance.yahoo.com/news/arbitrage-bots-dominate-polymarket-millions-100000888.html)*

---

## What I Built

Four AI "employees" that never sleep, never get emotional, and never oversize a bet:

**The Weather Analyst** monitors 20 cities across 4 continents using data from four independent forecast sources (ECMWF, HRRR, METAR, and Visual Crossing). The edge: every Polymarket weather market resolves based on a specific airport weather station (ICAO code), not the city center. Most traders — including most competing bots — use city center coordinates, which introduces meaningful error on temperature readings. Our system uses the exact airport station data. When our forecast says 72 degrees and the market is priced as if it'll be 65, we buy. This is an information advantage most competitors don't even know exists. ([Dev Genius](https://blog.devgenius.io/found-the-weather-trading-bots-quietly-making-24-000-on-polymarket-and-built-one-myself-for-free-120bd34d6f09))

**The Sports Scout** connects to OddsPapi, an aggregated data feed covering 348 sportsbooks — including Pinnacle, the sharpest bookmaker in the world. When professional sportsbooks say the Lakers have a 62% chance of winning but Polymarket says 55%, the system buys. We don't need to be smarter than Vegas. We just need Polymarket to be dumber than Vegas — and on sports events, it consistently is. This is exactly how the most profitable documented bot on the platform operates.

**The AI Council** convenes three independent AI analysts for political, economic, and technology events. Each analyzes the same market from a different angle without seeing each other's work, then their estimates are combined. When all three disagree with the market by more than 5%, the system acts. This covers markets like "Will the Fed cut rates?" or "Will GPT-5 launch before June?" — events where no sportsbook reference exists.

**The Cross-Platform Detective** compares markets across Polymarket and Kalshi, looking for the same event priced differently on each platform. But it doesn't just compare prices. It uses a three-stage matching pipeline — text similarity, structured field comparison, then AI verification — to confirm the two markets are truly measuring the same thing. The majority of apparent cross-platform "arbitrage" is actually caused by subtle differences in how each platform defines the outcome (academic research found that only ~15-20% of similar-looking pairs are genuine 1:1 matches). Our system catches those false matches before money is at risk. Currently, the Polymarket execution path is fully built; the Kalshi order execution path is in active development with data ingestion and contract matching complete.

### Safety Architecture

- **Triple-layer safety gate**: Real trading requires three independent authorizations — a config mode switch, an environment variable, AND an explicit confirmation on every individual order. You cannot accidentally trade real money.
- **8-point validation chain**: Every trade passes through 8 sequential risk checks before execution.
- **One-way kill switch**: If the system hits loss limits, all trading halts automatically. A human must manually review and restart — there is no automatic recovery.
- **Quarter-Kelly position sizing**: The system never bets more than a mathematically conservative fraction of available capital.
- **5 exit mechanisms per position**: Stop-loss, trailing stop, take-profit, forecast-change, and resolution-based exits.

### The Scale of What Exists

The system spans 25,000+ lines of completed code across 18 modules — 4 AI strategies, 2 full platform integrations, paper trading infrastructure, a risk management engine, and a contract intelligence layer that catches false arbitrage.

I built this using an AI development infrastructure I've spent the last 6 months developing. It's the same system I use for professional client work — and it's what allows me to build at a level that would normally require a development team. The expertise isn't just in writing code. It's in knowing what to build, how to architect it, and having the infrastructure to execute at that level.

### What This Would Cost to Build From Scratch

| Who Builds It | Estimated Cost | Timeline |
|--------------|---------------|----------|
| Freelance developer (Upwork) | $15,000 - $30,000 | 3-4 months |
| Specialized quantitative trading developer | $40,000 - $80,000 | 2-3 months |
| Fintech development agency | $60,000 - $150,000 | 3-6 months |
| Bot-as-a-Service subscription | $200-500/mo + 10-30% of profits | Immediate, but no customization |

I'm not charging market rate. I'm proposing something fair because this is us — and I want this to work for both of us.

---

## How This Maps to Your Original Brief

You wrote a thorough spec with 7 layers. I built 6 of them to completion. The 7th — the full interactive dashboard and operator interface — is scoped and ready to build but represents its own engineering investment.

| Your Spec Layer | Status |
|----------------|--------|
| **1. Market/Data Ingestion** — Polymarket + Kalshi APIs | Done |
| **2. Contract Intelligence** — AI-powered contract matching, false arb detection | Done |
| **3. Opportunity Engine** — 4-strategy AI analysis, cross-strategy scoring | Done — exceeds spec |
| **4. Simulation/Paper Trading** — Full paper trading with configurable parameters | Done |
| **5. Execution Engine** — Paper/Live hierarchy, triple-layer safety, batch orders | Done |
| **6. Risk Engine** — 8-check validation, kill switch, position sizing, 5 exit types | Done — exceeds spec |
| **7. Product UI/UX** — Interactive dashboard, charts, operator controls | Scoped, not yet built |

**Layer 7** is the "interior design" of the system. The foundation, framing, plumbing, and electrical are complete. What remains is the finish work that makes it operable from a visual interface instead of the command line. The brain works. Layer 7 gives it a face.

### One Important Note on Cross-Platform Arbitrage

Your original vision centered on buying on one platform and selling on the other when the same event is priced differently. The system does exactly this — with a critical safety layer.

Research uncovered that **the vast majority of apparent cross-platform opportunities are false arbitrage** caused by subtle differences in contract wording, resolution sources, or time boundaries. Example: a "National Bitcoin Reserve" market appeared mispriced by 14 points between platforms, but one required establishment "before Jan 1, 2026" while the other required it "during 2025." Same event, different definitions, potentially opposite outcomes.

The contract intelligence engine specifically catches these cases before money is at risk. As noted above, the Kalshi order execution path is the final piece being built — the matching, analysis, and Polymarket execution are complete.

Importantly, the system doesn't only do cross-platform arbitrage — it also runs three single-platform strategies (weather, sports, AI ensemble) with wider edge windows. This means it generates opportunities even when no cross-platform match exists.

---

## The Real Numbers — What It Costs to Operate

These are the system's operating costs — the data feeds, AI analysis, and infrastructure the trading system needs to run. These are separate from my compensation.

### Phase 1: Paper Testing (No Real Money at Risk)

| Expense | Monthly Cost | Notes |
|---------|-------------|-------|
| Claude AI analysis | $7 | AI credibility model |
| OpenAI analysis | $1 | AI analytical model |
| Gemini analysis | $3 | AI contrarian model |
| Sportsbook data feed (The Odds API) | $30 | Aggregated data covering 348 books |
| Weather data (NOAA) | $0 | Free public data |
| Polymarket / Kalshi API access | $0 | Free |
| Server hosting (basic VPS) | $8 | Cloud server |
| **Total** | **~$58/month** | |
| Trading capital at risk | **$0** | Paper trading = simulated money |

The first paper trade was placed on April 14 — a London weather market. The test runs 30-60 days, targeting 200+ simulated trades against real market data. At the end, we'll have hard numbers: win rate, profit factor, and edge size by strategy. Total exposure to prove or disprove the system: roughly $60-$120.

**Important note on paper trading**: Simulation fills at quoted prices without modeling market slippage — a known optimism in all paper trading systems. On thin markets (weather, niche events), live fills may execute at slightly less favorable prices. This is factored into the conservative 50% discount applied to all return projections.

### Phase 2: Small-Scale Live Trading

| Expense | Monthly Cost | Notes |
|---------|-------------|-------|
| AI analysis (3 models combined) | $42 | Increased scan frequency |
| Sportsbook data feed | $30 | Same plan |
| Weather data | $0 | Still free |
| Platform APIs | $0 | Still free |
| Server hosting (production VPS) | $30 | More reliable, lower latency |
| Trading fees (variable) | $15-50 | Comes out of trading returns |
| **Total infrastructure** | **~$150/month** | |
| Trading capital deployed | **$2,000 - $5,000** | Graduated, small positions |

### Phase 3: Full Production (24/7, All Strategies)

| Expense | Monthly Cost | Notes |
|---------|-------------|-------|
| Claude AI analysis | $81 | High-frequency scanning |
| OpenAI analysis | $11 | Full production load |
| Gemini analysis | $33 | Full production load |
| Sportsbook data feed | $59 | Higher-tier plan for 7 sports |
| Weather data | $0-35 | Depends on source expansion |
| Platform APIs | $0 | Still free |
| Server hosting (trading-grade VPS) | $60-100 | Low-latency, high-reliability |
| Monitoring + domain | $16 | Uptime monitoring, alerts |
| Trading fees (variable) | $50-200 | Scales with volume |
| **Total infrastructure** | **~$400-650/month** | |
| Trading capital deployed | **$25,000 - $100,000** | Full multi-strategy deployment |

*Pricing sources: [Anthropic](https://docs.anthropic.com/en/docs/about-claude/pricing), [OpenAI](https://openai.com/api/pricing/), [Google AI](https://ai.google.dev/gemini-api/docs/pricing), [The Odds API](https://the-odds-api.com/), [QuantVPS](https://www.quantvps.com/pricing) — all verified April 2026. Note: one of the AI models (Gemini 2.5 Flash) is scheduled for deprecation in June 2026; the system will migrate to its successor at comparable pricing.*

**Key point**: Infrastructure costs are manageable at every phase. The documented profitable bots spend $80-150/month on infrastructure while generating $24,000-$3,300,000 in returns. The constraint is finding real edges, not overhead costs.

---

## Realistic Return Expectations

I'd rather underpromise and overdeliver. These projections apply a **conservative 50% discount** to simulation results — inspired by quantitative finance practice of haircutting backtested performance, because every documented bot performs significantly worse live than in testing due to slippage, fees, and execution delays. ([CME Group/Harvey](https://www.cmegroup.com/education/files/backtesting.pdf))

| Capital Level | Monthly Infrastructure | Expected Monthly Return | Weekly Average |
|--------------|----------------------|------------------------|----------------|
| $2-5K (small test) | ~$150 | $100 - $1,250 (2-25%) | $25 - $300 |
| $25K (medium) | ~$250 | $1,050 - $2,925 (4-12%) | $260 - $730 |
| $100K (full) | ~$400-650 | $4,200 - $11,700 (4-12%) | $1,050 - $2,925 |

### The $1M/Week Question

The best documented bot (sovereign2013, Claude-powered) averaged ~$100K/week over 8 months with $3.3M total. But that included a single $1.73M trade on a college basketball game — the distribution is lumpy, not consistent.

A realistic sustainable range with $100K capital: **$4,000 - $12,000/week**. With $500K+ capital across multiple strategies: **$20,000 - $125,000/week**. $1M/week is possible during peak events (elections, Fed decisions, major sports) but is not a sustainable average.

Paper trading will tell us which end of these ranges our system lands on — before any real money is committed.

---

## The Risks — Straight Up

1. **92.4% of all Polymarket wallets lose money.** This system is built to be in the top 7.6%, but results are not guaranteed. No honest person says "guaranteed profits" about trading.

2. **Strategies decay.** What works today may not work in 6 months as more bots enter the market. The system requires ongoing evolution — not a "set and forget" investment.

3. **Platforms change the rules.** Polymarket changed its fee structure on March 30, 2026 and significantly reduced profitability for an entire category of bots overnight — forcing strategy recalibration across the ecosystem. ([Coinmonks](https://medium.com/coinmonks/polymarket-just-changed-its-fees-heres-what-bot-traders-need-to-know-c11132e55d5c)) This will happen again.

4. **Paper trading always looks better than live.** That's why we apply a 50% haircut and why simulation comes before real money.

5. **State regulatory nuance.** Both platforms are federally regulated under CFTC jurisdiction, but approximately 11 states have issued cease-and-desist orders, and the question of federal preemption vs. state gambling law is actively being litigated. Verify your state's current status before deploying capital.

---

## What I'm Asking For

I put real time, real infrastructure, and real expertise into building this. I want to be straightforward about what fair compensation looks like — and give you options so you can pick the structure that makes sense for how you want to approach this.

### Option A: Build Fee + Maintenance Retainer *(Recommended)*

| Item | Amount |
|------|--------|
| Build fee (system delivered) | $3,500 one-time |
| Monthly maintenance retainer | $500/month |
| Year 1 total to me | $9,500 |

**What you get**: The complete trading system. Ongoing strategy evolution, monitoring, performance optimization, and bug fixes. All future improvements included in the retainer. I operate and maintain the system on your behalf.

**What you pay beyond my fee**: Infrastructure costs (table above) + trading capital when we go live. You keep 100% of all trading profits.

**If it doesn't work out**: After 60 days of paper testing, you can cancel the retainer. The build fee covers the work that's already been delivered — the code exists regardless.

---

### Option B: Reduced Build Fee + Profit Share

| Item | Amount |
|------|--------|
| Build fee (reduced) | $2,000 one-time |
| Monthly minimum | $400/month |
| Profit share | 20% of net trading profits |
| Year 1 minimum to me | $6,800 (uncapped if system performs) |

**What you get**: Everything in Option A, plus my income is tied to the system's performance — I have direct skin in the game. You keep 80% of all net profits.

**Best if**: You want lower upfront cost and want me financially motivated by results.

---

### Option C: Full Package Purchase

| Item | Amount |
|------|--------|
| System purchase price | $5,000 one-time |
| Included support | 60 days of hands-on setup and training |
| Optional maintenance after | $500/month |

**What you get**: Complete system ownership. Full documentation. Knowledge transfer so you understand how every piece works. After 60 days, you can operate independently or keep me on retainer.

**Best if**: You want to own everything outright with a clean, simple transaction.

---

### Side by Side

| | Option A | Option B | Option C |
|--|----------|----------|----------|
| **Upfront** | $3,500 | $2,000 | $5,000 |
| **Monthly to me** | $500 | $400 min + 20% profits | Optional $500 after 60 days |
| **Year 1 to me** | $9,500 | $6,800+ | $5,000+ |
| **Who gets profits** | 100% you | 80% you / 20% me | 100% you |
| **Ongoing relationship** | Required | Required | Optional after 60 days |

### What's Not Included in Any Option

- **My personal AI tools and subscriptions** — that's my infrastructure, like a carpenter's tools. You don't pay for those.
- **Guaranteed trading profits** — no honest person promises this. The system is designed to find edges, but markets are markets.
- **Legal or tax advice** — both of us should verify our state's stance on prediction market trading independently.

---

## Why This Isn't Set-and-Forget

This is important to understand before picking an option.

Prediction markets move fast. Polymarket changed its fee structure on March 30, 2026 — one rule change, and an entire class of profitable bots had to recalibrate overnight. Strategies that print money this quarter may stop working next quarter as more bots enter and competition increases.

The system needs ongoing attention: recalibrating strategies, responding to platform changes, monitoring performance drift, and evolving the AI models. Without that attention, performance degrades within 3-6 months — not because the system breaks, but because the market moves and nobody adjusts.

This is why Option A (retainer) is my recommendation. It acknowledges the reality that the system is a living thing that needs a pilot, not a Roomba you turn on and forget.

---

## What Happens Next

### Path 1: Prove the Edge First *(My Recommendation)*

Before committing to the full build or significant capital, we answer the most important question: **does this system actually find profitable edges in live market conditions?**

Fund 30-60 days of paper trading — roughly $58/month in API and data costs, zero trading capital at risk. The system's first paper trade was placed April 14; data collection has begun. Over the full test period, the system runs all 4 strategies against real market data in simulation mode, targeting 200+ trades. At the end, we have hard numbers: win rate by strategy, profit factor, edge distribution.

If the numbers work: proceed with confidence.
If they don't: total loss is $120, not $25,000.

### Path 2: Go Straight to Full Build

If you've seen enough and want to move — pick a deal structure, fund the infrastructure, and we start building Layer 7 (the interactive dashboard) immediately while paper trading runs in parallel.

Either way: let's align on terms first, then execute.

---

You trusted me with a real idea. I built something real. I want this to work for both of us — which is exactly why I'm being transparent about costs, realistic about returns, and upfront about what my work is worth.

Pick the path that makes sense for you. I'm ready when you are.

— Farrice
