# Research Grounding System V1
## Purpose

This is the reliable research entrypoint for Codex Antigravity knowledge work.

Use it when a strategy, offer, content plan, market argument, ICP, or client recommendation needs current evidence instead of model memory.

## Main Command

```bash
python3 execution/research_router.py "your research question" \
  --depth quick|standard|deep|max \
  --intent market|audience|competitor|offer|general \
  --provider auto
```

Recommended default:

```bash
python3 execution/research_router.py "Validate this market and buyer strategy" \
  --depth deep \
  --intent market \
  --provider auto
```

## Depth Guide

| Depth | Use When | Default Behavior |
|---|---|---|
| `quick` | You need a fast source-backed check. | Cheap web-backed research. |
| `standard` | You need enough context for content, briefs, or light decisions. | Cited research plus quality gate. |
| `deep` | The output will shape strategy, positioning, audience, offer, or client recommendations. | Gemini Deep Research first, Perplexity fallback. |
| `max` | The decision is high-stakes and needs maximum context. | Gemini Deep Research Max first, Perplexity fallback. |

## Intent Guide

Use:

- `market` for market validation, pricing, channels, category, demand.
- `audience` for ICP, social listening, buyer psychology, language.
- `competitor` for positioning, pricing, market gaps, alternatives.
- `offer` for value perception, pricing, proof, objections, conversion.
- `general` when none of the above is clearly right.

## Output Folder

Each run creates:

```text
research_outputs/YYYY-MM-DD-topic-slug/
  request.json
  research_plan.md
  raw/
  source_ledger.md
  final_report.md
  qa_report.md
```

Use `final_report.md` for synthesis. Use `source_ledger.md` to audit what the system actually found.

## Truth Rules

- Market, pricing, revenue, competitor, and data claims need URLs.
- Social listening quotes must be real and attributed.
- If something is not source-backed, label it `inference` or `unverified`.
- Do not turn a directional signal into a proven claim.
- If tools fail, say they failed. Do not fill gaps from memory.

## Health Check

Run:

```bash
python3 execution/research_router.py --health
```

This checks dependencies, provider keys, budget estimates, and Drive export readiness without printing secrets.

## Google Docs Export

Keep markdown as the source of truth. Export only final reports:

```bash
python3 execution/research_router.py "question" \
  --depth deep \
  --intent market \
  --export-drive \
  --drive-folder-id "optional-folder-id"
```

## Long Gemini Runs

Gemini Deep Research can run for several minutes. If it times out, use the interaction id printed by the run or saved in `.tmp/deep-research-status/`:

```bash
python3 execution/research_router.py "same question" \
  --depth deep \
  --provider gemini \
  --resume "interaction-id"
```

