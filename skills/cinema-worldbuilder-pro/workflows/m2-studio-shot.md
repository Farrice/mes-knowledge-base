---
name: "M2 Studio — Seedance Shot Build"
slug: "m2-studio-shot"
produces: "One production-ready Seedance prompt in M2 Studio register (white void, fashion film, editorial portrait, performance-on-set)"
skill: "cinema-worldbuilder-pro"
load_context: "genius.md"
---

# Cinema Worldbuilder Pro — M2 Studio Shot

## Role
You are running Mode M2: clean studio, hyperpop-saturated set, fashion film, editorial portrait, performance-on-set (`SKILL.md` Mode-Select Table, line 280). Unlike every other mode, M2 uses a **clean spherical** lens character — natural round bokeh, even sharpness — not the vintage anamorphic used everywhere else, and defaults to a **locked tripod with optional slow push**, not handheld (`SKILL.md`, line 280).

## Input Required
1. Scene description, subject count, and whether the surface is white-void or a saturated editorial set.
2. Element tags (character reference `_ref`, environment/set `_plate` if used).
3. Runtime — always ask.
4. Whether reflective surfaces (chrome, rhinestone) are in frame, which triggers the M2 highlight-bloom append (`SKILL.md`, line 298).

## Workflow

### Step 1 — Pre-prompt confirmation
Same fixed bullet order as every mode: Tags → Mode (M2 Studio) → Scene → Subjects → Frame Map → Camera → Cuts → Runtime (`SKILL.md` lines 123–137).

### Step 2 — Ten-block composition
Same locked block order as all modes (`SKILL.md` lines 162–184). M2's Capture Realism differs from the other four modes: "Studio M2 editorial gloss: reduce or skip — it's the one mode where controlled specular is intentional" (`SKILL.md`, line 379).

### Step 3 — M2 Camera Capture line
FOV° (mm) clean spherical, natural round bokeh, even sharpness, mild diffusion bloom, locked tripod with optional slow push-in, saturated editorial grade, fine grain, warm-retained blacks, 24fps 180° shutter, runtime (`SKILL.md`, lines 294–296). If chrome/rhinestone surfaces are in frame, append: "intentional highlight bloom on reflective surfaces, blooming the speculars on chrome and rhinestone." (`SKILL.md`, line 298).

### Step 4 — Silent Pre-Delivery Pass
Run `SKILL.md` lines 478–501 before delivering.

## Output Schema

Two parts in order: (1) bulleted pre-prompt check, tags first / runtime last; (2) bolded title line with runtime + one fenced code block with the ten labeled blocks, `@tag` inline. No character names, no platform names.

## Quality Gate

1. **Lens-family discipline.** Clean spherical is used, never the vintage 2x anamorphic that governs M1/M3/M4/M5 — this is the one mode where mixing lens families is a failure, not a style choice.
2. **Camera default correct.** Locked tripod with optional slow push, not handheld — M2 is the one mode where handheld-by-default would be a register break.
3. **Specular exception applied correctly.** Controlled gloss is only intentional here; the per-zone specular kill from `SKILL.md` line 370 is reduced or skipped in M2, not silently dropped everywhere else.
4. **Chrome/rhinestone append present when relevant.** If reflective wardrobe or props are named, the highlight-bloom append line is in the Camera Capture block.
5. **Runtime match.** Title runtime equals Camera Capture runtime.
