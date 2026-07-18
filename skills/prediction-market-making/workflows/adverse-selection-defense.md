---
workflow: "adverse-selection-defense"
skill: "prediction-market-making"
produces: "Complete defense system: news monitoring, auto-cancel/widen rules, inventory thresholds, heartbeat management, kill switch configuration"
tokens: "~2,800"
---

# Adverse Selection Defense

> Adverse selection is the #1 reason market makers lose money on Polymarket. The poly-maker author confirms the bot is "unprofitable" specifically because adverse selection destroyed returns faster than rewards accumulated. This workflow designs a complete multi-layer defense system that makes profitable market making possible. Without this, you are paying infrastructure costs to lose money to informed traders.

---

## Inputs Required

| Input | Required | Default |
|-------|----------|---------|
| Market type (sports / crypto / political / esports) | Yes | — |
| Specific market name and event details | Yes | — |
| Event duration and score event frequency | Yes | — |
| Bot's current spread and size parameters | Yes | — |
| Capital deployed in this market | Yes | — |
| Risk tolerance (conservative / balanced / aggressive) | Yes | balanced |
| Infrastructure status (which WebSocket channels active?) | Yes | — |

---

## The Adverse Selection Problem — Why This Workflow Exists

1. You post a bid at 48c and ask at 52c on "Team A wins"
2. Team A scores. True probability jumps to ~75%
3. Informed trader buys your 52c ask immediately
4. By the time you react, you sold at 52c something worth 75c
5. Loss: 23c per contract, potentially thousands of contracts
6. Typical adverse moves: 40-50 points on major news events

**The math**: If rewards generate $200/day and adverse selection costs $250/day, you lose $50/day regardless of spread optimization quality. Defense is the load-bearing wall of profitability.

---

## Layer 1: Event Detection Sources

### Sports Markets (Primary — via Sports WebSocket)

**Connection**: `wss://sports-api.polymarket.com/ws`
- No subscription message needed — auto-streams all `sport_result` events
- Heartbeat: SERVER sends ping every 5 seconds, YOU respond pong within 10 seconds
- Missing heartbeat: connection drop only (recoverable, but you lose score data)

**Events to Monitor**:
| Event Type | Detection Latency | Market Impact | Direction |
|-----------|-------------------|---------------|-----------|
| Score change (goal, basket, touchdown) | <1 second via WS | 5-50 cents | Toward scoring team |
| Period transition (halftime, quarter end) | <1 second | 1-5 cents | Varies |
| Injury/substitution | 5-30 seconds (delayed feed) | 3-15 cents | Against injured team |
| Red card / ejection | <2 seconds | 10-30 cents | Against penalized team |
| Official review / VAR decision | 10-60 seconds | 5-20 cents | Varies |
| Game status change (delay, suspension) | <5 seconds | Varies widely | Uncertain |

### Crypto / Political Markets (via News APIs + Social)

**Sources** (prioritized by speed):
1. Twitter/X firehose for keyword monitoring (fastest but noisiest)
2. News wire APIs (Reuters, AP) for official announcements
3. On-chain oracle data for resolution-relevant events
4. Platform-specific: UMA Optimistic Oracle proposals (`0xCB1822859cEF82Cd2Eb4E6276C7916e692995130`)

### Market Data Signals (via Market WebSocket)

**Connection**: `wss://ws-subscriptions-clob.polymarket.com/ws/market`
- Subscribe with token IDs for monitored markets
- Heartbeat: YOU send PING every 10 seconds

**Derived Signals**:
| Signal | Threshold | Meaning |
|--------|-----------|---------|
| Midpoint move > 3c in < 5 seconds | Auto-widen | Informed flow detected |
| Midpoint move > 5c in < 10 seconds | Auto-cancel | Major news event |
| Volume spike > 5x average | Alert | Possible informed trading |
| `tick_size_change` event | WITHDRAW | Approaching resolution |
| `market_resolved` event | CLOSE ALL | Market done |
| Spread widening by competitors | Widen yours | Others detected something |

---

## Layer 2: Auto-Cancel Rules

**Trigger**: Any Layer 1 event classified as "major" (score change, injury, resolution proximity).

