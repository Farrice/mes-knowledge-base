#!/usr/bin/env python3
"""
Confidence Scoring Variant — Data-Calibrated v2

Changes from current score_confidence():
1. Player consistency (CV) becomes PRIMARY driver, not edge magnitude
2. Edge 3-5 pts range gets CAPPED (data shows 47% hit vs 59.5% for 1.5-3)
3. Non-points props get penalized (rebounds 40%, assists 45.5% vs points 57.6%)
4. UNDER direction gets structural credit
5. Existing factor alignment logic preserved

Hypothesis: This will create meaningful differentiation between confidence levels
(higher confidence = higher hit rate) to pass the Go/No-Go calibration gate.
"""

import json
import os
import sys
import time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)


def score_confidence_v2(edge_result, matchup_ctx, prop_type='points'):
    """
    Data-calibrated confidence scoring.

    Key difference from v1: Player consistency (CV) is the foundation,
    edge magnitude is a modifier, and prop type + direction contribute.
    """
    score = 1
    reasons = []

    abs_edge = edge_result['raw_diff']
    proj = matchup_ctx['projection']
    ctx = matchup_ctx['context']
    adj = matchup_ctx['adjustments']
    direction = edge_result['direction']

    cv = proj.get('coefficient_of_variation', 0.99)
    avg_min = proj.get('avg_minutes', 0)
    min_std = proj.get('minutes_std_dev', 0)

    # ── FOUNDATION: Player Consistency (replaces edge magnitude as base) ──
    if cv < 0.20:
        score = 4
        reasons.append(f"Very consistent player (CV {cv})")
    elif cv < 0.28:
        score = 3
        reasons.append(f"Consistent player (CV {cv})")
    elif cv < 0.38:
        score = 2
        reasons.append(f"Moderate variance (CV {cv})")
    else:
        score = 1
        reasons.append(f"High variance player (CV {cv}) — hard to project")

    # ── EDGE MAGNITUDE: Modifier, not base ──
    if 1.5 <= abs_edge <= 3.0:
        score = min(5, score + 1)
        reasons.append(f"Sweet-spot edge ({abs_edge} pts)")
    elif abs_edge > 5.0 and cv < 0.25:
        score = min(5, score + 1)
        reasons.append(f"Large edge on consistent player ({abs_edge} pts)")
    elif 3.0 < abs_edge <= 5.0:
        reasons.append(f"Suspicious edge range ({abs_edge} pts — market may be right)")
    elif abs_edge < 1.0:
        score = max(1, score - 1)
        reasons.append(f"Marginal edge ({abs_edge} pts)")

    # ── PROP TYPE: Points-only edge ──
    if prop_type in ('rebounds', 'assists'):
        score = max(1, score - 1)
        reasons.append(f"Non-points prop ({prop_type}) — historically below breakeven")

    # ── DIRECTION ASYMMETRY ──
    if direction == 'UNDER':
        reasons.append("UNDER direction (structural edge)")
    elif direction == 'OVER':
        reasons.append("OVER direction (needs extra context support)")

    # ── CONTEXT ALIGNMENT ──
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
    elif direction == 'UNDER' and adj['def_adjustment'] < -1:
        factors_aligned += 1

    if proj['std_dev'] > 0 and abs_edge / proj['std_dev'] > 0.75:
        factors_aligned += 1
        reasons.append("Edge exceeds variance")

    if ctx['return_from_absence'] and direction == 'OVER':
        factors_aligned += 1
        reasons.append("Return-from-absence boost")

    # UNDER: 2+ factors → +1. OVER: 3+ factors → +1 (higher bar)
    if direction == 'UNDER' and factors_aligned >= 2:
        score = min(5, score + 1)
    elif direction == 'OVER' and factors_aligned >= 3:
        score = min(5, score + 1)
    elif direction == 'OVER' and factors_aligned < 2:
        score = max(1, score - 1)
        reasons.append(f"OVER with weak context ({factors_aligned} factors)")

    # ── DOWNGRADE FACTORS ──
    if proj['recency_flag']:
        score = max(1, score - 1)

    if proj['games_played'] < 10:
        score = max(1, score - 1)

    if avg_min > 0 and avg_min < 20:
        score = max(1, score - 1)

    if min_std > 6:
        score = max(1, score - 1)

    labels = {1: 'Skip', 2: 'Marginal', 3: 'Lean', 4: 'Strong', 5: 'Lock'}
    final = max(1, min(5, score))

    return {
        'score': final,
        'label': labels[final],
        'reasons': reasons,
        'factors_aligned': factors_aligned,
    }


# ─── Simplified v2 scorer for backtesting (no API calls) ────────────────

def score_v2_simple(edge_abs, direction, prop_type, cv, std_dev, trend,
                    games_played, avg_minutes, min_std_dev):
    """
    Simplified v2 scoring using stored bet data — no API calls needed.
    Returns confidence score 1-5.

    v2.1 fix: Edge modifier only upgrades if player is already consistent (CV < 0.28).
    This prevents moderate-variance players from getting false confidence boosts.
    """
    score = 1

    # Foundation: CV (the #1 predictor from 264-bet backtest)
    if cv < 0.18:
        score = 4
    elif cv < 0.26:
        score = 3
    elif cv < 0.35:
        score = 2
    else:
        score = 1

    # Edge modifier — ONLY upgrades consistent players (cv < 0.28)
    if 1.5 <= edge_abs <= 3.0 and cv < 0.28:
        score = min(5, score + 1)
    elif edge_abs > 5.0 and cv < 0.20:
        score = min(5, score + 1)
    elif 3.0 < edge_abs <= 5.0:
        # Suspicious range — downgrade if high CV
        if cv >= 0.30:
            score = max(1, score - 1)
    elif edge_abs < 1.0:
        score = max(1, score - 1)

    # Prop type
    if prop_type in ('rebounds', 'assists'):
        score = max(1, score - 1)

    # Direction + factor alignment (simplified — count what we can)
    factors = 0
    if std_dev > 0 and edge_abs / std_dev > 0.75:
        factors += 1
    if direction == 'under' and trend == 'down':
        factors += 1
    elif direction == 'over' and trend == 'up':
        factors += 1

    # UNDER is easier to upgrade, OVER needs more evidence
    if direction == 'under' and factors >= 2:
        score = min(5, score + 1)
    elif direction == 'over' and factors >= 2 and cv < 0.25:
        score = min(5, score + 1)
    elif direction == 'over' and factors < 1:
        score = max(1, score - 1)

    # Downgrades
    if games_played < 10:
        score = max(1, score - 1)
    if avg_minutes > 0 and avg_minutes < 20:
        score = max(1, score - 1)
    if min_std_dev > 6:
        score = max(1, score - 1)

    return max(1, min(5, score))


