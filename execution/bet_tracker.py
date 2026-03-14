#!/usr/bin/env python3
"""
NBA Bet Tracker — CLI for logging prop bets, recording results, and analyzing performance.

Usage:
    python execution/bet_tracker.py init 500
    python execution/bet_tracker.py log "Jayson Tatum" points 27.5 over --projection 30.2 --confidence 4 --stake 20 --odds -110
    python execution/bet_tracker.py result 2026-03-14-001 31 win
    python execution/bet_tracker.py summary
    python execution/bet_tracker.py summary --date 2026-03-14
    python execution/bet_tracker.py calibration
    python execution/bet_tracker.py roi
"""

import argparse
import json
import os
import sys
from datetime import datetime

DATA_FILE = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    '.agent', 'bet-tracking.json'
)

VALID_PROPS = ['points', 'rebounds', 'assists', 'threes', 'steals', 'blocks', 'pts_reb_ast']


def load_data():
    """Load tracking data from JSON file."""
    if not os.path.exists(DATA_FILE):
        print(f"Error: Tracking file not found at {DATA_FILE}")
        print("Run 'python execution/bet_tracker.py init <bankroll>' first.")
        sys.exit(1)
    with open(DATA_FILE, 'r') as f:
        return json.load(f)


def save_data(data):
    """Save tracking data to JSON file."""
    os.makedirs(os.path.dirname(DATA_FILE), exist_ok=True)
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=2)


def calculate_payout(stake, odds):
    """Calculate profit from American odds.
    Negative odds (e.g., -110): payout = stake * (100 / abs(odds))
    Positive odds (e.g., +150): payout = stake * (odds / 100)
    """
    if odds < 0:
        return stake * (100 / abs(odds))
    else:
        return stake * (odds / 100)


def generate_bet_id(bets, date_str):
    """Generate bet ID in format YYYY-MM-DD-NNN."""
    existing = [b for b in bets if b['date'] == date_str]
    seq = len(existing) + 1
    return f"{date_str}-{seq:03d}"


# --- Commands ---

def cmd_init(args):
    """Initialize bankroll and tracking file."""
    if os.path.exists(DATA_FILE):
        resp = input(f"Tracking file already exists. Overwrite? (y/N): ").strip().lower()
        if resp != 'y':
            print("Aborted.")
            return

    data = {
        "bankroll": {
            "initial": args.bankroll,
            "current": args.bankroll
        },
        "bets": []
    }
    save_data(data)
    print(f"Initialized bankroll: ${args.bankroll:.2f}")
    print(f"Tracking file: {DATA_FILE}")


def cmd_log(args):
    """Log a new bet."""
    data = load_data()
    date_str = datetime.now().strftime('%Y-%m-%d')
    bet_id = generate_bet_id(data['bets'], date_str)
    edge = round(abs(args.projection - args.line), 2)

    bet = {
        "id": bet_id,
        "date": date_str,
        "player": args.player,
        "prop": args.prop,
        "line": args.line,
        "direction": args.direction,
        "projection": args.projection,
        "edge": edge,
        "confidence": args.confidence,
        "stake": args.stake,
        "odds": args.odds,
        "actual": None,
        "outcome": None,
        "payout": None,
        "notes": args.notes or ""
    }

    data['bets'].append(bet)
    save_data(data)

    print(f"Bet logged: {bet_id}")
    print(f"  {args.player} {args.prop} {args.direction} {args.line}")
    print(f"  Projection: {args.projection}  |  Edge: {edge}")
    print(f"  Confidence: {args.confidence}/5  |  Stake: ${args.stake:.2f}  |  Odds: {args.odds:+d}")


def cmd_result(args):
    """Record the outcome of a bet."""
    data = load_data()

    bet = next((b for b in data['bets'] if b['id'] == args.bet_id), None)
    if not bet:
        print(f"Error: Bet ID '{args.bet_id}' not found.")
        sys.exit(1)

    if bet['outcome'] is not None:
        print(f"Error: Bet '{args.bet_id}' already has a result: {bet['outcome']}")
        sys.exit(1)

    payout = calculate_payout(bet['stake'], bet['odds'])
    bet['actual'] = args.actual
    bet['outcome'] = args.outcome
    bet['payout'] = round(payout, 2) if args.outcome == 'win' else 0.0

    if args.outcome == 'win':
        data['bankroll']['current'] = round(data['bankroll']['current'] + payout, 2)
    else:
        data['bankroll']['current'] = round(data['bankroll']['current'] - bet['stake'], 2)

    save_data(data)

    print(f"Result recorded: {args.bet_id} -> {args.outcome.upper()}")
    print(f"  {bet['player']} {bet['prop']} {bet['direction']} {bet['line']}")
    print(f"  Actual: {args.actual}  |  Line: {bet['line']}")
    if args.outcome == 'win':
        print(f"  Profit: +${payout:.2f}")
    else:
        print(f"  Loss: -${bet['stake']:.2f}")
    print(f"  Bankroll: ${data['bankroll']['current']:.2f}")


