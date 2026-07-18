---
description: "Review resolved market data, calculate per-city sigma, identify systematic biases, and produce optimized config.json with commentary"
---

# Self-Calibration Review

> Analyzes all resolved market data to produce per-city per-source sigma values, identify systematic forecast biases, evaluate parameter performance, and output an optimized config.json. This workflow combines the Self-Calibration Analyst (accuracy review) with the Config Optimizer (parameter tuning) into a single calibration pass. Run after 30+ resolved markets, then again every 50 additional resolutions.

---

## Inputs

| Input | Required | Source | Notes |
|-------|----------|--------|-------|
| Resolved market data | Yes | `data/markets/*.json` | All JSON files where market has resolved (WIN or LOSS) |
| Current calibration | If exists | `data/calibration.json` | Previous sigma values; omit if first calibration |
| Current config | Yes | `config.json` | Current parameter values for comparison |
| Account history | Yes | Balance log | Starting balance, current balance, all trade P&L |

---

## Process

### PHASE 1 — Collect Forecast Errors

For each resolved market file in `data/markets/`:

```
1. Confirm market is resolved:
   - yes_price >= $0.95 (WIN) or yes_price <= $0.05 (LOSS)
   - Do NOT trust "closed" status flag — use price convergence only

2. Extract the LAST forecast snapshot before resolution:
   - forecast_temp: the temperature predicted
   - actual_temp: the resolution temperature (from METAR or Polymarket)
   - source: which forecast model was used (HRRR, ECMWF)

3. Calculate absolute error:
   error = abs(forecast_temp - actual_temp)

4. Group by (city, forecast_source):
   errors["NYC"]["HRRR"] = [1.2, 0.8, 2.1, 0.4, ...]
   errors["NYC"]["ECMWF"] = [1.5, 1.1, 1.9, 0.7, ...]
```

### PHASE 2 — Calculate Per-City Sigma

For each (city, source) pair:

```
IF sample_count >= CALIBRATION_MIN (30):
    new_sigma = mean(errors)    # MAE, not RMSE
    old_sigma = current calibration value OR default (2.0F / 1.2C)
    delta = new_sigma - old_sigma

    IF abs(delta) > 0.05:       # stability filter
        RECOMMEND UPDATE: sigma = new_sigma
    ELSE:
        NO CHANGE: sigma stable within noise threshold

IF sample_count < 30:
    INSUFFICIENT DATA: continue using default sigma
    Report: "{city} has {n} samples, needs {30-n} more for calibration"
```

**Why MAE not RMSE**: MAE is more robust to outliers. A single 10-degree miss (e.g., unexpected storm) doesn't distort sigma the way squaring the error would. For a Gaussian probability model where sigma directly controls position sizing, MAE is the conservative and correct choice.

**Why 0.05 threshold**: Prevents calibration from oscillating on noise. If new MAE is 2.03 and old sigma is 2.00, nothing changes. Creates parameter stability across scan cycles.

### PHASE 3 — Diagnose Systematic Biases

For each city, look for patterns in the errors:

```
1. DIRECTIONAL BIAS:
   mean_signed_error = mean(forecast - actual)
   If > +0.5: "Systematic warm bias — forecasts run hot"
   If < -0.5: "Systematic cold bias — forecasts run cold"

2. TIME-OF-DAY BIAS:
   Group errors by forecast horizon (D+0, D+1, D+2, D+3)
   If D+0 errors << D+2 errors: "Accuracy degrades with horizon" (expected)
   If D+0 errors >> D+2 errors: "Possible METAR anchoring issue"

3. SEASONAL PATTERN:
   If data spans 30+ days, check if errors correlate with date
   Winter storms = higher sigma
   Summer stable = lower sigma

4. SOURCE DISAGREEMENT:
   For cities with both HRRR and ECMWF data:
   Compare sigma_HRRR vs sigma_ECMWF
   If one source is consistently better: note for source selection optimization

5. CORRELATION CHECK:
   Are errors correlated across nearby cities on the same day?
   If yes: weather system moved through region; not independent trades
   Flag for portfolio risk assessment
```

### PHASE 4 — Evaluate Current Parameters

Analyze trade outcomes against current config to identify parameter improvements:

**Kelly Fraction Analysis**:
```
Current: KELLY_FRACTION = 0.25
Calculate optimal Kelly from actual win_rate and avg_payoff:
  actual_win_rate = wins / total_trades
  avg_win_payoff = mean(payout for winning trades)
  avg_loss = mean(loss for losing trades)
  optimal_kelly = (win_rate * avg_win_payoff - (1-win_rate) * avg_loss) / avg_win_payoff

If win_rate > 65% AND avg_payoff > 5x AND max_drawdown < 10%:
    Consider increasing to 0.28-0.30
If win_rate < 55% OR max_drawdown > 10%:
    Decrease to 0.20
NEVER recommend above 0.33 (one-third Kelly)
```

