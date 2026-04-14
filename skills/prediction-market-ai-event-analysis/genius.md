# Prediction Market AI Event Analysis — Genius Context

> Load this file before executing any workflow when deep analysis is required.
> Contains the full extraction intelligence — 12 Genius Patterns, 10 Hidden
> Knowledge items, 3 Exemplars + 1 Anti-Exemplar, 7 Signature Moves, and
> Quality Rubric. Dense, practitioner-oriented.

---

## The Central Thesis

Prediction market trading is **information-transfer arbitrage, not forecasting**. The 7.6% of wallets that profit detect when market price deviates from a superior reference price (sportsbook odds, exchange spot prices, multi-model ensemble consensus) and capture the convergence. sovereign2013's $1-to-$3.3M run proves it: 37,247 bets in ~8 months, almost exclusively sports, Claude-powered, multiple bets per minute. The bot never asks "will the Lakers win?" It asks "is Polymarket wrong relative to Vegas?"

---

## 12 Genius Patterns

### GP-1: The Vegas Anchor (Reference Price Arbitrage)
**Source**: Sources 1, 3, 10 | **Confidence**: HIGH

sovereign2013 treats professional sportsbook odds as ground truth and exploits Polymarket deviations. Professional sportsbooks employ quantitative analysts with survival-level incentives for accuracy. Polymarket pricing comes from retail bettors, crypto participants, and sentiment-driven actors.

**The mechanic**: When Pinnacle prices Lakers at 62% implied probability and Polymarket prices them at 55%, the 7-point gap minus fees (0.75% sports taker) represents extractable edge. You don't need to be smarter than the market. You need the market to be dumber than another market. In sports, it reliably is.

### GP-2: The Ensemble Independence Requirement
**Source**: Sources 6, 7, 10 | **Confidence**: HIGH

Each model must forecast INDEPENDENTLY before aggregation. GPT-4o analyzes first. Claude analyzes separately. Gemini analyzes separately. Then results combine. If models see each other's outputs, you get herding — three models that agree because they influenced each other provide zero additional signal beyond one model.

**Weight allocation**: GPT-4o 40% (broad analytical reasoning, statistical pattern recognition), Claude 35% (source credibility evaluation, nuanced uncertainty reasoning), Gemini 25% (contrarian perspective, alternative data interpretation). Weights from open-source "Fully Autonomous Polymarket AI Trading Bot," reflecting observed performance across political, sports, and economic markets.

**The disagreement signal**: High model disagreement is itself actionable.
- All 3 agree: high confidence
- 2 agree, 1 dissents: moderate confidence, investigate the dissent
- All 3 disagree: NO TRADE

The pattern of disagreement matters more than the direction — Claude dissenting on credibility carries different weight than GPT-4o dissenting on statistics.

### GP-3: The Paper-to-Live Haircut (The 0.5x-0.7x Rule)
**Source**: Source 9 | **Confidence**: HIGHEST (verified by live trading data with exact loss figures)

**This is the most valuable pattern in the entire research.** Jung-Hua Liu's live trading analysis is the only source that honestly reports FAILURE with exact numbers.

**The data**:
- Paper simulation: 522x returns
- Live v2: -49.5% loss (4 wins / 11 losses)
- Live v3: -13% loss (2 wins / 2 losses)

**The 5 causes of degradation**:
1. **Slippage**: Your order moves market price against you. On thin Polymarket books, $2K moves price 2-4 cents.
2. **Latency**: Between signal generation and order execution, price changes. Even 500ms matters in 5-minute markets.
3. **Fee drag**: 1.56% fee at $0.50 entry + exit. Breakeven win rate is ~53%, not 50%.
4. **Liquidity illusion**: Quoted price exists at specific depth. Full order may not fill at that price.
5. **Micro-bounce reversion**: v2 weighted 65% of signal on final 60 seconds, capturing transient bounces that reverted by window close.

**Executable rule**: Whatever paper backtest shows, multiply expected edge by 0.5-0.7 before committing capital. If the edge doesn't survive the haircut, it isn't real. This single rule separates the 7.6% from the 92.4%.

