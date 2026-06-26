---
description: Operator Coach 3 Next Prompts for post-output next steps, recommendations, go with your verdict, extraction output closeouts, completed work closeouts, ideas, missing pieces, and what to ask next
---

# /steering-compass - Co-Creative Steering Compass

Use this when the user asks what they are missing, what to do next, how to steer the system, how to turn completed work into momentum, wants the always-on Operator Lesson expanded, asks for contextual continuation prompts, or says a fast approval phrase like "go with your verdict."

## Steps

1. Read `semantic_libraries/antigravity/primitives/high-floor-operator-os.md`.
2. Read `semantic_libraries/antigravity/primitives/collaborative-steering-compass.md`.
3. Read `semantic_libraries/antigravity/references/no-lazy-path-gate.md`.
4. Read `semantic_libraries/antigravity/primitive-map.md`.
5. Read `semantic_libraries/antigravity/references/frontier-followup-patterns.md`.
6. Use `execution/contextual_next_prompts.py` for deterministic closeout or execute-next rendering when a local helper is appropriate.
7. Return kickoff, midpoint, closeout, ad hoc steering, or Operator Lesson guidance depending on the current session stage.
8. For Standard/Deep closeouts, return **3 Next Prompts** using the Insightful Momentum standard: Use Now, Harden, and Expand. Each prompt must include when to use it, Operator Insight, Hidden Gap/Opportunity, Capability Revealed, a copy-paste prompt, expected output, quality bar, skip condition, and suggested skills/workflows.

## Rule

Do not use the full compass for tiny answers; use the micro Operator Lesson instead. Use the full Insightful Momentum 3 Next Prompts format for builds, strategy, extraction, client work, workflow changes, system design, major decisions, or user learning moments.

The prompts should teach the move behind the move. They must expose one practical unknown unknown, reveal a specific Codex capability or route, and push toward a more remarkable outcome when the work has creative, strategic, system, or client stakes.

Use frontier follow-up patterns as the ceiling: preserve thread context like a
research assistant, suggest concrete output families like an agentic workspace,
bridge real information gaps, and avoid engagement-bait suggestions that do not
earn their slot.

Fast-flow approval phrases such as "go with your verdict," "use your recommendation," "run with that," and "do the next step" mean continue the recommended safe path when the route is clear. Do not answer those phrases with more prompts unless the next step is risky, external, destructive, paid, global, or genuinely ambiguous.

## Helper

Use the deterministic helper when a local status/receipt-grounded closeout prompt set is useful:

```bash
python3 execution/contextual_next_prompts.py --objective "[current objective]"
```

Use the execution helper when the user wants the next safe action rather than coaching:

```bash
python3 execution/contextual_next_prompts.py --stage execute-next --objective "[current objective]"
```
