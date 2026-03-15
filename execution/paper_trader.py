#!/usr/bin/env python3
"""
NBA Paper Trader — Automated pipeline for paper trading against real lines.

Pulls tonight's games and player props from The Odds API, runs each prop
through the projection engine, and generates a pick slate. Logs all picks
as paper bets for tracking. Run this daily for 30+ days to accumulate
200+ paper bets before risking real money.

Usage:
    python execution/paper_trader.py slate                    # Generate tonight's paper picks
    python execution/paper_trader.py slate --bankroll 500     # With custom bankroll
    python execution/paper_trader.py slate --game <event_id>  # Specific game only
    python execution/paper_trader.py results                  # Enter results for pending paper bets
    python execution/paper_trader.py status                   # Paper trading progress dashboard
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from execution.odds_fetcher import api_request, SPORT, PROP_MARKETS, REGIONS, ODDS_FORMAT
from execution.nba_stats import find_player
from execution.projection_engine import analyze_prop

DATA_FILE = os.path.join(ROOT, '.agent', 'bet-tracking.json')
PAPER_LOG = os.path.join(ROOT, '.agent', 'paper-trading.json')

# Map Odds API prop market names to our prop types
MARKET_TO_PROP = {
    'player_points': 'points',
    'player_rebounds': 'rebounds',
    'player_assists': 'assists',
    'player_threes': 'threes',
}


def load_paper_data():
    """Load or initialize paper trading data."""
    if os.path.exists(PAPER_LOG):
        with open(PAPER_LOG, 'r') as f:
            return json.load(f)
    return {
        'started': datetime.now().strftime('%Y-%m-%d'),
        'bankroll': {'initial': 1000, 'current': 1000},
        'bets': [],
        'daily_slates': [],
    }


def save_paper_data(data):
    """Save paper trading data."""
    os.makedirs(os.path.dirname(PAPER_LOG), exist_ok=True)
    with open(PAPER_LOG, 'w') as f:
        json.dump(data, f, indent=2)


def fetch_todays_games():
    """Get tonight's games from The Odds API."""
    events, remaining, used = api_request(f'/sports/{SPORT}/events')
    now = datetime.now(timezone.utc)
    today = []
    for event in events:
        commence = datetime.fromisoformat(event['commence_time'].replace('Z', '+00:00'))
        diff = (commence - now).total_seconds()
        if -3600 <= diff <= 86400:  # Within last hour to next 24 hours
            today.append(event)
    return today, remaining, used


def fetch_props_for_game(event_id):
    """Fetch player props for a game. Returns dict of player → prop → line."""
    props = {}

    for market in PROP_MARKETS:
        data, remaining, used = api_request(
            f'/sports/{SPORT}/events/{event_id}/odds',
            {'regions': REGIONS, 'markets': market, 'oddsFormat': ODDS_FORMAT}
        )

        if not data or 'bookmakers' not in data:
            continue

        game_info = {
            'home_team': data.get('home_team', ''),
            'away_team': data.get('away_team', ''),
        }

        for book in data.get('bookmakers', []):
            for mkt in book.get('markets', []):
                for outcome in mkt.get('outcomes', []):
                    player_name = outcome.get('description', '')
                    direction = outcome.get('name', '')  # Over/Under
                    line = outcome.get('point', 0)
                    price = outcome.get('price', 0)
                    prop_type = MARKET_TO_PROP.get(market, market)

                    if player_name not in props:
                        props[player_name] = {'game_info': game_info}
                    if prop_type not in props[player_name]:
                        props[player_name][prop_type] = {
                            'line': line,
                            'best_over_odds': -110,
                            'best_under_odds': -110,
                            'books': [],
                        }

                    # Track best odds
                    if direction == 'Over' and price > props[player_name][prop_type]['best_over_odds']:
                        props[player_name][prop_type]['best_over_odds'] = price
                    if direction == 'Under' and price > props[player_name][prop_type]['best_under_odds']:
                        props[player_name][prop_type]['best_under_odds'] = price

                    props[player_name][prop_type]['line'] = line
                    if book['title'] not in props[player_name][prop_type]['books']:
                        props[player_name][prop_type]['books'].append(book['title'])

    return props


