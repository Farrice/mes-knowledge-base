# Mastery Transfer Proof Spine

**Status:** `SHADOW`
**Owner:** `/source-to-skill-system`

## Purpose

Use this companion primitive when an extraction or source-to-skill build claims
to transfer, generalize, field-validate, or surpass expertise. It separates
those claims from ordinary source capture, structural validation, and one-run
behavior proof.

This is not a new extraction command, universal score, or mandatory gate. It
composes evidence already owned by behavior proof, `skill_benchmark.py`,
`blind_pass.py`, `/repeatability-spine`, and real outcome receipts.

## Activation Boundary

Apply the spine when at least one is true:

- the build claims expertise was transferred or replicated;
- the method is expected to work on unfamiliar or cross-domain inputs;
- the output uses `surpass`, `transcend`, `better than`, `5x`, `10x`, or an
  equivalent superiority claim;
- a cold-start proof is being treated as readiness for broad or consequential
  use; or
- promotion from cold/SHADOW status is being considered.

Do not require it for summaries, references, thin source maps, or a capability
that claims only `RUNNABLE` behavior. It may recommend the next evidence action
but cannot block the nearest safe use unless a factual, proof, safety, privacy,
or permission veto already applies.

## Proof Ladder

The highest earned state is the highest contiguous `PASS`. A later state cannot
repair or skip an earlier missing state.

| State | What it proves | Minimum evidence |
|---|---|---|
| `CAPTURED` | The source is locally available and bounded. | Source files plus uncertainty limits. |
| `GROUNDED` | Material mechanics trace to the source and inference is labeled. | Ledger, source map, or fidelity review. |
| `RUNNABLE` | A cold agent can invoke the capability and produce the contracted shape. | Cold-start receipt and structural/routing validation. |
| `TRANSFERRED` | The capability changes a realistic unfamiliar input without hidden chat context. | At least one behavior proof with diagnosis, mechanics, delta, validation, and risk. |
| `GENERALIZED` | The behavior survives near transfer, far transfer, and a case where it must abstain or hand off. | Sealed held-out near, far, and negative-control cases. |
| `BLIND_PREFERRED` | An evaluator independent of the builder prefers the treatment for a material reason without a preservation regression. | Blinded comparison, precommitted mapping, evaluator receipt, and preservation locks. |
| `FIELD_VALIDATED` | The capability was used in reality and produced an observed outcome in the claimed lane. | Prospective use and outcome receipts; craft preference alone does not qualify. |
| `SURPASSING` | The capability beats a named baseline on a predeclared dimension and threshold without material regression. | All prior states plus comparison baseline, metric, threshold, measured result, and claim boundary. |

## Claim Rules

- A cold-start PASS can earn `RUNNABLE`; it does not prove transfer.
- A builder-authored example can support development but cannot earn
  `BLIND_PREFERRED`.
- Development fixtures visible during construction cannot earn
  `GENERALIZED`; held-out cases must be sealed before the evaluated variant is
  produced.
- `FIELD_VALIDATED` is lane-specific. A real use in content does not validate
  sales, revenue, retention, health, or another outcome class.
- `SURPASSING` is dimension-bounded. Speed, scale, quality, cost, range, and
  commercial outcome are separate claims.
- Ambitious MES targets such as 5x, 10x, or 30 days remain `TARGET HYPOTHESIS`
  until the declared comparison supports them.
- File presence, hashes, router discovery, self-authored receipts, and model
  preference cannot be laundered into human, field, market, or causal proof.

## Reused Proof Tools

| Existing owner | Native job in this spine |
|---|---|
| Behavior-Changing Extraction Contract | Establish `TRANSFERRED` behavior. |
| `execution/skill_benchmark.py` | Supply seen and rotating held-out benchmark cases and gaming checks. |
| `execution/blind_pass.py` | Record an actual blind comparison; the builder may not self-grade. |
| `/repeatability-spine` | Preserve good behavior and add regression guards after failure. |
| Outcome/revenue receipts | Separate drafted, used, response, behavior, sale, collection, refund, and retention events. |
| Human craft owner | Certify taste, materiality, preservation, and whether no change was better. |

## Mastery Transfer Handoff

```markdown
## Mastery Transfer Handoff
- **Capability:**
- **Current state:**
- **Source evidence:**
- **Comparison baseline:**
- **Named dimension:**
- **Evidence passed:**
- **First unearned state:**
- **Preservation locks:**
- **Independent evaluator:**
- **Field-event state:**
- **Next evidence action:**
- **Claim boundary:**
```

## Promotion Boundary

This primitive remains SHADOW. Promotion requires three independent production
receipts across different capabilities, at least one independent blind
preference, zero proof-state inflation on negative controls, no automatic
question burden for ordinary source work, preserved creative range, and
Farrice's explicit approval.

Keep it SHADOW or remove it if it adds ceremony without changing a claim,
promotion decision, test design, or next evidence action.

## Verification

```bash
python3 execution/verify_mastery_transfer_proof_spine.py \
  --pilot extractions/oren-1person-ai-marketing/funnel-flywheel-2026/mastery-transfer-shadow-pilot.json
```
