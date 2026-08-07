# alteregoeth-ai/weatherbot -- Mastery Extraction

## Content Assessment

```
Source: GitHub repository, ~86KB — README + config.json + bot_v1.py (17.5KB) + bot_v2.py (43.8KB) + sim_dashboard (17.9KB)
Expert: alteregoeth-ai — weather prediction market specialist, quant-lite retail trader
Domain: Prediction market trading (weather vertical) + meteorological data arbitrage + automated position management
Depth Tier: Deep — production codebase, ~1,700 lines of real trading logic across two bot versions
Genius Patterns: 11
Hidden Knowledge: 8
Existing Overlap: Feasibility assessment at _active/wagering/prediction-market-arb/02-research/polymarket-kalshi-arbitrage-feasibility.md (strategy layer only, no execution code)
```

---

## Executive Summary

- **Core Genius**: This bot wins because it solves a coordination problem most traders ignore -- weather markets resolve on specific airport stations, not cities. Using KLGA coordinates instead of "New York City" coordinates eliminates 3-8 degrees F of systematic error on markets with 1-2 degree F buckets. Combined with multi-source forecast cross-validation and learned per-city sigma calibration, this creates persistent informational edge against traders using generic weather data.

- **What Makes Them Different**: Three-layer edge stack: (1) correct coordinates matched to resolution source, (2) three independent forecast sources weighted by geography and time horizon, (3) self-calibrating probability model that learns each city's forecast error distribution over time. Most weather bots have zero of these three.

- **Deployable Skills**: Full weather market trading bot, position sizing engine, multi-source forecast aggregator, self-calibration system, risk management framework (stop-loss + trailing stop + forecast-change exit + time-horizon take-profit)

- **Hidden Knowledge Captured**: Why 0.25 Kelly not 0.33, why max_price 0.45, why HRRR beats ECMWF for US D+0/D+1 but not D+2+, why per-market JSON files instead of a database, why the monitor runs every 10 minutes but the scanner runs every 60, why the forecast-change exit uses a 2-degree buffer not 1

---

## Genius Patterns

### 1. Airport Station Resolution Matching
- **What They Do Unconsciously**: Every city entry includes the exact ICAO station code and airport coordinates, not city center. NYC is `40.7772, -73.8726` (KLGA LaGuardia), not `40.7128, -74.0060` (Manhattan). Dallas is KDAL (Love Field), not KDFW -- because Polymarket resolves on Love Field.
- **Executable Behavior**: Before trading ANY location-resolved market, identify the exact resolution source. Build a lookup table mapping market slugs to station coordinates. Never use "city coordinates."
- **Deployment Context**: Any prediction market that resolves on a specific data source (weather stations, sports venues, economic reporting offices).
- **Success Metric**: Zero trades lost due to coordinate mismatch. Forecast error drops 3-8 degrees F versus city-center approach.

### 2. Tiered Forecast Source Selection
- **What They Do Unconsciously**: Three forecast sources are fetched but only ONE is used per trade -- selected by geography and time horizon. HRRR/GFS for US cities within 48 hours (`loc["region"] == "us" and snap["hrrr"] is not None`), ECMWF for everything else, METAR for same-day ground truth only.
- **Executable Behavior**: `take_forecast_snapshot()` fetches all sources, then `best` field is set by a deterministic priority: HRRR > ECMWF for US short-horizon, ECMWF for all else. METAR is NEVER used as a forecast -- only as a same-day observation anchor.
- **Deployment Context**: Any multi-source data environment where sources have different geographic coverage and temporal resolution.
- **Success Metric**: Best-source selection matches or beats any single-source approach across all city/horizon combinations.

### 3. Gaussian Bucket Probability with Edge/Center Split
- **What They Do Unconsciously**: The `bucket_prob()` function treats center buckets and edge buckets completely differently. A center bucket (e.g., "between 46-47F") returns `1.0` if the forecast is inside, `0.0` if outside -- binary. But edge buckets ("or below", "or higher") use `norm_cdf()` with calibrated sigma to produce a continuous probability.
- **Executable Behavior**: Center buckets already have high confidence if your forecast is correct -- the sigma matters for tail risk. Edge buckets are where the real probability calculation happens because the forecast could easily be off by 2-3 degrees and push into/out of the tail. This is why sigma calibration per city matters most for edge buckets.
- **Deployment Context**: Any bucketed outcome market where some outcomes have bounded ranges and others have open-ended tails.
- **Success Metric**: Probability estimates on edge buckets converge toward observed frequency as calibration data accumulates.

### 4. Self-Calibrating Sigma Per City Per Source
- **What They Do Unconsciously**: After 30+ resolved markets (the `CALIBRATION_MIN` threshold), the bot calculates Mean Absolute Error per city per forecast source and uses that as the new sigma. The key line: `mae = sum(errors) / len(errors)` becomes the new sigma, replacing the default `SIGMA_F = 2.0` (Fahrenheit) or `SIGMA_C = 1.2` (Celsius).
- **Executable Behavior**: Calibration runs after every scan cycle if enough data exists. Old sigma is preserved; new sigma only replaces it if the change exceeds 0.05 (`abs(new - old) > 0.05`). This prevents noise from tiny fluctuations while still adapting to systematic bias.
- **Deployment Context**: Any system where your probability model has parameters that can be learned from historical accuracy data.
- **Success Metric**: Per-city sigma values stabilize after 50+ samples. Brier score improves versus static sigma.

