---
description: Verify true outliers across a creator list using baseline-relative math — views ÷ creator's own average — before any idea is borrowed
---

# Outlier Scan

"Just because a video gets 100,000 views does not mean it's an outlier." Signal = multiple of
the creator's OWN baseline, nothing else.

## Pre-Flight Gate

Load `../genius.md` → Decision Framework §3. Required: candidate videos/posts (from an
inspiration list, Social Intelligence DB batch, or a scroll session) with access to each
creator's recent output for baseline computation.

## Skill Acquisition

- `../genius.md` (Baseline Click, thumbnail attribution)
- `../references/frameworks.md` §2
- DB-backed runs: /bc-intel-bridge supplies the scraped metrics

## Execution

1. **Baseline per creator**: Median/typical views across their recent posts (exclude their own
   outliers from the average — you want the floor they normally hit).
2. **Multiple**: views ÷ baseline per candidate. Bands: <2× noise · 2-3× interesting · ≥3-5× true
   outlier ("rip it" territory) · ≥10× nuclear (also check comment clusters — what is everyone
   asking?).
3. **Platform attribution note**: On YouTube, attribute outliers to packaging (thumbnail+title)
   first — the topic is pre-isolated. On feed platforms, the first frame + first line carry more.
4. **Comment mine** (outliers only): The dominant comment question/argument is itself an idea.
5. **Route**: Each true outlier → /bc-contextualize before ANY adaptation. Flag Extract
   Candidates (pattern-rich creators) for /extract graduation.

## Content Type Adaptations

| Type | Adaptation |
|------|-----------|
| YouTube | Packaging attribution; harvest thumbnail+title as the idea unit |
| IG/TikTok | Baseline from same content type (reels vs carousels differ) |
| LinkedIn | Baseline = typical reactions; comments weigh heavier than impressions |
| Social Intelligence DB | Batch metrics are already banked — compute multiples directly |

## Output Requirements

Outlier table: creator · candidate · baseline · multiple · verdict · attribution note · comment-
mine finding · route (contextualize / ignore / extract-candidate).
Execution prompt: references/prompts-v2/outlier-scan-report.md — honor its Output Contract.

## Quality Gate

No raw-view judgments anywhere. Baselines shown, not asserted. Every ≥3× outlier routed through
the transfer filter, never straight to production. Flops-at-scale (high views, sub-baseline)
explicitly labeled.
