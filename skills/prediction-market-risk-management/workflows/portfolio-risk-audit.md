---
name: "Portfolio Risk Audit"
skill: "prediction-market-risk-management"
produces: "Full risk assessment across all active positions with dashboard, correlation analysis, strategy health, and recommended adjustments"
version: "1.0"
---

# Portfolio Risk Audit

Comprehensive risk assessment across all active trading positions, all strategies, and all platforms. This is the portfolio-level view that the 8-check validation chain (per-trade) cannot provide — it catches correlation risk, strategy decay, platform threats, and slow-burn degradation that individual trade checks miss.

**Run daily during active trading. Every 4 hours during volatile periods. Immediately after any kill switch trigger or unusual market event. This audit is not optional.**

---

## Inputs Required

```
PORTFOLIO STATE:
- All open positions: market_id, strategy, direction, entry_price, current_price, size,
  entry_time, hours_to_resolution, market_category, current_best_bid
- All strategies: name, status, 30-day trade count, 30-day P&L, 30-day win rate,
  average edge per trade, opportunity frequency trend
- Platform state: capital deployed per platform, last heartbeat timestamp,
  last API error (if any), current fee schedule
- Trading capital: total bankroll, deployed amount, reserve (cash) amount
- Recent history: last 50 completed trades with P&L, strategy, timestamp
- Kill switch state: triggered (bool), reason, last trigger timestamp

RISK CONFIG (current settings):
- All position-sizing parameters
- Kill switch trigger thresholds (all 3 levels)
- Strategy allocation limits
- Correlation rebalance threshold (default: 30%)
```

---

## Section 1: Portfolio Exposure Summary

Calculate and report:

```
PORTFOLIO EXPOSURE
==========================================
Total Trading Capital:     ${bankroll}
Total Deployed:            ${sum_all_positions}  ({deployed_pct}% of bankroll)
Cash Available:            ${bankroll - deployed}
Deployment Ratio Status:   {OK if <30% | YELLOW if 30-50% | RED if >50%}

Platform Breakdown:
  Polymarket:              ${poly_amount} ({poly_pct}%)  {OK if <60% | WARNING if >=60%}
  Kalshi:                  ${kalshi_amount} ({kalshi_pct}%)  {OK if <60% | WARNING if >=60%}

Strategy Breakdown:
  Weather Trading:         ${weather_amount} ({weather_pct}%)  {OK if <40% | WARNING if >=40%}
  AI Ensemble:             ${ai_amount} ({ai_pct}%)
  Market Making:           ${mm_amount} ({mm_pct}%)
  Cross-Platform Arb:      ${arb_amount} ({arb_pct}%)

Open Positions:            {count} / {max_concurrent (15)}
Largest Single Position:   ${largest} in {market_id} ({largest_pct}% of bankroll)
```

**Violations to flag:**
- Portfolio deployment >30%: YELLOW — capital is concentrated, consider closing rotation candidates
- Single platform >60%: RED — diversify or withdraw excess immediately
- Single strategy >40%: RED — rebalance or pause new trades in this strategy
- Positions at 15 cap: RED — must close before new trades
- Any single position >10% of bankroll: RED — exceeds max_position_per_market

---

## Section 2: Position-Level Analysis

For EACH open position, calculate:

```
POSITION: {market_id}
  Strategy:          {name}
  Direction:         {YES/NO}
  Category:          {crypto/sports/geopolitical}
  Entry:             ${entry_price} -> Current bid: ${current_best_bid}
  Size:              ${amount} ({pct_of_bankroll}% of bankroll)
  Unrealized P&L:    ${unrealized} ({unrealized_pct}%)
  Time held:         {hours}h
  Time to resolution: {hours_remaining}h
  Edge remaining:    {current_estimated_prob - current_market_price}%
  Fee paid at entry: ${fee_amount}
  Exit scenarios:
    - Stop-loss at:    ${entry * 0.80} (loss: ${loss_amount})
    - Take-profit at:  ${tp_price} (profit: ${profit_amount})
    - Current best bid: ${best_bid} (P&L if exit now: ${exit_pnl})
  STATUS:            {HOLD | ROTATE | EXIT | STOP-LOSS ZONE | TRAILING ACTIVE}
```

