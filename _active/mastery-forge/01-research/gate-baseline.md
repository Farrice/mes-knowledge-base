# Oracle Graduation Gate — Baseline Audit (2026-08-06)

## What the ledger claimed vs what it holds

`paper_trader.py status` showed **264 settled bets, 56.4% hit rate, +21.3% ROI** — which naively passes the 200-bet graduation bar. Audit findings:

1. **226 of 264 bets are backfills** (`"backfilled": true, type: paper-backfill`) — retroactively reconstructed, not prospectively logged. Honest prospective record: **38 bets, 57.9%** (small sample, ~1 week in March 2026).
2. **Closing lines were captured for 1 of 264 bets** (in `.agent/bet-tracking.json`, 0 of 264 in the paper log) — CLV, the #1 edge indicator, is effectively unmeasured.
3. **Confidence calibration is inverted**: C3=62%, C4=57%, C5=50%. Highest-confidence picks perform worst. The confidence scorer is adding noise, not signal.
4. Gate verdict before fix: NO-GO (correctly), but its bet-count criterion was counting backfills toward the 200.

## Fixes shipped today

- `execution/live_trader.py check_gate()` — **prospective-only counting**. Backfilled bets excluded from all four criteria; excluded count reported as context. New honest baseline: `38/200 prospective · hit 57.9% PASS · CLV pending (0 pts) · calibration FAIL`.
- `execution/paper_trader.py closes` — **automatic closing-line capture**: fetches current lines for all pending bets near game start (grouped per event to conserve Odds API quota), records `closing_line` + `clv` per bet. CLV accrues from bet one of the new exam window.
- `.agent/workflows/picks-tonight.md` — Step 9 (closing-line discipline), Graduation line on the pick card, and **Oracle Mode** section: when the gate returns GO, cards become ready-to-place slips (stake, book, receipt); Farrice places them; the system never touches money.

## Open items for the exam window

- **Season gap**: pipeline is NBA-only (`odds_fetcher.SPORT='basketball_nba'`); no NBA lines until late October. Decision needed on interim cadence (deep-research brief in flight covers MLB/WNBA/event-market feasibility).
- **Calibration fix**: confidence scorer needs re-derivation before the new window — otherwise C5 keeps failing the gate. Candidate for Phase A corpus work.
- 200 prospective bets at ~5/day ≈ 6-8 weeks of nightly slates once lines are live.
