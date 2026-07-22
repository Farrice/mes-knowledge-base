---
description: Topic lane selection + 90-day commitment plan for algorithmic semantic matching
---

# `/diandra-semantic-lanes` — 90-Day Semantic Lane Strategy

Designs a 90-day topical commitment strategy that gives LinkedIn's unified LLM retrieval model a clear, consistent signal about what you're an authority on. The AI has "world knowledge" — it connects related topics automatically. Your job is to go deep, not wide.

## When to Use
- Starting a new brand or content strategy from scratch
- Quarterly content strategy review
- After `/diandra-algorithm-audit` identifies topic scatter
- When reach has plateaued despite consistent posting (likely a lane problem)

## Usage

```
/diandra-semantic-lanes --profile "[what you do + who you serve]" --lanes "[current topics]"
```

## What It Does

1. **Loads**: `skills/diandra-escobar-linkedin-growth/genius.md` (Pattern 15, 13, 12)
2. **Reads**: `skills/diandra-escobar-linkedin-growth/workflows/19-semantic-lane-strategy.md`
3. **Diagnoses**: Current topic scatter with score
4. **Selects**: 2-3 optimal lanes via weighted scoring
5. **Maps**: Semantic adjacency — what the AI auto-connects
6. **Designs**: 13-week calendar with lane+bucket assignments
7. **Deploys**: Month-by-month progression (Signal → Depth → Authority)
8. **Delivers**: Anti-scatter guardrails with temptation list

## Stacks With

- `/diandra-headline-engineer` → Align headline with selected lanes
- `/diandra-content-engine` → Daily production within declared lanes
- `/diandra-algorithm-audit` → Full diagnostic before lane strategy

**Execution prompts**: before producing the deliverable, check `skills/diandra-escobar-linkedin-growth/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