def cmd_summary(args):
    """Print daily or overall summary."""
    data = load_data()
    bets = data['bets']

    if args.date:
        bets = [b for b in bets if b['date'] == args.date]
        header = f"Summary for {args.date}"
    else:
        header = "Overall Summary"

    settled = [b for b in bets if b['outcome'] is not None]
    pending = [b for b in bets if b['outcome'] is None]
    wins = [b for b in settled if b['outcome'] == 'win']
    losses = [b for b in settled if b['outcome'] == 'loss']

    total_staked = sum(b['stake'] for b in settled)
    total_returned = sum(b['stake'] + b['payout'] for b in wins)
    net = total_returned - total_staked
    win_rate = (len(wins) / len(settled) * 100) if settled else 0
    roi = (net / total_staked * 100) if total_staked > 0 else 0

    print(f"\n{'=' * 44}")
    print(f"  {header}")
    print(f"{'=' * 44}")
    print(f"  {'Total Bets:':<22} {len(bets):>8}")
    print(f"  {'Settled:':<22} {len(settled):>8}")
    print(f"  {'Pending:':<22} {len(pending):>8}")
    print(f"  {'Wins:':<22} {len(wins):>8}")
    print(f"  {'Losses:':<22} {len(losses):>8}")
    print(f"  {'Win Rate:':<22} {win_rate:>7.1f}%")
    print(f"  {'─' * 40}")
    print(f"  {'Total Staked:':<22} ${total_staked:>8.2f}")
    print(f"  {'Total Returned:':<22} ${total_returned:>8.2f}")
    print(f"  {'Net Profit/Loss:':<22} ${net:>+8.2f}")
    print(f"  {'ROI:':<22} {roi:>+7.1f}%")
    print(f"{'=' * 44}\n")


def cmd_calibration(args):
    """Print confidence level hit rates."""
    data = load_data()
    settled = [b for b in data['bets'] if b['outcome'] is not None]

    expected = {1: '~30%', 2: '~40%', 3: '~50%', 4: '~55%+', 5: '~65%+'}

    print(f"\n{'=' * 52}")
    print(f"  Confidence Calibration")
    print(f"{'=' * 52}")
    print(f"  {'Conf':<6} {'Bets':>6} {'Wins':>6} {'Hit Rate':>10} {'Expected':>10}")
    print(f"  {'─' * 48}")

    for level in range(1, 6):
        level_bets = [b for b in settled if b['confidence'] == level]
        level_wins = [b for b in level_bets if b['outcome'] == 'win']
        count = len(level_bets)
        wins = len(level_wins)
        rate = (wins / count * 100) if count > 0 else 0
        rate_str = f"{rate:.1f}%" if count > 0 else "N/A"
        print(f"  {level:<6} {count:>6} {wins:>6} {rate_str:>10} {expected[level]:>10}")

    print(f"{'=' * 52}\n")


def cmd_roi(args):
    """Print bankroll history and ROI."""
    data = load_data()
    initial = data['bankroll']['initial']
    current = data['bankroll']['current']

    # Simulate bankroll history to find peak and max drawdown
    bankroll = initial
    peak = initial
    max_drawdown = 0

    settled = [b for b in data['bets'] if b['outcome'] is not None]
    for bet in settled:
        if bet['outcome'] == 'win':
            bankroll += bet['payout']
        else:
            bankroll -= bet['stake']

        if bankroll > peak:
            peak = bankroll

        drawdown = peak - bankroll
        if drawdown > max_drawdown:
            max_drawdown = drawdown

    overall_roi = ((current - initial) / initial * 100) if initial > 0 else 0

    print(f"\n{'=' * 44}")
    print(f"  Bankroll Report")
    print(f"{'=' * 44}")
    print(f"  {'Initial Bankroll:':<22} ${initial:>8.2f}")
    print(f"  {'Current Bankroll:':<22} ${current:>8.2f}")
    print(f"  {'Peak Bankroll:':<22} ${peak:>8.2f}")
    print(f"  {'Max Drawdown:':<22} ${max_drawdown:>8.2f}")
    print(f"  {'Overall ROI:':<22} {overall_roi:>+7.1f}%")
    print(f"{'=' * 44}\n")


def main():
    parser = argparse.ArgumentParser(
        description='NBA Bet Tracker — Log props, record results, analyze performance.'
    )
    subparsers = parser.add_subparsers(dest='command', help='Command to run')

    # init
    p_init = subparsers.add_parser('init', help='Initialize bankroll')
    p_init.add_argument('bankroll', type=float, help='Starting bankroll amount')

    # log
    p_log = subparsers.add_parser('log', help='Log a new bet')
    p_log.add_argument('player', help='Player name')
    p_log.add_argument('prop', choices=VALID_PROPS, help='Stat type')
    p_log.add_argument('line', type=float, help='Posted line')
    p_log.add_argument('direction', choices=['over', 'under'], help='Over or under')
    p_log.add_argument('--projection', type=float, required=True, help='Your projected value')
    p_log.add_argument('--confidence', type=int, required=True, choices=range(1, 6),
                       metavar='1-5', help='Confidence score (1-5)')
    p_log.add_argument('--stake', type=float, required=True, help='Dollar amount wagered')
    p_log.add_argument('--odds', type=int, default=-110, help='American odds (default: -110)')
    p_log.add_argument('--notes', type=str, default='', help='Optional notes')

    # result
    p_result = subparsers.add_parser('result', help='Record bet outcome')
    p_result.add_argument('bet_id', help='Bet ID (e.g., 2026-03-14-001)')
    p_result.add_argument('actual', type=float, help='Actual stat value')
    p_result.add_argument('outcome', choices=['win', 'loss'], help='Win or loss')

    # summary
    p_summary = subparsers.add_parser('summary', help='Daily or overall summary')
    p_summary.add_argument('--date', type=str, default=None, help='Date filter (YYYY-MM-DD)')

    # calibration
    subparsers.add_parser('calibration', help='Confidence level hit rates')

    # roi
    subparsers.add_parser('roi', help='Bankroll history and ROI')

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(1)

    commands = {
        'init': cmd_init,
        'log': cmd_log,
        'result': cmd_result,
        'summary': cmd_summary,
        'calibration': cmd_calibration,
        'roi': cmd_roi,
    }

    commands[args.command](args)


if __name__ == '__main__':
    main()
