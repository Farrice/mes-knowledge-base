---
description: "/persona-reality-audit — audit the actual buyer list against the imagined persona before any targeting or creative decision, diagnose wrong-person vs. funnel-mismatch, and name the aspiration gap."
---

# Persona Reality Audit

"They'll think... we sell to the hip Gen Z girl. But then you pull it up... you sell to the older Gen X woman. But that older Gen X woman wants to be that younger Gen Z woman" [09:54]. Oren walks into every persona conversation expecting a mismatch, because the reveal is reliable. This workflow runs that same audit: real data first, imagined persona second, and a named diagnosis for whichever gap surfaces — because a persona built on the imagined buyer optimizes for someone who was never going to buy.

## Pre-Flight Gate

> **🔒 Pre-Flight Gate**: cite genius.md **Pattern 8 — Persona-Reality Audit** and **Signature Move 4 — Audit-The-Actual-List-First**. Do not accept a stated persona ("we sell to X") as ground truth until the actual buyer list has been pulled. If no real buyer data exists yet (true zero-point), route to `identity-zero-point` instead — this workflow requires an existing audience to audit.

## Skill Acquisition

1. `skills/oren-identity-brand-os/genius.md` — Pattern 8 (Persona-Reality Audit), Signature Move 4 (Audit-The-Actual-List-First), rubric row "Real-buyer grounding."
2. Cross-stack: `icp-deep-canvasser` for identity-level depth once the real buyer is confirmed; `avatar-machine` for a full avatar build downstream.

## Input Required

- Actual buyer/subscriber list, or the closest available proxy (ESP data, order history, ad-account audience insights, social-follower demographic breakdown)
- The imagined persona currently in use (whatever's written in the brief, deck, or brand doc)
- Funnel map (how buyers actually arrive — organic, paid, referral, in-person)

## Execution Steps

**Step 1 — Pull the Actual List [09:25].** Before opening the brief, pull real data on who's actually buying. Oren names a specific tool ("Audience Signal") that could not be independently verified as a real product [UNCONFIRMED] — describe the mechanism (running your list through a persona-clustering pass), not the tool name. Use whatever's available: your ESP's segment data, a persona-clustering tool, or a manual cross-tab of order data against social profiles.

**Step 2 — State the Imagined Persona.** Write down, verbatim, who the brief currently claims the buyer is. Do not soften or hedge it — the gap only shows up if both sides are stated plainly.

**Step 3 — Compare and Name the Gap [09:54].** Lay the actual list beside the imagined persona. Three possible outcomes: (a) they match — rare, note it and move on; (b) mismatch with an aspiration gap — the real buyer is older or different but *aspires* to be the imagined persona (his Gen X/Gen Z example); (c) mismatch with no aspiration link — the real buyer simply isn't who the brief assumes, full stop.

**Step 4 — Diagnose the Failure Mode.** Two named failure modes, pick one: **marketing to the wrong person** (the brief targets someone real but who isn't the actual buyer and never will be), or **funnel mismatch** (the intended buyer exists but never makes it through the funnel — the product, price point, or channel filters them out before purchase). These require different fixes: the first needs a persona rewrite, the second needs a funnel audit.

**Step 5 — Route the Aspiration Gap (if present).** If Step 3 surfaced an aspiration link, do not flatten it into the demographic reality — serve the identity the real buyer *wants*, not the one their age bracket implies. This feeds directly into `aspiration-gap-split-test` if the gap is testable in ad creative.

## Content Type Adaptations

| Format | Adaptation |
|---|---|
| E-commerce / DTC | Actual list = order history + ESP segments; funnel-mismatch check includes cart-abandon data |
| B2B / service | Actual list = closed-deal CRM records, not lead-gen form fills |
| Content / newsletter | Actual list = subscriber survey + engagement data, not raw follower count |
| Ad-account audit | Actual list = Meta/Google audience insights against the stated target |

## Output Requirements

- Actual-list summary (who's really buying, in plain language)
- Imagined-persona statement (verbatim from the brief)
- Gap verdict: match / aspiration-gap mismatch / clean mismatch
- Failure-mode diagnosis: wrong-person or funnel-mismatch, with the reasoning
- One recommended next action (persona rewrite, funnel fix, or handoff to split-test)

## Quality Gate

> Cite genius.md **Expert-Specific Quality Rubric** row **Real-buyer grounding**: score 10 requires an audited list with the mismatch surfaced and the aspiration gap explicitly named, not an imagined persona presented as plausible.
- Was the actual list pulled before any persona language was accepted?
- Is the failure mode named specifically (wrong-person vs. funnel-mismatch), not left vague?
- If an aspiration gap exists, was it served rather than flattened?
- Was "Audience Signal" avoided as a verified product name?

Execution prompt: `references/prompts-v2/persona-reality-audit.md` — honor its Output Contract.
