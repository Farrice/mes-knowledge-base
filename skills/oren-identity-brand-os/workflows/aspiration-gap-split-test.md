---
description: "/aspiration-gap-split-test — design a see-myself vs. see-who-I-want-to-be avatar split test, route the split audiences to separate creative and landing experiences, and run the four-question demo ladder before locking targeting."
---

# Aspiration-Gap Split Test

At Lift Foils, testing the brand's own pros against customer look-alikes against younger aspirational avatars surfaced something close to an even split between people who wanted to see themselves in the ad and people who wanted to see who they were chasing (Oren's practitioner account only — see the label below) [16:18]. The fix wasn't picking a winner. It was building two creatives and routing them to two different landing experiences, "because people bought for different reasons" [16:21]. This workflow builds that test.

## Pre-Flight Gate

> **🔒 Pre-Flight Gate**: cite genius.md **Pattern 10 — Aspiration-Gap Avatar Split**, **Pattern 11 — The Four-Question Demo Ladder**, and **Signature Move 5 — Split-And-Route**. This workflow requires `persona-reality-audit` to have already run (or existing real-buyer data) — you cannot split-test an avatar gap against an imagined persona. If no real audience data exists, stop and run that workflow first.

## Skill Acquisition

1. `skills/oren-identity-brand-os/genius.md` — Pattern 10 (Aspiration-Gap Avatar Split), Pattern 11 (Four-Question Demo Ladder), Signature Move 5 (Split-And-Route), Anti-Pattern note on the Lift ~50/50 figure.
2. Cross-stack: `dara-static-engine` / `dara-test-plan` for the ad-testing execution once avatars are defined; `copy-engine` for the routed landing-page copy per split.

## Input Required

- Confirmed real buyer profile (from `persona-reality-audit` or equivalent)
- Available avatar tiers: brand/pro talent, customer look-alikes, younger/aspirational look-alikes
- Testing budget and channel (paid social, email, landing-page infrastructure for split routing)

## Execution Steps

**Step 1 — Run the Four-Question Demo Ladder [17:08].** Answer each question separately, in sequence, without collapsing them: (1) Who is the actual demo (from the real-buyer audit)? (2) Who does that demo think they are? (3) Who do they want to be? (4) Who do they want to hear from? Question 4 breaks the mirror assumption — Oren's corollary example is a brand selling to elder women that converted better on young, good-looking male UGC than on same-demographic UGC [17:15]. Do not assume the messenger matches the demo.

**Step 2 — Build the Avatar Tiers.** Define at minimum: the brand's own team or pro-talent tier, a customer-look-alike tier (people who look like the actual buyer), and a younger/aspirational tier (who the buyer wants to become, per Question 3). Three tiers minimum; more if the real-buyer audit surfaced additional segments.

**Step 3 — Test, Don't Assume [16:18].** Run all tiers as live creative variants. State plainly: **the Lift Foils "roughly even split" is Oren's own practitioner recollection, not an externally verified benchmark** — treat it as a hypothesis worth testing on this brand's own data, never as a number to plan a budget around.

**Step 4 — Split-And-Route [16:21].** When the test reveals a genuine split (not just noise), do not average toward a single "winning" creative. Build separate landing experiences for each cluster — Lift routed "see-myself" viewers and "see-who-I-want-to-be" viewers to different landing pages because they bought for different reasons. Define what each landing experience emphasizes differently: proof and familiarity for see-myself; possibility and transformation for see-who-I-want-to-be.

**Step 5 — Confirm the Messenger Separately from the Avatar.** Using Question 4's answer, check whether the creative's on-camera talent should match the demo or the aspiration — these can diverge, and testing should isolate messenger choice from avatar choice where budget allows.

## Content Type Adaptations

| Format | Adaptation |
|---|---|
| Paid social ad testing | Full split as written; route to distinct landing pages per Step 4 |
| Email marketing | Split-send by cluster instead of separate landing pages; subject-line tone shifts per avatar |
| Organic content | Post-variant testing (see-myself vs. aspirational framing) across content pillars rather than paid split |
| Sales page / VSL | Build two proof stacks (peer-testimonial-led vs. transformation-led) rather than two full pages if budget is limited |

## Output Requirements

- Four-Question Demo Ladder answers, stated separately
- Avatar-tier definitions (minimum three)
- Test design (what's being measured, over what sample or timeframe)
- Split-routing plan (landing experiences or content variants per cluster) if a split is confirmed
- The Lift Foils figure explicitly labeled as an unverified practitioner claim, never cited as a benchmark

## Quality Gate

> Cite genius.md **Expert-Specific Quality Rubric** row **Aspiration crossability**: score 10 requires the aspirational self read as a reachable step, not a fantasy — check that the younger/aspirational avatar tier isn't an impossible ideal.
- Were all four ladder questions answered separately, none collapsed into "who is the customer"?
- Was the messenger choice (Question 4) tested independently from the avatar choice?
- Is the Lift Foils split explicitly flagged as unverified, never presented as a proven number?
- If a split was confirmed, was it routed to separate experiences rather than averaged into one creative?

Execution prompt: `references/prompts-v2/aspiration-gap-split-test.md` — honor its Output Contract.
