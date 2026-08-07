# Search Content Mastery — Data Contract

## Core Records

| Record | Schema | Authority |
|---|---|---|
| `SearchProjectManifest` | `schemas/search-content-mastery/search-project-manifest.schema.json` | Portable project truth and boundaries |
| `SearchBrief` | `schemas/search-content-mastery/search-brief.schema.json` | Approved search and production decision |
| `ContentScoreReceipt` | `schemas/search-content-mastery/content-score-receipt.schema.json` | Transparent predicted quality, judgment, and override |
| `SearchEvent` | `schemas/search-content-mastery/search-event.schema.json` | One dated observation at one independent outcome stage |
| `ServiceReceipt` | `schemas/search-content-mastery/service-receipt.schema.json` | Bounded delivery completeness and proof gaps |

## Import Law

1. Preserve the raw CSV/JSON under its SHA-256 hash.
2. Accept only a named profile in `import-profiles.json`.
3. Require every canonical field; reject unknown fields.
4. A non-canonical source header requires an explicit complete mapping file.
5. Preserve declared and observed date range.
6. Reject duplicates by raw hash.
7. Normalize into a separate file; never modify the raw import.

## Outcome Law

`PREDICTED`, `PUBLISHED`, `INDEXED`, `RANKED`, `CITED`, `TRAFFIC`, `CONVERTED`, and `COLLECTED` are independent observations. A later stage does not backfill an earlier one, and readiness never creates an event.

## Override Law

Farrice's override is authoritative for the current decision, but it is additive. Preserve the original composite, override score, operator, reason, and time.

## Learning Law

Recommendations are append-only `PROPOSED` records with evidence event IDs and `causal_status: UNCONFIRMED`. Only a human may promote them into system behavior.