### GP-4: Quarter-Kelly Consensus
**Source**: Sources 6, 7, 9 | **Confidence**: HIGH

Every profitable bot architecture converges on quarter-Kelly: f = 0.25 * f_star.

- **Why not full Kelly**: Extreme variance. 5 losses on full Kelly can wipe 50%+ of bankroll.
- **Why not half-Kelly**: Prediction market edge estimates have wider error bars than traditional finance. Quarter-Kelly provides additional buffer against edge overestimation.

**Hard caps layered on top**:
- Max single position: 5-10% of bankroll (even if Kelly says more)
- Max correlated exposure: 15% (5 NBA games same night = correlated)
- Daily loss limit: 5% drawdown triggers circuit breaker, halt all trading

**Formula**:
```
Edge = (Your_Probability - Market_Price) / (1 - Market_Price)
Position = 0.25 * Edge * Bankroll
Cap at min(Position, 0.05 * Bankroll)
```

### GP-5: The Bayesian Swarm (70/30 Market Integration)
**Source**: Source 7 (PolySwarm paper) | **Confidence**: HIGH (academic)

PolySwarm's two-stage aggregation:

**Stage 1**: 25 of 50 specialized LLM personas independently evaluate. Confidence-weighted average into p_swarm.

**Stage 2**: Bayesian mixture: 0.70 * p_swarm + 0.30 * p_market.

**Why 70/30**: Market price contains information the swarm doesn't have (other traders, insider knowledge). Ignoring it is arrogant. Deferring entirely means you can never find edge.

**Why 25 of 50**: Marginal accuracy flattens after ~25. Random sampling prevents any single persona from dominating. A contrarian agent correct 30% of the time provides massive value on those occasions but dilutes signal when wrong. Random sampling lets the system benefit without systematic dilution.

**Trade trigger**: combined_p > market_p + 5% AND std_dev < 30%.

### GP-6: Latency Arbitrage Physics (The Shrinking Window)
**Source**: Sources 3, 4, 5, 11 | **Confidence**: HIGH

- 2024: Average arbitrage window = 12.3 seconds
- 2026: Average arbitrage window = 2.7 seconds
- 73% of arbitrage profits captured by sub-100ms execution bots

The 0x8dxd case: $313 to $438K on 15-minute BTC/ETH/SOL contracts. 98% win rate, 6,615 predictions. Strategy: latency, not forecasting. When BTC moves 0.05%+ on Binance but Polymarket hasn't repriced, actual probability is ~85% while market shows 50/50.

**Entry barrier**: Now a hardware problem. New entrants without infrastructure cannot compete in sub-5-second windows. Alpha has decayed into infrastructure arms race.

### GP-7: The Portfolio Construction Insight
**Source**: Source 6 | **Confidence**: MEDIUM-HIGH

**Portfolio allocation across strategy types matters more than any individual strategy.**

| Profile | Allocation | Monthly Return | Max Drawdown | Sharpe |
|---------|-----------|---------------|-------------|--------|
| Conservative | 80% arb, 20% MM | 4.2% | 0.8% | 2.1 |
| Balanced | 50% arb, 30% AI ensemble, 20% MM | 11.7% | 3.2% | 1.6 |
| Aggressive | 30% arb, 50% AI/momentum, 20% MM | 23.4% | 8.9% | 1.1 |

Market making provides the steady floor (0.5-2% monthly, <1% drawdown). Arbitrage provides core return. AI ensemble provides upside. The mix determines risk-adjusted outcome.

**Market making floor**: Simultaneous buy/sell with 4-cent spreads. Never exceed 30% one-side exposure. Widen spreads during volatility. Withdraw before major news.

### GP-8: The Information-Theoretic Edge Detectors
**Source**: Source 7 (PolySwarm paper) | **Confidence**: HIGH

Four mathematical detection tools:

