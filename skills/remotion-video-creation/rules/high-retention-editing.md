# High-Retention Editing Rules
> Source: PJ Accetturo Post-Production Mastery + Social Media Best Practices

This file provides **editorial intelligence** for Remotion compositions. Use these rules to transform raw AI clips into cinematic, high-retention content.

---

## Core Philosophy

> "Editing isn't assembly; it's authorship. The same raw materials can become boring or electric depending on how they're cut."
> — PJ Accetturo

AI video has inherent imperfections. Editing:
1. **Masks weaknesses** (cut before artifacts)
2. **Amplifies strengths** (hold on beautiful frames)
3. **Creates momentum** (pacing carries viewers past technical limits)

---

## 1. Pacing Rules

### 1.1 The 2-Second Rule (Social Media)
- **No shot should exceed 2 seconds** in the first 5 seconds of a video
- This creates "scroll-stopping" velocity
- Exception: Emotional beat (a moment of silence for impact)

### 1.2 Staccato vs. Legato
| Pacing Style | Frame Count (30fps) | Use When |
|--------------|---------------------|----------|
| **Staccato** (Rapid) | 15-30 frames (0.5-1s) | Energy, urgency, tension, hooks |
| **Measured** | 45-90 frames (1.5-3s) | Explanation, product demos, trust |
| **Legato** (Slow) | 90-150+ frames (3-5s) | Emotion, aspiration, resolution |

### 1.3 Building Rhythm
Start FAST → Slow DOWN for product → ACCELERATE to CTA

```typescript
// Example: 10-second video pacing
// Frames per shot sequence:
const pacingMap = [
  30,  // 1s - Hook (fast)
  24,  // 0.8s - Problem 1 (faster)
  18,  // 0.6s - Problem 2 (fastest)
  60,  // 2s - Product reveal (slow, let it breathe)
  45,  // 1.5s - Feature 1
  45,  // 1.5s - Feature 2
  30,  // 1s - CTA build
  48,  // 1.6s - CTA hold (end strong)
];
```

---

## 2. Cut Strategy

### 2.1 Hard Cut (Default)
- Use for 80% of cuts
- Creates energy and forward momentum
- Essential for hiding AI artifacts (cut away before weirdness)

### 2.2 Dissolve / Cross-Fade
- Use **only** for emotional transitions
- Signals "time passing" or "tone shift"
- `duration: 6-12 frames` (very fast dissolve)

### 2.3 Crash Cut
- Hard cut with **simultaneous audio shift**
- Maximum impact for "breakthrough" moments
- Example: Anxiety → Peace transition

```typescript
// Remotion Crash Cut Pattern
<Sequence from={anxietyEndFrame} durationInFrames={1}>
  {/* Brief black/flash frame */}
  <AbsoluteFill style={{backgroundColor: 'white', opacity: 0.8}} />
</Sequence>
<Sequence from={anxietyEndFrame + 1}>
  <PeaceScene />
</Sequence>
```

### 2.4 Motion Match Cuts
- Cut on motion (hand moving, head turning)
- The viewer's eye follows the movement across the cut
- Hides jarring transitions between AI clips

---

## 3. AI Weakness Masking

### 3.1 Face Drift / Morphing
**Problem:** AI faces shift over multi-second clips.
**Solution:**
- Trim clip to 1-1.5s max
- Cut BEFORE the drift begins
- Use B-roll to cover the rest of the audio

### 3.2 Artifacts / Glitches
**Problem:** Random visual glitches in AI footage.
**Solution:**
- Add motion blur overlay during problematic frames
- Or: Cut 2 frames before the artifact
- Or: Apply aggressive zoom to hide artifact zone

### 3.3 Static / Robotic Motion
**Problem:** AI movement looks stiff.
**Solution:**
- Add subtle camera shake (1-3px random translate)
- Apply 0.95-1.05x speed variation
- Layer with handheld-style pan

```typescript
// Add organic motion to static AI clips
const organicOffset = Math.sin(frame * 0.1) * 3;
style={{ transform: `translate(${organicOffset}px, ${organicOffset * 0.5}px)` }}
```

---

## 4. Audio Architecture

### 4.1 The 3-Layer Stack
Every video needs three audio layers:
1. **Primary**: Voiceover or dialogue
2. **Secondary**: Music (mixed -6 to -12db below VO)
3. **Tertiary**: Sound design (swooshes, impacts, ambient)

### 4.2 Cut-to-Beat Sync
- Major cuts should land ON music beats
- Creates subliminal rhythm the viewer *feels*
- At 120 BPM, beats fall every 15 frames (30fps)

### 4.3 The "Pre-Fade" Technique
- Start music 10-15 frames BEFORE the scene it belongs to
- Creates anticipation and smooths transitions
- End music 5-10 frames AFTER the scene ends (tail)

---

## 5. Color Grading Patterns

### 5.1 Emotional Color Map
| Emotion | Grade |
|---------|-------|
| Anxiety / Struggle | Cool blue, desaturated, crushed blacks |
| Peace / Resolution | Warm golden, lifted shadows |
| Energy / Action | High saturation, punchy contrast |
| Premium / Trust | Neutral with subtle warmth, soft highlights |

### 5.2 Unifying AI Clips
AI clips from different generations have inconsistent color.
**Solution:** Apply a global LUT or grade in Remotion:

```tsx
// Global color grade wrapper
<AbsoluteFill style={{
  filter: 'saturate(0.9) contrast(1.1) brightness(1.02)',
  // Subtle warm overlay
  background: 'linear-gradient(rgba(255,200,150,0.05), transparent)'
}}>
  {children}
</AbsoluteFill>
```

---

## 6. Quality Checkpoints

Before final render, verify:

- [ ] **Hook Test**: Does something compelling happen in first 0.5 seconds?
- [ ] **3-Second Exit**: Would you keep watching after 3 seconds?
- [ ] **Face Check**: Any visible face drift/morphing?
- [ ] **Artifact Scan**: Any glitches visible at 1x speed?
- [ ] **Audio Sync**: Do cuts land on beats?
- [ ] **Color Consistency**: Do all clips feel unified?
- [ ] **CTA Clarity**: Is the call to action unmistakable?

---

## Integration with Remotion

When building compositions, reference these rules:

```typescript
// At the top of Composition.tsx
// @see rules/high-retention-editing.md for pacing and cut strategy
```

Apply the principles using:
- `Sequence` for precise cut timing
- `interpolate` for dissolves/fades
- `spring` for organic motion
- CSS `filter` for color grading
