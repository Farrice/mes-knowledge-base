---
thread: stanton-extraction-deploy
status: ready
resume_hint: Collect PASS/FAIL/FIX on REVIEW-clean-posts.md, fold FIXes via /stanton-clamp-audit, post Receipt Arc slot 1
unfinished: 14 post verdicts pending; 4 newsjacks need VERIFY LIVE at posting; loop lines untested live
branch: main
pin: true
---

# Andrew Stanton Extraction — Forge + Deploy + Enrich (skill, /stanton-produce, 6-engine wiring, Receipt Arc)

## Purpose
- **Next session should do:** collect Farrice's PASS/FAIL/FIX verdicts on the 14 Content OS posts, fold any FIXes back through `/stanton-clamp-audit` (re-checking affected loop lines), then take the Receipt Arc launch live — post slot 1 (P1-1 magnesium) with its first-comment loop line and start the 15-min reply window.
- **Not in scope:** rebuilding or re-extracting Stanton (extraction + enrichment are COMPLETE — extend, never rebuild); rewriting post bodies wholesale (they are reviewed drafts awaiting verdicts); pushing the git branch (local commits only, no push authorized).

## Load First
- `skills/andrew-stanton-audience-engineering/OPERATORS-GUIDE.md` — the full deployment map (what fires automatically, maintenance rules, failure modes)
- `skills/andrew-stanton-audience-engineering/USER-GUIDE.md` — the leverage map (3 ways to use it, per-situation workflow table)
- `_active/linkedin-launch/content-os/launch-sequence-stanton.md` — the Receipt Arc: 14-post order, 13 paste-ready loop lines, finale bookend, watch-items
- `_active/linkedin-launch/content-os/REVIEW-clean-posts.md` — the 14 bodies awaiting PASS/FAIL/FIX
- `skills/andrew-stanton-audience-engineering/references/exemplars.md` — the eight-point Stanton-Grade Gate + exemplar bank (append on every felt PASS)

## Current State
- **Objective:** deploy Pixar-grade audience engineering across all of Farrice's content surfaces; immediate surface = the LinkedIn launch.
- **What is already done:** full extract-forge of Andrew Stanton from the Perell How I Write interview (21 `/stanton-*` workflows incl. the `/stanton-produce` conductor; agent persona; deep integration: Domain 7, Content Council seat `@andrew-stanton`, invocation card, 4 sovereign pins, all indexes); Stanton wired INSIDE 6 engines (parallax, linkedin-daily, copy-engine, autopilot, writers-room, depth layer); enrichment pass (TED-talk secondary layer `references/ted-talk-layer.md`, exemplar bank + Stanton-Grade Gate `references/exemplars.md`); USER-GUIDE v2 + OPERATORS-GUIDE; first live `/stanton-produce` run produced the Receipt Arc (finalized 8.33/10 with named rubric anchors; gate 8/8 with two live catches). Commits on `session/session-pin-formula`: ec87d6e4, 0be3ca98, 5b676c89, 709cf6521, 301b25dc2, 17d613950.
- **What is uncertain or stale:** the 14 post bodies have NO verdicts yet (posting is gated on them); 4 newsjacks (slots 5, 10, 12, 13) carry `[VERIFY LIVE]` swaps that must be re-verified near posting date; loop-line live performance is untested (why adversarial scored 8 not 9); P3-1/P3-2 are the closest change-pair — if either draws a FAIL, cut one not both.
- **Latest proof/receipt:** chain finalize trace `trace_20260713_181251_andrew-stanton-audience-engineering.json` (8.33/10, anchors named); prose 2/10 across all artifacts; Toy Story 5 credits web-VERIFIED.

## Suggested Skills / Workflows
- `/stanton-clamp-audit` — re-run on any body Farrice marks FIX, then re-read its loop line (a body change can orphan the debt its comment opens)
- `/stanton-produce` — for the NEXT launch surface (Parallax edition is the natural candidate; both launch engines would then be gate-tested)
- `/linkedin-daily` — the daily engine now runs the premise litmus + clamp automatically; use it for the distribution/commenting plan on posting days
- `/resume stanton-extraction-deploy` — to reload this thread

## Exact Next Prompt
```text
Load .agent/handoffs/LATEST.md context. I've done my PASS/FAIL/FIX pass on REVIEW-clean-posts.md — here are my verdicts: [paste]. Fold the FIXes through /stanton-clamp-audit, re-check the affected Receipt Arc loop lines, and give me the final go-package for slot 1 (P1-1 + its first comment + the 10 comment targets for the day).
```

## Acceptance Criteria
- Every FIX verdict resolved with a clamp-audited revision; affected loop lines re-verified against Gate 2 (no handed-4s)
- Slot 1 posted with its loop line; newsjack slots re-verified live before their windows
- Exemplar bank appended if any run earns a felt PASS

## Risk Notes
- Newsjack claims (FTC $53,088, ChatGPT citation behavior, 21-day study) must be re-verified at posting time, not trusted from the June/July drafts
- The git branch holds 6 unpushed Stanton commits among ~190 other dirty files from parallel session work — commit surgically, never `git add .`
- SessionEnd closeout spine may auto-fire in degraded mode; it is guarded against double-fire (docs/solutions/2026-07-07-sessionend-hook-reentry-guard.md) — do not run session_closeout_intelligence.py separately
