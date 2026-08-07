# Source Ledger — Dakota (Thief of Boredom) / dakota-content-design

## Where the ground truth actually lives (read this first)

`extractions/` has **zero** entries for Dakota or thiefofboredom — confirmed
2026-07-17 via `ls extractions/ | grep -i dakota` (0 results) and a full
`grep -ril "dakota|thiefofboredom"` across `extractions/` (0 hits). This is
the failure mode the envelope warns about: the skill's own `SKILL.md`
frontmatter claims `source: claude.ai export 2026-07-01` but no file at that
path is reachable from the live tree.

The primary source **does exist**, archived, not in `extractions/`:
`_archive/claude-export-2026-07-01.tar.gz` contains three raw Claude.ai
conversation transcripts where Dakota's own YouTube videos were pasted in
full and extracted. Verified by direct read (not by trusting a census file):

| Conversation ID | File (inside tar, path `claude-export/normalized/conversations/`) | Size (`wc -c`) | Video source | Created |
|---|---|---|---|---|
| `a718e600-4edb-4832-a55a-ebb02bc64932` | `a718e600-...932.md` | 63,508 bytes | "everything I know about creating viral carousels in 29 minutes" — `https://www.youtube.com/watch?v=kzu-QSaskK4` | 2025-12-16 |
| `141e8809-3391-4d56-8257-a753b1633182` | `141e8809-...182.md` | 55,234 bytes | same video, re-extracted in an earlier session | 2025-10-01 |
| `13b7362e-f27b-444d-a0a7-b51143f48786` | `13b7362e-...786.md` | 62,862 bytes | "what I learned from 20 million views on Instagram in 90 days" — `https://www.youtube.com/watch?v=N7iz-3UCJrY` | 2025-12-16 |

These were extracted for this repair (`tar -xzf` on the two matching IDs) and
read in full — every quote below was located verbatim in the transcript text
inside the human-turn message, not in the AI's summarized output. The AI
extraction turns in those files (the pre-existing `genius.md`/prompt content)
were themselves generated from these transcripts, which is why `genius.md`'s
patterns already read as grounded even without a `references/` file — this
ledger makes that grounding auditable instead of asserted.

## Claim-by-claim

