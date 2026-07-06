# Strategic Color System — 5 Layers × 4 Roles

The decision model behind `/satori-color` (WF-17): color is not chosen, it is *argued for*. This reference expands the 5 strategic layers and the 4 functional roles into a working decision procedure, then walks a full palette build end-to-end with real hex codes and WCAG AA verification. Source: Satori Graphics' **"Color full guide"** video (2026). Companion to genius.md GP-15.

---

## THE CORE MYTH

Every amateur color decision starts from a lookup table — red means danger, blue means trust, green means growth. That table is the myth.

> *"One of the biggest myths in graphic design is that colors have fixed meanings. They don't."*

A color has no meaning until **context** assigns it one. Context = the four things sitting next to the color: **typography, imagery, industry, and audience**. Change any of them and the same hue flips register.

Take one red — say a deep, saturated crimson:
- Set in a thin serif, on a watch dial, in the jewellery category → **premium, heritage, restraint**.
- Set in a heavy italic, on a livery, in motorsport → **loud, fast, adrenaline** (F1).
- Set in a bold sans, as a full-bleed field, in entertainment tech → **streaming, appetite, play** (Netflix).

Same wavelength. Three unrelated meanings. The red did not change — the *context* did all the work. This is why "what color should I use?" is the wrong question. The right question is: **what is this color supposed to achieve, for whom, against what, and next to what?** That question is what the five layers force you to answer, in order.

**Practitioner note**: The myth cuts both ways. Rejecting fixed meanings is not license for arbitrary color — cultural and functional constraints (Layers 1 and 3) are real and non-negotiable. "No fixed meaning" means the *emotional* read is contextual, not that anything goes.

---

## THE 5 LAYERS

Walk them **in order, 1 → 5**. Each layer is a gate: you do not proceed to the next until the current one is answered. Skipping to Layer 2 (emotion) before Layer 1 (function) is how you get a beautiful palette nobody can operate. Skipping Layer 4 (competition) is how you disappear.

| # | Layer | The key question | Failure mode |
|---|---|---|---|
| 1 | **Functional** | Can people *understand and operate* what they're looking at? | A gorgeous palette that fails comprehension |
| 2 | **Emotional** | What does it make them *feel* — for *this* audience? | Treating "blue = trust" as a rule, not a guide |
| 3 | **Cultural** | What does it *mean* to this audience's culture? | Ignoring cultural context on a global audience |
| 4 | **Competitive** | Fit the category (instant trust) or break it (stand out)? | Vanishing into a sea of identical competitors |
| 5 | **Strategic** | What is this color trying to *achieve*? | Decorating instead of deciding |

### Layer 1 — Functional

**Definition**: Color as an operating system for comprehension. Before a palette is allowed to be beautiful, it has to *work*: buttons must read as pressable, links as clickable, error states as errors, disabled as disabled, primary action as distinct from secondary. This is the WCAG-and-affordance layer.

**The key question**: *Can a stranger understand what they're looking at and know what to do next — with the sound off and no explanation?*

**Concrete examples**:
- A checkout where "Pay" and "Cancel" are the same weight and hue → users hesitate; conversion drops. Function failed before emotion got a vote.
- Status color that ships as green-success / red-error only → invisible to red-green colorblind users (~8% of men). Add an icon or a value shift, not just a hue shift.
- A dark-mode toggle where "on" and "off" differ by a 1.2:1 luminance step → nobody can tell the state. Function demands a value gap, not just a color swap.

**Common failure mode**: Designing the mood board first and retrofitting function. The palette looks incredible in the pitch and collapses the moment it has to render a form, a table, and three button states.

### Layer 2 — Emotional

**Definition**: The felt temperature of the palette — warm reads as energetic/appetite/urgency, cool as calm/clinical/control — modulated by saturation (loud vs quiet) and value contrast (dramatic vs gentle). But the emotion is *contextual*, never fixed.

**The key question**: *What should the viewer feel in the first half-second — and does this audience read that hue the same way I do?*

**Concrete examples**:
- Blue is the default "trust" reach — but the same blue is **cold, corporate, clinical, and boring** in the wrong context. A meditation app and a tax-audit firm cannot use blue for the same reason.
- High saturation + high value contrast = energy and youth (sports drink). The same hues at low saturation + low contrast = premium and calm (skincare). The *relationship between the colors* carries more emotion than the hues themselves.
- Warm amber signals earned warmth and appetite in food/wellness; the identical amber signals *caution* on machinery. Industry (Layer overlap with 3/4) rewrites the feeling.

