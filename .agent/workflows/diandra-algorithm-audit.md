---
description: Diagnose what's suppressing LinkedIn reach through algorithm signal analysis
---

# `/diandra-algorithm-audit` — Algorithm Suppression Audit

Forensic analysis of every technical signal the 2026 LinkedIn retrieval system uses to discover, rank, and distribute content. Not a content audit — a plumbing diagnosis.

## When to Use
- Reach has dropped without obvious content quality change
- New account isn't gaining traction despite good content
- Suspect engagement pod usage is causing suppression
- Client onboarding — diagnose algorithmic health before content strategy

## Usage

```
/diandra-algorithm-audit [profile URL or paste profile + last 10 posts]
```

## What It Does

1. **Loads**: `skills/diandra-escobar-linkedin-growth/genius.md` (Patterns 13-18)
2. **Reads**: `skills/diandra-escobar-linkedin-growth/workflows/15-algorithm-suppression-audit.md`
3. **Audits 6 layers**: 5-Field Author Signal → First-50-Word Truncation → Semantic Lane Consistency → Save-Worthiness → Engagement Health → Account Leverage
4. **Produces**: Scored suppression report with root cause analysis and fix prescriptions

## Related Workflows

- `/diandra-headline-engineer` → Fix headline issues found in Layer 1
- `/diandra-first-50` → Fix truncation issues found in Layer 2
- `/diandra-semantic-lanes` → Fix lane scatter found in Layer 3
- `/diandra-save-architect` → Fix save-worthiness gaps found in Layer 4

**Execution prompts**: before producing the deliverable, check `skills/diandra-escobar-linkedin-growth/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
