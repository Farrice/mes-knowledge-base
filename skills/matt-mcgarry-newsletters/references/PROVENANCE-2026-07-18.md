# Provenance — matt-mcgarry-newsletters repair

Anchor → source file + location. Archive: `_archive/claude-export-2026-07-01.tar.gz`
(332,779,255 bytes on disk; 1,149,022,993 bytes uncompressed; 7,728 members). Located via
Python `tarfile` per-member content scan for the substring `mcgarry` (case-insensitive,
name-fragment match, no punctuation assumptions) — filename-only search returns zero hits
since the export names files by conversation UUID.

| Anchor (in genius.md) | Source file (in archive) | Location | Size (`wc -c`) |
|---|---|---|---|
| "Another common mistake... newsletters and email marketing are the same thing" | `conversations/fc98a3b6-695e-4f97-b22c-d58382317649.md` | transcript ~13:21-13:38 | 99,415 |
| "I have never seen a newsletter fail because they picked the wrong niche..." | `conversations/fc98a3b6-695e-4f97-b22c-d58382317649.md` | transcript ~16:26-16:39 | 99,415 |
| "So I see that as a really big mistake... wait till they've built an audience to make money" | `conversations/fc98a3b6-695e-4f97-b22c-d58382317649.md` | transcript ~33:33-33:46 | 99,415 |
| "People play business and waste time on things like the perfect logo..." | `conversations/fc98a3b6-695e-4f97-b22c-d58382317649.md` | transcript ~25:47-26:04 | 99,415 |
| "If you just start your newsletter and you publish... once a week... never do anything else..." | `conversations/fc98a3b6-695e-4f97-b22c-d58382317649.md` | transcript ~11:36-11:48 | 99,415 |
| "One thing that the legacy media companies do wrong is they use the newsletter as like a marketing email..." | `conversations/c19670f1-6229-4c4a-804c-4ba09aadb4fb.md` | transcript ~25:48-26:02 | 144,268 |
| "$1M ARR with just 8,000 subscribers" (bio line, pre-existing) | `conversations/fc98a3b6-695e-4f97-b22c-d58382317649.md` | "we hit a million dollars in annual recurring revenue when I had just 8,000 newsletter subscribers" ~1:00-1:06 | 99,415 |
| "$100K+ from his first product launch to a list under 5,000" (bio line, pre-existing) | `conversations/fc98a3b6-695e-4f97-b22c-d58382317649.md` | "over 100,000 in sales from that first product launch with less than 5,000 subscribers" ~1:09-1:19 | 99,415 |
| "10M+ subscribers and $100M+ in sales" (bio line, pre-existing) | `conversations/27a02a2f-858b-4615-a278-7034e809ecc4.md` | "I've helped clients add over 10 million subscribers and over 100 million in sales" ~0:23-0:32 | 36,332 |
| "Organic sources converted... at 6,000%+ the rate" (Pattern: Source-Quality Audit, pre-existing) | `conversations/c19670f1-6229-4c4a-804c-4ba09aadb4fb.md` | "converted to customers at over 6,000% higher rate than the co-edge and recommendation sources" ~38:55-39:00 | 144,268 |
| "Alex Lieberman writes every issue for Kip, CMO of HubSpot" (Pattern: Pick a Problem, pre-existing) | `conversations/fc98a3b6-695e-4f97-b22c-d58382317649.md` | "his market of one is a guy named Kip who is the CMO of HubSpot" ~19:07-19:11 | 99,415 |
| James Clear + Cody Sanchez as landed clients (bio line, pre-existing) | `conversations/fc98a3b6-695e-4f97-b22c-d58382317649.md` | "We've been able to land clients like Cody Sanchez, James Clear, Dan Martell..." ~1:32-1:36 | 99,415 |

Full claim-by-claim table (including LIKELY/UNCONFIRMED downgrades for 1440 Media and The
Flyover client status) is in `references/source-ledger.md`.
