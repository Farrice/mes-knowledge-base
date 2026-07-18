---
name: "Voice OS — Voice Card Recompile"
skill: voice-os
maps_to_front_door: "/voice-compile"
full_protocol: skills/voice-os/references/prompts-v2/voice-card-recompile.md
---

# Voice Card Recompile

## When to Use

When `python3 execution/voice_ratchet.py status` reports 5+ pending entries since the last
compile, on the quarterly schedule (next: 2026-10-07 per VOICE-CARD.md §8), or when a §3
stylometric claim is contradicted by 3+ new corpus pieces. Not speculative — one of these three
conditions must actually have fired.

## Input Required

- Pending entry count (from `voice_ratchet.py status`)
- Trigger reason (5+ pending | quarterly | stylometric contradiction, with the contradicting
  pieces named)

## Steps

1. Confirm the trigger actually fired before recompiling.
2. Fold new `calibration-log.md` verdicts into VOICE-CARD.md §6 — a deduplicating merge into the
   curated bank, not a raw append of log lines.
3. If a §3 stylometric claim was contradicted by 3+ new pieces, update §3; otherwise state "§3
   unchanged" explicitly.
4. Bump the card version (patch for §6 additions, minor for a new §4 register or §5 ban, major
   for a §1-§2 identity/law rewrite — major bumps require Farrice sign-off).
5. Regenerate `PORTABLE-VOICE-CARD.md`.
6. Flag re-export to Drive/other consuming agents as a recommendation — this workflow does not
   automate the export.

Full protocol: `skills/voice-os/references/prompts-v2/voice-card-recompile.md`.

## Output Contract

```
Trigger: [5+ pending | quarterly | stylometric contradiction: N pieces]
Pending entries folded: [N]
§6 changes: [new entry → deduped against existing entry, or "no duplicate found"] (repeat)
§3 stylometrics: [unchanged | updated — old claim → new claim, pieces cited]
Version: [old] → [new]
PORTABLE-VOICE-CARD.md: regenerated
Re-export recommendation: [target] — action required, not automated
```

## Quality Gate

- One of the three named trigger conditions genuinely fired before this ran.
- §6 entries were deduplicated against existing content, not simply appended.
- §3 left unchanged unless a genuine 3+-piece contradiction was cited.
- Version bumped and stated explicitly, old → new.
- Re-export flagged as a recommendation, never silently completed or silently skipped.
