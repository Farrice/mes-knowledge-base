#!/usr/bin/env python3
"""
NBA Live Trader — Conservative live deployment with real money guardrails.

Phase 3 of the betting system upgrade. Only activates after Phase 2
paper trading validates the system (200+ paper bets, positive CLV,
hit rate > 53%). Enforces tighter limits than paper trading.

Usage:
    python execution/live_trader.py check                     # Go/No-Go gate check
    python execution/live_trader.py slate --bankroll 500      # Generate live picks (with gate)
    python execution/live_trader.py slate --bankroll 500 --override  # Skip gate (use carefully)
    python execution/live_trader.py weekly                    # Weekly performance review
    python execution/live_trader.py milestone                 # 500-bet milestone tracker
"""

import argparse
import json
import os
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, ROOT)

from execution.odds_fetcher import api_request, SPORT, PROP_MARKETS, REGIONS, ODDS_FORMAT
from execution.nba_stats import find_player
from execution.projection_engine import analyze_prop

PAPER_LOG = os.path.join(ROOT, '.agent', 'paper-trading.json')
LIVE_LOG = os.path.join(ROOT, '.agent', 'live-trading.json')

# Phase 3 Conservative Limits
LIMITS = {
    'max_single_bet_pct': 2.0,       # 2% max per bet (was 5% in paper)
    'max_daily_exposure_pct': 8.0,    # 8% max daily (was 15% in paper)
    'max_parlay_pct': 1.5,            # 1.5% max per parlay
    'min_confidence': 3,              # Only confidence 3+ bets
    'min_edge_pts': 1.5,              # Minimum 1.5 pts edge (was 1.0)
    'max_picks_per_day': 5,           # Cap at 5 picks
    'milestone_target': 500,          # Bets needed for full validation
}


def load_paper_data():
    """Load paper trading data for gate check."""
    if not os.path.exists(PAPER_LOG):
        return None
    with open(PAPER_LOG, 'r') as f:
        return json.load(f)


def load_live_data():
    """Load or initialize live trading data."""
    if os.path.exists(LIVE_LOG):
        with open(LIVE_LOG, 'r') as f:
            return json.load(f)
    return {
        'started': None,
        'bankroll': {'initial': 0, 'current': 0},
        'bets': [],
        'weekly_reviews': [],
        'gate_status': 'LOCKED',
    }


def save_live_data(data):
    """Save live trading data."""
    os.makedirs(os.path.dirname(LIVE_LOG), exist_ok=True)
    with open(LIVE_LOG, 'w') as f:
        json.dump(data, f, indent=2)


# ─── Go/No-Go Gate ─────────────────────────────────────────────────────────

def check_gate():
    """
    Check if Phase 2 paper trading results meet Go/No-Go criteria.

    Requirements:
    1. 200+ settled paper bets
    2. Hit rate > 53% on -110 lines
    3. Positive average CLV
    4. Confidence calibration (higher confidence = higher hit rate)

    Returns (passed: bool, report: dict)
    """
    paper = load_paper_data()
    if paper is None:
        return False, {'error': 'No paper trading data found. Run Phase 2 first.'}

    bets = paper.get('bets', [])
    settled = [b for b in bets if b.get('outcome') is not None]

    report = {
        'total_paper_bets': len(bets),
        'settled': len(settled),
        'required': 200,
        'criteria': {},
    }

    # Criterion 1: 200+ settled bets
    enough = len(settled) >= 200
    report['criteria']['bet_count'] = {
        'status': 'PASS' if enough else 'FAIL',
        'value': len(settled),
        'required': 200,
    }

    if not settled:
        return False, report

    # Criterion 2: Hit rate > 53%
    wins = [b for b in settled if b['outcome'] == 'win']
    hit_rate = len(wins) / len(settled) * 100
    beating = hit_rate > 53
    report['criteria']['hit_rate'] = {
        'status': 'PASS' if beating else 'FAIL',
        'value': round(hit_rate, 1),
        'required': 53.0,
    }

    # Criterion 3: Positive CLV
    clv_bets = [b for b in settled if b.get('clv') is not None]
    if clv_bets:
        avg_clv = sum(b['clv'] for b in clv_bets) / len(clv_bets)
        positive = avg_clv > 0
    else:
        avg_clv = 0
        positive = False
    report['criteria']['clv'] = {
        'status': 'PASS' if positive else ('PENDING' if not clv_bets else 'FAIL'),
        'value': round(avg_clv, 1),
        'data_points': len(clv_bets),
        'required': 'positive',
    }

    # Criterion 4: Confidence calibration
    calibrated = True
    conf_rates = {}
    for level in range(2, 6):
        level_bets = [b for b in settled if b.get('confidence') == level]
        if level_bets:
            conf_rates[level] = len([b for b in level_bets if b['outcome'] == 'win']) / len(level_bets) * 100
        else:
            conf_rates[level] = None

    # Check that higher confidence levels have higher hit rates
    prev_rate = 0
    for level in range(2, 6):
        if conf_rates[level] is not None:
            if conf_rates[level] < prev_rate and prev_rate > 0:
                calibrated = False
            prev_rate = conf_rates[level]

    report['criteria']['calibration'] = {
        'status': 'PASS' if calibrated else 'FAIL',
        'rates': conf_rates,
    }

    passed = enough and beating and positive and calibrated
    report['overall'] = 'GO' if passed else 'NO-GO'

    return passed, report


