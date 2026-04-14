---
workflow: "reward-optimization"
skill: "prediction-market-making"
produces: "Full Q chain calculation, spread/size tuning, reward vs adverse selection trade-off modeling, per-market tuning recommendations"
tokens: "~2,600"
---

# Reward Optimization

> The Polymarket reward program distributes $5M+/month to market makers. This workflow analyzes the quadratic scoring formula, calculates optimal spread/size combinations, models the trade-off between reward maximization and adverse selection exposure, and outputs specific tuning recommendations per market. The goal: capture the maximum share of the reward pool while staying above the adverse selection break-even line.

---

## Inputs Required

| Input | Required | Default |
|-------|----------|---------|
| Market name + condition/token IDs | Yes | — |
| Current orderbook snapshot (bids + asks with sizes) | Yes | — |
| Reward parameters: v (max spread), b (in-game multiplier) | Yes | v=10c, b=1.0 |
| Your available capital for this market | Yes | — |
| Current inventory position (% Yes vs % No) | Yes | 50/50 |
| Adverse selection history (recent fills during events) | No | estimated |
| Number of competing market makers | Yes | estimated from book |

---

## Step 1: The Q Calculation Chain

This is the complete scoring pipeline from raw quotes to final reward share. Every number must be calculated, not estimated.

### Q_one and Q_two (Per-Side Scores)

For each side of your two-sided quote:

```
Q_one = S(v, s_bid) = ((v - s_bid) / v)^2 * b_bid
Q_two = S(v, s_ask) = ((v - s_ask) / v)^2 * b_ask

where:
  v = max spread from midpoint (market parameter, typically 10 cents)
  s_bid = distance from midpoint to your bid
  s_ask = distance from midpoint to your ask
  b_bid = your bid size in USDC
  b_ask = your ask size in USDC
```

**Worked example** (midpoint 0.55, v = 10c):
- Your bid at 0.53 (s = 2c), size $5,000: Q_one = ((10-2)/10)^2 * 5000 = 0.64 * 5000 = 3,200
- Your ask at 0.57 (s = 2c), size $5,000: Q_two = ((10-2)/10)^2 * 5000 = 0.64 * 5000 = 3,200

### Q_min (Two-Sided Scoring)

**For midpoints between 0.10 and 0.90** (standard markets):
```
Q_min = max(min(Q_one, Q_two), max(Q_one/c, Q_two/c))
where c = 3.0
```

This formula has two components:
1. `min(Q_one, Q_two)` — rewards balanced two-sided quoting (uses the weaker side)
2. `max(Q_one/c, Q_two/c)` — safety net for single-sided quoters (divides by 3)
3. The outer `max()` takes the better of the two approaches

For balanced quotes: `min(3200, 3200) = 3200`. Safety net: `max(3200/3, 3200/3) = 1067`. Final: `max(3200, 1067) = 3200`. Full reward for balanced two-sided.

For single-sided (ask only, no bid): `min(0, 3200) = 0`. Safety net: `max(0, 3200/3) = 1067`. Final: `max(0, 1067) = 1067`. Penalized to 1/3.

**For extreme midpoints (<0.10 or >0.90)**:
```
Q_min = min(Q_one, Q_two)
```
No c=3.0 safety net. If either side is weak, your entire score collapses. This makes markets near resolution reward-hostile.

### Q_normal (Normalized Against Competition)

```
Q_normal = your_Q_min / sum(all_Q_mins_in_market)
```

This is your share of the reward pool for this market in this sampling minute.

**Competition modeling** — calculate each competitor's Q_min:
```
For each competitor (identifiable by resting order clusters on the book):
  Estimate their spread from midpoint
  Estimate their resting size
  Calculate their S(v,s) for each side
  Calculate their Q_min using the same formula
```

### Q_epoch (Time-Weighted Accumulation)

```
Q_epoch = sum(Q_normal for each of 10,080 one-minute samples in weekly epoch)
```

Every minute your quotes are resting on the book, a sample is taken. Minutes where your orders are cancelled (heartbeat failure, score event withdrawal, stop-loss sleep) score ZERO. This is why uptime matters as much as spread quality.

### Q_final (Epoch-Level Share)

```
Q_final = your_Q_epoch / sum(all_makers_Q_epochs)
```

Your share of the weekly reward distribution. This determines your actual payout.

