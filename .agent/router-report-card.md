# Router Report Card — 2026-08-16 10:00

Weekly glance at the router learning loop: `skill_router_hook` (suggest) -> `routing-intelligence.json` (log) -> `session_ledger_hook` (reconcile auto_match/auto_miss) -> `run_routing_learning()` (nudge weights + surface synonym candidates).

## (a) Suggested-vs-Loaded Match Rate (7d)
- 1 decision(s) reconciled — too early to trend confidently (auto_match 1 / auto_miss 0, 100.0% match).

## (b) Skill Weight Movers (vs 1.0 baseline)
**Top gainers:**
- `april-dunford-positioning` -> 1.82 (+0.82)
- `creative-campaign-strategy` -> 1.82 (+0.82)
- `ethan-smith-aeo` -> 1.82 (+0.82)
- `geoff-woods-ai-thought-partner` -> 1.82 (+0.82)
- `seena-rez-tiktok-commerce` -> 1.81 (+0.81)

**Top losers:**
- `corey-mcclain-persona-engineering` -> 0.5 (-0.5)
- `doc-coauthoring` -> 0.5 (-0.5)
- `nate-b-jones-context-engineering` -> 0.5 (-0.5)
- `supercomputer` -> 0.5 (-0.5)
- `voice-os` -> 0.63 (-0.37)

## (c) Abstention / Gap Count
- 1 gap(s) logged in the last 7d (4 total on record).

## (d) Pending Synonym Candidates
- 20 candidate(s) awaiting human review -> `.agent/synonym-candidates.md`

## (e) Health Check — Is the Loop Alive?
- 172 routing decision(s) logged in the last 7d — loop is live.
