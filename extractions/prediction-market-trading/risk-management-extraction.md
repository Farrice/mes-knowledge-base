# Cross-Strategy Risk Management — MES 3.0 Mastery Extraction
## Domain: Prediction Market Capital Protection
## Sources: WeatherBot (alteregoeth-ai/weatherbot), Sovereign Trader Analysis (multi-source), Polymarket Official Docs, Polymarket Arbitrage Bot (ImMike/polymarket-arbitrage), Poly-Maker Market Making Bot (warproxxx/poly-maker), Polymarket Agents Framework (Polymarket/agents)
## Extraction Date: 2026-04-13

---

## THE CORE TRUTH

**92.4% of Polymarket wallets are unprofitable.** The 7.6% that survive share one trait: they treat risk management as the product, not an afterthought bolted onto strategy. Every edge decays. Arbitrage windows compressed from 12.3 seconds (2024) to 2.7 seconds (2026) to dead. Strategies that printed money in February fail by March. The ONLY durable asset is the system that keeps you alive while edges rotate.

The paper-to-live gap is the single most important finding in prediction market trading: simulation showed 522x returns while live v2 lost 49.5% and live v3 lost 13% using identical signal logic. Every backtest lies. The question is not "will my strategy work?" but "will I survive when it doesn't?"

---

## LAYER 1: SURFACE INTELLIGENCE — The Numbers That Matter

### Position Sizing Parameters (WeatherBot `bot_v2.py`)

| Parameter | Value | Function | Code Reference |
|-----------|-------|----------|----------------|
| `KELLY_FRACTION` | 0.25 | Quarter-Kelly cap on all positions | `calc_kelly()` line 758 |
| `MAX_BET` | $20 | Hard ceiling regardless of Kelly output | `bet_size()` line 762 |
| `MIN_EV` | 0.10 | Minimum 10% expected value to enter | `scan_and_update()` line 1268 |
| `MAX_PRICE` | 0.45 | Never buy contracts above 45 cents | Config + line 1318 |
| `MAX_SLIPPAGE` | 0.03 | Maximum bid-ask spread tolerance | Line 1306 |
| `MIN_VOLUME` | 500 | Minimum market volume for liquidity | Line 1265 |
| `MIN_HOURS` | 2.0 | Don't enter markets resolving in <2h | Line 1243 |
| `MAX_HOURS` | 72.0 | Don't enter markets >72h from resolution | Line 1120 |

### Arbitrage Bot Risk Parameters (polymarket-arbitrage `config.yaml`)

| Parameter | Value | Function | Config Location |
|-----------|-------|----------|-----------------|
| `max_position_per_market` | $15 (conservative) / $200 (default class) | Per-market exposure ceiling | `risk:` section + `RiskConfig` |
| `max_global_exposure` | $50 (conservative) / $5,000 (default class) | Total portfolio exposure cap | `risk:` section + `RiskConfig` |
| `max_daily_loss` | $10 (conservative) / $500 (default class) | Daily loss trigger for kill switch | `risk:` section |
| `max_drawdown_pct` | 15% (conservative) / 10% (default class) | Drawdown from peak trigger | `risk:` section |
| `slippage_tolerance` | 0.02 (2 cents) | Max allowed slippage signal-to-execution | `trading:` section |
| `order_timeout_seconds` | 60 | Cancel unfilled orders after this | `trading:` section |
| `default_order_size` | $5 | Standard order size | `trading:` section |
| `max_order_size` | $10 | Hard ceiling per order | `trading:` section |
| `min_edge` | 1% (bundle) / 2% (cross-platform) | Minimum edge after fees to trade | `trading:` + `CrossPlatformArbEngine` |

### Market Maker Risk Controls (poly-maker `trading.py`)

