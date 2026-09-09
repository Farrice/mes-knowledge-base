---
description: "/scrapes — ONE door for every Scrapes Skill System: dump raw text (a topic, a URL, a draft, a video link, 'set up my templates'), it classifies the job, locks the brand, and runs the right door (social-carousel / social-post / social-repurpose / deck-build / video-to-shorts / video-to-ebook / template pool / visual identity / brand voice / a single tool). Never posts."
---
<!-- umbrella front door for the vendored Scrapes Skill Systems (2026-09-03). Design: _active/harness/scrapes-skill-systems/ORCHESTRATION-DESIGN.md · User's guide: _active/harness/scrapes-skill-systems/USER-GUIDE.md -->

# /scrapes — raw text in, the right Scrapes pipeline out

You do not need to know the skill names. Paste what you have and, when it is not obvious, who it is for.

## Step 1 — Classify the job (deterministic table, first match wins)

| What the text carries | Door |
|---|---|
| "carousel", "slides for a post", "swipe" | `/social-carousel` |
| a finished post or short idea + "image", "instagram post", "single image" | `/social-post` |
| "repurpose", "atomize", "version for <platform>", "thread from" | `/social-repurpose` |
| "deck", "presentation", "slides for a talk" (not a readout or research brief → `/briefs`) | `/deck-build` |
| a YouTube URL or video file + "shorts", "clips", "reframe" | `/video-to-shorts` |
| a YouTube URL + "ebook", "article", "pdf", "long-form" | `/video-to-ebook` |
| "templates", "template pool", "set up carousels", "onboard my brand" | **Template pool** (Step 3) |
| "visual identity", "design tokens", "brand bible", "match this design" | `mkt-visual-identity` (Import mode from the brand's DESIGN.md when one exists; Farrice approves) |
| "brand voice", "voice profile", "sound like me/her" | `mkt-brand-voice` — Import from canon, never interview (Farrice: FARRICE-MASTER-CONTEXT + VOICE-CARD; clients: their CLAUDE.md + engine docs) |
| a single utility: "screenshot this page", "annotate", "transcribe this file", "find an image of", "excalidraw", "fact check this" | the matching `tool-*` / `viz-*` skill directly, brand lock still applies when it writes into a brand folder |
| anything else | say which door fits closest and ask ONE question; never guess a pipeline |

Publishing asks ("post this", "schedule") → stop: sends stay human. Say so in one line.

## Step 2 — BRAND LOCK (every door, no exceptions)
`python3 execution/scrapes_brand.py resolve --from-prompt "<the text>" --cwd "$PWD"`. Exit 3 → one question: "Which brand: farrice, jen, andrea?" and wait. Exit 0 → carry the `BRAND LOCK:` line into the door. Then `scrapes_brand.py check <brand> --pool <platform>-<format>` when the door renders visuals; a `blocked` render path means the template pool is missing — offer Step 3 instead of improvising.

## Step 3 — Template pool (onboarding, his approvals)
Owner: `00-social-content` onboarding Step O3.6, `.claude/skills/00-social-content/references/onboarding.md`. The wrapper adds only the brand lock and the cost line.
1. Refs: 4–6 images in `{brand_context}/visual_refs/` (the brand's own carousel frames or design-system exports). Never a competitor's frames.
2. Cost line before anything runs: `ssc-template-builder` is AI-first via GPT Image ≈ $0.17 per generated image, usually 1–3 per ref. `python3 execution/openai_budget_guard.py check --n=<refs*2>`; DENIED = stop, never retry.
3. Phase 4.95: per-ref `slug` (style-neutral, composition + role) and `role` (cover | body | cta) from a quick read of each ref. Phase 4.96 only when a ref carries an image zone.
4. Phase 5: ONE `ssc-template-builder` agent per ref, spawn contract copied byte-for-byte from onboarding.md (seven slots, fixed boilerplate; nothing about the ref's composition in the spawn). Existence check on disk after each: `template.html` + `preview.png` + `rationale.md`, else re-spawn.
5. Phase 5.2: organize + write `manifest.json` (the orchestrator is the only manifest writer). 5.5 gates. 6 brand bible v2. 6.7 launch the Template Studio (`content_studio.py {pool} --mode template`, background) and wait for his approvals. His approval = `status: approved`.
6. Log: one line under `## 00-social-content` in `context/learnings.md` (which refs built clean, which needed the ladder); `openai_budget_guard.py log` per generated image.

## Step 4 — Run the door
Read and execute the door's workflow file in `.agent/workflows/`. Every dispatch carries the brand's `brand_context` path explicitly. Cost stated before any AI call. Studio approvals are Farrice's.

## Never
Post or schedule. Edit inside `.claude/skills/*`. Run without the BRAND LOCK line. Pick a brand because it "seems obvious".
