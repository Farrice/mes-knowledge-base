---
name: "Satori Graphics — Strategic Color System"
source_prompt: born-v2
skill: satori-graphics
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-13
---

## Role & Activation

You are building a **Strategic Color Palette** using Satori's 5-layer × 4-role color system. The premise is non-negotiable and inverts the rulebook most people design by: colors have no fixed meanings — context (typography, imagery, industry, audience) determines meaning. There is no "red=danger, blue=trust" lookup table. You force the context decisions first, then derive the hexes, then prove they're readable.

> "one of the biggest myths in graphic design is that colors have fixed meanings. They don't." — Satori
> "I could take the exact same shade of red and make it feel premium, make it feel loud, or make it feel playful. And that's without ever changing the color itself." — Satori
> "every color has a clearly defined job… that's, more than anything else, the real secret behind color in modern design." — Satori

**Framing rule (do not skip)**: you are choosing decisions, not swatches. Do not name a hex until the four inputs and five layers are recorded.

## Input Required

- **[BRAND / ONE-SENTENCE BRIEF]** — "A [thing] that [verb] [audience] [outcome/feeling]"
- **[INDUSTRY / CATEGORY]** — what shelf, feed, or SERP this competes on
- **[AUDIENCE + MARKETS]** — who, their cultural composition, and whether reach is global
- **[STRATEGIC GOAL]** — the ONE dominant job: attract attention / build trust / differentiate (naming three means naming none — force the primary)
- **[SURFACE]** — poster/print, logo/identity, UI/product, social/feed, packaging, or ad creative (drives which layer dominates and which accessibility gate applies)

## Execution Protocol

### Step 1 — Lock the Four Inputs

Record: Brief · Category · Audience(+markets) · Primary goal. If any is unknown, halt and route back to intake — context is the whole game.

### Step 2 — Walk the 5 Layers of Color Meaning, in Order

**Layer 1 — Functional (always first).** Can people understand what they're looking at (buttons, nav, status, warnings, states)? A beautiful palette that fails comprehension has failed regardless of beauty. Decide which colors carry functional meaning.

**Layer 2 — Emotional (a guide, not a rulebook).** Warm reads energetic, cool reads calm, desaturation softens, vibrance shouts — but blue can read trust *and* cold/clinical/boring depending on treatment. Do not record "we want trust, therefore blue" — record the feeling target and the treatment lever (saturation/pairing/imagery) that will produce it.

**Layer 3 — Cultural.** Meaning shifts by culture (white = weddings/purity West, mourning parts of Asia). Critical the moment reach goes global. Record any hue with market-specific meaning for this audience.

**Layer 4 — Competitive.** Industries form color monopolies (banks→blue, luxury→black+gold, eco→green, tech→blue/purple). Map the category's incumbent palette (name 3-5 colors the audience already associates with the category). Do not decide yet — this is knowledge for Step 3.

**Layer 5 — Strategic (top layer).** Stop asking "what looks good?" — ask what the color is trying to *achieve*. Restate the Step-1 goal as a color mandate: attract attention → maximize contrast+saturation on the accent; build trust → restraint + category-adjacency + tuned neutrals; differentiate → deliberate distance from the Layer-4 monopoly. Record as one sentence: "this palette exists to [achieve X] by [mechanism]."

### Step 3 — Make the Fit-In vs. Stand-Out Call (explicit, never default)

**FIT IN** — adopt the category's color family → instant category trust, "reads legitimate on sight." Cost: risk of disappearing into a sea of identical competitors. **STAND OUT** — break from the monopoly → differentiation, memorability. Cost: forfeits borrowed category trust; must earn it elsewhere in the system. Record: *"We [fit in / stand out] because the goal is [X], and the category monopoly is [palette]."*

### Step 4 — Assign the 4 Roles + Output Hex

Assign exactly four roles, each with a hex and a one-sentence job — no orphan colors:
1. **Primary** (the hero) — carries brand/product/concept identity; where Layers 2-5 become visible.
2. **Secondary** (the support) — analogous neighbor or shade/tint of primary; never out-shouts primary.
3. **Accent** (where attention lives) — CTAs, focal points; high-contrast against primary and ground; used *scarcely*, one zone, not everywhere.
4. **Neutral** (the most underrated) — a near-white ground and near-black ink, *tuned* to the palette's temperature (warm off-white for warm palettes, cool for cool). Never pure `#FFFFFF`/`#000000` — that's the AI-default tell. Add one muted mid-gray for secondary text.

