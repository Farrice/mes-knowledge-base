---
name: "Mode 2A — 3-Panel Character Sheet (Default)"
slug: "mode-2a-character-sheet"
produces: "One horizontal three-panel character reference sheet prompt (headless front / rear / chest-up face lock)"
skill: "banana-pro-director"
load_context: "genius.md"
---

# Banana Pro Director — Mode 2A: 3-Panel Character Sheet

## Role
You are running Mode 2A: the default character-sheet format. Three panels in one horizontal frame — full body front (headless), full body rear (head attached), and a tight chest-up face lock. This is the primary sheet format; the 6-panel (Mode 2B) is legacy and only runs on explicit user request, never proposed here.

**Before executing:** confirm a Mode 1 single-image base outfit reference already exists and is approved. If not, stop and build that first — `SKILL.md` § Mode 2 is explicit that the sheet is "built ONLY after a single-image base reference exists."

## Input Required
1. **Approved base reference** (from Mode 0 + Mode 1) — the locked character and locked outfit this sheet will replicate across three panels.
2. **Garment neckline read**, to select the headless-cut variant:
   - Variant A (ghost mannequin / hollow) — structured or closed necklines (collar, crew neck, tank, turtleneck, hood, keyhole).
   - Variant B (clean neck cut) — strapless, halter, spaghetti-strap, deep cowl, scooped/plunging necklines.
3. Any reference images to attach (character canonical, wardrobe reference).

## Workflow

### Step 1 — Confirm format
If the user asked for "a character sheet" with no format named, proceed straight to the 3-panel. Do not ask which format, do not mention the 6-panel exists.

### Step 2 — Read the neckline, pick the variant
Apply the diagnostic in `SKILL.md` § "THE HEADLESS CUT — TWO VARIANTS (PICK BY GARMENT)." Wrong-variant selection is the most common failure mode for this workflow — re-check the garment's neckline against the two definitions before writing.

### Step 3 — Pre-prompt check
Bullet format per `SKILL.md` § "Mode 2A pre-prompt check": References, Left, Center, Right, Outfit, Backdrop. Wait for the green light.

### Step 4 — Deliver the single prompt
One fenced code block containing the identity paragraph (once), the wardrobe paragraph (once), all three labeled panels (LEFT/CENTER/RIGHT), and the uniform flat-grade close stated as applying across all three panels — never three separate prompts.

## Output Schema

A single fenced code block containing, in this exact order:
1. One identity paragraph (build, skin, hair, makeup, identity markers, nails) — stated once, governs all three panels.
2. One wardrobe paragraph (full outfit head-to-toe) — stated once, governs all three panels.
3. **LEFT PANEL** — headless front, using the locked Variant A or Variant B language verbatim (with garment-specific fill-ins), full headroom preserved, hair removed with the head.
4. **CENTER PANEL** — full body rear, head attached, hair fall and garment back construction described.
5. **RIGHT PANEL** — tight chest-up face lock, explicitly *not* waist-up.
6. The closing flat-grade paragraph, stating explicitly that the gray value, shadowless light, and zero-cast-shadow are identical across all three panels, plus the mandatory skin-tone consistency clause.

No aspect ratio anywhere in the block. No panel delivered as a separate prompt.

## Quality Gate

1. **Correct variant.** Does the LEFT panel use the ghost-mannequin hollow (Variant A) for a structured neckline or the clean neck cut (Variant B) for a bare-shoulder garment — matched correctly to the actual garment, not defaulted?
2. **Right panel discipline.** Is the RIGHT panel framed chest-up (not waist-up) with the face filling most of the panel — the sheet's whole reason for existing?
3. **Skin-tone consistency clause present.** Does the prompt explicitly state identical skin value/hue across all three panels? (`SKILL.md` flags this as the #1 place rear panels drift darker/tanner without it.)
4. **Uniform flat grade, stated per-panel.** Is the flatness (gray value, shadowless light, zero cast shadow) declared as applying uniformly across all three cells, not just once at the top?
5. **Single prompt, single output.** Is this one fenced code block producing one image with three panels — never three separate deliverables?
6. **6-panel never offered.** Did the workflow avoid mentioning or proposing Mode 2B unless the user named it first?
