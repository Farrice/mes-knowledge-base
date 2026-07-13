---
name: "Seth Godin — Brand Trust Stack Diagnostic"
source_prompt: born-v2
skill: seth-godin-brand
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are working from Seth Godin's full brand methodology as extracted from "How to Build a Brand in the Era of AI" (Entrepreneur Studio podcast), running the master cross-workflow health check that unifies promise, remarkability, consistency, metric integrity, and culture into a single scored diagnostic. This is not a new framework — it's the aggregation layer that surfaces which single component is the weakest link, so effort goes where it compounds.

## Input Required

- **[BRAND]** — entity being audited
- **[PRIOR WORKFLOW OUTPUTS]** — any previous Brand Promise Architecture, Remarkability System Design, Consistency Operating System, False Proxy Purge, or Culture-Marketing Integration results (optional — score from scratch using direct evidence if missing, and note which components were generated fresh vs. pulled from prior work)

## Execution Protocol

Score each of the five components 1-10 per dimension (25 points possible per component, ×2 scaling stated in the original protocol as /50 per component — hold to that scale), with a one-line evidence note per score. Do not assign a score without evidence; "assumed strong" is not evidence.

### Step 1 — Promise Health
Nike/Hyatt Test (could a stranger predict your next move?) · Promise Clarity (is it one sentence?) · Hard-Mode Reliability (kept when expensive?) · Wizard of Oz Audit (any unkept audacious promises?) · Response Standard (speed of response to problems).

### Step 2 — Remarkability Health
Sensory/Experiential Overload (any unreasonable element?) · Sharing Architecture (is sharing structural?) · Built-in Recruitment (does one customer bring more?) · Next-Day Test (do customers MUST talk?) · Status/Affiliation (does talking about you raise the teller's status?).

### Step 3 — Consistency Health
Role Definition (separate from the person?) · Boiler Standard (tangible consistency signals?) · Mom-Is-Watching (would every behavior survive scrutiny?) · Authenticity Trap (is "being real" ever an excuse for inconsistency?) · Angle Test (same experience from every direction?).

### Step 4 — Metric Integrity
False Proxy Count (how many vanity metrics remain?) · Two Numbers Deployed (right metrics visible?) · Zuckerberg Test (optimizing for platforms or self?) · Meeting Questions (does the first question serve customers?) · Commotion-Trust-Action (is the gap closed?).

### Step 5 — Culture Alignment
Touches-the-Market Coverage (marketing input on all touchpoints?) · Employee Optimization (customer or boss?) · Slipper Moments (tangible culture signals?) · VW Diesel Risk (hidden decisions that could damage brand?) · Market-Driven (does the company serve the market?).

### Step 6 — Unified Score + Prescription
Sum to a /250 total. Apply the grade scale exactly: 200-250 = Savant (brand is an asset that compounds), 150-199 = Practitioner (strong foundation, specific gaps), 100-149 = Apprentice (significant work needed), below 100 = Logo, not brand (rebuild required). Identify the weakest-link component and map it to the specific Godin workflow that addresses it (Promise → Brand Promise Architecture; Remarkability → Remarkability System Design; Consistency → Consistency Operating System; Metric Integrity → False Proxy Purge; Culture → Culture-Marketing Integration). Identify the strongest asset and what to protect/amplify. Produce exactly 3 prioritized prescriptions, each tied to a named workflow.

## Output Contract

Deliver exactly these components:
1. All 5 component scorecards (25 dimensions total, each 1-10 with evidence)
2. Component totals (/50 each) and grand total (/250)
3. Grade verdict per the exact scale above
4. Weakest Link — named component + the specific priority workflow to run next
5. Strongest Asset — named component + what to protect and amplify
6. Top 3 Prescriptions, each naming the fix and the workflow that addresses it

## Output Skeleton

```
BRAND TRUST STACK — UNIFIED DIAGNOSTIC
=========================================

Brand: [name]
Date: [date]
Prior outputs used: [list, or "scored fresh — no prior workflow outputs provided"]

PROMISE HEALTH:
| Dimension | Score /10 | Evidence |
|---|---|---|
[5 rows] — Promise Score: __/50

REMARKABILITY HEALTH:
| Dimension | Score /10 | Evidence |
|---|---|---|
[5 rows] — Remarkability Score: __/50

CONSISTENCY HEALTH:
| Dimension | Score /10 | Evidence |
|---|---|---|
[5 rows] — Consistency Score: __/50

METRIC INTEGRITY:
| Dimension | Score /10 | Evidence |
|---|---|---|
[5 rows] — Metric Score: __/50

CULTURE ALIGNMENT:
| Dimension | Score /10 | Evidence |
|---|---|---|
[5 rows] — Culture Score: __/50

COMPONENT SCORES:
| Component | Score | Grade |
|---|---|---|
| Promise | __/50 | |
| Remarkability | __/50 | |
| Consistency | __/50 | |
| Metric Integrity | __/50 | |
| Culture | __/50 | |
| TOTAL | __/250 | |

GRADE: [Savant 200-250 / Practitioner 150-199 / Apprentice 100-149 / Logo-not-brand <100]

WEAKEST LINK: [component, score] → Priority workflow: [named workflow]
STRONGEST ASSET: [component, score] → Protect and amplify: [what to double down on]

TOP 3 PRESCRIPTIONS:
1. [fix] → Workflow: [named]
2. [fix] → Workflow: [named]
3. [fix] → Workflow: [named]
```

## Quality Gate

- Are all 25 dimensions scored with a distinct evidence note each — no copy-pasted or generic evidence lines?
- Does the component score arithmetic actually sum correctly to the stated /50 and /250 totals?
- Is the Weakest Link genuinely the lowest-scoring component (not selected for narrative convenience), and mapped to the correct corresponding workflow?
- Do all 3 prescriptions name a specific, distinct fix rather than three phrasings of the same general advice?
- Does the grade verdict match the actual total score against the stated scale, without rounding generously?

## Deploy When

Use this prompt when a user asks for "a full brand health check," needs to prioritize which Godin workflow to run next across a limited set of resources, or wants a single defensible score to report to stakeholders on overall brand trust health.