1. **KL Divergence**: Measures probability distribution divergence. Applied to cross-market inconsistencies (e.g., "Trump wins" vs "Republican wins" pricing mismatch).
2. **Jensen-Shannon Divergence**: Symmetric, bounded KL variant. Better for comparing two market prices.
3. **Negation Pair Checks**: YES + NO must sum to $1.00. When $0.97, buying both guarantees 3% profit. By 2026, nearly exhausted.
4. **Bayesian Network Consistency**: Maps logical relationships across 100+ markets via graph theory. "Trump wins 2028" at 35% means "Republican wins" CANNOT be below 35%. Violations >3% trigger multi-leg trades within 500ms.

These are **detection mechanisms**, not strategies. Most traders skip detection and trade on narrative.

### GP-9: The Structural Market Segmentation
**Source**: Source 5 | **Confidence**: HIGH

**Ultra-short crypto (5-min, 15-min BTC/ETH/SOL)**: Bot-dominated. 98%+ profits to sub-100ms bots. Humans cannot compete. Edge = speed. Reference = exchange spot.

**Longer-dated events (sports, elections, economics)**: Retain human-judgment opportunity. Edge = information processing, not latency. Reference = sportsbook odds (sports), polling (politics), models (economics). 2-15 minute repricing window exploitable by Claude-speed bots.

**Strategic implication**: Do NOT start with ultra-short crypto. Start with sports arbitrage. Lower infrastructure, public reference prices, wide persistent gap.

### GP-10: The v2-to-v3 Iteration Model
**Source**: Source 9 | **Confidence**: HIGHEST (live data with exact parameters)

**v2 failure** (-49.5%): 80% trades favored UP during downtrend. 65% signal weight on final 60 seconds = noise capture. No trend filter.

**v3 fixes** (-13%): Longer lookback weights (120s, 240s). 10-minute hard trend filter. Confidence halved on conflicting signals. Counter-trend rejection unless BTC > 0.10%.

**The 7x improvement**: v3 didn't become profitable. It reduced capital destruction by 7x. Realistic trajectory: catastrophic loss -> controlled loss -> breakeven -> modest profit.

**INFERRED**: sovereign2013 went through equivalent iterations. The $1 starting balance suggests early versions tested with minimal capital. The $3.3M was not v1.

### GP-11: The Hallucination-Correlation Risk
**Source**: Source 7 | **Confidence**: HIGH

LLMs confidently assert false facts. In multi-model ensembles: **correlated hallucination**. If all three models hallucinate the same incorrect "fact," the ensemble provides false consensus, not error correction.

Models trained on overlapping data develop overlapping blind spots. GPT-4o, Claude, Gemini all learned from similar internet text. Errors correlate more than random agents.

**Mitigation**: The 30% market weight partially addresses this. Real defense: never trust ensemble factual claims without checking verifiable data (scores, schedules, injuries) against authoritative APIs. Ensemble evaluates probability. Deterministic code verifies facts.

