---
description: "Fast-path NBA picks — auto-detects mode (tonight's slate or review past results) and runs the betting edge system with minimal ceremony. Say 'check my picks' and go."
---

# /check-picks — Quick NBA Picks Gateway

Fast entry point into the NBA Betting Edge system. Detects intent automatically and routes to the right workflow without asking questions.

## Usage

```
/check-picks                    # Tonight's slate — full edge analysis
/check-picks review             # Review recent results + calibration
/check-picks [date]             # Picks or review for a specific date
/check-picks [Player Name]      # Quick single-player prop check
```

## Auto-Detection Logic

Parse user input to determine mode:

1. **"review"**, **"results"**, **"how did we do"**, **"yesterday"** → **Review Mode**
2. **A past date** (before today) → **Review Mode** for that date
3. **A player name** → **Quick Prop Mode** (single player analysis)
4. **Default** (no modifier, "check my picks", today's date, future date) → **Tonight Mode**

---

## Tonight Mode (Default)

Run the full game-day analysis in a streamlined sequence. No input prompts — assume $100 bankroll (or read current from `.agent/bet-tracking.json`), moderate risk tolerance.

### Step 1 — Pull Tonight's Slate
```bash
python execution/odds_fetcher.py games
```
If no games tonight, say so and offer to analyze the next game day.

### Step 2 — Pull Lines + Injury Context
Run in parallel:
```bash
python execution/odds_fetcher.py lines
```
Use perplexity_search: "NBA games [today's date] injury report confirmed starting lineups rest schedule"

**Injury Hard Gate**: Any player OUT voids their props. Any player RETURNING gets +10-15% boost. Flag QUESTIONABLE players.

### Step 3 — Run Projections
For each game with edge potential (injury situations, pace mismatches, B2B fatigue, public money games), pull stats and run projections:
```bash
python execution/nba_stats.py matchup "[Player]" "[Opponent]" --prop [type]
python execution/projection_engine.py analyze "[Player]" [prop] "[Opponent]" --line [X]
```
Focus on 2-3 highest-edge games, not the entire slate.

### Step 4 — Three-Lens Conviction Test
For every pick, run all three lenses (statistical, narrative, market intelligence) per genius.md Pattern 10. Anti-bias check: no more than 70% same direction.

### Step 5 — Build Pick Slate
Load genius context from `skills/nba-betting-edge/genius.md` and produce:

**Pick Slate Table:**
| Player | Prop | Line | Projection | Edge | Conf | Direction | Best Book | Reasoning |
|--------|------|------|-----------|------|------|-----------|-----------|-----------|

**Parlay Suggestions** (if 2+ picks at confidence 3+):
- Correlation analysis between legs
- Kelly sizing from bankroll

**Bankroll Status**: Current bankroll from `.agent/bet-tracking.json`

**Four Horsemen Audit**: Quick pass — Fear/Greed/Hope/Ignorance scan on final slate.

### Step 6 — Log Reminder
After delivering picks, remind:
```
To log bets: python execution/bet_tracker.py log "[Player]" [prop] [line] [direction] --projection [X] --confidence [N]
Tomorrow: /check-picks review
```

---

## Review Mode

### Step 1 — Pull Results
```bash
python execution/bet_tracker.py summary
```
If no results logged yet, help the user enter them:
```bash
python execution/bet_tracker.py result [bet_id] [actual_value] [win/loss]
```

### Step 2 — Quick Calibration
- Win/loss record + ROI
- Projection accuracy (how close were projections to actuals?)
- Confidence calibration (are high-confidence picks hitting more?)
- CLV check if closing lines were recorded

### Step 3 — Pattern Check
Which genius patterns contributed to wins vs. losses? Quick 2-3 sentence assessment.

### Step 4 — Bankroll Update
Current bankroll, trajectory, any drawdown alerts.

---

## Quick Prop Mode

Single player analysis — fast version:
```bash
python execution/nba_stats.py matchup "[Player]" "[Opponent]" --prop [type]
python execution/projection_engine.py analyze "[Player]" [prop] "[Opponent]" --line [X]
```
Output: Projection, edge, confidence, direction, one-paragraph reasoning.

---

## Quality Gate
1. Every pick has a quantified edge (not "I think")
2. Injury gate fired before projections
3. Three-Lens Test ran for every pick
4. Four Horsemen audit on final slate
5. Anti-bias check (no 70%+ same direction)
6. Bankroll sizing from Kelly, not gut feel
