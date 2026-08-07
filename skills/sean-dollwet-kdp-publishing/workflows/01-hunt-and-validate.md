---
name: hunt-and-validate
description: Run a dated 5–10-topic Amazon demand scan using multiple marketplace and reader-problem signals, risk exclusions, uncertainty, and a reversible GO/HOLD/NO-GO verdict before drafting.
produces: Dated demand-validation dossier with evidence table, sensitivity analysis, attack surfaces, and one recommended topic
expert: Sean Dollwet
load_context: genius.md
---

# Hunt & Validate — Evidence Before Manuscript

## Pre-Flight Gate

Run first. AI topic suggestions are ideation, not validation. Do not proceed until one topic has current marketplace evidence, independent reader-problem corroboration, an acceptable risk class, and Farrice's niche approval.

Load `genius.md`, `references/kdp-policy-and-evidence-boundary.md`, and `references/prompts-v2/demand-validation-report.md`.

## Execution

### 1. Build a 5–10-topic candidate set

Combine the operator's real experience, Amazon category browsing, recurring reader questions, and AI ideation. Narrow each candidate to one problem, one reader, and the phrase a buyer would plausibly search. Exclude medical treatment, legal, investing/tax, mental-health treatment, or other high-stakes claims unless a qualified reviewer is already in scope.

### 2. Capture dated marketplace snapshots

For each topic, record:

`captured_at, marketplace, format, query, title, author, ASIN, visible_BSR, reviews, price, publication_date_if_visible, source_url_or_screenshot, observation_notes`

Sample several relevant books from different publishers. Note which result is sponsored, authoritative/celebrity-led, bundled, or not comparable. Do not translate a rank into revenue unless the estimate is labeled `SOURCE_REPORTED`, dated, and sensitivity-tested.

### 3. Add independent demand corroboration

Capture repeated problem language from current search suggestions, forums, communities, customer questions, or other reader surfaces. Record source and date. A model saying a topic is “trending” does not count.

### 4. Find the attack surface without copying

Abstract repeated reader complaints, missing coverage, stale information, weak positioning, poor sample quality, or dated visual conventions. Review count is one friction signal, not a moat or required threshold. Never retain competitor wording, distinctive sequence, stories, examples, or protected material.

### 5. Run sensitivity and red flags

- Re-test the verdict if BSR, review, or search-result thresholds move materially.
- Check whether the exact query has multiple relevant sellers rather than one outlier.
- Treat ranking without buyer events as ambiguous, not automatically proof of dead demand.
- Reject a topic if success depends on unsupported claims, copied authority, unowned rights, or an audience the operator cannot serve responsibly.

### 6. Issue the decision

Use `GO`, `HOLD`, or `NO-GO`:

- `GO`: multiple current signals, a specific reader/problem, a defensible gap, and no unresolved critical risk.
- `HOLD`: promising but missing a material data point, qualified reviewer, or rights answer.
- `NO-GO`: absent/contradictory demand, no credible differentiation, or unacceptable risk.

Recommend one topic and surface the weakest assumption. Income remains `UNTESTED`.

## Output Requirements

- Candidate verdict table with evidence class and uncertainty.
- Per-topic marketplace snapshot table.
- Independent reader-problem corroboration.
- Attack-surface map and prohibited-copy boundary.
- Threshold sensitivity and risk-class read.
- One recommended topic plus one alternative.
- Exact data gaps and the niche approval checkpoint.

`Execution prompt: references/prompts-v2/demand-validation-report.md`

## Quality Gate

- [ ] Five to ten topics were compared unless a smaller set was explicitly approved.
- [ ] Every marketplace observation names date, marketplace, format, query, source, and uncertainty.
- [ ] Multiple signals—not one BSR or review threshold—support each verdict.
- [ ] Reader-problem evidence exists outside AI output.
- [ ] High-stakes and rights risks were screened.
- [ ] Competitor research was abstracted without retained protected expression.
- [ ] No rank, revenue, search volume, sales, or income value was fabricated.
- [ ] Drafting is blocked until niche approval.
