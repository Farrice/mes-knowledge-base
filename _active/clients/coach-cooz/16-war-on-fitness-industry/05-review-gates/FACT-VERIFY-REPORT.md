# Fact Verification Report — "War on Fitness Industry" Funnel

**Verdict: YELLOW — SHIP WITH FIXES**

Two testimonial quotes on the squeeze page are NOT verbatim (Allison reordered + fabricated segment; Sammy heavily compressed). One internal contradiction (8 vs. 9 months). One factual mis-framing of Cody McBroom's slogan. Ed Mylett attribution unverifiable. Fixes are surgical — no full rewrite required, but launch is blocked until testimonial verbatim integrity is restored (the strategy spine itself makes this a hard rule).

## Summary

Total factual claims audited: **28** across 4 files. Verified verbatim: **17**. Verified as self-report (Cooz's account): **4**. Likely-with-edit needing fix: **2**. Fabricated/reordered needing cut or fix: **2** (Allison, Sammy). Mis-framed source needing correction: **1** (McBroom). Unverifiable attribution: **1** (Ed Mylett — already flagged in BRIEF). Internal contradiction: **1** (8 vs. 9 months).

---

## Critical Issues (RED — must fix before ship)

### 1. Allison quote — REORDERED + PARTIALLY FABRICATED
- **In SQUEEZE-PAGE.md**: `"I got a lot stronger than what I went in as. It's not just gains—I'm not only getting a trainer but a life coach."`
- **Actual verbatim (RAW-PROOF-INVENTORY.md)**: `"You're not only getting a trainer but a life coach. I 100% got a lot stronger than what I went in as. It's only gains szn from here."`
- **Failure**: The phrase "It's not just gains—" does not exist in source. The pronoun was changed from "You're" to "I'm." The clauses were reordered.
- **Fix**: Replace with true verbatim: `"You're not only getting a trainer but a life coach. I 100% got a lot stronger than what I went in as."` (accept shortening at the end; do not invent connective phrases).

### 2. Sammy quote — COMPRESSED / PARAPHRASED
- **In SQUEEZE-PAGE.md**: `"His expertise has transformed my life. He creates a fun but serious environment and helps you crush your workouts. If you're looking for a personable trainer, Coach Cooz's services are well worth the investment."`
- **Actual verbatim (RAW-PROOF-INVENTORY.md)**: `"...his expertise on fitness and nutrition have transformed my life. Coach Cooz provides a fun but serious environment throughout training sessions. He creates an exceptional workout routine that tailors to your specific goals and helps you crush your workouts. If you're looking for a personable trainer that will help you achieve your goals Coach Cooz's services are well worth the investment"`
- **Failure**: "His expertise has transformed my life" is a rewrite of "his expertise on fitness and nutrition have transformed my life." "He creates a fun but serious environment" is a stitched-together compression that doesn't exist in source. "If you're looking for a personable trainer, Coach Cooz's services…" cuts the source's "…that will help you achieve your goals" without ellipsis.
- **Fix**: Use verbatim excerpts joined with ellipses: `"His expertise on fitness and nutrition have transformed my life. Coach Cooz provides a fun but serious environment... helps you crush your workouts. If you're looking for a personable trainer that will help you achieve your goals, Coach Cooz's services are well worth the investment."` Ellipses are the only permitted compression.

### 3. Cody McBroom "slogan" — MIS-FRAMED
- **In STRATEGY-SPINE.md line 94**: `"Cody McBroom's anti-fitness slogan ('We help average people achieve above average physiques')"`
- **Verified reality**: TCM's trademarked slogan is **"Choose Hard™"**. The "above-average physiques" line is TCM's **mission description**, not the slogan.
- **Failure**: Calling it "slogan" is wrong (the slogan is "Choose Hard"); the exact phrasing doesn't appear verbatim on TCM's site.
- **Fix**: Reframe as `"TCM's mission — 'help the average person become above average' — is the truth hiding in plain sight."` OR cut the McBroom reference entirely.

### 4. Cooz body-fat timeline — INTERNAL CONTRADICTION
- **SQUEEZE-PAGE.md Section 3**: `"22% body fat, eight months later"`
- **STRATEGY-SPINE.md line 44 + BRIEF.md line 82**: `"nine months later"` / `"8% drop in 9 months"`
- **Failure**: Squeeze page says 8 months; strategy + brief say 9 months.
- **Fix**: Confirm the number with Cooz directly, then reconcile all three docs. Recommended default: "nine months later" (matches two of three sources and BRIEF's own reconciliation note).

---

## Caveats (YELLOW — proceed with awareness)

### 5. Karima quote — LIGHT EDIT (verbatim intent preserved)
- **Verdict**: LIKELY VERBATIM. Emoji strip + "have" → dropped are minor edits.
- **Recommend**: restore to `"I have lost 8 lbs. But most importantly, I feel stronger than I have in many years. Ever grateful."` — one keystroke fix.

### 6. Ed Mylett attribution — UNVERIFIABLE
- **Quote**: `"people don't want the things… they want what they think the things will make them feel"`
- **Result**: Cooz himself flagged uncertainty. Quote does NOT appear in any customer-facing files. No customer-facing risk today, but if ever deployed, use loose attribution or cut entirely.

### 7. "$5,000 / $4,000 with podcast credit" pricing
- **Verdict**: LIKELY (internal source authoritative). No fix needed if Cooz owns these numbers.

### 8. "Only 3 spots this month" (SQUEEZE-PAGE Section 9)
- **Verdict**: UNCONFIRMED as a real capacity constraint. This is a marketing urgency device.
- **Action**: Confirm with Cooz that 3 is the real cap; if not, drop the number to avoid an urgency-manufactured claim.

---

## Verified (GREEN — cleared)

### Testimonials — verbatim confirmed
- **Jess**: verbatim match, RAW line 77. ✓
- **Robin**: verbatim match, RAW line 107. ✓
- **Jessica**: verbatim match, RAW line 99. ✓

### Cooz self-report claims (labeled honestly)
- 14% BF = miserable (self-report, labeled ✓)
- 22% BF = happy (self-report, labeled ✓)
- 8% differential (consistent; matches 22 − 14 = 8 percentage points) ✓
- Copy explicitly says disclaimer — exemplary handling ✓

### External facts
- Cooz = Acusio Bivona, coachcooz.com Squarespace, black/gold/white palette ✓
- 42 verbatim testimonials extant across coachcooz.com + Yelp ✓
- Yelp business = "Fitness Over Hollywood" with 5.0 stars ✓

---

## Final Tally

- **VERIFIED**: 17 claims
- **VERIFIED as self-report**: 4 claims
- **LIKELY (minor edit)**: 2
- **UNCONFIRMED (needs decision)**: 4
- **FABRICATED / REORDERED (must fix)**: 2
- **MIS-FRAMED (must fix)**: 1
- **CONTRADICTIONS**: 1

---

## Recommendation

**SHIP WITH FIXES.** Four surgical edits close every open issue:

1. Restore Allison quote to true verbatim
2. Restore Sammy quote to true verbatim (compressed only with ellipses)
3. Reconcile 8 vs. 9 months across all three files (recommend 9)
4. Fix STRATEGY-SPINE line 94 to call the McBroom line a "mission" not "slogan"

Once done, this funnel is GREEN.
