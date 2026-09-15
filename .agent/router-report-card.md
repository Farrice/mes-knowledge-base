# Router Report Card — 2026-09-15 07:00

Weekly glance at the router learning loop: `skill_router_hook` (suggest) -> `routing-intelligence.json` (log) -> `session_ledger_hook` (reconcile auto_match/auto_miss) -> `run_routing_learning()` (nudge weights + surface synonym candidates).

## (a) Suggested-vs-Loaded Match Rate (7d)
- 2 decision(s) reconciled — too early to trend confidently (auto_match 1 / auto_miss 1, 50.0% match).

## (b) Skill Weight Movers (vs 1.0 baseline)
**Top gainers:**
- `sean-dollwet-kdp-publishing` -> 1.57 (+0.57)
- `april-dunford-positioning` -> 1.52 (+0.52)
- `creative-campaign-strategy` -> 1.52 (+0.52)
- `ethan-smith-aeo` -> 1.52 (+0.52)
- `geoff-woods-ai-thought-partner` -> 1.52 (+0.52)

**Top losers:**
- `ben-watkins-storytelling` -> 0.62 (-0.38)
- `corey-mcclain-persona-engineering` -> 0.62 (-0.38)
- `doc-coauthoring` -> 0.62 (-0.38)
- `gemini-api-dev` -> 0.62 (-0.38)
- `nate-b-jones-context-engineering` -> 0.62 (-0.38)

## (c) Abstention / Gap Count
- 0 gap(s) logged in the last 7d (4 total on record).

## (d) Pending Synonym Candidates
- 24 candidate(s) awaiting human review -> `.agent/synonym-candidates.md`

## (e) Health Check — Is the Loop Alive?
- 227 routing decision(s) logged in the last 7d — loop is live.
