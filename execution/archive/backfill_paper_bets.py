#!/usr/bin/env python3
"""
NBA Paper Bet Backfill — Generate historical paper bets from past game data.

Walks through each player's game log, calculates what the projection engine
would have predicted BEFORE each game (using only prior data), compares to
an estimated line (season average proxy), and logs settled paper bets.

This is NOT a perfect backtest — we don't have historical sportsbook lines.
The season average is a reasonable proxy for what books set as a baseline.
The goal is to accumulate enough data to activate the self-learning loops.

Usage:
    python execution/backfill_paper_bets.py --games 20              # Last 20 games per player
    python execution/backfill_paper_bets.py --games 30 --dry-run    # Preview without logging
    python execution/backfill_paper_bets.py --games 15 --min-edge 2 # Stricter edge filter
"""

import argparse
import json
import math
import os
import sys
import time
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from execution.nba_stats import find_player, get_player_gamelog, PROP_STAT_MAP, API_DELAY, SEASON

PAPER_LOG = os.path.join(ROOT, '.agent', 'paper-trading.json')

# Top NBA prop targets — stars and key starters with consistent minutes
TARGET_PLAYERS = [
    "Nikola Jokic", "Shai Gilgeous-Alexander", "Luka Doncic",
    "Jayson Tatum", "Anthony Edwards", "Donovan Mitchell",
    "Jalen Brunson", "Trae Young", "LaMelo Ball",
    "Cade Cunningham", "Scottie Barnes", "Domantas Sabonis",
    "De'Aaron Fox", "Tyrese Maxey", "Devin Booker",
    "Jaylen Brown", "Karl-Anthony Towns", "Paolo Banchero",
    "Alperen Sengun", "Jalen Green", "Amen Thompson",
    "Victor Wembanyama", "Julius Randle", "Damian Lillard",
    "Giannis Antetokounmpo", "Ja Morant", "Brandon Ingram",
    "Rudy Gobert", "Deni Avdija", "Cooper Flagg",
    "Franz Wagner", "Evan Mobley", "Bam Adebayo",
    "Jimmy Butler", "Pascal Siakam", "Jalen Williams",
    "Anthony Davis", "LeBron James", "Stephen Curry",
    "Kyrie Irving",
]

# Props to backtest
PROP_TYPES = ['points', 'rebounds', 'assists']


def load_paper_data():
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
    os.makedirs(os.path.dirname(PAPER_LOG), exist_ok=True)
    with open(PAPER_LOG, 'w') as f:
        json.dump(data, f, indent=2)


def calculate_projection_at_game(games, game_index, prop_type):
    """
    Calculate what the 60/25/15 projection would have been BEFORE game at game_index.
    Uses only games AFTER game_index (older games, since logs are reverse-chronological).

    Returns (projection, season_avg, std_dev, last_10_avg) or None if insufficient data.
    """
    stat_col = PROP_STAT_MAP.get(prop_type)
    if stat_col is None:
        return None

    # Games before this one (higher indices = older games)
    prior_games = games[game_index + 1:]
    if len(prior_games) < 5:
        return None  # Need at least 5 prior games

    values = [g[stat_col] for g in prior_games]

    season_avg = sum(values) / len(values)
    last_10 = values[:10]
    last_3 = values[:3]

    last_10_avg = sum(last_10) / len(last_10)
    last_3_avg = sum(last_3) / len(last_3)

    # Weighted projection: 60% last 10, 25% season, 15% last 3
    projection = (last_10_avg * 0.60) + (season_avg * 0.25) + (last_3_avg * 0.15)

    # Standard deviation of last 10
    mean = last_10_avg
    variance = sum((x - mean) ** 2 for x in last_10) / len(last_10)
    std_dev = variance ** 0.5

    return {
        'projection': round(projection, 1),
        'season_avg': round(season_avg, 1),
        'last_10_avg': round(last_10_avg, 1),
        'last_3_avg': round(last_3_avg, 1),
        'std_dev': round(std_dev, 1),
        'games_played': len(values),
    }


def score_confidence(edge_abs, std_dev, factors_aligned):
    """Simplified confidence scoring for backfill."""
    if edge_abs >= 5 and std_dev < edge_abs and factors_aligned >= 2:
        return 5
    elif edge_abs >= 3 and factors_aligned >= 2:
        return 4
    elif edge_abs >= 1.5 and factors_aligned >= 1:
        return 3
    elif edge_abs >= 1:
        return 2
    return 1


