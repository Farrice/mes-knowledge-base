---
name: "YouTube Video Context Analysis — Source-to-Skill Extraction Map"
source_prompt: born-v2
skill: youtube-video-context-analysis
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are operating the YouTube Video Context Analysis discipline at its extraction handshake: turning a completed video context package into an extraction-ready source map for `/extract` or `/extract-forge`. Use this before running either of those workflows when the source is a YouTube video. The future skill built from this map must not depend on visual assumptions the ledger did not verify.

## Input Required

- [VIDEO_CONTEXT_PACKAGE_PATH]: `extractions/video-context/<video-id>/` — must already contain `video-context-ledger.md`, `video-context-ledger.json`, `analysis.md`, and `uncertainty-report.md`
- [EXTRACTION_TARGET]: what is being built from this source — a skill, a research finding, a strategy brief, content, or a creative reference
- [SOURCE_MAP_REFERENCE]: the Video Context Source Map (source classes and downstream routing table)

## Execution Protocol

1. **Route by source class**, per the Video Context Source Map:
   - **Spoken evidence** (from `observed_spoken` rows) → can support claims, frameworks, examples, quotes, content hooks.
   - **Frame evidence** (from `observed_visual` rows, only when actually reviewed) → can support visual proof, demo steps, setting, composition, product state.
   - **OCR evidence** (from `observed_onscreen_text` rows) → can support slide titles, UI labels, chart labels, claims shown on screen.
   - **Inferred context** (from `inferred_context` rows) → can support hypotheses, strategy reads, creative interpretation — never presented as fact the video proved.
   - **Uncertainty** (from `uncertain_or_unavailable` rows) → becomes limitations and follow-up tasks, not silently dropped.
2. **Pull claims, frameworks, and phrasing from `observed_spoken` rows only.** These are safe to quote or paraphrase into the extraction target as the speaker's own words/ideas.
3. **Pull demos, slides, settings, edits, and product state from `observed_visual` rows only when they were actually reviewed.** If a demo step matters to the extraction target but the frame was never reviewed, flag it as a gap rather than describing the step from inference.
4. **Pull slide titles, UI labels, charts, and shown claims from `observed_onscreen_text` rows.** These are often the most reusable detail for tutorial or framework extraction (Hidden Knowledge: OCR Is Often The Bridge For Tutorials).
5. **Preserve `uncertain_or_unavailable` rows in the extraction notes**, not just the source ledger. The person or workflow running `/extract` or `/extract-forge` next needs to see what was never verified, so they don't build on a gap unknowingly.
6. **Do not let `inferred_context` rows pose as verified source material.** If an inference is genuinely useful (a strategic read, a pattern), label it as inference in the extraction map, not as something the video demonstrated.
7. **Name the run order** so the handoff is unambiguous: full visual context ledger first, extraction second.

## Output Contract

- An extraction-ready source map document that routes each relevant ledger row to its correct extraction use (claims/frameworks/phrasing, demo/visual proof, on-screen claims, inference-labeled hypotheses, and carried-forward limitations).
- Explicit run-order instructions for the downstream `/extract` or `/extract-forge` call.
- A carried-forward limitations section so no unverified visual assumption becomes silent skill material.

## Output Skeleton

```
# Source-to-Skill Extraction Map — [video title / id]

## Run Order
1. /video-context-ledger [YOUTUBE_URL]
2. /extract-forge extractions/video-context/[video-id]/video-context-ledger.md

## Claims, Frameworks, Phrasing (from observed_spoken)
- [row/timestamp]: [what it supports in the extraction target]

## Visual Proof, Demo Steps, Product State (from observed_visual, reviewed only)
- [row/timestamp]: [what it supports]

## On-Screen Claims, Slide/UI Labels (from observed_onscreen_text)
- [row/timestamp]: [what it supports]

## Inference — Labeled, Not Verified (from inferred_context)
- [row/timestamp]: [hypothesis or strategic read — explicitly marked as not directly observed]

## Carried-Forward Limitations (from uncertain_or_unavailable)
- [row/timestamp]: [what this blocks the extraction target from claiming]
```

## Quality Gate

- Does every routed item cite the ledger row/timestamp it came from?
- Are `observed_visual` items limited to rows that were actually reviewed, with unreviewed demo steps flagged as gaps instead?
- Is every `inferred_context` item explicitly labeled as inference, never presented as source-verified?
- Are all `uncertain_or_unavailable` rows carried into the extraction notes rather than dropped at the source-map stage?
- Does the map specify run order so the handoff to `/extract` or `/extract-forge` is unambiguous?

## Deploy When

- A YouTube video is the primary source for a new skill, agent, or knowledge extraction.
- The extraction target needs to be built without silently inheriting unverified visual assumptions.
