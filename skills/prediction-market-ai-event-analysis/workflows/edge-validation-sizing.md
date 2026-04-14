---
description: "Take identified price discrepancies, run 6-point validation (data integrity, gap explanation, fee-adjusted edge, quarter-Kelly sizing, timing, kill conditions), and output a complete validated trade plan or rejection with reasons."
---

# Edge Validation & Sizing

> **Crown Jewels 2 + 3** — From GP-3 (Paper-to-Live Haircut), GP-4 (Quarter-Kelly), GP-12 (Capital Rotation), SM-5 (Gap Explanation Protocol), SM-6 (Timing Matrix), SM-7 (Circuit Breaker)

## Purpose

Take an identified price discrepancy (from the Odds Discrepancy Scanner or Multi-Model Ensemble) and determine whether it represents real exploitable edge or is noise/trap/error. If validated, produce a complete trade plan with entry, sizing, exit targets, and kill conditions. If rejected, explain exactly why.

This workflow embodies the principle that **execution is 70% of success**. Identifying the gap is the easy part. Getting from gap to profit requires validation, sizing, timing, and discipline.

---

## Input Requirements

For each market being validated, you need:
- Market name and event details
- Polymarket current YES/NO prices (must be <60 seconds old)
- Reference price and source (sportsbook odds, ensemble probability, or both)
- Raw gap percentage
- Current bankroll
- List of all active positions (for correlation check)
- Time to event resolution

---

## Validation Point 1: Data Integrity

**This is a hard gate. Failure here = no trade, no exceptions.**

Run these checks:

| Check | Pass Condition | Failure Mode |
|-------|---------------|--------------|
| Polymarket price freshness | Updated within 60 seconds | Stale price — gap may not exist |
| Reference price freshness | Updated within 5 minutes (sportsbook) or 10 minutes (ensemble) | Stale reference — gap may be outdated |
| Event match | Both prices reference identical event with identical rules | Different overtime rules, different date, wrong team — comparing different products |
| Data feed integrity | No known API outages, no manual entry errors | Feed lag creates phantom gaps |
| Market status | Market is active and accepting orders | Frozen/paused/resolved markets |

**Output**: PASS or FAIL with specific failure reason. If FAIL, stop. Do not proceed to Point 2.

---

## Validation Point 2: Gap Explanation

**Every gap demands a reason.** Classify into one of six categories:

### Category 1: Information Asymmetry (VALID EDGE)
Polymarket participants don't have information that the reference source has. Examples:
- Sportsbook line moved on injury report that hasn't propagated to Polymarket
- Sharp money moved the line, retail hasn't noticed
- Lineup change announced, Polymarket still pricing old lineup

**Action**: PROCEED. This is the core edge type. Monitor for gap closure — once Polymarket catches up, edge disappears.

### Category 2: Narrative Mispricing (VALID EDGE)
Public sentiment inflating or deflating probability beyond what fundamentals support. Examples:
- Big-name team overvalued because of brand recognition
- Recency bias (team won last 3, market overweights streak)
- Media narrative pushing price away from fair value

**Action**: PROCEED. But recognize this edge type may correct faster than information asymmetry as narrative shifts.

### Category 3: Low Liquidity (VALID BUT FRAGILE)
Price is stale because nobody is trading, or order book is too thin for meaningful execution.

**Warning**: Your order may BE the price movement. If the order book shows only $500 at the current price, a $200 position is fine. A $2,000 position will move the market against you.

**Action**: PROCEED CAREFULLY. Size down. Use limit orders, not market orders. Account for the fact that your entry will worsen your fill price.

### Category 4: Data Error (INVALID)
Feed is wrong, odds are from a different time, prices are for different events.

**Action**: DO NOT TRADE. Verify data sources, wait for feed correction, re-scan.

### Category 5: Structural Difference (INVALID)
Markets have different rules. Common traps:
- One market includes overtime, the other doesn't
- Different resolution dates
- "Will X happen by June" vs "Will X happen by December"

**Action**: DO NOT TRADE. You're comparing different products. The gap is real but not arbitrageable.

### Category 6: Unknown (TREAT AS INVALID)
Can't determine why the gap exists.

