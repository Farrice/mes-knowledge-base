---
description: Validate raw user intent before building. Runs the 4-stage intent pipeline.
---

# Pre-Flight Intent Validation

Use this workflow when the user provides a rough, raw, or incomplete concept.

## Execute the Intent Pipeline

Read and follow `directives/intent-pipeline.md`. It runs 4 stages:

1. **SCORE** — Rate intent sharpness 1-5 (checklist: deliverable, audience, context, end state, specificity)
2. **SHARPEN** — If Score ≤ 3, run DICE on missing dimensions only (one round max)
3. **ROUTE** — Match domain → experts using detection table
4. **PRESENT** — Show expert recommendation, await confirmation

## After Pipeline Completes

Based on the refined objective:
- **Swarm-worthy** (multi-domain, 2+ perspectives) → Hand off to `/swarm` or `/parallel-swarm`
- **Single-expert** (clear domain match) → Invoke expert directly via `/deploy-skill`
- **Direct execution** (simple, clear task) → Execute immediately

Do NOT execute until the user confirms the sharpened objective and approach.

---

## When to Use
- User says "I want to build...", "Create a...", "Make me a..."
- Request is vague or lacks specifics
- Request involves a new workflow, skill, or multi-step system
- Intent Sharpness Score is 1-3

## When NOT to Use
- Clear, specific requests with all parameters (Score 4-5)
- Bug fixes or corrections
- Simple factual questions
- User says "just do it"
