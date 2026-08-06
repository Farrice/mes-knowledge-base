# Video Studio Policy (Edit Bay) — BINDING

Goal this serves: Farrice ships credible video weekly without learning editing; the system
stays free-first and never re-litigates retired tools. Scar: creator pipelines default to
paid aggregators (Bonanno pays Higgsfield for Seedance we run fal-direct); un-governed
generation drains wallets; un-compounded corrections repeat forever.

1. **NO HIGGSFIELD** (Farrice, 2026-08-06). Retired everywhere. Generated media routes
   through `/generate` (fal-first) + `fal_budget_guard.py`. seedance-1080p stays
   HARD-BLOCKED; 720p serves B-roll/overlay scale. Photoreal people → fal people lane.
2. **Free-first B-roll ladder, ordered, mandatory**: own footage/screen recs → free stock
   (Pexels/Pixabay) → graphics-as-code → fal-generated (quoted first). Which rung served
   each beat is recorded in the cutlist.
3. **Stock provenance**: every stock download carries `license` + `source_url` in
   `manifest.jsonl`. No unlicensed footage, ever.
4. **Graphics routing**: HyperFrames = overlays on real footage + standalone graphic beats;
   Remotion = full programmatic compositions (charts/maps/caption comps — the 34-rule skill).
   Neither ported into the other. All graphics pass the design stack (front-end taste).
5. **QA loop mandatory on visual stages** (overlays/captions/graphics); rough cuts are
   spot-checked only. Loop cap: 3 iterations, then surface to Farrice (compass, not cage).
6. **Corrections compound**: no edit closes until Farrice's notes are promoted to
   `_active/farrice-brand/voice/video-style.md` § Correction Log.
7. **His voice is his own**: no voice clone, no TTS narration on published work (ruling
   2026-08-06). Zero-camera mode = his recorded VO + assembled visuals.
8. **Three formats default** (yt-169 / vert-916 / linkedin); LinkedIn always burns captions.
9. **Distribution = publish-ready packages; Farrice posts.** No auto-publish wiring.
10. **Every render manifest-indexed** (asset_index ENGINE CONTRACT) with version chain
    (`renders/vNN.mp4` + fixlists) — the audit trail is the QA loop's memory.

Front door: `skills/video-studio/SKILL.md`. Execution: `execution/edit_bay.py`,
`execution/transcribe_local.py`, `execution/video_qa.py`, `execution/broll_source.py`.
Source extraction: `extractions/brad-bonanno-edit-bay/extraction-report.md`.
