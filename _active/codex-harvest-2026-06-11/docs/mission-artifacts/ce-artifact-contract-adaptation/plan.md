# Unit Plan: CE Artifact Contract Adaptation

Created: 2026-05-08
Mission: ce-artifact-contract-adaptation

Stable-ID rule: never renumber existing U-IDs after reordering, splitting, or deleting units.

## Implementation Units

- U1. **Mission Control artifact contract**
  - Covers: R1, R2, R4, AE1, AE2, AE3
  - Scope: `execution/mission_control.py`
  - Decision: Add `--artifact-contract engineering` as an optional creation-time contract that writes mission-local artifacts and keeps legacy missions on `none`.
  - Tests or verification: Python compile, create a smoke mission, validate old and new missions.
  - Dependencies: none

- U2. **Mission workflow operating instructions**
  - Covers: R3, R4, AE4
  - Scope: `.agent/workflows/mission.md`
  - Decision: Teach Mission OS when to use the engineering contract, how U-IDs work, and what not to adopt blindly from CE.
  - Tests or verification: router/search checks and manual workflow read-through.
  - Dependencies: U1

- U3. **Durable artifact sinks**
  - Covers: R5
  - Scope: `docs/mission-artifacts/README.md`, `docs/solutions/README.md`, `docs/pulse-reports/README.md`
  - Decision: Make mission artifacts, generalized solved problems, and pulse reports visible without adding a duplicate command layer.
  - Tests or verification: file existence and generated smoke mission artifacts.
  - Dependencies: U1

- U4. **Live contract smoke mission**
  - Covers: AE1, AE2
  - Scope: `.agent/missions/ce-artifact-contract-adaptation/` and `docs/mission-artifacts/ce-artifact-contract-adaptation/`
  - Decision: Use the new contract on this implementation so the first artifact set records the actual rationale.
  - Tests or verification: mark librarian complete, add handoff, validate mission.
  - Dependencies: U1, U2, U3

## Sequencing

1. U1
2. U2
3. U3
4. U4

## Risks

- Command bloat: mitigated by keeping the contract inside `/mission` instead of adding CE clone commands.
- Placeholder artifacts: mitigated by filling this mission's artifacts with real implementation rationale.
- Over-enforcement on old missions: mitigated by keeping `artifact_contract.type = none` as the default.

## Validation Mapping

| Assertion | Covered by U-ID | Validator | Pass signal |
|---|---|---|---|
| Engineering missions can generate artifact contracts | U1, U4 | scrutiny | Smoke mission has six generated files |
| Existing missions are not forced into new artifacts | U1 | scrutiny | Legacy mission validation still passes |
| Mission workflow teaches the contract clearly | U2 | user-outcome | `/mission` contains usage rules and skip rules |
| Durable solved-problem and pulse sinks are visible | U3 | user-outcome | README files exist in all three docs folders |
