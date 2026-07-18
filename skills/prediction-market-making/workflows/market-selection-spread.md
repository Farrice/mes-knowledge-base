---
workflow: "market-selection-spread"
skill: "prediction-market-making"
produces: "Market ranking by reward efficiency + optimal spread parameters + deployment configuration"
tokens: "~2,500"
---

# Market Selection & Spread Design

> Scan available Polymarket markets, calculate expected reward income per market, rank by reward pool / competition ratio, design optimal spread width, and output a complete deployment configuration. The goal is to answer: "Which markets should I quote, at what spread, with how much capital?"

---

## Inputs Required

Before starting, collect from the user:

| Input | Required | Default |
|-------|----------|---------|
| Available capital (USDC.e) | Yes | — |
| Risk tolerance (conservative / balanced / aggressive) | Yes | balanced |
| Market focus (sports only / all / specific leagues) | No | sports only |
| Current date + upcoming event schedule | Yes | — |
| Number of markets to quote simultaneously | No | 5 |
| Existing infrastructure status (WebSocket live? heartbeat stable?) | Yes | — |

---

## Step 1: Enumerate Reward-Eligible Markets

For each active market with a reward pool, identify:

**Market Identity**
- Event name and type (NBA, EPL, CL, UFC, CS2, IPL, MLB, NHL)
- Condition ID and token IDs (Yes + No)
- Event start time and estimated duration (pre-game + in-game)

**Reward Data** (April 2026 reference pools):
| Sport | Pool/Game | Typical Duration | Daily Pool Estimate |
|-------|-----------|-----------------|-------------------|
| Champions League QF | $24,000 | 3 days | $8,000 |
| EPL | $10,000 | 2 days | $5,000 |
| NBA | $7,700 | 1.5 days | $5,133 |
| CS2 A-Tier | $5,500 | 1 day | $5,500 |
| IPL Cricket | $4,500 | 1 day | $4,500 |
| UFC Main Card | $4,250 | 1 day | $4,250 |
| MLB | $1,650 | 1 day | $1,650 |
| NHL | $1,500 | 1 day | $1,500 |

**Market Health Checks** — reject if ANY fail:
- [ ] Midpoint between 0.10 and 0.90 (extreme midpoints = strict min Q_min, reward-hostile)
- [ ] 24h volume > $10,000 (illiquid = thin books, high adverse selection)
- [ ] Not approaching resolution (midpoint not >0.85 or <0.15)
- [ ] Not on known manipulation list
- [ ] Reward pool > $3,000/game (below this, infrastructure cost exceeds reward income)

---

## Step 2: Assess Competitive Landscape

For each market passing Step 1:

**Orderbook Analysis** (fetch via `GET /book?token_id=X`):
- Count resting order clusters (each cluster = one market maker)
- Estimate each competitor's spread (distance from midpoint to best bid/ask)
- Estimate each competitor's resting size
- Calculate each competitor's approximate score: `S = ((v - s_competitor) / v)^2 * size`

**Competition Classification**:
| Competing Makers | Classification | Expected Q Share |
|-----------------|---------------|-----------------|
| 1-3 | Low competition | 25-40% achievable |
| 4-7 | Moderate competition | 15-25% achievable |
| 8-12 | High competition | 8-15% achievable |
| 13+ | Saturated | <8% — consider skipping |

**Volatility Assessment** (poly-maker method):
- Calculate annualized volatility across 8 windows: 1h, 3h, 6h, 12h, 24h, 7d, 14d, 30d
- Compute `volatility_sum = 24h + 7d + 14d`
- If `volatility_sum >= 20`: EXCLUDE market entirely
- Record 3-hour volatility as real-time trade gate value

---

## Step 3: Calculate Expected Daily Reward Per Market

For each surviving market:

**Your Proposed Quotes**:
```
bid_price = midpoint - proposed_spread
ask_price = midpoint + proposed_spread
bid_size = capital_for_market / 2
ask_size = capital_for_market / 2
```

**Score Calculation** (quadratic formula):
```
Your S(v,s) = ((v - your_spread) / v)^2 * your_size

For two-sided (midpoint 0.10-0.90):
  Q_min = max(min(S_bid, S_ask), max(S_bid/3.0, S_ask/3.0))

For extreme midpoints (<0.10 or >0.90):
  Q_min = min(S_bid, S_ask)   [strict — no c=3.0 safety net]
```

**Q_normal (your share)**:
```
Q_normal = your_Q_min / (your_Q_min + sum(all_competitor_Q_mins))
```

**Expected Daily Reward**:
```
expected_daily = daily_reward_pool * Q_normal
```

**Geometric Mean Cross-Check** (poly-maker method):
```
gm_reward_per_100 = (bid_reward_per_100 * ask_reward_per_100) ** 0.5
```
If `gm_reward_per_100 < 0.75`: market is not worth quoting at this capital level.

---

## Step 4: Calculate Reward Per Dollar of Capital