def run_analysis(player_name, prop_type, opponent, line, bankroll):
    """Run projection engine analysis. Returns result or None on error."""
    try:
        result = analyze_prop(player_name, prop_type, opponent, line, bankroll)
        if 'error' in result:
            return None
        return result
    except Exception:
        return None


def cmd_slate(args):
    """Generate tonight's paper trading slate."""
    bankroll = args.bankroll

    print(f"\n{'='*80}")
    print(f"  PAPER TRADING SLATE — {datetime.now().strftime('%B %d, %Y')}")
    print(f"  Bankroll: ${bankroll:.2f}")
    print(f"{'='*80}")

    # Step 1: Get tonight's games
    print(f"\n  Fetching tonight's games...")
    games, remaining, used = fetch_todays_games()

    if not games:
        print("  No games found in the next 24 hours.")
        return

    if args.game:
        games = [g for g in games if g['id'] == args.game]
        if not games:
            print(f"  Game {args.game} not found.")
            return

    print(f"  Found {len(games)} games  |  API: {used} used / {remaining} remaining")

    for g in games:
        commence = datetime.fromisoformat(g['commence_time'].replace('Z', '+00:00'))
        print(f"    {g['away_team']} @ {g['home_team']}  |  {commence.strftime('%I:%M %p')}  |  {g['id']}")

    # Step 2: Fetch props for each game
    all_picks = []
    games_analyzed = 0

    for game in games:
        away = game['away_team']
        home = game['home_team']
        event_id = game['id']

        print(f"\n  {'─'*70}")
        print(f"  Analyzing: {away} @ {home}")
        print(f"  {'─'*70}")

        props = fetch_props_for_game(event_id)
        if not props:
            print(f"    No props available yet for this game.")
            continue

        games_analyzed += 1
        game_picks = []

        for player_name, player_props in props.items():
            game_info = player_props.get('game_info', {})

            # Determine opponent for this player
            # Check if player is on home or away team
            # We'll try both and see which one the projection engine can resolve
            opponent = away if find_player(player_name) else home

            for prop_type, prop_data in player_props.items():
                if prop_type == 'game_info':
                    continue

                line = prop_data['line']

                # Try to determine opponent more accurately
                # The player could be on either team
                result = run_analysis(player_name, prop_type, away, line, bankroll)
                if result is None:
                    result = run_analysis(player_name, prop_type, home, line, bankroll)
                if result is None:
                    continue

                # Only include picks with confidence >= 2
                if result['confidence']['score'] >= 2:
                    pick = {
                        'player': result['player'],
                        'prop': prop_type,
                        'line': line,
                        'projection': result['projection']['matchup_adjusted'],
                        'edge': result['edge'],
                        'confidence': result['confidence'],
                        'sizing': result['sizing'],
                        'best_odds': (prop_data['best_over_odds']
                                      if result['edge']['direction'] == 'OVER'
                                      else prop_data['best_under_odds']),
                        'game': f"{away} @ {home}",
                        'event_id': event_id,
                    }
                    game_picks.append(pick)

        # Sort by confidence, then edge
        game_picks.sort(key=lambda x: (x['confidence']['score'], abs(x['edge']['edge'])), reverse=True)

        # Show top picks for this game
        if game_picks:
            for pick in game_picks[:5]:  # Top 5 per game
                e = pick['edge']
                c = pick['confidence']
                print(f"    {pick['player']:<22} {pick['prop']:<8} "
                      f"Line: {pick['line']:>5.1f}  Proj: {pick['projection']:>5.1f}  "
                      f"Edge: {e['edge']:>+5.1f}  {e['direction']:<6} "
                      f"Conf: {c['score']}/5  ${pick['sizing']['suggested_amount']:.2f}")
                all_picks.append(pick)
        else:
            print(f"    No actionable picks for this game.")

    if not all_picks:
        print(f"\n  No picks met the confidence threshold tonight.")
        return

    # Step 3: Filter and rank final slate
    # Remove confidence 1 (Skip) picks
    actionable = [p for p in all_picks if p['confidence']['score'] >= 3]
    actionable.sort(key=lambda x: (x['confidence']['score'], abs(x['edge']['edge'])), reverse=True)

    # Anti-bias check
    if actionable:
        dirs = [p['edge']['direction'] for p in actionable]
        over_pct = dirs.count('OVER') / len(dirs) * 100
        under_pct = dirs.count('UNDER') / len(dirs) * 100
        bias_warning = over_pct >= 70 or under_pct >= 70
    else:
        bias_warning = False

    # Total exposure check
    total_exposure = sum(p['sizing']['suggested_pct'] for p in actionable)

    print(f"\n{'='*80}")
    print(f"  FINAL PAPER SLATE — {len(actionable)} picks from {games_analyzed} games")
    print(f"{'='*80}")
    print(f"  {'Player':<22} {'Prop':<8} {'Line':>5} {'Proj':>5} {'Edge':>6} {'Dir':<6} {'Conf':<5} {'Size':>7}")
    print(f"  {'─'*75}")

    for p in actionable:
        print(f"  {p['player']:<22} {p['prop']:<8} {p['line']:>5.1f} "
              f"{p['projection']:>5.1f} {p['edge']['edge']:>+5.1f}  "
              f"{p['edge']['direction']:<6} {p['confidence']['score']}/5   "
              f"${p['sizing']['suggested_amount']:>6.2f}")

    print(f"  {'─'*75}")
    print(f"  Total exposure: {total_exposure:.1f}% of bankroll")

    if bias_warning:
        print(f"  BIAS WARNING: {max(over_pct, under_pct):.0f}% picks lean one direction.")

    if total_exposure > 15:
        print(f"  EXPOSURE WARNING: Over 15% daily limit.")

    # Step 4: Log paper bets
    data = load_paper_data()
    data['bankroll']['current'] = bankroll
    date_str = datetime.now().strftime('%Y-%m-%d')
    slate_entry = {
        'date': date_str,
        'games_analyzed': games_analyzed,
        'total_props_scanned': sum(1 for _ in all_picks),
        'actionable_picks': len(actionable),
    }
    data['daily_slates'].append(slate_entry)

    logged = 0
    for p in actionable:
        bet_id = f"paper-{date_str}-{logged + 1:03d}"
        bet = {
            'id': bet_id,
            'date': date_str,
            'type': 'paper',
            'player': p['player'],
            'prop': p['prop'],
            'line': p['line'],
            'direction': p['edge']['direction'].lower(),
            'projection': p['projection'],
            'edge': p['edge']['edge'],
            'confidence': p['confidence']['score'],
            'suggested_stake': p['sizing']['suggested_amount'],
            'odds': p['best_odds'],
            'game': p['game'],
            'event_id': p['event_id'],
            'actual': None,
            'outcome': None,
            'closing_line': None,
            'clv': None,
        }
        data['bets'].append(bet)
        logged += 1

    save_paper_data(data)
    print(f"\n  {logged} paper bets logged to {PAPER_LOG}")
    print(f"  Run 'python execution/paper_trader.py results' tomorrow to enter outcomes.")
    print()


