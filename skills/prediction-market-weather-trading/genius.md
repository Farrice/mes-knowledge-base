# Weather Trading — Genius Context

> Load this file before any workflow. Every pattern below comes from the production weatherbot codebase (bot_v2.py, 1,050 lines). Parameters are actual values with the reasoning behind each one.

---

## How to Use This Skill (Model Calibration)

These patterns are intuition primitives, not a checklist to recite. Absorb the discipline — defensive defaults, sequential priority, information exits over price exits — then run the specific math for the specific trade. If the output mechanically narrates "now checking coordinate accuracy... now applying Kelly sizing... now setting the stop-loss," that is the failure mode: `scan_and_update()` never logs its own steps, it just executes them in order.

Specifically:
- Do NOT enumerate which genius patterns you applied unless asked. Name the filter, the threshold, the number — never the pattern label.
- Do NOT round or estimate a number the filter cascade depends on. EV, Kelly %, sigma, spread, and hours-to-resolution gate REJECT/ACCEPT decisions; a plausible-sounding fabricated number is worse than an honest "no data supplied."
- This system's texture is defensive-first, never swaggering. Every default starts conservative (quarter Kelly, $20 hard cap, $0.45 max price, SIGMA_F 2.0) and earns aggression only through 30+ resolved samples of calibration. Confident, round-number overreach before the data supports it — the "sounds like a trader" voice instead of the bot's own hedged, threshold-gated posture — is this skill's version of polish-is-the-tell: it signals someone using prediction-market vocabulary ("edge," "EV," "Kelly") without the filter cascade actually running underneath.
- The test: would the weatherbot's author recognize this output as the same disciplined, sequential decision pipeline that scans, filters, sizes, and exits in a fixed priority order — or as someone wearing trading vocabulary over a discretionary call? If it's the second, rebuild against the seven-filter cascade (`directives`-grade thresholds: EV ≥0.10, price <$0.45, volume ≥500, spread ≤$0.03, hours 2.0-72.0, size ≥$0.50), not against the terminology.

---

## 11 Genius Patterns

### 1. Airport Station Resolution Matching
Every city entry in the LOCATIONS dictionary uses exact ICAO station coordinates, not city center. NYC is `40.7772, -73.8726` (KLGA LaGuardia), not `40.7128, -74.0060` (Manhattan). Dallas is KDAL (Love Field), not KDFW — because Polymarket resolves on Love Field.

**Execute**: Before trading ANY market, identify the exact resolution source. Build a lookup mapping market slugs to station coordinates. Never use "city coordinates."

**Known mappings**:
| City | ICAO | Coordinates | Common Mistake |
|------|------|-------------|----------------|
| New York | KLGA | 40.7772, -73.8726 | Using Central Park or JFK (KJFK) |
| Chicago | KORD | 41.9742, -87.9073 | Using Midway (KMDW) |
| Miami | KMIA | 25.7959, -80.2870 | Using city center |
| Dallas | KDAL | 32.8471, -96.8518 | Using DFW (KDFW) — different station, different microclimate |
| London | EGLL | 51.4700, -0.4543 | Using city center Met Office readings |
| Tokyo | RJTT | 35.5494, 139.7798 | Using city center |
| Seoul | RKSS | 37.5586, 126.7906 | Using Incheon (RKSI) |

**Why the edge persists**: Casual traders use consumer weather apps. Resolution criteria are buried in fine print. Most people don't know what an ICAO code is. This is structural, not fleeting.

### 2. Tiered Forecast Source Selection
Three forecast sources are fetched but only ONE is used per trade — selected by geography and time horizon. The `best` field is set by deterministic priority:
- **HRRR > ECMWF** for US cities within 48 hours (`loc["region"] == "us" and snap["hrrr"] is not None`)
- **ECMWF** for everything else (international, or US beyond 48 hours)
- **METAR** is NEVER used as a forecast — only as a same-day observation anchor

All source values are stored in the forecast snapshot even when not selected. Data collection is decoupled from source selection.

