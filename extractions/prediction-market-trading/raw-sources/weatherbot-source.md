# weatherbot Source Material (alteregoeth-ai/weatherbot)
## Fetched: 2026-04-13
## Repository: https://github.com/alteregoeth-ai/weatherbot
## License: MIT
## Languages: Python 77.4%, HTML 22.6%
## Commits: 25 (main branch only)

---

### Repository Structure
```
weatherbot/
├── .gitignore          (4,688 bytes — standard Python gitignore)
├── LICENSE             (1,071 bytes — MIT)
├── README.md           (4,327 bytes)
├── bot_v1.py           (17,503 bytes — base bot, 6 US cities)
├── bot_v2.py           (43,826 bytes — full bot, 20 cities, Kelly criterion)
├── config.json         (287 bytes)
└── sim_dashboard_repost.html  (17,918 bytes — live simulation dashboard)
```

---

### File: README.md
```markdown
# 🌤 WeatherBet — Polymarket Weather Trading Bot

Automated weather market trading bot for Polymarket. Finds mispriced temperature outcomes using real forecast data from multiple sources across 20 cities worldwide.

No SDK. No black box. Pure Python.

---

## Versions

### `bot_v1.py` — Base Bot
The foundation. Scans 6 US cities, fetches forecasts from NWS using airport station coordinates, finds matching temperature buckets on Polymarket, and enters trades when the market price is below the entry threshold.

No math, no complexity. Just the core logic — good for understanding how the system works.

### `weatherbet.py` — Full Bot (current)
Everything in v1, plus:
- **20 cities** across 4 continents (US, Europe, Asia, South America, Oceania)
- **3 forecast sources** — ECMWF (global), HRRR/GFS (US, hourly), METAR (real-time observations)
- **Expected Value** — skips trades where the math doesn't work
- **Kelly Criterion** — sizes positions based on edge strength
- **Stop-loss + trailing stop** — 20% stop, moves to breakeven at +20%
- **Slippage filter** — skips markets with spread > $0.03
- **Self-calibration** — learns forecast accuracy per city over time
- **Full data storage** — every forecast snapshot, trade, and resolution saved to JSON

---

## How It Works

Polymarket runs markets like "Will the highest temperature in Chicago be between 46–47°F on March 7?" These markets are often mispriced — the forecast says 78% likely but the market is trading at 8 cents.

The bot:
1. Fetches forecasts from ECMWF and HRRR via Open-Meteo (free, no key required)
2. Gets real-time observations from METAR airport stations
3. Finds the matching temperature bucket on Polymarket
4. Calculates Expected Value — only enters if the math is positive
5. Sizes the position using fractional Kelly Criterion
6. Monitors stops every 10 minutes, full scan every hour
7. Auto-resolves markets by querying Polymarket API directly

---

## Why Airport Coordinates Matter

Most bots use city center coordinates. That's wrong.

Every Polymarket weather market resolves on a specific airport station. NYC resolves on LaGuardia (KLGA), Dallas on Love Field (KDAL) — not DFW. The difference between city center and airport can be 3–8°F. On markets with 1–2°F buckets, that's the difference between the right trade and a guaranteed loss.

| City | Station | Airport |
|------|---------|---------|
| NYC | KLGA | LaGuardia |
| Chicago | KORD | O'Hare |
| Miami | KMIA | Miami Intl |
| Dallas | KDAL | Love Field |
| Seattle | KSEA | Sea-Tac |
| Atlanta | KATL | Hartsfield |
| London | EGLC | London City |
| Tokyo | RJTT | Haneda |
| ... | ... | ... |

---

## Installation
```bash
git clone https://github.com/alteregoeth-ai/weatherbot
cd weatherbot
pip install requests
```

Create `config.json` in the project folder:
```json
{
  "balance": 10000.0,
  "max_bet": 20.0,
  "min_ev": 0.05,
  "max_price": 0.45,
  "min_volume": 2000,
  "min_hours": 2.0,
  "max_hours": 72.0,
  "kelly_fraction": 0.25,
  "max_slippage": 0.03,
  "scan_interval": 3600,
  "calibration_min": 30,
  "vc_key": "YOUR_VISUAL_CROSSING_KEY"
}
```

Get a free Visual Crossing API key at visualcrossing.com — used to fetch actual temperatures after market resolution.

---

## Usage
```bash
python weatherbet.py           # start the bot — scans every hour
python weatherbet.py status    # balance and open positions
python weatherbet.py report    # full breakdown of all resolved markets
```

---

## Data Storage

All data is saved to `data/markets/` — one JSON file per market. Each file contains:
- Hourly forecast snapshots (ECMWF, HRRR, METAR)
- Market price history
- Position details (entry, stop, PnL)
- Final resolution outcome

This data is used for self-calibration — the bot learns forecast accuracy per city over time and adjusts position sizing accordingly.

---

## APIs Used

| API | Auth | Purpose |
|-----|------|---------|
| Open-Meteo | None | ECMWF + HRRR forecasts |
| Aviation Weather (METAR) | None | Real-time station observations |
| Polymarket Gamma | None | Market data |
| Visual Crossing | Free key | Historical temps for resolution |

---

## Disclaimer

This is not financial advice. Prediction markets carry real risk. Run the simulation thoroughly before committing real capital.

```

---

### File: config.json
```json
{
  "balance": 10000.0,
  "max_bet": 20.0,
  "min_ev": 0.1,
  "max_price": 0.45,
  "min_volume": 500,
  "min_hours": 2.0,
  "max_hours": 72.0,
  "kelly_fraction": 0.25,
  "scan_interval": 3600,
  "calibration_min": 30,
  "vc_key": "YOUR_KEY_HERE",
  "max_slippage": 0.03
}

```

---

