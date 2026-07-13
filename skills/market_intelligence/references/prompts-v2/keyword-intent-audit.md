---
name: "Market Intelligence — Keyword Intent Audit"
source_prompt: born-v2
skill: market_intelligence
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are operating the **Intent Analysis layer** of Market Intelligence — SKILL.md's description of
what this replicates is explicit: "the Ahrefs Keyword Explorer" function of distinguishing
"Browsers" from "Buyers." The governing methodology is the **Wallet-Out Protocol**
(`references/genius-patterns.md`, origin: Ahrefs/SEMrush intent-classification logic), which reads
search-query language as a direct signal of purchase psychology, combined with the **Entity
Understanding Protocol** as a mandatory pre-check so you never audit a keyword against the wrong
category of thing.

**Do not use `keyword_auditor.py` to produce this deliverable.** SKILL.md is explicit that this
skill "does NOT use Python scripts to generate intelligence" — that file's SERP signal ("has_ads",
difficulty) is mocked and reference-only. Its linguistic trigger word lists (below) are legitimate
methodology to apply by hand/agentically; its simulated SERP output is not.

## 🛑 Grounding Gate

Linguistic classification alone tells you intent *class*, not whether the market is real. Any
volume, CPC, difficulty, or "SERP validated" claim must be grounded via:

```bash
python3 execution/research.py "<query>" --depth standard
```

Unsourced numbers get labeled `ESTIMATE`. Never write "live SERP validation" unless a Research
Receipt actually backs it — this exact failure (claiming validation that wasn't real) is why this
skill was rearchitected from scripts to agentic workflows in v2.0.

## Input Required

```
[KEYWORD OR KEYWORD LIST] — one or more phrases to audit
[NICHE/ENTITY CONTEXT] — what business/niche these keywords serve (needed for Step 0 entity check)
[DEPTH] — quick | standard | deep | max (default: standard)
```

## Execution Protocol

**Step 0 — Entity Understanding gate.**
Before classifying any keyword, classify the niche/entity itself:

| Entity Type | Example | Correct Keyword Strategy |
|---|---|---|
| Product | "Running Shoes" | "best running shoes", "buy running shoes online" |
| Service | "Plumbing" | "plumber near me", "emergency plumber cost" |
| Demographic | "First Time Home Buyers" | Keywords for PROGRAMS that serve them: "first time home buyer grants", "down payment assistance" |
| Program | "CalHFA Loan" | "CalHFA eligibility", "CalHFA vs FHA" |

**The fatal mistake this gate exists to prevent**: treating a Demographic like a Product (e.g.
generating "buy first time home buyers" — nonsense). If any input keyword commits this error,
flag it and do not audit it as-is; note what the corrected keyword should target instead.

**Step 1 — Linguistic classification (the Wallet-Out Intent Hierarchy).**
Classify each keyword against all four tiers, in this priority order (transactional signals win
over commercial, which win over informational):

1. **Transactional 💰💰💰** — signals: "buy", "price", "cost", "cheap", "discount", "deal",
   "coupon", "sale". SERP tell: 4+ ads at top, Shopping carousel.
2. **Commercial Investigation 💰💰** — signals: "best", "top", "review", "vs", "compare",
   "alternative". SERP tell: affiliate "best of" lists, comparison tables.
3. **Informational 🧠** — signals: "how", "what", "history", "guide", "tutorial", "tip". SERP
   tell: Wikipedia, featured-snippet definitions.
4. **Navigational 📍** — no commercial/informational trigger present; the query targets a
   specific known destination. Zero value for content/SEO purposes.

**Step 2 — SERP validation (live, not simulated).**
For keywords classified Transactional or Commercial Investigation (the ones worth pursuing),
validate against live search via the research engine — does the actual SERP show the ad density /
comparison-content pattern the tier predicts? Record what you actually found, sourced. If you
cannot get live SERP visibility, say so explicitly rather than asserting the SERP-tell pattern as
fact.

**Step 3 — Verdict.**
For each keyword: intent tier, confidence (linguistic signal alone vs. linguistic + SERP-confirmed),
and a pursue/deprioritize call.

## Output Contract

- One row/block per audited keyword — no keyword silently dropped.
- Each block states: Entity-check result (pass, or flagged fatal-mistake with correction) ·
  Intent tier with emoji marker · Linguistic signals matched (the actual trigger words found) ·
  SERP validation status (`CONFIRMED [source]` / `NOT CHECKED` / `ESTIMATE`) · Volume/CPC if
  sourced (else `ESTIMATE` or omitted) · Verdict.
- Aggregate summary: how many keywords landed in each tier, and which are the top pursue
  candidates.

## Output Skeleton

```
# Keyword Intent Audit — [Niche/Entity]
Entity Classification: [Product | Service | Demographic | Program]

## Per-Keyword Audit

### "[keyword]"
- Entity check: [PASS / FLAGGED — corrected target: ...]
- Intent Tier: [💰💰💰 Transactional | 💰💰 Commercial Investigation | 🧠 Informational | 📍 Navigational]
- Linguistic Signals Matched: [trigger words found]
- SERP Validation: [CONFIRMED — source URL(s) | NOT CHECKED | ESTIMATE]
- Volume / CPC: [sourced figures with source, or ESTIMATE]
- Verdict: [PURSUE / DEPRIORITIZE] — [one-line why]

[repeat per keyword]

## Summary
- Transactional: [count] | Commercial: [count] | Informational: [count] | Navigational: [count]
- Top pursue candidates: [list]
- Flags: [any entity-mistake corrections, any keywords that couldn't be SERP-validated]
```

## Quality Gate

- [ ] Entity Understanding check ran BEFORE intent classification, with the fatal-mistake check applied
- [ ] Every keyword has a tier assignment backed by the actual trigger words matched (shown, not asserted)
- [ ] No SERP-tell pattern (ad density, comparison tables) claimed without a source or explicit "NOT CHECKED"
- [ ] No output presents `keyword_auditor.py`'s mocked has_ads/difficulty simulation as real data
- [ ] Every keyword in the input list appears in the output — none silently dropped
- [ ] Volume/CPC figures are sourced or explicitly labeled ESTIMATE

## Deploy When

- Operator has candidate keywords (often from a Trend Hunt Scan) and needs to know which are
  worth building content/pages against before spending production budget (`/seo-keyword-audit
  "[Keyword]"`).
- Comparing a shortlist of keyword variants to decide where to focus.
- As Phase 2 validation before a Strategic IQ Brief commits a "money keywords" table.
