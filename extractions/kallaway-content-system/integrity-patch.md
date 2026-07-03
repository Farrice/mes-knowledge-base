# Kallaway Trend Hook Engine Integrity Patch

## Patch Verdict

This extraction is promoted from `patch proof/source` to trusted use when the
ledger sees this package-local integrity patch plus the fresh cold-start proof
run below.

## Source Boundary

- Source package: `extractions/kallaway-content-system/`
- Source summary: `extractions/kallaway-content-system/extraction-report.md`
- Grounding mode: transcript-backed extraction plus deterministic local radar
  fixture.
- Uncertainty: no private Sandcastles, private LinkedIn, private-feed, login, or
  unpublished platform claim is allowed.
- Visual and OCR boundary: do not infer visual/OCR evidence from this extraction
  unless a captured frame, OCR row, screenshot, or approved manual evidence row
  is present.
- Public-data boundary: public data lanes are budget and permission gated.
  Missing public data must return a fallback receipt, not a trend claim.

## Build Shape Decision

- Build shape decision: existing workflow layer, not a new hot command, not a
  new expert island, and not plugin packaging.
- Existing owner: `/kallaway-trend-hook-engine`.
- Duplicate route check: `/kallaway-trend-hook-engine` remains the owner for
  Sandcastles-style alternative signal intake, social outlier scoring, hook
  pattern clustering, and creative reaction handoff.
- Rejected duplicate surfaces: do not create another Kallaway trend expert,
  another hot command, or a plugin until plugin readiness says package now.
- Companion fit: this extraction stacks into the existing Kallaway AI content
  engine and downstream Kallaway content production workflows.

## Practitioner First-Run Path

Inputs:

- A compliant manual CSV, owned metrics export, or approved LinkedIn evidence
  export.
- Optional topic and business objective.

Step order:

1. Confirm the data lane: manual CSV, owned metrics, approved LinkedIn evidence,
   public-data request, or missing data.
2. Run the deterministic radar script.
3. Review included and excluded rows before trusting pattern output.
4. Read the hook pattern report and creative reaction brief.
5. Hand off only validated patterns into `/ai-topic-mining`,
   `/ai-hook-extractor`, `/kcs-topic-format`, `/kcs-hook-triad`, or
   `/ai-creative-sprint`.

Outputs:

- `normalized-signals.json`
- `outlier-ledger.csv`
- `hook-pattern-report.md`
- `creative-reaction-brief.md`
- `book-and-content-opportunity-map.md`
- `run-receipt.json`
- `run-receipt.md`

Quality gate:

- No unsupported trend claims.
- Sponsored or unapproved rows excluded from winner scoring.
- Outlier scores and confidence labels present.
- Hook clusters cite source signal IDs.
- Creative brief forces human reaction before script generation.

Failure modes:

- Missing data returns an empty-data receipt and next data step.
- Missing public-data token or budget keeps the manual/owned-data lane alive.
- Low-confidence clusters stay creative prompts, not validated formulas.

## Cold-Start Firing Proof

Natural-language probe:

`Sandcastles alternative social outlier hook trend radar`

Observed route result after repair:

| Surface | First route |
|---|---|
| command menu | `kallaway-trend-hook-engine` |
| workflow router | `kallaway-trend-hook-engine` |
| routing governor | `kallaway-trend-hook-engine` |

## Behavior Proof

Applied scenario:

- Before: `execution/fixtures/kallaway_trend_hook_radar_sample.csv` contained 8
  raw compliant and non-compliant sample rows.
- Run command:

```bash
python3 execution/kallaway_trend_hook_radar.py \
  --signals-csv execution/fixtures/kallaway_trend_hook_radar_sample.csv \
  --topic "AI content systems" \
  --business-objective "sell a workflow repair audit" \
  --run-id integrity-patch-2026-06-11
```

- After: `_active/farrice-content-os/04-deliverables/kallaway-trend-hook-engine/integrity-patch-2026-06-11/`
  contains a transformed artifact set: normalized signals, outlier ledger, hook
  pattern report, creative reaction brief, opportunity map, and run receipt.
- Behavior delta: the workflow changed raw social rows into a compliant scoring
  ledger, excluded 2 unsafe rows, clustered 3 hook patterns, and produced a
  human creative reaction brief instead of generic hook advice.

## Validation Coverage

Verifier coverage:

```bash
python3 -m py_compile execution/kallaway_trend_hook_radar.py
python3 execution/kallaway_trend_hook_radar.py --run-id test-empty
python3 execution/kallaway_trend_hook_radar.py --signals-csv execution/fixtures/kallaway_trend_hook_radar_sample.csv --topic "AI content systems" --business-objective "sell a workflow repair audit" --run-id test-manual
python3 execution/validate_skill.py source-command-kallaway-trend-hook-engine
python3 execution/command_menu.py search "Kallaway hooks trend analysis Sandcastles alternative"
python3 execution/workflow_router.py search "social outlier hook trend radar Sandcastles"
```

Current patch verifier:

```bash
python3 execution/audit_extraction_integrity.py --since 2026-05-01 --until 2026-06-11 --out _active/extraction-engine-drift-audit/04-deliverables/may-june-extraction-integrity-ledger.json
```
