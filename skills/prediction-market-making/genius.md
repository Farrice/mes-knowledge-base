# Prediction Market Making — Genius Context

> Complete extraction intelligence from 5 source layers: Polymarket official docs, ImMike/polymarket-arbitrage, warproxxx/poly-maker, Polymarket/agents, ecosystem strategy analysis. Load this before executing any workflow. Contains 21 genius patterns, 13 hidden knowledge items, 3 exemplars + 1 anti-exemplar, 7 signature moves, and quality rubric.

---

## Genius Patterns (21)

### Pattern 1: The Quadratic Reward Cliff

The reward scoring function `S(v,s) = ((v-s)/v)^2 * b` creates an exponential payoff for tighter spreads.

**Worked example** (v = 10 cents max spread, b = 1.0 in-game multiplier):
- 1-cent spread: S = ((10-1)/10)^2 = 0.81
- 2-cent spread: S = ((10-2)/10)^2 = 0.64
- 3-cent spread: S = ((10-3)/10)^2 = 0.49
- 5-cent spread: S = ((10-5)/10)^2 = 0.25

The 1-cent quoter earns **3.24x** the reward of the 5-cent quoter. The marginal reward for tightening from 2 cents to 1 cent (+0.17) is worth more than tightening from 5 cents to 3 cents (+0.24 across two steps). The optimal strategy is as tight as adverse selection risk permits.

### Pattern 2: The Two-Sided Quoting Multiplier

For midpoints between 0.10 and 0.90:
`Q_min = max(min(Q_one, Q_two), max(Q_one/c, Q_two/c))` where c = 3.0

Single-sided quoting divides your score by 3. A perfectly balanced two-sided quoter with modest size earns 3x the score of a one-sided quoter with the same total capital. This is Polymarket's explicit engineering decision to force real liquidity provision.

### Pattern 3: The Post-Only Order as Zero-Fee Guarantee

Post-Only orders are rejected if they would cross the spread. Combined with `maker_fee_bps: 0`:
- Crypto markets: takers pay `0.072 * C * p * (1-p)` — makers pay 0
- Sports markets: takers pay `0.03 * C * p * (1-p)` — makers pay 0
- Geopolitical: exempt entirely

Post-Only only works with GTC and GTD order types. FOK and FAK are taker-intent by design. The ImMike config confirms: `maker_fee_bps: 0`, `taker_fee_bps: 150`.

### Pattern 4: The Heartbeat Kill Switch

"If a valid heartbeat is not received within 10 seconds (with a 5-second buffer), all open orders are cancelled."

- Send heartbeats every 5 seconds minimum (effective window is 15 seconds, but 5-second cadence provides safety margin)
- Use the **most recent** heartbeat_id — stale IDs are rejected
- If your bot crashes, your entire book is wiped within 15 seconds

Infrastructure priority #1. Before spread optimization, before reward calculation, before adverse selection defense — heartbeat management. A missed heartbeat costs every open order simultaneously.

### Pattern 5: The Extreme Midpoint Rule

For midpoints < 0.10 or > 0.90, Q_min switches from the c=3.0 formula to `min(Q_one, Q_two)` — strict minimum only. No safety net.

This prevents gaming at extremes. A market at 0.95 has one side (No at 0.05) that is structurally hard to quote tightly. The strict min forces genuine two-sided participation.

**Implication**: Markets near resolution (>0.90 or <0.10) are reward-hostile. Pull liquidity as markets approach extremes.

### Pattern 6: The GTD Stale Order Defense

GTD (Good-Til-Date) orders auto-expire. Platform enforces 60-second minimum: `expiration = now + 60 + N`.

For market makers, GTD is the stale order defense. A 5-minute GTD cycle forces regular requoting. The ImMike execution engine confirms: `order_timeout_seconds: 60`.

**Optimal pattern**: 5-minute GTD cycles during normal conditions, 60-second cycles during high-volatility windows.

### Pattern 7: The Matching Engine Tuesday Restart

Every Tuesday at 7:00 AM ET, the matching engine restarts (~90 seconds downtime). API returns HTTP 425 (Too Early).

**Correct behavior**: Detect 425 (NOT an error — planned restart signal). Pause order placement. Exponential backoff: 1s, 2s, 4s, 8s. Resume on 200 response. Re-establish heartbeat immediately. Re-quote all markets from scratch.

