# Router Report Card — 2026-08-08 18:38

Weekly glance at the router learning loop: `skill_router_hook` (suggest) -> `routing-intelligence.json` (log) -> `session_ledger_hook` (reconcile auto_match/auto_miss) -> `run_routing_learning()` (nudge weights + surface synonym candidates).

## (a) Suggested-vs-Loaded Match Rate (7d)
- 8 decisions reconciled: **12.5% match rate** (auto_match 1, auto_miss 7).

## (b) Skill Weight Movers (vs 1.0 baseline)
**Top gainers:**
- `april-dunford-positioning` -> 1.88 (+0.88)
- `creative-campaign-strategy` -> 1.88 (+0.88)
- `ethan-smith-aeo` -> 1.88 (+0.88)
- `geoff-woods-ai-thought-partner` -> 1.88 (+0.88)
- `seena-rez-tiktok-commerce` -> 1.87 (+0.87)

**Top losers:**
- `corey-mcclain-persona-engineering` -> 0.5 (-0.5)
- `doc-coauthoring` -> 0.5 (-0.5)
- `nate-b-jones-context-engineering` -> 0.5 (-0.5)
- `supercomputer` -> 0.5 (-0.5)
- `voice-os` -> 0.57 (-0.43)

## (c) Abstention / Gap Count
- 0 gap(s) logged in the last 7d (3 total on record).

## (d) Pending Synonym Candidates
- 20 candidate(s) awaiting human review -> `.agent/synonym-candidates.md`

## (e) Health Check — Is the Loop Alive?
- 175 routing decision(s) logged in the last 7d — loop is live.