**Action Protocol**:
```
1. IMMEDIATELY cancel all orders in affected market
   Method: Batch DELETE /orders targeting specific order IDs
   Rate limit: 3,000/10s burst — use this, NOT cancel-all (250/10s, 4x slower)
   
2. If batch DELETE fails (rate limited):
   Fallback: DELETE /cancel-market-orders (1,000/10s burst)
   
3. Log: timestamp, event type, orders cancelled, estimated market impact
```

**Re-Quote Timing by Event Type**:

| Event | Cancel Delay | Re-Quote Spread | Decay to Base |
|-------|-------------|----------------|---------------|
| Score change (basketball) | Immediate | 2x base, re-quote after 5s | 60 seconds |
| Score change (soccer/football) | Immediate | 3x base, re-quote after 10s | 90 seconds |
| Injury report | Immediate | 2x base, re-quote after 15s | 120 seconds |
| Red card / ejection | Immediate | 3x base, re-quote after 10s | 90 seconds |
| Period transition (halftime) | Immediate | 1.5x base, re-quote after 3s | 30 seconds |
| Resolution proposal (political) | Immediate | DO NOT re-quote until resolved | Manual |
| Midpoint move > 5c in 10s | Immediate | 2x base, re-quote after 10s | 60 seconds |

**The 1-Second Delay Gift**: Sports markets impose a 1-second delay on marketable orders (status: `delayed`). This gives you 1 second of buffer before a taker order hits your resting quote. Use it — cancel within that window.

---

## Layer 3: Auto-Widen Rules

**When to widen instead of cancel**: Moderate events that shift price 1-5 cents but don't represent major score changes. Cancelling loses reward accumulation; widening preserves some reward while reducing exposure.

**Widen Formula**:
```
new_spread = base_spread * (1 + event_severity * widen_factor)

event_severity levels:
  0.5 = minor (foul, possession change, routine play)
  1.0 = moderate (scoring opportunity, close call, substitution)
  1.5 = significant (penalty kick, power play, controversial call)
  2.0 = major (score, injury, ejection) — should be AUTO-CANCEL, not widen

widen_factor by risk tolerance:
  conservative: 1.0 (double on severity 1.0)
  balanced: 0.75
  aggressive: 0.5
```

**Auto-Tighten**: Exponential decay back to base spread:
```
At time t after event:
  current_spread = base_spread + (widened_spread - base_spread) * exp(-t / decay_constant)

decay_constant by event type:
  Minor event: 15 seconds
  Moderate event: 30 seconds
  Significant event: 60 seconds
```

**Smart Cancellation Integration**: Do NOT cancel and replace on every tick during widening/tightening. Apply the poly-maker materiality threshold:
```python
should_update = (
    price_diff > 0.005 or          # Price moved more than half a cent
    size_diff > order['size'] * 0.1 or  # Size changed more than 10%
    existing_order_size == 0         # No existing order
)
```
This preserves reward scoring continuity — cancelled/re-placed orders have a gap in sampling.

---

## Layer 4: Inventory Rebalancing Thresholds

Based on ImMike risk manager pattern — pre-trade validation, not post-trade cleanup.

**Validation Chain** (runs before EVERY order placement):
```python
projected_exposure = abs(current_market_exposure + new_exposure)
if projected_exposure > max_position_per_market:
    REJECT order  # Never let it through
```

**Tiered Response**:

| Inventory Imbalance | Action | Rationale |
|---------------------|--------|-----------|
| **< 20%** | No action. Symmetric quotes. | Normal market making flow |
| **20-30%** (Warning) | Asymmetric spread: widen overweight side +0.5c per 10% over threshold, tighten underweight -0.5c | Self-correcting without explicit dumps. Preserves reward score on underweight side |
| **30-40%** (Hard cap) | Cancel overweight side entirely. Only quote underweight side. | Accept 1/3 reward penalty (c=3.0 divisor) to prevent further accumulation. `max_position_per_market` enforces this. |
| **> 40%** (Emergency) | If `auto_unwind_on_breach: true`: dump 10% at market. If false (default): hold position, stop quoting entirely for this market. | For market making: auto_unwind should be FALSE. Stop quoting, don't panic-sell inventory at market. |

