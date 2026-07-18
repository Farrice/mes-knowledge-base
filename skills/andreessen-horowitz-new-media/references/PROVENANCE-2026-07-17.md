# PROVENANCE — andreessen-horowitz-new-media repair (Wave 3 Lane 4 Batch 1)

Ground truth source: `extractions/marc-andreessen-ben-horowitz/transcript.txt`
(55,427 bytes confirmed via `wc -c`; internal a16z discussion, Marc Andreessen &
Ben Horowitz, ~45 min; added to the extraction corpus 2026-03-21 per
`git log --diff-filter=A --follow`). No YouTube URL or original air date is
embedded in the file itself — all "2026-03-21" date anchors below refer to the
corpus-addition commit, not the original recording date, and are labeled as such.

| Anchor (in genius.md) | Source location | Verbatim? |
|---|---|---|
| "You can't be half and half...the whole motion of the old world will kill you in the new world and vice versa" | transcript.txt, opening third (Binary Commitment discussion) | Yes — exact substring, confirmed via grep |
| "old media is defenseoriented...When in doubt, flood the zone" | transcript.txt, opening Ben Horowitz monologue | Yes — exact substring incl. transcription artifact "defenseoriented" |
| "the audience would be, you know, a thousandth of the size on the defense" | transcript.txt, NYT/WSJ leak narrative | Yes — exact substring |
| "this like inherently deceptive practice um of abstracting things away from people" | transcript.txt, 80-year aberration discussion | Yes — exact substring |
| "he he had made no news and like mission accomplished, right?" | transcript.txt, board CEO anti-exemplar | Yes — exact substring |
| "we've really made sure to hire people who really understand the platform...vibe and the taste and the...spirit...of the platform" | transcript.txt, platform-native staffing discussion | Yes — exact substring |
| "have one idea and then cross-post it...across every platform but it doesn't fully appreciate...what that platform is built for and what that platform rewards" | transcript.txt, cross-posting critique | Yes — quoted material avoids the mis-transcribed word "crossost" itself; surrounding text is exact |
| "generally when we get attacked on the comments...somebody with like four followers or like a bot" | transcript.txt, gaming-lobby genealogy passage | Yes — exact substring |
| "everything from like Howard Dean...that would be nothing" | transcript.txt, out-of-context destruction passage | Yes — exact substring |
| "we're up 35%, you know, month over month" (Instagram) | transcript.txt, platform-native staffing discussion | Yes — exact substring |
| Hero = 18-year-old Instagram hire, "grew up on...Instagram" | transcript.txt: "We have this guy, Hero, who's...18 years old and has been...grew up on on Instagram" | Yes — exact substring |
| Richard = 18-year-old video hire, skipped college for "the NBA" | transcript.txt: "we hired Richard, another 18-year-old...to go straight from high school with the NBA...previously done the Clulu video...and the browser[-]based video" | Yes — exact substring |
| "Write a press release" / "Hire a PR firm" / "Let legal review every post" | Not found in transcript.txt via full-text search for "press release," "PR firm," "legal" | No — labeled LIKELY (doctrine-consistent extrapolation) in `references/source-ledger.md`, not presented as a quote |
| "12 hours up...24 hours down...36 hours...gone from our collective memory" | transcript.txt, viral post lifecycle discussion | Yes — exact substring (paraphrased in SKILL.md's pre-existing "12h up, 24h down, 36h forgotten" line, which predates this repair and is left in place) |

## Correction made this repair
The pre-repair genius.md "Talent Inversion" pattern attributed the Instagram hire
to "Richard." The transcript names two separate 18-year-old hires: **Richard**
(video production — Clulu video, browser-based video) and **Hero** (Instagram,
35% MoM growth). Corrected in `genius.md` to name Hero for the Instagram claim
and retain Richard for video, per Source 1. See `references/source-ledger.md`
claim ledger for the full note.
