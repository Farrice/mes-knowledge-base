# NBA Betting Edge Skill — Genius Context

> Load this file before executing any workflow. It contains the full
> analytical framework — patterns, behavioral finance principles, and
> statistical edge detection methods that make this system actually work.

## Genius Patterns

8 betting-specific mastery behaviors decoded into executable frameworks. Rooted in Jim O'Shaughnessy's behavioral finance principles, adapted for NBA player prop markets.

---

## Pattern 1: The Line Inefficiency Detector
**Execute**: Vegas sets thousands of individual prop lines daily. Public money inflates lines on star players (Curry, LeBron, Luka) and prime-time nationally televised games. The edge lives where name recognition diverges from recent form. Check: Is this line priced for the player's reputation or their last 10 games?
**Success Metric**: Identify 2+ lines per slate where the gap between reputation-pricing and recent-form-pricing exceeds 2 points.

---

## Pattern 2: The Context Stack
**Execute**: A player's stat line is never context-free. Six variables create the real prediction — evaluate ALL six before touching any prop line:
1. **Pace of play** — opponent's tempo (possessions/game)
2. **Rest days** — back-to-back, 3-in-4, days off
3. **Home/Away** — most players have measurable home/away splits
4. **Defensive matchup** — opponent's defensive rating vs. position
5. **Minutes projection** — blowout risk, rotation changes, foul trouble history
6. **Return from absence** — players returning from injury/rest (1+ games missed) tend to SPIKE, not regress. The combination of fresh legs, motivation, and maintained usage share creates above-average performances. Factor this into projections as a +10-15% boost to the weighted projection. *Calibrated 2026-03-14: Wembanyama returned from 1-game absence and hit 32/12/8/3 vs. a 24.2 season avg.*

A "25.5 points" line means completely different things at home in a high-pace game vs. away on a back-to-back against the #1 defense. Never evaluate a prop without stacking all six.
**Success Metric**: Zero picks made without all six context variables documented.

---

## Pattern 3: Recency Bias Arbitrage
**Execute**: Adapted from O'Shaughnessy's Arbitrage of Human Nature (Pattern 1) — the public and even sharp bettors overweight the last 1-2 games. A player who scored 40 last game gets hammered on overs. A player in a 2-game slump gets hammered on unders. But a single game is noise, not signal.

**Weighting formula**:
- 10-game rolling average: **60%** weight
- Season average: **25%** weight
- Last 3 games: **15%** weight

Never let a single outlier game drive conviction. If the last game is 2+ standard deviations from the season average, it's an outlier — the market will overcorrect, and you take the other side.
**Success Metric**: Accurate identification of recency-bias-inflated lines that revert to mean within 3 games.

---

## Pattern 4: The Correlation Map (Parlay Architecture)
**Execute**: Parlays compound edge — but only if legs are independent or positively correlated. Before building any parlay, map the correlation structure:

- **Same-team players in projected blowouts**: Correlated UNDERS (starters sit in 4th quarter)
- **High-pace games**: Correlated OVERS for all players in the game
- **Usage redistribution**: When Player A is out, Player B's stats go UP — positive correlation for Player B overs
- **Opposing players**: Generally independent unless game flow is extreme

**Rules**:
- Same-game parlays REQUIRE correlation awareness
- Cross-game parlays should seek INDEPENDENT outcomes for true edge multiplication
- Never build a parlay where all legs depend on the same game flow scenario
- Max 3 legs — each additional leg compounds the house edge exponentially

**Success Metric**: Every parlay has documented correlation analysis. No "hope parlays" (uncorrelated long shots stacked for payout).

---

## Pattern 5: The Four Horsemen of Bad Bets
**Execute**: Adapted directly from O'Shaughnessy's Four Horsemen Defense (Pattern 9). Before finalizing any pick slate, run this audit:

1. **Fear**: "Am I avoiding this pick because this player burned me last time?" If yes — check the data, not the memory.
2. **Greed**: "Am I stacking this parlay because the payout is exciting?" If the payout drives the pick instead of the edge, cut legs until the edge drives the payout.
3. **Hope**: "Am I taking this line despite bad matchup data because he's 'due'?" Players are never "due." Regression to mean is statistical, not karmic.
4. **Ignorance**: "Am I betting this prop without checking injury reports, rest status, or the matchup?" If ANY of the Context Stack variables are unknown, the bet is uninformed.

