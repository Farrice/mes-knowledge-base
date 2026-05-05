---
description: Build differentiation matrix mapping customer-cares × competitor-says-not to identify positioning territory and produce 5+ recommended hero angles
---

# 06 — White Space Positioning Map

> Per Omar: "We want a what's-missing section which gives us the angles, the emotions, or proofs that competitors are not using. And these gaps become our differentiating opportunities."

White space is the gap between what customers want to be told and what the marketplace tells them. This workflow surfaces that gap and converts it into hero positioning.

## Pre-Flight Gate

Run this workflow when:
- ✅ Choosing positioning angle for new brand or relaunch
- ✅ Crafting hero hook for a campaign
- ✅ In a sophisticated/saturated category where every claim sounds like every other claim
- ✅ Existing positioning feels generic or interchangeable with competitors

Skip when:
- ❌ Customer research not yet complete (run `/omar-research-stack` first)
- ❌ Fewer than 4 competitors exist in category (use direct positioning, no white space needed)

## Skill Acquisition

Load before executing:
- `skills/omar-eddaoudi-scaling-ops/genius.md` (Patterns 3-4: 5-Competitor Sweet Spot, White Space Identification)
- `skills/omar-eddaoudi-scaling-ops/references/4-prompt-research-stack.md` (customer-cares input)

## Execution

### Step 1: Lock the Competitor Set at 5

Finalize EXACTLY 5 competitors. Not 2 (insufficient signal), not 3 (low statistical significance), not 10+ (bloat).

Selection criteria:
- Direct competitors (same product category, same price band)
- Add 1-2 adjacent competitors (different category but competing for same customer attention)
- Use SEMrush organic competitors + client knowledge
- Validate: would the customer realistically compare us to all 5?

### Step 2: Pull Competitor Ad Library

For each of the 5 competitors:
- Pull 10-20 ads from Meta Ads Library (or internal scraping tool)
- Extract per ad: hook, body copy, CTA, format, headline, psychological trigger deployed, creative type
- Capture homepage value prop (screenshot)
- Pull 20-30 customer reviews per competitor

### Step 3: Build the "What Competitors Say" Inventory

From competitor ads + websites, compile:
- All hooks used (verbatim)
- All claimed benefits (verbatim)
- All proof types deployed (testimonials, certifications, research mentions, founder stories, etc.)
- All emotional registers (aspirational / clinical / friendly / authoritative / etc.)
- All positioning territories occupied

### Step 4: Build the "What Customers Care About" Inventory

From customer research stack output (`/omar-research-stack`):
- Top pain points (verbatim language)
- Top benefits (verbatim language, including surprise benefits)
- Top objections (verbatim language)
- Specific phrases customers use that aren't in marketer vocabulary

### Step 5: Cross-Reference for White Space

Build the matrix:

| Customer Cares About | Competitor 1 Says | Competitor 2 Says | Competitor 3 Says | Competitor 4 Says | Competitor 5 Says | White Space? |
|---------------------|-------------------|-------------------|-------------------|-------------------|-------------------|---------------|
| [Pain point in customer language] | [yes/no/partial] | ... | ... | ... | ... | [Y if all "no" or "partial"] |
| [Benefit in customer language] | ... | ... | ... | ... | ... | ... |
| [Surprise benefit] | ... | ... | ... | ... | ... | ... |
| [Objection unaddressed] | ... | ... | ... | ... | ... | ... |

White space conditions:
- All 5 competitors say "no" → blank territory
- 4/5 say "no" + 1 says "partial" → near-white space (you can claim it dominantly)
- All 5 use same framing for this → rephrasing opportunity

### Step 6: Tier White Space Opportunities

For each identified white space, score:
- **Customer evidence strength** (1-10): How strongly do customers care? (frequency × intensity in research data)
- **Competitor absence** (1-10): How completely is this absent in competitor messaging?
- **Brand fit** (1-10): How authentically can your brand claim this?
- **Total score**: Sum / 30

Tier into:
- **Tier 1 (24+)**: Hero positioning candidates (use as primary brand message)
- **Tier 2 (18-23)**: Campaign-level angles (use as primary hook for specific campaigns)
- **Tier 3 (12-17)**: Tactical hooks (use as variation in ad portfolio)
- **Tier 4 (<12)**: Skip — not strong enough

### Step 7: Produce Hero Angle Recommendations

From Tier 1-2 white space, produce 5+ recommended hero angles:

For each:
- The angle in 6-12 words
- Customer evidence (verbatim quotes from research)
- Why competitors don't say this
- Why your brand can credibly claim it
- Suggested deployment (hero copy / brand tagline / category-defining campaign)

### Step 8: Build the Positioning Map

Produce a visual or table-based map showing:
- Where each of your 5 competitors sits (their dominant claim/territory)
- Where the white space sits (the unclaimed territory)
- Where YOUR brand could plant the flag (the recommended Tier 1 white space)

### Step 9: Deliverable

Produce `white-space-positioning-map.md`:
1. 5-competitor lock-in rationale
2. Competitor messaging inventory
3. Customer language inventory (cross-referenced from research stack)
4. White space matrix (full cross-reference table)
5. Tiered white space opportunities (with scores)
6. 5+ hero angle recommendations
7. Positioning map (where competitors are, where white space is)
8. Recommended deployment strategy

## Content Type Adaptations

| Brand Stage | Adaptation |
|-------------|-----------|
| Pre-launch new brand | Heavy focus on Tier 1 — choose ONE white space as brand's defining position |
| Relaunch / repositioning | Look for white space drift — what did your brand once own that competitors have copied? |
| Campaign-level decision | Tier 2-3 sufficient — pick angles for current campaign without disturbing brand position |
| Saturated category | Look for "rephrasing opportunity" — same idea, different language ownership |
| Premium positioning move | Cross-reference with luxury / premium framing absence |

## Output Requirements

The deliverable must include:
- ✅ Exactly 5 competitors with rationale
- ✅ Complete competitor messaging inventory
- ✅ Cross-reference matrix with white space identified
- ✅ Tier-scored white space opportunities (minimum 8-12 identified)
- ✅ 5+ hero angle recommendations
- ✅ Positioning map / table
- ✅ Recommended hero positioning with deployment plan

## Quality Gate

Score against `genius.md` Quality Rubric Criterion 2 (Customer Language Authenticity). Pass condition: 8+/10.

**Veto**:
- Hero angles use marketer language instead of customer language → rebuild with verbatim
- Competitor count != 5 → re-cap (not 3, not 10)
- White space matrix has "themes" instead of specific claims → re-do at claim-level granularity

**Anti-pattern check**:
- White space identified but not customer-evidenced → drop unless customer research supports
- Hero angles that "could work for any brand" → not white space, just generic claims
- Skipping positioning map → no synthesis, just data
- White space tier 4 angles getting recommended → only Tier 1-2 qualify for hero deployment
