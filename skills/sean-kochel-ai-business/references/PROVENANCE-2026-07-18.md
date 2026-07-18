# PROVENANCE — sean-kochel-ai-business repair

Anchor → source file + location. Every anchor below was opened and read this session
(see `references/source-ledger.md` for the full VERIFIED/LIKELY/UNCONFIRMED breakdown).

| Anchor (in genius.md, new content) | Source file | Location | Date |
|---|---|---|---|
| "Most builders think that better features automatically means more users... Quibby... raised $1.75 billion... died in 6 months... violated the six principles of persuasion by Robert Chelini" | `_archive/claude-export-2026-07-01.tar.gz:claude-export/normalized/conversations/23c8f9f6-e3e3-4aca-b0cf-7f2080e6b351.md` | human turn, transcript opening (lines 30-38 of extracted file) | 2025-10-28 (conversation created) |
| "This doesn't really tell me anything... Am I tired of remembering passwords? No, I'm not... I don't think they're doing a great job" | `_archive/claude-export-2026-07-01.tar.gz:claude-export/normalized/conversations/f551b192-de2c-4e6f-a552-66b97aebfd03.md` | human turn, Pick Key teardown (mid-transcript, line 30 of extracted file) | 2026-01-30 (conversation created) |
| "this seems very undifferentiated to me from other social media scheduling tools... I would like to see that type of information hoisted" | same file as above | human turn, Postsyncer teardown (mid-transcript, line 30) | 2026-01-30 |
| "instead of saying join thousands of customers, it would be a lot more effective to say join a group of founders just like you" | same file as above | human turn, "Yes!" book section (mid-transcript, line 30) | 2026-01-30 |
| "telling them, 'Hey, don't litter. There's a fine.' is actually a lot less effective... than to say, 'Most people don't litter here'" | same file as above | human turn, "Yes!" book section, framing example (mid-transcript, line 30) | 2026-01-30 |
| "No invented conversion-rate projections or fabricated statistics — impact is described qualitatively unless the user supplied real numbers" | `skills/sean-kochel-ai-business/references/prompts-v2/crown_jewel_01_diagnostic.md` | Quality Gate, line 133 | 2026-07-11 (refactored, per frontmatter) |
| "Scarcity implementation ties to a real, named constraint... never fabricated urgency" / "without inventing names, companies, or dollar figures" | `skills/sean-kochel-ai-business/references/prompts-v2/crown_jewel_03_cialdini.md` | Quality Gate, lines 133-134 | 2026-07-11 (refactored) |
| "'We use GPT-4 so we have AI' — this is a *feature*, not a moat..." | `skills/sean-kochel-ai-business/genius.md` (pre-repair) | AI Moat Decay Analysis section, line 29 | 2026-04-09 (git blame: commit a49fda981) |
| Recognition-test / How-to-Use section product references (Quibi, Dropbox, Notion, Stripe, Pick Key, Postsyncer) | Both archive conversation files above | throughout | 2025-10-28 / 2026-01-30 |

## Method note (per ENVELOPE source-search discipline)

`extractions/sean-kochel/` contains only `transcript.txt` (17,843 bytes, `wc -c`
confirmed) and `extraction-report-design-first-build.md` (13,417 bytes) — both fully
read and confirmed to be exclusively about `sean-kochel-design-first-build`, not this
skill (explicit "NO overlap" statement in the extraction report, line 12). Per the
SOURCE-SEARCH DISCIPLINE instruction, absence was not claimed from a directory listing
alone: `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, confirmed via
`wc -c`) was scanned member-by-member (7,720 files) with a Python `tarfile` per-member
content grep for `kochel` (case-insensitive), which surfaced the two primary sources
above plus four additional hits not used (see source-ledger.md §6, flagged
UNCONFIRMED-relevance rather than silently read or silently dropped).
