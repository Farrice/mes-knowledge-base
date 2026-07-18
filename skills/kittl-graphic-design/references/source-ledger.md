# Kittl Graphic Design — Source Ledger

Claim-by-claim provenance for `genius.md` and `SKILL.md`. Labels: **VERIFIED** (verbatim or near-verbatim match against a source file, quote checked), **LIKELY** (grounded in a source file but paraphrased/synthesized, or reflects a single presenter's practice rather than official platform documentation), **UNCONFIRMED** (no source file locates this — flagged, not silently dropped).

This is a TOOL skill (Kittl, a commercial design platform). There is no single named human expert to fact-check against a biography; provenance here means "did this come from actual extraction material," not "is this externally famous."

## Primary Sources (read in full for this repair)

1. `knowledge/extractions/inbox/Claude-👨🏽_🎨💎💎 Kittl ! Graphic Design Mastery.md` (250,951 bytes) — the original MES 3.0 extraction chat. Created 1/10/2026, exported 1/22/2026. Built from three unnamed Kittl YouTube video transcripts (titles given in-chat: "How To Pair Fonts With Imagery Based On Aesthetic & Emotion," "Trending Typography Composition Tips," "Use This Prompt Cheat Sheet To Make Better AI Images"). The raw video transcripts themselves were NOT preserved in the export (the chat's three `File:` attachments show empty content) — so Patterns/Tacit knowledge trace to this Claude-authored extraction of the transcripts, not to the original video audio.
2. `extractions/creative-direction/kittl_notes.md` (2,038 bytes), `kittl_flows_advanced.md` (3,419 bytes), `kittl_video_nodes.md` (1,653 bytes) — a later, separate research pass on Kittl's platform UI/features, added to the repo 2026-04-14 (commit `ae3591dad`). These describe the live product (AI models, Kittl Flows, Kittl Video), independent of the Patterns/Tacit extraction above.

## Claims

| Claim | Label | Source |
|---|---|---|
| Patterns 1–18 (Mood-First Font Selection through Emotional Design Vocabulary) — execute steps + success metrics | VERIFIED | Matches `### Pattern N` sections in source #1, lines 130–336 (verbatim core language; genius.md trims "Deployment Context" field and tightens wording, no substantive change) |
| Tacit 1–8 (90s Serif Secret through Edit Prompts ≠ Generation Prompts) | VERIFIED | Matches `### Tacit Knowledge N` sections in source #1, lines 396–418 (near-verbatim) |
| Presenter is named "Graham," host/designer for Kittl | LIKELY | Stated in source #1 line 43 ("the presenter is someone named Graham") and line 62 — this is the extraction chat's own claim about the video content; not independently corroborated against a public Kittl creator credit, so treated as LIKELY rather than VERIFIED |
| Hall of Fame Exemplars ("Everbloom Botanicals," "Apex Ascent," "Cosmic Bloom") and the Anti-Exemplar ("Tech Solutions Inc.") | LIKELY | Illustrative compositions synthesized in genius.md to demonstrate the patterns in combination — not literal Kittl case studies from source #1, which contains its own separate (different) example outputs for its Crown Jewel prompts. Treat as instructional fiction grounded in the real patterns, not as real client work |
| Expert-Specific Quality Rubric (4/7/10 anchors) | LIKELY | Synthesized scoring rubric derived from the Patterns/Tacits above; not a verbatim rubric from source #1 |
| "4 Building Blocks of a Good Prompt (Official Kittl Guide)" — 5 Ws, adjectives, output style, negatives | VERIFIED | `extractions/creative-direction/kittl_notes.md` lines 19–43, verbatim structure and near-verbatim bullet text |
| Kittl Flows / Smartboards / AI Image Boards pipeline mechanics | VERIFIED | `extractions/creative-direction/kittl_flows_advanced.md` lines 3–37 |
| "34 Design Hacks" list | UNCONFIRMED past item 20 | `extractions/creative-direction/kittl_flows_advanced.md` header claims 34 hacks but only 20 are enumerated (lines 45–65) — hacks 21–34 are NOT in the source file. Do not cite hack numbers above 20 as sourced |
| Kittl Video launch Feb 3, 2026; AI Video Boards; modular CAMERA/ACTION/AUDIO/TEXT prompt structure | VERIFIED | `extractions/creative-direction/kittl_video_nodes.md` lines 1–34, verbatim dates and bullet text |
| AI model roster + specs (Nano Banana Pro, Seedream 4, Veo 3.1, Kling 3.0, token/sec figures, duration ranges) | LIKELY | `extractions/creative-direction/kittl_video_nodes.md` lines 18–25 and `kittl_flows_advanced.md` lines 67–76 — reflects the platform's model lineup at the time of this research pass (2026-04-14); fast-moving product surface, not re-verified live for this repair |
| "23 unconscious mastery behaviors" / "23 deterministic practitioner prompts" framing | LIKELY | Source #1 line 65 claims 23 patterns; genius.md/SKILL.md compress to 18 patterns + 8 tacits actually written out. The "23" figure in SKILL.md's execution-prompts count refers to the prompt files in `references/prompts-v2/`, a distinct count from the pattern count — not the same 23 |

## Absence Check (Rule 2 — an absence claim is itself a provenance claim)

Before labeling anything UNCONFIRMED, the following were opened and read in full: `extractions/creative-direction/kittl_notes.md` (2,038 bytes, non-empty, fully read), `kittl_flows_advanced.md` (3,419 bytes, non-empty, fully read), `kittl_video_nodes.md` (1,653 bytes, non-empty, fully read), and the first 1,323 lines of `knowledge/extractions/inbox/Claude-👨🏽_🎨💎💎 Kittl ! Graphic Design Mastery.md` (250,951 bytes total — the Patterns/Tacit sections needed for this repair fall in lines 130–418 and were confirmed present; the remaining ~4,900 lines are the Crown Jewel prompt bodies, not re-read in full for this repair since they don't back any claim touched here). No file was assumed empty or unrecoverable without an actual read.