| Claim (as it appears in SKILL.md / genius.md / AGENT.md) | Label | Basis |
|---|---|---|
| "grew from 180K to 250K+ Instagram followers in 2025" | VERIFIED | `a718e600`: "January 2025, I had 180K followers... I'm at like 247K now"; `13b7362e`: "I have 250,000 followers" — both figures independently confirmed across the two conversations. |
| "70K+ followers gained in 2025... 20M+ views in 90 days" | VERIFIED | `a718e600`: "I've gained nearly 70,000 followers on Instagram in 2025"; `13b7362e` title + body: "20 million views on Instagram in 90 days." |
| "54K followers and 11M views in a single month" (February) | LIKELY | `a718e600`: "from February to March alone, I had over 11 million views... I gained over 50,000 followers in that month. 54,000 new followers" (worded as Feb–March window). `13b7362e` states a different figure for the same period: "I had 11 million views in February alone... 50,000 followers in just February alone." The two sources disagree on 54K vs 50K and on whether it's Feb-only or Feb–March — genius.md's "54K" is sourced but not cross-confirmed. |
| "a 4.6M-view carousel on day three of the experiment" / Test-Verify-Scale numbers | VERIFIED | `13b7362e`, verbatim sequence: Feb 9 test "133,000 views... 893 sends or shares and 2,000 saves"; Feb 10 verify "three times increase... 350,000 views"; Feb 11 "4.6 million views on this carousel post... nine slides"; "got 24 23,000 followers" (≈23K). |
| "69K shares / 83K saves on 4.6M views" | VERIFIED | `13b7362e`: "318,000 likes, 69,000 shares, and 83,000 saves." |
| "~100 followers per solid post... ~3K/month... ~36K/year" | VERIFIED | `13b7362e`: "I probably get about a hundred followers at least per post... one post a day equals 3,000 followers... by the end of the year, I'm gaining 36,000 followers." |
| "+33K follows, −24K unfollows, net +8K" | VERIFIED | `13b7362e`: "an increase of... 33,000 new followers. Yeah, I've got 24,000 people who have unfollowed me, but that's a net growth of 8,000 followers." |
| "Some people work three years to get 10,000 views" | VERIFIED (near-verbatim) | `13b7362e`: "Some people work for three years to get 10,000 views." (genius.md drops "for," otherwise exact.) |
| Reels get "tested" on a follower slice; carousels reach actual followers + get pushed to Reels page + Explore | VERIFIED | `a718e600`: full paragraph beginning "On Instagram, carousels reach your actual followers... it kind of does this little test out on a few of your followers... which I think is just stupid." |
| "Other" analytics bucket = Reels-page distribution (881K of 1M example) | VERIFIED | `a718e600`: "That other 881,000 views, that other is the reals page... that other is coming from reals." |
| Second-chance slide re-serve mechanic | VERIFIED | `a718e600`: "Instagram is going to give them a second chance to see your post and show the next slide... Your reel does not do that." |
| Revelational vs Informative split, "tip #4" example | VERIFIED | `a718e600`: "if it's like five things you should do and you're like tip number four do this, no one's really going to share just tip number four." |
| "How I" beats "How to" hook framing | VERIFIED | `a718e600`: "flip the script and say how I, how I lost 10 pounds, how I lost 15 pounds in three weeks." |
| "realizations I made following Jesus in my 20s" hook example | VERIFIED | `a718e600`, verbatim phrase used as Dakota's own example hook. |
| Film treatment stack (blur radius 2/4, noise 15%, exposure −1.2, brightness down, B&W, paper texture last) | VERIFIED | `a718e600`: "radius of two on my blur... noise... amount of 15%... exposure about 1.2... bring the brightness down... paper effect... apply at the end"; separately, "box blur... I want it to be four here" for a sourced (non-selfie) image. |
| Canvas 2160×2700, grid 5 down/3 in, kerning −80 to −100, line spacing 18, lowercase + capital "I" | VERIFIED | `a718e600`: "2160 by 2700"; "five boxes down from the top and three boxes in from the side"; "line spacing, which I keep at 18"; "negative anywhere between negative 80 and 100"; "capitalize my eyes... keep everything else uh lowercase." |
| Pinterest vibe-mining, copy-paste into Photoshop, content-aware fill, artboard duplication, RAM/template management | VERIFIED | `a718e600`, full production-workflow section (Pinterest paste, "content aware fill," "option... or alt and click," RAM warning re: large files. |
| Rights boundary — will not sell prints of Pinterest-sourced images | VERIFIED | `13b7362e`: "I don't own the rights to the photos... no, I will not make prints out of these these graphics that I make." |
| Wendy's Diner rule (don't abandon a working format) | VERIFIED | `13b7362e`, full analogy: "it doesn't mean stop making pancakes all together and go try to be a French restaurant. That's stupid and you're going to fail." |
| "Faith-based creative business coach" descriptor | LIKELY | Not a verbatim self-label in either transcript. Inferred from consistent context: `13b7362e` references "a faith-based growth guide" he sells and repeated Christian-content examples ("things nobody told me about following Jesus," "spiritual maturity looks less like having answers"). Reasonable characterization, not a direct quote. |
| "DM me the word DACA on Instagram" (coaching CTA) | VERIFIED (as transcribed) | `a718e600`: literal transcript text, "DM me the word DACA on Instagram" — near-certainly a transcription artifact for "DAKOTA" by the Merlin AI auto-transcriber, but quoting it as written is accurate to the source. Flagging so it isn't mistaken for a real CTA if reused verbatim in client-facing copy. |
| Workflow files (`01-design-viral-carousel.md`, `02-write-standalone-slides.md`, `03-audit-carousel-performance.md`) and `references/prompts-v2/*` | UNCONFIRMED against these three transcripts | These appear to be downstream synthesis (the "Crown Jewel prompts" the AI generated from the transcripts inside `a718e600` and `13b7362e`, per those conversations' own artifact logs), not verbatim Dakota material. Not independently re-verified line-by-line in this repair pass — treat their specific numeric claims (e.g. "40+ search terms," time estimates) as AI-generated elaboration on top of VERIFIED core patterns, not Dakota quotes themselves. |

## Method note (for the adversarial verifier)

Every VERIFIED row above was located by direct string search inside the
extracted `.md` transcript files, not inferred from the pre-existing
`genius.md` prose. Extraction command used: `tar -xzf
_archive/claude-export-2026-07-01.tar.gz -C <scratch> claude-export/normalized/conversations/<id>.md`
for the three IDs listed in `_active/harness/claude-export/harvest/census-full.json`
entry `expert: "Dakota"`. File sizes above are `wc -c` on the extracted
files, not estimates.
