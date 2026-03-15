---
description: "NBA Betting Edge — systematic player prop analysis using behavioral finance principles, statistical edge detection, and correlation-aware parlay construction with Kelly criterion bankroll discipline"
---

# /betting-edge — NBA Betting Edge

Systematic NBA player prop analysis and parlay construction. Uses real NBA.com game log data via `nba_stats.py` for projections, `projection_engine.py` for matchup-adjusted edge detection, Perplexity for injury/narrative context, Jim O'Shaughnessy's behavioral finance framework for bias detection, a 6-variable Context Stack for every prediction, and a Multi-Angle Conviction Test that argues both sides before picking a direction. Confidence scoring drives Kelly criterion position sizing.

**The standard**: Every pick has a quantified edge (projection vs. line) calculated from real NBA.com game log data, every projection uses the weighted formula (60% 10-game avg / 25% season / 15% last 3) with pace and defensive matchup adjustments, every pick passes the Three-Lens Test (statistical + narrative + market intelligence), every parlay has documented correlation analysis, every slate passes the Four Horsemen audit, same-day injury reports are confirmed before any projections, and closing lines are recorded for CLV tracking. No gut-feel picks. No single-direction bias.

## Usage

```
/betting-edge                          # Tonight's full slate analysis
/betting-edge [team1] vs [team2]       # Specific game analysis
/betting-edge review                   # Log results, calibrate confidence model
/betting-edge bankroll                 # Set up or review bankroll strategy
```

## Mode Detection

Parse the user's input to determine mode:
- **"review"**, **"results"**, **"how did we do"** → Route to `skills/nba-betting-edge/workflows/performance-review-calibration.md`
- **"bankroll"**, **"sizing"**, **"kelly"** → Route to `skills/nba-betting-edge/workflows/bankroll-strategy-position-sizing.md`
- **Default** (no modifier, game names, player names) → Route to `skills/nba-betting-edge/workflows/game-day-research-picks.md`

---

## Steps

### Step 0 — Budget Gate

Read `.agent/perplexity-usage.json`. Estimate 2-3 Perplexity queries for this session (~$0.10-0.15 using `sonar-pro`).

- **If budget > $5**: Proceed with full research (3 queries).
- **If budget $2-5**: Run with 2 queries. Supplement with WebSearch for secondary data.
- **If budget < $2**: Degrade to WebSearch-only mode. Notify user: "Perplexity budget low — running with web search only. Data quality may be reduced."

### Step 1 — Load Context

1. **Always load**: `skills/nba-betting-edge/genius.md` (8 genius patterns — the analytical framework)
2. **Load the routed workflow** based on mode detection
3. **Jim O'Shaughnessy at Tier 0**: Reference his Four Horsemen Defense and behavioral arbitrage principles from the genius patterns (already embedded). Only escalate to loading his full AGENT.md if the user is on a losing streak and needs deeper behavioral coaching.

### Step 2 — Execute Workflow

Run the loaded workflow with full genius context. The workflow handles all phases internally.

### Step 3 — Performance Logging (Review Mode Only)

After the review workflow completes:
1. Log to Performance DB via `execution/log_performance.py`:
   ```bash
   python execution/log_performance.py log "NBA betting edge - [date] review" --skill nba-betting-edge --type review --quality [ROI-mapped score] --intent [confidence calibration accuracy] --expert [pattern effectiveness] --adversarial [edge sustainability] --status Keep --notes "[summary]"
   ```
2. Log individual bets via `execution/bet_tracker.py`
3. This feeds the autoresearch loop — Phase 1 (Feedback Ratchet) activates after 20+ entries

### Step 4 — Bet Tracking (Research Mode)

After the pick slate is delivered, remind the user:
- Log bets placed: `python execution/bet_tracker.py log "[Player]" [prop] [line] [direction] --projection [X] --confidence [N] --stake [amount]`
- Tomorrow, run `/betting-edge review` to log results and calibrate

---

## Data Sources

### Real Stats — NBA.com via nba_api (PRIMARY for projections)
Pull actual game logs, season averages, and team stats via `execution/nba_stats.py`:
```bash
python execution/nba_stats.py player "Nikola Jokic"                     # Season averages
python execution/nba_stats.py gamelog "Nikola Jokic" --games 10          # Last 10 game logs
python execution/nba_stats.py projection "Nikola Jokic" points          # Weighted 60/25/15 projection
python execution/nba_stats.py teams                                      # All team pace + defensive ratings
python execution/nba_stats.py matchup "Nikola Jokic" "Spurs"            # Full matchup context
```
**This replaces Perplexity for all statistical data.** Never estimate stats from web searches when the API has real data.

### Projection Engine — Edge Detection
Full edge analysis combining stats + lines via `execution/projection_engine.py`:
```bash
python execution/projection_engine.py analyze "Nikola Jokic" points "Spurs" --line 28.5
python execution/projection_engine.py batch props.json --bankroll 100    # Batch analysis
```
**Outputs**: matchup-adjusted projection, edge magnitude, confidence score, Kelly sizing.

### Live Odds — The Odds API
Pull real sportsbook lines via `execution/odds_fetcher.py` (Pattern 9: Line Shopping Edge):
```bash
python execution/odds_fetcher.py games              # Tonight's games + event IDs
python execution/odds_fetcher.py lines              # Spreads, totals, moneylines (all books)
python execution/odds_fetcher.py props <event_id>   # Player props with multi-book comparison
python execution/odds_fetcher.py usage              # Check API budget (500 req/month)
```
**Always run `games` → `lines` → `props` before analysis.** This eliminates the Ignorance Horseman on lines.

### Bet Tracking + CLV
Record bets and track closing line value via `execution/bet_tracker.py`:
```bash
python execution/bet_tracker.py log "[Player]" [prop] [line] [direction] --projection [X] --confidence [N] --stake [amount]
python execution/bet_tracker.py close [bet_id] [closing_line]   # Record closing line at game time
python execution/bet_tracker.py result [bet_id] [actual] [outcome]
python execution/bet_tracker.py clv                              # CLV analysis (gold standard metric)
```

### Perplexity — Injury Reports & Narrative Context ONLY
Perplexity is now used ONLY for data that nba_api cannot provide:
- Same-day injury reports and lineup confirmations
- Narrative context (revenge games, playoff implications, coaching changes)
- Line movement and sharp money signals

**Slate scan** (Phase 1):
"NBA games [today's date] full injury report confirmed starting lineups back-to-back schedule"

**Do NOT use Perplexity for**: player stats, season averages, game logs, team pace/ratings — use nba_stats.py instead.

---

## Confidence → Kelly Sizing Quick Reference

| Confidence | Label | Edge Required | Max Stake | Parlay Eligible |
|-----------|-------|--------------|-----------|----------------|
| 5 | Lock | > 5 pts | 4-5% bankroll | Yes (anchor leg) |
| 4 | Strong | > 3 pts | 3-4% bankroll | Yes |
| 3 | Lean | > 1 pt | 2-3% bankroll | Yes (secondary) |
| 2 | Marginal | Any | 1% max | No |
| 1 | Skip | Any | No bet | No |

**Daily limits**: Max 15% total exposure. Max 5% single bet. Max 2% per parlay.
