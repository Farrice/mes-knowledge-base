---
name: "The \"Premium at Scale\" Positioner"
source_prompt: "skills/ross-mckay-premium-at-scale/references/prompts/premium-at-scale-positioner.md"
skill: ross-mckay-premium-at-scale
standard: structure-pure-v2
refactored: 2026-07-11
---

# The "Premium at Scale" Positioner

## Purpose
Transforms a commodity product into a mass-market luxury item.

## Input Required
```
PRODUCT_CATEGORY: [e.g., Protein Bars, Energy Drinks, Toothpaste]
COMPETITOR_PRICE_FLOOR: [The average price point of mass-market competitors]
SCIENTIFIC_ANCHOR: [A data point or efficacy metric that can be over-indexed]
```

## Instructions
Act as an elite CPG Brand Strategist applying Ross McKay's methodology. Your task is to generate a positioning brief that:
1. Matches the `[COMPETITOR_PRICE_FLOOR]` (or stays within 10% of it).
2. Defines a visual architecture that mimics high-end luxury, removing all category confusion (no "noise" on the packaging).
3. Bases the entire product efficacy claim on the `[SCIENTIFIC_ANCHOR]` to justify the "best in class" label.
4. Identifies the niche cultural association (e.g., specific run clubs, elite athletes) that will build the initial cult following before scaling.

Incorporate the mindset that price point does not equal premium. Premium is derived from aesthetics, strict adherence to quality norms, and associations.

## Output Contract
Deliver a positioning brief with four labeled sections:
- Price Alignment: the stated price point and its relationship to `[COMPETITOR_PRICE_FLOOR]` (must land at or within 10% of it)
- Visual Architecture: the packaging/design direction that reads as luxury, with the specific "noise" being removed named explicitly
- Scientific Anchor Claim: one sentence stating the efficacy claim built on `[SCIENTIFIC_ANCHOR]`, plus the "best in class" positioning line it justifies
- Niche Cultural Beachhead: the specific community/subculture targeted first, and why that community confers credibility before mass scale
- No invented data points beyond `[SCIENTIFIC_ANCHOR]` as supplied — do not fabricate additional statistics to strengthen the claim

## Output Skeleton
```
PREMIUM AT SCALE BRIEF: [PRODUCT_CATEGORY]

1. PRICE ALIGNMENT
Price point: [$X, within 10% of COMPETITOR_PRICE_FLOOR]
Rationale: [why this price enables mass distribution while the brand reads premium]

2. VISUAL ARCHITECTURE
Design direction: [one-line description of the luxury visual cue being borrowed]
Noise removed: [specific category convention being stripped from the packaging]

3. SCIENTIFIC ANCHOR CLAIM
Anchor: [SCIENTIFIC_ANCHOR, as supplied]
Claim line: [one sentence turning the anchor into a "best in class" statement]

4. NICHE CULTURAL BEACHHEAD
Target community: [specific niche group, not a broad demographic]
Why this community first: [credibility/halo effect this group confers before mass retail]
```

## Quality Gate
- Stated price point is at or within 10% of `[COMPETITOR_PRICE_FLOOR]` — never priced above the mass-market floor to signal "premium"
- The Scientific Anchor Claim uses only `[SCIENTIFIC_ANCHOR]` as supplied — no additional invented statistics
- The niche cultural beachhead is a specific, named subculture (not "fitness enthusiasts" or another broad segment)
- The Visual Architecture section names a concrete design decision, not a general adjective like "clean" or "modern" with no specifics
- The brief nowhere equates "premium" with "higher price" — the through-line is design, claim, and association

## Deploy When
- Launching a consumer product in a crowded category where mass volume and distinct branding must coexist
- Repositioning an existing commodity-priced product to read as elevated without raising price
- Building the initial go-to-market brief before packaging design begins
