# Source Ledger — Maria Wendt: Digital Product Mastery

Every source consulted during the Wave 3 Lane 4 Batch 10 repair (2026-07-18), with a
VERIFIED / LIKELY / UNCONFIRMED label per claim cluster. Sizes from `wc -c`; tarball
contents inspected via `python3 tarfile` per-member scans (never shell `tar -x` on the
whole archive — 7,720 members).

## VERIFIED — read in full, quotes checked against file text

| Source | Size | What it grounds |
|---|---|---|
| `extractions/maria-wendt/transcript.txt` | 11,751 bytes | "Give me 10 minutes and I'll get you your first digital product sale" (YouTube video transcript, first-person). Grounds Genius Patterns 1 (Research-First Kill Switch — "who struggles with what when trying to do something"), 2 (Destination Painting), 4 (MVP in 60 minutes, "good enough is good enough"), 7 (headline structure examples), 8 (Find-One-Help-One outreach script, verbatim), 9 (Identity Shift $5-$10 product, ThriveCart mention). Her own first-product origin story (single-serve recipe book) is verbatim in this file. |
| `extractions/maria-wendt-2/transcript.txt` | 12,443 bytes | "I've made over $3 million selling digital products... 36 lessons" (YouTube video transcript, first-person, numbered list format). Grounds Genius Patterns 3 (Value-Anchored Pricing), 5 (Trust Depth / warm audience), 6 (Pre-Sell Validation Gate), 10 (Product Ladder). Grounds nearly all "Hidden Knowledge" bullets (Passion Trap, Feature Gravity Well, Perfectionism Tax, 3-Second Confusion Kill, Message-Market Fit, Shortcut Framing, Overbuild-Undersell, Real Urgency Only, First 10 Customers) — these are Wendt's own numbered lessons 1-36, quoted close to verbatim in genius.md. |

## LIKELY — genuine primary source located, not re-verified line-by-line this pass

Found via `python3 tarfile` per-member text scan of `_archive/claude-export-2026-07-01.tar.gz`
(7,720 members; filtered on the fragment `wendt` with no punctuation, then narrowed by
distinctive keyword co-occurrence). These are real Maria Wendt YouTube transcripts
(several via Merlin AI transcription) pasted as attachments into prior Claude
conversations — genuine primary material, but not copied into `extractions/` and not
re-checked verbatim against every genius.md claim during this repair (time-boxed to the
two files above as the anchored ground truth). Recommend a follow-up extraction pass to
promote these into `extractions/maria-wendt-3` etc. if the skill needs deeper grounding.

| Conversation file (in tarball) | Title | Size |
|---|---|---|
| `claude-export/normalized/conversations/838c2c5d-e657-42a6-a4e2-a9bebc878923.md` | "FC/VP-Maria Wendt: How to Start An Automated Business Selling Digital Products (Your First 3 Days)" — attached raw Merlin AI transcript | 25,751 bytes |
| `claude-export/normalized/conversations/4f070a7f-370d-4071-9b79-37aa1cfc5705.md` | "Digital Products-Maria Wendt: My Successful $13M Digital Product Funnel (Copy Me!)" | 47,927 bytes |
| `claude-export/normalized/conversations/feb31fab-6445-4996-84c7-593905fdb67f.md` | "Digital Products-Maria Wendt: Step-By-Step: How To Make Your First $500 Selling Digital Products" | 48,294 bytes |
| `claude-export/normalized/conversations/5fb4d480-659e-41d5-ab0c-3d6145cd069d.md` | "Maria Wendt: How I Gained 400K Instagram Followers In 22 Months (7 Key Lessons)" | 42,221 bytes |
| `claude-export/normalized/conversations/03cb447e-5909-412e-a357-29b9f4ac444c.md` | "Maria Wendt: How To Automate 1 Sale Every Day" | 57,675 bytes |
| `claude-export/normalized/conversations/43b95751-4673-48ed-af6f-2c7d0c43bc10.md` | "Maria Wendt: How To Sell Low-Ticket Products (When You've Only Sold High-Ticket Offers)" | 62,649 bytes |
| `claude-export/normalized/conversations/3677c60f-308d-4eaf-8d2e-ca16f5807994.md` | "SVP-Maria Wendt: Turn 1 Digital Product Into 5 Income Streams" | 23,934 bytes |
| `claude-export/normalized/conversations/ab42baba-d940-4f7a-a432-acb8d3f88a7f.md` | "If I Needed $100 Fast, I'd Do This Digital Product Strategy" | 37,130 bytes |
| `claude-export/normalized/conversations/f23f584f-8c5a-4e62-a3dd-a512e3bb1d94.md` | "Coach Fresh/VP-Maria Wendt: How To Create A Viral Digital Product" | 62,988 bytes |
| `claude-export/normalized/conversations/5ff77dd8-35c1-493b-8b6d-a45c0412de3e.md` | "150 Instagram Reel Hooks To Attract Buyers (Not Viewers)" | 64,833 bytes |
| `claude-export/normalized/conversations/15bf3181-2f31-4a0d-951f-5443f5f0cdde.md` | "DP-Maria Wendt: The Ultimate Guide To Instagram Captions (to make money)" | 39,107 bytes |