**Calendar-aware bots** pre-cancel at 6:59 AM ET and have fresh quotes at 7:02 AM ET.

### Pattern 8: The Reward Pool Economics

April 2026 reward pools per game:
- NBA: $7,700 | EPL: $10,000 | Champions League QF: $24,000
- MLB: $1,650 | NHL: $1,500 | UFC Main Card: $4,250
- CS2 A-Tier: $5,500 | IPL Cricket: $4,500

With 10,080 one-minute samples per weekly epoch, daily distribution at midnight UTC:

`Expected_daily = (your_Q_final / total_Q_final) * daily_reward_pool`

A Champions League QF at $24K over ~3 days = ~$8K/day. With 10 competing makers and 15% Q_final capture = $1,200/day from one market.

### Pattern 9: The Inventory 30% Rule

"Never exceed 30% exposure on one side." When inventory drifts past 30%, you are a directional bettor.

- Widen spread on overweight side, tighten on underweight
- At 40%+: cancel overweight side entirely

The ImMike risk manager validates projected exposure BEFORE order placement: `projected_exposure = abs(current_market_exposure + new_exposure)`. Pre-trade validation, not post-trade cleanup.

### Pattern 10: The WebSocket Architecture Priority Stack

Four simultaneous data streams required:

1. **Market Channel** (`wss://ws-subscriptions-clob.polymarket.com/ws/market`): Book snapshots, price changes, trades. Subscribe with token IDs.
2. **User Channel** (`wss://ws-subscriptions-clob.polymarket.com/ws/user`): Your fills, cancellations, trade lifecycle (MATCHED -> MINED -> CONFIRMED or FAILED/RETRYING). Requires API credentials.
3. **Sports Channel** (`wss://sports-api.polymarket.com/ws`): Scores, periods, status changes. Auto-streams, no subscription needed.
4. **RTDS Channel** (`wss://ws-live-data.polymarket.com`): Real-time data streaming. Optional auth.

Heartbeat protocol differs by channel:
- Market/User: YOU send PING every 10 seconds, server responds PONG
- Sports: SERVER sends ping every 5 seconds, YOU respond pong within 10 seconds

**Critical asymmetry**: Missing user channel heartbeat cancels ALL orders. Missing market/sports heartbeat only drops data feed.

### Pattern 11: The Rate Limit Architecture

- `POST /order`: 3,500/10s burst, 36,000/10min sustained
- `DELETE /order`: 3,000/10s burst, 30,000/10min sustained
- `POST /orders` (batch): 1,000/10s burst, 15,000/10min sustained
- `DELETE /cancel-all`: 250/10s burst, 6,000/10min sustained

**Key insight**: Batch orders accept up to 15 orders per request. Effective throughput: 15,000 orders/10s via batching vs 3,500/10s individual — a 4.3x multiplier. All market making bots should batch.

### Pattern 12: The Maker Rebate Flywheel

Taker fees fund maker rebates. Flywheel: tight spreads -> more taker volume -> more fees -> larger rebates -> more makers -> tighter spreads. A market maker in high-volume sports markets benefits: the takers filling your orders generate the rebate pool supplementing your income.

### Pattern 13: The 8-Check Risk Validation Chain

Every order passes ALL 8 checks in sequence (from ImMike risk manager):

1. **Kill switch status** — if triggered, reject everything (no exceptions)
2. **Market blacklist** — hard block on specific markets
3. **Whitelist filter** — if non-empty, only whitelisted markets allowed
4. **24h volume minimum** — skip illiquid markets (`min_24h_volume: 10000`)
5. **Per-market exposure limit** — projected exposure must be under cap
6. **Global exposure limit** — portfolio-level notional ceiling
7. **Daily loss limit** — if `daily_pnl < -max_daily_loss`, trigger kill switch
8. **Drawdown limit** — if `current_drawdown > max_drawdown_pct`, trigger kill switch

Kill switch is **one-way**: requires manual reset. `auto_unwind_on_breach: false` (default) — stop quoting, don't panic-sell.

Drawdown uses peak-to-trough: `current_drawdown = (peak_pnl - total_pnl) / peak_pnl`. A bot up $500 now flat = 100% drawdown from peak. Set `max_drawdown_pct` relative to expected daily P&L variance, not absolute capital.

### Pattern 14: The Slippage Validation Gate

ImMike enforces `slippage_tolerance: 0.02` (2%) — comparing intended price at signal time vs actual price at order time.

