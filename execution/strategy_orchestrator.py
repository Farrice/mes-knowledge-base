#!/usr/bin/env python3
"""
CLI wrapper for the Strategy Orchestrator.

Usage:
  python execution/strategy_orchestrator.py scan         # Run multi-strategy scan
  python execution/strategy_orchestrator.py scan-weather  # Weather only (Phase 1)
  python execution/strategy_orchestrator.py scan-sports   # Sports arb only
  python execution/strategy_orchestrator.py status        # Show orchestrator status
  python execution/strategy_orchestrator.py run           # Continuous multi-strategy mode
  python execution/strategy_orchestrator.py run-weather   # Continuous weather-only mode
"""

import sys
import os
import logging

# Add project root to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from projects.prediction_market_arb.paper_trader import PaperTrader
from projects.prediction_market_arb.strategy_orchestrator import StrategyOrchestrator

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(name)s] %(levelname)s: %(message)s",
    datefmt="%H:%M:%S",
)
# Quiet down noisy loggers
logging.getLogger("urllib3").setLevel(logging.WARNING)
logging.getLogger("requests").setLevel(logging.WARNING)


def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    command = sys.argv[1]

    if command == "scan":
        # Full multi-strategy scan
        trader = PaperTrader()
        trader.scan_and_trade_multi()

    elif command == "scan-weather":
        # Weather-only scan (Phase 1 behavior)
        trader = PaperTrader()
        trader.scan_and_trade()

    elif command == "scan-sports":
        # Sports-only scan
        orch = StrategyOrchestrator()
        opps = orch._scan_sports()
        if opps:
            print(f"\nFound {len(opps)} sports arbitrage opportunities:")
            for i, opp in enumerate(opps[:10]):
                print(f"  {i+1}. {opp.question[:60]}...")
                print(f"     Edge: {opp.edge_after_fees:+.1%} | "
                      f"Ref: {opp.reference_source}")
        else:
            print("No sports arbitrage opportunities found.")
            print("Check: ODDSPAPI_KEY environment variable set?")

    elif command == "status":
        orch = StrategyOrchestrator()
        orch.status()

    elif command == "run":
        # Continuous multi-strategy mode
        trader = PaperTrader()
        trader.run(multi_strategy=True)

    elif command == "run-weather":
        # Continuous weather-only mode (Phase 1)
        trader = PaperTrader()
        trader.run(multi_strategy=False)

    else:
        print(f"Unknown command: {command}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
