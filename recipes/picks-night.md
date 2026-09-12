---
job: picks-night
name: Betting picks night
family: harness
tier_default: T1
runs: 0
last_ratchet: never
---

## The job
From tonight's NBA slate to a shareable pick card with real statistical edge, confidence, and bet sizing — nothing bet without him.

## Sub-jobs / lanes
- L1 Load system — `skills/nba-betting-edge/genius.md`, bankroll from `.agent/bet-tracking.json` and `.agent/paper-trading.json` [parallel]
- L2 Games and lines — `python3 execution/odds_fetcher.py games`, `python3 execution/odds_fetcher.py lines` [parallel]
- L3 Injury check — Perplexity within `.agent/perplexity-usage.json` budget, else WebSearch [after: L2]
- L4 Game selection — skip spreads over 12, focus the 2 to 3 games with real edge [after: L3]
- L5 Props and projections — `execution/odds_fetcher.py props <event_id>`, `execution/projection_engine.py analyze` per focus game [after: L4]
- L6 Pick card — confidence scoring (1-5), bet sizing, shareable card [after: L5]
- L7 Track record — `/picks-status` dashboard update once results settle [after: L6]

## Ask me first
- Q: Real money or paper only tonight? · look first: `.agent/bet-tracking.json`, `.agent/paper-trading.json`
- Q: Any specific player he wants checked? · look first: nothing on disk — only if raised in chat

## Handles alone
Games and lines pull, injury check, game and prop selection, projections, confidence scoring, bet sizing, pick card, track record update.

## Comes back when
- No games tonight (say so and stop, never invent a slate)
- A confirmed OUT changes a prop he already flagged
- A bet size would exceed his standing bankroll rule

## Needs approval
Placing any real-money bet — this system produces the pick card only; placing stays his.

## Needs
`execution/odds_fetcher.py` · `execution/projection_engine.py` · `skills/nba-betting-edge` · `.agent/bet-tracking.json` · `.agent/perplexity-usage.json`.

## When it breaks
| Failure | Keep-going move | Ask when |
|---|---|---|
| no games tonight | say so, stop | never |
| Perplexity budget low | fall back to WebSearch for injuries | never skip the injury check |
| a player is confirmed OUT | void the prop; flag any returning player for a boost | always — a voided prop changes the card |

## Done means
Pick card produced with confidence and sizing for each pick · injury report cross-checked · nothing bet without him.

## Ratchet log
- none yet