**Rebalancing Via Size, Not Spread** (alternative strategy):
Keep spreads equal on both sides but make overweight side 2-3x larger in size. This maintains reward scoring symmetry while incentivizing flow that reduces position. Use when 1/3 reward penalty from cancelling one side is unacceptable.

**Position Merging** (capital recovery):
When holding BOTH Yes and No tokens, merge to recover locked capital:
```python
amount_to_merge = min(yes_position, no_position)
if amount_to_merge > 20:  # MIN_MERGE_SIZE
    client.merge_positions(amount_to_merge, market, is_neg_risk)
    # Calls CTF contract 0x4D97DCd97eC945f40cF65F87097ACe5EA0476045
    # For neg risk: routes through Adapter 0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296
```

**Reverse Position Block** (poly-maker pattern):
When holding opposite token (e.g., No) and about to place a buy order for Yes: BLOCK the buy. Wait for merge to clear opposing position, then redeploy freed capital. Prevents capital-inefficient simultaneous opposing positions.

---

## Layer 5: Resolution Proximity Defense

Markets approaching resolution have maximum adverse selection risk — insiders know the outcome with increasing certainty.

**Graduated Withdrawal**:

| Midpoint Range | Action | Reason |
|---------------|--------|--------|
| 0.15-0.85 | Normal quoting | Standard reward zone |
| 0.85-0.90 / 0.10-0.15 | Widen spread 2x, reduce size 50% | Approaching extreme Q_min penalty |
| > 0.90 / < 0.10 | WITHDRAW ENTIRELY | Strict min Q_min (no c=3.0 safety net) + insider risk |
| `tick_size_change` event | IMMEDIATE WITHDRAWAL regardless of midpoint | Early warning of imminent resolution |

**The Hard-Coded Price Range** (poly-maker pattern):
```python
if order['price'] >= 0.1 and order['price'] < 0.9:
    # Create order
else:
    print("Not creating order — outside acceptable price range (0.1-0.9)")
```
Enforce this as a hard block in the order creation path, not as a soft warning.

---

## Layer 6: Heartbeat Management (Infrastructure Defense)

Missing the user channel heartbeat cancels ALL orders across ALL markets. This is the single most expensive infrastructure failure.

**Heartbeat Architecture**:
```
User channel (CRITICAL — miss = ALL ORDERS CANCELLED):
  - YOU send PING with latest heartbeat_id every 5 seconds
  - Stale heartbeat_ids are REJECTED — always use most recent
  - Server responds PONG
  - If no PONG within 3 seconds: RETRY IMMEDIATELY
  - If second retry fails within 5 seconds: EMERGENCY RECONNECT
  - On reconnect: cancel all + re-establish heartbeat + re-post entire book

Market channel (important, not critical):
  - YOU send PING every 10 seconds
  - Miss = data feed loss, NOT order cancellation
  - Reconnect and re-subscribe on failure

Sports channel (REVERSED direction):
  - SERVER sends ping every 5 seconds
  - YOU respond pong within 10 seconds
  - Miss = score data loss (bad for defense, not for orders)
```

**Reconnection Protocol** (applies to ALL channels):
```
1. Detect disconnect (no PONG for 15s, explicit close, read error)
2. Exponential backoff: 1s, 2s, 4s, 8s (max 8s)
3. On reconnect:
   a. Re-subscribe with current token/condition IDs
   b. Send heartbeat IMMEDIATELY
   c. If user channel: cancel all, re-fetch via REST, re-post quotes
   d. If market channel: re-fetch full book via GET /book to sync state
4. If 5 consecutive failures: trigger kill switch, alert operator
```

**Tuesday Restart** (every Tuesday, 7:00 AM ET, ~90s downtime):
```
6:58 AM ET: Cancel all orders across all markets
7:00 AM ET: Engine restarts — API returns HTTP 425 (Too Early)
7:00-7:02 AM ET: Exponential backoff probes (1s, 2s, 4s, 8s)
  - 425 = planned restart, NOT an error
  - Do NOT crash on 425 — this is the most common bot failure
First 200 response: Immediately re-establish heartbeat, re-post full book
```

