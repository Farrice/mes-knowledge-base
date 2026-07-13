---
name: "Polymarket Market Maker — Adverse Selection Defense Configuration"
source_prompt: born-v2
skill: prediction-market-making
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are building the defense layer that determines whether a Polymarket market-making deployment survives. This is the single highest-leverage system in the stack: the poly-maker author's own README verdict is that a sophisticated production bot — dual WebSocket, smart cancellation, stop-loss with sleep, position merging, 8-window volatility analysis — is "not profitable" on spread capture, specifically because adverse selection erodes returns faster than rewards accumulate. If reward income runs $200/day and adverse selection costs $250/day, the market maker loses $50/day regardless of how well-optimized the spread is. Defense is the load-bearing wall, not an add-on.

You are synthesizing patterns from three source layers: Polymarket's own WebSocket/heartbeat/rate-limit documentation, warproxxx/poly-maker's smart-cancellation and stop-loss-sleep logic, and ImMike/polymarket-arbitrage's 8-check risk validation chain. Build the defense system as a set of deterministic, testable rules — nothing in this layer should depend on judgment calls made in the moment. The moment for judgment is now, while designing the thresholds; execution must be mechanical.

## Input Required

```
[MARKET_TYPE] — sports / crypto / political / esports
[MARKET_NAME_AND_EVENT_DETAILS]
[EVENT_DURATION_AND_SCORE_EVENT_FREQUENCY] — e.g. NBA ~20 score events/game
[CURRENT_SPREAD_AND_SIZE_PARAMETERS] — your bot's live bid/ask spread and size
[CAPITAL_DEPLOYED_IN_THIS_MARKET]
[RISK_TOLERANCE] — conservative / balanced / aggressive
[INFRASTRUCTURE_STATUS] — which WebSocket channels are active (market / user / sports / RTDS)
```

## Execution Protocol

Build the defense system in the same eight layers this skill's material defines. Each layer is a distinct failure mode with a distinct fix — do not collapse them into one generic "risk management" paragraph.

**Layer 1 — Event detection sources.** Specify the primary detection channel for the given market type. Sports: `wss://sports-api.polymarket.com/ws`, auto-streams `sport_result` events, server pings every 5s and you respond within 10s (missing this drops the connection but does NOT cancel orders — only the user channel heartbeat does that). Map expected detection latency and price impact per event type: score change <1s / 5-50c impact, period transition <1s / 1-5c, injury 5-30s / 3-15c, red card <2s / 10-30c, VAR review 10-60s / 5-20c. For crypto/political, specify news-wire and on-chain oracle sources instead (Twitter/X firehose fastest but noisiest, news wire APIs for confirmed announcements, UMA Optimistic Oracle proposals for resolution-relevant signals). Layer in the market-data signal thresholds regardless of market type: midpoint move >3c/5s = auto-widen trigger, >5c/10s = auto-cancel trigger, volume spike >5x average = alert, `tick_size_change` = withdraw, `market_resolved` = close all.

**Layer 2 — Auto-cancel rules.** For any event classified "major" (score change, injury, resolution proximity), specify: immediate cancellation via batch `DELETE /orders` targeting specific order IDs (3,000/10s burst) — NOT `cancel-all` (250/10s, 4x slower). Map event type to cancel delay, re-quote spread multiplier, and decay-to-base period using the event-type table: basketball score change → immediate cancel, 2x spread after 5s, decay 60s; soccer/football score → immediate, 3x after 10s, decay 90s; injury → immediate, 2x after 15s, decay 120s; red card → immediate, 3x after 10s, decay 90s; halftime → immediate, 1.5x after 3s, decay 30s; political resolution proposal → immediate cancel, DO NOT re-quote until manually resolved. Note the sports-market 1-second delay on marketable orders as usable buffer — cancel within that window before a taker order can hit the resting quote.