**Common failure mode**: Reaching for the emotion cliché — blue=trust, green=health, black=luxury — and treating it as a rule instead of a starting hypothesis to pressure-test against the actual audience.

### Layer 3 — Cultural

**Definition**: The meaning a color carries inside a specific culture, independent of your intent. This layer is a hard constraint, not a preference — get it wrong on a global audience and the design is *offensive*, not merely off-brand.

**The key question**: *What does this color already mean to the specific people who will see it — before I add any of my own meaning?*

**The cultural read table** (verify against the *actual* target market, never assume):

| Color | One culture / context | Another culture / context |
|---|---|---|
| **White** | West → weddings, purity, cleanliness, space | Parts of Asia → mourning, death, funerals |
| **Green** | Sustainability, nature, "go", health, money/finance | Strong religious associations (e.g. Islam); in finance also gains/growth |
| **Blue** | Trust, stability, calm, corporate reliability | Also cold, clinical, distant, boring — and in some contexts, mourning |
| **Red** | Danger, passion, sale/urgency (West) | Luck, prosperity, celebration (much of East Asia) |

**Concrete examples**:
- A wedding brand launching a white-heavy identity across the US and East Asian markets: pure in one, funereal in the other. The fix is usually *proportion and pairing* (white as accent-of-a-warm-neutral, not the dominant field) or market-specific variants.
- A fintech using green for "growth" in a market where green reads primarily religious → the finance signal never lands.

**Common failure mode**: Designing for your own cultural default and assuming it's universal. On a single-market brand this layer can be quick; on a global one it is where palettes get recalled.

### Layer 4 — Competitive

**Definition**: Color positioned *against the category*. Every category has an incumbent color language (fintech = blue, wellness = sage/beige, luxury = black/gold). You get exactly one decision here: **fit in** to borrow the category's instant trust, or **break out** to be seen. This is the layer with its own decision tree — see below.

**The key question**: *When my color sits in the feed / on the shelf / in the search results next to my competitors — do I want to belong, or be the one that isn't like the others?*

**Concrete examples**:
- A new bank that goes blue: instant "this is a legitimate bank" recognition — at the cost of blending into every other bank.
- A new bank that goes coral: impossible to ignore in a blue sea — at the risk of reading as "not a serious bank" if the rest of the system doesn't earn the break.
- A wellness brand in a category of sage-green and oat-beige: the fifteenth sage brand is invisible; a deep-forest-and-amber brand is *legible as different* on the same shelf.

**Common failure mode**: Choosing the category color by reflex ("everyone in wellness uses sage, so we'll use sage") and disappearing — or breaking the category with no strategic reason and forfeiting the free trust.

### Layer 5 — Strategic

**Definition**: The layer that names the *job of the whole palette* — the outcome color is being deployed to produce. Attract attention? Manufacture trust? Signal differentiation? Justify a premium? This is where the previous four layers resolve into a single decision, and it is the difference between deciding and decorating.

**The key question**: *What is this color system trying to achieve for the business — and would a different palette achieve it better?*

**Concrete examples**:
- Goal = premium justification → restraint, low saturation, generous neutral, one disciplined accent. A loud palette actively fights a premium price.
- Goal = feed-stopping attention for a low-cost impulse product → high saturation, high contrast, an accent that punches. Restraint would be a strategic error here.
- Goal = category trust for a regulated service → deliberate fit-in on the base, tiny break on the accent to stay ownable.

**Common failure mode**: Building a palette that is internally beautiful but not pointed at any business outcome — "it looks cool" instead of "it does X." This is the color equivalent of the Rent Test (GP-01) failure: every color has to pay rent by serving the strategy.

---

## THE 4 ROLES

The 5 layers decide *what the colors mean*. The 4 roles decide *what each color does*. This is the operational half of the system — and per Satori, the real separator between amateur and professional palettes.

> *"Every color has a clearly defined job… that's, more than anything else, the real secret behind color in modern design."*

