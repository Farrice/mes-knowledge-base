---
description: "/meg-aov-architect — raise average order value through catalog cohesion and shipping arbitrage, before any upsell app gets installed. 'AOV is where the margin lives.'"
---

# AOV Architect

Most AOV problems are diagnosed as funnel problems. They are not. They are catalog problems wearing funnel clothing. An upsell app cannot create the desire for a second item — it can only route a desire that already exists. If the catalog lacks cohesion, the app finds nothing to route. This workflow fixes the root cause first: designs that belong together because they reflect the same person, not the same color palette.

## Pre-Flight

Read these files before executing:
1. `skills/meg-heckman-buyer-trigger-os/genius.md` (Layer 3 Factory Mechanics, Layer 4 Diagnostic Mechanics, AOV row)
2. `skills/meg-heckman-buyer-trigger-os/references/genius-patterns.md` (Pattern 16 — Symptom Displacement)

> **Pre-Flight Gate**: Before touching the catalog, answer: Does this store have a repeatable design loop? If the 5-step loop (generate → test → scale/cut → email → repeat) is not yet running, catalog cohesion will not hold — you will be building families out of unvalidated orphans. Sequence holds: cohesion audit before cohesion build; loop first before either.

## Input Required

- The full catalog (product titles, design descriptions, live listing URLs if available)
- The store's current AOV (from Shopify analytics or best estimate)
- The store's supplier and shipping rate card — first-item rate, each-additional rate (required for Step 1 math)
- The sub-identity the store was built around (or run `/meg-sub-identity-map` first if unclear)
- Current email/upsell setup, if any (relevant to sequencing gate in Step 4)

---

## Workflow

### Step 1: The Shipping Arbitrage Math

Run this before any catalog work. The math is the reason cohesion compounds.

