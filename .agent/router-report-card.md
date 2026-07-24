# Router Report Card — 2026-07-24 15:29

Weekly glance at the router learning loop: `skill_router_hook` (suggest) -> `routing-intelligence.json` (log) -> `session_ledger_hook` (reconcile auto_match/auto_miss) -> `run_routing_learning()` (nudge weights + surface synonym candidates).

## (a) Suggested-vs-Loaded Match Rate (7d)
- 36 decisions reconciled: **19.4% match rate** (auto_match 7, auto_miss 29).

## (b) Skill Weight Movers (vs 1.0 baseline)
**Top gainers:**
- `geoff-woods-ai-thought-partner` -> 2.0 (+1.0)
- `april-dunford-positioning` -> 1.85 (+0.85)
- `creative-campaign-strategy` -> 1.84 (+0.84)
- `ethan-smith-aeo` -> 1.78 (+0.78)
- `kallaway-illusion-of-novelty` -> 1.76 (+0.76)

**Top losers:**
- `brand-operating-system` -> 0.5 (-0.5)
- `corey-mcclain-persona-engineering` -> 0.5 (-0.5)
- `david-bayer-elite-communication` -> 0.5 (-0.5)
- `david-placek-naming` -> 0.5 (-0.5)
- `deliberate` -> 0.5 (-0.5)

## (c) Abstention / Gap Count
- 1 gap(s) logged in the last 7d (3 total on record).

## (d) Pending Synonym Candidates
- 8 candidate(s) awaiting human review -> `.agent/synonym-candidates.md`

## (e) Health Check — Is the Loop Alive?
- 215 routing decision(s) logged in the last 7d — loop is live.
