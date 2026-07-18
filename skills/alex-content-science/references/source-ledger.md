# Source Ledger — alex-content-science

Every claim in `genius.md` and `SKILL.md`, traced to its source and labeled
VERIFIED / LIKELY / UNCONFIRMED. Primary source is the transcript of three
YouTube videos (`extractions/alex-content-science/transcript.txt`, 21,666
bytes, confirmed via `wc -c` 2026-07-17). Secondary source is the extraction
report (`extractions/alex-content-science/extraction-report.md`, 17,524
bytes), which itself states its material comes from "YouTube videos (3) —
~30 min total + Perplexity enrichment research" — the enrichment portion is
NOT primary-source and is labeled accordingly below.

## VERIFIED (verbatim in transcript.txt, confirmed by direct string search)

| Claim / Quote | Location in transcript.txt |
|---|---|
| "that's not stealing like an artist. That's just stealing." | ~offset 317, opening third of transcript |
| "same font, same background, same quotes, same format. If I covered the account names, you would be able to tell who posted what." | ~offset 2102 |
| "you're choosing to be another brown cow and then wondering why no one is stopping to look at your content." | ~offset 2815 |
| "So you copy a competitor's video. It does okay. So you copy another one. Then that does okay, too." / "So what do you do? You panic. You go back to copying and now you're stuck." | ~offset 3021–3232 (Sheep Cycle passage) |
| "They followed you for a trend, not for you." | ~offset 3350 |
| "Dark shelves, minimalist decor, clean lines, natural light from the window" framing of the consultant's-office read | early Detail Stack breakdown segment (Kai/NPC Fisen example) |
| "calm reads as authority. Calm reads as expensive." | ~offset 6832 (pattern-interrupt passage) |
| "You stop scrolling because something feels different, even if you can't explain [music] why." | ~offset 6857 — quoted with the source transcript's own "[music]" audio-cue annotation intact |
| "You've been watching one person sit in a chair for 25 seconds and suddenly there's a physical object... 'Wait, what is he doing?'" | ~offset 7162 (retention/pen-to-mouth passage) |
| "If I were Kai's personal speaking coach, here are four more strategies I would give him" (paraphrased in genius.md as "four more strategies") | mid-transcript, Kai/speaking-coach segment |
| "They break down the surface and think they've done the work. Wow, that's a really good hook." | ~offset 14524 |
| "Ask yourself, why did they choose the angle? What rule did they break? What problem were they solving? What did they refuse to do?" | ~offset 14798 |
| "Has nothing to do with the specific video." (One-Sentence Principle Test) | ~offset 15141 |
| "Lead with a visual result. Show the tool easy. Creates a reason to comment. Use your identity to build trust before the content does the teaching." | ~offset 11236 (R vs. A comparison) |
| R opens with a Wimbledon tennis serve; A opens with a rotating gold smartphone | R vs. A comparison passage |
| "They understood the AI is a production tool, not a content strategy." | ~offset 13105 (faceless dark-fantasy IP page passage) |
| "over 110,000 followers. 74 posts completely faceless" | ~offset 12060 |
| "318 likes. July 2025" → "Nearly 800,000 views" (few months later) | ~offset 12480–12679 |
| "2.7 million views. The creator has over 90,000 followers. That's a 30x ratio." | ~offset 4808 |
| "That's not coincidence, that's a system." (Brand System Recognition — NPC Fisen cross-video comparison) | Detail Stack step-3 walkthrough, second NPC Fisen video segment |
| "There's someone working at the desk in the background." (Status Signal as Set Dressing) | same segment |
| Alex's channel is "Grow with Alex" / "@growwithalex," "200,000 plus on YouTube, 40,000 plus on my newsletter" | opening ~30 seconds of transcript |

## LIKELY (consistent with source material but not a verbatim transcript quote)

| Claim | Basis | Why LIKELY not VERIFIED |
|---|---|---|
| Competitor Database Method specifics — alt/research account, subscribing to all niche channels, YouTube filters (last 3 years, 1M+/1,000,000+ views), building a Notion database | `extraction-report.md`, Genius Pattern #11 | extraction-report.md's own header states this report draws on "3 YouTube videos + Perplexity enrichment research" — this specific executable behavior does not appear as a direct quote in transcript.txt; treated as the extractor's synthesis, possibly enrichment-sourced |
| "The 5 Levels of Views" framework existing as a named system | transcript.txt closing line: "I made a video breaking down the five levels of views and growth and what to focus on for each stage" | The reference to the video's existence is VERIFIED (it's a direct line in transcript.txt); the framework's internal structure is not — that video is not among the three source transcripts, so its content is UNCONFIRMED (see below) |
| Alex's wardrobe/environment reads generalized as "identity design principles" beyond the two specific examples shown | extraction-report.md Genius Patterns #5–#6, applying the two on-screen examples as a general rule | The two specific instances (consultant's-office background, black-crew-neck outfit) are VERIFIED; the generalized "always design your environment/wardrobe this way" framing is the extractor's abstraction |

## UNCONFIRMED (no source, or source explicitly absent — verified by direct read, not assumed)

| Claim | Status |
|---|---|
| "The 5 Levels of Views" internal framework (the specific tiers/criteria) | Referenced by title only in transcript.txt; the video itself is not one of the three source transcripts on file. `extraction-report.md` Hidden Knowledge #7 states outright: "specifics weren't fully detailed in available transcripts." No fabricated structure has been added anywhere in this skill — flagged UNCONFIRMED rather than invented. |
| The three "Hall of Fame Exemplars" in genius.md ("Finance as Fine Dining," "Silent Authority Mini-Documentaries," "Generic Productivity Tool Review") | These are illustrative composites, not real, named accounts identified in transcript.txt or extraction-report.md. They pre-date this repair pass and were left in place (additive-first boundary — not deleted), but are now explicitly flagged UNCONFIRMED/illustrative in genius.md itself so they are never mistaken for verified case studies. |
| NPC Fisen "refuses music, refuses flashy clothes, refuses clickbait energy" as an enumerated list of three specific refusals | extraction-report.md Hidden Knowledge #6 paraphrases this; transcript.txt supports the *concept* (the refuse-to-do lens, VERIFIED above) but does not itemize these three specific refusals in that exact form — treated as extractor inference, not a direct quote |

## Absence check (performed, not assumed)

- `extractions/` was searched for any file matching `alex` beyond `alex-content-science/` (`ls extractions/ | grep -i alex`) — only `alex-content-science/`, `alex-myatt/`, and `alex-suzuki-digital-product-revenue-os` exist; no additional Alex-content-science source material was found or overlooked.
- Both source files were read in full and their byte sizes recorded via `wc -c` (not `wc -l`, per the "verify absence" instruction): `transcript.txt` = 21,666 bytes; `extraction-report.md` = 17,524 bytes. Neither is empty or truncated.
- No 0-byte or "unrecoverable" claim is made anywhere in this ledger.
