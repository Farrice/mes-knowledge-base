# Provenance — Kieran Flanagan Audience Intelligence Repair

Anchor → source file + location. All quotes verified by direct `grep` against `extractions/kieran-flanagan/transcript.txt` (27,523 bytes, one physical line — no internal line breaks, so "location" is the file, not a line number) during this repair pass, 2026-07-18.

| Anchor (genius.md location) | Claim | Source | Status |
|---|---|---|---|
| Model Calibration, opening quote | "I have perfected this. This is really good. It took me 12 months to kind of go back and forth" | `extractions/kieran-flanagan/transcript.txt` | VERIFIED |
| Model Calibration, bullet 2 | "this is not like an ICP, right? This is actually content they react to and it's all based upon research and engagement data" | `extractions/kieran-flanagan/transcript.txt` | VERIFIED |
| Anti-Patterns item 1 | "first draft when you look at this, I do not use this to post content" | `extractions/kieran-flanagan/transcript.txt` | VERIFIED |
| Anti-Patterns item 2 | "So obviously I would never ship this" | `extractions/kieran-flanagan/transcript.txt` | VERIFIED |
| Anti-Patterns item 3 | "This one sucked. It was my worst performing post. People did not like a product position" | `extractions/kieran-flanagan/transcript.txt` | VERIFIED |
| Anti-Patterns item 4 | "I was never a big fan of the kind of vibe marketing where it was workflow tools because it's not vibing... This is not software" | `extractions/kieran-flanagan/transcript.txt` | VERIFIED |
| Anti-Patterns item 5 | "Firecrawl doesn't have a great time getting LinkedIn posts... you could just have to go and like export your own files to upload" | `extractions/kieran-flanagan/transcript.txt` | VERIFIED |
| Anti-Patterns item 6 | "too many people will use these cut and paste. That's not how you do that, right?" | `extractions/kieran-flanagan/transcript.txt` | VERIFIED |
| Anti-Patterns item 7 | "this is not like an ICP, right? This is actually content they react to" | `extractions/kieran-flanagan/transcript.txt` | VERIFIED (same passage as Model Calibration bullet 2) |
| Rubric row "Audience source" | Top-30% performance filtering | `extractions/kieran-flanagan/transcript.txt`: "it will look at the top 30% of your best performing posts" | VERIFIED |
| Show attribution correction (Anti-Patterns section intro) | Source show is *Marketing Against the Grain*, not "Greg Isenberg Show" as `extraction-report.md` line 4 states | `extractions/kieran-flanagan/transcript.txt`: "this episode of Marketing Against the Grain" (appears twice) vs. `extractions/kieran-flanagan/extraction-report.md` line 4 | Transcript claim VERIFIED; extraction-report.md attribution flagged UNCONFIRMED/likely mislabeled |
| Pattern 3 numeric figures (20-30 words, 50-100 words, 4x, 80%/20%, 60-80%) | Anti-vocabulary effectiveness statistics | `extractions/kieran-flanagan/extraction-report.md` Pattern 3 / Hidden Knowledge #2 (synthesis, not transcript-sourced) | UNCONFIRMED as Kieran's own words — see source-ledger.md for full explanation; left in place, not removed (additive-first) |
| Pattern 3 "Common Anti-Vocabulary Items" list | delve, tapestry, landscape, etc. | Not found in `extractions/kieran-flanagan/transcript.txt` (grepped, zero matches) | UNCONFIRMED — illustrative generic list, not Kieran-sourced |

Full claim-by-claim reasoning, including LIKELY-tier items and the gap named for future repair, is in `references/source-ledger.md`.
