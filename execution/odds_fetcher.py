#!/usr/bin/env python3
"""
NBA Odds Fetcher — Pull live betting lines from The Odds API.

Covers game lines (spreads, totals, moneylines) and player props
(points, rebounds, assists, threes) across DraftKings, FanDuel, BetMGM, Caesars.

Free tier: 500 requests/month. Each market × region = 1 request.

Usage:
    python execution/odds_fetcher.py games                     # Tonight's NBA games
    python execution/odds_fetcher.py lines                     # Spreads + totals for all games
    python execution/odds_fetcher.py props <event_id>          # Player props for a specific game
    python execution/odds_fetcher.py props <event_id> --player "Nikola Jokic"
    python execution/odds_fetcher.py full                      # Games + lines + props for all games
    python execution/odds_fetcher.py usage                     # Check remaining API requests
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone
import requests
from dotenv import load_dotenv

# Load .env from project root
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(ROOT, '.env'))

API_KEY = os.environ.get('ODDS_API_KEY')
BASE_URL = 'https://api.the-odds-api.com/v4'
SPORT = 'basketball_nba'
REGIONS = 'us'
ODDS_FORMAT = 'american'

PROP_MARKETS = ['player_points', 'player_rebounds', 'player_assists', 'player_threes']
GAME_MARKETS = ['h2h', 'spreads', 'totals']


def api_request(endpoint, params=None):
    """Make a request to The Odds API and return JSON + headers."""
    if not API_KEY:
        print("Error: ODDS_API_KEY not found in .env")
        sys.exit(1)

    if params is None:
        params = {}
    params['apiKey'] = API_KEY

    url = f"{BASE_URL}{endpoint}"
    resp = requests.get(url, params=params)
    if resp.status_code != 200:
        print(f"API Error {resp.status_code}: {resp.text}")
        sys.exit(1)

    remaining = resp.headers.get('x-requests-remaining', '?')
    used = resp.headers.get('x-requests-used', '?')
    return resp.json(), remaining, used


# ── Commands ──────────────────────────────────────────────────────

def cmd_games(args):
    """List tonight's NBA games with event IDs."""
    data, remaining, used = api_request(f'/sports/{SPORT}/events')

    now = datetime.now(timezone.utc)
    today_games = []
    for event in data:
        commence = datetime.fromisoformat(event['commence_time'].replace('Z', '+00:00'))
        # Show games within next 24 hours
        diff = (commence - now).total_seconds()
        if 0 <= diff <= 86400:
            today_games.append(event)

    if not today_games:
        # Show all upcoming if none today
        today_games = data[:10]
        print("No games in next 24 hours. Showing next upcoming:\n")

    print(f"{'─' * 80}")
    print(f"  NBA Games — {datetime.now().strftime('%B %d, %Y')}")
    print(f"{'─' * 80}")
    for g in today_games:
        commence = datetime.fromisoformat(g['commence_time'].replace('Z', '+00:00'))
        time_str = commence.strftime('%I:%M %p ET')
        print(f"  {g['away_team']:<28} @ {g['home_team']:<28} {time_str}")
        print(f"  Event ID: {g['id']}")
        print()
    print(f"{'─' * 80}")
    print(f"  API requests: {used} used / {remaining} remaining")
    print(f"{'─' * 80}")


