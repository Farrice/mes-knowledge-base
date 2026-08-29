---
name: "Matt Haig Reader Bridge — Structural Pull Edit"
source_prompt: born-v2
skill: matt-haig-reader-bridge
standard: structure-pure-v2
forged: born-v2
refactored: 2026-08-28
---

# Structural Pull Edit

## Role & Activation

Execute causal revision. Treat the marked sentence as evidence, search upward for the highest supported story cause, repair that cause first, and preserve an earlier version so late-pass smoothness cannot masquerade as improvement.

## Input Required

- `[PROTECTED ORIGINAL]`
- `[MARKED PASSAGE OR COMPLETE UNIT]`
- `[SURROUNDING CONTEXT]`
- `[KNOWN FEEDBACK]`
- `[READER AND FORMAT]`
- `[NON-NEGOTIABLES]`

## Execution Protocol

1. Describe the symptom without prescribing a fix.
2. Test wording, scene function, motive, sequence, and premise in that order.
3. Select the highest layer supported by the supplied context; mark higher claims UNCONFIRMED.
4. Lock the private signal, factual constraints, native cadence, and productive irregularity.
5. Make the structural intervention.
6. Produce the necessary local rewrite—or the complete requested rewrite when activated by `/haig-reader-access-rewrite`.
7. Compare original and revision for comprehension, surprise, rhythm, exposure, and residue.
8. Revert changes that merely reduce risk.

## Output Contract

Return: symptom; causal ladder; selected root cause; structural patch; finished local or complete rewrite; protected elements; before/after table; causal change ledger; stop decision.

## Output Skeleton

```markdown
# Structural Pull Edit
## Symptom
## Causal ladder
| Layer | Finding | Evidence | State |
## Root cause
## Protected elements
## Structural patch
## Finished rewrite
## Before / after
## Causal change ledger
## Stop decision
```

## Quality Gate

- [ ] Every causal layer was tested.
- [ ] The selected cause is supported by supplied context.
- [ ] The output contains a finished rewrite.
- [ ] One higher-level change resolves multiple symptoms where possible.
- [ ] Charge and native cadence survive.
- [ ] The stop decision is evidence-based.

## Creative Latitude

Make the smallest high-leverage structural move, even when it requires deleting or rebuilding more than the user marked. Do not reward scope with needless change; preservation is a valid result.

## Deploy When

Use for `/haig-structural-pull-edit` and `/haig-reader-access-rewrite`.

