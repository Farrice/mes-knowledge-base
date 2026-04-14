---
description: "Scan weather markets, identify edges using airport station precision and multi-source forecasts, produce ranked opportunity table"
---

# Market Forecast & Edge Detection

> Systematic scan of all active Polymarket weather markets. Maps every city to its exact ICAO resolution station, pulls forecasts from the correct source for each geography and time horizon, calculates edge-vs-center bucket probabilities with calibrated sigma, and ranks opportunities by expected value. Output is a deployable opportunity table with the top 3 edges flagged for immediate action.

---

## Inputs

Provide before running this workflow:

| Input | Required | Default | Notes |
|-------|----------|---------|-------|
| Active city list | Yes | Full 20-city rotation | Can narrow to subset for focused scan |
| Account balance | Yes | — | Current available balance for Kelly sizing |
| Calibration data | If available | Default sigma (2.0F / 1.2C) | From `data/calibration.json` or prior calibration review |
| Date range | No | D+0 through D+3 | Which forecast horizons to scan |
| Custom filters | No | Standard filters | Override MIN_EV, MAX_PRICE, etc. if needed |

---

## Process

### STEP 1 — Coordinate Lookup

Map every city in the active rotation to its exact ICAO resolution station. Use the verified lookup table. Never use city-center coordinates.

```
LOCATION TABLE (verify against Polymarket resolution criteria):

City            ICAO   Lat       Lon        Unit  Region
New York        KLGA   40.7772   -73.8726   F     us
Chicago         KORD   41.9742   -87.9073   F     us
Miami           KMIA   25.7959   -80.2870   F     us
Dallas          KDAL   32.8471   -96.8518   F     us
Houston         KHOU   29.6454   -95.2789   F     us
Los Angeles     KLAX   33.9425   -118.4081  F     us
Denver          KDEN   39.8561   -104.6737  F     us
Phoenix         KPHX   33.4373   -112.0078  F     us
Seattle         KSEA   47.4502   -122.3088  F     us
Atlanta         KATL   33.6407   -84.4277   F     us
London          EGLL   51.4700   -0.4543    C     eu
Paris           LFPG   49.0097   2.5479     C     eu
Tokyo           RJTT   35.5494   139.7798   C     asia
Seoul           RKSS   37.5586   126.7906   C     asia
Singapore       WSSS   1.3502    103.9940   C     asia
Dubai           OMDB   25.2528   55.3644    C     me
Sydney          YSSY   -33.9461  151.1772   C     oceania
São Paulo       SBGR   -23.4356  -46.4731   C     sa
Mexico City     MMMX   19.4363   -99.0721   C     na
Mumbai          VABB   19.0896   72.8656    C     asia
```

For any new city not in this table: identify the ICAO code from the Polymarket resolution criteria, look up airport coordinates from aviation databases, and add to the table before proceeding.

### STEP 2 — Forecast Acquisition

For each city, fetch forecasts from ALL three sources. Store all values even if only one is selected.

**Source 1 — ECMWF (all cities, all horizons)**:
```
API: api.open-meteo.com/v1/forecast
Params: latitude={lat}&longitude={lon}&hourly=temperature_2m&models=ecmwf_ifs025&forecast_days=7
Note: Use bias_correction=true
Extract: Daily high temperature for each target date
```

**Source 2 — HRRR/GFS (US cities only, 0-72h)**:
```
API: api.open-meteo.com/v1/forecast
Params: latitude={lat}&longitude={lon}&hourly=temperature_2m&models=gfs_seamless&forecast_days=3
Extract: Daily high temperature for each target date
Note: HRRR embedded in GFS seamless model. Only available for US region cities.
```

**Source 3 — METAR (all cities, same-day only)**:
```
API: aviationweather.gov/api/data/metar
Params: ids={ICAO}&format=json
Extract: Current observed temperature
Note: NEVER use as forecast. Same-day observation anchor only.
```

**Best source selection** (deterministic priority):
- US city AND D+0 or D+1 AND HRRR available → **HRRR**
- Everything else → **ECMWF**
- METAR → observation only, never forecast

