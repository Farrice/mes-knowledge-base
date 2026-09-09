# Template Conventions — index

This is the style guide for writing `template.html` and `instructions.md` per ref. It is NOT a strict schema — it's the shape of conventions to follow so templates stay consistent across the brand. If a convention doesn't fit your ref, deviate with a comment explaining why. The conventions are defaults, not laws.

> **Progressive disclosure.** The conventions are split into addressable slices so the builder loads only the slice the current step needs — never the full body at spawn. Read the slice for the step you're on:

| Slice | Covers | Read at |
|---|---|---|
| `conventions/slots-and-html.md` | File structure (1 template = 1 folder); `template.html` anatomy + key conventions; `instructions.md` anatomy; `## Slots` schema; strategy field values; bbox notation; **"When `_measurements.yaml` exists, it is the POSITION CONTRACT"** | Step 1 (Template Card) · Step 4 (author HTML) |
| `conventions/ai-image-zone.md` | What belongs inside an AI image zone vs HTML chrome; the `brand-badge` per-post logo slot; the **`[ai-image-zone:N]` comment block format** (Route A/B, fixed-hero vs free-subject `prompt_delta`, `identity_input`); how the runtime uses the blocks | Step 3 (generate) · Step 4 (write the block) |
| `conventions/routing-and-validation.md` | Background route decision; scene-template / pure-typography / complex-bg routes; chrome auto-inject; **anti-patterns** (brand-fidelity / process / hard-rule); validation gates G1–G4; `ai-image-style.md` format; `moves.md` meta-block format | Step 2.5 (substitution / route) · validation |

**Anchor cross-references** elsewhere in the pack (e.g. `template-conventions.md` "When `_measurements.yaml` exists…", `template-conventions.md` #8 / #9, "Third category — brand-badge", `[ai-image-zone]` → Route A) resolve to the slice that owns that section per the table above — `_measurements.yaml` / slot / numbered conventions → `slots-and-html.md`; `[ai-image-zone]` / brand-badge → `ai-image-zone.md`; anti-patterns / gates → `routing-and-validation.md`.
