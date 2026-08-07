# Source Ledger — Pat Flynn: Passive Income Architecture

Repair pass, Wave 3 Lane 4 Batch 13 (2026-07-17/18). Ground-truth check per envelope: `ls extractions/ | grep -i flynn` and `find . -iname "*pat*flynn*"` return **no dedicated Pat Flynn extraction folder** under `extractions/` — the skill's own frontmatter records `source: claude.ai export 2026-07-01`, pointing at the bulk Claude conversation archive, not a standalone extraction.

That archive was located and read directly (not assumed empty): `_archive/claude-export-2026-07-01.tar.gz` (317MB) contains a normalized-conversations tree at `claude-export/normalized/conversations/*.md`. `_active/harness/claude-export/index.json` lists 21 Pat Flynn-titled conversations. Five were opened this pass via `python3 tarfile` per-member extraction (member name, decompressed size recorded below) and grepped for the claims already asserted in `genius.md`. The remaining ~16 Pat Flynn conversations in the archive were **not** opened this pass — claims traceable only to those are labeled UNCONFIRMED, not silently assumed true.

## Sources Opened (size = decompressed member size, confirmed non-zero)

| # | Conversation title | Created | Archive member | Size |
|---|---|---|---|---|
| 1 | MES 3.0-Pat Flynn: Building Actual Passive Income | 2025-06-21 | `claude-export/normalized/conversations/fa99b805-bab2-48ca-909f-455969b0cd69.md` | 183,789 bytes |
| 2 | Pat Flynn: My honest advice for anyone who wants passive income | 2025-06-21 | `claude-export/normalized/conversations/fc4bf858-d643-4f92-9b4c-fc56af88302d.md` | 71,783 bytes |
| 3 | Pat Flynn: How Lean Learning Created a Million-Dollar Empire | 2025-06-20 | `claude-export/normalized/conversations/dfab4324-a28d-4ef2-b534-4ff89aa5257f.md` | 135,110 bytes |
| 4 | Pat Flynn: Your Path to Simple Passive Income | 2025-07-04 | `claude-export/normalized/conversations/c2e8b7ad-2146-4f5e-962e-82e43d315220.md` | 99,713 bytes |
| 5 | Fresh-Pat Flynn on How to Attract Superfans to Future-Proof Your Business | 2025-07-04 | `claude-export/normalized/conversations/90a84bdf-b478-4882-aba5-5ae3d471cbd5.md` | 74,958 bytes |