**Rate limiting**: Sleep 0.3 seconds between cities to avoid API throttling. 20 cities = 6 seconds overhead — trivial against 3600-second scan interval.

### STEP 3 — Market Discovery & Bucket Matching

For each city and each target date (D+0 through D+3):

**Find the Polymarket event**:
```
Slug pattern: highest-temperature-in-{city}-on-{month}-{day}-{year}
API: gamma-api.polymarket.com/events?slug={slug}
```

**Parse outcome buckets**. Three bucket types:
- **Center bucket**: "between 46-47F" — bounded range
- **Low edge bucket**: "45F or below" — open-ended lower tail
- **High edge bucket**: "48F or higher" — open-ended upper tail
- **Exact bucket**: "be 47F" — single degree (rare)

**Match forecast to single bucket**. Find exactly ONE bucket where the forecast temperature falls. Do not spread across multiple buckets — single forecast, single bucket, single position.

### STEP 4 — Probability Calculation

For the matching bucket, calculate probability using calibrated sigma:

**Center bucket** (forecast inside "between X-Y"):
```
probability = 1.0 if forecast is within bucket range
probability = 0.0 if forecast is outside bucket range
```
Center buckets are binary — the sigma matters for tail risk but the probability is high-confidence if the forecast is correct.

**Edge bucket** ("X or below" / "X or higher"):
```
sigma = calibrated sigma for (city, source) pair, or default (2.0F / 1.2C)
For "X or below":  p = norm_cdf((boundary - forecast) / sigma)
For "X or higher": p = 1.0 - norm_cdf((boundary - forecast) / sigma)
```
Edge buckets are where calibrated sigma matters most — a 2-3 degree forecast error can push probability dramatically.

### STEP 5 — Edge Calculation & Filtering

For each matched bucket with probability estimate:

**Expected Value**:
```
ask_price = current market ask price
b = (1 / ask_price) - 1       # payout odds
EV = p * b - (1 - p)          # expected value per dollar risked
```

**Kelly fraction**:
```
full_kelly = (p * b - (1 - p)) / b
fractional_kelly = full_kelly * 0.25
position_pct = min(max(0, fractional_kelly), 1.0)
raw_size = position_pct * balance
capped_size = min(raw_size, 20.00)
final_size = capped_size if capped_size >= 0.50 else REJECT
```

**Apply all filters** — reject if ANY fails:
| Filter | Threshold | Reason |
|--------|-----------|--------|
| EV | >= 0.10 | Below this, fees + slippage eat the edge |
| Ask price | < $0.45 | Above this, payout ratio doesn't justify risk |
| Volume | >= 500 | Below this, prices are stale/illiquid |
| Spread | <= $0.03 | Beyond this, execution costs exceed edge |
| Hours to resolution | >= 2.0 | Below 2h, METAR is public and market is efficient |
| Hours to resolution | <= 72.0 | Beyond 3 days, forecast skill degrades sharply |
| Position size | >= $0.50 | Below this, trade is noise |

### STEP 6 — Rank & Output

Sort all passing opportunities by EV descending. Flag top 3 for immediate action.

---

## Output Template

```
WEATHER MARKET SCAN — {date} {time} UTC
================================================
Active cities: {n} | Markets scanned: {n} | Edges identified: {n}
Calibration: {calibrated/default} | Balance: ${balance}

TOP EDGES (sorted by EV):
┌─────┬────────────┬────────┬──────────┬──────────┬────────┬───────┬──────────┬─────────┬──────────┬───────────┐
│  #  │ City       │ Date   │ Bucket   │ Forecast │ Source │ Sigma │ Prob     │ Ask     │ EV       │ Size      │
├─────┼────────────┼────────┼──────────┼──────────┼────────┼───────┼──────────┼─────────┼──────────┼───────────┤
│  1  │ {city}     │ {date} │ {bucket} │ {temp}   │ {src}  │ {sig} │ {p:.0%}  │ ${ask}  │ +{ev:.2f}│ ${size}   │
│  2  │ ...        │ ...    │ ...      │ ...      │ ...    │ ...   │ ...      │ ...     │ ...      │ ...       │
│  3  │ ...        │ ...    │ ...      │ ...      │ ...    │ ...   │ ...      │ ...     │ ...      │ ...       │
└─────┴────────────┴────────┴──────────┴──────────┴────────┴───────┴──────────┴─────────┴──────────┴───────────┘

ALL PASSING EDGES:
{same table format for remaining edges, if any}

FILTERED OUT:
- {n} markets: spread > $0.03
- {n} markets: volume < 500
- {n} markets: EV < 0.10
- {n} markets: price > $0.45
- {n} markets: hours outside 2-72 window
- {n} markets: position size < $0.50

FORECAST SNAPSHOT (for data collection — all markets, all sources):
{city} {date}: ECMWF={temp}° HRRR={temp}° METAR={temp}° | Best={source} {temp}°
{...for all city/date combinations scanned}

NOTES:
- Markets within 6h of resolution: verify METAR trend before acting
- Cities with < 30 calibration samples: using default sigma (marked *)
- Model disagreement flags: {any cities where HRRR and ECMWF differ by 3°F+}
```