| Parameter | Function | Code Reference |
|-----------|----------|----------------|
| `stop_loss_threshold` | PnL % trigger for emergency sell (param-configurable) | `trading.py` line 431 |
| `spread_threshold` | Max spread for stop-loss execution (won't sell into wide spreads) | `trading.py` line 431 |
| `volatility_threshold` | 3-hour volatility ceiling — blocks buys AND triggers sells | `trading.py` lines 431, 475 |
| `sleep_period` | Hours to pause trading after risk-off event (cooldown) | `trading.py` line 439 |
| `take_profit_threshold` | % above avgPrice for take-profit orders | `trading.py` line 509 |
| `max_size` | Maximum position size per market | `trading.py` line 384 |
| `min_size` | Minimum order size (prevents dust trades) | `trading.py` line 452 |
| Price range guard | Buy orders only placed between $0.10-$0.90 | `trading.py` line 243 |
| Price change guard | Cancel all orders if price drifts > $0.05 from reference | `trading.py` line 475 |
| Smart cancellation | Only cancel/replace if price diff > $0.005 OR size diff > 10% | `trading.py` lines 221-226 |
| Stale trade cleanup | Pending trades removed after 15 seconds | `main.py` line 137 |
| Position merging | Merge YES+NO positions to recover USDC collateral | `trading.py` lines 312-323 |

### Stop-Loss Architecture (WeatherBot `monitor_positions()`)

| Mechanism | Trigger | Code Location |
|-----------|---------|---------------|
| Stop-loss | Price drops 20% from entry (`entry * 0.80`) | Line 1195, 1540 |
| Trailing stop | Moves to breakeven when position is +20% | Line 1198, 1556 |
| Take-profit (48h+) | Exit at $0.75 | Line 1553 |
| Take-profit (24-48h) | Exit at $0.85 | Line 1551 |
| Take-profit (<24h) | Hold to resolution | Line 1549 |
| Forecast-change exit | Close if forecast shifts 2+ degrees outside bucket | Lines 1216-1240 |

### The 8-Check Order Validation Chain (polymarket-arbitrage `risk_manager.py`)

Every order passes through this sequential gate. ANY failure = order rejected. Checks 7 and 8 auto-trigger the kill switch if `kill_switch_enabled`:

| Check | What It Validates | Failure Action |
|-------|-------------------|----------------|
| 1. Kill switch status | `kill_switch_triggered == False` | Reject (trading halted) |
| 2. Market blacklist | `order.market_id not in blacklist` | Reject silently |
| 3. Whitelist (if set) | `order.market_id in whitelist` | Reject silently |
| 4. 24h volume minimum | `market_volume >= min_24h_volume (10,000)` | Reject (illiquid) |
| 5. Per-market exposure | `projected_exposure <= max_position_per_market` | Reject (concentrated) |
| 6. Global exposure | `projected_global <= max_global_exposure` | Reject (overleveraged) |
| 7. Daily loss limit | `daily_pnl >= -max_daily_loss` | **Reject + TRIGGER KILL SWITCH** |
| 8. Drawdown limit | `current_drawdown <= max_drawdown_pct` | **Reject + TRIGGER KILL SWITCH** |

The kill switch is a one-way door: once `kill_switch_triggered = True`, ALL subsequent orders are rejected at Check 1. The system logs the reason via `logger.critical()`. Recovery requires manual intervention — there is no auto-reset.

### Portfolio-Level Controls (Sovereign Analysis + Arbitrage Bot)

| Control | Value | Source |
|---------|-------|--------|
| Max capital per market | 10% | Medium/Illumination strategy guide |
| Daily drawdown circuit breaker | 5% — pauses ALL trading | Same + PolySwarm paper |
| Correlation rebalance threshold | 30% | Portfolio construction data |
| Human underperformance vs bots | ~18% worse using identical strategies | 50,000+ wallet analysis |
| Cross-platform size cap | min(buy_liquidity, sell_liquidity, $100) | `CrossPlatformArbEngine.check_arbitrage()` |

### Platform Risk Parameters (Polymarket Docs)

| Risk | Detail | Mitigation |
|------|--------|------------|
| Heartbeat timeout | 10-second window (5s buffer), miss = ALL orders cancelled | Send heartbeat every 5 seconds using latest `heartbeat_id` |
| Matching engine restart | Tuesdays 7 AM ET, ~90s downtime, HTTP 425 | Exponential backoff (1-2s, doubling), detect 425 vs permanent failure |
| Trading disabled | HTTP 503 — exchange paused | Cancel-only mode still works; detect and halt new orders |
| Rate limits (orders) | 3,500/10s burst, 36,000/10min sustained | Track request counts per window; batch via `POST /orders` (15 max) |
| Cancel-all rate | 250/10s, 6,000/10min | Emergency exits are rate-limited — plan accordingly |
| Fee peak | At 50% probability: `fee = C * feeRate * 0.50 * 0.50 = C * feeRate * 0.25` | Crypto feeRate 0.072, Sports 0.03, Geopolitical 0 |

---

## LAYER 2: HIDDEN PATTERNS — What the Code Reveals That Documentation Won't

### Why Quarter-Kelly and Not Half or Full

The Kelly Criterion formula for prediction markets:
```
f* = (p * b - (1 - p)) / b
where b = (1/price) - 1 (the odds ratio)
```

Worked example from WeatherBot `calc_kelly()`:
- Forecast probability `p` = 0.80
- Market price = $0.10 (90% underpriced)
- Odds ratio `b` = (1/0.10) - 1 = 9
- Full Kelly: `f* = (0.80 * 9 - 0.20) / 9 = (7.2 - 0.2) / 9 = 0.778`
- Quarter-Kelly: `f = 0.25 * 0.778 = 0.194` (19.4% of bankroll)
- With MAX_BET cap: `min(0.194 * $10,000, $20) = $20`

The MAX_BET hard cap is the second gate. Even when Kelly says bet 19.4% of $10K ($1,940), the actual bet is $20. This creates a three-layer sizing defense:
1. Kelly fraction (0.25) reduces variance by ~75% while sacrificing only ~25% of expected growth rate
2. MAX_BET ($20) prevents any single trade from being material
3. MAX_PRICE (0.45) prevents buying expensive contracts where downside overwhelms edge

**Why 0.25 specifically?** Quarter-Kelly is consensus across ALL implementations found: WeatherBot, PolySwarm paper ("`f = 0.25 x f*`"), the live trading analysis, and the arbitrage bot (which uses fixed sizing that implicitly operates below quarter-Kelly via small order caps). At quarter-Kelly, the probability of ruin over 1,000 trades approaches zero even with significant edge estimation error. At full Kelly, a 20% overestimate of your edge leads to negative expected log-wealth. Quarter-Kelly survives a 75% overestimate.

### Why Two Monitoring Loops

WeatherBot runs `monitor_positions()` every 10 minutes and `scan_and_update()` every 60 minutes. The arbitrage bot mirrors this with `_monitor_order_timeouts()` checking every 10 seconds while the main arb detection loop runs at its own cadence. This is not redundant — it reflects a fundamental priority hierarchy:

**Position protection is more urgent than opportunity discovery.** A stop-loss that triggers 50 minutes late can destroy a position. A new opportunity discovered 50 minutes late just means a slightly different entry price. The 10-minute monitor checks ONLY existing positions against stop/trailing/take-profit levels. The 60-minute scan does the expensive work: fetching forecasts from 3 sources across 20 cities, checking Polymarket events, running calibration.

This is the pattern behind every successful risk system: **defense runs at higher frequency than offense.**

### The Forecast-Change Exit Buffer

Lines 1216-1240 implement the most sophisticated exit in the WeatherBot codebase. It doesn't just check "is forecast still in our bucket?" — it applies a 2-degree buffer (Fahrenheit) or 1-degree (Celsius) to prevent whipsawing on small fluctuations:

```python
buffer = 2.0 if unit == "F" else 1.0
mid_bucket = (old_bucket_low + old_bucket_high) / 2
forecast_far = abs(forecast_temp - mid_bucket) > (abs(mid_bucket - old_bucket_low) + buffer)
```

The exit only fires when BOTH conditions are true: forecast has left the bucket AND the new forecast is meaningfully far from the bucket midpoint. This prevents the scenario where a forecast oscillates between 67 and 68 degrees, which could trigger repeated exits and re-entries (churning through fees and slippage).

### Time-Horizon Take-Profit: Why It Changes

The take-profit thresholds in `monitor_positions()` encode a deep insight about prediction market dynamics:

- **48h+ to resolution**: Take profit at $0.75 — you're exposed to significant forecast uncertainty over 2+ days. Lock in gains when available.
- **24-48h**: Take profit at $0.85 — forecast is more reliable, hold for higher price.
- **<24h**: No take-profit, hold to resolution — with hours left, the forecast is highly accurate and the contract will converge to $1.00 or $0.00. Taking profit at $0.85 sacrifices the final $0.15 when you have the highest confidence.

This is the inverse of what most traders do. Most traders take profits too early (fear of loss) and hold losers too long (hope of recovery). The weatherbot does the opposite: it holds LONGER when it has MORE information, and exits FASTER when uncertainty is high.

### The v2-to-v3 Insight: One Change, 7x Improvement

Live v2 lost 49.5%. Live v3 lost 13%. The primary change: **longer lookback windows for momentum signals.** V2 weighted 65% of its signal on the final 60 seconds. V3 rebalanced to favor 120s and 240s lookbacks.

What this reveals about risk: **short-term signals in thin markets are noise, not edge.** The 60-second window captured "transient micro-bounces that reverted by window close." The signal was real but too noisy to trade profitably after execution costs. The risk management lesson: your signal quality IS your risk management. A bad signal with perfect stops still loses money — it just loses it slower.

### The RiskManager as Sequential Gate vs Parallel Check

The polymarket-arbitrage `RiskManager.check_order()` is designed as a SEQUENTIAL chain, not parallel checks. This matters:

- **Check 1 (kill switch) is first** because it's O(1) and catches the most critical state
- **Checks 2-4 (blacklist/whitelist/volume) are cheap filters** that eliminate obviously bad orders
- **Checks 5-6 (exposure limits) compute projected state** — more expensive but necessary
- **Checks 7-8 (loss/drawdown) trigger the kill switch** — they don't just reject the order, they CHANGE STATE permanently

The `update_pnl()` method also independently checks loss and drawdown limits, meaning the kill switch can trigger even between orders (during portfolio mark-to-market). This dual-trigger design prevents the edge case where PnL deteriorates between order validations.

### The PolySwarm Uncertainty Gate

The PolySwarm paper uses a standard deviation filter: swarm disagreement must be below 30% to enter a trade. This is a risk control masquerading as a trade filter. When 25 LLM agents strongly disagree, the edge estimate is unreliable. High disagreement = uncertain edge = don't bet. The filter prevents the most dangerous trades: those where your confidence is high but your confidence IS WRONG.

### Cross-Platform Fee Accounting as Risk Control

The arbitrage bot's `CrossPlatformArbEngine` calculates net edge after ALL costs:
```
gross = sell_price - buy_price
fees = (buy_price * buy_platform_taker_fee + sell_price * sell_platform_taker_fee + gas_cost * 2)
net = gross - fees
```

With Polymarket taker fee at 1.5% and Kalshi at ~1%, plus $0.02 gas per order (x2 for both legs), the minimum gross edge must be ~3.5% to clear the fee hurdle. The 2% `min_edge` threshold on net edge means the bot requires ~5.5% gross price discrepancy between platforms. This explains why cross-platform arbitrage is "rare and fleeting" — markets are efficient enough that 5.5% discrepancies close within seconds.

---

## LAYER 3: SIGNATURE MOVES — The Patterns That Separate Survivors from Casualties

### Signature Move 1: Layered Position Sizing with Hard Caps

Every profitable system found uses the same architecture: probabilistic sizing (Kelly) PLUS absolute caps. Never just Kelly. Never just fixed sizing. The layers:

1. **Kelly fraction** — scales position to edge strength
2. **Absolute cap** — prevents catastrophic single-trade loss
3. **Price ceiling** — avoids expensive contracts with unfavorable risk/reward
4. **Volume floor** — ensures liquidity for entry AND exit

WeatherBot implements all four. PolySwarm implements the first three. The arbitrage bot uses fixed sizing ($5 default, $10 max) which is even MORE conservative — effectively operating at a tiny fraction of Kelly. The 92.4% who lose money? They use full Kelly (overleveraged), no caps (one bad trade = ruin), and trade in illiquid markets (can't exit when they need to).

### Signature Move 2: Multiple Simultaneous Exit Mechanisms

WeatherBot runs FIVE exit mechanisms in parallel:
1. **Stop-loss** (price-based, 20% drawdown)
2. **Trailing stop** (moves to breakeven at +20%)
3. **Take-profit** (time-horizon dependent)
4. **Forecast-change exit** (fundamental signal invalidation with buffer)
5. **Resolution** (hold to market close)

The arbitrage bot adds a sixth:
6. **Order timeout** (`_monitor_order_timeouts()` cancels unfilled orders after 60 seconds)

The poly-maker adds three more:
7. **Compound stop-loss** (PnL below threshold AND spread narrow enough to exit)
8. **Volatility exit** (3-hour volatility exceeds threshold — sell regardless of PnL)
9. **Risk-off cooldown** (after stop/volatility exit, no new buys for `sleep_period` hours)

These are NOT redundant — they protect against different failure modes:
- Stop-loss: "I was wrong about this trade"
- Trailing: "I was right but the edge is closing"
- Take-profit: "I have enough profit to justify exiting uncertainty"
- Forecast-change: "The world changed — my thesis is invalid"
- Resolution: "I was right and the market confirmed it"
- Order timeout: "The market moved and my order is stale/dangerous"
- Compound stop: "I'm losing AND the market is liquid enough to exit cleanly"
- Volatility exit: "The market is too chaotic to hold any position"
- Risk-off cooldown: "I just got burned — don't re-enter immediately"

Most losing traders have ONE exit mechanism (or none). Every additional exit mechanism reduces the probability of catastrophic loss.

### Signature Move 3: Calibration-Driven Parameter Adjustment

The `run_calibration()` function in WeatherBot recalculates sigma (forecast uncertainty) per city per source using Mean Absolute Error on resolved markets. This means the bot's risk parameters are ALIVE — they evolve based on actual performance data.

```python
for source in ["ecmwf", "hrrr", "metar"]:
    for city in set(m["city"] for m in resolved):
        errors = [abs(snap["temp"] - m["actual_temp"]) for ...]
        if len(errors) >= CALIBRATION_MIN:  # minimum 30 data points
            new_sigma = sum(errors) / len(errors)
```

When ECMWF is consistently 3 degrees off for Tokyo, the sigma adjusts from the default 1.2C to 3.0C. This widens the probability distribution, REDUCING position sizes for Tokyo ECMWF trades because the estimated edge is smaller with higher uncertainty.

This is the prediction market version of Bayesian updating: the system gets smarter about its own limitations over time.

### Signature Move 4: The Kill Switch as One-Way State Machine

The arbitrage bot's `RiskManager` implements the kill switch as a permanent state change, not a toggle:

```python
def _trigger_kill_switch(self, reason):
    self.state.kill_switch_triggered = True
    self.state.kill_switch_reason = reason
    logger.critical(f"KILL SWITCH TRIGGERED: {reason}")
```

Once triggered, there is NO automatic recovery. Every subsequent `check_order()` call hits the kill switch check FIRST and returns False immediately. The `auto_unwind_on_breach` flag is False by default — even EXISTING positions are not automatically liquidated. This is deliberate: automatic unwinding during market stress can lock in losses that would have recovered. The kill switch says "stop digging" without saying "fill in the hole at the worst possible price."

Recovery requires human review: diagnose the trigger, review parameters, manually reset state. This mirrors the circuit breaker pattern in traditional exchanges.

### Signature Move 5: Compound Stop-Loss Triggers (Poly-Maker)

The poly-maker stop-loss is the most sophisticated found across all sources because it uses a COMPOUND trigger — not just "price dropped X%":

```python
if (pnl < params['stop_loss_threshold'] and spread <= params['spread_threshold']) or row['3_hour'] > params['volatility_threshold']:
```

This fires when EITHER:
- **PnL is below threshold AND spread is narrow enough to execute** (prevents selling into wide spreads where you'd get crushed on slippage)
- **3-hour volatility exceeds threshold** (market is too chaotic to hold positions regardless of PnL)

After triggering, the bot enters a **risk-off cooldown period**:
```python
risk_details['sleep_till'] = str(pd.Timestamp.utcnow() + pd.Timedelta(hours=params['sleep_period']))
```

During cooldown, NO new buy orders are placed for that market. This prevents the revenge-trading pattern where a bot immediately re-enters a losing position. The cooldown is PER-MARKET (stored in `positions/{condition_id}.json`), so one volatile market doesn't shut down the entire bot.

Additionally, the bot merges YES+NO positions to recover collateral: when you hold both sides, merging converts them back to USDC. This is free capital recovery that most bots miss entirely.

### Signature Move 6: Smart Order Cancellation

The poly-maker only cancels and replaces orders when the change is MATERIAL:
```python
should_cancel = (
    price_diff > 0.005 or
    size_diff > order['size'] * 0.1 or
    existing_buy_size == 0
)
```

If price drifted by less than half a cent AND size changed by less than 10%, the existing order stays. This reduces:
- API calls (staying within rate limits)
- Cancel-replace latency (keeping your place in the queue)
- Gas costs (fewer on-chain transactions)

This is the opposite of the naive approach (cancel and replace on every tick), which burns through rate limits and creates windows of zero exposure.

### Signature Move 7: Position Monitoring at Higher Frequency Than Opportunity Scanning

As detailed in Layer 2: WeatherBot defense runs at 6x the frequency of offense (10 min vs 60 min). The arbitrage bot's `_monitor_order_timeouts()` runs every 10 seconds while arb detection operates at its own cadence. PolySwarm's 5-second scan loop prioritizes risk checks before new trade evaluation. The live trading analysis that improved from v2 to v3 did so partly by adding a "hard rule blocking signals opposing 10-minute trend" — a risk check that runs on every signal before it can become a position.

---

## LAYER 4: STRATEGIC ARCHITECTURE — The Three-Tier Risk Model

### Tier 1: Per-Trade Risk

Every individual trade must pass through:
- **Edge estimation** (Kelly math with calibrated sigma, or fee-adjusted net edge for arbitrage)
- **Position sizing** (quarter-Kelly with MAX_BET cap, or fixed sizing with max_order_size)
- **Entry filters** (MIN_EV, MAX_PRICE, MIN_VOLUME, MAX_SLIPPAGE, MIN_HOURS, MAX_HOURS)
- **8-check validation chain** (kill switch, blacklist, whitelist, volume, per-market exposure, global exposure, daily loss, drawdown)
- **Exit plan** (stop-loss placed at entry, trailing stop armed, take-profit threshold set by time horizon, order timeout)

### Tier 2: Per-Strategy Risk

Each strategy type has its own risk envelope:
- **Weather trading**: Capped by MAX_BET per trade, 20 cities diversify geographic risk, calibration adjusts per city
- **AI ensemble probability**: Uncertainty filter (swarm std dev < 30%), minimum 5% divergence from market price
- **Market making**: Inventory caps (never >30% exposure on one side), spread widening during volatility, disabled in efficient markets (`mm_enabled: false` in arb bot config). Poly-maker adds: compound stop-loss (PnL + spread + volatility), risk-off cooldown period per market, position merging for collateral recovery, smart order cancellation to minimize API churn, price range guard ($0.10-$0.90)
- **Cross-platform arbitrage**: Size limited by `min(buy_liquidity, sell_liquidity, $100)`, fee-adjusted edge must clear ~5.5% gross threshold
- **Latency arbitrage**: Time-based exits, execution speed monitoring (if latency degrades, stop trading)

### Tier 3: Portfolio-Level Risk

The portfolio wraps all strategies:
- **10% max capital per market** (WeatherBot implicit via MAX_BET/$10K ratio; arbitrage bot explicit via `max_position_per_market`)
- **5% daily drawdown circuit breaker** — pauses ALL trading across ALL strategies
- **30% correlation rebalance threshold** — if strategies become correlated, reduce exposure
- **Global exposure ceiling** ($50 conservative, $5,000 standard — hard reject at ceiling)
- **Kill switch as portfolio-level emergency brake** — one-way trigger, manual recovery only
- **Capital rotation** — exit closed spreads, rotate to new opportunities (capital doesn't sit idle)

### The Two-Layer Security Architecture

From the Polymarket Agents framework: "LLM proposes, code validates." The AI agent identifies opportunities and suggests trades. Deterministic code validates every parameter before execution. The arbitrage bot's architecture makes this concrete: the arb engine DETECTS opportunities, but the execution engine passes every signal through `RiskManager.check_order()` before any API call is made. This prevents:
- Hallucinated edges (LLM confidently asserts false probability)
- Size errors (LLM suggests position larger than risk limits)
- Invalid orders (code catches API validation issues before submission)
- Stale signals (slippage validation compares signal price vs current market)

This is not a nice-to-have. It's existential. LLMs hallucinate. When an LLM hallucinates in a trading context, the result is real money lost.

---

## LAYER 5: DEEP MEANING — The Paper-to-Live Gap as Centerpiece

### The Most Important Finding in Prediction Market Trading

**Simulation: 522x returns. Live v2: -49.5%. Live v3: -13%.**

This is not an anomaly. This is the norm. Every backtest lies because it cannot capture:

1. **Execution fees**: Polymarket's fee formula `fee = C * feeRate * p * (1-p)` peaks at 50% probability. A crypto trade at $0.50 costs 1.8% in fees alone. The backtest assumed zero fees. The arbitrage bot's explicit fee accounting (1.5% Polymarket taker + 1% Kalshi taker + $0.04 gas round-trip) shows the real friction.

2. **Slippage on thin order books**: The backtest assumes you get the displayed price. In reality, 2-4 cent slippage is normal. The arbitrage bot enforces 2-cent slippage tolerance — orders outside this are rejected (`slippage_rejections` tracked in `ExecutionStats`).

3. **Market impact**: Your own trades move the price. A $5,000 bet in a thin market can move the price 5-10 cents against you. The backtest assumed infinite liquidity. The arbitrage bot caps cross-platform trades at `min(buy_liquidity, sell_liquidity, $100)` to minimize impact.

4. **Latency**: Between signal generation and order execution, the price moves. In latency arbitrage, the window compressed from 12.3 seconds (2024) to 2.7 seconds (2026). By the time your order lands, the edge may be gone. The arb engine tracks "opportunity lifespan" in duration buckets (<100ms, 500ms, 1s, etc.) to measure this.

5. **Adversarial environment**: Other bots are competing for the same edges. Some bots front-run your orders. The backtest assumed you were the only trader.

### What Separates the 7.6% from the 92.4%

From the 50,000+ wallet analysis, losing wallets share these patterns:
- **Full Kelly sizing** (or larger) — one bad streak wipes them out
- **No stop-losses** — they hold losers hoping for recovery
- **Paper results = live expectations** — they deploy capital based on backtest returns
- **Single strategy** — when the edge decays, they have nothing to fall back on
- **Inconsistent risk management** — humans underperform bots by 18% using identical strategies due to emotional interference with sizing and exits

The 7.6% that profit:
- **Quarter-Kelly** with hard caps
- **Automated exits** — stops execute without human interference
- **Paper-to-live graduation** — they test with real (tiny) money before scaling
- **Multi-strategy** — when arbitrage dies, they rotate to market making or AI probability
- **Bot-assisted execution** — the bot doesn't panic, doesn't revenge-trade, doesn't override stops

### Platform Risk as Existential Threat

Fee changes killed latency arbitrage overnight. When Polymarket adjusted crypto fees to 0.072, strategies that relied on thin spreads became unprofitable instantly. The traders who survived had already diversified across strategies and market types (sports fees are 0.03, geopolitical fees are 0). Platform risk is not "something that might happen" — it's the primary risk. The platform IS the market.

The heartbeat protocol is the clearest example: miss one 10-second heartbeat and ALL your open orders are cancelled. If those orders are the short side of a market-making position, you're suddenly exposed to unlimited directional risk. One network hiccup, one server restart, one Cloudflare throttle — and your risk model is invalidated.

---

## LAYER 6: EXEMPLAR ANALYSIS

### Exemplar 1: The WeatherBot Position Management Trifecta

The `monitor_positions()` function (lines 1503-1590) is the clearest example of production-grade risk management in prediction markets. In 87 lines of Python, it implements:

- Real-time price fetching with fallback to cached prices
- Trailing stop activation (breakeven at +20%)
- Time-horizon-dependent take-profit (no profit-taking <24h, $0.85 at 24-48h, $0.75 at 48h+)
- Stop-loss check with separate loss classification (stop_loss vs trailing_stop)
- Balance update and state persistence after any closure

The key design choice: it fetches `bestBid` (not midpoint or last trade) for exit pricing. This means it evaluates what you'd ACTUALLY get if you sold right now — not the theoretical midpoint. This is the difference between paper risk management and real risk management.

### Exemplar 2: The 8-Check Validation Chain (Arbitrage Bot)

The `RiskManager.check_order()` method is the most complete pre-trade risk gate found across all sources. The sequential design means:

1. **Cheapest checks first** (kill switch = one boolean check)
2. **Progressively more expensive** (exposure calculations require summing positions)
3. **State-changing checks last** (daily loss and drawdown can trigger kill switch — you want to be sure the order would have passed every other check before triggering an irreversible state change)

The dual-trigger pattern (kill switch triggered in both `check_order()` AND `update_pnl()`) means the system catches deteriorating conditions even when no new orders are being submitted. A portfolio losing money while idle still hits the kill switch.

### Exemplar 3: The Paper-to-Live Degradation Quantification

Jung-Hua Liu's live trading analysis is the only honest accounting of paper-to-live degradation found across all sources:

| Metric | Simulation | Live v2 | Live v3 |
|--------|-----------|---------|---------|
| Return | 522x | -49.5% | -13% |
| Win Rate | ~53%+ | 25-27% | ~50% |
| Key Flaw | N/A | 65% weight on 60s window | Improved lookbacks |
| Fee Impact | Ignored | 1.56% per round-trip | Same |
| Slippage | Ignored | 2-4 cents | Same |

The v2-to-v3 improvement came from ONE change: longer lookback windows. This reduced noise but did NOT eliminate the paper-to-live gap. Even v3 lost 13%. The lesson: expect 80-95% degradation from paper to live, and size your live deployment accordingly.

### Exemplar 4: The Heartbeat as Infrastructure Kill Switch

From Polymarket docs: "If a valid heartbeat is not received within 10 seconds (with a 5-second buffer), all open orders are cancelled."

This is not a feature — it's an existential risk. For a market maker with 50 open orders providing two-sided liquidity, a missed heartbeat means:
- All 50 orders cancelled simultaneously
- If one side was already filled, you have unhedged directional exposure
- Re-posting orders takes time, during which you can't capture spread
- If the cancel-all rate limit (250/10s) throttles your recovery, you're exposed even longer

The arbitrage bot's `monitoring.heartbeat_interval: 30` (seconds) is for its own internal health check — distinct from Polymarket's mandatory 10-second WebSocket heartbeat for order management.

### Anti-Exemplar: The 92.4% Pattern

The composite failure mode of unprofitable wallets:

1. **Find a "working" strategy in backtest** (522x returns!)
2. **Deploy with full Kelly sizing** ($1,000 bet on a $5,000 account)
3. **First few trades win** (confirmation bias: "the system works!")
4. **Inevitable drawdown begins** (market conditions shift)
5. **Override stops or never set them** ("it'll come back")
6. **Increase size to recover losses** (revenge trading, anti-Kelly)
7. **Single catastrophic loss** (one trade wipes 30%+ of account)
8. **Tilt trading** (emotional entries, no edge calculation)
9. **Account depleted** (join the 92.4%)

Every step in this cascade could be prevented by the systems described in this extraction. But every step REQUIRES automation to prevent — humans don't reliably execute risk management under stress. The arbitrage bot's key warnings section says it plainly: "Always start in dry-run mode before live trading. Begin with minimal capital ($50-100). Monitor actively; don't leave unattended."

---

## CROWN JEWEL PROMPTS

### Prompt 1: Position Size Calculator

```
You are a prediction market position sizing engine. Given the following inputs, calculate the exact position size using the full Kelly framework with all safety caps applied.

INPUTS:
- Edge estimate (your probability): [p]
- Market price (ask): [price]
- Current bankroll: [bankroll]
- Strategy type: [weather|ai_ensemble|market_making|arbitrage|cross_platform]
- Kelly fraction: [default 0.25]
- Max bet: [default $20]
- Max price: [default $0.45]
- Min EV threshold: [default 0.10]
- Max position per market: [default 10% of bankroll]

CALCULATION CHAIN (show every step):

1. ODDS RATIO: b = (1/price) - 1
2. FULL KELLY: f* = (p * b - (1 - p)) / b
3. FRACTIONAL KELLY: f = kelly_fraction * max(0, f*)
4. RAW BET: raw = f * bankroll
5. EXPECTED VALUE: EV = p * (1/price - 1) - (1 - p)
6. FEE IMPACT: Calculate fee using Polymarket formula: fee = shares * feeRate * price * (1 - price)
   - Sports feeRate: 0.03
   - Crypto feeRate: 0.072
   - Geopolitical feeRate: 0 (exempt)
   For cross-platform: add buy_platform_fee + sell_platform_fee + gas_cost * 2
7. NET EV: EV after fees and estimated slippage (2-4 cents)
8. POSITION SIZE: min(raw, max_bet, max_position_per_market)

GATE CHECKS (any failure = NO TRADE):
- [ ] Price < max_price (0.45)?
- [ ] EV > min_ev (0.10)?
- [ ] Net EV (after fees + slippage) > 0?
- [ ] Position size >= $0.50 minimum?
- [ ] Position would be < max_position_per_market?
- [ ] Global exposure after this trade < max_global_exposure?
- [ ] Daily P&L still above -max_daily_loss?
- [ ] Current drawdown still below max_drawdown_pct?

OUTPUT FORMAT:
- Position size: $X.XX
- Shares: X.XX (size / price)
- Expected value per dollar: +X.XX
- Fee cost: $X.XX
- Net expected profit: $X.XX
- Risk of total loss on this trade: $X.XX (position size)
- Gate check results: PASS/FAIL with details

WORKED EXAMPLE:
p=0.80, price=$0.10, bankroll=$10,000, sports market
b = 9, f* = 0.778, f = 0.194, raw = $1,944
But MAX_BET = $20, so position = $20
Shares = 200
EV = 0.80 * 9 - 0.20 = 7.00 per dollar risked
Fee = 200 * 0.03 * 0.10 * 0.90 = $0.54
200 shares * $1.00 payout * 80% - $20 cost - $0.54 fee = $139.46 expected profit
Gate: All pass. TRADE.
```

### Prompt 2: Portfolio Risk Dashboard

```
You are a prediction market portfolio risk auditor. Analyze the current portfolio state across all active strategies and produce a comprehensive risk report.

PORTFOLIO STATE (fill in current data):
Strategy 1 - [Name]:
  - Active positions: [count]
  - Total capital deployed: $[amount]
  - Current P&L: $[amount]
  - Markets: [list market IDs or descriptions]

Strategy 2 - [Name]: [same format]
Strategy 3 - [Name]: [same format]

ANALYSIS REQUIRED:

1. CONCENTRATION RISK
   For each position, calculate: position_size / total_bankroll * 100%
   Flag any position > max_position_per_market (VIOLATION — would fail Check 5)
   Flag any strategy > 40% of bankroll (WARNING)
   Flag global exposure > max_global_exposure (VIOLATION — would fail Check 6)

2. CORRELATION MATRIX
   Identify correlated positions:
   - Same underlying event (e.g., two weather markets on the same city)
   - Same category (e.g., all sports, all crypto)
   - Same resolution timeframe (clustering of exits)
   - Same platform (Polymarket vs Kalshi — platform failure correlation)
   - Directional correlation (all positions benefit from same market move)
   If aggregate correlated exposure > 30%, flag for rebalancing.

3. PLATFORM RISK INDICATORS
   - Total open orders (approaching rate limits? 3,500/10s for orders)
   - Heartbeat health (any recent misses? Last successful heartbeat timestamp?)
   - Time since last matching engine restart (next Tuesday 7 AM ET risk)
   - Fee regime exposure (what % of positions are in crypto [0.072] vs sports [0.03] vs geopolitical [0]?)
   - Kill switch status: triggered? reason?

4. DRAWDOWN ANALYSIS
   - Current drawdown from peak: (peak_pnl - current_pnl) / peak_pnl * 100%
   - Daily P&L: current session total
   - Distance to kill switch: max_daily_loss - abs(daily_pnl)
   - Distance to drawdown trigger: max_drawdown_pct - current_drawdown
   - Estimated worst-case loss if ALL positions hit stop-loss simultaneously

5. STRATEGY HEALTH
   For each strategy, calculate:
   - Win rate (last 20 trades)
   - Average P&L per trade
   - Sharpe ratio estimate: avg_return / std_dev_return
   - Edge decay indicator: is win rate trending down over last 50 trades?
   - Opportunity frequency: are opportunities becoming rarer? (arb window compression)

OUTPUT FORMAT:
## PORTFOLIO RISK DASHBOARD
- Total bankroll: $X
- Deployed capital: $X (X% of bankroll)
- Global exposure utilization: X% of max
- Unrealized P&L: $X
- Drawdown from peak: X%
- Kill switch distance: $X daily loss / X% drawdown

## 8-CHECK GATE STATUS
- Kill switch: [CLEAR/TRIGGERED: reason]
- Blacklist: [X markets blacklisted]
- Volume filter: [X markets below threshold]
- Per-market exposure: [highest utilization: X% of max in market Y]
- Global exposure: [X% of max]
- Daily loss: [X% of limit consumed]
- Drawdown: [X% of limit consumed]

## ALERTS (if any)
- [RED] Concentration violation: [details]
- [YELLOW] Correlation warning: [details]
- [RED] Edge decay detected: [strategy]
- [RED] Kill switch imminent: [metric at X% of trigger]

## RECOMMENDATIONS
- [specific action items with reasoning]
```

### Prompt 3: Kill Switch Configuration

```
You are a prediction market risk engineer designing a 3-level kill switch system. For each level, specify exact trigger conditions, automated actions, recovery procedures, and test protocol.

REFERENCE IMPLEMENTATIONS:
- Arbitrage bot: Single-level kill switch (daily loss OR drawdown triggers, no auto-recovery, manual reset)
- WeatherBot: No explicit kill switch but implicit via balance depletion
- PolySwarm: Daily loss limits suspend trading
- Sovereign analysis: 5% daily drawdown pauses all trading

CONTEXT:
- Platform: Polymarket (CLOB API) + optionally Kalshi
- Heartbeat: 10-second window, 5-second buffer
- Rate limits: 3,500 orders/10s, cancel-all 250/10s
- Matching engine restarts: Tuesdays 7 AM ET
- Error codes: 503 (trading disabled), 425 (engine restarting), 429 (rate limited)

DESIGN THE THREE LEVELS:

## LEVEL 1: YELLOW — Reduced Operations
Trigger conditions (ANY of):
- Daily P&L reaches -50% of max_daily_loss (warning threshold)
- Single position loss exceeds 2x expected max loss
- API error rate exceeds 5% of requests in last 10 minutes
- Heartbeat response time exceeds 7 seconds (approaching 10s timeout)
- Win rate drops below 40% over last 10 trades
- Global exposure exceeds 70% of max_global_exposure

Automated actions:
- Reduce all new position sizes by 50% (halve max_bet / max_order_size)
- Widen all market-making spreads by 2x
- Increase position monitoring frequency (10 min -> 5 min / 10s -> 5s)
- Log alert with full RiskState snapshot
- Set `level = "YELLOW"` in state

Recovery to GREEN:
- All trigger conditions clear for 30+ minutes
- No new alerts in recovery window
- Automatic (no manual approval needed)

## LEVEL 2: ORANGE — New Positions Halted
Trigger conditions (ANY of):
- Daily P&L reaches -80% of max_daily_loss
- Drawdown reaches 75% of max_drawdown_pct
- HTTP 503 received (trading disabled / cancel-only mode)
- HTTP 425 received (matching engine restart)
- Two or more positions hit stop-loss in same 30-minute window
- Consecutive losing trades >= 5

Automated actions:
- Halt ALL new position entry across all strategies (check_order returns False for new orders)
- Existing positions: stops remain active, no modifications
- Cancel all resting limit orders (market-making inventory)
- Begin exponential backoff on API requests (1s, 2s, 4s, 8s)
- Log alert with full state + P&L breakdown per strategy

Recovery to YELLOW:
- HTTP 503/425 resolved (successful API response)
- P&L recovers above -60% of max_daily_loss
- Manual approval required (operator confirms conditions are safe)

## LEVEL 3: RED — Full Emergency Exit
Trigger conditions (ANY of):
- Daily P&L exceeds max_daily_loss (kill switch trigger)
- Drawdown exceeds max_drawdown_pct (kill switch trigger)
- Unable to reach Polymarket API for 5+ minutes
- Heartbeat missed (all orders auto-cancelled by platform)
- Manual trigger (human panic button)

Automated actions:
- Trigger kill_switch (state.kill_switch_triggered = True, permanent until manual reset)
- Cancel ALL open orders via cancel-all endpoint (respect 250/10s rate limit)
- If auto_unwind_on_breach = True: market-sell all positions at best available bid
- If auto_unwind_on_breach = False: positions remain but no new orders
- Log complete state: all positions, P&L, order history, API error logs, kill_switch_reason
- Send notification to operator (Telegram/Discord/email)
- Enter cooldown period: 24 hours minimum

Recovery from RED:
- MANUAL ONLY — no automatic recovery
- Required: root cause analysis document
- Required: parameter review (were limits too loose? too tight?)
- Required: paper trading for minimum 2 days before live re-entry
- Manual state reset: `state.kill_switch_triggered = False`

## TEST PROTOCOL
For each level, describe:
1. Simulate trigger: use dry_run mode with simulated P&L to approach threshold
2. Verify actions: check logs for correct state transitions and order cancellations
3. Test recovery: verify conditions for level downgrade work correctly
4. Test cascading: YELLOW -> ORANGE -> RED escalation in one session
5. Test rate limits: verify emergency exit works within cancel-all 250/10s limit
6. Frequency: full test monthly, individual level tests weekly
```

### Prompt 4: Paper-to-Live Migration Plan

```
You are a prediction market deployment strategist. Take a backtested strategy and produce a realistic degradation estimate plus graduated deployment plan.

BACKTEST RESULTS (fill in):
- Strategy name: [name]
- Strategy type: [weather|ai_ensemble|market_making|arbitrage|cross_platform|momentum]
- Backtest period: [dates]
- Backtest return: [X%]
- Backtest win rate: [X%]
- Backtest max drawdown: [X%]
- Number of trades: [N]
- Average trade size: $[X]
- Average holding period: [X hours]

STEP 1: DEGRADATION ESTIMATE

Apply the Paper-to-Live Degradation Model derived from the Jung-Hua Liu analysis (simulation 522x vs live -49.5%/-13%):

| Factor | Typical Impact | Your Estimate |
|--------|---------------|---------------|
| Execution fees (Polymarket) | -1.5% to -3% per round-trip (crypto: higher, geopolitical: zero) | |
| Cross-platform fees | Additional -1% Kalshi + $0.04 gas round-trip | |
| Slippage | -2 to -4 cents per trade on thin books (arb bot enforces 2c max) | |
| Market impact | -0.5% to -5% depending on size vs liquidity | |
| Latency | -10% to -50% of edge depending on speed | |
| Adversarial competition | -20% to -80% edge decay over 3 months | |
| Signal noise (live vs backtest) | Win rate typically drops 15-30% | |
| Order fill rate | Not all orders fill (arb bot simulates 80% fill probability) | |

REALISTIC RETURN ESTIMATE:
- Optimistic (10th percentile): backtest_return * 0.20 (80% degradation)
- Expected (50th percentile): backtest_return * 0.10 (90% degradation)
- Pessimistic (90th percentile): NEGATIVE (strategy loses money live)

"Expect 80-95% degradation from paper to live. If the strategy is not profitable at 90% degradation, do not deploy."

STEP 2: GRADUATED DEPLOYMENT PLAN

Phase 0 — Paper Trading (2-4 weeks minimum):
- Run strategy with ZERO real capital (`trading_mode: "dry_run"`, `data_mode: "real"`)
- Log every signal, entry, exit, P&L as if real
- Compare paper results to backtest expectations
- GATE: Paper win rate within 10% of backtest? If no, diagnose before proceeding.
- Track opportunity lifespan (how quickly do arb windows close?)

Phase 1 — Micro-Live ($50-$100 capital):
- Deploy with real capital at 1% of target allocation
- MAX_BET: $1 / max_order_size: $2 (absolute cap)
- max_daily_loss: $5 / max_drawdown_pct: 15%
- Purpose: Validate execution pipeline (API auth, order submission, fills, cancellations, heartbeat)
- Duration: Minimum 50 trades or 2 weeks
- GATE: Execution matches paper results within 15%? No API errors? Fills at expected prices? Slippage within tolerance?

Phase 2 — Small-Live ($500-$1,000 capital):
- Deploy at 10% of target allocation
- MAX_BET: $5 / max_order_size: $10
- max_daily_loss: $50 / max_drawdown_pct: 10%
- Purpose: Validate risk management under real conditions
- Duration: Minimum 100 trades or 4 weeks
- GATE: Drawdown within 1.5x backtest max drawdown? Win rate within 20% of backtest? Kill switch never triggered?

Phase 3 — Full Deployment (target capital):
- Deploy at 100% of target allocation
- MAX_BET: target maximum
- Full kill switch configuration (3-level from Prompt 3)
- Monthly review: compare to Phase 2 performance
- GATE: If any month's performance is worse than Phase 2's worst week, scale back to Phase 2

CRITICAL RULES:
- Never skip phases. The 92.4% who lose money skip straight from backtest to full deployment.
- Never increase size during a winning streak. Wait for the FULL phase duration.
- If a phase fails its gate, go BACK one phase, not forward.
- Human traders underperform bots by 18% due to poor sizing and inconsistent risk management. Automate everything that can be automated.
- The arbitrage bot defaults to dry_run for a reason. Respect it.
```

### Prompt 5: Risk Parameter Optimizer

```
You are a prediction market risk parameter tuner. Review historical performance data and recommend specific parameter adjustments.

HISTORICAL DATA (fill in last 30-90 days):
- Total trades: [N]
- Win rate: [X%]
- Average winning trade P&L: $[X]
- Average losing trade P&L: $[X]
- Max drawdown: [X%]
- Kill switch triggers: [count and reasons]
- Current parameters:
  - Kelly fraction: [X] (WeatherBot) or fixed order size: $[X] (arb bot)
  - Max bet / max_order_size: $[X]
  - Min EV threshold / min_edge: [X]
  - Max price: [X]
  - Max slippage / slippage_tolerance: [X]
  - Stop-loss: [X%]
  - Trailing stop activation: [X%]
  - Take-profit thresholds: [X, X, X by time horizon]
  - Max position per market: $[X]
  - Max global exposure: $[X]
  - Max daily loss: $[X]
  - Max drawdown pct: [X%]

ANALYSIS DIMENSIONS:

1. KELLY FRACTION / ORDER SIZE ANALYSIS
   - Calculate actual vs theoretical Kelly for each trade
   - If actual avg position = X% of Kelly recommendation, effective fraction is X
   - If win rate < 50%, REDUCE Kelly fraction (current edge may be overestimated)
   - If win rate > 65%, consider SLIGHT increase (0.25 -> 0.30 max)
   - NEVER exceed 0.33 Kelly regardless of performance
   - For fixed sizing: if max_order_size consistently caps positions, consider raising (if risk budget allows)

2. STOP-LOSS OPTIMIZATION
   - Of trades that hit stop-loss, what % eventually would have been profitable?
   - If > 30% of stopped trades would have won: widen stop (too tight)
   - If < 10% of stopped trades would have won: tighten stop (too loose)
   - Optimal stop = minimize (stopped winners * avg win) - (avoided losses * avg loss saved)

3. TAKE-PROFIT ANALYSIS
   - Of trades that hit take-profit, what was the final resolution price?
   - If > 50% resolved at $1.00 (would have been full win): take-profit is too aggressive
   - If < 20% resolved at $1.00: take-profit is correctly capturing uncertain positions
   - By time horizon: are the thresholds (0.75/0.85/hold) optimal for YOUR strategy?

4. MIN EV / MIN EDGE THRESHOLD
   - Plot win rate vs EV at entry
   - If trades with EV 0.10-0.15 have <45% win rate: raise min_ev to 0.15
   - If trades with EV 0.10-0.15 have >55% win rate: current threshold is fine
   - For cross-platform arb: if most opportunities are found between 2-3% net edge, lower min_edge may capture more volume

5. EXPOSURE LIMIT ANALYSIS
   - How often did max_position_per_market block a trade? (If rarely: limit may be too loose; if often: limit may be preventing good trades)
   - How often did max_global_exposure block a trade?
   - What was the maximum simultaneous exposure actually reached?
   - Are the limits protecting you or just preventing trading?

6. KILL SWITCH CALIBRATION
   - How many times was the kill switch triggered?
   - After each trigger, would continuing to trade have been profitable or not?
   - If kill switch triggered during temporary drawdowns that recovered: limits may be too tight
   - If kill switch triggered before catastrophic losses: limits are correctly calibrated
   - max_daily_loss and max_drawdown_pct should be tight enough to protect but loose enough to survive normal variance

7. SLIPPAGE AND FEE ANALYSIS
   - Compare intended price vs actual fill price across all trades
   - If average slippage > slippage_tolerance: either reduce position sizes or trade more liquid markets
   - Track slippage by market category (crypto [higher fees, thinner books] vs sports [lower fees])
   - Calculate fee drag: total fees paid / total volume traded

8. CALIBRATION CHECK (WeatherBot-specific)
   - Compare forecast sigma per city per source vs actual errors
   - If sigma underestimates errors: positions are oversized (DANGEROUS)
   - If sigma overestimates errors: positions are undersized (leaving money on table, but safe)
   - Always err toward overestimating sigma

OUTPUT FORMAT:
## PARAMETER RECOMMENDATIONS

| Parameter | Current | Recommended | Reason | Confidence |
|-----------|---------|-------------|--------|------------|
| Kelly fraction | 0.25 | [X] | [data-driven reason] | [HIGH/MEDIUM/LOW] |
| Max bet | $20 | $[X] | [reason] | [confidence] |
| Max daily loss | $500 | $[X] | [kill switch analysis] | [confidence] |
| [etc.] | | | | |

## IMPLEMENTATION PRIORITY
1. [Highest-impact change first — usually the one losing the most money]
2. [Second]
3. [Third]

## WARNING: Change ONE parameter at a time. Run for minimum 50 trades before evaluating. Changing multiple parameters simultaneously makes it impossible to attribute improvement or degradation to any specific change.
```

---

## INTEGRATION MAP: How Risk Management Connects Everything

```
                    ┌─────────────────────────────┐
                    │   PORTFOLIO LEVEL            │
                    │   max_global_exposure         │
                    │   5% daily circuit breaker    │
                    │   30% correlation limit       │
                    │   Kill switch (one-way)       │
                    └──────────┬──────────────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         │                     │                     │
┌────────┴───────┐   ┌────────┴───────┐   ┌────────┴────────┐
│ WEATHER STRAT  │   │ AI ENSEMBLE    │   │ CROSS-PLATFORM  │
│ Kelly 0.25     │   │ Kelly 0.25     │   │ Fixed $5-$10    │
│ MAX_BET $20    │   │ StdDev <30%    │   │ min_edge 2%     │
│ 5 exit mechs   │   │ 5% min edge    │   │ $100 size cap   │
│ Calibration    │   │ Multi-model    │   │ Fee accounting  │
└────────┬───────┘   └────────┬───────┘   └────────┬────────┘
         │                     │                     │
         └─────────────────────┼─────────────────────┘
                               │
              ┌────────────────┴──────────────────┐
              │   8-CHECK VALIDATION CHAIN         │
              │   1. Kill switch                   │
              │   2. Blacklist                     │
              │   3. Whitelist                     │
              │   4. Volume minimum                │
              │   5. Per-market exposure            │
              │   6. Global exposure               │
              │   7. Daily loss (-> kill switch)    │
              │   8. Drawdown (-> kill switch)      │
              └────────────────┬──────────────────┘
                               │
                    ┌──────────┴──────────────────┐
                    │   PLATFORM LAYER             │
                    │   Heartbeat (5s send)         │
                    │   Rate limits tracked          │
                    │   HTTP 425/503 handling        │
                    │   Fee-aware sizing             │
                    │   Slippage validation          │
                    │   Order timeout (60s)          │
                    └──────────────────────────────┘
```

---

## OPERATIONAL CHECKLIST: Before Every Trading Session

- [ ] Kill switch status: CLEAR (check `state.kill_switch_triggered`)
- [ ] Heartbeat thread running and responsive (<5s latency)
- [ ] Daily P&L counter reset (or carried from overnight)
- [ ] Current drawdown from peak: ___% (ORANGE at 75% of max, RED at max)
- [ ] Daily loss consumed: ___% of max_daily_loss (ORANGE at 80%, RED at 100%)
- [ ] Largest single position: ___% of bankroll (RED at >max_position_per_market)
- [ ] Global exposure: ___% of max_global_exposure (YELLOW at 70%)
- [ ] Aggregate correlated exposure: ___% (Rebalance at >30%)
- [ ] Next matching engine restart: Tuesday 7 AM ET (is it Tuesday?)
- [ ] API rate limit headroom: ___% remaining in current window
- [ ] Calibration data freshness: last update ___ (stale after 7 days)
- [ ] Paper-to-live performance tracking: current degradation ___% from backtest
- [ ] Order timeout monitor running (cancels stale orders after 60s)
- [ ] Fee regime check: any recent platform fee changes?

---

## KEY CITATIONS INDEX

| Finding | Source | Location |
|---------|--------|----------|
| 92.4% wallets unprofitable | Sovereign Analysis / 50K wallet study | Source 3, Source 5 |
| 522x paper vs -49.5% live | Jung-Hua Liu live trading analysis | Source 9 |
| Quarter-Kelly consensus | WeatherBot + PolySwarm + live analysis | `calc_kelly()`, PolySwarm Section 351 |
| 12.3s -> 2.7s arbitrage compression | Multi-source ecosystem data | Source 3 line 107 |
| 18% human underperformance | 50K wallet comparative analysis | Source 3 line 131 |
| 8-check validation chain | polymarket-arbitrage `risk_manager.py` | `check_order()` method |
| Kill switch auto-trigger on loss/drawdown | polymarket-arbitrage `risk_manager.py` | `update_pnl()` + `_trigger_kill_switch()` |
| RiskConfig defaults ($200/market, $5K global, 10% drawdown) | polymarket-arbitrage `risk_manager.py` | `RiskConfig` dataclass |
| Cross-platform fee accounting | polymarket-arbitrage `cross_platform_arb.py` | `CrossPlatformArbEngine.__init__()` |
| Slippage validation + order timeout | polymarket-arbitrage `execution.py` | `ExecutionEngine` architecture |
| Heartbeat 10s kill switch | Polymarket official docs | Order creation page, line 358 |
| Matching engine Tuesday restart | Polymarket official docs | Matching engine page, line 385 |
| Fee formula `C * feeRate * p * (1-p)` | Polymarket official docs | Fees page, line 182 |
| 5% circuit breaker | Medium/Illumination strategy guide | Source 6 line 298 |
| Calibration via MAE per city | WeatherBot `run_calibration()` | `bot_v2.py` lines 781-809 |
| Forecast-change exit with buffer | WeatherBot `scan_and_update()` | `bot_v2.py` lines 1216-1240 |
| Time-horizon take-profit | WeatherBot `monitor_positions()` | `bot_v2.py` lines 1548-1553 |
| v2->v3 longer lookback improvement | Jung-Hua Liu analysis | Source 9 lines 438-476 |
| PolySwarm uncertainty filter <30% | PolySwarm arXiv paper | Source 7 line 338 |
| Cancel-all rate limit 250/10s | Polymarket official docs | Rate limits page, line 253 |
| "Always start in dry-run mode" | polymarket-arbitrage README | Key Warnings section |
| Opportunity lifespan tracking | polymarket-arbitrage `arb_engine.py` | Duration buckets feature |
| Compound stop-loss (PnL + spread + volatility) | poly-maker `trading.py` | Line 431 |
| Risk-off cooldown period per market | poly-maker `trading.py` | Lines 439-472 |
| Position merging (YES+NO -> USDC recovery) | poly-maker `trading.py` | Lines 312-323 |
| Smart order cancellation (material change threshold) | poly-maker `trading.py` | Lines 221-226 |
| 3-hour volatility threshold blocks buys + triggers sells | poly-maker `trading.py` | Lines 431, 475 |
| Price range guard ($0.10-$0.90) | poly-maker `trading.py` | Line 243 |
| Stale trade cleanup (15s timeout) | poly-maker `main.py` | Line 137 |
| WebSocket-driven real-time orderbook | poly-maker `websocket_handlers.py` | `connect_market_websocket()` |
| Official Polymarket agent framework (auth + trading pipeline) | Polymarket/agents `polymarket.py` | Full class |