**For market making**: Use 1% tolerance (tighter than arb default). Market makers provide liquidity, not chase price. Any significant slippage means the market moved and your quote is stale.

### Pattern 15: The Smart Order Cancellation Threshold (poly-maker)

The bot does NOT cancel/replace on every tick. Materiality threshold:

```python
should_cancel = (
    price_diff > 0.005 or          # Price moved more than half a cent
    size_diff > order['size'] * 0.1 or  # Size changed more than 10%
    existing_buy_size == 0          # No existing order
)
```

Critical for two reasons:
1. **Rate limit conservation**: Every cancel-and-replace costs 2 API calls
2. **Reward scoring continuity**: Cancelled/re-placed orders have a gap in sampling. Gap costs reward points. Resting orders accumulate continuously.

### Pattern 16: The Stop-Loss / Risk-Off Sleep Period (poly-maker)

Multi-condition stop-loss with FORCED SLEEP PERIOD:

```python
if (pnl < stop_loss_threshold and spread <= spread_threshold) or volatility_3h > volatility_threshold:
    # Sell position at best bid (emergency liquidation)
    # Cancel ALL orders
    # Write risk-off timestamp to file
    # Sleep for N hours — NO BUYING during this period
```

The sleep period prevents the death spiral: stop-loss -> re-enter -> stop-loss -> re-enter. Risk-off state persisted to JSON, survives bot restarts.

**The fundamental tension**: Stop-losses are necessary for survival but destructive for profitability. Every minute in risk-off = zero reward accrual. The poly-maker bot chose survival over profitability.

### Pattern 17: Position Merging for On-Chain Capital Recovery (poly-maker)

When holding BOTH Yes and No tokens, positions cancel out but capital stays locked on-chain:

```python
amount_to_merge = min(pos_1, pos_2)
if float(amount_to_merge) > CONSTANTS.MIN_MERGE_SIZE:  # 20 minimum
    client.merge_positions(amount_to_merge, market, is_neg_risk)
```

Calls Conditional Tokens contract (`0x4D97DCd97eC945f40cF65F87097ACe5EA0476045`) to convert matching Yes+No pairs back to USDC.e. For neg risk: routes through Neg Risk Adapter (`0xd91E80cF2E7be2e162c6513ceD06f1dD0dA35296`). Executed via Gnosis Safe.

Without merging: 500 Yes + 300 No = $300 unnecessarily locked. Merging recovers as liquid USDC.e.

### Pattern 18: Google Sheets as Market Selection Control Plane (poly-maker)

5 tabs: Full Markets, All Markets, Volatility Markets, Selected Markets, Hyperparameters.

Market selection sorts by `gm_reward_per_100` (geometric mean of bid and ask reward per $100). Composite score combines standardized reward, inverted volatility, and price proximity to extremes.

Human-in-the-loop: bot calculates projections, human selects which markets to quote. Prevents deployment into markets with hidden manipulation or imminent resolution.

### Pattern 19: The Volatility / Reward Ratio (poly-maker)

Calculates annualized volatility across 8 windows (1h, 3h, 6h, 12h, 24h, 7d, 14d, 30d). `volatility_sum = 24h + 7d + 14d`. Markets with `volatility_sum >= 20` excluded entirely. 3-hour volatility is real-time trade gate.

A $10K EPL match with 5% volatility is far more profitable than a $24K CL QF with 40% volatility.

### Pattern 20: The Reverse Position Block (poly-maker)

When holding opposite token (e.g., No tokens and about to place Yes buy), the bot blocks:

```python
rev_pos = get_position(rev_token)
if rev_pos['size'] > row['min_size']:
    print("Bypassing creation of new buy order because there is a reverse position")
```

Prevents building opposing positions simultaneously. Waits for merge to clear, then redeploys freed capital.

### Pattern 21: The LLM-Deterministic Split Architecture (Polymarket/agents)

Official framework: LLMs handle analysis, deterministic code handles execution.

Pipeline: Events -> RAG filter (ChromaDB) -> Market mapping -> LLM Superforecaster -> Probability -> `one_best_trade()` -> Execution.

LLM determines WHICH markets to quote and HOW WIDE. Deterministic layer handles ALL order lifecycle. Putting an LLM in the heartbeat loop or cancellation path would be catastrophic.

---

## Hidden Knowledge (13)

