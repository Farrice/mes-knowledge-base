---
description: Classify every claim in existing health/supplement copy against the 5-bucket risk taxonomy, run the net-impression test, and score for FTC/FDA disease-claim risk
---

# /claim-audit — Deterministic Claim-Risk Classifier

Audit existing copy (ad, landing page, email, social post, product listing) sentence-by-sentence against the claim-risk taxonomy, then re-check the whole piece for net-impression risk. Produces a scored diagnostic with specific flags — this is the deterministic classifier at the core of the skill.

## Pre-Flight Gate

**Use this when**:
- Copy already exists (drafted by a human, another skill, or an unaudited AI) and needs a compliance pass before it ships
- A brand's existing marketing needs a risk inventory before a launch or ad-account review
- You're diagnosing why an ad got rejected on Meta/TikTok/Amazon

**Do NOT use this when**:
- Copy doesn't exist yet — start with `/claim-safe-hooks` or `/compliant-rewrite` instead so compliance is front-loaded, not retrofitted
- The task is verifying whether evidence EXISTS for a claim (that's `/claim-substantiation-map`)
- This is a full pre-launch sign-off — run `/pre-launch-compliance-gate` instead, which wraps this workflow plus platform + disclaimer checks

## Skill Acquisition

Load before executing:
- `genius.md` — GP-01 (Claim-Risk Taxonomy), GP-02 (Substantiation Ladder), GP-03 (Net Impression)
- `references/red-flag-word-bank.md` — token-level flag list

## Execution

### Step 1: Segment the Copy

Break the input into discrete claim-bearing units: headline, subhead, each body paragraph, each bullet, each testimonial, each CTA, image captions/alt text if provided.

### Step 2: Classify Each Unit (5-Bucket Taxonomy)

For every unit, assign exactly one bucket from genius.md GP-01:
1. Disease claim (express)
2. Disease claim (implied) — check against the 5 triggers (outcome-stacking, contextual imagery, symptom-matching, substitute-for-treatment framing, citation-borrowing)
3. Structure/function claim
4. Qualified health claim
5. General wellbeing / puffery

Flag any Bucket 1 or 2 unit immediately — these are hard-stop violations regardless of evidence.

### Step 3: Net Impression Pass

Re-read the ENTIRE piece as a skimming stranger (genius.md GP-03 test). Answer:
- What does a reasonable consumer think this product does, based on headline + imagery + one testimonial + CTA together?
- Does any combination of individually-compliant units add up to an implied disease claim?

Flag net-impression failures separately from sentence-level failures — a piece can pass Step 2 unit-by-unit and still fail here.

### Step 4: Testimonial Check

For every testimonial/review quoted or referenced:
- Does it depict an atypical result without a typical-result disclosure? (genius.md GP-05)
- Does it use disease-claim language the brand couldn't say itself? (Anti-Pattern #1 — a customer's words don't launder a disease claim)

### Step 5: Score and Report

```markdown
# Claim Audit — [asset name]

## Unit-Level Classification
| Unit | Text (excerpt) | Bucket | Flag |
|---|---|---|---|
| Headline | "..." | [1-5] | [none / HARD-STOP / evidence-check-needed] |
| ... | | | |

## Net Impression
- Reasonable-consumer read: [...]
- Net impression flags: [none / describe]

## Testimonial Check
- [pass/fail per testimonial, with reasoning]

## Risk Score
| Category | Count |
|---|---|
| Bucket 1/2 (HARD-STOP disease claims) | n |
| Net impression flags | n |
| Testimonial flags | n |
| Bucket 3/4 needing evidence-tier check | n |

## Verdict
[CLEAR — no flags / REWRITE NEEDED — n hard-stops / BLOCKED — net impression fails regardless of unit-level edits]

## Next workflow
[If hard-stops: /compliant-rewrite. If evidence gaps: /claim-substantiation-map. If clean: /pre-launch-compliance-gate before ship.]
```

## Content Type Adaptations

| Content type | Audit focus | Common failure |
|---|---|---|
| **Meta/paid ad** | Net impression + Personal Attributes check | Second-person symptom hooks ("Struggling with...") |
| **Amazon listing** | Token-level scan (disease names anywhere) | Compliant sentence containing an unrelated disease-name token |
| **Long-form landing page** | Testimonial check is heaviest lift | Real customer quotes containing disease-claim language used verbatim |
| **Email sequence** | Cross-email net impression (does the SEQUENCE imply a disease claim even if no single email does?) | Escalating urgency across emails building toward an implied cure claim |
| **Social/organic post** | Hook-level Bucket 1/2 check | Hooks written for shock value default to disease-claim language |

## Output Requirements

1. Every claim-bearing unit classified, no unit skipped
2. Net impression assessed as a whole, separate from unit-level scoring
3. Testimonials checked against GP-05 independently
4. Clear HARD-STOP vs. advisory distinction — do not bury disease claims in a generic "risk score"
5. Explicit next-workflow recommendation

## Quality Gate

- [ ] No Bucket 1/2 unit was missed or downgraded to Bucket 3/5
- [ ] Net impression was tested as a whole read, not inferred from unit scores
- [ ] Every testimonial was checked independently
- [ ] Verdict matches the actual flag count (a single hard-stop cannot produce a CLEAR verdict)

If any check fails, redo the audit before delivery — a missed disease claim here is the failure mode this entire skill exists to prevent.
