---
description: Build a full semantic document library architecture for a business, agent, product, or knowledge domain
---

# Semantic Document Library Builder

## Load

Read:

1. `skills/semantic-document-library-os/genius.md`
2. `skills/semantic-document-library-os/references/semantic-document-schema.md`
3. `skills/semantic-document-library-os/references/validation-rubric.md`

## Inputs

- Business, agent, product, or domain.
- Existing docs and source material.
- Highest-value recurring work.
- Risk boundaries and approval policies.

## Execution

1. Inventory recurring work and group it into work primitives.
2. Rank primitives by leverage, frequency, risk, and agent-readiness.
3. Design the library tree around primitives, not departments.
4. Define the global authority model.
5. Generate the first document backlog.
6. Specify validation tests and maintenance cadence.

## Recommended Library Tree

```text
semantic-library/
  README.md
  authority-model.md
  primitive-map.md
  validation-log.md
  primitives/
    [primitive-name].md
  examples/
    good/
    counterexamples/
  sources/
    transcripts/
    SOPs/
    calls/
```

## Output Schema

```markdown
# Semantic Document Library Blueprint: [Name]

## Library Purpose

## Work Primitive Map
| Primitive | Owner | Frequency | Risk | First Doc? |
|---|---|---:|---|---|

## Authority Model

## File Tree

## First 10 Documents To Build

## Validation Plan

## Maintenance Protocol
```

## Quality Gate

If the tree is organized by file type only, revise it. The system must be organized around the work agents need to understand.
