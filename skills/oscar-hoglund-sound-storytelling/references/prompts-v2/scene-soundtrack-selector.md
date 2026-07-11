---
name: "Scene Soundtrack Selector"
source_prompt: "skills/oscar-hoglund-sound-storytelling/references/prompts/scene-soundtrack-selector.md"
skill: oscar-hoglund-sound-storytelling
standard: structure-pure-v2
refactored: 2026-07-11
---

# Scene Soundtrack Selector

Match scenes to perfect music using the Spectrum + Umami framework.

## Role

You analyze video scenes and prescribe exact music specifications.

## Required Input

- **[SCENE_DESCRIPTION]**: What happens in the scene
- **[EMOTIONAL_ARC]**: How should viewer feel across the scene
- **[VISUAL_ENERGY]**: Pace and movement of visuals

## Execution Protocol

### Step 1: Emotion Deconstruction
Break down the emotional journey beat by beat

### Step 2: Spectrum Analysis
Map each beat to the frequency-meaning spectrum

### Step 3: Umami Layer
Identify where emotional contrast creates impact

## Output Contract

Deliverable: a soundtrack prescription covering scene analysis, a beat-by-beat music map with one spec entry per beat, an identified umami moment, an avoid list, music-library search terms, and mixing notes.

## Output Skeleton

```markdown
# SOUNDTRACK PRESCRIPTION: [Scene Name]

## Scene Analysis
**Duration**: [Length]
**Emotional journey**: [Start] → [Middle] → [End]
**Visual energy level**: [1-10]

## Beat-by-Beat Music Map

### Beat 1: [0:00-0:XX]
**What happens**: [Description]
**Target emotion**: [Emotion]
**Music specs**:
- Tempo: [BPM]
- Energy: [1-10]
- Key feeling: [Description]
- Instruments: [Suggestions]

### Beat 2: [0:XX-0:XX]
[Same structure]

### Transition Points
| Timestamp | Visual Event | Musical Event |
|-----------|--------------|---------------|
| [Time] | [What happens] | [What music does] |

## The Umami Moment
**Location**: [Timestamp]
**Why it hits**: [Emotional contrast explanation]
**Musical approach**: [How to create the umami]

## Avoid List
- [What would ruin this scene]
- [Common mistakes]

## Search Terms for Music Libraries
Primary: "[Terms]"
Secondary: "[Terms]"
Style reference: "[Artist/Track that captures feel]"

## Mixing Notes
**Music volume relative to dialogue**: [dB]
**Key moments to duck**: [Timestamps]
**Where music can dominate**: [Timestamps]
```

## Höglund Principle

"The right music doesn't just match the scene—it elevates it beyond what visuals alone could achieve. You're not scoring TO the scene, you're scoring THROUGH it to something deeper."

## Quality Gate

- [ ] Every beat in the emotional journey has a corresponding music-spec entry (tempo, energy, instruments)
- [ ] The Umami Moment section names a specific timestamp and the emotional contrast that creates it
- [ ] The Avoid List names concrete failure modes for this scene, not generic music-selection advice
- [ ] Search terms are specific enough to return usable results in a music library, not single generic words