def backfill_player(player_name, num_games, min_edge, min_confidence, dry_run=False):
    """
    Backfill paper bets for a single player.
    Returns list of settled bet dicts.
    """
    player = find_player(player_name)
    if not player:
        return []

    # Pull full season game log
    try:
        all_games = get_player_gamelog(player['id'])
    except Exception:
        return []

    if not all_games or len(all_games) < 10:
        return []

    # Determine how many games to backtest (capped by available data minus buffer)
    max_backtest = min(num_games, len(all_games) - 5)  # Need 5 prior games minimum
    if max_backtest <= 0:
        return []

    bets = []

    for prop_type in PROP_TYPES:
        stat_col = PROP_STAT_MAP.get(prop_type)
        if stat_col is None:
            continue

        for i in range(max_backtest):
            game = all_games[i]
            actual = game.get(stat_col)
            if actual is None:
                continue

            game_date = game.get('GAME_DATE', '')
            matchup = game.get('MATCHUP', '')
            minutes = game.get('MIN', 0)

            # Skip games with very low minutes (garbage time, injury exit)
            if minutes and minutes < 15:
                continue

            # Calculate what our projection would have been BEFORE this game
            proj_data = calculate_projection_at_game(all_games, i, prop_type)
            if proj_data is None:
                continue

            projection = proj_data['projection']
            season_avg = proj_data['season_avg']
            std_dev = proj_data['std_dev']

            # Estimated line = season average (books' baseline proxy)
            estimated_line = season_avg

            # Edge calculation
            edge = projection - estimated_line
            if abs(edge) < 0.5:
                continue  # No meaningful edge

            direction = 'over' if edge > 0 else 'under'
            edge_abs = abs(edge)

            # Check minimum edge
            if edge_abs < min_edge:
                continue

            # Count aligned factors (simplified — no pace/defense adjustment in backfill)
            factors = 0
            if edge_abs > std_dev:
                factors += 1  # Edge exceeds volatility
            if proj_data['last_10_avg'] != proj_data['season_avg']:
                trend_edge = proj_data['last_10_avg'] - season_avg
                if (direction == 'over' and trend_edge > 0) or \
                   (direction == 'under' and trend_edge < 0):
                    factors += 1  # Trend supports direction

            confidence = score_confidence(edge_abs, std_dev, factors)
            if confidence < min_confidence:
                continue

            # Determine outcome
            if direction == 'over':
                outcome = 'win' if actual > estimated_line else 'loss'
            else:
                outcome = 'win' if actual < estimated_line else 'loss'

            # Kelly sizing (simplified)
            kelly_pct = min(edge_abs / 110 / 2, 0.05) * 100  # Half-Kelly, capped at 5%
            suggested_stake = round(1000 * kelly_pct / 100, 2)

            bet = {
                'player': player['full_name'],
                'prop': prop_type,
                'line': estimated_line,
                'direction': direction,
                'projection': projection,
                'edge': round(edge, 1),
                'confidence': confidence,
                'suggested_stake': suggested_stake,
                'odds': -110,
                'game': matchup,
                'game_date': game_date,
                'actual': actual,
                'outcome': outcome,
                'closing_line': None,
                'clv': None,
                'backfilled': True,
            }
            bets.append(bet)

    return bets