**Action**: DO NOT TRADE. Unexplained gaps are more often traps than opportunities. If the gap persists for 2+ hours and grows, re-evaluate. Otherwise, pass.

**Output**: Gap classification + 1-sentence explanation.

---

## Validation Point 3: Fee-Adjusted Edge

Calculate the true edge after ALL friction costs:

### Fee Calculation

```
Entry_Fee:
  Sports: 0.75% (taker) or 0% (maker, but may not fill)
  Non-sports: 2.00% (taker) or 0% (maker)

Exit_Fee (if rotating capital, not holding to resolution):
  Same as entry fee

Slippage (based on market daily volume):
  High volume (>$100K): 0.5-1.0%
  Medium volume ($10K-$100K): 1.0-3.0%
  Low volume (<$10K): 3.0-5.0%
  Add 1-2% if position > 5% of daily volume
```

### Net Edge

```
For rotation strategy (exit before resolution):
  Net_Edge = Raw_Gap - Entry_Fee - Exit_Fee - Slippage

For hold-to-resolution:
  Net_Edge = Raw_Gap - Entry_Fee - Slippage
```

### Paper-to-Live Haircut (GP-3)

```
Realistic_Edge = Net_Edge * Haircut_Factor

Haircut factors:
  Sports, high-volume market: 0.7 (best case)
  Sports, medium-volume: 0.6
  Sports, low-volume: 0.5
  Non-sports, any volume: 0.5-0.6
  Ultra-short crypto: 0.0-0.3 (effectively unviable for most)
```

### Threshold Gate

**Realistic_Edge > 2%**: PROCEED to sizing.
**Realistic_Edge 1-2%**: MARGINAL. Flag as borderline. Only proceed if classification is HIGH confidence information asymmetry AND timing is optimal (1-6h window).
**Realistic_Edge < 1%**: REJECT. Edge does not survive friction. The 92.4% lose money on trades exactly like this.

**Output**: Raw gap, fee drag, slippage estimate, net edge, realistic edge, PROCEED/MARGINAL/REJECT.

---

## Validation Point 4: Position Sizing

### Kelly Criterion (Quarter Fraction)

```
# For YES side trades:
Edge = (Your_Probability - Market_Price) / (1 - Market_Price)

# Kelly optimal fraction:
f_star = Edge / Odds
  where Odds = (1 - Market_Price) / Market_Price for YES
  or Odds = Market_Price / (1 - Market_Price) for NO

# Quarter-Kelly:
f = 0.25 * f_star

# Dollar position:
Position = f * Bankroll
```

### Hard Caps (Non-Negotiable)

| Cap | Limit | Rationale |
|-----|-------|-----------|
| Single position max | 5% of bankroll | Even if Kelly says more, edge estimates have wide error bars |
| Absolute max per trade | 10% of bankroll | NEVER exceed regardless of perceived edge |
| Final position | min(Quarter_Kelly, 5% cap) | Whichever is smaller |

### Correlation Check

**Correlated positions** = positions that could all lose from the same cause:
- Multiple NBA games same night (injury to key player affects multiple bets)
- Multiple games same league same day
- Events sharing a common driver (weather, political outcome)

```
Total_Correlated_Exposure = sum of all positions sharing correlation factor
Max_Correlated_Exposure = 15% of bankroll

If adding this position pushes correlated exposure > 15%:
  Reduce position to stay within 15% limit
  OR reject if minimum viable position is below $10
```

### Bankroll Health Check

Before sizing, verify:
- Daily loss so far: if already at 3%+ daily drawdown, reduce position by 50%
- If at 5%+ daily drawdown: CIRCUIT BREAKER. No new positions. Full stop for 24 hours.
- If 3 consecutive losses today: reduce all new positions by 50% for next 10 trades

**Output**: Quarter-Kelly position, cap-adjusted position, correlation status, final recommended size.

---

## Validation Point 5: Timing Check

Apply the Timing Matrix (SM-6):

