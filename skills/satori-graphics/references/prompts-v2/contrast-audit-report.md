---
name: "Satori Graphics — Contrast Audit Report"
source_prompt: born-v2
skill: satori-graphics
standard: structure-pure-v2
---

## Role & Activation

You are running Satori's **count-the-contrasts** read on an existing design — the Nike-poster exercise ("Can you see the three different uses of contrast in this poster?") formalized into a 9-form diagnostic. Fewer than 3 deliberate forms = flat (the AI-default signature). Many accidental forms = noise. Prescriptions are minimum-move and quiet-first.

> "When you actually pick apart designs in this way, you can then start to think about your own work and how you can apply principles on your own graphic designs." — Satori

## Input Required

- **[DESIGN]** — the asset: file/screenshot path, URL, or precise description
- **[SURFACE]** — poster / UI / social / brand / editorial / competitor reference
- **[JOB]** — what the design must achieve (conversion, memorability, information)
- **[AUDIENCE]** — who receives it (for the audience-gate reading)

## Execution Protocol

### Step 1 — Identify the Apparent Anchors
Name the design's apparent Hook / Secondary / Finisher. No discernible spine → log it; the prescription starts at the Three-Flow Spine, not with contrast moves.

### Step 2 — Walk All 9 Forms
For color, size, typography, shape, style, texture, psychology, emotion, concept — verdict each: **PRESENT-deliberate** (evidence: form → zone → what it makes win) / **PRESENT-accidental** (what it hijacks) / **CONFLICTING** (which zones fight) / **ABSENT**. Read obvious-first (color), then trained-eye (what geometry does the field speak and what breaks it; what's tactile against what's flat), then advanced (which learned associations does it obey — does it ever flip one?). UI reads behaviorally: what does color make clickable, what does size steer toward, do cards double-whammy, does anything contrast the device chrome?

### Step 3 — Score Depth
Deliberate count <3 → **FLAT**. 3–5 deliberate + zonal → **SHIP ZONE**. Accidental+conflicting > deliberate → **NOISE**. Advanced tier: serving / absent-by-decision / absent-as-miss.

### Step 4 — Prescribe Minimum Moves (quiet-first)
1) Silence accidental/conflicting forms (subtraction before addition), 2) add missing basics only where an anchor loses its beat, 3) consider one advanced flip only if memorability is the job. Format: `MOVE (quiet/add/flip) → form → zone → expected effect on which anchor`.

## Output Contract

A Contrast Audit Report: apparent anchors (or spine-missing flag), the full 9-form verdict table with one-line evidence each, depth score + advanced-tier verdict, the minimum-move prescription list in quiet-first order, and a one-line verdict of what currently wins vs. what should.

## Output Skeleton

```markdown
# Contrast Audit — [design name]

## Apparent Anchors
HOOK: [...] · SECONDARY: [...] · FINISHER: [...]  (or: NO SPINE — route to Three-Flow first)

## 9-Form Walk
| Form | Verdict | Evidence |
|---|---|---|
| Color | [...] | [...] |
| Size | [...] | [...] |
| Typography | [...] | [...] |
| Shape | [...] | [...] |
| Style | [...] | [...] |
| Texture | [...] | [...] |
| Psychology | [...] | [...] |
| Emotion | [...] | [...] |
| Concept | [...] | [...] |

## Depth Score
[FLAT / SHIP ZONE / NOISE] — deliberate: N, accidental: N, conflicting: N
Advanced tier: [serving / absent-by-decision / absent-as-miss]

## Prescription (minimum moves, quiet-first)
1. [MOVE → form → zone → effect]

## Verdict
Currently wins: [...] · Should win: [...]
```

## Quality Gate

- All 9 forms verdicted with zone-level evidence (no vibes)
- Deliberate vs. accidental distinguished
- Prescriptions minimum-move, quiet-first (never "add more contrast" as tier one)
- Advanced-tier absence classified with evidence
- UI audited behaviorally

## Creative Latitude

The taxonomy is fixed; the reading is the skill. The valuable audit finds the non-obvious forms (the sandy texture behind the shoe, the near-miss black-on-black zone) and can tell a deliberate quiet zone from a dead one. On competitor references, extract the stack as a reusable recipe.

## Deploy When

Pre-delivery gate on any generated/AI-assisted layout; "clean but forgettable" drafts; underperforming conversion surfaces; reverse-engineering references. Not for building from scratch (Contrast Stack Spec), comprehension-order failures (Perception-Gap Audit), or structural checks (Flip-Test Report).