| Role | Its job | Where it lives | Where the layers show |
|---|---|---|---|
| **Primary** | Carries the identity; the hero color you'd name the brand by | Logo, headers, brand fields, key surfaces | This is where Layers 2–5 become visible |
| **Secondary** | Supports the primary; adds depth and flexibility without stealing focus | Section backgrounds, supporting graphics, secondary UI | Extends the emotional range |
| **Accent** | Where attention *goes* — the eye's destination | CTAs, focal points, highlights, links, key data | Layer 1 (function) matters most here |
| **Neutral** | Structure, breathing room, readability — the ground everything stands on | Text, backgrounds, borders, dividers, whitespace | Makes every other color legible |

**A working proportion** (practitioner heuristic, not Satori-attributed — treat as a default, not a law): roughly **60% neutral / 25% primary / 10% secondary / 5% accent**. The accent is the *smallest* footprint precisely because it is the loudest — scarcity is what makes it read as the destination.

### Why neutrals are the most underrated

Everyone fights over the primary and the accent. The professionals know the palette lives or dies on the neutrals. Neutrals are the whitespace, the paper, the ink, the dividers — the color that lets *every other color mean something*.

> *"Without them, every color ends up fighting for attention and eventually none of them would win."*

Without a strong neutral field, three saturated colors all shout at once, contrast collapses, and the accent loses its power to point — because everything is already loud, nothing is loud. The neutral is what creates the *quiet* against which the accent becomes a signal. A palette with a considered warm off-white and a considered near-black ink, plus one primary, will out-perform a palette of four "brand colors" and no neutral discipline every time.

**Neutrals are rarely pure grey.** A warm off-white (`#F4F1EA`) reads premium and human; a cold `#FFFFFF` reads default and clinical. A green-tinted near-black (`#141A16`) unifies a green-primary system; a pure `#000000` reads harsh and detaches from the brand. Tint your neutrals toward the primary — that's the move that makes the whole system feel authored rather than assembled.

---

## FIT-IN vs STAND-OUT (the competitive decision tree)

This is Layer 4 made operational. Run it before locking the primary and accent.

```
START: What is the category's incumbent color language?
        (Audit 5–8 direct competitors. Name the dominant hue + saturation.)
  │
  ├─ Is the brand a NEW ENTRANT in a TRUST-CRITICAL category?
  │  (finance, health, legal, security, childcare)
  │        │
  │        ├─ YES → Lean FIT-IN on the BASE (primary + neutral adopt the
  │        │         category signal for instant legitimacy),
  │        │         then BREAK on the ACCENT to stay ownable.
  │        │         → "Recognizably legitimate, distinctly ours."
  │        │
  │        └─ NO  → continue ↓
  │
  ├─ Is the category VISUALLY HOMOGENEOUS?
  │  (a "sea of identical competition" — same hue everywhere)
  │        │
  │        ├─ YES → Lean STAND-OUT. Fitting in = invisible.
  │        │         Break the dominant hue OR break its saturation/value.
  │        │         (You can keep the category HUE but crush the saturation
  │        │          the whole category shares — that alone reads as different.)
  │        │
  │        └─ NO  → the category already tolerates variety;
  │                  choose on Layer 5 (strategic goal), not on differentiation.
  │
  └─ Does the brand's PRICE POSITION contradict the category color?
     (premium brand in a category coded cheap/loud, or vice-versa)
           │
           ├─ YES → BREAK, but toward the price signal, not toward novelty.
           │         (Premium-in-a-loud-category → restraint + one deep accent.)
           │
           └─ NO  → default to FIT-IN-BASE / BREAK-ACCENT — the safest
                     high-trust, still-ownable posture.
```

**The two failure poles**:
- **Over-fit** → you inherit trust *and* invisibility. The fifteenth blue fintech nobody remembers.
- **Over-break** → you inherit attention *and* illegitimacy. The coral bank that reads as a toy.

**The reliable default** for most briefs: **fit-in on the base, break on the accent.** Adopt enough of the category to be instantly understood; own one deliberate move (usually the accent) so you're not interchangeable.

---

## WORKED EXAMPLE — Premium wellness/performance brand

**Brief (one sentence)**: *A premium recovery-and-performance brand for high-earning professionals who train seriously and expect the calm, expensive restraint of a luxury wellness label — not the neon of a sports brand.*

