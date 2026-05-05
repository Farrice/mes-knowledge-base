# The 4-Prompt Research Stack

> Per Omar's signature move: "I tested this and I found that having one prompt per objective is much better than having a prompt that has all the requirements built in. It just confuses the eye and it doesn't go in depth with the research or the output."

**Critical principle:** Run these as 4 SEPARATE AI calls. Never bundle into one mega-prompt. Each prompt outputs to its own structured table. Combine outputs only after all 4 run independently.

---

## Pre-flight: Data Preparation

Before running any prompt, prepare the following inputs as cleaned CSVs:

### Customer Reviews CSV
- Columns: `product_name | star_rating | review_text | review_date | verified_purchase (Y/N)`
- Cleaning rule 1: Delete reviews under 10 words (no insight signal)
- Cleaning rule 2: Delete generic praise/hate ("best ever" / "I hate it") with no because-clause
- Source priority: Own brand reviews > Amazon competitor reviews > Reddit discussions
- Target volume: 50-200 cleaned reviews

### Support Tickets CSV
- Columns: `ticket_id | customer_question | resolution | category | date`
- Strip personal identifying info before processing
- Target volume: 50+ tickets if existing brand; skip if pre-launch

### FAQ Document
- Format: Question | Answer pairs in plain text
- Must reflect ACTUAL customer questions, not marketing-imagined questions
- If FAQ is generic, flag and skip until support tickets analyzed

---

## Prompt 1: Pain Point Extraction

```
You are a creative strategist analyzing customer reviews for a [PRODUCT CATEGORY] brand.

I'm pasting [N] customer reviews below. Extract every distinct pain point mentioned by customers.

For each pain point, provide:
1. Pain point in customer's own language (verbatim phrase if possible)
2. Frequency (how many reviews mention this pain point)
3. Emotional intensity (1-5 scale based on language used)
4. Stage in customer journey (pre-purchase / first use / long-term use)

Output as a markdown table sorted by frequency (highest first).

DO NOT:
- Paraphrase pain points into marketing language
- Combine distinct pain points into "themes"
- Add pain points not present in the reviews

REVIEWS:
[paste cleaned review CSV here]
```

---

## Prompt 2: Benefit Hierarchy Extraction

```
You are a creative strategist analyzing customer reviews for a [PRODUCT CATEGORY] brand.

I'm pasting [N] customer reviews below. Extract every distinct benefit customers report from using the product.

For each benefit, provide:
1. Benefit in customer's own language (verbatim phrase)
2. Frequency (how many reviews mention this benefit)
3. Whether the benefit was expected before purchase (Y/N based on review context)
4. Whether customers compare it to alternatives they tried (Y/N)

Output as a markdown table sorted by frequency.

Then identify:
- The TOP 3 BENEFITS by frequency (these become primary ad angles)
- The TOP 2 SURPRISE BENEFITS (unexpected wins — these are differentiation gold)
- Any benefits where customers say "I tried X before and it didn't work" (mechanism opportunity)

DO NOT:
- Use marketing benefit language (e.g., "transformative," "life-changing")
- Combine distinct benefits into "categories"
- Add benefits not present in reviews

REVIEWS:
[paste cleaned review CSV here]
```

---

## Prompt 3: Objection Mapping

```
You are a creative strategist analyzing customer reviews and support tickets for a [PRODUCT CATEGORY] brand.

I'm pasting reviews and support tickets below. Extract every objection, hesitation, or concern customers express — including:
- Pre-purchase doubts (skepticism, price concerns, "will this work for me?")
- Post-purchase concerns (usage confusion, expectation mismatches)
- Comparison objections ("but [competitor] does X")
- Trust objections ("I've been burned before by similar products")

For each objection, provide:
1. Objection in customer's own language (verbatim phrase)
2. Frequency
3. Where it surfaces (review / support ticket / both)
4. Whether the brand currently addresses this in marketing (you can guess based on review responses if visible)

Output as a markdown table sorted by frequency.

Then provide:
- TOP 5 objections that should be PRE-HANDLED in ad creative
- TOP 3 objections that should be addressed on landing page
- Any objections that suggest a product or onboarding problem (not a copy problem)

DO NOT:
- Soften objections into "concerns" — keep customer's exact framing
- Combine distinct objections into "themes"

DATA:
[paste cleaned reviews CSV + support tickets CSV]
```

---

## Prompt 4: Sentiment Analysis (Three-Bucket)

```
You are a creative strategist analyzing customer reviews for a [PRODUCT CATEGORY] brand.

I'm pasting [N] customer reviews below. Sort them into three sentiment buckets and extract patterns from each.

BUCKET 1 — Positive Sentiment (4-5 star reviews)
For each, extract:
- The because-clause (WHY did they love it?)
- Specific language they use to describe the experience
- What they compared it to (if anything)

BUCKET 2 — Negative Sentiment (1-2 star reviews)
For each, extract:
- The because-clause (WHY did they hate it?)
- Specific language used in complaint
- Whether the issue is product-related, expectation-related, or service-related

BUCKET 3 — Mixed/Neutral Sentiment (3 star reviews)
For each, extract:
- What they liked
- What they disliked
- Whether they would recommend (if stated)

Output three markdown tables, one per bucket.

Then synthesize:
- "We love how customers describe X" — list 5+ verbatim positive language patterns to use in ads
- "We need to address Y in marketing" — list 3+ verbatim negative patterns we should pre-handle
- "Customers compare us to Z" — list any specific competitor mentions

CRITICAL: Only use verbatim customer language. Do not paraphrase into marketing speak.

REVIEWS:
[paste cleaned review CSV]
```

---

## Output Synthesis (After All 4 Prompts Run)

Compile a single deliverable: `customer-research-synthesis.md` with:

1. **Top 5 Pain Points** (from Prompt 1) — these become problem-aware ad hooks
2. **Top 3 Benefits + Top 2 Surprise Benefits** (from Prompt 2) — these become solution-aware ad hooks
3. **Top 5 Pre-Handle Objections** (from Prompt 3) — these go IN the ad creative
4. **Verbatim Language Inventory** (from Prompt 4) — copy bank for hooks, headlines, body copy
5. **Mechanism Opportunity** (from Prompts 1-2) — if customers say "I tried X, it didn't work" → mechanism counter-position opportunity

---

## Anti-Patterns (Never Do)

- ❌ One mega-prompt asking for "pain points, benefits, objections, and sentiment all at once"
- ❌ Asking AI to "summarize the themes" — themes are marketer abstractions, the goal is verbatim language
- ❌ Running on uncleaned data (generic praise/hate produces garbage)
- ❌ Skipping support tickets when they exist (highest-quality objection signal)
- ❌ Adding LLM-generated benefits/pains not present in reviews

## Tier Adaptation

**Light tier** (pre-launch, no own data): Run Prompts 1-2 on competitor Amazon reviews + Reddit discussions. Skip Prompt 3 (no support tickets). Run Prompt 4 on competitor reviews to learn category language.

**Standard tier** (existing brand): Run all 4 prompts on own data + supplement with 1-2 competitor review pulls.

**Deep tier** (mature brand pre-relaunch): Run all 4 prompts on own data + 3-5 competitor review pulls + own support tickets + own FAQ. Cross-reference outputs.
