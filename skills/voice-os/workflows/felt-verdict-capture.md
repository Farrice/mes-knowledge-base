---
name: "Voice OS — Felt Verdict Capture"
skill: voice-os
maps_to_front_door: "/voice-ratchet"
full_protocol: skills/voice-os/references/prompts-v2/felt-verdict-capture.md
---

# Felt Verdict Capture

## When to Use

The instant Farrice reacts to a specific line — praise or wince — in any session where his own
voice is under discussion. Never batched, never deferred to end-of-session. This is the raw
material the calibration bank (VOICE-CARD.md §6) cannot get any other way.

## Input Required

- The verbatim line reacted to (unparaphrased)
- Verdict: praise or wince (binary)
- Why: the actual specific reason it landed or failed, in Farrice's own words where possible
- Source: the draft, session, or context it came from

## Steps

1. Capture the reaction the moment it happens, silently, in-session — the same standing rule as
   thought-bank capture. Deferred capture is a named anti-pattern: a felt verdict not logged
   in-session is one the loop never learns from.
2. Run `python3 execution/voice_ratchet.py add --verdict <pass|fail> --line "<verbatim>" --why
   "<why>" --source "<source>"` (or `/voice-ratchet`). The script dedupes on exact line text.
3. This entry lands in `calibration-log.md`, the raw append log — distinct from VOICE-CARD.md §6,
   the curated distillation. Folding into §6 happens later, at Recompile, not here.
4. Optionally check `python3 execution/voice_ratchet.py status` for the pending-since-last-
   compile count. Informational only — do not trigger a recompile from within this capture.

Full protocol: `skills/voice-os/references/prompts-v2/felt-verdict-capture.md`.

## Output Format

```
Line: "[verbatim text]"
Verdict: [PRAISE | WINCE]
Why: [specific, not a generic craft label]
Source: [draft / session / context]
Pending since last compile: [N] — [RECOMPILE RECOMMENDED at 5+ | below threshold]
```

## Quality Gate

- Captured in the same turn/session as the reaction — no deferral.
- Line is verbatim, not paraphrased or summarized.
- Verdict is binary (praise/wince), no hedged middle state.
- "Why" names the specific reason this line landed or failed, not a generic voice-rule
  restatement.
- Source is traceable to the actual draft or session.
