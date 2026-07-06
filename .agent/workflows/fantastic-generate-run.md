---
description: Cost-gated generation runbook — budget pre-flight + exact commands, draft-cheap then promote the winner. Never auto-fires paid APIs
---

# /fantastic-generate-run

> Cost-gated generation runbook — budget pre-flight + exact commands, draft-cheap then promote the winner. Never auto-fires paid APIs.

## Quick Deploy

```
Load: skills/fantastic-posters/genius.md
Execute: skills/fantastic-posters/workflows/06-generate-run.md
```

## Usage

```
/fantastic-generate-run [brief, asset path, or a /satori-design-think Production Brief]
```

## When to Use

When compiled prompts are ready and you (Farrice) approve spend at the cost gate.

## Cost & Safety

This is the thinking/plan layer. Any paid generation is **cost-gated and human-triggered**
(`python3 execution/cost_gate.py check --service <id>` → approve → run). Never auto-fired.
seedance-1080p is hard-blocked.

## Related Workflows

Studio stages: `/fantastic-studio` · `/fantastic-reference-ground` · `/fantastic-art-direct` · `/fantastic-divergence` · `/fantastic-model-route` · `/fantastic-prompt-compile` · `/fantastic-generate-run` · `/fantastic-critique-refine` · `/fantastic-format-pack`
Composes the design brain: `/satori-design-think` · `/satori-concept` · `/satori-color` · `/satori-lift-audit` · `/satori-anti-ai-slop`
Dispatcher: `execution/creative_router.py` · Full spec: skills/fantastic-posters/workflows/06-generate-run.md
