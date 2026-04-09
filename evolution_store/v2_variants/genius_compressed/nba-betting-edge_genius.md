# NBA Betting Edge — Genius Context

> Load before executing any workflow. Full analytical framework.

## Core Operating System

Edge detection through behavioral finance principles adapted for NBA player prop markets. Vegas misprices lines based on reputation, recency bias, and slow injury adjustments. The system exploits these inefficiencies using a weighted projection formula (60% 10-game rolling / 25% season / 15% last 3), mandatory six-variable context stacking, same-day injury confirmation as a HARD GATE, and a structured three-lens adversarial conviction test before every pick. Data pipeline: `execution/nba_stats.py` + `execution/projection_engine.py`. Perplexity for injury reports only.

---

## Genius Patterns (Compressed)

### GP1: The Line Inefficiency Detector
Public money inflates lines on star players and prime-time games. The edge lives where name recognition diverges from recent form. Check: is this line priced for the player's reputation or their last 10 games? Target: 2+ lines per slate where reputation-pricing vs. recent-form gap exceeds 2 points.

### GP2: The Context Stack
A stat line is never context-free. Evaluate ALL six variables before touching any prop: (1) Pace of play, (2) Rest days, (3) Home/Away, (4) Defensive matchup, (5) Minutes projection, (6) Return from absence (+10-15% boost for players returning from 1+ missed games — fresh legs, motivation, maintained usage). Zero picks without all six documented.

### GP3: Recency Bias Arbitrage
Public overweights last 1-2 games. Weighting formula: 10-game rolling average 60%, season average 25%, last 3 games 15%. A single game is noise. If last game is 2+ standard deviations from season average, it's an outlier — the market will overcorrect and you take the other side.

### GP4: The Correlation Map (Parlay Architecture)
Parlays compound edge only if legs are independent or positively correlated. Same-team in blowouts = correlated UNDERS. High-pace = correlated OVERS. Usage redistribution when Player A out = Player B OVERS. Max 3 legs. Cross-game parlays should seek independent outcomes. Never build a parlay where all legs depend on same game flow.

### GP5: The Four Horsemen of Bad Bets
Before finalizing any slate, audit: (1) Fear — avoiding a pick because the player burned you? (2) Greed — stacking parlays for exciting payouts? (3) Hope — taking a line despite bad data because he's "due"? (4) Ignorance — betting without checking injury/rest/matchup? If any Horseman is active, downgrade by 1 confidence level or remove entirely.

### GP6: The Injury Cascade (HARD GATE)
No pick survives without same-day injury confirmation for EVERY player being bet on AND key teammates. Check injury reports FIRST before any statistical work. For OUT players, calculate redistributed usage. For RETURNING players, apply +10-15% boost. Books set lines on season averages — when a starter is out, replacement/beneficiary lines are often too low. Injuries affect both player props AND game totals. Calibrated: Giannis DNP turned game into 221-total blowout (under 227 line).

### GP7: The Pace Multiplier
Combined pace top-10 matchups: add +5-8% to counting stat projections. Bottom-10: subtract 5-8%. Extreme pace mismatches: faster team dictates pace at home, slower on road. Always apply pace adjustment before edge calculation.

### GP8: The Bankroll Constant
Every bet sized proportional to edge magnitude and confidence. Half-Kelly: bet size = (edge / odds) / 2. Hard limits: max single bet 5% bankroll, max daily exposure 15%, max parlay stake 2%. Drawdown protocol: if bankroll drops 20% from peak, reduce all sizes by 50% until recovery. If tempted to bet more than Kelly suggests, Greed is active.

### GP9: The Line Shopping Edge
Different books price the same prop differently. Use `execution/odds_fetcher.py` to compare across DraftKings, FanDuel, BetMGM, Caesars. Always bet at the best price — a 15-cent odds difference over 100 bets is the difference between profit and loss.

