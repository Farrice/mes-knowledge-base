---
description: Mandatory copy and social quality gate for LinkedIn revenue copy, AI Misfire punch passes, public offers, outreach, marketplace proposals, checkout copy, punch, voice, and tension
---

# /publishable-copy-gate - Publishable Copy Gate

## Purpose

Prevent public, revenue-critical, client-facing, or market-facing copy from shipping while it is only strategically correct.

This gate exists because "fundamentally sound but flat" is a failure state. Publishable copy must create attention, tension, buyer recognition, proof pressure, and a clear next action.

## Trigger

Run this gate before Autopilot treats any of these as publishable:

- LinkedIn posts, first comments, comment banks, carousels, scripts, or newsletters
- outreach, DM bridges, email copy, follow-ups, or reply scripts
- offers, checkout copy, sales pages, landing pages, VSLs, ads, or CTAs
- marketplace proposals or job-application openers
- client-facing copy, public proof assets, revenue-critical public writing, or acquisition assets

Allowed skip reasons:

- not public-facing
- not copy
- user requested raw strategy only
- explicit skip from the user
- local artifact sidecar includes `skipCopyGate: true` with a concrete `skipReason`

## Required Stack

Use the stack. Do not merely name it.

1. `/copywriting-agent --deep`
   - Reject generic, merely professional, or strategically correct but flat output.
   - Force punch, voice, tension, buyer language, enemy, proof, CTA, and platform fit.
2. `/high-taste-writing-os` when the issue is flow, taste, reader pull, voice, perspective shift, or "correct but I do not want to read it."
   - Compose the piece before scoring conversion quality.
   - Require a Taste Evidence Ledger for high-stakes public/revenue copy.
3. `/low-cognitive-load-message-gate` when the copy asks the buyer to decode the problem, offer, CTA, proof, or brand role.
   - Run before final copy scoring.
   - Treat its result as supporting evidence for clarity, buyer language, CTA clarity, and anti-slop.
   - It does not replace the required `Copy Gate Result`.
4. `/excellence-gate --domain copy`
   - Fail slop, abstraction, unsupported claims, vague promise, and weak CTA.
5. Platform-specific social gates:
   - LinkedIn default: Lara Acosta for hook, rehook, F-shape, and authority borrowing.
   - LinkedIn default: Josh Sanders for reach, comment strategy, and early distribution.
   - LinkedIn default: Kallaway for non-obvious frame and cultural/market tension.
   - LinkedIn default: Erica Mallet for enemy, belief shift, voice, and magnetic positioning.
6. Offer and conversion support when relevant:
   - Cardinal Mason for buyer language, context depth, proof clarity, and conversion logic.
   - Revenue Offer Agent when the copy changes price, promise, scope, or buying path.
7. Sam Parr mechanics support when relevant:
   - `/sam-parr-copywriting-mechanics` for headline gravity, curiosity gaps, proof-first ads, story-led desire, visual proof translation, objection-by-detail, rhythm, humor fit, and copywork benchmarks.
   - Use only as a bounded mechanics pass. It never replaces this gate.

## Publishable Checks

Every public or revenue-critical copy asset must score at least 8/10 on the major dimensions before final delivery.

Before revising a draft that already has a strong hook, scene, voice, proof, or
tension, create a `Preservation Lock` from `/repeatability-spine` so the pass
does not flatten the strongest voice/proof/tension while improving polish.

If the user has rejected a prior version as generic, flat, confusing, over-scored, or not deployable, the gate starts from that user-calibrated baseline. Do not preserve prior high scores. Name the exact failure and what changed before assigning any PASS.

Hard rule: if the **User-calibrated baseline** is **≤ 4/10**, the verdict must be **REVISE** or **REWORK** until the delta is demonstrated. Do not ship a ceremonial PASS while the user is saying “this is a 3–4/10”; lower scores, explain the mechanism change, and rerun the gate after revisions.

