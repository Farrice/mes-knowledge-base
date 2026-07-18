---
description: "Full trade lifecycle plan — entry sizing, all five exit scenarios, decision tree, and risk parameters from a single identified edge"
---

# Trade Execution Plan

> Takes an identified edge from the Market Forecast & Edge Detection workflow and produces the complete trade lifecycle: verified entry with real ask pricing, Kelly-derived position size with triple cap, and all five exit scenarios (stop-loss, trailing stop, take-profit, forecast-change, resolution) with dollar amounts, trigger conditions, and probabilities. Output is a deployable trade ticket and decision tree.

---

## Inputs

Provide from the scan output or manual identification:

| Input | Required | Source | Notes |
|-------|----------|--------|-------|
| City + ICAO code | Yes | Scan output | Must be the ICAO station, not city name |
| Target date | Yes | Scan output | The market resolution date |
| Matching bucket | Yes | Scan output | e.g., "58-59F" or "13C or higher" |
| Forecast temperature | Yes | Scan output | From the best source for this city/horizon |
| Forecast source | Yes | Scan output | HRRR, ECMWF, or METAR |
| Calibrated sigma | Yes | Calibration data or default | Per-city per-source, or 2.0F / 1.2C default |
| Market ask price | Yes | Scan output | Will be RE-VERIFIED before execution |
| Market bid price | Yes | Scan output | For spread calculation |
| Market volume | Yes | Scan output | Must be >= 500 |
| Hours to resolution | Yes | Calculated | From now to market resolution time |
| Account balance | Yes | Current | Available balance for position sizing |

---

## Process

### STEP 1 — Input Validation

Run all filters against the provided inputs. If ANY filter fails, produce a REJECTION ticket instead of a trade ticket.

**Hard rejections** (no override):
```
Spread check:    (ask - bid) <= $0.03     → REJECT if spread too wide
Price check:     ask < $0.45              → REJECT if contract too expensive
Volume check:    volume >= 500            → REJECT if illiquid
Time check:      2.0 <= hours <= 72.0     → REJECT if too close or too far
```

**Edge validation**:
```
Probability:     calculated from bucket_prob() with calibrated sigma
b (payout odds):  (1 / ask) - 1
EV:              p * b - (1 - p)          → REJECT if EV < 0.10
```

### STEP 2 — Real Price Verification (Two-Pass)

The scan used cached/event API prices. Before execution, make a SECOND API call to the individual market endpoint for real-time pricing.

```
Fetch: Real bestAsk and bestBid from individual market endpoint
Compare: |real_ask - scan_ask| <= MAX_SLIPPAGE ($0.03)
If real_ask > scan_ask + $0.03:  REJECT — stale price, re-scan
If real_ask > $0.45:             REJECT — price moved above threshold
If real_spread > $0.03:          REJECT — spread widened
```

If real price passes all checks, use real_ask (not scan_ask) for all downstream calculations.

### STEP 3 — Position Sizing (Triple-Capped Kelly)

```
LAYER 1 — Kelly Calculation:
  b = (1 / ask) - 1                           # payout odds
  full_kelly = (p * b - (1 - p)) / b          # raw Kelly fraction
  fractional_kelly = full_kelly * 0.25          # quarter Kelly

LAYER 2 — Dollar Sizing:
  raw_size = fractional_kelly * balance
  capped_size = min(raw_size, $20.00)           # hard dollar cap

LAYER 3 — Floor Filter:
  final_size = capped_size if capped_size >= $0.50 else REJECT
  shares = final_size / ask
```

Record:
- Kelly % (full and fractional)
- Raw dollar size (before cap)
- Final dollar size (after cap)
- Number of shares
- Position as % of balance

### STEP 4 — Define All Exit Parameters

**A. Stop-Loss** (fires every 10 minutes in monitor):
```
stop_price = entry_ask * 0.80
max_loss = final_size * 0.20
trigger: current_price <= stop_price
action: sell all shares at market bid
```

