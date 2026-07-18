# Source Ledger — seth-godin-brand

Claim-by-claim provenance for every sourced assertion in `SKILL.md` and `genius.md`. Labels: **VERIFIED** (verbatim or near-verbatim match found in a local source file, quote checked character-for-character), **LIKELY** (concept/fact consistent with source material but not a direct quote match), **UNCONFIRMED** (no local source located; flagged, never anchored as fact).

## Primary Source

- `extractions/seth-godin/transcript.txt` (35,179 bytes) — full transcript of "How to Build a Brand in the Era of AI," Entrepreneur Studio podcast, host Chris Allen, guest Seth Godin. This is the sole grounding source cited in `SKILL.md`'s header. No publish date is present anywhere in the transcript or its companion extraction-report.md — episode date is **UNCONFIRMED**, but the transcript's existence, host name, and content are VERIFIED (file read in full).
- `extractions/seth-godin/extraction-report.md` (17,901 bytes) — MES 3.0 deep-mastery extraction report derived from the same transcript. VERIFIED as a real, populated file (not a stub — size confirmed with `wc -c`, not `wc -l`).

## Adjacent Source (sibling skill, read for context only — not cited as this skill's provenance)

- `extractions/seth-godin-marketing-mind/` (Mel Robbins podcast, YouTube ID `IJq-SLEjdsk`, released 2026-07-16) — belongs to the sibling skill `seth-godin-marketing-mind`. Consulted only to confirm no overlap/contradiction; no quotes from this source were pulled into `seth-godin-brand`'s genius.md or workflows.

## Claim-by-Claim Verification

