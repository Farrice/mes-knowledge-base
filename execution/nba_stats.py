#!/usr/bin/env python3
"""
NBA Stats Engine — Pull real player and team statistics from NBA.com via nba_api.

Replaces Perplexity-sourced stat estimates with actual API data.
All projections in the betting system flow through this module.

Usage:
    python execution/nba_stats.py player "Nikola Jokic"                    # Season averages
    python execution/nba_stats.py gamelog "Nikola Jokic"                   # Last 10 game logs
    python execution/nba_stats.py gamelog "Nikola Jokic" --games 20        # Last 20 game logs
    python execution/nba_stats.py projection "Nikola Jokic" points        # Weighted projection for prop
    python execution/nba_stats.py teams                                    # All team pace + defensive ratings
    python execution/nba_stats.py matchup "Nikola Jokic" "San Antonio Spurs"  # Full matchup context
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime

# Rate limit: NBA.com throttles aggressively. Pause between calls.
API_DELAY = 0.6  # seconds between API calls

# Cache directory for reducing API hits
CACHE_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))),
    '.agent', 'nba-cache'
)

SEASON = '2025-26'

# ─── Player Lookup (fuzzy matching with accent handling) ────────────────────

def _normalize(name):
    """Normalize name for fuzzy matching: lowercase, strip accents."""
    import unicodedata
    name = unicodedata.normalize('NFD', name.lower())
    return ''.join(c for c in name if unicodedata.category(c) != 'Mn')


def find_player(name):
    """Find a player by name with fuzzy matching. Returns dict with id, full_name, etc."""
    from nba_api.stats.static import players

    all_players = players.get_players()
    query = _normalize(name)

    # Exact match first (normalized)
    for p in all_players:
        if _normalize(p['full_name']) == query:
            return p

    # Partial match (last name or full name contains query)
    matches = [p for p in all_players if query in _normalize(p['full_name'])]
    if len(matches) == 1:
        return matches[0]
    if len(matches) > 1:
        # Prefer active players
        active = [p for p in matches if p['is_active']]
        if len(active) == 1:
            return active[0]
        if active:
            return active[0]
        return matches[0]

    # Last name only match
    matches = [p for p in all_players if _normalize(p['last_name']) == query]
    if matches:
        active = [p for p in matches if p['is_active']]
        return active[0] if active else matches[0]

    return None


def find_team(name):
    """Find a team by name/city/abbreviation."""
    from nba_api.stats.static import teams

    all_teams = teams.get_teams()
    query = name.lower()

    for t in all_teams:
        if query in [t['full_name'].lower(), t['nickname'].lower(),
                     t['abbreviation'].lower(), t['city'].lower()]:
            return t

    # Partial match
    for t in all_teams:
        if query in t['full_name'].lower():
            return t

    return None


# ─── Caching Layer ──────────────────────────────────────────────────────────

def _cache_path(key):
    os.makedirs(CACHE_DIR, exist_ok=True)
    return os.path.join(CACHE_DIR, f"{key}.json")


def _cache_get(key, max_age_hours=6):
    """Get cached data if fresh enough."""
    path = _cache_path(key)
    if not os.path.exists(path):
        return None
    try:
        with open(path, 'r') as f:
            data = json.load(f)
        cached_at = datetime.fromisoformat(data['_cached_at'])
        age_hours = (datetime.now() - cached_at).total_seconds() / 3600
        if age_hours < max_age_hours:
            return data['payload']
    except (json.JSONDecodeError, KeyError):
        pass
    return None


def _cache_set(key, payload):
    """Cache data with timestamp."""
    path = _cache_path(key)
    with open(path, 'w') as f:
        json.dump({'_cached_at': datetime.now().isoformat(), 'payload': payload}, f)


# ─── Player Game Logs ───────────────────────────────────────────────────────

def get_player_gamelog(player_id, season=SEASON, num_games=None):
    """Pull player game log for a season. Returns list of dicts."""
    cache_key = f"gamelog_{player_id}_{season}"
    cached = _cache_get(cache_key, max_age_hours=4)
    if cached:
        games = cached
    else:
        from nba_api.stats.endpoints import playergamelog
        time.sleep(API_DELAY)
        log = playergamelog.PlayerGameLog(player_id=player_id, season=season)
        df = log.get_data_frames()[0]
        games = df.to_dict('records')
        _cache_set(cache_key, games)

    if num_games:
        games = games[:num_games]
    return games


def get_season_averages(player_id, season=SEASON):
    """Calculate season averages from game logs."""
    games = get_player_gamelog(player_id, season)
    if not games:
        return None

    stats = ['PTS', 'REB', 'AST', 'STL', 'BLK', 'FG3M', 'MIN', 'TOV',
             'FGM', 'FGA', 'FG_PCT', 'FTM', 'FTA']
    averages = {}
    n = len(games)
    for stat in stats:
        vals = [g[stat] for g in games if g.get(stat) is not None]
        if vals:
            averages[stat] = round(sum(vals) / len(vals), 1)

    averages['GP'] = n
    averages['player_id'] = player_id
    return averages


# ─── Weighted Projection (60/25/15 formula) ─────────────────────────────────

PROP_STAT_MAP = {
    'points': 'PTS',
    'rebounds': 'REB',
    'assists': 'AST',
    'threes': 'FG3M',
    'steals': 'STL',
    'blocks': 'BLK',
    'pts_reb_ast': None,  # composite
}


def calculate_projection(player_id, prop_type, season=SEASON):
    """
    Calculate weighted projection using the 60/25/15 formula.

    Returns dict with:
      - projection: weighted projection
      - season_avg: full season average
      - last_10_avg: last 10 games average
      - last_3_avg: last 3 games average
      - std_dev: standard deviation of last 10
      - games_played: total games this season
      - recent_trend: 'up', 'down', or 'stable'
      - last_game: most recent game stat
    """
    games = get_player_gamelog(player_id, season)
    if not games:
        return None

    stat_col = PROP_STAT_MAP.get(prop_type)
    if stat_col is None and prop_type == 'pts_reb_ast':
        # Composite: PTS + REB + AST
        values = [g['PTS'] + g['REB'] + g['AST'] for g in games]
    elif stat_col:
        values = [g[stat_col] for g in games]
    else:
        return None

    if len(values) < 3:
        return None

    season_avg = sum(values) / len(values)
    last_10 = values[:10]
    last_3 = values[:3]

    last_10_avg = sum(last_10) / len(last_10)
    last_3_avg = sum(last_3) / len(last_3)

    # Weighted projection: 60% last 10, 25% season, 15% last 3
    projection = (last_10_avg * 0.60) + (season_avg * 0.25) + (last_3_avg * 0.15)

    # Standard deviation of last 10 games
    mean = last_10_avg
    variance = sum((x - mean) ** 2 for x in last_10) / len(last_10)
    std_dev = variance ** 0.5

    # Trend detection
    if last_3_avg > last_10_avg * 1.10:
        trend = 'up'
    elif last_3_avg < last_10_avg * 0.90:
        trend = 'down'
    else:
        trend = 'stable'

    # Check for outlier recency bias (last game is 2+ std_dev from season avg)
    recency_flag = None
    if std_dev > 0 and abs(values[0] - season_avg) > 2 * std_dev:
        recency_flag = 'outlier_high' if values[0] > season_avg else 'outlier_low'

    return {
        'projection': round(projection, 1),
        'season_avg': round(season_avg, 1),
        'last_10_avg': round(last_10_avg, 1),
        'last_3_avg': round(last_3_avg, 1),
        'std_dev': round(std_dev, 1),
        'games_played': len(values),
        'recent_trend': trend,
        'last_game': values[0],
        'recency_flag': recency_flag,
        'last_10_values': last_10,
    }


# ─── Team Stats (Pace + Defensive Rating) ──────────────────────────────────

def get_all_team_stats(season=SEASON):
    """Get pace, offensive rating, and defensive rating for all 30 teams."""
    cache_key = f"team_advanced_{season}"
    cached = _cache_get(cache_key, max_age_hours=12)
    if cached:
        return cached

    from nba_api.stats.endpoints import leaguedashteamstats
    time.sleep(API_DELAY)
    stats = leaguedashteamstats.LeagueDashTeamStats(
        season=season,
        measure_type_detailed_defense='Advanced'
    )
    df = stats.get_data_frames()[0]
    teams = {}
    for _, row in df.iterrows():
        teams[row['TEAM_NAME']] = {
            'team_id': int(row['TEAM_ID']),
            'team_name': row['TEAM_NAME'],
            'gp': int(row['GP']),
            'w': int(row['W']),
            'l': int(row['L']),
            'pace': round(float(row['PACE']), 1),
            'off_rating': round(float(row['OFF_RATING']), 1),
            'def_rating': round(float(row['DEF_RATING']), 1),
            'net_rating': round(float(row['NET_RATING']), 1),
        }
    _cache_set(cache_key, teams)
    return teams


def get_team_stats(team_name, season=SEASON):
    """Get stats for a specific team."""
    all_stats = get_all_team_stats(season)
    # Try exact match first
    if team_name in all_stats:
        return all_stats[team_name]
    # Fuzzy match
    query = team_name.lower()
    for name, stats in all_stats.items():
        if query in name.lower():
            return stats
    return None


# ─── League Average Pace (for pace adjustment) ─────────────────────────────

def get_league_avg_pace(season=SEASON):
    """Get the league average pace for normalizing pace adjustments."""
    all_stats = get_all_team_stats(season)
    paces = [t['pace'] for t in all_stats.values()]
    return round(sum(paces) / len(paces), 1)


# ─── Matchup Context ───────────────────────────────────────────────────────

def build_matchup_context(player_name, opponent_name, prop_type='points', season=SEASON):
    """
    Build full Context Stack for a player prop matchup.

    Returns:
      - player info + projection
      - opponent defensive context
      - pace adjustment factor
      - home/away detection (from recent games)
    """
    player = find_player(player_name)
    if not player:
        return {'error': f"Player not found: {player_name}"}

    opp_stats = get_team_stats(opponent_name, season)
    if not opp_stats:
        return {'error': f"Team not found: {opponent_name}"}

    projection = calculate_projection(player['id'], prop_type, season)
    if not projection:
        return {'error': f"Not enough data for {player_name} {prop_type}"}

    # Pace adjustment
    league_pace = get_league_avg_pace(season)
    opp_pace = opp_stats['pace']
    pace_factor = (opp_pace - league_pace) / league_pace  # e.g., +0.03 = 3% faster

    # Apply pace adjustment to projection
    pace_adjusted = projection['projection'] * (1 + pace_factor)

    # Opponent defensive context
    # Lower def_rating = better defense (fewer points allowed per 100 possessions)
    league_avg_def = 113.0  # approximate
    def_adjustment = (opp_stats['def_rating'] - league_avg_def) / league_avg_def

    # Apply defensive adjustment (positive = weaker defense = boost projection)
    matchup_adjusted = pace_adjusted * (1 + def_adjustment)

    # Check recent games for return-from-absence
    games = get_player_gamelog(player['id'], season, num_games=10)
    games_missed = 0
    if len(games) >= 2:
        from datetime import datetime as dt
        try:
            d1 = dt.strptime(games[0]['GAME_DATE'].strip(), '%b %d, %Y')
            d2 = dt.strptime(games[1]['GAME_DATE'].strip(), '%b %d, %Y')
            gap_days = (d1 - d2).days
            if gap_days > 3:  # More than 3 days between games suggests missed games
                games_missed = gap_days // 2 - 1  # rough estimate
        except (ValueError, KeyError):
            pass

    return {
        'player': {
            'name': player['full_name'],
            'id': player['id'],
        },
        'prop_type': prop_type,
        'projection': {
            'raw': projection['projection'],
            'pace_adjusted': round(pace_adjusted, 1),
            'matchup_adjusted': round(matchup_adjusted, 1),
            'season_avg': projection['season_avg'],
            'last_10_avg': projection['last_10_avg'],
            'last_3_avg': projection['last_3_avg'],
            'std_dev': projection['std_dev'],
            'trend': projection['recent_trend'],
            'recency_flag': projection['recency_flag'],
            'last_game': projection['last_game'],
            'games_played': projection['games_played'],
        },
        'adjustments': {
            'pace_factor': round(pace_factor * 100, 1),  # percentage
            'def_adjustment': round(def_adjustment * 100, 1),  # percentage
        },
        'opponent': {
            'name': opp_stats['team_name'],
            'pace': opp_stats['pace'],
            'def_rating': opp_stats['def_rating'],
            'off_rating': opp_stats['off_rating'],
            'record': f"{opp_stats['w']}-{opp_stats['l']}",
        },
        'context': {
            'league_avg_pace': league_pace,
            'estimated_games_missed': games_missed,
            'return_from_absence': games_missed > 0,
        },
        'last_10_values': projection['last_10_values'],
    }


# ─── CLI ────────────────────────────────────────────────────────────────────

def cmd_player(args):
    """Show season averages for a player."""
    player = find_player(args.name)
    if not player:
        print(f"Player not found: {args.name}")
        sys.exit(1)

    print(f"\n{'='*50}")
    print(f"  {player['full_name']} (ID: {player['id']})")
    print(f"  Active: {player['is_active']}")
    print(f"{'='*50}")

    avgs = get_season_averages(player['id'])
    if not avgs:
        print("  No game data found for current season.")
        return

    print(f"\n  {SEASON} Season Averages ({avgs['GP']} games)")
    print(f"  {'─'*40}")
    print(f"  PTS: {avgs.get('PTS', 'N/A'):>6}  |  REB: {avgs.get('REB', 'N/A'):>6}  |  AST: {avgs.get('AST', 'N/A'):>6}")
    print(f"  STL: {avgs.get('STL', 'N/A'):>6}  |  BLK: {avgs.get('BLK', 'N/A'):>6}  |  3PM: {avgs.get('FG3M', 'N/A'):>6}")
    print(f"  MIN: {avgs.get('MIN', 'N/A'):>6}  |  TOV: {avgs.get('TOV', 'N/A'):>6}  |  FG%: {avgs.get('FG_PCT', 'N/A'):>6}")
    print()


def cmd_gamelog(args):
    """Show recent game logs for a player."""
    player = find_player(args.name)
    if not player:
        print(f"Player not found: {args.name}")
        sys.exit(1)

    num = args.games or 10
    games = get_player_gamelog(player['id'], num_games=num)

    print(f"\n  {player['full_name']} — Last {len(games)} Games")
    print(f"  {'─'*75}")
    print(f"  {'Date':<15} {'Matchup':<15} {'MIN':>4} {'PTS':>4} {'REB':>4} {'AST':>4} {'3PM':>4} {'W/L':>4}")
    print(f"  {'─'*75}")
    for g in games:
        print(f"  {g['GAME_DATE']:<15} {g['MATCHUP']:<15} {g['MIN']:>4} {g['PTS']:>4} {g['REB']:>4} {g['AST']:>4} {g['FG3M']:>4} {g['WL']:>4}")
    print()


def cmd_projection(args):
    """Show weighted projection for a player prop."""
    player = find_player(args.name)
    if not player:
        print(f"Player not found: {args.name}")
        sys.exit(1)

    prop = args.prop
    if prop not in PROP_STAT_MAP:
        print(f"Invalid prop type: {prop}")
        print(f"Valid types: {', '.join(PROP_STAT_MAP.keys())}")
        sys.exit(1)

    proj = calculate_projection(player['id'], prop)
    if not proj:
        print(f"Not enough data for projection.")
        sys.exit(1)

    print(f"\n  {player['full_name']} — {prop.upper()} Projection")
    print(f"  {'─'*45}")
    print(f"  Weighted Projection (60/25/15): {proj['projection']}")
    print(f"  Season Average:                 {proj['season_avg']}")
    print(f"  Last 10 Average:                {proj['last_10_avg']}")
    print(f"  Last 3 Average:                 {proj['last_3_avg']}")
    print(f"  Std Dev (last 10):              {proj['std_dev']}")
    print(f"  Trend:                          {proj['recent_trend']}")
    print(f"  Last Game:                      {proj['last_game']}")
    if proj['recency_flag']:
        print(f"  ⚠  Recency Flag:               {proj['recency_flag']}")
    print(f"  Games Played:                   {proj['games_played']}")
    print(f"\n  Last 10 values: {proj['last_10_values']}")
    print()


def cmd_teams(args):
    """Show all team pace and defensive ratings."""
    teams = get_all_team_stats()
    sorted_teams = sorted(teams.values(), key=lambda t: t['pace'], reverse=True)

    print(f"\n  NBA Team Advanced Stats ({SEASON})")
    print(f"  {'─'*70}")
    print(f"  {'Team':<25} {'Pace':>6} {'OffRtg':>7} {'DefRtg':>7} {'NetRtg':>7} {'Record':>8}")
    print(f"  {'─'*70}")
    for t in sorted_teams:
        record = f"{t['w']}-{t['l']}"
        print(f"  {t['team_name']:<25} {t['pace']:>6.1f} {t['off_rating']:>7.1f} {t['def_rating']:>7.1f} {t['net_rating']:>7.1f} {record:>8}")
    print()


def cmd_matchup(args):
    """Show full matchup context for a player vs opponent."""
    ctx = build_matchup_context(args.player, args.opponent, args.prop or 'points')
    if 'error' in ctx:
        print(f"Error: {ctx['error']}")
        sys.exit(1)

    p = ctx['projection']
    o = ctx['opponent']
    a = ctx['adjustments']
    c = ctx['context']

    print(f"\n{'='*60}")
    print(f"  MATCHUP: {ctx['player']['name']} vs {o['name']}")
    print(f"  Prop: {ctx['prop_type'].upper()}")
    print(f"{'='*60}")

    print(f"\n  Projection Breakdown")
    print(f"  {'─'*45}")
    print(f"  Raw (60/25/15):            {p['raw']}")
    print(f"  + Pace Adjustment ({a['pace_factor']:+.1f}%):  {p['pace_adjusted']}")
    print(f"  + Defense Adj ({a['def_adjustment']:+.1f}%):    {p['matchup_adjusted']}")
    print(f"  Season Average:            {p['season_avg']}")
    print(f"  Last 10 Average:           {p['last_10_avg']}")
    print(f"  Last 3 Average:            {p['last_3_avg']}")
    print(f"  Std Dev:                   {p['std_dev']}")
    print(f"  Trend:                     {p['trend']}")
    if p['recency_flag']:
        print(f"  Recency Flag:              {p['recency_flag']}")

    print(f"\n  Opponent Context")
    print(f"  {'─'*45}")
    print(f"  {o['name']} ({o['record']})")
    print(f"  Pace:        {o['pace']} (league avg: {c['league_avg_pace']})")
    print(f"  Def Rating:  {o['def_rating']}")
    print(f"  Off Rating:  {o['off_rating']}")

    if c['return_from_absence']:
        print(f"\n  ⚠  RETURN FROM ABSENCE — est. {c['estimated_games_missed']} games missed")
        print(f"     Consider +10-15% boost to projection")

    print(f"\n  Last 10 Game Values: {ctx.get('last_10_values', [])}")
    print()


def main():
    parser = argparse.ArgumentParser(description='NBA Stats Engine — Real data from NBA.com')
    sub = parser.add_subparsers(dest='command')

    # player
    p_player = sub.add_parser('player', help='Season averages for a player')
    p_player.add_argument('name', help='Player name (fuzzy match)')

    # gamelog
    p_log = sub.add_parser('gamelog', help='Recent game logs')
    p_log.add_argument('name', help='Player name')
    p_log.add_argument('--games', type=int, default=10, help='Number of games (default: 10)')

    # projection
    p_proj = sub.add_parser('projection', help='Weighted projection for a prop')
    p_proj.add_argument('name', help='Player name')
    p_proj.add_argument('prop', help=f"Prop type: {', '.join(PROP_STAT_MAP.keys())}")

    # teams
    sub.add_parser('teams', help='All team pace + defensive ratings')

    # matchup
    p_match = sub.add_parser('matchup', help='Full matchup context')
    p_match.add_argument('player', help='Player name')
    p_match.add_argument('opponent', help='Opponent team name')
    p_match.add_argument('--prop', default='points', help=f"Prop type (default: points)")

    args = parser.parse_args()

    if args.command == 'player':
        cmd_player(args)
    elif args.command == 'gamelog':
        cmd_gamelog(args)
    elif args.command == 'projection':
        cmd_projection(args)
    elif args.command == 'teams':
        cmd_teams(args)
    elif args.command == 'matchup':
        cmd_matchup(args)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