**B. Trailing Stop** (fires every 10 minutes in monitor):
```
activation_price = entry_ask * 1.20
new_stop = entry_ask (breakeven)
trigger: price rose above activation, then dropped below entry
action: sell all shares — guaranteed breakeven or better
```
Note: Stop moves to breakeven only, not higher. Deliberately conservative.

**C. Take-Profit** (fires every 10 minutes in monitor):
```
if hours_to_resolution > 48:   take_profit = $0.75
if hours_to_resolution 24-48:  take_profit = $0.85
if hours_to_resolution < 24:   take_profit = NONE (hold to resolution)

profit_at_tp = shares * take_profit - final_size
trigger: current_price >= take_profit threshold
action: sell all shares at take-profit price
```

**D. Forecast-Change Exit** (fires every 60 minutes in scan):
```
bucket_midpoint = (low + high) / 2   (for center buckets)
                  or boundary         (for edge buckets)
buffer = 2.0F or 1.0C

trigger: |new_forecast - bucket_midpoint| > (bucket_width + buffer)
action: sell all shares immediately regardless of P&L
```
The 2-degree buffer prevents whipsawing on normal forecast fluctuations. Exit only when the forecast GENUINELY changed, not noise.

**E. Resolution** (fires in auto-resolution check):
```
WIN detection:  yes_price >= $0.95 → payout = shares * $1.00
LOSS detection: yes_price <= $0.05 → payout = $0.00

Note: Use price convergence, NOT API "resolved" status.
Polymarket's closed flag is unreliable — price is the robust signal.
```

### STEP 5 — Build Scenario Map

Calculate expected outcomes for each scenario:

```
For each exit scenario:
  - Trigger condition (what price/forecast level)
  - Dollar P&L if triggered
  - Estimated probability based on historical data
  - Time horizon (when this scenario typically fires)
```

### STEP 6 — Build Decision Tree

Map the monitoring cadence to exit priority:

```
ENTRY (now)
  │
  ├─→ MONITOR (every 10 minutes)
  │     ├─→ Check stop-loss     → SELL if price <= stop
  │     ├─→ Check trailing stop → SELL if trailing activated AND price <= entry
  │     └─→ Check take-profit   → SELL if price >= TP threshold
  │
  ├─→ SCAN (every 60 minutes)
  │     ├─→ Fetch fresh forecast
  │     └─→ Check forecast-change → SELL if forecast shifted 2+F beyond bucket
  │
  └─→ RESOLUTION (auto-check after market close time)
        ├─→ yes_price >= $0.95 → WIN: payout $1.00/share
        └─→ yes_price <= $0.05 → LOSS: payout $0.00
```

---

## Output Schema

A Trade Execution Plan produces exactly one of two shapes per input set — never both, and never a hybrid:

- **Rejection Ticket** — produced when ANY Step 1 hard filter or Step 2 real-price re-verification fails. Contains only: reason, actual value, threshold, and a one-line next action. No entry math, no exit scenarios.
- **Trade Execution Blueprint** — produced when every filter clears. Contains: header (market, bucket, forecast/source/sigma, hours to resolution, scan timestamp); Entry block (probability, verified ask/bid/spread, EV, full and fractional Kelly, capped position size, share count, balance-risk %); all six Exit Scenarios A-F (stop-loss, trailing stop, take-profit, forecast-change, resolution-WIN, resolution-LOSS), each with trigger condition, dollar outcome, and an estimated probability grounded in this trade's actual sigma/hours/bucket-distance — not a generic guess; a weighted-EV line combining the WIN/LOSS resolution probabilities; the Decision Tree; and the Pre-Flight Checklist. Add a Portfolio Summary block only when this blueprint is one of several trades drawn from a single scan.

Every dollar figure in either shape must derive from the supplied inputs and the Step 1-4 formulas — no invented prices, probabilities, or share counts. See the Output Template below for exact field layout.

