# LIFT System — Decision Criteria & Scoring Rubric

The LIFT System is Satori's acronym and sequenced audit pattern over four canonical composition disciplines (focal-point dominance, eye-flow choreography, tension/release, scalability — see SKILL.md caveat #4 for full attribution). Satori's contribution is the audit sequence + the 1-10 anchored scoring rubric below.

---

## L — Leverage Point

**Definition**: The single most important element on the layout. Dominated via scale, contrast, positioning, or isolation. A stranger should name it in <2 seconds.

### Tools to establish leverage
| Tool | How | Risk |
|---|---|---|
| **Scale** | Make the leverage element 1.5–4× the size of the next-largest | Overdone = imbalance; tested via flip-test |
| **Contrast** | Bright vs muted, sharp vs soft, dense vs sparse | Multiple high-contrast moves = no leverage |
| **Positioning** | Optical center, rule-of-thirds intersection, isolated quadrant | Dead-center can feel default; off-center has tension |
| **Isolation** | Surround with white space; nothing else in the local zone | Too much isolation = lonely; too little = competition |

### Leverage failure modes
1. **Multiple leverage points** competing for attention (no clear focal)
2. **Decoration outweighs content** (frame is louder than picture)
3. **Brand mark dominating where the message should** (logo as leverage)
4. **CTA not the leverage** when CTA is the goal of the design
5. **Symmetry kills leverage** — too even = no peak

### Score 1–10
- 10 — Stranger names it in <1 sec. Single, unambiguous, dominant.
- 8 — Named in 2 sec. One supporting element close in weight but resolves correctly.
- 6 — Named in 4-5 sec. Multiple competing candidates; resolves with reading.
- 4 — Can't name confidently. Visual chaos or even-weight layout.
- ≤3 — No leverage; the layout doesn't know what it wants you to see.

---

## I — Internal Rhythm (Eye Choreography)

**Definition**: Spacing, alignment, and contrast establish a trusted rhythm; eye choreography is the mechanism that carries the viewer from the leverage point through supporting elements. Predictable spacing builds trust; deliberate disruption re-engages attention.

### Components
- **Predictable spacing** — consistent margins/gutters relax the brain
- **Sequential weight drop** — leverage > primary support > secondary support > details
- **Deliberate disruption** — one or two intentional breaks (rotated element, glow, scale jump) re-engage when attention starts to drift
- **Natural reading flow** — left-to-right, top-to-bottom unless culture-targeted otherwise; eye honors gravity

### Diagnostic questions
1. Where does the eye go second? Is that intentional?
2. Where does the eye go third?
3. Are spacing/alignment predictable enough to trust?
4. Is there at least one re-engagement disruption? (Optional but high-tier)
5. Does the journey end at the desired action point (CTA / closing message)?

### Score 1–10
- 10 — Choreographed beat-by-beat. Spacing trusted. Disruption purposeful. Ends at CTA.
- 8 — Clear flow with ≥1 minor predictability gap. Mostly choreographed.
- 6 — Flow exists but feels accidental. No deliberate disruption.
- 4 — Confused journey; eye bounces. Spacing inconsistent.
- ≤3 — No flow; layout reads as random arrangement.

---

## F — Friction & Flow

**Definition**: Friction (tight spacing, blur, rotated block, scribble, tight leading) deployed strategically for emphasis. Flow (smooth-reading zones) releases tension.

### Good friction (serves leverage)
- Tight leading on a quote that demands attention
- Blur reinforcing theme (depersonalization, motion)
- Rotated 45° block forcing eye to pause and re-route
- Scribble across a face for editorial commentary
- Half-cut word at edge inviting completion

### Bad friction (compounds noise)
- 4+ fonts competing
- Multiple high-contrast focal points
- Decorative elements without reason (GP-01 violation)
- Random texture/noise that doesn't serve concept
- Crowded margins, no breathing room

### The friction/flow ratio (practitioner heuristic — not Satori-attributed)
Satori's source on this is qualitative: *"Too much tension creates chaos and too much smoothness creates boredom."* The numeric ratios below are practitioner conventions for translating his qualitative principle into a working scale; treat them as heuristics, not absolutes.
- ~80% flow / ~20% friction — trustable, readable, with key emphasis (default for most marketing / corporate / brand work)
- ~60% flow / ~40% friction — editorial / streetwear / artistic; requires confident execution
- ~50/50 — chaos territory; only attempt with mastery
- Pure flow (no friction) — boring; viewer has no anchor for emphasis

### Score 1–10
- 10 — Friction precisely placed at leverage emphasis; flow zones release. Ratio appropriate to brief.
- 8 — Friction works; one minor bad-friction instance.
- 6 — Some friction, some flow, but the *why* of friction unclear.
- 4 — Friction without purpose; or flow without any emphasis.
- ≤3 — Either frictionless boredom or noise-as-friction chaos.

---

## T — Transferability

**Definition**: The identity holds at thumbnail size, on light + dark backgrounds, across ≥2 formats (web/print/motion/social). If the concept is scale-dependent, the concept is wrong.

### Transferability test sequence
1. **Thumbnail test** — shrink to 64×64 px. Can you still recognize the leverage and brand?
2. **Light/dark test** — place on white and on black. Does it hold? (Logo should ideally have a dark + light variant.)
3. **Format test** — mock at:
   - Mobile screen (375 × 667)
   - Desktop hero (1920 × 1080)
   - Square social (1080 × 1080)
   - Vertical reel (1080 × 1920)
   - Print flyer (A4)
   Pick at least 2 from this list relevant to the brief.
4. **Motion test** (if applicable) — does the leverage point still anchor when set in motion?

### Score 1–10
- 10 — Holds across thumbnail + light/dark + 3 formats. Identity unmistakable everywhere.
- 8 — Holds across thumbnail + 2 formats. Minor adaptation needed for one format.
- 6 — Holds at full size only; thumbnail or one format breaks.
- 4 — Concept is size-dependent; fails at thumbnail or one major context.
- ≤3 — Only works in one ideal context.

---

## LIFT Composite Scoring

Sum the four scores (max 40). Convert to grade:

| Composite | Grade | Action |
|---|---|---|
| 36–40 | A — Ship | Ready for delivery |
| 32–35 | B — Polish | Minor polish on weakest dimension |
| 28–31 | C — Rework | Rework the weakest 1–2 dimensions |
| 24–27 | D — Major rework | Restart at concept layer |
| <24 | F — Restart | Concept is wrong; full restart |

**Veto rule**: If any single dimension scores ≤4, composite cannot exceed C grade regardless of total. The weakest link defines the grade.

---

## LIFT Pre-Apply Checklist

Before scoring, confirm:
- [ ] Why-before-what gate passed (every element has a reason)
- [ ] One-sentence brief documented (the design intent is clear)
- [ ] Visual primitive locked (which line type / geometry / motif)
- [ ] Predictive-empathy emotion identified (what should the viewer feel after?)

If any of the above is missing, the LIFT score is **invalid** — the foundation isn't there yet.

---

## When LIFT Doesn't Apply

LIFT is for **layouts** — posters, web pages, slides, ads, social tiles, listing cards, key visuals.

LIFT does NOT apply to:
- Logo design (use `/satori-logo-concept` and the logo-specific quality criteria)
- Pure typography selection (use Kittl)
- Color palette selection alone (use brand strategy tools)
- Pure brand naming (use Greg Hoffman / Dai Media)
