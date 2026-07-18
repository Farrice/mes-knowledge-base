---
name: "M5 Atmospheric — Seedance Shot Build"
slug: "m5-atmospheric-shot"
produces: "One production-ready Seedance prompt in M5 Atmospheric register (abandoned environments, no-humans plates, landscapes, weather, mood establishing)"
skill: "cinema-worldbuilder-pro"
load_context: "genius.md"
---

# Cinema Worldbuilder Pro — M5 Atmospheric Shot

## Role
You are running Mode M5: abandoned environments, no-humans plates, landscapes, weather, mood establishing (`SKILL.md` Mode-Select Table, line 283). This is the environment-as-subject mode — camera is "locked-off or extremely slow push-in / pull-back" only (line 283), and the M5 Camera Capture line closes on an explicit statement: "No humans, environment is the subject." (`SKILL.md`, line 313).

## Input Required
1. Location, time of day, weather, and the palette (M5 requires actual hex values, not palette words — `SKILL.md` line 316).
2. Environment plate tag if a reference plate is attached (`@plate_tag`); M5 frequently runs plate-only with no character tags at all.
3. Runtime — locked-off atmospheric shots can run long; still always ask, never default.

## Workflow

### Step 1 — Pre-prompt confirmation
Tags → Mode (M5 Atmospheric) → Scene → Subjects (often "none — pure environment") → Frame Map → Camera → Cuts → Runtime (`SKILL.md` lines 123–137).

### Step 2 — Ten-block composition, no-humans variant
Same locked order (`SKILL.md` lines 162–184), but Subject Lock and Cross-Frame Rules are dropped entirely when no humans are in frame. Capture Realism drops the skin sentence and applies matte-not-glossy to environmental surfaces instead — "No humans (M5 pure environment) drops the skin sentence; keep atmosphere and contrast curve; apply matte-not-glossy to environmental surfaces (wet concrete, metal, glass)." (`SKILL.md`, line 379).

### Step 3 — M5 Camera Capture line
FOV° (mm) vintage 2x anamorphic, oval bokeh, soft edge falloff, light diffusion bloom, locked-off or extremely slow push-in only, color-negative film with fine grain, palette grade in actual hex values, atmospheric haze, weathered material detail, 24fps 180° shutter, runtime, closing on "No humans, environment is the subject." (`SKILL.md`, lines 311–313).

### Step 4 — Silent Pre-Delivery Pass
`SKILL.md` lines 478–501.

## Output Schema

Two parts in order: (1) bulleted pre-prompt check — Subjects line reads "none — pure environment" when applicable; (2) bolded title line with runtime + one fenced code block, blocks present limited to what the no-humans variant requires, `@plate_tag` anchored in World Plate.

## Quality Gate

1. **No-humans discipline held.** Subject Lock and Cross-Frame Rules are absent (not stubbed empty) when the scene has no human figures; Capture Realism's skin sentence is dropped, not left in with placeholder text.
2. **Hex values, not palette words.** M5's grade line names actual hex codes, per the mode's own requirement (`SKILL.md` line 283, "palette-driven (specify hex)").
3. **Camera motion register correct.** Locked-off or extremely slow push/pull only — no handheld, no orbital, no hard cuts unless the user explicitly requests a departure from the mode.
4. **Closing line present.** "No humans, environment is the subject." appears verbatim at the end of Camera Capture.
5. **Runtime match.** Title runtime equals Camera Capture runtime.
