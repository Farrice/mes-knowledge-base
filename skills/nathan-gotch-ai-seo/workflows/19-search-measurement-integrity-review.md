---
name: "Search Measurement Integrity Review"
produces: "AI/traditional search measurement audit, observation contract, and proof-gap verdict"
expert: "Nathan Gotch AI SEO"
load_context: "genius.md + references/search-content-mastery-source-ledger.md"
tier: 1
menu_exempt: true
source: "portfolio — LiLD7_tjn4o, 3sHPiOIHPTY, 53h_-LoEGiw, 6o0mabKRmIo"
---

# Nathan Gotch — Search Measurement Integrity Review

Audit a tracker, report, experiment, or service claim so sampled AI visibility, traditional rank, citations, traffic, conversions, and revenue cannot collapse into one flattering score.

## Input Required

- **[MEASUREMENT_CLAIM]**: the claim, dashboard, score, or experiment under review
- **[IMPORT_RECEIPTS]**: raw hashes, field mappings, date ranges, and normalized local exports
- **[AI_OBSERVATIONS]**: exact prompt, surface, model/version when exposed, session mode, locale, run, answer, citations, and evidence
- **[WORK_ANNOTATIONS]**: dated shipped actions for the category
- **[OUTCOME_EVENTS]**: independent SearchEvents, if any

## Workflow

1. Identify whether the claim concerns a prediction, publication, indexation, rank, citation, traffic, conversion, or collected revenue.
2. Separate generated-answer brand mentions from retrieval citations and both from observable referral traffic.
3. Inspect provenance. Without a first-party platform source, label AI prompt demand modeled or `UNCONFIRMED`; never call it true search volume.
4. Inspect sampling: seed cluster, prompt variants, reruns, model/version, personalization/authentication, locale, time, native versus simulated citations, and run variance.
5. Inspect traditional imports for raw hash, mapping, date range, and schema completeness.
6. Read movement against dated work annotations. Report correlation and uncertainty; do not assign one-asset causation without stronger design.
7. Keep all outcome stages independent. Name the earliest proven stage and every later missing stage.
8. Propose a next observation or workflow review. Mark it `UNCONFIRMED`, append-only, and `HUMAN_REQUIRED`.

## Output Requirements

- Measurement claim verdict
- Provenance and sampling audit
- Independent outcome-stage table
- Confounders and attribution limits
- Earliest proven state, missing states, and next falsifiable observation
- Human-promoted recommendation only
- Execution prompt: `references/prompts-v2/39-search-measurement-integrity-review.md`

## Quality Gate

- [ ] No synthetic prompt count is labeled true demand
- [ ] One prompt/run is not called stable rank
- [ ] Mentions, citations, traffic, conversions, and collected revenue remain separate
- [ ] Every accepted import retains hash, mapping, and date range
- [ ] Work annotations and measurement windows are visible
- [ ] No automatic skill change or market guarantee is made