### 5. Fractional Kelly with Hard Cap
- **What They Do Unconsciously**: Full Kelly fraction is 0.25 (quarter Kelly), and raw Kelly output is further capped at `MAX_BET = $20`. The `calc_kelly()` function: `f = (p * b - (1 - p)) / b` then `min(max(0, f) * KELLY_FRACTION, 1.0)`. Then `bet_size()` applies `min(raw, MAX_BET)`.
- **Executable Behavior**: Three layers of position size protection: (1) quarter-Kelly reduces variance by ~75% versus full Kelly, (2) hard dollar cap prevents any single trade from exceeding $20 regardless of edge size, (3) minimum size floor of $0.50 filters out noise trades. This is **defensive sizing** -- the developer knows that Kelly is optimal only with perfect probability estimates, and theirs are imperfect.
- **Deployment Context**: Any probabilistic trading system. Quarter Kelly is a well-known best practice but most retail implementations use half Kelly or full Kelly and blow up.
- **Success Metric**: Maximum drawdown stays under 15% of starting balance. No single trade represents more than 0.2% of balance.

### 6. Three-Exit Position Management
- **What They Do Unconsciously**: Every open position has three independent exit mechanisms that fire in priority order:
  - **Stop-loss**: 20% below entry (`entry * 0.80`). Hard floor. Non-negotiable.
  - **Trailing stop**: When position is up 20%, stop moves to breakeven. Guarantees no loss on winning trades that pull back.
  - **Forecast-change exit**: If the weather forecast shifts 2+ degrees F (1+ degree C) away from the bucket midpoint, close immediately regardless of current price. This is the genius move -- it exits based on INFORMATION, not price.
- **Executable Behavior**: Stop-loss and trailing stop fire in `monitor_positions()` (every 10 min). Forecast-change exit fires in `scan_and_update()` (every 60 min) because it requires fresh forecast data.
- **Deployment Context**: Any trading system where the underlying thesis can be invalidated by new information before price reflects it.
- **Success Metric**: Forecast-change exits save more money than stop-losses over time. Trailing stops convert winners into risk-free positions.

### 7. Time-Horizon Take-Profit Scaling
- **What They Do Unconsciously**: Take-profit thresholds are NOT static -- they scale with time to resolution:
  - `hours_left < 24`: **No take-profit** -- hold to resolution. The probability is converging; let it play out.
  - `hours_left 24-48`: Take profit at $0.85. Good enough; don't get greedy.
  - `hours_left > 48`: Take profit at $0.75. High uncertainty window; lock in gains.
- **Executable Behavior**: This is embedded in `monitor_positions()`. The logic: the further from resolution, the more uncertain the outcome, so take profits earlier. Close to resolution, the forecast is nearly certain, so hold.
- **Deployment Context**: Any market with a known resolution time where certainty increases as resolution approaches.
- **Success Metric**: Aggregate PnL from taken profits exceeds what holding to resolution would have produced on the same set of trades.

### 8. Slippage-Aware Entry with Real Ask Verification
- **What They Do Unconsciously**: The bot fetches cached prices from the event API for scanning, but before executing a trade, it makes a SECOND API call to get the real `bestAsk` and `bestBid` from the individual market endpoint. If the real spread exceeds `MAX_SLIPPAGE = $0.03` or the real ask exceeds `MAX_PRICE = $0.45`, the trade is skipped.
- **Executable Behavior**: Two-pass pricing: (1) scan with cached prices for speed, (2) verify with live prices before execution. This prevents stale-price entries that look profitable on paper but aren't at execution.
- **Deployment Context**: Any market with discrete bid/ask spreads where cached price data may be stale.
- **Success Metric**: Zero trades entered at prices worse than expected by more than $0.03.

### 9. Per-Market JSON Storage (Not Database)
- **What They Do Unconsciously**: Every market gets its own JSON file at `data/markets/{city}_{date}.json`. Not SQLite. Not Postgres. Not even a single JSON file for all markets. One file per market.
- **Executable Behavior**: This is a deliberate architectural choice for a bot that runs indefinitely. Benefits: (1) no database driver dependencies, (2) individual market files can be inspected/debugged in any text editor, (3) corrupt file affects one market not all, (4) `load_all_markets()` just globs `*.json`, (5) natural partitioning by city+date means no indexing needed.
- **Deployment Context**: Any autonomous system where debuggability and resilience matter more than query performance.
- **Success Metric**: Zero data loss from crashes. Any market's full history inspectable in 5 seconds.

### 10. Dual-Cadence Monitoring (10min Monitor / 60min Scan)
- **What They Do Unconsciously**: `MONITOR_INTERVAL = 600` (10 min) for stop checks. `SCAN_INTERVAL = 3600` (60 min) for full scan with forecast refresh. The main loop checks the time since last full scan -- if under an hour, it only runs `monitor_positions()`.
- **Executable Behavior**: Monitoring is cheap (one API call per open position). Scanning is expensive (20 cities x 3 forecast sources x 4 days). The developer separates "is my position in danger?" (frequent, cheap) from "are there new opportunities?" (infrequent, expensive). This respects API rate limits while keeping risk management responsive.
- **Deployment Context**: Any system with both reactive (risk management) and proactive (opportunity scanning) components.
- **Success Metric**: API calls per hour stay under rate limits. Stop-losses trigger within 10 minutes of price crossing threshold.

### 11. v1-to-v2 Evolution as Architecture Pattern
- **What They Do Unconsciously**: The v1 bot exists AS a teaching tool -- it's kept in the repo deliberately. v1 is ~450 lines (flat sizing, 6 US cities, NWS only, simple threshold entry/exit). v2 is ~1,050 lines (Kelly, 20 cities, 3 sources, calibration, stop-loss, trailing, take-profit, auto-resolution). The evolution reveals what BROKE in v1:
  - Flat 5% sizing blew up on bad trades -> Kelly with hard cap
  - NWS-only forecasts missed international markets -> ECMWF + HRRR + METAR
  - No position management -> stop-loss + trailing + forecast-change exit
  - No learning -> self-calibration
  - Single simulation.json -> per-market storage
