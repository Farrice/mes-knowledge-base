# Buyer Signal Cockpit Spec

## Purpose

The Buyer Signal Cockpit is the private demo surface for the Ready Buyer Engine. It shows how Jen/Jiing can turn scattered real estate attention into scored, routed, human-ready next actions.

This is not a live CRM, advertising system, or automated decision system. It is a sandbox spec for a reviewable pilot.

## Demo Inputs

Use fake-safe examples until Jen approves real data.

| Demo Input | Example | What The Cockpit Produces |
|---|---|---|
| Listing | $875K Canoga Park townhome near Warner Center | Buyer fit brief, content angles, open-house DM, seller proof note. |
| Zillow-style lead | "Want to tour this weekend, budget maybe $850K, no preapproval yet" | Readiness score, next question, lender route, no-tour-before-strategy flag. |
| Instagram comment | `READY` on a buyer math Reel | DM reply, intake questions, email capture, score route. |
| Seller inquiry | "Thinking of selling in Reseda but not sure when" | seller readiness brief, equity/timeline questions, consult prep. |

## Lead Card Fields

| Field | Meaning |
|---|---|
| Lead name | First name or anonymized label. |
| Source | Zillow, Instagram, open house, referral, past client, website, partner. |
| Stated need | Buy, sell, buy-sell, explore, referral, unknown. |
| Target area | Neighborhoods or geographic constraints stated by the lead. |
| Price range | Stated range only; do not infer. |
| Timeline | 0-30, 31-90, 91-180, 180+, unknown. |
| Financial readiness | Preapproval, lender intro needed, cash/equity stated, unknown. |
| Decision group | Who needs to be part of the decision, stated by the lead. |
| Main concern | Payment, area, timing, selling first, assistance, offer strength, unknown. |
| Score | 0-100 based on stated intent and behavior. |
| Route | Book, team follow-up, lender/title route, nurture, education only. |
| Next best action | The next message, task, or appointment rule. |
| Compliance notes | What must be checked before publishing or advising. |

## Score Model

Use the score as a triage aid, not as a promise or exclusion rule.

| Factor | Points | What Counts |
|---|---:|---|
| Timeline | 20 | 0-90 days earns strongest score; vague someday earns low score. |
| Motivation | 20 | Job change, family logistics, move-up, relocation, equity event, probate, divorce, inherited property, or clear personal reason. |
| Financial readiness | 15 | Preapproval, lender conversation, cash/equity, realistic budget, or willingness to do payment review. |
| Price/geography fit | 15 | $800K-$900K target zone, strategic listing fit, or clear seller-side opportunity. |
| Decision authority | 10 | spouse, co-owner, heirs, or stakeholders aligned or identified. |
| Engagement quality | 10 | referral, partner intro, repeated replies, thoughtful DM, high-intent comment. |
| Responsiveness | 10 | replies quickly, books quickly, provides needed info. |

## Route Rules

| Score | Route | Action |
|---:|---|---|
| 75-100 | Book within 72 hours | Jen/team consult, value-confirmed calendar invite, preparation brief. |
| 55-74 | Nurture plus partner route | lender/title/market education, one clarifying question, follow-up task. |
| 0-54 | Education only | send resource, add to nurture, no private showing or time-heavy consult. |

## Human Routing

| Route Label | Meaning |
|---|---|
| Jen needed | High-trust consult, seller conversation, complex buyer strategy, offer/listing moment. |
| Team can handle | intake, scheduling, lender intro, document collection, routine follow-up. |
| Nurture quietly | education, monthly check-in, content path, no urgent human attention. |
| Partner review | lender, title, attorney, broker, or transaction coordinator input required. |

## Sample Lead Cards

### Lead A: Ready Buyer

| Field | Value |
|---|---|
| Source | Referral from past client |
| Stated need | First purchase in SFV |
| Target area | Lake Balboa, Reseda, Canoga Park |
| Price range | $800K-$875K |
| Timeline | 60-90 days |
| Financial readiness | Spoke with lender, wants second look at payment |
| Decision group | buyer and partner |
| Main concern | payment comfort and neighborhood tradeoff |
| Score | 82 |
| Route | Book within 72 hours |
| Next best action | Invite to Buyer Strategy Session with payment scenarios and Valley Match Map. |

### Lead B: Tour-First Browser

| Field | Value |
|---|---|
| Source | Zillow-style inquiry |
| Stated need | "Can I see this house Saturday?" |
| Target area | Woodland Hills or Canoga Park |
| Price range | "maybe $850K" |
| Timeline | unknown |
| Financial readiness | not preapproved |
| Decision group | unknown |
| Main concern | wants to see homes before math |
| Score | 46 |
| Route | Education only, then lender route if responsive |
| Next best action | "Happy to help. Before we spend your weekend touring, let's see what this price range looks like monthly. Have you spoken with a lender yet?" |

### Lead C: Seller With Timing Question

| Field | Value |
|---|---|
| Source | Instagram DM from seller content |
| Stated need | might sell in Reseda |
| Target area | Reseda |
| Price range | seller-side opportunity |
| Timeline | 3-6 months |
| Financial readiness | likely equity, not verified |
| Decision group | owner and spouse |
| Main concern | selling before buying |
| Score | 76 |
| Route | Jen needed |
| Next best action | Seller Trust File plus consult prep: address, mortgage estimate, timeline, move plan, decision-makers. |

## AI Boundaries

The cockpit may:

- summarize what a lead stated
- score readiness based on stated answers and behavior
- draft Jen-voice replies
- suggest next-best action
- flag missing info
- route to lender/title/broker review

The cockpit must not:

- infer protected traits
- target based on protected classes
- provide legal, tax, or lending advice
- promise assistance approval
- claim guaranteed income or closings
- publish externally without approval
- make final representation or compensation language

## Demo Screen Layout

```text
Ready Buyer Engine

[Today Queue]
- 3 leads need scoring
- 2 leads need lender intro
- 1 seller consult needs prep
- 4 nurture replies can wait

[Lead Card]
Name / Source / Need / Score / Route / Next Action

[Content From This Listing]
6 hooks / 3 stories / 1 DM keyword / 1 seller proof angle

[Proof Dashboard]
Qualified leads / booked consults / signed clients / protected time / proof assets
```

## Acceptance Criteria

- Jen can understand every route without technical explanation.
- Every card shows why the next action is recommended.
- No lead gets a private showing route without readiness or strategy step.
- Every public-facing line keeps Jen's warm-friend voice.
- Every finance, DPA, buyer-agreement, and legal-adjacent line is marked for review.