### Hidden 1: Why Polymarket Pays $5M+/Month
Platform revenue = taker fees. Taker volume = f(spread tightness). Rewards buy tight spreads, which attract taker volume generating far more than $5M in fees. The program is customer acquisition cost, not charity.

### Hidden 2: The Display Price Threshold
"If spread > $0.10, last traded price shown instead of midpoint." Wide-spread markets look dead to casual traders, discouraging participation. Tight spreads earn rewards AND generate additional taker volume through display.

### Hidden 3: The Settlement Risk Window
Order lifecycle: MATCHED -> MINED -> CONFIRMED (or MATCHED -> RETRYING -> FAILED). During MATCHED-to-CONFIRMED, capital is committed but not settled. Invisible in backtests, real in production.

### Hidden 4: The Neg Risk Capital Efficiency Arbitrage
In multi-outcome neg risk markets, "A No share in any market can be converted into 1 Yes share in every other market." Post collateral once, quote across all outcomes, use conversion to rebalance without additional deposits.

### Hidden 5: The Tick Size Volatility Signal
At extreme territory (>0.96 or <0.04), tick size changes via WebSocket `tick_size_change` event. Available: 0.1, 0.01, 0.001, 0.0001. Early warning of approaching resolution. Widen or withdraw entirely.

### Hidden 6: The Size Formula Capital Lock
`maxOrderSize = balance - sum(openOrderSize - filledAmount)`. Every open order locks capital. 20 orders across 5 markets = significant locked capital. Cancel stale orders rather than posting alongside them.

### Hidden 7: The Sports Market 1-Second Delay
Sports markets impose 1-second delay on marketable orders (status: `delayed`). Polymarket's own adverse selection defense. For market makers: a gift — 1 second of buffer before a taker order hits your resting quote.

### Hidden 8: The Batch Endpoint Asymmetry
`POST /orders` (batch) = 1,000/10s = 15,000 effective. `DELETE /cancel-all` = only 250/10s. In crisis, batch-cancelling specific orders is 4x faster than cancel-all. Target specific markets via batch delete.

### Hidden 9: The "Markets Too Efficient" Config Comment
ImMike config: `mm_enabled: false` — "Disabled for real data (markets too efficient)." Pure spread capture not viable: spreads too tight (min_spread: 0.05 = 5 cents), adverse selection eats spread, gas ($0.02/order) erodes further. Rewards program is what makes it viable.

### Hidden 10: The Author's Verdict — "This Bot Is Not Profitable" (poly-maker)
From the poly-maker README, the most critical line in the ecosystem. This is from a sophisticated production bot with dual WebSocket, smart cancellation, stop-loss with sleep, position merging, Google Sheets control, 8-window volatility analysis. If THIS bot is unprofitable, the lesson is clear: profitability requires surviving adverse selection WITHOUT triggering stop-losses so frequently that reward uptime is destroyed. The bot chose survival over profitability — correct choice, but reveals the fundamental tension.

### Hidden 11: The 0.1-0.9 Price Range Hard Block (poly-maker)
```python
if order['price'] >= 0.1 and order['price'] < 0.9:
    # Create order
else:
    print("Not creating buy order because its outside acceptable price range (0.1-0.9)")
```
Matches extreme midpoint Q_min rule but goes further — won't even place orders outside 0.10-0.90.

### Hidden 12: The Geometric Mean Reward (poly-maker)
```python
gm_reward_per_100 = round((best_bid_reward * best_ask_reward) ** 0.5, 2)
```
Geometric mean, not arithmetic. If bid earns $5/100 and ask earns $0.50/100: arithmetic mean = $2.75, geometric = $1.58. Geometric better predicts actual income because Q_min uses the MINIMUM of two sides. Markets sorted by `gm_reward_per_100` descending, minimum threshold 0.75.

### Hidden 13: The Cross-Platform Fee Asymmetry
Polymarket taker: 1.5% (maker: 0%). Kalshi taker: ~1.0%. A market maker providing liquidity on Polymarket (0% maker) while consuming on Kalshi (1% taker) has structural fee advantage. Polymarket = preferred venue for resting orders.

---

## Hall of Fame Exemplars

### Exemplar 1: The Reward Scoring Algorithm — Full Optimization Path

**Context**: NBA game, $7,700 pool, 4 competitors, midpoint 0.55, v = 10 cents.