### 3. Gaussian Bucket Probability with Edge/Center Split
The `bucket_prob()` function treats center buckets and edge buckets completely differently:
- **Center bucket** (e.g., "between 46-47F"): Returns `1.0` if forecast is inside, `0.0` if outside. Binary.
- **Edge bucket** ("or below" / "or higher"): Uses `norm_cdf()` with calibrated sigma for continuous probability.

**Why this matters**: Center buckets already have high confidence if the forecast is correct — sigma matters for tail risk. Edge buckets are where the real probability calculation happens because the forecast could easily be off 2-3 degrees and push into/out of the tail. This is why sigma calibration per city matters most for edge buckets.

### 4. Self-Calibrating Sigma Per City Per Source
After 30+ resolved markets (`CALIBRATION_MIN = 30`), the bot calculates Mean Absolute Error per city per forecast source and uses that as the new sigma:
```
mae = sum(abs(forecast - actual) for each resolved market) / count
```
The MAE becomes the new sigma, replacing the default `SIGMA_F = 2.0` (Fahrenheit) or `SIGMA_C = 1.2` (Celsius).

**Stability filter**: New sigma only replaces old if `abs(new - old) > 0.05`. Prevents noise from tiny fluctuations while still adapting to systematic bias.

**Why MAE not RMSE**: MAE is more robust to outliers. A single 10-degree miss doesn't distort the sigma the way RMSE would. For a Gaussian model where sigma controls position sizing, MAE is the conservative choice.

**Per-city, per-source granularity**: Chicago ECMWF might have sigma 1.8 while Chicago HRRR has sigma 1.5. Different forecast models have different accuracy profiles for different locations.

### 5. Fractional Kelly with Hard Cap
Three layers of position size protection:
```
Full Kelly: f = (p * b - (1 - p)) / b    where b = (1/ask - 1)
Fractional:  f_adj = f * KELLY_FRACTION   (0.25 = quarter Kelly)
Capped:      min(max(0, f_adj) * balance, MAX_BET)   (MAX_BET = $20)
Floored:     reject if < $0.50 (noise filter)
```

**Why 0.25 not 0.33**: Quarter Kelly reduces variance by ~75% versus full Kelly at ~75% of the growth rate. The developer knows Kelly is optimal only with perfect probability estimates, and theirs are imperfect. Conservative default earns its way to confidence through calibration.

**Why MAX_BET = $20**: At a $10K bankroll, $20 per position limits single loss to 0.2% of balance. Prevents ruin during the calibration phase when estimates are least reliable.

### 6. Three-Exit Position Management
Every open position has three independent exit mechanisms firing in priority order:

**Stop-loss** (price-based, downside protection): `entry * 0.80`. Hard floor. Non-negotiable. Fires in both `scan_and_update()` and `monitor_positions()`.

**Trailing stop** (price-based, profit protection): When price rises 20% above entry, stop moves to breakeven. Converts winners into risk-free positions. Note: moves only to breakeven, not higher — deliberately conservative.

**Forecast-change exit** (information-based, thesis invalidation): If forecast shifts 2+F (1+C) outside bucket + buffer, close immediately regardless of current price. This exits based on INFORMATION, not price.

**Why three**: Stop-loss alone lets you ride losers as the forecast deteriorates. Trailing alone doesn't protect against sudden gaps. Forecast-change alone doesn't protect against price manipulation or liquidity events. Together they cover price risk, profit risk, and information risk.

### 7. Time-Horizon Take-Profit Scaling
Take-profit thresholds scale with time to resolution:
- `hours_left < 24`: **No take-profit** — hold to resolution. Probability is converging.
- `hours_left 24-48`: Take profit at **$0.85**. Good enough; don't get greedy.
- `hours_left > 48`: Take profit at **$0.75**. High uncertainty; lock in gains.

Embedded in `monitor_positions()`. The further from resolution, the more uncertain, so take profits earlier.

### 8. Slippage-Aware Entry with Real Ask Verification
Two-pass pricing:
1. **Scan** with cached/event API prices for speed
2. **Verify** with real-time `bestAsk`/`bestBid` from individual market endpoint before execution