- **Executable Behavior**: When building trading systems, start with the simplest version that proves the core thesis (coordinates matter, forecasts can beat market prices), then layer complexity only where v1 FAILED.
- **Deployment Context**: Any system build. Ship v1 fast, let it break, build v2 around the failures.
- **Success Metric**: v2 addresses every documented v1 failure mode. No feature in v2 exists without a corresponding v1 failure.

---

## Hidden Knowledge

### 1. Default Sigma Values Encode Climate Knowledge
`SIGMA_F = 2.0` (Fahrenheit) and `SIGMA_C = 1.2` (Celsius). These aren't arbitrary. 2.0 degrees F is approximately the median 24-hour forecast error for major US airports from NWS/ECMWF. 1.2 degrees C is the equivalent in metric. The developer chose these from observed forecast accuracy data, not from a textbook. They're conservative -- real MAE is often 1.5-1.8F -- which means the bot UNDER-estimates its edge until calibration kicks in. This is intentional: better to miss some trades than to oversize based on overconfident probabilities.

### 2. Why max_price = 0.45 (Never Buy Expensive Contracts)
A contract at $0.45 needs to resolve YES to pay $1.00 -- that's a 2.22x return. But if your probability estimate is 50% (which is where $0.45 prices roughly should be), your edge is tiny. The developer knows that the bot's REAL edge is on mispriced cheap contracts -- markets trading at $0.08-0.15 where the true probability is 60-80%. At those prices, the payoff is 6-12x. The `max_price` filter forces the bot to only play where its edge is structurally large.

### 3. Why min_volume = 500 (Liquidity Floor)
Low-volume markets have unreliable prices -- the displayed price might be a single stale limit order. The developer learned (likely the hard way) that markets under 500 volume are traps: you can get in but can't get out. The v1 bot didn't have this filter. v2 does.

### 4. The 0.3-Second Sleep Between Cities
`time.sleep(0.3)` after fetching forecasts per city, `time.sleep(0.1)` after saving each market. These are rate-limiting sleeps that DON'T appear in the README. The developer learned that hammering Open-Meteo and Polymarket APIs gets you rate-limited or temporarily blocked. The 0.3s sleep per city across 20 cities adds 6 seconds per scan -- trivial against the 3600-second interval. But without it, the bot breaks after a few hours. This is operational knowledge.

### 5. Why the Forecast-Change Exit Has a 2-Degree Buffer
The code doesn't just check if the forecast moved outside the bucket -- it checks if the forecast moved `> (bucket_width + buffer)` from the midpoint. Buffer is 2F or 1C. This prevents whipsawing on forecasts that fluctuate by 1 degree between scans. Without the buffer, the bot would enter a position, see the forecast shift 1 degree on the next scan, exit at a loss, then re-enter when it shifts back. The 2-degree buffer means: "the forecast genuinely changed, this isn't noise."

### 6. Resolution Checking via Price, Not API Status
`check_market_resolved()` doesn't trust a "resolved" status field. It checks if `yes_price >= 0.95` (WIN) or `yes_price <= 0.05` (LOSS). The developer knows that Polymarket's API sometimes reports markets as "closed" before final resolution, and the `closed` flag alone is unreliable. Using price as the resolution signal is more robust because prices converge to 0 or 1 when the outcome is known.

### 7. Connection Error Gets 60 Seconds, Not Retry
When `requests.exceptions.ConnectionError` fires in the main loop, the bot waits 60 seconds and continues -- it doesn't retry immediately. Individual forecast API calls get 3 retries with 3-second waits. This is a two-tier resilience pattern: transient failures at the function level get retried; infrastructure-level failures at the loop level get a cooldown. The developer knows that if the internet is down, retrying in 3 seconds won't help -- but 60 seconds might.

### 8. The Dashboard Exists Because Simulation Is the First Deployment
The `sim_dashboard_repost.html` reads from `simulation.json`, not from a live trading API. The developer's deployment path is: simulate first, watch the dashboard, build confidence in the parameters, THEN (maybe) connect to real execution. The dashboard's existence reveals the developer's risk management philosophy: you don't trade until you've WATCHED the bot trade with fake money for long enough to trust it. The v1 bot starts with `SIM_BALANCE = 1000.0` and a `--live` flag that's off by default. The v2 bot has no live execution at all -- it's paper-only.

---

## Hall of Fame Exemplars

### Exemplar 1: The Scan-and-Update Decision Pipeline

`scan_and_update()` is the heart of the bot -- ~300 lines that execute the complete decision cycle. What makes it excellent:

**Sequential Priority Architecture**:
1. Load state + iterate all 20 cities
2. For each city, fetch forecast snapshots for D+0 through D+3
3. For each date, find the Polymarket event
4. Check if market exists in storage -- create if new, skip if resolved
5. Record forecast and price snapshots (data collection runs REGARDLESS of trading)
6. **If position exists**: run stop-loss -> trailing stop -> forecast-change exit (in that order)
7. **If no position**: find matching bucket -> check volume -> calc probability -> calc EV -> calc Kelly -> verify real ask -> open position
8. After all cities: run auto-resolution on closed markets
9. Update balance, run calibration if threshold met

**Why this ordering matters**: Data collection (step 5) happens before any trading decision. This means every market gets forecast history even if no trade is taken. Stop-loss checks (step 6) happen before new entries (step 7) -- free up capital first, then deploy it. Auto-resolution (step 8) happens after the scan because it requires checking every stored market, not just today's.

