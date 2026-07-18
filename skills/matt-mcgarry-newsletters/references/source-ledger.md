# Source Ledger — matt-mcgarry-newsletters

Ground truth for this skill is claude.ai conversation exports containing YouTube/podcast
transcripts of Matt McGarry, archived in `_archive/claude-export-2026-07-01.tar.gz`
(`claude-export/normalized/conversations/*.md`, 332,779,255 bytes compressed / 1,149,022,993
bytes uncompressed across 7,728 members). SKILL.md's `source:` frontmatter line
("claude.ai export 2026-07-01") pointed at this archive but no `references/` ledger existed
until this repair — the archive was never opened to confirm it, which is itself the gap this
ledger closes.

**Method**: `python3 -m tarfile`-style per-member scan (`tarfile.open(...).getmembers()`,
`extractfile().read()`) over all 7,728 members, matching `mcgarry` (case-insensitive,
punctuation-stripped) in file content, not just filenames — a filename-only pass returns
zero hits because the export names files by conversation UUID. 11 members matched; 2 were
false positives (a rotator-cuff research citation "Mihata, T., Gates, J., McGarry, M. H."
in an unrelated PDF export, and an Instagram creator "Daniel McGarry" in an unrelated
keyframe-animation transcript). The 9 real sources below are Matt McGarry
(Newsletter Operator / GrowLetter) content.

## Sources Consulted

