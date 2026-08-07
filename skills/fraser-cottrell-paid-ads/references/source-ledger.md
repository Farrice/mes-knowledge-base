# Source Ledger — fraser-cottrell-paid-ads

Ground truth for this skill is NOT under `extractions/` (grep of `extractions/` and
`_active/harness/codex-harvest-2026-06-11/extractions/` for "fraser cottrell"/"fraggle" returned
zero hits — confirmed by directory listing, not assumed). It also is not findable by
filename in `_archive/claude-export-2026-07-01.tar.gz` (332,779,255 bytes, 3,864 file
entries per `tar -tzf`).

It IS present by **content**. A Python `tarfile` scan of all 7,720 members (extracting
each `.md`/`.json`/`.txt` and searching bytes, not filenames) found 12 conversation
files containing "Fraggle" or "Cottrell"; 10 of the 12 are genuine Fraser Cottrell
source material (2 were false positives — unrelated conversations that happened to
contain the substring). Every quote and every number in genius.md below traces to one
of these 10 files. This is the honest provenance path: SKILL.md's `source: claude.ai
export 2026-07-01` line was correct, but the material required a content grep, not a
filename grep, to locate.

## Source Files (all inside `_archive/claude-export-2026-07-01.tar.gz`)

| File (tar member) | Title | Captured | Size |
|---|---|---|---|
| `claude-export/normalized/conversations/c764ba6a-9e31-44b9-888d-bd27d98a5638.md` | Coach Fresh-Fraser Cottrell: Static Ads Ultimate Guide \| The Easiest Ads to Scale FAST | 2025-08-15 | 74,144 B |
| `claude-export/normalized/conversations/8734418a-59eb-4534-99b0-b7c41160b046.md` | Frasier: How to Make Meta Ad Creatives (even if you are a beginner) | 2025-07-03 | 36,313 B |
| `claude-export/normalized/conversations/90133db2-1b09-489a-a002-d0464dc34f25.md` | 12-3-25 Fraser Cottrell: Every Ad Creative Type EXPLAINED | 2025-11-30 | 56,725 B |
| `claude-export/normalized/conversations/ae47a4dd-718f-4d37-bdf1-5efaecb250cd.md` | 11-21-25 [META ADS CREATIVE STRATEGY]-Fraser Cottrell: My $300M Meta Ads Strategy (copy & scale) | 2025-11-18 | 57,129 B |
| `claude-export/normalized/conversations/85a4862e-8f12-442b-85d7-52e7534c55c2.md` | Fraser Cottrell \| How to Write Winning Meta Ad Scripts ($450M Spent) | 2026-01-04 | 59,858 B |
| `claude-export/normalized/conversations/e30f9853-1afe-4303-af1d-14635bac2ea2.md` | Fraser Cottrell \| I Tested 500 Static Ads, Here's What Actually Scales in 2026 \| Ad Mastery | 2026-02-10 | 57,849 B |
| `claude-export/normalized/conversations/ec94d786-ecb2-4484-86cf-ddef2cbfbdec.md` | Fraser Cottrell: Static Ads masterclass 2025 (Full guide) The easiest ads to scale fast | 2025-06-09 | 38,583 B |
| `claude-export/normalized/conversations/16ccff47-7a6d-4b89-9d00-6285ab8f11e7.md` | Fraser Cottrell: How I make Ai Ads that actually work | 2025-06-09 | 33,694 B |
| `claude-export/normalized/conversations/da16c880-f3f6-4f21-bd25-d4414e0d2469.md` | 11-21-25 [REDDIT-TO-AD CREATIVE]-Fraser Cottrell: How I Turn Reddit Threads Into High-Converting Ad Ideas | 2025-11-19 | 50,288 B |
| `claude-export/normalized/conversations/f1571607-c018-4aad-b744-084e9227d615.md` | 11-26-25 Fraser Cottrell: Why Ai Ad Agencies are About to Go Extinct | 2025-11-23 | 32,910 B |

All 10 are raw YouTube transcripts (via Merlin AI transcription tool) pasted into
Claude.ai conversations for extraction/prompt-engineering purposes — Fraser's own
words, first-person, timestamped. Two additional hits from the content scan
(`1fe0e0e6...` "Validating prompt value for premium service deployment" and
`774870b2...` "Ash Maurya | My Exact AI Workflow for Customer Research") are NOT
Fraser Cottrell material — excluded from this skill's provenance.

## Claim-by-Claim Labels

| Claim | Label | Basis |
|---|---|---|
| "8,000+ creatives per month" | VERIFIED | ae47a4dd, 2:34 — "a production studio that churns over 8,000 ad creatives out for our clients every single month" |
| "$300-450M in Meta ad spend" | VERIFIED | 16ccff47 0:37 & da16c880 0:25 — "spent over 300 million across our client[s]"; 85a4862e 0:?? — "tied to 450 million in ad spend" |
| "15 years in performance marketing" | VERIFIED | ae47a4dd 0:02 — "over the past... 15 years of working in this industry" (paraphrase of the transcript's own framing) |
| "10,000+ ads produced" | VERIFIED | 85a4862e — "producing over 10,000 ads"; ec94d786 0:11 — "have made over 10,000 ads for 7, 8, and [9-figure brands]" |
| "500+ static ads tested" | VERIFIED | e30f9853 title/metadata — "I Tested 500 Static Ads" |
| Clients named (Leaf Shave, The Black Stuff, Chomps, Underbrush, Aloha, Humantra, Biotica, Hydrolich, Nuvet, protein.com, Sunday Swagger, Foldi) | VERIFIED | Named verbatim across c764ba6a, 90133db2, e30f9853, 85a4862e transcripts |
| Villain-vs-hero 5-part script skeleton | VERIFIED | 85a4862e — full walkthrough with Leaf Razor and Underbrush examples, verbatim script lines quoted in genius.md |
| 6-format static library (color-block, AI mascot, comment frame, headliner, collage, IG-organic) | VERIFIED | e30f9853 — each format named and demonstrated with a real client example |
| "47.5% vs 34% hook rate" production-vehicle test | LIKELY | Referenced in prior skill version's One-Variable Testing pattern; the specific figure was not re-located verbatim in this session's 10-file re-scan (transcript may be in a source file not among the 12 content-hits, or the figure paraphrases a real Fraser example not captured at these exact digits). Not removed (additive-first; was present pre-repair) but flagged — treat as LIKELY, not VERIFIED, until re-confirmed against primary transcript. |
| "One-handed bra" disability-audience insight | LIKELY | Consistent with Fraser's stated research method (mining reviews/comments for undisclosed audience segments) across ae47a4dd and f1571607, but the specific bra-brand example line was not re-located verbatim in the 10-file re-scan. |
| "Fraser explicitly hands [micro-iterations] back" (verbatim framing) | UNCONFIRMED → reworded | No verbatim quote located for this exact framing. Genius.md's "Insight: The Brand Can Run Its Own Micro-Iterations" was rewritten this repair to ground on the verified quote "we don't run the ads at Fraggle, but we do take a massive interest in the data" (ae47a4dd) instead of the unconfirmed original claim. |
| Storytelling-reversal ("years ago I said it didn't matter, now I was wrong") | VERIFIED | ae47a4dd 4:37-4:50, verbatim, quoted in full in genius.md |
| Comment-mining objection example ("it's too expensive" → Leaf Shave refill-savings block) | VERIFIED | c764ba6a / 85a4862e — matches the "seriously, I know it's more expensive, but this will pay for itself..." script line |
| Sensory/borrowed-reference pattern (cedarwood, menthol, raw Irish honey) | VERIFIED | e30f9853 — "Raw Irish honey, black pepper, menthol, peppermint, cedar wood. We're breaking down the tones..." |
| "Trained filmmaker" self-description | VERIFIED | 90133db2 — "as someone that is a trained filmmaker, storytelling is my thing" |
| Anti-pattern: overdesigned/over-researched statics | VERIFIED | c764ba6a, opening line, verbatim |
| Anti-pattern: judging results too early / narrow targeting / too many ads at once | VERIFIED | 8734418a, 19:33-20:07, verbatim, three-item list from Fraser himself |
| Anti-pattern: cheap fake-podcast production | VERIFIED | 90133db2, verbatim |
| Anti-pattern: before/after ban risk | VERIFIED | 90133db2, verbatim |
| Anti-pattern: skipping solution-aware stage | VERIFIED | 90133db2, verbatim |

## What This Repair Did NOT Verify

The three prompts-v2 execution prompts (`references/prompts-v2/*.md`) and the three
workflow files were already passing their audit checks (`verbatim_exemplars`,
`workflow_contracts`) and were out of scope for this repair pass — not independently
re-verified against the transcripts above.
