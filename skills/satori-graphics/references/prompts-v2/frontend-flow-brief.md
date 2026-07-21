---
name: "Satori Graphics — Frontend Flow Brief"
source_prompt: born-v2
skill: satori-graphics
standard: structure-pure-v2
---

## Role & Activation

You are compiling layout thinking into a **build-ready front-end brief**: one page journey (three-flow spine at page scale), a temporal beat map (punch → linger → release — the Apple product-page pattern), behavioral contrast (contrast as choice architecture), and directional wiring — the antidote to AI front-end's evenly-weighted, rhythm-less sections.

> "Movement isn't just about where the eye goes. It's about when the eye goes there and how long for. This is called temporal flow." — Satori
> "Something like 99% of designers don't consider this temporal flow… be it a poster, marketing brochure, website, whatever it is." — Satori

## Input Required

- **[PAGE + PURPOSE]** — landing / product / portfolio / dashboard / artifact / email, and the one action the page exists for
- **[SECTIONS/CONTENT]** — the content blocks on the table
- **[AESTHETIC DIRECTION]** — the committed tone (from frontend-design thinking or /satori-design-think); this brief structures the journey inside it
- **[BRAND TOKENS]** — palette/type constraints, if any
- **[AUDIENCE + ARRIVAL STATE]** — who lands and in what psychological state

## Execution Protocol

### Step 1 — Page Spine
Finisher first: "if they do nothing else, they ___" (the primary CTA). Then Hook (the <1-sec hero moment) and Secondary (the middle stops: proof, features, story). ONE primary journey; secondary CTAs/nav/footer are micro-routes that loop and reconnect, never compete. Two primary CTAs = neither wins.

### Step 2 — Beat Map
Assign every section a beat: **PUNCH** (hero: full-bleed visual or dominant type, max contrast, minimal copy) · **LINGER** (detail blocks: clean grid, proof, readable rhythm) · **RELEASE** (breathing zone: vast white space around a single element). Sequence punch → linger → release as repeatable phrases, always **ending on release into the finisher** — the CTA sits in calm, not clutter. Skipped release = exhausting; equal-weight sections = the AI-template tell.

### Step 3 — Behavioral Contrast (choice architecture)
Primary CTA = the page's one saturated accent + size contrast over secondary actions (the larger option gets clicked). Option steering = preferred choice larger/louder by design. Cards = double-whammy (pop off the ground + internal contrast-pairing). Urgency = a reserved red-family used ONLY for urgency. Quiet zones (nav/footer/legal) deliberately flat to fund the zones that steer. Stack check: ≥3 deliberate forms page-wide, zonal, each serving a spine anchor.

### Step 4 — Directional Wiring
Hero subjects point INTO content/CTA, never off-screen. Section shapes/diagonals lead downward into the next beat. Scroll cues as shapes, not literal arrows, on premium surfaces. Light gradients fall toward the next section's entry. Include image-selection requirements (gaze/angle direction).

### Step 5 — Compile + Verify
DESIGN.md-ready notes: release-zone min-heights (spacing rhythm), emphasis scale ratios, the reserved urgency color, contrast tokens. Then the 10%-zoom test: the full-page comp should show punch/linger/release as visible dense/empty banding; uniform banding = no rhythm, rework beats.

## Output Contract

A Frontend Flow Brief: page spine (finisher-first line included), the section-by-section beat map, behavioral-contrast directives per zone (specific values/ratios), directional notes + image requirements, DESIGN.md-ready notes, and the zoom-rhythm verdict. Executable by a developer or generation tool without re-asking; codifiable into DESIGN.md without re-deriving.

## Output Skeleton

```markdown
# Frontend Flow Brief — [page name]

## Page Spine
If they do nothing else: [primary action]
HOOK: [hero moment] → SECONDARY: [middle stops] → FINISHER: [CTA + its calm zone]

## Beat Map
| Section | Beat | Behavior |
|---|---|---|
| [...] | PUNCH/LINGER/RELEASE | [...] |

## Behavioral Contrast
- Primary CTA: [accent + scale directive]
- Option steering: [...]
- Cards: [double-whammy spec]
- Urgency color (reserved): [...]
- Quiet zones: [...]

## Directional Wiring
- [subject/shape]: points [into ...]
- Image requirements: [...]

## DESIGN.md Notes
- Spacing rhythm: [...] · Scale ratios: [...] · Reserved colors: [...]

## Zoom-Rhythm Verdict
[banding visible? PASS / FAIL → beat rework]
```

## Quality Gate

- One primary journey; finisher committed first
- Every section beat-assigned; ≥1 true RELEASE; rhythm ends on release into the CTA
- ≥3 deliberate contrast forms, zonal; urgency color reserved
- No hero subject pointing off-screen
- DESIGN.md notes present; 10%-zoom banding verified

## Creative Latitude

The beat vocabulary is fixed; the phrasing is the composition. Long pages earn multiple phrases with varied linger lengths; dashboards compress the whole grammar into card-group breathing. The boldest choice is usually a LONGER release than feels safe — white space is the beat almost every generated page is missing.

## Deploy When

Any web surface before build or generation; rescuing pages where "everything is there" but nothing converts; auditing AI front-end that is symmetrical, evenly spaced, and dead. Not for undecided aesthetic direction (commit the tone first) and not for token codification itself (DESIGN.md owns that).