| Time to Event | Posture | Position Approach |
|---------------|---------|-------------------|
| > 48 hours | MONITOR ONLY | Do not enter. Lines will move significantly. Edge may disappear or expand. |
| 24-48 hours | SCAN MODE | Begin tracking. Enter only if edge is large (>5% realistic) and gap is clearly explained. Use smaller position (50% of calculated size). |
| 6-24 hours | PRIMARY WINDOW | Full position sizing. Lines settling. This is where most edge lives. |
| 1-6 hours | PEAK WINDOW | Highest edge capture. Last line moves create maximum Polymarket lag. Full position sizing. |
| < 1 hour | EXIT WINDOW | Close existing positions if targets reached. Avoid NEW entries — too close to resolution, volatility spikes, and you can't exit if wrong. |
| Live/in-play | DIFFERENT GAME | Requires real-time data feeds. Much higher variance. Only trade if infrastructure supports live updates. |

### Timing Adjustments

If timing is SUB-OPTIMAL (>48h or <1h), either:
- Reduce position to 25% of calculated size (hedge against timing risk)
- Or DEFER: set alert for when market enters 6-24h window

**Output**: Timing classification, any position adjustment, optimal entry window if current timing is suboptimal.

---

## Validation Point 6: Kill Conditions

Every validated trade MUST have explicit exit criteria defined BEFORE entry. No trade without kill conditions.

### Price-Based Exit

```
Target_Exit_Price = Reference_Probability (where the edge closes)
Stop_Loss_Price = Entry_Price - (Position_Size * Max_Loss_Tolerance)

For rotation strategy:
  Take profit if Polymarket price reaches reference probability (edge captured)
  
For hold-to-resolution:
  No price exit — hold for event outcome
  But still subject to time-based and loss-based exits
```

### Time-Based Exit

```
If edge hasn't expanded within [X hours], close position:
  Sports: close 1 hour before event
  Political: close 24 hours before resolution deadline
  Economic: close when data release is imminent
```

### Loss-Based Exit

```
Maximum acceptable loss on this trade = Position_Size
Never hold through resolution if the position has already moved against you 
  AND the edge has disappeared (reference price now aligns with Polymarket)
```

### Portfolio-Level Kill Switch

```
If this trade loss would push daily drawdown past 5%:
  DO NOT ENTER
  
If already in trade and daily drawdown reaches 5%:
  Close ALL positions, not just this one
  24-hour trading halt
```

**Output**: Target exit price, stop loss level, time-based exit window, portfolio kill switch status.

---

## Final Verdict

Combine all six validation points into a single decision:

### VALIDATED
All 6 points pass. Trade plan is complete with entry, size, exit, and kill conditions.

### VALIDATED WITH CAVEATS
Points 1-2 pass, but 3-6 have minor flags (marginal edge, suboptimal timing, correlation concerns). Trade is permissible at reduced size with tighter kill conditions.

### REJECTED
Any hard failure in Points 1-2 (data integrity, gap explanation = invalid/unknown). Or realistic edge < 1% after haircut. Or circuit breaker is active.

### NEEDS INVESTIGATION
Gap explanation is uncertain. Route to Multi-Model Ensemble workflow for deeper analysis before re-validating.

---

## Output Format

```
EDGE VALIDATION REPORT
=====================

MARKET: [name]
EVENT: [details + date/time]
REFERENCE: [sportsbook/ensemble] at [probability]%
POLYMARKET: $[price] ([implied]%)

VALIDATION SUMMARY:
  1. Data Integrity:    [PASS/FAIL] — [detail]
  2. Gap Explanation:   [category] — [1-sentence why]
  3. Fee-Adjusted Edge: Raw [X]% -> Net [X]% -> Realistic [X]% — [PROCEED/MARGINAL/REJECT]
  4. Position Size:     $[X] (quarter-Kelly $[X], cap-adjusted $[X]) — [X]% of bankroll
  5. Timing:            [classification] — [adjustment if any]
  6. Kill Conditions:   Target $[X] | Stop $[X] | Time exit [X hours before event]

VERDICT: [VALIDATED / VALIDATED WITH CAVEATS / REJECTED / NEEDS INVESTIGATION]

TRADE PLAN (if VALIDATED):
  Direction:    [BUY YES / BUY NO]
  Entry price:  $[X]
  Position:     $[X] ([X]% of bankroll)
  Target exit:  $[X] (edge captured)
  Stop loss:    $[X] (max acceptable loss)
  Time exit:    [X hours before event] if target not reached
  Kill switch:  Close if daily drawdown reaches [X]%
  
  Correlated positions: [list or "none"]
  Total correlated exposure: [X]% of bankroll (limit: 15%)
  
  Expected value: $[X] (realistic edge * position)
  Risk/reward:    [X]:1

REJECTION REASON (if REJECTED):
  [Specific failure point and explanation]
  [What would need to change for this to become viable]
```

