---
thread: farrice-brand
status: active
resume_hint: Premium Minimal React library built + verified (12 components, validate clean); blocked on /design-login to create the Claude Design project and upload
branch: main
pin: false
---

# Premium Minimal → Claude Design component library

## Purpose

Turn the Premium Minimal brand package (docs + tokens + SVG/PPTX templates) into a real React component library so claude.ai/design's agent builds in Farrice's brand instead of generic components. Parallax gets the same treatment second, as a separate project — never mixed.

## Current State

**Built and locally verified** at `_active/farrice-brand/premium-minimal/library/`. 12 components in four groups — Structure (`Surface`, `Grid`, `Column`, `DecisionLine`), Identity (`Masthead`, `FieldIndex`), Typography (`Display`, `FunctionalLabel`, `Secondary`), Decision (`RouteSet`, `ProofBoundary`, `DarkRecommendation`). The six named in `package/02-DESIGN-CONTRACT.md` plus the primitives needed to build a page.

Proof: `package-validate.mjs` exits clean — 12/12 previews render in headless Chromium, 0 bad / 0 thin / 0 identical variants, 25 tokens defined and 20 referenced with none missing, no font warnings. All 29 preview cells graded `good` on the absolute rubric from sheets I read. Three rebuild passes. Final driver run verdict: `pendingGrade: []`, `learningsUnmerged: []`, `upload.any: true`, `deletePaths: []`.

**Blocked on authorization.** `DesignSync` returns "needs design-system authorization" — Farrice must run `/design-login`. Nothing has been uploaded; no project created yet, so `.design-sync/config.json` has no `projectId`. That is the documented safe state: the next run just re-verifies.

Two defects found by eye that every machine check passed: cells clipping at the card edge (fixed — all twelve now `cardMode: "column"`), and `Surface size="feed"` rendering its composition below the visible cell (fixed with a `maxWidth: 420` wrapper; any future `feed`/`carousel` preview needs the same).

Uncertain: only screen rendering was verified. Nothing was checked as a produced asset at native pixel dimensions — no 1584×396 export, no PPTX, no print. The `Surface` padding maths is proportional and should hold, but it is unproven against a real export.

Farrice approved one deviation: the contract's Helvetica-Neue-only rule is relaxed to its own fallback chain for browser rendering (Arial on non-Mac). Screen work only — recorded in `NOTES.md` and stated in `conventions.md`.

Local review page was served at `http://127.0.0.1:58739/.review.html` (that server dies with the session; re-serve with `node .ds-sync/storybook/http-serve.mjs ./ds-bundle`). Farrice had not yet given a verdict on the cards.

Cost to date: $0 — no paid APIs.

## Remaining Priority

Farrice runs `/design-login`; then create the Claude Design project, record `projectId` in `.design-sync/config.json` before any upload, and push via the incremental path. Parallax follows as a separate library and a separate project.

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- Previous handoff on this thread: `.agent/handoffs/2026-08-24-farrice-brand.md` — everything it lists as shipped is EXTEND-ONLY.
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
