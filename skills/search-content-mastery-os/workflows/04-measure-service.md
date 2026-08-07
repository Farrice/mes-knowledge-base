---
description: "Normalize local search exports, append independent outcome events, queue learning proposals, and validate a service delivery pack."
menu_exempt: "Routed through /search-content-mastery measure or service."
---

# Search Content Mastery — Measure And Service

## Diagnose Before Treat

Name the evidence source and the exact outcome stage it can support. A rank-tracker export cannot prove collection; an AI citation observation cannot prove traffic; GA4 traffic cannot prove causation.

## Execution

1. Import a strict local export or observation:

   ```bash
   python3 execution/search_content_mastery.py measure --project <path> --source <gsc|ga4|gbp|youtube|clarity|rank_tracker|ai_citation> --input <csv-or-json> [--mapping <mapping.json>] [--date-start YYYY-MM-DD --date-end YYYY-MM-DD] [--content-id <id> --stage <stage>]
   ```

2. Review proposed changes without mutation:

   ```bash
   python3 execution/search_content_mastery.py measure --project <path> --recommend
   python3 execution/search_content_mastery.py measure --project <path> --review-recommendations
   ```

3. Validate a nine-artifact delivery map:

   ```bash
   python3 execution/search_content_mastery.py service --project <path> --artifacts <artifact-map.json>
   ```

## Output Schema

- Raw and normalized import refs, hash, mapping, row count, and date range.
- Optional independent SearchEvent.
- `PROPOSED` recommendations with causal status and evidence IDs.
- ServiceReceipt with scope, proof gaps, and `UNTESTED` prototype state.

## Quality Gate

- Raw import is unchanged and hash-addressed.
- No unknown or incomplete schema was accepted.
- Outcome stages remain independent.
- Recommendations do not mutate system files.
- Service boundaries preserve live offer canon and forbid market guarantees.

Execution prompt: `references/prompts-v2/search-measurement-experiment.md` and `references/prompts-v2/search-service-delivery-pack.md` — honor their Output Contracts.

