---
description: The count-the-contrasts diagnostic — walk an existing design zone by zone, name every contrast form present/absent/conflicting, score stack depth, and prescribe the minimum moves to reach the ship zone
---

# 23 — Contrast Audit

> **/satori-contrast-audit** — Read any design the way Satori reads the Nike poster: "Can you see the three different uses of contrast in this poster?" Name every form present. Fewer than 3 deliberate = flat. Many accidental = noise.

The diagnostic twin of `/satori-contrast-stack`. Same 9-form table, run in reverse — over your draft, a client's existing asset, or a competitor reference you want to steal structure from.

> *"When you actually pick apart designs in this way, you can then start to think about your own work and how you can apply principles on your own graphic designs."* — Satori

## Pre-Flight Gate

**Use this when**:
- A draft is "clean but forgettable" — the AI-default suspicion (evenly-distributed emphasis)
- Pre-delivery gate on any generated/AI-assisted layout (pairs with `/satori-anti-ai-slop`)
- Reverse-engineering a reference design that works, to extract its stack
- A CTA/conversion surface underperforms and the hypothesis is "nothing wins"

**Do NOT use this when**:
- Building the stack from scratch — `/satori-contrast-stack`
- The failure is comprehension *order* — `/satori-perception-gap` (contrast may be fine, sequencing wrong)
- Structural/technical issues — `/satori-flip-test`
- No design exists yet — nothing to audit

## Skill Acquisition

```
Load: skills/satori-graphics/genius.md
  ├─ GP-20 (Contrast Stack — the form taxonomy + operating rules)
  ├─ GP-18 (Three-Flow Rule — the anchors contrast should serve)
  └─ HK-13 (Contrast is choice architecture — behavioral reading for UI)
Load: skills/satori-graphics/references/contrast-stack.md
```

## Execution

### Step 1 — Identify the Anchors (or their absence)

Before counting, name the design's apparent Hook / Secondary / Finisher. If no spine is discernible, log it — the prescription will start at workflow 21, not with contrast moves.

### Step 2 — Walk the 9 Forms, Zone by Zone

For each form — color, size, typography, shape, style, texture, psychology, emotion, concept — mark:

| Verdict | Meaning | Evidence required |
|---|---|---|
| **PRESENT-deliberate** | The form exists and serves an anchor | One line: form → zone → what it makes win |
| **PRESENT-accidental** | The form exists but serves nothing (noise) | What it's hijacking |
| **CONFLICTING** | Two instances of the form fight each other | The two zones in contest |
| **ABSENT** | Not used | — |

Read like the Nike exercise: obvious first (color), then the trained-eye forms (shape: what geometry does the field speak, what breaks it? texture: what's tactile against what's flat?), then the advanced tier (what learned associations does the design obey — and does it ever flip one?).

For UI: read behaviorally (HK-13) — what does color contrast make clickable? What does size steer toward? Do cards double-whammy? Does anything contrast the device chrome?

### Step 3 — Score Stack Depth

- **Deliberate count** `< 3` → **FLAT** (generic risk; the AI-default signature)
- **3–5 deliberate, zonal** → **SHIP ZONE**
- **Accidental + conflicting > deliberate** → **NOISE** (contrast everywhere = contrast nowhere)

Also verdict: advanced tier — present-and-serving / absent-as-decision (evidence of intent) / absent-as-miss.

### Step 4 — Prescribe Minimum Moves

Prescribe the *fewest* moves to reach ship zone, in this order:
1. **Silence accidental/conflicting forms first** (HK-10: subtraction before addition — quiet the noise, don't add louder signal)
2. **Add missing basic forms** only where an anchor is losing its beat
3. **Consider one advanced flip** only if memorability is the brief's job

Each prescription: `MOVE (quiet/add/flip) → form → zone → expected effect on which anchor`.

### Step 5 — Output

Execution prompt: `references/prompts-v2/contrast-audit-report.md`

## Content-Type Adaptations

| Surface | Audit emphasis |
|---|---|
| **Poster/print** | Zonal discipline — is quiet space deliberate (Nike black-on-black) or accidental? |
| **UI/landing** | Behavioral: CTA color-pop, option size-steering, card double-whammy, urgency reds |
| **Social** | Frame 1 only carries the verdict; forms below the fold barely exist |
| **Brand system** | Typography contrast in the lockup; style consistency ACROSS assets (style contrast between assets = drift, not design) |
| **Competitor reference** | Extract the stack as a reusable recipe: forms → zones → effect |

## Output Requirements

A **Contrast Audit Report**: (1) apparent anchors (or "no spine — route to 21"), (2) the 9-form table with verdict + one-line evidence each, (3) depth score (FLAT / SHIP ZONE / NOISE) + advanced-tier verdict, (4) prescription list (minimum moves, quiet-first order), (5) one-line overall: what currently wins, what should.

## Quality Gate

- [ ] All 9 forms explicitly verdicted (no form skipped as "n/a" without reason)
- [ ] Every PRESENT verdict carries zone-level evidence, not vibes
- [ ] Deliberate vs. accidental distinguished (a form existing ≠ a form chosen)
- [ ] Prescriptions are minimum-move and quiet-first (never "add more contrast" as tier one)
- [ ] Advanced-tier absence classified as decision or miss — with evidence
- [ ] UI audits read behaviorally (what gets clicked), not just visually

## Related Workflows

- **`/satori-contrast-stack`** (22) — generative twin; run after the audit to rebuild the stack
- **`/satori-lift-audit`** (01) — when the audit reveals the deeper failure is hierarchy, not contrast
- **`/satori-anti-ai-slop`** (09) — pairs on generated work: flat emphasis + template perfection travel together
- **`/satori-flip-test`** (10) — the 90-second structural check alongside this 5-minute read
- **`/satori-three-flow`** (21) — where the prescription starts when no spine exists
