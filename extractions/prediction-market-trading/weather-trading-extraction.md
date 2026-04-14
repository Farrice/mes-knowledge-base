# Weather Trading Extraction Report

## Content Assessment
- Source: Research dossier + alteregoeth-ai/weatherbot analysis
- Expert: Composite (alteregoeth-ai/weatherbot developers + documented weather traders)
- Domain: Prediction market weather trading
- Depth Tier: Standard
- Genius Patterns: 12
- Hidden Knowledge: 8

---

## Layer 1 — Surface Intelligence

### The Core Business Model
Weather prediction markets on Polymarket resolve daily. Typical format: "Will the high temperature in NYC exceed 75°F on April 15?" Markets trade as binary options (YES/NO) priced 0-100 cents. Weather is uniquely suited to algorithmic trading because:
- Outcomes are objective and machine-verifiable
- Resolution data is public (government weather stations)
- Forecasting models are mature and freely available
- Markets are liquid ($300K-$400K daily volume per market)
- Retail participants systematically misprice weather events

### Data Source Stack (All Free)
1. **Open-Meteo API** — Primary. Provides ECMWF (European) and HRRR (US high-resolution) model outputs. No API key required. Hourly resolution, 16-day forecast horizon.
2. **METAR Aviation Network** — Real-time airport weather observations. Updates every 20-60 minutes. The ground truth source for calibration.
3. **Visual Crossing** — Historical weather data + forecasts. Free tier: 1000 records/day. Best for backtesting calibration accuracy.
4. **api.weather.gov** — NWS (National Weather Service) forecasts. Free, no key. Good secondary model for US markets.

### Risk Configuration (Consensus Parameters)
```
balance: 10000          # Starting/current bankroll
max_bet: 20             # Maximum single position ($20)
min_ev: 0.05            # Minimum expected value to trade (5%)
max_price: 0.45         # Never buy above 45 cents (avoid favorites)
min_volume: 2000        # Market must have $2K+ volume
min_hours: 2.0          # Don't trade within 2 hours of resolution
max_hours: 72.0         # Don't trade more than 72 hours out
kelly_fraction: 0.25    # Quarter-Kelly position sizing
max_slippage: 0.03      # Max 3 cents price movement tolerance
scan_interval: 3600     # Re-scan markets every hour
calibration_min: 30     # Need 30+ samples before trusting per-city calibration
```

### Two-Layer Architecture
- **Layer 1 (LLM Reasoning)**: Claude/GPT analyzes weather data, generates probability estimates, identifies edges. The LLM reasons about forecast uncertainty, model disagreement, microclimate effects, and market mispricing.
- **Layer 2 (Deterministic Code)**: Python executes trades. The LLM never touches API keys, wallet credentials, or order execution. This separation is non-negotiable — it prevents prompt injection from draining funds.

### Fee Structure
- Taker fee: 1.25% (paid when you buy at market price)
- Maker fee: 0% (paid when your limit order is filled)
- Implication: Always use limit orders. The 1.25% taker fee eats into thin weather edges.

### Documented Results
- $1K → $24K on London weather markets alone
- $65K total profit across NYC, London, Seoul markets
- Multiple independent implementations confirm profitability

---

## Layer 2 — Hidden Patterns

### Pattern 1: The Airport Station Edge (THE Critical Insight)
Every Polymarket weather market resolves based on a specific airport weather station — NOT the city center, NOT the nearest weather.com station, NOT an average. The resolution source is pinned to an ICAO code.

**Why this matters**: Airport weather stations sit on tarmac surrounded by open runway. City center stations sit among buildings that create urban heat island effects. The difference is 3-8°F on any given day. On bucket markets where the spread between YES and NO is 1-2°F, using city center data is fatal.

**Correct ICAO codes**:
- NYC → **KLGA** (LaGuardia Airport) — NOT Central Park, NOT JFK
- Dallas → **KDAL** (Dallas Love Field) — NOT KDFW (DFW Airport). This is the single most common error.
- London → **EGLL** (Heathrow)
- Seoul → **RKSS** (Gimpo)

**The edge is structural**: Most retail traders use weather.com or generic forecast apps that report city-center temperatures. They're trading on the wrong data. This information asymmetry persists because it requires reading the fine print of market resolution criteria.

### Pattern 2: Model Disagreement = Opportunity
When ECMWF and HRRR disagree by more than 2°F, the market is pricing uncertainty poorly. One model will be closer to the station observation. Track which model wins per city per season, and you develop a structural advantage.

### Pattern 3: The 72-Hour Sweet Spot
- Beyond 72 hours: Forecast skill drops sharply. Models disagree. Market prices are noisy. Not enough edge.
- Under 2 hours: Market has already priced in the METAR observations. No edge left.
- 6-48 hours: Prime trading window. Models are skilled, but retail hasn't updated their priors.

### Pattern 4: Volume as Signal
Markets below $2K volume have wide spreads and illiquidity risk. Markets above $300K are efficient enough that edges are thin. The sweet spot is $5K-$50K volume — enough liquidity to enter/exit, not enough sophistication to price weather perfectly.

### Pattern 5: Seasonal Calibration Drift
A model that's well-calibrated for NYC summer temperatures will systematically over/underpredict in winter. Per-city, per-season calibration is essential. The weatherbot stores this as a running accuracy log and adjusts confidence after 30+ samples.

