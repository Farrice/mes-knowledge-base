# Router Report Card — 2026-08-31 07:00

Weekly glance at the router learning loop: `skill_router_hook` (suggest) -> `routing-intelligence.json` (log) -> `session_ledger_hook` (reconcile auto_match/auto_miss) -> `run_routing_learning()` (nudge weights + surface synonym candidates).

## (a) Suggested-vs-Loaded Match Rate (7d)
- 2 decision(s) reconciled — too early to trend confidently (auto_match 2 / auto_miss 0, 100.0% match).

## (b) Skill Weight Movers (vs 1.0 baseline)
**Top gainers:**
- `sean-dollwet-kdp-publishing` -> 1.69 (+0.69)
- `april-dunford-positioning` -> 1.64 (+0.64)
- `creative-campaign-strategy` -> 1.64 (+0.64)
- `ethan-smith-aeo` -> 1.64 (+0.64)
- `geoff-woods-ai-thought-partner` -> 1.64 (+0.64)

**Top losers:**
- `ben-watkins-storytelling` -> 0.5 (-0.5)
- `corey-mcclain-persona-engineering` -> 0.5 (-0.5)
- `doc-coauthoring` -> 0.5 (-0.5)
- `gemini-api-dev` -> 0.5 (-0.5)
- `nate-b-jones-context-engineering` -> 0.5 (-0.5)

## (c) Abstention / Gap Count
- 0 gap(s) logged in the last 7d (4 total on record).

## (d) Pending Synonym Candidates
- 24 candidate(s) awaiting human review -> `.agent/synonym-candidates.md`

## (e) Health Check — Is the Loop Alive?
- 277 routing decision(s) logged in the last 7d — loop is live.
