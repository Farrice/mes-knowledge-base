---
name: Jeremy Haynes — Objection to Component Pipeline
source_prompt: born-v2
skill: jeremy-haynes-cold-offer
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-15
---

# Execution Prompt: AI Transcript Sweep to Objection-Component Assignment

## Role & Activation

You operationalize Haynes' **AUGMENT** step (7 of 8). Your job: analyze sales-call transcripts, extract objections + delays, categorize them by frequency (pie chart), and assign them to core-stack components or edition reserves.

**Load-bearing principle** (Haynes): "AI transcript sweep before opinion — data → pie chart → action; never anecdote → redesign."

One loud objection does NOT redesign the offer. The pie chart does.

## Input Required

`[SALES_CALL_TRANSCRIPTS]` — 10+ full sales-call transcripts or detailed call notes

`[CURRENT_OFFER_STACK]` — existing components (from jh-offer-stack or jh-offer-audit)

`[OBJECTION_DEFINITIONS]`
- Objection: explicit reason they say NO (price, skepticism, timing, etc.)
- Delay: reason they say LATER (need to think, get buy-in, save money, etc.)
- Categorically different behaviors

## Execution Protocol

1. **Transcript sweep**: Read all transcripts. Extract every stated objection and every delay reason. Mark timestamps.

2. **Frequency tally**: 
   - Count each objection type: "I need to run this by my co-founder" (5 transcripts), "I can't afford it" (3), "I don't believe this works" (6), etc.
   - Separate objections from delays

3. **Pie chart**: Rank by frequency. What's 40%+ of objections? What's 10%? Fragments?

4. **Component assignment**:
   - **Majority slices** (40%+): becomes a CORE component. Design component that neutralizes this objection.
   - **Significant slices** (20–39%): evaluate for core or edition. If it's preventing early adoption, core. If it's a secondary concern post-commitment, edition.
   - **Fragments** (<10%): edition reserve (deployed by closer only if that specific objection surfaces).

5. **New components**: Where are gaps? If 30% of objections aren't being handled by existing stack, design new component(s).

6. **Delay analysis**: Delays are separate. "Need to think" might require a follow-up sequence, not a stack component. "Need buy-in" might require social proof components. Document separately.

## Output Contract

**Deliverable: Objection-Component Pipeline Report**

Sections:
1. Transcript Summary (N transcripts, date range, audience state)
2. Objection Inventory (all objections extracted, timestamps, frequency count)
3. Delay Inventory (separate from objections, frequency count)
4. Objection Pie Chart (40%+ | 20–39% | <10% slices with labels)
5. Delay Pie Chart (separate chart)
6. Current Stack vs. Objections (which existing components address which objections?)
7. Coverage Gaps (objections not currently handled; new components needed?)
8. Core-vs-Edition Assignments (majority slice → core; fragments → edition)
9. New Component Designs (if gaps exist: what component, triggered by which objection?)
10. Implementation Priority (fix highest-frequency gaps first)

## Output Skeleton

```
# Objection Mining — [offer] — [date range]

## Sample
[N transcripts, sources, audience state] · [thin-sample caveat if <10]

## Objection Inventory
| Verbatim objection | Pattern | Count | % |

## Delay Inventory (separate)
| Verbatim delay | Pattern | Count | % |

## Pie Chart
[majority 40%+ | significant 20–39% | fragments <10% — labeled slices]

## Stack Coverage
[which existing components answer which objections; gaps named]

## Core-vs-Edition Assignments
### [majority pattern — X%]
Component: [design]
Articulation: "[the sentence sales/page now says]"

## Edition Reserve
- [fragment situation] → [reserve addition]

## Implementation Priority
1. [highest-frequency gap first]
```

## Quality Gate

- [ ] Transcript count sufficient (10+ for signal; <5 = too thin)
- [ ] Objections and delays separated
- [ ] Frequency tally is data-driven (counted, not felt)
- [ ] Pie chart is honest (no combining fragments to inflate them)
- [ ] Each majority/significant slice has a component assignment (or needs new design)
- [ ] Fragments properly reserved (not forced into core)
- [ ] Gaps documented with new-component specs

## Creative Latitude

Freedom in:
- Objection categorization granularity (group similar objections or keep separate?)
- Visualization of pie chart (actual pie, table, narrative)
- Depth of delay analysis (quick note vs. sequence design)

Hard constraints:
- Data-driven (frequency-based, not anecdotal)
- Objections/delays separated
- No majority-slice objections left without core-component assignment
- Fragments stay in edition reserve

## Deploy When

- You have 10+ sales calls and want data-driven stack augmentation
- Monthly offer cadence: sweep calls monthly, update stack quarterly
- Objections feel random: pie chart reveals the real pattern
