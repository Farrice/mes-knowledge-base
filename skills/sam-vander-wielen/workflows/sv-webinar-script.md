---
description: Write the live webinar run-of-show on the Vander Wielen structure — consent ask, self-costing disqualifier, standalone teaching, gap-naming close, on-webinar bonus stack
tier: 1
---

# /sv-webinar-script — The Consent-and-Disqualify Webinar

Produces the **run-of-show plus scripted beats** for a live webinar built to sell at $1,000+ without pressure. This structure produced **128 sales in about five minutes** — Sam's *"most on-webinar signups ever."*

The whole design rests on one inversion: **you ask permission to sell, then you narrow who is allowed to buy.** Attendees describe the result as *"I didn't feel like I had to buy. I wanted to."*

## Pre-Flight Gate

Load `genius.md`. Score the planned webinar on the **Decision Rubric**:

| Level | Name |
|---|---|
| 1 | Pressure |
| 2 | Signposted |
| 3 | Granted |
| 4 | Narrowed |
| 5 | Relaxed Confidence |

**Ship at 4. Aim for 5.** If the draft sits at 1–2, rebuild the structure — do not polish the copy.

Also run the Recognition Test: *would a non-buyer still feel they got the better end of the deal?* If the teaching is a teaser for the paid product, the whole script fails.

## Skill Acquisition

1. `skills/sam-vander-wielen/genius.md`
2. `skills/sam-vander-wielen/references/source-quotes.md` — **the open and close are near-verbatim deployable; read them before writing**
3. The offer being sold + its price
4. The one thing the audience must believe to buy

## Execution

### Beat 1 — The Consent Ask (first 5 minutes, before any teaching)

Adapt this structure, keeping the shape:

> "After you've attended this live training, this free next hour is going to be very valuable. **Is it okay with you if at the end of this training I share with you about [OFFER]? Say yes in the comments.**"

Requirements:
- It is a **real question** in the chat, not a rhetorical signpost
- It comes **before** the teaching, so the audience grants it rather than tolerates it
- The value promise for the free hour is specific

### Beat 2 — The Disqualifier (immediately after the yes)

> "And by the way — that's if it's a good fit for you **and for me**. I don't want you to buy it if you're not the right fit, because **[REASON THAT COSTS YOU SOMETHING REAL]**."

**The reason is the whole mechanic.** Sam's: *"because I know I'm going to have to deal with you on the back end"* — credible because she still personally answers support for 5,500 members. A generic "I only want the right people" reads as a tactic and scores 3, not 4.

Find the presenter's true cost: personal delivery time, capacity limits, a support promise, a refund policy they actually honor. **If no real cost exists, do not fake one** — ship at level 3 and say so.

### Beat 3 — The Reframe Ask

Somewhere early, ask the audience to change posture, not just pay attention:

> "What if we stopped acting like this thing wasn't going to work and just started planning for it to work out?"

Adapt to the domain. This is the belief shift the offer later resolves.

### Beat 4 — The Teaching (the standalone hour)

Deliver complete, usable value on **one** problem. It must genuinely stand alone. Structure it so that finishing it **opens a specific next question** — that question is what the close and the bonus will answer.

Do not withhold the good part. Sam's audience gets the entire legal roadmap free.

### Beat 5 — The Gap-Naming Close

Name the gap your own teaching just created, then resolve it:

> "Today I've taught you [WHAT THEY NOW KNOW]. But even if you do that — [THE QUESTION THAT REMAINS]? [SECOND FORM OF IT]? It's all right here. I taught you everything I know. And I'm going to send it to you free if you purchase right now."

Requirements:
- The gap must be **real and created by the teaching**, not manufactured
- The bonus **answers exactly that gap** (Sam's book teaches the marketing her legal training doesn't)
- Show the bonus physically if it's physical

### Beat 6 — On-Webinar Bonus Stack

- A live-only financial incentive (Sam added one for the first time this launch)
- A live-only bonus the replay will not carry
- Both stated plainly, once, without countdown theatre

### Beat 7 — The Order Bump Handoff

Checkout carries the multi-bump stack. Build in `/sv-order-bump-stack`.

## Content Type Adaptations

| Context | Adjustment |
|---|---|
| **Selling a call, not a checkout** | Close asks for the booking; the bonus is a pre-call asset that answers the gap |
| **Regulated industry (legal/medical/financial/housing)** | Disqualifier language gets compliance review. In real estate, "who this isn't for" carries fair-housing risk — route through review before writing |
| **Recorded/evergreen webinar** | Consent ask still works ("type yes"), but the *live* comment surge is gone; compensate with a stated commitment prompt |
| **Low-ticket (<$500)** | Keep consent, drop the disqualifier — the capacity cost isn't credible at that price |
| **Cold audience** | Extend the teaching, shorten the close; the gap must be even more concrete |

## Output Schema

```
WEBINAR RUN-OF-SHOW — [Offer] — [Date]

Rubric score: [1–5] — [named level] — [why]
Recognition Test: PASS/FAIL — [reasoning]

| # | Beat | Minutes | Purpose |

## Scripted Beats
### Consent Ask (verbatim)
### Disqualifier (verbatim)
  - The real cost cited: [ ]
  - Why it is credible: [ ]
### Reframe Ask (verbatim)
### Teaching outline
  - Standalone value delivered: [ ]
  - The question it opens: [ ]
### Gap-Naming Close (verbatim)
  - The gap: [ ]
  - How the bonus answers it: [ ]
### Bonus stack (live-only vs. replay-carried)

## Chat Prompts (where the audience types)

## What the replay does NOT get
```

## Quality Gate

Reject and rebuild if:
- The consent ask is rhetorical rather than a real chat question
- The disqualifier's reason costs the seller nothing (fake scarcity — scores 3, don't claim 4)
- The teaching does not stand alone
- The bonus does not answer the gap the teaching opened
- Countdown-timer urgency substitutes for a real deadline
- Any figure from Sam's launch appears as the user's own projection
- Disqualification language ships into a regulated vertical without review

**Execution prompt**: `references/prompts-v2/webinar-run-of-show.md`