### Rotation Signal Logic (from extraction Section 18)
- **ROTATE**: Unrealized P&L has captured >70% of original expected value AND time to resolution > 12h. Capital is better deployed elsewhere. Prediction market edges are front-loaded.
- **EXIT**: Edge remaining < 1% (spread closed, no value in holding). OR current market price moved against you beyond original edge with no recovery thesis.
- **STOP-LOSS ZONE**: Price within 5% of stop-loss trigger. Alert — prepare for exit.
- **TRAILING ACTIVE**: Position is +20% from entry, trailing stop moved to breakeven.
- **HOLD**: Significant edge remains and time to resolution within profitable window.

### Flag positions needing attention:
- Any position with >50% unrealized loss (well past stop-loss — execution issue?)
- Any position held beyond original max_hours threshold
- Any position where market volume dropped below min_volume since entry
- Any position approaching resolution within min_hours (2h) window
- Any rotation candidate sitting idle for >6 hours (capital drag)

---

## Section 3: Correlation Matrix

Group positions by potential correlation factors. This is where the portfolio-level view catches risk invisible at the per-trade level.

### Category Clusters
```
CORRELATION CLUSTERS
==========================================

Cluster: Weather — US Cities
  Positions:         {list with sizes}
  Aggregate exposure: ${total}  ({pct}% of bankroll)
  Correlation risk:  {LOW (<15%) | MEDIUM (15-30%) | HIGH (>30%)}
  Scenario:          "If a cold front sweeps the eastern US, {N} positions worth ${X} are all affected"
  Recommended action: {None | Reduce by ${amount} to stay under 30% correlated}

Cluster: Political — Election Markets
  Positions:         {list}
  Aggregate exposure: ${total}
  Correlation risk:  {level}
  Scenario:          "{describe correlated event}"

Cluster: Crypto Markets
  Positions:         {list}
  Fee regime:        0.072 (highest tier)
  Aggregate fee drag: ${total_fees_paid}
```

### Resolution Time Clusters
```
RESOLUTION CLUSTERS
==========================================
Next 12h:     {N} positions, ${total}  ({pct}% of deployed)
12-24h:       {N} positions, ${total}
24-48h:       {N} positions, ${total}
48-72h:       {N} positions, ${total}
72h+:         {N} positions, ${total}
```

If >40% of deployed capital resolves in same 24-hour window: RED WARNING — a single bad day could create outsized losses. Diversify resolution timing.

### Directional Clusters
Identify positions that all benefit from the same market direction. Five weather bets on "higher than expected temperatures" in different cities = a SINGLE directional bet spread across multiple markets, not diversification.

```
DIRECTIONAL ANALYSIS:
  Long weather-above:  {N} positions, ${total}
  Long weather-below:  {N} positions, ${total}
  Net directional:     ${net}  ({direction})
  Balanced?            {YES if |net| < 20% of total | NO — directional risk}
```

If aggregate correlated exposure in ANY cluster > 30% of bankroll: trigger rebalancing recommendation.

---

## Section 4: Strategy Health Check

For each active strategy, assess health using rolling 30-day data:

```
STRATEGY: {name}
==========================================
Status: {ACTIVE | CAUTION | DEGRADING | RECOMMEND-PAUSE}

Performance (30-day rolling):
  Trades:           {count}
  Win rate:         {pct}% (threshold: >50%)
  Average edge:     {pct}% per trade (threshold: > fees + slippage)
  Net P&L:          ${amount}
  Sharpe proxy:     {mean_pnl / std_pnl}
  Fee drag:         {total_fees / total_volume}%

Trend (vs 30 days ago):
  Edge:    {30d_ago}% -> {now}%    {STABLE | COMPRESSING | EXPANDING}
  Volume:  {30d_ago} -> {now}      {STABLE | DECLINING | GROWING}
  Win rate: {30d_ago}% -> {now}%   {trend}
  Opportunity frequency: {30d_ago}/day -> {now}/day  {trend}

Paper-to-Live Degradation:
  Backtest expected:    {backtest_winrate}%
  Live actual:          {live_winrate}%
  Degradation:          {degradation_pct}%
  Within acceptable band (80-95% of backtest)? {YES/NO}

Recommendation: {Continue | Reduce allocation by X% | Pause pending review | Retire — reallocate capital}
```