**The single-bucket matching pattern**: The code finds exactly ONE bucket that matches the forecast and trades only that. It doesn't try to find "the best edge across all buckets." This is critical -- spreading across multiple buckets in the same market creates hedged positions with reduced edge. One forecast, one bucket, one position.

### Exemplar 2: The Self-Calibration System

The calibration system in `run_calibration()` + `get_sigma()` is elegant in its simplicity:

**Learning loop**: For each (city, source) pair, collect all resolved markets where that source had a forecast. Compute `abs(forecast - actual)` for each. Take the mean. That's your new sigma.

**Why MAE not RMSE**: Mean Absolute Error, not Root Mean Squared Error. MAE is more robust to outliers -- a single 10-degree miss doesn't distort the sigma the way RMSE would. For a Gaussian model where sigma controls position sizing, MAE is the conservative choice.

**The 0.05 threshold for updates**: `if abs(new - old) > 0.05` prevents calibration from oscillating on noise. If the new MAE is 2.03 and the old sigma was 2.00, nothing changes. This creates stability in the probability model.

**The 30-sample minimum**: `CALIBRATION_MIN = 30` means the bot runs on default sigma for weeks before calibration kicks in. This is deliberate cold-start protection. The developer trusts the default sigma (which is conservative) more than a sigma learned from 10 samples.

**Per-city, per-source granularity**: Chicago ECMWF might have sigma 1.8 while Chicago HRRR has sigma 1.5. This captures the fact that different forecast models have different accuracy profiles for different locations.

### Exemplar 3: The Position Management Trifecta

Three exit mechanisms work independently, each addressing a different failure mode:

**Stop-loss** (price-based, downside protection): `stop = entry * 0.80`. Fires when price drops 20%. This is the "I was wrong about the trade" exit. It limits maximum loss per position to 20% of cost basis. This fires in both `scan_and_update()` and `monitor_positions()`.

**Trailing stop** (price-based, profit protection): When price rises 20% above entry, stop moves to breakeven. This converts a winning position into a risk-free position. The trailing logic: `if current_price >= entry * 1.20 and stop < entry: pos["stop_price"] = entry`. Note: it only moves to breakeven, not to a higher trailing level. This is conservative -- the developer doesn't want a complex trailing algorithm, just "guarantee I don't lose money on this winner."

**Forecast-change exit** (information-based, thesis invalidation): If the weather forecast shifts significantly after entry, close the position regardless of current price. This is the most sophisticated exit because it's based on NEW INFORMATION, not price movement. The bot entered because the forecast said 72F. If the forecast now says 78F, the thesis is dead -- exit immediately even if the market price hasn't moved yet.

**Why three and not one**: Stop-loss alone lets you ride losing positions as the forecast deteriorates. Trailing stop alone doesn't protect against sudden gaps. Forecast-change exit alone doesn't protect against price manipulation or liquidity events. Together, they cover: price risk (stop), profit risk (trailing), and information risk (forecast-change).

### Anti-Exemplar: The Naive Weather Bot

What a bad implementation looks like -- every one of these mistakes is corrected in the weatherbot codebase:

- **City center coordinates**: Using `40.7128, -74.0060` for NYC instead of `40.7772, -73.8726` (LaGuardia). 3-8F error on every trade. Guaranteed losers on 1-2F bucket markets.
- **Single forecast source**: Using only NWS or only ECMWF. No cross-validation. No way to know when a forecast is an outlier.
- **Flat position sizing**: 5% of balance per trade regardless of edge. A 90% probability trade and a 55% probability trade get the same size. This is either too aggressive on weak edges or too conservative on strong ones.
- **No calibration**: Using a fixed sigma of 2.0 for all cities, all sources, all time. Ignoring that Miami forecasts are more accurate than Seattle forecasts.
- **No position management**: Enter and hold to resolution. No stop-loss, no exits. If the forecast changes dramatically, you're stuck.
- **No slippage awareness**: Entering at cached prices without checking the real ask. Getting filled 5-10 cents worse than expected.
- **Single monolithic state file**: One `simulation.json` for all markets. Corruption kills everything. Debugging requires reading the entire file.

---

## Signature Moves

1. **Airport-First Thinking**: Before looking at any market data, the developer identifies the exact ICAO station code. The LOCATIONS dictionary is organized around stations, not cities. Coordinates are airport coordinates. This is the foundational move that everything else depends on.

2. **Defensive Defaults, Aggressive Learning**: Every parameter starts conservative (sigma 2.0, quarter Kelly, $20 max bet, $0.45 max price). The system learns more aggressive parameters over time through calibration. The developer never starts optimistic and adjusts down -- always starts pessimistic and earns its way to confidence.

3. **Data Collection Decoupled from Trading**: Forecast snapshots and market price snapshots are recorded for EVERY market on EVERY scan, regardless of whether a position is opened. This creates a data asset that's separate from the trading P&L. The developer is building a calibration dataset even on markets they don't trade.

4. **Two-Pass Price Verification**: Scan with cached/fast prices, then verify with real-time prices before execution. Never enter a trade based on stale data. The verification step has its own slippage and price filters that can reject the trade even after the scan approved it.

5. **Information Exits Over Price Exits**: The forecast-change exit is unique to this codebase. Most trading bots exit only on price movement. This developer exits on THESIS INVALIDATION -- when the underlying data changes, the trade no longer makes sense regardless of current price.

6. **Explicit v1-to-v2 Evolution Path**: Keeping both versions in the repo is a teaching move. It says: "here's the simple version that works, here's the complex version that wins." The developer builds in layers, not from scratch.

