# Source Ledger — andreessen-horowitz-new-media

Single source of record for every factual claim this skill carries. Labels per
`directives/verification-agent-protocol.md`: VERIFIED (independently confirmed),
LIKELY (consistent with the source / doctrine-consistent extrapolation, not a
verbatim quote), UNCONFIRMED (asserted only in the source, or not independently
checked — quarantined).

## Source Manifest

| # | Source | Type | Status |
|---|---|---|---|
| 1 | `extractions/marc-andreessen-ben-horowitz/transcript.txt` — internal a16z discussion on new-media strategy, Marc Andreessen & Ben Horowitz, ~45 min, ~55,427 bytes (`wc -c`), added to the extraction corpus 2026-03-21 per `git log --diff-filter=A` | Primary (full transcript, verbatim-quote checked line by line for this repair) | VERIFIED present and non-empty (file read + size confirmed 2026-07-17; no publish date or video URL embedded in the file itself — dating is by corpus-addition commit, not original air date) |
| 2 | `extractions/marc-andreessen-ben-horowitz/extraction-report.md` | Secondary (MES 3.0 extraction derived from Source 1) | VERIFIED internally consistent with Source 1 — spot-checked quotes below |

All doctrine in `genius.md` and the 4 workflows derives from Source 1, either
directly (verbatim quote) or via Source 2's paraphrase of Source 1. No claim in
this skill is attributed to Andreessen/Horowitz from training-memory knowledge of
their public writing (a16z blog, Marc's essays, etc.) — this skill is scoped to
what the two of them say in this specific internal discussion.

## Claim Ledger

| Claim | Label | Basis |
|---|---|---|
| "You can't be half and half...the whole motion of the old world will kill you in the new world and vice versa" | VERIFIED | Verbatim in Source 1 |
| "old media is defense[]oriented. In new media, offense is always better than defense" + flood-the-zone opening | VERIFIED | Verbatim in Source 1 (transcription artifact "defenseoriented" preserved) |
| NYT/WSJ leak of early fund results nearly caused an existential crisis for a16z | VERIFIED | Verbatim narrative in Source 1 ("the New York Times got a leak of our results...they misinterpreted the results") |
| Board CEO who said nothing and considered it "mission accomplished" | VERIFIED | Verbatim in Source 1 |
| Howard Dean / out-of-context destruction example | VERIFIED | Verbatim in Source 1 |
| "inherently deceptive practice...of abstracting things away from people" (80-year corporate-branding aberration) | VERIFIED | Verbatim in Source 1 |
| Platform-native hiring: "not just how the platform works technically, but also the vibe and the taste and the spirit" | VERIFIED | Verbatim in Source 1 |
| Cross-posting critique: "have one idea and then cross-post it...across every platform but it doesn't fully appreciate...what that platform is built for" | VERIFIED | Verbatim in Source 1 (transcribed "crossost"; quoted material used in this skill avoids the mis-transcribed word itself) |
| Hostile comments = "somebody with like four followers or like a bot" | VERIFIED | Verbatim in Source 1 |
| Gaming lobby genealogy (Call of Duty → Something Awful → YouTube → social comments) | VERIFIED | Verbatim in Source 1 |
| Joe Rogan CEO test, attributed to "Jordy from TVPN" | VERIFIED | Verbatim in Source 1 |
| Instagram 18-year-old hire "grew up on Instagram," 35% MoM growth cited | VERIFIED — named **Hero**, not Richard | Source 1: "We have this guy, Hero, who's...18 years old and has been...grew up on...Instagram" |
| Video-production 18-year-old hire, "went straight from high school with the NBA" (i.e., skipped college) | VERIFIED — named **Richard**, hired for video (Clulu / browser-based video work), not Instagram | Source 1: "we hired Richard, another 18-year-old...he had previously done the Clulu video...and the browser[-]based video" |
| ⚠ Correction: earlier draft of this skill's "Talent Inversion" pattern attributed the Instagram hire to "Richard" | CORRECTED this repair | Source 1 names two separate 18-year-old hires (Richard = video, Hero = Instagram); the skill's genius.md now names Hero for the Instagram claim and keeps Richard for video |
| "Write a press release" / "Hire a PR firm" / "Let legal review every post" as named anti-patterns | LIKELY (doctrine-consistent, not a verbatim quote) | Not found verbatim in Source 1 via full-text search for "press release," "PR firm," "legal"; these are reasonable extrapolations from the stated doctrine (offense over defense, speed over approval gates, founder-direct over corporate-abstracted) but are not things Andreessen or Horowitz say in this transcript |
| "35% MoM" Instagram growth figure | VERIFIED | Verbatim in Source 1: "we're up 35%, you know, month over month right now" |
| Fellowship: 2,000 applications, 65 selected | VERIFIED | Verbatim in Source 1 |
| Viral post lifecycle "12h up, 24h down, 36h forgotten" | VERIFIED | Verbatim in Source 1: "they tend to take off within like 12 hours...it's like 12 hours up and then it's like 20 24 hours down and then 36 hours later it's like gone from our collective memory" |

## Recognition Test

See `genius.md`, "How to Use This Skill (Model Calibration)": would Andreessen or
Horowitz recognize an output as their new-media doctrine applied to a new problem —
binary commitment, context-length defense, platform-native staffing, interestingness
over safety — or as a generic content-strategy deck wearing OODA-loop vocabulary?