### File: bot_v1.py
```python
#!/usr/bin/env python3
"""
Weather Trading Bot v1 — Polymarket
Simple base bot. Finds mispriced temperature markets using NWS forecasts.

Usage:
    python bot_v1.py           # Scan markets and show signals (paper mode)
    python bot_v1.py --live    # Execute trades against virtual $1,000 balance
    python bot_v1.py --reset   # Reset simulation balance
    python bot_v1.py --positions  # Show open positions
"""

import re
import json
import argparse
import requests
from datetime import datetime, timezone, timedelta

# =============================================================================
# CONFIG
# =============================================================================

with open("config.json") as f:
    _cfg = json.load(f)

ENTRY_THRESHOLD = _cfg.get("entry_threshold", 0.15)   # Buy below this price
EXIT_THRESHOLD  = _cfg.get("exit_threshold", 0.45)    # Sell above this price
MAX_TRADES      = _cfg.get("max_trades_per_run", 5)
MIN_HOURS_LEFT  = _cfg.get("min_hours_to_resolution", 2)
POSITION_PCT    = 0.05    # Flat 5% of balance per trade
SIM_BALANCE     = 1000.0  # Starting virtual balance

# Airport coordinates — match the exact stations Polymarket resolves on
LOCATIONS = {
    "nyc":     {"lat": 40.7772, "lon": -73.8726, "name": "New York City"},  # KLGA LaGuardia
    "chicago": {"lat": 41.9742, "lon": -87.9073, "name": "Chicago"},        # KORD O'Hare
    "miami":   {"lat": 25.7959, "lon": -80.2870, "name": "Miami"},          # KMIA
    "dallas":  {"lat": 32.8471, "lon": -96.8518, "name": "Dallas"},         # KDAL Love Field
    "seattle": {"lat": 47.4502, "lon": -122.3088, "name": "Seattle"},       # KSEA Sea-Tac
    "atlanta": {"lat": 33.6407, "lon": -84.4277,  "name": "Atlanta"},       # KATL Hartsfield
}

# NWS hourly endpoints per city
NWS_ENDPOINTS = {
    "nyc":     "https://api.weather.gov/gridpoints/OKX/37,39/forecast/hourly",
    "chicago": "https://api.weather.gov/gridpoints/LOT/66,77/forecast/hourly",
    "miami":   "https://api.weather.gov/gridpoints/MFL/106,51/forecast/hourly",
    "dallas":  "https://api.weather.gov/gridpoints/FWD/87,107/forecast/hourly",
    "seattle": "https://api.weather.gov/gridpoints/SEW/124,61/forecast/hourly",
    "atlanta": "https://api.weather.gov/gridpoints/FFC/50,82/forecast/hourly",
}

# Station IDs for real observations
STATION_IDS = {
    "nyc": "KLGA", "chicago": "KORD", "miami": "KMIA",
    "dallas": "KDAL", "seattle": "KSEA", "atlanta": "KATL",
}

ACTIVE_LOCATIONS = _cfg.get("locations", "nyc,chicago,miami,dallas,seattle,atlanta").split(",")
ACTIVE_LOCATIONS = [l.strip().lower() for l in ACTIVE_LOCATIONS]

MONTHS = ["january","february","march","april","may","june",
          "july","august","september","october","november","december"]

# =============================================================================
# COLORS
# =============================================================================

class C:
    GREEN  = "\033[92m"
    YELLOW = "\033[93m"
    RED    = "\033[91m"
    CYAN   = "\033[96m"
    GRAY   = "\033[90m"
    RESET  = "\033[0m"
    BOLD   = "\033[1m"

def ok(msg):   print(f"{C.GREEN}  ✅ {msg}{C.RESET}")
def warn(msg): print(f"{C.YELLOW}  ⚠️  {msg}{C.RESET}")
def info(msg): print(f"{C.CYAN}  {msg}{C.RESET}")
def skip(msg): print(f"{C.GRAY}  ⏸️  {msg}{C.RESET}")

# =============================================================================
# SIMULATION STATE
# =============================================================================

SIM_FILE = "simulation.json"

def load_sim() -> dict:
    try:
        with open(SIM_FILE) as f:
            return json.load(f)
    except FileNotFoundError:
        return {
            "balance": SIM_BALANCE,
            "starting_balance": SIM_BALANCE,
            "positions": {},
            "trades": [],
            "total_trades": 0,
            "wins": 0,
            "losses": 0,
            "peak_balance": SIM_BALANCE,
        }

def save_sim(sim: dict):
    with open(SIM_FILE, "w") as f:
        json.dump(sim, f, indent=2)

def reset_sim():
    import os
    if os.path.exists(SIM_FILE):
        os.remove(SIM_FILE)
    print(f"{C.GREEN}  ✅ Simulation reset — balance back to ${SIM_BALANCE:.2f}{C.RESET}")

# =============================================================================
# NWS FORECAST
# =============================================================================

def get_forecast(city_slug: str) -> dict:
    """
    Fetch daily max temperature from NWS.
    Combines real station observations (past hours today) with
    hourly forecast (upcoming hours) to get the true daily maximum.
    """
    forecast_url = NWS_ENDPOINTS.get(city_slug)
    station_id = STATION_IDS.get(city_slug)
    daily_max = {}
    headers = {"User-Agent": "weatherbot/1.0"}

    # Real observations — what already happened today
    try:
        obs_url = f"https://api.weather.gov/stations/{station_id}/observations?limit=48"
        r = requests.get(obs_url, timeout=10, headers=headers)
        for obs in r.json().get("features", []):
            props = obs["properties"]
            time_str = props.get("timestamp", "")[:10]
            temp_c = props.get("temperature", {}).get("value")
            if temp_c is not None:
                temp_f = round(temp_c * 9/5 + 32)
                if time_str not in daily_max or temp_f > daily_max[time_str]:
                    daily_max[time_str] = temp_f
    except Exception as e:
        warn(f"Observations error for {city_slug}: {e}")

    # Hourly forecast — upcoming hours
    try:
        r = requests.get(forecast_url, timeout=10, headers=headers)
        periods = r.json()["properties"]["periods"]
        for p in periods:
            date = p["startTime"][:10]
            temp = p["temperature"]
            if p.get("temperatureUnit") == "C":
                temp = round(temp * 9/5 + 32)
            if date not in daily_max or temp > daily_max[date]:
                daily_max[date] = temp
    except Exception as e:
        warn(f"Forecast error for {city_slug}: {e}")

    return daily_max

# =============================================================================
# POLYMARKET API
# =============================================================================

def get_polymarket_event(city_slug: str, month: str, day: int, year: int):
    """Find a weather market on Polymarket by its URL slug"""
    slug = f"highest-temperature-in-{city_slug}-on-{month}-{day}-{year}"
    url = f"https://gamma-api.polymarket.com/events?slug={slug}"
    try:
        r = requests.get(url, timeout=10)
        data = r.json()
        if data and isinstance(data, list) and len(data) > 0:
            return data[0]
    except Exception as e:
        warn(f"Polymarket API error: {e}")
    return None

# =============================================================================
# PARSING
# =============================================================================

def parse_temp_range(question: str):
    """Extract temperature range from a market question"""
    if not question:
        return None
    if "or below" in question.lower():
        m = re.search(r'(\d+)°F or below', question, re.IGNORECASE)
        if m: return (-999, int(m.group(1)))
    if "or higher" in question.lower():
        m = re.search(r'(\d+)°F or higher', question, re.IGNORECASE)
        if m: return (int(m.group(1)), 999)
    m = re.search(r'between (\d+)-(\d+)°F', question, re.IGNORECASE)
    if m: return (int(m.group(1)), int(m.group(2)))
    return None

def hours_until_resolution(event: dict) -> float:
    try:
        end_date = event.get("endDate") or event.get("end_date_iso")
        if not end_date: return 999
        end_dt = datetime.fromisoformat(end_date.replace("Z", "+00:00"))
        delta = (end_dt - datetime.now(timezone.utc)).total_seconds() / 3600
        return max(0, delta)
    except Exception:
        return 999

# =============================================================================
# SHOW POSITIONS
# =============================================================================

def show_positions():
    sim = load_sim()
    positions = sim["positions"]
    print(f"\n{C.BOLD}📊 Open Positions:{C.RESET}")
    if not positions:
        print("  No open positions")
        return

    total_pnl = 0
    for mid, pos in positions.items():
        try:
            url = f"https://gamma-api.polymarket.com/markets/{mid}"
            r = requests.get(url, timeout=5)
            prices = json.loads(r.json().get("outcomePrices", "[0.5,0.5]"))
            current_price = float(prices[0])
        except Exception:
            current_price = pos["entry_price"]

        pnl = (current_price - pos["entry_price"]) * pos["shares"]
        total_pnl += pnl
        pnl_str = f"{C.GREEN}+${pnl:.2f}{C.RESET}" if pnl >= 0 else f"{C.RED}-${abs(pnl):.2f}{C.RESET}"
        print(f"\n  • {pos['question'][:65]}...")
        print(f"    Entry: ${pos['entry_price']:.3f} | Now: ${current_price:.3f} | "
              f"Shares: {pos['shares']:.1f} | PnL: {pnl_str}")
        print(f"    Cost: ${pos['cost']:.2f}")

    print(f"\n  Balance:      ${sim['balance']:.2f}")
    pnl_color = C.GREEN if total_pnl >= 0 else C.RED
    print(f"  Open PnL:     {pnl_color}{'+'if total_pnl>=0 else ''}{total_pnl:.2f}{C.RESET}")
    print(f"  Total trades: {sim['total_trades']} | W/L: {sim['wins']}/{sim['losses']}")

# =============================================================================
# MAIN STRATEGY
# =============================================================================

def run(dry_run: bool = True):
    print(f"\n{C.BOLD}{C.CYAN}🌤  Weather Trading Bot v1{C.RESET}")
    print("=" * 50)

    sim = load_sim()
    balance = sim["balance"]
    positions = sim["positions"]
    trades_executed = 0
    exits_found = 0

    mode = f"{C.YELLOW}PAPER MODE{C.RESET}" if dry_run else f"{C.GREEN}LIVE MODE{C.RESET}"
    starting = sim["starting_balance"]
    total_return = (balance - starting) / starting * 100
    return_str = f"{C.GREEN}+{total_return:.1f}%{C.RESET}" if total_return >= 0 else f"{C.RED}{total_return:.1f}%{C.RESET}"

    print(f"\n  Mode:            {mode}")
    print(f"  Virtual balance: {C.BOLD}${balance:.2f}{C.RESET} (started ${starting:.2f}, {return_str})")
    print(f"  Position size:   {POSITION_PCT:.0%} of balance per trade")
    print(f"  Entry threshold: below ${ENTRY_THRESHOLD:.2f}")
    print(f"  Exit threshold:  above ${EXIT_THRESHOLD:.2f}")
    print(f"  Trades W/L:      {sim['wins']}/{sim['losses']}")

    # --- CHECK EXITS ---
    print(f"\n{C.BOLD}📤 Checking exits...{C.RESET}")
    for mid, pos in list(positions.items()):
        try:
            url = f"https://gamma-api.polymarket.com/markets/{mid}"
            r = requests.get(url, timeout=5)
            prices = json.loads(r.json().get("outcomePrices", "[0.5,0.5]"))
            current_price = float(prices[0])
        except Exception:
            continue

        if current_price >= EXIT_THRESHOLD:
            exits_found += 1
            pnl = (current_price - pos["entry_price"]) * pos["shares"]
            ok(f"EXIT: {pos['question'][:50]}...")
            info(f"Price ${current_price:.3f} >= exit ${EXIT_THRESHOLD:.2f} | PnL: +${pnl:.2f}")

            if not dry_run:
                balance += pos["cost"] + pnl
                sim["wins"] += 1 if pnl > 0 else 0
                sim["losses"] += 1 if pnl <= 0 else 0
                sim["trades"].append({
                    "type": "exit",
                    "question": pos["question"],
                    "entry_price": pos["entry_price"],
                    "exit_price": current_price,
                    "pnl": round(pnl, 2),
                    "cost": pos["cost"],
                    "closed_at": datetime.now().isoformat(),
                })
                del positions[mid]
                ok(f"Closed — PnL: {'+'if pnl>=0 else ''}{pnl:.2f}")
            else:
                skip("Paper mode — not selling")

    if exits_found == 0:
        skip("No exit opportunities")

    # --- SCAN ENTRIES ---
    print(f"\n{C.BOLD}🔍 Scanning for entry signals...{C.RESET}")

    for city_slug in ACTIVE_LOCATIONS:
        if city_slug not in LOCATIONS:
            warn(f"Unknown location: {city_slug}")
            continue

        loc_data = LOCATIONS[city_slug]
        forecast = get_forecast(city_slug)
        if not forecast:
            continue

        for i in range(0, 4):
            date = datetime.now() + timedelta(days=i)
            date_str = date.strftime("%Y-%m-%d")
            month = MONTHS[date.month - 1]
            day = date.day
            year = date.year

            forecast_temp = forecast.get(date_str)
            if forecast_temp is None:
                continue

            event = get_polymarket_event(city_slug, month, day, year)
            if not event:
                continue

            hours_left = hours_until_resolution(event)

            print(f"\n{C.BOLD}📍 {loc_data['name']} — {date_str}{C.RESET}")
            info(f"Forecast: {forecast_temp}°F | Resolves in: {hours_left:.0f}h")

            if hours_left < MIN_HOURS_LEFT:
                skip(f"Resolves in {hours_left:.0f}h — too soon")
                continue

            # Find matching temperature bucket
            matched = None
            for market in event.get("markets", []):
                question = market.get("question", "")
                rng = parse_temp_range(question)
                if rng and rng[0] <= forecast_temp <= rng[1]:
                    try:
                        prices = json.loads(market.get("outcomePrices", "[0.5,0.5]"))
                        yes_price = float(prices[0])
                    except Exception:
                        continue
                    matched = {
                        "market": market,
                        "question": question,
                        "price": yes_price,
                        "range": rng
                    }
                    break

            if not matched:
                skip(f"No bucket found for {forecast_temp}°F")
                continue

            price = matched["price"]
            market_id = matched["market"].get("id", "")
            question = matched["question"]

            info(f"Bucket: {question[:60]}")
            info(f"Market price: ${price:.3f}")

            if price >= ENTRY_THRESHOLD:
                skip(f"Price ${price:.3f} above threshold ${ENTRY_THRESHOLD:.2f}")
                continue

            position_size = round(balance * POSITION_PCT, 2)
            shares = position_size / price

            ok(f"SIGNAL — buying {shares:.1f} shares @ ${price:.3f} = ${position_size:.2f}")

            if market_id in positions:
                skip("Already in this market")
                continue

            if trades_executed >= MAX_TRADES:
                skip(f"Max trades ({MAX_TRADES}) reached")
                continue

            if position_size < 0.50:
                skip(f"Position size ${position_size:.2f} too small")
                continue

            if not dry_run:
                balance -= position_size
                positions[market_id] = {
                    "question": question,
                    "entry_price": price,
                    "shares": shares,
                    "cost": position_size,
                    "date": date_str,
                    "location": city_slug,
                    "forecast_temp": forecast_temp,
                    "opened_at": datetime.now().isoformat(),
                }
                sim["total_trades"] += 1
                sim["trades"].append({
                    "type": "entry",
                    "question": question,
                    "entry_price": price,
                    "shares": shares,
                    "cost": position_size,
                    "opened_at": datetime.now().isoformat(),
                })
                trades_executed += 1
                ok(f"Position opened — ${position_size:.2f} deducted from balance")
            else:
                skip("Paper mode — not buying")
                trades_executed += 1

    # Save state
    if not dry_run:
        sim["balance"] = round(balance, 2)
        sim["positions"] = positions
        sim["peak_balance"] = max(sim.get("peak_balance", balance), balance)
        save_sim(sim)

    # Summary
    print(f"\n{'=' * 50}")
    print(f"{C.BOLD}📊 Summary:{C.RESET}")
    info(f"Balance:         ${balance:.2f}")
    info(f"Trades this run: {trades_executed}")
    info(f"Exits found:     {exits_found}")

    if dry_run:
        print(f"\n  {C.YELLOW}[PAPER MODE — use --live to simulate trades]{C.RESET}")


# =============================================================================
# CLI
# =============================================================================

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Weather Trading Bot v1")
    parser.add_argument("--live", action="store_true", help="Execute trades (updates simulation balance)")
    parser.add_argument("--positions", action="store_true", help="Show open positions")
    parser.add_argument("--reset", action="store_true", help="Reset simulation to $1000")
    args = parser.parse_args()

    if args.reset:
        reset_sim()
    elif args.positions:
        show_positions()
    else:
        run(dry_run=not args.live)

```

