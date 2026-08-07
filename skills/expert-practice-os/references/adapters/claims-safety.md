# Claims and Safety Adapter

## Hold Conditions

Return a hold before lane selection when:

- credentials or scope are absent,
- a non-clinical practitioner promises diagnosis or treatment,
- the protocol cannot plausibly support the outcome,
- a guarantee exceeds available evidence,
- source examples are presented as practitioner or client proof,
- confidential or testimonial evidence lacks permission,
- financial, legal, health, or other high-stakes claims lack qualified review, or
- external action exceeds authorization.

## Required Codes

| Condition | Terminal reason | Verifier error when violated |
|---|---|---|
| Qualification incomplete | `HOLD_QUALIFICATION_INCOMPLETE` | `E_INPUT_QUALIFICATION_MISSING` |
| Scope or claim unsafe | `HOLD_SCOPE_OR_CLAIMS_UNSAFE` | `E_SCOPE_HIGH_STAKES_UNCLEARED` |
| Mechanism mismatch | `HOLD_MECHANISM_NOT_CREDIBLE` | `E_ROUTE_PROTOCOL_PROMISE_MISMATCH` |
| Unsupported guarantee | `HOLD_CLAIM_UNSUPPORTED` | `E_CLAIM_UNSUPPORTED_GUARANTEE` |
| Permission absent | `HOLD_PERMISSION_UNAVAILABLE` | `E_PROOF_PERMISSION_VIOLATION` |
| Unauthorized action | `HOLD_UNAUTHORIZED_ACTION` | `E_ACTION_UNAUTHORIZED_EXTERNAL` |

## Evidence Rule

Keep `SOURCE_REPORTED`, practitioner evidence, demand, delivery, outcome, and repeatability proof separate. When evidence is unavailable, use the approved unknown labels; do not write a smoother claim.
