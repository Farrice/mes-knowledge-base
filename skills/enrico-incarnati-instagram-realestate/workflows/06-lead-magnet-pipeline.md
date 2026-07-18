---
description: Build ManyChat-powered lead generation funnels — keyword triggers, PDF guides, email collection
---

# /enrico-leads — Lead Magnet Pipeline

Build a complete lead generation system for real estate agents using keyword-triggered DMs, PDF lead magnets, and email list building. Turns Instagram followers into owned contacts.

## Usage

```
/enrico-leads [agent name or niche]
```

Examples:
- `/enrico-leads @_jiing "first-time buyers in [City]"`
- `/enrico-leads "luxury homes agent"`

## Context Loading

// turbo-all

Before executing, read:
1. `skills/enrico-incarnati-instagram-realestate/genius.md` — Pattern 6 (Friday Night), Pattern 7 (ManyChat Engine), Pattern 12 (Save-Magnet)
2. `skills/enrico-incarnati-instagram-realestate/references/profile-optimization-checklist.md` — Link Store section

## Steps

### Step 1: Lead Magnet Design — The Magnet Suite

Design 5 lead magnets for different buyer awareness stages:

```
LEAD MAGNET SUITE
─────────────────
MAGNET 1: "THE CHECKLIST" — Highest conversion, lowest effort
Title: "[N] Things to Check Before Buying a Home in [City]"
Keyword trigger: "checklist"
Format: PDF, 2-3 pages, mobile-optimized
Content: Actionable checklist with 12-15 items
When to deploy: Friday Night Strategy, Digital Clipboard posts
Buyer stage: Solution-Aware → ready to look at homes

MAGNET 2: "THE GUIDE" — Authority builder, email collector
Title: "The [City] Buyer's Guide — Everything You Need to Know in [Year]"
Keyword trigger: "guide"
Format: PDF, 8-10 pages, designed with branding
Content: Market overview, neighborhood breakdown, process steps, financing overview
When to deploy: Market update posts, proximity play content
Buyer stage: Problem-Aware → starting to research

MAGNET 3: "THE CALCULATOR" — Math-based, practical
Title: "Can I Afford to Buy in [City]? The Real Numbers"
Keyword trigger: "calculator"
Format: PDF or interactive Google Sheet
Content: Income required by price point, down payment scenarios, monthly payment breakdown
When to deploy: Visual Math content pieces
Buyer stage: Unaware → surprised by accessibility OR Problem-Aware → needs numbers

MAGNET 4: "THE INSIDER LIST" — Exclusivity, urgency
Title: "Off-Market & Coming Soon Homes in [City] — This Week"
Keyword trigger: "insider"
Format: Email-only delivery (weekly)
Content: Properties not yet on MLS, pocket listings, coming-soon alerts
When to deploy: Stories, exclusivity-play posts
Buyer stage: Most-Aware → actively looking

MAGNET 5: "THE RELOCATION KIT" — Niche-specific
Title: "Moving to [City]? Your Complete Relocation Checklist"
Keyword trigger: "relocate" or "moving"
Format: PDF, 5-6 pages
Content: Schools, neighborhoods, cost of living, lifestyle, what to expect
When to deploy: Proximity play content, city guides
Buyer stage: Problem-Aware → considering the area
```

### Step 2: ManyChat Configuration Blueprint

For each lead magnet, design the full automation flow:

```
MANYCHAT FLOW: [MAGNET NAME]
────────────────────────────

TRIGGER: Comment contains "[keyword]" on any post
↓
STEP 1: Auto-DM (instant)
"Hey [first_name]! 👋 Here's your [magnet name]:
[PDF Link or download page]

Save it to your phone — you'll want it next time you [relevant action].

Quick question: Are you actively looking to [buy/sell] in [City] right now?
A) Yes, ready to go
B) Just exploring
C) Planning for the future"
↓
STEP 2: Response routing
If A → "Amazing! I'd love to help. What's your ideal timeline? I have [availability] this week for a quick chat."
If B → "Perfect — no rush! I'll send you my monthly [City] market update so you stay in the loop. What's your email?"
If C → "Smart to plan ahead. I'll add you to my insider list — you'll get first access to new listings and market changes. What's your email?"
↓
STEP 3: Email capture
"Got it! Drop your email below and I'll send you [weekly/monthly resource]"
↓
STEP 4: Tag + segment
Tag contact based on response: Hot Lead / Warm Lead / Future Lead
Add email to appropriate email sequence
↓
STEP 5: Follow-up (24 hours later, automated)
"Hey [first_name] — hope [the resource] was helpful! By the way, did you know that [one interesting fact about the City market]? I share these every week if you want to stay in the loop. 🏠"
```

### Step 3: Content → Lead Magnet Deployment Map

Map every content format to the right lead magnet:

```
CONTENT → MAGNET MAP
────────────────────
Visual Math → Calculator
Green Screen Reaction → Guide
Digital Clipboard → Checklist
S-Tier Ranking → Guide or Insider List
This vs That → Checklist
Proximity Play → Relocation Kit
Friday Night Strategy → Checklist (primary)
Market Update → Insider List
Listing Showcase → Book a call (direct)
```

### Step 4: CTA Library (Never Say "Link in Bio")

```
CTA ALTERNATIVES — KEYWORD TRIGGERS
────────────────────────────────────
Instead of "link in bio" (kills engagement), use:

"Comment 'checklist' and I'll send this to your DMs"
"Type 'guide' in the comments and I'll DM you the full version"
"Drop 'calculator' below and I'll send you the numbers"
"Reply 'insider' to get access to off-market listings"
"Comment 'tour' if you want to see this home in person"
"Type 'sold' and I'll share how much homes in your area went for"
"Drop '[City]' in the comments for the full neighborhood breakdown"

RULE: Every piece of content should have ONE keyword CTA.
The keyword becomes the engagement metric AND the lead capture.
```

### Step 5: Email Nurture Sequences (Downstream)

```
SEQUENCE 1: HOT LEADS (responded "Ready to go")
Day 0: Personal video message introducing yourself
Day 1: "3 things you should know about buying in [City] right now"
Day 3: Property recommendations based on their criteria
Day 7: "Market update + 'I found something you might love'"
Day 14: Check-in — "Still looking? Here's what changed this week"

SEQUENCE 2: WARM LEADS (responded "Exploring")
Day 0: Monthly market overview
Day 7: Neighborhood spotlight (proximity play)
Day 14: Educational tip + lead magnet reminder
Day 30: "Market shifted — here's what changed" + soft CTA
Day 45: "Quick question — has your timeline moved up?"

SEQUENCE 3: FUTURE LEADS (responded "Planning")
Monthly: Market update newsletter
Quarterly: "Is now a good time to buy?" analysis
Event-triggered: Interest rate changes, new developments, policy changes
```

### Step 6: Deliverable

Produce a conversation artifact containing:
1. Complete Lead Magnet Suite (5 magnets with specs)
2. ManyChat flow blueprints (all 5 funnels)
3. Content → Magnet deployment map
4. CTA Library (10+ keyword alternatives)
5. Email nurture sequences (3 temperature levels)
6. PDF outline for the primary lead magnet (ready to design)
7. ManyChat setup tutorial steps
8. Metrics to track (keyword comment count, DM conversion, email capture rate)

---

## Output Schema

The final deliverable is a single artifact with these required fields:

```
- lead_magnet_suite: exactly 5 (Checklist, Guide, Calculator, Insider List, Relocation Kit), each with
  title, keyword_trigger, format, content_summary, buyer_awareness_stage
- manychat_flows: one full flow per magnet — trigger, auto-DM copy, response routing (A/B/C branches),
  email capture step, tag/segment step, 24h follow-up copy
- content_to_magnet_map: every content format from the expansion pack mapped to its matching magnet
- cta_library: 10+ keyword-trigger alternatives, zero "link in bio" instances
- email_sequences: 3 (Hot/Warm/Future), each with day-by-day touchpoints
- metrics_to_track: keyword volume, DM conversion rate, email capture rate
```

## Quality Gate

Before delivering, verify:
1. **Zero "link in bio" instances anywhere.** Anti-Pattern 6 — every CTA in the suite must be a keyword-comment trigger per source: "Instead what you should use is Many Chat where you tell them to comment a keyword on your post and then you DM them the checklist."
2. **Each ManyChat flow captures email, not just delivers the PDF.** Per source, the point is "building an asset that you finally own" — a flow that DMs the resource and stops (no email ask, no tag/segment) is incomplete.
3. **Response routing is branched, not linear.** The A/B/C ("ready to go" / "just exploring" / "planning for the future") routing must produce genuinely different next messages — identical follow-up text across branches is a fail.
4. **Magnet-to-format mapping is causally sound.** Digital Clipboard → Checklist and Visual Math → Calculator make sense because the content format and magnet share a mechanic; an arbitrary or unexplained pairing is a fail.
5. **Recognition check**: would Enrico Incarnati recognize this as the full ManyChat lead engine he describes — comment keyword → auto-DM → qualifying question → email capture → segmented follow-up — or does it stop at "send them a PDF"?

---

## Stacking Chains

- **Compound with Stockton Walbeck** → Apply the 5-Rule scoring system to each lead magnet
- **Compound with Sabri Suby** → Layer pain extraction psychology into DM sequences
- **Compound with Luke Iha** → Build proof ladder into the email nurture sequences
- **After setup** → Feed data into `/enrico-sprint` for weekly deployment
- **For Equity Union pitch** → "We install this for every agent on your team" — the scalable service
