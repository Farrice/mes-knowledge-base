---
description: Compliant Kallaway trend hook engine for Sandcastles-style signal intake, social outlier scoring, hook pattern clustering, and creative reaction handoff
---

# /kallaway-trend-hook-engine - Kallaway Trend Hook Engine

Load and execute `skills/kallaway-ai-content-engine/workflows/trend-hook-radar.md`.

## Required Context

Read:

1. `skills/kallaway-ai-content-engine/SKILL.md`
2. `skills/kallaway-ai-content-engine/workflows/trend-hook-radar.md`
3. `skills/kallaway-ai-content-engine/references/kallaway-trend-hook-plugin-spec.md`
4. `extractions/video-context/a7VjpIqq8Xk/desire-hook-evidence-map.md`
5. `extractions/video-context/a7VjpIqq8Xk/uncertainty-report.md`

Then use `execution/kallaway_trend_hook_radar.py` for the deterministic data contract and reports.

## Default Execution

Pre-flight route:

1. Lock the intent: trend/outlier analysis, hook pattern extraction, creative reaction, or plugin packaging.
2. Name the input state: manual CSV, owned metrics, approved LinkedIn evidence, public-data request, or missing data.
3. Route to the safest execution path and state any assumptions before running.

If the user supplied a CSV/export path:

```bash
python3 execution/kallaway_trend_hook_radar.py \
  --signals-csv [CSV_PATH] \
  --topic "[TOPIC]" \
  --business-objective "[OBJECTIVE]"
```

If the user supplied approved LinkedIn evidence:

```bash
python3 execution/kallaway_trend_hook_radar.py \
  --approved-linkedin-csv [CSV_PATH] \
  --topic "[TOPIC]" \
  --business-objective "[OBJECTIVE]"
```

If no data is supplied, run an empty-data check and return the exact next data step:

```bash
python3 execution/kallaway_trend_hook_radar.py
```

Only run public-data lanes when the user explicitly asks for that and budget/permission checks are acceptable:

```bash
python3 execution/kallaway_trend_hook_radar.py \
  --execute-apify \
  --apify-lane youtube \
  --apify-query "[QUERY]" \
  --limit 3
```

## Output

Produce:

- source evidence summary
- compliance boundary
- normalized signal receipt
- outlier/winner-line summary
- hook pattern summary
- creative reaction handoff
- book/content opportunity handoff
- next Kallaway component chain

## Validation And Test Gate

After local execution, verify the workflow with the relevant subset:

```bash
python3 -m py_compile execution/kallaway_trend_hook_radar.py
python3 execution/kallaway_trend_hook_radar.py --run-id test-empty
python3 execution/kallaway_trend_hook_radar.py --signals-csv execution/fixtures/kallaway_trend_hook_radar_sample.csv --topic "AI content systems" --business-objective "sell a workflow repair audit" --run-id test-manual
env APIFY_TOKEN= python3 execution/kallaway_trend_hook_radar.py --execute-apify --apify-lane youtube --apify-query "creator hook systems" --limit 1 --run-id test-apify-fallback
python3 execution/validate_skill.py source-command-kallaway-trend-hook-engine
python3 execution/command_menu.py search "Kallaway hooks trend analysis Sandcastles alternative"
python3 execution/workflow_router.py search "social outlier hook trend radar Sandcastles"
python3 execution/plugin_readiness_audit.py kallaway-trend-hook-engine --stdout
```

Quality gate:

- Empty-data test produces no fake trend claims.
- Manual CSV test produces stable outlier scores, confidence labels, and hook clusters.
- Budget/token fallback produces a structured fallback and still writes reports.
- Compliance test rejects unapproved LinkedIn rows and sponsored rows.
- Router test surfaces `/kallaway-trend-hook-engine` first for Kallaway trend/hook/Sandcastles/outlier queries.
- Plugin readiness controls whether packaging happens now or stays workflow-only.

## Failure And Fallback Handling

- Missing CSV: ask for the minimum CSV fields or run the empty-data receipt.
- Missing APIFY token or red budget: keep manual/owned-data workflow alive and record fallback in `run-receipt.json`.
- Missing source evidence: rerun the video-context ledger or state that method grounding is pending.
- Low-confidence clusters: keep them as creative prompts, not validated hook formulas.
- Stale or unsupported platform data: mark the row as excluded or low confidence.

## Handoff Chain

After the radar run, route the output through the smallest useful Kallaway chain:

`/kallaway-trend-hook-engine -> /ai-topic-mining -> /ai-hook-extractor -> /kcs-topic-format -> /kcs-hook-triad -> /ai-creative-sprint`

Skip downstream components when the radar has no compliant trend data.

## Stop Conditions

Stop and ask before:

- scraping LinkedIn
- login automation
- publishing or engagement actions
- DMs, comments, likes, follows, or outreach
- writing outside the workspace
- building the actual plugin when readiness is below `PACKAGE NOW`

**Execution prompts**: before producing the deliverable, check `skills/kallaway-ai-content-engine/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
