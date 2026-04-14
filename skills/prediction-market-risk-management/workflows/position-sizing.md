---
name: "Position Sizing Calculator"
skill: "prediction-market-risk-management"
produces: "Kelly-optimal position size with all risk limits, fee impact, and 8-check validation applied"
version: "1.0"
---

# Position Sizing Calculator

Calculate the exact position size for a proposed trade, applying Kelly criterion at quarter-strength with all risk limits enforced. This workflow takes a trade proposal and runs it through the complete validation chain from the extraction — the same architecture that separates the 7.6% profitable wallets from the 92.4% that lose money.

**Every trade runs through this. No exceptions. No overrides.**

---

## Inputs Required

Before calculating, gather these inputs. If any are missing, request them explicitly.

```
TRADE PROPOSAL:
- estimated_probability: Your model's probability estimate (0.0-1.0)
- market_price: Current contract price / ask on platform (0.0-1.0)
- direction: YES or NO
- market_id: Which market (for correlation and blacklist checking)
- market_category: crypto | sports | geopolitical (determines fee rate)
- strategy: Which strategy generated this signal (weather|ai_ensemble|market_making|arbitrage|cross_platform)
- market_volume_24h: 24-hour trading volume in dollars
- hours_to_resolution: Time until market resolves

PORTFOLIO STATE:
- bankroll: Total trading capital
- current_open_positions: List of (market_id, size, strategy, entry_price, current_price, hours_to_resolution)
- daily_pnl: Current session P&L
- peak_pnl: Peak P&L for drawdown calculation
- kill_switch_triggered: Boolean
- blacklisted_markets: List of market IDs
- whitelisted_markets: List (empty = all allowed)

RISK CONFIG (use defaults if not specified):
- kelly_fraction: 0.25
- max_bet: $20
- min_ev: 0.10
- max_price: 0.45
- min_volume: 500
- max_slippage: 0.03
- min_hours: 2.0
- max_hours: 72.0
- max_position_per_market: 10% of bankroll (or $200 for arb bot)
- max_global_exposure: 30% of bankroll (or $5,000 for arb bot)
- max_daily_loss: 5% of bankroll (or $500 for arb bot)
- max_drawdown_pct: 10%
- max_concurrent_positions: 15
- max_strategy_allocation: 40% of bankroll

FEE RATES (Polymarket):
- crypto: 0.072
- sports: 0.03
- geopolitical: 0 (exempt)
- cross_platform_additional: Kalshi ~1% + $0.04 gas round-trip
```

---

## Step 1: The 8-Check Validation Chain

Run checks sequentially. ANY failure = REJECT. Do not proceed to sizing on a rejected trade. This mirrors the `RiskManager.check_order()` architecture from polymarket-arbitrage.

### Check 1: Kill Switch Status
```
IF kill_switch_triggered == True:
    REJECT — "Kill switch active: {reason}. Manual reset required."
```
This is O(1) and catches the most critical state first.

### Check 2: Market Blacklist
```
IF market_id in blacklisted_markets:
    REJECT — "Market {market_id} is blacklisted."
```

### Check 3: Whitelist (if active)
```
IF whitelisted_markets is not empty AND market_id not in whitelisted_markets:
    REJECT — "Market {market_id} not in whitelist."
```

### Check 4: Volume Minimum
```
IF market_volume_24h < min_volume (500):
    REJECT — "24h volume ${volume} below minimum ${min_volume}. Illiquid — exit will be worse than entry."
```

### Check 5: Per-Market Exposure
```
existing_market_exposure = sum of positions in this market_id
projected = existing_market_exposure + proposed_size
IF projected > max_position_per_market:
    REJECT — "Would exceed per-market limit. Current: ${existing}, Proposed: ${proposed_size}, Max: ${max_position_per_market}."
```

### Check 6: Global Exposure
```
current_global = sum of ALL open positions
projected_global = current_global + proposed_size
IF projected_global > max_global_exposure:
    REJECT — "Would exceed global exposure. Current: ${current_global}, Max: ${max_global_exposure}."
```

### Check 7: Daily Loss Limit
```
IF daily_pnl <= -max_daily_loss:
    REJECT + TRIGGER KILL SWITCH — "Daily loss ${daily_pnl} exceeds limit ${max_daily_loss}. KILL SWITCH TRIGGERED."
```
This check CHANGES STATE. If it fires, the kill switch is permanently set.

### Check 8: Drawdown Limit
```
current_drawdown = (peak_pnl - current_pnl) / peak_pnl * 100
IF current_drawdown >= max_drawdown_pct:
    REJECT + TRIGGER KILL SWITCH — "Drawdown {current_drawdown}% exceeds limit {max_drawdown_pct}%. KILL SWITCH TRIGGERED."
```

Report each check: PASS / REJECT with actual values.

---

## Step 2: Pre-Trade Filters

These are strategy-level filters beyond the 8-check chain. Any failure = REJECT.

