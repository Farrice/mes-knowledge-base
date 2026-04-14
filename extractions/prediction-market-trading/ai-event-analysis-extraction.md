# MES 3.0 Deep Extraction: AI-Powered Prediction Market Trading Ecosystem
## Central Case Study: sovereign2013

---

## Content Assessment

```
Source: Multi-source research compilation (11 sources, 607 lines)
  — Financial news (Finbold, Yahoo Finance, Finance Magnates)
  — Academic paper (PolySwarm, arXiv 2604.03888v1)
  — Live trading analysis (Jung-Hua Liu, v2/v3 engine results)
  — Open-source repositories (5 GitHub projects)
  — Wallet analytics (Polymarket, ScanWhale, PolymarketAnalytics)
Expert: Composite
  — sovereign2013 (sports arbitrage, $1 to $3.3M, Claude-powered)
  — PolySwarm researchers (50-agent Bayesian swarm, academic rigor)
  — Jung-Hua Liu (live trading failure analysis, v2/v3 iteration)
  — 0x8dxd (latency arbitrage, $313 to $438K, 98% win rate)
  — Open-source developers (multi-model ensemble architectures)
Domain: AI-powered prediction market trading
  — Sports arbitrage, ensemble forecasting, multi-model systems,
    latency exploitation, portfolio construction
Depth Tier: DEEP
  — Multiple expert perspectives + academic rigor + live trading
    FAILURES + open-source implementation + wallet forensics
Genius Patterns: 12
Hidden Knowledge: 10
Exemplars: 3 + 1 anti-exemplar
Existing Overlap: None in Antigravity system
```

---

## Executive Summary

### Core Genius

Prediction market trading is NOT a forecasting problem. It is an **information-transfer arbitrage** problem. The 7.6% of wallets that profit do not predict outcomes better than the market. They detect when the market's price deviates from a superior reference price (sportsbook odds, exchange spot prices, multi-model ensemble consensus) and capture the convergence.

sovereign2013's $1-to-$3.3M run is the proof case: 37,247 bets in ~8 months, almost exclusively sports, Claude-powered, multiple bets per minute. The bot does not "know" sports. It knows that **Vegas knows sports**, and it knows that **Polymarket participants don't know what Vegas knows**.

### What Makes This Domain Different

1. **The reference price exists and is public.** Unlike equity markets where "fair value" is debatable, sportsbook odds represent the most accurate public probability estimates for sporting events. The edge is measurable in basis points, not vibes.

2. **The paper-to-live gap is the central risk.** Simulations show 522x returns. The same logic live lost 49.5% (v2) and 13% (v3). This is the most important finding across all 11 sources. Anyone who ignores this will join the 92.4%.

3. **Execution is 70% of success, strategy is 30%.** This is not a metaphor. Slippage (2-4 cents), fees (0.75-2%), latency (your order moves the price), and liquidity (the quoted price may not be available at size) collectively destroy edges that look massive on paper.

4. **14 of 20 top wallets are bots.** This is a bot ecosystem. Humans underperform bots by ~18% on identical strategies due to poor position sizing and inconsistent risk management. The human edge, if any, exists only in long-dated markets where judgment and context matter more than speed.

### Deployable Skills

- Sportsbook-vs-Polymarket gap scanning
- Multi-model ensemble probability estimation with Bayesian aggregation
- Quarter-Kelly position sizing with hard caps and circuit breakers
- Paper-to-live degradation modeling (the 0.5x-0.7x haircut)
- Portfolio construction across 4 strategy types
- Edge validation (real edge vs. noise vs. data error vs. structural difference)

### Hidden Knowledge Captured

- Why sovereign2013 focuses on sports (not crypto, not politics)
- Why Claude gets 35% weight (source credibility evaluation)
- Why PolySwarm uses 25 of 50 agents per evaluation (diversity > consensus)
- Why the portfolio construction table is the real insight, not any single strategy
- The exact mechanics of paper-to-live degradation (5 specific causes)
- What the 92.4% do wrong (3 behavioral patterns)
- Why arbitrage windows compress (12.3s to 2.7s) and what that means for entrants
- The information-theoretic tools that detect edge (KL divergence, negation pairs)

---

## Genius Patterns

