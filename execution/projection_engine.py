#!/usr/bin/env python3
"""
NBA Projection Engine — Combine real stats with live lines to detect edges.

This is the core analytical engine. It pulls actual game log data from nba_stats.py,
compares adjusted projections to live sportsbook lines from odds_fetcher.py,
and outputs edge analysis with confidence scoring.

Usage:
    python execution/projection_engine.py analyze "Nikola Jokic" points "San Antonio Spurs" --line 28.5
    python execution/projection_engine.py batch "players.json"     # Analyze multiple players from file
    python execution/projection_engine.py slate                    # Full slate analysis (all tonight's props)

The 'analyze' command is the workhorse — used by the game-day workflow to replace
Perplexity-sourced estimates with real data-driven projections.
"""

import argparse
import json
import os
import sys

# Add project root to path for imports
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from execution.nba_stats import (
    find_player, find_team, calculate_projection, get_team_stats,
    get_league_avg_pace, get_player_gamelog, build_matchup_context
)


# ─── Edge Calculation ───────────────────────────────────────────────────────

def calculate_edge(projection, line):
    """
    Calculate the edge between our projection and the posted line.

    Returns:
      - edge: raw difference (projection - line)
      - edge_pct: percentage edge
      - direction: 'OVER' or 'UNDER'
      - magnitude: 'significant' (>2), 'strong' (>5), or 'marginal' (<1)
    """
    edge = projection - line

    if abs(edge) < 0.001:
        return {
            'edge': 0, 'edge_pct': 0, 'direction': 'SKIP',
            'magnitude': 'none', 'raw_diff': 0
        }

    direction = 'OVER' if edge > 0 else 'UNDER'
    abs_edge = abs(edge)

    if abs_edge >= 5:
        magnitude = 'strong'
    elif abs_edge >= 2:
        magnitude = 'significant'
    elif abs_edge >= 1:
        magnitude = 'lean'
    else:
        magnitude = 'marginal'

    edge_pct = (edge / line) * 100 if line != 0 else 0

    return {
        'edge': round(edge, 1),
        'edge_pct': round(edge_pct, 1),
        'direction': direction,
        'magnitude': magnitude,
        'raw_diff': round(abs_edge, 1),
    }


# ─── Confidence Scoring ────────────────────────────────────────────────────