def fetch_todays_games():
    """Get tonight's games."""
    events, remaining, used = api_request(f'/sports/{SPORT}/events')
    now = datetime.now(timezone.utc)
    today = []
    for event in events:
        commence = datetime.fromisoformat(event['commence_time'].replace('Z', '+00:00'))
        diff = (commence - now).total_seconds()
        if -3600 <= diff <= 86400:
            today.append(event)
    return today, remaining, used


def fetch_props_for_game(event_id):
    """Fetch player props for a game."""
    props = {}
    market_to_prop = {
        'player_points': 'points',
        'player_rebounds': 'rebounds',
        'player_assists': 'assists',
        'player_threes': 'threes',
    }

    for market in PROP_MARKETS:
        data, _, _ = api_request(
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
                    direction = outcome.get('name', '')
                    line = outcome.get('point', 0)
                    price = outcome.get('price', 0)
                    prop_type = market_to_prop.get(market, market)

                    if player_name not in props:
                        props[player_name] = {'game_info': game_info}
                    if prop_type not in props[player_name]:
                        props[player_name][prop_type] = {
                            'line': line, 'best_over_odds': -110,
                            'best_under_odds': -110, 'books': [],
                        }
                    if direction == 'Over' and price > props[player_name][prop_type]['best_over_odds']:
                        props[player_name][prop_type]['best_over_odds'] = price
                    if direction == 'Under' and price > props[player_name][prop_type]['best_under_odds']:
                        props[player_name][prop_type]['best_under_odds'] = price
                    props[player_name][prop_type]['line'] = line
                    if book['title'] not in props[player_name][prop_type]['books']:
                        props[player_name][prop_type]['books'].append(book['title'])

    return props


# ─── CLI Commands ───────────────────────────────────────────────────────────

def cmd_check(args):
    """Run Go/No-Go gate check."""
    passed, report = check_gate()

    print(f"\n{'='*60}")
    print(f"  PHASE 3 GO/NO-GO GATE CHECK")
    print(f"{'='*60}")

    if 'error' in report:
        print(f"\n  {report['error']}")
        print()
        return

    print(f"\n  Paper Trading: {report['settled']}/{report['required']} settled bets")
    print(f"  {'─'*55}")

    for name, criteria in report['criteria'].items():
        status = criteria['status']
        icon = 'PASS' if status == 'PASS' else 'FAIL' if status == 'FAIL' else 'PENDING'
        if name == 'bet_count':
            print(f"  {icon}  Bet count:       {criteria['value']}/{criteria['required']}")
        elif name == 'hit_rate':
            print(f"  {icon}  Hit rate:        {criteria['value']}% (need > {criteria['required']}%)")
        elif name == 'clv':
            print(f"  {icon}  Avg CLV:         {criteria['value']:+.1f} pts ({criteria['data_points']} data points)")
        elif name == 'calibration':
            rates = criteria.get('rates', {})
            rates_str = ', '.join(f"C{k}={v:.0f}%" for k, v in rates.items() if v is not None)
            print(f"  {icon}  Calibration:     {rates_str}")

    print(f"\n  {'='*55}")
    if passed:
        print(f"  VERDICT: GO — System validated. Ready for live deployment.")
        print(f"\n  Conservative limits for Phase 3:")
        print(f"    Max single bet:    {LIMITS['max_single_bet_pct']}% of bankroll")
        print(f"    Max daily exposure: {LIMITS['max_daily_exposure_pct']}%")
        print(f"    Min confidence:     {LIMITS['min_confidence']}/5")
        print(f"    Min edge:           {LIMITS['min_edge_pts']} pts")
        print(f"    Max picks/day:      {LIMITS['max_picks_per_day']}")
    else:
        remaining = max(0, 200 - report.get('settled', 0))
        print(f"  VERDICT: NO-GO — Continue paper trading.")
        if remaining > 0:
            print(f"  Need {remaining} more paper bets (~{remaining // 5} days at 5/day)")
    print()


def cmd_slate(args):
    """Generate live picks with conservative guardrails."""
    # Gate check (unless overridden)
    if not args.override:
        passed, report = check_gate()
        if not passed:
            print(f"\n  GATE BLOCKED: Phase 2 paper trading not yet validated.")
            print(f"  Run 'python execution/live_trader.py check' for details.")
            print(f"  Use --override to skip gate (not recommended).")
            return

    bankroll = args.bankroll
    data = load_live_data()

    if data['started'] is None:
        data['started'] = datetime.now().strftime('%Y-%m-%d')
        data['bankroll'] = {'initial': bankroll, 'current': bankroll}

    # Check today's existing exposure
    date_str = datetime.now().strftime('%Y-%m-%d')
    today_bets = [b for b in data['bets'] if b['date'] == date_str]
    today_exposure = sum(b['stake'] for b in today_bets)
    today_exposure_pct = (today_exposure / bankroll * 100) if bankroll > 0 else 0

    if today_exposure_pct >= LIMITS['max_daily_exposure_pct']:
        print(f"\n  DAILY LIMIT REACHED: {today_exposure_pct:.1f}% exposure today.")
        print(f"  Max allowed: {LIMITS['max_daily_exposure_pct']}%")
        return

    if len(today_bets) >= LIMITS['max_picks_per_day']:
        print(f"\n  PICK LIMIT REACHED: {len(today_bets)} picks today (max {LIMITS['max_picks_per_day']}).")
        return

    remaining_exposure = LIMITS['max_daily_exposure_pct'] - today_exposure_pct
    remaining_picks = LIMITS['max_picks_per_day'] - len(today_bets)

    print(f"\n{'='*80}")
    print(f"  LIVE TRADING SLATE — {datetime.now().strftime('%B %d, %Y')}")
    print(f"  Bankroll: ${bankroll:.2f}  |  Today: {today_exposure_pct:.1f}% used  |  {remaining_picks} picks left")
    print(f"{'='*80}")

    # Fetch games
    games, api_remaining, api_used = fetch_todays_games()
    if not games:
        print("  No games in next 24 hours.")
        return

    if args.game:
        games = [g for g in games if g['id'] == args.game]

    print(f"  {len(games)} games  |  API: {api_used} used / {api_remaining} remaining")

    all_picks = []

    for game in games:
        away = game['away_team']
        home = game['home_team']

        print(f"\n  Analyzing: {away} @ {home}...")
        props = fetch_props_for_game(game['id'])
        if not props:
            continue

        for player_name, player_props in props.items():
            game_info = player_props.get('game_info', {})
            for prop_type, prop_data in player_props.items():
                if prop_type == 'game_info':
                    continue

                line = prop_data['line']
                result = None
                for opponent in [away, home]:
                    try:
                        r = analyze_prop(player_name, prop_type, opponent, line, bankroll)
                        if 'error' not in r:
                            result = r
                            break
                    except Exception:
                        continue

                if result is None:
                    continue

                # Apply Phase 3 filters
                conf = result['confidence']['score']
                edge = abs(result['edge']['edge'])

                if conf < LIMITS['min_confidence']:
                    continue
                if edge < LIMITS['min_edge_pts']:
                    continue

                # Cap sizing at conservative limit
                max_stake = bankroll * LIMITS['max_single_bet_pct'] / 100
                suggested = min(result['sizing']['suggested_amount'], max_stake)

                pick = {
                    'player': result['player'],
                    'prop': prop_type,
                    'line': line,
                    'projection': result['projection']['matchup_adjusted'],
                    'edge': result['edge'],
                    'confidence': result['confidence'],
                    'stake': round(suggested, 2),
                    'best_odds': (prop_data['best_over_odds']
                                  if result['edge']['direction'] == 'OVER'
                                  else prop_data['best_under_odds']),
                    'game': f"{away} @ {home}",
                    'event_id': game['id'],
                }
                all_picks.append(pick)

    # Sort by confidence × edge
    all_picks.sort(key=lambda x: (x['confidence']['score'], abs(x['edge']['edge'])), reverse=True)

    # Enforce daily limits
    final_picks = []
    exposure = today_exposure_pct
    for pick in all_picks:
        if len(final_picks) >= remaining_picks:
            break
        pick_pct = pick['stake'] / bankroll * 100
        if exposure + pick_pct > LIMITS['max_daily_exposure_pct']:
            continue
        exposure += pick_pct
        final_picks.append(pick)

    # Anti-bias check
    if final_picks:
        dirs = [p['edge']['direction'] for p in final_picks]
        over_pct = dirs.count('OVER') / len(dirs) * 100
        bias = over_pct >= 70 or (100 - over_pct) >= 70
    else:
        bias = False

    # Output
    if not final_picks:
        print(f"\n  No picks met Phase 3 criteria tonight (conf >= {LIMITS['min_confidence']}, edge >= {LIMITS['min_edge_pts']} pts).")
        return

    print(f"\n{'='*80}")
    print(f"  LIVE PICKS — {len(final_picks)} bets  |  Conservative Mode")
    print(f"{'='*80}")
    print(f"  {'Player':<22} {'Prop':<8} {'Line':>5} {'Proj':>5} {'Edge':>6} {'Dir':<6} {'Conf':<5} {'Stake':>8}")
    print(f"  {'─'*75}")

    total_stake = 0
    for p in final_picks:
        total_stake += p['stake']
        print(f"  {p['player']:<22} {p['prop']:<8} {p['line']:>5.1f} "
              f"{p['projection']:>5.1f} {p['edge']['edge']:>+5.1f}  "
              f"{p['edge']['direction']:<6} {p['confidence']['score']}/5   "
              f"${p['stake']:>7.2f}")

    total_pct = (today_exposure + total_stake) / bankroll * 100
    print(f"  {'─'*75}")
    print(f"  New exposure: ${total_stake:.2f} ({total_stake/bankroll*100:.1f}%)")
    print(f"  Total daily:  ${today_exposure + total_stake:.2f} ({total_pct:.1f}%)")

    if bias:
        print(f"  BIAS WARNING: {max(over_pct, 100-over_pct):.0f}% one direction — consider Three-Lens review")

    # Log picks
    for p in final_picks:
        bet_id = f"live-{date_str}-{len(data['bets']) + 1:03d}"
        bet = {
            'id': bet_id,
            'date': date_str,
            'type': 'live',
            'player': p['player'],
            'prop': p['prop'],
            'line': p['line'],
            'direction': p['edge']['direction'].lower(),
            'projection': p['projection'],
            'edge': p['edge']['edge'],
            'confidence': p['confidence']['score'],
            'stake': p['stake'],
            'odds': p['best_odds'],
            'game': p['game'],
            'event_id': p['event_id'],
            'actual': None,
            'outcome': None,
            'payout': None,
            'closing_line': None,
            'clv': None,
        }
        data['bets'].append(bet)

    save_live_data(data)
    print(f"\n  {len(final_picks)} live bets logged.")
    print(f"  REMINDER: Record closing lines at game time for CLV tracking.")
    print(f"  REMINDER: Enter results tomorrow via 'python execution/live_trader.py result <id> <actual>'")
    print()


def cmd_result(args):
    """Record a live bet result."""
    data = load_live_data()
    bet = next((b for b in data['bets'] if b['id'] == args.bet_id), None)
    if not bet:
        print(f"Error: Bet ID '{args.bet_id}' not found.")
        sys.exit(1)

    if bet['outcome'] is not None:
        print(f"Error: Bet already settled: {bet['outcome']}")
        return

    actual = args.actual
    bet['actual'] = actual

    if bet['direction'] == 'over':
        bet['outcome'] = 'win' if actual > bet['line'] else 'loss'
    else:
        bet['outcome'] = 'win' if actual < bet['line'] else 'loss'

    if args.closing_line is not None:
        bet['closing_line'] = args.closing_line
        if bet['direction'] == 'over':
            bet['clv'] = round(bet['closing_line'] - bet['line'], 1)
        else:
            bet['clv'] = round(bet['line'] - bet['closing_line'], 1)

    stake = bet['stake']
    if bet['outcome'] == 'win':
        odds = bet.get('odds', -110)
        payout = stake * (100 / abs(odds)) if odds < 0 else stake * (odds / 100)
        bet['payout'] = round(payout, 2)
        data['bankroll']['current'] = round(data['bankroll']['current'] + payout, 2)
    else:
        bet['payout'] = 0
        data['bankroll']['current'] = round(data['bankroll']['current'] - stake, 2)

    save_live_data(data)

    icon = 'WIN' if bet['outcome'] == 'win' else 'LOSS'
    profit = f"+${bet['payout']:.2f}" if bet['outcome'] == 'win' else f"-${stake:.2f}"
    print(f"  {icon}: {bet['player']} {bet['prop']} {bet['direction'].upper()} {bet['line']}")
    print(f"  Actual: {actual}  |  {profit}  |  Bankroll: ${data['bankroll']['current']:.2f}")
    if bet.get('clv') is not None:
        print(f"  CLV: {bet['clv']:+.1f} pts")


def cmd_weekly(args):
    """Weekly performance review."""
    data = load_live_data()
    bets = data['bets']
    settled = [b for b in bets if b['outcome'] is not None]

    if not settled:
        print("\nNo settled live bets yet.")
        return

    # Group by week
    from collections import defaultdict
    weeks = defaultdict(list)
    for b in settled:
        # ISO week
        dt = datetime.strptime(b['date'], '%Y-%m-%d')
        week_key = f"{dt.isocalendar()[0]}-W{dt.isocalendar()[1]:02d}"
        weeks[week_key].append(b)

    print(f"\n{'='*70}")
    print(f"  WEEKLY PERFORMANCE REVIEW")
    print(f"{'='*70}")
    print(f"  {'Week':<12} {'Bets':>5} {'Wins':>5} {'Hit%':>7} {'P/L':>10} {'ROI':>7} {'CLV':>7}")
    print(f"  {'─'*65}")

    for week in sorted(weeks.keys()):
        wb = weeks[week]
        wins = [b for b in wb if b['outcome'] == 'win']
        total_stake = sum(b['stake'] for b in wb)
        total_payout = sum(b.get('payout', 0) for b in wins)
        losses = sum(b['stake'] for b in wb if b['outcome'] == 'loss')
        net = total_payout - losses
        hit = len(wins) / len(wb) * 100
        roi = (net / total_stake * 100) if total_stake > 0 else 0

        clv_bets = [b for b in wb if b.get('clv') is not None]
        avg_clv = sum(b['clv'] for b in clv_bets) / len(clv_bets) if clv_bets else 0

        print(f"  {week:<12} {len(wb):>5} {len(wins):>5} {hit:>6.1f}% ${net:>+8.2f} {roi:>+6.1f}% {avg_clv:>+6.1f}")

    # Totals
    total_wins = [b for b in settled if b['outcome'] == 'win']
    total_staked = sum(b['stake'] for b in settled)
    total_returned = sum(b.get('payout', 0) for b in total_wins)
    total_lost = sum(b['stake'] for b in settled if b['outcome'] == 'loss')
    total_net = total_returned - total_lost
    overall_hit = len(total_wins) / len(settled) * 100
    overall_roi = (total_net / total_staked * 100) if total_staked > 0 else 0

    print(f"  {'─'*65}")
    print(f"  {'TOTAL':<12} {len(settled):>5} {len(total_wins):>5} {overall_hit:>6.1f}% ${total_net:>+8.2f} {overall_roi:>+6.1f}%")

    # Drawdown check
    bankroll = data['bankroll']['initial']
    peak = bankroll
    max_dd = 0
    for b in sorted(settled, key=lambda x: x['date']):
        if b['outcome'] == 'win':
            bankroll += b.get('payout', 0)
        else:
            bankroll -= b['stake']
        peak = max(peak, bankroll)
        dd = peak - bankroll
        max_dd = max(max_dd, dd)

    dd_pct = (max_dd / data['bankroll']['initial'] * 100) if data['bankroll']['initial'] > 0 else 0

    print(f"\n  Bankroll: ${data['bankroll']['current']:.2f} (started ${data['bankroll']['initial']:.2f})")
    print(f"  Max Drawdown: ${max_dd:.2f} ({dd_pct:.1f}%)")

    if dd_pct > 20:
        print(f"\n  DRAWDOWN ALERT: {dd_pct:.1f}% drawdown exceeds 20% threshold.")
        print(f"  Consider reducing position sizes or pausing until review.")
    print()


def cmd_milestone(args):
    """500-bet milestone tracker."""
    data = load_live_data()
    bets = data['bets']
    settled = [b for b in bets if b['outcome'] is not None]

    target = LIMITS['milestone_target']
    progress = len(settled) / target * 100

    print(f"\n{'='*60}")
    print(f"  500-BET MILESTONE TRACKER")
    print(f"{'='*60}")

    # Progress bar
    bar_len = 40
    filled = int(bar_len * min(progress, 100) / 100)
    bar = '#' * filled + '-' * (bar_len - filled)
    print(f"\n  [{bar}] {progress:.0f}%")
    print(f"  {len(settled)}/{target} bets settled")

    if settled:
        wins = [b for b in settled if b['outcome'] == 'win']
        hit_rate = len(wins) / len(settled) * 100
        total_staked = sum(b['stake'] for b in settled)
        total_won = sum(b.get('payout', 0) for b in wins)
        total_lost = sum(b['stake'] for b in settled if b['outcome'] == 'loss')
        net = total_won - total_lost
        roi = (net / total_staked * 100) if total_staked > 0 else 0

        print(f"\n  Running Stats")
        print(f"  {'─'*50}")
        print(f"  Hit Rate:    {hit_rate:.1f}% ({'ABOVE' if hit_rate > 52.4 else 'BELOW'} breakeven)")
        print(f"  ROI:         {roi:+.1f}%")
        print(f"  Net P/L:     ${net:+.2f}")

        clv_bets = [b for b in settled if b.get('clv') is not None]
        if clv_bets:
            avg_clv = sum(b['clv'] for b in clv_bets) / len(clv_bets)
            print(f"  Avg CLV:     {avg_clv:+.1f} pts ({'POSITIVE' if avg_clv > 0 else 'NEGATIVE'})")

        # Milestones
        milestones = [50, 100, 200, 300, 400, 500]
        print(f"\n  Milestones")
        print(f"  {'─'*50}")
        for m in milestones:
            if len(settled) >= m:
                sub = settled[:m]
                sub_wins = [b for b in sub if b['outcome'] == 'win']
                sub_rate = len(sub_wins) / len(sub) * 100
                print(f"  {m:>3} bets:  {sub_rate:.1f}% hit rate  {'PASS' if sub_rate > 52.4 else 'FAIL'}")
            else:
                remaining = m - len(settled)
                print(f"  {m:>3} bets:  {remaining} more needed")

    if len(settled) >= target:
        print(f"\n  MILESTONE REACHED: {target} bets completed!")
        print(f"  System is fully validated. Consider Phase 4 (ML models, automation).")

    print()


def main():
    parser = argparse.ArgumentParser(
        description='NBA Live Trader — Phase 3 conservative deployment'
    )
    sub = parser.add_subparsers(dest='command')

    # check
    sub.add_parser('check', help='Go/No-Go gate check')

    # slate
    p_slate = sub.add_parser('slate', help='Generate live picks')
    p_slate.add_argument('--bankroll', type=float, required=True, help='Current bankroll')
    p_slate.add_argument('--game', type=str, default=None, help='Specific game event ID')
    p_slate.add_argument('--override', action='store_true', help='Skip gate check')

    # result
    p_result = sub.add_parser('result', help='Record a live bet result')
    p_result.add_argument('bet_id', help='Bet ID')
    p_result.add_argument('actual', type=float, help='Actual stat value')
    p_result.add_argument('--closing-line', type=float, default=None, help='Closing line')

    # weekly
    sub.add_parser('weekly', help='Weekly performance review')

    # milestone
    sub.add_parser('milestone', help='500-bet milestone tracker')

    args = parser.parse_args()

    commands = {
        'check': cmd_check,
        'slate': cmd_slate,
        'result': cmd_result,
        'weekly': cmd_weekly,
        'milestone': cmd_milestone,
    }

    if args.command in commands:
        commands[args.command](args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