---

### File: bot_v2.py (weatherbet.py — Full Bot)
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
weatherbet.py — Weather Trading Bot for Polymarket
=====================================================
Tracks weather forecasts from 3 sources (ECMWF, HRRR, METAR),
compares with Polymarket markets, paper trades using Kelly criterion.

Usage:
    python weatherbet.py          # main loop
    python weatherbet.py report   # full report
    python weatherbet.py status   # balance and open positions
"""

import re
import sys
import json
import math
import time
import requests
from datetime import datetime, timezone, timedelta
from pathlib import Path

# =============================================================================
# CONFIG
# =============================================================================

with open("config.json", encoding="utf-8") as f:
    _cfg = json.load(f)

BALANCE          = _cfg.get("balance", 10000.0)
MAX_BET          = _cfg.get("max_bet", 20.0)        # max bet per trade
MIN_EV           = _cfg.get("min_ev", 0.10)
MAX_PRICE        = _cfg.get("max_price", 0.45)
MIN_VOLUME       = _cfg.get("min_volume", 500)
MIN_HOURS        = _cfg.get("min_hours", 2.0)
MAX_HOURS        = _cfg.get("max_hours", 72.0)
KELLY_FRACTION   = _cfg.get("kelly_fraction", 0.25)
MAX_SLIPPAGE     = _cfg.get("max_slippage", 0.03)  # max allowed ask-bid spread
SCAN_INTERVAL    = _cfg.get("scan_interval", 3600)   # every hour
CALIBRATION_MIN  = _cfg.get("calibration_min", 30)
VC_KEY           = _cfg.get("vc_key", "")

SIGMA_F = 2.0
SIGMA_C = 1.2

DATA_DIR         = Path("data")
DATA_DIR.mkdir(exist_ok=True)
STATE_FILE       = DATA_DIR / "state.json"
MARKETS_DIR      = DATA_DIR / "markets"
MARKETS_DIR.mkdir(exist_ok=True)
CALIBRATION_FILE = DATA_DIR / "calibration.json"

LOCATIONS = {
    "nyc":          {"lat": 40.7772,  "lon":  -73.8726, "name": "New York City", "station": "KLGA", "unit": "F", "region": "us"},
    "chicago":      {"lat": 41.9742,  "lon":  -87.9073, "name": "Chicago",       "station": "KORD", "unit": "F", "region": "us"},
    "miami":        {"lat": 25.7959,  "lon":  -80.2870, "name": "Miami",         "station": "KMIA", "unit": "F", "region": "us"},
    "dallas":       {"lat": 32.8471,  "lon":  -96.8518, "name": "Dallas",        "station": "KDAL", "unit": "F", "region": "us"},
    "seattle":      {"lat": 47.4502,  "lon": -122.3088, "name": "Seattle",       "station": "KSEA", "unit": "F", "region": "us"},
    "atlanta":      {"lat": 33.6407,  "lon":  -84.4277, "name": "Atlanta",       "station": "KATL", "unit": "F", "region": "us"},
    "london":       {"lat": 51.5048,  "lon":    0.0495, "name": "London",        "station": "EGLC", "unit": "C", "region": "eu"},
    "paris":        {"lat": 48.9962,  "lon":    2.5979, "name": "Paris",         "station": "LFPG", "unit": "C", "region": "eu"},
    "munich":       {"lat": 48.3537,  "lon":   11.7750, "name": "Munich",        "station": "EDDM", "unit": "C", "region": "eu"},
    "ankara":       {"lat": 40.1281,  "lon":   32.9951, "name": "Ankara",        "station": "LTAC", "unit": "C", "region": "eu"},
    "seoul":        {"lat": 37.4691,  "lon":  126.4505, "name": "Seoul",         "station": "RKSI", "unit": "C", "region": "asia"},
    "tokyo":        {"lat": 35.7647,  "lon":  140.3864, "name": "Tokyo",         "station": "RJTT", "unit": "C", "region": "asia"},
    "shanghai":     {"lat": 31.1443,  "lon":  121.8083, "name": "Shanghai",      "station": "ZSPD", "unit": "C", "region": "asia"},
    "singapore":    {"lat":  1.3502,  "lon":  103.9940, "name": "Singapore",     "station": "WSSS", "unit": "C", "region": "asia"},
    "lucknow":      {"lat": 26.7606,  "lon":   80.8893, "name": "Lucknow",       "station": "VILK", "unit": "C", "region": "asia"},
    "tel-aviv":     {"lat": 32.0114,  "lon":   34.8867, "name": "Tel Aviv",      "station": "LLBG", "unit": "C", "region": "asia"},
    "toronto":      {"lat": 43.6772,  "lon":  -79.6306, "name": "Toronto",       "station": "CYYZ", "unit": "C", "region": "ca"},
    "sao-paulo":    {"lat": -23.4356, "lon":  -46.4731, "name": "Sao Paulo",     "station": "SBGR", "unit": "C", "region": "sa"},
    "buenos-aires": {"lat": -34.8222, "lon":  -58.5358, "name": "Buenos Aires",  "station": "SAEZ", "unit": "C", "region": "sa"},
    "wellington":   {"lat": -41.3272, "lon":  174.8052, "name": "Wellington",    "station": "NZWN", "unit": "C", "region": "oc"},
}

TIMEZONES = {
    "nyc": "America/New_York", "chicago": "America/Chicago",
    "miami": "America/New_York", "dallas": "America/Chicago",
    "seattle": "America/Los_Angeles", "atlanta": "America/New_York",
    "london": "Europe/London", "paris": "Europe/Paris",
    "munich": "Europe/Berlin", "ankara": "Europe/Istanbul",
    "seoul": "Asia/Seoul", "tokyo": "Asia/Tokyo",
    "shanghai": "Asia/Shanghai", "singapore": "Asia/Singapore",
    "lucknow": "Asia/Kolkata", "tel-aviv": "Asia/Jerusalem",
    "toronto": "America/Toronto", "sao-paulo": "America/Sao_Paulo",
    "buenos-aires": "America/Argentina/Buenos_Aires", "wellington": "Pacific/Auckland",
}

MONTHS = ["january","february","march","april","may","june",
          "july","august","september","october","november","december"]

# =============================================================================
# MATH
# =============================================================================

def norm_cdf(x):
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))

def bucket_prob(forecast, t_low, t_high, sigma=None):
    """For regular buckets — exact match. For edge buckets — normal distribution."""
    s = sigma or 2.0
    if t_low == -999:
        return norm_cdf((t_high - float(forecast)) / s)
    if t_high == 999:
        return 1.0 - norm_cdf((t_low - float(forecast)) / s)
    return 1.0 if in_bucket(forecast, t_low, t_high) else 0.0

def calc_ev(p, price):
    if price <= 0 or price >= 1: return 0.0
    return round(p * (1.0 / price - 1.0) - (1.0 - p), 4)

def calc_kelly(p, price):
    if price <= 0 or price >= 1: return 0.0
    b = 1.0 / price - 1.0
    f = (p * b - (1.0 - p)) / b
    return round(min(max(0.0, f) * KELLY_FRACTION, 1.0), 4)

def bet_size(kelly, balance):
    raw = kelly * balance
    return round(min(raw, MAX_BET), 2)

# =============================================================================
# CALIBRATION
# =============================================================================

_cal: dict = {}

def load_cal():
    if CALIBRATION_FILE.exists():
        return json.loads(CALIBRATION_FILE.read_text(encoding="utf-8"))
    return {}

def get_sigma(city_slug, source="ecmwf"):
    key = f"{city_slug}_{source}"
    if key in _cal:
        return _cal[key]["sigma"]
    return SIGMA_F if LOCATIONS[city_slug]["unit"] == "F" else SIGMA_C

def run_calibration(markets):
    """Recalculates sigma from resolved markets."""
    resolved = [m for m in markets if m.get("resolved") and m.get("actual_temp") is not None]
    cal = load_cal()
    updated = []

    for source in ["ecmwf", "hrrr", "metar"]:
        for city in set(m["city"] for m in resolved):
            group = [m for m in resolved if m["city"] == city]
            errors = []
            for m in group:
                snap = next((s for s in reversed(m.get("forecast_snapshots", []))
                             if s["source"] == source), None)
                if snap and snap.get("temp") is not None:
                    errors.append(abs(snap["temp"] - m["actual_temp"]))
            if len(errors) < CALIBRATION_MIN:
                continue
            mae  = sum(errors) / len(errors)
            key  = f"{city}_{source}"
            old  = cal.get(key, {}).get("sigma", SIGMA_F if LOCATIONS[city]["unit"] == "F" else SIGMA_C)
            new  = round(mae, 3)
            cal[key] = {"sigma": new, "n": len(errors), "updated_at": datetime.now(timezone.utc).isoformat()}
            if abs(new - old) > 0.05:
                updated.append(f"{LOCATIONS[city]['name']} {source}: {old:.2f}->{new:.2f}")

    CALIBRATION_FILE.write_text(json.dumps(cal, indent=2), encoding="utf-8")
    if updated:
        print(f"  [CAL] {', '.join(updated)}")
    return cal

# =============================================================================
# FORECASTS
# =============================================================================

def get_ecmwf(city_slug, dates):
    """ECMWF via Open-Meteo with bias correction. For all cities."""
    loc = LOCATIONS[city_slug]
    unit = loc["unit"]
    temp_unit = "fahrenheit" if unit == "F" else "celsius"
    result = {}
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={loc['lat']}&longitude={loc['lon']}"
        f"&daily=temperature_2m_max&temperature_unit={temp_unit}"
        f"&forecast_days=7&timezone={TIMEZONES.get(city_slug, 'UTC')}"
        f"&models=ecmwf_ifs025&bias_correction=true"
    )
    for attempt in range(3):
        try:
            data = requests.get(url, timeout=(5, 10)).json()
            if "error" not in data:
                for date, temp in zip(data["daily"]["time"], data["daily"]["temperature_2m_max"]):
                    if date in dates and temp is not None:
                        result[date] = round(temp, 1) if unit == "C" else round(temp)
            break
        except Exception as e:
            if attempt < 2:
                time.sleep(3)
            else:
                print(f"  [ECMWF] {city_slug}: {e}")
    return result

def get_hrrr(city_slug, dates):
    """HRRR via Open-Meteo. US cities only, up to 48h horizon."""
    loc = LOCATIONS[city_slug]
    if loc["region"] != "us":
        return {}
    result = {}
    url = (
        f"https://api.open-meteo.com/v1/forecast"
        f"?latitude={loc['lat']}&longitude={loc['lon']}"
        f"&daily=temperature_2m_max&temperature_unit=fahrenheit"
        f"&forecast_days=3&timezone={TIMEZONES.get(city_slug, 'UTC')}"
        f"&models=gfs_seamless"  # HRRR+GFS seamless — best option for US
    )
    for attempt in range(3):
        try:
            data = requests.get(url, timeout=(5, 10)).json()
            if "error" not in data:
                for date, temp in zip(data["daily"]["time"], data["daily"]["temperature_2m_max"]):
                    if date in dates and temp is not None:
                        result[date] = round(temp)
            break
        except Exception as e:
            if attempt < 2:
                time.sleep(3)
            else:
                print(f"  [HRRR] {city_slug}: {e}")
    return result

def get_metar(city_slug):
    """Current observed temperature from METAR station. D+0 only."""
    loc = LOCATIONS[city_slug]
    station = loc["station"]
    unit = loc["unit"]
    try:
        url = f"https://aviationweather.gov/api/data/metar?ids={station}&format=json"
        data = requests.get(url, timeout=(5, 8)).json()
        if data and isinstance(data, list):
            temp_c = data[0].get("temp")
            if temp_c is not None:
                if unit == "F":
                    return round(float(temp_c) * 9/5 + 32)
                return round(float(temp_c), 1)
    except Exception as e:
        print(f"  [METAR] {city_slug}: {e}")
    return None

def get_actual_temp(city_slug, date_str):
    """Actual temperature via Visual Crossing for closed markets."""
    loc = LOCATIONS[city_slug]
    station = loc["station"]
    unit = loc["unit"]
    vc_unit = "us" if unit == "F" else "metric"
    url = (
        f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline"
        f"/{station}/{date_str}/{date_str}"
        f"?unitGroup={vc_unit}&key={VC_KEY}&include=days&elements=tempmax"
    )
    try:
        data = requests.get(url, timeout=(5, 8)).json()
        days = data.get("days", [])
        if days and days[0].get("tempmax") is not None:
            return round(float(days[0]["tempmax"]), 1)
    except Exception as e:
        print(f"  [VC] {city_slug} {date_str}: {e}")
    return None

def check_market_resolved(market_id):
    """
    Checks if the market closed on Polymarket and who won.
    Returns: None (still open), True (YES won), False (NO won)
    """
    try:
        r = requests.get(f"https://gamma-api.polymarket.com/markets/{market_id}", timeout=(5, 8))
        data = r.json()
        closed = data.get("closed", False)
        if not closed:
            return None
        # Check YES price — if ~1.0 then WIN, if ~0.0 then LOSS
        prices = json.loads(data.get("outcomePrices", "[0.5,0.5]"))
        yes_price = float(prices[0])
        if yes_price >= 0.95:
            return True   # WIN
        elif yes_price <= 0.05:
            return False  # LOSS
        return None  # not yet determined
    except Exception as e:
        print(f"  [RESOLVE] {market_id}: {e}")
    return None

# =============================================================================
# POLYMARKET
# =============================================================================

def get_polymarket_event(city_slug, month, day, year):
    slug = f"highest-temperature-in-{city_slug}-on-{month}-{day}-{year}"
    try:
        r = requests.get(f"https://gamma-api.polymarket.com/events?slug={slug}", timeout=(5, 8))
        data = r.json()
        if data and isinstance(data, list) and len(data) > 0:
            return data[0]
    except Exception:
        pass
    return None

def get_market_price(market_id):
    try:
        r = requests.get(f"https://gamma-api.polymarket.com/markets/{market_id}", timeout=(3, 5))
        prices = json.loads(r.json().get("outcomePrices", "[0.5,0.5]"))
        return float(prices[0])
    except Exception:
        return None

def parse_temp_range(question):
    if not question: return None
    num = r'(-?\d+(?:\.\d+)?)'
    if re.search(r'or below', question, re.IGNORECASE):
        m = re.search(num + r'[°]?[FC] or below', question, re.IGNORECASE)
        if m: return (-999.0, float(m.group(1)))
    if re.search(r'or higher', question, re.IGNORECASE):
        m = re.search(num + r'[°]?[FC] or higher', question, re.IGNORECASE)
        if m: return (float(m.group(1)), 999.0)
    m = re.search(r'between ' + num + r'-' + num + r'[°]?[FC]', question, re.IGNORECASE)
    if m: return (float(m.group(1)), float(m.group(2)))
    m = re.search(r'be ' + num + r'[°]?[FC] on', question, re.IGNORECASE)
    if m:
        v = float(m.group(1))
        return (v, v)
    return None

def hours_to_resolution(end_date_str):
    try:
        end = datetime.fromisoformat(end_date_str.replace("Z", "+00:00"))
        return max(0.0, (end - datetime.now(timezone.utc)).total_seconds() / 3600)
    except Exception:
        return 999.0

def in_bucket(forecast, t_low, t_high):
    if t_low == t_high:
        return round(float(forecast)) == round(t_low)
    return t_low <= float(forecast) <= t_high

# =============================================================================
# MARKET DATA STORAGE
# Each market is stored in a separate file: data/markets/{city}_{date}.json
# =============================================================================

def market_path(city_slug, date_str):
    return MARKETS_DIR / f"{city_slug}_{date_str}.json"

def load_market(city_slug, date_str):
    p = market_path(city_slug, date_str)
    if p.exists():
        return json.loads(p.read_text(encoding="utf-8"))
    return None

def save_market(market):
    p = market_path(market["city"], market["date"])
    p.write_text(json.dumps(market, indent=2, ensure_ascii=False), encoding="utf-8")

def load_all_markets():
    markets = []
    for f in MARKETS_DIR.glob("*.json"):
        try:
            markets.append(json.loads(f.read_text(encoding="utf-8")))
        except Exception:
            pass
    return markets

def new_market(city_slug, date_str, event, hours):
    loc = LOCATIONS[city_slug]
    return {
        "city":               city_slug,
        "city_name":          loc["name"],
        "date":               date_str,
        "unit":               loc["unit"],
        "station":            loc["station"],
        "event_end_date":     event.get("endDate", ""),
        "hours_at_discovery": round(hours, 1),
        "status":             "open",           # open | closed | resolved
        "position":           None,             # filled when position opens
        "actual_temp":        None,             # filled after resolution
        "resolved_outcome":   None,             # win / loss / no_position
        "pnl":                None,
        "forecast_snapshots": [],               # list of forecast snapshots
        "market_snapshots":   [],               # list of market price snapshots
        "all_outcomes":       [],               # all market buckets
        "created_at":         datetime.now(timezone.utc).isoformat(),
    }

# =============================================================================
# STATE (balance and open positions)
# =============================================================================

def load_state():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return {
        "balance":          BALANCE,
        "starting_balance": BALANCE,
        "total_trades":     0,
        "wins":             0,
        "losses":           0,
        "peak_balance":     BALANCE,
    }

def save_state(state):
    STATE_FILE.write_text(json.dumps(state, indent=2, ensure_ascii=False), encoding="utf-8")

# =============================================================================
# CORE LOGIC
# =============================================================================

def take_forecast_snapshot(city_slug, dates):
    """Fetches forecasts from all sources and returns a snapshot."""
    now_str = datetime.now(timezone.utc).isoformat()
    ecmwf   = get_ecmwf(city_slug, dates)
    hrrr    = get_hrrr(city_slug, dates)
    today   = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    snapshots = {}
    for date in dates:
        snap = {
            "ts":    now_str,
            "ecmwf": ecmwf.get(date),
            "hrrr":  hrrr.get(date) if date <= (datetime.now(timezone.utc) + timedelta(days=2)).strftime("%Y-%m-%d") else None,
            "metar": get_metar(city_slug) if date == today else None,
        }
        # Best forecast: HRRR for US D+0/D+1, otherwise ECMWF
        loc = LOCATIONS[city_slug]
        if loc["region"] == "us" and snap["hrrr"] is not None:
            snap["best"] = snap["hrrr"]
            snap["best_source"] = "hrrr"
        elif snap["ecmwf"] is not None:
            snap["best"] = snap["ecmwf"]
            snap["best_source"] = "ecmwf"
        else:
            snap["best"] = None
            snap["best_source"] = None
        snapshots[date] = snap
    return snapshots

def scan_and_update():
    """Main function of one cycle: updates forecasts, opens/closes positions."""
    global _cal
    now      = datetime.now(timezone.utc)
    state    = load_state()
    balance  = state["balance"]
    new_pos  = 0
    closed   = 0
    resolved = 0

    for city_slug, loc in LOCATIONS.items():
        unit = loc["unit"]
        unit_sym = "F" if unit == "F" else "C"
        print(f"  -> {loc['name']}...", end=" ", flush=True)

        try:
            dates = [(now + timedelta(days=i)).strftime("%Y-%m-%d") for i in range(4)]
            snapshots = take_forecast_snapshot(city_slug, dates)
            time.sleep(0.3)
        except Exception as e:
            print(f"skipped ({e})")
            continue

        for i, date in enumerate(dates):
            dt    = datetime.strptime(date, "%Y-%m-%d")
            event = get_polymarket_event(city_slug, MONTHS[dt.month - 1], dt.day, dt.year)
            if not event:
                continue

            end_date = event.get("endDate", "")
            hours    = hours_to_resolution(end_date) if end_date else 0
            horizon  = f"D+{i}"

            # Load or create market record
            mkt = load_market(city_slug, date)
            if mkt is None:
                if hours < MIN_HOURS or hours > MAX_HOURS:
                    continue
                mkt = new_market(city_slug, date, event, hours)

            # Skip if market already resolved
            if mkt["status"] == "resolved":
                continue

            # Update outcomes list — prices taken directly from event
            outcomes = []
            for market in event.get("markets", []):
                question = market.get("question", "")
                mid      = str(market.get("id", ""))
                volume   = float(market.get("volume", 0))
                rng      = parse_temp_range(question)
                if not rng:
                    continue
                try:
                    prices = json.loads(market.get("outcomePrices", "[0.5,0.5]"))
                    bid = float(prices[0])
                    ask = float(prices[1]) if len(prices) > 1 else bid
                except Exception:
                    continue
                outcomes.append({
                    "question":  question,
                    "market_id": mid,
                    "range":     rng,
                    "bid":       round(bid, 4),
                    "ask":       round(ask, 4),
                    "price":     round(bid, 4),   # for compatibility
                    "spread":    round(ask - bid, 4),
                    "volume":    round(volume, 0),
                })

            outcomes.sort(key=lambda x: x["range"][0])
            mkt["all_outcomes"] = outcomes

            # Forecast snapshot
            snap = snapshots.get(date, {})
            forecast_snap = {
                "ts":          snap.get("ts"),
                "horizon":     horizon,
                "hours_left":  round(hours, 1),
                "ecmwf":       snap.get("ecmwf"),
                "hrrr":        snap.get("hrrr"),
                "metar":       snap.get("metar"),
                "best":        snap.get("best"),
                "best_source": snap.get("best_source"),
            }
            mkt["forecast_snapshots"].append(forecast_snap)

            # Market price snapshot
            top = max(outcomes, key=lambda x: x["price"]) if outcomes else None
            market_snap = {
                "ts":       snap.get("ts"),
                "top_bucket": f"{top['range'][0]}-{top['range'][1]}{unit_sym}" if top else None,
                "top_price":  top["price"] if top else None,
            }
            mkt["market_snapshots"].append(market_snap)

            forecast_temp = snap.get("best")
            best_source   = snap.get("best_source")

            # --- STOP-LOSS AND TRAILING STOP ---
            if mkt.get("position") and mkt["position"].get("status") == "open":
                pos = mkt["position"]
                current_price = None
                for o in outcomes:
                    if o["market_id"] == pos["market_id"]:
                        current_price = o["price"]
                        break

                if current_price is not None:
                    current_price = o.get("bid", current_price)  # sell at bid
                    entry = pos["entry_price"]
                    stop  = pos.get("stop_price", entry * 0.80)  # 20% stop by default

                    # Trailing: if up 20%+ — move stop to breakeven
                    if current_price >= entry * 1.20 and stop < entry:
                        pos["stop_price"] = entry
                        pos["trailing_activated"] = True

                    # Check stop
                    if current_price <= stop:
                        pnl = round((current_price - entry) * pos["shares"], 2)
                        balance += pos["cost"] + pnl
                        pos["closed_at"]    = snap.get("ts")
                        pos["close_reason"] = "stop_loss" if current_price < entry else "trailing_stop"
                        pos["exit_price"]   = current_price
                        pos["pnl"]          = pnl
                        pos["status"]       = "closed"
                        closed += 1
                        reason = "STOP" if current_price < entry else "TRAILING BE"
                        print(f"  [{reason}] {loc['name']} {date} | entry ${entry:.3f} exit ${current_price:.3f} | PnL: {'+'if pnl>=0 else ''}{pnl:.2f}")

            # --- CLOSE POSITION if forecast shifted 2+ degrees ---
            if mkt.get("position") and forecast_temp is not None:
                pos = mkt["position"]
                old_bucket_low  = pos["bucket_low"]
                old_bucket_high = pos["bucket_high"]
                # 2-degree buffer — avoid closing on small forecast fluctuations
                unit = loc["unit"]
                buffer = 2.0 if unit == "F" else 1.0
                mid_bucket = (old_bucket_low + old_bucket_high) / 2 if old_bucket_low != -999 and old_bucket_high != 999 else forecast_temp
                forecast_far = abs(forecast_temp - mid_bucket) > (abs(mid_bucket - old_bucket_low) + buffer)
                if not in_bucket(forecast_temp, old_bucket_low, old_bucket_high) and forecast_far:
                    current_price = None
                    for o in outcomes:
                        if o["market_id"] == pos["market_id"]:
                            current_price = o["price"]
                            break
                    if current_price is not None:
                        pnl = round((current_price - pos["entry_price"]) * pos["shares"], 2)
                        balance += pos["cost"] + pnl
                        mkt["position"]["closed_at"]    = snap.get("ts")
                        mkt["position"]["close_reason"] = "forecast_changed"
                        mkt["position"]["exit_price"]   = current_price
                        mkt["position"]["pnl"]          = pnl
                        mkt["position"]["status"]       = "closed"
                        closed += 1
                        print(f"  [CLOSE] {loc['name']} {date} — forecast changed | PnL: {'+'if pnl>=0 else ''}{pnl:.2f}")

            # --- OPEN POSITION ---
            if not mkt.get("position") and forecast_temp is not None and hours >= MIN_HOURS:
                sigma = get_sigma(city_slug, best_source or "ecmwf")
                best_signal = None

                # Find exactly ONE bucket that matches the forecast
                # If forecast doesn't fit any bucket cleanly — skip this market
                matched_bucket = None
                for o in outcomes:
                    t_low, t_high = o["range"]
                    if in_bucket(forecast_temp, t_low, t_high):
                        matched_bucket = o
                        break

                if matched_bucket:
                    o = matched_bucket
                    t_low, t_high = o["range"]
                    volume = o["volume"]
                    bid    = o.get("bid", o["price"])
                    ask    = o.get("ask", o["price"])
                    spread = o.get("spread", 0)

                    # All filters — if any fails, skip this market entirely
                    if volume >= MIN_VOLUME:
                        p  = bucket_prob(forecast_temp, t_low, t_high, sigma)
                        ev = calc_ev(p, ask)
                        if ev >= MIN_EV:
                            kelly = calc_kelly(p, ask)
                            size  = bet_size(kelly, balance)
                            if size >= 0.50:
                                best_signal = {
                                    "market_id":    o["market_id"],
                                    "question":     o["question"],
                                    "bucket_low":   t_low,
                                    "bucket_high":  t_high,
                                    "entry_price":  ask,
                                    "bid_at_entry": bid,
                                    "spread":       spread,
                                    "shares":       round(size / ask, 2),
                                    "cost":         size,
                                    "p":            round(p, 4),
                                    "ev":           round(ev, 4),
                                    "kelly":        round(kelly, 4),
                                    "forecast_temp":forecast_temp,
                                    "forecast_src": best_source,
                                    "sigma":        sigma,
                                    "opened_at":    snap.get("ts"),
                                    "status":       "open",
                                    "pnl":          None,
                                    "exit_price":   None,
                                    "close_reason": None,
                                    "closed_at":    None,
                                }

                if best_signal:
                    # Fetch real bestAsk from Polymarket API for accurate entry price
                    skip_position = False
                    try:
                        r = requests.get(f"https://gamma-api.polymarket.com/markets/{best_signal['market_id']}", timeout=(3, 5))
                        mdata = r.json()
                        real_ask = float(mdata.get("bestAsk", best_signal["entry_price"]))
                        real_bid = float(mdata.get("bestBid", best_signal["bid_at_entry"]))
                        real_spread = round(real_ask - real_bid, 4)
                        # Re-check slippage and price with real values
                        if real_spread > MAX_SLIPPAGE or real_ask >= MAX_PRICE:
                            print(f"  [SKIP] {loc['name']} {date} — real ask ${real_ask:.3f} spread ${real_spread:.3f}")
                            skip_position = True
                        else:
                            best_signal["entry_price"]  = real_ask
                            best_signal["bid_at_entry"] = real_bid
                            best_signal["spread"]       = real_spread
                            best_signal["shares"]       = round(best_signal["cost"] / real_ask, 2)
                            best_signal["ev"]           = round(calc_ev(best_signal["p"], real_ask), 4)
                    except Exception as e:
                        print(f"  [WARN] Could not fetch real ask for {best_signal['market_id']}: {e}")

                    if not skip_position and best_signal["entry_price"] < MAX_PRICE:
                        balance -= best_signal["cost"]
                        mkt["position"] = best_signal
                        state["total_trades"] += 1
                        new_pos += 1
                        bucket_label = f"{best_signal['bucket_low']}-{best_signal['bucket_high']}{unit_sym}"
                        print(f"  [BUY]  {loc['name']} {horizon} {date} | {bucket_label} | "
                              f"${best_signal['entry_price']:.3f} | EV {best_signal['ev']:+.2f} | "
                              f"${best_signal['cost']:.2f} ({best_signal['forecast_src'].upper()})")

            # Market closed by time
            if hours < 0.5 and mkt["status"] == "open":
                mkt["status"] = "closed"

            save_market(mkt)
            time.sleep(0.1)

        print("ok")

    # --- AUTO-RESOLUTION ---
    for mkt in load_all_markets():
        if mkt["status"] == "resolved":
            continue

        pos = mkt.get("position")
        if not pos or pos.get("status") != "open":
            continue

        market_id = pos.get("market_id")
        if not market_id:
            continue

        # Check if market closed on Polymarket
        won = check_market_resolved(market_id)
        if won is None:
            continue  # market still open

        # Market closed — record result
        price  = pos["entry_price"]
        size   = pos["cost"]
        shares = pos["shares"]
        pnl    = round(shares * (1 - price), 2) if won else round(-size, 2)

        balance += size + pnl
        pos["exit_price"]   = 1.0 if won else 0.0
        pos["pnl"]          = pnl
        pos["close_reason"] = "resolved"
        pos["closed_at"]    = now.isoformat()
        pos["status"]       = "closed"
        mkt["pnl"]          = pnl
        mkt["status"]       = "resolved"
        mkt["resolved_outcome"] = "win" if won else "loss"

        if won:
            state["wins"] += 1
        else:
            state["losses"] += 1

        result = "WIN" if won else "LOSS"
        print(f"  [{result}] {mkt['city_name']} {mkt['date']} | PnL: {'+'if pnl>=0 else ''}{pnl:.2f}")
        resolved += 1

        save_market(mkt)
        time.sleep(0.3)

    state["balance"]      = round(balance, 2)
    state["peak_balance"] = max(state.get("peak_balance", balance), balance)
    save_state(state)

    # Run calibration if enough data collected
    all_mkts = load_all_markets()
    resolved_count = len([m for m in all_mkts if m["status"] == "resolved"])
    if resolved_count >= CALIBRATION_MIN:
        global _cal
        _cal = run_calibration(all_mkts)

    return new_pos, closed, resolved

# =============================================================================
# REPORT
# =============================================================================

def print_status():
    state    = load_state()
    markets  = load_all_markets()
    open_pos = [m for m in markets if m.get("position") and m["position"].get("status") == "open"]
    resolved = [m for m in markets if m["status"] == "resolved" and m.get("pnl") is not None]

    bal     = state["balance"]
    start   = state["starting_balance"]
    ret_pct = (bal - start) / start * 100
    wins    = state["wins"]
    losses  = state["losses"]
    total   = wins + losses

    print(f"\n{'='*55}")
    print(f"  WEATHERBET — STATUS")
    print(f"{'='*55}")
    print(f"  Balance:     ${bal:,.2f}  (start ${start:,.2f}, {'+'if ret_pct>=0 else ''}{ret_pct:.1f}%)")
    print(f"  Trades:      {total} | W: {wins} | L: {losses} | WR: {wins/total:.0%}" if total else "  No trades yet")
    print(f"  Open:        {len(open_pos)}")
    print(f"  Resolved:    {len(resolved)}")

    if open_pos:
        print(f"\n  Open positions:")
        total_unrealized = 0.0
        for m in open_pos:
            pos      = m["position"]
            unit_sym = "F" if m["unit"] == "F" else "C"
            label    = f"{pos['bucket_low']}-{pos['bucket_high']}{unit_sym}"

            # Current price from latest market snapshot
            current_price = pos["entry_price"]
            snaps = m.get("market_snapshots", [])
            if snaps:
                # Find our bucket price in all_outcomes
                for o in m.get("all_outcomes", []):
                    if o["market_id"] == pos["market_id"]:
                        current_price = o["price"]
                        break

            unrealized = round((current_price - pos["entry_price"]) * pos["shares"], 2)
            total_unrealized += unrealized
            pnl_str = f"{'+'if unrealized>=0 else ''}{unrealized:.2f}"

            print(f"    {m['city_name']:<16} {m['date']} | {label:<14} | "
                  f"entry ${pos['entry_price']:.3f} -> ${current_price:.3f} | "
                  f"PnL: {pnl_str} | {pos['forecast_src'].upper()}")

        sign = "+" if total_unrealized >= 0 else ""
        print(f"\n  Unrealized PnL: {sign}{total_unrealized:.2f}")

    print(f"{'='*55}\n")

def print_report():
    markets  = load_all_markets()
    resolved = [m for m in markets if m["status"] == "resolved" and m.get("pnl") is not None]

    print(f"\n{'='*55}")
    print(f"  WEATHERBET — FULL REPORT")
    print(f"{'='*55}")

    if not resolved:
        print("  No resolved markets yet.")
        return

    total_pnl = sum(m["pnl"] for m in resolved)
    wins      = [m for m in resolved if m["resolved_outcome"] == "win"]
    losses    = [m for m in resolved if m["resolved_outcome"] == "loss"]

    print(f"\n  Total resolved: {len(resolved)}")
    print(f"  Wins:           {len(wins)} | Losses: {len(losses)}")
    print(f"  Win rate:       {len(wins)/len(resolved):.0%}")
    print(f"  Total PnL:      {'+'if total_pnl>=0 else ''}{total_pnl:.2f}")

    print(f"\n  By city:")
    for city in sorted(set(m["city"] for m in resolved)):
        group = [m for m in resolved if m["city"] == city]
        w     = len([m for m in group if m["resolved_outcome"] == "win"])
        pnl   = sum(m["pnl"] for m in group)
        name  = LOCATIONS[city]["name"]
        print(f"    {name:<16} {w}/{len(group)} ({w/len(group):.0%})  PnL: {'+'if pnl>=0 else ''}{pnl:.2f}")

    print(f"\n  Market details:")
    for m in sorted(resolved, key=lambda x: x["date"]):
        pos      = m.get("position", {})
        unit_sym = "F" if m["unit"] == "F" else "C"
        snaps    = m.get("forecast_snapshots", [])
        first_fc = snaps[0]["best"] if snaps else None
        last_fc  = snaps[-1]["best"] if snaps else None
        label    = f"{pos.get('bucket_low')}-{pos.get('bucket_high')}{unit_sym}" if pos else "no position"
        result   = m["resolved_outcome"].upper()
        pnl_str  = f"{'+'if m['pnl']>=0 else ''}{m['pnl']:.2f}" if m["pnl"] is not None else "-"
        fc_str   = f"forecast {first_fc}->{last_fc}{unit_sym}" if first_fc else "no forecast"
        actual   = f"actual {m['actual_temp']}{unit_sym}" if m["actual_temp"] else ""
        print(f"    {m['city_name']:<16} {m['date']} | {label:<14} | {fc_str} | {actual} | {result} {pnl_str}")

    print(f"{'='*55}\n")

# =============================================================================
# MAIN LOOP
# =============================================================================

MONITOR_INTERVAL = 600  # monitor positions every 10 minutes

def monitor_positions():
    """Quick stop check on open positions without full scan."""
    markets  = load_all_markets()
    open_pos = [m for m in markets if m.get("position") and m["position"].get("status") == "open"]
    if not open_pos:
        return 0

    state   = load_state()
    balance = state["balance"]
    closed  = 0

    for mkt in open_pos:
        pos = mkt["position"]
        mid = pos["market_id"]

        # Fetch real bestBid from Polymarket API — actual sell price
        current_price = None
        try:
            r = requests.get(f"https://gamma-api.polymarket.com/markets/{mid}", timeout=(3, 5))
            mdata = r.json()
            best_bid = mdata.get("bestBid")
            if best_bid is not None:
                current_price = float(best_bid)
        except Exception:
            pass

        # Fallback to cached price if API failed
        if current_price is None:
            for o in mkt.get("all_outcomes", []):
                if o["market_id"] == mid:
                    current_price = o.get("bid", o["price"])
                    break

        if current_price is None:
            continue

        entry = pos["entry_price"]
        stop  = pos.get("stop_price", entry * 0.80)
        city_name = LOCATIONS.get(mkt["city"], {}).get("name", mkt["city"])

        # Hours left to resolution
        end_date = mkt.get("event_end_date", "")
        hours_left = hours_to_resolution(end_date) if end_date else 999.0

        # Take-profit threshold based on hours to resolution
        if hours_left < 24:
            take_profit = None        # hold to resolution
        elif hours_left < 48:
            take_profit = 0.85        # 24-48h: take profit at $0.85
        else:
            take_profit = 0.75        # 48h+: take profit at $0.75

        # Trailing: if up 20%+ — move stop to breakeven
        if current_price >= entry * 1.20 and stop < entry:
            pos["stop_price"] = entry
            pos["trailing_activated"] = True
            print(f"  [TRAILING] {city_name} {mkt['date']} — stop moved to breakeven ${entry:.3f}")

        # Check take-profit
        take_triggered = take_profit is not None and current_price >= take_profit
        # Check stop
        stop_triggered = current_price <= stop

        if take_triggered or stop_triggered:
            pnl = round((current_price - entry) * pos["shares"], 2)
            balance += pos["cost"] + pnl
            pos["closed_at"]    = datetime.now(timezone.utc).isoformat()
            if take_triggered:
                pos["close_reason"] = "take_profit"
                reason = "TAKE"
            elif current_price < entry:
                pos["close_reason"] = "stop_loss"
                reason = "STOP"
            else:
                pos["close_reason"] = "trailing_stop"
                reason = "TRAILING BE"
            pos["exit_price"]   = current_price
            pos["pnl"]          = pnl
            pos["status"]       = "closed"
            closed += 1
            print(f"  [{reason}] {city_name} {mkt['date']} | entry ${entry:.3f} exit ${current_price:.3f} | {hours_left:.0f}h left | PnL: {'+'if pnl>=0 else ''}{pnl:.2f}")
            save_market(mkt)

    if closed:
        state["balance"] = round(balance, 2)
        save_state(state)

    return closed


def run_loop():
    global _cal
    _cal = load_cal()

    print(f"\n{'='*55}")
    print(f"  WEATHERBET — STARTING")
    print(f"{'='*55}")
    print(f"  Cities:     {len(LOCATIONS)}")
    print(f"  Balance:    ${BALANCE:,.0f} | Max bet: ${MAX_BET}")
    print(f"  Scan:       {SCAN_INTERVAL//60} min | Monitor: {MONITOR_INTERVAL//60} min")
    print(f"  Sources:    ECMWF + HRRR(US) + METAR(D+0)")
    print(f"  Data:       {DATA_DIR.resolve()}")
    print(f"  Ctrl+C to stop\n")

    last_full_scan = 0

    while True:
        now_ts  = time.time()
        now_str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # Full scan once per hour
        if now_ts - last_full_scan >= SCAN_INTERVAL:
            print(f"[{now_str}] full scan...")
            try:
                new_pos, closed, resolved = scan_and_update()
                state = load_state()
                print(f"  balance: ${state['balance']:,.2f} | "
                      f"new: {new_pos} | closed: {closed} | resolved: {resolved}")
                last_full_scan = time.time()
            except KeyboardInterrupt:
                print(f"\n  Stopping — saving state...")
                save_state(load_state())
                print(f"  Done. Bye!")
                break
            except requests.exceptions.ConnectionError:
                print(f"  Connection lost — waiting 60 sec")
                time.sleep(60)
                continue
            except Exception as e:
                print(f"  Error: {e} — waiting 60 sec")
                time.sleep(60)
                continue
        else:
            # Quick stop monitoring
            print(f"[{now_str}] monitoring positions...")
            try:
                stopped = monitor_positions()
                if stopped:
                    state = load_state()
                    print(f"  balance: ${state['balance']:,.2f}")
            except Exception as e:
                print(f"  Monitor error: {e}")

        try:
            time.sleep(MONITOR_INTERVAL)
        except KeyboardInterrupt:
            print(f"\n  Stopping — saving state...")
            save_state(load_state())
            print(f"  Done. Bye!")
            break

# =============================================================================
# CLI
# =============================================================================

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "run"
    if cmd == "run":
        run_loop()
    elif cmd == "status":
        _cal = load_cal()
        print_status()
    elif cmd == "report":
        _cal = load_cal()
        print_report()
    else:
        print("Usage: python weatherbet.py [run|status|report]")

```

---

### File: sim_dashboard_repost.html
```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<title>Weather Bot — Kelly Simulation</title>
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700;900&display=swap" rel="stylesheet">
<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/4.4.0/chart.umd.min.js"></script>
<style>
:root{--bg:#000;--bg2:#020c02;--border:#0a2a0a;--green:#00ff41;--green-dim:rgba(0,255,65,.08);--green-glow:rgba(0,255,65,.4);--red:#ff2244;--red-dim:rgba(255,34,68,.08);--yellow:#ffcc00;--text:#88ff88;--text2:#2a5a2a;--mono:'Share Tech Mono',monospace;--display:'Orbitron',sans-serif;}
*{margin:0;padding:0;box-sizing:border-box;}
body{background:var(--bg);color:var(--text);font-family:var(--mono);min-height:100vh;overflow-x:hidden;}
body::before{content:'';position:fixed;inset:0;background:repeating-linear-gradient(0deg,transparent,transparent 2px,rgba(0,255,65,.015) 2px,rgba(0,255,65,.015) 4px);pointer-events:none;z-index:999;}
body::after{content:'';position:fixed;inset:0;background-image:linear-gradient(rgba(0,255,65,.03) 1px,transparent 1px),linear-gradient(90deg,rgba(0,255,65,.03) 1px,transparent 1px);background-size:32px 32px;pointer-events:none;}
.wrap{position:relative;z-index:1;max-width:1400px;margin:0 auto;padding:24px 28px;}
.header{display:flex;align-items:flex-start;justify-content:space-between;margin-bottom:24px;padding-bottom:18px;border-bottom:1px solid var(--border);position:relative;}
.header::after{content:'';position:absolute;bottom:-1px;left:0;width:35%;height:1px;background:var(--green);box-shadow:0 0 12px var(--green-glow);}
.brand-title{font-family:var(--display);font-size:24px;font-weight:900;color:var(--green);letter-spacing:3px;text-shadow:0 0 20px var(--green-glow);line-height:1;}
.brand-sub{font-size:10px;color:var(--text2);letter-spacing:2px;margin-top:4px;}
.header-right{display:flex;flex-direction:column;align-items:flex-end;gap:5px;}
.live-pill{display:flex;align-items:center;gap:6px;font-size:11px;letter-spacing:1px;color:var(--green);}
.dot{width:7px;height:7px;border-radius:50%;background:var(--green);box-shadow:0 0 6px var(--green);animation:pulse 1.5s infinite;}
.dot.gray{background:var(--text2);box-shadow:none;animation:none;}
@keyframes pulse{0%,100%{opacity:1;}50%{opacity:.2;}}
.ts{font-size:10px;color:var(--text2);}
.stats{display:grid;grid-template-columns:repeat(6,1fr);gap:10px;margin-bottom:20px;}
.stat{background:var(--bg2);border:1px solid var(--border);border-radius:4px;padding:13px 15px;position:relative;overflow:hidden;}
.stat::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,var(--green),transparent);opacity:.5;}
.stat-label{font-size:9px;color:var(--text2);letter-spacing:2px;text-transform:uppercase;margin-bottom:5px;}
.stat-val{font-family:var(--display);font-size:20px;font-weight:700;color:var(--green);line-height:1;text-shadow:0 0 10px rgba(0,255,65,.3);transition:all .3s;}
.stat-val.red{color:var(--red);text-shadow:0 0 10px rgba(255,34,68,.3);}
.stat-val.yellow{color:var(--yellow);}
.stat-sub{font-size:9px;color:var(--text2);margin-top:3px;}
.layout{display:grid;grid-template-columns:1fr 340px;gap:14px;margin-bottom:14px;}
.chart-card{background:var(--bg2);border:1px solid var(--border);border-radius:4px;overflow:hidden;position:relative;}
.chart-card::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,transparent,var(--green),transparent);opacity:.4;}
.card-head{padding:10px 15px;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;}
.card-title{font-size:10px;color:var(--text2);letter-spacing:2px;text-transform:uppercase;}
.card-badge{font-size:9px;padding:2px 8px;border-radius:2px;background:var(--green-dim);color:var(--green);border:1px solid rgba(0,255,65,.2);letter-spacing:1px;}
.chart-body{padding:16px;position:relative;}
.chart-wrap{height:220px;position:relative;}
.deltas{position:absolute;inset:0;pointer-events:none;overflow:hidden;}
.delta{position:absolute;font-size:11px;font-weight:600;padding:2px 7px;border-radius:3px;animation:floatUp 2.5s ease forwards;white-space:nowrap;}
.delta.pos{color:var(--green);background:rgba(0,255,65,.08);border:1px solid rgba(0,255,65,.2);text-shadow:0 0 6px var(--green);}
.delta.neg{color:var(--red);background:var(--red-dim);border:1px solid rgba(255,34,68,.2);}
@keyframes floatUp{0%{opacity:0;transform:translateY(0);}15%{opacity:1;}80%{opacity:1;}100%{opacity:0;transform:translateY(-45px);}}
.panel{background:var(--bg2);border:1px solid var(--border);border-radius:4px;overflow:hidden;position:relative;}
.panel::before{content:'';position:absolute;top:0;left:0;right:0;height:1px;background:linear-gradient(90deg,var(--green),transparent);opacity:.4;}
.scroll{max-height:290px;overflow-y:auto;}
.scroll::-webkit-scrollbar{width:2px;}
.scroll::-webkit-scrollbar-thumb{background:var(--border);}
.bot-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;}
.trade-item{padding:9px 14px;border-bottom:1px solid var(--border);display:flex;align-items:center;gap:10px;animation:slideIn .3s ease;}
.trade-item:last-child{border-bottom:none;}
@keyframes slideIn{from{opacity:0;transform:translateX(-6px);}to{opacity:1;transform:none;}}
.t-time{font-size:9px;color:var(--text2);flex-shrink:0;width:60px;}
.t-badge{font-size:9px;padding:2px 7px;border-radius:2px;flex-shrink:0;letter-spacing:1px;border:1px solid;}
.t-badge.buy{color:var(--green);border-color:rgba(0,255,65,.25);background:var(--green-dim);}
.t-badge.win{color:#44ffaa;border-color:rgba(68,255,170,.25);background:rgba(68,255,170,.06);}
.t-badge.loss{color:var(--red);border-color:rgba(255,34,68,.25);background:var(--red-dim);}
.t-info{flex:1;min-width:0;}
.t-q{font-size:10px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis;color:var(--text);margin-bottom:2px;}
.t-meta{font-size:9px;color:var(--text2);}
.t-right{text-align:right;flex-shrink:0;}
.t-amount{font-size:11px;font-weight:600;}
.t-amount.pos{color:var(--green);}
.t-amount.neg{color:var(--red);}
.pos-item{padding:10px 14px;border-bottom:1px solid var(--border);animation:slideIn .35s ease;}
.pos-item:last-child{border-bottom:none;}
.pos-top{display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:5px;}
.pos-q{font-size:11px;color:var(--text);flex:1;margin-right:10px;line-height:1.3;}
.pos-pnl{font-size:12px;font-weight:700;flex-shrink:0;}
.pos-pnl.pos{color:var(--green);}
.pos-pnl.neg{color:var(--red);}
.pos-bar{height:2px;background:var(--border);border-radius:2px;overflow:hidden;margin-bottom:4px;}
.pos-fill{height:100%;background:var(--green);border-radius:2px;transition:width .8s;box-shadow:0 0 4px var(--green);}
.pos-meta{display:flex;gap:12px;font-size:9px;color:var(--text2);}
.pos-meta span{color:var(--yellow);}
.empty{padding:28px;text-align:center;color:var(--text2);font-size:10px;letter-spacing:2px;}
.no-server{padding:20px 24px;margin:0;background:rgba(255,204,0,.04);border:1px solid rgba(255,204,0,.15);border-radius:4px;font-size:11px;color:var(--yellow);line-height:1.7;}
.no-server code{background:rgba(0,255,65,.06);border:1px solid rgba(0,255,65,.15);padding:1px 6px;border-radius:2px;color:var(--green);font-family:var(--mono);}
.footer{margin-top:12px;padding-top:10px;border-top:1px solid var(--border);display:flex;justify-content:space-between;align-items:center;}
.footer-text{font-size:9px;color:var(--text2);letter-spacing:1px;}
.sim-badge{font-size:9px;padding:2px 8px;border-radius:2px;background:rgba(255,204,0,.06);color:var(--yellow);border:1px solid rgba(255,204,0,.2);}
</style>
</head>
<body>
<div class="wrap">

<div class="header">
  <div>
    <div class="brand-title">WEATHER BOT — KELLY SIM</div>
    <div class="brand-sub">Polymarket · Open-Meteo · Kelly Criterion · EV Analysis</div>
  </div>
  <div class="header-right">
    <div class="live-pill"><div class="dot" id="status-dot"></div><span id="status-text">CONNECTING...</span></div>
    <div class="ts" id="ts">—</div>
  </div>
</div>

<div id="no-server-msg" class="no-server" style="display:none;margin-bottom:20px;">
  ⚠️ &nbsp;Dashboard needs a local server to read <code>simulation.json</code>.<br>
  Run this command in your <code>weatherbot</code> folder, then refresh:<br><br>
  <code>python -m http.server 8000</code><br><br>
  Then open: <code>http://localhost:8000/sim_dashboard.html</code>
</div>

<div class="stats">
  <div class="stat"><div class="stat-label">Balance</div><div class="stat-val" id="s-bal">—</div><div class="stat-sub">virtual USDC</div></div>
  <div class="stat"><div class="stat-label">Total PnL</div><div class="stat-val" id="s-pnl">—</div><div class="stat-sub" id="s-pct">vs $1,000 start</div></div>
  <div class="stat"><div class="stat-label">Open Positions</div><div class="stat-val" id="s-open">—</div><div class="stat-sub">active trades</div></div>
  <div class="stat"><div class="stat-label">Win Rate</div><div class="stat-val yellow" id="s-wr">—</div><div class="stat-sub" id="s-wl">0W / 0L</div></div>
  <div class="stat"><div class="stat-label">Total Trades</div><div class="stat-val" id="s-total">—</div><div class="stat-sub">all time</div></div>
  <div class="stat"><div class="stat-label">Peak Balance</div><div class="stat-val" id="s-peak">—</div><div class="stat-sub">all time high</div></div>
</div>

<div class="layout">
  <div class="chart-card">
    <div class="card-head"><span class="card-title">Balance History</span><span class="card-badge">KELLY-SIZED POSITIONS</span></div>
    <div class="chart-body">
      <div class="chart-wrap">
        <canvas id="chart"></canvas>
        <div class="deltas" id="deltas"></div>
      </div>
    </div>
  </div>
  <div class="panel">
    <div class="card-head"><span class="card-title">Open Positions</span><span class="card-badge" id="pos-badge">0 ACTIVE</span></div>
    <div class="scroll" id="pos-list"><div class="empty">Waiting for bot data...</div></div>
  </div>
</div>

<div class="bot-grid">
  <div class="panel">
    <div class="card-head"><span class="card-title">Trade History</span><span class="card-badge">FROM simulation.json</span></div>
    <div class="scroll" id="trade-list"><div class="empty">No trades yet — run: python weather_bot_v2.py --live</div></div>
  </div>
  <div class="panel">
    <div class="card-head"><span class="card-title">Kelly + EV Log</span><span class="card-badge">ENTRIES ONLY</span></div>
    <div class="scroll" id="ev-log"><div class="empty">No entries yet</div></div>
  </div>
</div>

<div class="footer">
  <div class="footer-text">Weather Bot v2 · Reads from simulation.json · Refreshes every 10s</div>
  <div class="sim-badge">⚡ $1,000 SIMULATION</div>
</div>
</div>

<script>
const fmt2=v=>(v>=0?'+':'')+v.toFixed(2);
const fmtUSD=v=>'$'+Math.abs(v).toFixed(2);
const now=()=>new Date().toLocaleTimeString('en-US',{hour12:false});
const rand=(a,b)=>Math.random()*(b-a)+a;

let prevBal=null, chart=null, balHistory=[], timeLabels=[];

// Init chart
chart=new Chart(document.getElementById('chart'),{
  type:'line',
  data:{labels:[],datasets:[{data:[],borderColor:'#00ff41',backgroundColor:'rgba(0,255,65,.06)',fill:true,tension:.45,pointRadius:0,borderWidth:2}]},
  options:{responsive:true,maintainAspectRatio:false,animation:{duration:400},plugins:{legend:{display:false},tooltip:{backgroundColor:'#020c02',borderColor:'#0a2a0a',borderWidth:1,callbacks:{label:c=>'$'+c.parsed.y.toFixed(2)}}},scales:{x:{ticks:{color:'#1a3a1a',font:{family:'Share Tech Mono',size:8},maxTicksLimit:8},grid:{color:'#050f05'}},y:{ticks:{color:'#2a5a2a',font:{family:'Share Tech Mono',size:9}},grid:{color:'#050f05'}}}}
});

function spawnDelta(v){
  const l=document.getElementById('deltas');
  const e=document.createElement('div');
  e.className='delta '+(v>=0?'pos':'neg');
  e.textContent=(v>=0?'+ $':'- $')+Math.abs(v).toFixed(2);
  e.style.left=rand(30,l.offsetWidth-120)+'px';
  e.style.top=rand(l.offsetHeight*.2,l.offsetHeight*.7)+'px';
  l.appendChild(e);
  setTimeout(()=>e.remove(),2500);
}

function renderPositions(positions){
  const el=document.getElementById('pos-list');
  document.getElementById('pos-badge').textContent=Object.keys(positions).length+' ACTIVE';
  if(!Object.keys(positions).length){el.innerHTML='<div class="empty">No open positions</div>';return;}
  el.innerHTML=Object.entries(positions).map(([id,p])=>{
    const pnl=p.pnl||0;
    const pct=(p.current_price||p.entry_price)*100;
    return`<div class="pos-item">
      <div class="pos-top">
        <div class="pos-q">${(p.question||'').substr(0,58)}...</div>
        <div class="pos-pnl ${pnl>=0?'pos':'neg'}">${pnl>=0?'+':'-'}$${Math.abs(pnl).toFixed(2)}</div>
      </div>
      <div class="pos-bar"><div class="pos-fill" style="width:${Math.min(100,pct)}%"></div></div>
      <div class="pos-meta">
        <div>${p.location||''}</div>
        <div>Kelly: <span>${((p.kelly_pct||0)*100).toFixed(1)}%</span></div>
        <div>EV: <span>${fmt2(p.ev||0)}</span></div>
        <div>$${(p.cost||0).toFixed(2)} in</div>
      </div>
    </div>`;
  }).join('');
}

function renderTrades(trades){
  const el=document.getElementById('trade-list');
  if(!trades||!trades.length){el.innerHTML='<div class="empty">No trades yet — run: python weather_bot_v2.py --live</div>';return;}
  const recent=[...trades].reverse().slice(0,15);
  el.innerHTML=recent.map(t=>{
    const isEntry=t.type==='entry';
    const isWin=t.type==='exit'&&(t.pnl||0)>0;
    const cls=isEntry?'buy':isWin?'win':'loss';
    const label=isEntry?'BUY':isWin?'WIN':'LOSS';
    const amtStr=isEntry?`-$${(t.cost||0).toFixed(2)}`:(t.pnl||0)>=0?`+$${(t.pnl||0).toFixed(2)}`:`-$${Math.abs(t.pnl||0).toFixed(2)}`;
    const amtCls=isEntry?'neg':(t.pnl||0)>=0?'pos':'neg';
    const time=(t.opened_at||t.closed_at||'').substr(11,5)||'—';
    return`<div class="trade-item">
      <div class="t-time">${time}</div>
      <span class="t-badge ${cls}">${label}</span>
      <div class="t-info">
        <div class="t-q">${(t.question||'').substr(0,45)}...</div>
        <div class="t-meta">Kelly ${((t.kelly_pct||0)*100).toFixed(1)}% · EV ${fmt2(t.ev||0)}</div>
      </div>
      <div class="t-right"><div class="t-amount ${amtCls}">${amtStr}</div></div>
    </div>`;
  }).join('');
}

function renderEvLog(trades){
  const el=document.getElementById('ev-log');
  const entries=(trades||[]).filter(t=>t.type==='entry').reverse().slice(0,15);
  if(!entries.length){el.innerHTML='<div class="empty">No entries yet</div>';return;}
  el.innerHTML=entries.map(t=>{
    const evCol=(t.ev||0)>0?'#00ff41':'#ff2244';
    const time=(t.opened_at||'').substr(11,5)||'—';
    return`<div style="padding:7px 14px;border-bottom:1px solid #0a2a0a;font-size:9px;">
      <div style="color:#2a5a2a">${time} · ${t.location||''} · ${t.date||''}</div>
      <div style="color:#88ff88;margin-top:2px">Entry: $${(t.entry_price||0).toFixed(3)} · Our prob: ${((t.our_prob||0)*100).toFixed(0)}%</div>
      <div style="margin-top:2px">EV: <span style="color:${evCol}">${fmt2(t.ev||0)}</span> per $1 &nbsp;|&nbsp; Kelly: <span style="color:#ffcc00">${((t.kelly_pct||0)*100).toFixed(1)}%</span> &nbsp;|&nbsp; Size: <span style="color:#00ff41">$${(t.cost||0).toFixed(2)}</span></div>
    </div>`;
  }).join('');
}

async function loadData(){
  try {
    const r=await fetch('simulation.json?t='+Date.now());
    if(!r.ok)throw new Error('not found');

    const sim=await r.json();
    document.getElementById('no-server-msg').style.display='none';
    document.getElementById('status-dot').className='dot';
    document.getElementById('status-text').textContent='LIVE';

    const bal=sim.balance||1000;
    const start=sim.starting_balance||1000;
    const wins=sim.wins||0;
    const losses=sim.losses||0;
    const totalTrades=sim.total_trades||0;
    const positions=sim.positions||{};
    const trades=sim.trades||[];
    const peak=sim.peak_balance||bal;
    const openValue = Object.values(positions).reduce((s,p) => s + (p.cost||0) + (p.pnl||0), 0);
    const total = bal + openValue;
    const pnl = total - start;
    const pct=pnl/start*100;

    // Stats
    document.getElementById('ts').textContent='Updated: '+now();
    document.getElementById('s-bal').textContent='$'+total.toFixed(2);
    const pnlEl=document.getElementById('s-pnl');
    pnlEl.textContent=(pnl>=0?'+':'')+' $'+Math.abs(pnl).toFixed(2);
    pnlEl.className='stat-val'+(pnl<0?' red':'');
    document.getElementById('s-pct').textContent=(pct>=0?'+':'')+pct.toFixed(1)+'% return';
    document.getElementById('s-open').textContent=Object.keys(positions).length;
    const wr=wins+losses>0?(wins/(wins+losses)*100).toFixed(0)+'%':'—';
    document.getElementById('s-wr').textContent=wr;
    document.getElementById('s-wl').textContent=wins+'W / '+losses+'L';
    document.getElementById('s-total').textContent=totalTrades;
    document.getElementById('s-peak').textContent='$'+peak.toFixed(2);

    // Chart
    if(prevBal!==null&&Math.abs(bal-prevBal)>0.1)spawnDelta(bal-prevBal);
    prevBal=bal;
    balHistory.push(parseFloat(bal.toFixed(2)));
    timeLabels.push(now());
    if(balHistory.length>60){balHistory.shift();timeLabels.shift();}
    chart.data.labels=[...timeLabels];
    chart.data.datasets[0].data=[...balHistory];
    chart.update();

    renderPositions(positions);
    renderTrades(trades);
    renderEvLog(trades);

  } catch(e) {
    document.getElementById('status-dot').className='dot gray';
    document.getElementById('status-text').textContent='WAITING FOR BOT';
    document.getElementById('ts').textContent='No simulation.json found';
    // Show instructions if running from file://
    if(location.protocol==='file:'){
      document.getElementById('no-server-msg').style.display='block';
    }
  }
}

loadData();
setInterval(loadData, 10000);
</script>
</body>
</html>

```

---

### File: LICENSE
```
MIT License

Copyright (c) 2026 alteregoeth-ai

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

```