```
capital_required = (bid_size + ask_size) * (1 + buffer_for_rebalancing)
  where buffer_for_rebalancing = 0.2 (20% overhead for inventory management)

reward_per_dollar = expected_daily / capital_required
```

**Rank all markets by reward_per_dollar descending.**

Apply portfolio-level filters:
- No single market > 30% of total capital (concentration risk)
- Skip markets where capital requirement exceeds reward justification
- Flag markets with high score-event frequency (NBA ~20/game, EPL ~3-5/game)
- Flag approaching resolution (midpoint trending past 0.85 or 0.15)

---

## Step 5: Design Optimal Spread Per Market

For each selected market, determine spread width:

**Adverse Selection Risk by Market Type**:
| Market Type | Score Events/Game | Avg Price Move | Risk Level | Base Spread |
|------------|-------------------|----------------|------------|-------------|
| NBA/NFL | 15-25 | 3-8 cents | High | 2.5-3.5 cents |
| EPL/CL | 3-5 | 10-20 cents | Medium-High | 2.0-3.0 cents |
| UFC | 1-3 | 15-40 cents | High per event | 3.0-4.0 cents |
| CS2/Esports | 10-20 (rounds) | 1-3 cents | Low per event | 2.0-3.0 cents |
| IPL Cricket | 5-10 (wickets) | 3-8 cents | Medium | 2.5-3.0 cents |
| MLB | 20-30 | 1-3 cents | Medium | 2.5-3.5 cents |

**Spread Optimization Model**:
```
For each candidate spread s from 1 to 5 cents (0.5c increments):

  reward_score(s) = ((v - s) / v)^2
  
  adverse_selection_cost(s) = events_per_day * P(informed_fill_at_s) * avg_loss_per_fill(s)
    where P(informed_fill) decreases as spread widens
    and avg_loss = typical_move - s (when move > s)
  
  spread_capture(s) = expected_fills_per_day * s
  
  net_value(s) = expected_reward(s) + spread_capture(s) - adverse_selection_cost(s) - gas_cost
    where gas_cost = $0.02 * estimated_daily_orders
```

Select the spread s that maximizes net_value(s).

**Inventory-Adjusted Spread** (initial deployment = symmetric):
```
Balanced inventory: symmetric (bid and ask equidistant from midpoint)
20% drift: widen overweight +0.5c, tighten underweight -0.5c
30% drift: cancel overweight side entirely
```

---

## Step 6: Build Deployment Configuration

For each selected market, output:

```
MARKET DEPLOYMENT CONFIG
========================

Market: [Event Name] — [Outcome]
Condition ID: [X]
Token IDs: Yes=[X], No=[X]
Midpoint: $0.XX

CAPITAL ALLOCATION:
  Total for market: $X,XXX (XX% of portfolio)
  Bid capital: $X,XXX
  Ask capital: $X,XXX
  Rebalance reserve: $X,XXX (20% of allocated)

SPREAD PARAMETERS:
  Base spread: X.X cents each side
  Score-event spread: XX cents (2x base) for 10s, decay to base over 60s
  Post-Only: REQUIRED (0% maker fee guarantee)
  Order type: GTD (expiration = now + 360 seconds)
  Smart cancel threshold: price_diff > 0.005 OR size_diff > 10%

REWARD PROJECTION:
  Your S(v,s): X.XX
  Estimated Q_normal share: XX.X%
  Expected daily reward: $X,XXX
  GM reward per $100: $X.XX

RISK PARAMETERS:
  max_position_per_market: $X,XXX (30% of allocation)
  Inventory drift widen trigger: 20%
  Inventory drift cancel trigger: 30%
  Slippage tolerance: 1.0%
  Price range: 0.10 - 0.90 only

ADVERSE SELECTION DEFENSE:
  Score event source: [Sports WS / News API]
  Score events expected: ~X per game
  Auto-cancel method: Batch DELETE /orders (NOT cancel-all — 4x faster)
  Re-quote delay: X seconds at Xx spread
  Extreme midpoint exit: >0.90 or <0.10

ORDER MANAGEMENT:
  Batch mode: POST /orders (15/request, 15,000 effective/10s)
  GTD refresh cycle: 5 min normal, 60s high-volatility
  Tuesday restart: Cancel 6:58 AM ET, probe from 7:02 AM ET
```

---

## Step 7: Output Portfolio Summary