### Price Filter
```
IF market_price > max_price (0.45):
    REJECT — "Price ${market_price} exceeds max ${max_price}. Contracts above 45c have asymmetric downside."
```
Rationale: At $0.80, you pay 80 cents to win 20 cents profit. One loss erases 4+ wins.

### Time Filter
```
IF hours_to_resolution < min_hours (2.0):
    REJECT — "Only {hours}h to resolution. Market has priced in current observations."
IF hours_to_resolution > max_hours (72.0):
    REJECT — "{hours}h to resolution exceeds max. Forecast skill degrades beyond 72h."
```

### Position Count Filter
```
IF len(current_open_positions) >= max_concurrent_positions (15):
    REJECT — "At position capacity ({count}/{max}). Close positions before new trades."
```

### Slippage Filter
```
IF current_spread > max_slippage (0.03):
    REJECT — "Spread ${spread} exceeds slippage tolerance ${max_slippage}."
```

---

## Step 3: Calculate Expected Value and Fee Impact

### Raw Edge
```
edge = estimated_probability - market_price
IF edge <= 0: REJECT — "No positive expected value."
IF edge < min_ev (0.10): REJECT — "Edge {edge} below minimum {min_ev}. Signal-to-noise too low."
```

### Fee Calculation
Using Polymarket formula: `fee = shares * feeRate * price * (1 - price)`

```
feeRate = {crypto: 0.072, sports: 0.03, geopolitical: 0}[market_category]
fee_per_share = feeRate * market_price * (1 - market_price)
```

Note: Fee peaks at 50% probability. A crypto trade at $0.50: fee = 0.072 * 0.50 * 0.50 = 0.018 per share (1.8%).

For cross-platform arbitrage, add:
```
total_fees = buy_platform_fee + sell_platform_fee + (gas_cost * 2)
```
With Polymarket taker at 1.5% + Kalshi at ~1% + $0.04 gas round-trip, minimum gross edge ~5.5%.

### Net Expected Value
```
estimated_slippage = 0.02  # 2 cents conservative estimate (arb bot enforces 2c max)
net_ev_per_share = edge - fee_per_share - estimated_slippage
IF net_ev_per_share <= 0: REJECT — "Edge evaporates after fees (${fee_per_share}) + slippage (${estimated_slippage}). Net EV: ${net_ev_per_share}."
```

---

## Step 4: Calculate Kelly-Optimal Size

```
# Odds ratio for binary prediction market
b = (1 / market_price) - 1

# Full Kelly
f_star = (estimated_probability * b - (1 - estimated_probability)) / b

# Quarter-Kelly
f = kelly_fraction * max(0, f_star)

# Raw position size
raw_position_size = f * bankroll
```

If `f_star <= 0`: REJECT — "Kelly says don't bet. Odds structure doesn't justify position at this price."

Report:
```
Full Kelly: {f_star:.4f} ({f_star * 100:.1f}% of bankroll = ${f_star * bankroll:.2f})
Quarter-Kelly: {f:.4f} ({f * 100:.1f}% of bankroll = ${f * bankroll:.2f})
Raw position size: ${raw_position_size:.2f}
```

### Worked Example
p=0.80, price=$0.10, bankroll=$10,000, sports market
- b = (1/0.10) - 1 = 9
- f* = (0.80 * 9 - 0.20) / 9 = 7.0 / 9 = 0.778
- f = 0.25 * 0.778 = 0.194 (19.4% = $1,944)
- But MAX_BET = $20, so position = $20
- Shares = 200 at $0.10
- Fee = 200 * 0.03 * 0.10 * 0.90 = $0.54
- Expected profit = 200 * $1.00 * 0.80 - $20 - $0.54 = $139.46

---

## Step 5: Apply Position Caps (Sequential — Size Can Only Decrease)

```
# Layer 1: Individual position cap
capped = min(raw_position_size, max_bet)

# Layer 2: Per-market cap (10% of bankroll)
capped = min(capped, max_position_per_market - existing_market_exposure)

# Layer 3: Strategy allocation cap (40% of bankroll)
current_strategy_exposure = sum(positions where strategy matches)
remaining_strategy = (bankroll * max_strategy_allocation) - current_strategy_exposure
IF remaining_strategy <= 0: REJECT — "Strategy at allocation limit."
capped = min(capped, remaining_strategy)

# Layer 4: Global exposure cap
remaining_global = max_global_exposure - current_global_exposure
IF remaining_global <= 0: REJECT — "Portfolio at exposure limit."
capped = min(capped, remaining_global)

# Layer 5: Minimum viable size
IF capped < 0.50: REJECT — "Position size ${capped} below $0.50 minimum. Not worth execution costs."
```

Report each layer:
```
Raw Kelly size:        ${raw_position_size}
After max_bet cap:     ${after_max_bet}       [binding: yes/no]
After per-market cap:  ${after_market}         [binding: yes/no]
After strategy cap:    ${after_strategy}       [binding: yes/no]
After global cap:      ${final_size}           [binding: yes/no]
BINDING CONSTRAINT:    {which cap was tightest}
```