Walk the five layers.

**Layer 1 — Functional.** The system has to render: long-form editorial (protocols, science), a store (product cards, "Add to cart"), data (recovery scores, trends), and dark + light surfaces. Requirement: one unmistakable action color, body text at AA-normal (≥4.5:1) on both a light and a dark ground, and status/data colors that survive greyscale. → *Function demands a high-contrast neutral pair + one accent reserved for action.*

**Layer 2 — Emotional.** Target feeling: **calm authority + earned vitality.** Not clinical-cold (rules out a blue base), not loud-athletic (rules out electric lime/orange at full saturation). Warmth has to be present but *disciplined*. → *Deep, low-saturation base; a single warm accent for the vitality note.*

**Layer 3 — Cultural.** Primary market: US/UK/EU premium consumers. Green reads health/nature/vitality here with no funerary or dominant-religious conflict in this market. Warm amber reads appetite/warmth/gold-adjacent premium. No white-as-mourning risk (white is a minor neutral, not the field). → *Green base and amber accent are culturally clean for this audience.* (Flag for a future APAC launch: re-audit the white and green proportions.)

**Layer 4 — Competitive (run the tree).** Category audit: wellness is a **sea of sage-green and oat-beige**; performance is black + electric neon. This brand sits between them and the category is visually homogeneous on the wellness side. Decision: **keep the category HUE (green) — instant "health" recognition — but break its SATURATION and VALUE.** Everyone else is soft sage; we go **deep forest**. That single move reads as different on the same shelf while keeping the free trust of "this is wellness." Then **break on the accent**: instead of the expected brighter-green or teal, use **warm amber** — the earned-vitality note that neither the sage-wellness nor the neon-performance camp owns. → *Fit-in on hue, stand-out on saturation + accent.*

**Layer 5 — Strategic.** Job of the palette: **justify a premium price and signal seriousness without shouting.** That mandates restraint (low saturation, dominant neutral, a *single* small accent). A second bright color would break the premium read. → *Four roles, one accent, neutrals do the heavy lifting.*

### The 4 roles, resolved (with verified WCAG AA)

| Role | Name | Hex | Job in this system |
|---|---|---|---|
| **Primary** | Pine | `#1F3D2F` | Deep-forest identity field — the "wellness, but premium" fit-in-hue / break-saturation move |
| **Secondary** | Stone | `#7C7263` | Warm taupe support for section grounds and secondary UI; adds depth without a second loud hue |
| **Accent** | Amber | `#C6822E` | The single attention color — CTAs, focal data, highlights. Deliberately scarce |
| **Accent (on-light)** | Amber-deep | `#9A5F1C` | Darkened accent variant for accent *text/icons on the light ground* (the base Amber fails AA there) |
| **Neutral — dark** | Ink | `#141A16` | Green-tinted near-black; body text on light, and the dark-mode field |
| **Neutral — light** | Paper | `#F4F1EA` | Warm off-white; the dominant field and the light-mode text-on-dark color |

**WCAG AA verification** (computed, ratio : threshold). AA-normal = 4.5:1, AA-large = 3:1 (≥18pt or 14pt bold), UI/graphical objects = 3:1.

| Foreground | Background | Ratio | Verdict | Use |
|---|---|---|---|---|
| Ink `#141A16` | Paper `#F4F1EA` | **15.66:1** | PASS (normal) | Body text, light mode |
| Pine `#1F3D2F` | Paper `#F4F1EA` | **10.54:1** | PASS (normal) | Headings on light |
| Paper `#F4F1EA` | Pine `#1F3D2F` | **10.54:1** | PASS (normal) | Reversed text on brand field |
| Paper `#F4F1EA` | Ink `#141A16` | **15.66:1** | PASS (normal) | Body text, dark mode |
| Ink `#141A16` | Amber `#C6822E` | **5.58:1** | PASS (normal) | **CTA: ink label on amber fill** |
| Amber `#C6822E` | Ink `#141A16` | **5.58:1** | PASS (normal) | Accent text/icons on dark |
| Amber `#C6822E` | Pine `#1F3D2F` | **3.75:1** | PASS (large only) | Accent *large* text on primary |
| Amber-deep `#9A5F1C` | Paper `#F4F1EA` | **4.62:1** | PASS (normal) | Accent text/icons on light |
| Stone `#7C7263` | Paper `#F4F1EA` | **4.19:1** | PASS (large only) | Secondary/caption text — large only |
| Amber `#C6822E` | Paper `#F4F1EA` | **2.81:1** | **FAIL** | Guardrail: never amber-as-text on paper |