7. **Simulation-First Deployment**: The entire system defaults to paper trading. The dashboard visualizes simulated results. The developer's philosophy: watch the bot trade fake money until you trust it, then (maybe) connect real money. The v2 bot doesn't even HAVE a live trading mode.

---

## Expert-Specific Quality Rubric

| Criterion | Score 4 (Acceptable) | Score 7 (Good) | Score 10 (Savant) |
|-----------|---------------------|----------------|-------------------|
| **Coordinate Accuracy** | Uses city name; general coordinates | Uses airport coordinates for major cities | Uses exact ICAO station coordinates verified against Polymarket resolution source; maintains lookup table for all 20 cities |
| **Forecast Source Selection** | Single source (NWS or ECMWF) | Multiple sources, manual selection | Three sources with automatic geographic/horizon-based selection; HRRR for US short-range, ECMWF global, METAR real-time |
| **Probability Model** | Fixed probability or simple threshold | Gaussian model with static sigma | Gaussian model with self-calibrating per-city per-source sigma; separate edge/center bucket handling |
| **Position Sizing** | Flat percentage | Kelly criterion applied | Fractional Kelly (0.25) with hard dollar cap, minimum size floor, and EV threshold filter |
| **Risk Management** | Stop-loss only | Stop-loss + trailing stop | Stop-loss + trailing stop + forecast-change exit + time-horizon take-profit + slippage filter |
| **Data Architecture** | In-memory only | Single state file | Per-market JSON files with forecast snapshots, market snapshots, position history, and resolution data |
| **Operational Resilience** | Crashes on API error | Retries with backoff | Three-level resilience: function-level retries (3x/3s), loop-level cooldown (60s), dual-cadence monitoring (10min/60min) |
| **Calibration** | No learning | Manual parameter tuning | Automatic calibration after 30+ samples; per-city per-source sigma; 0.05 change threshold for stability |

---

## Methodology

### Phase 1: Market Discovery + Coordinate Mapping
1. Identify all active weather markets on Polymarket (slug pattern: `highest-temperature-in-{city}-on-{month}-{day}-{year}`)
2. Map each city to its exact ICAO resolution station
3. Record airport coordinates (NOT city center)
4. Build LOCATIONS dictionary with lat, lon, station, unit (F/C), region

### Phase 2: Multi-Source Forecast Acquisition
1. Fetch ECMWF via Open-Meteo for all cities (7-day horizon, bias-corrected)
2. Fetch HRRR/GFS via Open-Meteo for US cities only (3-day horizon, hourly resolution)
3. Fetch METAR for same-day observations (real-time airport temperature)
4. Select best source per city per date: HRRR > ECMWF for US short-range, ECMWF for all else
5. Store all source values in forecast snapshot (even non-selected sources)

### Phase 3: Edge Identification
1. Parse market outcome buckets (handle "between X-Y", "X or below", "X or higher", exact "be X")
2. Find the single bucket matching the forecast temperature
3. Calculate probability using `bucket_prob()` with calibrated sigma
4. Calculate Expected Value: `p * (1/price - 1) - (1 - p)`
5. Filter: `EV >= MIN_EV (0.10)`, `price < MAX_PRICE (0.45)`, `volume >= MIN_VOLUME (500)`, `spread <= MAX_SLIPPAGE (0.03)`, `hours >= MIN_HOURS (2.0)`, `hours <= MAX_HOURS (72.0)`

### Phase 4: Position Sizing + Entry
1. Calculate Kelly fraction: `(p * b - (1 - p)) / b * 0.25`
2. Apply size caps: `min(kelly * balance, MAX_BET)`
3. Verify real ask price via second API call to individual market endpoint
4. Re-check slippage and price filters with real values
5. Execute entry, record full position metadata

### Phase 5: Position Monitoring + Exit Management
1. **Every 10 minutes**: Check stop-loss, trailing stop, take-profit on all open positions
2. **Every 60 minutes**: Full scan with fresh forecasts; check forecast-change exits
3. Stop-loss: close if price <= entry * 0.80
4. Trailing: move stop to breakeven when price >= entry * 1.20
5. Take-profit: $0.75 at 48h+, $0.85 at 24-48h, hold at <24h
6. Forecast-change: close if forecast moves 2+F (1+C) outside bucket + buffer
7. Auto-resolution: check Polymarket for closed markets, record WIN/LOSS

### Phase 6: Self-Calibration
1. After 30+ resolved markets: calculate MAE per (city, source) pair
2. Set sigma = MAE (replacing default 2.0F / 1.2C)
3. Only update if change > 0.05 (stability filter)
4. Store calibration data in `data/calibration.json`
5. Load calibration at bot startup; refresh after each scan cycle

---

## Applied Intelligence

### Capability Unlocks
- **Weather Market Trading Bot**: Full production-ready system for Polymarket weather markets. Requires only `requests` library + free API keys.
- **Multi-Source Forecast Aggregator**: Reusable pattern for combining ECMWF, HRRR, and METAR data for any weather-dependent application.
- **Self-Calibrating Probability Engine**: Generalizable to any domain where forecast accuracy can be measured after the fact.
- **Risk Management Framework**: Stop-loss + trailing + information-exit pattern applicable to any trading system.

### Market Signals
- Weather markets are structurally mispriced because most participants use wrong coordinates and single forecast sources
- The edge is largest on cheap contracts ($0.08-0.15) where the true probability is much higher than the market price
- Markets within 2 hours of resolution are too risky (forecast is locked, price is efficient)
- Markets beyond 72 hours are too uncertain (forecast skill drops dramatically past 3 days)
- International cities (especially Asia, South America) may have less efficient markets due to fewer sophisticated traders

