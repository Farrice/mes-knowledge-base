---
description: Front door for Voice OS — check calibration state, set/explain a fidelity mode, or run a voice pass on an existing draft
tier: system
---

# /voice-os — Voice OS Front Door

The always-on voice alignment spine for anything carrying Farrice's own name. Loads `_active/farrice-brand/voice/VOICE-CARD.md`, applies the Dial (MIRROR/BLEND/STRETCH/OFF), and enforces the identity + banned-moves floor. Full spec: `skills/voice-os/SKILL.md`.

## Usage

```
/voice-os [status|mode <name>|apply <file>]
```

Bare `/voice-os` (no argument) defaults to `status`.

## status

// turbo
Run `python3 execution/voice_ratchet.py status`.

Report to Farrice:
- Card version and compiled date (from the script output)
- Total calibration entries (PASS/FAIL split)
- Pending-since-last-compile count
- RECOMPILE RECOMMENDED flag if present — recommend `/voice-compile`

If the script reports `VOICE-CARD.md: not found`, say so plainly and stop. Do not improvise a voice from memory or training data.

## mode `<name>`

`<name>` is one of `mirror`, `blend`, `stretch`, `off` (case-insensitive).

1. Read `skills/voice-os/SKILL.md` § The Dial for the mode's fidelity level, when it applies, and what's fixed vs. free.
2. State the mode explicitly for the rest of the session: "Voice OS is now in [MODE] — [one-line description of what's locked and what's free]."
3. If the requested mode conflicts with the artifact type (e.g., `mirror` requested for a client deliverable, which is always OFF), flag the conflict and ask which should win — explicit mode naming usually wins, but OFF for client work is close to a hard rule.

No script call needed — mode-setting is a session-state declaration, not a file write.

## apply `<file>`

Run a voice pass on an existing draft.

1. **Load.** Read `_active/farrice-brand/voice/VOICE-CARD.md` in full. Read the relevant §4 channel register for the draft's format (LinkedIn, Substack edition, Notes/Threads, email/DM, client doc).
2. **Determine mode.** Use the artifact-type decision table in `skills/voice-os/SKILL.md` unless Farrice already named a mode this session.
3. **Audit.** Read the draft against:
   - §5 Banned Moves — flag any hit, cite which of the 10 inline entries (or the full 64-entry bank at `directives/ai-slop-detector.md`) it matches.
   - §6 Calibration Bank — pattern-match the draft's strongest/weakest lines against the PASS and FAIL examples.
   - §1 Identity Spine + §2 Voice Law, in MIRROR/BLEND only — check the POV anchors aren't softened and the signature moves aren't absent where the piece calls for them.
4. **Verify.** Run `python3 execution/prose_classifier.py check <file>`.
5. **Rewrite.** Every flagged line gets a specific rewrite, not a general note — show the before/after.
6. **Report.** A short Voice Pass Receipt: mode used, moves flagged, lines rewritten, prose_classifier result, and whether the draft is ready to ship.

## Chain Compatibility

- **Leads to**: `/voice-ratchet` (log any felt verdict Farrice gives during the pass), `/voice-compile` (when status flags RECOMPILE RECOMMENDED)
- **Pairs with**: `/voice-audit` (Sean Mabry — deeper line-by-line QA, point it at VOICE-CARD.md as the reference)
- **Composes with, never replaces**: writers-room, `/parallax`, `/ghostwrite`, How-I-Write OS — those own craft; this owns identity fidelity