Claim: "$13 million" gross revenue figure and "student Brooke... a million dollars" —
present verbatim in `838c2c5d-...md` transcript attachment (Wendt's own words, spoken
directly to camera). LIKELY VERIFIED but not cross-checked against a second source, so
kept at LIKELY rather than promoted to VERIFIED.

## UNCONFIRMED — traced to source, but the source is a prior AI's own invention, not Wendt

**Section: genius.md, "Patterns from claude.ai export — Maria $600K/month System"
(Genius Patterns 11-16 + "Hidden Knowledge (export layer)")** — Tri-Channel Revenue
Split, $5 Ad Validation Kill Switch, Email Psychology Rhythm, Vulnerability-Profit
Paradox, Micro-Trust Mechanics (17-second pause / number specificity / lowercase
confidence), Content Multiplication Batch Week.

Investigation: scanned all 7,720 members of `_archive/claude-export-2026-07-01.tar.gz`
for `wendt` (73 hits), then narrowed to files co-occurring with the distinctive figures
this section cites (`17-second`, `11,752`, `tri-channel`, `600k/month`,
`vulnerability-profit`). Opened `claude-export/normalized/conversations/838c2c5d-...md`
at the "17-second" hit directly: the text reads —

> "I've identified **12 breakthrough expansion opportunities** from this $13M
> methodology: 1. **Hidden Virtuoso Pattern**: The '17-Second Strategic Pause' used in
> sales but perfect for negotiation mastery..."

This is a prior Claude session's own "MES 3.0 / Transcendence Opportunities" output —
patterns the AI proposed as *inferred* from the raw transcript, not a quote of Maria
Wendt saying "17-second pause." The "$600K/month" framing in the same corpus
(`5fb4d480-...md`) is likewise Claude's own extraction-summary language ("$500-600K/month
proven revenue" — an AI-written content assessment, not a Wendt quote). None of the
specific figures in Patterns 11-16 (`$11,752`, `1,847 days`, the 25/25/50 tri-channel
split, ROAS≥4 ladder, 7am/1pm cadence, `+47%` / `+23%` lift numbers) were found verbatim
in either verified transcript or in the 11 LIKELY transcripts sampled above.

**Label: UNCONFIRMED.** Directionally plausible — Wendt does discuss channel
sequencing, ad testing discipline, and content batching in verified sources — but the
precise numbers should not be presented to a user as Wendt's stated figures. A
provenance caveat has been added directly above this section in genius.md (additive,
content preserved per repair boundaries) rather than deleting it, since removing content
outright is out of scope for this repair pass and the strategic *direction* has plausible
grounding even where the numbers do not.

## Workflow files (references/prompts, references/prompts-v2, references/_legacy-prompts)
Not separately re-verified this pass — `workflow_contracts` and `anti_patterns_sourced`
checks already PASS per the audit; these files were not touched.
