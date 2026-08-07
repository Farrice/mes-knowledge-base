# Goal Packet — Human-Promoted Learning Loop

| Field | Locked value |
|---|---|
| `target` | Search-content measurement recommendations produced by `execution/search_content_mastery.py`; no automatic edits to skills, workflows, prompts, routers, or canon. |
| `scope` | Append observed `SearchEvent` records and produce source-referenced workflow-change recommendations. Excludes automatic promotion, cleanup, deletion, publishing, connectors, schedulers, and external writes. |
| `per_item_criteria` | A recommendation must cite at least one dated event, name the affected workflow decision, state the counterfactual, and distinguish correlation from causation. |
| `permitted_side_effect` | Append a `PROPOSED` recommendation record inside the project pack only. |
| `proof_artifact` | Project `ledgers/outcomes.jsonl`, import receipts, score receipts, and `ledgers/recommendations.jsonl`. |
| `measurable_stop` | Stop after one recommendation set per explicit measure run; no open-ended self-review. |
| `turn_cap` | One generation pass plus one validation repair pass. |
| `evaluator` | Schema validation, evidence-path existence, stage independence, and human review. |
| `wake_up_check` | `python3 execution/search_content_mastery.py measure --project <pack> --review-recommendations` |
| `human_checkpoint` | Required before any recommendation is promoted into a skill, workflow, prompt, router, or offer. |
| `rollback_or_archive_rule` | Records are append-only. A rejected recommendation receives a new `REJECTED` decision row; prior rows are never deleted or rewritten. |

## Evolution Council Verdict

- **Target:** project-local search-content recommendations.
- **Goal packet complete:** yes.
- **Recommended path:** queue-only.
- **Permitted side effect:** append `PROPOSED` recommendation rows.
- **Proof artifact:** outcome, import, and recommendation ledgers.
- **Stop condition:** one validated recommendation set per explicit run.
- **No-regression check:** skill and workflow trees remain unchanged by measurement commands.
- **Human checkpoint:** Farrice explicitly promotes or rejects a recommendation.
- **Open risk:** imported correlations can be mistaken for causal SEO rules; every recommendation must keep that limitation visible.