---

## Example Output

```
WEATHER MARKET SCAN — 2026-04-14 09:00 UTC
================================================
Active cities: 20 | Markets scanned: 47 | Edges identified: 6
Calibration: 14/20 cities calibrated | Balance: $10,000.00

TOP EDGES (sorted by EV):
┌─────┬────────────┬────────┬──────────┬──────────┬────────┬───────┬──────────┬─────────┬──────────┬───────────┐
│  #  │ City       │ Date   │ Bucket   │ Forecast │ Source │ Sigma │ Prob     │ Ask     │ EV       │ Size      │
├─────┼────────────┼────────┼──────────┼──────────┼────────┼───────┼──────────┼─────────┼──────────┼───────────┤
│  1  │ Tokyo      │ Apr 16 │ 18-19C   │ 18.5C    │ ECMWF  │ 1.12  │ 100%     │ $0.09   │ +0.89    │ $18.20    │
│  2  │ Chicago    │ Apr 15 │ 58-59F   │ 58F      │ HRRR   │ 1.72* │ 100%     │ $0.12   │ +0.78    │ $16.40    │
│  3  │ London     │ Apr 15 │ 13C+     │ 15.2C    │ ECMWF  │ 1.45  │ 87%      │ $0.21   │ +0.42    │ $9.00     │
└─────┴────────────┴────────┴──────────┴──────────┴────────┴───────┴──────────┴─────────┴──────────┴───────────┘

ALL PASSING EDGES:
│  4  │ Miami      │ Apr 15 │ 84-85F   │ 84F      │ HRRR   │ 1.48  │ 100%     │ $0.14   │ +0.36    │ $7.20     │
│  5  │ Seoul      │ Apr 16 │ 15-16C   │ 15.8C    │ ECMWF  │ 1.30  │ 100%     │ $0.18   │ +0.28    │ $5.60     │
│  6  │ NYC        │ Apr 15 │ 67F+     │ 70.2F    │ HRRR   │ 1.72  │ 78%      │ $0.23   │ +0.19    │ $3.80     │

FILTERED OUT:
- 2 markets: spread > $0.03 (Dubai Apr 15, Singapore Apr 16)
- 1 market: volume < 500 (Mexico City Apr 16)
- 3 markets: EV < 0.10
- 0 markets: price > $0.45
- 1 market: hours outside 2-72 window (Phoenix Apr 14 — <2h)

NOTES:
- Chicago using default sigma (28 samples, below 30 threshold) — marked *
- Model disagreement: Denver Apr 16 — HRRR 62F vs ECMWF 57F (5F gap, DO NOT TRADE)
```

---

## Post-Scan Actions

After generating the scan output:
1. **Record all forecast snapshots** to per-market JSON files — even for markets with no edge. This builds the calibration dataset.
2. **Top 3 edges**: Route to the [Trade Execution Plan](trade-execution-plan.md) workflow for full lifecycle planning before entry.
3. **Model disagreements 3F+**: Flag for manual investigation. Do not trade until resolved.
4. **Cities approaching 30 calibration samples**: Note which cities will graduate from default sigma soon.
5. **Save scan timestamp**: Next full scan in 60 minutes. Monitor positions every 10 minutes in between.
