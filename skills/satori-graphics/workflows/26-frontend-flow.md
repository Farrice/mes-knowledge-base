---
description: The front-end bridge — compile the three-flow spine, contrast stack, and temporal beats into page-level section rhythm, behavioral contrast directives, and DESIGN.md-ready notes, then hand off to the build tool
---

# 26 — Frontend Flow

> **/satori-frontend-flow** — Layout thinking compiled for interfaces. AI front-end defaults to evenly-weighted sections, uniform emphasis, and no rhythm — this workflow is the antidote: one journey per page, contrast as choice architecture, and the punch → linger → release beat structure almost nobody engineers.

> *"Something like 99% of designers don't consider this temporal flow… be it a poster, marketing brochure, website, whatever it is."* — Satori

The Apple product-page pattern, made deployable: opening hero hits hard and fast (punch) → clean technical detail blocks slow the eye (linger) → vast white space around a single product (release). A page is a temporal composition, not a stack of sections.

## Pre-Flight Gate

**Use this when**:
- Building or briefing any web surface: landing page, product page, portfolio, dashboard shell, artifact page
- An existing page "has everything" but converts poorly — the CTA doesn't win, nothing steers
- Prepping a `frontend-design` / `/product-build` / artifact run and you want non-generic structure BEFORE code
- Auditing AI-generated front-end that is symmetrical, evenly spaced, and dead (the template tell)

**Do NOT use this when**:
- The aesthetic direction/tone itself is undecided — run `frontend-design`'s design-thinking or `/satori-design-think` first for the bold direction; this workflow structures the journey inside it
- Token codification is the task — `/design-md-*` (Jack Roberts); this workflow *feeds* DESIGN.md notes, doesn't write the spec
- Pure component styling with no page journey (a button variant needs no spine)
- Print/poster — use workflows 21/22/24 directly

## Skill Acquisition

```
Load: skills/satori-graphics/genius.md
  ├─ GP-18 (Three-Flow Rule — the page's journey spine)
  ├─ GP-20 (Contrast Stack — behavioral contrast, HK-13)
  ├─ GP-04 L6 (Temporal Flow — the beat structure)
  └─ HK-14 (Temporal flow is the 99% edge)
Load: skills/satori-graphics/references/layout-flow-hierarchy.md
Load: skills/satori-graphics/references/contrast-stack.md    # Front-End Application section
```

## Execution

### Step 1 — The Page Spine (three-flow at page scale)

Commit the page's single primary journey:
- **Hook** — the hero moment: what stops the scroll/land in <1 sec (headline, product visual, or both)
- **Secondary Detail** — the middle stops that carry them deeper: proof, features, story blocks
- **Finisher** — the ONE action the page exists for (primary CTA). Write it first, Step-1-of-21 style: "if they do nothing else, they ___"

Rule: one primary journey per page. Secondary CTAs, nav, footers are micro-routes (movement L3) — they loop and reconnect; they never compete. Two primary CTAs = two journeys = neither wins.

### Step 2 — Beat Map (temporal flow across the scroll)

Assign every section a beat — the page reads like music:

| Beat | Section behavior | Craft levers |
|---|---|---|
| **PUNCH** | Hero: hits hard and fast | Full-bleed visual or dominant type; maximum contrast; minimal copy |
| **LINGER** | Detail blocks: the eye slows and scans | Clean grid blocks, feature rows, proof; moderate density; readable rhythm |
| **RELEASE** | Breathing zones: the pause that gives rhythm resolution | Vast white space around a single element (the Apple move); no competing content |

Sequence discipline: punch → linger → release, repeatable as a phrase (a long page = multiple phrases), always **ending on release into the finisher** — the CTA sits in calm space, not in clutter. Skipping release = "rhythm without resolution = exhausting" (L6 mistake). Equal-weight sections = no rhythm = the AI-template tell.

**Decision forced**: the beat map — `SECTION → BEAT → one-line behavior`.

### Step 3 — Behavioral Contrast Assignment (HK-13)

Contrast on interfaces is choice architecture. Assign deliberately:

