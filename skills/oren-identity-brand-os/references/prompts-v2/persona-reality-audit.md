---
name: "Oren John — Persona Reality Audit"
source_prompt: born-v2
skill: oren-identity-brand-os
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-15
---

## Role & Activation

You are running Oren John's Persona Reality Audit. Oren walks into every persona conversation expecting the real buyer to differ from the imagined one — he treats the reveal as reliable enough to run every time. His diagnostic example: "They'll think... we sell to the hip Gen Z girl. But then you pull it up... you sell to the older Gen X woman. But that older Gen X woman wants to be that younger Gen Z woman" [09:54]. This audit pulls real data first and treats the stated persona as a hypothesis to be tested, never a given.

## Input Required

- [ACTUAL LIST]: the real buyer/subscriber list or closest proxy (ESP data, order history, ad-account audience insights)
- [IMAGINED PERSONA]: the persona currently stated in the brief, deck, or brand doc, verbatim
- [FUNNEL MAP]: how buyers actually arrive (organic, paid, referral, in-person)

## Execution Protocol

**Step 1 — Pull the Actual List [09:25].** Before touching the brief, pull real data on who's actually buying. Oren names a specific tool ("Audience Signal") that could not be independently verified as a real product — [UNCONFIRMED]. Describe the mechanism (a persona-clustering pass over [ACTUAL LIST]), never assert the tool name as real. Use ESP segment data, order-data cross-tabs, or an equivalent persona-clustering tool.

**Step 2 — State the Imagined Persona.** Reproduce [IMAGINED PERSONA] verbatim, unsoftened. The gap only shows up if both sides are stated plainly, not hedged toward each other in advance.

**Step 3 — Compare and Name the Gap [09:54].** Classify the result: (a) match — rare, note it; (b) mismatch with an aspiration gap — the real buyer differs but aspires to be the imagined persona; (c) clean mismatch — no aspiration link, the real buyer simply isn't who the brief assumes.

**Step 4 — Diagnose the Failure Mode.** Name exactly one: **marketing to the wrong person** (targets someone real, but not the actual buyer) or **funnel mismatch** (the intended buyer exists but the product, price, or channel filters them out before purchase). These require different fixes — do not blend them.

**Step 5 — Route the Aspiration Gap.** If Step 3 found an aspiration link, do not flatten it to demographic reality — name the identity the real buyer wants served, not the one their bracket implies.

## Output Contract

- Actual-list summary in plain language
- Imagined-persona statement, verbatim
- Gap verdict: match / aspiration-gap mismatch / clean mismatch
- Failure-mode diagnosis, named specifically, with reasoning
- One recommended next action
- No assertion of "Audience Signal" as a verified product name

## Output Skeleton

```
PERSONA REALITY AUDIT — [brand] — [date]

ACTUAL LIST: [who's really buying, plain language]
IMAGINED PERSONA (verbatim): "[stated persona]"

GAP VERDICT: [match / aspiration-gap mismatch / clean mismatch]
[if mismatch] Aspiration link: [what the real buyer wants to become, if any]

FAILURE MODE: [wrong-person / funnel-mismatch]
Reasoning: [why this diagnosis, not the other]

NEXT ACTION: [persona rewrite / funnel audit / handoff to aspiration-gap-split-test]
```

## Quality Gate

- Was the actual list pulled before any persona language was accepted as fact?
- Is the failure mode named specifically, not left vague or blended?
- If an aspiration gap exists, was it named and routed rather than flattened?
- Is "Audience Signal" described only as a mechanism, never asserted as a verified product?

## Deploy When

Before any targeting, creative-brief, or persona-defining decision — mandatory prerequisite for `aspiration-gap-split-test` and `two-demographic-split`.
