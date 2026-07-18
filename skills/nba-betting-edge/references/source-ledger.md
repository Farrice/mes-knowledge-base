# NBA Betting Edge — Source Ledger

> Claim-by-claim provenance for `genius.md`. This skill is not a person-extraction
> (no `extractions/` transcript exists for Jim O'Shaughnessy — confirmed by `ls extractions/
> | grep -i shaughnessy` returning nothing). It is a home-built system that (a) adapts two
> named O'Shaughnessy patterns from `skills/jim-oshaughnessy-philosopher-financier/`, an
> in-repo skill file, not an interview transcript, and (b) tracks its own live performance
> data in `.agent/backtest-results/` and `.agent/bet-tracking.json`. Labels: VERIFIED (read
> the exact source, quote/number matches) / LIKELY (real entities, plausible, no primary
> file found to confirm the exact figure) / UNCONFIRMED (could not locate any source after
> a real search — listed, not silently dropped).

## O'Shaughnessy framework attribution

| Claim | Label | Source |
|---|---|---|
| "The Arbitrage of Human Nature" — Pattern 1, separating unchanging human-nature constants from surface dynamics | VERIFIED | `skills/jim-oshaughnessy-philosopher-financier/references/genius-patterns.md:7-11` and `genius.md:13` (verbatim pattern name + execute line present in both). |
| "The Four Horsemen Defense" — Fear/Greed/Hope/Ignorance pre-decision audit | VERIFIED | `skills/jim-oshaughnessy-philosopher-financier/references/genius-patterns.md:55-58` and `genius.md:61` (verbatim: "Am I being driven by fear? Greed? Hope? Am I simply ignorant of something crucial?"). |
| These two patterns trace to O'Shaughnessy's actual public work (books/interviews), not just this repo's paraphrase | UNCONFIRMED | No transcript or interview file exists under `extractions/` for O'Shaughnessy (checked: `ls extractions/ | grep -i shaughnessy` → empty; `grep -rl "O'Shaughnessy" extractions/` → only incidental mentions in unrelated Tom Noske / Nick Saraev extraction reports, not source material). The two patterns are grounded in-repo but their fidelity to O'Shaughnessy's actual published ideas ("Arbitrage of Human Nature," a real concept from his writing on behavioral finance) is LIKELY-but-not-source-verified from this session — flagging honestly rather than inventing a citation. |

## Live system data (the actual "expert record" for this skill)

| Claim | Label | Source |
|---|---|---|
| 2025-26 season points model: 54.0% overall hit rate, 52.4% breakeven, 154 "strong edge" bets at 57.8% hit, 1075 observations across 20 players | VERIFIED | `.agent/backtest-results/backtest_points_202526_20players.json` (fields: `overall_hit_rate`, `breakeven`, `strong_edge_hit_rate`, `strong_edge_count`, `total_observations` — read directly). |
| 2024-25 season points model: 56.5% hit, 66.0% strong-edge hit on 350 bets, 1348 observations | VERIFIED | `.agent/backtest-results/backtest_points_202425_20players.json`. |
| 2025-26 assists model: 53.4% overall hit, but strong-edge bucket is 0.0% on n=1 | VERIFIED | `.agent/backtest-results/backtest_assists_202526_20players.json`. |
| 2025-26 rebounds model: 53.5% overall hit, strong-edge bucket 20.0% on n=5 | VERIFIED | `.agent/backtest-results/backtest_rebounds_202526_20players.json`. |
| "264-bet backtest," CV<0.18 → 70-81% hit, CV>0.35 → 0-29% hit, Conf 3/4/5 = 59.5%/63.0%/66.7%, edge 1.5-3pts sweet spot vs. 3-5pts "suspicious" (47%) | VERIFIED | `execution/projection_engine.py:78-137`, function `score_confidence()` — docstring and inline comments state these exact figures ("Key insight from 264-bet backtest," "Calibration results on 264 bets: Conf 3: 59.5%..."). This is the code that currently runs; the genius.md Evolution Log entry (2026-03-21) is a faithful paraphrase of this same file, not an invented number. Note: the 264-bet backtest itself (raw per-bet results) is not saved anywhere in `.agent/backtest-results/` — only the code's summary of its findings survives; the aggregate figures are corroborated twice (docstring + genius.md) but the raw dataset is UNCONFIRMED/not recoverable in this repo. |
| Anthony Edwards OVER 28.5 anti-exemplar (vs. Pistons, 2025-12-05): KAT flips questionable→ACTIVE same day, Edwards finishes 23 | LIKELY | `skills/nba-betting-edge/genius.md` Hall of Fame "Anti-Exemplar" (pre-existing content, not added this repair). Real players/team, plausible scenario, but no archived box score or injury-report file exists in this repo to independently confirm the exact final line (23 pts) — narrative, not receipt. |
| Wembanyama return-from-absence 32/12/8/3 vs. 24.2 season avg (2026-03-14); Giannis DNP → MIL@ATL 122-99 under 227; Maxey OUT → BKN@PHI under 217.5 | LIKELY | `skills/nba-betting-edge/genius.md` Pattern 2 / Pattern 6 calibration notes (pre-existing). Real players, plausible game-log-shaped figures, but no cached game log or odds snapshot for these specific dates exists under `.agent/nba-cache/` or `.agent/backtest-results/` to verify the exact final scores. |
| Jokic OVER 26.5 vs. Blazers (2025-11-12); Maxey UNDER 27.5 vs. Celtics (2026-02-28) — Hall of Fame Exemplars | LIKELY | `skills/nba-betting-edge/genius.md` Hall of Fame Exemplars 1-2 (pre-existing). Same basis as above: real players/teams, no independently verifiable box-score file in-repo for these exact dates. |
| `.agent/bet-tracking.json` live ledger: Giannis rebounds UNDER 11.5 (2026-03-14, win, actual 6.0); Evan Mobley points UNDER 24.5 and Donovan Mitchell points UNDER 30.5 (both 2026-03-21, outcome pending) | VERIFIED | `.agent/bet-tracking.json` (read directly; 64 lines, 3 bet records, one settled). Not cited as an anti-pattern anchor in this repair (outcomes are null/inconclusive) but confirms the tracker is live and real, supporting the "not hypothetical" framing of the Anti-Patterns section. |

## Anti-Patterns section (added this repair) — anchor summary

All 5 items in `genius.md` § Anti-Patterns cite either (a) pre-existing in-skill narrative content (Edwards anti-exemplar, 10/10-UNDER calibration note — both LIKELY per above) or (b) files read directly this session with exact field values quoted (assists/rebounds backtest JSON, `projection_engine.py` — VERIFIED). No new narrative claims were invented; the two LIKELY-sourced items were already present in the skill before this repair and are carried forward, not authored fresh.
