# Prediction Market Risk Management — Genius Context

Deep domain knowledge for cross-strategy risk management in prediction markets. Load this file at Tier 2 when the task requires nuanced risk reasoning, system architecture decisions, parameter tuning, or emergency protocol design.

**Source**: MES 3.0 Deep Extraction — WeatherBot (alteregoeth-ai/weatherbot), Sovereign Trader Analysis, Polymarket Official Docs, Polymarket Arbitrage Bot (ImMike/polymarket-arbitrage), Poly-Maker Market Making Bot (warproxxx/poly-maker), Polymarket Agents Framework (Polymarket/agents). 7,281 lines of source code and documentation.

---

## 1. The Core Truth

**92.4% of Polymarket wallets are unprofitable.** The 7.6% that survive share one trait: they treat risk management as the product, not an afterthought bolted onto strategy. Every edge decays. Arbitrage windows compressed from 12.3 seconds (2024) to 2.7 seconds (2026) to dead. Strategies that printed money in February fail by March. The ONLY durable asset is the system that keeps you alive while edges rotate.

The paper-to-live gap is the single most important finding in prediction market trading: simulation showed 522x returns while live v2 lost 49.5% and live v3 lost 13% using identical signal logic. Every backtest lies. The question is not "will my strategy work?" but "will I survive when it doesn't?"

---

## 2. Kelly Criterion — Why Quarter and Not Full

The Kelly Criterion formula for prediction markets:
```
f* = (p * b - (1 - p)) / b
where b = (1/price) - 1 (the odds ratio)
```

### Worked Example (WeatherBot `calc_kelly()`)
- Forecast probability `p` = 0.80
- Market price = $0.10 (90% underpriced)
- Odds ratio `b` = (1/0.10) - 1 = 9
- Full Kelly: `f* = (0.80 * 9 - 0.20) / 9 = (7.2 - 0.2) / 9 = 0.778`
- Quarter-Kelly: `f = 0.25 * 0.778 = 0.194` (19.4% of bankroll)
- With MAX_BET cap: `min(0.194 * $10,000, $20) = $20`

### The Three-Layer Sizing Defense
1. **Kelly fraction (0.25)** reduces variance by ~75% while sacrificing only ~25% of expected growth rate
2. **MAX_BET ($20)** prevents any single trade from being material — even when Kelly says bet $1,940, actual bet is $20
3. **MAX_PRICE (0.45)** prevents buying expensive contracts where downside overwhelms edge

### Why 0.25 Specifically
Quarter-Kelly is consensus across ALL implementations found: WeatherBot, PolySwarm paper ("`f = 0.25 x f*`"), live trading analysis, and the arbitrage bot (which uses fixed sizing that implicitly operates below quarter-Kelly via small order caps).

The math: At quarter-Kelly, the probability of ruin over 1,000 trades approaches zero even with significant edge estimation error. At full Kelly, a 20% overestimate of your edge leads to negative expected log-wealth. Quarter-Kelly survives a 75% overestimate. The fraction compensates for estimation error, not just variance.

### When to Deviate
- **Higher (0.30 max)**: Only after 200+ validated trades proving calibration accuracy. Even then, NEVER exceed 0.33.
- **Lower (0.10-0.15)**: During micro-live phase, when operating in a new strategy domain, or during periods of unusual market behavior.

---

## 3. The 8-Check Sequential Validation Chain

From polymarket-arbitrage `risk_manager.py`. Every order passes through this sequential gate. ANY failure = order rejected. The sequential design matters — cheapest checks first, state-changing checks last:

| Check | Validates | Failure Action | Cost |
|-------|-----------|----------------|------|
| 1. Kill switch status | `kill_switch_triggered == False` | Reject (trading halted) | O(1) — one boolean |
| 2. Market blacklist | `market_id not in blacklist` | Reject silently | O(1) |
| 3. Whitelist (if set) | `market_id in whitelist` | Reject silently | O(1) |
| 4. 24h volume minimum | `market_volume >= 10,000` | Reject (illiquid) | O(1) |
| 5. Per-market exposure | `projected <= max_position_per_market` | Reject (concentrated) | O(n) — sum positions |
| 6. Global exposure | `projected_global <= max_global_exposure` | Reject (overleveraged) | O(n) — sum all |
| 7. Daily loss limit | `daily_pnl >= -max_daily_loss` | **Reject + TRIGGER KILL SWITCH** | O(1) |
| 8. Drawdown limit | `current_drawdown <= max_drawdown_pct` | **Reject + TRIGGER KILL SWITCH** | O(1) |

