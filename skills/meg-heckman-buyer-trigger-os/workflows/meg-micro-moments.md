---
description: "/meg-micro-moments — audit any brand against Heckman's 7 trust micro-moments and install the missing ones as shipped artifacts (welcome email, customer-life email, co-creation ask, spotted feature, comment-voice card, drop calendar). 'Building a brand has nothing to do with being known. It is all about trust. And trust is earned in these micro moments.'"
---

# The Micro-Moments Install (Trust Layer)

Sloth Hiking Club launched January 2025 with zero followers, no list, nobody knowing who they were. Claimed 18 months later: $1.7M in sales, 84,000 customers (UNCONFIRMED, self-reported). Her explanation is not reach — it is seven free touchpoints, run in customer-lifecycle order, each earning the right to the next. "84,000 people didn't buy from Sloth Hiking Club because we were famous. They bought because in a hundred tiny moments, we were worth trusting."

This workflow audits a brand against all seven, then SHIPS the missing artifacts — not advice about them. Every artifact leaves in the brand's named-human voice, ready to send.

## Pre-Flight

1. `skills/meg-heckman-buyer-trigger-os/genius.md` (Trust Mechanics — Layer 5, Design Mechanics § Tattoo Test, Exemplars 5–7)
2. Brand voice source: the client's own words — founder emails, existing replies, how they actually talk. If none exists, capture 3 voice decisions before writing (spunky/dry/zen; emoji or not; who signs).

