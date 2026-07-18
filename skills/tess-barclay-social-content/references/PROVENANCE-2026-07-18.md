# Provenance — tess-barclay-social-content repair (Wave 3 Lane 4 Batch 17)

Primary source for everything below: `_archive/claude-export-2026-07-01.tar.gz` → member
`claude-export/normalized/conversations/6c48787f-c4f5-4654-9625-e93a6ee8a882.md`
(extracted this session to a scratchpad copy for line-numbered reference; the tar member
itself has no stable line numbers, so anchors below cite the extracted scratchpad copy's
line numbers, which mirror the tar member's content 1:1 starting after its YAML frontmatter
at source line 12). Video: Tess Barclay, "2026 is the end of influencers & the start of
casual content.. here's what will work," Busy Blooming (YouTube), published 2025-11-28,
`https://www.youtube.com/watch?v=rR-mxDCDKBQ` (transcript captured via Merlin AI).

Found by: content-scanning `_archive/claude-export-2026-07-01.tar.gz` (7,720 files) via
Python `tarfile` for the phrases "sweatsuit," "polished casual," "older sibling," "corner
of social media," and "end of influencers" — none of which appear anywhere in
`extractions/tess-barclay/transcript.txt` (that file is a different, unrelated Tess Barclay
video about using Claude the AI product; see `references/source-ledger.md` item 1).

## Anchor Table (genius.md Anti-Patterns section)

| genius.md item | Source line(s) (scratchpad copy) | Verbatim source text |
|---|---|---|
| Aesthetic-influencer content dying | ~371-373 | "I think we are experiencing truly the death of the aesthetic influencer and the birth of polished human content" |
| Personalityless aesthetic filler | ~406-411 | "you're seeing all this like aesthetic content that's just like morning routines and aesthetic Sunday resets, aesthetic all this like kind of personalityless content, I don't think we'll win" |
| Expert-tone vs. testimony | ~736-741 | "not from this place of like here's what you're going to do to clear your skin, but more from like this human place of like, okay, I have tried everything in the world to clear my skin and these are the five products I'm obsessed with" |
| Heavily edited/graphics short-form losing | ~578-586 | "content...that's like really highly edited with like clicks and a bunch of graphics and all this stuff. I don't think that will win as much as just a simple backflipped quick 30-second video talking about something real" |
| No-voiceover Pinterest morning routines dying | ~485-489 | "Here's my perfect aesthetic, no voice over timestamped Pinterest come to life morning routine. I think that's going to die in 2026" |
| Topic-bucket "niching down" rejected | ~315-325 | "The reason I hate the advice niching down so much is because a niche in traditional marketing, a niche is not a topic... you're picking one big bucket of like fitness or fashion or whatever it is" |
| Demographic-first targeting outdated (Sprout Social) | ~337-353 | "Sprout Social did this report... influencer discovery for brands will no longer be rooted in demographic... 'we want a creator who has women who are 20 to 30 who live in Canada.' Like that's not what they're interested anymore" |
| Course-first monetization discouraged | ~803-809 | "I wouldn't necessarily recommend a course because I feel like sometimes that can hold back your content and it's maybe a little bit outdated depending on like what you do" |

## Anchor Table (genius.md Genius Patterns + Hidden Knowledge, spot-checked)

| genius.md item | Source line(s) | Verbatim source text |
|---|---|---|
| "Niche is an audience, not a topic" | ~316-319 | "a niche in traditional marketing, a niche is not a topic. A niche is talking about a niche audience and a niche market" |
| "Sweatsuit in 4K" | ~415-417 | "sitting in your apartment in a sweatuit but in 4K" (source has transcription typo "sweatuit"; genius.md corrects spelling only) |
| $25/month Busy Blooming HQ | ~640-642 | "It's $25 a month" |
| Weekly Q&A, Tuesday noon EST | ~849-851 | "We do a Q&A every Tuesday at noon EST" |
| ~15-minute YouTube sit-downs + IG cascade | ~747-751 | "I would do sitdown videos on YouTube that are about 15 minutes long. And then I would do Instagram carousels and short form video extended from that" |
| Screen-time discipline / feed cleansing | ~453-461 | "people are getting more strict with their screen time... cleansing their feeds of anything that doesn't make them feel really great" |
| "Frozen by opportunity" | ~268-270 | "you do I see this all the time get frozen by opportunity because there are so many different platforms" |

Line numbers are approximate (±3 lines) because the scratchpad extraction preserves the tar
member's own line breaks verbatim; all quotes above were confirmed present via direct
`Read` of the extracted file this session, not estimated from memory.

## Known Provenance Gap (flagged, not silently dropped)

`extractions/tess-barclay/transcript.txt` (27,447 bytes per `wc -c`) exists but is NOT the
source used above — it is a different Tess Barclay video (a "how creators should use
Claude" walkthrough). `agents/tess-barclay/memory/context.md` claims the primary source is
the "2026 is the end of influencers" transcript, which matches the archive file used here,
not the file currently sitting in `extractions/tess-barclay/`. This repair worker did not
rename, delete, or overwrite `extractions/tess-barclay/transcript.txt` (out of scope, and
git-write is disallowed for this worker) — flagging it here for the conductor to decide
whether to backfill the correct transcript into `extractions/` from the archive.
