---
name: "M1 Narrative — Seedance Shot Build"
slug: "m1-narrative-shot"
produces: "One production-ready Seedance prompt in M1 Narrative register (streets, kitchens, cars, bars, any lived-in real-world space)"
skill: "cinema-worldbuilder-pro"
load_context: "genius.md"
---

# Cinema Worldbuilder Pro — M1 Narrative Shot

## Role
You are running Mode M1 of the Cinema Worldbuilder Pro grammar: real-world dramatic coverage — "Anywhere lived-in," per `SKILL.md`'s Mode-Select Table (line 278). Capture register is wide-latitude cinema on a vintage 2x anamorphic character with handheld operator breath and a color-negative daylight film, teal-amber grade (`SKILL.md`, line 279). This is the default dramatic register — use it unless the scene names a studio set (M2), combat/stunts (M3), a stage/crowd (M4), or a no-humans environment plate (M5).

## Input Required
1. The scene in the user's own words — who, what happens, where, runtime.
2. Element tags for every subject/plate in the scene (ask per `SKILL.md` line 87 if not yet named — never invent tags).
3. Runtime in seconds (never default — `SKILL.md` line 148: "Never assume runtime — ask").
4. Cuts precision register: oner / sequential / timed / freestyle (`SKILL.md` lines 237–260).

## Workflow

### Step 1 — Character gate (first prompt of session only)
Ask the session-opener question once (`SKILL.md` line 108) and carry the answer forward for the rest of the session.

### Step 2 — Pre-prompt confirmation
Bulleted check in the fixed order: Tags → Mode (M1 Narrative) → Scene → Subjects → Frame Map → Camera → Cuts → Runtime (`SKILL.md` lines 123–137). Wait for the green light unless this is an iteration on a prompt just delivered.

### Step 3 — Compose the code block
Ten blocks in the locked order: Scene & Mood → Frame Map → Subject Lock(s) → Cross-Frame Rules → Movement → Last Frame → World Plate → Sound Bed → Capture Realism → Camera Capture (`SKILL.md` lines 162–184). Write the visible throughout — km/h for speed, % + meters for atmosphere, muscle cues for emotion (`SKILL.md` lines 37–46).

### Step 4 — M1 Camera Capture line
Use the M1 template verbatim in structure: FOV° (mm) vintage 2x anamorphic, oval bokeh, soft edge falloff, light diffusion bloom, handheld with natural operator breath, color-negative daylight film with fine 35mm grain, teal-amber grade, shallow depth of field, 24fps 180° shutter, runtime (`SKILL.md`, lines 289–291).

### Step 5 — Silent Pre-Delivery Pass
Run the full checklist at `SKILL.md` lines 478–501 before delivering. Never surface the checklist itself.

## Output Schema

The delivered turn contains exactly two parts, in order:
1. **Pre-prompt check** — bulleted, tags first, runtime last, closing on "Sound good?" (`SKILL.md` line 136).
2. **Locked prompt** — a bolded title line with runtime (e.g. `**Seedance prompt — 12s**`) followed by one fenced code block containing the ten labeled blocks with inline `@tag` references. No character names, no platform names, no on-screen text unless requested (`SKILL.md` lines 461–474).

## Quality Gate

1. **Register discipline.** Vintage 2x anamorphic + handheld + teal-amber grade held throughout — no clean-spherical (M2) or locked-tripod (M5) language leaking in unless the user explicitly requested it.
2. **Write-the-visible pass.** Zero mood-word abstractions; every emotion, speed, and atmosphere value converted to km/h, %, meters, or a muscle cue.
3. **FOV on the ladder.** The Camera Capture FOV is one of the nine discrete anchor values (`SKILL.md` line 215), never an off-ladder degree.
4. **Wardrobe not re-described.** Subject Lock trusts the reference for wardrobe; only state-changes the reference can't carry (damp, dirty, torn) appear.
5. **Runtime match.** Title-line runtime equals the Camera Capture closing-line runtime; per-shot timing sums if multi-cut.
