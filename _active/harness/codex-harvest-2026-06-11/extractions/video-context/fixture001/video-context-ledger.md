# Video Context Ledger

| Timestamp | Type | Evidence | Source | Confidence | Notes |
|---|---|---|---|---|---|
| 00:00 | `observed_spoken` | Today I am showing how a video context ledger separates what is spoken from what is only inferred. | caption/subtitle | high |  |
| 00:00 | `observed_visual` | Frame image extracted: fixture-frame-000000.jpg | ffmpeg frame sample | medium | Observed evidence is limited to the existence of the frame image until a human or vision adapter describes it. |
| 00:18 | `observed_spoken` | The main claim is simple: transcript evidence alone is not visual evidence. | caption/subtitle | high |  |
| 00:30 | `observed_onscreen_text` | Evidence Types | fixture OCR | medium |  |
| 00:30 | `observed_visual` | Frame image extracted: fixture-frame-000030.jpg | ffmpeg frame sample | medium | Observed evidence is limited to the existence of the frame image until a human or vision adapter describes it. |
| 00:30 | `observed_visual` | A slide title is visible in the fixture note: Evidence Types. | fixture visual note | medium |  |
| 00:51 | `observed_spoken` | When frames or OCR are unavailable, the report should say that clearly. | caption/subtitle | high |  |
| unknown | `uncertain_or_unavailable` | Fixture mode: no live YouTube, ffmpeg, or OCR adapter was used. | adapter availability | high | This is an explicit limitation, not an inferred fact. |