def main():
    parser = argparse.ArgumentParser(description='Backfill historical paper bets')
    parser.add_argument('--games', type=int, default=20,
                        help='Number of recent games per player to backtest (default: 20)')
    parser.add_argument('--min-edge', type=float, default=1.5,
                        help='Minimum edge in points to qualify (default: 1.5)')
    parser.add_argument('--min-confidence', type=int, default=3,
                        help='Minimum confidence score to log (default: 3)')
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview results without logging to paper-trading.json')
    parser.add_argument('--max-bets', type=int, default=250,
                        help='Maximum total bets to generate (default: 250)')
    parser.add_argument('--players', type=str, default=None,
                        help='Comma-separated player names (default: use built-in target list)')
    args = parser.parse_args()

    players = args.players.split(',') if args.players else TARGET_PLAYERS

    print(f"\n{'='*70}")
    print(f"  NBA PAPER BET BACKFILL")
    print(f"{'='*70}")
    print(f"  Players:        {len(players)}")
    print(f"  Games/player:   {args.games}")
    print(f"  Min edge:       {args.min_edge} pts")
    print(f"  Min confidence: {args.min_confidence}/5")
    print(f"  Max bets:       {args.max_bets}")
    print(f"  Dry run:        {args.dry_run}")
    print(f"{'='*70}\n")

    all_bets = []
    player_count = 0
    skipped = 0

    for player_name in players:
        if len(all_bets) >= args.max_bets:
            break

        print(f"  [{player_count+1}/{len(players)}] {player_name}...", end=' ', flush=True)
        player_bets = backfill_player(
            player_name, args.games, args.min_edge, args.min_confidence, args.dry_run
        )

        if player_bets:
            # Cap per player to prevent one player dominating
            remaining = args.max_bets - len(all_bets)
            player_bets = player_bets[:min(len(player_bets), remaining, 15)]
            all_bets.extend(player_bets)
            wins = sum(1 for b in player_bets if b['outcome'] == 'win')
            print(f"{len(player_bets)} bets ({wins}W/{len(player_bets)-wins}L)")
        else:
            skipped += 1
            print(f"skipped (no data or no edge)")

        player_count += 1
        time.sleep(API_DELAY)  # Rate limit protection

    # Summary
    total = len(all_bets)
    wins = sum(1 for b in all_bets if b['outcome'] == 'win')
    losses = total - wins
    hit_rate = wins / total * 100 if total > 0 else 0

    # Confidence breakdown
    conf_stats = {}
    for level in range(2, 6):
        level_bets = [b for b in all_bets if b['confidence'] == level]
        level_wins = sum(1 for b in level_bets if b['outcome'] == 'win')
        if level_bets:
            conf_stats[level] = {
                'bets': len(level_bets),
                'wins': level_wins,
                'rate': round(level_wins / len(level_bets) * 100, 1)
            }

    # Direction breakdown
    overs = [b for b in all_bets if b['direction'] == 'over']
    unders = [b for b in all_bets if b['direction'] == 'under']
    over_wins = sum(1 for b in overs if b['outcome'] == 'win')
    under_wins = sum(1 for b in unders if b['outcome'] == 'win')

    print(f"\n{'='*70}")
    print(f"  BACKFILL RESULTS")
    print(f"{'='*70}")
    print(f"  Total bets:     {total}")
    print(f"  Wins:           {wins}")
    print(f"  Losses:         {losses}")
    print(f"  Hit Rate:       {hit_rate:.1f}%")
    print(f"  Players used:   {player_count - skipped}/{player_count}")
    print(f"{'─'*70}")
    print(f"  Direction breakdown:")
    print(f"    OVER:  {len(overs)} bets, {over_wins}W ({over_wins/len(overs)*100:.1f}% hit)" if overs else "    OVER:  0 bets")
    print(f"    UNDER: {len(unders)} bets, {under_wins}W ({under_wins/len(unders)*100:.1f}% hit)" if unders else "    UNDER: 0 bets")
    print(f"{'─'*70}")
    print(f"  Confidence calibration:")
    for level, stats in sorted(conf_stats.items()):
        print(f"    Conf {level}: {stats['bets']:>4} bets, {stats['wins']:>4}W, {stats['rate']:>5.1f}% hit")

    # Projection accuracy
    errors = [abs(b['projection'] - b['actual']) for b in all_bets]
    if errors:
        mean_error = sum(errors) / len(errors)
        print(f"{'─'*70}")
        print(f"  Mean Projection Error: {mean_error:.1f} pts")

    if args.dry_run:
        print(f"\n  DRY RUN — no bets logged. Remove --dry-run to persist.")
    else:
        # Log to paper-trading.json
        data = load_paper_data()
        existing_ids = set(b['id'] for b in data['bets'])
        logged = 0

        for bet in all_bets:
            game_date = bet.pop('game_date')
            date_str = game_date if game_date else datetime.now().strftime('%Y-%m-%d')
            # Generate unique bet ID
            bet_id = f"backfill-{date_str}-{logged + 1:04d}"
            while bet_id in existing_ids:
                logged += 1
                bet_id = f"backfill-{date_str}-{logged + 1:04d}"

            bet['id'] = bet_id
            bet['date'] = date_str
            bet['type'] = 'paper-backfill'
            bet['event_id'] = None

            # Update bankroll simulation
            stake = bet['suggested_stake']
            if bet['outcome'] == 'win':
                payout = stake * (100 / 110)  # -110 odds
                data['bankroll']['current'] = round(data['bankroll']['current'] + payout, 2)
            else:
                data['bankroll']['current'] = round(data['bankroll']['current'] - stake, 2)

            data['bets'].append(bet)
            existing_ids.add(bet_id)
            logged += 1

        save_paper_data(data)
        print(f"\n  {logged} backfilled bets logged to {PAPER_LOG}")

    print()


if __name__ == '__main__':
    main()