Her stated figures: "$4.75 for the first item, then $1.99 for the second, and $1.99 for the third — as you add more products, that shipping price starts to go down." (LIKELY — supplier-dependent; recalibrate with the brand's actual rate card before presenting numbers.)

**Worked example using her reported rates:**

| Order size | Shipping paid (supplier) | Revenue at $25/item | Contribution vs. 1-item order |
|---|---|---|---|
| 1 item | $4.75 | $25.00 | baseline |
| 2 items | $6.74 ($4.75 + $1.99) | $50.00 | +$18.26 margin improvement |
| 3 items | $8.73 ($4.75 + $1.99 + $1.99) | $75.00 | +$35.52 margin improvement |

The flat shipping cost passed to the customer does not move. Supplier fulfillment cost rises only $1.99 per additional item. Every item added to a cohesive order is worth more margin than the item count implies — because the incremental fulfillment cost is fixed and low.

**Run this with the brand's actual numbers:**
- First-item fulfillment cost: ___
- Each-additional fulfillment cost: ___
- Current average selling price per item: ___
- Current AOV: ___

Then calculate: at what item count does the order hit the $45+ AOV threshold? At what item count does gross margin per order exceed a single-item order's margin by 50%? That number is the cohesion target — the family size the catalog needs to support.

### Step 2: Catalog Cohesion Audit

Map every live design (or top-20 by sales) against the sub-identity framework. The question is not "what category is this?" — it is "which PERSON does this reflect, and at which moment of their life?"

| Design | Sub-identity it reflects (behavioral moment) | Person-moment it captures | Natural pair (design name or "orphan") |
|---|---|---|---|
| (design 1) | | | |

**Classification rules:**
- Same person, different moments = same family. "I survived a 30-minute hike" and "Officially a hiker (30 minutes counts)" are the same person at two points in the same joke.
- Similar visual aesthetic ≠ same family. Matching color palettes, similar font choices, or shared "nature" subject matter are not cohesion. They are decoration consistency.
- Topic ≠ person. "Hiking designs" is a category. "The casual hiker who is genuinely proud of a 30-minute stroll" is a person. The family is built around the person.

**Flag orphans explicitly.** An orphan is a design with no natural pair in the current catalog — the person it reflects has no other moment represented. Orphans suppress AOV structurally because the buyer has no second item to buy that feels like them. They are not a design quality problem; they are a catalog architecture problem.

### Step 3: Concept-Family Design

For each sub-identity that has at least one design but no family (fewer than 3 items sharing a person), build the family.

The brief for each new concept: ONE person, ONE additional moment. Not a variation on the existing design — a new moment for the same person. The hiker who earned the 30 minutes gets a design for the drive home. Gets a design for telling the story later. Gets a design for going again despite the ache.

**Family naming as identity claim:**
Name collections around the person, not the product type. "The Casual Hiker Collection" tells someone they belong. "Hiking Apparel" tells someone what they are buying. Collections named as identity claims do trigger work before the design loads.

Feed gaps to `/meg-concept-sprint`: list the sub-identity, the existing design(s), and the person-moment(s) missing. The sprint generates the concepts; this workflow defines which gaps to fill first (highest-orphan-count sub-identity goes first).

**Priority order for family completion:**
1. Sub-identities with 1 design and proven sales — one new concept completes a pair, immediate AOV lift
2. Sub-identities with 2 designs — one new concept creates the triple and crosses the $45 threshold at average price
3. Orphans with no sales data yet — deprioritize; validate the person before building the family

### Step 4: Sequencing Gate

Cohesion before upsell funnels. "If you're newer, I would focus first on creating more products or designs that people genuinely want to buy and pair together."

The sequencing law exists because of the math, not preference. An upsell app placed in the cart between two items only converts if the buyer already wants item two. If item two does not exist, or exists but reflects a different person, the app fires into a gap. The prompt reads as pressure, not as a suggestion for them.

**The right sequence:**
1. Run the shipping-arbitrage math → set the target family size
2. Complete the catalog audit → identify orphans and incomplete families
3. Brief and test new concepts to complete at least three families → validate each via paid test
4. Enable upsell or bundle apps once two or more families have 3+ validated items each

A store that has one strong design and installs an upsell app is showing the buyer more things by a stranger. A store with a cohesive family is showing the buyer more moments of themselves. The conversion rate on the second is structurally higher before any app logic runs.

### Step 5: Bundle and Pricing Math

The $45+ AOV target is a default, not a law. Calibrate against the brand's actual margin, supplier costs, and ad spend before treating it as the ceiling.

**What bundle pricing does:**
A "buy 2, save $X" offer converts on identity logic, not discount logic — if both items reflect the same person, the saving is incidental. If they do not reflect the same person, the discount is doing all the work, which means margin is buying AOV. Discount-led bundling is a warning sign.

Test: remove the discount and present the pair as a collection. If conversion drops significantly, the cohesion is not real — the price was covering for a weak family. If conversion holds, the identity fit is doing the work and the discount was leaving margin on the table.

**The $45 math, worked:**
Two items at $25 = $50 AOV, exceeds threshold. Two items at $22 = $44, narrowly below. If the brand's average item price is below $22.50, a two-item family is not sufficient — families need three items or pricing adjustment before the $45 target is structurally reachable.

Run this with the brand's actual ASP and supplier rates. The target is margin per order, not AOV as a vanity metric.

## Content Type Adaptations

| Store type | Adaptation |
|---|---|
| POD store | Full workflow as-is; use supplier rate card from Printify/Printful/etc. for Step 1 math |
| Streetwear drops | Capsule = pre-built cohesion — each drop is already a family; audit whether capsule items share a PERSON or only an aesthetic |
| Digital products | Marginal fulfillment near zero; the math in Step 1 is even stronger (no per-unit cost); bundle logic is pure margin with no downside |
| Client store audit | Run Step 2 first (catalog audit); present the orphan map before any recommendations; let the data make the case |

## Output Format

```
AOV ARCHITECT — [brand/store] — [date]

SHIPPING MATH
  Supplier first-item cost: ___ / each-additional: ___
  Current AOV: ___ / $45 target reached at: ___ items
  Margin per order (1 item): ___ / (2 items): ___ / (3 items): ___

CATALOG MAP
  Sub-identities found: ___
  Complete families (3+ items, same person): ___
  Incomplete families (1–2 items): ___
  Orphans (no natural pair): ___

ORPHAN LIST
  [Design name] — person: ___ — missing moment: ___
  [Design name] — person: ___ — missing moment: ___

FAMILY BUILD PRIORITIES
  1. [Sub-identity] — existing: ___ — brief for /meg-concept-sprint: ___
  2. [Sub-identity] — existing: ___ — brief for /meg-concept-sprint: ___

SEQUENCING VERDICT
  Cohesion status: [ready for upsell apps | not yet — complete families first]
  Recommended next step: ___

BUNDLE PRICING TEST
  Discount-led or identity-led? [test result]
  $45 target reachable at current ASP? [yes / needs 3-item family / needs pricing adjustment]

NEXT: [/meg-concept-sprint with orphan briefs | /meg-trigger-audit on new concepts before production | /meg-funnel-doctor if AOV is above $45 but ROAS is still weak]
```

## Quality Gate

- Math shown with the brand's actual supplier figures, labeled LIKELY if supplier-dependent or estimated
- Every family built around a PERSON (behavioral moment), not a product type or visual aesthetic
- Sequencing honored — no upsell app recommendations appear before cohesion exists
- Discount-led bundling flagged if detected
- Orphan designs named explicitly, not softened into "areas for growth"

## Common Pitfalls

- **Upsell-app-first instinct.** The app is visible; the cohesion gap is not. Recovery: run Step 2 before touching any app settings — show the orphan map, then make the sequencing case.
- **Families built on visual similarity instead of identity.** Matching colors, shared subject matter, or font consistency are not a family. Recovery: for each proposed pair, answer "Is this the same PERSON?" If the answer is "they're both outdoor designs," the pair is decorative.
- **Discount-led bundling.** Buying AOV with margin instead of building it with cohesion. Recovery: test the pair without the discount; if conversion collapses, the family is not real.
- **Orphans left unpaired when one new concept would complete a family.** One additional design at the right moment converts the orphan into the highest-performing pair in the store — because validated demand already exists. Recovery: identify the highest-sales orphan first; it is the highest-ROI brief you can write today.
- **Treating $45 as universal law.** It is her calibration default for POD/Meta 2026. At lower ASPs, higher margins, or digital products, the arithmetic changes. Recovery: always run the brand's actual numbers in Step 1 before citing any threshold.