Files 1-3 and 5 are raw Merlin-AI YouTube transcripts pasted into Claude by the user (timestamp-marked, unpunctuated auto-caption style — genuine primary source, Pat Flynn's own spoken words). File 4 is the same transcript style. None are 0-byte or unrecoverable; the claim-search below is grounded in an actual read, not an assumption of absence per the envelope's rule against false "unrecoverable" claims.

## Claim-by-Claim

| # | Claim | Location | Label | Basis |
|---|---|---|---|---|
| 1 | "the biggest mistake... is well, what should I sell" | `genius.md` Anti-Patterns, item 1 | VERIFIED | Source #1, transcript lines matching timestamp 7:45-7:52 (grep-confirmed verbatim) |
| 2 | "many people just choose products because it has a really high commission... not because it's actually helpful" | `genius.md` Anti-Patterns, item 2 | VERIFIED | Source #1, timestamp 12:29-12:41, verbatim (near-exact; original transcript reads "...it's going to make them a lot of money but... you're just promoting things because it's making money not because it's actually helpful") |
| 3 | Universal "bug spray"/"kill all bugs" didn't sell; relabeled ant/cockroach/fly spray sold; "serves everybody... serving nobody" | `genius.md` Anti-Patterns, item 3; also Genius Patterns "Bug-Spray Specificity" | VERIFIED | Source #1, timestamps 11:09-11:37 and 22:08-22:12, verbatim |
| 4 | "A lot of us consume just in case" vs. just-in-time; "shiny object syndrome" | `genius.md` Anti-Patterns, item 4; Genius Patterns "Just-In-Time Learning" | VERIFIED | Source #4, timestamp 24:01-24:30, verbatim. Overlapping "knowledge hoarding" phrasing also present in Source #3, timestamp 22:02-22:08 |
| 5 | "a funnel is very soulless in my opinion... we often remove the heart" | `genius.md` Anti-Patterns, item 5 | VERIFIED | Source #5, timestamp 12:33-12:51, verbatim |
| 6 | First month made $7,908.55 from a $29 ebook; "the FBI is going to come and knock on my door" | `genius.md` Anti-Patterns, item 6; Hidden Knowledge "Success That Feels Illegal" | VERIFIED | Source #1, timestamp 5:19-5:59, verbatim |
| 7 | "This is an awesome life, but it's not my awesome life" (Airport Test / declined CEO seat) | `genius.md` Genius Patterns "The Airport Test" | VERIFIED | Source #1, timestamp 46:37-46:40, verbatim ("okay with it this is an awesome life but it's not my awesome life") |
| 8 | "Hurt people hurt people" | `genius.md` Hidden Knowledge "The Hater→Superfan Conversion" | VERIFIED | Source #1, timestamp 20:10, verbatim; also recurs in Source #3, timestamp 58:02-58:10 |
| 9 | "You can't read the label when you're inside the bottle" | `genius.md` Hidden Knowledge "The Mastermind Hot Seat" | VERIFIED | Source #1, timestamp 31:25-31:27, verbatim |
| 10 | "Serve first... it always pays you back in one way or another over time" | `genius.md` Genius Patterns "Serve-First Monetization" | VERIFIED | Source #1, timestamp 12:42-12:49, verbatim ("serve first is one of my phrases it always pays you back in one way or another over time") |
| 11 | "If you can't find one, how are you going to find a hundred, a thousand, ten thousand?" (1-1-1 pattern) | `genius.md` Genius Patterns "The 1-1-1 Validation Strategy" | UNCONFIRMED | Not found verbatim in the 5 sources opened this pass. A closely related line IS confirmed in Source #1 timestamp 22:29-22:31 ("it's better to find one than 10 than 100"), which supports the underlying claim but not this exact phrasing — this exact sentence was not re-verified and should not be treated as a locked quote until a source surfaces it |
| 12 | SwitchPod / Deep Pocket Monster subscriber and revenue figures ("tens of thousands sold," "1M+ subs") | `genius.md` Genius Patterns "The 20% Itch Rule" | UNCONFIRMED | Pre-existing claim; not located in the 5 sources opened this pass. 16 additional Pat Flynn conversations remain in the archive unopened — plausible but not re-verified this session |
| 13 | "Storytelling is going to be the most powerful number one skill..."; Jay Abraham pairing; Pokemon/Ford Field pitch line | `genius.md` Genius Patterns "Storytelling as the Master Skill," "Immerse Before You Create" | UNCONFIRMED | Pre-existing claims; several dedicated storytelling-titled conversations exist in the archive (e.g. "The No. 1 Skill For Anyone to Learn," multiple versions) but were not opened this pass — not re-verified, not contradicted |
| 14 | "An egg broken from the outside, life ends..."; MKBHD reference; Michael Hyatt as named virtual mentor | `genius.md` Hidden Knowledge "Judge Inputs, Not Numbers," "The Mastermind Hot Seat" | LIKELY / UNCONFIRMED | "Hyatt" confirmed present in Source #1 (timestamp 30:09, "Hyatt he's like a leader of leaders") supporting the mastermind claim generally (LIKELY); the egg metaphor and MKBHD reference were not located in the 5 sources opened and are UNCONFIRMED |
| 15 | Fiverr 15-year-old Fortnite coach; "model student left a conference after lunch" | `genius.md` Genius Patterns "Just-In-Time Learning" | UNCONFIRMED | Pre-existing claim; not located in the 5 sources opened this pass |
| 16 | Workflow files (3 total) carry Output Schema/Contract + Quality Gate | `workflows/*.md` | VERIFIED | Passed pre-existing heartbeat check (`workflow_contracts`); not modified this pass |

## Gap Named

The failure this protocol guards against is invented provenance. This pass verified 10 of the skill's core claims verbatim against real transcript files pulled by member name out of the actual archive tarball (sizes recorded above, none zero or missing), and it explicitly UNCONFIRMED five pre-existing claims (rows 11-15) rather than assert them as sourced. Those five are not contradicted — they read as plausible Pat Flynn material and were left in place per the additive-first/no-deletion boundary — but until one of the ~16 unopened Pat Flynn conversations in `_archive/claude-export-2026-07-01.tar.gz` is read and cross-checked, they should not be cited as VERIFIED quotes.