Trade is skipped if: real spread exceeds `MAX_SLIPPAGE = $0.03` OR real ask exceeds `MAX_PRICE = $0.45`. Never enter based on stale data.

### 9. Per-Market JSON Storage (Not Database)
Every market gets its own JSON file at `data/markets/{city}_{date}.json`. One file per market.

**Why**: (1) No database driver dependencies, (2) individual files inspectable in any text editor, (3) corrupt file affects one market not all, (4) `load_all_markets()` just globs `*.json`, (5) natural partitioning by city+date means no indexing needed.

### 10. Dual-Cadence Monitoring
- `MONITOR_INTERVAL = 600` (10 min): Stop-loss, trailing stop, take-profit checks. Cheap — one API call per open position.
- `SCAN_INTERVAL = 3600` (60 min): Full scan with forecast refresh, new entries, forecast-change exits. Expensive — 20 cities x 3 sources x 4 days.

Separates "is my position in danger?" (frequent, cheap) from "are there new opportunities?" (infrequent, expensive). Respects API rate limits while keeping risk management responsive.

### 11. v1-to-v2 Evolution as Architecture Pattern
v1 (~450 lines) is kept in the repo deliberately as a teaching tool. The evolution reveals what broke:
- Flat 5% sizing -> Kelly with hard cap (v1 blew up on bad trades)
- NWS-only -> ECMWF + HRRR + METAR (v1 missed international markets)
- No position management -> stop-loss + trailing + forecast-change exit
- No learning -> self-calibration
- Single simulation.json -> per-market storage (v1 corruption killed all data)

**Lesson**: Ship v1 fast, let it break, build v2 around the failures. No feature in v2 exists without a corresponding v1 failure.

---

## 8 Hidden Knowledge Items

### 1. Default Sigma Values Encode Climate Knowledge
`SIGMA_F = 2.0` and `SIGMA_C = 1.2` are NOT arbitrary. 2.0F is approximately the median 24-hour forecast error for major US airports from NWS/ECMWF. These are conservative — real MAE is often 1.5-1.8F — meaning the bot UNDER-estimates its edge until calibration kicks in. Intentional: better to miss trades than to oversize on overconfident probabilities.

### 2. Why max_price = 0.45
A contract at $0.45 pays 2.22x. But at that price, the market probability is ~45%, so edge is tiny. The bot's REAL edge is on mispriced cheap contracts — markets at $0.08-0.15 where true probability is 60-80%. At those prices, payoff is 6-12x. The filter forces the bot to only play where its edge is structurally large.

### 3. Why min_volume = 500
Low-volume markets have unreliable prices — the displayed price might be a single stale limit order. Markets under 500 volume are traps: you can get in but can't get out. v1 didn't have this filter. v2 does. (Learned the hard way.)

### 4. The 0.3-Second Sleep Between Cities
`time.sleep(0.3)` after fetching forecasts per city, `time.sleep(0.1)` after saving each market. These DON'T appear in the README. 0.3s per city across 20 cities = 6 seconds per scan — trivial against the 3600-second interval. Without it, the bot gets rate-limited or temporarily blocked after a few hours.

### 5. Why the Forecast-Change Exit Has a 2-Degree Buffer
The code doesn't just check if the forecast moved outside the bucket — it checks if the forecast moved `> (bucket_width + buffer)` from the midpoint. Buffer is 2F or 1C. This prevents whipsawing on forecasts that fluctuate by 1 degree between scans. Without the buffer: enter, see 1-degree shift, exit at loss, re-enter when it shifts back. The 2-degree buffer means "the forecast genuinely changed, this isn't noise."

### 6. Resolution Checking via Price, Not API Status
`check_market_resolved()` doesn't trust a "resolved" status field. It checks if `yes_price >= 0.95` (WIN) or `yes_price <= 0.05` (LOSS). Polymarket's API sometimes reports "closed" before final resolution, and the `closed` flag alone is unreliable. Price convergence to 0 or 1 is the robust resolution signal.