**The two honest guardrails this surfaces** (this is why you verify instead of eyeballing):
1. **Base Amber must never be a text or thin-line color on Paper (2.81:1).** On the light ground, the accent is only allowed as a *fill* with Ink text on top (5.58:1), or swapped for **Amber-deep** when it must be text/icon (4.62:1). The accent's usage envelope is constrained — that constraint is the system, not a flaw.
2. **Stone is large-text-only.** Fine for section labels and captions at ≥18pt; do not use it for body copy on Paper.

### DESIGN.md-ready tokens

```json
{
  "$meta": {
    "brand": "premium-wellness-performance",
    "brief": "Premium recovery/performance for serious professionals — luxury-wellness restraint, not sports-brand neon.",
    "competitive_call": "fit-in on hue (green=health), break on saturation (deep forest, not sage) + accent (amber)",
    "wcag": "AA verified — see usage notes; ratios computed against paired grounds"
  },
  "color": {
    "primary":        { "value": "#1F3D2F", "name": "Pine",       "role": "primary",   "usage": "identity field, headings-on-light" },
    "secondary":      { "value": "#7C7263", "name": "Stone",      "role": "secondary", "usage": "supporting grounds, secondary UI; LARGE text only on Paper" },
    "accent":         { "value": "#C6822E", "name": "Amber",      "role": "accent",    "usage": "CTA fill (Ink label), accents on dark; NEVER text on Paper" },
    "accent-onlight": { "value": "#9A5F1C", "name": "Amber-deep", "role": "accent",    "usage": "accent text/icons on Paper (AA-normal)" },
    "neutral-dark":   { "value": "#141A16", "name": "Ink",        "role": "neutral",   "usage": "body text on light; dark-mode field" },
    "neutral-light":  { "value": "#F4F1EA", "name": "Paper",      "role": "neutral",   "usage": "dominant field; text on dark" }
  },
  "semantic": {
    "bg":             "{color.neutral-light}",
    "bg-inverse":     "{color.neutral-dark}",
    "text":           "{color.neutral-dark}",
    "text-inverse":   "{color.neutral-light}",
    "heading":        "{color.primary}",
    "action":         "{color.accent}",
    "action-label":   "{color.neutral-dark}",
    "link":           "{color.accent-onlight}",
    "muted":          "{color.secondary}"
  }
}
```

Hand this block to `skills/design-md/` for codification into the full token spec — Satori's `/satori-color` *decides* the palette (the 5-layer argument, the competitive call); DESIGN.md *records* it as the system of record. Keep the layer reasoning in `$meta` so the *why* travels with the tokens and survives the next designer.

---

## Cross-links

- **`/satori-color` (WF-17, `workflows/17-color.md`)** — the workflow this reference operationalizes. Run it to *produce* a palette; return here for the decision criteria, the competitive tree, and the WCAG discipline.
- **`skills/design-md/`** — token codification. The `/satori-color` output block feeds design-md, which owns the canonical token spec, aliasing, and export. Satori decides; design-md records.
- **`skills/kittl-graphic-design/`** — type. Color is only one of the four context variables that assign meaning (Layer 1 of the myth: typography, imagery, industry, audience). Lock the palette here, then set it in the *right* type via Kittl — the same amber reads premium in a thin serif and loud in a heavy italic.
- **genius.md GP-15** — the summary framing this reference expands.
- **`references/source-quotes.md`** — verbatim Satori grounding material for the broader skill.

---

## When this system doesn't apply

- **A single decorative graphic with no brand life** — you don't need 5 layers to color one poster; run the emotional layer and go.
- **A locked brand with existing tokens** — don't re-derive; *audit* the existing palette against Layers 1 and 4 and the WCAG table, and only touch what fails.
- **Pure data visualization palettes** — categorical/sequential/diverging color has its own perceptual rules (ordering, colorblind-safety, equal-luminance steps) that sit *above* Layer 1; use a dataviz-specific palette method, then borrow this system only for the brand-accent overlay.
