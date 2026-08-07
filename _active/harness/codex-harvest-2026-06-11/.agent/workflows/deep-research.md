---
description: Deep Research
---

# /deep-research — Research Grounding System V1

Use this workflow when research will become the basis for strategy, positioning, offers, content, client recommendations, or other knowledge work where hallucinations would create bad decisions.

The stable entrypoint is:

```bash
python3 execution/research_router.py "[research question]" \
  --depth quick|standard|deep|max \
  --intent market|audience|competitor|offer|general \
  --provider auto|gemini|perplexity|web
```

## Default Routing

| Depth | Use For | Default Provider |
|---|---|---|
| `quick` | single fact checks, light sanity checks | Perplexity/web-backed |
| `standard` | content, competitor scan, source-backed context | Perplexity/web-backed |
| `deep` | strategy, avatar, market, offer, positioning | Gemini Deep Research first, Perplexity fallback |
| `max` | board-level briefs, high-stakes decisions, full context gathering | Gemini Deep Research Max first, Perplexity fallback |

## Required Output

Every run creates:

```text
research_outputs/YYYY-MM-DD-topic-slug/
  request.json
  research_plan.md
  raw/
  source_ledger.md
  final_report.md
  qa_report.md
```

## Truth Standard

- Data, market, pricing, competitor, and revenue claims need source URLs.
- Social listening quotes must be real and attributed.
- Unsupported claims must be labeled `inference` or `unverified`.
- Final reports must separate `verified`, `directional`, `inference`, and `unverified`.
- If every provider fails, return an honest unverified report instead of filling gaps with model memory.

## Health Check

Run this before relying on the system:

```bash
python3 execution/research_router.py --health
```

The health check reports provider availability, budget estimates, dependencies, and Google Drive export readiness without printing secrets.

## Google Docs Export

Markdown remains the source artifact. To export the final report as a native Google Doc:

```bash
python3 execution/research_router.py "[research question]" \
  --depth deep \
  --intent market \
  --export-drive \
  --drive-folder-id "[optional folder id]"
```

If no Drive folder id is provided, the Google Doc is created privately in the authenticated account's Drive.

## Resume Long Gemini Runs

Gemini Deep Research can take several minutes. If a run times out, use the saved interaction id:

```bash
python3 execution/research_router.py "[same research question]" \
  --depth deep \
  --provider gemini \
  --resume "[interaction id]"
```

Status files are written to `.tmp/deep-research-status/`.

## Fallback Contract

`auto` provider order:

1. Gemini for `deep` and `max`.
2. Perplexity if Gemini errors, rate-limits, times out, or budget blocks.
3. Manual web fallback if Perplexity is unavailable.

The final report must state which provider actually served the run.

