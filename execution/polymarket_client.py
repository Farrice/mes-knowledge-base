#!/usr/bin/env python3
"""
Polymarket Client CLI — Query markets, orderbooks, and prices.

Usage:
    python execution/polymarket_client.py markets                    # List active markets
    python execution/polymarket_client.py markets --category weather # Filter by category
    python execution/polymarket_client.py market <condition_id>      # Single market details
    python execution/polymarket_client.py price <market_id>          # Current prices
    python execution/polymarket_client.py book <token_id>            # Orderbook
    python execution/polymarket_client.py event <slug>               # Event by slug
    python execution/polymarket_client.py balance                    # Paper balance
"""

import argparse
import json
import logging
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from projects.prediction_market_arb.config import load_config
from projects.prediction_market_arb.state import StateManager
from projects.prediction_market_arb.polymarket_client import create_client


def main():
    parser = argparse.ArgumentParser(description="Polymarket Client CLI")
    parser.add_argument("command", choices=["markets", "market", "price", "book",
                                            "event", "balance", "search"])
    parser.add_argument("arg", nargs="?", default=None, help="Market/token/slug ID")
    parser.add_argument("--category", type=str, default=None)
    parser.add_argument("--limit", type=int, default=20)
    parser.add_argument("--config", type=str, default=None)
    args = parser.parse_args()

    logging.basicConfig(level=logging.WARNING)
    config = load_config(args.config)
    state = StateManager(config.paper.data_dir)
    client = create_client(config, state)

    if args.command == "markets":
        markets = client.get_markets(limit=args.limit, category=args.category)
        for m in markets:
            vol = f"${m.volume:,.0f}" if m.volume else "$0"
            print(f"  {m.id[:12]}... | {vol:>10s} | {m.question[:60]}")
        print(f"\n  Total: {len(markets)} markets")

    elif args.command == "market":
        if not args.arg:
            print("Usage: polymarket_client.py market <condition_id>")
            return
        m = client.get_market(args.arg)
        if m:
            print(json.dumps(m.to_dict(), indent=2))
        else:
            print(f"Market not found: {args.arg}")

    elif args.command == "price":
        if not args.arg:
            print("Usage: polymarket_client.py price <market_id>")
            return
        prices = client.get_market_price(args.arg)
        if prices:
            print(f"  Yes: ${prices['yes']:.3f}")
            print(f"  No:  ${prices['no']:.3f}")
        else:
            print(f"Could not fetch prices for {args.arg}")

    elif args.command == "book":
        if not args.arg:
            print("Usage: polymarket_client.py book <token_id>")
            return
        book = client.get_orderbook(args.arg)
        print("  BIDS:")
        for price, size in sorted(book["bids"], reverse=True)[:10]:
            print(f"    ${price:.3f} x {size:.1f}")
        print("  ASKS:")
        for price, size in sorted(book["asks"])[:10]:
            print(f"    ${price:.3f} x {size:.1f}")

    elif args.command == "event":
        if not args.arg:
            print("Usage: polymarket_client.py event <slug>")
            return
        event = client.get_event(args.arg)
        if event:
            print(json.dumps(event, indent=2, default=str))
        else:
            print(f"Event not found: {args.arg}")

    elif args.command == "search":
        if not args.arg:
            print("Usage: polymarket_client.py search <query>")
            return
        events = client.search_events(args.arg)
        for e in events[:20]:
            print(f"  {e.get('slug', '')[:40]:40s} | {e.get('title', '')[:50]}")

    elif args.command == "balance":
        balance = client.get_balance()
        print(f"  Balance: ${balance:.2f}")


if __name__ == "__main__":
    main()
