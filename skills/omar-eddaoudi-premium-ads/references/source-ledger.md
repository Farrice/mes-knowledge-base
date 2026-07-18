# Source Ledger — Omar Eddaoudi: Premium Ads Mastery

Every source consulted for the Wave 3 repair pass, labeled VERIFIED / LIKELY / UNCONFIRMED per claim used in `genius.md`. Ground truth = `extractions/omar-eddaoudi/` (repo root). File sizes recorded per the batch's source-search discipline.

## Source Files

| File | Size | Speaker Confirmation | Confidence |
|---|---|---|---|
| `extractions/omar-eddaoudi/transcript.txt` | 12,702 bytes | No self-identification found in-file (0 hits on "Omar"); `extraction-report.md` at this level labels the expert generically as "luxury-branding (Strategic Brand Analyst)," not "Omar Eddaoudi" by name. | LIKELY (thematically consistent with the skill's premium-positioning content and stored under this expert's extraction folder, but the speaker is not named on-camera in this file) |
| `extractions/omar-eddaoudi/extraction-report.md` | 6,491 bytes | Synthesis of `transcript.txt` above | LIKELY (inherits transcript.txt's confidence) |
| `extractions/omar-eddaoudi/module_2/module_2_transcript.txt` | 64,251 bytes | Confirmed: "If you're new to the channel, my name is Omar. I'm the founder at Orow Labs." | VERIFIED |
| `extractions/omar-eddaoudi/module_2/extraction-report.md` | 7,620 bytes | Synthesis of module_2_transcript.txt above | VERIFIED (synthesis quality LIKELY, source speaker VERIFIED) |
| `extractions/omar-eddaoudi/module_3/01_zero_to_seven_figures.txt` | 30,840 bytes | First-person operator voice ("I've scaled multiple brands... this is the exact process that I use"), same channel/style as module_2, no name-check found in this specific file | LIKELY |
| `extractions/omar-eddaoudi/module_3/02_wellness_ad_teardown.txt` | 11,561 bytes | Same channel/style as module_3/01, no explicit name-check in this file | LIKELY |
| `extractions/omar-eddaoudi/module_3/03_static_ad_design_principles.txt` | 16,472 bytes | Same channel/style as module_3/01, no explicit name-check in this file | LIKELY |

## Claims Used in genius.md

| Claim / Quote | Source | Label |
|---|---|---|
| "If you're new to the channel, my name is Omar. I'm the founder at Orow Labs." | module_2_transcript.txt | VERIFIED — verbatim, self-identification |
| "you need to avoid overselling the features because those are commodities honestly" | module_2_transcript.txt | VERIFIED — verbatim |
| "In practicality, you don't want to be competing with people's standards" | module_2_transcript.txt | VERIFIED — verbatim |
| "you don't own a [Patek], you merely look after it for the next generation" (source ASR renders the brand name "Pek Philippe"/"PEX") | module_2_transcript.txt | LIKELY — the sentiment and slogan structure are verbatim in-source; "Patek Philippe" as the intended brand name is an inference from the garbled ASR transcription, not a clean text match. Flagged, not silently corrected. |
| "I don't want my customers to hit my website and have like 26 different objections" | module_3/01_zero_to_seven_figures.txt | VERIFIED — verbatim |
| "they don't enrich it, they don't analyze it, and they don't extract anything meaningful from it" | module_3/01_zero_to_seven_figures.txt | VERIFIED — verbatim |
| "The brands that fail don't fail because they have a bad product, they usually fail because they don't have these fundamentals in place" | module_3/01_zero_to_seven_figures.txt | VERIFIED — verbatim |
| "helped get to 83k a month... from 3k a month" / AOV "at least $60 on the front end" | module_3/01_zero_to_seven_figures.txt | VERIFIED — verbatim figures |
| "first ad that we're going to be analyzing is an ad from Whoop... they use a principle called semantic reversal" | module_3/02_wellness_ad_teardown.txt | VERIFIED — verbatim |
| Value Inversion / Controlled Distance / Archetypal Mirroring pattern definitions | module_1 `extraction-report.md` (synthesis of `transcript.txt`) | LIKELY — synthesis is internally consistent and matches the skill's theme, but rests on a speaker-confidence gap noted above |
| Narrative Hegemony / Mirror-Bridge Identity / Objection-First Creative / LLM Retrieval Optimization pattern definitions | module_2 `extraction-report.md` (synthesis of module_2_transcript.txt) | VERIFIED for the underlying source speaker; synthesis wording is LIKELY (a compiled distillation, not a direct quote) |
| "Reddit and Trustpilot" as sentiment/retrieval signal | module_2 `extraction-report.md` | LIKELY — appears in the synthesis report, not located as a standalone verbatim sentence in module_2_transcript.txt during this pass |
| "Arctic Expedition" campaign (Rolex/Greenland, 1978) | genius.md Hall of Fame Exemplars | UNCONFIRMED as a real campaign — explicitly labeled "Reconstructed" in the existing skill text; treat as an illustrative composite, not a documented case study. Not modified this pass; provenance note added inline. |
| "Atelier Invitation" series | genius.md Hall of Fame Exemplars | UNCONFIRMED as a real campaign — same reconstructed-composite status as above |
| "Premium Quality, Limited-Time Offer" anti-exemplar ad | genius.md Hall of Fame Exemplars | UNCONFIRMED as a real campaign — illustrative composite dramatizing sourced mechanics (Value Inversion, Controlled Distance), not a named real ad |

## Rule Applied

A claim that a source is absent is itself a provenance claim. Every "no self-identification found" line above reflects an actual grep/read of the file, not an assumption — see the byte sizes and hit counts recorded. No 0-byte or "unrecoverable" claims were made; all seven source files were opened and read in full or via targeted search during this repair pass.
