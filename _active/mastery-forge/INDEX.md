# Mastery Forge — Round 1: "The Oracle"

**Status:** active (opened 2026-08-06)
**Plan of record:** `~/.claude/plans/i-need-you-to-joyful-fountain.md` (approved 2026-08-06)
**Owner intent:** a meta-agent that learns a domain to *verified* mastery, then runs in production; Farrice keeps only the irreversible 10% (placing positions). First domain: prediction markets / sports. Execution boundary: **it decides, he executes** (SENDS-STAY-HUMAN analog; browser-automation-safety Tier 2).

## Doctrine (binding for this project)
- Mastery is graded by **falsifiable tests reality can check** — paper ledger, CLV, calibration, blind bars. Never by a critic agent (gauntlet-loop verdict, `directives/blind-bar-protocol.md`).
- The graduation gate IS the product. Paper-to-live gap receipts: sim 522x → live −49.5% (`skills/prediction-market-risk-management/SKILL.md`); 92.4% of Polymarket wallets unprofitable.
- Extend, never rebuild: `bet_tracker.py` / `paper_trader.py` / `live_trader.py` gate, `/deep-research`, `/extract`, forge-os F0–F7 spine.
- Real-money autonomy stays OFF until Farrice's explicit new decision (compass doctrine).

## Structure
- `01-research/` — gate baseline, God Agent delta memo, deep-research briefs
- (folders created as populated — org rule)

## Tracks
1. **God Agent harvest** — Riley Brown "They Built an AI 'God Agent' for 1,000 Employees" (HQXi4snP36I) → corpus extension of `extractions/riley-brown/` (new-video assets in `extractions/riley-brown-god-agent/`) → delta memo vs the Antigravity harness.
2. **The Oracle** — LEARN (deep-research + nba-betting-edge fusion) → VERIFY (paper loop w/ CLV capture from bet one) → GRADUATE (`live_trader.py check` gate) → PRODUCTION (nightly ready-to-place slip).
   - **Exam-lane decision (Farrice, 2026-08-06): BOTH — port the pipeline to WNBA props (Oracle's stats exam through October) AND stand up a prediction-markets track (Kalshi/Polymarket event contracts).** The two are separate disciplines (stats modeling vs information arb) and get separate ledgers — never blended into one track record. Next build: `odds_fetcher` sport parameterization + WNBA stats feed; prediction-market track starts from the 4 existing prediction-market skills (`/edge-validation-sizing` first), NOT the parked arb project.
3. **Phase D (later)** — extract the repeatable Forge pipeline into forge-os once the Oracle proves the shape.
