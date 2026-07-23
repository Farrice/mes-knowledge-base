---
description: On-demand charisma-texture overlay (Rock humble-confidence + Reynolds wit) over any working content — a separate take, never destructive, Farrice decides per piece
---

# /texture-over — The Charisma Texture Pass (Farrice 2026-07-22)

Play Farrice's named charisma textures OVER any working draft, on demand, as a side-by-side take. Born from the role-models disclosure (memory: `user_role-models-voice-north-stars`): **The Rock** (humble-confidence — wins carried low, certainty without chest-thumping) and **Ryan Reynolds** (wit, boyish charm, self-aware asides). Placement is deliberately NOT permanent: Farrice judges piece by piece until enough verdicts pick its home.

## Usage
- `/texture-over <file-or-pasted-draft>` — default light dose
- `/texture-over <file> --dose light|medium` — light = 2-4 touches; medium = every third beat may carry one

## Steps
1. Load `_active/farrice-brand/voice/VOICE-CARD.md` (the hard floor travels: no exclamation marks, no performance, wince test final) + memory `user_role-models-voice-north-stars` (the texture definitions).
2. Read the source fully. Identify 2-4 spots where a texture touch is EARNED: a win being stated (→ Rock: carry it low, fact-plain, "say it without flinching" register), a self-indicting beat (→ Reynolds: one sly aside or parenthetical, max one parenthetical per piece), a close that can hold quiet certainty (→ Rock: settled, short).
3. Apply as a sibling take (`<name>.textured.md` or a labeled TAKE section) — never modify the original. Every touch gets listed in a short **texture ledger** at the bottom so the dose is visible and judgeable.
4. Gates: `python3 execution/prose_classifier.py check <file>`; wit never breaks the banned-moves floor (no cheap question closes, no mic-drop-deflation, em-dash rules hold).
5. Bank Farrice's felt verdict on the pair to `.agent/jam/taste-ledger.jsonl` (dial: charisma-texture). Standing rule: after ~5 verdicts, /weekly-closeout decides the texture's permanent home (voice-over default vs on-demand only).

**Restraint law (Farnsworth's, borrowed)**: if the reader notices the texture, it failed. The Rock beat reads as a man stating a fact; the Reynolds beat reads as a friend who couldn't resist. Neither reads as a persona.

PoC: `_active/farrice-brand/content/bayer-voice-test/2026-07-22-calling-rent-test.md` Take B (4 touches, ledger included).
