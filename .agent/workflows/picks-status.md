---
description: Full track record dashboard
---

# /picks-status — Track Record Dashboard

Shows the complete system performance in a format you can share with friends or potential subscribers. This is the "proof" that the system works.

## Usage

```
/picks-status               # Full dashboard
/picks-status shareable     # Extra clean format for screenshots/sharing
```

## Steps

### Step 1 — Pull All Data
```bash
python execution/paper_trader.py status
```

Also analyze the full bet history:
```python
# Read .agent/paper-trading.json and calculate:
# - Overall win rate and ROI
# - Win rate by confidence level (proves the system knows when it's confident)
# - Best and worst players
# - Points vs rebounds vs assists performance
# - OVER vs UNDER performance
# - Recent streak (last 20 bets)
```

### Step 2 — Output Dashboard

**Standard format:**
```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
  NBA BETTING EDGE — TRACK RECORD
  System v2.1  |  Since [start date]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

  OVERALL
  Record:           [W]-[L] ([X]%)
  ROI:              [+X]%
  Paper Bankroll:   $[X] (started $1,000)
  Total Bets:       [X]

  BY CONFIDENCE (higher = better)
  Conf 5 (Lock):    [X]W-[Y]L ([Z]%)
  Conf 4 (Strong):  [X]W-[Y]L ([Z]%)
  Conf 3 (Lean):    [X]W-[Y]L ([Z]%)

  LAST 20 BETS
  [X]W-[Y]L ([Z]%)  |  Streak: [X]W / [X]L

  TOP PERFORMERS
  [Player 1]: [X]W-[Y]L ([Z]%)
  [Player 2]: [X]W-[Y]L ([Z]%)
  [Player 3]: [X]W-[Y]L ([Z]%)

  LIVE READINESS
  Go/No-Go: [X]/200 bets  |  [PASS/PENDING]
  Hit Rate > 53%: [PASS/FAIL]
  Confidence Calibrated: [PASS/FAIL]
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

**Shareable format** (for Discord/screenshots — even cleaner):
```
NBA Betting Edge | Track Record
[W]-[L] ([X]%) | ROI: [+X]% | Since [date]
Bankroll: $1,000 → $[X]
High-confidence picks: [X]% win rate
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

### Step 3 — Recommendations
Based on the data, suggest:
- If hit rate is trending up: "System is improving. Keep running daily picks."
- If hit rate is dipping: "Recent streak is cold. Stick to Confidence 4+ picks only until it recovers."
- If close to 200+ real-line bets: "Getting close to live-ready. [X] more bets needed."
- If track record is strong enough to share: "This track record is ready to show potential subscribers."

## Output Rules
- This is the "sales page" for the system — make it look impressive but honest
- No jargon — confidence levels are labeled (Lock, Strong, Lean), not explained
- The shareable format should fit in a Discord message or screenshot