**Critical design choices:**
- Checks 7 and 8 don't just reject — they CHANGE STATE permanently by triggering the kill switch
- The `update_pnl()` method also independently checks loss and drawdown limits, meaning the kill switch can trigger even BETWEEN orders (during portfolio mark-to-market)
- This dual-trigger design prevents the edge case where PnL deteriorates between order validations

---

## 4. The Kill Switch as One-Way State Machine

```python
def _trigger_kill_switch(self, reason):
    self.state.kill_switch_triggered = True
    self.state.kill_switch_reason = reason
    logger.critical(f"KILL SWITCH TRIGGERED: {reason}")
```

Once triggered, there is NO automatic recovery. Every subsequent `check_order()` call hits the kill switch check FIRST and returns False immediately. The `auto_unwind_on_breach` flag is False by default — even EXISTING positions are not automatically liquidated.

**Why no auto-unwind**: Automatic unwinding during market stress can lock in losses that would have recovered. The kill switch says "stop digging" without saying "fill in the hole at the worst possible price."

Recovery requires human review: diagnose the trigger, review parameters, manually reset state. This mirrors the circuit breaker pattern in traditional exchanges.

---

## 5. Multiple Simultaneous Exit Mechanisms

WeatherBot runs FIVE exit mechanisms in parallel:
1. **Stop-loss** — price drops 20% from entry (`entry * 0.80`)
2. **Trailing stop** — moves to breakeven when position is +20%
3. **Take-profit** — time-horizon dependent (see below)
4. **Forecast-change exit** — fundamental signal invalidation with 2-degree buffer
5. **Resolution** — hold to market close

The arbitrage bot adds:
6. **Order timeout** — cancels unfilled orders after 60 seconds

The poly-maker adds three more:
7. **Compound stop-loss** — PnL below threshold AND spread narrow enough to exit
8. **Volatility exit** — 3-hour volatility exceeds threshold, sell regardless of PnL
9. **Risk-off cooldown** — after stop/volatility exit, no new buys for `sleep_period` hours (PER MARKET)

**These are NOT redundant — they protect against different failure modes:**
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

---

## 6. Time-Horizon Take-Profit Scaling

From WeatherBot `monitor_positions()`:
- **48h+ to resolution**: Take profit at $0.75 — exposed to significant forecast uncertainty, lock in gains when available
- **24-48h**: Take profit at $0.85 — forecast more reliable, hold for higher price
- **<24h**: No take-profit, hold to resolution — forecast is highly accurate, contract converges to $1.00 or $0.00

This is the INVERSE of what most traders do. Most take profits too early (fear of loss) and hold losers too long (hope of recovery). The weatherbot holds LONGER when it has MORE information, and exits FASTER when uncertainty is high.

---

## 7. Compound Stop-Loss Architecture (Poly-Maker)

The most sophisticated stop-loss found across all sources:

```python
if (pnl < params['stop_loss_threshold'] and spread <= params['spread_threshold']) or row['3_hour'] > params['volatility_threshold']:
```

