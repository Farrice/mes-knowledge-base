# Provenance — Tim Danilov: Niche Bending Repair

Anchor → source file + location. Full claim-by-claim table lives in
`references/source-ledger.md`; this is the compact anchor map for the new
content added in this repair pass.

| Anchor (as written in genius.md) | Source file | Location |
|---|---|---|
| "a topic like I have a gardening channel" | `extractions/niche-bending/transcript.txt` | Line 1, ~180 words in ("Most people think a niche is just a [music] topic like I have a gardening channel.") |
| "Do not bend a format you cannot deliver the expertise in." | `extractions/niche-bending/transcript.txt` | Line 1, ~1,750 words in (rule-of-the-video sentence, immediately preceded by "There is one rule in niche bending that matters more than anything else.") |
| "Anyone can copy a format, but very few can fill the formats with high value knowledge." | `extractions/niche-bending/transcript.txt` | Line 1, immediately after the dentist/toothpaste example |
| "don't try to use a finance format if you don't understand money" | `extractions/niche-bending/transcript.txt` | Line 1, same sentence cluster as the expertise-constraint rule |
| "you're competing against the likes of National Geographic" | `extractions/niche-bending/transcript.txt` | Line 1, in the Tazoo/nature-documentary passage |
| "this isn't due to a lack of interest. It's an opportunity" | `extractions/niche-bending/transcript.txt` | Line 1, in the empty-square grid-mapping passage |
| 2026-02-16 publish date | `_active/harness/codex-harvest-2026-06-11/extractions/video-context/fLDrB_wmbNE/metadata.json` | `upload_date`/`publish_date` fields: `"20260216"` |
| Video title "The NEW YouTube Strategy Dominating in 2026" | same `metadata.json` | `title` field |
| Video URL `https://www.youtube.com/watch?v=fLDrB_wmbNE` | same `metadata.json` | `webpage_url` field |
| Uploader "vidIQ" | same `metadata.json` | `uploader`/`channel` fields |
| Case-study numbers ($56K/mo/30 days; 150M views; $23K/<90 days) | `extractions/niche-bending/transcript.txt` | Line 1, opening ~60 words |
| Finn's Play / Minecraft Wolf / Spider-Man NPC chain + view counts | `extractions/niche-bending/transcript.txt` | Line 1, empty-square-method passage, mid-transcript |
| Vegas-casino VidIQ AI-coach demo | `extractions/niche-bending/transcript.txt` | Line 1, closing third of transcript |
| "Unboxing Your First Roth IRA" example | **not found in any source** | See `references/source-ledger.md` — labeled UNCONFIRMED, flagged in-line in `genius.md` with a provenance note |
| "A Comprehensive Guide to Investing for Beginners" anti-exemplar | **not found in any source** | See `references/source-ledger.md` — labeled UNCONFIRMED, flagged in-line in `genius.md` with a provenance note |

All quotes above were verified verbatim by direct grep/read against
`extractions/niche-bending/transcript.txt` (11,053 bytes, confirmed via
`wc -c`, not a truncated or zero-byte file).
