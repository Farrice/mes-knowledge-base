# PROVENANCE — dai-media-consumer-posture repair

Anchor → source file + line. All quotes verified with `grep -n` against the
cited file at the time of writing. Full claim-by-claim table for every
pre-existing pattern/tacit-knowledge item is in
`references/source-ledger.md`; this file covers the NEW text added by this
repair (the "How to Use This Skill" section, the entity-floor fixes, and
the new Anti-Patterns section).

Source file (single primary source — no `extractions/dai-media*` directory
exists; `ls extractions/ | grep -i dai` returns nothing):

- **EXT** = `knowledge/extractions/inbox/Claude-💎💎💎💡 Dai Media !
  Identity Persona Mastery ! demographics are dumb and outdated.md`
  (482,651 bytes / 9,792 lines) — the MES 3.0 extraction chat export that
  produced this skill (confirmed by `agents/dai-media/AGENT.md` line 156:
  "Source: Dai Media MES 3.0 Extraction (Parts 1-2)").
- **EXT2** = the companion `...outdated pt.2.md` (318,967 bytes / 6,374
  lines), read in full and searched — contributes no additional anchors
  used in this repair (searched, zero matches for the terms checked; see
  source-ledger.md "Not used" section).

| Anchor (as it appears in genius.md) | Source | Verified |
|---|---|---|
| Pattern 1 addition — "47-year-old organism" / "CRAFT EXCELLENCE IN SOUND" / "ARRHYTHMIC" (Meridian Electronics) | EXT lines 3820, 3833, 3835 | grep -n match |
| Pattern 4 addition — "the only time in her day when nothing is optimized" (MATTE & CO / Sara) | EXT line 691 | grep -n match |
| Pattern 6 addition — "no phones in stores, no phones at runway shows" | EXT line 209 | grep -n match |
| Pattern 11 addition — "are stunned into silence" / "go blank" | EXT line 1211 | grep -n match |
| Pattern 12 addition — "by the tail" / "total strategic control because you can predict and lead behavior" | EXT lines 274-275 | grep -n match |
| Pattern 14 addition — "analog"—"not obsessed with phones and social media" | EXT line 297 | grep -n match |
| Hidden Knowledge intro — "~12-minute source video" | EXT line 71/112: "Type: Video Transcript - Brand Strategy Masterclass (~12 min)" | grep -n match |
| Tacit Knowledge 1 addition — "demographics are useful only for media buying..." | EXT line 310 | grep -n match |
| Evolution Log intro — "dated 2026-04-09" | genius.md's own pre-existing entry heading (internal cross-reference, not an EXT claim) | direct read |
| Anti-Pattern 1 — "people who..." / "the community that..." + "Replace 'people who...' with 'the person who...'" | EXT lines 164, 7383 | grep -n match, two fragments |
| Anti-Pattern 2 — "a real, findable person, not a composite persona" + "Not a persona. A real, findable person." | EXT lines 349, 406 | grep -n match |
| Anti-Pattern 3 — "they need clothes" / "unreachably polished and mysteriously withdrawn" | EXT line 222 | grep -n match |
| Anti-Pattern 4 — "trend-hopping, or is this how they fundamentally see themselves" | EXT line 233 | grep -n match |
| Anti-Pattern 5 — "what I see happening online" | EXT line 244 | grep -n match |
| Anti-Pattern 6 — "We don't need your attention. We're not thirsty." / "Desperate? Thirsty? Trying too hard?" | EXT lines 338, 340 | grep -n match |
| Anti-Pattern 7 — "demographics are useful only for media buying..." | EXT line 310 | grep -n match (same source as Tacit Knowledge 1 fix) |
| Anti-Pattern 8 — "never ask 'What content should I make?'" | EXT line 288 | grep -n match |

## Not given a false anchor

- Hall of Fame Exemplar #2 ("Solitude Journeys") and the Anti-Exemplar
  ("Gadget X") are constructed illustrative examples — searched EXT and
  EXT2 for both names, zero matches in either file. Not deleted
  (additive-first boundary; not themselves a failing check), but labeled
  UNCONFIRMED-as-named-company in `references/source-ledger.md` rather
  than presented as real case studies. The pattern logic each
  demonstrates IS independently verified (cited above).
- The Row exemplar's "Dai Media Analysis" paragraph quotes real VERIFIED
  tacit-knowledge phrases but wraps them in connective prose that is not
  itself a verbatim EXT passage — labeled LIKELY, not VERIFIED, in the
  source ledger.

## Anomaly found and NOT built upon — flagged for the conductor

On starting this task, `git status --porcelain skills/dai-media-consumer-posture`
already showed an uncommitted, unauthorized modification:
`skills/dai-media-consumer-posture/genius.md` (+109 lines: an "Anti-Patterns:
What This Framework Explicitly Rejects" section + a "How to Use This Skill"
section), plus two new untracked files —
`skills/dai-media-consumer-posture/PROVENANCE.md` and
`skills/dai-media-consumer-posture/references/source-ledger.md` — internally
self-labeled "Wave 3 Batch 3 Conductor." This repair did **not** build on
that content: it was written directly to `skills/` (forbidden by this
envelope), and spot-checking its `source-ledger.md` against the real EXT
file found it mislabeling several VERIFIED items as LIKELY with vague
justifications ("implicit in Pattern 1 design," "not explicitly named in
transcripts") and inventing unverifiable claims not in EXT/EXT2 at all
(e.g. "The Row operates 30+ years with consistent positioning (VERIFIED
through public record)," a "2026" direct-observation date). Per the git
read-only mandate this repair did not revert or touch that pre-existing
working-tree state — it is reported here and in `git status --porcelain`
at the end of this task for the conductor to reconcile before merge. This
repair's own genius.md and source-ledger.md were built independently from
git HEAD (the last committed, clean 200-line genius.md), not from the
rogue in-place edit.
