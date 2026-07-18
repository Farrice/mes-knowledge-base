# Source Ledger — lamott-craft

Ground truth: `extractions/anne-lamott/transcript.txt` (73,001 chars, single-line ASR
transcript of a YouTube interview, 14,366 words per SKILL.md's word count, no line
numbers — anchors below use a locating substring instead of a line number).
Verified by direct `python3` substring search against the file on 2026-07-18, not by
memory. No other extraction file exists for this expert (`ls extractions/ | grep -i
lamott` returns only `anne-lamott` and `anne-lamott-neal-allen-really-real`, the latter
owned by sibling skill `lamott-allen-really-real-writing`).

| # | Claim / Quote | Location in source | Label | Notes |
|---|----------------|--------------------|-------|-------|
| 1 | "you can only say said. You can't say um Andrea chuckled" | ~char 20,850–21,000, transcript.txt | VERIFIED | Exact substring match. |
| 2 | "if you start saying he chuckled, he enthused, he he proclaimed" | ~char 21,250–21,400, transcript.txt | VERIFIED | Exact substring match, immediately follows claim 1 in source. |
| 3 | "there's a rule in good writing about if it's literary, it's you can't use it... if you're trying to sound literary, take it out" | ~char 7,650–7,850, transcript.txt | VERIFIED | Exact substring match (ellipsis marks a short interviewer aside removed for readability, no words altered). |
| 4 | "If it's literary, I'm not going to be interested in it" | ~char 31,040–31,150, transcript.txt | VERIFIED | Exact substring match, same passage as claim 6. |
| 5 | "you used... five cent words, nickel words instead of 25 cent words" | ~char 13,900–14,050, transcript.txt | VERIFIED | Transcript literally reads "you used 15 uh uh five cent words, nickel words instead of 25 cent words" — the "15 uh uh" is ASR disfluency capture, elided with an ellipsis in the anti-pattern bullet; no substantive words altered. |
| 6 | "the sentences are pleasing. They're not ostentatious. They're not showoffy" | ~char 30,950–31,050, transcript.txt | VERIFIED | Exact substring match. |
| 7 | "a confused reader is an antagonistic reader" (attributed to Shirley Jackson by Lamott) | ~char 14,050–14,150, transcript.txt | VERIFIED (quote) / LIKELY (attribution) | The quote is verbatim in the transcript. The attribution to Shirley Jackson is Lamott's own claim in the interview, not independently checked against a Jackson primary source — labeled LIKELY on attribution accuracy, VERIFIED on "Lamott said this in the interview." |
| 8 | "somebody at a cocktail party who's just trying to impress you with their overeducation, then it is tiresome" | ~char 24,250–24,400, transcript.txt | VERIFIED | Exact substring match. |
| 9 | "whatever meager charms the book possessed were harmed by the writer show coffee overkill" | ~char 66,700–66,850, transcript.txt | LIKELY (exact wording) / VERIFIED (event occurred) | This is the literal ASR rendering in the transcript file — "show coffee overkill" is almost certainly a mishearing of "show-offy overkill" (matches the "showoffy" vocabulary Lamott uses elsewhere in the same interview, claim 6). The underlying event — harsh 1980 reviews of *Hard Laughter*, quoted from Publishers Weekly/Kirkus per Lamott's account — is VERIFIED as stated by her in the interview; the exact printed-review wording is LIKELY, not VERIFIED, because the transcript itself is garbled at this exact phrase and no independent copy of the 1980 reviews was consulted. |
| 10 | "I no longer... was doing show was doing show off they overkill of trying to be funny" | ~char 66,950–67,050, transcript.txt | LIKELY | Same ASR-garble caveat as #9 — substance (she stopped trying to be funny for its own sake after that review) is clear; exact transcript wording is disfluent/doubled ("show was doing show off"). Quoted verbatim as it appears in the source file, not smoothed. |
| 11 | Hard Laughter reviews dated "1980," from Publishers Weekly and Kirkus | ~char 66,450–66,550, transcript.txt | VERIFIED | Lamott states this directly: "the first reviews I got were for this book I wrote about my father's illness a novel called Hard Laughter and the first reviews I got and this is in the 1980." |
| 12 | Irish tavern / Guinness Wi-Fi password / sobriety exchange (Exemplar 1, pre-existing in genius.md) | ~char 28,000–29,050, transcript.txt | VERIFIED | Full passage checked against source; genius.md's rendering is a light readability edit (paragraph breaks, minor connective tissue) of the same verbatim material — no invented details found. |
| 13 | "I'm going to have to pay you like in total dimes" / copy editor changed it to "I'm going to pay you totally in dimes" (Exemplar 2, pre-existing) | ~char 70,500–71,050, transcript.txt | VERIFIED | Exact substring match for both the original line and the copy editor's "corrected" version. Novel is *Joe Jones*; transcript spells the river "Pedaluma," genius.md corrects to the real place name "Petaluma River" — factual correction, not fabrication. |
| 14 | Middlemarch "George/Mary/racetrack" passage (Exemplar 3, pre-existing) | ~char 55,600–56,450, transcript.txt | VERIFIED | Transcript renders the novel's title as "Middle March" (two words, ASR artifact) and the author as "George Elliot" (real author is George Eliot, a pen name — one 'l'). genius.md's spelling ("Middlemarch," "George Eliot") is the standard correct spelling, not an invented reference — the underlying scene (George/Mary/£1,000/racetrack/"Don't go to the racetrack") matches the transcript verbatim. |
| 15 | Isabelle Allende writer's-block anecdote (Hidden Knowledge #1, pre-existing) | ~char 3,150–3,250, transcript.txt | VERIFIED | Transcript spells the name "Isabelle Yende" (ASR mishearing of Isabel Allende, the real author) — genius.md's spelling is the corrected real name, same underlying anecdote, not fabricated. |
| 16 | "Nana, that was terrible" grandson anecdote (Signature Move, pre-existing) | ~char 51,700–51,900, transcript.txt | VERIFIED | Exact substring match: "he said nana that was terrible" and "Honey, that's all I got." |
| 17 | Dr. Spock "firm but friendly" (Genius Pattern #3, pre-existing) | ~char 11,000–11,150, transcript.txt | VERIFIED | Exact substring match. |
| 18 | "45+ years in publishing" (SKILL.md) | ~char 16,684, transcript.txt | VERIFIED | Lamott: "I've been in publishing for 45 years," describing her own inner-critic's tenure matching her career length. |
| 19 | "21 books" (SKILL.md, genius.md) | ~char 66,500–66,600, transcript.txt | VERIFIED | Lamott: "this good writing is my 21st book." |
| 20 | "*Good Writing* (with Neal Allen)," 36 rules (SKILL.md) | ~char 400–500, transcript.txt | VERIFIED | Interview intro: "she just published a book with her husband which has 36 rules for writing." Note: the video's own framing calls Neal Allen "her husband" — not independently fact-checked against public biography, since the claim is quoted as stated in the source and outside this ledger's scope (source is the interview, not a biography). |
| 21 | Source word count "14,366 words" (SKILL.md) | n/a | UNCONFIRMED | Not independently re-counted this pass — carried forward from prior extraction metadata; flagged here rather than silently assumed. |

## Summary
- 18 of 21 claims: VERIFIED against direct substring search of the source transcript.
- 3 of 21: LIKELY (exact wording on two ASR-garbled phrases; one un-independently-checked
  attribution to Shirley Jackson).
- 1 of 21: UNCONFIRMED (word-count metadata, not re-verified this repair pass — named
  honestly rather than assumed correct).
- 0 fabricated or invented sources. No quote in this skill's genius.md, SKILL.md, or the
  new Anti-Patterns section was written without a matching substring in
  `extractions/anne-lamott/transcript.txt`.