```
TRADE EXECUTION BLUEPRINT
==========================================================
Market: {city} {ICAO} | {date} | Bucket: {bucket}
Forecast: {temp} ({source}) | Sigma: {sigma} | Hours to resolution: {hours}h
Scan time: {timestamp}

─── ENTRY ────────────────────────────────────────────────
  Probability:     {p:.1%} (calibrated sigma {sigma})
  Market Ask:      ${ask:.3f} (VERIFIED — real-time, not cached)
  Market Bid:      ${bid:.3f}
  Spread:          ${spread:.3f} (OK, <= $0.03)
  EV per dollar:   +${ev:.2f}

  Kelly Fraction:  {frac_kelly:.1%} (full Kelly {full_kelly:.1%} * 0.25)
  Position Size:   ${size:.2f} {cap_note}
  Shares:          {shares:.2f} @ ${ask:.3f}
  Balance Risk:    {pct:.2%} of ${balance}

─── EXIT SCENARIOS ───────────────────────────────────────

  A. STOP-LOSS (price <= ${stop:.3f})
     Max loss:      -${max_loss:.2f}
     Trigger:       Price drops 20% from entry
     Monitor:       Every 10 minutes
     Est. probability: ~{stop_prob}%

  B. TRAILING STOP (price hits ${trail_act:.3f}, then drops to ${ask:.3f})
     Outcome:       Breakeven ($0.00)
     Trigger:       Price rises 20%, then falls below entry
     Monitor:       Every 10 minutes
     Est. probability: ~{trail_prob}%

  C. TAKE-PROFIT (price >= ${tp:.2f}, {tp_window})
     Profit:        +${tp_profit:.2f}
     Trigger:       Price reaches TP threshold for time window
     Monitor:       Every 10 minutes
     Est. probability: ~{tp_prob}%

  D. FORECAST-CHANGE EXIT (forecast moves {buffer}+ beyond bucket)
     Est. exit price: ~${fc_price:.2f}
     Est. P&L:       ${fc_pnl}
     Trigger:        Fresh forecast invalidates thesis
     Monitor:        Every 60 minutes (requires forecast refresh)
     Est. probability: ~{fc_prob}%

  E. RESOLUTION — WIN (actual temp in {bucket})
     Payout:         ${win_payout:.2f} ({shares:.2f} shares * $1.00)
     Profit:         +${win_profit:.2f}
     Est. probability: ~{win_prob}%

  F. RESOLUTION — LOSS (actual temp outside {bucket})
     Payout:         $0.00
     Loss:           -${size:.2f}
     Est. probability: ~{loss_prob}%

─── EXPECTED VALUE ───────────────────────────────────────
  Weighted EV: ({win_prob}% * +${win_profit:.2f}) + ({loss_prob}% * -${size:.2f}) = +${weighted_ev:.2f}
  (Excludes early exit scenarios which generally improve EV)

─── DECISION TREE ────────────────────────────────────────
  ENTRY → [10min: stop/trail/TP] → [60min: forecast-change] → [Resolution: auto-resolve]

  Priority: Stop-loss checked FIRST (protect capital),
            then trailing (protect profits),
            then take-profit (lock gains),
            then forecast-change (thesis check),
            then hold to resolution.

─── PRE-FLIGHT CHECKLIST ─────────────────────────────────
  [ ] Real ask price verified (not stale)
  [ ] Spread <= $0.03
  [ ] Position size within Kelly cap
  [ ] Stop-loss price recorded
  [ ] Monitor cadence set (10min position, 60min forecast)
  [ ] Balance updated after entry
```

---

## Example Output

