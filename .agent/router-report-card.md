# Router Report Card — 2026-07-06 09:18

Weekly glance at the router learning loop: `skill_router_hook` (suggest) -> `routing-intelligence.json` (log) -> `session_ledger_hook` (reconcile auto_match/auto_miss) -> `run_routing_learning()` (nudge weights + surface synonym candidates).

## (a) Suggested-vs-Loaded Match Rate (7d)
- 1 decision(s) reconciled — too early to trend confidently (auto_match 0 / auto_miss 1, 0.0% match).

## (b) Skill Weight Movers (vs 1.0 baseline)
- (no `.agent/skill-weights.json` yet — no weight nudges recorded)

## (c) Abstention / Gap Count
- 1 gap(s) logged in the last 7d (1 total on record).

## (d) Pending Synonym Candidates
- 0 candidate(s) awaiting human review -> `.agent/synonym-candidates.md`

## (e) Health Check — Is the Loop Alive?
- 70 routing decision(s) logged in the last 7d — loop is live.