def cmd_lines(args):
    """Get spreads, totals, and moneylines for all NBA games."""
    data, remaining, used = api_request(f'/sports/{SPORT}/odds', {
        'regions': REGIONS,
        'markets': ','.join(GAME_MARKETS),
        'oddsFormat': ODDS_FORMAT
    })

    now = datetime.now(timezone.utc)

    print(f"\n{'═' * 90}")
    print(f"  NBA Game Lines — {datetime.now().strftime('%B %d, %Y')}")
    print(f"{'═' * 90}")

    for game in data:
        commence = datetime.fromisoformat(game['commence_time'].replace('Z', '+00:00'))
        diff = (commence - now).total_seconds()
        if diff < -7200:  # Skip games started more than 2 hours ago
            continue

        time_str = commence.strftime('%I:%M %p ET')
        print(f"\n  {game['away_team']} @ {game['home_team']}  |  {time_str}")
        print(f"  Event ID: {game['id']}")
        print(f"  {'─' * 84}")

        # Collect best lines across books
        spreads = {}
        totals = {}
        moneylines = {}

        for book in game.get('bookmakers', []):
            book_name = book['title']
            for market in book.get('markets', []):
                if market['key'] == 'spreads':
                    for outcome in market['outcomes']:
                        key = outcome['name']
                        if key not in spreads or abs(outcome.get('point', 0)) < abs(spreads[key].get('point', 0)):
                            spreads[key] = {**outcome, 'book': book_name}
                elif market['key'] == 'totals':
                    for outcome in market['outcomes']:
                        key = outcome['name']
                        totals[key] = {**outcome, 'book': book_name}
                elif market['key'] == 'h2h':
                    for outcome in market['outcomes']:
                        key = outcome['name']
                        if key not in moneylines or outcome['price'] > moneylines[key]['price']:
                            moneylines[key] = {**outcome, 'book': book_name}

        # Print spread
        if spreads:
            print(f"  {'Spread:':<12}", end='')
            for team, info in spreads.items():
                point = info.get('point', 0)
                price = info.get('price', 0)
                sign = '+' if point > 0 else ''
                print(f"  {team[:20]:<20} {sign}{point} ({price:+d}) [{info['book']}]", end='')
            print()

        # Print total
        if totals:
            over = totals.get('Over', {})
            under = totals.get('Under', {})
            if over:
                print(f"  {'Total:':<12}  O/U {over.get('point', '?')}  |  Over {over.get('price', '?'):+d} [{over.get('book', '?')}]  |  Under {under.get('price', '?'):+d} [{under.get('book', '?')}]")

        # Print moneyline
        if moneylines:
            print(f"  {'Moneyline:':<12}", end='')
            for team, info in moneylines.items():
                print(f"  {team[:20]:<20} {info['price']:+d} [{info['book']}]", end='')
            print()

    print(f"\n{'═' * 90}")
    print(f"  API requests: {used} used / {remaining} remaining")
    print(f"{'═' * 90}\n")


def cmd_props(args):
    """Get player props for a specific game."""
    event_id = args.event_id
    player_filter = args.player.lower() if args.player else None

    all_props = {}

    # Fetch each prop market separately to stay organized
    for market in PROP_MARKETS:
        data, remaining, used = api_request(
            f'/sports/{SPORT}/events/{event_id}/odds',
            {
                'regions': REGIONS,
                'markets': market,
                'oddsFormat': ODDS_FORMAT
            }
        )

        if not data or 'bookmakers' not in data:
            continue

        game_title = f"{data.get('away_team', '?')} @ {data.get('home_team', '?')}"

        for book in data.get('bookmakers', []):
            book_name = book['title']
            for mkt in book.get('markets', []):
                for outcome in mkt.get('outcomes', []):
                    player = outcome.get('description', 'Unknown')
                    if player_filter and player_filter not in player.lower():
                        continue

                    direction = outcome.get('name', '')  # Over/Under
                    price = outcome.get('price', 0)
                    point = outcome.get('point', 0)
                    prop_type = market.replace('player_', '')

                    if player not in all_props:
                        all_props[player] = {}
                    if prop_type not in all_props[player]:
                        all_props[player][prop_type] = {}
                    if direction not in all_props[player][prop_type]:
                        all_props[player][prop_type][direction] = []

                    all_props[player][prop_type][direction].append({
                        'line': point,
                        'price': price,
                        'book': book_name
                    })

    # Print results
    print(f"\n{'═' * 90}")
    if 'game_title' in dir():
        pass
    print(f"  Player Props — Event: {event_id}")
    print(f"{'═' * 90}")

    if not all_props:
        print("  No player props available for this event.")
        print(f"{'═' * 90}\n")
        return

    for player in sorted(all_props.keys()):
        print(f"\n  {player}")
        print(f"  {'─' * 84}")
        for prop_type in sorted(all_props[player].keys()):
            directions = all_props[player][prop_type]
            over_opts = directions.get('Over', [])
            under_opts = directions.get('Under', [])

            # Find best over (highest price = best odds for bettor)
            best_over = max(over_opts, key=lambda x: x['price']) if over_opts else None
            best_under = max(under_opts, key=lambda x: x['price']) if under_opts else None

            line = best_over['line'] if best_over else (best_under['line'] if best_under else '?')

            over_str = f"O {best_over['price']:+d} [{best_over['book']}]" if best_over else "N/A"
            under_str = f"U {best_under['price']:+d} [{best_under['book']}]" if best_under else "N/A"

            # Show all books for comparison
            all_books_over = ', '.join(f"{o['price']:+d} [{o['book']}]" for o in sorted(over_opts, key=lambda x: -x['price'])) if over_opts else ''
            all_books_under = ', '.join(f"{u['price']:+d} [{u['book']}]" for u in sorted(under_opts, key=lambda x: -x['price'])) if under_opts else ''

            print(f"    {prop_type:<10}  Line: {line:<6}  Best Over: {over_str:<30}  Best Under: {under_str}")
            if len(over_opts) > 1:
                print(f"    {'':>10}  All books (Over):  {all_books_over}")
            if len(under_opts) > 1:
                print(f"    {'':>10}  All books (Under): {all_books_under}")

    print(f"\n{'═' * 90}")
    print(f"  API requests: {used} used / {remaining} remaining")
    print(f"{'═' * 90}\n")


