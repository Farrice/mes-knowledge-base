---
thread: mastery-forge
status: ready
resume_hint: WNBA port next (odds_fetcher sport param + WNBA stats feed) then Platt calibration — exam starts ticking; human-pending: 5 sends, Chris text, gws auth, ntfy
unfinished: WNBA port, calibration layer, CLV data accrual; god-agent first instance awaits Farrice's Chris text
branch: main
pin: true
---

# Mastery Forge — Oracle Round 1 + God Agent Uncage (dashboard live, forge born)

## Purpose
- **Next session should do:** the WNBA port — parameterize `execution/odds_fetcher.py` (SPORT is hardcoded `basketball_nba`) so `paper_trader.py` / `picks-tonight` can run `basketball_wnba`, stand up a WNBA stats source for `execution/projection_engine.py`, and generate the first real prospective WNBA paper slate tonight. Then ship the Platt-scaling calibration layer (feature-leakage shallow-tree check first) per `skills/nba-betting-edge/references/oracle-2026-research.md` §3, with an ECE readout wired into `live_trader.py check`.
- **Not in scope:** real-money anything (gate is NO-GO: 38/200 prospective), the prediction-markets/Kalshi track (separate ledger, later), re-researching anything (52-source brief is on disk), re-extracting the God Agent video, selling the god-agent offer (uncaged but first move is Chris's $0 proof install — Farrice sends the text himself).

## Load First
- `_active/knowledge/mastery-forge/INDEX.md` — project doctrine, decisions, Oracle quick reference
- `_active/knowledge/mastery-forge/01-research/gate-baseline.md` — honest ledger state + open items
- `skills/nba-betting-edge/references/oracle-2026-research.md` — edge sources, no-vig CLV method, calibration fix path, WNBA lane rationale
- `~/.claude/plans/i-need-you-to-joyful-fountain.md` — the living plan (Parts 1-4, expand never replace)

## Current State
- **Objective:** a forged betting master under a falsifiable graduation exam; it decides, Farrice executes; real money locked until `live_trader.py check` says GO (200+ prospective bets, >53%, positive CLV, calibrated confidence).
- **What is already done (2026-08-06, all committed on main):** gate integrity (226 backfills excluded; prospective baseline 38/200 · 57.9%); `paper_trader.py closes` (CLV auto-capture) + quota persistence in `odds_fetcher.api_request`; Oracle Board v2 LIVE cockpit at `http://127.0.0.1:8765/oracle` (pulse_serve `/oracle` route, 3 allow-listed actions with CLI twins, system-activity strip, ROI splits, drill-downs, demo mode, nav quad) — every action verified over HTTP; event listener + Desktop "Agent Inbox" + weekly harness-evals/verdict-to-diff card minters + notify.py (all launchd-loaded); God Agent harvest (riley-brown corpus extension + delta memo, all 5 adoptable moves SHIPPED); god-agent offer UNCAGED with Miller positioning package + Chris 2-week proof-install plan + demo kit (`_active/knowledge/mastery-forge/02-offer/`); Sean Perry verified (poker pro; replicable part = receipts-driven content lane, plan Part 3F).
- **What is uncertain or stale:** Odds API remaining quota (UNCONFIRMED until first line fetch; page shows it once `.agent/odds-api-quota.json` populates); WNBA stats source for the projection engine not yet chosen (the NBA engine reads `execution/nba_stats.py` — a WNBA equivalent is the port's real work); C5 confidence inversion stands until calibration ships; gmail/calendar listener sources SKIPPED until Farrice runs `gws auth login`.
- **Latest proof/receipt:** live-server battery 2026-08-06 ~13:00 — all 3 oracle actions `{ok:true}` with real side effects (note→minted card `card-event-inbox-2026-08-06-oracle-note-130348.md`), jail holds, siblings regression-clean; finalize rows 8.33/8.33/8.0/8.33 PASS in `knowledge/log.md`.

## Suggested Skills / Workflows
- `/oracle-board` — the live cockpit (serve-first; static fallback `python3 execution/oracle_dashboard.py --open`)
- `/picks-tonight` — nightly slate once WNBA lines flow; Step 9 closes discipline
- `/betting-edge` + `/edge-validation-sizing` — the domain skills the port extends
- `python3 execution/live_trader.py check` — graduation readout after any slate

## Exact Next Prompt
```text
Continue the Mastery Forge / Oracle project (thread: mastery-forge). Read
_active/knowledge/mastery-forge/INDEX.md, 01-research/gate-baseline.md, and
skills/nba-betting-edge/references/oracle-2026-research.md first.

Build 1 — WNBA port: parameterize execution/odds_fetcher.py (SPORT hardcoded
basketball_nba) so paper_trader.py and picks-tonight run basketball_wnba too;
stand up a WNBA stats source for execution/projection_engine.py (nba_stats.py
is the NBA analog). Done = a real WNBA paper slate generated tonight, logged
prospectively, closes captured before tip-off.

Build 2 — calibration: feature-leakage shallow-tree check on projection
features, then a Platt-scaling layer over confidence scores with an ECE
readout in live_trader.py check (research brief §3; <1,000 samples = Platt).

Binding: prospective-only counting, separate ledger per lane, no real money
(decides-he-executes), cost card on anything new, verify everything you claim
(run it, screenshot it) before reporting.
```

## Acceptance Criteria
- `paper_trader.py slate` produces a WNBA slate from live lines; bets logged with `event_id`, prospective class.
- `paper_trader.py closes` captures WNBA closing lines; CLV data points > 0 on the gate readout.
- Calibration layer merged: gate calibration row driven by Platt-adjusted scores + ECE shown; leakage check result documented in `_active/knowledge/mastery-forge/01-research/`.
- Oracle Board reflects all of it after one refresh; Odds API quota visible on-page.

## Risk Notes
- Odds API free-tier budget is finite and now the exam's fuel — batch requests per event (existing pattern), watch the on-page quota readout.
- WNBA player-name matching may differ from `nba_stats.find_player`; verify before trusting projections (factual veto applies to any stated stat).
- Two-driver tree: a Codex session was active today (pulse/readout-os commits) — check `git status` before starting; never run both tools concurrently.
- Human-pending items (not the next session's to do, only to surface): five LinkedIn sends · Chris text (`positioning-plain-terms.md` §7) · `gws auth login` · ntfy `NTFY_TOPIC` in `.env`.

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
