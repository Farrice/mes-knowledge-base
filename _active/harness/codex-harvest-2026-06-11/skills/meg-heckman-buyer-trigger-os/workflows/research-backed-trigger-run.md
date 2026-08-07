---
description: Run current public research, social listening, source-led evidence capture, and buyer-trigger mapping before applying Meg Heckman's trigger model.
---

# Research-Backed Trigger Run

## Input

- Niche, product, offer, page, apparel concept, buyer community, or market.
- Mode to support: research, audit, generate, score, or transfer.
- Research depth: quick, standard, deep, or max. Default is standard.
- Optional Apify lane: preview by default; execute only when explicitly approved.
- Optional source-only mode when the user wants Meg/source mechanics without live research.

## Command Contract

Default public/free run:

```bash
python3 execution/buyer_trigger_research.py "[topic]" --mode research
```

Mode-specific research:

```bash
python3 execution/buyer_trigger_research.py "[topic]" --mode generate
python3 execution/buyer_trigger_research.py "[topic]" --mode audit
python3 execution/buyer_trigger_research.py "[topic]" --mode score
python3 execution/buyer_trigger_research.py "[topic]" --mode transfer
```

Source-only run:

```bash
python3 execution/buyer_trigger_research.py "[topic]" --mode [mode] --source-only
```

Apify preview:

```bash
python3 execution/buyer_trigger_research.py "[topic]" --mode research --apify preview
```

Codex web-search or user-provided source ingestion:

```bash
python3 execution/buyer_trigger_research.py "[topic]" --mode research \
  --seed-url "https://source.example/page-1" \
  --seed-url "https://source.example/page-2"
```

Codex web-search snippet ingestion when a page blocks readers:

```bash
python3 execution/buyer_trigger_research.py "[topic]" --mode research \
  --seed-finding-json '{"url":"https://source.example/page","claim":"Source-backed search snippet or extracted finding","source_type":"social_listening"}'
```

Apify execution, only after explicit approval:

```bash
python3 execution/buyer_trigger_research.py "[topic]" --mode research --apify execute --apify-run-cap 0.25
```

Do not use `execution/research_router.py --provider auto` for the default lane because it can invoke paid providers.

## Steps

1. Load `references/source-ledger.md` and `references/genius-patterns.md`.
2. Name Meg source anchors used for the trigger model.
3. Build a query plan with public web, public social listening, marketplace/review, competitor/alternative, and purchase-intent lanes.
4. Run `execution/buyer_trigger_research.py` unless source-only mode is explicitly selected.
5. If Codex web search finds stronger sources than the free local search fallback, pass those URLs with `--seed-url` or pass source-backed snippets with `--seed-finding-json` so they enter the same source ledger.
6. Confirm the output package contains:
   - `buyer_trigger_research_report.md`
   - `source_ledger.md`
   - `insight_ledger.md`
   - `evidence.json`
   - sidecar metadata
7. Read the research status:
   - `REAL`: use evidence as the current-world basis.
   - `DEGRADED`: use evidence only as research-informed hypothesis and surface the gaps.
   - `FAILED`: do not produce trends, quotes, buyer language, competitor claims, or market claims.
   - `SOURCE_ONLY`: use Meg mechanics only and say no live research was run.
8. Map each evidence item to one of Meg's six triggers.
9. Separate `Meg Source Mechanics` from `Live Evidence Used`.
10. Produce the Trigger Fit Table or mode-specific output with evidence IDs or source URLs attached.
11. Run grounding checks for substantial research-backed artifacts.

## Output

Required sections:

- Trigger Research Trace
- Research Receipt
- Source Ledger
- Insight Ledger
- Meg Mechanics Used
- Live Evidence Used
- Domain Extrapolation
- Trigger Fit Table
- Evidence Gaps / Risks

## Trigger Fit Table

| Candidate | Target Buyer | Identity Signal | Recognition Speed | Specificity | Social Currency Moment | Familiar/Twist Pair | Emotion-First Reason | Risk | Revision |
|---|---|---|---|---|---|---|---|---|---|

## Trust Rules

- No current buyer insight, trend, social-listening claim, competitor claim, marketplace claim, pricing claim, or direct quote may appear as fact without a source URL.
- Direct quotes require nearby source URL, context, and quote confidence.
- Evidence IDs are not decoration; they are the permission to make the claim.
- If the evidence package is thin, the output must say `research-informed hypothesis`.
- If the package is failed, the output must be a gap report, not a creative answer.

## Apify Guard

Apify is useful for richer public social listening, but it is never default execution.

- Preview first.
- Show monthly state, spent, remaining, estimated run cost, projected spend, per-run cap, and execution/fallback status.
- Hard-stop if monthly state is red, projected usage crosses the hard-stop threshold, or estimated run cost exceeds the per-run cap.
- If Apify falls back, continue with public URL-backed citations and label the social-listening limit.

## Quality Gate

Reject the run if:

- current claims lack URLs;
- Meg mechanics and live evidence are blended together;
- social listening is inferred without public/user-provided language;
- Apify execution is hidden or uncapped;
- a `FAILED` evidence package still produces trend/concept recommendations;
- Josh or MyBPM appears without being explicitly requested.
