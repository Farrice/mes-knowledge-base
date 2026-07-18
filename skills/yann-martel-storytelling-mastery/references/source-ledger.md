# Yann Martel — Source Ledger

Every claim/quote used to repair `skills/yann-martel-storytelling-mastery/genius.md`, labeled claim-by-claim. Ground truth = `extractions/yann-martel/transcript.txt` (79,659 bytes, single interview transcript, verified via `wc -c` — not 0-byte, not empty) and `extractions/yann-martel/extraction-report.md` (13,674 bytes).

## VERIFIED (verbatim quote located in transcript.txt, checked by direct offset read)

| Claim / Quote | Location (approx. char offset) |
|---|---|
| "what you don't want to do is write it out too much that it leaves nothing to the imagination of the reader" | ~7195–7300 |
| "The more you withdraw, the more the reader, the viewer has to come halfway." | ~9195–9270 |
| "you have the facts of the story, you have the research, you have the scenes, but then as you write the book, it kind of elevates into a story" | ~24555–24705 |
| "I just chosen for what they might symbolize" | ~16035–16105 |
| "vehicles for human thought" | ~16000–16950 (same passage as above, monkey/donkey Holocaust allegory novel — the transcript renders the title as "Beatus and Virgil" / "Beatric and Virgil" at ~15612, ~18950, ~61350, ~63500, an ASR transcription garble of the real title; not asserted here as a clean verbatim title) |
| "That's why I never describe my characters... If you emphasize anything about someone's nose, you suddenly imagine this enormous nose... It's a caricature." | ~64520–64960 |
| "How can you not address the question of who killed the little boy?" | ~73985–74060 |
| "in genre fiction, you want a confirmation of your expectations" | ~74060–74180 |
| "I would have so much rather you written something that's half as sincere as that, filled and littered with typos, than to have AI write that. It felt like a violation and a betrayal." | ~45240–45480 (diarization markers ">>" present mid-quote in the raw transcript — see note below) |
| "it's just you masturbating on the page thinking you're really clever. It's just annoying." | ~41460–41625 (Martel quoting his editor's verdict on the `Life of Pi` lifeboat margin-floating dialogue experiment — the passage at ~39500–41000 confirms this is the Pi/blind-Frenchman lifeboat scene, not a different book; corrected from an initial mis-attribution to `Beatrice and Virgil` during drafting of this ledger) |
| "It's not about praise. Art is a gift." | ~56380–56480 |
| "you don't give a gift wanting a gift in return." | ~56610–56720 |
| "don't have sentences that are the same length one after the other. You don't want to have 17, 10 word sentences in a row. That gets boring." | ~34390–34540 |
| "you got to be really sparing with the exclamation mark because it's highly manipulative" | ~31760–31870 |
| "Hey, that's a great idea. I could elevate the humble footnote." | ~66120–66220 |
| "The words that have been coming to mind for me are satisfying and mysterious." | ~74340–74440 |
| "Turtles of the Pacific" (Manila-envelope research example) | ~1600–2100 (envelope system passage) |
| "bamboozle" (Indian-English word Martel logged as a research fragment) | ~1418–1566 |
| Roughly 400 pages of research notes accumulated over ~2.5 years before drafting `Life of Pi` | ~1995–2075 ("I had like 400 pages of of of a hodgepodge of..." — transcription stutter present; the "400 pages" figure is quoted as a fact, not inside quotation marks, because the surrounding words repeat mid-utterance ("of of of") in a way that would misrepresent Martel's fluency if reproduced as a clean verbatim quote) |

## Note on transcription artifacts
The source transcript uses `>>` inline to mark speaker-turn breaks, occasionally mid-sentence within what is otherwise one continuous statement by Martel (see the AI-sincerity quote above). Where a quote spans one of these markers, the marker was silently removed for readability; the surrounding words were not altered, added, or reordered. Flagged here rather than left undisclosed.

## LIKELY (paraphrase of a clearly-stated position, not a verbatim lift)
- Martel treats punctuation (period, comma, exclamation mark, paragraph break) as tempo/breath control rather than grammar housekeeping — synthesized from the punctuation passage (~30700–33500), consistent with `references/source-map.md` "Punctuation" section.
- Martel separates genre fiction's expectation-fulfillment contract from literary fiction's permission to disorient — synthesized from the genre passage (~49850–53500), consistent with `references/source-map.md` "Genre and Literary Fiction" section.

## UNCONFIRMED
- None of the quotes used in this repair are UNCONFIRMED — every quote cited above was located verbatim (or disclosed-edited per the note above) in `extractions/yann-martel/transcript.txt` before use. No quote was anchored from memory or from the well-known text of `Life of Pi` itself (e.g., the Richard Parker "did not look back" ending) — that passage is discussed in the transcript (~70200–71150) but was not quoted verbatim from the novel, only referenced as an anecdote in Martel's own words, which is how it is used in this repair.

## Files consulted
- `extractions/yann-martel/transcript.txt` (79,659 bytes, `wc -c` verified)
- `extractions/yann-martel/extraction-report.md` (13,674 bytes, `wc -c` verified)
- `skills/yann-martel-storytelling-mastery/references/source-map.md` (pre-existing, passed `source_ledger` check independently)
- `skills/yann-martel-storytelling-mastery/genius.md` (pre-existing, repaired in place — original content preserved, additive-first)