Fires when EITHER:
- **PnL is below threshold AND spread is narrow enough to execute** (prevents selling into wide spreads where you'd get crushed on slippage)
- **3-hour volatility exceeds threshold** (market too chaotic regardless of PnL)

After triggering, the bot enters a **risk-off cooldown period** (per-market, stored in `positions/{condition_id}.json`):
```python
risk_details['sleep_till'] = str(pd.Timestamp.utcnow() + pd.Timedelta(hours=params['sleep_period']))
```

During cooldown, NO new buy orders for that market. This prevents revenge-trading. One volatile market doesn't shut down the entire bot.

Additionally: position merging (YES+NO -> USDC collateral recovery) — free capital recovery that most bots miss.

---

## 8. Smart Order Cancellation

```python
should_cancel = (
    price_diff > 0.005 or
    size_diff > order['size'] * 0.1 or
    existing_buy_size == 0
)
```

Only cancel and replace when change is MATERIAL (price drift > half cent OR size change > 10%). This reduces API calls (staying within rate limits), cancel-replace latency (keeping queue position), and gas costs. The opposite of naive cancel-and-replace on every tick, which burns through rate limits and creates windows of zero exposure.

---

## 9. Why Two Monitoring Loops

WeatherBot: `monitor_positions()` every 10 minutes, `scan_and_update()` every 60 minutes. The arbitrage bot mirrors this with `_monitor_order_timeouts()` every 10 seconds while arb detection runs at its own cadence.

**Position protection is more urgent than opportunity discovery.** A stop-loss that triggers 50 minutes late can destroy a position. A new opportunity discovered 50 minutes late just means a slightly different entry price.

The universal pattern behind every successful risk system: **defense runs at higher frequency than offense.**

---

## 10. The Paper-to-Live Gap — Deep Analysis

### The Most Important Finding
| Metric | Simulation | Live v2 | Live v3 |
|--------|-----------|---------|---------|
| Return | 522x | -49.5% | -13% |
| Win Rate | ~53%+ | 25-27% | ~50% |
| Key Flaw | N/A | 65% weight on 60s window | Improved lookbacks |
| Fee Impact | Ignored | 1.56% per round-trip | Same |
| Slippage | Ignored | 2-4 cents | Same |

### Why Every Backtest Lies
1. **Execution fees**: Polymarket's fee formula `fee = C * feeRate * p * (1-p)` peaks at 50% probability. A crypto trade at $0.50 costs 1.8% in fees alone.
2. **Slippage on thin order books**: 2-4 cent slippage is normal. Arb bot enforces 2-cent tolerance.
3. **Market impact**: A $5,000 bet in a thin market moves the price 5-10 cents against you.
4. **Latency**: Between signal and execution, price moves. Arb window compressed from 12.3s to 2.7s.
5. **Adversarial environment**: Other bots compete for the same edges. Some front-run your orders.

### The v2-to-v3 Insight
Live v2 lost 49.5%. Live v3 lost 13%. Primary change: **longer lookback windows for momentum signals.** V2 weighted 65% on the final 60 seconds. V3 rebalanced to 120s and 240s lookbacks. Short-term signals in thin markets are noise, not edge. Your signal quality IS your risk management.

### Degradation Model
- Optimistic (10th percentile): backtest_return * 0.20 (80% degradation)
- Expected (50th percentile): backtest_return * 0.10 (90% degradation)
- Pessimistic (90th percentile): NEGATIVE (strategy loses money live)

**If the strategy is not profitable at 90% degradation, do not deploy.**

---

## 11. Gradual Scaling Protocol

| Phase | Duration | Capital | Max Bet | Gate to Advance |
|-------|----------|---------|---------|-----------------|
| Paper | 2-4 weeks | $0 (dry_run mode) | N/A | Win rate within 10% of backtest, no bugs |
| Micro-live | 50+ trades or 2 weeks | $50-$100 | $1-$2 | Execution matches paper within 15%, no API errors |
| Small-live | 100+ trades or 4 weeks | $500-$1,000 | $5-$10 | Drawdown within 1.5x backtest max, win rate within 20% |
| Full deploy | Ongoing | Target capital | Target max | Monthly review vs Phase 2 performance |

**Critical rules:**
- Never skip phases. The 92.4% who lose money skip straight from backtest to full deployment.
- Never increase size during a winning streak. Wait for the FULL phase duration.
- If a phase fails its gate, go BACK one phase, not forward.
- Human traders underperform bots by 18% — automate everything that can be automated.
- The arbitrage bot defaults to dry_run for a reason. Respect it.

---

## 12. Forecast-Change Exit Buffer

Lines 1216-1240 of WeatherBot implement the most sophisticated exit in the codebase:

```python
buffer = 2.0 if unit == "F" else 1.0
mid_bucket = (old_bucket_low + old_bucket_high) / 2
forecast_far = abs(forecast_temp - mid_bucket) > (abs(mid_bucket - old_bucket_low) + buffer)
```

Exit only fires when BOTH conditions are true: forecast has left the bucket AND new forecast is meaningfully far from bucket midpoint. Prevents whipsawing on small fluctuations where a forecast oscillates between 67 and 68 degrees — churning through fees and slippage.

---

## 13. Calibration-Driven Parameter Adjustment

WeatherBot's `run_calibration()` recalculates sigma (forecast uncertainty) per city per source using Mean Absolute Error on resolved markets:

```python
for source in ["ecmwf", "hrrr", "metar"]:
    for city in set(m["city"] for m in resolved):
        errors = [abs(snap["temp"] - m["actual_temp"]) for ...]
        if len(errors) >= CALIBRATION_MIN:  # minimum 30 data points
            new_sigma = sum(errors) / len(errors)
```

When ECMWF is consistently 3 degrees off for Tokyo, sigma adjusts from default 1.2C to 3.0C. This widens the probability distribution, REDUCING position sizes because estimated edge is smaller with higher uncertainty. The prediction market version of Bayesian updating.

---

## 14. PolySwarm Uncertainty Gate

Standard deviation filter: swarm disagreement must be below 30% to enter a trade. When 25 LLM agents strongly disagree, the edge estimate is unreliable. High disagreement = uncertain edge = don't bet. This prevents the most dangerous trades: those where your confidence is high but your confidence IS WRONG.

---

## 15. Cross-Platform Fee Accounting

The arbitrage bot's `CrossPlatformArbEngine` calculates net edge after ALL costs:
```
gross = sell_price - buy_price
fees = (buy_price * buy_platform_taker_fee + sell_price * sell_platform_taker_fee + gas_cost * 2)
net = gross - fees
```

With Polymarket taker at 1.5% and Kalshi at ~1%, plus $0.02 gas per order (x2 for both legs), minimum gross edge must be ~3.5% to clear fees. The 2% `min_edge` on net means the bot requires ~5.5% gross discrepancy. This explains why cross-platform arbitrage is "rare and fleeting."

Cross-platform size cap: `min(buy_liquidity, sell_liquidity, $100)` — prevents market impact on thin books.

---

## 16. Platform Risk as Existential Threat

### Fee Changes Kill Strategies Overnight
When Polymarket adjusted crypto fees to 0.072, strategies relying on thin spreads became instantly unprofitable. Survivors had already diversified across strategy types and market categories (sports 0.03, geopolitical 0).

### The Heartbeat Protocol
From Polymarket docs: "If a valid heartbeat is not received within 10 seconds (with a 5-second buffer), all open orders are cancelled."

For a market maker with 50 open orders: missed heartbeat = all 50 cancelled = if one side already filled, unhedged directional exposure = if cancel-all rate limit (250/10s) throttles recovery, exposed even longer. One network hiccup, one server restart, one Cloudflare throttle — and your risk model is invalidated.

The arb bot's `monitoring.heartbeat_interval: 30` is its own internal health check, distinct from Polymarket's mandatory 10-second WebSocket heartbeat.

### Matching Engine Restarts
Tuesdays 7 AM ET, ~90 seconds downtime. HTTP 425 during restart. Exponential backoff (1-2s, doubling). Detect 425 vs permanent failure. Trading disabled (HTTP 503) = cancel-only mode still works.

---

## 17. The Two-Layer Security Architecture

**Layer 1 — LLM Reasoning**: Receives market data, generates probability estimates, proposes trades. Has NO access to API keys, wallet credentials, or order execution functions.

**Layer 2 — Deterministic Execution**: Receives proposals from Layer 1. Validates against ALL risk rules. Rejects violations with no override mechanism from Layer 1. Executes valid proposals. Logs everything.

This prevents:
- Hallucinated edges (LLM confidently asserts false probability)
- Size errors (LLM suggests position larger than risk limits)
- Invalid orders (code catches API validation issues before submission)
- Stale signals (slippage validation compares signal price vs current market)
- Prompt injection (worst outcome = bad proposal, which Layer 2 rejects)

This is not a nice-to-have. It is existential.

---

## 18. Capital Rotation vs Hold-to-Resolution

Most positions lock capital until resolution. But prediction market edges are front-loaded — the biggest price movement happens shortly after signal identification.

**The rotation principle**: Exit when spread between entry and current has captured >70% of original expected value. Rotate capital into next opportunity.

**Annualized impact example**:
- Hold-to-resolution: $20 makes $3 in 3 days = ~18% over 3 days
- Capital rotation: $20 makes $2.10 (70% of edge) in 6 hours, redeploys 4 times = $8.40 on same $20

**When NOT to rotate**: Exiting costs more in fees + slippage than remaining expected value. Market is illiquid and exit would cross a wide spread.

---

## 19. The Anti-Exemplar: The 92.4% Pattern

The composite failure cascade of unprofitable wallets:
1. Find a "working" strategy in backtest (522x returns!)
2. Deploy with full Kelly sizing ($1,000 bet on $5,000 account)
3. First few trades win (confirmation bias: "the system works!")
4. Inevitable drawdown begins (market conditions shift)
5. Override stops or never set them ("it'll come back")
6. Increase size to recover losses (revenge trading, anti-Kelly)
7. Single catastrophic loss (one trade wipes 30%+ of account)
8. Tilt trading (emotional entries, no edge calculation)
9. Account depleted (join the 92.4%)

Every step requires automation to prevent — humans don't reliably execute risk management under stress. The arb bot's key warning: "Always start in dry-run mode before live trading. Begin with minimal capital ($50-100). Monitor actively; don't leave unattended."

---

## 20. Integration Architecture

```
                    +-------------------------------+
                    |   PORTFOLIO LEVEL              |
                    |   max_global_exposure           |
                    |   5% daily circuit breaker      |
                    |   30% correlation limit         |
                    |   Kill switch (one-way)         |
                    +---------------+---------------+
                                    |
         +--------------------------+-------------------------+
         |                          |                         |
+--------+--------+   +------------+----------+   +----------+---------+
| WEATHER STRAT   |   | AI ENSEMBLE           |   | CROSS-PLATFORM     |
| Kelly 0.25      |   | Kelly 0.25            |   | Fixed $5-$10       |
| MAX_BET $20     |   | StdDev <30%           |   | min_edge 2%        |
| 5 exit mechs    |   | 5% min edge           |   | $100 size cap      |
| Calibration     |   | Multi-model           |   | Fee accounting     |
+---------+-------+   +-----------+-----------+   +----------+---------+
          |                        |                          |
          +------------------------+--------------------------+
                                   |
                  +----------------+------------------+
                  |   8-CHECK VALIDATION CHAIN         |
                  |   1. Kill switch                    |
                  |   2. Blacklist                      |
                  |   3. Whitelist                      |
                  |   4. Volume minimum                 |
                  |   5. Per-market exposure             |
                  |   6. Global exposure                |
                  |   7. Daily loss (-> kill switch)     |
                  |   8. Drawdown (-> kill switch)       |
                  +----------------+------------------+
                                   |
                    +--------------+------------------+
                    |   PLATFORM LAYER                 |
                    |   Heartbeat (5s send)             |
                    |   Rate limits tracked             |
                    |   HTTP 425/503 handling           |
                    |   Fee-aware sizing                |
                    |   Slippage validation             |
                    |   Order timeout (60s)             |
                    +----------------------------------+
```

---

## 21. Market Maker Risk Controls (Poly-Maker)

Full control set from `trading.py`:
| Control | Function |
|---------|----------|
| `stop_loss_threshold` | PnL % trigger for emergency sell |
| `spread_threshold` | Max spread for stop-loss execution (won't sell into wide spreads) |
| `volatility_threshold` | 3-hour volatility ceiling — blocks buys AND triggers sells |
| `sleep_period` | Hours to pause trading after risk-off event |
| `take_profit_threshold` | % above avgPrice for take-profit |
| `max_size` | Maximum position size per market |
| `min_size` | Minimum order size (prevents dust trades) |
| Price range guard | Buy orders only between $0.10-$0.90 |
| Price change guard | Cancel all orders if price drifts > $0.05 from reference |
| Smart cancellation | Only cancel/replace if price diff > $0.005 OR size diff > 10% |
| Stale trade cleanup | Pending trades removed after 15 seconds |
| Position merging | Merge YES+NO positions to recover USDC collateral |

---

## 22. Operational Checklist — Before Every Trading Session

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

## Key Citations Index

| Finding | Source | Location |
|---------|--------|----------|
| 92.4% wallets unprofitable | Sovereign Analysis / 50K wallet study | Source 3, Source 5 |
| 522x paper vs -49.5% live | Jung-Hua Liu live trading analysis | Source 9 |
| Quarter-Kelly consensus | WeatherBot + PolySwarm + live analysis | `calc_kelly()`, PolySwarm S351 |
| 12.3s -> 2.7s arb compression | Multi-source ecosystem data | Source 3 line 107 |
| 18% human underperformance | 50K wallet analysis | Source 3 line 131 |
| 8-check validation chain | polymarket-arbitrage `risk_manager.py` | `check_order()` |
| Kill switch auto-trigger | polymarket-arbitrage `risk_manager.py` | `update_pnl()` + `_trigger_kill_switch()` |
| Compound stop-loss | poly-maker `trading.py` | Line 431 |
| Risk-off cooldown per market | poly-maker `trading.py` | Lines 439-472 |
| Position merging (YES+NO) | poly-maker `trading.py` | Lines 312-323 |
| Heartbeat 10s kill switch | Polymarket docs | Order creation page |
| Fee formula `C * feeRate * p * (1-p)` | Polymarket docs | Fees page |
| Calibration via MAE per city | WeatherBot `run_calibration()` | `bot_v2.py` lines 781-809 |
| Time-horizon take-profit | WeatherBot `monitor_positions()` | `bot_v2.py` lines 1548-1553 |
| v2->v3 lookback improvement | Jung-Hua Liu analysis | Source 9 lines 438-476 |
| PolySwarm uncertainty filter | PolySwarm arXiv paper | Source 7 line 338 |
