# Behavior-Changing Extraction Contract

## Purpose

Use this contract when source material is supposed to enhance the system, not merely become a summary, notes file, mechanics list, or command shell.

The standard: a source-to-system build is not complete until it proves the extracted intelligence changes a realistic input, workflow, decision, or artifact.

## Required Behavior-Changing Proof

Every capability-enhancing extraction must include a proof artifact matched to the source type.

| Source Type | Proof Artifact |
|---|---|
| Copywriting, content, persuasion, sales | Before/after transformation with weak-link diagnosis, source mechanic, behavior delta, proof object or proof gap, and next gate. |
| Workflow, operations, agent systems | Cold-start run showing input, selected route, produced output, validation, and handoff. |
| Strategy or business method | Applied scenario with decision, tradeoff, output, quality gate, and remaining risk. |
| Creative method | Example asset or transformation showing what changed and why. |
| Research or analysis method | Test query or case showing source-grounded reasoning and decision change. |

## Minimum Proof Shape

```markdown
## Behavior Proof
- **Input tested:**
- **Weakness diagnosed:**
- **Source mechanics used:**
- **Output produced:**
- **Behavior delta:**
- **Validation run:**
- **Remaining risk:**
```

## Failure Mode This Prevents

This contract exists because a build can pass structural checks while failing the user's real objective. Registry sync, route discoverability, command bridge creation, and mechanics ledgers are necessary but not sufficient.

## Proof Ceiling And Handoff

A valid behavior proof can earn `TRANSFERRED` in the
`mastery-transfer-proof-spine.md` ladder. It does not by itself prove that the
capability generalizes, is independently preferred, works in the field, or
surpasses a named baseline.

When a build makes one of those higher claims, hand the existing proof artifacts
to the Mastery Transfer Proof Spine. Preserve the first unearned state and next
evidence action instead of inflating one successful transformation.

## Quality Gate

Reject the extraction if:

- it cannot transform or improve a realistic input,
- it cannot explain what changed behaviorally,
- it has source claims without evidence or marked uncertainty,
- it creates command wiring without a cold-start proof,
- it lists experts without integration evidence,
- it creates documents that future agents still have to interpret manually,
- or it calls a capability "deployed" before validation proves use.
- or it calls one development-visible example generalized, field-valid, or
  surpassing.

## Integration Points

- `/source-to-skill-system` owns applying this contract during source-to-system builds.
- `/extraction-governor-agent` owns warning when a proposed build lacks behavior proof.
- `/repeatability-spine` owns repair when a prior extraction passed structurally but failed usefulness.
- `/expert-composition-governor` owns preventing expert names from being treated as proof.
- `mastery-transfer-proof-spine.md` owns evidence progression beyond one
  behavior-changing proof.

## Last Updated

2026-08-26