---

## Step 6: Correlation Check

Review all current open positions for correlation with this trade.

**Same-category correlation**: If 2+ existing positions in same market category (e.g., weather in different cities) and this adds a 3rd+, flag. A jet stream shift affects all simultaneously.

**Same-resolution-window**: If 3+ positions resolve in same 24-hour window, flag. A single bad day hits all of them.

**Directional correlation**: If proposed trade and existing position would both lose on same underlying event, flag explicitly. Five "uncorrelated" $20 positions that all benefit from the same weather pattern = a single $100 directional bet in disguise.

If correlated aggregate exposure > 30% of bankroll: reduce position size by 30% and flag for rebalancing.

---

## Step 7: Generate Output

### If APPROVED:
```
POSITION SIZING RESULT: APPROVED
==========================================
Market:     {market_id}
Direction:  {YES/NO}
Strategy:   {strategy}
Category:   {market_category}

POSITION SIZE: ${final_size}
Entry Price:   ${market_price}
Shares:        {final_size / market_price}

EDGE ANALYSIS:
  Estimated probability: {estimated_probability}
  Market price:          {market_price}
  Raw edge:              {edge * 100}%
  Fee per share:         ${fee_per_share}
  Estimated slippage:    ${estimated_slippage}
  Net edge:              {net_ev_per_share * 100}%
  Net expected profit:   ${shares * net_ev_per_share}

RISK METRICS:
  Kelly fraction used:    {f} (quarter of {f_star})
  Binding constraint:     {which_cap}
  Portfolio exposure:     {new_total / bankroll * 100}% of max {max_global_exposure / bankroll * 100}%
  Strategy allocation:    {new_strategy / bankroll * 100}% of max {max_strategy_allocation * 100}%
  Per-market utilization: {new_market / max_position_per_market * 100}%
  Kill switch distance:   ${max_daily_loss - abs(daily_pnl)} daily / {max_drawdown_pct - current_drawdown}% drawdown
  Concurrent positions:   {count + 1} / {max_concurrent}
  Correlation flags:      {none / details}

EXECUTION PARAMETERS:
  Slippage budget:  ${final_size * max_slippage} (cancel if fill deviates more)
  Order timeout:    60 seconds (cancel unfilled orders)

EXIT PLAN (set at entry):
  Stop-loss:        ${market_price * 0.80} (-20% from entry)
  Trailing stop:    Activates at ${market_price * 1.20} (+20%), trails to breakeven
  Take-profit:      {"$0.75" if hours > 48 else "$0.85" if hours > 24 else "Hold to resolution"}
  Resolution:       {hours_to_resolution}h

CONFIDENCE: {HIGH if edge > 3x min_ev | MEDIUM if 2-3x | STANDARD if 1-2x}
```

### If REJECTED:
```
POSITION SIZING RESULT: REJECTED
==========================================
Market:           {market_id}
Failed Check:     {check_name} (Check #{number} of 8-chain + pre-trade filters)
Rejection Reason: {specific reason}
Actual Value:     {value}
Threshold:        {threshold}
Recommendation:   {wait for better price / skip market / reduce positions first / diagnose kill switch}
```

---

## Practitioner Notes

- **Never override a rejection.** The rules exist because they were validated across WeatherBot, PolySwarm, the arbitrage bot, and the poly-maker. Overriding "just this once" is Step 5 of the 92.4% failure cascade.

- **The binding constraint tells you something.** If max_bet is always binding, your bankroll supports larger positions than the cap allows. If global exposure is always binding, you have too many concurrent positions. Track which constraint binds most often.

- **Recalculate after every fill.** Portfolio state changes with each trade. A position approved 5 minutes ago may be rejected now if another trade filled.

- **Edge decay matters.** If more than 30 minutes pass between calculation and execution, recalculate. Market prices move.

- **Fee awareness is survival.** A strategy with 3% theoretical edge and 2.5% in fees has 0.5% actual edge. One bad trade erases 5 good ones. Always calculate net-of-fees.

- **The exit plan is set at ENTRY, not later.** Stop-loss, trailing stop, and take-profit thresholds are defined before the order is placed. Deciding exits after you're in the position introduces emotional interference — the exact failure mode that makes humans 18% worse than bots.

- **Quarter-Kelly is the default, not a suggestion.** The only valid reasons to change: (a) 200+ validated trades proving calibration accuracy, or (b) micro-live phase using 0.10-0.15 for extra caution. NEVER exceed 0.33 regardless of performance.

- **For cross-platform arbitrage**: Use fixed sizing ($5 default, $10 max) instead of Kelly. Size limited by `min(buy_liquidity, sell_liquidity, $100)`. The edge is structural (price discrepancy), not probabilistic, so Kelly framing is less applicable.

- **Track slippage budget utilization.** If >20% of trades are cancelled due to slippage, the market is thinner than your volume filter suggests. Tighten min_volume.