| Dimension | Pass Standard |
|---|---|
| Hook | Stops the right buyer without sounding like generic AI commentary. |
| Punch | Has compression, surprise, and forward motion. |
| Voice | Sounds like Farrice's Creative Strategist + AI Operating Partner lane, not category wallpaper. |
| Tension | Names a real contradiction, cost, enemy, or emotional pressure. |
| Buyer language | Uses the buyer's felt language: "looks finished but I still have to rescue it." |
| Low cognitive load | One problem, plain offer language, customer-as-hero, and repeatable phrase are clear before conversion scoring. |
| Brand-jack / attention anchor | Borrows current attention ethically without fake affiliation. |
| Enemy / belief | Makes the wrong belief visible and gives the reader a sharper one. |
| Proof | Shows the correction, mechanism, or diagnostic lens instead of relying on claims. |
| Sam Parr mechanics | If used, shows original weak section, rewritten section, proof object or proof gap, curiosity gap, rhythm pass, story desire path, objection detail, humor fit, copywork plan, and reader-behavior delta where relevant. |
| CTA | Asks for one concrete artifact or next step, not a vague call. |
| Anti-slop | Removes filler, cliches, hype, lazy abstractions, and "AI automation" wallpaper. |
| Platform fit | Fits the channel's reading behavior, comment mechanics, and conversion path. |

If any major score is below 8/10, revise before final delivery. Do not ship a confidence note around weak copy.

## Score Discipline

High scores require proof. A 9+ is reserved for copy with live market/user evidence, a validated buyer quote, or a clearly observed performance signal. Expert-name routing, clean formatting, or a static prose check is not enough.

Flag and revise before final if:

- the average score is inflated above the evidence,
- the gate says PASS while the user has just scored the draft 3-4/10,
- the proof is only "expert stack applied,"
- the review only says a classifier passed,
- the hook creates confusion instead of curiosity,
- the copy is coherent but does not create buyer recognition or action pressure.

## LinkedIn Default Gate

For LinkedIn assets, apply this lens:

- Lara Acosta: first line, rehook every 6-8 lines, F-shape scan, authority borrowing without name-dropping theater.
- Josh Sanders: comment-worthiness, early engagement path, manual reply fuel, and comments that add distinctions.
- Kallaway: non-obvious angle, cultural tension, and a frame the feed has not already flattened.
- Erica Mallet: belief-first structure, named enemy, voice magnetism, and identity pull.

## Output Requirement

Every gated artifact or final answer must include a real `Copy Gate Result`.

When revising an existing strong draft, include:

```markdown
## Preservation Lock
- **Keep**: [strongest voice/proof/tension]
- **Change**: [specific revision request]
- **Do not disturb**: [lines, mechanism, scene, or buyer recognition]
- **Risk**: [likely flattening/degradation]
- **Gate**: `/publishable-copy-gate`
```

```markdown
## Copy Gate Result

| Dimension | Score | Evidence | Revision Applied |
|---|---:|---|---|
| Hook | 0-10 | [specific line or mechanic] | [what changed] |
| Punch | 0-10 | [specific line or mechanic] | [what changed] |
| Voice | 0-10 | [specific line or mechanic] | [what changed] |
| Tension | 0-10 | [specific line or mechanic] | [what changed] |
| Buyer language | 0-10 | [specific line or mechanic] | [what changed] |
| Low cognitive load | 0-10 | [specific gate result or "not used"] | [what changed] |
| Brand-jack / attention anchor | 0-10 | [specific line or mechanic] | [what changed] |
| Enemy / belief | 0-10 | [specific line or mechanic] | [what changed] |
| Proof | 0-10 | [specific line or mechanic] | [what changed] |
| Sam Parr mechanics | 0-10 | [specific direct-response mechanic, or "not used"] | [what changed] |
| CTA | 0-10 | [specific line or mechanic] | [what changed] |
| Anti-slop | 0-10 | [specific line or mechanic] | [what changed] |
| Platform fit | 0-10 | [specific line or mechanic] | [what changed] |

**Verdict:** PASS / REVISE / REWORK
**Current intent marker:** [artifact/session marker when applicable]
**User-calibrated baseline:** [prior user score/rejection signal, or "none available"]
**Failure addressed:** [specific change from rejected/weak version]
**Score discipline:** [why these scores are not inflated; name live proof if any 9+ appears]
**Expert deployment evidence:** [what each expert lens changed, not just names]
**Prose/slop review:** [manual anti-slop review plus any tools; classifier-only is not sufficient]
**Skipped gates:** [none or exact reason]
**Remaining risk:** [specific risk, not a generic caveat]
```

## Guardrail

If an artifact says it used Copywriting Agent, social expert routing, public/revenue copy, or publishable copy, it must either include `Copy Gate Result` or carry an explicit sidecar skip.
