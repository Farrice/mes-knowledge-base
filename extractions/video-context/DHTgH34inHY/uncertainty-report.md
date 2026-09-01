# Uncertainty Report — DHTgH34inHY

## Evidence Available

- Complete YouTube metadata for the 3,729-second source.
- Native English automatic captions preserved as both original VTT files and parsed into 1,574 timestamped caption cues.
- A 10,969-word reading transcript reconstructed from the rolling-caption stream.
- Seven human-inspected cue frames from 47:22 through 60:52.
- SHA-256 checksums for every frozen package file in `manifest.json`.

## Evidence Classification

- `observed_spoken`: words present in the native caption stream. This verifies what the source states, not whether the statement is externally true.
- `observed_visual`: only what is visible in an inspected frame.
- `inferred`: a build or behavior conclusion synthesized from several source rows and explicitly labeled.
- `uncertain_or_unavailable`: attribution, external truth, or visual proof that this package cannot establish.

## Evidence Limits

1. Automatic captions may contain punctuation, homophone, name, and speaker-turn errors. The captions render Donella Meadows as “Danella Meadows”; the analysis uses the independently well-established spelling only as a normalization, not as a new claim from the captions.
2. Caption cues do not reliably encode who is speaking. Claims used in the build were context-reviewed, but the row-level ledger retains `UNRESOLVED_FROM_CAPTIONS` instead of inventing diarization.
3. The seven frames establish the interview format near the AI-system discussion and closing sequence. They do not constitute a complete frame crawl and cannot prove that no graphic appears elsewhere.
4. No slide, application UI, code, diagram, or procedural demonstration is visible in the inspected frames. Therefore the extracted mechanics are transcript-led.
5. Anecdotes, company histories, sales figures, publication counts, time-saving claims, and other numerical claims are **verified as stated in the interview only** unless a separate source is named. No independent fact-check was performed for this build.
6. The source is one interview. Its operating ideas are candidates for applied practice, not evidence that they cause commercial or creative outcomes.

## Use Boundary

Use the source to ground the human-project/AI-task distinction, system-gap inquiry, inexpensive iteration, proud-artifact standard, and traction loop. Do not present this package as proof of universal AI productivity, business success, Godin authorship of every captioned sentence, or production effectiveness of the new workflow.

