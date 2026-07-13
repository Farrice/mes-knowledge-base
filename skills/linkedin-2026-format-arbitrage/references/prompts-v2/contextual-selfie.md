---
name: "The Contextual Selfie (Costly Signal)"
source_prompt: "skills/linkedin-2026-format-arbitrage/references/prompts/contextual-selfie.md"
skill: linkedin-2026-format-arbitrage
standard: structure-pure-v2
refactored: 2026-07-11
---

# The Contextual Selfie (Costly Signal)

**Context:** The Contextual Selfie counteracts AI fatigue. It relies on "Costly Signaling Theory"—a real, unpolished photo of a creator working in their actual environment carries more algorithmic and human trust than a generated graphic.

## Your Objective
Design a LinkedIn post built around a specific physical image of the creator, using the text to challenge a dominant narrative (The Anti-Guru approach).

## Input Parameters
* **The "Guru" Trope to Attack:** [e.g., "Prompt packs," "Hustle culture," "Waking up at 4 AM"]
* **The Sovereign Reality (The Truth):** [The leveraged, anti-hustle reality the user actually lives]
* **Current Physical Context:** [What the user is literally doing right now, e.g., "Working at home desk with toddler's drawing visible"]

## The Costly Signal Architecture

### 1. The Visual Directive
Describe exactly what the photograph should look like.
* **Rule:** It must NOT look like a stock photo. It should show the "messy middle" of real work.
* **Elements:** What is on the desk? What is the posture? What is on the screen in the background?

### 2. The Text (The Anti-Guru Manifesto)
* **The Tone:** Direct, slightly contrarian, grounded in reality.
* **The Structure:**
    * **Hook:** Directly attack the trope. (e.g., "Stop buying ChatGPT prompt packs. I'm serious.")
    * **The Evidence:** State what you *actually* see happening in the market (the failure of the trope).
    * **The Pivot (The Selfie Tie-In):** Explicitly connect the text to the reality of the photo. (e.g., "I'm a stay-at-home dad who builds AI Brains. No hustle. Just leverage.")
    * **The Re-Frame:** Give them a new way to look at the problem.

### 3. The Pinned Comment
Provide the strategic first comment to drive Early Velocity.
* **Content:** A behind-the-scenes detail about the photo itself, or a soft CTA for a lead magnet.

## Output Contract

**Voice layer (binding — Farrice 2026-07-13):** if this deliverable ships under Farrice's own name, load `_active/farrice-brand/voice/VOICE-CARD.md` + dial mode (default BLEND, per `skills/voice-os/SKILL.md`) as a layer BEFORE drafting — binding `farrice_voice_alignment`.

Deliver exactly three components:
1. **Photo Instructions** — a directive block describing the required image (setting, objects visible, posture, what's on the screen). Must specify anti-stock-photo cues, not stage direction for a polished shot.
2. **Post Text** — hook / evidence / selfie-pivot / re-frame structure, formatted with single-sentence paragraphs.
3. **Pinned Comment Text** — one behind-the-scenes detail or soft CTA, ready to post immediately after publishing.

## Output Skeleton
```
PHOTO INSTRUCTIONS
------------------
Setting: [where, real not staged]
Visible objects: [2-4 specific unglamorous items — the "messy middle" cues]
Posture/framing: [candid, mid-task, not posed-for-camera]
Screen/background detail: [what's actually on screen, if visible]

POST TEXT
---------
[HOOK — direct attack on the named guru trope, one sentence]

[EVIDENCE — what's actually failing in the market because of this trope]

[PIVOT — explicit tie from text to the photo's reality, names the sovereign truth]

[RE-FRAME — the new way to see the problem, one closing line]

PINNED COMMENT
--------------
[Behind-the-scenes detail about the photo OR a soft CTA — one comment, not both]
```

## Quality Gate
- [ ] Photo instructions explicitly reject polish (no "professional," "clean," or stock-photo language)
- [ ] Hook names the guru trope directly, not vaguely
- [ ] Text-to-photo pivot is explicit — a reader could not miss the connection between what's said and what's shown
- [ ] Every paragraph in the post is one sentence (no dense blocks)
- [ ] Pinned comment adds something the post didn't already say, not a restatement
