# Proof-State Schema

## Stage Enum

- `STAGE_0_PAID_PROOF`
- `STAGE_1_REPEATABLE_PRACTICE`
- `STAGE_2_PRODUCTIZED_PRACTICE`
- `STAGE_3_SCALED_COMPANY`

`proof_stage` is achieved evidence. `next_stage` is permitted work. One completed founding unit can permit Stage 1 work while achieved proof remains Stage 0.

## Provenance Enum

- `RUNTIME_OBSERVED`
- `ORCHESTRATOR_ATTESTED`
- `OPERATOR_ATTESTED`

Runtime provenance must come from a detached observed run and hashed artifacts. A model cannot self-declare it.

## Evidence Classes

| Class | Supports | Does not support |
|---|---|---|
| Source | Method attribution | Practitioner or client results |
| Practitioner | Authority, scope, mechanism hypothesis | Offer demand |
| Demand | Buyer events and collected payment | Client outcome |
| Delivery | The promised unit occurred and revealed friction | Repeatability |
| Outcome | Permissioned bounded client change | Universal causality |
| Repeatability | Comparable clients, stable acquisition/delivery, capacity, retention, margin | Company-stage team economics |

## Terminal Decisions

- `ADVANCE_TO_REPEATABILITY`
- `REVISE_POP`
- `STOP_OR_HOLD`

`terminal_reason_code` explains a valid outcome. `verifier_error_codes` identify an invalid artifact or contract violation. A valid hold has `verifier_status: PASS` and no verifier errors.

## Registration Gate

`registration_eligible=true` requires all of:

1. detached `RUNTIME_OBSERVED` proof,
2. passing behavior verification, and
3. separate human registration approval.

The cold build always emits `registration_eligible: false`.