**Expected payout**:
```
weekly_payout = weekly_reward_pool * Q_final
daily_payout = weekly_payout / 7   (distributed daily at midnight UTC)
```

---

## Step 2: Spread Sensitivity Analysis

Model your reward score as a function of spread width to find the optimal point.

**Generate the reward curve**:

| Your Spread (s) | S(v,s) score | vs 2c spread | vs 5c spread |
|-----------------|-------------|-------------|-------------|
| 1.0c | ((10-1)/10)^2 = 0.81 | +26.6% | +224% |
| 1.5c | ((10-1.5)/10)^2 = 0.7225 | +12.9% | +189% |
| 2.0c | ((10-2)/10)^2 = 0.64 | baseline | +156% |
| 2.5c | ((10-2.5)/10)^2 = 0.5625 | -12.1% | +125% |
| 3.0c | ((10-3)/10)^2 = 0.49 | -23.4% | +96% |
| 3.5c | ((10-3.5)/10)^2 = 0.4225 | -34.0% | +69% |
| 4.0c | ((10-4)/10)^2 = 0.36 | -43.8% | +44% |
| 5.0c | ((10-5)/10)^2 = 0.25 | -60.9% | baseline |

**Key insight**: The curve is CONVEX. Each additional cent of tightening yields MORE marginal reward than the last. Tightening from 5c to 4c gains 0.11 score. Tightening from 2c to 1c gains 0.17 score. This creates an arms race where the tightest quoter captures disproportionate share.

**Competition-Adjusted Reward**:
For your spread s and N competitors with spreads s_1 through s_N:
```
your_reward_share(s) = S(v,s) / (S(v,s) + sum(S(v, s_i) for i in 1..N))
```

Plot this for each candidate spread. The optimal spread is where marginal reward from tightening exceeds marginal adverse selection cost from tightening.

---

## Step 3: Size Optimization

Size scales the score linearly: doubling size doubles S(v,s). But doubling size also doubles adverse selection exposure.

**Size vs Spread Trade-Off**:
```
Option A: $10,000 at 2c spread -> S = 0.64 * 10000 = 6,400
Option B: $20,000 at 3c spread -> S = 0.49 * 20000 = 9,800
Option C: $10,000 at 1c spread -> S = 0.81 * 10000 = 8,100
```

Option B scores highest but requires 2x capital and 2x adverse selection exposure. Option C scores second but has the tightest spread (highest adverse selection per fill). Option A is the conservative choice.

**Capital Efficiency Metric**:
```
score_per_dollar = S(v,s) / capital_deployed
  Option A: 6400/10000 = 0.64 per dollar
  Option B: 9800/20000 = 0.49 per dollar
  Option C: 8100/10000 = 0.81 per dollar
```

Tighter spreads are more capital-efficient. But capital efficiency must be balanced against absolute score (which determines reward share in competition).

**Size Formula Capital Lock** (critical constraint):
```
maxOrderSize = balance - sum(openOrderSize - filledAmount)
```
Every open order locks capital. With 20 orders across 5 markets, significant capital is locked. Size optimization must account for portfolio-level capital allocation, not just per-market optimization.

---

## Step 4: Adverse Selection Break-Even Analysis

The central question: at what spread does reward income equal adverse selection cost?

**Adverse Selection Cost Model**:
```
AS_cost(s) = events_per_day * fill_probability(s) * avg_loss_per_fill(s) * avg_size_filled

where:
  fill_probability(s) = f(spread width, event magnitude, cancellation speed)
    Wider spread -> lower fill probability (informed trader needs bigger move to profit)
    Faster cancellation -> lower fill probability (less time exposed)
    
  avg_loss_per_fill(s) = avg_event_move - s
    If event moves price 10c and your spread is 3c, loss per filled contract = 7c
    If spread is 8c, loss = 2c (but fill is also less likely)
```

**Break-Even Spread**:
```
At break-even: reward_income(s) = adverse_selection_cost(s) + gas_cost

reward_income(s) = daily_pool * (S(v,s) / total_market_S)
AS_cost(s) = events * P(fill|s) * (avg_move - s) * avg_size
gas_cost = $0.02 * daily_orders
```

Solve for s. This is the MINIMUM spread that generates net positive daily income. Any tighter and you lose money despite higher rewards.

**Per-Market Type Break-Even Estimates** (with 5-second cancellation speed):