def cmd_full(args):
    """Full slate: games + lines + props for each game."""
    # First get events
    events, remaining, used = api_request(f'/sports/{SPORT}/events')

    now = datetime.now(timezone.utc)
    today_games = []
    for event in events:
        commence = datetime.fromisoformat(event['commence_time'].replace('Z', '+00:00'))
        diff = (commence - now).total_seconds()
        if 0 <= diff <= 86400:
            today_games.append(event)

    if not today_games:
        print("No games in next 24 hours.")
        return

    # Get game lines
    print("\n" + "=" * 90)
    print("  FULL SLATE — GAME LINES")
    print("=" * 90)
    cmd_lines(args)

    # Get props for each game
    print("\n" + "=" * 90)
    print("  PLAYER PROPS BY GAME")
    print("=" * 90)

    for game in today_games:
        print(f"\n  >>> {game['away_team']} @ {game['home_team']}")
        args_copy = argparse.Namespace(event_id=game['id'], player=None)
        cmd_props(args_copy)


def cmd_usage(args):
    """Check API usage."""
    # Make a minimal request to check headers
    data, remaining, used = api_request(f'/sports/{SPORT}/events')
    print(f"\n{'═' * 44}")
    print(f"  The Odds API Usage")
    print(f"{'═' * 44}")
    print(f"  {'Requests Used:':<22} {used:>8}")
    print(f"  {'Requests Remaining:':<22} {remaining:>8}")
    print(f"  {'Monthly Limit:':<22} {'500':>8}")
    print(f"{'═' * 44}\n")


def main():
    parser = argparse.ArgumentParser(
        description='NBA Odds Fetcher — Pull live betting lines from The Odds API.'
    )
    subparsers = parser.add_subparsers(dest='command', help='Command to run')

    # games
    subparsers.add_parser('games', help="List tonight's NBA games with event IDs")

    # lines
    subparsers.add_parser('lines', help='Get spreads, totals, moneylines for all games')

    # props
    p_props = subparsers.add_parser('props', help='Get player props for a specific game')
    p_props.add_argument('event_id', help='Event ID (from games command)')
    p_props.add_argument('--player', type=str, default=None, help='Filter by player name')

    # full
    subparsers.add_parser('full', help='Full slate: games + lines + props for all games')

    # usage
    subparsers.add_parser('usage', help='Check remaining API requests')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        'games': cmd_games,
        'lines': cmd_lines,
        'props': cmd_props,
        'full': cmd_full,
        'usage': cmd_usage,
    }

    commands[args.command](args)


if __name__ == '__main__':
    main()
