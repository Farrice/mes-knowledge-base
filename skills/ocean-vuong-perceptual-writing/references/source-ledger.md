# Source Ledger — Ocean Vuong Perceptual Writing

Ground-truth sources for `skills/ocean-vuong-perceptual-writing/`. Every claim in `genius.md` and `SKILL.md` traced to a source and labeled VERIFIED / LIKELY / UNCONFIRMED. Primary source is `extractions/ocean-vuong/transcript.txt` (75,514 bytes, single-line podcast transcript, "How I Write" interview — no line breaks, so exact byte offsets are used in PROVENANCE.md instead of line numbers) plus `extractions/ocean-vuong/extraction-report.md` (31,645 bytes, 14-pattern extraction). External claims (bio facts not spoken in the interview) were checked against live web sources on 2026-07-18.

## Labeling key
- **VERIFIED** — exact or near-exact quote/fact located in the cited source, checked verbatim.
- **LIKELY** — consistent with the source/public record but not a verbatim match; reasonable synthesis.
- **UNCONFIRMED** — could not locate in any source consulted; flagged, not deleted (additive-first boundary).

## Biographical claims (genius.md, "The Writer Who Re-Sees")

| Claim | Label | Source |
|---|---|---|
| MacArthur "Genius Grant" Fellow | VERIFIED | External: umass.edu/news "Ocean Vuong Named 2019 MacArthur Fellow"; oceanvuong.com/about |
| T.S. Eliot Prize winner (for *Night Sky with Exit Wounds*) | VERIFIED | External: tseliot.com prize page, "Ocean Vuong on winning the T.S. Eliot Prize 2017" |
| NYU professor | VERIFIED | transcript.txt opening line: "he's a professor at NYU"; external confirms Professor of Modern Poetry and Poetics, NYU MFA |
| Arrived in the US at age 2, from Vietnam, without English | VERIFIED | External: Wikipedia/Britannica — emigrated from Ho Chi Minh City to Hartford, CT at age two after a refugee camp stay |
| Taught himself to read through library books while his grandmother and mother remained illiterate | LIKELY | External sources confirm the family's illiteracy and his library use broadly (his novel is dedicated to his illiterate mother as its "phantom readership"); the specific "taught himself to read through library books" framing is a reasonable synthesis, not a single verbatim source |
| Debut novel *On Earth We're Briefly Gorgeous* "sold to 11 out of 12 editors who saw it" | **UNCONFIRMED — likely misstatement** | transcript.txt (~offset 13,400) has Vuong recalling "one of the editors said, 'What about the reader in the Midwest?'" during submission — this establishes there were multiple (roughly a dozen) editors involved, but nowhere states a "sold to 11/12" acceptance ratio. No external source corroborates this specific statistic either. This looks like a conflation of the Midwest-editor anecdote into a fabricated stat. Flagged for conductor review — not deleted per additive-first boundary. |
| *Night Sky with Exit Wounds* won the T.S. Eliot Prize | VERIFIED | Same as above (tseliot.com) |
| The New Yorker published him from the unsolicited slush pile | VERIFIED | transcript.txt (~offset 13,900): "The New Yorker gave me... they published me out of the slush. And I never — cuz I sent into the slush and I thought, 'There's no way they're reading the slush'... but to their credit, they're really out there looking at the culture." |

## Theory attributions

| Claim | Label | Source |
|---|---|---|
| Shklovsky's ostranenie / "make the stone stony" | VERIFIED | extraction-report.md line 53; consistent with standard Shklovsky literary-theory attribution ("Art as Technique," 1917) |
| Aristotle's mimesis vs. poiesis framing | VERIFIED | extraction-report.md line 30, Pattern discussion throughout; Vuong's own mimesis/poiesis vocabulary is used repeatedly in transcript.txt |
| Heidegger's phenomenology / "threshold" | LIKELY | extraction-report.md references Heidegger's threshold concept in the poietic-threshold pattern discussion; not a verbatim Vuong quote isolated in transcript excerpts checked |
| Lotman's cultural semiotics (synchronic/diachronic, "engulfs innovation... spits out homogenization") | VERIFIED | extraction-report.md line 211, direct paraphrase of Yuri Lotman's concentric-circle model as discussed by Vuong |

