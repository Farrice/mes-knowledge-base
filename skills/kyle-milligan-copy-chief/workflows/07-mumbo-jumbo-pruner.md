---
name: mumbo-jumbo-pruner
description: Count competing undefined concepts in one to six lines, select one supported concept, and minimally define, delete, or postpone the rest.
produces: Undefined Concept Register
routing: long-tail
menu_exempt: permanently internal undefined-concept scalpel; no public command by approved architecture
source_rows: SL-048, SL-062
prompt: references/prompts-v2/mumbo-jumbo-pruner.md
---

# Mumbo-Jumbo Pruner

## Role

Reduce cognitive object count in one short excerpt. This is not a generic simplicity, readability, or full-body rewrite workflow.

## Source and Ownership

- **Kyle:** two-undefined-concept diagnosis, `SL-048`.
- **Co-authored, Kyle-led demonstration:** multiple health constructs, `SL-062`.
- **Truth lock:** the finance/health examples are not reusable offer facts.

## Input Required

1. One to six exact lines.
2. Intended Promise Card or section job.
3. Product Truth definitions for every proposed mechanism, process, object, or branded construct.
4. Audience and awareness level.
5. Evidence IDs and domain constraints.

## Hard Stop / Refusal

Return `HOLD_CONCEPTS` when:

- the top-level promise is broken;
- the product mechanism is unresolved or disputed;
- no supported concept can be selected;
- the excerpt exceeds six lines or the request expands into full body copy;
- a regulated mechanism lacks domain review.

Do not invent definitions to rescue an undefined mechanism.

## Procedure

### 1. Extract Candidate Concepts

List every noun phrase or causal object the reader must understand to follow the claim.

### 2. Classify Each Concept

Use:

- `SUPPORTED_DEFINED`;
- `SUPPORTED_NEEDS_PLAIN_DEFINITION`;
- `DUPLICATE_LABEL`;
- `UNSUPPORTED`;
- `CONTRADICTORY`;
- `POSTPONE`.

Cite Product Truth IDs.

### 3. Count Simultaneous Objects

Record how many concepts the reader must carry in each line and where the count becomes ambiguous.

### 4. Select One Primary Concept

Choose the concept that best carries the Promise Card. Every other concept gets `DEFINE`, `DELETE`, `MERGE`, `POSTPONE`, or `ESCALATE`.

### 5. Make One Minimal Repair

Rewrite only enough to establish the primary concept and remove the conflict. Preserve valid wording and evidence.

## Output Contract

```markdown
# Undefined Concept Register

## Section Lock
- Promise/job:
- Audience:
- Evidence boundary:

## Concept Register
| Concept | First line | Definition / PT IDs | Status | Action |

## Object Count
| Line | Simultaneous concepts | Reader burden |

## Primary-Concept Decision
- Primary concept:
- Why it carries the promise:
- Concepts removed/postponed:

## Minimal Rewrite
- Before:
- After:
- Preserved evidence:

## Handoff
- Next owner:
- Recheck condition:
- Open risk:
```

## Quality Gate

- [ ] Scope is one to six lines.
- [ ] Every proposed concept is listed and evidence-classified.
- [ ] One supported primary concept is selected.
- [ ] No mechanism or definition is invented.
- [ ] Minimal rewrite preserves passing material.
- [ ] Finance/health examples and source facts do not transfer.
- [ ] Promise-level failure escalates instead of receiving a clarity edit.

## Handoff

Pass the minimal rewrite to workflow 04 or 05 for one recheck. Route mechanism uncertainty to Luke and regulated content to its factual/domain owner.

## Execution Prompt

Read and honor `../references/prompts-v2/mumbo-jumbo-pruner.md`.
