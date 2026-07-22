---
description: "Hot launcher for Meg Heckman's source-traced and research-backed buyer-trigger OS"
---

# /buyer-trigger-os

Run the Meg Heckman Buyer-Trigger OS from a cold start without losing source grounding or current evidence grounding.

This is a thin launcher, not a replacement for the full skill. It must load `skills/meg-heckman-buyer-trigger-os/SKILL.md`, follow its Source-Trace Default, and use exactly one workflow mode. When current buyer insights, trends, social listening, purchase intent, or market evidence are requested, it must run the Research-Trace Default before producing recommendations.

## Usage

```text
/buyer-trigger-os audit [product, offer, page, ad, or concept]
/buyer-trigger-os generate [niche, product type, tone, and constraints]
/buyer-trigger-os score [candidate list]
/buyer-trigger-os transfer [non-apparel offer, landing page, client creative, or product]
/buyer-trigger-os research [niche, product, offer, market, or buyer community]

/buyer-trigger-os generate --research [niche or product]
/buyer-trigger-os audit --research [product, page, offer, or concept]
/buyer-trigger-os score --research [candidate list]
/buyer-trigger-os transfer --research [non-apparel offer or page]
/buyer-trigger-os [mode] --source-only [Meg/source-only run; no live research]
```

## Modes

| Mode | Workflow |
|---|---|
| `audit` | `skills/meg-heckman-buyer-trigger-os/workflows/buyer-trigger-audit.md` |
| `generate` | `skills/meg-heckman-buyer-trigger-os/workflows/apparel-concept-generator.md` |
| `score` | `skills/meg-heckman-buyer-trigger-os/workflows/product-design-scoring.md` |
| `transfer` | `skills/meg-heckman-buyer-trigger-os/workflows/cross-vertical-transfer.md` |
| `research` | `skills/meg-heckman-buyer-trigger-os/workflows/research-backed-trigger-run.md` |

## Source-Trace Default

Before producing a meaningful output:

1. Load `skills/meg-heckman-buyer-trigger-os/references/source-ledger.md`.
2. Load `skills/meg-heckman-buyer-trigger-os/references/genius-patterns.md`.
3. Name the timestamp anchors used from `extractions/video-context/7MNa2YTPGs4/video-context-ledger.md`.
4. Separate `Source Mechanics` from `Domain Extrapolation`.
5. Use the Trigger Fit Table unless the user asks for a different shape.
6. Mark revenue/margin claims as source claims only.
7. Do not claim visual evidence unless frame/OCR evidence has been reviewed.

## Research-Trace Default

Use this when the request includes `research`, `--research`, current buyer insights, trends, social listening, purchase intent research, market evidence, live buyer language, competitor signals, or any claim that depends on the current outside world.

1. Keep Meg's source mechanics and live evidence separate.
2. Run the default public/free lane through `python3 execution/buyer_trigger_research.py "[topic]" --mode [research|audit|generate|score|transfer]`.
3. Do not call `execution/research_router.py --provider auto` for the default lane because it can invoke paid providers.
4. Public social listening is part of the default research lane through URL-backed public web sources.
5. If Codex web search finds stronger public sources, pass them into the runner with `--seed-url` or `--seed-finding-json` so the evidence still lands in the same ledger.
6. Apify is preview-only unless the user explicitly asks to use Apify or the run passes `--apify execute`; even then it must honor the budget guard and per-run cap.
7. If the runner returns `DEGRADED`, label the output as research-informed and keep validation gaps visible.
8. If the runner returns `FAILED`, do not invent trends, quotes, buyer language, or market claims. Produce the gap report and ask for source material or approval for deeper research.

The runner writes:

- `buyer_trigger_research_report.md`
- `source_ledger.md`
- `insight_ledger.md`
- `evidence.json`
- sidecar metadata

## Example Loading Rule

Josh and MyBPM are proof examples, not templates. Load those project files only when the user explicitly mentions Josh, MyBPM, or asks for examples.

## Output Minimum

- Intent interpreted.
- Mode chosen.
- Source anchors used.
- Trigger Research Trace when research is requested.
- Research Receipt when research is requested.
- Source Ledger and Insight Ledger when research is requested.
- Source mechanics.
- Live evidence used when research is requested.
- Domain extrapolation.
- Trigger Fit Table or selected workflow output.
- Weakest trigger and concrete revision.
- Remaining risk or live-buyer proof needed.

## Trust Rules

- No trend, buyer-language, social-listening, competitor, pricing, or market claim may appear as fact without a source URL.
- Direct quotes require a nearby source URL and quote confidence.
- Source mechanics from Meg are not the same thing as live market evidence.
- Paid/quota tools, authenticated scraping, browser automation, connector writes, external publishing, global mirrors, and real Codex subagents require explicit approval.

**Execution prompts**: before producing the deliverable, check `skills/meg-heckman-buyer-trigger-os/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