```
PORTFOLIO MARKET MAKING PLAN
==============================
Capital: $XX,XXX  |  Risk: [level]  |  Markets: [N] active

RISK MANAGER CONFIGURATION:
  max_position_per_market: $XX,XXX
  max_global_exposure: $XX,XXX
  max_daily_loss: $X,XXX  [conservative 1% / balanced 2% / aggressive 3%]
  max_drawdown_pct: X%  [conservative 5% / balanced 10% / aggressive 15%]
  kill_switch_enabled: true
  auto_unwind_on_breach: false
  min_24h_volume: 10,000

MARKET ALLOCATION:
| Rank | Market | Capital | Spread | GTD | Inv Cap | Daily Reward | Risk |
|------|--------|---------|--------|-----|---------|-------------|------|
| 1 | [name] | $X (X%) | Xc | 5m | 30% | $X,XXX | Med |
| 2 | [name] | $X (X%) | Xc | 5m | 25% | $X,XXX | High |

RESERVE: $X,XXX (XX%) — opportunistic high-pool events (CL, UFC)
BUFFER: $X,XXX (XX%) — rebalancing + emergency margin

PROJECTED MONTHLY P&L:
  Conservative (15% Q share): $X,XXX/month (X.X%)
  Balanced (25% Q share): $X,XXX/month (X.X%)
  Optimistic (35% Q share): $X,XXX/month (X.X%)
  Gas: -$XX/month | Infrastructure: -$XXX/month

DEPLOYMENT SEQUENCE:
  Week 1: [market 1] — single market validation
  Week 2: Add [markets 2-3] — multi-market batch testing
  Week 3: Full deployment + first opportunistic event
  Week 4: Optimization cycle (spread tightening experiments)
```

---

## Worked Example: $50K Capital, Balanced Risk, Sports Only

| Rank | Market | Pool | Est. Daily | Capital | Reward/$1 | Risk | Action |
|------|--------|------|-----------|---------|-----------|------|--------|
| 1 | CL QF: Real Madrid v Arsenal | $24K | $8K | $15K | 0.53/day | Med | Deploy |
| 2 | NBA: Lakers v Celtics | $7.7K | $3.85K | $8K | 0.48/day | Med | Deploy |
| 3 | EPL: Man City v Liverpool | $10K | $5K | $12K | 0.42/day | Med | Deploy |
| 4 | CS2: NaVi v FaZe | $5.5K | $2.75K | $5K | 0.55/day | Low | Deploy |
| 5 | MLB: Yankees v Dodgers | $1.65K | $825 | $5K | 0.17/day | Low | Skip |

Total allocated: $40K/50K (80%). Reserve: $5K. Buffer: $5K.
Projected daily at 25% Q share: $2,940-$5,880. Monthly: $4,200-$9,500.

---

## Validation Checklist

Before deploying any market:

- [ ] Heartbeat stable 24+ hours continuously
- [ ] Two-sided quotes verified via GET /orders
- [ ] Post-Only confirmed (no maker fees on fills)
- [ ] GTD expiration cycling correctly at 5-min intervals
- [ ] Risk manager 8-check chain active and tested
- [ ] Score-event auto-cancel tested (batch DELETE, NOT cancel-all)
- [ ] Smart cancellation threshold: no requoting on immaterial ticks
- [ ] Price range 0.10-0.90 enforced
- [ ] Batch ordering via POST /orders (not individual POST /order)
- [ ] Tuesday restart handler tested against HTTP 425
- [ ] Position merging enabled for capital recovery
- [ ] Daily P&L logging + kill switch thresholds configured

---

## Key Formulas

```
Reward Score:      S(v,s) = ((v-s)/v)^2 * b
Two-sided Q_min:   max(min(Q_one, Q_two), max(Q_one/3, Q_two/3))  [0.10-0.90]
Extreme Q_min:     min(Q_one, Q_two)  [<0.10 or >0.90]
Q_normal:          your_Q_min / sum(all_Q_mins)
Expected daily:    daily_pool * Q_normal
Fee (takers):      C * feeRate * p * (1-p)    [makers = 0]
Max order size:    balance - sum(openOrderSize - filledAmount)
Geometric mean:    (bid_reward * ask_reward) ** 0.5
```

---

## Output Schema

A **Market Selection & Deployment Plan** with three parts:
1. **Market Deployment Config** (Step 6 template) per selected market — condition/token IDs, capital allocation, spread parameters, reward projection, risk parameters, adverse-selection defense, order management.
2. **Portfolio Summary** (Step 7 template) — risk-manager configuration, a ranked market allocation table (rank, market, capital, spread, GTD, inventory cap, daily reward, risk level), reserve/buffer split, and a 3-scenario projected monthly P&L (conservative/balanced/optimistic Q-share).
3. **Validation Checklist** (Step 5's 12 items) marked complete or explicitly flagged as outstanding before capital deploys.

## Quality Gate

1. **The Health-Check Test** — did every listed market pass all 5 Step-1 health checks (midpoint range, 24h volume, resolution distance, manipulation list, minimum pool) before appearing in the plan?
2. **The Competition Test** — is each market's competitor count classified (1-3 / 4-7 / 8-12 / 13+) with the matching expected-Q-share band from Step 2, not a guessed percentage?
3. **The Concentration Test** — does any single market exceed 30% of total capital? If so, the plan must be rejected and rebalanced before output.
4. **The Volatility-Gate Test** — is `volatility_sum` (24h+7d+14d) checked against the >=20 exclusion threshold for every candidate market before it reaches the deployment table?
5. **The Checklist-Complete Test** — are all 12 Validation Checklist items explicitly marked (not left as bare unchecked boxes)?