### 7. Connection Error Gets 60 Seconds, Not Retry
When `requests.exceptions.ConnectionError` fires in the main loop, the bot waits 60 seconds and continues — it doesn't retry immediately. Individual forecast API calls get 3 retries with 3-second waits. Two-tier resilience: transient failures at function level get retried; infrastructure failures at loop level get a cooldown. If the internet is down, retrying in 3 seconds won't help.

### 8. The Dashboard Exists Because Simulation Is the First Deployment
`sim_dashboard_repost.html` reads from `simulation.json`, not a live trading API. The developer's deployment path: simulate first, watch the dashboard, build confidence, THEN (maybe) connect to real execution. v1 starts with `SIM_BALANCE = 1000.0` and a `--live` flag off by default. v2 has no live execution at all — paper-only.

---

## Exemplars

### Exemplar 1: The Scan-and-Update Decision Pipeline
`scan_and_update()` — ~300 lines, the heart of the bot. Sequential priority architecture:
1. Load state + iterate all 20 cities
2. Fetch forecast snapshots D+0 through D+3 per city
3. Find Polymarket event per date
4. Check market storage — create if new, skip if resolved
5. **Record forecast + price snapshots REGARDLESS of trading** (data collection decoupled from trading)
6. If position exists: stop-loss -> trailing stop -> forecast-change exit (in that order)
7. If no position: find matching bucket -> check volume -> calc probability -> calc EV -> calc Kelly -> verify real ask -> open position
8. After all cities: auto-resolution on closed markets
9. Update balance, run calibration if threshold met

**Critical detail**: Single-bucket matching. The code finds exactly ONE bucket matching the forecast and trades only that. No spreading across multiple buckets — that creates hedged positions with reduced edge.

### Exemplar 2: The Self-Calibration System
`run_calibration()` + `get_sigma()`:
- For each (city, source) pair, collect resolved markets where that source had a forecast
- Compute `abs(forecast - actual)` for each, take the mean = new sigma
- Only update if `abs(new - old) > 0.05` (stability filter)
- 30-sample minimum = weeks of default sigma before calibration kicks in (deliberate cold-start protection)
- Per-city, per-source granularity captures different accuracy profiles per location

### Exemplar 3: The Position Management Trifecta
Three independent exit mechanisms, each addressing a different failure mode:
- **Stop-loss**: `entry * 0.80`. "I was wrong about the trade." Limits max loss to 20% of cost basis.
- **Trailing stop**: When up 20%, stop moves to breakeven. Converts winners into risk-free positions. Conservative — only moves to breakeven, not higher.
- **Forecast-change exit**: When underlying data changes, trade no longer makes sense. Exits on thesis invalidation regardless of price. The most sophisticated exit because it acts on NEW INFORMATION.

### Anti-Exemplar: The Naive Weather Bot
Every one of these mistakes is corrected in the weatherbot codebase:
- City center coordinates (3-8F systematic error on every trade)
- Single forecast source (no cross-validation, no outlier detection)
- Flat position sizing (5% of balance regardless of edge)
- No calibration (fixed sigma for all cities, all sources, all time)
- No position management (enter and hold to resolution)
- No slippage awareness (entering at cached prices, getting filled 5-10 cents worse)
- Single monolithic state file (corruption kills everything)

---

## Anti-Patterns (Sourced from Production Codebase)

> Every item below is corrected in `alteregoeth-ai/weatherbot` bot_v2.py — cataloged verbatim in the MES 3.0 extraction dossier's "Anti-Exemplar: The Naive Weather Bot" and "Red Flags (Immediate Stop)" sections. Extraction date: 2026-04-13/2026-04-14 (see `git log` on the source files). A quote you cannot find in these files is UNCONFIRMED, never anchored — the two lists below are the full set that IS anchored.