| Zone | Contrast play |
|---|---|
| **Primary CTA** | The color-contrast lever — the one saturated accent on its ground ("how social media UI creates an addictive response"); size contrast vs. secondary actions (the larger option gets clicked) |
| **Option steering** | Preferred plan/choice visibly larger + higher contrast; de-emphasized options quieter — steering by contrast, not persuasion copy |
| **Cards/features** | Double-whammy: card pops off the ground AND its internal content contrast-pairs |
| **Urgency/status** | The for-sale-sign red family — reserved exclusively for urgency so it never cries wolf |
| **Quiet zones** | Deliberately flat regions (nav, footer, legal) that buy contrast budget for the zones that steer |

Stack check: ≥3 deliberate forms page-wide (color, size, typography minimum; texture/style/psychology as the brand tolerates), zonal not global, every form serving a spine anchor.

### Step 4 — Directional Wiring (screen-scale gaze path)

- Hero subjects (faces, products, illustrations) point INTO the content/CTA, never off-screen
- Section shapes/diagonals lead downward into the next beat; angles that point off-page leak attention
- Scroll cues are shapes, not literal arrows, on premium surfaces
- Light gradients fall toward the next section's entry

### Step 5 — Compile the Handoff

Produce the build-ready brief:
1. **Section order + beat map** (Step 2 table)
2. **Contrast directives per zone** (Step 3, specific: "CTA = the page's only saturated orange, 1.4× secondary-button scale")
3. **Directional notes** (Step 4, incl. image-selection requirements: gaze/angle direction)
4. **DESIGN.md-ready notes** — spacing rhythm (release-zone min-heights), emphasis scale ratios, the reserved-urgency color, contrast tokens — for `/design-md-*` codification
5. **Thumbnail test, screen edition** — zoom the full-page comp to ~10%: the punch/linger/release rhythm should be visible as light/dark/dense/empty banding; uniform banding = no rhythm, rework beats

Then hand off: `frontend-design` skill or `/product-build` executes the code; `/satori-contrast-audit` re-audits the built page; `/satori-perception-gap` proves the journey transmits.

Execution prompt: `references/prompts-v2/frontend-flow-brief.md`

## Content-Type Adaptations

| Surface | Spine note | Beat note |
|---|---|---|
| **Landing page** | Finisher = the one conversion action | Classic single phrase: punch → linger(×2–3) → release → CTA |
| **Product page** | Hook = product visual (the hero IS the product) | The Apple pattern verbatim |
| **Portfolio/personal** | Hook = identity moment; finisher = contact/booking | Releases showcase single works — one piece per breath |
| **Dashboard/app shell** | Hook = primary metric/action; journey = task path | Beats compress: punch (status) → linger (data); release = white space between card groups |
| **Artifact/report page** | Hook = the headline finding | Every finding block gets its own mini-phrase; end on release + next-step |
| **Email** | One phrase total | Punch (headline) → linger (3 lines max) → release → button |

## Output Requirements

A **Frontend Flow Brief** containing: page spine (`HOOK → SECONDARY → FINISHER` with the finisher-first line), the beat map, behavioral-contrast directives per zone (specific values/ratios where possible), directional notes with image requirements, DESIGN.md-ready notes, and the zoomed-out rhythm verdict. Executable by a developer or generation tool without re-asking; codifiable by Jack Roberts without re-deriving.

## Quality Gate

Guards anti-patterns **#17 uncommitted journey**, **#18 flat emphasis**, **#7 loud-by-default**, plus the frontend-design skill's generic-AI-aesthetic ban.

- [ ] ONE primary journey; secondary actions demoted to micro-routes
- [ ] Finisher (primary action) committed before the hook
- [ ] Every section carries a beat; no equal-weight section runs; at least one true RELEASE zone
- [ ] Rhythm ends on release into the CTA (the action sits in calm)
- [ ] ≥3 deliberate contrast forms, zonal; urgency color reserved; option steering explicit
- [ ] No hero subject pointing off-screen
- [ ] 10%-zoom banding shows the rhythm
- [ ] DESIGN.md notes present (spacing rhythm, scale ratios, reserved colors)

## Related Workflows

- **`/satori-design-think`** (20) — upstream for full concept-first pipeline; frontend-flow slots in as the layout stage
- **`frontend-design` skill / `/product-build`** — downstream executors of this brief
- **`/design-md-synthesize`** (Jack Roberts) — codifies the DESIGN.md notes into tokens
- **`/satori-contrast-audit`** (23) — re-audit the built page
- **`/satori-perception-gap`** (18) — post-build: does the journey transmit on a dimmed phone at night?
- **`/satori-three-flow`** (21) / **`/satori-contrast-stack`** (22) — the component plays this compiles
