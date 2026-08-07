# YouTube Video Context Analysis: Genius Context

## Core Thesis

Video understanding is multi-channel evidence work. A transcript tells what was said. Frames tell what was visually present. OCR tells what text appeared on screen. Analysis becomes trustworthy only when these streams stay separate until the source map shows how they support, contradict, or fail to verify one another.

## Evidence Lanes

1. `observed_spoken`: caption/subtitle text with timestamps.
2. `observed_visual`: frame evidence or explicit human/vision notes tied to timestamps.
3. `observed_onscreen_text`: OCR or manually verified text on screen.
4. `inferred_context`: interpretation or synthesis that is not directly observed.
5. `uncertain_or_unavailable`: missing captions, failed frames, unavailable OCR, blocked network, or ambiguous evidence.

## Signature Moves

- **Ledger Before Summary**: build the evidence table before writing the executive summary.
- **Visual Humility**: if no frame or OCR was captured, say what could not be verified instead of guessing.
- **Timestamp Anchoring**: every claim worth reusing should point back to a time range.
- **Cross-Channel Contradiction Scan**: compare spoken claims against slides, demos, charts, settings, and on-screen text.
- **Extraction-Ready Source Map**: convert the ledger into a downstream input for `/extract`, `/extract-forge`, research, creative reference, or content workflows.

## Anti-Patterns

- Transcript-only summaries that pretend to know visuals.
- Treating thumbnails, titles, or video descriptions as proof of in-video evidence.
- Collapsing "the speaker probably showed X" into an observed visual row.
- Omitting missing-tool limitations.
- Producing a clever synthesis without a timestamped source map.

## Quality Standard

A strong output can answer five questions plainly:

- What did it hear?
- What did it see?
- What text appeared on screen?
- What did it infer?
- What could it not verify?

