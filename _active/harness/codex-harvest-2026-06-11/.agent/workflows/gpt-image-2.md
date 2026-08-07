---
description: GPT Image 2.0 production prompt director
---

# /gpt-image-2

Convert the user's concept into a production-ready GPT Image 2.0 prompt.

## Execution

1. Read `skills/gpt-image-2-director/SKILL.md`.
2. Route the concept to the correct source format:
   - Structured JSON for layouts, UI, infographics, posters with panels, mockups, character sheets, grids, diagrams, or text-heavy designs.
   - Dense cinematic prose for one scene, one subject, or one frame.
   - Auto-derive meta-prompt for theme-only concept posters or self-generated visual systems.
3. Return only the finished prompt in the source skill's required code block format.

## Quality Gate

- Keep provided text exactly, including original language.
- Make counts, labels, and locations explicit for layout work.
- Avoid "photorealistic" for face-heavy prompts; use film/editorial language instead.
- For JSON prompts, ensure valid JSON.