> **Pre-Flight Gate**: Moments install onto a product that passes the mirror/poster gate. If the catalog is posters, trust artifacts amplify silence — run `/meg-trigger-audit` first. (Moment #1 IS that gate; a failing #1 stops the install.)

## Input Required

- Brand: name, niche, sub-identity (behavioral-moment person)
- Named human who signs (founder/co-founder name — "Eric, Founder" pattern; anonymous brands fail this layer)
- Current state per moment: designs live? ads running? list size? email cadence? UGC on hand? last drop date?
- One product or drop currently in motion (artifacts anchor to something real)

---

## Workflow

### Step 1: AUDIT — Score the Seven Moments

Walk the trust ladder in lifecycle order. Each moment: PRESENT / WEAK / ABSENT + one-line evidence.

| # | Moment | The test | Lifecycle position |
|---|--------|----------|--------------------|
| 1 | Tattoo Test | Can the current lead design finish "My customer is the person who ___"? Would they tattoo it? | Before product exists |
| 2 | Reply in Brand Voice | Every ad/organic comment from the last week answered AS the brand, banter not support-desk? | Stranger meets you |
| 3 | Give Before You Ask | Welcome email = deliver promise + human hi + one reply-question — or an invoice with a logo? | 10 seconds after opt-in |
| 4 | Their Life, Not Your Shelf | Last 4 emails: how many were about the customer's moment vs. the catalog? | Relationship |
| 5 | Customers Write Products | Standing ask-question in emails? Reply→product→free-tee loop ever fired? | Ownership |
| 6 | Feature Customers | Customer photos celebrated by name anywhere? Review flow that rewards photos/video? | Belonging |
| 7 | Never Skip a Week | Fixed drop day? Longest gap since launch? Shipped on a no-applause week? | Forever |

Scoring is behavioral evidence, not intention ("we plan to" = ABSENT). Verdict line: **X/7 present. The one that quietly kills the rest right now: ___** (a broken #7 is usually it — "a brand is like a heartbeat; nobody notices it until it stops").

### Step 2: INSTALL ORDER — Pick the Three That Move First

Never hand back seven simultaneous builds ("you don't even need all seven this week. Just pick one"). Select by lifecycle leverage:

- No list yet → #2 (comments are the only trust surface strangers see) + #3 (the 84%-open email must not be an invoice) + #7 (rhythm from day one is free).
- List exists, flat engagement → #4 (their-life email this week) + #5 (end it with one question) + #6 (first spotted feature).
- Everything half-present → fix the WEAK ones before adding ABSENT ones; a weak welcome email outranks a missing UGC program.

State the order and the one-line reason each.

### Step 3: SHIP THE ARTIFACTS

Execution prompt: `references/prompts-v2/micro-moments-install.md` — honor its Output Contract and Skeleton. For deeper single-surface production, route to the Layer-5 engines: emails → `/meg-trust-email-engine` (prompts: `trust-welcome-email`, `customer-life-email`, `cocreation-ask-email`) · comments → `/meg-community-voice` (`brand-voice-replies`) · features + rhythm → `/meg-fan-flywheel` (`spotted-feature-pack`).

Produce every artifact for the three selected moments, in the brand's voice, signed by the named human. Calibration anchors are genius.md Exemplars 5–7 — match their register (conversational, fragmentary, zero catalog-speak), not their content.

**#2 → Comment-Voice Card + 5 live replies.** Voice card: 3 adjectives, energy-matching rule (banter answers banter), never-do list (no "Thanks for reaching out!", no deflect-to-DM unless money/private). Then draft replies to the brand's 5 most recent real comments.

**#3 → The 3-line welcome email.** Line 1 delivers the promise instantly, no games. Line 2 says hi like the named human actually talks. Line 3 asks ONE niche question they'll want to answer. Nothing else — no button the size of a house. Subject reads like a person, not a campaign.

**#4 → One customer-life email.** A specific lived moment of the sub-identity (their "drive home after a hike"), second person, sensory beats, the lies they tell themselves — affection, never mockery ("the joke is WITH the niche"). Product appears only in the last line, or not at all. Plus a bank of 5 further moment titles ranked by recognition strength.

**#5 → The "need your help" email.** Backstory beat (why you're asking) → the open question about a product that doesn't exist yet → 3 example lanes → "doesn't need to be a finished idea" → free-product promise if it ships → "hit reply" → signature. Plus the build rule for the operator: when a reply makes you laugh out loud, build it, send them one free.

**#6 → The "spotted" feature email + ask-DM.** Feature one real customer properly celebrated ("You wore them, we noticed. Tag us and you'll be featured next"), plus the 5-customer photo-request DM and a review-flow tweak that rewards photo/video.

**#7 → The drop calendar.** Named day, what ships weekly (design/email/feature — size explicitly declared irrelevant), the no-applause clause in writing: "the drop happens anyways."

### Step 4: RHYTHM WIRE — Make It Unskippable

One-line weekly operating row the brand adds to its existing cadence (Factory Loop Step 4/5 if installed): which moment fires on which day, who owns it, and the 10-minute fallback version of each artifact for overloaded weeks — because "the size of the drop matters way less than the fact that it never misses."

---

## Output Schema

```
MICRO-MOMENTS INSTALL — [brand] — [date]

AUDIT (X/7 present)
  1 Tattoo Test        [PRESENT/WEAK/ABSENT] — [evidence]
  2 Brand-Voice Replies [.] — [evidence]
  3 Give Before Ask     [.] — [evidence]
  4 Their Life          [.] — [evidence]
  5 Co-Creation         [.] — [evidence]
  6 Feature Customers   [.] — [evidence]
  7 Never Skip a Week   [.] — [evidence]
  Quiet killer: [#] — [one line]

INSTALL ORDER: [#, #, #] — [one-line reason each]

ARTIFACTS (ready to ship, in [named human]'s voice)
  [Full text of each artifact for the three selected moments]

RHYTHM WIRE
  [Day] — [moment] — [owner] — 10-min fallback: [what]

CLAIMS NOTE: all SHC figures self-reported/UNCONFIRMED; stat citations (84% open,
81% Edelman, 92% Nielsen) are her citations — LIKELY, not independently verified.
```

## Example Output

**Context**: MyBPM (EDM streetwear, mybpm.store), sub-identity "the one still texting the group chat about last night's set at 9am Monday," signer: Farrice. List exists (small), no fixed drop day, welcome email is a 10% code + product grid.

**AUDIT (2/7 present)** — #1 PRESENT (designs pass tattoo test — "raver who never made it to the afters" line), #3 WEAK (code delivered but reads invoice: logo, grid, SHOP NOW), #7 ABSENT (last drop 3 weeks ago, no named day). Quiet killer: #7 — store reads dormant to anyone who scrolls back.

**INSTALL ORDER**: #3, #4, #7.

**#3 Welcome email (excerpt):**

> **Subject: your 10% is inside (+ one question)**
>
> Code MYBPM10 — works right now, no minimum, no games.
>
> I'm Farrice. I started this because festival merch either screams or says nothing, and the people I dance next to deserve better than both.
>
> Quick one while you're here: what was the last set that made you text someone MID-SONG? Hit reply. I read everything.

**#4 Customer-life email title bank (top 2)**: "Can we talk about the Monday after the festival?" · "The group chat at 3am vs the group chat at 9am."

**What makes this excellent**: the welcome email is three moves and nothing else — promise delivered in line one with "no games" stated, the hi sounds like a person with a reason to exist, and the single question targets the sub-identity's exact behavioral moment (texting mid-song), which makes replying feel like joining, not filling out a survey. No button block, no grid. The quiet-killer call names rhythm, not content, as the real gap — matching her diagnosis order.

## Quality Gate

- Audit uses behavioral evidence; no moment scored PRESENT on intention
- Exactly three moments installed; the other four parked with one-line triggers
- Every artifact signed by a named human and written in captured voice, not template voice
- Customer-life email: product absent until last line; affection not mockery; a specific moment, not a theme
- Co-creation email contains all six beats (backstory → question → lanes → low bar → reward → hit reply)
- Drop calendar has a named day and the no-applause clause
- All revenue/stat claims labeled (UNCONFIRMED / LIKELY per genius.md ledger)
- The Tattoo Test verdict is honest — a poster catalog stops the install and routes to `/meg-trigger-audit`

## Common Pitfalls

- **Installing all seven at once.** Seven half-moments read as a brand doing marketing; three shipped moments read as a brand being real. Pick three.
- **Persona-doc voice.** If the welcome email could be sent by any brand in the niche, the named-human layer failed. Steal phrasing from how the founder actually texts.
- **Co-creation as survey.** "What products would you like to see?" is market research and gets silence. The ask works because it's playful, low-bar, and rewarded — a bit, not a form.
- **Featuring the product in the feature.** The "spotted" email celebrates the CUSTOMER (name, trail, moment); the tee is set dressing. Invert it and it becomes a catalog with faces.
- **Treating rhythm as content strategy.** #7 is not "post more" — it is one unbroken promise on one named day. Costco's hot dog, not a content calendar.
