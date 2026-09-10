# Preservation Lock — Codex Editorial Study

- **Good example:** `../same-door/` at commit `dbfa77ef3`
- **Primary failure class:** creative revision degradation
- **Keep:** the approved 22-board Calm Closer system, its exports, palette roles, factual claims, and listing-photo provenance
- **Change:** create three separate experimental boards with a materially more editorial and premium composition
- **Do not disturb:** any file under `../same-door/`
- **Risk:** producing the same system with larger type instead of a genuinely different visual thesis
- **Gate:** three boards must use a distinct layout grammar, remain readable at phone size, contain no ornamental background geometry, and render without changing the preserved folder

## Regression guard

The experiment lives only in `production/codex-editorial-study/`. Before delivery, verify that `git diff dbfa77ef3 -- ../same-door` contains no changes introduced by this study.

## Replay prompt

Repeat this class of work. Good example: `../same-door/` at `dbfa77ef3`. Preserve the complete approved system. Build experiments beside it, never over it. Change the visual thesis through composition, typography, cropping, and hierarchy. Do not ship unless the experiment is materially different, phone-readable, and regression-free.
