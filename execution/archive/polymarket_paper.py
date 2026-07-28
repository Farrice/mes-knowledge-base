#!/usr/bin/env python3
"""
Polymarket Paper Trader — Paper trading against real Polymarket weather markets.

Scans weather markets, fetches multi-source forecasts, calculates edge via
Gaussian bucket probability, validates through 8-check risk manager, and
executes paper trades with fractional Kelly sizing.

Usage:
    python execution/polymarket_paper.py scan         # One-shot scan and trade
    python execution/polymarket_paper.py monitor      # Check exits on open positions
    python execution/polymarket_paper.py run           # Continuous loop (Ctrl+C to stop)
    python execution/polymarket_paper.py status        # Current positions, balance, P&L
    python execution/polymarket_paper.py report        # Full performance report
"""

import argparse
import logging
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from projects.prediction_market_arb.paper_trader import PaperTrader


def setup_logging(verbose: bool = False):
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
        datefmt="%H:%M:%S",
    )


def main():
    parser = argparse.ArgumentParser(
        description="Polymarket Paper Trader — weather market trading simulation"
    )
    parser.add_argument("command", choices=["scan", "monitor", "run", "status", "report"],
                        help="Command to execute")
    parser.add_argument("--config", type=str, default=None,
                        help="Path to config.json (default: package default)")
    parser.add_argument("-v", "--verbose", action="store_true",
                        help="Verbose logging")
    args = parser.parse_args()

    setup_logging(args.verbose)
    trader = PaperTrader(config_path=args.config)

    if args.command == "scan":
        trader.scan_and_trade()
    elif args.command == "monitor":
        trader.monitor_positions()
    elif args.command == "run":
        trader.run()
    elif args.command == "status":
        trader.status()
    elif args.command == "report":
        trader.report()


if __name__ == "__main__":
    main()
