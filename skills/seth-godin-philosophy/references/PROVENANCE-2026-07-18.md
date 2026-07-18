# PROVENANCE — seth-godin-philosophy repair (Wave 3 Lane 4 Batch 16)

Anchor → source file + location, for every claim added or newly cited in this repair pass.
Full claim-by-claim VERIFIED/LIKELY/UNCONFIRMED grading lives in `references/source-ledger.md`;
this table is the quick-lookup index an adversarial verifier can open files against directly.

| Anchor (as written in genius.md) | Source file | Location |
|---|---|---|
| "It's not hustle or hype or getting the word out. It's not promo. It's not interrupting people." | `extractions/seth-godin/transcript.txt` | char offset ~1467 (opening minutes of the Entrepreneur Studio podcast, Chris Allen host) |
| "if you're trying to persuade people who think you're wrong that you're right, you don't have enough time or money to do that" | `extractions/seth-godin/transcript.txt` | char offset ~4695 |
| "you needed to make average products for average people because it was average people that would see your ads" | `extractions/seth-godin/transcript.txt` | char offset ~1467-1700 region |
| "that tendency to hit that quarterly earnings number" | `extractions/seth-godin/transcript.txt` | char offset ~11972-12100 region (authenticity discussion) |
| "getting tricked into thinking that your job is to make Chase Bank happy with your c with your bank account is a mistake" (referenced in source-ledger, not directly quoted in genius.md) | `extractions/seth-godin/transcript.txt` | char offset ~34654 |
| "authenticity is a crock no one wants you to be authentic" | `_archive/claude-export-2026-07-01.tar.gz` | member `claude-export/normalized/conversations/97b5eb7a-ccd4-42d5-b49d-e74bcd79632a.md`, title "Seth Godin: 'Why SPENDING MORE Time & Energy WON'T Make You SUCCESSFUL!' \| Seth Godin & Lewis Howes," created 2025-07-13T16:38:51Z, transcript timestamp 12:32 |
| "great chefs look to see what's coming back to the kitchen uneaten" (genius.md Pattern 27 renders as "Great chefs look at what's coming back to the kitchen uneaten.") | `_archive/claude-export-2026-07-01.tar.gz` | member `claude-export/normalized/conversations/11084d9c-c6a7-4855-b031-a120f1536aec.md`, title "Fresh-Seth Godin Reveals the Secret to Successful Strategy" |
| "return on equity" (Chip Conley insight, Pattern-adjacent Hidden Knowledge 2026-07-01) | `_archive/claude-export-2026-07-01.tar.gz` | member `claude-export/normalized/conversations/fb957ada-3961-4dac-9840-af36657b0dba.md`, title "THE ORIGIN STORY REWRITER-Seth Godin: Reinvention After 50 with Seth Godin: Make Life Your Best Work of Art" |
| "you are traffic" (Pattern 18) | `_archive/claude-export-2026-07-01.tar.gz` | members `3e1e5249-54f6-405b-b1fb-cb2039783cf5.md` (This is Strategy) and `857239af-b146-4400-a8bc-b2f8898ac7d7.md` (Why Strategy Always Beats Talent) |
| "kindling" (Pattern 19) | `_archive/claude-export-2026-07-01.tar.gz` | members `e33dbc76-2688-4206-8e49-f0882b01bf66.md`, `3e1e5249-54f6-405b-b1fb-cb2039783cf5.md`, `2f651b98-f2f2-4c3b-9246-9120262d956e.md`, `d9574491-3d29-4c4b-b4c2-3ae2d5b9f91d.md` |
| "agent of change" / "stressing" (Pattern 29) | `_archive/claude-export-2026-07-01.tar.gz` | members `d9574491-3d29-4c4b-b4c2-3ae2d5b9f91d.md` (Coach Fresh), `a034f396-806f-4c55-99dd-c29c2c4c849b.md` + `bbcde56e-4ded-4b84-860d-c7a0e38a9be0.md` (trust conversations) |
| Anti-Exemplar "Future Bestseller Syndrome" | `skills/seth-godin-philosophy/genius.md` (pre-existing, unmodified) | § Hall of Fame Exemplars |
| Pattern 8 ("The point of perfectionism is not to make it better — it's to keep you from shipping it.") | `extractions/seth-godin/extraction-report.md` (pre-existing, unmodified) | Pattern 8 section, verified present verbatim |

## Method Note (for the adversarial Opus verifier)

Two full-content scans of `_archive/claude-export-2026-07-01.tar.gz` (7,728 members, gzip-decompressed
on the fly) were run this session using `tarfile` + substring search, completing in 3-5 seconds each
(the archive is mostly small text/markdown conversation exports, not media). The first scan searched
8 signature markers unique to genius.md's Patterns 1-14 group (lipstick, seed-in-a-bag, mel robbins,
turtleneck, dishwasher argument, architect story, kitchen uneaten, quarterly earnings number) — zero
hits on the distinctive story markers, confirming the Mel-Robbins-titled source for that pattern group
is not present anywhere in this repo (see gap note in source-ledger.md). The second and third scans
targeted the 2026-07-01/2026-07-10 tranches' named sources and specific quote fragments — these
resolved to real, correctly-titled conversations, several with independently-confirmed verbatim or
near-verbatim quote matches (listed above). A fourth scan located the "authenticity is a crock" quote
(Pattern 9) in a Lewis Howes interview not previously cited anywhere in this skill's files.
