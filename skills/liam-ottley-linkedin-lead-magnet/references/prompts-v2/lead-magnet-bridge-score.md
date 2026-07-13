---
name: "Liam Ottley — Lead Magnet Bridge Concept & Score"
source_prompt: born-v2
skill: liam-ottley-linkedin-lead-magnet
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are operating in the frame Liam Ottley teaches in "How to Turn LinkedIn into a Personal Brand Lead Magnet with AI." The lead magnet is not the content — it is the visible bridge between public expertise and a paid transformation. Content can get attention without creating revenue if that bridge is vague. This prompt exists to force the bridge to be scored honestly before more content gets built on top of it, because a weak bridge invalidates everything downstream.

## Input Required

- Candidate lead magnet concept(s) (may be more than one to score against each other): [CONCEPT(S)]
- ICP and buyer outcome: [ICP / OUTCOME]
- Proof inventory (from the positioning step): [PROOF]
- Paid offer the lead magnet should ultimately route toward: [OFFER OR "no paid offer yet — flag this"]

## Execution Protocol

1. **Score each candidate concept against all five gates from the source method.** Every gate is pass/fail with a one-line justification — do not average around a weak gate.

   | Gate | Pass Criteria |
   |---|---|
   | Buyer outcome | Solves a painful or valuable problem |
   | Specificity | Names a concrete ICP, problem, or moment |
   | Fast value | Delivers a quick win or diagnosis |
   | Proof fit | Shows why this expert is credible |
   | Paid-offer bridge | Makes the next step obvious |

2. **Apply the routing rule explicitly stated in the source method**: if the bridge is weak (any gate fails, especially Paid-offer bridge or Specificity), do not proceed to draft more content around it. State plainly that this concept should route to `/bank-lead-magnet` or `skills/stockton-walbeck-lead-magnets/` for deeper scoring/taxonomy work before content is built on top of it — this is a source-mandated stop condition, not a suggestion to soften.

3. **If multiple concepts are supplied**, rank them by gates passed, and name the single primary concept the rest of the operating plan should build around.

4. **State explicitly whether the paid-offer bridge exists.** If no paid offer was supplied, this is a hard finding: the lead magnet can only ever collect attention, not revenue, until an offer exists to route to.

## Output Contract


**Voice layer (binding — Farrice 2026-07-13):** if this deliverable ships under Farrice's own name, load `_active/farrice-brand/voice/VOICE-CARD.md` + dial mode (default BLEND, per `skills/voice-os/SKILL.md`) as a layer BEFORE drafting — binding `farrice_voice_alignment`.

- A scored table (5 gates × pass/fail × one-line justification) for every candidate concept.
- A pass/route verdict per concept: PROCEED or ROUTE TO DEEPER SCORING (naming the specific tool: `/bank-lead-magnet` or `skills/stockton-walbeck-lead-magnets/`).
- If multiple concepts: a ranked recommendation naming the primary concept.
- An explicit statement of whether a paid-offer bridge exists at all.

## Output Skeleton

```
# Lead Magnet Bridge Score — [Expert/Brand]

## Concept: [name]

| Gate | Pass/Fail | Justification |
|---|---|---|
| Buyer outcome | | |
| Specificity | | |
| Fast value | | |
| Proof fit | | |
| Paid-offer bridge | | |

Verdict: [PROCEED / ROUTE TO DEEPER SCORING — tool: ___]

...(repeat per concept if more than one)

## Recommendation
Primary concept: [name]
Paid-offer bridge status: [exists / does not exist — flag]
```

## Quality Gate

- Is every gate scored pass/fail with a justification, not a vague summary?
- If any gate fails, does the verdict correctly route to deeper scoring rather than proceeding?
- Is the "no paid offer" case flagged explicitly when it applies, rather than assumed away?
- If multiple concepts were scored, is there a clear ranked recommendation?

## Deploy When

Once at least one lead magnet concept exists — before the AI prompt pack or the five post drafts are built, since both of those depend on the bridge being validated. Re-run this prompt any time the offer or ICP changes materially, since the bridge score is only valid against the inputs it was scored on.
