---
name: 531-swipe-discipline
description: Build a five-read, three-breakdown, one-primary Swipe Packet from relevant comparable promotions without transferring their facts or wording.
produces: Swipe Packet
routing: long-tail
menu_exempt: pending detached behavior proof and Verification approval
source_rows: SL-023
prompt: references/prompts-v2/531-swipe-discipline.md
---

# 5-3-1 Swipe Discipline

## Role

Turn assignment-specific research into an inspectable drafting receipt: five relevant reads, three structural breakdowns, and one primary swipe. This is not daily copywork, VOC mining, or permission to copy control facts.

## Source and Ownership

- **Owner:** Kyle Milligan method.
- **Observed anchor:** `SL-023` / `H-019`, 24:42–25:11.
- **Cross-cutting restraint:** `SL-020` research-break detection and `SL-021` “do the least.”
- **Truth boundary:** Swipe content is external input. Its claims remain unverified unless the Product Truth Packet independently supports them.

## Input Required

1. Product Truth Packet: offer, verified capabilities, mechanism/catalyst status, supported result, prohibited claims.
2. Audience Card: reader, awareness, problem, and what cannot be assumed.
3. One desired action and target format.
4. Five accessible comparable promotions with source path/URL, brand, format, audience, and provenance.
5. Domain constraints, including any regulated-claim review requirement.

## Hard Stop / Refusal

Return `HOLD_531` and generate no Swipe Packet when:

- fewer than five relevant, accessible promotions exist;
- offer, audience, action, or mechanism/opportunity status is unknown;
- provenance is missing;
- the only available controls are high-status but materially irrelevant;
- regulated evidence has not passed its domain gate;
- the user asks the system to invent missing swipes.

Name the exact missing item. Do not substitute source-video examples or another expert's remembered examples.

## Procedure

### 1. Establish the Relevance Test

Score each candidate `0`, `1`, or `2` on:

- audience proximity;
- problem/desire proximity;
- mechanism or opportunity proximity;
- format/placement proximity;
- proof burden and desired-action proximity.

Record the reason for every score. Synthetic or reported performance labels are context only; they cannot override relevance.

### 2. Read Five

For all five, capture:

- opening move;
- governing claim;
- argument sequence;
- proof forms;
- transitions;
- action placement;
- non-transferable facts, wording, brands, metrics, testimonials, and credentials.

### 3. Break Down Three

Choose three by relevance and complementary learning value. For each, map:

`claim → expected skepticism → proof → result/demonstration → next beat`

Also record one structural move worth borrowing and one transfer veto.

### 4. Choose One Primary

Choose the closest audience/problem/mechanism/format/proof match. Explain why it beats the other two, even if another has a higher performance or status label.

### 5. Freeze the Borrowing Boundary

Split material into:

- `STRUCTURE_ALLOWED` — abstract sequence, proof placement, transition logic;
- `FACT_REQUIRES_PRODUCT_TRUTH` — any factual claim needing independent support;
- `TRANSFER_FORBIDDEN` — brand, wording, metric, customer, authority, testimonial, mechanism, or source fact.

## Output Contract

Produce exactly one `Swipe Packet`:

```markdown
# Swipe Packet

## Assignment Lock
- Offer:
- Audience:
- Desired action:
- Mechanism/opportunity status:
- Proof boundary:

## Five-Source Relevance Map
| ID | Provenance | Audience | Problem | Mechanism | Format/proof | Total | Decision |

## Three Breakdowns
### <ID>
- Governing claim:
- Argument sequence:
- Claim/proof map:
- Transferable structure:
- Transfer veto:

## Primary Swipe
- ID:
- Why this one:
- Deliberate deviations allowed:

## Borrowing Boundary
- STRUCTURE_ALLOWED:
- FACT_REQUIRES_PRODUCT_TRUTH:
- TRANSFER_FORBIDDEN:

## Handoff
- Next owner: unique-promise-spine
- Evidence IDs:
- Open risk:
```

## Quality Gate

- [ ] Exactly five sources were read; exactly three were broken down; exactly one is primary.
- [ ] Every source has provenance and a written relevance reason.
- [ ] Primary choice is based on assignment fit, not fame or a performance label alone.
- [ ] No source fact, metric, testimonial, mechanism, credential, or wording moved into Product Truth.
- [ ] The borrowing boundary is explicit.
- [ ] Regulated or unverifiable material is held, not normalized.
- [ ] Output is a packet, not draft copy.

## Handoff

Pass only the Swipe Packet, Product Truth IDs, locked primary choice, validation status, and one open risk to `02-unique-promise-spine.md`.

## Execution Prompt

Read and honor `../references/prompts-v2/531-swipe-discipline.md`.
