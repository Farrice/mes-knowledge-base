---
description: Review last night's picks
---

# /picks-review — Morning Results Review

Fully automated results review. Looks up what actually happened last night, records wins and losses, updates your track record. Run this every morning after last night's games.

## Usage

```
/picks-review               # Review last night's results
/picks-review [date]         # Review a specific date
```

## What This Does

1. Finds all pending (unresolved) paper bets
2. Looks up actual stat lines from NBA.com
3. Records each bet as a win or loss
4. Updates your paper bankroll
5. Shows your updated track record
6. Tells you if the system is getting better or worse

## Steps (System Executes Automatically)

### Step 1 — Find Pending Bets
```bash
python execution/paper_trader.py results
```
If no pending bets: "No pending bets to review. Run `/picks-tonight` to generate today's picks."

### Step 2 — Look Up Actual Results
For each pending bet, pull the player's actual stat line:
```bash
python execution/nba_stats.py gamelog "[Player]" --games 3
```
Find the game from the bet date and extract the actual value.

### Step 3 — Record Results
For each bet:
```bash
python execution/paper_trader.py result [bet_id] [actual_value]
```

### Step 4 — Show Results Card

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  RESULTS — [Date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  [WIN/LOSS] [Player] [OVER/UNDER] [Line] [Prop]
  Predicted: [X]  |  Actual: [Y]  |  [+$X / -$X]

  [WIN/LOSS] [Player] ...

  ─────────────────────────────────────
  Last Night: [X]W-[Y]L  |  P/L: [+/-$X]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Step 5 — Show Updated Dashboard
```bash
python execution/paper_trader.py status
```

Present the key numbers in plain English:
- "You're at [X] total bets with a [X]% win rate"
- "Paper bankroll: $[X] (started at $1,000)"
- "The system needs [X] more bets before we can consider live betting"

### Step 6 — Next Action
Tell the user: "Run `/picks-tonight` later today for tonight's picks."

## Output Rules
- Celebrate wins briefly, don't dwell on losses
- Show the running record prominently
- Plain English — no technical analysis unless asked
- Always end with the next action
