---
description: Generate a strategic color palette — walk the 5 layers of color meaning, make an explicit fit-in-vs-stand-out call, and output 4 role-assigned colors with hex values, one-sentence jobs, and WCAG-checked pairs ready for a DESIGN.md tokens block.
---

# 17 — Strategic Color System (/satori-color)

> Turn "what color should this be?" into a defensible decision: a 5-layer meaning log, an explicit fit-in/stand-out call, and four role-assigned colors with hex + job + WCAG note — a palette you can paste straight into a DESIGN.md tokens block.

Color was the gap in this skill — previously deferred to "pick something that looks good." This closes it. The premise is non-negotiable and it inverts the rulebook most people design by:

> *"one of the biggest myths in graphic design is that colors have fixed meanings. They don't."* — Satori

There is no "red = danger, blue = trust" lookup table here. Meaning is set by context — the typography around the color, the imagery, the industry, the audience. This workflow forces the context decisions first, then derives the hexes, then proves they're readable. Aesthetic-first is the failure mode; decision-first is the whole method (`genius.md` — GP-01, Anti-Pattern #8).

## Pre-Flight Gate

**Use this when**:
- Starting a brand, product, or campaign and the palette needs to come *from strategy*, not from "what looks nice"
- A DESIGN.md, Brand OS, or UI build needs color tokens locked with rationale + accessibility
- An existing palette "feels off" and you need to diagnose *which of the 5 layers* it failed
- You're deciding whether to blend into a category or break from it — a positioning-level color call
- The audience is global / multi-market and cultural color meaning is live

**Do NOT use this when**:
- The task is pure typography selection → use `kittl-graphic-design`
- You just need a stylized poster/image *produced* → use `fantastic-posters` (this workflow *decides* the palette; posters *consume* it)
- The palette is already decided and you only need it codified into a full system → use `/satori-design-md-grid` (this feeds it; that formats the whole DESIGN.md)
- You're writing an AI image/video prompt's color direction → use `creative-direction`
- The brief is unclear — no brand, industry, audience, or goal. Fix intake first:

> *"context is super super important when considering the meaning of color."* — Satori

Without the four inputs there is no context, and without context there is no correct color. Halt and get them. Per `genius.md` ("When NOT to Use Satori Tools"), Satori owns the composition/psychology layer that sits *above* type (Kittl) and *below* DESIGN.md codification (Jack Roberts) — color strategy lives here; token codification lives one layer down.

## Skill Acquisition

```
Load: skills/satori-graphics/genius.md
Load: skills/satori-graphics/references/color-system.md    # deep companion — the 5 layers + 4-role system in full depth
Load: skills/satori-graphics/references/source-quotes.md    # verbatim Satori grounding
```

Relevant `genius.md` patterns to have in hand:
- **GP-01 (Why-Before-What)** — every color must pay rent by earning a defined job
- **GP-08 (One-Sentence Brief)** — the brand sentence feeds the intake in Step 1
- **GP-02 (Predictive Empathy)** — powers the Emotional layer (design for the *next* emotion)
- **GP-11 (Anti-AI-Slop)** — neutrals are tuned, never mechanical `#000`/`#FFF`

## Execution

**Framing rule (do not skip):** you are choosing *decisions*, not swatches. Do not open a color picker until Steps 1–3 are recorded. A color with no upstream decision is decoration, and decoration without reason gets evicted.

### Step 1: Lock the Four Inputs (Intake)

Write down all four before touching a hex. If any is unknown, halt and route back to intake — context is the whole game.

- **Brand** — the one-sentence brief (GP-08). *"A [thing] that [verb] [audience] [outcome/feeling]."*
- **Industry / category** — what shelf, feed, or SERP this competes on
- **Audience** — who, and critically their **cultural composition** and whether reach is global (this arms Layer 3)
- **Strategic goal** — pick the ONE dominant job: **attract attention** / **build trust** / **differentiate**. If you name three, you've named none — force the primary.

Record: `Brief · Category · Audience(+markets) · Primary goal`.

### Step 2: Walk the 5 Layers of Color Meaning

Walk them **in order**. Each layer produces exactly one recorded decision. This ordered pass is the "5-layer decision log" in the output — do not jump to the pretty layer (Emotional) and skip Functional.

