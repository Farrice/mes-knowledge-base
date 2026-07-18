# PROVENANCE — luke-iha-avatar-machine heartbeat repair (2026-07-17)

Every anchor added during this repair pass, mapped to the exact source file + location it was
read from. All sources are inside `extractions/luke-iha-avatar-machine/` (the only ground truth
permitted for this task) unless otherwise noted. No web search, no training-memory fill-in.

## genius.md — "Anti-Patterns (auto-fail)" source anchors

| Anti-pattern bullet | Anchor added | Source file : location |
|---|---|---|
| Single-adjective market descriptions | "Salty Vs. Sweet" contrast | `Copy_of_The_AI_Avatar_Machine.txt` : line 135 |
| Scores with no marketing consequence | "Marketing Consequences:" required per dimension | `Copy_of_The_AI_Avatar_Machine.txt` : lines 285, 315, 339; `AI_Manifold_Brief_(Dirty).txt` : line 154 (table column "Specific Consequence") |
| Hooks that clash with Identity in the lead | "activating an autopilot REJECTION response" | `The_Resonance_Hierarchy.txt` : line 123 |
| Beliefs over BS limit / under Epiphany Threshold | "The 9 is the 'BS limit' – too outlandish" | `BASIC_ET_PROMPT.txt` : line 29 |
| Reframes that argue instead of AWE | "Splitting the Atom" (line 630); "Agree, Wedge, Elaborate" (AWE) framework (line 720) | `Copy_of_The_AI_Avatar_Machine__Day_3.txt` : lines 630, 720 |
| Invented "specific language" | "How to swipe" SOP + sourcing list | `Copy_of_SOP_for_Swiping.txt` : lines 55–175 |
| Loose frameworks instead of assembled Manifold | "combine all of this info into a comprehensive, detailed summary" | `BuildABuyerSnapshot.txt` : line 171 (identical instruction at `Build_A_Better_Buyer-_Updated.txt` : line 116) |
| Generic ICP/demographic-profile floor | raw demographic bullets (Young vs. Old, reading ability, tech familiarity) | `Copy_of_The_AI_Avatar_Machine.txt` : lines 160–175 |

## genius.md — "How to Use This Skill (Model Calibration)" grounding

- The "Beta Males Get Less Women → Beta Males Get More Women → the 3 'beta male' moves" drill example: verbatim from `BASIC_ET_PROMPT.txt` line 42 and `Copy_of_The_AI_Avatar_Machine__Day_2.txt` line 83 (already present in the pre-existing genius.md exemplar section; reused here for the calibration note rather than invented fresh).
- The Manifold-vs-downstream-copy distinction (scaffolding visible internally, invisible in shipped copy) is an editorial synthesis of the skill's own stated purpose (`SKILL.md` line 14: "the single document the rest of your copy system runs on") and the Ejection Trigger concept (`Copy_of_The_AI_Avatar_Machine.txt` line 156; `The_Resonance_Hierarchy.txt` line 125) — labeled here as synthesis, not a direct Iha quote, because no single source line states this framing explicitly.

## references/source-ledger.md

Full claim-by-claim sourcing table is inside the file itself. Two items are explicitly flagged
as gaps rather than invented:
1. Co-instructor's surname "Castelli" — not found in the 3 workshop-day transcripts (only "Mario"
   appears); sourced only from `extractions/luke-iha-avatar-machine/PROVENANCE.md`'s folder-name
   metadata. Labeled UNCONFIRMED.
2. The "5 live-call transcripts" and "2 pitch decks" referenced in
   `extractions/luke-iha-avatar-machine/PROVENANCE.md` are not present among the 14 files actually
   extracted — meaning genius.md's "Hidden Knowledge (from the live calls...)" section header
   cannot be verified as to *which* source produced it. Every individual claim inside that section
   WAS re-verified against the 14 available files (see source-ledger.md Claim Ledger) and is
   VERIFIED on content; only the "live calls" attribution in the header is unconfirmed.

## workflows/avatar-machine-orchestrator.md — Output Requirements / Quality Gate

Not a sourcing task — this file describes the skill's own orchestration mechanics (Phase 0–5,
dependency DAG, Gate A/B/C references) which were already fully specified earlier in the same
file and in `SKILL.md`'s Tier-0 table (line 37–39) and `avatar-manifold.md`'s own Quality Gate
section. The new Output Requirements / Quality Gate sections restate and formalize those existing
mechanics in the house format used by every other workflow file in this skill (see
`workflows/core-wound.md` and `workflows/pain-matrix.md` for the matched style) — no new factual
claims were introduced, so no VERIFIED/LIKELY/UNCONFIRMED label applies to this file.
