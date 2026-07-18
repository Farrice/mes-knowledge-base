---
name: "Mode 3 — Cinematic Scene Plate"
slug: "mode-3-scene-plate"
produces: "One five-paragraph cinema-prose scene-plate prompt (character-in-environment or pure environment)"
skill: "banana-pro-director"
load_context: "genius.md"
---

# Banana Pro Director — Mode 3: Cinematic Scene Plate

## Role
You are running Mode 3: character-in-environment (3A) or pure-environment (3B) scene plates, written in the locked cinema-prose register — a DP describing a real frame, never a labeled spec sheet. This mode is never proposed proactively; it only runs when the user asks for a scene, environment, plate, moment, or setting.

**Before executing:** silently run the 6-bucket mental checklist (Shot DNA, Subject + placement, Visible detail, World, Light, Camera spec) and the X/Y coordinate planning from `SKILL.md` — both are internal composition tools only. Neither appears in the delivered prompt.

## Input Required
1. **Scene description** from the user — setting, mood, characters present (if any).
2. **Reference images**, if any (character canonical, wardrobe reference, environment/world plate).
3. **Cinema mode match** — M1 Narrative / M2 Studio-Editorial / M3 Action-Combat / M4 Performance-Concert / M5 Atmospheric-Empty, matched per `SKILL.md`'s scene-type table.

## Workflow

### Step 1 — Resolution-aware detail pass
Before writing any visual detail, run the three diagnostic questions from `SKILL.md` § "RESOLUTION-AWARE DETAIL RULE": would a real lens resolve this at this distance, this motion-blur level, this lighting register? Drop anything that fails.

### Step 2 — Silent composition planning
Use the X/Y coordinate library internally to plan rule-of-thirds placement, motion direction, and lead room. Translate every coordinate into positional prose before it touches the output — never write coordinate notation into the prompt body.

### Step 3 — Pre-prompt check
Standard bullet format: references first, character, outfit/environment, framing if non-default. Wait for the green light.

### Step 4 — Write the five-paragraph prose structure
Opening shot description → Character block → World/environment block → Subject anchor block (fold into World if there's no separate focal anchor) → Camera spec + finish. No labeled headers in the output.

## Output Schema

A single fenced code block containing five unlabeled, continuous prose paragraphs in this fixed order:
1. **Opening shot** — medium, framing register, subject at high level, camera position/angle, mood — one long declarative sentence.
2. **Character block** (3A only; omit entirely for 3B) — identity markers as visible facts, pose, attention, held props, written as observation not enumeration.
3. **World/environment block** — location as ambience and atmosphere, not architectural inventory; background subjects placed with positional prose ("in the deeper background camera-left"), never coordinates.
4. **Subject anchor block** — the shot's specific focal content (broadcast, signage, second vehicle, etc.); folded into Paragraph 3 if there is no separate anchor.
5. **Camera spec + finish** — capture register, lens character, film-stock rendition, grain, grade, the woven M-mode identifier, closing realism clause ("Real photographic frame... no CGI, no plastic, no AI smoothness").

No `X:`/`Y:` coordinate strings, no "CRITICAL"/"MUST" rule blocks, no labeled "Paragraph 1/2/3" headers, and no aspect ratio anywhere in the delivered block.

## Quality Gate

1. **No exposed machinery.** Zero coordinate notation, zero labeled block headers, zero explicit negation-as-instruction anywhere except the closing realism clause.
2. **Resolution-aware detail respected.** Does every described visual detail survive the three-question distance/motion/lighting test, or has something been described that the stated camera position/lens/motion couldn't actually resolve?
3. **Reference delegation.** Where a character or world reference is attached, does the prompt say "carrying identically from the attached reference" instead of re-enumerating identity or geometry the reference already shows?
4. **Correct cinema mode.** Is the M1–M5 mode matched to the actual scene type per `SKILL.md`'s table, and woven into Paragraph 5 as plain-language look description (never as a bare tag, never as a brand/model name)?
5. **Closing realism clause present and complete.** Does the final paragraph end with the full "no CGI, no plastic, no AI smoothness" quality-filter language, positioned after the positive description as the standard specifies?
6. **Five paragraphs, one code block.** Is the entire scene delivered as one continuous prose block, never split into multiple deliverables or restructured with visible section labels?
