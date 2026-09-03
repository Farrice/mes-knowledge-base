---
thread: studio-preview-wrapper
status: ready
resume_hint: Build our Studio preview page (true 4:5 in LinkedIn/IG frames, plain comment box, Approve/Retire) per STUDIO-PREVIEW-BRIEF.md; fresh executor session, $0
branch: worktree-scrapes-routing
pin: false
---

# Handoff · studio-preview-wrapper · 2026-09-03 · status: ready (for a fresh executor session)

## What to build
Our own review page for the Scrapes carousel pool and runs: true 4:5 preview inside LinkedIn and Instagram frames, a plain comment box that writes the vendor's `comments.json`, Approve / Retire writing `manifest.json` + `styles.json`. Full brief with file shapes, page spec, tests, and hand-back: `_active/harness/scrapes-skill-systems/STUDIO-PREVIEW-BRIEF.md`.

## Why
Farrice, 2026-09-03, after reviewing the pool in the vendor Studio: not cropped to true size, no LinkedIn/Instagram preview, comment flow unusable. Approvals for the 11 templates were written straight into `manifest.json` as a workaround; `portrait-statement-cta` retired.

## Do NOT rebuild
The pool, the renderer, `scrapes_brand.py`, the door. Never edit inside `.claude/skills/*`.

## Done when
He opens the URL, sees true-ratio previews in both frames, submits a comment that lands in `comments.json` in the vendor shape, taps Approve and the manifest changes, tests green both directions, lane merged to main.