**Max Price Analysis**:
```
Current: MAX_PRICE = $0.45
Calculate win_rate by entry price bucket:
  <$0.10:     {win_rate}
  $0.10-0.20: {win_rate}
  $0.20-0.30: {win_rate}
  $0.30-0.45: {win_rate}

If win rate drops sharply above $0.25: lower to $0.30
If profitable trades exist at $0.45-0.55: consider raising to $0.50
```

**Min EV Analysis**:
```
Current: MIN_EV = 0.10
Distribution of entry EV for winners vs losers:
If most losses cluster at EV 0.10-0.15: raise to 0.15
If profitable trades being filtered at EV 0.08-0.10: lower to 0.08
```

**Time Window Analysis**:
```
Current: MIN_HOURS = 2.0, MAX_HOURS = 72.0
Win rate by hours-to-resolution bucket:
  2-6h:   {win_rate}  {pnl}
  6-12h:  {win_rate}  {pnl}
  12-24h: {win_rate}  {pnl}
  24-48h: {win_rate}  {pnl}
  48-72h: {win_rate}  {pnl}

Identify the sweet spot. Adjust min/max accordingly.
```

**City Performance**:
```
For each city:
  Trades: {n} | Wins: {n} | Win rate: {pct}
  Gross PnL: ${pnl} | Avg PnL/trade: ${avg}
  Calibrated sigma: {sigma}

Cities to ADD: Good forecast skill, many markets, currently not traded
Cities to REMOVE: Poor forecast skill (sigma > 3.0F), low volume, net negative PnL
Cities with sigma < 1.5F: High-confidence — consider increased Kelly for this city only
```

**Volume Filter Analysis**:
```
Current: MIN_VOLUME = 500
Win rate and exit quality by volume bucket:
  500-1000:  {win_rate} | Avg slippage on exit: {slip}
  1000-5000: {win_rate} | Avg slippage on exit: {slip}
  5000+:     {win_rate} | Avg slippage on exit: {slip}

If markets 500-750 have worse exits: raise to 750
```

**Slippage Analysis**:
```
Current: MAX_SLIPPAGE = $0.03
Actual execution slippage distribution:
  Trades entered with spread 0.00-0.01: {n} trades, {avg_pnl}
  Trades entered with spread 0.01-0.02: {n} trades, {avg_pnl}
  Trades entered with spread 0.02-0.03: {n} trades, {avg_pnl}

If higher-spread trades underperform: tighten threshold
```

### PHASE 5 — Produce Outputs

Generate three deliverables: sigma report, config recommendation, and portfolio analysis.

---

## Output Schema

A Calibration Report has four required sections, always in this order:

1. **Per-City Sigma** — one row per (city, source) pair carrying sample count, old σ, new σ, delta, and status (IMPROVED / SLIGHT DEGRADATION / STABLE / NO CHANGE), plus three explicit call-outs: insufficient-data cities (<30 samples, still on default sigma), high-risk cities (σ > 3.0, removal candidates), and high-confidence cities (σ < 1.5F / 0.8C, Kelly-increase candidates).
2. **Parameter Optimization** — a recommended `config.json` where every changed value carries an inline comment justifying it against the data reviewed, plus explicit `UNCHANGED` lines for parameters left alone (never silently omitted).
3. **Portfolio Analysis** — city performance ranking (win rate + net PnL + sigma per city), diversification breakdown (US vs international, climate-zone coverage), error-correlation notes between nearby cities, and add/remove candidates.
4. **Calibration Data** — the updated `calibration.json` payload, ready for storage, with per-city per-source sigma and sample counts.

Every sigma, delta, win-rate, and PnL figure must trace to the resolved-market data actually reviewed in Phase 1-4 — never a plausible-sounding placeholder invented to fill the table. See the Output Template below for the exact field layout.

