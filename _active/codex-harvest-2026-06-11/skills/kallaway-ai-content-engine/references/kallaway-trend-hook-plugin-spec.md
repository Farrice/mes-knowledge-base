# Kallaway Trend Hook Engine - Plugin-Ready Spec

## Packaging Verdict Gate

Do not build the plugin from this spec until local plugin-readiness scoring says `PACKAGE NOW`. Until then, keep this as a workflow plus thin command wrapper.

Current package shape:

- Local workflow: `.agent/workflows/kallaway-trend-hook-engine.md`
- Local script: `execution/kallaway_trend_hook_radar.py`
- Local Kallaway workflow extension: `skills/kallaway-ai-content-engine/workflows/trend-hook-radar.md`
- Source evidence: `extractions/video-context/a7VjpIqq8Xk/`
- Global thin wrapper target: `/Users/farricecain/.codex/skills/source-command-kallaway-trend-hook-engine/SKILL.md`

## Plugin Purpose

Give Codex a reusable, compliant alternative to the Sandcastles-style workflow pattern for social trend analysis, outlier scoring, hook pattern extraction, and creative reaction handoff.

The plugin must not claim to reproduce Sandcastles proprietary software. It packages a local workflow pattern that can accept approved inputs and produce reusable reports.

## Inputs

| Input | Required | Permission Boundary |
|---|---:|---|
| Manual CSV | No | User-provided, read-only. |
| Owned metrics CSV | No | User-owned export only. |
| Approved LinkedIn CSV/export/screenshot reference | No | No scraping or login automation. |
| Manual JSON | No | User-provided, read-only. |
| Public YouTube/Reddit/TikTok/Instagram/web lane | No | Budget-guarded explicit execution only. |
| Topic(s) | No | Used for creative-reaction moves, not trend claims. |
| Business objective | No | Used to bias opportunity mapping. |

Minimum useful row fields:

`platform`, `creator`, `hook_text`, `views`, `avg_views`, `topic`, `url`.

## API Shape

Local command equivalent:

```bash
python3 execution/kallaway_trend_hook_radar.py \
  --signals-csv path/to/signals.csv \
  --topic "creator hook systems" \
  --business-objective "sell an AI content audit"
```

Plugin tool shape:

```json
{
  "input_files": [
    {
      "path": "path/to/signals.csv",
      "kind": "manual_csv"
    }
  ],
  "topics": ["creator hook systems"],
  "business_objective": "sell an AI content audit",
  "public_data": {
    "execute": false,
    "lanes": ["youtube", "reddit"],
    "queries": ["creator hook systems"],
    "limit": 10
  },
  "source_package": "extractions/video-context/a7VjpIqq8Xk/"
}
```

Tool response:

```json
{
  "status": "ok",
  "run_id": "2026-05-28-120000",
  "run_dir": "_active/farrice-content-os/04-deliverables/kallaway-trend-hook-engine/2026-05-28-120000",
  "outputs": {
    "normalized_signals": ".../normalized-signals.json",
    "outlier_ledger": ".../outlier-ledger.csv",
    "hook_pattern_report": ".../hook-pattern-report.md",
    "creative_reaction_brief": ".../creative-reaction-brief.md",
    "book_and_content_opportunity_map": ".../book-and-content-opportunity-map.md",
    "run_receipt_json": ".../run-receipt.json"
  },
  "apify_status": []
}
```

## Data Permissions

Allowed:

- Read manual CSV/JSON rows supplied by the user.
- Read owned analytics exports.
- Read approved LinkedIn evidence only when user labels it as export, screenshot, owned, manual, or approved.
- Run public-data lanes only with explicit execution flag and existing budget guard.

Disallowed:

- LinkedIn scraping.
- Login automation.
- Circumventing platform permissions.
- Publishing or engagement actions.
- Outreach, DMs, comments, likes, or follows.
- Creating claims from missing data.

## Outputs

| File | Purpose |
|---|---|
| `normalized-signals.json` | Full `SignalItem` ledger with compliance and inclusion flags. |
| `outlier-ledger.csv` | Scores, confidence, winner-line status, and reason codes. |
| `hook-pattern-report.md` | Pattern clusters and evidence boundary. |
| `creative-reaction-brief.md` | Human creative reaction prompts and candidate hook moves. |
| `book-and-content-opportunity-map.md` | Book, series, lead magnet, and production opportunities. |
| `run-receipt.json` | Machine-readable receipt for validation and routing. |
| `run-receipt.md` | Human-readable closeout. |

## Fresh-Thread Tests

1. Direct command:
   - Prompt: `Run /kallaway-trend-hook-engine on this CSV and make no unsupported trend claims.`
   - Pass: Codex loads the workflow, runs the script, and names the output folder.

2. Natural language:
   - Prompt: `I need a Sandcastles alternative for finding outlier hooks from my manual creator spreadsheet.`
   - Pass: Router surfaces `/kallaway-trend-hook-engine`.

3. Empty data:
   - Prompt: `Run the trend hook engine with no data and tell me what it can safely conclude.`
   - Pass: Output says no trend claim yet and asks for the minimum next data step.

4. LinkedIn compliance:
   - Prompt: `Analyze these LinkedIn rows.`
   - Pass: Rows without approved/export/screenshot/owned/manual status are rejected from scoring.

5. Budget fallback:
   - Prompt: `Try YouTube public-data lane without an Apify token.`
   - Pass: Structured fallback is written; manual-data brief still exists.

6. Plugin packaging:
   - Prompt: `Should this become a plugin now?`
   - Pass: Codex runs plugin-readiness scoring and follows the `PACKAGE NOW` gate.

## Packaging Risks

- Plugin installation cannot grant private social-platform access.
- Public-data actors may change fields or pricing.
- Hook generation quality depends on row quality and human creative reaction.
- The source video has OCR unavailable, so visual/demo claims need a human or vision adapter before being treated as evidence.
- Workflow should stay a Kallaway AI Content Engine extension, not a duplicate content OS.

## Plugin Acceptance Bar

Package only when all are true:

- Local workflow, source command, and wrapper validate.
- Empty-data, manual CSV, LinkedIn compliance, and budget fallback tests pass.
- Router surfaces the command for Kallaway hooks, trend analysis, Sandcastles alternative, and social outlier queries.
- A fresh thread can run the workflow without hidden context.
- The readiness score returns `PACKAGE NOW`; otherwise, improve the workflow layer first.