**Layer 1 — FUNCTIONAL (ask this first, always).**
Color that helps people *understand*: buttons, nav, status, warnings, dashboard states, focus rings. Ask: *"Can a person understand what they're looking at?"* If the palette can't answer that, it has failed its primary job **regardless of how beautiful it is**. Decide: which colors will carry meaning-of-function (interactive vs static, success/warn/error/info if applicable).
→ *Decision recorded:* functional roles the palette must serve.

**Layer 2 — EMOTIONAL (a guide, not a rulebook).**
How the color makes people *feel* — warm reads energetic, cool reads calm; desaturation/tints soften, vibrance shouts. Blue can read trust *and* cold/corporate/clinical/boring depending on use. This is where the myth dies:

> *"I could take the exact same shade of red and make it feel premium, make it feel loud, or make it feel playful. And that's without ever changing the color itself."* — Satori

So do not record "we want trust, therefore blue." Record the *feeling target* and note that treatment (saturation, pairing, imagery) will set it, not the hue alone.
→ *Decision recorded:* desired feeling + the treatment lever (tint/saturation/pairing) that will produce it.

**Layer 3 — CULTURAL.**
Meaning shifts by culture. White = weddings/purity in the West, mourning/funerals in parts of Asia. Green = sustainability, or finance, or religious meaning depending on audience. Critical the moment reach goes global.
→ *Decision recorded:* any hue that carries a market-specific meaning for this audience, and whether that helps or must be avoided.

**Layer 4 — COMPETITIVE.**
Industries form color monopolies — banks love blue, luxury loves black + gold, eco loves green, tech leans blue/purple.

> *"Most industries gradually develop color monopolies... Do you fit into this, or do you want to stand out?"* — Satori

Map the category's incumbent palette here (name the 3–5 colors the audience already associates with the category). Do not decide yet — Step 3 makes the call. This is knowledge; knowledge is the power to choose.
→ *Decision recorded:* the category's color monopoly, as a named palette.

**Layer 5 — STRATEGIC (the top layer).**
Stop asking "what looks good?" and ask what the color is *trying to achieve*.

> *"professional designers ask what this color is trying to achieve."* — Satori

Restate the Step 1 goal as a color mandate: *attract attention* → maximize contrast + saturation on the accent; *build trust* → restraint, category-adjacency, tuned neutrals; *differentiate* → deliberate distance from the Layer 4 monopoly.
→ *Decision recorded:* one sentence — "this palette exists to [achieve X] by [mechanism]."

### Step 3: Make the Fit-In vs Stand-Out Call (explicit)

Using the Layer 4 monopoly and the Layer 5 mandate, make the call *out loud* — never by default:

- **FIT IN** — adopt the category's color family → instant category trust, "reads legitimate on sight." Cost: risk of disappearing into a sea of identical competitors.
- **STAND OUT** — break from the monopoly → differentiation, memorability. Cost: forfeits borrowed category trust; must earn it through the rest of the system.

Record the call and tie it to the strategic goal: *"We [fit in / stand out] because the goal is [X], and the category monopoly is [palette]."* A trust-goal brand in a chaotic category often fits in; an attention-goal brand in a monochrome category almost always stands out.

### Step 4: Assign the 4 Roles + Output Hex

Every color now gets a defined job. This is the real secret, not the swatches:

> *"every color has a clearly defined job... And that's, more than anything else, is the real secret behind color in modern design."* — Satori

Assign **exactly four roles**. Output an actual hex for each, plus a one-sentence job. No orphan colors (rent test, GP-01).

1. **PRIMARY — the hero.** Carries the brand/product/concept identity; where the Emotional + Cultural + Competitive + Strategic decisions become visible. *Derive it:* it is the Step 2–3 decision made into a hue + treatment.
2. **SECONDARY — the support.** Adds flexibility, depth, and variation without stealing the spotlight. *Derive it:* an analogous neighbor or a shade/tint of primary; must never out-shout primary.
3. **ACCENT — where attention lives.** CTAs, focal points, the one thing you want acted on. Functional color matters most here — it guides behavior and creates hierarchy. *Derive it:* high-contrast against primary and against the neutral ground; often complementary or a deliberately hot signal color. Use it *scarcely* — one zone, not everywhere.
4. **NEUTRAL — the most underrated.** Creates structure, breathing room, readability; lets primary + accent do their jobs. **Without neutrals, every color fights for attention and none wins.** *Derive it:* a near-white ground and a near-black ink, **tuned** to the palette's temperature — warm off-white for warm palettes, cool for cool. Never pure `#FFFFFF`/`#000000` (that's the AI-default tell — GP-11). Add one muted mid-gray for secondary text.