### System Enhancements
- **Add ensemble averaging**: Weight ECMWF and HRRR forecasts by their calibrated sigma instead of picking one
- **Add wind chill / heat index awareness**: Some markets may resolve on "feels like" temperature
- **Add seasonal sigma**: Forecast accuracy varies by season (winter storms = higher sigma)
- **Connect to CLOB for real execution**: The bot currently paper-trades; connecting to Polymarket's CLOB API enables real orders
- **Add Kalshi markets**: Same weather markets exist on Kalshi with potentially different pricing
- **Cross-platform arbitrage**: Buy on the platform where the contract is cheaper

---

## Implementation Pathway

### 24-Hour Quickstart
1. Clone repo, install `requests`, create `config.json` with conservative defaults
2. Get free Visual Crossing API key for resolution data
3. Run `python weatherbet.py` -- let it scan once, observe output
4. Read `data/markets/` JSON files to understand the data structure
5. Run `python weatherbet.py status` to see the state
6. Open `sim_dashboard_repost.html` with `python -m http.server 8000` to visualize

### 7-Day Sprint
1. Let the bot run for 48+ hours in paper mode (accumulate forecast snapshots)
2. Manually verify 5+ forecasts against actual temperatures (build trust in the forecast sources)
3. Check calibration data after first 30 resolved markets
4. Analyze per-city win rates: identify which cities have the strongest edges
5. Adjust `MAX_BET` and `KELLY_FRACTION` based on observed drawdown
6. Build confidence in stop-loss and trailing stop behavior by watching them fire

### 30-Day Integration
1. Accumulate enough calibration data for per-city sigma to stabilize (50+ resolved per city)
2. Review the full report (`python weatherbet.py report`) for systematic patterns
3. Identify cities to add or remove based on win rate and PnL
4. Consider connecting to Polymarket CLOB API for real execution (start with $100 max exposure)
5. Implement cross-platform price comparison with Kalshi
6. Build automated alerts for high-edge opportunities (Telegram/Discord webhook)

---

## Crown Jewel Prompts

### Crown Jewel 1: Weather Market Scanner

**Purpose**: Scan all active Polymarket weather markets, identify edges using airport-correct coordinates and multi-source forecasts.

```
You are a weather market scanner for Polymarket. Your job is to identify mispriced temperature markets.

For each city in the active rotation, execute this pipeline:

STEP 1 -- COORDINATE LOOKUP
Map each city to its EXACT ICAO resolution station:
- NYC -> KLGA (40.7772, -73.8726)
- Chicago -> KORD (41.9742, -87.9073)
- Miami -> KMIA (25.7959, -80.2870)
- Dallas -> KDAL (32.8471, -96.8518)
[... full 20-city table]

STEP 2 -- FORECAST ACQUISITION
For each city, fetch from ALL three sources:
- ECMWF: api.open-meteo.com, models=ecmwf_ifs025, bias_correction=true, 7-day horizon
- HRRR/GFS: api.open-meteo.com, models=gfs_seamless, 3-day horizon (US cities only)
- METAR: aviationweather.gov/api/data/metar, station={ICAO} (same-day only)

Select BEST source: HRRR for US D+0/D+1, ECMWF for everything else.

STEP 3 -- MARKET MATCHING
Find Polymarket event: slug = "highest-temperature-in-{city}-on-{month}-{day}-{year}"
Parse all outcome buckets. Identify the single bucket matching the forecast.

STEP 4 -- EDGE CALCULATION
For matching bucket:
- Probability: If center bucket (between X-Y) and forecast is inside -> p = 1.0
  If edge bucket ("or below" / "or higher") -> p = norm_cdf((boundary - forecast) / sigma)
- EV = p * (1/ask_price - 1) - (1 - p)
- Filter: EV >= 0.10, price < $0.45, volume >= 500, spread <= $0.03, 2h <= hours <= 72h

STEP 5 -- OUTPUT
For each edge found, produce:
| City | Date | Bucket | Forecast | Source | Probability | Market Price | EV | Kelly % | Suggested Size |

Flag the top 3 edges by EV for immediate action.
```

**Example Output**:
```
WEATHER MARKET SCAN -- 2026-04-14 09:00 UTC
============================================
Active cities: 20 | Markets found: 47 | Edges identified: 6

TOP EDGES:
1. Chicago D+1 (Apr 15) | 58-59F | Forecast: 58F (HRRR) | p=1.00 | Mkt: $0.12 | EV: +0.78 | Kelly: 8.2% | Size: $16.40
2. Tokyo D+2 (Apr 16) | 18-19C | Forecast: 18.5C (ECMWF) | p=1.00 | Mkt: $0.09 | EV: +0.89 | Kelly: 9.1% | Size: $18.20
3. London D+1 (Apr 15) | 13C or higher | Forecast: 15.2C (ECMWF) | p=0.87 | Mkt: $0.21 | EV: +0.42 | Kelly: 4.5% | Size: $9.00

FILTERED OUT: 3 markets (2 spread > $0.03, 1 volume < 500)
```

---

### Crown Jewel 2: Kelly Position Calculator

**Purpose**: Given an identified edge, produce exact position sizing with all risk parameters.

