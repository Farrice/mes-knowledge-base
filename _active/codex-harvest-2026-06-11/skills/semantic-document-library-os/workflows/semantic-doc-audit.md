---
description: Audit existing documents for agent usability, semantic clarity, authority, validation, and execution risk
---

# Semantic Document Audit

## Load

Read:

1. `skills/semantic-document-library-os/genius.md`
2. `skills/semantic-document-library-os/references/semantic-document-schema.md`
3. `skills/semantic-document-library-os/references/validation-rubric.md`

## Inputs

- Document, folder, SOP, workflow, skill, or knowledge base to audit.
- Intended agent task.
- Consequence level: low, medium, or high.

## Execution

1. Identify the real work primitive behind the document.
2. Separate access instructions from semantic meaning.
3. Score whether the document explains objects, authority, inputs, outputs, risks, examples, and validation.
4. Find hidden human assumptions the agent would have to infer.
5. Classify autonomy level: read, draft, stage, execute with review, or execute independently.
6. Produce a prioritized fix plan.

## Output

```markdown
# Semantic Document Audit: [Document]

## Verdict
PASS / REVISE / REWORK

## Work Primitive
- Surface action:
- Real primitive:
- Consequence level:

## Scores
| Dimension | Score /10 | Finding |
|---|---:|---|
| Primitive clarity |  |  |
| Inputs and source of truth |  |  |
| Authority and permissions |  |  |
| Decision rules |  |  |
| Examples and counterexamples |  |  |
| Quality tests |  |  |
| Failure modes |  |  |
| Maintenance protocol |  |  |

## Hidden Human Assumptions
- 

## Fix Plan
| Priority | Fix | Why It Matters |
|---|---|---|
```

## Quality Gate

If the audit only says "add more detail," revise it. The output must name the exact missing semantic field and the operational risk it creates.
