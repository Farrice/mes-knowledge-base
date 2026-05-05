---
description: Run the 4-prompt AI customer research stack to extract pain points, benefits, objections, and sentiment from review/support/FAQ data
---

# 02 — AI-Powered Customer Research Stack

> Per Omar: "Marketing is a guess game and the best marketers are the best at guessing — and the way you get good at guessing is you educate yourself on who you're guessing about."

The 4-prompt research stack. Bridges raw customer data → ad-ready customer language. Run after profit architecture, before any creative briefing.

## Pre-Flight Gate

Run this workflow when:
- ✅ New brand engagement (mandatory after profit architecture passes)
- ✅ Existing brand with stale or missing avatar / customer language
- ✅ Pre-relaunch / repositioning of existing brand
- ✅ CAC inflating with no clear creative diagnosis

Skip / defer when:
- ❌ Profit architecture not yet complete (run `/omar-profit-architecture` first)
- ❌ No customer data + no Amazon/Reddit category proxy data available
- ❌ Last research stack run within 90 days (no significant data shift)

## Skill Acquisition

Load before executing:
- `skills/omar-eddaoudi-scaling-ops/genius.md` (Pattern 2: CDP, Pattern 4: WSI)
- `skills/omar-eddaoudi-scaling-ops/references/4-prompt-research-stack.md` (the actual prompts + data prep)

## Execution

### Step 1: Data Collection + Cleaning

Collect what's available:

**Always required**:
- Customer reviews (own brand if existing; Amazon + Reddit category if pre-launch)
- Target volume: 50-200 cleaned reviews

**Highly recommended (existing brands)**:
- Support tickets (last 90 days, target 50+)
- FAQ data (only if customer-driven, not marketer-imagined)

**Cleaning rules** (apply BEFORE any AI prompts):
- Delete reviews under 10 words
- Delete generic praise/hate without because-clauses
- Strip personally identifying info from support tickets
- Format all data as CSV with columns specified in reference

**Critical**: Do not skip cleaning. Garbage in → garbage out × 4 prompts.

### Step 2: Run Prompt 1 — Pain Point Extraction

Paste cleaned review CSV into Prompt 1 (see reference file). Output: pain points table sorted by frequency, with verbatim language and emotional intensity.

Validation: Pain points should use verbatim customer language, not paraphrased "themes."

### Step 3: Run Prompt 2 — Benefit Hierarchy

Same input, different prompt. Output: benefit table + top 3 benefits + top 2 surprise benefits + mechanism opportunities.

Validation: Identify "I tried X before and it didn't work" patterns — these are mechanism counter-positioning gold.

### Step 4: Run Prompt 3 — Objection Mapping

Input: cleaned reviews + support tickets. Output: objection table + top 5 to pre-handle in creative + top 3 for landing page + product/onboarding red flags.

Validation: Objections must keep customer's exact framing, not softened to "concerns."

### Step 5: Run Prompt 4 — Sentiment Analysis (Three-Bucket)

Input: cleaned reviews. Output: three tables (positive/negative/neutral) with because-clauses, plus verbatim language inventory.

Validation: At least 5 verbatim positive language patterns + 3 negative patterns to address must be extracted.

### Step 6: Synthesize Into Research Deliverable

Compile `customer-research-synthesis.md`:
1. Top 5 Pain Points (Prompt 1)
2. Top 3 Benefits + Top 2 Surprise Benefits (Prompt 2)
3. Top 5 Pre-Handle Objections (Prompt 3)
4. Verbatim Language Inventory (Prompt 4)
5. Mechanism Opportunity Identified (Y/N + description)
6. Identified product/onboarding red flags (if any)

### Step 7: Pass to Avatar Workflow

Hand off to `/omar-avatar-trigger-map` — the synthesis becomes the input for 1-page avatar construction.

## Content Type Adaptations

| Brand Stage | Adaptation |
|-------------|-----------|
| Pre-launch (no own data) | Run Prompts 1-2 on competitor Amazon + Reddit. Skip Prompt 3 (no support tickets). Run Prompt 4 on competitor reviews to learn category language. |
| Existing brand (some data) | Run all 4 on own data + supplement with 1-2 competitor review pulls |
| Mature brand pre-relaunch | Run all 4 on own data + 3-5 competitor review pulls + own support tickets + own FAQ. Cross-reference outputs. |
| B2B / high-ticket | Augment review data with sales call transcripts. Adjust Prompt 3 to include "why we lost the deal" patterns. |
| Subscription product | Add cancellation reason analysis (typically in support tickets) as 5th prompt. |

## Output Requirements

The deliverable must include:
- ✅ Cleaned data CSVs (input artifacts preserved)
- ✅ All 4 prompt outputs as separate sections
- ✅ Synthesis document with 6 required sections
- ✅ Verbatim language inventory (minimum 5 positive + 3 negative phrases)
- ✅ Mechanism opportunity flagged (Y/N + description if Y)
- ✅ Recommended next workflow

## Quality Gate

Score against `genius.md` Quality Rubric Criterion 2 (Customer Language Authenticity). Pass condition: 8+/10.

**Veto**: If outputs use paraphrased "themes" instead of verbatim customer language → fail. Re-run prompts with stricter "verbatim only" instruction.

**Anti-pattern check**:
- Did you bundle prompts into one mega-prompt? (Re-do as 4 separate calls)
- Did AI add benefits/pains not in the data? (Re-prompt with stricter "DO NOT add not-present items" instruction)
- Are objections softened? (Restore verbatim framing)
- Is data uncleaned? (Re-clean and re-run — generic praise/hate produces shallow output)

**Iteration loop**: After ad portfolio runs, return to this workflow quarterly to refresh language inventory with new customer data.
