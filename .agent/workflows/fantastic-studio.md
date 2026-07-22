---
description: Concept-first, multi-model, self-critiquing image pipeline — art-direct → diverge → route → generate → refine → format pack
---

# /fantastic-studio

> Concept-first, multi-model, self-critiquing image pipeline — art-direct → diverge → route → generate → refine → format pack.

## Quick Deploy

```
Load: skills/fantastic-posters/genius.md
Execute: skills/fantastic-posters/workflows/00-studio.md
```

## Usage

```
/fantastic-studio [brief, asset path, or a /satori-design-think Production Brief]
```

## When to Use

Any client-facing or brand-defining visual that must be remarkable, not just rendered. The front door to the whole Studio.

## Cost & Safety

This is the thinking/plan layer. Any paid generation is **cost-gated and human-triggered**
(`python3 execution/cost_gate.py check --service <id>` → approve → run). Never auto-fired.
seedance-1080p is hard-blocked.

## Related Workflows

Studio stages: `/fantastic-studio` · `/fantastic-reference-ground` · `/fantastic-art-direct` · `/fantastic-divergence` · `/fantastic-model-route` · `/fantastic-prompt-compile` · `/fantastic-generate-run` · `/fantastic-critique-refine` · `/fantastic-format-pack`
Composes the design brain: `/satori-design-think` · `/satori-concept` · `/satori-color` · `/satori-lift-audit` · `/satori-anti-ai-slop`
Dispatcher: `execution/creative_router.py` · Full spec: skills/fantastic-posters/workflows/00-studio.md

**Execution prompts**: before producing the deliverable, check `skills/fantastic-posters/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
