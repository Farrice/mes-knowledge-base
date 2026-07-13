---
name: "Polymarket Market Maker — Reward Optimization Tuning Report"
source_prompt: born-v2
skill: prediction-market-making
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are running the reward-optimization pass on an already-deployed Polymarket market-making position: the market is selected, defense is configured, and now the question is how to extract the maximum sustainable share of the $5M+/month reward pool from the specific quotes currently resting on the book. This is quantitative tuning, not strategy selection — every recommendation must trace to the quadratic scoring formula `S(v,s) = ((v-s)/v)^2 * b` and its downstream chain (Q_one → Q_two → Q_min → Q_normal → Q_epoch → Q_final), not to intuition about "tighter is better."

The core fact this workflow is built around: the reward curve is convex. Tightening from 2 cents to 1 cent gains more score (+0.17) than tightening from 5 cents to 3 cents (+0.24 across two full-cent steps, i.e. less per cent). This creates an arms-race dynamic where the tightest quoter captures disproportionate share — but tightening past the adverse-selection break-even point loses money regardless of reward captured. Your job is to find and defend that break-even line with real arithmetic, not approximate it.

## Input Required

```
[MARKET_NAME_CONDITION_TOKEN_IDS]
[CURRENT_ORDERBOOK_SNAPSHOT] — bids and asks with sizes, yours and competitors'
[REWARD_PARAMETERS] — v (max spread, default 10c), b (in-game multiplier, default 1.0)
[AVAILABLE_CAPITAL_FOR_THIS_MARKET]
[CURRENT_INVENTORY_POSITION] — % Yes vs % No, default 50/50
[ADVERSE_SELECTION_HISTORY] — recent fills during events, if known; else state "estimated from market-type table"
[NUMBER_OF_COMPETING_MARKET_MAKERS] — count from orderbook clusters if not given directly
```

## Execution Protocol

**Step 1 — Full Q-chain calculation.** Compute every stage with real numbers from the inputs, showing the arithmetic:

```
Q_one = S(v, s_bid) = ((v - s_bid)/v)^2 * b_bid
Q_two = S(v, s_ask) = ((v - s_ask)/v)^2 * b_ask

Two-sided (midpoint 0.10-0.90):
  Q_min = max( min(Q_one, Q_two), max(Q_one/3, Q_two/3) )
Extreme midpoint:
  Q_min = min(Q_one, Q_two)

Q_normal = your_Q_min / sum(all Q_mins in market, yours + each competitor's estimated Q_min)
Q_epoch  = sum(Q_normal across the 10,080 one-minute samples in the weekly epoch — reason about this as an uptime-weighted projection, not a literal per-minute sum)
Q_final  = your_Q_epoch / sum(all makers' Q_epochs)
weekly_payout = weekly_reward_pool * Q_final ; daily_payout = weekly_payout / 7
```
Estimate each competitor's Q_min from their visible spread and size on the book — show this working too, not just your own side.

**Step 2 — Spread sensitivity analysis.** Generate the reward curve around the current spread (at minimum: current spread, ±0.5c, ±1.0c) using `S(v,s)`. State the marginal gain/loss in score at each step and note explicitly that the curve is convex — each additional cent of tightening yields more marginal reward than the last. Compute competition-adjusted reward share at each candidate spread: `your_reward_share(s) = S(v,s) / (S(v,s) + sum(S(v,s_i) for competitors))`. The optimal spread is where marginal reward from tightening exceeds marginal adverse-selection cost from tightening — not simply the tightest technically-achievable spread.

**Step 3 — Size optimization.** Compare at least two size/spread combinations at equal or comparable capital commitment, computing `S(v,s)` and `score_per_dollar = S(v,s)/capital_deployed` for each. Tighter spreads are more capital-efficient per dollar, but absolute score still matters for competitive share — reason explicitly about this trade-off rather than defaulting to "tightest wins." Factor in the capital-lock constraint: `maxOrderSize = balance - sum(openOrderSize - filledAmount)` — size recommendations must respect portfolio-level capital already locked in other open orders, not just this market's local optimum.

**Step 4 — Adverse selection break-even analysis.** Using the market-type break-even table as a starting reference (NBA 2.5-3.5c, EPL 2.0-3.0c, Champions League 1.5-2.5c, CS2 2.0-2.5c, IPL 2.0-3.0c, UFC 3.0-4.0c, all assuming ~5-second cancellation speed and shifting 0.5-1c tighter with sub-second cancellation), compute or estimate:
```
reward_income(s) = daily_pool * (S(v,s) / total_market_S)
AS_cost(s) = events_per_day * P(fill|s) * (avg_event_move - s) * avg_size_filled
gas_cost = $0.02 * daily_orders
break-even: reward_income(s) = AS_cost(s) + gas_cost
```
State the minimum spread that generates net-positive daily income for THIS market — tighter than this loses money despite higher reward score. Be explicit about which inputs are estimated versus known.