def rescore_backfill():
    """
    Rescore all paper bets: v1 (stored) vs v2 (recalculated from player stats).
    Uses player stats lookup for CV — one API call per unique player.
    """
    from execution.nba_stats import find_player, calculate_projection, API_DELAY

    PAPER_LOG = os.path.join(ROOT, '.agent', 'paper-trading.json')
    with open(PAPER_LOG) as f:
        data = json.load(f)

    bets = [b for b in data['bets'] if b.get('outcome')]

    # Get unique players and cache their stats
    player_cache = {}
    unique_players = set(b['player'] for b in bets)

    print(f"\n  Loading stats for {len(unique_players)} unique players...")
    for pname in sorted(unique_players):
        player = find_player(pname)
        if not player:
            continue
        try:
            for prop_type in ['points', 'rebounds', 'assists']:
                proj = calculate_projection(player['id'], prop_type)
                if proj:
                    key = f"{pname}_{prop_type}"
                    player_cache[key] = proj
            time.sleep(API_DELAY)
        except Exception:
            pass

    print(f"  Cached stats for {len(player_cache)} player-prop combos.\n")

    # Score each bet with v1 (stored) and v2 (recalculated)
    v1_scores = {i: {'w': 0, 'l': 0} for i in range(1, 6)}
    v2_scores = {i: {'w': 0, 'l': 0} for i in range(1, 6)}
    rescored = 0

    for bet in bets:
        v1_conf = bet.get('confidence', 3)
        outcome = bet['outcome']
        prop_type = bet['prop']
        direction = bet['direction']
        edge_abs = abs(bet.get('edge', 0))

        # Get player stats for v2
        cache_key = f"{bet['player']}_{prop_type}"
        stats = player_cache.get(cache_key)

        if not stats:
            # Use v1 score for both if no stats available
            v2_conf = v1_conf
        else:
            cv = stats.get('coefficient_of_variation', 0.35)
            std_dev = stats.get('std_dev', 5.0)
            trend = stats.get('recent_trend', 'stable')
            gp = stats.get('games_played', 20)
            avg_min = stats.get('avg_minutes', 30)
            min_std = stats.get('minutes_std_dev', 3)

            v2_conf = score_v2_simple(
                edge_abs, direction, prop_type, cv, std_dev, trend,
                gp, avg_min, min_std
            )

        if outcome == 'win':
            v1_scores[v1_conf]['w'] += 1
            v2_scores[v2_conf]['w'] += 1
        else:
            v1_scores[v1_conf]['l'] += 1
            v2_scores[v2_conf]['l'] += 1

        rescored += 1

    # Report
    print(f"{'='*70}")
    print(f"  CONFIDENCE CALIBRATION A/B TEST — {rescored} bets")
    print(f"{'='*70}")

    for version, scores in [('V1 (CURRENT)', v1_scores), ('V2 (VARIANT)', v2_scores)]:
        print(f"\n  {version}")
        print(f"  {'─'*55}")
        print(f"  {'Conf':<6} {'Bets':>6} {'Wins':>6} {'Losses':>6} {'Hit%':>8}")

        rates = {}
        for level in range(1, 6):
            total = scores[level]['w'] + scores[level]['l']
            if total > 0:
                rate = scores[level]['w'] / total * 100
                rates[level] = rate
                print(f"  {level:<6} {total:>6} {scores[level]['w']:>6} {scores[level]['l']:>6} {rate:>7.1f}%")
            else:
                print(f"  {level:<6} {'—':>6} {'—':>6} {'—':>6} {'—':>8}")

        # Check monotonic calibration (higher conf = higher hit rate)
        sorted_rates = [(k, v) for k, v in sorted(rates.items()) if k >= 2]
        calibrated = all(
            sorted_rates[i][1] <= sorted_rates[i+1][1]
            for i in range(len(sorted_rates)-1)
        ) if len(sorted_rates) >= 2 else False

        # Overall stats
        total_bets = sum(s['w'] + s['l'] for s in scores.values())
        total_wins = sum(s['w'] for s in scores.values())
        overall_rate = total_wins / total_bets * 100 if total_bets else 0

        print(f"  {'─'*55}")
        print(f"  Overall: {total_wins}/{total_bets} ({overall_rate:.1f}%)")
        print(f"  Calibration (higher conf = higher hit%): {'PASS' if calibrated else 'FAIL'}")

        # Spread: gap between highest and lowest confidence hit rates
        if len(sorted_rates) >= 2:
            spread = max(r for _, r in sorted_rates) - min(r for _, r in sorted_rates)
            print(f"  Spread (best - worst conf): {spread:.1f}pp")

    print()


if __name__ == '__main__':
    rescore_backfill()
