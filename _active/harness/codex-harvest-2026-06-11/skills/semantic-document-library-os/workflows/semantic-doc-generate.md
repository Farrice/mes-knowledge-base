---
description: Generate one agent-executable semantic document from a transcript, SOP, workflow, article, or messy knowledge source
---

# Semantic Document Generator

## Load

Read:

1. `skills/semantic-document-library-os/genius.md`
2. `skills/semantic-document-library-os/references/semantic-document-schema.md`
3. `skills/semantic-document-library-os/references/examples.md`

## Inputs

- Source material.
- Intended agent job.
- Audience or operator.
- Allowed authority level.
- Source of truth.

## Execution

1. Extract the real work primitive.
2. Name the action behind the interface or document.
3. Pull out explicit rules, tacit rules, authority limits, examples, and failure modes.
4. Mark gaps instead of inventing policy.
5. Generate the semantic document using the schema.
6. Add two tests: one normal case and one edge case.

## Output

Produce a complete semantic document with all required schema sections. If source material is thin, include `[GAP: ...]` markers and a "Gap Closure Questions" section.

## Quality Gate

The document must let an agent decide when to act, when to ask, and when to stop. If it only explains what the task is, it is not complete.