**Strategy status rules:**
- **ACTIVE**: Win rate >50%, edge stable or expanding, P&L positive, degradation <90%
- **CAUTION**: Win rate 45-50%, OR edge compressing >15% over 30 days, OR degradation approaching 90%
- **DEGRADING**: Win rate <45%, OR edge compressing >30%, OR negative 30-day P&L
- **RECOMMEND-PAUSE**: Win rate <40%, OR 30-day P&L negative and worsening, OR opportunity frequency declining >50%

**Edge decay is the leading indicator.** Latency arb compressed from 12.3s to 2.7s to dead. Monitor opportunity frequency — if opportunities are becoming rarer, the strategy is compressing regardless of current win rate.

---

## Section 5: Platform Risk Indicators

Monitor platform-level risk factors that exist OUTSIDE your strategy logic:

```
PLATFORM RISK: Polymarket
==========================================
Fee Status:
  Expected taker fee:    {expected}%
  Actual avg (7 days):   {actual}%
  Discrepancy:           {NONE | ${diff}%}  {OK if <0.1% | ALERT if >=0.1%}
  Fee change killed latency arb overnight — monitor this.

API Health:
  Heartbeat:             {OK: last {X}s ago | DANGER: last {X}s ago (10s = platform cancels all)}
  Avg latency (24h):     {ms}  {OK if <2x baseline | DEGRADED if 2-5x | DOWN if 5x+}
  Error rate (24h):      {pct}%  {OK if <1% | CAUTION if 1-5% | RED if >5%}
  Rate limit headroom:   {remaining}/{max} per 10s window

Infrastructure:
  Next engine restart:   Tuesday 7 AM ET ({countdown})
  HTTP 503 incidents:    {count in last 7d}
  HTTP 425 incidents:    {count in last 7d}
  Cancel-all capacity:   250/10s — sufficient for {position_count} positions? {YES/NO}

PLATFORM RISK: Kalshi (if applicable)
  [Same structure]
```

**Critical alerts:**
- Fee discrepancy >0.1%: Immediate investigation. If confirmed, Level 1 kill switch for affected strategies.
- API error rate >5%: Reduce position sizes by 50% until resolved.
- Heartbeat >7s: DANGER — approaching 10s platform kill switch. Check network.
- Tuesday approaching: Plan for 90s downtime window. No new orders during restart.
- Cancel-all rate limit vs position count: If you have 300+ open orders and can only cancel 250/10s, emergency exits are physically impossible in one window.

---

## Section 6: Drawdown and Kill Switch Proximity

```
KILL SWITCH STATUS
==========================================
Current Level:     {GREEN | YELLOW | ORANGE | RED}
Kill Switch:       {CLEAR | TRIGGERED: {reason} at {timestamp}}

Trigger Proximity:
  Daily P&L:       ${daily_pnl}  | Limit: -${max_daily_loss}  | Distance: ${distance}  ({pct_consumed}% consumed)
  Drawdown:        {current}%    | Limit: {max_drawdown}%      | Distance: {distance}%
  Win rate (20):   {current}%    | L1 trigger: 45%             | Distance: {distance}%
  API latency:     {current}ms   | L1 trigger: {2x_baseline}ms | Distance: {distance}ms
  Global exposure: {current}%    | L1 trigger: 70%             | Distance: {distance}%

Nearest trigger:   {metric_name}
Buffer remaining:  {how much deterioration before first trigger fires}

Worst-Case Scenario:
  If ALL positions hit stop-loss simultaneously:
    Total loss: -${all_stops_loss}  ({pct}% of bankroll)
    Would trigger kill switch? {YES at Level {X} | NO — within limits}
    Would survive? {YES — bankroll remains ${remaining} | CRITICAL — near ruin}
```

