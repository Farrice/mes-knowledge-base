# PROVENANCE — patrick-dang-online-business repair (Wave 3 Lane 4 Batch 13, 2026-07-18)

Anchor → source file + location table. Primary source (S1) confirmed via
`python3 -c "import tarfile; ..."` per-member scan of `_archive/claude-export-2026-07-01.tar.gz`
(7,728 members, scanned for literal `Patrick Dang`, 13 hits by content, filenames don't
carry the expert name so filename-only search would have missed all of them).

| Anchor in genius.md | Source | Location |
|---|---|---|
| "sitting on a gold mine" | S1 | `7ea68873-...md`, transcript body, ~line 30 region (single-block transcript, located via regex `re.finditer`) |
| "each box is a skill you need to start a business" | S1 | same file, "boxes" passage |
| "cannot be explained in one sentence... ended the call" | S1 | same file, sales-call anecdote passage |
| Restaurant/kitchen metaphor | S1 | same file, "restaurant"/"kitchen" passage (8 kitchen hits, 10 restaurant hits) |
| "one traffic source, one conversion method, and one offer" | S1 | same file, One-One-One passage |
| "3 days later that video is dead" / binge-watch | S1 | same file, short-form vs. long-form passage |
| "you never want to charge by the hour" | S1 | same file, pricing passage |
| "193,000 learners... 70,000 reviews" | S1 | same file, Udemy history passage |
| "693 YouTube subscribers and 3,528 LinkedIn followers... $7,000 per month" | S1 | same file, Yvon example |
| Matcha ice-cream shop flop | S1 | same file, origin-story passage (5 "matcha" hits) |
| "version one's not going to look pretty... becomes a machine" | S1 | same file, flywheel passage |
| "are you here for the content, or are you looking to..." | S1 | same file, DM-hack passage |
| "I don't want to disappoint them... big step" | S1 | same file, call-friction passage |
| "I'm Asian, right?... universities in Asia" | S1 | same file, positioning-by-contrast passage |
| "fonts, the colors, your color grade... taste" | S1 | same file, taste passage |
| "this is Brandon and 30 days ago..." | S1 | same file, social-proof passage |
| Tyler — "56K in 60 days" | S1 | same file, Tyler network-first passage |
| "army of five full-time employees" | S1 | same file, AI passage |
| 7 Anti-Pattern bullets (new section) | S1 | same file, each cited inline with the specific verbatim quote used |

**S1 identity**: YouTube video "The Most Overlooked $10K/Month Online Business Anyone Can
Start (Even With a 9-5)" by Patrick Dang (`https://www.youtube.com/watch?v=lHfsW17Z7g0`),
Merlin AI transcript, captured in claude.ai conversation id
`7ea68873-caed-4cd8-af6f-a95e19d1aa7f` (created 2025-12-23T15:24:15Z), archived at
`_archive/claude-export-2026-07-01.tar.gz` →
`claude-export/normalized/conversations/7ea68873-caed-4cd8-af6f-a95e19d1aa7f.md`,
117,861 bytes (size confirmed via `TarInfo.size` at scan time, 2026-07-18).

**Note on prior "3.5K" approximation**: genius.md previously read "693 YouTube
subscribers and ~3.5K LinkedIn followers." Source has the exact figure 3,528 — updated
to the precise number in this pass since precision was available and unused.

**Note on d4094ca5 (Calum Johnson interview)**: located in the same archive search,
genuinely a Patrick Dang source (130-minute interview), but not traced as the origin of
any specific pattern in this skill — flagged UNCONFIRMED as a contributor rather than
claimed as grounding, per the "false unrecoverable/absent claims" hard rule in the
envelope. It was opened and read (81,057 bytes), not left unread-and-assumed-irrelevant.
