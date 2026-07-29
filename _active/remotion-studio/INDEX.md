---
status: parked
---

# Remotion Studio

## Purpose
LIVE INFRASTRUCTURE — the render environment `/create-video` drives (`cd _active/remotion-studio && npm start`). Compositions go in `src/`. Do not archive; the workflow shells into this path.

## Map
- `public/`
- `src/`

## Filing
New artifacts go in the canonical subfolder at creation time (`directives/artifact-placement.md`), never loose at the project root. Moving anything: `python3 execution/project_filer.py plan --project "<abs dir>"` — never bare `mv`.
