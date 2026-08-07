# Unit Plan: System Cohesion Silver Platter Audit

Created: 2026-05-11
Mission: system-cohesion-silver-platter-audit

Stable-ID rule: never renumber existing U-IDs after reordering, splitting, or deleting units.

## Implementation Units
- U1. **Mission and library preflight**
  - Covers: R3, R7
  - Scope: Mission state, solution search, Library Decision.
  - Decision: apply existing Mission OS, routing governor, expert composition, and Knowledge Librarian patterns.
  - Tests or verification: mission created with librarian required and engineering artifact contract; solution search recorded.
  - Dependencies: none

- U2. **Baseline proof and activation scan**
  - Covers: R4, R5
  - Scope: control-plane verifier, Autopilot verifier, skill-system verifier, expert-composition verifier, harness check, system health, protocol audit, routing intelligence.
  - Decision: separate structural pass/fail from activation and lived-route failures.
  - Tests or verification: all required proof commands run and summarized in review ledger.
  - Dependencies: U1

- U3. **Silver Platter audit lens**
  - Covers: R2, AE1
  - Scope: `skills/mark-kashef-silver-platter-agentic-os` audit and validation scripts.
  - Decision: treat this workspace as audit-existing, not greenfield.
  - Tests or verification: audit script output, example validation, and both skill validations.
  - Dependencies: U2

- U4. **Unified operating tree artifact**
  - Covers: R1, R2, R8
  - Scope: `system_cohesion_map.md` and sidecar metadata.
  - Decision: create a readable map with root node, hot control routes, cold assets, Pantry, Prep, Plate, activation status, gaps, owners, and verifiers.
  - Tests or verification: artifact guards and user-outcome review.
  - Dependencies: U2, U3

- U5. **Routing scenario ledger**
  - Covers: R4, R6, AE2, AE3, AE4
  - Scope: natural-language route tests and routing feedback log.
  - Decision: log route-choice-burden failures as structured misroutes instead of treating them as commentary.
  - Tests or verification: scenario outputs captured; failed scenarios appear in routing intelligence underperforming routes.
  - Dependencies: U2

- U6. **Closeout, validation, and handoff**
  - Covers: R5, R8
  - Scope: review, solution-capture, pulse, mission validation, handoff.
  - Decision: keep the first pass as audit plus tree; defer code/router repairs to the next implementation pass.
  - Tests or verification: mission validation passes; artifact guards pass.
  - Dependencies: U4, U5

## Sequencing
1. U1
2. U2
3. U3
4. U5
5. U4
6. U6

## Risks
- A healthy verifier set could hide lived routing friction: mitigated by natural-language scenario tests.
- The audit could become another thing to remember: mitigated by treating `/autopilot` as root and the audit as Mission OS evidence.
- Large library counts could be misread as bloat: mitigated by separating on-disk inventory from hot control routes and activation data.
- First-pass findings could turn into unapproved global changes: mitigated by workspace-only scope and read-only global comparison.

## Validation Mapping
| Assertion | Covered by U-ID | Validator | Pass signal |
|---|---|---|---|
| Mission uses existing governance instead of adding a new OS | U1 | scrutiny | Mission exists with engineering contract and Library Decision. |
| Structural control plane is healthy or exact failures are named | U2 | scrutiny | Baseline proof commands pass or produce recorded findings. |
| Silver Platter classifies the workspace correctly | U3 | scrutiny | Audit returns `audit-existing` and skill validations pass. |
| User receives a cohesive tree and build order | U4 | user-outcome | `system_cohesion_map.md` includes required sections and is rendered in conversation. |
| Natural-language steering gaps are captured | U5 | scrutiny | Failed scenarios are logged as routing misroutes. |
| First pass is validated and handoff-ready | U6 | scrutiny | Artifact guards and mission validation pass. |
