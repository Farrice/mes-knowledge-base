# Synthesize DESIGN.md from a Creative Brief

Generate a complete, production-grade DESIGN.md from a verbal brief — no source URL, no codebase, no brand to copy. The hardest mode; the highest taste bar.

## When to use

- User describes a *feeling* or aesthetic ("brutalist + warm dark mode for dev tools")
- New product / new brand with no precedent
- Library import would feel derivative

## Inputs

- `brief` — the user's verbal description (1-3 sentences ideal)
- `output_path` — where to write (default: `./DESIGN.md`)

## Pre-Workflow: Tier 1.5 Recall Grounding

Per `directives/recall-grounding-protocol.md`, this workflow is grounding-relevant. **Auto-fire silently:**

```
mcp__recall__search(query="<brief keywords>", limit=5)
```

Pull 1-3 high-signal cards on the named aesthetic, design movement, or brand archetype. Inject as source material in the synthesis. If signal is weak (< 2 cards), skip silently and proceed without grounding.

## Pre-Workflow: Taste Calibration

For high-stakes work (client deliverable, launch product), route through taste skills before drafting tokens:

1. Read `skills/oren-taste-development/SKILL.md` (Tier 1) — frame the aesthetic question
2. Read `skills/nate-b-jones-ai-taste-mastery/SKILL.md` (Tier 1) — judgment calibration

Skip for prototypes / internal tools. The cost is ~2-3K tokens; only worth it when output ships.

## Workflow

### Step 1 — Deconstruct the brief

Pull out:
- **Cultural anchor(s)** — named movements, eras, or brands ("brutalist," "Bauhaus," "1970s NASA telemetry")
- **Tension** — what two things are in conflict? ("brutalist + warm" — concrete + cozy)
- **Functional surface** — what's it for? (dev tools, consumer fintech, editorial newsletter)
- **Emotional target** — primary + secondary feelings the user should experience

If any dimension is missing, ask **one** clarifying question. Never ask more than one.

### Step 2 — Establish the visual thesis

Write the `description` field FIRST. Constraint: 2-3 sentences, must include both anchors of the tension, must name a cultural reference.

✓ "Brutalist precision meets warm dark-mode hospitality. The interface borrows the structural confidence of Vignelli's Subway Map but renders it in the glow of 1990s cathode ray monitors."

✗ "A modern, clean design system for dev tools."

The `## Overview` markdown section expands this thesis into 2-3 paragraphs. If you can't write the description in this voice, route to taste skills.

### Step 3 — Pick the cultural anchors' actual tokens

For each anchor, source real values:

| Anchor | What to borrow |
|---|---|
| Bauhaus | Primary triad (red/yellow/blue), geometric sans (Futura), strict grid |
| Brutalist | Concrete grays, monospace overlays, harsh contrast, 0px radius |
| 1970s NASA | Orange/charcoal/cream, technical labels in caps, fixed-width data |
| Editorial broadsheet | Serif headlines, generous leading, hairline rules |
| Y2K / cybernetic | Neon greens / cyans, scanline textures, glow effects |
| Scandinavian | Warm neutrals, sans-serif (Inter/IBM Plex), generous whitespace |

If the brief names a brand ("X.com but classier"), pull the brand's library file as inspiration but customize per [03-import-brand.md](03-import-brand.md).

### Step 4 — Build the color palette

Start with 4 semantic tokens minimum:
- `primary` — the brand anchor; the most-loaded color
- `neutral` — body background canvas
- `ink` — primary text
- One of: `tertiary` (accent CTA) OR `surface` (card / panel)

Add `secondary` if you need a third tier (typically subdued slate for borders/captions).

**Test contrast immediately:** every text/background pair must clear WCAG AA (4.5:1) before you commit. Use `npx @google/design.md lint` after drafting — fix in priority order.

### Step 5 — Build typography

Pick fonts:
- One primary typeface (covers headlines + body) — easier to ship
- Optional second typeface for a specific role (technical labels, long-form serif body)

Define 9-12 levels. Don't sprawl. Canonical naming:
```
hero-display  (only for marketing)
headline-lg, headline-md, headline-sm
body-lg, body-md, body-sm
label-md, label-sm, label-caps
caption
```

### Step 6 — Decide the geometric register

Pick one and commit:
- **Sharp** — `rounded.sm: 4px`, `rounded.md: 6px` — feels engineered, brutalist, editorial
- **Soft** — `rounded.sm: 8px`, `rounded.md: 12px`, `rounded.lg: 16px` — feels approachable, consumer
- **Pill-friendly** — heavy use of `rounded.full` for chips and buttons — playful, modern consumer

### Step 7 — Spacing scale

Use 4px or 8px base unit. Stick to one scale:
```
xs: 4px, sm: 8px, md: 16px, lg: 32px, xl: 64px
```

Some brutalist/density-first systems use 2px gridlines — fine, but document why in `## Layout`.

### Step 8 — Components

Define minimum 4 component blocks: `button-primary`, `button-secondary`, `input`, `card`. Add hover variants for interactives. Reference tokens via `{path.to.token}`, never literals.

### Step 9 — Write the markdown body

8 sections in order. Don't skip `## Do's and Don'ts` — it's where the brand's discipline lives. Examples:

✓ "Do use the tertiary color only for the single most important action per screen."
✓ "Don't mix sharp and soft corners in the same view."
✓ "Don't use more than two type weights on a single screen."

Generic don'ts ("don't use too much color") are useless — make them specific.

### Step 10 — Validate

```bash
python3 execution/design_md_validate.py <output_path>
```

Iterate until 0 errors and ≤ 2 warnings. Refer to `genius.md` Section 4 for the 7 lint-fix patterns.

### Step 11 — The Virgil Test

Before declaring done, apply (from `genius.md` Section 7):

1. Does it have a clear point of view? (read `description` aloud — does it sound generic?)
2. Is there a specific cultural anchor? (named movement / era / reference?)
3. One-sentence concept test — can you describe the brand in one sentence?
4. Would removing any token make the system stronger? (cut bloat)
5. Would this still be interesting without the logo?

If any answer is weak, revise before shipping.

## Quality bar

Synthesize-from-brief is the highest-craft mode. It must:
- Pass lint with 0 errors and ≤ 2 warnings
- Pass the Virgil Test (all 5)
- Name at least one specific cultural reference in the description
- Have a tension that distinguishes it from competitors

If output feels generic, you under-loaded taste skills or skipped Recall grounding. Re-run.

## See also

- [genius.md](../genius.md) — Sections 1-2 (token theory), Section 3 (WCAG math), Section 7 (Virgil Test)
- [examples/yaml-token-format.md](../examples/yaml-token-format.md) — Heritage example (full structure reference)
- `skills/creative-direction/genius.md` — for cinematic/visual extension once tokens are set