---

## Example Validated Trade

```
EDGE VALIDATION REPORT
=====================

MARKET: Utah State vs Arizona (college basketball)
EVENT: April 14, 2026 — tip-off 9:00 PM ET
REFERENCE: Pinnacle at 44.2% (stripped from -127/+107)
POLYMARKET: $0.38 (38%)

VALIDATION SUMMARY:
  1. Data Integrity:    PASS — Both prices current, same event, same rules (includes OT)
  2. Gap Explanation:   INFORMATION ASYMMETRY — Pinnacle line moved 45 min ago on injury 
                        report (Arizona starting PG questionable). Polymarket hasn't adjusted.
  3. Fee-Adjusted Edge: Raw 6.2% -> Net 3.7% (1.5% fees, 1.0% slippage) -> Realistic 2.2% (0.6x) — PROCEED
  4. Position Size:     $89 (quarter-Kelly $89, cap $500) — 0.9% of $10K bankroll
  5. Timing:            PEAK WINDOW (4 hours to tip-off) — full sizing
  6. Kill Conditions:   Target $0.44 | Stop $0.32 | Time exit 1h before tip-off

VERDICT: VALIDATED

TRADE PLAN:
  Direction:    BUY YES (Utah State)
  Entry price:  $0.38
  Position:     $89 (0.9% of bankroll)
  Target exit:  $0.44 (Polymarket converges to reference)
  Stop loss:    $0.32 (if drops 6 cents, edge thesis broken)
  Time exit:    8:00 PM ET (1h before tip-off) if target not reached
  Kill switch:  Close if daily drawdown reaches 5% ($500)
  
  Correlated positions: none
  Total correlated exposure: 0.9% (well within 15% limit)
  
  Expected value: $1.96 (2.2% * $89)
  Risk/reward:    1.5:1 (potential $5.34 gain vs $3.56 risk to stop)
```

---

## Example Rejected Trade

```
EDGE VALIDATION REPORT
=====================

MARKET: BTC 5-minute binary option
EVENT: Rolling 5-minute windows
REFERENCE: Binance spot at $67,420 (implied ~50/50 on +0.05% move)
POLYMARKET: $0.52 (52%)

VALIDATION SUMMARY:
  1. Data Integrity:    PASS — prices current
  2. Gap Explanation:   UNKNOWN — 2% gap exists but 5-min BTC approximates random walk. 
                        No structural reason for persistent edge.
  3. Fee-Adjusted Edge: Raw 2% -> Net -1.12% (2% fees, 1.12% slippage) — REJECT
  4-6: Not evaluated (rejected at Point 3)

VERDICT: REJECTED

REJECTION REASON:
  Fee drag consumes entire paper edge. 5-minute BTC options approximate random walks 
  at this horizon (HK-9). Paper returns in this segment are curve-fit to noise. 
  This is the WORST market for AI-powered trading.
  
  To become viable: Switch to hourly+ timeframe where signal-to-noise exceeds fee drag, 
  OR achieve sub-100ms execution for latency arbitrage (requires dedicated Polygon RPC 
  nodes and infrastructure investment).
```

---

## Workflow Chaining

- **If VALIDATED**: Execute trade per plan. After resolution, log result to paper trading journal or live P&L tracker.
- **If NEEDS INVESTIGATION**: Route to `multi-model-ensemble.md` for deeper probability analysis. Return here with ensemble output as new reference price.
- **If REJECTED**: Log rejection reason. If the same market type keeps getting rejected, reassess strategy allocation (GP-7).
- **After every 10 validated trades**: Calculate actual paper-to-live ratio. If ratio < 0.5, halt live trading and diagnose execution issues.

## Circuit Breaker Status Check

Before EVERY validation, confirm circuit breaker status:

```
Daily P&L: $[X] ([X]% of bankroll)
Consecutive losses: [N]
Circuit breaker: [CLEAR / TRIGGERED — reason]

If TRIGGERED: No new trades. 24-hour halt. Manual review required.
```