**Layer 3 — Auto-widen rules.** For moderate events (price shift 1-5 cents, not a major score change), widen instead of cancel — cancelling forfeits reward-sampling continuity. Use: `new_spread = base_spread * (1 + event_severity * widen_factor)` with severity levels 0.5 (minor)/1.0 (moderate)/1.5 (significant)/2.0 (major — should trigger Layer 2 cancel, not widen), and widen_factor by risk tolerance: conservative 1.0, balanced 0.75, aggressive 0.5. Decay back to base via `current_spread = base_spread + (widened_spread - base_spread) * exp(-t/decay_constant)`, decay_constant 15s (minor)/30s (moderate)/60s (significant). Layer in the poly-maker smart-cancellation materiality threshold so widening doesn't itself generate needless cancel/replace churn: only update if `price_diff > 0.005 OR size_diff > order_size*0.1 OR existing_order_size == 0`.

**Layer 4 — Inventory rebalancing thresholds.** Pre-trade validation, not post-trade cleanup: `projected_exposure = abs(current_market_exposure + new_exposure)`; reject any order that would push projected exposure over `max_position_per_market` before it's ever placed. Tiered response: <20% imbalance = no action; 20-30% = asymmetric spread (widen overweight +0.5c per 10% over threshold, tighten underweight −0.5c); 30-40% = cancel the overweight side entirely (accept the 1/3 Q_min penalty rather than accumulate further); >40% = emergency — if `auto_unwind_on_breach: false` (the recommended default for market making), stop quoting the market entirely rather than dump inventory at market. Note the size-based rebalancing alternative (keep spreads symmetric, make the overweight side 2-3x larger) for cases where the 1/3 reward penalty from cancelling one side is unacceptable. Include position merging (`amount_to_merge = min(yes_position, no_position)`, executed when >20 contracts, recovers capital locked as offsetting Yes+No pairs) and the reverse-position block (refuse a new buy on one side while holding an unmerged opposing position).

**Layer 5 — Resolution proximity defense.** Graduated withdrawal by midpoint band: 0.15-0.85 normal quoting; 0.85-0.90 or 0.10-0.15 → widen 2x, reduce size 50%; >0.90 or <0.10 → withdraw entirely (strict `min(Q_one,Q_two)` Q_min applies here, no c=3.0 safety net, and insider-information risk is highest near resolution); any `tick_size_change` event → immediate withdrawal regardless of current midpoint, since it's an early warning signal independent of price level. State the hard-coded 0.10-0.90 price range block as a hard rejection in the order-creation path, not a soft warning.

**Layer 6 — Heartbeat management.** This is infrastructure defense: missing the USER channel heartbeat cancels ALL orders across ALL markets simultaneously — the single most expensive failure mode in the system. Specify: send PING with the most recent heartbeat_id every 5 seconds (stale IDs are rejected), retry immediately if no PONG within 3s, emergency reconnect if a second retry fails within 5s (cancel all, re-establish heartbeat, re-post the entire book from scratch). Market channel is important but not order-critical (miss = data feed loss, reconnect and re-subscribe). Sports channel direction is reversed (server pings, you pong). Include the reconnection protocol (exponential backoff 1s/2s/4s/8s, re-subscribe, immediate heartbeat, and for user channel: cancel all + re-fetch + re-post) and the Tuesday restart protocol specifically (cancel all at 6:58 AM ET, expect HTTP 425 "Too Early" during the ~90s restart window and treat it as a planned signal not an error, probe with backoff from 7:00-7:02 AM ET, re-establish on first 200).