---

## Section 7: Risk Parameter Analysis

Based on recent trading data, assess whether current parameters are well-calibrated:

```
PARAMETER HEALTH
==========================================
Kelly Fraction (0.25):
  Actual avg position vs Kelly recommendation: {actual_pct}% of optimal
  Assessment: {Appropriately conservative | Could increase to 0.30 if 200+ trades validated | Reduce — edge estimates unreliable}

Stop-Loss (-20%):
  Trades that hit stop: {count} ({pct}% of total)
  Of stopped trades, would have been profitable: {recovery_pct}%
  Assessment: {Too tight (>30% would have recovered) | Well calibrated | Too loose (<10% recovered)}

Take-Profit:
  Trades that hit TP: {count}
  Of TP trades, resolved at $1.00: {pct}%
  Assessment: {Too aggressive (>50% would have resolved higher) | Well calibrated | Appropriate for time horizons}

Min EV (0.10):
  Trades with EV 0.10-0.15: win rate {pct}%
  Assessment: {Raise to 0.15 if <45% win rate | Keep current | Could lower if >60%}

Slippage Budget:
  Trades cancelled for slippage: {count} ({pct}% of attempts)
  Average actual slippage: ${avg_slip}
  Assessment: {Tighten min_volume if >20% cancelled | Well calibrated | Could loosen}
```

**WARNING**: Change ONE parameter at a time. Run for minimum 50 trades before evaluating. Changing multiple simultaneously makes attribution impossible.

---

## Section 8: Risk Dashboard (Summary Output)

```
========================================
PORTFOLIO RISK DASHBOARD
{date} {time}
========================================

OVERALL STATUS: {GREEN | YELLOW | RED}

Capital:     ${bankroll} deployed ${deployed} ({pct}%)             {OK | WARN | RED}
Positions:   {N} open, {N} rotation candidates, {N} flagged       {OK | WARN | RED}
Strategies:  {N} active, {N} caution, {N} degrading               {OK | WARN | RED}
Platforms:   {N} OK, {N} degraded                                  {OK | WARN | RED}
Kill Switch: {level}  Nearest trigger: {metric} at {distance}     {OK | WARN | RED}
Correlation: {N} clusters, max cluster ${amount} ({pct}%)         {OK | WARN | RED}
Heartbeat:   {status}  Last: {X}s ago                             {OK | WARN | RED}

TODAY'S P&L:     ${daily_pnl} ({daily_pct}%)
30-DAY P&L:      ${monthly_pnl} ({monthly_pct}%)
PAPER-TO-LIVE:   {degradation}% average across strategies

==========================================
RECOMMENDED ACTIONS (priority order):
==========================================

1. [{RED/YELLOW}] {Most urgent — e.g., "Close 3 weather positions that captured >80% of edge — freeing ${X} for redeployment"}
2. [{RED/YELLOW}] {Second — e.g., "Reduce weather strategy from 42% to 35% allocation — exceeds 40% limit"}
3. [{YELLOW}] {Third — e.g., "Run withdrawal test on Kalshi — last test was 45 days ago"}
4. [{INFO}] {Optional — e.g., "Consider raising min_ev to 0.15 — low-edge trades underperforming"}

==========================================
POSITIONS NEEDING ATTENTION:
==========================================
- {market_id}: {reason — e.g., "50%+ unrealized loss, edge evaporated, EXIT signal"}
- {market_id}: {reason — e.g., "Held 80h, past max_hours, volume declining"}
- {market_id}: {reason — e.g., "Rotation candidate: captured 85% of edge, 36h to resolution"}

==========================================
WATCH LIST:
==========================================
- Strategy: {name} edge compressing — down {X}% over 30 days
- Platform: {name} API latency elevated — {X}x normal for {N} days
- Correlation: Weather cluster at {X}% — approaching 30% rebalance threshold
- Resolution: {N} positions (${total}) resolve in next 12h — monitor closely
```

---

## Output Schema

A single deliverable with all 8 sections present, in order — never a subset, even when some sections read "no issues found":