```
TRADE EXECUTION BLUEPRINT
==========================================================
Market: Chicago KORD | Apr 15 | Bucket: 58-59F
Forecast: 58F (HRRR) | Sigma: 1.72 | Hours to resolution: 28h
Scan time: 2026-04-14 09:15 UTC

─── ENTRY ────────────────────────────────────────────────
  Probability:     100.0% (HRRR forecast 58F, sigma 1.72)
  Market Ask:      $0.120 (VERIFIED)
  Market Bid:      $0.105
  Spread:          $0.015 (OK)
  EV per dollar:   +$0.78

  Kelly Fraction:  8.2% (full Kelly 32.8% * 0.25)
  Position Size:   $16.40 (capped at $20 max)
  Shares:          136.67 @ $0.12
  Balance Risk:    0.16% of $10,000.00

─── EXIT SCENARIOS ───────────────────────────────────────

  A. STOP-LOSS (price <= $0.096)
     Max loss:      -$3.28
     Est. probability: ~5%

  B. TRAILING STOP (price hits $0.144, then drops to $0.120)
     Outcome:       Breakeven ($0.00)
     Est. probability: ~10%

  C. TAKE-PROFIT (price >= $0.85, 24-48h window)
     Profit:        +$99.67
     Est. probability: ~15%

  D. FORECAST-CHANGE EXIT (forecast moves 2F+ beyond 58-59F)
     Est. exit price: ~$0.06-0.10
     Est. P&L:       -$2.73 to -$8.20
     Est. probability: ~8%

  E. RESOLUTION — WIN (actual temp 58-59F)
     Payout:         $136.67 (136.67 shares * $1.00)
     Profit:         +$120.27
     Est. probability: ~62%

  F. RESOLUTION — LOSS (actual temp outside 58-59F)
     Payout:         $0.00
     Loss:           -$16.40
     Est. probability: ~38%

─── EXPECTED VALUE ───────────────────────────────────────
  Weighted EV: (62% * +$120.27) + (38% * -$16.40) = +$68.34

─── DECISION TREE ────────────────────────────────────────
  ENTRY → [10min: stop/trail/TP] → [60min: forecast-change] → [Resolution]
```

---

## Multi-Trade Portfolio View

When executing multiple trades from a single scan, add a portfolio summary:

```
PORTFOLIO SUMMARY — {n} trades from scan
═══════════════════════════════════════
Total capital deployed:  ${total}
Total balance risk:      {pct:.1%}
Worst-case loss (all stop): -${worst}
Expected portfolio EV:   +${portfolio_ev}

Correlation check:
- {n} US cities, {n} international → geographic diversification OK
- {n} same-day, {n} D+1, {n} D+2 → time diversification OK
- Max single-city exposure: ${max_city} ({city})

WARNING: If 2+ trades are in nearby cities on the same date,
weather events may be correlated. Treat as ONE position for risk.
```

---

## Rejection Ticket

When a trade fails any filter, produce a rejection ticket instead:

```
TRADE REJECTED — {city} {date} {bucket}
════════════════════════════════════════
Reason: {specific filter that failed}
  Filter value: {actual value}
  Threshold:    {required value}

{If spread: "Wait for spread to tighten and re-scan."}
{If price: "Contract too expensive. Wait for price to drop below $0.45."}
{If volume: "Market too thin. Risk of getting trapped in position."}
{If EV: "Edge too small. Fees and slippage would eat the profit."}
{If time: "Too close to resolution — market is efficient. OR too far — forecast unreliable."}
```

---

## Quality Gate

- Did Step 1 (hard filters) and Step 2 (real-price re-verification) run and clear BEFORE any sizing or exit math was produced — never sized first, filtered after?
- Is the position size the output of all three Kelly layers in strict order (fractional Kelly → $20 dollar cap → $0.50 floor), not a shortcut estimate?
- Are all six exit branches (A-F: stop-loss, trailing stop, take-profit, forecast-change, resolution-WIN, resolution-LOSS) present and independently triggered — none silently merged or dropped?
- Does the take-profit threshold scale correctly to hours-to-resolution (HOLD under 24h, $0.85 at 24-48h, $0.75 above 48h), never a flat threshold applied regardless of horizon?
- Is resolution determined by price convergence ($0.95 WIN / $0.05 LOSS), never by an assumed "closed" API status flag?
- If real bestAsk/bestBid verification data wasn't supplied for Step 2, is the ticket explicitly marked provisional rather than presented as execution-ready?
- For multi-trade scans, is same-date/nearby-city weather correlation flagged in the Portfolio Summary so correlated trades aren't priced as independent bets?
