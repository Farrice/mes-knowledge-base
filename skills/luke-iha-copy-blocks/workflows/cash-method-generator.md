---
description: Generate 20+ ad concepts from one product using the systematic Concept × Angle × Style × Hook matrix
---

# CASH Method Generator

Systematic ad ideation engine. Produces a multiplication matrix with 50-180+ unique ad variation paths from a single product. Never run out of ideas.

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.


## PHASE 0: LOAD MARKET CACHE (warm_core — $0, no re-research)
If this market is already grounded, read its cached intelligence instead of guessing:
```bash
// turbo
cat .tmp/copy-engine/<slug>/warm-core.json 2>/dev/null || echo "NO CACHE — run /copy-engine for this market first (grounds it once, then this is free), or supply the market psychology manually."
```
Load the relevant fields (`dominant_emotion`, `core_wound`, `pain_to_promise_gap`, `market_beliefs`{4 cells}, `top_voc_soundbites`) — sourced from real research, not guessed. No cache + not supplied → ground first.

## PHASE 1: SKILL ACQUISITION (Do this FIRST)

Read these files in order before proceeding:
1. /Users/farricecain/Google Antigravity/skills/luke-iha-copy-blocks/SKILL.md
2. /Users/farricecain/Google Antigravity/skills/luke-iha-copy-blocks/references/genius-patterns.md (focus on GP2: CASH Multiplication Engine and GP6: The Concept Layer)

## PHASE 2: INPUT REQUIREMENTS

Collect from user:
- **Product/Offer**: What's being sold? Features, benefits, price point, mechanism
- **Target Audience**: Who buys this? Demographics, psychographics, awareness level
- **Competitive Context**: What else is in the market? What claims are saturated?
- **Previous Winners** (optional): Any past ads that performed well? What worked?

## PHASE 3: CONCEPT GENERATION (C)

Generate 3-5 **Concepts** — emotional territories the ad operates within.

Rules:
- A concept is NOT a product description
- A concept is expressible in one sentence WITHOUT mentioning the product
- A concept frames the CONVERSATION the audience enters

For each concept, articulate:
- The emotional territory in one sentence
- Why this territory resonates with the target audience
- How it differs from competitor messaging

Example output (for a supplement):
1. "The food industry has silently destroyed your gut"
2. "Your body is fighting itself and you don't know why"
3. "The ancient wisdom your doctor never learned"

## PHASE 4: ANGLE GENERATION (A)

For each Concept, generate 4-6 **Angles** — specific perspectives that bring the concept to life.

Rules:
- Each angle should feel like a DIFFERENT conversation within the same territory
- Angles should vary in emotional register (fear, aspiration, curiosity, anger, empathy)
- At least one angle per concept should be contrarian

Example (for Concept 1):
- 1A: The specific ingredient hiding in "healthy" foods
- 1B: What a food scientist's own kitchen looks like (insider confession)
- 1C: The correlation between processed food consumption and [specific health issue]
- 1D: Why your grandparents never had this problem
- 1E: The $14B industry built on keeping you sick

## PHASE 5: STYLE ASSIGNMENT (S)

Define 3-4 **Styles** — creative execution formats:
- **UGC**: Casual, phone-shot, testimonial-style
- **Editorial**: Polished, article-style, data-heavy
- **Talking Head**: Expert to camera, authority-driven
- **Demonstration**: Show the product/result visually
- **Meme/Humor**: Pattern interrupt through entertainment

Note: Each style changes the RHYTHM of copy blocks, not the content.

## PHASE 6: HOOK GENERATION (H)

For the top 10 C×A×S combinations, write 2-3 **Hooks** each.

Hook types to deploy:
- **Solve hooks**: "Here's why [problem] — and the fix"
- **Show hooks**: "I [achieved result] using [unexpected method]"
- **Proof-of-work hooks**: Demonstrate expertise through the hook itself
- **Contrarian hooks**: Contradict common belief
- **Story hooks**: Open with narrative

## PHASE 7: OUTPUT FORMAT (CASH Matrix)

Deliver the complete CASH matrix:

```
## CASH Matrix: [Product Name]

### Concepts (3-5)
C1: [Concept statement]
C2: [Concept statement]
...

### Angles (4-6 per concept)
C1-A1: [Angle]  C1-A2: [Angle]  C1-A3: [Angle]...
C2-A1: [Angle]  C2-A2: [Angle]  C2-A3: [Angle]...

### Styles
S1: [Style]  S2: [Style]  S3: [Style]  S4: [Style]

### Top 20 Hook Variations
| # | Concept | Angle | Style | Hook | Type |
|---|---------|-------|-------|------|------|
| 1 | C1 | A2 | S1 | "[Hook text]" | Contrarian |
| 2 | C1 | A3 | S3 | "[Hook text]" | Show |
...

### Multiplication Summary
Concepts: X × Angles: ~Y × Styles: Z = **[Total] unique variation paths**

### Priority Testing Order
[Top 5 variations to test first, with rationale]
```

---

## FINALIZE
After producing the deliverable, log it through the quality gate (skip only for pure brainstorming):
```bash
// turbo
python3 execution/chain_runner.py finalize "[what you produced] for <market>" \
  --expert luke-iha --skill luke-iha-copy-blocks --workflow cash-method-generator \
  --type Content --intent N --expert-score N --adversarial N --factual N \
  --notes "Factual Grounding: N | Verification: PASS|N/A | Cache: WARM|COLD"
```
If the output contains stats / prices / dates / named entities, FIRST build a proof-claims ledger and run the deterministic G5 gate (see `/copy-engine` Phase 5):
```bash
// turbo
python3 execution/verify_proof_ledger.py --draft <draft-file> --ledger .tmp/copy-engine/<slug>/proof-claims.md || echo "label/cut claims before delivery"
```
Grep finalize output for `QUALITY GATE BLOCKED` and do NOT deliver on a match (finalize exits 0 even when it blocks).

## Quality Gate

> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
