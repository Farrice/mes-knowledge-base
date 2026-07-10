# Router Report Card — 2026-07-09 07:00

Weekly glance at the router learning loop: `skill_router_hook` (suggest) -> `routing-intelligence.json` (log) -> `session_ledger_hook` (reconcile auto_match/auto_miss) -> `run_routing_learning()` (nudge weights + surface synonym candidates).

## (a) Suggested-vs-Loaded Match Rate (7d)
- 12 decisions reconciled: **8.3% match rate** (auto_match 1, auto_miss 11).

## (b) Skill Weight Movers (vs 1.0 baseline)
**Top gainers:**
- `dara-denney-meta-ads` -> 1.33 (+0.33)
- `strength-conditioning-os` -> 1.18 (+0.18)
- `satori-graphics` -> 1.13 (+0.13)
- `swarm-commander` -> 1.13 (+0.13)
- `chief-of-staff-os` -> 1.08 (+0.08)

**Top losers:**
- `supercomputer` -> 0.5 (-0.5)
- `david-placek-naming` -> 0.62 (-0.38)
- `design-md` -> 0.67 (-0.33)
- `creative-direction` -> 0.72 (-0.28)
- `brand-operating-system` -> 0.77 (-0.23)

## (c) Abstention / Gap Count
- 2 gap(s) logged in the last 7d (2 total on record).

## (d) Pending Synonym Candidates
- 2 candidate(s) awaiting human review -> `.agent/synonym-candidates.md`

## (e) Health Check — Is the Loop Alive?
- 201 routing decision(s) logged in the last 7d — loop is live.
