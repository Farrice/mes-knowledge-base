# YouTube Video Context Analysis: Genius Context

## How to Use This Skill (Model Calibration)

These evidence lanes are intuition primitives, not a checklist to stamp onto every output. Absorb the discipline — spoken, visual, on-screen text, inference, and uncertainty stay in separate lanes until the source map explicitly combines them — then write naturally. If the output mechanically prints "Lane 1: observed_spoken, Lane 2: observed_visual…" as prose headers outside an actual ledger table, that is the checklist failure this calibration exists to prevent. The test: would this discipline recognize this as a genuine multi-channel evidence build — or as a transcript summary wearing evidence-lane vocabulary? If it's the second, rebuild before shipping.

Specifically:
- Do NOT announce the machinery in analysis prose ("first I will separate observed evidence from inference…"). Build the ledger, then write the synthesis; let the separation show in the structure, not in narration.
- Do NOT backfill an `observed_visual` row from what the transcript implies is on screen. A sampled-but-unreviewed frame, or a video with no frame extraction at all, produces zero `observed_visual` rows — the empty lane is the honest output, not a gap to paper over.
- This discipline's texture is closer to a claims auditor than a summarizer: plain, uncertainty-forward, unafraid of saying "not verified." Polish that smooths over an unreviewed claim into confident prose is the tell-class failure — see the anti-patterns below, several of which are real production incidents, not hypotheticals.
- Every visual or on-screen-text claim needs a citable source (a frame, an OCR pass, a human note, or a configured vision adapter) — never the transcript alone, per the Core Rule this whole skill is built around.

## Core Thesis

Video understanding is multi-channel evidence work. A transcript tells what was said. Frames tell what was visually present. OCR tells what text appeared on screen. Analysis becomes trustworthy only when these streams stay separate until the source map shows how they support, contradict, or fail to verify one another.

> "Transcripts preserve the words. But ~30-50% of meaning in modern video — especially short-form, screen-recorded, or on-camera teaching — lives in the visual channel: hooks-as-cuts, B-roll patterns, on-screen text, gesture, energy, slide content, product demonstrations." — `directives/video-vision-protocol.md`, "Purpose" section (dated 2026-07-04 by file mtime).

## Evidence Lanes

1. `observed_spoken`: caption/subtitle text with timestamps.
2. `observed_visual`: frame evidence or explicit human/vision notes tied to timestamps.
3. `observed_onscreen_text`: OCR or manually verified text on screen.
4. `inferred_context`: interpretation or synthesis that is not directly observed.
5. `uncertain_or_unavailable`: missing captions, failed frames, unavailable OCR, blocked network, or ambiguous evidence.

The wrapper that feeds this pipeline enforces a hard 600-second (10-minute) duration cap by default — `DEFAULT_MAX_DURATION_SEC = 600` in `execution/fetch-video-context.py` — so any video past that length falls straight to `uncertain_or_unavailable` for the visual/OCR lanes unless the cap is explicitly overridden with `--max-duration`.

## Signature Moves

- **Ledger Before Summary**: build the evidence table before writing the executive summary.
- **Visual Humility**: if no frame or OCR was captured, say what could not be verified instead of guessing.
- **Timestamp Anchoring**: every claim worth reusing should point back to a time range.
- **Cross-Channel Contradiction Scan**: compare spoken claims against slides, demos, charts, settings, and on-screen text.
- **Extraction-Ready Source Map**: convert the ledger into a downstream input for `/extract`, `/extract-forge`, research, creative reference, or content workflows.

`execution/fetch-video-context.py` hard-codes 18 recognized video hosts (`KNOWN_VIDEO_HOSTS`, e.g. `youtube.com`, `tiktok.com`, `vimeo.com`, `loom.com`) for fast-path detection and falls through to a `yt-dlp --simulate` probe for anything else — the source-class judgment call itself is deterministic, not inferred by the model.

## Anti-Patterns

- Collapsing a spoken aside like "as you can see here" into an `observed_visual` row instead of logging it as `uncertain_or_unavailable` — named verbatim as an Anti-Pattern in `references/prompts-v2/full-visual-context-ledger.md` (forged 2026-07-13): "collapsing 'the speaker probably showed X' into an observed visual row."
- Citing a thumbnail, title, or video description as proof of what appeared inside the video — flagged the same way in `references/prompts-v2/frame-ledger.md` (2026-07-13): "treating thumbnails, titles, or video descriptions as proof of in-video evidence."
- Preserving row-shaped ledger evidence without ever reconstructing a clean, readable transcript surface — the exact failure class the ~2026-06-30 repair fixed (per `execution/video_context_ledger.py` and `execution/verify_video_context_source_package.py` mtimes), documented in `_active/harness/codex-harvest-2026-06-11/_active/extraction-engine-drift-audit/04-deliverables/EXTRACTION_ENGINE_DRIFT_AUDIT_PLAN.md`: "YouTube captions were preserved as row-shaped ledger evidence but not reconstructed into a clean transcript surface."
- Marking a source package's proof column "present" while the underlying fetch had already failed — the real case of `extractions/video-context/Zc4E_K48v48` (linked to the `attention-hijack-hooks` A-tier capability), verdict "quarantine from arsenal," logged in `may-june-extraction-integrity-ledger.md` across the 2026-05-01 to 2026-06-11 audit window.
- Depending on the assistant to remember invoking `/watch` manually instead of the deterministic wrapper — the exact banned pattern dated 2026-05-03 in `feedback_ai-memory-dependent-observability.md`, which is the whole reason `execution/fetch-video-context.py` exists as a `// turbo` call instead of a slash command.
- Letting a video source get over-triaged into a conceptual template instead of having its source mechanics preserved — named as an open audit risk to check for in `EXTRACTION_ENGINE_DRIFT_AUDIT_PLAN.md`'s Audit Goals (harvested 2026-06-11), not a settled verdict but a standing failure mode to watch for on every run.

## Quality Standard

A strong output can answer five questions plainly:

- What did it hear?
- What did it see?
- What text appeared on screen?
- What did it infer?
- What could it not verify?

The rubric's own Failure Conditions section names the sharpest version of the first anti-pattern above in six words: "Claims that the system saw visuals" when frames/OCR are unavailable (`references/quality-rubric.md`, Failure Conditions).
