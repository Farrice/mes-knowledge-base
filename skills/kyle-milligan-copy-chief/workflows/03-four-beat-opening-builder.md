---
name: four-beat-opening-builder
description: Build three evidence-bounded opening candidates from a valid Promise Card using the separate four-beat progression, then recommend one without blending.
produces: Three openings and recommendation
routing: long-tail
menu_exempt: pending detached behavior proof and Verification approval
source_rows: SL-038, SL-047
prompt: references/prompts-v2/four-beat-opening-builder.md
---

# Four-Beat Opening Builder

## Role

Turn one valid Promise Card into three distinct opening hypotheses. This produces openings only—never a full VSL lead, body, fascination set, or generic hook batch.

## Source and Ownership

- **Kyle:** separate opening sequence at `SL-038`.
- **Co-authored recitation:** `SL-047`.
- **Naming veto:** Four Punches (`SL-022`) is a broader precedent language. It is not this four-beat sequence.

The sequence is:

`researched interrupt → consequential claim → relevant credibility → demonstrated result`

Credibility and result may swap when the evidence earns it.

## Input Required

1. Valid Promise Card with one supported result and forbidden expansion.
2. Primary swipe's structural map and transfer veto.
3. Audience, awareness, traffic/placement, and desired action.
4. Voice constraints or an explicit note that voice evidence is unavailable.
5. Verified credibility and result evidence with Product Truth IDs.
6. Output format, length, and domain constraints.

## Hard Stop / Refusal

Return `HOLD_OPENING` when:

- the Promise Card is invalid or bundled;
- demonstrated-result evidence is absent;
- credibility implies an endorsement not in Product Truth;
- the interrupt depends on a copied control fact or invented authority;
- adjective escalation substitutes for proof;
- the requested opening enters regulated territory without review;
- the user asks for a full body under this workflow.

## Procedure

### 1. State the Reader State

Record what the reader knows, what they doubt, and why this message appears now. Do not manufacture emotional pain.

### 2. Design Three Researched Interrupts

Choose three distinct hypotheses from verified evidence, such as:

- a consequential omission or contrast;
- a specific, qualified datum;
- a concrete operational scene.

No question barrage. No control-swipe fact.

### 3. Complete the Four Beats

For each hypothesis:

1. **Interrupt:** relevant and evidence-linked.
2. **Consequential claim:** one promise, not an outcome bundle.
3. **Credibility:** exact proof that answers the claim's skepticism.
4. **Demonstrated result:** shows the promised effect using supported evidence.

Swap 3 and 4 only when the output reads more naturally and claim/proof fit remains intact.

### 4. Run Truth and Continuity Checks

Map every factual clause to Product Truth IDs. Ensure one concept carries across adjacent lines and every result proves the preceding claim.

### 5. Recommend One

Choose the option with the strongest audience fit, singular promise, proof fit, and continuation. Do not synthesize a fourth blended option.

## Output Contract

Use any stricter caller contract when supplied. Otherwise produce:

```markdown
# Opening Set

## Opening 1 — <hypothesis>
<multi-line opening>

### Beat and Evidence Map
| Line | Beat | Claim | Evidence IDs | Qualifier |

## Opening 2 — <hypothesis>
...

## Opening 3 — <hypothesis>
...

## Recommendation
- Selected option:
- Audience fit:
- Singular promise:
- Proof fit:
- Continuation strength:
- Why the others remain rejected:

## Proof Boundary
- Supported:
- Prohibited:
- Next gate:
```

## Quality Gate

- [ ] Exactly three distinct opening hypotheses and one recommendation exist.
- [ ] Each option contains the four jobs without naming the framework in reader-facing copy.
- [ ] Every factual clause maps to evidence and retains qualifiers.
- [ ] Credibility answers the doubt created by the claim.
- [ ] Demonstrated result proves the exact promise rather than a neighboring benefit.
- [ ] No control facts, invented authority, endorsements, or unsupported outcomes appear.
- [ ] The recommendation selects one option and does not blend.
- [ ] The result stops before body-copy production.

## Handoff

Pass the selected opening, Promise Card, Beat/Evidence Map, preservation notes, and one open risk to `04-first-four-lines-audit.md`.

## Execution Prompt

Read and honor `../references/prompts-v2/four-beat-opening-builder.md`.
