#!/usr/bin/env python3
"""
Polymarket WebSocket CLI — Connect to market and user data streams.

Usage:
    python execution/polymarket_ws.py connect <token_id1> [token_id2 ...]
    python execution/polymarket_ws.py status

Note: WebSocket connections are typically managed by the paper trader's
continuous mode. This CLI is for testing and debugging.
"""

import argparse
import asyncio
import json
import logging
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from projects.prediction_market_arb.config import load_config
from projects.prediction_market_arb.state import StateManager
from projects.prediction_market_arb.polymarket_client import create_client
from projects.prediction_market_arb.polymarket_ws import PolymarketWebSocket


def on_book_update(data):
    market = data.get("market", "")[:12]
    bids = len(data.get("bids", []))
    asks = len(data.get("asks", []))
    print(f"  [BOOK] {market}... | {bids} bids, {asks} asks")


def on_price_change(data):
    print(f"  [PRICE] {data['market'][:12]}... | "
          f"{data['side']} ${data['price']:.3f} x {data['size']:.1f}")


def main():
    parser = argparse.ArgumentParser(description="Polymarket WebSocket CLI")
    parser.add_argument("command", choices=["connect", "status"])
    parser.add_argument("tokens", nargs="*", default=[],
                        help="Token IDs to subscribe to")
    parser.add_argument("--config", type=str, default=None)
    parser.add_argument("-v", "--verbose", action="store_true")
    args = parser.parse_args()

    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO)

    if args.command == "status":
        config = load_config(args.config)
        state = StateManager(config.paper.data_dir)
        client = create_client(config, state)
        ws = PolymarketWebSocket(config, client)
        status = ws.is_connected
        print(f"\n  Market channel: {'Connected' if status['market'] else 'Disconnected'}")
        print(f"  User channel:   {'Connected' if status['user'] else 'Disconnected'}")
        return

    if args.command == "connect":
        if not args.tokens:
            print("Usage: polymarket_ws.py connect <token_id1> [token_id2 ...]")
            return

        config = load_config(args.config)
        state = StateManager(config.paper.data_dir)
        client = create_client(config, state)

        ws = PolymarketWebSocket(config, client)
        ws.on_book_update = on_book_update
        ws.on_price_change = on_price_change

        print(f"  Connecting to {len(args.tokens)} tokens... (Ctrl+C to stop)")
        try:
            asyncio.run(ws.start(token_ids=args.tokens))
        except KeyboardInterrupt:
            print("\n  Disconnected")


if __name__ == "__main__":
    main()
