# Future Extraction Regression Guard

## Why This Exists

The first Sam Parr build passed structural checks but did not meet the real extraction philosophy: harvest intelligence into the system so future work becomes better.

This guard prevents future source-to-system builds from passing when they only create:

- summaries,
- mechanics lists,
- route wiring,
- registry entries,
- or command shells.

## Behavior-Changing Proof Standard

For any extraction that claims to enhance a capability, the build must include at least one behavior proof artifact.

| Source Type | Required Proof |
|---|---|
| Copywriting, content, persuasion, sales | Before/after transformation with diagnosis, source mechanic, behavior delta, and next gate. |
| Workflow, operations, agent systems | Cold-start run showing input, selected route, produced output, validation, and handoff. |
| Strategy or business method | Applied scenario with decision, tradeoff, output, and quality gate. |
| Creative method | Example asset or transformation showing what changed and why. |

## Fail Conditions

Reject the build if:

- it cannot improve or transform a realistic input,
- it cannot explain what changed behaviorally,
- it claims source depth without timestamp or source evidence,
- it adds a command but no cold-start proof,
- it routes experts but shows no integration evidence,
- it creates docs that future agents still have to interpret manually.

## Required Closeout Evidence

Every future source-to-system extraction should end with:

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

## Sam Parr Regression Fixture

The Sam Parr proof lab in `06-before-after-proof-lab.md` is the regression fixture for copywriting extractions. If future copywriting source builds cannot produce a comparable proof artifact, they are incomplete.

