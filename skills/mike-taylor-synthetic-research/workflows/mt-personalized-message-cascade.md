---
description: "/mt-personalized-message-cascade — after a top-level message validates in aggregate, re-run the SAME grounded panel to find individual/segment-level positioning angles. Insight-mining discipline, not a copy generator: find the angle, then write the real copy yourself."
---

# Personalized Message Cascade

"I use this more for insights in general... and then once I understand the angle of attack, then I'll kind of write it myself." This workflow is the step after a message validates in aggregate — it exists to find HOW to say the validated thing differently to different people, never to ship the AI's draft as the finished piece.

## Pre-Flight
Read `skills/mike-taylor-synthetic-research/genius.md` (Pattern 15).

> **Pre-Flight Gate**: A top-level message/offer must already be validated (via `mt-persona-panel-triage.md` or `mt-concept-headline-triage.md`) before this workflow runs. This cascades FROM a validated aggregate — it doesn't generate one.

## Input Required
- The validated top-level message/offer
- The grounded panel (real customer transcripts, per `mt-persona-grounding.md`, if available — this workflow is strongest when grounded; cold-generated personas can still run it, with a lower-confidence label)
- The individual or segment to personalize for (a named real customer if grounded, or a persona role if not)

## Workflow

### Step 1: Confirm the Validated Message
State the top-level message this cascade is personalizing. Do not run this workflow on an unvalidated message — that's `mt-persona-panel-triage.md`'s job.

### Step 2: The Personalization Prompt
Issue the individual-level ask against the grounded (or persona) context:
> "Write a personalized [email/message] to [Name/Role] telling them about [the validated offer/message]."

### Step 3: Extract the Angle, Not the Copy
Read the output for WHAT made it different from a generic version — which specific concern, phrase, or framing did it lead with for this person? That angle is the deliverable. The literal sentences the model wrote are draft material, not the finished asset.

### Step 4: Human-Written Final Pass
Write the actual outreach/copy yourself, informed by the extracted angle. State explicitly in the output that the AI draft was used for angle discovery and the shipped version is human-written.

### Step 5: Repeat Per Segment, Not Per Individual at Scale
This workflow is built for high-value individual outreach (a specific named customer, a specific segment worth 5 minutes) — not for mass-personalizing hundreds of emails. At scale, the angle-finding insight from a few representative runs should generalize into segment templates, not get re-run per recipient.

## Content Type Adaptations
| Format | Adaptation |
|---|---|
| Sales outreach to a known lead | Direct application — grounded if a transcript/call history exists |
| Re-engagement email to a churned customer | Ground in their actual stated churn reason if known |
| Investor/partner pitch personalization | Same shape; angle = what this specific reader cares about, not a generic pitch |
| Segment-level (not individual) email variants | Run once per segment persona, extract angle, template the segment — never per-recipient at scale |

## Output Format
```
PERSONALIZED MESSAGE CASCADE — [recipient/segment] — [date]
VALIDATED TOP-LEVEL MESSAGE: [...]
GROUNDING: [transcript-grounded / persona-based]

AI DRAFT (angle-discovery only, not final)
[the model's draft]

EXTRACTED ANGLE: [what made this framing specific to this recipient — the concern/phrase/emphasis that differs from generic]

HUMAN-WRITTEN FINAL
[the actual shipped copy, informed by the angle, written by the operator]
```

## Quality Gate
> Review against `genius.md § Quality Rubric` before delivering.
- [ ] The top-level message being personalized was already validated, not generated fresh here
- [ ] The AI draft is explicitly labeled angle-discovery material, never presented as final copy
- [ ] The extracted angle names a specific concern/phrase/framing, not a vague "make it more personal"
- [ ] A human-written final pass exists and is distinguished from the AI draft in the output
- [ ] This workflow wasn't run per-individual at mass scale — segment templating used instead

## Common Pitfalls
- **Shipping the AI draft verbatim.** This is the exact discipline break Taylor names explicitly — the model finds the angle, the human writes the sentence.
- **Running this on an unvalidated message.** Personalizing an unvalidated pitch just personalizes the wrong thing faster.
- **Scaling this per-recipient instead of per-segment.** Defeats the purpose and produces uneven quality across hundreds of drafts.

Execution prompt: `references/prompts-v2/personalized-message-cascade.md`