### GP-12: Capital Rotation vs. Hold-to-Resolution
**Source**: Sources 1, 6 | **Confidence**: MEDIUM-HIGH (INFERRED from sovereign2013's trading velocity)

sovereign2013 places bets multiple times per minute across 37,247+ predictions. This implies capital rotation, not hold-to-resolution.

Buy at $0.55 when fair value is $0.62. If Polymarket converges to $0.62, you've captured 7 cents. Holding to resolution exposes you to 38% total loss risk. Selling at $0.62 locks profit, frees capital.

**Capital rotation is why $1 becomes $3.3M.** Each dollar deployed dozens or hundreds of times, each capturing small edge. The velocity of deployment, not edge size, drives the exponential curve.

---

## 10 Hidden Knowledge Items

### HK-1: Why Sports, Not Crypto or Politics

Sports have the best reference price. Professional sportsbook odds are priced by specialists with decades of expertise and survival-level accuracy incentives. No equivalent reference exists for crypto (exchange prices are spot, not probabilistic) or politics (polling aggregates are noisy/lagging). Sports have the tightest feedback loop: precise reference, quick resolution, thousands of repeating matchup types per season.

### HK-2: Why Claude at 35% (Not 25%, Not 40%)

Claude's weight reflects **source credibility evaluation**. In markets with information asymmetry (injury reports, insider leaks, conflicting sources), the critical question isn't "what does data say?" but "which sources to trust?"

When one journalist reports an injury and three others repeat without independent verification, Claude identifies the 3:1 ratio as 1:0 actual sources. GPT-4o is stronger at statistical pattern recognition (40%). Gemini provides the contrarian check (25%). Weights reflect complementary capabilities, not quality rankings.

### HK-3: The 92.4% Failure Taxonomy

50,000+ wallets analyzed. Three dominant failure modes:

1. **Oversized positions**: 20-50% bankroll on single events. One loss destroys months.
2. **Late entries**: Seeing mispricing after half-corrected. Edge at entry < fees.
3. **Inconsistent risk management**: Disciplined on wins, emotional on losses. Holding losers hoping for reversal.

Humans underperform bots by ~18% due to these three behavioral patterns. Bot advantage is emotional absence.

### HK-4: The PolySwarm 25-of-50 Design Choice

50 distinct LLM personas but only 25 per evaluation, sampled without replacement. Marginal accuracy flattens after ~25 while cost scales linearly. Random subsampling prevents any persona from dominating. Contrarian agent correct 30% of the time provides massive value occasionally — random sampling lets system benefit without systematic dilution.

### HK-5: Why "Execution Is 70%" Is Not a Cliche

**Strategy (30%)**: Identifying that Polymarket is mispriced by 5 points vs Pinnacle. Easy.

**Execution (70%)**:
- Getting filled at quoted price (slippage)
- Filling before price moves (latency)
- Filling at full size (liquidity)
- Paying less than edge in fees (maker vs taker)
- No 5 correlated positions going wrong (portfolio risk)
- Circuit breaker actually halting at 5% drawdown (discipline)
- Rebalancing as new info arrives (dynamic management)

Strategy with 10% edge + poor execution = 3%. Strategy with 5% edge + perfect execution = 4%.

### HK-6: The API Cost Trap

PolySwarm: "thousands per day in API costs at scale." 25 agents x 200 markets x 12 scans/min x 60 min x 24 hr = 86.4M inference calls/day. Even at $0.001/call = $86K/day. Realistic optimization brings to $1-5K/day — still major.

This is why sovereign2013's sports arbitrage (FREE sportsbook odds as reference) is structurally superior to brute-force multi-agent approaches. Bot must be profitable enough to cover API costs before generating returns.

### HK-7: Front-Running as Predator Strategy

Some bots trade against OTHER BOTS. Monitoring the mempool (pending Polygon transactions), front-running bots detect incoming large buys, purchase first, sell into the demand.

Implication: Your bot competes against bots exploiting YOUR orders. Defense: batch transactions, private RPC nodes, never place large market orders signaling intent.

### HK-8: The Gambot Principle (Stripping the Vig)

Pull odds from Pinnacle (sharpest book), remove house edge, calculate true implied probabilities. First step of sovereign2013's inferred strategy.

**Why Pinnacle**: Lowest margins (2-3% vig major sports), accepts and adjusts to sharp bets rather than limiting them. Lines most closely approximate true probabilities. DraftKings/FanDuel run higher margins and limit sharps.

**Conversion**: Pinnacle Lakers -150 / Opponents +130 -> implied 60% / 43.5% = 103.5% total (3.5% vig). Stripped: 60/103.5 = 57.97%, 43.5/103.5 = 42.03%. These become reference for Polymarket comparison.

### HK-9: Why Live v3 Still Lost (The Random Walk Problem)

"5-minute BTC options approximate random walks at short horizons." No signal engineering can reliably predict 5-minute random walk direction. 522x paper returns were curve-fit to historical noise.

**Lesson**: Short-duration crypto binary options are the WORST market for AI trading — underlying process closest to random. Long-duration events (NBA Finals, GDP exceeds X) have actual information content AI can process.

### HK-10: The $40M Extraction Number

Arbitrage traders extracted ~$40M from Polymarket Apr 2024-Apr 2025. Every dollar from the 7.6% came from the 92.4%. Bots aren't creating value — extracting it. As bot penetration increases, extractable capital pool shrinks. Bots eating each other's lunch.

**Long-term**: Self-correcting. More bots = compressed edges, shrinking windows, declining returns. The $1-to-$3.3M era may not be repeatable. First-mover advantage was real and is fading.

---

## Hall of Fame Exemplars

### Exemplar 1: The PolySwarm Bayesian Aggregation Pipeline
**Source**: Source 7 (Academic) | **Why exemplary**: Highest rigor

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
[Stage 1: Confidence-weighted average -> p_swarm]
  |
  v
[Stage 2: Bayesian mixture -> 0.70 * p_swarm + 0.30 * p_market]
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

Gold standard because: respects market (30% weight), preserves diversity (random sampling), quantifies uncertainty (std dev filter), sizes conservatively (quarter-Kelly), hard stop (daily loss limit).

### Exemplar 2: The Live Trading Failure Analysis (v2 to v3)
**Source**: Source 9 | **Why exemplary**: Only honest live performance data

**v2**: 4W/11L, -49.5% ROI. Root cause: 65% weight on final 60s captured micro-bounces. 80% trades favored UP in downtrend.

**v3**: 2W/2L, -13% ROI. Fixes: longer lookbacks, 10-min trend filter, confidence halving, counter-trend rejection.

Matters more than success stories because it has zero survivorship bias. Exact technical parameters of failure + exact fixes. Reproducible knowledge.

### Exemplar 3: The Utah State Bet ($1.73M Volume, $179K Profit)
**Source**: Source 1 | Demonstrates sovereign2013's operational mechanics.

Largest documented single bet: Utah State vs Arizona (college basketball). $1.73M volume, $179K profit.

**INFERRED mechanics**: At quarter-Kelly, implies 10%+ perceived edge and $5-10M+ bankroll. College basketball chosen over NBA because less attention = less efficient pricing. Volume executed in increments as liquidity was available (consistent with "multiple bets per minute" pattern). Information asymmetry: sportsbooks model these accurately, Polymarket overweights name recognition.

### Anti-Exemplar: The 92.4%
**Source**: Sources 3, 4, 5

50,000+ wallets. 92.4% unprofitable. Five failure modes:
1. **Predict instead of arbitrage**: Buy "Yes" because they think team will win, without checking if price reflects that probability.
2. **Size on confidence, not Kelly**: "I'm really sure" -> 30% bankroll on one bet.
3. **Trade wrong markets**: Humans in ultra-short crypto where bots capture 73% of profits.
4. **Ignore fees**: 2% edge minus 1.56% fees minus 2-4 cents slippage = negative.
5. **Hold losers**: Disposition effect — hold losing positions hoping for reversal instead of cutting and rotating.

---

## 7 Signature Moves

### SM-1: The Line Movement Detector
**INFERRED**: sovereign2013's primary pattern.

Monitor sportsbook line movements real-time. When a line moves (injury, lineup change, sharp money), immediately check if Polymarket adjusted. If not, execute. Timing window: 2-15 minutes between sportsbook move and Polymarket adjustment. Not fast enough for latency arb but more than enough for Claude-speed reasoning.

### SM-2: The Ensemble Credibility Arbiter

When model outputs diverge, route disagreement through credibility lens: Is disagreement about DATA (GPT-4o likely right), SOURCES (Claude likely right), or CONSENSUS (Gemini's contrarian view worth investigating)? Nature of disagreement, not direction, determines trust.

### SM-3: The Cumulative Probability Violation Scan

Monitor related markets for logical inconsistencies. Mutually exclusive outcomes summing >100% (e.g., recession timing probabilities = 111%) = guaranteed spread minus transaction costs. Requires graph-theory mapping of 100+ market relationships.

### SM-4: The Market Making Floor

20% portfolio to automated market making. Simultaneous limit orders YES/NO with 4-cent spreads. Never exceed 30% one-side inventory. Widen spreads during volatility. Withdraw before major news. Generates 0.5-2% monthly regardless of prediction accuracy.

### SM-5: The Gap Explanation Protocol

Every identified edge demands a REASON before execution:

| Explanation | Action |
|------------|--------|
| Information asymmetry (Polymarket doesn't know what sportsbooks know) | EXECUTE |
| Narrative mispricing (public sentiment over/underweighting) | EXECUTE |
| Low liquidity (stale price, thin book) | EXECUTE CAREFULLY |
| Data error (feed wrong or delayed) | DO NOT EXECUTE |
| Structural difference (different rules, overtime, etc.) | DO NOT EXECUTE |
| Unknown | DO NOT EXECUTE |

### SM-6: The Timing Matrix

| Time to Event | Posture |
|---------------|---------|
| > 48 hours | Monitor only. Lines will move. |
| 24-48 hours | Begin scanning for persistent gaps. |
| 6-24 hours | Primary trading window. Lines settling. |
| 1-6 hours | Peak edge window. Last line moves, max Polymarket lag. |
| < 1 hour | Exit window. Close if target reached. Avoid new entries. |
| Live/in-play | Different game. Real-time feeds required. Much higher variance. |

### SM-7: The Circuit Breaker Protocol

Non-negotiable. Automated. No override without manual review.

- 5% daily drawdown -> halt ALL trading 24 hours
- 3 consecutive losses -> reduce positions 50% for next 10 trades
- Any single position > 10% bankroll -> auto-reject
- Correlated exposure > 15% -> block new entries in same category

---

## Expert-Specific Quality Rubric

| Dimension | Score 4 | Score 7 | Score 10 |
|-----------|---------|---------|----------|
| **Edge Identification** | "I think Lakers will win" — no reference, no quantification | Gap with sportsbook anchor but thin explanation or fees ignored | Quantified gap (bps) + sportsbook reference + WHY gap exists + fee-adjusted edge |
| **Position Sizing** | Gut feel ("$500 on this") | Kelly-based but missing caps or no correlation check | Quarter-Kelly + 5% single cap + 15% correlated cap + 5% daily circuit breaker |
| **Ensemble Quality** | Single model or rubber stamp | Models used but not independently, or disagreement ignored | Independent forecasting -> weighted aggregation -> disagreement analysis -> credibility resolution |
| **Execution Realism** | Paper = live assumed | Some costs mentioned but unquantified | 0.5x-0.7x haircut applied; slippage, latency, liquidity, fee drag all quantified |
| **Risk Management** | No downside protection | Some limits but incomplete | Full stack: position caps + correlation limits + daily breaker + kill conditions + rebalancing |
| **Market Selection** | Whatever looks interesting | One type without clear rationale | Explicit segmentation matched to infrastructure capability |

---

## sovereign2013 Inferred Methodology (ALL ITEMS MARKED INFERRED)

Based on wallet analysis of 37,247 bets, $1 to $3.3M, sports-focused, Claude-powered:

1. **INFERRED**: Pulls Pinnacle odds, strips vig, calculates true implied probabilities (Gambot principle)
2. **INFERRED**: Compares against Polymarket prices in real-time
3. **INFERRED**: Uses Claude for credibility evaluation on ambiguous signals (injury reports, conflicting sources)
4. **INFERRED**: Applies quarter-Kelly with hard caps (position size implied by $1.73M Utah State volume)
5. **INFERRED**: Rotates capital rather than holding to resolution (multiple bets per minute pattern)
6. **INFERRED**: Focuses on college sports over major leagues (wider inefficiency gaps)
7. **INFERRED**: Iterated through multiple bot versions (the $1 start suggests early testing with minimal capital)
8. **INFERRED**: Monitors line movements as primary trigger, not static odds comparison

The bot's code is not public. These inferences come from on-chain behavior, trading velocity, market selection patterns, and position sizes. Treat as high-confidence hypotheses, not confirmed methodology.