### Pattern 6: Maker vs Taker Discipline
At 1.25% taker fees, a 5% edge becomes 3.75% after fees. Smart operators place limit orders at their target price and wait. Patient capital beats reactive trading.

### Pattern 7: The Paper-to-Live Gap
Expect 30-50% performance degradation from paper trading to live. Sources: slippage, timing delays, emotional override, and the fact that paper trading doesn't account for your orders moving the market.

### Pattern 8: Multi-City Diversification
Running the same system across 4-5 cities (NYC, London, Seoul, Dallas, Tokyo) provides natural diversification. Weather events are largely uncorrelated across hemispheres, reducing drawdown volatility.

---

## Layer 3 — Signature Moves

### Signature 1: Station-Pinned Forecast Ensemble
Pull forecasts from all 4 data sources, but anchor EVERY forecast to the correct airport ICAO code. Convert all model outputs to station-equivalent temperatures using historical offset data. This is the core competitive moat — most traders skip this step entirely.

### Signature 2: Self-Calibrating Confidence
The weatherbot stores every prediction alongside the actual outcome. After 30+ predictions per city, it calculates a calibration curve: "When I say 70% probability, it actually happens X% of the time." If X ≠ 70, adjust. This creates a system that gets more accurate over time, compounding the edge.

### Signature 3: Kelly Fraction at 0.25
Full Kelly sizing is theoretically optimal but assumes perfect probability estimates. Weather forecasts are NOT perfect. Quarter-Kelly (0.25) provides ~75% of the growth rate at ~50% of the drawdown. This is consensus across all documented implementations.

### Signature 4: LLM-Reasoning + Deterministic-Execution Split
The LLM analyzes weather data and generates probability estimates. Deterministic code handles order placement, risk checks, and portfolio management. The LLM never touches credentials. This architecture prevents: prompt injection attacks, hallucinated trade parameters, and "confident but wrong" position sizing.

### Signature 5: Contrarian Positioning on Extreme Events
When weather models predict a heat wave or cold snap, retail traders pile into the obvious direction. The edge is in the MAGNITUDE — markets tend to overshoot on extreme events. The pro move: fade the extreme if models show convergence toward a less extreme outcome within 24 hours.

---

## Layer 4 — Decision Architecture

### Decision Tree: Trade or Pass

```
1. Is there an active weather market?
   NO → Pass
   YES → Continue

2. Map to correct airport ICAO code
   Can't identify resolution station → Pass (never guess)
   Identified → Continue

3. Pull all 4 model forecasts
   Models agree within 1°F → Low uncertainty, check for edge
   Models disagree by 2°F+ → High uncertainty, flag for deeper analysis

4. Generate probability estimate for each bucket
   P(YES) vs Market Price
   Expected Value = P(YES) * Payout - (1 - P(YES)) * Cost
   EV < 0.05 → Pass
   EV ≥ 0.05 → Continue

5. Check risk gates
   Volume < $2K → Pass
   Hours to resolution < 2 → Pass
   Hours to resolution > 72 → Pass
   Market price > 0.45 → Pass
   All clear → Size and trade

6. Calculate position size
   Kelly fraction: 0.25 * bankroll * edge / odds
   Cap at max_bet ($20)
   Check slippage tolerance (3 cents)

7. Execute via limit order (avoid taker fees)
```

### When to Override the System
- **Severe weather warnings**: NWS severe thunderstorm/tornado warnings can shift temperatures 10-15°F in hours. Override model consensus with real-time data.
- **Market microstructure events**: If you see large block orders moving the price, pause. Someone may have information you don't.
- **Calibration failure**: If your last 10 predictions in a city are systematically wrong, stop trading that city until you diagnose the bias.

---

## Layer 5 — Quality Rubric

### What Separates Good from Great

| Dimension | Amateur (1-3) | Competent (4-6) | Expert (7-9) | Master (10) |
|-----------|--------------|-----------------|--------------|-------------|
| Station Mapping | Uses city center data | Knows about airport stations | Correct ICAO for all markets | Historical offset calibration per station |
| Data Sources | Single weather app | 2 sources cross-referenced | All 4 sources with model weighting | Dynamic model weighting by city + season |
| Position Sizing | Flat bet or gut feel | Fixed fraction | Kelly with fraction | Adaptive Kelly based on calibration accuracy |
| Calibration | No tracking | Tracks win/loss rate | Per-city accuracy with 30+ samples | Per-city, per-season, per-model decomposition |
| Risk Management | No stop-loss | Max bet limit | Full risk config | Dynamic risk adjustment based on drawdown |
| Execution | Market orders | Limit orders | Limit orders + slippage monitoring | Maker-only with queue position optimization |
| Diversification | Single city | 2-3 cities | 5+ cities across hemispheres | Correlation-aware portfolio construction |

### Red Flags (Immediate Stop)
- Trading with city-center temperature data
- Using full Kelly (1.0 fraction) on weather markets
- Trading within 2 hours of resolution
- Buying positions above 45 cents
- Skipping calibration tracking
- Letting the LLM touch wallet credentials
- Trading markets below $2K volume

### Green Flags (System Working)
- Calibration curve within 5% of perfect (diagonal line)
- Win rate above 55% over 50+ trades
- Per-city tracking shows improving accuracy over time
- Drawdowns stay under 15% of bankroll
- Maker-order fill rate above 60%
