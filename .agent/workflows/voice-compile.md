---
description: Recompile VOICE-CARD.md from accumulated calibration verdicts and sources, bump version, regenerate the portable export
tier: system
---

# /voice-compile — Recompile the Voice Card

Recompiling is judgment work an LLM does — reading verdicts, deciding what's a genuine pattern vs. a one-off, updating prose. This workflow guides that judgment; `execution/voice_ratchet.py` only tracks state (counts, compile point). Never let the script's `mark-compiled` stand in for actually doing the compile.

## When to Run

- `python3 execution/voice_ratchet.py status` reports RECOMPILE RECOMMENDED (5+ pending entries)
- Quarterly, per VOICE-CARD.md §8 (next date is recorded in the card itself)
- A §3 stylometric claim gets contradicted by 3+ new corpus pieces
- Farrice asks for it directly

## Steps

### 1. Read current state
// turbo
Run `python3 execution/voice_ratchet.py status` to confirm pending count and current version.

Read `_active/farrice-brand/voice/VOICE-CARD.md` in full, and `_active/farrice-brand/voice/calibration-log.md` for every entry since the last compile (the entries at the bottom of the table, past the `entries_at_compile` count reported by `status`).

### 2. Re-read sources
Re-read every path listed in the card's frontmatter `sources:` field. Check for material drift — new corpus pieces, updated feedback files, new banned-move entries in `directives/ai-slop-detector.md`. This step is what distinguishes a real recompile from a mechanical append.

### 3. Fold new verdicts into §6
For each pending calibration-log entry:
- **Genuine new pattern** (not just another instance of an existing PASS/FAIL type) → add to §6 as a new bank entry with its why.
- **Another instance of an already-documented pattern** → skip promoting it individually; it reinforces confidence in the existing entry but doesn't need its own line.
- **Contradicts an existing §6 entry** → flag this explicitly to Farrice before resolving either way; don't silently overwrite a standing judgment.

Dedupe §6 as you go — no two entries making the same point.

### 4. Check stylometric deltas (§3)
If new corpus pieces exist since the last compile, spot-check whether the §3 measurements (sentence-length rhythm, em-dash counts, characteristic openings/closings) still hold. Update only on real drift, not noise from a single new sample.

### 5. Bump version and date
- New §6 entries only → patch bump (e.g., 1.0 → 1.1)
- New §4 channel register or §5 ban → minor bump
- §1/§2 identity or voice-law rewrite → major bump, **requires Farrice sign-off first** — these sections are load-bearing per §8's own rule
- Update `compiled:` in frontmatter to today's date

### 6. Regenerate the portable card
Rewrite `_active/farrice-brand/voice/PORTABLE-VOICE-CARD.md` from the updated VOICE-CARD.md — self-contained, no internal repo paths, so an external AI or tool can use it standalone. Carry forward: Identity Spine, Voice Law, the Dial, Banned Moves, and a condensed Calibration Bank (most load-bearing PASS/FAIL examples, not the full running log).

### 7. Mark compiled
// turbo
Run `python3 execution/voice_ratchet.py mark-compiled` — records the current entry count as the new compile point so future `status` calls report pending correctly.

### 8. Recommend re-export
Tell Farrice the portable card changed and should be re-synced anywhere external AIs or tools consume it (Drive, other agents) — this workflow does not automate that export.

## Chain Compatibility

- **Follows**: `/voice-ratchet` (accumulates the entries this workflow folds in)
- **Leads to**: re-export of `PORTABLE-VOICE-CARD.md`; `/voice-os status` to confirm the new version
- **Pairs with**: `/voice-audit` for a quality check on the recompiled card's accuracy against a fresh sample
