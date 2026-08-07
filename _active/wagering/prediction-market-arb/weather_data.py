"""
Weather Data Pipeline — Multi-source forecast engine for Polymarket weather markets.

Sources (all free, no API key except Visual Crossing):
  1. Open-Meteo ECMWF — global coverage, reliable for D+1 to D+5
  2. Open-Meteo HRRR — US only (CONUS), best for D+0 and D+1
  3. METAR — real-time airport station observations, same-day ground truth
  4. Visual Crossing — historical actuals, used for resolution verification only

Tiered source selection:
  - US cities D+0/D+1: HRRR (highest resolution)
  - Everything else: ECMWF
  - Same-day: METAR overrides both (it's actual observations, not forecasts)

Edge calculation:
  - Gaussian bucket probability using calibrated sigma per (city, source) pair
  - Expected value = probability × (1/price - 1) - (1 - probability)
  - Edge = EV as fraction of price (must exceed min_ev to trade)

Self-calibration:
  - Track forecast error (MAE) per city × source after each resolved market
  - After calibration_min (default 30) markets, calibrated sigma replaces default
  - Sigma ≈ MAE × sqrt(π/2) for Gaussian-distributed errors
"""

import logging
import math
import re
from datetime import datetime, timezone, timedelta
from typing import Optional

import requests

from projects.prediction_market_arb.constants import (
    ICAO_STATIONS, US_HRRR_CITIES, MONTHS,
    OPEN_METEO_ECMWF_URL, OPEN_METEO_HRRR_URL, METAR_URL, VISUAL_CROSSING_URL,
)
from projects.prediction_market_arb.models import ForecastSnapshot
from projects.prediction_market_arb.resilience import retry_transient
from projects.prediction_market_arb.state import StateManager

logger = logging.getLogger("polymarket.weather")


# =============================================================================
# GAUSSIAN PROBABILITY (no scipy dependency — we implement norm_cdf directly)
# =============================================================================

def _norm_cdf(x: float) -> float:
    """Standard normal CDF approximation (Abramowitz & Stegun, max error 1.5e-7)."""
    if x < -8.0:
        return 0.0
    if x > 8.0:
        return 1.0
    return 0.5 * (1.0 + math.erf(x / math.sqrt(2.0)))


def bucket_probability(forecast: float, bucket_low: float, bucket_high: float,
                       sigma: float) -> float:
    """
    Calculate probability of actual temperature falling in [bucket_low, bucket_high].

    Uses Gaussian distribution centered on forecast with standard deviation sigma.
    For edge buckets ("X or below" / "X or higher"), one side extends to ±infinity.
    """
    if sigma <= 0:
        sigma = 0.01  # Prevent division by zero

    # Edge bucket: "X or below"
    if bucket_low <= -900:
        return _norm_cdf((bucket_high - forecast) / sigma)

    # Edge bucket: "X or higher"
    if bucket_high >= 900:
        return 1.0 - _norm_cdf((bucket_low - forecast) / sigma)

    # Normal bucket: between low and high
    p_high = _norm_cdf((bucket_high - forecast) / sigma)
    p_low = _norm_cdf((bucket_low - forecast) / sigma)
    return max(0.0, p_high - p_low)


def calc_edge(probability: float, market_price: float) -> dict:
    """
    Calculate expected value and edge for a trade.

    EV = prob × payout - (1 - prob) × cost
    For binary markets: payout = 1/price - 1, cost = 1
    Simplified: EV = prob / price - 1

    Returns dict with ev, edge, and kelly_f (raw, before fraction adjustment).
    """
    if market_price <= 0 or market_price >= 1.0:
        return {"ev": 0.0, "edge": 0.0, "kelly_f": 0.0}

    # Expected value per dollar
    ev = probability / market_price - 1.0

    # Edge as fraction of price (for comparison with min_ev threshold)
    edge = ev * market_price

    # Raw Kelly fraction: f* = (p * b - (1-p)) / b where b = 1/price - 1
    b = (1.0 / market_price) - 1.0
    if b > 0:
        kelly_f = (probability * b - (1.0 - probability)) / b
    else:
        kelly_f = 0.0

    return {"ev": ev, "edge": edge, "kelly_f": max(0.0, kelly_f)}


# =============================================================================
# WEATHER PIPELINE
# =============================================================================