def score_confidence(edge_result, matchup_ctx, prop_type='points'):
    """
    Data-calibrated confidence scoring (v2.1 — evolved 2026-03-21).

    Key insight from 264-bet backtest: Player consistency (CV) is the #1
    predictor of pick success, not edge magnitude. Large edges (3-5 pts)
    actually hit WORSE than mid-range (1.5-3 pts) — the market is often
    right when our projection diverges significantly.

    Calibration results on 264 bets:
      Conf 3: 59.5% hit | Conf 4: 63.0% hit | Conf 5: 66.7% hit
      (v1 was flat ~56.5% across all levels)

    Foundation: CV drives base score, edge is a modifier (not the base),
    prop type and direction contribute, context factors upgrade/downgrade.
    """
    score = 1
    reasons = []

    abs_edge = edge_result['raw_diff']
    direction = edge_result['direction']
    proj = matchup_ctx['projection']
    ctx = matchup_ctx['context']
    adj = matchup_ctx['adjustments']

    cv = proj.get('coefficient_of_variation', 0.99)
    avg_min = proj.get('avg_minutes', 0)
    min_std = proj.get('minutes_std_dev', 0)

    # ── FOUNDATION: Player Consistency (CV) ──
    # Data: CV < 0.18 players hit 70-81%, CV > 0.35 hit 0-29%
    if cv < 0.18:
        score = 4
        reasons.append(f"Very consistent player (CV {cv})")
    elif cv < 0.26:
        score = 3
        reasons.append(f"Consistent player (CV {cv})")
    elif cv < 0.35:
        score = 2
        reasons.append(f"Moderate variance (CV {cv})")
    else:
        score = 1
        reasons.append(f"High variance player (CV {cv}) — hard to project")

    # ── EDGE MAGNITUDE: Modifier, not base ──
    # Data: 1.5-3 pts = 59.5% (sweet spot), 3-5 pts = 47% (suspicious)
    # Edge upgrade ONLY for consistent players (CV < 0.28)
    if 1.5 <= abs_edge <= 3.0 and cv < 0.28:
        score = min(5, score + 1)
        reasons.append(f"Sweet-spot edge ({abs_edge} pts)")
    elif abs_edge > 5.0 and cv < 0.20:
        score = min(5, score + 1)
        reasons.append(f"Large edge on consistent player ({abs_edge} pts)")
    elif 3.0 < abs_edge <= 5.0:
        reasons.append(f"Suspicious edge range ({abs_edge} pts — market may be right)")
        if cv >= 0.30:
            score = max(1, score - 1)
            reasons.append("High CV + large edge = likely mispricing on our side")
    elif abs_edge < 1.0:
        score = max(1, score - 1)
        reasons.append(f"Marginal edge ({abs_edge} pts)")

    # ── PROP TYPE ──
    # Data: points 57.6%, rebounds 40%, assists 45.5%
    if prop_type in ('rebounds', 'assists'):
        score = max(1, score - 1)
        reasons.append(f"Non-points prop ({prop_type}) — historically below breakeven")

    # ── DIRECTION ASYMMETRY ──
    # Data: UNDER hits 59.2%, OVER hits 48.5%
    if direction == 'UNDER':
        reasons.append("UNDER direction (structural edge)")
    elif direction == 'OVER':
        reasons.append("OVER direction (needs extra context support)")

    # ── CONTEXT ALIGNMENT FACTORS ──
    factors_aligned = 0

    if direction == 'OVER' and proj['trend'] == 'up':
        factors_aligned += 1
        reasons.append("Trend supports OVER")
    elif direction == 'UNDER' and proj['trend'] == 'down':
        factors_aligned += 1
        reasons.append("Trend supports UNDER")

    if direction == 'OVER' and adj['pace_factor'] > 1:
        factors_aligned += 1
        reasons.append(f"Pace boost (+{adj['pace_factor']}%)")
    elif direction == 'UNDER' and adj['pace_factor'] < -1:
        factors_aligned += 1
        reasons.append(f"Pace suppression ({adj['pace_factor']}%)")

    if direction == 'OVER' and adj['def_adjustment'] > 1:
        factors_aligned += 1
        reasons.append(f"Weak defense (+{adj['def_adjustment']}%)")
    elif direction == 'UNDER' and adj['def_adjustment'] < -1:
        factors_aligned += 1
        reasons.append(f"Strong defense ({adj['def_adjustment']}%)")

    if proj['std_dev'] > 0 and abs_edge / proj['std_dev'] > 0.75:
        factors_aligned += 1
        reasons.append("Edge exceeds variance")

    if ctx['return_from_absence'] and direction == 'OVER':
        factors_aligned += 1
        reasons.append("Return-from-absence boost")

    # UNDER: 2+ factors → upgrade. OVER: needs 2+ factors AND low CV
    if direction == 'UNDER' and factors_aligned >= 2:
        score = min(5, score + 1)
        reasons.append(f"{factors_aligned} factors aligned (UNDER threshold met)")
    elif direction == 'OVER' and factors_aligned >= 2 and cv < 0.25:
        score = min(5, score + 1)
        reasons.append(f"{factors_aligned} factors + low CV (OVER threshold met)")
    elif direction == 'OVER' and factors_aligned < 1:
        score = max(1, score - 1)
        reasons.append(f"OVER with no context support ({factors_aligned} factors)")

    # ── DOWNGRADE FACTORS ──
    if proj['recency_flag']:
        score = max(1, score - 1)
        reasons.append(f"Recency flag: {proj['recency_flag']} — beware bias")

    if proj['games_played'] < 10:
        score = max(1, score - 1)
        reasons.append(f"Small sample ({proj['games_played']} games)")

    if avg_min > 0 and avg_min < 20:
        score = max(1, score - 1)
        reasons.append(f"Low minutes ({avg_min} avg) — role player risk")

    if min_std > 6:
        score = max(1, score - 1)
        reasons.append(f"Unstable minutes (std_dev {min_std}) — usage unpredictable")

    labels = {1: 'Skip', 2: 'Marginal', 3: 'Lean', 4: 'Strong', 5: 'Lock'}
    final = max(1, min(5, score))

    return {
        'score': final,
        'label': labels[final],
        'reasons': reasons,
        'factors_aligned': factors_aligned,
    }