**Hard rule**: If any Horseman is detected, the pick must be downgraded by 1 confidence level or removed entirely.
**Success Metric**: Four Horsemen audit documented on every final pick slate. Zero picks survive with an active Horseman.

---

## Pattern 6: The Injury Cascade (HARD GATE)
**Execute**: When a key player is OUT, the usage and opportunity for remaining players shifts. This is the single largest source of mispriced lines because books adjust slowly and incompletely.

**⚠️ HARD GATE**: No pick survives without same-day injury confirmation. Check the injury report for EVERY player being bet on AND every key teammate whose absence would change the analysis. A star player sitting (Giannis, Maxey, etc.) voids the prop AND changes the game total projection. This is not optional — it's a prerequisite that fires BEFORE any statistical work.

**Process**:
1. Check injury reports FIRST — before any statistical analysis. Pull same-day reports, not day-before.
2. For every OUT player, calculate redistributed usage:
   - Points: Redistribute based on usage rate and shot attempts
   - Assists: The backup point guard or secondary ballhandler absorbs
   - Rebounds: Big man rotation changes create the biggest mismatches
3. Check how the remaining players performed in previous games WITHOUT the injured player (this data is gold — books often don't fully price it in)
4. For players RETURNING from absence (1+ games missed): apply return-from-absence boost (+10-15% to projection). See Context Stack variable #6.

**The edge**: Books set lines based on season averages. When a starter is out, the line for the replacement/beneficiary is often too low because the season average includes games where the starter played.

**Dual impact**: Injuries affect BOTH player props AND game totals. A star player sitting kills the game total (fewer possessions from the bench unit, blowout risk increases → starters sit earlier). *Calibrated 2026-03-14: Giannis DNP turned MIL@ATL into a 122-99 blowout (221 total, under 227 line). Maxey OUT turned BKN@PHI into a 201-point grind (under 217.5 line).*
**Success Metric**: Zero picks placed without same-day injury confirmation for all relevant players.

---

## Pattern 7: The Pace Multiplier
**Execute**: Games with high combined pace (possessions per game) inflate ALL counting stats. Low-pace grind games suppress them. The pace differential between teams is a stronger predictor of total stats than individual player averages alone.

**Calibration**:
- Combined pace top-10 in league matchups: Add **+5-8%** to counting stat projections
- Combined pace bottom-10: Subtract **5-8%** from counting stat projections
- Extreme pace mismatches (top-5 vs. bottom-5): The faster team usually dictates pace at home, slower team dictates on road

**Application**: If Ja Morant averages 25 PPG but tonight's game projects as a top-5 pace matchup, the real projection is ~26-27. If the line is set at 24.5, that's a 2+ point edge.
**Success Metric**: Pace adjustment applied to every projection before edge calculation.

---

## Pattern 8: The Bankroll Constant
**Execute**: Adapted from O'Shaughnessy's systematic risk management — edge detection without position sizing is gambling, not investing. Every bet must be sized proportional to edge magnitude and confidence level.

**Kelly Criterion (simplified)**:
- **Fractional Kelly** (half-Kelly recommended): Bet size = (edge / odds) / 2
- This automatically sizes larger on high-confidence picks and smaller on marginal ones

**Hard limits**:
- Max single bet: **5%** of bankroll
- Max daily exposure: **15%** of bankroll
- Max parlay stake: **2%** of bankroll (higher variance = smaller size)
- Drawdown protocol: If bankroll drops 20% from peak, reduce all sizes by 50% until recovery

**The discipline test**: If you're tempted to bet more than Kelly suggests, a Horseman is active (usually Greed). If you're tempted to skip a bet that Kelly says to take, Fear is active.
**Success Metric**: Zero bets placed without explicit size calculation. Bankroll tracked to the dollar.

---

## Pattern 9: The Line Shopping Edge
**Execute**: Different sportsbooks price the same prop differently. Use `execution/odds_fetcher.py` to pull lines from DraftKings, FanDuel, BetMGM, Caesars, and others simultaneously. Always bet at the book with the best price — this is free edge.

**Process**:
1. Run `python execution/odds_fetcher.py props [event_id]` to get all player props with multi-book comparison
2. For each pick, identify the book offering the best OVER price (highest positive or least negative odds)
3. Compare lines across books — if one book has a line 0.5+ points different from consensus, that book is mispricing
4. A 15-cent odds difference (e.g., -105 vs. -120) on the same line is meaningful — over 100 bets, it's the difference between profit and loss

**Commands**:
```bash
python execution/odds_fetcher.py games              # Get event IDs
python execution/odds_fetcher.py lines              # Spreads, totals, moneylines
python execution/odds_fetcher.py props <event_id>   # Player props with book comparison
python execution/odds_fetcher.py props <event_id> --player "Nikola Jokic"  # Filter by player
python execution/odds_fetcher.py usage              # Check API request budget (500/month)
```

**Success Metric**: Every bet placed at the best available price across books. Average odds improvement of 5-10 cents per bet vs. single-book betting.

---

## Pattern 10: The Multi-Angle Conviction Test
**Execute**: Never default to OVER or UNDER based on a single thesis. Every pick must survive a structured adversarial process that argues BOTH sides before reaching a conclusion. The goal is to find where the REAL edge lives — sometimes that's OVER, sometimes UNDER, sometimes it's a skip. The system wins by being right, not by being consistently biased in one direction.

**Process — The Three-Lens Test**:
For every prop or game total, run all three lenses BEFORE picking a direction:

**Lens 1 — The Statistical Case**
What do the numbers say? Weighted projection (60/25/15), pace adjustment, matchup adjustment. This produces a raw number. Compare to line. Which side has the mathematical edge?

**Lens 2 — The Narrative Case (Devil's Advocate)**
Now argue the OPPOSITE of what the stats suggest. What story could make the stats wrong tonight?
- OVER arguments: Rivalry game → extra intensity. Playoff positioning → every possession matters. Player has something to prove (contract year, trade rumors, return from absence). Opponent's defense has regressed recently. Pace-up spot that the season average doesn't capture.
- UNDER arguments: Blowout risk → starters sit early. Back-to-back fatigue. Team has clinched/eliminated → low motivation. Key teammate returns → usage redistributed. Defensive matchup the stats haven't captured (recent lineup change, new defensive scheme).

**Lens 3 — The Market Intelligence Case**
What is the market telling you? Smart money and books have information you don't.
- If the line is significantly ABOVE the season average, ask WHY before assuming it's wrong. Sometimes the market knows about a matchup advantage, a revenge game, a minutes increase, or a role change that the season average doesn't reflect.
- If the line moves significantly from open to current, that's sharp money. Respect it — don't fight it without a strong reason.
- If all books agree on the same line, the line is probably fair. If one book diverges, THAT book might be mispricing.

**Decision Rule**:
- If all 3 lenses agree → Confidence 4-5. Strong conviction.
- If 2 of 3 agree → Confidence 3-4. Lean the direction of the majority.
- If lenses conflict → Confidence 1-2. Either skip or take the smallest position.
- If Lens 2 (narrative) is stronger than Lens 1 (stats) → Reduce confidence by 1 level. Stats should lead, but narrative can override when the context is genuinely unique.

**The anti-bias rule**: If you find yourself picking the same direction (OVER or UNDER) for 70%+ of picks on a given slate, STOP. Re-run Lens 2 on every pick. A legitimate edge doesn't always point the same direction — if it does, you're probably applying a bias, not reading the data.

*Calibrated 2026-03-14: First slate had 10/10 UNDER picks — a clear signal of single-thesis bias. While game total UNDERs went 3-1, player prop UNDERs went 1-1. The blanket UNDER approach left OVER value on the table (Wemby return-from-absence OVER was the right play at 28.5 with a 32-pt night). The system must read between the lines, not default to one side.*

**Success Metric**: No more than 70% of picks on any slate point the same direction. Every pick has documented Three-Lens analysis. Picks that survive all three lenses hit at a higher rate than single-lens picks.