Your quotes: Buy 0.53, Sell 0.57 (4-cent spread, s = 2 cents from adjusted midpoint)
- You: S = ((10-2)/10)^2 = 0.64, two-sided Q_min = 0.64
- Competitor A (8-cent spread, s=4): S = 0.36, Q_min = 0.36
- Competitor B (6-cent spread, s=3): S = 0.49, Q_min = 0.49
- Competitor C (10-cent spread, s=5): S = 0.25, Q_min = 0.25
- Competitor D (single-sided, s=2): S = 0.64 one side, 0 other. Q_min = max(min(0.64,0), max(0.64/3, 0/3)) = 0.213

**Q_normal**: 0.64 / (0.64 + 0.36 + 0.49 + 0.25 + 0.213) = 0.64 / 1.553 = **41.2%**

**Daily reward** (3-day window): $7,700 / 3 = $2,567/day * 0.412 = **$1,058/day**

Two cents tighter than Competitor B earns $1,058 vs their $811 — $247/day premium for 2 cents of tightening.

### Exemplar 2: The Order Lifecycle of a Market Making Bot

**Minute 0:00** — Initialize: authenticate (L2 via POST /auth/api-key), connect 3 WebSocket channels, start heartbeat at 5s interval, fetch orderbook, initialize risk manager.

**Minute 0:01** — Post initial quotes: calculate fair value, set 3-cent spread each side, create Post-Only GTC buy + sell, run through 8-check risk manager, batch submit via POST /orders, verify `live` status.

**Minute 0:05** — Heartbeat: send with latest heartbeat_id. If fails, immediate retry. If second fails within 5s, re-establish WebSocket and re-post all orders.

**Minute 0:12** — Buy filled (MATCHED): update inventory, update P&L, validate slippage, adjust quotes (widen buy +0.5c, tighten sell -0.5c), monitor MATCHED -> MINED -> CONFIRMED.

**Minute 0:30** — Score event: immediately cancel ALL via batch DELETE /orders (NOT cancel-all — 4x faster). Wait 2-5s. Re-fetch book. Re-quote at 2x spread. Tighten back over 60 seconds.

**Minute 5:00** — GTD cycle: cancel all resting, re-fetch book, post fresh Post-Only GTD orders (expiration = now + 360), log P&L + inventory + reward estimate, check kill switch.

### Exemplar 3: The WebSocket + Heartbeat Architecture

```
[MARKET CHANNEL]                    [USER CHANNEL]                     [SPORTS CHANNEL]
wss://ws-subscriptions-clob.        wss://ws-subscriptions-clob.       wss://sports-api.
polymarket.com/ws/market            polymarket.com/ws/user              polymarket.com/ws

Subscribe:                          Subscribe:                          Subscribe:
{                                   {                                   (none — auto-streams)
  "assets_ids": ["tok1","tok2"],      "auth": {
  "type": "market",                      "apiKey": "...",
  "custom_feature_enabled": true         "secret": "...",
}                                        "passphrase": "..."
                                       },
                                       "condition_ids": ["cond1"]
                                     }

Events received:                    Events received:                    Events received:
- book (snapshot)                   - order (placed/cancelled)          - sport_result
- price_change (level update)       - trade (MATCHED->CONFIRMED)        - (scores, periods,
- last_trade_price (execution)                                            status changes)
- tick_size_change (extremes)
- best_bid_ask (custom feature)
- market_resolved (custom feature)

Heartbeat:                          Heartbeat:                          Heartbeat:
YOU send PING every 10s             YOU send PING every 10s             SERVER sends ping/5s
Server responds PONG                Server responds PONG                YOU respond pong/10s
Miss = connection drop              Miss = ALL ORDERS CANCELLED         Miss = connection drop
```

**Reconnection**: Detect disconnect -> exponential backoff 1s, 2s, 4s, 8s -> re-subscribe -> immediate heartbeat -> if user channel: cancel all + re-fetch + re-post.

### Anti-Exemplar: The Single-Sided "Market Maker"

Bot quotes only Yes side at $0.55 midpoint (buy at 0.53 and 0.51). What goes wrong:
1. **Reward penalty**: Q_min uses Q/3 because min(Q_one, Q_two) = 0. Score divided by 3x.
2. **Adverse selection**: Every fill is directional. Team scores = your buys correct. Underdog scores = holding overvalued inventory.
3. **No spread income**: Without opposing side, no spread capture.
4. **Inventory runaway**: Every fill adds same side. 100% one-sided within minutes.
5. **No risk gating**: Without check_order() rejecting at max_position_per_market, position grows until capital exhausted.

