---
description: Turn a brief (or a /satori-design-think Production Brief) into a rich art-direction spec — concept, hierarchy, color hex, feeling, memory hook, anti-slop
---

# /fantastic-art-direct

> Turn a brief (or a /satori-design-think Production Brief) into a rich art-direction spec — concept, hierarchy, color hex, feeling, memory hook, anti-slop.

## Quick Deploy

```
Load: skills/fantastic-posters/genius.md
Execute: skills/fantastic-posters/workflows/02-art-direct.md
```

## Usage

```
/fantastic-art-direct [brief, asset path, or a /satori-design-think Production Brief]
```

## When to Use

Before generating anything that must carry a real idea. Ingests the satori brain; kills generic-template output.

## Cost & Safety

This is the thinking/plan layer. Any paid generation is **cost-gated and human-triggered**
(`python3 execution/cost_gate.py check --service <id>` → approve → run). Never auto-fired.
seedance-1080p is hard-blocked.

## Related Workflows

Studio stages: `/fantastic-studio` · `/fantastic-reference-ground` · `/fantastic-art-direct` · `/fantastic-divergence` · `/fantastic-model-route` · `/fantastic-prompt-compile` · `/fantastic-generate-run` · `/fantastic-critique-refine` · `/fantastic-format-pack`
Composes the design brain: `/satori-design-think` · `/satori-concept` · `/satori-color` · `/satori-lift-audit` · `/satori-anti-ai-slop`
Dispatcher: `execution/creative_router.py` · Full spec: skills/fantastic-posters/workflows/02-art-direct.md

**Execution prompts**: before producing the deliverable, check `skills/fantastic-posters/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