# ─── Kelly Criterion Sizing ────────────────────────────────────────────────

def kelly_sizing(confidence, bankroll, odds=-110):
    """
    Half-Kelly position sizing based on confidence score.

    Maps confidence to estimated win probability, then calculates
    optimal bet size using Kelly criterion with half-Kelly safety.
    """
    # Confidence → estimated win probability
    # Calibrated from 264-bet backtest (2026-03-21, v2.1 scoring):
    #   Conf 5: 66.7% | Conf 4: 63.0% | Conf 3: 59.5%
    #   Conf 2: 35.6% (correctly identified as "don't bet")
    # Still needs live CLV validation over 500+ real bets
    win_prob_map = {
        5: 0.65,   # very consistent player + sweet-spot edge + context
        4: 0.62,   # consistent player + edge + some context
        3: 0.58,   # consistent player or moderate edge
        2: 0.50,   # marginal — don't bet (breakeven)
        1: 0.45,   # skip — high variance, no reliable edge
    }

    prob = win_prob_map.get(confidence, 0.50)

    # Convert American odds to decimal
    if odds < 0:
        decimal_odds = 1 + (100 / abs(odds))
    else:
        decimal_odds = 1 + (odds / 100)

    # Kelly formula: f* = (bp - q) / b
    b = decimal_odds - 1  # net odds
    p = prob
    q = 1 - p
    kelly = (b * p - q) / b if b > 0 else 0
    half_kelly = max(0, kelly / 2)

    # Cap by confidence level
    max_pct = {5: 0.05, 4: 0.04, 3: 0.03, 2: 0.01, 1: 0}
    capped = min(half_kelly, max_pct.get(confidence, 0))

    return {
        'kelly_full': round(kelly * 100, 2),
        'kelly_half': round(half_kelly * 100, 2),
        'suggested_pct': round(capped * 100, 2),
        'suggested_amount': round(bankroll * capped, 2),
        'estimated_win_prob': prob,
        'note': 'Win probabilities are UNCALIBRATED — need 500+ bets for real calibration'
    }


# ─── Full Analysis ─────────────────────────────────────────────────────────