def cmd_results(args):
    """Enter results for pending paper bets."""
    data = load_paper_data()
    pending = [b for b in data['bets'] if b['outcome'] is None]

    if not pending:
        print("\nNo pending paper bets. Run 'slate' first.")
        return

    # Group by date
    dates = sorted(set(b['date'] for b in pending))

    print(f"\n{'='*60}")
    print(f"  PENDING PAPER BETS — {len(pending)} bets across {len(dates)} dates")
    print(f"{'='*60}")

    for date in dates:
        day_bets = [b for b in pending if b['date'] == date]
        print(f"\n  {date} ({len(day_bets)} bets)")
        print(f"  {'─'*55}")

        for b in day_bets:
            print(f"  {b['id']}  {b['player']:<20} {b['prop']:<8} "
                  f"{b['direction'].upper():<6} {b['line']:>5.1f}  "
                  f"Proj: {b['projection']:>5.1f}")

    print(f"\n  To enter results, use:")
    print(f"  python execution/paper_trader.py result <bet_id> <actual_value>")
    print(f"  Example: python execution/paper_trader.py result paper-2026-03-15-001 28")
    print()


def cmd_result(args):
    """Record a single paper bet result."""
    data = load_paper_data()
    bet = next((b for b in data['bets'] if b['id'] == args.bet_id), None)

    if not bet:
        print(f"Error: Bet ID '{args.bet_id}' not found.")
        sys.exit(1)

    if bet['outcome'] is not None:
        print(f"Error: Bet already has result: {bet['outcome']}")
        sys.exit(1)

    actual = args.actual
    bet['actual'] = actual

    # Determine win/loss
    if bet['direction'] == 'over':
        bet['outcome'] = 'win' if actual > bet['line'] else 'loss'
    else:
        bet['outcome'] = 'win' if actual < bet['line'] else 'loss'

    # Record closing line if provided
    if args.closing_line is not None:
        bet['closing_line'] = args.closing_line
        if bet['direction'] == 'over':
            bet['clv'] = round(bet['closing_line'] - bet['line'], 1)
        else:
            bet['clv'] = round(bet['line'] - bet['closing_line'], 1)

    # Simulate bankroll impact
    stake = bet['suggested_stake']
    if bet['outcome'] == 'win':
        odds = bet.get('odds', -110)
        if odds < 0:
            payout = stake * (100 / abs(odds))
        else:
            payout = stake * (odds / 100)
        data['bankroll']['current'] = round(data['bankroll']['current'] + payout, 2)
        profit_str = f"+${payout:.2f}"
    else:
        data['bankroll']['current'] = round(data['bankroll']['current'] - stake, 2)
        profit_str = f"-${stake:.2f}"

    save_paper_data(data)

    result_icon = 'WIN' if bet['outcome'] == 'win' else 'LOSS'
    print(f"  {result_icon}: {bet['player']} {bet['prop']} {bet['direction'].upper()} {bet['line']}")
    print(f"  Actual: {actual}  |  Line: {bet['line']}  |  {profit_str}")
    if bet.get('clv') is not None:
        clv_label = "POSITIVE" if bet['clv'] > 0 else "NEGATIVE"
        print(f"  CLV: {bet['clv']:+.1f} pts ({clv_label})")
    print(f"  Paper Bankroll: ${data['bankroll']['current']:.2f}")


