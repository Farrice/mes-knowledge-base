# Router Report Card — 2026-08-24 07:00

Weekly glance at the router learning loop: `skill_router_hook` (suggest) -> `routing-intelligence.json` (log) -> `session_ledger_hook` (reconcile auto_match/auto_miss) -> `run_routing_learning()` (nudge weights + surface synonym candidates).

## (a) Suggested-vs-Loaded Match Rate (7d)
- 1 decision(s) reconciled — too early to trend confidently (auto_match 0 / auto_miss 1, 0.0% match).

## (b) Skill Weight Movers (vs 1.0 baseline)
**Top gainers:**
- `april-dunford-positioning` -> 1.74 (+0.74)
- `creative-campaign-strategy` -> 1.74 (+0.74)
- `ethan-smith-aeo` -> 1.74 (+0.74)
- `geoff-woods-ai-thought-partner` -> 1.74 (+0.74)
- `seena-rez-tiktok-commerce` -> 1.73 (+0.73)

**Top losers:**
- `corey-mcclain-persona-engineering` -> 0.5 (-0.5)
- `doc-coauthoring` -> 0.5 (-0.5)
- `nate-b-jones-context-engineering` -> 0.5 (-0.5)
- `supercomputer` -> 0.5 (-0.5)
- `ben-watkins-storytelling` -> 0.58 (-0.42)

## (c) Abstention / Gap Count
- 0 gap(s) logged in the last 7d (4 total on record).

## (d) Pending Synonym Candidates
- 22 candidate(s) awaiting human review -> `.agent/synonym-candidates.md`

## (e) Health Check — Is the Loop Alive?
- 220 routing decision(s) logged in the last 7d — loop is live.