**REST API Fallback** (when WebSocket down):
```
GET /book?token_id=X          (1,500 req/10s)
GET /price?token_id=X         (1,500 req/10s)
GET /midpoint?token_id=X      (1,500 req/10s)
POST /books (batch, 500 tokens) (500 req/10s)
```

---

## Layer 7: Kill Switch Hierarchy (from ImMike RiskManager)

The 8-check validation chain runs on EVERY order. All checks must pass in sequence:

```
Check 1: Kill switch status        → if triggered, REJECT (no exceptions)
Check 2: Market blacklist          → hard block on specific markets
Check 3: Whitelist filter          → if non-empty, only whitelisted allowed
Check 4: 24h volume minimum        → min_24h_volume: 10,000
Check 5: Per-market exposure limit → projected_exposure < max_position_per_market
Check 6: Global exposure limit     → portfolio notional ceiling
Check 7: Daily loss limit          → if daily_pnl < -max_daily_loss, trigger kill switch
Check 8: Drawdown limit            → if drawdown > max_drawdown_pct, trigger kill switch
```

**Kill Switch Properties**:
- ONE-WAY: once triggered, requires manual reset
- `auto_unwind_on_breach: false` (default) — stop opening, don't panic-sell
- Drawdown = peak-to-trough: `(peak_pnl - total_pnl) / peak_pnl`
- WARNING: Bot up $500, now flat = 100% drawdown from peak. Set max_drawdown_pct relative to expected daily P&L variance, NOT absolute capital.

**Kill Switch Configuration by Risk Tolerance**:
| Parameter | Conservative | Balanced | Aggressive |
|-----------|-------------|----------|------------|
| max_daily_loss | 1% of capital | 2% of capital | 3% of capital |
| max_drawdown_pct | 5% | 10% | 15% |
| auto_unwind | false | false | false |
| per_market_max | 25% capital | 30% capital | 40% capital |

**Stop-Loss Sleep Period** (poly-maker pattern):
After a stop-loss triggers, the bot refuses to re-enter for a configurable number of hours. This prevents the death spiral: stop-loss -> re-enter -> stop-loss -> re-enter. Risk-off state persisted to JSON file, survives bot restarts. Bot checks `current_time < start_trading_at` before any buy order.

**The fundamental tension**: Stop-losses are necessary for survival but destructive for profitability. Every minute in risk-off = zero reward accrual (10,080 one-minute samples per epoch). The poly-maker bot's stop-losses triggered so frequently that sleep periods accumulated, reducing active quoting time below the threshold needed for rewards to exceed adverse selection losses.

---

## Layer 8: Slippage Validation Gate

**Pre-order check**: Compare intended execution price at signal time vs actual market price at order time.

```python
if abs(intended_price - current_market_price) > slippage_tolerance:
    REJECT order  # Market has moved, quote is stale
```

**Settings**:
- Market making: `slippage_tolerance: 0.01` (1% — tighter than 2% arb default)
- Market makers provide liquidity, not chase price. Any significant slippage = stale quote.

---

## Defense Configuration Output Template

