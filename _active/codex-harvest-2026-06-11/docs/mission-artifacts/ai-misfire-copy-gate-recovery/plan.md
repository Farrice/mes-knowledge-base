# Unit Plan: AI Misfire Copy Gate Recovery

Created: 2026-05-10
Mission: ai-misfire-copy-gate-recovery

Stable-ID rule: never renumber existing U-IDs after reordering, splitting, or deleting units.

## Implementation Units
- U1. **Failure Evidence Lock**
  - Covers: R3
  - Scope: routing/performance logs and mission artifacts.
  - Decision: Treat false Copy Gate PASS as a misroute and performance failure.
  - Tests or verification: routing/performance log IDs recorded in review ledger.
  - Dependencies: none
- U2. **Copy Rebuild**
  - Covers: R1, R4, AE2
  - Scope: four active AI Misfire revenue-suite source copies.
  - Decision: Rebuild around "AI output as x-ray of the missing marketing system," with attention-jack opening and artifact-first CTA.
  - Tests or verification: extracted publishable sections pass prose check, active-suite guard, and manual calibration review.
  - Dependencies: U1
- U3. **Copy Gate Calibration Guard**
  - Covers: R2, AE1, AE3
  - Scope: `execution/publishable_copy_guard.py`.
  - Decision: Current-intent Copy Gates must include user baseline, failure addressed, score discipline, and cannot use classifier-only review or 9+ scores without proof.
  - Tests or verification: guard run against active suite plus targeted score-inflation fixture.
  - Dependencies: U1

## Sequencing
1. U1
2. U2
3. U3

## Risks
- Risk: The copy becomes "clever" but not clear. Mitigation: every hook resolves into the buyer's private "I cannot ship this" artifact moment.
- Risk: Guard becomes ceremony with more required words. Mitigation: add numeric score-inflation checks and classifier-only failure, not just required labels.
- Risk: News-jack ages quickly. Mitigation: keep source links and refresh before posting if the current enterprise-agent conversation cools.

## Validation Mapping
| Assertion | Covered by U-ID | Validator | Pass signal |
|---|---|---|---|
| False 9+ Copy Gate scores are blocked | U3 | `publishable_copy_guard.py` | Active suite passes only after score discipline; high-score fixture fails. |
| Active copy is rebuilt from newest intent | U2 | active-suite guard and manual review | Four active docs remain; flagship post uses marketing-void thesis and no stale full pack. |
| Failure is logged for future learning | U1 | routing/performance logs | Log IDs exist and review ledger records them. |
