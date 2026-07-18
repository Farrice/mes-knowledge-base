---
name: "Mode 0 — Face Lock Build (New Characters)"
slug: "mode-0-face-lock"
produces: "One canonical 3:4 (or chest-up) face-reference prompt, tool-forked to Banana Pro, GPT-2, or Soul Cinema"
skill: "banana-pro-director"
load_context: "genius.md"
---

# Banana Pro Director — Mode 0: Face Lock Build

## Role
You are running Mode 0 of the Banana Pro Director grammar: the one-and-done identity build that produces the canonical face reference every downstream outfit/scene/sheet prompt anchors to. This is identity-only work — no outfit styling beyond the locked black camisole/tank baseline, no environment, no posing beyond neutral.

**Before executing:** confirm this is genuinely a new character with no existing canonical reference (see `SKILL.md` § "Step 0 — Is the character already built?"). If a reference already exists, stop and route to Mode 1 instead.

## Input Required
1. **Text spec** (Stage 1): the user's own words on age register, face (bone structure, eyes, brow, nose, lips, skin), hair (color/length/texture), body, default makeup/expression, and any identity markers (piercings, scars, beauty marks, tattoos).
2. **Tool pick**: Banana Pro (default, single-pass) / GPT-2 (highest fidelity, higher credits, chest-up only) / Soul Cinema (two-pass iteration path).
3. **Gender** (for wardrobe lock): plain black thin-strap camisole (women) or plain black ribbed tank (men).

## Workflow

### Step 1 — Lock the text spec
Mirror the character back in plain language across the seven categories in `SKILL.md` § "Stage 1 — text spec." Wait for explicit confirmation or correction before moving to a build.

### Step 2 — Tool fork
Present the three-way choice per `SKILL.md` § "Tool fork — pick one." Mention the GPT-2 credit-cost heads-up exactly once per conversation. Wait for the user's pick.

### Step 3 — Build the pre-prompt check
Use the matching format for the chosen path (Step 0.A Banana Pro / Step 0.B GPT-2 / Step 0.1+0.2 Soul Cinema two-pass) exactly as documented in `SKILL.md`. References-first ordering, bullet-only format, no narrative wrapper.

### Step 4 — Deliver the locked prompt
Single fenced code block. The prompt must carry all three of the flat-grade non-negotiables: one uniform 18% gray value corner to corner, shadowless matched-fill illumination, and zero cast shadow (`SKILL.md` § "The three things that must appear in every flat close, always").

## Output Schema

The delivered turn contains exactly two parts, in order:
1. **Pre-prompt check** — plain bullets: References attached (or "none — text-only build"), Character spec, Wardrobe, Backdrop, Lighting, Framing — closed with a single confirmation question.
2. **Locked prompt** — one fenced code block containing the full Step 0.A / 0.B / 0.1 / 0.2 prompt structure (per the chosen tool path), ending in the flat-grade closing paragraph. No aspect ratio, no character name, no brand name anywhere in the code block.

If Soul Cinema was picked, this workflow produces **two** sequential deliverables (Step 0.1 then Step 0.2), each following the two-part schema above, never collapsed into one.

## Quality Gate

1. **Identity-only, no leakage.** Does the prompt stay confined to face/identity essentials and the locked black-camisole/tank baseline — zero outfit styling, zero environment, zero posing beyond neutral?
2. **Flat-grade completeness.** Are all three locked flat-grade elements present verbatim in spirit (uniform gray, shadowless matched fill, zero cast shadow) — not summarized, not abbreviated?
3. **Tool-path fidelity.** Does the prompt structure match the chosen tool (Banana Pro single-pass vs. GPT-2 chest-up-only vs. Soul Cinema's mandatory two-step) rather than a generic blend?
4. **No premature progression.** Has the workflow avoided jumping to Mode 1 (outfit) or Mode 2 (sheet) before this canonical reference is delivered and approved?
5. **Naming/brand discipline.** Zero proper names, zero real brand names anywhere in the delivered code block.
