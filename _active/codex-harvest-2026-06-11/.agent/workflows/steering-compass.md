---
description: Operator Coach 3 Next Prompts for post-output next steps, recommendations, go with your verdict, extraction output closeouts, completed work closeouts, ideas, missing pieces, and what to ask next
---

# /steering-compass - Co-Creative Steering Compass

Use this when the user asks what they are missing, what to do next, how to steer the system, how to turn completed work into momentum, wants the always-on Operator Lesson expanded, asks for contextual continuation prompts, or says a fast approval phrase like "go with your verdict."

## Steps

1. Read `semantic_libraries/antigravity/primitives/collaborative-steering-compass.md`.
2. Read `semantic_libraries/antigravity/primitive-map.md`.
3. Read and execute `skills/semantic-document-library-os/workflows/steering-compass.md`.
4. Return kickoff, midpoint, closeout, ad hoc steering, or Operator Lesson guidance depending on the current session stage.
5. For Standard/Deep closeouts, return **3 Next Prompts**: Use Now, Harden, and Expand. Each prompt must include when to use it, why it is recommended, a copy-paste prompt, expected output, quality bar, skip condition, and suggested skills/workflows.

## Rule

Do not use the full compass for tiny answers; use the micro Operator Lesson instead. Use the full 3 Next Prompts format for builds, strategy, extraction, client work, workflow changes, system design, major decisions, or user learning moments.

## Helper

Use the deterministic helper when a local status/receipt-grounded closeout prompt set is useful:

```bash
python3 execution/contextual_next_prompts.py --objective "[current objective]"
```