```
CALIBRATION REPORT — {date}
══════════════════════════════════════════════════════════
Total resolved markets: {n} | Calibrated pairs: {n}/{total_pairs}
Trading period: {start_date} to {end_date} ({days} days)
Overall win rate: {pct}% | Net PnL: ${pnl}

═══ SECTION 1: PER-CITY SIGMA ═══════════════════════════

City            Source   Samples  Old σ    New σ    Delta    Status
─────────────── ──────── ──────── ──────── ──────── ──────── ──────────────────
NYC (KLGA)      HRRR     {n}      {old}    {new}    {delta}  {IMPROVED/DEGRADED/STABLE}
NYC (KLGA)      ECMWF    {n}      {old}    {new}    {delta}  {status}
Chicago (KORD)  HRRR     {n}      {old}    {new}    {delta}  {status}
Miami (KMIA)    HRRR     {n}      {old}    {new}    {delta}  {status}
London (EGLL)   ECMWF    {n}      {old}    {new}    {delta}  {status}
Tokyo (RJTT)    ECMWF    {n}      {old}    {new}    {delta}  {status}
...

INSUFFICIENT DATA (< 30 samples):
  {city}: {n} samples, needs {30-n} more. Using default σ = {default}.
  ...

HIGH-RISK CITIES (σ > 3.0):
  {city}: σ = {sigma} — forecast skill too low. RECOMMEND REMOVAL.

HIGH-CONFIDENCE CITIES (σ < 1.5F / 0.8C):
  {city}: σ = {sigma} — consider Kelly 0.28-0.30 for this city only.

SYSTEMATIC BIASES:
  {city}: Warm bias +{offset}°. Forecasts consistently run {offset}° above actual.
  {city}: Cold bias -{offset}°. Forecasts consistently run {offset}° below actual.
  {city}: HRRR σ={hrrr_sigma} vs ECMWF σ={ecmwf_sigma} — {source} is better by {delta}°.

═══ SECTION 2: PARAMETER OPTIMIZATION ═══════════════════

RECOMMENDED config.json:
{{
  "balance": {balance},
  "max_bet": {max_bet},           // {reason}
  "min_ev": {min_ev},             // {reason}
  "max_price": {max_price},       // {reason}
  "min_volume": {min_volume},     // {reason}
  "min_hours": {min_hours},       // {reason}
  "max_hours": {max_hours},       // {reason}
  "kelly_fraction": {kelly},      // {reason}
  "scan_interval": 3600,          // UNCHANGED
  "calibration_min": 30,          // UNCHANGED
  "max_slippage": {slippage}      // {reason}
}}

CHANGES FROM CURRENT:
  {param}: {old} → {new} | Reason: {reason}
  ...

NO CHANGE:
  {param}: {value} | Reason: {reason_to_keep}
  ...

═══ SECTION 3: PORTFOLIO ANALYSIS ══════════════════════

CITY PERFORMANCE RANKING:
  1. {city}: {win_rate}% win rate, +${pnl} net, σ={sigma} — KEEP (top performer)
  2. ...
  ...
  N. {city}: {win_rate}% win rate, -${pnl} net, σ={sigma} — REMOVE (net negative)

DIVERSIFICATION:
  US cities: {n} | International: {n}
  Climate zone coverage: {tropical, temperate, continental, maritime}
  Error correlation: {low/medium/high} between {city_pairs}

ADD CANDIDATES:
  {city}: Polymarket has active markets, good forecast data available, no current coverage
  ...

TIME-OF-DAY SWEET SPOT:
  Peak performance window: {hour_range} hours to resolution
  Avoid: {hour_range} (too close) and {hour_range} (too far)

═══ SECTION 4: CALIBRATION DATA (for storage) ══════════

Updated calibration.json:
{{
  "last_updated": "{timestamp}",
  "total_samples": {n},
  "cities": {{
    "{city}": {{
      "hrrr": {{"sigma": {val}, "samples": {n}, "last_error": {val}}},
      "ecmwf": {{"sigma": {val}, "samples": {n}, "last_error": {val}}}
    }},
    ...
  }}
}}
```

---

## Example Output

