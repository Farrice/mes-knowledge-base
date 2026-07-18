---
name: "Voice OS — Post-Draft Verification Pass"
skill: voice-os
maps_to_front_door: "/voice-os apply <file>"
full_protocol: skills/voice-os/references/prompts-v2/post-draft-voice-verification-pass.md
---

# Post-Draft Verification Pass

## When to Use

After a craft expert finishes a MIRROR- or BLEND-mode draft, before it ships under Farrice's
name. Not specified for STRETCH or OFF drafts. This is the last gate — a piece can pass every
craft check (structure sound, hook sharp, no slop) and still not sound like Farrice; this
workflow is what catches that specific failure.

## Input Required

- Draft file path
- Mode (MIRROR or BLEND — confirm before running; stop if the draft is STRETCH or OFF)

## Steps

1. Run `python3 execution/prose_classifier.py check <file>`. 5+ signals flags the draft and caps
   Expert Standard at 6 under the root Quality Gate.
2. Read the draft's strongest lines against VOICE-CARD.md §6 Calibration Bank — both PASS and
   FAIL columns. A FAIL-bank match (forced jargon, tells-instead-of-shows, generic question
   close) gets rewritten even if `prose_classifier.py` passed it clean.
3. Rewrite any flagged line, re-run both checks, repeat until both pass. "Not ready" means
   rewrite, never disclose-and-ship.
4. If a felt reaction (praise or wince) surfaces on any specific line during this review, capture
   it immediately per the Felt Verdict Capture workflow — do not defer it to later in the
   session.

Full protocol: `skills/voice-os/references/prompts-v2/post-draft-voice-verification-pass.md`.

## Output Requirements

- `prose_classifier.py` result: pass/fail, signal count.
- §6 pattern-match findings: any FAIL-bank matches, named, quoted, and the rewrite applied.
- Final verdict: READY or NOT READY — binary, no hedged middle state.
- If NOT READY on the first pass: the corrected draft, then re-verified before delivery.

## Quality Gate

- Draft confirmed MIRROR or BLEND before this workflow ran at all.
- `prose_classifier.py` ran before any verdict was rendered.
- Draft's strongest lines checked against BOTH the PASS and FAIL columns, not the automated tool
  alone.
- Any FAIL-bank match was rewritten, not merely flagged.
- Delivered draft is free of "per my voice guidelines" or any card-quoting narration.
- Verdict is binary; no draft shipped with a noted-but-unaddressed failure.
