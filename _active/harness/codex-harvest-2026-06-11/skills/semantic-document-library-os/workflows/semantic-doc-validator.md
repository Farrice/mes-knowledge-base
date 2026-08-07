---
description: Test whether an agent can execute a task from a semantic document without hidden human explanation
---

# Semantic Document Validator

## Load

Read:

1. `skills/semantic-document-library-os/genius.md`
2. `skills/semantic-document-library-os/references/validation-rubric.md`

## Inputs

- Semantic document to test.
- Realistic task.
- Allowed tools or no-tool constraint.
- Expected output.

## Execution

1. Run the cold-start test: assume the agent only has the semantic document and the task.
2. Simulate the agent's interpretation before execution.
3. Check whether it can identify inputs, authority, source of truth, risks, and validation.
4. Attempt or reason through the task.
5. Record where the document forced guessing.
6. Produce exact revisions.

## Output

Use the validator output format from `references/validation-rubric.md`.

## Quality Gate

A document cannot pass if the agent must rely on unstated business context, hidden founder preferences, or vague human review.
