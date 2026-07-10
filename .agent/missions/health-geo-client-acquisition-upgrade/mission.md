# Mission: Health GEO Client Acquisition Upgrade

## Charter
- Slug: health-geo-client-acquisition-upgrade
- Mode: code
- Status: complete
- Goal: Enhance the Health Performance GEO daily automation into a client-acquisition content data moat for creative strategy, copywriting, ghostwriting, AEO, SEO, and GEO offers
- Created: 2026-06-23T13:55:16+00:00
- Updated: 2026-06-23T14:00:13+00:00
- Librarian: complete

## Validation Contract
- Define correctness before execution.
- Assign every feature or workstream to at least one assertion.
- Run scrutiny and user-outcome validators at milestone boundaries.

| ID | Assertion | Covered by | Validator | Pass signal |
|---|---|---|---|---|
| VA1 | Automation prompt explicitly converts daily intelligence into client-acquisition content, audits, and offer bridges. | U1 | rg Client Acquisition Opportunity Map AUTOMATION_PROMPT.md | Required section exists |
| VA2 | Service ladder progresses from audit to ghostwriting/copywriting to AEO SEO GEO to creative strategy. | U2 | read SERVICE_LADDER.md | Rungs are present in order |
| VA3 | Polished offer source of truth exists locally. | U3 | test -f CLIENT_ACQUISITION_OFFER.md | Offer file exists and states positioning |

## Artifact Contract
- Type: engineering
- Root: `docs/mission-artifacts/health-geo-client-acquisition-upgrade`
- Rule: Strategy, requirements, U-ID plans, review, learning capture, and pulse reports are durable mission artifacts.

| Kind | Path | Status | Purpose |
|---|---|---|---|
| strategy_anchor | `docs/mission-artifacts/health-geo-client-acquisition-upgrade/strategy-anchor.md` | created | Mission strategy grounding; summarize STRATEGY.md when present or capture the guiding bet. |
| requirements | `docs/mission-artifacts/health-geo-client-acquisition-upgrade/requirements.md` | created | Requirements with stable R/A/F/AE identifiers before planning. |
| unit_plan | `docs/mission-artifacts/health-geo-client-acquisition-upgrade/plan.md` | created | Implementation or workstream plan with stable U-IDs, sequencing, risks, and tests. |
| review_ledger | `docs/mission-artifacts/health-geo-client-acquisition-upgrade/review.md` | created | Scrutiny and user-outcome review record, including residual work decisions. |
| solution_capture | `docs/mission-artifacts/health-geo-client-acquisition-upgrade/solution-capture.md` | created | Fresh solved-problem or reusable-knowledge capture for docs/solutions when generalizable. |
| pulse | `docs/mission-artifacts/health-geo-client-acquisition-upgrade/pulse.md` | created | Post-ship or post-delivery signal report, with docs/pulse-reports handoff when applicable. |


## Approved Package Load Set
- None recorded.


## Mission Activation Queue
| ID | Owner | Workflow/Skill | Status | Expected artifact | Evidence path | Assertion | Blocker | Next action |
|---|---|---|---|---|---|---|---|---|
| A1 | Oren Operational Systems | source-command-mission | complete | AUTOMATION_PROMPT.md upgraded to client-acquisition engine | _active/health-performance-ip-library/AUTOMATION_PROMPT.md | VA1 |  |  |
| A2 | Luke Iha plus Nicolas Cole | source-command-convene | complete | SERVICE_LADDER.md offer progression from audit to creative strategy | _active/health-performance-ip-library/04-deliverables/SERVICE_LADDER.md | VA2 |  |  |
| A3 | Farrice Engine offer layer | farrice-engine offer | complete | CLIENT_ACQUISITION_OFFER.md polished offer source of truth | _active/health-performance-ip-library/04-deliverables/CLIENT_ACQUISITION_OFFER.md | VA3 |  |  |

## Execution Receipt
- Planned lanes: A1, A2, A3
- Executed lanes: A1, A2, A3
- Skipped or blocked lanes: [none]
- Proof artifacts: _active/health-performance-ip-library/AUTOMATION_PROMPT.md, _active/health-performance-ip-library/04-deliverables/SERVICE_LADDER.md, _active/health-performance-ip-library/04-deliverables/CLIENT_ACQUISITION_OFFER.md
- Validators run: rg Client Acquisition Opportunity Map AUTOMATION_PROMPT.md, read SERVICE_LADDER.md, test -f CLIENT_ACQUISITION_OFFER.md
- Resume command: /mission resume health-geo-client-acquisition-upgrade

## Fresh Session Packet
- Required: True
- Fresh session packet: `[none]`
- Resume command: `/mission resume health-geo-client-acquisition-upgrade`
- Next command: `[none]`
- State sources: .agent/missions/health-geo-client-acquisition-upgrade/mission.json, .agent/intent-memory/current.json, .agent/system-cohesion-state.json
- Notes: [none]

## Handoffs
- 2026-06-23T13:58:45+00:00 | orchestrator | Upgraded Health Performance GEO automation into client-acquisition content data moat with prompt, ladder, offer brief, and mission artifacts.