```
CALIBRATION REPORT — 2026-04-14
══════════════════════════════════════════════════════════
Total resolved markets: 847 | Calibrated pairs: 31/40
Trading period: 2026-03-01 to 2026-04-14 (45 days)
Overall win rate: 67% | Net PnL: +$4,218.50

═══ SECTION 1: PER-CITY SIGMA ═══════════════════════════

City            Source   Samples  Old σ    New σ    Delta    Status
─────────────── ──────── ──────── ──────── ──────── ──────── ──────────────────
NYC (KLGA)      HRRR     89       2.00     1.72     -0.28    IMPROVED — high confidence
NYC (KLGA)      ECMWF    92       2.00     1.85     -0.15    IMPROVED
Chicago (KORD)  HRRR     76       2.00     2.14     +0.14    SLIGHT DEGRADATION
Miami (KMIA)    HRRR     84       2.00     1.48     -0.52    EXCELLENT — best US city
London (EGLL)   ECMWF    67       1.20     1.45     +0.25    DEGRADATION — maritime variability
Tokyo (RJTT)    ECMWF    71       1.20     1.12     -0.08    STABLE
Seoul (RKSS)    ECMWF    62       1.20     1.18     -0.02    NO CHANGE (delta < 0.05)

INSUFFICIENT DATA:
  Singapore: 18 samples, needs 12 more. Using default σ = 1.2C.
  Mexico City: 22 samples, needs 8 more. Using default σ = 1.2C.

HIGH-RISK:
  Lucknow: σ = 2.8C — forecast skill too low. RECOMMEND REMOVAL.

HIGH-CONFIDENCE:
  Miami: σ = 1.48F — consider Kelly 0.30 for Miami trades.
  Tokyo: σ = 1.12C — consider Kelly 0.28 for Tokyo trades.

SYSTEMATIC BIASES:
  Chicago: Warm bias +0.6F. HRRR consistently runs 0.6F above actual at KORD.
  London: Maritime systems cause σ spikes during frontal passages.

═══ SECTION 2: PARAMETER OPTIMIZATION ═══════════════════

RECOMMENDED config.json:
{
  "balance": 14218.50,
  "max_bet": 25.0,           // INCREASED — 67% win rate supports it
  "min_ev": 0.12,            // INCREASED — 68% of losses from EV 0.10-0.12
  "max_price": 0.35,         // DECREASED — win rate drops 72% to 48% above $0.35
  "min_volume": 750,         // INCREASED — 500-750 markets had 12% worse exits
  "min_hours": 3.0,          // INCREASED — <3h markets 15% lower win rate
  "max_hours": 48.0,         // DECREASED — D+3 sigma is 40% higher
  "kelly_fraction": 0.28,    // INCREASED — win rate + payoff justify it
  "scan_interval": 3600,     // UNCHANGED
  "calibration_min": 30,     // UNCHANGED
  "max_slippage": 0.025      // TIGHTENED — spread > 0.025 lost 8% more
}

KEY FINDINGS:
  - Sweet spot: $0.08-$0.20 contracts, 6-36 hours to resolution
  - Miami, NYC, and Tokyo are highest-performing cities
  - London and Lucknow are net negative — consider removing
  - HRRR beats ECMWF by 0.4F MAE for US cities within 24h
```

---

## Quality Gate

- Is sigma computed as Mean Absolute Error, never RMSE — MAE is the deliberate choice here because a single outlier miss (an unexpected storm) shouldn't distort a parameter that directly controls position sizing?
- Did every (city, source) pair with fewer than 30 resolved samples get flagged "insufficient data, using default" rather than a calculated sigma presented as if reliable?
- Was the 0.05 stability threshold applied before recommending a sigma update — is "no change" the correct call whenever `abs(new - old) <= 0.05`?
- Does the Kelly Fraction recommendation stay at or below 0.33 (one-third Kelly) regardless of how strong the observed win rate looks — is full Kelly never the output on an imperfect probability model?
- Is every recommended `config.json` change backed by a specific figure pulled from the reviewed data (a win-rate bucket, a slippage distribution, an entry-price cohort) rather than a generic "seems reasonable" adjustment?
- Are cities with σ > 3.0F explicitly flagged for removal and cities with σ < 1.5F flagged as Kelly-increase candidates, using the thresholds this workflow itself sets in Phase 2-4?
- Does the updated `calibration.json` payload in Section 4 match the sigma values reported in Section 1 — no drift between the human-readable report and the machine-storage payload?

---

## When to Run This Workflow

| Trigger | Action |
|---------|--------|
| 30 resolved markets (first time) | Run full calibration — graduate from default sigma |
| Every 50 additional resolutions | Run incremental calibration update |
| Max drawdown exceeds 10% | Emergency calibration — check for systematic bias |
| New city added to rotation | Wait for 30 samples, then calibrate that city |
| Season change (equinox) | Run calibration — seasonal patterns shift sigma |
| After removing/adding forecast source | Re-calibrate all affected (city, source) pairs |

## Post-Calibration Actions

1. **Update `data/calibration.json`** with new sigma values (only where delta > 0.05)
2. **Update `config.json`** with recommended parameters (after manual review)
3. **Record calibration event** in the market log for audit trail
4. **Flag cities for removal** if sigma > 3.0F (2.0C) after 50+ samples
5. **Flag cities for Kelly increase** if sigma < 1.5F (0.8C) and win rate > 70%
6. **Re-run the Market Forecast & Edge Detection** workflow with updated parameters to see how the opportunity set changes
