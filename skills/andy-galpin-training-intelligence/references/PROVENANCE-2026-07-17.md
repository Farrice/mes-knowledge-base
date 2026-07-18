# PROVENANCE — andy-galpin-training-intelligence repair

Anchor → source file + location, for every new claim/quote added in this
repair pass. All source files were extracted 2026-07-17 from
`_archive/claude-export-2026-07-01.tar.gz`
(archive-internal path `claude-export/normalized/conversations/<id>.md`)
into a scratch directory for reading; none were written back into the repo.

| Anchor (in `genius.md`) | Source file | Location | Verification |
|---|---|---|---|
| "the term metabolic flexibility has been hijacked... metabolic flexibility is not just maximize fat burning. Those are not the same thing." | `62bc60da-6ab9-4c81-99f8-bb15303e123c.md` | Lines ~1317–1323 (transcript timestamps 43:49–44:27) | VERIFIED — read directly, quote copied verbatim (trimmed of surrounding filler words) |
| "I personally, you know, I don't like protein powders to be honest. And it's a processed food... it's like never just protein. Never." | `62bc60da-6ab9-4c81-99f8-bb15303e123c.md` | Lines ~1750–1756 (timestamps 58:59–59:10) | VERIFIED |
| "if it's up to me, we're not going to use them. You'll never see me program one of them ever... it's never going to come out of my mouth." | `62bc60da-6ab9-4c81-99f8-bb15303e123c.md` | Lines ~3608–3617 (timestamps 123:52–124:06) | VERIFIED |
| "some of the common mistakes with HRV are looking at the flat score" | `62bc60da-6ab9-4c81-99f8-bb15303e123c.md` | Line ~5358 (timestamp 186:00) | VERIFIED |
| "most of the chicanery happens... trying to convince people that it's got to be done this way, that there's this particular scapegoat... my push back is always against that narrative — that's just never going to be the case." | `99f7153d-63d0-4dd1-9f92-37b3245c0eaa.md` | Lines ~630–644 (timestamps 21:14–21:34) | VERIFIED |
| "you're applying the wrong principle because it came from a different body of literature" | `c5097fef-9a41-4486-8bcd-967a91d6d6cf.md` | Character offset ~6263 (continuous-text transcript, no line-level timestamps in this file) | VERIFIED |
| "a lot of people actually make the mistake here — you don't need the muscles to have complete rest, it doesn't need to be completely turned off for two or 3 days... but you definitely don't want to work it hard multiple days in a row in your typical fashion." | `c5097fef-9a41-4486-8bcd-967a91d6d6cf.md` | Character offset ~32233–32421 | VERIFIED |
| "no supplement is mandatory, even the foundational ones... they are never meant to replace or be used instead of high quality food." | `c5097fef-9a41-4486-8bcd-967a91d6d6cf.md` | Character offset ~38773 | VERIFIED |

## Supporting evidence for existing (pre-repair) genius.md claims

Used to populate `references/source-ledger.md`'s claim-by-claim table; not
new text in `genius.md` itself.

| Claim | Source file | Location | Verification |
|---|---|---|---|
| Limiter-First Diagnosis / "figure out what's the actual limiting step" | `73e73f97-ae8b-4ca0-8f68-f14a941d3326.md` | Raw transcript portion (before first `## assistant` marker), "limiting factor" hits | VERIFIED |
| Wave-loading sequence (3×80%→2×85%→...→1×90%) | `c5097fef-9a41-4486-8bcd-967a91d6d6cf.md` | Character offset ~107504 | VERIFIED |
| Velocity floor "~0.73 m/s" | `c5097fef-9a41-4486-8bcd-967a91d6d6cf.md` | Character offset ~93633–94154 ("no lower than 73 m/s" — decimal dropped by Merlin AI transcription) | VERIFIED (transcription artifact noted, not corrected/invented) |
| Collagen + Vitamin C pairing | `62bc60da-6ab9-4c81-99f8-bb15303e123c.md` | ~127:01 | VERIFIED |
| "androgen receptor" / "stress bucket" phrases | `99f7153d-63d0-4dd1-9f92-37b3245c0eaa.md` | Multiple hits, confirmed present via grep | VERIFIED |
| Auto-regulation 2-up/2-down rule | `c5097fef-9a41-4486-8bcd-967a91d6d6cf.md` | Character offset ~46125–46376 | VERIFIED |

## Method note

All quotes were located by reading the raw pasted-transcript text (the first
human message in each conversation file — a Merlin-AI-transcribed YouTube
transcript), never the assistant's synthesized/extracted output in the same
file. Where the transcript file uses per-line timestamps (`62bc60da`,
`99f7153d`), citations use the `MM:SS` marker on the line. Where the
transcript is one continuous block with no line breaks (`c5097fef`,
`73e73f97`), citations use an approximate character offset into the raw
message text, sufficient for a verifier to `grep`/search and land within a
few hundred characters of the quote.