- **City-center coordinates**: "Using `40.7128, -74.0060` for NYC instead of `40.7772, -73.8726` (LaGuardia). 3-8F error on every trade. Guaranteed losers on 1-2F bucket markets." — Source: `extractions/prediction-market-trading/weatherbot-extraction.md`, "Anti-Exemplar: The Naive Weather Bot" (2026-04-13 extraction).
- **Single forecast source**: "Using only NWS or only ECMWF. No cross-validation. No way to know when a forecast is an outlier." — Source: `extractions/prediction-market-trading/weatherbot-extraction.md`, same section.
- **Flat position sizing**: "5% of balance per trade regardless of edge. A 90% probability trade and a 55% probability trade get the same size. This is either too aggressive on weak edges or too conservative on strong ones." — Source: `extractions/prediction-market-trading/weatherbot-extraction.md`, same section.
- **No calibration**: "Using a fixed sigma of 2.0 for all cities, all sources, all time. Ignoring that Miami forecasts are more accurate than Seattle forecasts." — Source: `extractions/prediction-market-trading/weatherbot-extraction.md`, same section.
- **No position management**: "Enter and hold to resolution. No stop-loss, no exits. If the forecast changes dramatically, you're stuck." — Source: `extractions/prediction-market-trading/weatherbot-extraction.md`, same section.
- **No slippage awareness**: "Entering at cached prices without checking the real ask. Getting filled 5-10 cents worse than expected." — Source: `extractions/prediction-market-trading/weatherbot-extraction.md`, same section.
- **Single monolithic state file**: "One `simulation.json` for all markets. Corruption kills everything. Debugging requires reading the entire file." — Source: `extractions/prediction-market-trading/weatherbot-extraction.md`, same section.
- **LLM touching execution credentials**: "The LLM never touches API keys, wallet credentials, or order execution. This separation is non-negotiable — it prevents prompt injection from draining funds." (stated as the positive rule; the anti-pattern is its inverse, listed explicitly as "Letting the LLM touch wallet credentials" under Red Flags). — Source: `extractions/prediction-market-trading/weather-trading-extraction.md`, "Two-Layer Architecture" + "Red Flags (Immediate Stop)" sections (2026-04-14 extraction).
- **Sizing above quarter-to-third Kelly**: "NEVER recommend above 0.33 (one-third Kelly)," paired with the Red Flag "Using full Kelly (1.0 fraction) on weather markets." Imperfect probability estimates make full Kelly a ruin risk, not an edge. — Source: `extractions/prediction-market-trading/weatherbot-extraction.md`, Crown Jewel 5 ("Weather Bot Config Optimizer"); `extractions/prediction-market-trading/weather-trading-extraction.md`, "Red Flags (Immediate Stop)" section.

---

## 7 Signature Moves

1. **Airport-First Thinking**: Before looking at any market data, identify the exact ICAO station code. The LOCATIONS dictionary is organized around stations, not cities.

2. **Defensive Defaults, Aggressive Learning**: Every parameter starts conservative (sigma 2.0, quarter Kelly, $20 max, $0.45 max price). The system learns more aggressive parameters through calibration. Never starts optimistic.

3. **Data Collection Decoupled from Trading**: Forecast and price snapshots recorded for EVERY market on EVERY scan, regardless of whether a position is opened. Builds calibration dataset on markets the bot doesn't trade.

4. **Two-Pass Price Verification**: Scan with cached prices, verify with real-time prices before execution. Verification has its own slippage and price filters that can reject the trade even after the scan approved it.

5. **Information Exits Over Price Exits**: Forecast-change exit is unique to this codebase. Most bots exit only on price. This developer exits on thesis invalidation — when underlying data changes, exit regardless of current price.

6. **Explicit v1-to-v2 Evolution Path**: Both versions kept in repo. "Here's the simple version that works, here's the complex version that wins." Builds in layers, not from scratch.

7. **Simulation-First Deployment**: Entire system defaults to paper trading. Dashboard visualizes simulated results. Watch the bot trade fake money until you trust it, then (maybe) connect real money. v2 doesn't even HAVE a live trading mode.

---

## Quality Rubric

