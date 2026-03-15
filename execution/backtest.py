#!/usr/bin/env python3
"""
NBA Projection Backtest — Prove the 60/25/15 formula works or kill it.

Tests the projection system against historical game data. For each game
(starting from game 11), generates a projection using ONLY data available
BEFORE that game, then compares to the actual result.

Since we don't have historical betting lines, we use the player's
season-to-date average as a proxy for the line (books typically set lines
near averages). This gives us a clean, unbiased test of whether our
weighted formula beats the naive "season average" baseline.

Usage:
    python execution/backtest.py run "Nikola Jokic" points               # Backtest one player
    python execution/backtest.py run "Nikola Jokic" points --season 2024-25
    python execution/backtest.py multi points --top 20                   # Top 20 players by GP
    python execution/backtest.py multi points --top 20 --season 2024-25
    python execution/backtest.py report                                  # Show saved results
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from execution.nba_stats import find_player, find_team, PROP_STAT_MAP, get_all_team_stats

RESULTS_DIR = os.path.join(ROOT, '.agent', 'backtest-results')
API_DELAY = 0.6

# ─── Core Backtest Logic ───────────────────────────────────────────────────

def get_raw_gamelog(player_id, season):
    """Pull full season game log without caching (backtest needs fresh data)."""
    from nba_api.stats.endpoints import playergamelog
    time.sleep(API_DELAY)
    log = playergamelog.PlayerGameLog(player_id=player_id, season=season)
    df = log.get_data_frames()[0]
    return df.to_dict('records')


def extract_stat(game, prop_type):
    """Extract the relevant stat from a game record."""
    stat_col = PROP_STAT_MAP.get(prop_type)
    if stat_col is None and prop_type == 'pts_reb_ast':
        return game['PTS'] + game['REB'] + game['AST']
    elif stat_col:
        return game[stat_col]
    return None


def backtest_player(player_id, player_name, prop_type, season='2025-26',
                    min_games_before=10):
    """
    Backtest the 60/25/15 projection formula for a single player.

    For each game after the first min_games_before games:
    1. Calculate season-to-date average (proxy for "the line")
    2. Calculate weighted projection using 60/25/15 formula
    3. Determine direction: OVER if projection > line, UNDER if projection < line
    4. Check if actual result agrees with our direction
    5. Track hit rate, edge accuracy, and calibration

    Returns a dict with full results.
    """
    games = get_raw_gamelog(player_id, season)
    if not games:
        return {'error': f'No games found for {player_name} in {season}'}

    # Games are sorted newest-first, reverse for chronological order
    games = list(reversed(games))

    if len(games) < min_games_before + 5:
        return {'error': f'Only {len(games)} games — need at least {min_games_before + 5}'}

    results = []

    for i in range(min_games_before, len(games)):
        # All games BEFORE this one (chronological order)
        prior_games = games[:i]
        current_game = games[i]
        actual = extract_stat(current_game, prop_type)

        if actual is None:
            continue

        # Extract stats from prior games
        prior_values = [extract_stat(g, prop_type) for g in prior_games]
        prior_values = [v for v in prior_values if v is not None]

        if len(prior_values) < min_games_before:
            continue

        # Season-to-date average (proxy for "the line")
        season_avg = sum(prior_values) / len(prior_values)

        # Last 10 games (most recent 10 in the prior set)
        last_10 = prior_values[-10:]
        last_10_avg = sum(last_10) / len(last_10)

        # Last 3 games
        last_3 = prior_values[-3:]
        last_3_avg = sum(last_3) / len(last_3)

        # Weighted projection: 60% last 10, 25% season, 15% last 3
        projection = (last_10_avg * 0.60) + (season_avg * 0.25) + (last_3_avg * 0.15)

        # The "line" is the season-to-date average
        line = season_avg

        # Edge and direction
        edge = projection - line
        if abs(edge) < 0.1:
            direction = 'SKIP'
        else:
            direction = 'OVER' if edge > 0 else 'UNDER'

        # Did the actual result agree with our direction?
        if direction == 'OVER':
            hit = actual > line
        elif direction == 'UNDER':
            hit = actual < line
        else:
            hit = None  # Skip

        # Projection accuracy
        proj_error = abs(projection - actual)

        # Would naive (season avg) have been right?
        # Naive always predicts "actual will be near the average"
        # So naive "OVER" if last game was over avg, etc. — but that's recency bias
        # Better comparison: naive = season avg as the prediction
        naive_error = abs(season_avg - actual)

        # Standard deviation of last 10 for context
        mean_10 = last_10_avg
        std_dev = (sum((x - mean_10) ** 2 for x in last_10) / len(last_10)) ** 0.5

        results.append({
            'game_num': i + 1,
            'date': current_game['GAME_DATE'],
            'matchup': current_game['MATCHUP'],
            'actual': actual,
            'projection': round(projection, 1),
            'season_avg': round(season_avg, 1),
            'line': round(line, 1),
            'edge': round(edge, 1),
            'direction': direction,
            'hit': hit,
            'proj_error': round(proj_error, 1),
            'naive_error': round(naive_error, 1),
            'std_dev': round(std_dev, 1),
        })

    if not results:
        return {'error': 'No valid backtest observations'}

    # ─── Aggregate Metrics ──────────────────────────────────────────────

    # Filter out skips
    directional = [r for r in results if r['direction'] != 'SKIP']
    hits = [r for r in directional if r['hit']]
    misses = [r for r in directional if not r['hit']]

    hit_rate = len(hits) / len(directional) * 100 if directional else 0

    # Average projection error vs naive error
    avg_proj_error = sum(r['proj_error'] for r in results) / len(results)
    avg_naive_error = sum(r['naive_error'] for r in results) / len(results)

    # Simulated ROI at -110 odds
    # Each hit pays +$90.91 on a $100 bet, each miss loses $100
    # (standard -110 payout)
    sim_profit = len(hits) * 90.91 - len(misses) * 100
    sim_roi = (sim_profit / (len(directional) * 100)) * 100 if directional else 0

    # Edge magnitude analysis
    strong_edge = [r for r in directional if abs(r['edge']) >= 2]
    strong_hits = [r for r in strong_edge if r['hit']]
    strong_rate = len(strong_hits) / len(strong_edge) * 100 if strong_edge else 0

    sig_edge = [r for r in directional if abs(r['edge']) >= 5]
    sig_hits = [r for r in sig_edge if r['hit']]
    sig_rate = len(sig_hits) / len(sig_edge) * 100 if sig_edge else 0

    # Direction balance
    overs = [r for r in directional if r['direction'] == 'OVER']
    unders = [r for r in directional if r['direction'] == 'UNDER']
    over_hit = len([r for r in overs if r['hit']]) / len(overs) * 100 if overs else 0
    under_hit = len([r for r in unders if r['hit']]) / len(unders) * 100 if unders else 0

    return {
        'player': player_name,
        'player_id': player_id,
        'prop': prop_type,
        'season': season,
        'total_games': len(games),
        'observations': len(results),
        'directional_bets': len(directional),
        'skipped': len(results) - len(directional),
        'metrics': {
            'hit_rate': round(hit_rate, 1),
            'hits': len(hits),
            'misses': len(misses),
            'sim_roi': round(sim_roi, 1),
            'sim_profit_per_100': round(sim_profit / len(directional), 2) if directional else 0,
            'avg_proj_error': round(avg_proj_error, 1),
            'avg_naive_error': round(avg_naive_error, 1),
            'proj_beats_naive': avg_proj_error < avg_naive_error,
            'strong_edge_rate': round(strong_rate, 1),
            'strong_edge_count': len(strong_edge),
            'sig_edge_rate': round(sig_rate, 1),
            'sig_edge_count': len(sig_edge),
        },
        'direction_balance': {
            'overs': len(overs),
            'unders': len(unders),
            'over_hit_rate': round(over_hit, 1),
            'under_hit_rate': round(under_hit, 1),
        },
        'observations_detail': results,
    }


# ─── Multi-Player Backtest ─────────────────────────────────────────────────

def get_top_players(season='2025-26', top_n=20):
    """Get top N players by games played for the given season."""
    from nba_api.stats.endpoints import leagueleaders
    time.sleep(API_DELAY)
    leaders = leagueleaders.LeagueLeaders(
        season=season,
        stat_category_abbreviation='PTS'
    )
    df = leaders.get_data_frames()[0]
    # Take top N by games played (GP column)
    df_sorted = df.sort_values('GP', ascending=False).head(top_n)
    return [(int(row['PLAYER_ID']), row['PLAYER']) for _, row in df_sorted.iterrows()]


def backtest_multi(prop_type, season='2025-26', top_n=20):
    """Backtest across multiple players. Returns aggregate results."""
    players = get_top_players(season, top_n)
    all_results = []
    player_summaries = []

    print(f"\n  Backtesting {len(players)} players — {prop_type.upper()} — {season}")
    print(f"  {'─'*60}")

    for pid, pname in players:
        print(f"  Testing {pname}...", end=' ', flush=True)
        result = backtest_player(pid, pname, prop_type, season)

        if 'error' in result:
            print(f"SKIP ({result['error']})")
            continue

        m = result['metrics']
        print(f"  {m['hit_rate']:.1f}% ({m['hits']}/{m['hits']+m['misses']})  "
              f"ROI: {m['sim_roi']:+.1f}%  "
              f"ProjErr: {m['avg_proj_error']:.1f} vs Naive: {m['avg_naive_error']:.1f}")

        all_results.append(result)
        player_summaries.append({
            'player': pname,
            'observations': result['directional_bets'],
            'hit_rate': m['hit_rate'],
            'sim_roi': m['sim_roi'],
            'avg_proj_error': m['avg_proj_error'],
            'avg_naive_error': m['avg_naive_error'],
            'proj_beats_naive': m['proj_beats_naive'],
        })

    if not all_results:
        print("  No valid results.")
        return None

    # Aggregate across all players
    total_bets = sum(r['directional_bets'] for r in all_results)
    total_hits = sum(r['metrics']['hits'] for r in all_results)
    total_misses = sum(r['metrics']['misses'] for r in all_results)
    overall_hit = total_hits / total_bets * 100 if total_bets else 0
    overall_profit = total_hits * 90.91 - total_misses * 100
    overall_roi = (overall_profit / (total_bets * 100)) * 100 if total_bets else 0

    proj_beats = sum(1 for r in all_results if r['metrics']['proj_beats_naive'])
    avg_proj_err = sum(r['metrics']['avg_proj_error'] for r in all_results) / len(all_results)
    avg_naive_err = sum(r['metrics']['avg_naive_error'] for r in all_results) / len(all_results)

    # Strong edge subset
    strong_bets = sum(r['metrics']['strong_edge_count'] for r in all_results)
    strong_hits_total = sum(
        len([o for o in r['observations_detail'] if abs(o['edge']) >= 2 and o['hit'] and o['direction'] != 'SKIP'])
        for r in all_results
    )
    strong_rate = strong_hits_total / strong_bets * 100 if strong_bets else 0

    aggregate = {
        'prop_type': prop_type,
        'season': season,
        'players_tested': len(all_results),
        'total_observations': total_bets,
        'overall_hit_rate': round(overall_hit, 1),
        'overall_roi': round(overall_roi, 1),
        'overall_profit': round(overall_profit, 2),
        'avg_proj_error': round(avg_proj_err, 1),
        'avg_naive_error': round(avg_naive_err, 1),
        'proj_beats_naive_pct': round(proj_beats / len(all_results) * 100, 1),
        'strong_edge_hit_rate': round(strong_rate, 1),
        'strong_edge_count': strong_bets,
        'breakeven': 52.4,
        'player_summaries': sorted(player_summaries, key=lambda x: x['hit_rate'], reverse=True),
    }

    # Save results
    os.makedirs(RESULTS_DIR, exist_ok=True)
    filename = f"backtest_{prop_type}_{season.replace('-', '')}_{len(all_results)}players.json"
    filepath = os.path.join(RESULTS_DIR, filename)
    with open(filepath, 'w') as f:
        json.dump(aggregate, f, indent=2)
    print(f"\n  Results saved to {filepath}")

    return aggregate


# ─── CLI ────────────────────────────────────────────────────────────────────

def cmd_run(args):
    """Backtest a single player."""
    player = find_player(args.player)
    if not player:
        print(f"Player not found: {args.player}")
        sys.exit(1)

    result = backtest_player(player['id'], player['full_name'],
                             args.prop, args.season)

    if 'error' in result:
        print(f"Error: {result['error']}")
        sys.exit(1)

    m = result['metrics']
    d = result['direction_balance']

    print(f"\n{'='*65}")
    print(f"  BACKTEST: {result['player']} — {result['prop'].upper()}")
    print(f"  Season: {result['season']}  |  {result['total_games']} games")
    print(f"{'='*65}")

    print(f"\n  Results ({result['directional_bets']} bets, {result['skipped']} skipped)")
    print(f"  {'─'*50}")
    print(f"  Hit Rate:              {m['hit_rate']:.1f}% ({m['hits']}/{m['hits']+m['misses']})")
    print(f"  Breakeven:             52.4%")
    print(f"  Simulated ROI:         {m['sim_roi']:+.1f}%")

    if m['hit_rate'] > 52.4:
        print(f"  BEATING BREAKEVEN")
    else:
        print(f"  BELOW BREAKEVEN")

    print(f"\n  Projection Quality")
    print(f"  {'─'*50}")
    print(f"  Avg Projection Error:  {m['avg_proj_error']:.1f} pts")
    print(f"  Avg Naive Error:       {m['avg_naive_error']:.1f} pts")
    print(f"  Formula beats naive:   {'YES' if m['proj_beats_naive'] else 'NO'}")

    print(f"\n  Edge Analysis")
    print(f"  {'─'*50}")
    print(f"  Strong edge (>2 pts):  {m['strong_edge_rate']:.1f}% ({m['strong_edge_count']} bets)")
    print(f"  Sig edge (>5 pts):     {m['sig_edge_rate']:.1f}% ({m['sig_edge_count']} bets)")

    print(f"\n  Direction Balance")
    print(f"  {'─'*50}")
    print(f"  OVER:                  {d['overs']} bets ({d['over_hit_rate']:.1f}% hit)")
    print(f"  UNDER:                 {d['unders']} bets ({d['under_hit_rate']:.1f}% hit)")

    # Show worst and best predictions
    sorted_by_error = sorted(result['observations_detail'], key=lambda x: x['proj_error'])
    best_5 = sorted_by_error[:5]
    worst_5 = sorted_by_error[-5:]

    print(f"\n  Best Predictions")
    print(f"  {'─'*50}")
    for r in best_5:
        print(f"  {r['date']:<15} Proj: {r['projection']:>5.1f}  Actual: {r['actual']:>5}  Err: {r['proj_error']:>4.1f}")

    print(f"\n  Worst Predictions")
    print(f"  {'─'*50}")
    for r in worst_5:
        print(f"  {r['date']:<15} Proj: {r['projection']:>5.1f}  Actual: {r['actual']:>5}  Err: {r['proj_error']:>4.1f}")

    print()

    if args.json:
        print(json.dumps(result, indent=2))


def cmd_multi(args):
    """Backtest across multiple players."""
    aggregate = backtest_multi(args.prop, args.season, args.top)

    if not aggregate:
        return

    print(f"\n{'='*75}")
    print(f"  AGGREGATE BACKTEST — {aggregate['prop_type'].upper()} — {aggregate['season']}")
    print(f"  {aggregate['players_tested']} players, {aggregate['total_observations']} observations")
    print(f"{'='*75}")

    print(f"\n  Overall Results")
    print(f"  {'─'*60}")
    print(f"  Hit Rate:                  {aggregate['overall_hit_rate']:.1f}%")
    print(f"  Breakeven:                 {aggregate['breakeven']}%")
    print(f"  Simulated ROI:             {aggregate['overall_roi']:+.1f}%")
    print(f"  Total Profit (per $100):   ${aggregate['overall_profit']:+.2f}")

    verdict = "EDGE DETECTED" if aggregate['overall_hit_rate'] > 52.4 else "NO EDGE"
    print(f"\n  VERDICT: {verdict}")

    print(f"\n  Projection Quality")
    print(f"  {'─'*60}")
    print(f"  Avg Projection Error:      {aggregate['avg_proj_error']:.1f} pts")
    print(f"  Avg Naive Error:           {aggregate['avg_naive_error']:.1f} pts")
    print(f"  Formula beats naive in:    {aggregate['proj_beats_naive_pct']:.0f}% of players")

    print(f"\n  Strong Edge Subset (>2 pts)")
    print(f"  {'─'*60}")
    print(f"  Hit Rate:                  {aggregate['strong_edge_hit_rate']:.1f}%")
    print(f"  Observations:              {aggregate['strong_edge_count']}")

    print(f"\n  Player Rankings")
    print(f"  {'─'*60}")
    print(f"  {'Player':<25} {'Obs':>5} {'Hit%':>7} {'ROI':>7} {'ProjErr':>8} {'Naive':>8}")
    print(f"  {'─'*60}")
    for p in aggregate['player_summaries']:
        marker = ' *' if p['hit_rate'] > 52.4 else ''
        print(f"  {p['player']:<25} {p['observations']:>5} {p['hit_rate']:>6.1f}% "
              f"{p['sim_roi']:>+6.1f}% {p['avg_proj_error']:>7.1f} {p['avg_naive_error']:>7.1f}{marker}")

    print(f"\n  * = beating breakeven (52.4%)")
    print()


def cmd_report(args):
    """Show saved backtest results."""
    if not os.path.exists(RESULTS_DIR):
        print("No backtest results found. Run a backtest first.")
        return

    files = sorted(os.listdir(RESULTS_DIR))
    if not files:
        print("No backtest results found.")
        return

    print(f"\n  Saved Backtest Results")
    print(f"  {'─'*50}")
    for f in files:
        if f.endswith('.json'):
            filepath = os.path.join(RESULTS_DIR, f)
            with open(filepath, 'r') as fh:
                data = json.load(fh)
            print(f"  {f}")
            print(f"    {data['prop_type'].upper()} — {data['season']} — "
                  f"{data['players_tested']} players, {data['total_observations']} obs")
            print(f"    Hit: {data['overall_hit_rate']}% | ROI: {data['overall_roi']:+.1f}% | "
                  f"{'EDGE' if data['overall_hit_rate'] > 52.4 else 'NO EDGE'}")
            print()


def main():
    parser = argparse.ArgumentParser(
        description='NBA Projection Backtest — Prove it or kill it'
    )
    sub = parser.add_subparsers(dest='command')

    # run (single player)
    p_run = sub.add_parser('run', help='Backtest a single player')
    p_run.add_argument('player', help='Player name')
    p_run.add_argument('prop', help=f"Prop type: {', '.join(PROP_STAT_MAP.keys())}")
    p_run.add_argument('--season', default='2025-26', help='Season (default: 2025-26)')
    p_run.add_argument('--json', action='store_true', help='Output JSON')

    # multi (multiple players)
    p_multi = sub.add_parser('multi', help='Backtest top N players')
    p_multi.add_argument('prop', help=f"Prop type: {', '.join(PROP_STAT_MAP.keys())}")
    p_multi.add_argument('--top', type=int, default=20, help='Number of players (default: 20)')
    p_multi.add_argument('--season', default='2025-26', help='Season (default: 2025-26)')

    # report
    sub.add_parser('report', help='Show saved backtest results')

    args = parser.parse_args()

    if args.command == 'run':
        cmd_run(args)
    elif args.command == 'multi':
        cmd_multi(args)
    elif args.command == 'report':
        cmd_report(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
