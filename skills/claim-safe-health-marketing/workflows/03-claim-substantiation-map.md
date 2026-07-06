---
description: Map every claim in a piece (or claim under consideration) to the evidence tier it actually requires, and confirm whether the brand's evidence clears that bar
---

# /claim-substantiation-map — Evidence-Tier Verification

For every claim (existing or proposed), determine the evidence tier the FTC/NAD standard requires for that claim's strength, then check what evidence the brand actually holds against that bar. This is the workflow that prevents "the copy sounds fine" from masking "we have no evidence for this."

## Pre-Flight Gate

**Use this when**:
- A new claim is being considered and you need to know what evidence would even be required before writing copy around it
- `/claim-audit` flagged a Bucket 3/4 claim as needing an evidence-tier check
- A brand wants to use language like "clinically proven," "studies show," or "doctors recommend" and you need to confirm the evidence supports that specific strength of claim
- Legal/regulatory due diligence before a funded brand's launch (Path A client context)

**Do NOT use this when**:
- The claim is already an obvious disease claim (Bucket 1/2) — no evidence tier rescues a disease claim; route straight to `/compliant-rewrite`
- You just need wording help, not an evidence check — use `/compliant-rewrite`
- You need the FULL pre-launch sign-off, not just the evidence piece — use `/pre-launch-compliance-gate`

## Skill Acquisition

Load before executing:
- `genius.md` — GP-02 (Substantiation Ladder), the NAD product-specificity rule
- `references/source-ledger.md` — for citing which regulatory source underlies each tier requirement

## Execution

### Step 1: Restate the Claim at Its Actual Strength

Write the claim exactly as it will appear in copy — strength matters. "Supports healthy inflammatory response" and "clinically proven to reduce inflammation" require different evidence tiers even though both are technically structure/function-adjacent language.

### Step 2: Assign the Required Evidence Tier

Using genius.md GP-02's 5-tier ladder, determine the MINIMUM tier this specific claim strength requires:
- Absolute/strong outcome language, "clinically proven," "clinically studied" → Tier 5 (RCT, product-specific)
- Moderate structure/function claim → Tier 4 minimum
- Mechanism/"how it works" narrative only → Tier 2 is sufficient IF the copy doesn't cross into an outcome claim
- Any claim relying on testimonials/reviews as its primary support → automatic fail; Tier 0 never qualifies as standing evidence

### Step 3: Product-Specificity Check (NAD Rule)

If evidence exists, confirm it was tested on:
- The SAME formula (not just the same active ingredient at a different dose)
- The SAME delivery mechanism
- A comparable population/context to the marketing claim

If the brand's evidence is ingredient-level only (e.g., "ashwagandha has been studied for X" ≠ "our product, dosed at Y, was studied for X"), flag the gap explicitly and require the copy to make an ingredient-level claim, not a product-level one (see genius.md Hall of Fame Exemplar #3, BrainPack, for the failure mode).

### Step 4: Gap Report

For any claim where required tier > actual evidence tier held:
- State the gap explicitly (required Tier 5, brand has Tier 2 in vitro data only)
- Offer the compliant claim strength that the ACTUAL evidence supports (route to `/compliant-rewrite` for the wording)
- Do not present "get better evidence" as the only option if a truthful, lower-strength claim still exists and sells

### Step 5: Output

```markdown
# Substantiation Map — [asset/brand/claim set]

| Claim (as written) | Required tier | Evidence held | Product-specific? | Gap | Recommended action |
|---|---|---|---|---|---|
| "..." | 5 | 2 (in vitro only) | N/A | Tier 3 gap | Downgrade to mechanism narrative + route to /compliant-rewrite |

## Verdict
[CLEARED — evidence meets bar for every claim / GAPS FOUND — n claims need downgrade or evidence collection / BLOCKED — core claim has no supportable version]
```

## Content Type Adaptations

| Context | Focus |
|---|---|
| **New product launch (Path A client)** | Run this BEFORE any copy is drafted — determines the ceiling of what claims are even available to write toward |
| **Existing brand claim inventory** | Cross-reference against `/claim-audit` output; substantiation map explains WHY a Bucket 3/4 claim is risky, audit explains WHAT'S risky |
| **Influencer/UGC brief** | Confirm the brief doesn't ask creators to make claims above the evidence tier the brand actually holds — brand liability extends to endorser claims (genius.md GP-05) |
| **Ingredient-deck / white-label brand** | Especially high NAD-rule risk — most white-label brands only have ingredient-level (not product-level) evidence; default to mechanism-narrative claims unless product-specific testing exists |

## Output Requirements

1. Every claim mapped to a specific required tier with the genius.md GP-02 reasoning shown, not just a number
2. Product-specificity explicitly checked, not assumed
3. Gap report offers a compliant alternative claim strength, not just a rejection
4. Verdict is unambiguous — CLEARED/GAPS/BLOCKED, no hedging

## Quality Gate

- [ ] No claim was scored against a lower tier than its actual strength requires
- [ ] Ingredient-vs-product evidence distinction was explicitly checked (NAD rule)
- [ ] Testimonial/anecdotal evidence was never counted as satisfying any tier above 0
- [ ] Every gap includes a recommended compliant alternative, not just a flag

If any check fails, redo the mapping — an incorrectly-cleared claim here becomes an FTC enforcement risk downstream, not just a stylistic miss.