| Market Type | Avg Event Move | Events/Day | Est. Break-Even Spread |
|------------|---------------|------------|----------------------|
| NBA | 5-8c | 20-25 | 2.5-3.5c |
| EPL | 10-20c | 3-5 | 2.0-3.0c |
| Champions League | 10-20c | 3-5 | 1.5-2.5c |
| CS2 | 1-3c | 15-20 | 2.0-2.5c |
| IPL | 3-8c | 8-12 | 2.0-3.0c |
| UFC | 15-40c | 2-4 | 3.0-4.0c |

The break-even varies by your cancellation speed. Sub-second cancellation shifts the break-even 0.5-1c tighter.

---

## Step 5: Two-Sided Balance Optimization

The Q_min formula penalizes imbalance. Optimizing the RATIO of bid-to-ask is as important as optimizing spread width.

**Balance Score Impact**:
```
Perfectly balanced (Q_one = Q_two = 3200):
  Q_min = max(min(3200, 3200), max(3200/3, 3200/3)) = 3200

Moderately imbalanced (Q_one = 4000, Q_two = 2000):
  Q_min = max(min(4000, 2000), max(4000/3, 2000/3))
        = max(2000, max(1333, 667))
        = max(2000, 1333) = 2000
  Lost: 1200 score points (37.5% reduction from the stronger side)

Severely imbalanced (Q_one = 5000, Q_two = 500):
  Q_min = max(min(5000, 500), max(5000/3, 500/3))
        = max(500, max(1667, 167))
        = max(500, 1667) = 1667
  The c=3.0 safety net kicks in, but you're still at 1667 vs potential 3200+ balanced
```

**Optimal balance strategy**: Keep spreads equal on both sides. When inventory forces asymmetry, prioritize:
1. Keep the weaker side's Q as high as possible (it determines Q_min)
2. Accept slightly lower total score for better balance
3. Use the geometric mean metric: `gm = (Q_one * Q_two)^0.5` — maximize this, not Q_one + Q_two

---

## Step 6: Uptime Optimization

Reward scoring samples every minute (10,080 per weekly epoch). Every minute off-book = zero score.

**Uptime Budget**:
| Event | Duration | Frequency | Weekly Minutes Lost |
|-------|----------|-----------|-------------------|
| Score event withdrawal | 5-60 seconds | 20-30/week | 10-30 min |
| GTD refresh cycle gap | 2-3 seconds | 288/day = 2,016/week | 67-100 min |
| Heartbeat failure | 15 seconds + recovery | 0-2/week | 0-5 min |
| Tuesday restart | 90 seconds | 1/week | 1.5 min |
| Stop-loss sleep period | 1-6 hours | 0-3/week | 0-1,080 min |
| Infrastructure downtime | varies | varies | varies |

**Target**: 95%+ uptime = 9,576 of 10,080 minutes. The poly-maker bot's stop-loss sleep periods were the primary uptime killer — accumulating enough sleep hours to destroy reward viability.

**GTD Cycle Optimization**:
The gap between GTD expiration and fresh quote placement costs scoring minutes. Minimize by:
1. Pre-calculate next quotes before cancelling current ones
2. Use batch POST /orders (15/request) to place all new quotes in one API call
3. Target < 3 seconds between cancel and fresh quotes

**Smart Cancellation for Uptime**:
The poly-maker threshold (price_diff > 0.005 OR size_diff > 10%) preserves uptime by NOT cancelling orders that don't need updating. An order that stays resting accumulates reward scores continuously. Cancel-and-replace creates a gap.

---

## Step 7: Output Tuning Recommendations

For each market being quoted, output:

