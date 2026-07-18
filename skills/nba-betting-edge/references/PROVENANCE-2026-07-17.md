# PROVENANCE — nba-betting-edge repair

Anchor → source file+location. Full claim ledger: `references/source-ledger.md`.

| Anchor (in repaired `genius.md`) | Source file + location | Label |
|---|---|---|
| "The Arbitrage of Human Nature" / "Four Horsemen Defense" pattern names, used in "How to Use This Skill" and Anti-Patterns framing | `skills/jim-oshaughnessy-philosopher-financier/references/genius-patterns.md:7-11,55-58` | VERIFIED |
| Anti-Pattern 1: Anthony Edwards / KAT injury-gate miss, 2025-12-05 | `skills/nba-betting-edge/genius.md` (pre-existing) Hall of Fame "Anti-Exemplar" | LIKELY (carried forward, not authored) |
| Anti-Pattern 2: 10/10 UNDER slate bias, 2026-03-14 | `skills/nba-betting-edge/genius.md` (pre-existing) Pattern 10 calibration note | LIKELY (carried forward, not authored) |
| Anti-Pattern 3: 264-bet confidence recalibration, 2026-03-21 | `skills/nba-betting-edge/genius.md` (pre-existing) Evolution Log; corroborated live in `execution/projection_engine.py:78-137` (`score_confidence()` docstring + logic) | VERIFIED |
| Anti-Pattern 4: assists strong-edge 0.0% hit, n=1 | `.agent/backtest-results/backtest_assists_202526_20players.json` | VERIFIED |
| Anti-Pattern 5: rebounds strong-edge 20.0% hit, n=5 | `.agent/backtest-results/backtest_rebounds_202526_20players.json` | VERIFIED |
| "How to Use" 2025-26 points model figures (54.0% hit, 52.4% breakeven, 154 strong-edge bets at 57.8%) | `.agent/backtest-results/backtest_points_202526_20players.json` | VERIFIED |
| No `extractions/` transcript exists for Jim O'Shaughnessy | Verified absence via `ls extractions/ | grep -i shaughnessy` (empty) and `grep -rl "O'Shaughnessy" extractions/` (only incidental hits in unrelated Tom Noske / Nick Saraev extraction reports) | Absence confirmed by real search, not assumed |
| Every other pattern (1-10), Evolution Log, Hall of Fame Exemplars 1-2, Signature Moves | `skills/nba-betting-edge/genius.md` (pre-existing, untouched content, preserved verbatim) | Pre-existing — not re-verified this repair (out of scope; additive-only) |
