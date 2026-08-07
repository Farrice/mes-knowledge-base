# Source Ledger — daniel-thrasher-affiliate

Claim-by-claim provenance for this repair pass (Wave 3 Lane 4 Batch 4). Written by the
repair worker per envelope instruction; supplements (does not replace) the existing
`references/prompts-v2/offer-selection-scorecard.md` source labeling, which already
passes the `source_ledger` heartbeat check independently.

## Sources checked, with disposition

| Source | Location | Size | Status |
|---|---|---|---|
| Primary transcript — "The Top 7 Affiliate Marketing Skills You'll Need in 2026 (In Order!)," YouTube, Daniel Thrasher / ClickBank, published via Merlin AI transcript tool | `https://www.youtube.com/watch?v=G8eJCr4-14c`; local copy inside `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/95bf31f8-08bc-421c-96f7-44d91a50833a.md` (conversation id `95bf31f8-08bc-421c-96f7-44d91a50833a`, created 2025-11-26) | 71,410 bytes | **VERIFIED** — full ~32-minute transcript with per-line timestamps, read in full this session. All new quotes added to `genius.md` in this repair are copied verbatim from this file. |
| Discarded continuation — "MES continuation meta-wrapper" (per `agents/daniel-thrasher/memory/context.md`), same YouTube video re-referenced, contains fabricated "Crown Jewel" income projections ($50-200 RPV, $15K-30K/mo) with no basis in the transcript | `_archive/claude-export-2026-07-01.tar.gz` → `claude-export/normalized/conversations/edf9bee0-194b-4aa6-8ff6-abd91ed7b968.md` (conversation id `edf9bee0-194b-4aa6-8ff6-abd91ed7b968`) | 14,795 bytes | **UNCONFIRMED / explicitly excluded.** Read in full to confirm the prior discard decision (`agents/daniel-thrasher/memory/context.md`) was correct — it was. No claim in this repair, or in the pre-existing skill files, draws on this file. Flagging again here so no future worker re-introduces the "Crown Jewel" income numbers. |
| `agents/daniel-thrasher/AGENT.md` + `agents/daniel-thrasher/memory/context.md` | repo | 3,850 + 898 bytes | **VERIFIED** — internal system files; cross-checked against the primary transcript and found consistent (identity, role, niche, lane boundary). |
| False-positive hit — `_active/harness/codex-harvest-2026-06-11/extractions/video-context/uf4fR3qcDkU/video-context-ledger.md` (matched a filename-search for "thrasher") | repo | 479,184 bytes | **EXCLUDED — not this expert.** Grepped and read the matching lines (~00:47:13–00:47:27): the hits are a speaker saying "grab those thrasher magazines" (skateboarding culture reference), unrelated to Daniel Thrasher of ClickBank. Recording this per envelope Rule 2 (verify before claiming absence/irrelevance, don't just assert it). |
| `extractions/` directory (root-level, 193 entries) | repo | — | **CONFIRMED ABSENT for this expert.** `ls extractions/ \| grep -i thrasher` returns nothing. `_active/harness/codex-harvest-2026-06-11/extractions/` also has no Thrasher-named folder. The real source material lives in the claude-export archive instead (see row 1), not in `extractions/`. |
| Pre-existing skill content: `SKILL.md`, pre-repair `genius.md`, `workflows/01-select-offer.md` / `02-build-campaign.md` / `03-optimize-and-scale.md`, `references/prompts-v2/*.md` | repo, unchanged by this repair | — | **LIKELY** — internally consistent with the primary transcript on every spot-check performed (three-filter method, seven-skill ladder, sell-the-click framing, five-element bridge page, hoplink parameters, ~20% email open rate, Pinterest addition, Make.com automation). Not independently re-verified line-by-line beyond the entities newly cited in this repair; no contradictions found. |

## New claims added in this repair (genius.md)

All six quotes newly inserted into `genius.md` (Anti-Patterns section + the 6
named-entity-floor fixes) are **VERIFIED** verbatim against the primary transcript —
exact timestamps and surrounding context are recorded in `PROVENANCE.md`.

One quote ("your traffic source, your traffic type, your campaign, your creative, your
ad, and your XTC LI," 20:24–20:30) has an auto-caption artifact on its final field name
— almost certainly ClickBank's actual "TID" (tracking ID) parameter, mis-transcribed by
the Merlin AI captioning tool. The quote used in `genius.md` is truncated before that
garbled word and flagged inline as "verbatim preserved, not corrected" — no claim is
made about what the real field name is.
