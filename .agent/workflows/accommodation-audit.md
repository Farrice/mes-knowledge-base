---
description: Accommodation vs Assimilation Content Audit
---

# Accommodation vs Assimilation Content Audit

Run the McRaney Accommodation Audit quality gate.

## Steps

1. Load: `skills/david-mcraney-belief-change/genius.md`
2. Load workflow: `skills/david-mcraney-belief-change/workflows/accommodation-audit.md`
3. Execute with inputs: Content (finished piece), Intended Belief Shift, Audience (optional)
4. Produce: 7-Point Audit (Surprise, Relevance, Safety, Route Match, Metacognition, Staged Delivery, Accommodation Test), Score, Verdict, Priority Fixes
5. Finalize via chain_runner.py

**Execution prompts**: before producing the deliverable, check `skills/david-mcraney-belief-change/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