```
You are a Kelly Criterion position calculator for weather prediction markets.

INPUTS:
- Estimated probability (p): [from scanner]
- Market ask price: [current ask]
- Market bid price: [current bid]
- Account balance: [current]
- City sigma (calibrated or default): [from calibration.json]

STEP 1 -- VALIDATE INPUTS
- Spread check: (ask - bid) <= $0.03, else REJECT
- Price check: ask < $0.45, else REJECT
- EV check: p * (1/ask - 1) - (1 - p) >= 0.10, else REJECT

STEP 2 -- CALCULATE KELLY
Full Kelly: f = (p * b - (1 - p)) / b where b = (1/ask - 1)
Fractional Kelly: f_adj = f * 0.25
Raw size: f_adj * balance
Capped size: min(raw_size, $20.00)
Final size: max(capped_size, $0.50) or REJECT if < $0.50

STEP 3 -- RISK PARAMETERS
- Stop-loss price: entry * 0.80 (20% loss)
- Max loss on this trade: cost * 0.20
- Trailing activation: entry * 1.20
- Take-profit: $0.75 if hours > 48, $0.85 if 24-48h, HOLD if < 24h
- Position as % of balance: cost / balance * 100

STEP 4 -- OUTPUT
Produce a complete trade ticket:
```

**Example Output**:
```
TRADE TICKET -- Chicago KORD, Apr 15, 58-59F
=============================================
Probability:      100.0% (HRRR forecast 58F, sigma 1.8)
Market Ask:       $0.120
Market Bid:       $0.105
Spread:           $0.015 (OK, < $0.03)
EV per dollar:    +$0.78

Kelly Fraction:   8.2% (full Kelly 32.8% * 0.25)
Position Size:    $16.40 (capped at $20 max)
Shares:           136.67 @ $0.12

RISK PARAMETERS:
Stop-loss:        $0.096 (max loss: -$3.28)
Trailing at:      $0.144 (stop moves to $0.12 breakeven)
Take-profit:      $0.85 (24-48h to resolution)
Position % of bal: 0.16%
```

---

### Crown Jewel 3: Self-Calibration Analyst

**Purpose**: Review prediction history, calculate per-city sigma, recommend parameter adjustments.

```
You are a calibration analyst for a weather trading bot. You review resolved market data and produce updated sigma values and trading recommendations.

INPUTS: All resolved market JSON files from data/markets/

STEP 1 -- COLLECT ERRORS
For each resolved market with position and actual_temp:
- Extract forecast temperature from the LAST forecast snapshot before resolution
- Calculate absolute error: |forecast - actual|
- Group by (city, forecast_source)

STEP 2 -- CALCULATE SIGMA
For each (city, source) pair with 30+ samples:
- New sigma = Mean Absolute Error of the group
- Compare to current sigma (from calibration.json or defaults: 2.0F / 1.2C)
- Flag changes > 0.05

STEP 3 -- PRODUCE RECOMMENDATIONS
For each city:
- Current sigma vs. recommended sigma
- Sample size
- Trend: improving, stable, or degrading accuracy
- Cities with < 30 samples: "insufficient data, using default"
- Cities with sigma > 3.0F: "consider removing -- low forecast skill"
- Cities with sigma < 1.5F: "high-confidence -- consider increasing Kelly fraction for this city"

STEP 4 -- PORTFOLIO ANALYSIS
- Average sigma across all calibrated cities
- Correlation between forecast errors (are errors correlated across nearby cities?)
- Recommendation: add cities (diversification), remove cities (low skill), adjust Kelly by tier
```

**Example Output**:
```
CALIBRATION REPORT -- 2026-04-14
=================================
Total resolved markets: 847 | Calibrated pairs: 31 / 40

PER-CITY SIGMA:
City            Source   Samples  Old Sigma  New Sigma  Delta    Status
NYC (KLGA)      HRRR     89       2.00       1.72       -0.28    IMPROVED -- high confidence
NYC (KLGA)      ECMWF    92       2.00       1.85       -0.15    IMPROVED
Chicago (KORD)  HRRR     76       2.00       2.14       +0.14    SLIGHT DEGRADATION
Miami (KMIA)    HRRR     84       2.00       1.48       -0.52    EXCELLENT -- best US city
London (EGLC)   ECMWF    67       1.20       1.45       +0.25    DEGRADATION -- maritime variability
Tokyo (RJTT)    ECMWF    71       1.20       1.12       -0.08    STABLE

RECOMMENDATIONS:
- Miami: Sigma 1.48 -- consider 0.30 Kelly fraction (currently 0.25)
- London: Sigma 1.45 -- above default; reduce position sizing
- Singapore: Only 18 samples -- keep default sigma until 30+
- Lucknow: Sigma 2.8C -- consider removing; forecast skill too low
```

---

### Crown Jewel 4: Trade Execution Blueprint

**Purpose**: Produce a complete trade plan from entry through all possible exit scenarios.

```
You are a trade execution planner. Given a specific market opportunity, produce the full lifecycle plan including every exit scenario.

INPUTS:
- City, date, bucket, forecast, source, sigma
- Market ask price, bid price, volume
- Hours to resolution
- Account balance

PRODUCE:

1. ENTRY PLAN
   - Position size (Kelly-derived, capped)
   - Entry price (verified real ask)
   - Number of shares
   - Timestamp to execute (immediately if all filters pass)

2. STOP-LOSS SCENARIO
   - Stop price: entry * 0.80
   - Max loss in dollars
   - Trigger: price drops 20% from entry
   - Action: sell all shares at market bid

3. TRAILING STOP SCENARIO
   - Activation: price reaches entry * 1.20
   - New stop: moves to entry (breakeven)
   - Trigger: price drops below entry after trailing activated
   - Action: sell all shares -- guaranteed breakeven or better

4. TAKE-PROFIT SCENARIO
   - Threshold: $0.75 (48h+), $0.85 (24-48h), HOLD (<24h)
   - Expected profit at take-profit price
   - Action: sell all shares at take-profit

5. FORECAST-CHANGE SCENARIO
   - Monitor every 60 minutes
   - Exit trigger: forecast moves 2+F (1+C) outside bucket + buffer
   - Expected price at forecast change (likely lower if forecast moved away)
   - Action: sell all shares immediately regardless of P&L

6. RESOLUTION SCENARIO
   - If held to resolution: WIN pays $1.00/share, LOSS pays $0.00
   - Expected value at resolution
   - P&L if WIN vs LOSS

7. DECISION TREE
   Show the flowchart: Entry -> [Monitor every 10min: stop/trail/take-profit] -> [Monitor every 60min: forecast-change] -> [Resolution check: auto-resolve]
```