**Layer 7 — Kill switch hierarchy.** The 8-check validation chain runs on every single order in sequence: kill switch status → market blacklist → whitelist filter → 24h volume minimum (10,000) → per-market exposure limit → global exposure limit → daily loss limit → drawdown limit. Kill switch is one-way (manual reset only); `auto_unwind_on_breach: false` by default (stop quoting, don't panic-sell). Drawdown is peak-to-trough (`(peak_pnl - total_pnl) / peak_pnl`) — flag explicitly that a bot up $500 and now flat reads as 100% drawdown from peak, so `max_drawdown_pct` must be set relative to expected daily P&L variance, not absolute capital. Configure by risk tolerance per the table (conservative: 1% max daily loss / 5% max drawdown / 25% per-market cap; balanced: 2% / 10% / 30%; aggressive: 3% / 15% / 40%). Include the stop-loss sleep period pattern: after a stop-loss triggers, refuse re-entry for N configurable hours, persisted to survive restarts — name the fundamental tension explicitly: sleep periods are necessary for survival but every minute in risk-off is zero reward accrual (out of 10,080 weekly one-minute samples), and this is the mechanism the poly-maker author identifies as what made the bot unprofitable.

**Layer 8 — Slippage validation gate.** Pre-order check: reject if `abs(intended_price - current_market_price) > slippage_tolerance`. Use 1% for market making (tighter than the 2% arbitrage default) — a market maker provides liquidity rather than chasing price, so any meaningful slippage means the quote is already stale.

Close with the decision tree: walk any given event through score-change check → midpoint-velocity check → inventory-imbalance check → resolution-proximity check → kill-switch check → Tuesday-restart-window check, in that order, and state which branch fires and why.

## Output Contract

- One fully populated defense configuration block per market, covering all 8 layers with market-type-specific numbers (not generic placeholders)
- Explicit dollar/time estimates for "adverse selection saved" vs "reward lost from widening/canceling" — net defense value must be stated, even if approximate, and labeled as an estimate
- The decision tree walked at least once against a concrete hypothetical event for this market, showing which branch fires
- Every threshold (cancel delay, widen multiplier, decay period, inventory %, drawdown %) must be tied to the risk tolerance tier supplied, not defaulted silently

## Output Skeleton

```
MARKET: [name]
TYPE: [sports / crypto / political / esports]
DEFENSE CONFIGURATION:

EVENT DETECTION
  Primary channel: ... | latency | events monitored
  Secondary channel(s): ... | thresholds
  Tertiary (if applicable): ...

AUTO-CANCEL RULES
  [event type: cancel delay | re-quote timing | re-quote multiplier | decay period]  (repeat per relevant event type)

AUTO-WIDEN RULES
  [severity tier: widen multiplier | decay constant]
  Smart-cancel materiality threshold: ...

INVENTORY LIMITS
  20% / 30% / 40% tier actions
  Position merging: enabled/threshold
  Reverse position block: active/inactive

RESOLUTION PROXIMITY
  Midpoint bands and actions
  tick_size_change handling
  Price range hard block: 0.10-0.90

HEARTBEAT
  User channel cadence and failure protocol
  Tuesday restart handling
  Reconnection protocol

KILL SWITCH
  max_daily_loss / max_drawdown_pct / auto_unwind / stop-loss sleep duration
  Slippage tolerance

ESTIMATED DEFENSE COSTS
  Adverse selection saved: $[X]/day — basis for estimate
  Reward lost from widening/canceling: $[Y]/day — basis for estimate
  Net defense value: $[X-Y]/day

DECISION TREE WALKTHROUGH (one worked hypothetical)
  Event: [describe] → branch fired → action taken → why
```

## Quality Gate

- Are all 8 layers present and market-type-specific, not a copy-pasted generic template?
- Does the kill switch config match the stated risk tolerance tier exactly (not a rounded-off approximation)?
- Is the user-channel vs market-channel vs sports-channel heartbeat distinction preserved (they have different failure consequences — collapsing them into one "heartbeat" line is a floor violation)?
- Is the stop-loss sleep tension (survival vs profitability) named explicitly, not glossed over?
- Does the decision tree walkthrough show an actual branch being selected for a real hypothetical event, not just the tree reprinted unused?
- Is the 0.10-0.90 price range enforced as a hard block, not a soft warning, in both Layer 5 and the order-management notes?

## Deploy When

A market-making deployment is going live or already running on a specific market and needs its full multi-layer adverse-selection defense specified before capital is exposed — or an existing defense config needs a fresh pass because market type, event cadence, or risk tolerance has changed.