class WeatherPipeline:
    """Multi-source weather forecast engine with self-calibration."""

    def __init__(self, config, state_manager: StateManager):
        self.config = config
        self.state = state_manager
        self._session = requests.Session()
        self._session.headers.update({"User-Agent": "polymarket-weather/0.1.0"})

    # -------------------------------------------------------------------------
    # Forecast Sources
    # -------------------------------------------------------------------------

    @retry_transient()
    def fetch_ecmwf(self, lat: float, lon: float, date: str,
                    unit: str = "F") -> Optional[float]:
        """Fetch max temperature from Open-Meteo ECMWF model."""
        try:
            temp_var = "temperature_2m_max"
            params = {
                "latitude": lat,
                "longitude": lon,
                "daily": temp_var,
                "start_date": date,
                "end_date": date,
                "temperature_unit": "fahrenheit" if unit == "F" else "celsius",
            }
            resp = self._session.get(OPEN_METEO_ECMWF_URL, params=params, timeout=15)
            resp.raise_for_status()
            data = resp.json()
            daily = data.get("daily", {})
            temps = daily.get(temp_var, [])
            if temps and temps[0] is not None:
                return round(float(temps[0]), 1)
        except Exception as e:
            logger.warning(f"ECMWF fetch failed ({lat}, {lon}): {e}")
        return None

    @retry_transient()
    def fetch_hrrr(self, lat: float, lon: float, date: str,
                   unit: str = "F") -> Optional[float]:
        """
        Fetch max temperature from Open-Meteo HRRR model (via forecast API).
        US cities only (CONUS coverage). Best for D+0 and D+1.
        """
        try:
            params = {
                "latitude": lat,
                "longitude": lon,
                "hourly": "temperature_2m",
                "models": "gfs_hrrr",
                "start_date": date,
                "end_date": date,
                "temperature_unit": "fahrenheit" if unit == "F" else "celsius",
            }
            resp = self._session.get("https://api.open-meteo.com/v1/forecast", params=params, timeout=15)
            resp.raise_for_status()
            data = resp.json()
            hourly = data.get("hourly", {})
            temps = hourly.get("temperature_2m", [])
            valid_temps = [t for t in temps if t is not None]
            if valid_temps:
                return round(max(valid_temps), 1)
        except Exception as e:
            logger.warning(f"HRRR fetch failed ({lat}, {lon}): {e}")
        return None

    @retry_transient()
    def fetch_metar(self, icao_code: str, unit: str = "F") -> Optional[float]:
        """
        Fetch latest temperature from METAR aviation weather observations.
        This is ground truth — actual measured temperature at the airport station.
        """
        try:
            params = {"ids": icao_code, "format": "json", "hours": 2}
            resp = self._session.get(METAR_URL, params=params, timeout=15)
            resp.raise_for_status()
            observations = resp.json()
            if not observations:
                return None

            # Get the most recent observation with a temperature
            for obs in observations:
                temp_c = obs.get("temp")
                if temp_c is not None:
                    temp_c = float(temp_c)
                    if unit == "F":
                        return round(temp_c * 9 / 5 + 32, 1)
                    return round(temp_c, 1)
        except Exception as e:
            logger.warning(f"METAR fetch failed ({icao_code}): {e}")
        return None

    @retry_transient()
    def fetch_visual_crossing(self, city_name: str, date: str,
                              unit: str = "F") -> Optional[float]:
        """
        Fetch historical actual temperature from Visual Crossing.
        Used for resolution verification ONLY (not for forecasting).
        Requires VISUAL_CROSSING_KEY environment variable.
        """
        api_key = self.config.visual_crossing_key if hasattr(self.config, 'visual_crossing_key') else ""
        if not api_key:
            return None
        try:
            url = f"{VISUAL_CROSSING_URL}/{city_name}/{date}"
            params = {
                "key": api_key,
                "unitGroup": "us" if unit == "F" else "metric",
                "include": "days",
                "elements": "tempmax",
            }
            resp = self._session.get(url, params=params, timeout=15)
            resp.raise_for_status()
            data = resp.json()
            days = data.get("days", [])
            if days:
                return round(float(days[0].get("tempmax", 0)), 1)
        except Exception as e:
            logger.warning(f"Visual Crossing fetch failed ({city_name}, {date}): {e}")
        return None

    # -------------------------------------------------------------------------
    # Source Selection (tiered — from weatherbot extraction)
    # -------------------------------------------------------------------------

    def fetch_forecast(self, city: str, date: str) -> Optional[ForecastSnapshot]:
        """
        Fetch forecast from all available sources and select the best one.

        Tiered selection:
          - US cities D+0/D+1: HRRR preferred (highest temporal resolution)
          - All other cases: ECMWF
          - Same-day: METAR overrides if available (ground truth)
        """
        if city not in ICAO_STATIONS:
            logger.error(f"Unknown city: {city}")
            return None

        icao, lat, lon, name, region, unit = ICAO_STATIONS[city]
        now = datetime.now(timezone.utc)
        target_date = datetime.strptime(date, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        days_ahead = (target_date.date() - now.date()).days

        # Fetch from all available sources
        ecmwf_temp = self.fetch_ecmwf(lat, lon, date, unit)
        hrrr_temp = None
        metar_temp = None

        if city in US_HRRR_CITIES:
            hrrr_temp = self.fetch_hrrr(lat, lon, date, unit)

        if days_ahead <= 0:  # Same day — METAR available
            metar_temp = self.fetch_metar(icao, unit)

        # Tiered source selection
        best_temp = None
        best_source = ""

        if metar_temp is not None and days_ahead <= 0:
            # Same-day: METAR is ground truth
            best_temp = metar_temp
            best_source = "metar"
        elif hrrr_temp is not None and city in US_HRRR_CITIES and days_ahead <= 1:
            # US D+0/D+1: HRRR preferred
            best_temp = hrrr_temp
            best_source = "hrrr"
        elif ecmwf_temp is not None:
            # Default: ECMWF
            best_temp = ecmwf_temp
            best_source = "ecmwf"
        else:
            logger.warning(f"No forecast available for {name} on {date}")
            return None

        # Get calibrated sigma
        sigma = self._get_sigma(city, best_source, unit)

        snapshot = ForecastSnapshot(
            city=city,
            timestamp=now.isoformat(),
            date=date,
            ecmwf_temp=ecmwf_temp,
            hrrr_temp=hrrr_temp,
            metar_temp=metar_temp,
            best_temp=best_temp,
            best_source=best_source,
            sigma=sigma,
            unit=unit,
        )

        # Persist snapshot for calibration data collection
        self.state.save_forecast_snapshot(snapshot)

        logger.info(f"Forecast: {name} {date} — {best_temp}°{unit} "
                    f"(source={best_source}, σ={sigma})")
        return snapshot

    def _get_sigma(self, city: str, source: str, unit: str) -> float:
        """Get calibrated sigma for a city/source pair, or return default."""
        cal = self.state.load_calibration()
        city_cal = cal.get(city, {})
        source_cal = city_cal.get(source, {})

        calibration_min = self.config.weather.calibration_min
        if source_cal.get("count", 0) >= calibration_min and source_cal.get("sigma"):
            return source_cal["sigma"]

        # Return default sigma
        if unit == "F":
            return self.config.weather.sigma_f
        return self.config.weather.sigma_c

    # -------------------------------------------------------------------------
    # Weather Market Discovery
    # -------------------------------------------------------------------------

    def scan_weather_markets(self, client) -> list:
        """
        Discover active weather markets on Polymarket and calculate edges.

        Weather markets follow the slug pattern:
          highest-temperature-in-{city}-on-{month}-{day}-{year}

        Returns list of dicts with market info, forecast, edge calculation.
        """
        results = []
        now = datetime.now(timezone.utc)

        for city, (icao, lat, lon, name, region, unit) in ICAO_STATIONS.items():
            for day_offset in range(0, 4):  # Today through D+3
                target = now + timedelta(days=day_offset)
                date_str = target.strftime("%Y-%m-%d")
                month = MONTHS[target.month - 1]
                day = target.day
                year = target.year

                slug = f"highest-temperature-in-{city}-on-{month}-{day}-{year}"
                event = client.get_event(slug)
                if not event:
                    continue

                # Check hours to resolution
                end_date = event.get("endDate") or event.get("end_date_iso", "")
                hours_left = self._hours_until(end_date)
                if hours_left < self.config.trading.min_hours_to_resolution:
                    continue
                if hours_left > self.config.trading.max_hours_to_resolution:
                    continue

                # Fetch forecast
                forecast = self.fetch_forecast(city, date_str)
                if not forecast or forecast.best_temp is None:
                    continue

                # Find matching bucket and calculate edge
                for market in event.get("markets", []):
                    question = market.get("question", "")
                    rng = parse_temp_range(question)
                    if not rng:
                        continue

                    # Calculate bucket probability
                    prob = bucket_probability(
                        forecast.best_temp, rng[0], rng[1], forecast.sigma
                    )

                    # Get market price
                    try:
                        prices = market.get("outcomePrices", "[0.5,0.5]")
                        if isinstance(prices, str):
                            prices = __import__("json").loads(prices)
                        yes_price = float(prices[0])
                    except (ValueError, IndexError):
                        continue

                    if yes_price <= 0 or yes_price >= 1.0:
                        continue

                    # Check volume
                    volume = float(market.get("volume", 0) or 0)

                    # Calculate edge
                    edge_calc = calc_edge(prob, yes_price)

                    # Check filters
                    if edge_calc["edge"] < self.config.trading.min_ev:
                        continue
                    if yes_price > self.config.trading.max_price:
                        continue

                    results.append({
                        "city": city,
                        "city_name": name,
                        "date": date_str,
                        "question": question,
                        "market_id": market.get("id", ""),
                        "condition_id": market.get("conditionId", ""),
                        "token_id": self._extract_token_id(market),
                        "bucket": rng,
                        "forecast_temp": forecast.best_temp,
                        "forecast_source": forecast.best_source,
                        "sigma": forecast.sigma,
                        "probability": round(prob, 4),
                        "market_price": yes_price,
                        "ev": round(edge_calc["ev"], 4),
                        "edge": round(edge_calc["edge"], 4),
                        "kelly_f": round(edge_calc["kelly_f"], 4),
                        "volume": volume,
                        "hours_left": round(hours_left, 1),
                        "neg_risk": market.get("neg_risk", False),
                        "unit": unit,
                    })

        # Sort by edge (highest first)
        results.sort(key=lambda x: x["edge"], reverse=True)
        logger.info(f"Weather scan complete: {len(results)} opportunities found")
        return results

    def _extract_token_id(self, market: dict) -> str:
        """Extract the YES token ID from a market's clobTokenIds field.

        clobTokenIds can be a JSON string or a Python list.
        The first element is always the YES token.
        """
        raw = market.get("clobTokenIds", "")
        if isinstance(raw, str):
            try:
                parsed = __import__("json").loads(raw)
                if parsed and isinstance(parsed, list):
                    return str(parsed[0])
            except (ValueError, TypeError):
                pass
        elif isinstance(raw, list) and raw:
            return str(raw[0])
        return ""

    def _hours_until(self, end_date_str: str) -> float:
        """Calculate hours until a market resolves."""
        if not end_date_str:
            return 999
        try:
            end = datetime.fromisoformat(end_date_str.replace("Z", "+00:00"))
            delta = (end - datetime.now(timezone.utc)).total_seconds() / 3600
            return max(0, delta)
        except (ValueError, TypeError):
            return 999


# =============================================================================
# TEMPERATURE PARSING (from weatherbot source)
# =============================================================================

def parse_temp_range(question: str) -> Optional[tuple]:
    """
    Extract temperature range from a Polymarket weather market question.

    Returns (low, high) tuple. Edge buckets use sentinel values:
      (-999, X) for "X or below"
      (X, 999)  for "X or higher"
    """
    if not question:
        return None

    q = question.lower()

    # "X°F or below" / "X°C or below"
    if "or below" in q:
        m = re.search(r'(\d+)°[FC]\s+or\s+below', question, re.IGNORECASE)
        if m:
            return (-999, int(m.group(1)))

    # "X°F or higher" / "X°C or higher"
    if "or higher" in q:
        m = re.search(r'(\d+)°[FC]\s+or\s+higher', question, re.IGNORECASE)
        if m:
            return (int(m.group(1)), 999)

    # "between X-Y°F" / "between X-Y°C"
    m = re.search(r'between\s+(\d+)\s*[-–]\s*(\d+)°[FC]', question, re.IGNORECASE)
    if m:
        return (int(m.group(1)), int(m.group(2)))

    return None