def cmd_status(args):
    """Show paper trading progress dashboard."""
    data = load_paper_data()
    bets = data['bets']
    settled = [b for b in bets if b['outcome'] is not None]
    pending = [b for b in bets if b['outcome'] is None]
    wins = [b for b in settled if b['outcome'] == 'win']
    losses = [b for b in settled if b['outcome'] == 'loss']

    total_staked = sum(b['suggested_stake'] for b in settled)
    total_won = 0
    for b in wins:
        odds = b.get('odds', -110)
        if odds < 0:
            total_won += b['suggested_stake'] * (100 / abs(odds))
        else:
            total_won += b['suggested_stake'] * (odds / 100)
    total_lost = sum(b['suggested_stake'] for b in losses)
    net = total_won - total_lost
    hit_rate = len(wins) / len(settled) * 100 if settled else 0
    roi = (net / total_staked * 100) if total_staked > 0 else 0

    # Go/No-Go criteria
    enough_bets = len(settled) >= 200
    beating_breakeven = hit_rate > 53
    clv_bets = [b for b in settled if b.get('clv') is not None]
    avg_clv = sum(b['clv'] for b in clv_bets) / len(clv_bets) if clv_bets else 0
    positive_clv = avg_clv > 0

    print(f"\n{'='*60}")
    print(f"  PAPER TRADING DASHBOARD")
    print(f"{'='*60}")
    print(f"  Started:           {data.get('started', 'N/A')}")
    print(f"  Days Active:       {len(set(b['date'] for b in bets))}")
    print(f"  {'─'*55}")
    print(f"  Total Bets:        {len(bets)}")
    print(f"  Settled:           {len(settled)}")
    print(f"  Pending:           {len(pending)}")
    print(f"  Wins:              {len(wins)}")
    print(f"  Losses:            {len(losses)}")
    print(f"  Hit Rate:          {hit_rate:.1f}%")
    print(f"  ROI:               {roi:+.1f}%")
    print(f"  Net P/L:           ${net:+.2f}")
    print(f"  {'─'*55}")
    print(f"  Paper Bankroll:    ${data['bankroll']['current']:.2f}")
    print(f"  Initial:           ${data['bankroll']['initial']:.2f}")

    if clv_bets:
        print(f"  {'─'*55}")
        print(f"  CLV Data Points:   {len(clv_bets)}")
        print(f"  Average CLV:       {avg_clv:+.1f} pts")
        clv_pos = len([b for b in clv_bets if b['clv'] > 0])
        print(f"  CLV Hit Rate:      {clv_pos/len(clv_bets)*100:.1f}%")

    # Confidence calibration
    if settled:
        print(f"\n  Confidence Calibration")
        print(f"  {'─'*55}")
        print(f"  {'Conf':<6} {'Bets':>6} {'Wins':>6} {'Hit%':>8}")
        for level in range(2, 6):
            level_bets = [b for b in settled if b['confidence'] == level]
            level_wins = [b for b in level_bets if b['outcome'] == 'win']
            if level_bets:
                rate = len(level_wins) / len(level_bets) * 100
                print(f"  {level:<6} {len(level_bets):>6} {len(level_wins):>6} {rate:>7.1f}%")

    # Go/No-Go
    print(f"\n  {'='*55}")
    print(f"  GO / NO-GO CRITERIA (need 200+ settled bets)")
    print(f"  {'─'*55}")

    progress = min(len(settled) / 200 * 100, 100)
    print(f"  Bets:              {len(settled)}/200 ({progress:.0f}%)")

    status_bet = 'PASS' if beating_breakeven else 'FAIL' if settled else 'PENDING'
    status_clv = 'PASS' if positive_clv else 'FAIL' if clv_bets else 'PENDING'

    print(f"  Hit Rate > 53%:    {status_bet} ({hit_rate:.1f}%)")
    print(f"  Positive CLV:      {status_clv} ({avg_clv:+.1f} pts)")

    if len(settled) >= 200:
        conf_calibrated = True
        for level in [3, 4, 5]:
            level_bets = [b for b in settled if b['confidence'] == level]
            if not level_bets:
                continue
            level_rate = len([b for b in level_bets if b['outcome'] == 'win']) / len(level_bets)
            prev_level_bets = [b for b in settled if b['confidence'] == level - 1]
            if prev_level_bets:
                prev_rate = len([b for b in prev_level_bets if b['outcome'] == 'win']) / len(prev_level_bets)
                if level_rate < prev_rate:
                    conf_calibrated = False

        status_cal = 'PASS' if conf_calibrated else 'FAIL'
        print(f"  Conf Calibrated:   {status_cal}")

        if beating_breakeven and positive_clv:
            print(f"\n  VERDICT: GO — Ready for live deployment (conservative limits)")
        else:
            print(f"\n  VERDICT: NO-GO — Continue iterating before risking real money")
    else:
        remaining_bets = 200 - len(settled)
        est_days = remaining_bets // 5 if remaining_bets > 0 else 0  # ~5 bets/day
        print(f"\n  Need {remaining_bets} more bets (~{est_days} days at 5/day)")

    print()


def main():
    parser = argparse.ArgumentParser(
        description='NBA Paper Trader — Automated paper trading pipeline'
    )
    sub = parser.add_subparsers(dest='command')

    # slate
    p_slate = sub.add_parser('slate', help="Generate tonight's paper trading picks")
    p_slate.add_argument('--bankroll', type=float, default=1000,
                         help='Paper bankroll (default: 1000)')
    p_slate.add_argument('--game', type=str, default=None,
                         help='Specific game event ID')

    # results
    sub.add_parser('results', help='Show pending paper bets')

    # result (single)
    p_result = sub.add_parser('result', help='Record a paper bet result')
    p_result.add_argument('bet_id', help='Paper bet ID')
    p_result.add_argument('actual', type=float, help='Actual stat value')
    p_result.add_argument('--closing-line', type=float, default=None,
                          help='Closing line at game time (for CLV)')

    # status
    sub.add_parser('status', help='Paper trading progress dashboard')

    args = parser.parse_args()

    if args.command == 'slate':
        cmd_slate(args)
    elif args.command == 'results':
        cmd_results(args)
    elif args.command == 'result':
        cmd_result(args)
    elif args.command == 'status':
        cmd_status(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
