---
description: Diagnose the gap between brand language and customer language — outputs the second-order unlock after product-market fit
---

# `/vince-messaging-market-fit-diagnostic` — Messaging-Market Fit Audit

Vince's second-order unlock. Product-Market Fit gets you to revenue. Messaging-Market Fit gets you to scale. This workflow diagnoses the gap and outputs ICP-resonant message variations grounded in actual customer voice.

## Genius Context (Load First)

Read `genius.md`. Internalize:
- **Pattern 2: Messaging-Market Fit as the Second-Order Unlock**
- **Pattern 1: The Data Bank**
- **Hidden Knowledge 4: Audience-First Product Discovery Inversion**

Then read `references/data-bank-source-mining.md` and `references/emotional-angle-library.md`.

## When to Run

- Brand has clear PMF but ad performance has plateaued
- New brand whose first ads feel "from the brand," not "from the customer"
- Brand expanding to new ICP segment (need MMF audit per segment)
- Pre-launch when product is finalized but messaging hasn't been tested
- Strategist sense-check: "Are we writing copy or extracting it?"

## Pre-Flight Gate

| Question | If NO → |
|---|---|
| Does the data bank exist (run `/vince-data-bank-build` first)? | Run that workflow first — this depends on it |
| Has brand shipped at least 30 days of paid ads? | Need ad copy corpus to compare against |
| Is brand at $500K+ revenue (PMF signal)? | Pre-PMF — message-MF audit is premature; focus on PMF |

## Input Required

