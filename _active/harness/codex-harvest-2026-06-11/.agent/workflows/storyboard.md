# Storyboard Generation

Create complete multi-shot storyboard sequences with connected prompts, production notes, and the 4-act trailer structure. Produces frame-by-frame direction with platform-specific prompts for each shot.

## Expert Loading

Load `skills/creative-direction/SKILL.md` at Tier 1. Load `genius.md` at Tier 2 — storyboarding requires deep reference across visual language (Section 1), trailer storytelling (Section 5), and AI prompting (Section 3).

## Workflow

### Step 1: Define the Narrative Arc

- **What is the story?** (product reveal, brand story, campaign video, social content, music video)
- **How many frames?** (3-8, recommend based on complexity)
- **Emotional journey?** Map using the 4-act trailer structure:
  - Act 1: The World (establish setting, "normal")
  - Act 2: The Disruption (conflict, stakes, the change)
  - Act 3: The Escalation (maximum intensity, peak)
  - Act 4: The Resolve (final hook, open loop)
- **Platform?** (Higgsfield, Kittl, or both)
- **Trailer archetype?** (Cold Open, Slow Burn, Spectacle, Character Study, Mystery Box, Emotional Gut Punch, Hype Machine)

### Step 2: Establish Global Consistency

Lock these across ALL frames:
- **Subject description** (exact, reusable across prompts)
- **Visual world** (environment, time of day, weather, setting)
- **Color palette** (consistent grade across all frames, specific hex codes)
- **Style reference** (art movement, film reference, brand DNA)
- **SoulID notes** (if character consistency needed across shots)

### Step 3: Design Each Frame

For every frame, specify:
- **Frame number + act position** (e.g., Frame 3 — Act 2: The Disruption)
- **Shot type + camera angle** (from visual language reference)
- **Camera movement** (specific to this frame's narrative purpose)
- **Lens/focal length** (for depth and compression)
- **Action description** (what happens in this specific moment)
- **Lighting** (consistent with world but adapted to frame mood)
- **Sound design cue** (what the viewer should "hear")
- **Transition** to next frame (cut, dissolve, whip pan, match cut)
- **Duration** (in seconds)
- **Speed ramp** (Linear, Flash In, Slow-mo, Bullet Time, etc.)

### Step 4: Generate Platform-Specific Prompts

Write production-ready prompts for each frame using the correct formula:
- Higgsfield: Subject + Physics + Environment + Camera + Light + Mood + Style Ref
- Kittl Video: CAMERA / ACTION / AUDIO / TEXT blocks
- Include SoulID consistency notes for multi-character sequences

### Step 5: Production Notes

- **Generation order** — Which frames to generate first (hero shots first for SoulID reference)
- **SoulID notes** — Character lock strategy
- **Speed ramp mapping** — Which preset per frame
- **Credit-saving tips** — Which frames to validate with Popcorn first
- **Assembly notes** — Recommended edit sequence

## Output Format

```
## Storyboard: [Title]
**Frames:** [Count] | **Platform:** [Name] | **Arc:** [Archetype]
**Global Subject:** [Locked description]
**Global World:** [Environment]
**Global Palette:** [Hex codes]
**Style Reference:** [Film/director/movement]

---

### Frame 1 — [Title] (Act 1: The World)
**Shot:** [Type] | **Camera:** [Movement] | **Lens:** [Focal]
**Action:** [What happens]
**Lighting:** [Setup]
**Sound:** [Design cue]
**Transition:** [To next frame]
**Duration:** [Seconds] | **Speed Ramp:** [Type]

**Prompt:**
[Full platform-specific prompt]

---

[Repeat for each frame]

### Production Notes
**Generation Order:** [Sequence]
**SoulID Strategy:** [Character lock approach]
**Credit Budget:** [Where to save/spend]
**Assembly:** [Edit sequence recommendations]
```