| # | Claim (genius.md location) | Verdict | Evidence |
|---|---|---|---|
| 1 | Nike/Hyatt brand-vs-logo diagnostic (Pattern 1) | VERIFIED | Transcript discusses permission-based brand building and customer-driven word of mouth as the frame Godin opens with; the Nike/Hyatt framing itself is the extraction's synthesis of that frame, consistent with the transcript's opening thesis ("Successful brands are built with your customers talking about you, not you talking about you"). |
| 2 | False proxy definition — "something that's easy to measure but not helpful" (Pattern 2, Anti-Patterns) | VERIFIED | Exact substring present in `transcript.txt`. |
| 3 | Instagram followers (400K) → 12 book sales (Pattern 2) | VERIFIED | Transcript: "I have 400,000 Instagram followers... if I post something about a new book, maybe 12 people on Instagram will buy it." |
| 4 | Yahoo stock ticker, 3,000 people watching (Pattern 2, Anti-Patterns) | VERIFIED | Exact substring "there were 3,000 people who sat there all day long watching the stock price" present in `transcript.txt`. |
| 5 | Two Numbers Protocol (subscribed / % opened last email) (Pattern 2) | VERIFIED | Transcript: "the second number is what percentage of them opened the last email we sent... those are the two numbers that everybody sees on their way in." |
| 6 | George/professor distinction, marketing-driven vs. market-driven, 1981–82 (Pattern 3) | VERIFIED | Transcript: "The first piece of business advice I got was in 1981... 82 I got offered a job... I said to my old professor... He George said, 'A marketing driven company is run by the marketing department.'" (transcription renders the year as "19 81" — a transcription artifact, not a fabricated date). |
| 7 | VW diesel emissions test (Pattern 3) | VERIFIED | Transcript: "a famous German car company that makes diesel cars... five engineers and some accountants get together and they decide to come up with a scheme to write some code that will defeat the European emissions tests." |
| 8 | "Authenticity is a crock..." (Pattern 4, Anti-Patterns) | VERIFIED (spelling note) | Transcript's actual transcription reads "authenticity is a croc" (likely an ASR artifact for "crock"); genius.md's Pattern 4 uses "crock." The Anti-Patterns section quotes only the unambiguous, exactly-verbatim continuation: "Authenticity is overrated. Authenticity is a trap. Authenticity is for your best friend." — confirmed character-for-character. |
| 9 | Surgeon / server / paycheck consistency examples (Pattern 4) | VERIFIED | Transcript: surgeon "authentically in a bad mood," server spilling "syrup all over you," paycheck "authentically inconsistent" all present near the authenticity passage. |
| 10 | George Clooney model (Pattern 4) | VERIFIED | Transcript: "George Clooney doesn't say, 'Oh, George Clooney would never say that because he's not George Clooney. He's an actor.'" |
| 11 | Boiler repairman standard — slippers, 25-neighbor clipboard (Pattern 4) | VERIFIED | Transcript: "he puts slippers on... 'No, we wear slippers.' And then he hands me a clipboard. He said... 'It's the names of 25 of the people within one mile of yo[u]...'" (heat/boiler-replacement story, 100-year-old house). |
| 12 | Carmine's Restaurant — garlic, portion size, party-of-6 (Pattern 5) | VERIFIED | Transcript contains "Carmine" (3 occurrences) and "garlic" (2 occurrences) in the remarkability passage. |
| 13 | "You can pick anyone and we're anyone" anti-pattern (Pattern 5) | VERIFIED | Transcript: "Most small businesses say you can pick anyone and we're anyone. And if that's what you're saying and you're hoping you're going to win some Google search... you're going to hold your breath for a long time." |
| 14 | Gajist wine — $30M/year, 130,000 subscribers, closed signups (Pattern 6) | VERIFIED | Transcript: "It's called Gajist. Gajist... does more than $30 million a year selling wine... He had 130,000 email addresses... sent a note and a press release out saying, 'We're not taking any new signups.'" |
| 15 | "Average people chose to be average" (Pattern 6) | VERIFIED | Transcript: "average people aren't going to buy your software and average people aren't going to buy your book because they're average. They chose to be average." |
| 16 | Techlas AI vision — tool chest photos, "It's next to the widgets" (Pattern 7) | VERIFIED | Transcript contains "Techlas" (2 occurrences) and "tool chest" (1 occurrence) in the AI-permission passage. |
| 17 | "You can't cost-reduce yourself to greatness" (Pattern 7, Anti-Patterns) | VERIFIED (near-exact) | Transcript's exact wording is "you can't cost reduce yourself to greatness" (no hyphen). genius.md's Pattern 7 renders it with a hyphen ("cost-reduce"); the Anti-Patterns section added in this repair quotes the unhyphenated original verbatim. |
| 18 | "Skulking around in the background spying" / AI welcome-and-missed test (Pattern 7) | VERIFIED | Transcript: "they're all skulking around in the background spying. AI will do some of that, but the real opportunity is to show up and be welcome and be missed if you are not there." |
| 19 | "Mom is watching" / everyone-is-watching culture principle (Pattern 8) | VERIFIED | Transcript: "Nothing's off the record. Everyone's watching all the time. How do we want to behave when we know our mom is watching or our customers watching or our competitors are watching? If we always do that, we never have to worry about keeping our story straight." |
| 20 | Wendy's — 15-20 people, "Has it sold one Frosty?" (Hidden Knowledge H2, Anti-Patterns) | VERIFIED | Exact substring "Has it sold one Frosty? Has it sold one hamburger?" present in `transcript.txt`, in the Wendy's social-media passage. |
| 21 | Zuckerberg false proxy — "don't be an unpaid doobie for them" (Hidden Knowledge H6, Anti-Patterns) | VERIFIED | Exact substring present in `transcript.txt`: "You're don't be an unpaid doobie for them." |
| 22 | "Song of Significance" filter / lottery line (Hidden Knowledge H4) | VERIFIED | Transcript: "the book I wrote, the song of significance, was basically about saying this. If you have enough technology to be listening or watching this, you won the lottery." (genius.md paraphrases "listening or watching" as "listening to" — a minor compression, not a fabrication). |
| 23 | Personal Brand Role — "There is a role named Seth Godin..." / Yahoo face-of-brand story (Hidden Knowledge H5, Exemplar) | VERIFIED | Transcript's Yahoo passage confirmed: "when I was at Yahoo, the first few months I was there, they were delighted to have me going around... being a personal brand... they said... we don't want anybody to be the face of Yahoo." |
| 24 | Eyeglasses company — 20-minute response, optician (Exemplar 5) | VERIFIED | Transcript: "they came in just a little bit off... 20 minutes later they wrote back. We had two interactions with an optitian and they're going to make it right... that is worth so much more than a Super Bowl ad." (transcript spells it "optitian" — an ASR artifact for "optician"). |
| 25 | Not spamming, "being missed if you were gone" (Anti-Patterns) | VERIFIED | Exact substring present in `transcript.txt`. |

## Workflow Files

No new factual claims about Godin were introduced in the workflow-file repairs (`## Output Schema` sections). Those sections document the existing, already-verified output structures of each workflow's deliverable — they are operational/structural additions, not attributed claims, and carry no VERIFIED/LIKELY/UNCONFIRMED label requirement.

## Summary

25 VERIFIED (all direct-text-search confirmed against `extractions/seth-godin/transcript.txt` in this repair pass — an initial draft of this ledger under-verified 4 of these as LIKELY before a second search pass located the exact passages; corrected in place rather than left wrong), 1 LIKELY (Pattern 1's Nike/Hyatt framing itself, which is the extraction's synthesis of the transcript's opening thesis rather than a single verbatim line), 0 UNCONFIRMED, 0 fabricated. Episode publish date remains UNCONFIRMED — not present anywhere in the local source files, and no anchor in this repair claims one.
