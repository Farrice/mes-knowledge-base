---
description: Generate tonight's NBA picks
---

# /picks-tonight — Tonight's NBA Picks

Fully automated daily pick generation. You don't need to understand any of the internals — just run this command before games start and you'll get tonight's picks with confidence ratings and bet sizing.

## Usage

```
/picks-tonight              # Full tonight's slate
/picks-tonight quick        # Skip injury research, faster but less accurate
```

## What This Does (You Don't Need To Know The Details)

1. Pulls tonight's NBA games and live sportsbook lines
2. Checks injury reports for every relevant player
3. Runs the projection engine on every available prop
4. Filters to only the picks with real statistical edge
5. Scores each pick's confidence (1-5 scale)
6. Calculates how much to bet based on confidence
7. Outputs a clean pick card you can share

## Steps (System Executes Automatically)

### Step 1 — Load System
Read `skills/nba-betting-edge/genius.md` for the analytical framework.
Read current bankroll from `.agent/bet-tracking.json` and `.agent/paper-trading.json`.

### Step 2 — Pull Tonight's Games
```bash
python execution/odds_fetcher.py games
python execution/odds_fetcher.py lines
```
If no games tonight, say "No NBA games tonight" and stop.

### Step 3 — Injury Check
Use Perplexity (check budget in `.agent/perplexity-usage.json` first):
"NBA games [today's date] full injury report confirmed starting lineups"

If Perplexity budget is low, use WebSearch instead.

**Hard rule**: Any player confirmed OUT — void their props. Any player RETURNING from absence — flag for boost.

### Step 4 — Identify Best Games
Skip blowout games (spread > 12). Focus on the 2-3 games with:
- Injury situations creating usage shifts
- Competitive spreads (starters play full minutes)
- Pace mismatches

### Step 5 — Pull Props + Run Projections
For each focus game:
```bash
python execution/odds_fetcher.py props <event_id>
```
For the best prop targets (consistent players, points props preferred):
```bash
python execution/projection_engine.py analyze "[Player]" [prop] "[Opponent]" --line [X]
```

### Step 6 — Filter and Build Slate
Only include picks with:
- Confidence 3+ (the system rates 1-5, 3+ means real edge)
- Points props preferred (rebounds/assists are less reliable)
- No more than 70% picks in the same direction

### Step 7 — Output Pick Card

Present picks in this EXACT format (clean enough to screenshot and share):

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  TONIGHT'S PICKS — [Date]
  System: NBA Betting Edge v2.1
  Paper Bankroll: $[X]  |  Record: [W]-[L] ([X]%)
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  PICK 1: [Player] [OVER/UNDER] [Line] [Prop]
  Confidence: [X]/5 ([Label])  |  Edge: [X] pts
  Best Book: [Book] at [Odds]
  Why: [1-sentence plain English reason]

  PICK 2: ...

  ─────────────────────────────────────
  PARLAY (if applicable):
  [Leg 1] + [Leg 2]  |  Sizing: $[X]
  ─────────────────────────────────────

  Total Exposure: $[X] ([X]% of bankroll)
  Slate Confidence: [X]/10
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Step 8 — Auto-Log Paper Bets
Log all picks automatically:
```bash
python execution/bet_tracker.py log "[Player]" [prop] [line] [direction] --projection [X] --confidence [N] --stake [amount]
```

Tell the user: "Picks logged. Run `/picks-review` tomorrow after games finish to record results."

## Output Rules
- Use plain English — no jargon about CV, Kelly criterion, or projection formulas
- "Confidence 4/5" is fine. Don't explain what drives it.
- "Edge: 2.5 pts" is fine. Don't explain the 60/25/15 formula.
- The pick card should be screenshot-ready for sharing
- Always end with the next action: "Run `/picks-review` tomorrow"
