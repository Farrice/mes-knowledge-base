---
name: "Voice OS — Pre-Draft Grounding Brief"
skill: voice-os
maps_to_front_door: "/voice-os mode <name>"
full_protocol: skills/voice-os/references/prompts-v2/pre-draft-voice-grounding-brief.md
---

# Pre-Draft Grounding Brief

## When to Use

Before any writing task that carries Farrice's own name — LinkedIn, Substack/Parallax, Notes/
Threads, email/DM, brand copy — and before handing the task to the craft expert that will
actually write it (writers-room, `/parallax`, `/ghostwrite`, How-I-Write OS). This workflow
produces the brief; it does not draft the piece.

## Input Required

- Artifact type (LinkedIn post, Substack edition, Note, DM, brand copy, divergent exploration,
  client deliverable, internal memo)
- Any explicit mode Farrice named ("sound like me," "surprise me," "through [X]'s lens")
- Which craft expert receives the brief

## Steps

1. Confirm `_active/farrice-brand/voice/VOICE-CARD.md` exists. If it doesn't, stop and say so —
   never improvise a voice from memory.
2. Determine the dial mode: explicit naming wins outright; otherwise match the cue table (§ Dial,
   VOICE-CARD.md §7) or fall back to the artifact-type default (SKILL.md decision table).
3. Load only the one §4 channel register that matches the artifact — not all five.
4. State what's fixed (identity anchors + voice law + banned moves in BLEND; everything in
   MIRROR; only the hard floor in STRETCH) and what's free for that mode.
5. State the hard floor unabridged, regardless of mode: privacy law, no fabrication about a real
   person, the AI-slop ban bank, the wince test, no cheap question closes.
6. Hand off to the named craft expert. This workflow never drafts the piece itself.

Full field-by-field protocol: `skills/voice-os/references/prompts-v2/pre-draft-voice-grounding-
brief.md`.

## Output Schema

```
Artifact: [type]
Mode: [MIRROR | BLEND | STRETCH | OFF] — determined by: [explicit | cue | decision-table row]
Channel register loaded: [name]
FIXED: [constraints for this mode]
FREE: [latitude for this mode]
HARD FLOOR: [all five items, unabridged]
Handoff: [craft expert] has full craft authority within the above.
```

## Quality Gate

- VOICE-CARD.md existence confirmed before proceeding — no improvised voice.
- Explicit mode naming (if present) overrode the decision table with no exceptions.
- Only the relevant §4 register loaded, not all five.
- All five hard-floor items stated unabridged, regardless of determined mode.
- Brief widens the craft expert's lane rather than dictating structure or rhetoric.