Output the four (plus the two neutral text values) as hex. Each line ends in its one-sentence job.

### Step 5: WCAG Contrast Pass (AA minimum) + Token Readiness

A beautiful palette that can't be read failed Layer 1. Prove every text/background pair before shipping.

- **Formula:** contrast ratio = (L_lighter + 0.05) / (L_darker + 0.05), where L is WCAG relative luminance.
- **AA thresholds:** **4.5:1** normal text · **3:1** large text (≥24px, or ≥18.66px bold) · **3:1** UI components & graphical objects. Target **AAA (7:1)** for body where you can.
- **Check every real pair:** body ink on neutral bg · off-white on primary (dark sections) · label on accent-fill (the CTA) · muted text on neutral bg · slate/secondary on neutral.
- **On a fail:** do **not** abandon the hue. Adjust *lightness* until it passes — same color logic as the "same red, different treatment" quote. Record the adjusted hex.
- **Guard the accent:** if the accent-as-text fails on the light ground (bright accents almost always do), lock it to fill/signal use only and forbid it as body text. Note this in the token comments so downstream builders don't misuse it.

### Step 6: Assemble the Strategic Palette

Compose the artifact: the 5-layer decision log, the fit-in/stand-out call, the 4 roles (hex + job), and the WCAG table. Format it as a DESIGN.md-ready tokens block (Step-by-step spec in Output Requirements).

## Content-Type Adaptations

| Content type | How the method shifts |
|---|---|
| **Poster / print** | Functional layer shrinks (no buttons); Strategic + Emotional dominate. **CMYK gamut check** — electric/neon accents often can't print; swap to nearest printable or specify a Pantone spot. Neutral "white" = the paper stock, not `#FFF`. Contrast still governs legibility at distance. |
| **Logo / identity** | Palette must survive **1-color / mono** (GP-10 memory hook). Test primary as a single-color mark; the accent is a *system* color, off-limits inside the mark. Cultural + Competitive layers weigh most — the category monopoly is strongest at the logo level. |
| **UI / product** | Functional layer is **priority #1** — status/state colors, focus rings, disabled states. WCAG AA is a **hard gate** (AAA for body). Accent = interactive/CTA only; neutrals carry ~80% of surface. Ship **full light + dark** token pairs, not one mode. |
| **Social / feed** | Competitive layer expands to "in-feed" — the palette must pop against platform chrome (white/black feed) and neighboring posts, not just the category. Accent does the stopping-power work; test at thumbnail. Fewer colors, higher contrast. |
| **Packaging** | Cultural layer is critical (global shelf) and Competitive means **shelf-adjacency** — stand out from the aisle-wall of same-color competitors. Material/finish (foil, matte, spot gloss) changes perceived color; specify **Pantone + finish**, not just hex. |
| **Ad creative** | Accent = the single attention magnet on the CTA; the strategic goal is usually *attract attention* → bias toward stand-out. Functional clarity of the CTA color **beats brand consistency** when they conflict. Test across placements (feed/story/banner) = transferability. |

## Output Requirements

The deliverable is a **Strategic Palette** with these parts, in this order:

1. **Inputs** — brand sentence · category · audience(+markets) · primary goal
2. **5-Layer Decision Log** — one recorded decision per layer (Functional → Emotional → Cultural → Competitive → Strategic), no layer skipped
3. **Fit-In / Stand-Out Call** — the explicit decision + one-line rationale tied to the goal
4. **The 4 Roles** — Primary / Secondary / Accent / Neutral, each with a **hex** and a **one-sentence job**
5. **WCAG Table** — every text/bg pair with its measured ratio and AA/AAA/FAIL verdict + fixes applied
6. **Token Block** — DESIGN.md / Tailwind-ready, with usage comments (including the accent-as-fill-only guard)

**Token block format:**

```markdown
## Color Tokens
--color-primary:    #16181D;  /* Primary  — carries the brand's [X] identity */
--color-secondary:  #3A4048;  /* Secondary — depth + section separation; never competes */
--color-accent:     #C6F04B;  /* Accent   — CTA + focal signal; FILL/UI only, not body text */
--color-bg:         #F5F3EE;  /* Neutral  — warm ground; breathing room + readability */
--color-text:       #16181D;  /* Body ink (= primary) */
--color-text-muted: #61666E;  /* Secondary text */
```