```
REWARD OPTIMIZATION: [Market Name]
===================================

CURRENT STATE:
  Midpoint: $0.XX
  Your spread: X.Xc bid / X.Xc ask
  Your size: $X,XXX bid / $X,XXX ask
  Inventory: XX% Yes / XX% No
  Competing makers: N (spreads: Xc, Xc, Xc, ...)

Q CHAIN CALCULATION:
  Q_one (bid): S = ((v-s)/v)^2 * b = X.XX * $X,XXX = X,XXX
  Q_two (ask): S = ((v-s)/v)^2 * b = X.XX * $X,XXX = X,XXX
  Q_min: max(min(X,XXX, X,XXX), max(X,XXX/3, X,XXX/3)) = X,XXX
  Q_normal: X,XXX / (X,XXX + sum_competitors) = XX.X%
  Expected daily reward: $X,XXX * XX.X% = $XXX

OPTIMIZATION ANALYSIS:
  Spread sensitivity:
    If tighten 0.5c: reward +$XX/day, AS risk +$XX/day, net +/-$XX
    If tighten 1.0c: reward +$XX/day, AS risk +$XX/day, net +/-$XX
    If widen 0.5c:   reward -$XX/day, AS risk -$XX/day, net +/-$XX
    If widen 1.0c:   reward -$XX/day, AS risk -$XX/day, net +/-$XX
    
  Recommended spread: X.Xc [tighter/wider/maintain]
  Reason: [marginal reward vs marginal AS at this point]

  Size sensitivity:
    If increase 25%: reward +$XX/day, AS risk +$XX/day, net +/-$XX
    If decrease 25%: reward -$XX/day, AS risk -$XX/day, net +/-$XX
    
  Recommended size: $X,XXX [increase/decrease/maintain]
  Reason: [capital efficiency vs absolute score competition]

  Balance analysis:
    Current Q_one/Q_two ratio: X.XX
    GM score: (Q_one * Q_two)^0.5 = X,XXX
    If perfectly balanced: Q_min would be X,XXX (+XX%)
    Action: [rebalance bid/ask sizes / adjust asymmetric spread]

UPTIME ANALYSIS:
  Estimated weekly uptime: X,XXX / 10,080 minutes (XX.X%)
  Score events causing withdrawal: ~X/week, ~X min lost
  GTD cycle gaps: ~X min/week
  Stop-loss sleep risk: [low/medium/high]
  
  Uptime improvement: [reduce GTD gap / faster score-event recovery / ...]

PROJECTED DAILY P&L (after optimization):
  Reward income: $XXX (XX.X% Q_final share)
  Spread capture: $XX (~X fills/day * Xc spread)
  Maker rebates: $X
  Adverse selection: -$XX (~X events * $X avg loss)
  Gas: -$X.XX ($0.02 * X orders)
  NET: $XXX/day

TUNING ACTIONS:
  1. [Specific action — e.g., "Tighten spread from 3c to 2.5c"]
  2. [Specific action — e.g., "Increase ask size by 15% to improve balance"]
  3. [Specific action — e.g., "Reduce GTD cycle from 5min to 3min for this high-reward market"]
  4. [Specific action — e.g., "Move $2,000 capital from [low-reward market] to this market"]
```

---

## Optimization Decision Framework

```
Is current spread at break-even or worse?
  YES --> Widen until net daily P&L is positive, then optimize from there
  NO  --> Continue

Is Q_normal share < 10%?
  YES --> Either tighten spread (if AS allows) or increase size (if capital allows)
          If neither: this market may not be worth quoting
  NO  --> Continue

Is balance ratio (Q_one/Q_two) > 1.5?
  YES --> Rebalance: adjust sizes to equalize Q_one and Q_two
  NO  --> Continue

Is uptime < 90%?
  YES --> Fix infrastructure first (heartbeat, GTD gaps, stop-loss frequency)
          Uptime gains are MORE valuable than spread optimization at <90%
  NO  --> Continue

Is there a higher reward-per-dollar market available?
  YES --> Consider rotating capital to higher-efficiency market
  NO  --> Fine-tune current spread/size within current market
```

---

## Key Formulas Reference

```
Reward Score:        S(v,s) = ((v-s)/v)^2 * b
Q_min (standard):    max(min(Q_one, Q_two), max(Q_one/3, Q_two/3))
Q_min (extreme):     min(Q_one, Q_two)
Q_normal:            your_Q_min / sum(all_Q_mins)
Q_epoch:             sum(Q_normal per minute over 10,080 weekly samples)
Q_final:             your_Q_epoch / sum(all_Q_epochs)
Expected weekly:     weekly_pool * Q_final
Geometric mean:      (Q_one * Q_two) ** 0.5
Score per dollar:    S(v,s) / capital_deployed
Break-even:          reward(s) = AS_cost(s) + gas
AS cost:             events * P(fill|s) * (avg_move - s) * avg_size
Fee (takers only):   C * feeRate * p * (1-p)
Max order size:      balance - sum(openOrderSize - filledAmount)
Drawdown:            (peak_pnl - total_pnl) / peak_pnl
```
