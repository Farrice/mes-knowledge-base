---
description: Audit + rewrite the first 50 words of any LinkedIn post for AI retrieval + human scroll-stop
---

# `/diandra-first-50` — First-50 Hook Rewriter

Your first ~50 words are the AI retrieval system's audition. This workflow audits those 50 words for semantic signal, rewrites them to serve both the AI and the human reader, and reassembles the full post.

## When to Use
- Before publishing any LinkedIn post (final quality gate)
- When a post underperformed and the hook might be the culprit
- Batch processing multiple posts for AI optimization
- After body-first writing (Pattern 6) — this is the LAST step

## Usage

```
/diandra-first-50 "[paste full post text]" --lane "[topic lane]"
/diandra-first-50 --batch [paste 3-5 posts]
```

## What It Does

1. **Loads**: `skills/diandra-escobar-linkedin-growth/genius.md` (Pattern 14, 6, 15)
2. **Reads**: `skills/diandra-escobar-linkedin-growth/workflows/17-first-50-hook-rewriter.md`
3. **Extracts**: First 50 words, isolated
4. **Dual audits**: AI semantic signal + human scroll-stop
5. **Classifies**: Failure mode (throat-clearing, story without context, etc.)
6. **Produces**: 3 rewrite candidates, scored on both dimensions
7. **Delivers**: Winning rewrite integrated into the full post
