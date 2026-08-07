---
description: Define the buyer by temperament rather than demographics, name the constant doubt behind their purchase, and explicitly cede the opposite buyer to a competitor
tier: 3
stacks_with: /icp-deep-dive, /avatar-machine, /sv-ai-objection-kill, /sv-webinar-script
---

# /sv-customer-personality-lock — Target the Temperament

Produces a **temperament profile**: who the buyer is by disposition, what constant doubt drives the purchase, what language speaks to that disposition, and — the part everyone skips — **which buyer you are handing to a competitor.**

Sam's, in seven words: ***"My customer is the person who does things right. They cross every tea twice."***

## Pre-Flight Gate

Load `genius.md`. This workflow **layers onto** a demographic/psychographic profile — it does not replace one. If no ICP work exists, run `/icp-deep-dive` or `/avatar-machine` first and bring the output here.

The question this adds that those don't:

> **What disposition makes someone buy this — and which opposite disposition should you actively send elsewhere?**

## Skill Acquisition

1. `skills/sam-vander-wielen/genius.md`
2. `skills/sam-vander-wielen/references/source-quotes.md`
3. Any existing ICP/avatar work
4. Real customer language — support threads, replies, reviews, survey text

## Execution

### Step 1 — Name the temperament

Write it in one sentence, about disposition rather than demographics. Sam's is a *personality*, not a job title or income band: the person who does things right, who crosses every t twice.

Test: could two people with identical demographics land on opposite sides of this line? If not, it's not a temperament.

### Step 2 — Name the constant doubt

The recurring anxiety this temperament carries — **independent of whatever substitute currently exists.**

Sam's: *"My customer always has a seed of doubt in the back of their mind if they have not done this completely legitimately."*

Trace how the doubt attaches to different substitutes over time:
- Pre-AI: a friend's borrowed contract — *"use this contract, my lawyer made this, just change a few things"*
- Also pre-AI: copying a stranger's — *"go on Nathan's website and take his privacy policy, cuz clearly he has a good one"*
- The doubt that follows: *"but wait, what if Nathan took it from somebody else? How do we even know Nathan's is good?"*
- Now: ChatGPT

**The doubt is durable; the substitute is not.** Marketing built on the doubt survives the next substitute. Marketing built against ChatGPT expires.

### Step 3 — Name the ceded buyer

Write the opposite temperament as a real person a real competitor should serve well. Sam's: *"the move fast, do it cheap, and I'm willing to take on more risk"* buyer — and her verdict on the competitor who serves them: ***"Great for them."***

Include:
- Their disposition
- What they'd want instead
- What a competitor's marketing to them sounds like — Sam's read: *"save hundreds of thousands of dollars on legal fees"*
- Why serving both would weaken your position

Nathan's articulation of the payoff: *"You don't have to answer for everyone. You can carve off — this is the type of person, even down to basically the personality that we serve."*

### Step 4 — Build the language map

For the chosen temperament, capture:
- **Their words for the doubt** — verbatim from real sources, never paraphrased upward
- **The reassurance they need** — Sam's: *"you're never going to feel confident until you know you've taken the right steps and you've buttoned up everything and you have all your own stuff"*
- **What makes them bounce** — pressure, vagueness, anything that sounds like corner-cutting

⚠️ Ship the buyer's researched words **exactly**. Paraphrasing them into elevated prose kills credibility silently.

### Step 5 — Respect what the purchase means

Sam's operating input: *"I really try to stay in touch with what this purchase means about my customer… it's not just another person I can get to spend two grand. It's not a game to me. I know it's a big deal. You and I probably are the first purchase for a lot of people when they're starting out. And it's scary to spend that much money."*

Write one line: **what buying this says about the buyer, and what it costs them emotionally.** This drives the webinar reframe ask (`/sv-webinar-script` Beat 3).

### Step 6 — Wire it into the assets

| Asset | What the temperament changes |
|---|---|
| Webinar disqualifier | The reason names the temperament mismatch |
| AI objection | Built on the constant doubt, not on AI |
| Subject lines | The outcome is the one this temperament wants |
| Ad creative | Speaks to disposition, not demographics |

## Content Type Adaptations

| Context | Adjustment |
|---|---|
| **Real estate / housing** | ⚠️ Temperament language can proxy for protected classes. Fair-housing review required before any of this reaches public copy |
| **Employer / recruiting** | Same caution — disposition language near protected characteristics |
| **B2B** | Temperament attaches to the *buying role* (the risk-averse ops lead vs. the move-fast founder) |
| **Broad consumer** | May legitimately have two temperaments; run this twice and segment rather than blending |
| **Regulated (health/finance)** | Constant-doubt language often touches outcome claims; route through review |

## Output Schema

```
TEMPERAMENT LOCK — [Product]

## The Temperament
One sentence: [ ]
Demographic-independence test: PASS/FAIL

## The Constant Doubt
[one sentence, substitute-independent]
Substitute history:
| Era | The substitute | The doubt it produced |

## The Ceded Buyer
Disposition: [ ]
What they want instead: [ ]
What a competitor says to them: [ ]
Why we don't serve them: [ ]

## Language Map
| Their words (VERBATIM — do not elevate) | Source |
Reassurance they need:
What makes them bounce:

## What the Purchase Means
What buying this says about them: [ ]
What it costs them emotionally: [ ]

## Asset Wiring
| Asset | Change |

## Compliance flags
```

## Quality Gate

Reject and rebuild if:
- The temperament is a demographic in disguise (fails the independence test)
- **No buyer is ceded** — this is the step that makes the position real
- The constant doubt is defined against the current substitute (it will expire)
- Customer language is paraphrased into elevated prose rather than quoted verbatim
- The "what the purchase means" line is missing — without it the assets treat buyers as transactions
- Temperament language ships into housing, lending, or employment copy without review

**Execution prompt**: `references/prompts-v2/temperament-lock.md`
