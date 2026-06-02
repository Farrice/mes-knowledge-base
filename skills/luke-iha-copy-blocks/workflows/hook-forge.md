---
description: Generate 30+ hooks using positioning types, psychological triggers, and proof-of-work patterns
---

# Hook Forge

Mass hook generation engine. Produces 30+ testable hooks for any offer using systematic positioning types, psychological trigger categories, and proof-of-work patterns. Includes scoring and priority testing recommendations.

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
1. /Users/farricecain/Google Antigravity/skills/luke-iha-copy-blocks/references/genius-patterns.md (focus on GP3: Solve vs Show, GP4: Proof-of-Work Hooks)
2. /Users/farricecain/Google Antigravity/skills/luke-iha-unaware-ads/references/genius-patterns.md (for hook psychology overlap)

## PHASE 2: INPUT REQUIREMENTS

Collect from user:
- **Product/Offer**: What's being sold?
- **Target Audience**: Who is this for? Awareness level?
- **Key Result/Transformation**: What's the main outcome?
- **Unique Mechanism** (optional): What makes it work differently?
- **Key Proof Points**: Best testimonial, most impressive stat, strongest credential
- **Platform**: Where will these hooks run? (affects length and style)

## PHASE 3: HOOK GENERATION — By Positioning Type

Generate 3+ hooks for each positioning type:

### Contrarian (3+ hooks)
Pattern: Contradicts common belief
"Everything you know about [topic] is wrong — and it's costing you [consequence]"

### Authority (3+ hooks)
Pattern: Leverages credibility or expertise
"After [impressive credential], here's the one thing I'd tell my younger self about [topic]"

### Demonstration (3+ hooks)
Pattern: Shows the result visually or through narrative
"Watch me [do impressive thing] in [surprisingly short time] using [unexpected method]"

### Confession (3+ hooks)
Pattern: Insider reveals hidden truth
"I spent [X years] in [industry] — here's what we never told you about [topic]"

### Data-Driven (3+ hooks)
Pattern: Uses surprising statistics
"[Surprising statistic]% of [audience] make this one mistake with [topic]"

### Story (3+ hooks)
Pattern: Opens with compelling narrative
"Last [timeframe], [specific person] was [in bad situation]. [Short time] later, [dramatic result]"

### Proof-of-Work (3+ hooks)
Pattern: Hook itself demonstrates expertise
"I analyzed [large number] of [things] and found the [number] pattern(s) that [result]"

## PHASE 4: HOOK GENERATION — By Architecture

Also generate:
### Solve Hooks (5+)
"Here's why [problem] — and the [descriptor] fix"
"The #1 mistake [audience] makes with [topic] (and what to do instead)"

### Show Hooks (5+)
"I [achieved result] using [unexpected method]"
"[Person] went from [bad state] to [good state] in [timeframe] — here's how"

## PHASE 5: SCORING

Score each hook on:
1. **Curiosity** (1-10): Does it create an open loop?
2. **Relevance** (1-10): Does it connect to a felt pain/desire?
3. **Specificity** (1-10): Does it contain concrete details?
4. **Testability** (1-10): Can it stand alone as a test unit?

Total score out of 40.

## OUTPUT FORMAT

```
## Hook Forge Output: [Product Name]

### Hooks by Positioning Type
[All hooks organized by type with scores]

### Hooks by Architecture
[Solve hooks and Show hooks with scores]

### Top 10 Priority Test Hooks
| Rank | Hook | Type | Score | Rationale |
|------|------|------|-------|-----------|

### Quick-Launch Pack
[Top 3 hooks formatted for immediate deployment on the target platform]
```

---

## FINALIZE
After producing the deliverable, log it through the quality gate (skip only for pure brainstorming):
```bash
// turbo
python3 execution/chain_runner.py finalize "[what you produced] for <market>" \
  --expert luke-iha --skill luke-iha-copy-blocks --workflow hook-forge \
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
