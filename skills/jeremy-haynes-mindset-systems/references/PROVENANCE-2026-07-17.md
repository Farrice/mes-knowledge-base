# Provenance — jeremy-haynes-mindset-systems repair

Anchor table: every quote/figure added or newly cited in this repair pass, mapped to exact source location. All char offsets located by direct Python string search against the transcript file, 2026-07-17 (file is a single continuous line with no newlines, so offsets substitute for line numbers — verify with `text[offset-50:offset+300]` against `extractions/transcripts/_wmR2nfNhAE.txt`).

| Anchor | Quote / Claim | Source File | Location | Confidence |
|---|---|---|---|---|
| A1 | "I'm on Jeremy 47.0 right now... intentionally done this exercise" | `extractions/transcripts/_wmR2nfNhAE.txt` | char ~100672 | VERIFIED |
| A2 | Jim Rohn's 1981 Anaheim presentation origin of Reasons Engine | `extractions/transcripts/_wmR2nfNhAE.txt` | char ~73563 (transcribed "Jim Ran") | VERIFIED |
| A3 | Daniel Goleman, *Vital Lies, Simple Truths* | `extractions/transcripts/_wmR2nfNhAE.txt` | char ~9499 (transcribed "Daniel Gleman") | VERIFIED |
| A4 | Richard Bandler, *Using Your Brain for a Change* | `extractions/transcripts/_wmR2nfNhAE.txt` | char ~15743 (transcribed "Richard Banler") | VERIFIED |
| A5 | Three Birkin bags, $25K + $30K + $24K | `extractions/transcripts/_wmR2nfNhAE.txt` | char ~60981 | VERIFIED (verbatim) / UNCONFIRMED (financial fact) |
| A6 | Fired 23 of 27 staff, kept 4 | `extractions/transcripts/_wmR2nfNhAE.txt` | char ~45726 | VERIFIED (verbatim) / UNCONFIRMED (underlying financials) |
| A7 | "Refunded about 109K worth of deals... I don't remember the exact number" | `extractions/transcripts/_wmR2nfNhAE.txt` | char ~33469 | VERIFIED (self-caveated) |
| A8 | "Dropped about 300 grand" over sewage smell + "104,500" lease break | `extractions/transcripts/_wmR2nfNhAE.txt` | char ~58215–58600 | VERIFIED (verbatim) / UNCONFIRMED (as fact) |
| A9 | Traffic-stop story: rage → workout → "just want to say thank you, officer" handshake | `extractions/transcripts/_wmR2nfNhAE.txt` | char ~84408 (stop) through ~87090 (workout/thank-you) | VERIFIED |
| A10 | "Your subconscious fires 20 to 40 million neurons a second... 20 to 40 thousand" (Dr. George Pratt) | `extractions/transcripts/_wmR2nfNhAE.txt` | char ~69582–69792 | VERIFIED (self-caveated: "I don't know if this is accurate or not") |
| A11 | "12 to 15 people tops" current deal capacity | `extractions/transcripts/_wmR2nfNhAE.txt` | char ~39630 | VERIFIED |
| A12 | Walls-closing-in / "100% no matter what going to die" mortality frame | `extractions/transcripts/_wmR2nfNhAE.txt` | char ~107611–111833 (squeeze/walls passage) | VERIFIED |
| A13 | "Camry and a double wide trailer" demonized reference figure | `extractions/transcripts/_wmR2nfNhAE.txt` | char ~65976 | VERIFIED |
| A14 | Transcript word count 22,682 | `extractions/transcripts/_wmR2nfNhAE.txt` | whole-file `len(text.split())` | VERIFIED (computed directly, 2026-07-17) |
| A15 | Company identity: Megalodon Marketing, Inner Circle, Master Internet Marketing are real | `skills/jeremy-haynes-cold-offer/references/source-receipts.md` | verification brief dated 2026-07-15 | VERIFIED (reused from sibling skill's verification pass) |
| A16 | quality-rubric.md 3-tier scale (Score 4 / 7 / 10) | `skills/jeremy-haynes-mindset-systems/references/quality-rubric.md` | table header, lines 1-8 | VERIFIED (direct file read) |

## Method note

All quotes above were located by exact or near-exact substring search (`str.find` / `grep -c -F`) against the raw transcript text, then read in ±150-400 char context windows to confirm the surrounding sentence matches the claim before it was added to genius.md or the source ledger. No quote was added on recall alone. Two names in the transcript are clearly mis-transcribed by the auto-captioning (Jim Rohn → "Jim Ran"; Daniel Goleman → "Daniel Gleman"; Richard Bandler → "Richard Banler") — these are flagged inline in the source ledger rather than silently corrected, since the mis-transcription itself is evidence the claim is genuinely auto-generated, not fabricated after the fact.