Outcome: 1/3 reward income, full adverse selection, zero spread capture. This is the documented failure mode that made poly-maker "unprofitable."

---

## Signature Moves (7)

### Move 1: Post-Only GTD Two-Sided Cycle
Post two-sided quotes using Post-Only GTD with 5-minute expiration. Every 5 minutes: cancel, re-fetch book, re-quote. Guarantees maker status (0% fees), automatic stale order protection, two-sided reward boost. 60-second minimum prevents microsecond cycling.

### Move 2: Inventory-Adjusted Asymmetric Spreads
At >20% drift to one side: widen overweight +1 cent, tighten underweight -1 cent. Self-correcting without explicit inventory dumps. At >30%: cancel overweight side entirely (per max_position_per_market).

### Move 3: Score-Event Rapid Withdrawal
On any sports score event (sports WebSocket): immediately cancel all via batch DELETE /orders (NOT cancel-all — 4x faster rate limit). Wait 2-5 seconds. Re-quote at 2x normal spread. Tighten back to normal over 60 seconds.

### Move 4: Calendar-Aware Tuesday Restart Protocol
At 6:58 AM ET every Tuesday: cancel all orders. At 7:02 AM ET: exponential backoff probes (1s, 2s, 4s — detect via HTTP 425). On first 200: immediately re-establish heartbeat and re-post full book.

### Move 5: Reward Pool Market Selection
Before deploying: `expected_reward = pool_per_game * estimated_market_share`. Focus on high-pool markets (CL $24K, EPL $10K) with fewer sophisticated competitors. Skip MLB ($1,650) unless competition is minimal. Volume filter: min_24h_volume 10,000.

### Move 6: Extreme Midpoint Exit
When midpoint crosses 0.90 or drops below 0.10: begin withdrawal. Strict min Q_min makes two-sided quoting punishing, and adverse selection spikes (insider info about outcome becomes more valuable). `tick_size_change` event is the early warning.

### Move 7: Batch Order Throughput Maximization
Always use POST /orders (batch, 15/request) instead of POST /order (single). Effective: 15,000/10s vs 3,500/10s. For 10 markets with buy+sell each, one batch handles all 20 orders. Pair with slippage_tolerance gate.

---

## Quality Rubric

| Dimension | Score 1-3 | Score 4-6 | Score 7-8 | Score 9-10 |
|-----------|-----------|-----------|-----------|------------|
| **Spread Optimization** | Fixed spread, no adaptation | Spread adjusts to volatility | Quadratic reward-aware spread sizing | Dynamic spread maximizing S(v,s) given real-time competition and inventory |
| **Reward Maximization** | Unaware of reward program | Knows rewards, single-sided | Two-sided with basic Q calculation | Full Q chain optimization with market selection by pool/competition ratio |
| **Adverse Selection Defense** | No defense, holds through news | Widens on "high volatility" | Score-event auto-cancel with rapid re-quote | Multi-layer: score events, injury news, resolution proximity, inventory limits, asymmetric adjustment |
| **Infrastructure** | REST polling, no heartbeat mgmt | WebSocket + basic heartbeat | Full 3-channel WebSocket + heartbeat priority + batch orders | Calendar-aware restarts, reconnection protocol, settlement risk tracking, rate limit optimization |
| **Risk Management** | No position limits | Basic capital allocation | Per-market exposure + daily loss cap | Full 8-check validation: kill switch, blacklist, volume, per-market, global, daily loss, drawdown |
| **Capital Efficiency** | One market, all capital | 3-5 markets, fixed allocation | Dynamic allocation by reward pool | Portfolio-level: capital rotates to highest marginal Q_final per dollar |

---

## Realistic P&L on $50K Capital

**Income streams**:
1. Spread capture: $250-$500/month (0.5-1.0%)
2. Liquidity rewards: $3,000-$8,000/month (6-16% — the real money)
3. Maker rebates: $100-$300/month (0.2-0.6%)

**Cost drivers**:
1. Adverse selection: -$500 to -$2,000/month (-1% to -4%)
2. Gas: -$50 to -$150/month ($0.02/order, ~2,500-7,500 orders/month)
3. Infrastructure: ~$300/month

**Net**: $2,800-$6,650/month (5.6-13.3%) — reward-dominated

Without rewards: marginally profitable at best (confirmed by `mm_enabled: false`).
