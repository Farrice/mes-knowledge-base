---
name: "M3 Action — Seedance Shot Build"
slug: "m3-action-shot"
produces: "One production-ready Seedance prompt in M3 Action register (combat, chase, stunts, war, mech battles, debris, smoke)"
skill: "cinema-worldbuilder-pro"
load_context: "genius.md"
---

# Cinema Worldbuilder Pro — M3 Action Shot

## Role
You are running Mode M3: combat, chase, stunts, war, mech battles, alien encounters, debris, smoke, dust (`SKILL.md` Mode-Select Table, line 281). Movement register is "handheld and shaky throughout, no stabilized shots" (line 281) — this is the one mode where the shake itself is the locked default, not a deviation from it.

## Input Required
1. The action beat(s) — physical, converted to observable motion, never mood words ("fast bike chase" is not acceptable input to carry forward unchanged — convert to km/h per `SKILL.md` line 34).
2. Element tags for every subject, vehicle, and prop with a canonical reference.
3. Runtime and cuts precision register — action sequences frequently need timed multishot (`SKILL.md` lines 246–251).
4. Whether any beat needs impact slow-motion (triggers the 96fps append, `SKILL.md` line 304) or is a pressure-fracture/impactless break (`SKILL.md` lines 419–423).

## Workflow

### Step 1 — Pre-prompt confirmation
Tags → Mode (M3 Action) → Scene → Subjects → Frame Map → Camera → Cuts → Runtime (`SKILL.md` lines 123–137).

### Step 2 — Ten-block composition with cut discipline
Same locked block order (`SKILL.md` lines 162–184). Movement layers (character / micro / environmental / camera) stay separate, never tangled (`SKILL.md` line 344). Speed changes get a hard cut at every transition — "Never blend speed inside a single continuous shot — one speed per beat, cut cleanly at the transition." (`SKILL.md`, line 271).

### Step 3 — M3 Camera Capture line
FOV° (mm) vintage 2x anamorphic, oval bokeh, soft edge falloff, light diffusion bloom, handheld and shaky throughout with no stabilized shots, color-negative film with heavier low-light grain, palette descriptor with dusty atmospheric haze, 24fps 180° shutter, runtime (`SKILL.md`, lines 300–302). Impact slow-motion append: "intercut 96fps high-speed slow-motion at the [moment] holding 180° shutter for natural motion blur." (line 304).

### Step 4 — Special protocols check
If the beat involves cracks/breaks/debris without a clean impact point, apply the pressure-fracture protocol: edge stress or slow pressure, never a point-of-strike; fracture moves edge-inward; asymmetric timing (`SKILL.md` lines 419–423).

### Step 5 — Silent Pre-Delivery Pass
`SKILL.md` lines 478–501.

## Output Schema

Two parts in order: (1) bulleted pre-prompt check; (2) bolded title line with runtime + one fenced code block, ten labeled blocks, `@tag` inline, `CUT`/`HARD CUT`/timecode notation per the chosen cuts register (`SKILL.md` lines 246–260).

## Quality Gate

1. **No stabilization leakage.** M3's handheld-and-shaky default is present throughout — no locked-off or smooth-push language borrowed from M2/M5.
2. **Speed in km/h everywhere.** Every vehicle, running figure, or pan/tracking speed is a km/h value, never "fast"/"slow."
3. **One speed per beat.** Hard cuts sit at every real-time/slow-motion transition; nothing blends mid-shot.
4. **Cut vocabulary correct.** Only the recognized terms — HARD CUT, SMASH CUT, MATCH CUT, INSERT CUT, REVERSE CUT, WHIP CUT — appear, and whip pans carry at least 0.8s of motion (`SKILL.md` line 264).
5. **Continuity stated where the scene stresses it.** Same subject set, geometry, eyeline, light, wardrobe state, and prop states held across internal edits (`SKILL.md` line 262).