## Core quotes (genius.md "How to Use This Skill" + "5 Operating Principles")

| Claim/quote | Label | Source |
|---|---|---|
| "80% of writing is looking and thinking. The last part is syntax." | VERIFIED | transcript.txt verbatim: "I think like 80% of writing is looking and thinking. The The last part is syntax." |
| "the spike protein... the downloading mechanism" | VERIFIED | transcript.txt verbatim: "that 20% is everything because that is like the spike protein. It is like the downloading mechanism." |
| "300,000 people beat you to it" (Species Test) | VERIFIED | transcript.txt verbatim, attributed to Vuong's teacher Ben Lerner in an undergrad office-hours anecdote |
| "the standard Ben Lerner set" | VERIFIED | transcript.txt verbatim: "my my teacher, Ben Lerner... I was an undergrad in his office hours... 'You see that line you wrote?... 300,000 people beat you to it.'" |
| Rose in a bride's hair vs. Mike Tyson's ear (Cliché Rescue) | VERIFIED | transcript.txt verbatim: "you take the same rose, put it in Mike Tyson's ear. Now you're somewhere else. So it's not the rose's fault." |
| "I'm not arguing for maximalist sentences. I'm arguing for idiosyncrasy and strangeness." (re: early Hemingway) | VERIFIED | transcript.txt verbatim |
| "too felt" / newspaper-sentence critique | VERIFIED | transcript.txt verbatim: "an editor would say, 'This is too conspicuous.' ...it's too felt." |
| "There's no such thing as cliché" (Shklovsky, via Vuong) | VERIFIED | transcript.txt verbatim |
| Robert Browning's "Meeting at Night," haunted Vuong 20 years | VERIFIED | transcript.txt verbatim: "I read it 20 years ago as a high school student. To this day I still think about that poem." |
| Eduardo Corral, "moss grows along the tree like applause," 9 years to write 45 pages | VERIFIED | transcript.txt verbatim ("Nine years" / "he's looked at moss for a long time"); the exact phrase "moss grows along the tree like applause" is confirmed via extraction-report.md lines 62 and 226 (transcript excerpt cuts off mid-word but the full simile is corroborated there) |
| Isaac Babel, "The low red sun rolls across the hills as if beheaded" | VERIFIED | transcript.txt verbatim |
| Japanese botanist / "medicinal plant method" | VERIFIED | transcript.txt verbatim: "reminds me of a Japanese botanist who was tasked to find medicinal plants in the rainforest... he had the record... for finding the most medicinal plants" |
| Skateboarding / "threw yourself off an eight-stair never expecting to land" | VERIFIED | transcript.txt verbatim |

## Comparative claims (genius.md "Key Differences from Other Writing Experts")

| Claim | Label | Source |
|---|---|---|
| Comparisons to Eric Roth, Nicolas Cole, Connelly, Pressfield, Dan Koe, Ward Farnsworth, Lara Acosta | N/A — editorial synthesis | Not sourced claims about Vuong; these are cross-skill positioning statements written by the extraction team comparing Vuong's roster-mate skills. No provenance anchor required — flagged here for transparency, not a factual claim about Vuong himself. |

## Notes for the conductor
- The one item requiring a decision is the "11 out of 12 editors" line in `genius.md` line 9 (unchanged from the passing original — outside this worker's scope, since only `recognition_test` and `source_ledger` were failing checks). Recommend either sourcing it properly (if a citable interview/article states this ratio) or softening to match the verified Midwest-editor anecdote.
- All other genius.md and SKILL.md factual claims checked in this pass came back VERIFIED or LIKELY; no other UNCONFIRMED items found.
