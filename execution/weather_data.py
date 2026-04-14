#!/usr/bin/env python3
"""
Weather Data CLI — Fetch forecasts and scan weather markets.

Usage:
    python execution/weather_data.py forecast <city>              # Forecast for a city
    python execution/weather_data.py forecast <city> --date 2026-04-15
    python execution/weather_data.py scan                          # Scan all weather markets
    python execution/weather_data.py cities                        # List supported cities
    python execution/weather_data.py metar <ICAO>                  # METAR observation
"""

import argparse
import logging
import os
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from projects.prediction_market_arb.config import load_config
from projects.prediction_market_arb.state import StateManager
from projects.prediction_market_arb.polymarket_client import create_client
from projects.prediction_market_arb.weather_data import WeatherPipeline
from projects.prediction_market_arb.constants import ICAO_STATIONS


def main():
    parser = argparse.ArgumentParser(description="Weather Data CLI")
    parser.add_argument("command", choices=["forecast", "scan", "cities", "metar"])
    parser.add_argument("arg", nargs="?", default=None, help="City slug or ICAO code")
    parser.add_argument("--date", type=str, default=None,
                        help="Date (YYYY-MM-DD, default: today)")
    parser.add_argument("--config", type=str, default=None)
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.WARNING)
    config = load_config(args.config)
    state = StateManager(config.paper.data_dir)
    weather = WeatherPipeline(config, state)

    if args.command == "cities":
        print("\n  Supported Cities:")
        print(f"  {'Slug':<15s} {'ICAO':<6s} {'Name':<20s} {'Region':<8s} {'Unit'}")
        print(f"  {'-'*60}")
        for slug, (icao, lat, lon, name, region, unit) in sorted(ICAO_STATIONS.items()):
            print(f"  {slug:<15s} {icao:<6s} {name:<20s} {region:<8s} °{unit}")
        print(f"\n  Total: {len(ICAO_STATIONS)} cities")

    elif args.command == "forecast":
        if not args.arg:
            print("Usage: weather_data.py forecast <city>")
            print("  Run 'weather_data.py cities' to see available cities")
            return
        city = args.arg.lower()
        date = args.date or datetime.now(timezone.utc).strftime("%Y-%m-%d")
        snapshot = weather.fetch_forecast(city, date)
        if snapshot:
            print(f"\n  Forecast: {ICAO_STATIONS[city][3]} on {date}")
            print(f"  {'='*40}")
            print(f"  Best:   {snapshot.best_temp}°{snapshot.unit} ({snapshot.best_source})")
            if snapshot.ecmwf_temp is not None:
                print(f"  ECMWF:  {snapshot.ecmwf_temp}°{snapshot.unit}")
            if snapshot.hrrr_temp is not None:
                print(f"  HRRR:   {snapshot.hrrr_temp}°{snapshot.unit}")
            if snapshot.metar_temp is not None:
                print(f"  METAR:  {snapshot.metar_temp}°{snapshot.unit}")
            print(f"  Sigma:  {snapshot.sigma}°{snapshot.unit}")
        else:
            print(f"No forecast available for {args.arg}")

    elif args.command == "metar":
        if not args.arg:
            print("Usage: weather_data.py metar <ICAO>")
            return
        temp = weather.fetch_metar(args.arg.upper())
        if temp is not None:
            print(f"  {args.arg.upper()}: {temp}°F")
        else:
            print(f"  No METAR data for {args.arg.upper()}")

    elif args.command == "scan":
        client = create_client(config, state)
        opportunities = weather.scan_weather_markets(client)
        if opportunities:
            print(f"\n  Weather Market Opportunities ({len(opportunities)}):")
            print(f"  {'City':<12s} {'Date':<12s} {'Forecast':<10s} {'Prob':<8s} "
                  f"{'Price':<8s} {'Edge':<8s} {'Vol':<10s}")
            print(f"  {'-'*70}")
            for opp in opportunities[:20]:
                print(f"  {opp['city']:<12s} {opp['date']:<12s} "
                      f"{opp['forecast_temp']:>6.1f}°{opp['unit']:<2s} "
                      f"{opp['probability']:>6.1%} "
                      f"${opp['market_price']:<6.3f} "
                      f"{opp['edge']:>6.1%} "
                      f"${opp['volume']:>8,.0f}")
        else:
            print("  No weather market opportunities found")


if __name__ == "__main__":
    main()
