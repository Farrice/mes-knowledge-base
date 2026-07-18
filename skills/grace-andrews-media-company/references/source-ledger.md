# Grace Andrews — Source Ledger

> Claim-by-claim provenance for `skills/grace-andrews-media-company/`. Ground truth check
> (2026-07-17): `ls extractions/ | grep -i grace` returns exactly one hit —
> `extractions/grace-andrews/extraction-report.md` (25,439 bytes, confirmed via `ls -la`).
> **No raw transcript exists anywhere in this repo for Grace Andrews.** Every claim below
> traces to that one synthesis file (itself an LLM-authored extraction from a YouTube
> interview — "Marketing GENIUS: If You Want To Grow An Audience In 2026, I'd Do This,"
> *Anatomy of a Dream* podcast w/ Tiffany K. Guillen, per extraction-report.md:6) or to the
> skill's own prior content. No claim in this skill is VERIFIED against a primary
> transcript — the ceiling for any Grace-voice quote is LIKELY.

## Source Inventory

| Source | Type | Status |
|---|---|---|
| `extractions/grace-andrews/extraction-report.md` | Synthesis (25,439 bytes, 227 lines) | Confirmed present — read in full for this repair |
| Raw YouTube transcript / podcast audio | Primary source | **Absent from repo** — not found by `extractions/` search, not found elsewhere in repo. Do not fabricate an "unrecoverable/0-byte" claim beyond this — the correct claim is "never ingested," confirmed by directory listing, not inference |
| `skills/ben-watkins-storytelling/genius.md` (lines 7-16) | Calibration model (structure only, not content) | Read in full — used to shape the "How to Use This Skill" section format, never copied verbatim |

## Claim-by-Claim Labels

| Claim / Pattern | Anchor | Label | Note |
|---|---|---|---|
| "media company that happens to sell a product" (core genius) | extraction-report.md:17 | LIKELY | Synthesis's own phrasing for Grace's core distinction; not a verbatim transcript quote |
| Trust Pathway 5-stage sequence (Attention → Discoverability → Connection → Trust → Conversion) | extraction-report.md:36 | VERIFIED | Verified as accurately reflecting the synthesis document's own stage list — not a claim about the raw interview |
| City Model (Grand Central / Destinations / Lines / Passengers) | extraction-report.md:59-63 | VERIFIED | Verified against synthesis; framework is consistently used across GP-6 and the DOAC exemplar |
| "Who do we know who knows someone who knows them?" | extraction-report.md:66 | LIKELY | Quoted verbatim from the synthesis document; Grace-voice attribution unconfirmed against a primary transcript |
| "the thing that stays with someone after they close the tab" | extraction-report.md:78 | LIKELY | Same basis as above |
| "the come-down creates a false sense of failure" | extraction-report.md:90 | LIKELY | Same basis as above |
| Sales-First Social Feed anti-exemplar | extraction-report.md:143-145 | VERIFIED (pattern) / LIKELY (quoted lines) | The pattern description is verified as present in the synthesis; embedded quoted dialogue ("You're speaking at everyone and reaching no one") is LIKELY Grace-voice |
| 8 Hidden Knowledge entries (HK-1 through HK-9, numbered non-sequentially in source) | extraction-report.md:11, 105-127 | VERIFIED | Count ("8 tacit insights detected") and content both verified against the synthesis header + body |
| Revenue Sequencing Intelligence / HK-9 (readiness signal, premature diversification, cannibalization warning) | genius.md (pre-existing, not in extraction-report.md) | UNCONFIRMED | Not found in extraction-report.md's Genius Patterns or Hidden Knowledge sections during this repair's source check — flagged here rather than silently left unlabeled. Pre-existing skill content, not authored in this repair pass; carried forward under additive-first boundaries |
| DOAC Grand Central declaration — "helping people become the best version of themselves" | extraction-report.md:61, 135 | LIKELY | Quoted in both GP-6 context and the DOAC Transit System exemplar; synthesis-sourced |
| 10M TikTok views → near-zero podcast subs / 500K podcast views → thousands of engaged buyers (80/20 split) | extraction-report.md:139-141 | VERIFIED | Numbers verified as present in the synthesis's own exemplar description — not independently verified against DOAC's actual analytics |

## Gap Named

No source ledger existed prior to this repair. This file is new. The skill's Revenue
Sequencing Intelligence pattern (genius.md, pre-existing) has no traceable anchor in
extraction-report.md — flagged UNCONFIRMED above rather than fabricating a citation or
silently deleting pre-existing content (additive-first boundary, per ENVELOPE.md).
