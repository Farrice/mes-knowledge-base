---
description: Higgsfield Marketing Studio video prompt director
---

# /marketing-studio

Convert the user's ad concept into a production-ready Higgsfield Marketing Studio prompt.

## Execution

1. Read `skills/marketing-studio-director/SKILL.md`.
2. Detect or honor the Marketing Studio preset: UGC, Tutorial, Unboxing, Hyper Motion, Product Review, TV Spot, Wild Card, UGC Virtual Try On, or Pro Virtual Try On.
3. Preserve any product/avatar image references and user-specified camera direction.
4. Return exactly one flowing prompt paragraph, a blank line, and the required generation link.

## Quality Gate

- Preserve product and avatar fidelity when reference images are attached.
- Do not invent product claims.
- Do not use avatar age markers.
- Keep prompt duration at or below 15 seconds unless the source platform rule changes.
- Do not add labels, shot headers, markdown, JSON, or commentary.