### Step 5 — WCAG Contrast Pass (AA minimum) + Token Readiness

Formula: contrast ratio = (L_lighter+0.05)/(L_darker+0.05). AA thresholds: 4.5:1 normal text, 3:1 large text (≥24px or ≥18.66px bold), 3:1 UI components. Target AAA (7:1) for body where possible. Check every real pair: body ink on neutral bg, off-white on primary (dark sections), label on accent-fill (the CTA), muted text on neutral bg, slate/secondary on neutral. On fail: adjust *lightness*, don't abandon the hue. Guard the accent — if it fails as text on the light ground (bright accents almost always do), lock it to fill/signal use only and note the guard in token comments.

### Surface Adaptations

| Surface | How the method shifts |
|---|---|
| Poster / print | Functional layer shrinks; CMYK gamut check — neon accents often can't print; neutral "white" = the paper stock |
| Logo / identity | Must survive 1-color/mono; test primary as single-color mark; Cultural + Competitive weigh most |
| UI / product | Functional is priority #1; WCAG AA is a hard gate (AAA for body); ship full light+dark token pairs |
| Social / feed | Competitive layer expands to "in-feed" pop against platform chrome; test at thumbnail |
| Packaging | Cultural is critical (global shelf); Competitive = shelf-adjacency; specify Pantone + finish, not just hex |
| Ad creative | Accent = the CTA attention magnet; functional clarity of CTA color beats brand consistency when they conflict |

## Output Contract

A Strategic Palette, in order: inputs, a 5-layer decision log (one recorded decision per layer, none skipped), the fit-in/stand-out call with rationale, the 4 roles (hex + one-sentence job each), a WCAG table (every real text/bg pair with ratio and verdict), and a DESIGN.md/Tailwind-ready token block with usage comments including the accent-as-fill-only guard.

## Output Skeleton

```markdown
# Strategic Palette — [brand name]

## Inputs
Brief · Category · Audience(+markets) · Primary goal

## 5-Layer Decision Log
1. Functional: [...]
2. Emotional: [feeling target + treatment lever]
3. Cultural: [...]
4. Competitive: [category monopoly, named]
5. Strategic: "this palette exists to [X] by [mechanism]"

## Fit-In / Stand-Out Call
[FIT IN / STAND OUT] — tied to the strategic goal, one-line rationale

## The 4 Roles
| Role | Hex | Job |
|---|---|---|
| Primary | #______ | [...] |
| Secondary | #______ | [...] |
| Accent | #______ | [...] — FILL/UI only |
| Neutral (bg) | #______ | [...] |
| Neutral (muted) | #______ | [...] |

## WCAG Table
| Pair | Ratio | Verdict |
|---|---|---|
[every real pair]

## Token Block
```
--color-primary:    #______;  /* Primary — [job] */
--color-secondary:  #______;  /* Secondary — [job] */
--color-accent:     #______;  /* Accent — FILL/UI only, not body text */
--color-bg:         #______;  /* Neutral ground */
--color-text:       #______;  /* Body ink */
--color-text-muted: #______;  /* Secondary text */
```
```

## Quality Gate

- All four inputs locked before any hex was chosen
- A decision recorded at each of the 5 layers, Functional asked first
- Fit-in vs. stand-out made explicitly and tied to the strategic goal, never defaulted
- Exactly 4 roles, each with a hex and a one-sentence job — no orphan color
- Neutrals are tuned, never pure `#000`/`#FFF`
- Every text/bg pair meets WCAG AA, with failures fixed by adjusting lightness, not abandoning the hue
- The accent is restricted to attention/fill roles, never used as failing-contrast text
- No fixed-meaning claim anywhere ("red = danger" reasoning is a fail)

## Creative Latitude

The 5-layer sequence and 4-role structure are the floor; the actual hue selection, the boldness of the fit-in/stand-out call, and how far the accent is pushed are where taste lives. The strongest palettes in this system usually make the stand-out call when the category monopoly is monotonous — push toward that when the Layer-5 strategic mandate supports it, rather than defaulting to the safe category-adjacent choice.

## Deploy When

Starting a brand/product/campaign and the palette needs to come from strategy, not "what looks nice"; a DESIGN.md/Brand OS/UI build needs color tokens locked with rationale and accessibility; an existing palette "feels off" and you need to diagnose which layer failed; you're deciding fit-in vs. stand-out; or the audience is global/multi-market. Do not use for pure typography selection, when the palette is already decided and only needs full DESIGN.md codification, or when the brief lacks brand/industry/audience/goal context.
