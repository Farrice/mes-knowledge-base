# Buyer-Trigger Design Psychology

## Purpose

Use this primitive when a product, offer, landing page, ad, design, merch concept, or client creative surface must create fast purchase intent by making a specific buyer feel seen.

This primitive generalizes Meg Heckman's print-on-demand buyer psychology into a cross-vertical Antigravity work primitive without losing the source boundaries.

Use the research-backed lane when the output depends on current buyer language, social listening, market evidence, trends, competitor claims, marketplace signals, or purchase intent outside the Meg source.

## Source Boundary

- Source package: `extractions/video-context/7MNa2YTPGs4/`
- Canonical expert spelling: Meg Heckman
- Alias preserved: Meg Hackman
- Primary evidence: timestamped spoken evidence in `video-context-ledger.md`
- Visual/OCR limit: frames were sampled, but OCR was unavailable; do not infer visual content without review
- Revenue/margin claims: source claims only, not independently verified

## Operating Definition

Buyer-trigger design is the practice of shaping a product or conversion surface so the right buyer:

1. recognizes themselves,
2. understands the hit quickly,
3. sees a specific lived scene,
4. imagines a social or professional reaction,
5. gets a familiar idea with a fresh twist,
6. feels first and justifies second.

## Trigger Fit Table

Use this table as the standard output:

| Candidate | Target Buyer | Identity Signal | Recognition Speed | Specificity | Social Currency Moment | Familiar/Twist Pair | Emotion-First Reason | Risk | Revision |
|---|---|---|---|---|---|---|---|---|---|

## Research-Backed Extension

For current-world work, run the public/free research lane before applying the trigger model:

```bash
python3 execution/buyer_trigger_research.py "[topic]" --mode research
```

Mode-specific runs use `--mode audit`, `--mode generate`, `--mode score`, or `--mode transfer`.

The research package must contain:

- Trigger Research Trace
- Research Receipt
- Source Ledger
- Insight Ledger
- Meg Mechanics Used
- Live Evidence Used
- Domain Extrapolation
- Trigger Fit Table
- Evidence Gaps / Risks

Apify is optional, guarded, and preview-first:

```bash
python3 execution/buyer_trigger_research.py "[topic]" --mode research --apify preview
```

Execute Apify only after explicit approval and with a per-run cap:

```bash
python3 execution/buyer_trigger_research.py "[topic]" --mode research --apify execute --apify-run-cap 0.25
```

Do not use paid/deep research providers silently. The default buyer-trigger research lane must not call `execution/research_router.py --provider auto`.

## Six Triggers

### 1. Identity Signal

Ask what the product lets the buyer say about themselves. If the answer is only "I like this topic," the signal is too weak.

### 2. Recognition Speed

The buyer should not need to decode the concept. In ads, thumbnails, product cards, or landing-page hero sections, the right person must get the hit fast.

### 3. Specific Person

Move from broad category to vivid person. Specificity should make the buyer feel the product was made for them, not for a demographic.

### 4. Social Currency Moment

Design the moment after purchase: comment, gift, share, status, inside joke, professional confidence, or public reaction.

### 5. Familiar/Twist Pair

Combine something the buyer already understands with something unexpected but true. Familiar-only is dull. Unexpected-only is confusing.

### 6. Emotion-First Reason

Create the feeling before stacking reasons. Copy, proof, page structure, product details, and offer mechanics should support the feeling instead of trying to manufacture it alone.

## Cross-Vertical Translation

| Original Apparel Logic | Product/Offer/Page Translation |
|---|---|
| The shirt says something about the buyer. | The offer/page names who the buyer is becoming or what they secretly know. |
| The joke reads instantly. | The headline or demo creates instant recognition. |
| Specific shirts feel personal. | Specific buyer scenes outperform broad ICP labels. |
| The wearer imagines a reaction. | The buyer imagines looking smart, prepared, advanced, funny, capable, or understood. |
| Familiar plus unexpected creates attention. | Known category plus non-obvious mechanism creates curiosity and trust. |
| Feeling comes first. | Proof and features come after the buyer feels the problem or desire. |

## Quality Gate

Reject output when:

- it is only pretty, clever, or original;
- the buyer cannot say what it says about them;
- the concept needs too much explanation;
- specificity is replaced by demographic labels;
- no social/reaction moment exists;
- the twist is confusing or absent;
- utility, price, or aesthetics carry the whole sale;
- claims exceed source evidence.
- current buyer insights, trends, social-listening claims, competitor claims, pricing claims, marketplace claims, or direct quotes appear without source URLs.
- evidence status is `FAILED` but the output still invents recommendations.

## Behavior Proof Requirement

For source-to-system builds and capability upgrades, include at least one before/after transformation:

- **Input tested:** existing concept, copy, page, or design.
- **Weakness diagnosed:** weakest buyer trigger.
- **Source mechanics used:** named trigger(s).
- **Output produced:** revised concept, copy, prompt, scorecard, or launch angle.
- **Behavior delta:** how purchase intent changed.
- **Validation run:** router, verifier, scorecard, or local artifact guard.
- **Remaining risk:** what still needs live buyer proof.

## Reuse Hook

Use this primitive in:

- `skills/meg-heckman-buyer-trigger-os/`
- `creative-direction` streetwear and apparel work
- Josh swing-nerd shirt testing
- MyBPM EDM streetwear prompt refinement
- offer and landing-page audits where identity and recognition matter
- client-facing creative diagnosis before design execution