```
MARKET: [name]
TYPE: [sports / crypto / political]
DEFENSE CONFIGURATION:

EVENT DETECTION:
  Primary: Sports WebSocket (wss://sports-api.polymarket.com/ws)
    Latency: <1 second for scores, <5 seconds for status changes
    Events: score changes, period transitions, injuries, ejections
  Secondary: Market WebSocket midpoint deviation
    Threshold: >3c/5s = auto-widen, >5c/10s = auto-cancel
  Tertiary: [News API / Twitter monitoring] (if applicable)

AUTO-CANCEL RULES:
  Score event: Cancel via batch DELETE /orders within 1s, re-quote after [X]s at [Y]x spread
  Injury: Cancel within 2s, re-quote after 15s at 2x spread
  Period transition: Cancel within 1s, re-quote after 3s at 1.5x spread
  Midpoint move >5c/10s: Cancel within 1s, re-quote after 10s at 2x spread
  Resolution proximity: Cancel, DO NOT re-quote until review

AUTO-WIDEN RULES:
  Minor event: Widen to 1.5x base, decay over 15s
  Moderate event: Widen to 2x base, decay over 30s
  Significant event: Widen to 2.5x base, decay over 60s
  Smart cancel threshold: Only update if price_diff > 0.005 or size_diff > 10%

INVENTORY LIMITS:
  20% imbalance: Asymmetric spread (+0.5c overweight, -0.5c underweight)
  30% imbalance: Cancel overweight side (max_position_per_market enforced)
  40% imbalance: Stop quoting market (auto_unwind: false)
  Position merging: Enabled (min merge size: 20 contracts)
  Reverse position block: Active

RESOLUTION PROXIMITY:
  0.85-0.90 / 0.10-0.15: 2x spread, 50% size
  >0.90 / <0.10: Full withdrawal
  tick_size_change: Immediate withdrawal
  Price range hard block: 0.10-0.90 only

HEARTBEAT:
  User channel: 5-second cadence, immediate retry on failure
  Tuesday restart: Cancel 6:58 AM ET, probe 7:02 AM ET
  Reconnection: Exponential backoff 1s-8s, kill switch after 5 failures

KILL SWITCH:
  max_daily_loss: $[X] ([Y]% of capital)
  max_drawdown_pct: [Z]%
  auto_unwind: false
  Stop-loss sleep: [N] hours after trigger
  Slippage tolerance: 1.0%

ESTIMATED DEFENSE COSTS:
  Adverse selection saved: $[X]/day (events caught * avg loss prevented)
  Reward lost from widening/canceling: $[Y]/day (time off book * hourly reward rate)
  Net defense value: $[X-Y]/day
```

---

## Decision Tree: Event Detected

```
Event detected
  |
  +--> Is it a score change / major news?
  |     YES --> CANCEL ALL in this market (batch DELETE /orders)
  |             Wait [event-specific delay]
  |             Re-quote at [event-specific multiplier] x base spread
  |             Decay to base over [event-specific period]
  |     NO  --> Continue
  |
  +--> Is midpoint moving > 3c in 5 seconds?
  |     YES --> AUTO-WIDEN to 2x base (do not cancel — preserve reward continuity)
  |             Monitor: if move continues > 5c in 10s, escalate to CANCEL
  |     NO  --> Continue
  |
  +--> Is inventory > 20% one-sided?
  |     YES --> Asymmetric spread adjustment
  |             If > 30%: cancel overweight side
  |             If > 40%: stop quoting this market
  |     NO  --> Continue
  |
  +--> Is midpoint > 0.85 or < 0.15?
  |     YES --> Widen 2x, reduce size 50%
  |             If > 0.90 or < 0.10: WITHDRAW ENTIRELY
  |     NO  --> Continue
  |
  +--> Has kill switch triggered?
  |     YES --> HALT ALL. Manual reset required.
  |     NO  --> Normal operations continue
  |
  +--> Is it Tuesday 6:58-7:02 AM ET?
        YES --> Execute Tuesday restart protocol
        NO  --> Normal operations continue
```

---

## Output Schema

A **Defense Configuration** per market (matching the template above): event-detection sources with latency figures, auto-cancel rules per event type (cancel delay + re-quote spread multiplier + decay window), auto-widen formula parameters, inventory rebalancing thresholds (20/30/40%), resolution-proximity rules, heartbeat/reconnection protocol, kill-switch parameters by risk tier, and an estimated net defense value (adverse-selection dollars saved per day minus reward dollars forgone per day from widening/canceling).

## Quality Gate

1. **The Event-Type Coverage Test** — does every applicable event type for this market's category (score change, injury, period transition, midpoint move, resolution proximity) carry an explicit cancel-delay + re-quote-spread + decay-window triple, not a generic "widen on news" rule?
2. **The Cancel-Not-Widen Test** — is every event routed correctly — severity-2.0 (major) events to auto-cancel (Layer 2), not auto-widen (Layer 3)?
3. **The Reward-Continuity Test** — does the config include the smart-cancellation materiality threshold (price_diff > 0.005 OR size_diff > 10%), so the plan avoids the "requote on every tick" failure mode?
4. **The Net-Value Test** — is defense value quantified as adverse-selection-saved minus reward-lost-to-widening, not asserted as pure upside with no cost side?
5. **The Kill-Switch Test** — are all 8 risk-validation checks (Layer 7) and the stop-loss sleep period both present, with `auto_unwind_on_breach: false` unless the user explicitly overrode it?
