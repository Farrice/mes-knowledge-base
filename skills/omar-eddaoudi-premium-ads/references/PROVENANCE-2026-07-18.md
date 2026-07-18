# Provenance — omar-eddaoudi-premium-ads repair pass

Anchor → source file + location. All sources under `extractions/omar-eddaoudi/` (repo root); byte sizes confirmed via `wc -c` before use — see `references/source-ledger.md` for the full VERIFIED/LIKELY/UNCONFIRMED table.

| Anchor (as it appears in genius.md) | Source file | Location | Label |
|---|---|---|---|
| "my name is Omar. I'm the founder at Orow Labs" | `module_2/module_2_transcript.txt` | single-block transcript, ~line 5 (found via string search, file has few line breaks) | VERIFIED |
| "you need to avoid overselling the features because those are commodities honestly" | `module_2/module_2_transcript.txt` | ~line 13 | VERIFIED |
| "you don't want to be competing with people's standards" | `module_2/module_2_transcript.txt` | ~line 13 | VERIFIED |
| "you don't own a [Patek]... merely look after it for the next generation" | `module_2/module_2_transcript.txt` | found via string search on "PEX" | LIKELY — brand name inferred from garbled ASR ("Pek Philippe"/"PEX") |
| "I don't want my customers to hit my website and have like 26 different objections" | `module_3/01_zero_to_seven_figures.txt` | line 1 (monolithic transcript block) | VERIFIED |
| "they don't enrich it, they don't analyze it, and they don't extract anything meaningful from it" | `module_3/01_zero_to_seven_figures.txt` | line 1 | VERIFIED |
| "The brands that fail don't fail because they have a bad product..." | `module_3/01_zero_to_seven_figures.txt` | line 1 | VERIFIED |
| "83k a month" / "3k a month" / "$60 on the front end" | `module_3/01_zero_to_seven_figures.txt` | line 1 | VERIFIED |
| "first ad... from Whoop... semantic reversal" | `module_3/02_wellness_ad_teardown.txt` | line 1 | VERIFIED |
| Value Inversion / Controlled Distance / Archetypal Mirroring definitions | `extraction-report.md` (root, module 1) | Genius Patterns section | LIKELY — synthesis report, speaker-confidence gap noted in ledger |
| Narrative Hegemony / Mirror-Bridge / Objection-First / LEO definitions | `module_2/extraction-report.md` | Genius Patterns section | VERIFIED speaker, LIKELY synthesis wording |
| "Reddit and Trustpilot" sentiment signal | `module_2/extraction-report.md` | Hidden Knowledge section | LIKELY — not located verbatim in module_2_transcript.txt during this pass |
| Arctic Expedition / Atelier Invitation / anti-exemplar ad concepts | pre-existing genius.md text (not authored this pass) | Hall of Fame Exemplars | UNCONFIRMED — already self-labeled "Reconstructed" in the file; provenance note added, content left as-is per additive-first rule |

## Anti-pattern items (genius.md § Anti-Patterns (Sourced))

All 6 anchor to `module_2/module_2_transcript.txt` or `module_3/01_zero_to_seven_figures.txt` verbatim quotes listed above, plus the pre-existing anti-exemplar ad (UNCONFIRMED, cross-referenced not duplicated).