- **Data bank** (output from `/vince-data-bank-build`)
- **Current ad copy** (top 20 ads by spend, last 90 days)
- **Landing page headlines** (all hero + product page H1s)
- **Email subject lines** (last 30 sent)
- **Brand voice doc** (if exists) or marketing director's stated brand voice principles
- **ICP definition** (current understanding of who you're talking to)

## Execution

You are Vince Nijhof diagnosing messaging-market fit. You don't suggest "better copy" — you surface the structural gap between what the brand says and what the customer says, then output specific message variations grounded in verbatim customer voice.

### Step 1: Brand Language Inventory
Extract from current marketing assets:
- 10 most-used phrases / claims / value props
- 5 most-used "voice tokens" (signature words / phrases the brand reaches for)
- The brand's stated positioning statement
- The brand's stated ICP description

### Step 2: Customer Language Inventory (from data bank)
For each top emotion category, list the most-repeated phrases customers use:
- Pain language (how they describe the problem)
- Outcome language (how they describe the win)
- Comparison language (how they describe what they tried before)
- Identity language (how they describe themselves)

### Step 3: The Gap Audit
Build a side-by-side table:

| Topic | Brand says | Customer says | Gap type |
|---|---|---|---|
| The pain | "[brand phrasing]" | "[customer phrasing]" | Abstract vs. Specific / Internal vs. Outcome / etc. |
| The product | "[brand phrasing]" | "[customer phrasing]" | Feature vs. Benefit / Generic vs. Sensory / etc. |
| The customer identity | "[brand phrasing]" | "[customer phrasing]" | Demographic vs. Psychographic / etc. |

Tag each row with gap severity:
- 🟢 Aligned (brand and customer say same thing in similar way)
- 🟡 Adjacent (overlap exists but customer is more specific / sensory)
- 🔴 Divergent (brand and customer fundamentally disagree on how to describe this)

### Step 4: ICP Reality Check
Compare brand's stated ICP to who's actually buying (per data bank):
- Demographics match? (age, location, income proxies from review patterns)
- Use cases match? (what brand says vs. what customer describes using it for)
- Identity match? (how brand assumes customer self-describes vs. actual self-description)

If divergent → the brand is talking to who they THINK is buying, not who IS buying. Massive MMF gap.

### Step 5: Message Variation Generation
For each 🔴 divergent topic + each top emotion category, output 3-5 message variations that:
- Use customer verbatim language
- Replace abstract claims with specific outcome language
- Match the actual ICP (not the assumed one)
- Trigger the named emotion

Format:

```
TOPIC: [The pain]
BRAND CURRENT: "[current copy]"
GAP DIAGNOSIS: [What's wrong — abstract / wrong ICP / wrong emotion / etc.]

CUSTOMER-GROUNDED VARIATIONS:
1. "[Variation lifting from customer voice]" — emotion: [X]
2. "[Variation 2]" — emotion: [X]
3. "[Variation 3]" — emotion: [X]

DEPLOY IN: [Hook line / headline / email subject / VSSL beat 1]
SOURCE QUOTES: [Reference data bank quotes that informed these]
```

### Step 6: Test Architecture Recommendation
Don't just output variations — design the test:
- Which 5-10 variations to ship in next 14 days
- As what (headline test, hook test, subject line test)
- Against what (current top performer)
- Success criteria (CTR / conversion / blended ROAS lift)

### Step 7: Identify the One Thing
Surface the SINGLE biggest MMF gap. If the brand fixes only one thing in the next 30 days, what's it? Name it explicitly. This is what closing MMF actually looks like — not "improve everything," but "the brand calls itself X but the customer experiences it as Y, fix that one frame."

## Output Schema

```markdown
# [Brand] — Messaging-Market Fit Diagnostic

## Brand Language Inventory
- Most-used phrases: [list]
- Voice tokens: [list]
- Stated positioning: "..."
- Stated ICP: "..."

## Customer Language Inventory (from data bank)
- Pain language top phrases: [list with frequency]
- Outcome language top phrases: [list]
- Comparison language: [list]
- Identity language: [list]

## Gap Audit Table
[Full table with severity flags]

## ICP Reality Check
- Stated ICP: "..."
- Actual ICP (per data bank): "..."
- Convergence: 🟢 / 🟡 / 🔴
- Implications: [what this means for messaging strategy]

## Message Variations (15-25 total)
[All variations grouped by topic, with deployment recommendation per]

## 14-Day Test Architecture
- Variations to ship: 5-10 priority
- As what: [headline / hook / subject line]
- Against what: current top performer
- Success criteria: [specific KPIs]

## The One Thing (CRITICAL)
**The single biggest MMF gap**: [one sentence diagnosis]
**The fix**: [one sentence solution]
**Expected outcome if fixed**: [specific KPI lift hypothesis]

## What NOT to Do
- [Anti-pattern 1: e.g., "Don't change everything at once — test the One Thing first"]
- [Anti-pattern 2: e.g., "Don't lift quotes verbatim into broad-audience copy if the quote uses niche jargon"]
```

## Quality Gate

Score against `genius.md` rubric. Critical for this workflow:
- **Customer Voice Grounding** (9+ required): every variation cites a data bank quote
- **Emotion Specificity** (8+ required): each variation names primary emotion
- **System vs. Tactic** (8+ required): output is the diagnostic + test architecture, not just "better copy"

## Content Type Adaptations

| If primary deployment is... | Variation focus on... |
|---|---|
| **Meta ad hooks** | First 3 seconds, scenario opens, customer-voice quotes as hook |
| **Landing page headlines** | H1 + sub-H1, address ICP identity in first frame |
| **Email subject lines** | Curiosity / loss emotions, customer phrasing not brand voice |
| **VSSL opening beats** | Pain + identification ("you're a [identity] who has [pain]") |
| **Influencer briefs** | Direction not script — give creator the gap diagnosis + emotion target |
| **PDP product description** | Outcome language replacing feature language |

## Pairs With

- `/vince-data-bank-build` — must run first
- `/vince-emotional-angle-engine` — generates concepts FROM the diagnosed gap
- `/vince-intent-first-launch` — applies kill-discipline to the variations before launch
- Lara Acosta `8-word rehook` — for short-form variations
- Luke Iha `vicious hooks` — for combative-tone variations
