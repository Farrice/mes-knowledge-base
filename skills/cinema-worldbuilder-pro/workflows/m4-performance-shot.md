---
name: "M4 Performance — Seedance Shot Build"
slug: "m4-performance-shot"
produces: "One production-ready Seedance prompt in M4 Performance register (stadium, arena, stage, jumbotron, lightstick crowd, festival pit)"
skill: "cinema-worldbuilder-pro"
load_context: "genius.md"
---

# Cinema Worldbuilder Pro — M4 Performance Shot

## Role
You are running Mode M4: stadium, arena, stage, jumbotron, lightstick crowd, festival pit (`SKILL.md` Mode-Select Table, line 282). Movement is "mixed handheld pit-photographer and orbital, hard cuts" (line 282) and the lens character carries "horizontal streak flares" on stage lights that no other mode uses (`SKILL.md`, line 308).

## Input Required
1. Performer(s) and crowd scale, plus whether this is a single-performer stage shot or a crowd/pit composite.
2. Element tags for every performer with a canonical reference (crowd figures do not get individual tags unless named).
3. Stage-lighting color cast in scene language (e.g. "magenta-red from LED cube above," "amber and ultraviolet wash from side rigs" — `SKILL.md` line 316).
4. Runtime and cuts register — M4 defaults toward hard cuts between angles (`SKILL.md` line 282).

## Workflow

### Step 1 — Pre-prompt confirmation
Tags → Mode (M4 Performance) → Scene → Subjects → Frame Map → Camera → Cuts → Runtime (`SKILL.md` lines 123–137).

### Step 2 — Ten-block composition
Same locked order (`SKILL.md` lines 162–184). Sound Bed stays diegetic-only even in a performance context — crowd noise and stage diegetic sounds are permitted, but never song names, lyrics, or "music plays" (`SKILL.md` line 355).

### Step 3 — M4 Camera Capture line
FOV° (mm) vintage 2x anamorphic, oval bokeh, horizontal streak flares on stage lights, light diffusion bloom, mixed handheld pit-photographer and orbital operator energy with hard cuts between angles, color-negative film with fine grain, stage-lighting color cast, heavy volumetric haze, real sweat sheen, 24fps 180° shutter, runtime (`SKILL.md`, lines 306–308). Replace the color-cast bracket with scene-specific language, never a bare palette list (`SKILL.md` line 316).

### Step 4 — Silent Pre-Delivery Pass
`SKILL.md` lines 478–501.

## Output Schema

Two parts in order: (1) bulleted pre-prompt check; (2) bolded title line with runtime + one fenced code block, ten labeled blocks, `@tag` inline, hard-cut triggers named in Movement per `SKILL.md` line 467.

## Quality Gate

1. **Streak-flare texture present.** Horizontal streak flares on stage lights are named in Camera Capture — the detail that distinguishes M4 from M1/M3/M5's shared anamorphic base.
2. **Stage color cast tied to a real source.** Every hue in World Plate/Camera Capture is attached to a named light source (LED cube, side rig, jumbotron), never a bare color-word list (`SKILL.md` line 196).
3. **Diegetic audio holds under performance pressure.** No song titles, lyrics, or score descriptors leak into Sound Bed even though the scene is a concert.
4. **Real sweat sheen, not glossy skin.** Capture Realism's per-zone specular kill on skin still applies (`SKILL.md` line 370) even as the environment itself reads volumetric and heavy-haze.
5. **Runtime match.** Title runtime equals Camera Capture runtime.