1. Portfolio Exposure Summary (total/deployed/cash, platform breakdown, strategy breakdown, largest single position, with OK/YELLOW/RED status per line)
2. Position-Level Analysis (per open position: entry vs. current bid, size, unrealized P&L, edge remaining, exit scenarios, STATUS tag of HOLD/ROTATE/EXIT/STOP-LOSS ZONE/TRAILING ACTIVE)
3. Correlation Matrix (category clusters, resolution-time clusters, directional clusters, each with an aggregate exposure % and LOW/MEDIUM/HIGH risk tag)
4. Strategy Health Check (per strategy: 30-day win rate, average edge, net P&L, Sharpe proxy, trend vs. 30 days ago, paper-to-live degradation %, ACTIVE/CAUTION/DEGRADING/RECOMMEND-PAUSE status)
5. Platform Risk Indicators (fee status, heartbeat/API health, infrastructure countdown to next Tuesday restart, cancel-all capacity vs. position count)
6. Drawdown and Kill Switch Proximity (current level, distance to each of the 5 trigger metrics, worst-case simultaneous-stop-loss scenario)
7. Risk Parameter Analysis (Kelly fraction, stop-loss, take-profit, min-EV, slippage budget — each with a data-driven assessment, never a default "looks fine")
8. Risk Dashboard summary (one-screen OK/WARN/RED status line per category, today's and 30-day P&L, prioritized RECOMMENDED ACTIONS, POSITIONS NEEDING ATTENTION, WATCH LIST)

## Quality Gate

- Are all 8 sections present, including ones with no findings (state "none flagged" rather than omitting the section)?
- Does every correlation cluster report an aggregate exposure % against the 30% rebalance threshold, not just a list of positions?
- Is at least one ROTATE/EXIT/STOP-LOSS ZONE/TRAILING ACTIVE status assigned per open position — never a blanket "HOLD" without checking the rotation-signal logic (>70% edge captured + >12h to resolution)?
- Does the kill-switch-proximity section report distance-to-trigger for all 5 tracked metrics (daily P&L, drawdown, win rate, API latency, global exposure), not just the two hardest limits?
- Does the Risk Parameter Analysis section respect the one-parameter-at-a-time rule — no bundled recommendation that changes 2+ parameters in a single pass?
- Does the final dashboard's RECOMMENDED ACTIONS list rank by urgency (RED before YELLOW before INFO), matching the section 1-6 findings rather than introducing new, unsupported claims?

---

## Practitioner Notes

- **The rotation candidates are free money.** Positions sitting at 80%+ captured edge with 24+ hours to resolution are tying up capital. Capital rotation is the single highest-impact optimization for most portfolios — prediction market edges are front-loaded.

- **Correlation is the hidden killer.** Five uncorrelated $20 positions have very different risk from five correlated $20 positions. The first is diversified. The second is a single $100 bet wearing a disguise. The weather cluster scenario is the most common: all cities affected by the same jet stream shift.

- **Strategy health degrades slowly, then suddenly.** Edge compression looks gentle at -5% per month until 6 months pass and the strategy is underwater. The trend comparison catches this before it becomes portfolio-level damage. Latency arb died this way.

- **Test withdrawals regularly.** The worst time to discover your withdrawal process doesn't work is when you need to withdraw. Run a small test withdrawal monthly. Record time to completion.

- **The heartbeat is your canary.** If heartbeat latency is creeping up, your network or the platform is degrading. At 7+ seconds, you're one hiccup from Polymarket cancelling ALL your orders. This is not theoretical — it is the design of their matching engine.

- **Dashboard status colors:**
  - GREEN: All metrics within normal ranges. Continue operations.
  - YELLOW: One or more metrics approaching thresholds. Increase monitoring. Prepare to act.
  - RED: One or more limits breached or triggers imminent. Take corrective action before next trading session.

- **This audit takes 10 minutes. The recovery from an unmonitored blowup takes months.** Skipping it because "everything seems fine" is how you miss the slow degradation that turns a profitable portfolio into a losing one. The 92.4% didn't see it coming either.