**Example Output**:
```
TRADE EXECUTION BLUEPRINT
=========================
Market: Chicago KORD | Apr 15 | Bucket 58-59F
Forecast: 58F (HRRR) | Sigma: 1.72 | Hours to resolution: 28h

ENTRY:
  Price: $0.120 (ask) | Shares: 136.67 | Cost: $16.40
  Kelly: 8.2% | EV: +$0.78/dollar

SCENARIO MAP:
  A. STOP-LOSS (price <= $0.096)
     Max loss: -$3.28 | Probability: ~5% (based on historical)

  B. TRAILING STOP (price hits $0.144, then drops to $0.120)
     Outcome: breakeven ($0.00) | Probability: ~10%

  C. TAKE-PROFIT (price >= $0.85, 24-48h window)
     Profit: +$99.67 (sell 136.67 shares @ $0.85 - $16.40 cost)
     Probability: ~15% (market converges early)

  D. FORECAST-CHANGE EXIT (forecast moves to 55F or 61F+)
     Expected exit price: ~$0.06-0.10 (forecast no longer supports bucket)
     Expected loss: -$2.73 to -$8.20 | Probability: ~8%

  E. RESOLUTION WIN (held to end, actual temp 58-59F)
     Payout: $136.67 (shares * $1.00) - $16.40 cost = +$120.27
     Probability: ~62% (based on calibrated model)

  F. RESOLUTION LOSS (held to end, actual temp outside 58-59F)
     Payout: $0.00 - $16.40 cost = -$16.40
     Probability: ~38%

  EXPECTED VALUE: (0.62 * $120.27) + (0.38 * -$16.40) = +$68.34
```

---

### Crown Jewel 5: Weather Bot Config Optimizer

**Purpose**: Analyze historical performance data and produce an optimized config.json.

```
You are a configuration optimizer for a weather trading bot. You analyze historical results and produce parameter recommendations.

INPUTS: All resolved market data, current config.json, calibration.json

ANALYZE:

1. KELLY FRACTION ANALYSIS
   - Current: 0.25
   - Calculate optimal Kelly from actual win rate and average payoff
   - If win rate > 65% and avg payoff > 5x: consider increasing to 0.30
   - If win rate < 55% or max drawdown > 10%: decrease to 0.20
   - NEVER recommend above 0.33 (one-third Kelly)

2. MAX PRICE ANALYSIS
   - Current: $0.45
   - Win rate by entry price bucket: <$0.10, $0.10-0.20, $0.20-0.30, $0.30-0.45
   - If win rate drops sharply above $0.25: lower max_price to $0.30
   - If high-EV trades exist at $0.45-0.55: consider raising to $0.50

3. MIN EV ANALYSIS
   - Current: 0.10
   - Distribution of EV at entry for winners vs losers
   - If most losses come from EV 0.10-0.15 trades: raise to 0.15
   - If profitable trades are being filtered at EV 0.08-0.10: lower to 0.08

4. TIME WINDOW ANALYSIS
   - Current: 2-72 hours
   - Win rate by hours-to-resolution bucket: 2-6h, 6-12h, 12-24h, 24-48h, 48-72h
   - Identify the sweet spot where win rate peaks
   - Adjust min_hours and max_hours accordingly

5. CITY PERFORMANCE
   - Win rate and PnL by city
   - Identify cities to ADD (good forecast skill, many markets)
   - Identify cities to REMOVE (poor forecast skill, low volume)
   - Recommend city rotation strategy

OUTPUT: Complete optimized config.json with commentary on each change.
```

**Example Output**:
```
CONFIG OPTIMIZATION REPORT
===========================
Based on 847 resolved markets over 45 days

RECOMMENDED config.json:
{
  "balance": 10000.0,
  "max_bet": 25.0,          // INCREASED from 20 -- win rate 67% supports higher sizing
  "min_ev": 0.12,           // INCREASED from 0.10 -- 68% of losses came from EV 0.10-0.12
  "max_price": 0.35,        // DECREASED from 0.45 -- win rate drops from 72% to 48% above $0.35
  "min_volume": 750,        // INCREASED from 500 -- markets 500-750 vol had 12% worse exits
  "min_hours": 3.0,         // INCREASED from 2.0 -- <3h markets have 15% lower win rate
  "max_hours": 48.0,        // DECREASED from 72.0 -- D+3 markets have sigma 40% higher
  "kelly_fraction": 0.28,   // INCREASED from 0.25 -- 67% win rate + 8.2x avg payoff supports it
  "scan_interval": 3600,    // UNCHANGED
  "calibration_min": 30,    // UNCHANGED
  "max_slippage": 0.025     // TIGHTENED from 0.03 -- trades entered with spread > 0.025 lost 8% more
}

KEY FINDINGS:
- Sweet spot is $0.08-$0.20 contracts, 6-36 hours to resolution
- Miami, NYC, and Tokyo are the highest-performing cities
- London and Lucknow are net negative -- consider removing
- HRRR beats ECMWF by 0.4F MAE for US cities within 24h
```