def analyze_prop(player_name, prop_type, opponent_name, line, bankroll=100):
    """
    Run complete edge analysis for a single player prop.

    Returns a comprehensive dict with projection, edge, confidence, and sizing.
    """
    # Build matchup context (calls nba_stats.py under the hood)
    ctx = build_matchup_context(player_name, opponent_name, prop_type)
    if 'error' in ctx:
        return ctx

    # Use matchup-adjusted projection for edge calculation
    adjusted_projection = ctx['projection']['matchup_adjusted']

    # Calculate edge
    edge = calculate_edge(adjusted_projection, line)

    # Score confidence (v2.1: prop_type affects scoring)
    confidence = score_confidence(edge, ctx, prop_type)

    # Kelly sizing
    sizing = kelly_sizing(confidence['score'], bankroll)

    return {
        'player': ctx['player']['name'],
        'prop': prop_type,
        'opponent': ctx['opponent']['name'],
        'line': line,
        'projection': {
            'raw': ctx['projection']['raw'],
            'pace_adjusted': ctx['projection']['pace_adjusted'],
            'matchup_adjusted': adjusted_projection,
            'season_avg': ctx['projection']['season_avg'],
            'last_10_avg': ctx['projection']['last_10_avg'],
            'last_3_avg': ctx['projection']['last_3_avg'],
        },
        'edge': edge,
        'confidence': confidence,
        'sizing': sizing,
        'context': {
            'pace_factor': ctx['adjustments']['pace_factor'],
            'def_adjustment': ctx['adjustments']['def_adjustment'],
            'trend': ctx['projection']['trend'],
            'std_dev': ctx['projection']['std_dev'],
            'recency_flag': ctx['projection']['recency_flag'],
            'return_from_absence': ctx['context']['return_from_absence'],
            'games_played': ctx['projection']['games_played'],
            'avg_minutes': ctx['projection'].get('avg_minutes', 0),
            'minutes_std_dev': ctx['projection'].get('minutes_std_dev', 0),
            'coefficient_of_variation': ctx['projection'].get('coefficient_of_variation', 0),
        },
        'last_10_values': ctx.get('last_10_values', []),
    }


# ─── CLI ────────────────────────────────────────────────────────────────────

def cmd_analyze(args):
    """Analyze a single player prop."""
    result = analyze_prop(
        args.player, args.prop, args.opponent,
        args.line, args.bankroll
    )

    if 'error' in result:
        print(f"Error: {result['error']}")
        sys.exit(1)

    p = result['projection']
    e = result['edge']
    c = result['confidence']
    s = result['sizing']
    ctx = result['context']

    print(f"\n{'='*65}")
    print(f"  EDGE ANALYSIS: {result['player']} {result['prop'].upper()}")
    print(f"  vs {result['opponent']}  |  Line: {result['line']}")
    print(f"{'='*65}")

    print(f"\n  Projection")
    print(f"  {'─'*50}")
    print(f"  Raw (60/25/15):       {p['raw']}")
    print(f"  Pace Adjusted:        {p['pace_adjusted']}  ({ctx['pace_factor']:+.1f}%)")
    print(f"  Matchup Adjusted:     {p['matchup_adjusted']}  ({ctx['def_adjustment']:+.1f}% def)")
    print(f"  Season Avg:           {p['season_avg']}")
    print(f"  Last 10 Avg:          {p['last_10_avg']}")
    print(f"  Last 3 Avg:           {p['last_3_avg']}")

    print(f"\n  Edge Detection")
    print(f"  {'─'*50}")
    direction_icon = 'OVER' if e['direction'] == 'OVER' else 'UNDER' if e['direction'] == 'UNDER' else 'SKIP'
    print(f"  Direction:            {direction_icon}")
    print(f"  Edge:                 {e['edge']:+.1f} pts ({e['edge_pct']:+.1f}%)")
    print(f"  Magnitude:            {e['magnitude'].upper()}")

    print(f"\n  Confidence: {c['score']}/5 ({c['label']})")
    print(f"  {'─'*50}")
    print(f"  Factors aligned:      {c['factors_aligned']}")
    for reason in c['reasons']:
        print(f"    - {reason}")

    print(f"\n  Sizing (Half-Kelly)")
    print(f"  {'─'*50}")
    print(f"  Suggested:            {s['suggested_pct']}% of bankroll")
    print(f"  Amount:               ${s['suggested_amount']:.2f}")
    print(f"  Est. Win Prob:        {s['estimated_win_prob']*100:.0f}%")
    print(f"  {s['note']}")

    if ctx['recency_flag']:
        print(f"\n  RECENCY WARNING: {ctx['recency_flag']}")
    if ctx['return_from_absence']:
        print(f"\n  RETURN FROM ABSENCE — consider boosting projection")

    print(f"\n  Last 10 values: {result['last_10_values']}")
    print(f"\n  Std Dev: {ctx['std_dev']}  |  Trend: {ctx['trend']}  |  GP: {ctx['games_played']}")
    print()

    # JSON output for programmatic use
    if args.json:
        print(json.dumps(result, indent=2))


