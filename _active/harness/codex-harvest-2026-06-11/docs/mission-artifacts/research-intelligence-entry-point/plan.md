# Unit Plan: Vibe Tax Brief Expert Council Entry Point

Created: 2026-05-11
Mission: research-intelligence-entry-point

Stable-ID rule: never renumber existing U-IDs after reordering, splitting, or deleting units.

## Implementation Units
- U1. **Active package**
  - Covers: R1, R2, R3, R4, R5, AE1, AE2, AE3
  - Scope: `_active/research-intelligence-entry-point/`
  - Decision: one package, not a parallel system; AI remains backstage in buyer-facing copy.
  - Tests or verification: file inventory, artifact/export guards, copy guard, manual review.
  - Dependencies: none
- U2. **Revenue surface promotion**
  - Covers: R6, AE4
  - Scope: `_active/cash-first-service-menu/`, `_active/service-first-productization/`, `.agent/workflows/service-first-productization.md`
  - Decision: promote Vibe Tax as primary while preserving support lanes.
  - Tests or verification: search for stale primary defaults and routing references.
  - Dependencies: U1
- U3. **Research routing context**
  - Covers: R6, AE4
  - Scope: `.agent/workflows/research-intelligence-agent.md`
  - Decision: Research Intelligence Agent loads the active package for buyer-language/market-brief prompts.
  - Tests or verification: command/workflow router searches and skill validation.
  - Dependencies: U1
- U4. **Mission and governance**
  - Covers: R7
  - Scope: `.agent/missions/research-intelligence-entry-point/`, `docs/mission-artifacts/research-intelligence-entry-point/`
  - Decision: keep a durable artifact trail and library decision.
  - Tests or verification: `mission_control.py validate`.
  - Dependencies: U1-U3

## Sequencing
1. U1
2. U2
3. U3
4. U4

## Risks
- Name feels too casual: pair "Vibe Tax" with "False Signal Diagnostic" and proof-heavy brief sections.
- Offer drifts into generic research: enforce keep/revise/stop/test and concrete buyer-language outputs.
- Social copy becomes clever but shallow: require first-50 gate, mini-example, and manual CTA.
- Routing conflict with AI Misfire: preserve AI Misfire as optional content-lane offer, not primary.

## Validation Mapping
| Assertion | Covered by U-ID | Validator | Pass signal |
|---|---|---|---|
| Active package exists and is complete | U1 | file inventory | required files present |
| Written package uses native artifact/source rules | U1 | artifact/export guards | no unrequested external exports |
| Public copy avoids generic AI/research language | U1 | publishable copy guard + manual copy gate | no banned phrases or ceremonial pass |
| Existing revenue surfaces point to Vibe Tax | U2 | targeted search | primary defaults updated |
| Research Intelligence Agent knows active package | U3 | targeted read/search | canonical service surface present |
| Mission state is valid | U4 | mission control validate | validation passes |