**Worked example (a performance-recovery brand for funded wellness brands — goal: differentiate + trust; STAND OUT from the sage-green "spa wellness" monopoly by going graphite performance-tech with an electric-lime output signal):**

| Role | Hex | Job |
|---|---|---|
| Primary | `#16181D` | Graphite that reads *performance*, not spa — anchors every surface |
| Secondary | `#3A4048` | Slate for section depth and dark-mode layering; supports, never shouts |
| Accent | `#C6F04B` | Electric lime = energy/output; owns the CTA and the one focal moment |
| Neutral (bg) | `#F5F3EE` | Warm off-white ground so the graphite doesn't read clinical |
| Neutral (muted) | `#61666E` | Secondary text / captions without competing with body ink |

| Pair | Ratio | Verdict |
|---|---|---|
| Primary text `#16181D` on bg `#F5F3EE` | 16.01:1 | AAA |
| Off-white `#F5F3EE` on primary `#16181D` (dark section) | 16.01:1 | AAA |
| Dark label `#16181D` on accent fill `#C6F04B` (CTA) | 13.50:1 | AAA |
| Slate `#3A4048` on bg `#F5F3EE` | 9.44:1 | AAA |
| Muted text `#61666E` on bg `#F5F3EE` | 5.21:1 | AA (normal) |
| Accent `#C6F04B` as **text** on bg `#F5F3EE` | 1.19:1 | **FAIL → fill-only, never body text** |

## Quality Gate

Guards against these `genius.md` anti-patterns:
- **#8 Aesthetic-first decisions** — colors chosen before concept. The whole "what looks good?" trap; the Layer 5 mandate is the antidote.
- **#7 Loud-by-default** — accent everywhere means nothing leads; underused neutrals. The 4-role system caps the accent to attention duty.
- **#1 Decoration without reason** — a color with no assigned role is chaff; the rent test evicts it.
- **#6 More-equals-better layering** — palette sprawl. Four roles, no more.

**Pass criteria (all must hold):**
- [ ] All four inputs locked (brand · category · audience · goal) **before** any hex was chosen
- [ ] A decision recorded at **each** of the 5 layers — Functional was asked *first*
- [ ] Fit-in vs stand-out made **explicitly** and tied to the strategic goal (never defaulted)
- [ ] Exactly **4 roles**, each with a hex + a one-sentence job (no color without a job)
- [ ] Neutrals are **tuned**, not pure `#000`/`#FFF` (GP-11)
- [ ] Every text/bg pair meets **WCAG AA** (4.5 normal / 3.0 large); failures fixed by adjusting *lightness*, not abandoning the hue
- [ ] Accent restricted to attention/fill roles; not used as text where it fails contrast
- [ ] **No fixed-meaning claim** anywhere in the rationale ("red = danger" reasoning is a fail)

Any unchecked box → revise before delivery.

## Related Workflows

- **`/satori-why-before-what`** (04) — run the rent test on each color; every hex must pay rent or get evicted
- **`/satori-design-md-grid`** (13) — the natural downstream: drop these tokens into a full DESIGN.md composition + grid spec
- **`/satori-brand-audit`** (14) — color is one touchpoint layer in the full brand audit; use this to *fix* the color findings it surfaces
- **`/satori-predictive-empathy`** (07) — deepen the Emotional layer; design the palette for the viewer's *next* emotion, not the impact color
- **`/satori-anti-ai-slop`** (09) — imperfection at the palette level (off-true neutrals, non-mechanical tints)
- **`/satori-lift-audit`** (01) — the Accent is the Leverage/attention color; functional color drives the "L" and the CTA
- **`/satori-poster-think`** (12) → `fantastic-posters` — hand this locked palette down as the color direction before any generation

## Source Grounding

This workflow is anchored to Satori's color teaching, verbatim (full set in `references/source-quotes.md`; the deep companion is `references/color-system.md`):

> *"one of the biggest myths in graphic design is that colors have fixed meanings. They don't."*

> *"context is super super important when considering the meaning of color."*

> *"I could take the exact same shade of red and make it feel premium, make it feel loud, or make it feel playful. And that's without ever changing the color itself."*

> *"Most industries gradually develop color monopolies... Do you fit into this, or do you want to stand out?"*

> *"professional designers ask what this color is trying to achieve."*

> *"every color has a clearly defined job... And that's, more than anything else, is the real secret behind color in modern design."*

Every step above forces a decision before a swatch — the Satori principle that **design is decision-making before it is expression**, applied to the one layer this skill had left open.