### GP10: The Multi-Angle Conviction Test
Every pick must survive three lenses: (1) Statistical — weighted projection vs. line, which side has mathematical edge? (2) Narrative (Devil's Advocate) — argue the OPPOSITE of stats; what story could make stats wrong tonight? (3) Market Intelligence — what is the line movement telling you? Smart money and books have info you don't. Decision: 3 lenses agree = Conf 4-5; 2 of 3 = Conf 3-4; conflict = Conf 1-2 or skip. Anti-bias rule: if 70%+ picks point same direction, STOP and re-run Lens 2 on everything.

---

## Evolution Log

### 2026-03-21: Confidence Calibration Overhaul (v2.1) — KEPT
**Problem**: Confidence scores were flat (~56.5% across Conf 3/4/5). **Root cause from 264-bet backtest**: Player consistency (CV) is the #1 predictor (CV < 0.18 = 70-81% hit; CV > 0.35 = 0-29%). Edge magnitude was WRONG foundation (3-5 pts hit only 47% vs 59.5% for 1.5-3 pts). Points props hit 57.6%, rebounds/assists below breakeven. UNDER hits 59.2%, OVER 48.5%. **Change**: Rebuilt `score_confidence()` — CV as base score, 1.5-3 pt edge "sweet spot," non-points penalty, OVER picks need more context factors. **Result**: Calibration PASSES. Conf 3: 59.5%, Conf 4: 63.0%, Conf 5: 66.7% (monotonically increasing, 31.1pp spread vs prior 6.5pp).

---

## Hidden Knowledge

| # | Principle | Deploy |
|---|-----------|--------|
| HK1 | Player consistency (CV) is the #1 predictor of prop hit rate, not edge magnitude | Use CV as the base of confidence scoring; CV < 0.18 = high confidence zone |
| HK2 | Edge 1.5-3 pts is the sweet spot; 3-5 pts is suspicious (likely mispricing for a reason) | Treat large edges with skepticism, not excitement |
| HK3 | UNDER hits 59.2% vs OVER 48.5% — structural bias toward UNDER in player props | OVER picks require more context factors to justify than UNDER |
| HK4 | Return-from-absence players tend to SPIKE (+10-15%) due to fresh legs + motivation + maintained usage | Factor return boost into projections; this is consistently underpriced |
| HK5 | Injuries have dual impact — both player props AND game totals shift when a star sits | Always reassess game total projections when key players are OUT |

---

## Signature Moves

1. **The "Pre-Flight Injury Scan"** — Initiates daily workflow with injury report check and cross-reference of every player's status on the slate, especially key teammates. Deploy at start of daily analysis and 2 hours before game time.
2. **The "Six-Variable Gridlock"** — Populates full Context Stack (Pace, Rest, Home/Away, Defensive Matchup, Minutes, Return Status) before considering any prop direction. Deploy when evaluating any player prop for the first time.
3. **The "Adversarial Three-Lens Test"** — Constructs arguments for OVER, UNDER, and market pricing using Statistical, Narrative, and Market Intelligence lenses. Actively seeks to disprove initial thesis. Deploy when a strong statistical edge is detected.
4. **The "Kelly-Calibrated Stake"** — Feeds edge magnitude and odds into half-Kelly formula to determine precise bankroll allocation. Never manually inputs bet size. Deploy when finalizing any pick before placement.
5. **The "Best Price Sweep"** — Compares lines across all integrated sportsbooks via `odds_fetcher.py` to ensure bet is placed at most advantageous odds. Deploy after pick is finalized, just before execution.

---

## Expert-Specific Quality Rubric

| Criterion | 4 (Acceptable) | 7 (Good) | 10 (Savant) |
|-----------|----------------|----------|-------------|
| Context Stack Completeness | Some variables checked but gaps in documentation | All 6 variables addressed for most picks | All 6 variables documented for every pick with specific data points, never a gap |
| Injury Gate Compliance | Injury reports checked but not same-day confirmed for all relevant players | Same-day confirmation for primary targets but may miss teammate impact | Same-day confirmation for ALL relevant players AND key teammates, with usage redistribution calculated |
| Conviction Testing | Single-thesis picks based on one angle | Two lenses applied with some adversarial testing | Full three-lens adversarial test documented, anti-bias rule enforced, direction-agnostic conviction |
| Bankroll Discipline | Bets sized by feel or flat-staked | Kelly-informed sizing but without strict adherence to limits | Half-Kelly calculated for every bet, hard limits enforced, drawdown protocol active |
| Recency Bias Detection | Some awareness of outlier games but weighting inconsistent | Weighted formula applied but occasional emotional override | Strict 60/25/15 weighting with outlier detection at 2+ SD, taking the other side of market overcorrections |
