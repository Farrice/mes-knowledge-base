# Source Ledger — rafa-conde-memorable-product-design

Every source consulted for the Wave 3 Lane 4 repair (2026-07-17/18), claim-by-claim. Ground truth = `extractions/rafa-conde/` (verified by direct file read this session, sizes recorded below) plus verbatim quotes already inside the skill files.

## Primary Source

- **`extractions/rafa-conde/transcript.txt`** — 64,881 bytes, 1,734 lines. Read in full-file passes plus targeted greps this session. **VERIFIED** as the source of every quote added to `genius.md` — each quote below was re-read at its cited line range and matches the file verbatim.

| Claim / quote added to genius.md | Location in transcript.txt | Label |
|---|---|---|
| "The goal is to communicate this idea as cleanly as you can to someone else." | lines 3-4 | VERIFIED (verbatim, re-read) |
| "don't just design the feature and share mock-ups. Don't just make a prototype and do a screen recording of you using the feature. Make an ad, right? Sell this idea." | lines 6-10 | VERIFIED (verbatim, re-read) |
| "you open the laptop and you see that video with the stars and the words. It was like a whole experience." | lines 31-33 | VERIFIED (verbatim, re-read) |
| "I think we lost like 20% or 30% of signups for people, you know, who would see the video first" (Retro onboarding-video skip friction) | lines 417-419 | VERIFIED (verbatim, re-read) — the 20-30% figure is Rafa's own recollection, not an audited analytics export; treat the number as his stated estimate, not an independently confirmed metric |
| "don't make users scroll or whatever. Don't like labels everywhere." | lines 533-535 | VERIFIED (verbatim, re-read) |
| "My first take was like way too much motion and I had like a little Ken Burn effect and all that stuff and I realized like it's too much." | lines 645-648 | VERIFIED (verbatim, re-read) |
| "If it's just talking, it's more boring." | line 1002 | VERIFIED (verbatim, re-read) |
| "Ultimately, it's that make it entertaining. They're paying attention. Like they want to consume this. They want to see this. It's it's funny. It's cool. Make something that it's interesting, funny, and hopefully communicates the idea very well." | lines 1016-1022 | VERIFIED (verbatim, re-read) |
| "it got rejected because it said it's too simple of an app. I need to add more stuff." (Hand Mirror App Store rejection) | lines 1320-1322 | VERIFIED as Rafa's own account (verbatim, re-read). The underlying App Store rejection itself is **UNCONFIRMED** as independent fact — no App Store review record was checked this session, only Rafa's retelling. |
| "the verge picked it up and wrote about it and then it blew up" (The Verge covering Hand Mirror) | lines 1330-1331 | VERIFIED as Rafa's own account (verbatim, re-read). That The Verge published a piece on Hand Mirror is **UNCONFIRMED** — no Verge article was located or fetched this session; this is Rafa's self-report only. |
| "I know like surprise and delight. It's a very overused term nowadays, but I'm just going to use it again cuz I don't know what else to call it" | lines 217-220 | VERIFIED (verbatim, re-read) |
| Rafa is a product designer / design engineer, worked on Hand Mirror and at Retro | `extraction-report.md` line 6, corroborated by transcript.txt lines 16-17 ("working as a design engineer at Retro") | LIKELY — self-reported in the source interview and Dive Club's own introduction of the guest; not independently cross-checked against Retro's team page or Rafa's LinkedIn this session |
| Episode: "Rafa Conde - Make your designs memorable," Dive Club, 59:01 | `extractions/rafa-conde/source-notes.md` lines 1-8 | VERIFIED — matches `extraction-report.md` line 5 and the transcript's own framing (line 11: "Welcome to Dive Club") |

## Secondary Extraction Files (read in full this session)

- **`extractions/rafa-conde/extraction-report.md`** — 4,481 bytes, 86 lines. **VERIFIED** as an internal synthesis document (prior extraction pass); used only to cross-check framing, not cited as an independent authority.
- **`extractions/rafa-conde/source-notes.md`** — 1,047 bytes, 23 lines. **VERIFIED** file exists and was read; lists YouTube URL `https://www.youtube.com/watch?v=3rnhlZj25iY` and five enrichment links (Rafa's site, Hand Mirror App Store listing, IDEO design thinking, Stanford d.school Bootleg, Don Norman emotional design essay, Laws of UX). **UNCONFIRMED** — none of these five enrichment URLs were fetched or verified this session (out of scope: this repair touches `genius.md` only, and none of the six failing checks require external re-verification); no claim added to `genius.md` this session depends on them.
- **`extractions/rafa-conde/forge-vision.md`** — 1,815 bytes, 55 lines. **VERIFIED** file exists and was read; internal positioning/roadmap document, not a factual-claim source.
- **`extractions/rafa-conde/amplifications/fourth-wall-experience-os.md`** — 2,378 bytes. **VERIFIED** file exists (`ls -la` confirms size); belongs to the sibling skill `rafa-conde-fourth-wall-experience-os` (being repaired separately this batch) and was not drawn on for this repair.

## Existing Skill Content (not re-verified, carried forward)

- `skills/rafa-conde-memorable-product-design/genius.md` (pre-repair version), `SKILL.md`, and `references/genius-patterns.md` / `hidden-knowledge.md` — **LIKELY**, unchanged content from a prior extraction pass; consistent with the transcript on spot-check but not claim-by-claim re-verified in this repair (out of scope — only the failing heartbeat checks were repaired; existing passing content was preserved per envelope boundaries).

## Explicitly Not Claimed

No anti-pattern, exemplar, or quote in the repaired `genius.md` was invented. Every quoted string was located verbatim in `extractions/rafa-conde/transcript.txt` and its line range recorded above. Where a quote reports a real-world outcome Rafa did not provide independent evidence for in the interview (the App Store rejection, the Verge coverage, the 20-30% signup figure), the ledger labels the *underlying fact* UNCONFIRMED while labeling the *quote itself* VERIFIED — the transcript is a reliable record of what Rafa said, not an audited record of what happened.
