---
description: Generate expert-powered viral video hooks for Jen Santulan's Instagram real estate property tours
---

# /listing-content — Jen's Expert-Powered Viral Hook Engine

Generate 6 video hooks for any property using Jen Santulan's authentic voice, powered by viral content frameworks from Kallaway, Brock Johnson, Seena Rez, Shaan Puri, and Harry Dry. Two-pass architecture: expert mechanics → Jen voice polish.

## Usage

```
/listing-content [property address or Zillow/Redfin URL]
```

## Steps

### 1. Property Research

Research the property using web search. Collect:

| Data Point | Required |
|------------|----------|
| Address, beds, baths, sqft | Yes |
| Price (list or estimated) | Yes |
| Property type (SFR, townhome, condo) | Yes |
| Key features (garage, pool, views, upgrades, finishes) | Yes |
| Year built | Yes |
| Lot size | If SFR |
| HOA details + community amenities | If condo/townhome |
| Neighborhood median home price | Yes |
| Nearby amenities (dining, shopping, schools, parks, recreation) | Yes |
| Freeway access / commute context | Yes |
| Market trends (year-over-year appreciation) | If available |
| Current comparable rental rates in the area | Yes |

**Factual accuracy is critical.** All data must be verified via web search. Do not guess or fabricate stats.

### 2. Key Selling Points Analysis

Before writing any hooks, complete this analysis:

**A. Key Property Features (5)** — The standout features that make this property special.

**B. Unique Selling Points (3)** — What combination of features makes this property rare or exceptional at its price point?

**C. Target Buyer Personas (3)** — Who is most likely to buy this property?
- For each: describe their situation, what they're upgrading from, what problem this property solves
- At least one persona MUST be a first-time buyer (Jen's niche)

**D. Neighborhood Advantages (3)** — What lifestyle benefits does the location provide? Name specific places (Westfield Topanga, Lake Balboa Park, etc.).

**E. Market Context (3 data points)** — How does this price compare to the area median? What's the market trend? What's the rent-vs-buy math?

**F. Expert Scrollstop Audit** — Answer these 4 questions:
1. What is the single most UNEXPECTED fact about this property? (The thing that makes you go "wait, really?")
2. What common belief about this area or price point does this property contradict?
3. What is the genuine scarcity element? (Low inventory, gated, unique feature, price vs. comps, etc.)
4. What micro-moment does this property enable that would make a great 3-second video opening?

**G. First-Time Buyer Angle** — Answer these 3 questions:
1. What is the rent-vs-mortgage math? (Current comparable rent vs. estimated mortgage at current rates)
2. What first-time buyer advantages exist at this specific price point?
3. What is the "permission moment"? (What makes a renter think "I could actually afford this")

### 3. Expert Analysis Pass (Internal Strategic Layer)

Using data from Steps 1-2, produce this strategic material. This is the raw intelligence that feeds into hook generation — it won't appear in the final deliverable.

**3A. Scrollstop Inventory**
Generate 3-4 potential scrollstop openers (5-8 words each) using different disruption types:
- Contradiction: "[Fact] that contradicts what they assumed"
- Specificity shock: "[Exact numbers] that are jaw-dropping together"
- Mid-action: "STOP. [Urgent personal address]"
- Insider reveal: "I wasn't going to post this yet, but..."

**3B. FTHB Permission Moment**
- The specific rent-vs-own math (with real numbers)
- The "you can do this" angle — what proof exists?
- What first-time buyer would say if they saw this listing

**3C. Emotion Map**
Assign exactly ONE target emotion per format:
1. Scrollstop Discovery → "Wait, what?"
2. First-Time Buyer Permission → "I could actually do this"
3. Lifestyle Transformation → "I want that life"
4. Smart Money → "I'd be smart to jump on this"
5. Scarcity / Urgency → "I can't miss this"
6. Complete Package → "This checks every box"

**3D. Share Triggers**
For each format, answer: "Why would someone send this to a friend?"
- Identity: "This is us!"
- Practical: "We should look at this"
- Social currency: "Can you believe this exists?"
- Tribal: "This is what WE deserve"

**3E. Scarcity Angle**
Identify the genuine urgency element. If none exists, define the "hidden gem" reframe.

**3F. Contrarian Data Point**
The one verifiable fact that subverts the viewer's expectations about this area/price/property type.

### 4. Generate 6 Video Hooks

Read and apply the master prompt at `skills/jen-santulan-listing-content/PROMPT.md`.

Generate 6 complete hooks — one per format. Each hook is a **single continuous block of spoken text** that Jen reads straight through on camera. **80-120 words spoken.**

Use the Expert Analysis from Step 3 as raw material. Write each hook in Jen's voice — warm, enthusiastic, conversational. The expert mechanics should be invisible to the viewer; they should only feel Jen's warmth and genuine excitement.

**Format per hook:**
```
## Hook [#]: [Format Name]
**Target emotion:** [one word/phrase]
**Word count:** [X words] (~[X] seconds spoken)

"[Complete spoken text including emoji placement and hashtags]"

*Why it works: [1-2 sentences on the psychological mechanic AND why it sounds like Jen]*
*Share trigger: [Why someone would send this to a friend]*
```

**The 6 formats:**
1. **Scrollstop Discovery** — Pattern interrupt opener into dream-worthy reveal (80-100 words)
2. **First-Time Buyer Permission** — Pain naming, permission moment, proof point (90-110 words) **← ALWAYS GENERATED**
3. **Lifestyle Transformation** — Vivid micro-moment, neighborhood life, share trigger (90-110 words)
4. **Smart Money** — Contrarian data, curiosity gap, education through surprise (85-105 words)
5. **Scarcity / Urgency** — Genuine scarcity fact, rare feature set, urgency invitation (75-95 words)
6. **Complete Package** — Rhythmic checklist reveal, rapid feature stacking, save trigger (85-105 words)

### 5. Quality Gate

Run all 6 hooks through the 11-test quality gate defined in the PROMPT.md. Any **must-pass** failure triggers a rewrite of that specific hook. Document pass/fail results briefly.

**Must-pass (7):** Warmth, First-Timer, Scrollstop, Length, Factual, Hashtag, FTHB Presence
**Should-pass (4):** Three Rules (Harry Dry), Share Test (Brock Johnson), One Emotion (Shaan Puri), Pattern Diversity

### 6. Performance Enhancement Notes

After all hooks, provide:

**Key Selling Points (✅ checklist):**
Quick-reference checklist of the property's strongest angles for Jennifer.

**Visual Strategy:**
- What to show in the first 3 seconds of each hook (must match the scrollstop)
- Which property features to point to on camera
- Suggestions for B-roll or location graphics
- On-screen text recommendations for key stats

**Delivery Guidelines:**
- Energy level and authentic emotion
- Hand gestures and movement through the property
- Signature phrases to emphasize
- How to close each hook naturally

**Share Engineering Notes:**
- Which 2 hooks are most shareable and why
- Suggested "send to" CTA for caption or pinned comment
- Which hooks are most likely to be saved (reference/checklist value)
- Screenshot-worthy moment recommendations

## Output Format

Deliver in this order:
1. Property Profile (table)
2. Key Selling Points Analysis (A through G)
3. Expert Analysis Pass (scrollstop inventory, FTHB permission, emotion map, share triggers, scarcity angle, contrarian data)
4. 6 Video Hooks (each with format label, target emotion, word count, full spoken text, "why it works" note, share trigger)
5. Quality Gate Results (brief pass/fail)
6. Performance Enhancement Notes (key selling points checklist, visual strategy, delivery guidelines, share engineering notes)