### GP-1: The Vegas Anchor (Reference Price Arbitrage)
**Source**: Sources 1, 3, 10 | **Confidence**: HIGH (verified by sovereign2013's track record)

sovereign2013 does not predict sporting outcomes. The bot treats professional sportsbook odds as ground truth and exploits Polymarket deviations from that truth.

**Why it works**: Professional sportsbooks employ quantitative analysts, former traders, and proprietary models. Their lines are survival mechanisms — inaccurate pricing means they lose money. Polymarket pricing comes from a mix of retail bettors, crypto participants, and sentiment-driven actors. The pool is smaller, less specialized, and more prone to narrative mispricing.

**The mechanic**: When Pinnacle prices Lakers at 62% implied probability and Polymarket prices them at 55%, the 7-point gap minus fees (0.75% sports taker fee) represents extractable edge. The bot never asks "will the Lakers win?" It asks "is Polymarket wrong relative to Vegas?"

**Why this matters**: This reframes the entire problem. You don't need to be smarter than the market. You need the market to be dumber than another market. In sports, it reliably is.

---

### GP-2: The Ensemble Independence Requirement
**Source**: Sources 6, 7, 10 | **Confidence**: HIGH (confirmed by PolySwarm paper + open-source implementations)

Each model in the ensemble must forecast INDEPENDENTLY before aggregation. GPT-4o analyzes first. Claude analyzes separately. Gemini analyzes separately. Then — and only then — results combine.

**Why it works**: If models see each other's outputs before forecasting, you get herding. Three models that agree because they influenced each other provide zero additional signal beyond one model. Independence preserves the diversity that makes ensembles valuable.

**The weight allocation**: GPT-4o 40% (broad analytical reasoning, statistical pattern recognition), Claude 35% (source credibility evaluation, nuanced uncertainty reasoning), Gemini 25% (contrarian perspective, alternative data interpretation). These weights come from the open-source "Fully Autonomous Polymarket AI Trading Bot" and reflect observed performance across political, sports, and economic markets.

**The disagreement signal**: High model disagreement is itself actionable. When all 3 agree: high confidence. When 2 agree, 1 dissents: moderate confidence, investigate the dissent. When all 3 disagree: NO TRADE. The pattern of disagreement matters more than the direction — Claude dissenting on credibility carries different weight than GPT-4o dissenting on statistics.

---

### GP-3: The Paper-to-Live Haircut (The 0.5x-0.7x Rule)
**Source**: Source 9 | **Confidence**: HIGHEST (verified by live trading data with exact loss figures)

This is the most valuable pattern in the entire research. Jung-Hua Liu's live trading analysis is the only source that honestly reports FAILURE with exact numbers.

**The data**:
- Paper simulation: 522x returns
- Live v2: -49.5% loss (4 wins / 11 losses)
- Live v3: -13% loss (2 wins / 2 losses)

**The 5 causes of degradation**:
1. **Slippage**: Your order moves the market price against you. On thin Polymarket books, a $2,000 order can move the price 2-4 cents.
2. **Latency**: Between signal generation and order execution, the price changes. Even 500ms matters in 5-minute markets.
3. **Fee drag**: 1.56% fee at $0.50 entry + exit costs. The breakeven win rate is ~53%, not 50%.
4. **Liquidity illusion**: The quoted price exists at a specific depth. Your full order may not fill at that price.
5. **Micro-bounce reversion**: v2 weighted 65% of signal on the final 60 seconds, capturing transient bounces that reverted by window close. This is the specific technical failure — the signal was real but captured noise, not trend.

**Executable rule**: Whatever paper backtest shows, multiply expected edge by 0.5 to 0.7 before committing capital. If the edge doesn't survive the haircut, it isn't real. This single rule separates the 7.6% from the 92.4%.

---

### GP-4: Quarter-Kelly Consensus
**Source**: Sources 6, 7, 9 | **Confidence**: HIGH (convergent across academic + practitioner sources)

Every profitable bot architecture converges on quarter-Kelly position sizing: f = 0.25 * f_star.

**Why not full Kelly**: Full Kelly maximizes long-term growth rate but has extreme variance. A string of 5 losses on full Kelly can wipe 50%+ of bankroll. Quarter-Kelly sacrifices ~25% of theoretical growth rate but reduces drawdown risk by ~75%.

**Why not half-Kelly**: Half-Kelly is the traditional conservative choice. But prediction market edge estimates have wider error bars than traditional finance (thinner markets, less data history, more structural uncertainty). Quarter-Kelly provides an additional buffer against edge overestimation.

**Hard caps layered on top**:
- Maximum single position: 5-10% of bankroll (even if Kelly says more)
- Maximum correlated exposure: 15% of bankroll (5 NBA games on the same night = correlated)
- Daily loss limit: 5% drawdown triggers circuit breaker, halt all trading, manual review required

**The formula**:
```
Edge = (Your_Probability - Market_Price) / (1 - Market_Price)
Position = 0.25 * Edge * Bankroll
Cap at min(Position, 0.05 * Bankroll)
```

---

### GP-5: The Bayesian Swarm (70/30 Market Integration)
**Source**: Source 7 (PolySwarm paper) | **Confidence**: HIGH (academic, peer-reviewed methodology)

PolySwarm's two-stage aggregation is the most rigorous approach documented:

**Stage 1**: 25 of 50 specialized LLM personas independently evaluate a market. Individual predictions are confidence-weighted and averaged into a swarm consensus (p_swarm).

**Stage 2**: Swarm consensus combined with market-implied probability through linear Bayesian mixture:
- 70% swarm weight (p_swarm)
- 30% market weight (p_market)

**Why 70/30 and not 100/0**: The market price contains information the swarm doesn't have. Other traders, other bots, insider knowledge — all embedded in the current price. Ignoring it is arrogant. But deferring to it entirely means you can never find edge. 70/30 respects the market while asserting the swarm's informational advantage.

**Why 25 of 50 agents**: Using all 50 creates computational overhead without proportional accuracy gains. Random sampling of 25 preserves analytical diversity (different personas = different blind spots) while keeping latency manageable. The randomness itself is a feature — it prevents any single persona from dominating every evaluation.

**Trade trigger**: Combined probability must exceed market-implied odds by minimum 5%, AND swarm standard deviation must be below 30% (uncertainty filter). High divergence among agents = low confidence = no trade, regardless of the mean estimate.

---

### GP-6: Latency Arbitrage Physics (The Shrinking Window)
**Source**: Sources 3, 4, 5, 11 | **Confidence**: HIGH (verified by multiple independent wallet analyses)

**The timeline**:
- 2024: Average arbitrage window = 12.3 seconds
- 2026: Average arbitrage window = 2.7 seconds
- 73% of arbitrage profits captured by sub-100ms execution bots

**What this means**: Latency arbitrage (exploiting pricing delays between Polymarket and exchanges like Binance/Coinbase) generated the most spectacular returns ($313 to $438K for 0x8dxd). But the window is compressing as more bots compete. By 2026, you need dedicated Polygon RPC nodes and sub-100ms execution to compete.

**The 0x8dxd case study**: Focused exclusively on 15-minute BTC, ETH, SOL contracts. When BTC moves 0.05%+ on Binance but Polymarket's binary option hasn't repriced, the actual probability is ~85% while the market still shows 50/50. The bot buys the near-certainty at a discount. 98% win rate across 6,615 predictions. Strategy: latency, not forecasting.

**Entry barrier**: This is now a hardware problem, not an intelligence problem. New entrants without infrastructure investment cannot compete in sub-5-second windows. The alpha has decayed into an infrastructure arms race.

---

### GP-7: The Portfolio Construction Insight
**Source**: Source 6 | **Confidence**: MEDIUM-HIGH (backtested, not yet verified at scale in live trading)

The single most overlooked insight across all sources: **portfolio allocation across strategy types matters more than any individual strategy.**

| Profile | Allocation | Monthly Return | Max Drawdown | Sharpe |
|---------|-----------|---------------|-------------|--------|
| Conservative | 80% arb, 20% MM | 4.2% | 0.8% | 2.1 |
| Balanced | 50% arb, 30% AI ensemble, 20% MM | 11.7% | 3.2% | 1.6 |
| Aggressive | 30% arb, 50% AI/momentum, 20% MM | 23.4% | 8.9% | 1.1 |

**Why this matters more than strategy selection**: A perfectly executed single strategy has higher variance than a diversified portfolio of imperfectly executed strategies. Market making provides the steady floor (0.5-2% monthly, <1% drawdown). Arbitrage provides the core return. AI ensemble provides the upside. The mix determines your risk-adjusted outcome.

**The market making floor**: Simultaneous buy/sell orders capturing 2-5% monthly with inventory risk. Never exceed 30% exposure on one side. Widen spreads during volatility. Withdraw liquidity before major news. This strategy works regardless of prediction accuracy — it profits from providing liquidity.

---

### GP-8: The Information-Theoretic Edge Detectors
**Source**: Source 7 (PolySwarm paper) | **Confidence**: HIGH (academically rigorous)

Four mathematical tools for detecting exploitable inefficiencies:

1. **KL Divergence**: Measures how one probability distribution diverges from another. Applied to cross-market inefficiencies — when two related markets (e.g., "Trump wins" and "Republican wins") have inconsistent pricing, KL divergence quantifies the gap.

2. **Jensen-Shannon Divergence**: Symmetric, bounded version of KL. Better for comparing two market prices against each other because it doesn't depend on which you treat as "true."

3. **Negation Pair Checks**: YES + NO contracts for the same event must sum to $1.00. When they sum to $0.97, buying both sides guarantees 3% profit. When they sum to $1.03, someone is overpaying. By 2026, pure negation pair arbitrage is nearly exhausted — too many bots.

4. **Bayesian Network Consistency**: Maps logical relationships across 100+ markets using graph theory. "Trump wins 2028" at 35% means "Republican wins 2028" CANNOT be below 35%. Violations exceeding transaction costs (>3% mispricing threshold) trigger multi-leg trades executed within 500ms.

**Why this matters**: These are not strategies. They are **detection mechanisms**. The strategies are what you do after detecting the inefficiency. Most traders skip the detection step and trade on narrative.

---

### GP-9: The Structural Market Segmentation
**Source**: Source 5 | **Confidence**: HIGH (verified by market data + wallet analyses)

Prediction markets segment into two fundamentally different ecosystems:

**Ultra-short crypto contracts (5-minute, 15-minute BTC/ETH/SOL)**: Bot-dominated. 98%+ of profits go to sub-100ms latency bots. Humans cannot compete. The edge is speed, not intelligence. Price reference = exchange spot prices.

**Longer-dated event markets (sports, elections, economic indicators)**: Retain human-judgment opportunity. Bots compete but the edge comes from information processing, not latency. Price reference = sportsbook odds (sports), polling aggregates (politics), economic models (indicators). The 2-15 minute repricing window is exploitable by Claude-speed bots (seconds, not milliseconds).

**Strategic implication for new entrants**: Do NOT start with ultra-short crypto contracts. Start with sports arbitrage against sportsbook lines. The infrastructure requirement is lower (seconds, not milliseconds), the reference prices are publicly available, and the sophistication gap between Polymarket participants and professional sportsbooks is wide and persistent.

---

### GP-10: The v2-to-v3 Iteration Model (Systematic Failure Analysis)
**Source**: Source 9 | **Confidence**: HIGHEST (live trading data with exact parameters)

Jung-Hua Liu's progression from v2 (-49.5%) to v3 (-13%) documents the EXACT mechanics of systematic improvement:

**v2 failure diagnosis**:
- 80% of trades favored UP during a downtrend (directional bias)
- Signal weights allocated 65% to final 60 seconds (noise capture)
- No medium-term trend filter (traded against momentum)
- No hard rules blocking counter-trend signals

**v3 fixes**:
- Rebalanced signal weights to favor longer lookbacks (120s, 240s) over short (30s, 60s)
- Added 10-minute trend filter as hard rule: signals opposing the trend are BLOCKED
- Confidence halved when composite signal conflicts with longer horizon
- Hard rule: reject signals opposing 15-minute trend unless BTC move exceeds 0.10%

**The 7x improvement**: v3 didn't become profitable. It reduced capital destruction by 7x. This is the realistic trajectory — you iterate from "catastrophic loss" to "controlled loss" to "breakeven" to "modest profit." Anyone expecting v1 to be profitable is delusional.

**INFERRED insight**: sovereign2013 almost certainly went through equivalent iterations. The $1 starting balance suggests early versions were tested with minimal capital. The $3.3M was not v1.

---

### GP-11: The Hallucination-Correlation Risk
**Source**: Source 7 (PolySwarm paper) | **Confidence**: HIGH (academic identification)

LLMs confidently assert false facts. In a multi-model ensemble, this creates a specific risk: **correlated hallucination**. If all three models hallucinate the same incorrect "fact" (e.g., misremembering a team's record, inventing a player injury), the ensemble provides false consensus rather than error correction.

**Why ensemble diversity doesn't fully solve this**: Models trained on overlapping data develop overlapping blind spots. GPT-4o, Claude, and Gemini all learned from similar internet text. Their errors correlate more than random agents would.

**Mitigation**: The Bayesian 30% market weight partially addresses this — the market price embeds real-world information that LLMs may hallucinate about. But the real defense is: never trust the ensemble's factual claims without checking verifiable data (scores, schedules, injury reports) against authoritative APIs. The ensemble evaluates probability. Deterministic code verifies facts.

---

### GP-12: Capital Rotation vs. Hold-to-Resolution
**Source**: Sources 1, 6 | **Confidence**: MEDIUM-HIGH (INFERRED from sovereign2013's trading velocity)

sovereign2013 places bets multiple times per minute across 37,247+ predictions. This velocity implies capital rotation, not hold-to-resolution.

**The logic**: Buy at $0.55 when the sportsbook-implied fair value is $0.62. If Polymarket price converges to $0.62, you've captured 7 cents of edge. Holding to resolution exposes you to the 38% chance of total loss on that position. Selling at $0.62 locks profit and frees capital for the next mispriced market.

**When to hold**: Only when the remaining edge-to-resolution exceeds the opportunity cost of rotating capital. If no better opportunities exist, holding is optimal. If 5 other markets are mispriced right now, rotation is optimal.

**The compounding effect**: Capital rotation is why $1 becomes $3.3M. Each dollar is deployed dozens or hundreds of times, each time capturing a small edge. Hold-to-resolution deploys each dollar once. The velocity of capital deployment, not the size of each edge, drives the exponential curve.

---

## Hidden Knowledge

### HK-1: Why Sports, Not Crypto or Politics
**Source**: Inferred from Sources 1, 3, 5, 11

sovereign2013 bets almost exclusively on sports. Not crypto (where 0x8dxd made $438K). Not politics (where PolySwarm's framework excels in theory). Why?

**The answer**: Sports have the best available reference price. Professional sportsbook odds are priced by specialists with decades of domain expertise and survival-level incentives for accuracy. No equivalent reference exists for crypto (exchange prices are spot, not probabilistic) or politics (polling aggregates are noisy and lagging). Sports arbitrage has the tightest feedback loop: reference price is precise, events resolve quickly, and the same matchup types repeat thousands of times per season, enabling statistical validation.

---

### HK-2: Why Claude at 35% (Not 25%, Not 40%)
**Source**: Sources 6, 10

Claude's weight in the ensemble reflects a specific capability: **source credibility evaluation**. In event markets with information asymmetry — injury reports, insider leaks, conflicting sources — the critical question isn't "what does the data say?" but "which sources should we trust?"

Claude's training emphasizes nuanced reasoning under uncertainty. When one journalist reports an injury and three others repeat the original report without independent verification, Claude identifies the 3:1 ratio as 1:0 actual sources. GPT-4o is stronger at statistical pattern recognition (hence 40%). Gemini provides the contrarian check (25%). The weights reflect complementary capabilities, not quality rankings.

---

### HK-3: The 92.4% Failure Taxonomy
**Source**: Sources 3, 4

Analysis of 50,000+ wallets reveals 92.4% are unprofitable. The three dominant failure modes:

1. **Oversized positions**: Betting 20-50% of bankroll on single events. One loss destroys months of gains. No Kelly discipline.
2. **Late entries**: Seeing a mispricing after it's already half-corrected. The edge at entry is smaller than fees.
3. **Inconsistent risk management**: Disciplined on wins, emotional on losses. Holding losers hoping for reversal instead of cutting.

Humans underperform bots by ~18% on identical strategies due to these three behavioral patterns. The bot advantage is not intelligence — it's emotional absence.

---

### HK-4: The PolySwarm 25-of-50 Agent Design Choice
**Source**: Source 7

PolySwarm builds 50 distinct LLM personas (macro economists, technical analysts, contrarians, domain specialists) but only uses 25 per market evaluation, sampled without replacement.

**Why not all 50**: Marginal accuracy gains flatten after ~25 agents while computational cost scales linearly. More importantly, random subsampling prevents any single persona from dominating every evaluation. A contrarian agent that's correct 30% of the time provides massive value on those occasions — but averaging it into every evaluation dilutes its signal when it's wrong the other 70%. Random sampling naturally creates evaluations where the contrarian's input is present and absent, allowing the system to benefit from contrarian insight without systematic dilution.

---

### HK-5: Why "Execution Is 70%" Is Not a Cliche
**Source**: Source 6

This claim appears in Source 6 without elaboration. Here's what it means concretely:

**Strategy** (the 30%): Identifying that Polymarket is mispriced relative to Pinnacle by 5 points on the Lakers game tonight. This is the easy part.

**Execution** (the 70%):
- Getting the order filled at the quoted price (slippage)
- Filling before the price moves (latency)
- Filling at full size (liquidity)
- Paying less than the edge in fees (fee optimization — maker vs. taker)
- Not having 5 correlated positions all go wrong simultaneously (portfolio risk)
- Having the circuit breaker actually halt trading after 5% drawdown (discipline)
- Rebalancing positions as new information arrives (dynamic management)

A strategy with 10% edge and poor execution nets 3%. A strategy with 5% edge and perfect execution nets 4%. Execution literally determines profitability more than edge size.

---

### HK-6: The API Cost Trap
**Source**: Source 7

PolySwarm identifies that frontier model deployments incur "thousands per day in API costs at scale." With 25 agents evaluating potentially hundreds of active markets on 5-second scan loops, the token consumption is enormous.

**The hidden math**: 25 agents * 200 active markets * 12 scans/minute * 60 minutes/hour * 24 hours = 86.4M inference calls per day. Even at $0.001 per call, that's $86K/day. Realistic cost optimization (caching, filtering before inference, reducing scan frequency for stable markets) brings this to $1-5K/day — still a major operating cost that directly reduces net profitability.

**Implication**: The bot must be profitable enough to cover its own API costs before generating returns for the operator. A $10K bankroll running $2K/day in API costs is dead on arrival. This is why sovereign2013's sports arbitrage (where the reference price comes from FREE sportsbook odds, not expensive LLM inference) is structurally superior to brute-force multi-agent approaches.

---

### HK-7: Front-Running as Predator Strategy
**Source**: Source 4

Some bots don't trade against the market. They trade against OTHER BOTS. By monitoring the mempool (pending transactions on Polygon), a front-running bot can detect incoming large buy orders, purchase the contract first, then sell into the demand the incoming order creates.

**The ecosystem implication**: Your bot isn't just competing against mispriced markets. It's competing against bots that are trying to exploit YOUR orders. This means: batch transactions to minimize visibility, use private RPC nodes to avoid mempool exposure, and never place large market orders that signal intent.

---

### HK-8: The Gambot Principle (Stripping the Vig)
**Source**: Source 11

Gambot pulls odds from Pinnacle (considered the sharpest sportsbook), removes the house edge (the "vig" or "juice"), and calculates true implied probabilities. This is the mechanical first step of sovereign2013's inferred strategy.

**Why Pinnacle specifically**: Among sportsbooks, Pinnacle runs the lowest margins (2-3% vig on major sports) and is known as the "sharp" book — they accept and adjust to large bets from professional bettors rather than limiting them. This means Pinnacle's lines most closely approximate true probabilities. DraftKings and FanDuel run higher margins and limit sharp bettors, making their lines less reliable as truth.

**The conversion math**: If Pinnacle offers Lakers -150 / Opponents +130, implied probabilities are 60% / 43.5% = 103.5% total (the 3.5% is vig). Stripping the vig: 60/103.5 = 57.97% and 43.5/103.5 = 42.03%. These "true probabilities" become the reference against which Polymarket prices are compared.

---

### HK-9: Why Live v3 Still Lost (The Random Walk Problem)
**Source**: Source 9

v3 reduced losses from -49.5% to -13%, a 7x improvement. But it still lost money. The fundamental issue:

"5-minute BTC options approximate random walks at short horizons."

**Translation**: At 5-minute timeframes, BTC price movements are essentially unpredictable. No amount of signal engineering can reliably predict which direction a random walk will take over the next 5 minutes. The 522x paper returns were curve-fit to historical noise — patterns that appeared predictive in backtesting were statistical mirages.

**The lesson for strategy selection**: Short-duration crypto binary options are the WORST market for AI-powered trading because the underlying process is closest to random. Long-duration event markets (who wins the NBA Finals, will GDP exceed X%) have actual information content that AI can process. sovereign2013 trades sports with hours-to-days horizons, not 5-minute crypto flips.

---

### HK-10: The $40M Extraction Number
**Source**: Sources 3, 4, 5

Arbitrage traders extracted approximately $40 million from Polymarket between April 2024 and April 2025. This $40M represents direct losses for other participants.

**What this means**: Prediction markets are zero-sum before fees and negative-sum after fees. Every dollar the 7.6% profit comes from the 92.4% that lose. The bots aren't creating value — they're extracting it from less sophisticated participants. As bot penetration increases (14 of 20 top wallets in 2026 vs. fewer in 2024), the pool of extractable capital shrinks. The bots are eating each other's lunch.

**Long-term implication**: Prediction market arbitrage is self-correcting. As more bots compete, edges compress, windows shrink, and returns decline. The $1-to-$3.3M era may not be repeatable. First-mover advantage was real. Late entrants face a mature competitive landscape.

---

## Hall of Fame Exemplars

### Exemplar 1: The PolySwarm Bayesian Aggregation Pipeline
**Source**: Source 7 (Academic Paper) | **Why it's exemplary**: Highest rigor

```
INPUT: Active Polymarket market
  |
  v
[Filter: volume > threshold, activity > threshold]
  |
  v
[Sample 25 of 50 personas without replacement]
  |
  v
[Parallel independent LLM inference — each persona evaluates separately]
  |
  v
[Stage 1: Confidence-weighted average → p_swarm]
  |
  v
[Stage 2: Bayesian mixture → 0.70 * p_swarm + 0.30 * p_market]
  |
  v
[Trade trigger: combined_p > market_p + 0.05 AND std_dev < 0.30]
  |
  v
[Position sizing: quarter-Kelly with hard cap ($10 default)]
  |
  v
[Risk check: daily loss limit, uncertainty filter]
  |
  v
EXECUTE or PASS
```

**Why this is the gold standard**: It respects the market (30% weight), preserves diversity (random agent sampling), quantifies uncertainty (standard deviation filter), sizes conservatively (quarter-Kelly), and has a hard stop (daily loss limit). Every other architecture should be measured against this.

---

### Exemplar 2: The Live Trading Failure Analysis (v2 to v3)
**Source**: Source 9 | **Why it's exemplary**: Only honest live performance data in the research

**v2 Engine Performance**:
- Record: 4W / 11L
- ROI: -49.5%
- Root cause: 65% signal weight on final 60 seconds captured transient micro-bounces that reverted. 80% of trades favored UP during a downtrend. No trend filter.

**v3 Engine Performance**:
- Record: 2W / 2L
- ROI: -13%
- Fixes applied: Longer lookback weights, 10-minute hard trend filter, confidence halving on conflicting signals, counter-trend signal rejection unless BTC move > 0.10%

**Why this matters more than success stories**: Success stories have survivorship bias. sovereign2013's $3.3M is real but unauditable in terms of methodology. Liu's failure analysis shows the EXACT technical parameters that cause loss and the EXACT fixes that reduce it. This is reproducible knowledge. The success stories are not.

---

### Exemplar 3: The Utah State Bet ($1.73M Volume, $179K Profit)
**Source**: Source 1 | **Why it's exemplary**: Demonstrates sovereign2013's operational mechanics

sovereign2013's largest documented single bet: Utah State Aggies vs. Arizona Wildcats (college basketball). Over $1.73 million in volume, generating $179,100 in pure profit.

**What this reveals (INFERRED)**:
- **Position size**: $1.73M volume on a single game implies substantial bankroll and extreme confidence in the edge. At quarter-Kelly, this suggests the perceived edge was 10%+ and bankroll was $5-10M+ at time of execution.
- **Market selection**: College basketball, not NBA. College games often have wider Polymarket-to-sportsbook gaps because less attention = less efficient pricing.
- **Execution**: This volume on Polymarket requires either a single large order (moving the market) or many smaller orders over time (capturing the edge in slices). Given sovereign's "multiple bets per minute" pattern, the latter is more likely — the bot bought in increments as liquidity was available.
- **The edge source**: Utah State (small program) playing Arizona (major program) creates an information asymmetry. Sportsbooks have models that accurately price these matchups. Polymarket participants likely overweight the name recognition of Arizona and underweight Utah State's actual probability.

---

### Anti-Exemplar: The 92.4% (What Failure Looks Like)
**Source**: Sources 3, 4, 5

**Profile**: 50,000+ wallets analyzed. 92.4% unprofitable.

**What they do wrong**:

1. **They predict instead of arbitrage.** They buy "Yes" on a team because they think that team will win, without checking whether the price already reflects that probability. They're expressing opinions in a market that punishes opinions and rewards information.

2. **They size on confidence, not Kelly.** "I'm really sure about this one" → 30% of bankroll on a single bet. One loss sets them back months. They mistake certainty of feeling for certainty of edge.

3. **They trade the wrong markets.** Humans enter ultra-short crypto binary options (5-minute BTC calls) where bots with sub-100ms latency capture 73% of profits. Humans literally cannot compete in this segment — their reaction time exceeds the opportunity window.

4. **They don't account for fees.** A 2% edge sounds good until 1.56% in fees and 2-4 cents in slippage consume it. The breakeven win rate is ~53%, not 50%. Most retail participants don't know this.

5. **They hold losers.** When a position moves against them, they hold hoping for reversal instead of cutting and rotating capital to the next opportunity. This is the disposition effect — well-documented in behavioral finance, rampant on Polymarket.

---

## Signature Moves

### SM-1: The Line Movement Detector
**INFERRED**: sovereign2013's primary operational pattern.

Monitor sportsbook line movements in real-time. When a line moves (injury announcement, lineup change, sharp money), immediately check if Polymarket has adjusted. If not, execute.

**Timing window**: 2-15 minutes between a sportsbook line move and Polymarket price adjustment. This is where the bulk of edge lives for sports arbitrage. Not fast enough for latency arb (sub-second) but more than fast enough for Claude-speed reasoning.

---

### SM-2: The Ensemble Credibility Arbiter
When model outputs diverge, route the disagreement through a credibility lens: Is the disagreement about DATA (GPT-4o likely right) or SOURCES (Claude likely right) or CONSENSUS (Gemini's contrarian view worth investigating)? The nature of the disagreement, not its direction, determines which model to trust.

---

### SM-3: The Cumulative Probability Violation Scan
Monitor related markets for logical inconsistencies. When outcome probabilities for mutually exclusive events sum to more than 100% (e.g., recession timing: Jan 12% + Feb 15% + Mar 18% + Apr 14% + No recession 52% = 111%), execute multi-leg trades capturing the guaranteed 11% spread minus transaction costs. Requires graph theory mapping of 100+ market relationships.

---

### SM-4: The Market Making Floor
Allocate 20% of portfolio to automated market making as a baseline income strategy. Place simultaneous limit orders on YES and NO sides with 4-cent spreads. Never exceed 30% inventory exposure on one side. Widen spreads during volatility spikes. Withdraw liquidity before major news. This generates 0.5-2% monthly regardless of prediction accuracy and smooths the portfolio's equity curve.

---

### SM-5: The Gap Explanation Protocol
Every identified edge demands a REASON. Before executing any trade:

| Explanation | Action |
|------------|--------|
| Information asymmetry (Polymarket doesn't know what sportsbooks know) | EXECUTE — core edge |
| Narrative mispricing (public sentiment over/underweighting) | EXECUTE — secondary edge |
| Low liquidity (stale price, thin book) | EXECUTE CAREFULLY — your order may BE the move |
| Data error (feed wrong or delayed) | DO NOT EXECUTE — verify first |
| Structural difference (different market rules, e.g., overtime inclusion) | DO NOT EXECUTE — comparing different products |
| Unknown | DO NOT EXECUTE — unexplained edges are often traps |

---

### SM-6: The Timing Matrix
| Time to Event | Posture |
|---------------|---------|
| > 48 hours | Monitor only. Lines will move. |
| 24-48 hours | Begin scanning for persistent gaps. |
| 6-24 hours | Primary trading window. Lines settling. |
| 1-6 hours | Peak edge window. Last line moves, maximum Polymarket lag. |
| < 1 hour | Exit window. Close positions if target reached. Avoid new entries. |
| Live/in-play | Different game. Real-time data feeds required. Much higher variance. |

---

### SM-7: The Circuit Breaker Protocol
Non-negotiable. Automated. No override without manual review.

- 5% daily drawdown → halt ALL trading for 24 hours
- 3 consecutive losses → reduce position sizes by 50% for next 10 trades
- Any single position exceeds 10% of bankroll → auto-reject
- Correlated exposure exceeds 15% → block new entries in same category

---

## Expert-Specific Quality Rubric

| Dimension | Score 4 | Score 7 | Score 10 |
|-----------|---------|---------|----------|
| **Edge Identification** | "I think the Lakers will win" — no reference price, no quantification | Gap identified with sportsbook anchor but explanation thin or fee impact ignored | Quantified gap (basis points) + sportsbook reference + explanation of WHY gap exists + fee-adjusted edge calculation |
| **Position Sizing** | Gut-feel sizing ("I'll put $500 on this") or no sizing guidance | Kelly-based but missing hard caps, or caps present but no correlation check | Quarter-Kelly with hard single-position cap (5%), correlated-exposure cap (15%), and daily drawdown circuit breaker (5%) |
| **Ensemble Quality** | Single model used, or models used as rubber stamps for a predetermined view | Models used but not independently, or disagreement between models ignored | Independent forecasting → weighted aggregation → disagreement analysis → credibility-weighted resolution |
| **Execution Realism** | Assumes paper backtest = live performance; no mention of fees or slippage | Mentions some execution costs but doesn't quantify the haircut | Paper-to-live 0.5x-0.7x haircut applied; slippage, latency, liquidity, and fee drag all quantified |
| **Risk Management** | No downside protection; "it's a sure thing" | Some limits mentioned but incomplete (e.g., position cap but no daily loss limit) | Full stack: position caps + correlation limits + daily circuit breaker + kill conditions per trade + portfolio rebalancing triggers |
| **Market Selection** | Trades whatever looks interesting; no systematic market filtering | Focuses on one market type but without clear rationale | Explicit segmentation: sports (seconds-level edge, sportsbook reference), crypto (ms-level, exchange reference), events (minutes-level, ensemble reference) — matched to infrastructure capability |

---

## Methodology

**Extraction approach**: 6-layer deep analysis across 11 sources. Cross-validated findings where multiple sources reported the same data (bot dominance statistics, 92.4% unprofitable figure, $40M extraction figure). Flagged all inferences about sovereign2013's methodology as INFERRED since wallet analysis reveals behavior but not code. Prioritized the live trading failure analysis (Source 9) as highest-value data due to its honesty about losses — the only source that reports exact failure mechanisms rather than success narratives.

**Key reliability notes**:
- sovereign2013's $3.3M figure is verified across multiple independent news outlets and on-chain wallet data
- The PolySwarm paper is academic (arXiv) with peer-review-level methodology
- Jung-Hua Liu's live trading data includes exact parameters, making it reproducible
- Open-source bot architectures are verifiable via GitHub
- All sovereign2013 strategy inferences are marked INFERRED — the bot's code is not public
- The 92.4% unprofitable statistic comes from analysis of 50,000+ wallets — large sample, high confidence

---

## Applied Intelligence

### Capability Unlocks

1. **Sportsbook Odds Scanning**: Compare Polymarket sports prices against Pinnacle/DraftKings/FanDuel implied probabilities in real-time. This is sovereign2013's core edge and is implementable with publicly available odds APIs.

2. **Multi-Model Ensemble Forecasting**: Independent Claude + GPT-4o + Gemini forecasting with Bayesian aggregation. Applicable beyond prediction markets to any domain requiring calibrated probability estimates.

3. **Paper-to-Live Degradation Modeling**: The 0.5x-0.7x haircut framework applies to ANY backtested strategy in ANY market. This is a universal risk management tool.

4. **Portfolio Strategy Allocation**: The conservative/balanced/aggressive allocation framework is directly implementable. Start conservative (80% arb / 20% MM), migrate to balanced as execution quality improves.

### Market Signals

- Arbitrage windows compressing (12.3s to 2.7s) means edge decay is accelerating. First-mover advantage is real and fading.
- 14/20 top wallets being bots means this is an infrastructure arms race, not an intelligence competition.
- The $40M annual extraction creates ceiling pressure — as more bots compete, each bot's share shrinks.
- Legal risk is non-trivial: Polymarket ToS prohibits US persons. This is unresolved and could change overnight.

### System Enhancements

- This extraction should feed a production skill at `skills/prediction-market-trading/`
- The multi-model ensemble pattern is transferable to the existing Antigravity expert routing system
- Quarter-Kelly position sizing should be extracted as a reusable framework for any probabilistic decision-making
- The paper-to-live degradation model should be added to `directives/quality_assurance.md` as a general principle

---

## Implementation Pathway

### 24-Hour Sprint
1. Set up Pinnacle/DraftKings odds API access (free tier available)
2. Build a spreadsheet comparing today's Polymarket sports prices against sportsbook implied probabilities
3. Calculate edge after fees (0.75% sports taker) for each market
4. Identify any gaps exceeding 3% — these are candidate trades for paper tracking
5. Start paper tracking: log every identified edge, the action you would have taken, and the actual resolution

### 7-Day Build
1. Automate the odds comparison (Python script pulling both APIs every 60 seconds)
2. Implement quarter-Kelly position sizing calculator
3. Set up the 3-model ensemble (Claude + GPT-4o + Gemini) for independent event evaluation
4. Build the paper trading dashboard with P&L tracking
5. Run 7 days of paper trading. Calculate paper-to-live haircut by comparing signal quality to hypothetical execution (add 2-4 cent slippage to every trade)
6. Evaluate: Is paper edge > 5% after haircut? If no, iterate signal quality before going live.

### 30-Day Deployment
1. **Week 1-2**: Live trading with MINIMUM capital ($50-$100). Conservative allocation (80% arb, 20% MM). Full circuit breakers active.
2. **Week 2-3**: Evaluate live performance against paper predictions. Calculate actual paper-to-live ratio. If ratio < 0.5, stop and diagnose.
3. **Week 3-4**: If ratio >= 0.5 and net profitable, begin scaling capital according to quarter-Kelly. Move to balanced allocation (50% arb, 30% AI ensemble, 20% MM) only after demonstrating live profitability.
4. **Ongoing**: Weekly review of strategy performance. Detect decay (falling hit rates, shrinking edges). Rotate strategies as alpha decays.

### Critical Go/No-Go Gates
- **Gate 1** (Day 7): Paper edge after haircut > 5%? If no → iterate before going live.
- **Gate 2** (Day 14): Live P&L positive or loss < 10% of capital? If loss > 10% → halt, diagnose, iterate.
- **Gate 3** (Day 30): Cumulative live Sharpe > 1.0? If no → reassess strategy mix and execution quality.

---

## Crown Jewel Prompts

### CJP-1: Sportsbook Odds Scanner

```
You are a sports arbitrage analyst. Your job is to identify mispriced markets on Polymarket by comparing against professional sportsbook odds.

INPUT: I will provide you with:
1. A list of active Polymarket sports markets with current YES/NO prices
2. Corresponding sportsbook odds from Pinnacle (or another sharp book)

PROCESS:
For each market:
1. Convert sportsbook odds to implied probability (strip the vig by normalizing to 100%)
2. Compare against Polymarket implied probability
3. Calculate the gap in percentage points
4. Subtract fee drag: 0.75% for sports taker fees on entry, plus estimated 0.75% on exit
5. Calculate net edge after fees

OUTPUT FORMAT (ranked by net edge, highest first):

| Market | Sportsbook Implied | Polymarket Price | Raw Gap | Fee Drag | Net Edge | Confidence | Action |
|--------|-------------------|-----------------|---------|----------|----------|------------|--------|

CONFIDENCE LEVELS:
- HIGH: Net edge > 5%, gap explained by information asymmetry or narrative mispricing
- MEDIUM: Net edge 2-5%, gap exists but explanation uncertain
- LOW: Net edge 1-2%, within noise range
- SKIP: Net edge < 1% or gap explained by structural difference (different rules, etc.)

ACTION:
- EXECUTE: High confidence, edge exceeds 3% after fees
- INVESTIGATE: Medium confidence, need ensemble validation
- MONITOR: Edge exists but too thin or explanation unclear
- SKIP: No actionable edge

FLAG: If any market shows > 10% gap, flag it as SUSPICIOUS and investigate whether it's a data error, structural difference, or genuine extreme mispricing before recommending action.

EXAMPLE OUTPUT:
| Lakers vs Celtics Game 3 | 62.3% | $0.55 (55%) | 7.3% | 1.5% | 5.8% | HIGH | EXECUTE |
| Warriors vs Heat | 48.1% | $0.46 (46%) | 2.1% | 1.5% | 0.6% | SKIP | SKIP |
| Utah State vs Arizona | 44.2% | $0.38 (38%) | 6.2% | 1.5% | 4.7% | HIGH | EXECUTE |
| Chiefs vs Eagles SB | 52.0% | $0.59 (59%) | -7.0% | n/a | -7.0% | REVERSE | INVESTIGATE (Polymarket overpriced) |
```

---

### CJP-2: Multi-Model Ensemble Forecaster

```
You are a prediction market ensemble forecaster. You will analyze a market using three distinct analytical perspectives, then aggregate them using Bayesian methods.

INPUT: A specific prediction market question, current market price, and relevant context.

PROCESS — Execute ALL THREE perspectives INDEPENDENTLY before aggregating:

**PERSPECTIVE 1 — ANALYTICAL (Weight: 40%)**
Analyze using statistical reasoning, historical base rates, and quantitative data. What do the numbers say? Identify the most relevant reference class. Calculate a probability estimate.
Output: P1 = [probability], Confidence = [1-10], Key reasoning: [2 sentences max]

**PERSPECTIVE 2 — CREDIBILITY (Weight: 35%)**
Evaluate the information sources. Which reports are primary vs. secondary? Which sources have track records of accuracy in this domain? Is there information asymmetry? Are insiders trading?
Output: P2 = [probability], Confidence = [1-10], Key reasoning: [2 sentences max]

**PERSPECTIVE 3 — CONTRARIAN (Weight: 25%)**
What is the consensus missing? What scenario would make the consensus wrong? What information is being underweighted? Play devil's advocate.
Output: P3 = [probability], Confidence = [1-10], Key reasoning: [2 sentences max]

**AGGREGATION**:
1. Weighted average: P_ensemble = 0.40 * P1 + 0.35 * P2 + 0.25 * P3
2. Market integration: P_final = 0.70 * P_ensemble + 0.30 * P_market
3. Disagreement = max(P1, P2, P3) - min(P1, P2, P3)

OUTPUT FORMAT:
```
MARKET: [name]
CURRENT PRICE: [price] ([implied probability])

PERSPECTIVE 1 (Analytical, 40%): [probability] | Confidence: [X]/10
  Reasoning: [2 sentences]

PERSPECTIVE 2 (Credibility, 35%): [probability] | Confidence: [X]/10
  Reasoning: [2 sentences]

PERSPECTIVE 3 (Contrarian, 25%): [probability] | Confidence: [X]/10
  Reasoning: [2 sentences]

ENSEMBLE: [P_ensemble]
MARKET-INTEGRATED: [P_final]
DISAGREEMENT: [spread between perspectives]

VERDICT:
- Edge vs market: [P_final - P_market] percentage points
- After fees: [edge - fee drag]
- Disagreement level: [LOW/MEDIUM/HIGH]
- Recommendation: [TRADE / INVESTIGATE / PASS]
- If TRADE: Direction [BUY YES / BUY NO], Quarter-Kelly size
```

EXAMPLE OUTPUT:
```
MARKET: Will Lakers win Game 3?
CURRENT PRICE: $0.55 (55%)

PERSPECTIVE 1 (Analytical, 40%): 63% | Confidence: 7/10
  Lakers are 8-2 in last 10 home games. Historical home-court advantage in playoff Game 3s is +4.2%.

PERSPECTIVE 2 (Credibility, 35%): 61% | Confidence: 8/10
  Pinnacle line moved from -140 to -155 in last 2 hours, indicating sharp money on Lakers. Primary source: line movement, not media speculation.

PERSPECTIVE 3 (Contrarian, 25%): 57% | Confidence: 5/10
  Celtics historically perform better in Game 3 after losing Game 2. Market may be underweighting Celtics adjustment capability.

ENSEMBLE: 60.8%
MARKET-INTEGRATED: 0.70 * 60.8% + 0.30 * 55% = 59.1%
DISAGREEMENT: 6 percentage points (63% - 57%)

VERDICT:
- Edge vs market: +4.1 percentage points
- After fees (1.5%): +2.6 percentage points
- Disagreement level: MEDIUM
- Recommendation: TRADE
- Direction: BUY YES at $0.55, Quarter-Kelly size
```
```

---

### CJP-3: Edge Validator

```
You are an edge validation specialist. Your job is to determine whether an identified price discrepancy represents real exploitable edge or is noise/trap/error.

INPUT: A market where a price gap has been identified between Polymarket and a reference source.

Run the gap through this 6-point validation framework:

**1. DATA INTEGRITY CHECK**
- Is the Polymarket price current (within last 60 seconds)?
- Is the reference price current?
- Are both prices for the SAME event with the SAME rules (e.g., both include overtime)?
- Are there any known data feed issues?
→ PASS / FAIL (if FAIL, stop — do not trade on bad data)

**2. GAP EXPLANATION**
Classify the gap into one of 6 categories:
- INFORMATION ASYMMETRY: Reference source has info Polymarket doesn't → VALID edge
- NARRATIVE MISPRICING: Public sentiment inflating/deflating → VALID edge (but may correct fast)
- LIQUIDITY: Low volume, stale price → VALID but execute carefully (you'll move the market)
- DATA ERROR: Feed lag, wrong odds, different event → INVALID — do not trade
- STRUCTURAL: Different market rules → INVALID — comparing different products
- UNKNOWN: Can't explain the gap → TREAT AS INVALID until explained

**3. FEE-ADJUSTED EDGE**
- Raw gap: [X]%
- Entry fee: [0.75% sports / 2% non-sports]
- Estimated slippage: [1-3% depending on liquidity]
- Exit fee (if rotating before resolution): [0.75% / 2%]
- Net edge after all costs: [X]%
→ Net edge > 2%? PROCEED. Net edge < 2%? REJECT (edge doesn't survive friction).

**4. SIZE VALIDATION**
- At quarter-Kelly, what position size does this edge justify?
- Does that size exceed 5% of bankroll? If yes, cap at 5%.
- Is this position correlated with other active positions? If correlated exposure > 15%, reduce.

**5. TIMING CHECK**
- How long until the event resolves?
- Is the edge likely to persist or close quickly?
- Is this the right time window for entry? (See timing matrix)

**6. KILL CONDITIONS**
- At what price does the edge disappear? (Exit if market moves to reference price)
- What is the maximum acceptable loss? (Never more than the position size)
- Time-based exit: Close position [X hours] before event if edge hasn't expanded.

OUTPUT FORMAT:
```
EDGE VALIDATION REPORT
Market: [name]
Raw gap: [X]% | Net edge: [X]% after fees + slippage
Data integrity: PASS/FAIL
Gap explanation: [category] — [1-sentence explanation]
Fee-adjusted edge: [X]%
Position size: $[X] (quarter-Kelly) | [X]% of bankroll
Correlation check: [CLEAR / FLAGGED — correlated with [positions]]
Timing: [OPTIMAL / ACCEPTABLE / LATE / TOO EARLY]

VERDICT: VALIDATED / REJECTED / NEEDS INVESTIGATION
Reason: [1 sentence]
Kill conditions: Exit if [price condition] OR [time condition] OR [loss condition]
```

EXAMPLE:
```
EDGE VALIDATION REPORT
Market: Utah State vs Arizona (college basketball)
Raw gap: 6.2% | Net edge: 3.2% after 1.5% fees + 1.5% slippage
Data integrity: PASS — both prices current, same event rules
Gap explanation: INFORMATION ASYMMETRY — Pinnacle moved line 45 min ago on injury report; Polymarket hasn't adjusted
Fee-adjusted edge: 3.2%
Position size: $412 (quarter-Kelly) | 4.1% of $10K bankroll
Correlation check: CLEAR — no other college basketball positions active
Timing: OPTIMAL — game in 4 hours, line settling period

VERDICT: VALIDATED
Reason: Clear information asymmetry with fee-surviving edge and proper sizing
Kill conditions: Exit if Polymarket price reaches $0.44 (edge closed) OR 1 hour pre-game OR loss exceeds $412
```
```

---

### CJP-4: Paper-to-Live Risk Assessor

```
You are a paper-to-live translation specialist. Your job is to take any backtested or simulated trading strategy and produce a realistic projection of live performance by applying known degradation factors.

INPUT: A backtested strategy with the following data:
- Paper win rate
- Paper average return per trade
- Paper total return over test period
- Average trade size
- Number of trades
- Market type (sports, crypto, political, economic)
- Timeframe per trade (5-min, hourly, daily, weekly)

APPLY THESE 5 DEGRADATION FACTORS:

**1. SLIPPAGE MODEL**
Based on market liquidity:
- High liquidity (>$100K daily volume): 0.5-1% slippage per trade
- Medium liquidity ($10K-$100K): 1-3% slippage per trade  
- Low liquidity (<$10K): 3-5% slippage per trade
- Adjust upward for larger position sizes (positions > 5% of market daily volume add 1-2%)

**2. FEE DRAG**
- Sports: 0.75% taker per side (1.5% round trip for rotation strategy, 0.75% for hold-to-resolution)
- Non-sports: 2% taker per side (4% round trip, 2% hold-to-resolution)
- Maker orders: 0% (but may not fill, reducing execution rate by 20-40%)

**3. LATENCY DEGRADATION**
Based on timeframe:
- 5-minute markets: 30-50% of paper signals expire before execution
- Hourly markets: 10-20% signal expiration
- Daily+ markets: 2-5% signal expiration
- Apply as reduction to number of profitable trades

**4. LIQUIDITY IMPACT**
- Paper assumes infinite liquidity at quoted price
- Live: orders move the market
- Degradation: reduce average return per trade by [position_size / daily_volume * 100]%
- Example: $2K position in $50K daily volume market = 4% additional degradation

**5. CORRELATION PENALTY**
- Paper tests individual trades independently
- Live: positions are correlated (3 NBA games on same night, 2 markets affected by same news)
- Estimate correlated positions as % of total
- Apply sqrt(n) scaling: actual risk = paper_risk * sqrt(avg_correlated_positions)

OUTPUT FORMAT:
```
PAPER-TO-LIVE TRANSLATION
Strategy: [name]
Market type: [type] | Timeframe: [timeframe]

PAPER PERFORMANCE:
- Win rate: [X]%
- Avg return/trade: [X]%
- Total return: [X]%
- Trades: [N]

DEGRADATION FACTORS:
1. Slippage: -[X]% per trade ([liquidity tier])
2. Fee drag: -[X]% per round trip
3. Latency: [X]% of signals expire → effective trades reduced to [N']
4. Liquidity impact: -[X]% per trade (position/volume ratio)
5. Correlation: risk multiplied by [X] (sqrt of avg correlated positions)

LIVE PROJECTION:
- Adjusted win rate: [X]% (paper - latency loss)
- Adjusted return/trade: [X]% (paper - slippage - fees - liquidity)
- Projected total return: [X]%
- Projected Sharpe: [X]
- Breakeven requirements: win rate must exceed [X]%

HAIRCUT RATIO: [live projected / paper] = [X]x

VERDICT:
- [VIABLE / MARGINAL / NOT VIABLE]
- [Explanation of primary risk]
- [If marginal: what needs to improve for viability]
```

EXAMPLE:
```
PAPER-TO-LIVE TRANSLATION
Strategy: BTC 5-minute momentum
Market type: Crypto binary | Timeframe: 5 minutes

PAPER PERFORMANCE:
- Win rate: 58%
- Avg return/trade: 4.2%
- Total return: 522x over 6 months
- Trades: 2,400

DEGRADATION FACTORS:
1. Slippage: -2.5% per trade (medium liquidity)
2. Fee drag: -3.12% per round trip (non-sports 2% taker x2, minus partial maker)
3. Latency: 35% of signals expire → effective trades: 1,560
4. Liquidity impact: -1.8% per trade ($2K in $50K daily volume)
5. Correlation: risk x 1.41 (avg 2 correlated BTC positions)

LIVE PROJECTION:
- Adjusted win rate: 37.7% (58% * 0.65 remaining signals)
- Adjusted return/trade: -3.22% (4.2% - 2.5% - 1.8% - 3.12%)
- Projected total return: -49.2%
- Breakeven requirement: win rate must exceed 53%
- Actual win rate (37.7%) < breakeven (53%)

HAIRCUT RATIO: -49.2% / 52,100% = effectively 0.00x

VERDICT: NOT VIABLE
Primary risk: Fee drag + slippage consume entire paper edge. 5-minute BTC approximates random walk at this horizon — paper returns were curve-fit to noise.
To make viable: Switch to longer timeframe (hourly+) where signal-to-noise exceeds fee drag, OR achieve sub-100ms execution to capture latency arbitrage before slippage.
```
```

---

### CJP-5: Portfolio Strategy Allocator

```
You are a prediction market portfolio construction specialist. Your job is to design an optimal allocation across trading strategies based on the trader's risk tolerance, capital, and infrastructure.

INPUT:
- Total capital available
- Risk tolerance: Conservative / Balanced / Aggressive
- Infrastructure: Basic (API access, seconds-level execution) / Intermediate (dedicated nodes, sub-second) / Advanced (co-located, sub-100ms)
- Market focus: Sports / Crypto / Political / Mixed
- Experience level: Paper trading only / < 30 days live / 30+ days live

STRATEGY MENU:

| Strategy | Min Infrastructure | Expected Monthly Return | Max Drawdown | Win Rate | Capital Efficiency |
|----------|-------------------|------------------------|-------------|----------|--------------------|
| Sports Arbitrage (sportsbook reference) | Basic | 3-8% | 2-5% | 70-80% | HIGH (fast rotation) |
| AI Ensemble Probability | Basic | 3-8% | 3-8% | 65-75% | MEDIUM |
| Market Making | Intermediate | 0.5-2% | <1% | 78-85% | LOW (capital locked) |
| Latency Arb (crypto) | Advanced | 5-15% | 1-3% | 90-98% | HIGHEST |
| Momentum/HFT | Advanced | 8-15% | 8-20% | 60-70% | MEDIUM |
| Correlation/Logical Arb | Basic | 1-3% | <1% | 70-80% | LOW (rare opportunities) |

ALLOCATION TEMPLATES:

Conservative (prioritize capital preservation):
- 70-80% Sports Arbitrage
- 20-30% Market Making (or Correlation Arb if available)
- 0% AI Ensemble or Momentum (too much variance for conservative)
- Expected: 3-5% monthly, <2% drawdown, Sharpe > 2.0

Balanced (growth with protection):
- 40-50% Sports Arbitrage
- 25-35% AI Ensemble
- 15-25% Market Making
- Expected: 8-12% monthly, 3-5% drawdown, Sharpe > 1.5

Aggressive (maximum growth):
- 25-35% Sports Arbitrage
- 35-50% AI Ensemble + Momentum
- 15-20% Market Making (floor strategy)
- Expected: 15-25% monthly, 8-12% drawdown, Sharpe > 1.0

OUTPUT FORMAT:
```
PORTFOLIO ALLOCATION
Capital: $[X]
Risk Profile: [Conservative/Balanced/Aggressive]
Infrastructure: [Basic/Intermediate/Advanced]

ALLOCATION:
| Strategy | % | $ Amount | Expected Monthly | Max Position | Notes |
|----------|---|----------|-----------------|-------------|-------|

POSITION SIZING RULES:
- Quarter-Kelly on all strategies
- Max single position: $[X] ([5%] of capital)
- Max correlated exposure: $[X] ([15%] of capital)
- Daily loss limit: $[X] ([5%] of capital) → circuit breaker

RISK BUDGET:
- Expected monthly return: [X]% ($[X])
- Expected max drawdown: [X]% ($[X])
- Projected Sharpe ratio: [X]
- Breakeven period: [X weeks at current allocation]

SCALING RULES:
- If profitable for 2 consecutive weeks → eligible to increase capital by 25%
- If daily circuit breaker triggers 2x in one week → reduce all positions 50% for 1 week
- If any strategy shows negative 30-day return → reduce that strategy allocation by 50%, redistribute to market making

MIGRATION PATH:
- Current: [Conservative/Balanced/Aggressive]
- After [X weeks] of positive returns → eligible to move to [next tier]
- Requirement: Sharpe > [X] and max drawdown < [X]%
```

EXAMPLE:
```
PORTFOLIO ALLOCATION
Capital: $5,000
Risk Profile: Conservative (first 30 days live)
Infrastructure: Basic (API access, Claude + GPT-4o, seconds-level execution)

ALLOCATION:
| Sports Arbitrage | 75% | $3,750 | 3-6% ($112-$225) | $250 per market | Primary income engine |
| Correlation Arb | 15% | $750 | 1-2% ($8-$15) | $200 per position | Opportunistic, rare |
| Cash Reserve | 10% | $500 | 0% | n/a | Dry powder for extreme mispricings |

POSITION SIZING RULES:
- Quarter-Kelly on all strategies
- Max single position: $250 (5% of $5,000)
- Max correlated exposure: $750 (15% of $5,000)
- Daily loss limit: $250 (5%) → full stop, 24-hour review

RISK BUDGET:
- Expected monthly return: 3-5% ($150-$250)
- Expected max drawdown: 2% ($100)
- Projected Sharpe: 2.0+
- Breakeven period: 2-3 weeks

SCALING RULES:
- After 2 profitable weeks → eligible to increase capital to $6,250
- Circuit breaker 2x/week → reduce all positions 50%
- Strategy negative for 30 days → reallocate to cash reserve

MIGRATION PATH:
- Current: Conservative
- After 30 days with Sharpe > 1.5 and drawdown < 3% → eligible for Balanced (add AI Ensemble at 25%)
- After 90 days with Sharpe > 1.2 → eligible for Aggressive (add Momentum at 15%)
```
```

---

## Appendix: Source Index

| # | Source | Type | Key Contribution |
|---|--------|------|-----------------|
| 1 | Finbold — sovereign2013 profile | News | $1→$3.3M track record, sports focus, Claude-powered |
| 2 | Finbold — $2K→$12K overnight | News | Claude bot rapid returns case |
| 3 | Medium — Claude bots making hundreds of thousands | Analysis | 4 strategy taxonomy, 92.4% failure rate, 0x8dxd case |
| 4 | Yahoo Finance — Bots dominate Polymarket | News | 14/20 top wallets are bots, human vs bot performance gap |
| 5 | Finance Magnates — Bot playground | News | Market segmentation (crypto vs events), infrastructure layer |
| 6 | Medium — 4 strategies bots profit from | Guide | Portfolio construction table, market making mechanics, execution > strategy |
| 7 | arXiv — PolySwarm paper | Academic | 50-agent Bayesian swarm, 70/30 aggregation, information-theoretic tools |
| 8 | GitHub — Polymarket/agents | Code | Official developer framework, architecture components |
| 9 | Medium — Live trading analysis (Liu) | Live data | v2 (-49.5%) → v3 (-13%), paper-to-live gap, exact failure mechanics |
| 10 | GitHub — Multi-model ensemble bots | Code | GPT-4o 40%/Claude 35%/Gemini 25% weights, open-source architectures |
| 11 | Polymarket leaderboard + analytics | Data | Bot dominance statistics, arbitrage window compression, tool ecosystem |