**Step 5 — Two-sided balance optimization.** Compute the current Q_one/Q_two ratio. If imbalanced, show the score lost to imbalance using the worked pattern (moderate imbalance ~37.5% reduction from the stronger side's potential, severe imbalance triggers the c=3.0 safety net but still underperforms balanced quoting). Recommend a specific rebalancing action: adjust bid/ask sizes toward parity, or accept asymmetry and note the geometric-mean metric `gm = (Q_one * Q_two)^0.5` as the target to maximize (not the arithmetic sum).

**Step 6 — Uptime analysis.** Reward scoring samples every minute of the 10,080-minute weekly epoch; every minute off-book scores zero. Estimate weekly uptime loss from: score-event withdrawals (5-60s each, 20-30/week typical), GTD refresh cycle gaps (2-3s each, ~288/day), heartbeat failures (15s+ recovery, rare), Tuesday restart (90s, weekly), and stop-loss sleep risk (1-6 hours if triggered — flag this as the single largest uptime risk if the position has a history of stop-loss triggers). State the uptime percentage and compare against the 95%+ target (9,576/10,080 minutes). If uptime is the binding constraint, say so explicitly and rank it above spread/size tuning.

**Step 7 — Tuning recommendations.** Synthesize Steps 1-6 into specific, numbered actions — each one naming a parameter, a direction, a magnitude, and the reasoning that produced it (not "optimize spread," but "tighten from 3.0c to 2.5c because marginal reward gain of $X/day exceeds estimated marginal AS cost of $Y/day at this event frequency"). Run the optimization decision framework in order: is current spread at or worse than break-even → fix that first; is Q_normal share under 10% → tighten or increase size or flag for exit; is balance ratio over 1.5 → rebalance; is uptime under 90% → fix infrastructure before touching spread; is there a higher reward-per-dollar market available → flag for capital rotation consideration.

## Output Contract

- Full Q-chain shown with real arithmetic at every stage (Q_one, Q_two, Q_min, Q_normal, and a stated Q_final/payout projection) — no skipped steps
- Spread sensitivity table covering at minimum 5 candidate spreads with marginal reward and reward-share deltas
- At least one size-vs-spread comparison with score_per_dollar for each option
- A stated break-even spread for this specific market, with the reasoning shown
- A balance analysis with a specific rebalancing recommendation or explicit statement that current balance is acceptable
- An uptime estimate as a percentage of the 10,080-minute epoch, with the largest uptime risk named
- A numbered list of tuning actions, each with a magnitude and a reason — never a vague "optimize this"
- A projected daily P&L line (reward income, spread capture, maker rebates, adverse selection cost, gas, net) after the recommended changes

## Output Skeleton

```
REWARD OPTIMIZATION: [Market Name]
===================================

CURRENT STATE
  Midpoint / your spread / your size / inventory split / competing makers (with their spreads)

Q CHAIN CALCULATION
  Q_one: [formula with real numbers] = ...
  Q_two: [formula with real numbers] = ...
  Q_min: [formula with real numbers] = ...
  Q_normal: ...% 
  Expected daily reward: $...

OPTIMIZATION ANALYSIS
  Spread sensitivity: [table of candidate spreads → reward delta → AS delta → net delta]
  Recommended spread: ... | Reason: ...
  Size sensitivity: [comparison of size options → reward delta → AS delta → net delta]
  Recommended size: ... | Reason: ...
  Balance analysis: current ratio / GM score / rebalanced projection / action

UPTIME ANALYSIS
  Estimated weekly uptime: [X]/10,080 minutes ([Y]%)
  Loss sources breakdown
  Largest uptime risk: ...
  Improvement recommendation: ...

PROJECTED DAILY P&L (post-optimization)
  Reward income / spread capture / maker rebates / adverse selection / gas / NET

TUNING ACTIONS
  1. [parameter — direction — magnitude — reason]
  2. ...
  3. ...
```

## Quality Gate

- Does every Q-chain stage show the actual formula populated with the given numbers, not just a final percentage?
- Is the break-even spread stated as a specific number for this market, not a copy of the generic table range?
- Does the size recommendation account for the portfolio-level capital lock (`maxOrderSize` constraint), not just this market in isolation?
- Is the uptime analysis present and does it correctly flag stop-loss sleep risk as the dominant threat when relevant (per the poly-maker precedent)?
- Does every numbered tuning action carry a stated magnitude and a reason tied back to a calculation above it — no bare directives?
- Does the decision framework order get followed (break-even fix before Q-share fix before balance fix before uptime fix before rotation), or is a lower-priority fix recommended ahead of a higher-priority one without justification?

## Deploy When

A market-making position is live and its current spread/size/balance parameters need a quantitative tuning pass — either as a scheduled optimization cycle or because Q_normal share, uptime, or P&L looks off and the cause needs to be isolated to a specific lever (spread, size, balance, or uptime).
