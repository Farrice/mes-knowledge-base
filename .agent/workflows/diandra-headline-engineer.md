---
description: LinkedIn headline optimized for both AI retrieval matching AND human conversion
---

# `/diandra-headline-engineer` — AI-Optimized Headline Engineer

Engineers LinkedIn headlines that serve two masters: the unified Llama 3 retrieval model (decides who sees your content) and the human reader (decides whether to trust/follow/connect).

## When to Use
- Setting up or updating a LinkedIn profile
- Reach dropped and the headline may be the culprit
- Client onboarding — headline is the first fix
- After running `/diandra-algorithm-audit` and getting a low 5-Field score

## Usage

```
/diandra-headline-engineer "[current headline]" --icp "[target audience]" --lanes "[topic lanes]"
```

## What It Does

1. **Loads**: `skills/diandra-escobar-linkedin-growth/genius.md` (Pattern 13, 15, 18)
2. **Reads**: `skills/diandra-escobar-linkedin-growth/workflows/16-ai-optimized-headline-engineer.md`
3. **Diagnoses**: Current headline against dual AI + human filter
4. **Generates**: 5 headline candidates using different architectural patterns
5. **Scores**: Each on AI matching AND human conversion
6. **Delivers**: Top 2 recommendations with reasoning