| Criterion | Score 4 (Acceptable) | Score 7 (Good) | Score 10 (Savant) |
|-----------|---------------------|----------------|-------------------|
| **Coordinate Accuracy** | Uses city name, general coords | Airport coordinates for major cities | Exact ICAO station coords verified against resolution source; 20-city lookup table |
| **Forecast Source Selection** | Single source | Multiple sources, manual selection | Three sources with automatic geographic/horizon selection; HRRR for US short-range, ECMWF global, METAR real-time |
| **Probability Model** | Fixed probability or threshold | Gaussian with static sigma | Gaussian with self-calibrating per-city per-source sigma; separate edge/center bucket handling |
| **Position Sizing** | Flat percentage | Kelly criterion | Fractional Kelly (0.25) with hard dollar cap ($20), min size floor ($0.50), EV threshold filter (0.10) |
| **Risk Management** | Stop-loss only | Stop-loss + trailing | Stop-loss + trailing + forecast-change exit + time-horizon take-profit + slippage filter |
| **Data Architecture** | In-memory only | Single state file | Per-market JSON files with forecast snapshots, market snapshots, position history, resolution data |
| **Operational Resilience** | Crashes on API error | Retries with backoff | Three-level: function retries (3x/3s), loop cooldown (60s), dual-cadence monitoring (10min/60min) |
| **Calibration** | No learning | Manual parameter tuning | Automatic after 30+ samples; per-city per-source sigma; 0.05 change threshold for stability |

---

## Complete Configuration Reference

| Parameter | Value | Reasoning |
|-----------|-------|-----------|
| `KELLY_FRACTION` | 0.25 | Quarter Kelly — 75% growth rate at 50% drawdown vs full Kelly |
| `MAX_BET` | $20.00 | 0.2% of $10K bankroll. Scale only after 50+ profitable trades |
| `MIN_EV` | 0.10 | 10% minimum expected value. Below this, fees + slippage eat the edge |
| `MAX_PRICE` | $0.45 | Forces bot into high-payoff cheap contracts ($0.08-$0.15 sweet spot) |
| `MIN_VOLUME` | 500 | Liquidity floor. Below this, prices are stale limit orders |
| `MAX_SLIPPAGE` | $0.03 | Maximum spread between scan price and execution price |
| `MIN_HOURS` | 2.0 | Below 2h, METAR observations are public and market is efficient |
| `MAX_HOURS` | 72.0 | Beyond 3 days, forecast skill degrades dramatically |
| `SIGMA_F` | 2.0 | Default Fahrenheit sigma (median 24h forecast error at US airports) |
| `SIGMA_C` | 1.2 | Default Celsius sigma (equivalent metric) |
| `CALIBRATION_MIN` | 30 | Minimum resolved markets before trusting learned sigma |
| `MONITOR_INTERVAL` | 600 (10 min) | Stop-loss / trailing / take-profit check frequency |
| `SCAN_INTERVAL` | 3600 (60 min) | Full scan with forecast refresh frequency |
| `STOP_LOSS` | entry * 0.80 | 20% max loss per position |
| `TRAIL_ACTIVATION` | entry * 1.20 | 20% gain triggers trailing stop to breakeven |
| `TP_48H_PLUS` | $0.75 | Take-profit when 48+ hours to resolution |
| `TP_24_48H` | $0.85 | Take-profit when 24-48 hours to resolution |
| `TP_UNDER_24H` | HOLD | No take-profit — hold to resolution |
| `FORECAST_BUFFER_F` | 2.0 | Degrees F forecast must move beyond bucket before exit |
| `FORECAST_BUFFER_C` | 1.0 | Degrees C forecast must move beyond bucket before exit |
| `SIGMA_UPDATE_THRESHOLD` | 0.05 | Minimum change to update calibrated sigma |
| `API_SLEEP_PER_CITY` | 0.3s | Rate limiting between forecast fetches |
| `API_SLEEP_PER_SAVE` | 0.1s | Rate limiting between market file saves |
| `RETRY_COUNT` | 3 | API call retries at function level |
| `RETRY_WAIT` | 3s | Wait between retries |
| `LOOP_COOLDOWN` | 60s | Wait after infrastructure-level connection errors |
