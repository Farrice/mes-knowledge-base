# Router Report Card — 2026-07-17 07:00

Weekly glance at the router learning loop: `skill_router_hook` (suggest) -> `routing-intelligence.json` (log) -> `session_ledger_hook` (reconcile auto_match/auto_miss) -> `run_routing_learning()` (nudge weights + surface synonym candidates).

## (a) Suggested-vs-Loaded Match Rate (7d)
- 34 decisions reconciled: **29.4% match rate** (auto_match 10, auto_miss 24).

## (b) Skill Weight Movers (vs 1.0 baseline)
**Top gainers:**
- `dara-denney-meta-ads` -> 1.75 (+0.75)
- `jenny-hoyos-shorts` -> 1.4 (+0.4)
- `seena-rez-tiktok-commerce` -> 1.4 (+0.4)
- `joey-cinema-os` -> 1.31 (+0.31)
- `kallaway-illusion-of-novelty` -> 1.31 (+0.31)

**Top losers:**
- `brand-operating-system` -> 0.5 (-0.5)
- `david-bayer-elite-communication` -> 0.5 (-0.5)
- `david-placek-naming` -> 0.5 (-0.5)
- `design-md` -> 0.5 (-0.5)
- `doc-coauthoring` -> 0.5 (-0.5)

## (c) Abstention / Gap Count
- 0 gap(s) logged in the last 7d (2 total on record).

## (d) Pending Synonym Candidates
- 5 candidate(s) awaiting human review -> `.agent/synonym-candidates.md`

## (e) Health Check — Is the Loop Alive?
- 163 routing decision(s) logged in the last 7d — loop is live.
