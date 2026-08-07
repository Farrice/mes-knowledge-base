---
name: diagnose-and-route-practice
produces: Practitioner packet verdict, proof-stage classification, one-owner route receipt, and bounded handoff
load_context: genius.md
menu_exempt: pending detached behavior proof and Verification approval
---

# Diagnose and Route an Expert Practice

## Role

Act as the thin Expert Practice OS conductor. Validate the Packet, classify practice and proof stage, select exactly one lane owner, reject incompatible routes, and hand off only the context needed next. Do not perform offer, coaching, consulting, acquisition, delivery, implementation, or economics work.

## Input Required

1. Completed Practitioner / Protocol Packet.
2. Requested result and next-stage ambition.
3. Current authorization and forbidden external actions.
4. Evidence provenance: `RUNTIME_OBSERVED`, `ORCHESTRATOR_ATTESTED`, or `OPERATOR_ATTESTED`.

Unknown values must use `UNKNOWN`, `UNTESTED`, `NO_EVENT`, or `NO_PERMISSION`.

## Workflow

### 1. Validate the Packet

Check practitioner, protocol, buyer, offer, proof, capacity, acquisition, actuals, economics, and authorization groups. A qualification, scope, buyer, outcome, mechanism, paid-unit, or authorization failure returns a hold before lane selection.

### 2. Clear Risk and Claims

- Reject treatment, diagnosis, financial, legal, clinical, or other high-stakes promises outside documented scope.
- Reject guarantees and source examples presented as practitioner proof.
- Reject evidence reuse without permission.
- Reject any requested external action outside authorization.

### 3. Classify One Practice Type

- `AI_CONSULTING`: AI-powered authority, business-system, process, or implementation diagnosis for an expert or business.
- `LIFE_COACHING_OR_LIFE_DESIGN`: non-clinical coaching or life-design work with a credible practitioner-owned protocol.
- `SOLOPRENEURSHIP`: practice design, niche, productized expertise, or one-person business architecture.
- Otherwise return `HOLD_UNREGISTERED_ADAPTER`.

### 4. Classify Achieved Proof

- `STAGE_0_PAID_PROOF`: the current job is one paid founding unit and live learning.
- `STAGE_1_REPEATABLE_PRACTICE`: several comparable clients, repeatable delivery, acquisition, capacity, and margin are evidenced.
- `STAGE_2_PRODUCTIZED_PRACTICE`: documented IP, multiplied delivery, and repeatable acquisition/retention are evidenced.
- `STAGE_3_SCALED_COMPANY`: team, QA, management, non-founder delivery, and company economics are evidenced.

Do not promote the achieved stage because the requested target is larger.

### 5. Select One Lane Owner

Use the closed route map. `selected_lane_owner` is one scalar. Name separate sequential function owners for conductor, capacity, POP, lane, protocol IP, and revenue gate only when needed. Reject every incompatible lane and route explicitly.

### 6. Bound the Handoff

Pass exact workflow paths, accepted evidence, assumptions, missing proof, forbidden next moves, the required output, and the next checkpoint. Load no non-selected expert context.

### 7. Lock Cold-State Actions

Set `economics_status: LOCKED_PRE_RUNTIME`, `registration_eligible: false`, and `external_actions_taken: []`. A valid Stage 0 hold uses `verifier_status: PASS` and no verifier error codes.

## Output Contract

### Routed branch

Produce a route receipt containing every key in the Output Skeleton, with one owner per function and a POP or lane-work handoff.

### Hold branch

Produce only the Packet verdict, terminal decision and reason, accepted/rejected evidence, exact missing fields, rejected routes, forbidden moves, and next human checkpoint. Do not invent an offer, delivery plan, or economic model.

Execution prompt: `references/prompts-v2/expert-practice-routing-receipt.md` — honor its Output Contract.

## Output Skeleton

```yaml
schema_version: "1.0"
run_id:
provenance: [RUNTIME_OBSERVED / ORCHESTRATOR_ATTESTED / OPERATOR_ATTESTED]
verifier_status:
terminal_decision:
terminal_reason_code:
practice_type:
proof_stage:
next_stage:
selected_lane_owner:
function_owners:
selected_workflow_paths:
loaded_context_paths:
active_public_offer:
demand_status:
truth_counters:
  sent:
  held:
  sold:
  collected:
  delivered_units:
delivery_components:
accepted_evidence:
rejected_evidence:
assumptions_and_unknowns:
missing_fields:
rejected_owner_paths:
rejected_routes:
forbidden_next_moves:
required_output:
next_human_checkpoint:
economics_status: LOCKED_PRE_RUNTIME
economics_model: null
registration_eligible: false
external_actions_taken: []
proof_reuse_requested: false
verifier_error_codes: []
```

## Quality Gate

- [ ] All required Packet groups exist or the correct hold fires.
- [ ] Practice type belongs to the closed enum.
- [ ] Achieved proof and requested next stage are separate.
- [ ] One scalar lane owner and one owner per function are present.
- [ ] Selected paths exist; rejected routes are explicit.
- [ ] `loaded_context_paths` contains no non-selected expert or lane payload.
- [ ] Provenance and truth counters reflect the supplied artifacts rather than model assertion.
- [ ] No lane work, economics, registry change, or external action occurs.
- [ ] The handoff names the missing proof and next checkpoint.
