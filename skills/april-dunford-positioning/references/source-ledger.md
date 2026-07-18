# Source Ledger — april-dunford-positioning

**Purpose**: Verification labels for factual/provenance claims in genius.md and SKILL.md.

**Verification Tiers**
- **VERIFIED**: Verbatim or near-verbatim quote confirmed present in a source file by direct read.
- **LIKELY**: Pattern consistent across multiple statements in the source transcripts; not a single verbatim anchor.
- **UNCONFIRMED**: No source file exists to check against; flagged honestly rather than invented.

## Ground-Truth Sources (verified by direct file read, sizes recorded via `wc -c`)

| File | Bytes (`wc -c`) | What it is |
|---|---|---|
| `extractions/april-dunford/transcript-1-positioning.txt` | 70,905 | Full transcript, "The Marketing Expert: Sell Anything with this Trick \| April Dunford" (Lenny's Podcast), youtube.com/watch?v=vM_1G1LCotU |
| `extractions/april-dunford/transcript-2-sales-pitch.txt` | 98,005 | Full transcript, "A step-by-step guide to crafting a sales pitch that wins \| April Dunford" (Lenny's Podcast), youtube.com/watch?v=-VqmFI9vY7w |
| `extractions/april-dunford/transcript.txt` | 70,691 | Duplicate of transcript-1-positioning.txt minus the 4-line header (content-identical) |
| `extractions/april-dunford/extraction-report.md` | 14,683 | Prior MES extraction synthesizing both transcripts into 12 genius patterns + 8 hidden-knowledge items — this is the direct ancestor of `genius.md`'s existing (pre-repair) pattern list |

No `[Vendor Name]`-style timestamp markers exist in either transcript (checked: zero `[HH:MM]` matches, one bare digit match that is not a timecode) — quotes below are anchored to file + a text search string, not a timecode, because no timecode data exists to cite honestly.

## Anti-Patterns Added This Repair (all VERIFIED against the transcripts above)

| # | Claim | Tier | Source | Verified how |
|---|---|---|---|---|
| 1 | "brand positioning" / tagline conflation is April's stated pet peeve | VERIFIED | transcript-1-positioning.txt | Exact string "my personal pet peeve is when people talk about brand positioning that drives me nuts" found verbatim via grep |
| 2 | "biggest mistake is not deliberately positioning" / building in competitive isolation | VERIFIED | transcript-1-positioning.txt | Exact string found verbatim via grep |
| 3 | Premature category creation called "a disaster" | VERIFIED | transcript-1-positioning.txt | Exact string "companies that love the idea of category creation are attempting to create a category" found verbatim via grep |
| 4 | Hero's-journey story arc rejected for lacking a competitor slot | VERIFIED | transcript-1-positioning.txt | Exact string "the problem with that storytelling arc is there's kind of no competitor in there" found verbatim via grep |
| 5 | Generic trend-as-insight is not a real insight ("any competitor could start the same way") | VERIFIED | transcript-2-sales-pitch.txt | Exact string found verbatim via grep |
| 6 | Investor-pitch/future-tense framing misapplied to sales pitches | VERIFIED | transcript-2-sales-pitch.txt | Exact string "sales pitch is all about right now" found verbatim via grep |
| 7 | FOMO/urgency backfires on indecisive buyers (Matt Dixon / Jolt Effect / Gong data) | VERIFIED | transcript-2-sales-pitch.txt | Exact string "if a customer is indecisive throwing fomo into the mix makes it worse" found verbatim via grep; "Matt Dixon," "jolt effect," and "gong" also confirmed present nearby in the same file |

## Pre-Existing genius.md Content (not rewritten, carried forward)

| Claim class | Tier | Source | Notes |
|---|---|---|---|
| 12 Genius Patterns (Context-Before-Product through Best Rep Test Protocol) | LIKELY | extractions/april-dunford/extraction-report.md, §"Genius Patterns" | Prior extraction synthesis of both transcripts; not re-verified line-by-line this pass (out of scope — these checks already PASS the heartbeat audit: `named_entity_floor`, `verbatim_exemplars`) |
| 8 Hidden Knowledge items (Positioning IS Context-Setting through Investor vs. Sales Pitch) | LIKELY | extractions/april-dunford/extraction-report.md, §"Hidden Knowledge" | Same as above |
| Hall of Fame Exemplars (Unseen Cost Pitch, Champion's Internal Sell, Feature Dump anti-exemplar) | UNCONFIRMED | none found | These are constructed/composite illustrations, not verbatim transcript material — no source file contains them; labeled UNCONFIRMED rather than invented-as-fact. They read as constructed teaching examples in the original extraction, which is a legitimate use, but they are not April's own words. |
| Evolution Log entry (Positioning Siege Test, 2026-04-09) | VERIFIED | `workflows/positioning-siege-test.md` exists in-repo | Internal system record, not expert-sourced; confirmed the referenced workflow file exists |

## What Was NOT Found (verified absent, not assumed absent)

- No timestamp/timecode data in either transcript file (checked via `grep -c` for `[HH:MM]` pattern — zero matches in both files).
- No third source document beyond the two transcripts + extraction-report.md + the header-stripped duplicate — confirmed via `ls -la extractions/april-dunford/` (4 files total, sizes recorded above).
- No existing `references/` ledger or workflow-level source citations prior to this repair — confirmed via `ls skills/april-dunford-positioning/references/` before writing this file.