def cmd_batch(args):
    """Analyze multiple props from a JSON file."""
    with open(args.file, 'r') as f:
        players = json.load(f)

    results = []
    for entry in players:
        result = analyze_prop(
            entry['player'], entry['prop'], entry['opponent'],
            entry['line'], args.bankroll
        )
        results.append(result)

    # Summary table
    print(f"\n{'='*95}")
    print(f"  BATCH ANALYSIS — {len(results)} Props")
    print(f"{'='*95}")
    print(f"  {'Player':<22} {'Prop':<8} {'Line':>5} {'Proj':>5} {'Edge':>6} {'Dir':<6} {'Conf':<8} {'Size':>6}")
    print(f"  {'─'*90}")

    for r in results:
        if 'error' in r:
            print(f"  {r.get('player', '?'):<22} ERROR: {r['error']}")
            continue
        print(f"  {r['player']:<22} {r['prop']:<8} {r['line']:>5.1f} "
              f"{r['projection']['matchup_adjusted']:>5.1f} "
              f"{r['edge']['edge']:>+5.1f}  {r['edge']['direction']:<6} "
              f"{r['confidence']['score']}/5 {r['confidence']['label']:<8} "
              f"${r['sizing']['suggested_amount']:>5.2f}")

    # Anti-bias check
    directions = [r['edge']['direction'] for r in results if 'error' not in r and r['edge']['direction'] != 'SKIP']
    if directions:
        over_pct = directions.count('OVER') / len(directions) * 100
        under_pct = directions.count('UNDER') / len(directions) * 100
        print(f"\n  Direction balance: {over_pct:.0f}% OVER / {under_pct:.0f}% UNDER")
        if over_pct >= 70 or under_pct >= 70:
            print(f"  BIAS WARNING: {max(over_pct, under_pct):.0f}% picks lean one direction.")
            print(f"  Re-run Three-Lens Test on every pick before finalizing.")

    # Total exposure
    total_exposure = sum(r['sizing']['suggested_pct'] for r in results if 'error' not in r)
    total_amount = sum(r['sizing']['suggested_amount'] for r in results if 'error' not in r)
    print(f"\n  Total exposure: {total_exposure:.1f}% of bankroll (${total_amount:.2f})")
    if total_exposure > 15:
        print(f"  EXPOSURE WARNING: Over 15% daily limit. Reduce position sizes or drop lowest conviction picks.")

    print()

    if args.json:
        print(json.dumps(results, indent=2))


def main():
    parser = argparse.ArgumentParser(description='NBA Projection Engine — Edge detection with real data')
    sub = parser.add_subparsers(dest='command')

    # analyze
    p_analyze = sub.add_parser('analyze', help='Analyze a single player prop')
    p_analyze.add_argument('player', help='Player name')
    p_analyze.add_argument('prop', help='Prop type (points, rebounds, assists, threes, steals, blocks)')
    p_analyze.add_argument('opponent', help='Opponent team name')
    p_analyze.add_argument('--line', type=float, required=True, help='Posted line')
    p_analyze.add_argument('--bankroll', type=float, default=100, help='Current bankroll (default: 100)')
    p_analyze.add_argument('--json', action='store_true', help='Output JSON for programmatic use')

    # batch
    p_batch = sub.add_parser('batch', help='Analyze multiple props from JSON file')
    p_batch.add_argument('file', help='JSON file with player props')
    p_batch.add_argument('--bankroll', type=float, default=100, help='Current bankroll')
    p_batch.add_argument('--json', action='store_true', help='Output JSON')

    args = parser.parse_args()

    if args.command == 'analyze':
        cmd_analyze(args)
    elif args.command == 'batch':
        cmd_batch(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