| # | File (in archive) | Title | Created | Size (bytes, `wc -c`) | Status |
|---|---|---|---|---|---|
| 1 | `conversations/fc98a3b6-695e-4f97-b22c-d58382317649.md` | 10-31-25 Matt McGarry: 7 Steps To Launch a Newsletter With 7-Figure Potential | 2025-10-31 | 99,415 | VERIFIED — read in full, primary source for launch/anti-pattern claims |
| 2 | `conversations/c19670f1-6229-4c4a-804c-4ba09aadb4fb.md` | Matt McGarry: How I'm Making 8 Figures Sending Emails | 2025-10-21 | 144,268 | VERIFIED — read in full, primary source for source-quality-audit claims |
| 3 | `conversations/27a02a2f-858b-4615-a278-7034e809ecc4.md` | Deep-extraction task transcript ("10 million subscribers... 100 million in sales" intro) | 2025-10-16 | 36,332 | VERIFIED — read in full, source for the 10M+/$100M+ aggregate claim |
| 4 | `conversations/9a417491-0f37-4064-97eb-e67339857b17.md` | 12-8-25 Matt McGarry: 10 Reasons You Should Start a Newsletter in 2026 (You're NOT Too Late) | 2025-12-08 | 76,074 | VERIFIED — read for cross-checks, not separately quoted in genius.md |
| 5 | `conversations/45cfb311-4274-4c5d-b4eb-157c8fffe5b3.md` | Matt McGarry: How To Sell Digital Products (Full Course), pt.1 | 2025-10-04 | 101,189 | VERIFIED — read for monetization/One Belief cross-checks |
| 6 | `conversations/4900f669-61bf-4d12-9953-1dfc0de9276e.md` | Matt McGarry: How To Sell Digital Products (Full Course), pt.2 | 2025-10-07 | 13,303 | LIKELY — scanned, no distinct claims pulled beyond pt.1 |
| 7 | `conversations/56f2816a-fa58-48ab-98e8-9570e178960f.md` | Matt McGarry \| 15 Steps to Sell Your First Digital Product | 2025-12-14 | 61,078 | VERIFIED — source for "$100M+ in sales" phrasing cross-check |
| 8 | `conversations/6b64bb27-f84f-4441-a88e-439a73b81bc3.md` | Matt McGarry: How To Get Email Subscribers From Social Media (podcast w/ Ryan Carr, Tailwind Agency) | 2025-06-22 | 83,431 | LIKELY — scanned for two-channel/discovery claims, not separately quoted |
| 9 | `conversations/0ba6d86b-1f45-4c64-b1f8-3616f4dc3c06.md` | Matt McGarry: Newsletters are DEAD | 2025-06-19 | 35,568 | VERIFIED — source for Newsletters 3.0 / ads-only-is-dead pattern |

Two additional matches on the raw `mcgarry` grep were confirmed NOT sources and excluded:
`conversations/f12761ef-f991-4feb-9fb1-550a972b87e4.md` (746,392 bytes — unrelated academic
PDF citing researcher "McGarry, M. H.") and `conversations/0832a48f-2005-40c6-a6b5-bc633affc5ff.md`
(104,477 bytes — unrelated animation-keyframe transcript naming Instagram creator
"Daniel McGarry").

## Claim-by-Claim Verification

| Claim (as written in SKILL.md / genius.md) | Label | Basis |
|---|---|---|
| "Grew The Hustle to 2.5M subscribers (acquired $30M+)" | VERIFIED | "2.5M" and "$30M" figures appear across sources #1-#5, #9 in McGarry's own bio recitation |
| "First employee at Milk Road (0 → 250K subs... acquired in 10 months)" | VERIFIED | "Milk Road" + "250,000"/"250K" confirmed in source #1, #9 |
| "Built his own newsletter to $1M ARR with just 8,000 subscribers" | VERIFIED | Verbatim in source #1: "we hit a million dollars in annual recurring revenue when I had just 8,000 newsletter subscribers" |
| "$100K+ from his first product launch to a list under 5,000" | VERIFIED | Verbatim in source #1: "over 100,000 in sales from that first product launch with less than 5,000 subscribers" |
| "Clients... James Clear, Cody Sanchez... add 10M+ subscribers and $100M+ in sales" | VERIFIED | James Clear + Cody Sanchez named directly as landed clients in source #1 ("We've been able to land clients like Cody Sanchez, James Clear, Dan Martell, J Shetty, Steven Bartlett..."); "10 million subscribers and over 100 million in sales" verbatim in source #3 |
| "Clients... 1440 Media" | LIKELY | Source #1 uses 1440 Media as a job-to-be-done example ("1440 Media, they have over 4.4 million subscribers, 25 million in revenue per year") — not explicitly stated as a GrowLetter client in the reviewed transcripts. Consistent with, not confirmed as, a client relationship. |
| "Clients... The Flyover" | LIKELY | Source #1: Guy Short, founder of The Flyover, says "before founding the Flyover, I studied Matt's content and much of our early success can be attributed to what I learned from Matt" — a content-student/success-story relationship, not explicitly named a paid consulting client in the reviewed transcripts. |
| "Alex Lieberman writes every issue for Kip, CMO of HubSpot" | VERIFIED | Verbatim in source #1: "his market of one is a guy named Kip who is the CMO of HubSpot" |
| "Organic sources converted to customers at 6,000%+ the rate of co-reg" | VERIFIED | Verbatim in source #2: "the organic sources converted to customers at over 6,000% higher rate than the co-edge [co-reg] and recommendation sources" |
| "Never seen a newsletter fail because of wrong niche... hundreds fail because they don't solve a problem" | VERIFIED | Verbatim in source #1, quoted directly in the new Anti-Patterns section |
| "Meta... clients spend $500K/month profitably" | LIKELY | "$500,000" figure appears in sources #2 and #5 in paid-spend context; exact $500K/month-profitable framing not independently re-verified line-by-line against genius.md's paraphrase in this repair pass |
| Anti-pattern quotes added in this repair (marketing-email conflation, wait-to-monetize, perfect-logo, autopilot-publishing, legacy-media-as-marketing-email) | VERIFIED | All five are verbatim substrings pulled directly from sources #1 and #2 with timestamp anchors — see `genius.md` → Anti-Patterns (Source-Verified) |
| Workflow files (`workflows/01-03-*.md`) and `references/prompts-v2/*.md` framework mechanics (signup-flow sequencing, paid-gate benchmark chain, product ladder order) | LIKELY | Structurally consistent with all 9 sources; not independently re-verified line-by-line in this repair pass (pre-existing content, unchanged) |

## Gaps Named Honestly

- The claim-by-claim table above covers the highest-stakes numeric/named claims (bio stats,
  client list, the two most-quoted mechanism numbers). It does not re-verify every sentence
  in the three workflow files or three v2 prompt files against source transcripts — those
  files were unchanged by this repair (workflow_contracts already passed) and are labeled
  LIKELY as a block rather than claim-by-claim.
- Two clients named in SKILL.md's bio line (1440 Media, The Flyover) are downgraded from the
  implicit "client" framing to LIKELY because the reviewed transcripts show one as a JTBD
  example and the other as a self-reported content-student success story, not an explicit
  paid-client statement from McGarry. This was not corrected in SKILL.md itself (out of
  scope for the failing checks; flagged here per the "no invented provenance" rule rather
  than silently passed through as VERIFIED).
