# Design Philosophy Architect

> Define what excellence looks like BEFORE any visual work begins — the critical Step 3 that separates world-class output from AI slop.

## Context Required
- **Load First**: `genius.md` — Step 3 (Define Excellence) and Anti-Slop Architecture
- **Complementary**: `canvas-design/SKILL.md` for philosophy-to-expression framework
- **Complementary**: `@oren` taste-development for CEV evaluation

## Inputs
- **Required**: What is being designed (format, purpose, audience)
- **Required**: What should the audience FEEL when they experience it?
- **Optional**: 2-5 visual references of work the user admires
- **Optional**: Existing brand guidelines or DESIGN.md
- **Optional**: Competitor designs to differentiate from

## Workflow

### Phase 1: End-Outcome Definition

Start with the end, not the beginning. Ask:

1. **What must happen after someone sees this?**
   - Buy something → Design for conversion (urgency, clarity, trust)
   - Learn something → Design for comprehension (hierarchy, flow, retention)
   - Feel something → Design for emotion (atmosphere, imagery, rhythm)
   - Share something → Design for memorability (distinctive, screenshot-worthy)
   - Trust someone → Design for credibility (sophistication, consistency, restraint)

2. **Who is the audience?**
   - Not demographics — posture. Are they skeptical? Excited? Comparing?
   - What visual language do they associate with quality in this domain?
   - What visual patterns would make them dismiss this as amateur?

3. **What is the competitive visual landscape?**
   - What does "everyone else" in this space look like?
   - Where is the visual sameness that creates an opportunity to stand out?
   - What would be genuinely surprising for this category?

### Phase 2: Reference Curation

Collect and analyze visual references:

**Sources to mine:**
- **Godly.website** — For web design excellence
- **Midjourney** — For illustration and visual style exploration
- **25.dev** — For component and interaction patterns
- **Behance/Dribbble** — For creative execution examples
- **Google Images** — For format-specific references ("beautiful [format]")
- **Canva** — For structural templates and layout patterns
- **Competitor sites** — For differentiation opportunities

**For each reference, extract:**
1. What specifically makes this excellent? (name concrete elements)
2. What emotional response does this design create?
3. What design decisions are doing the heaviest lifting?
4. What could be borrowed? What should be avoided?

### Phase 3: Philosophy Articulation

Write a design philosophy document (4-6 paragraphs) covering:

**Paragraph 1 — The Core Aesthetic Vision:**
Name the visual movement. Not "modern and clean" (that's every AI default). Something specific:
- "Brutalist Joy" — Raw structural honesty meets unexpected warmth
- "Chromatic Silence" — Color does the talking; everything else retreats
- "Analog Meditation" — Texture, grain, and breathing room
- "Metabolist Dreams" — Organic growth patterns in systematic structures

**Paragraph 2 — Spatial Philosophy:**
How does this design treat space?
- Dense and information-rich vs. airy and minimal
- Grid-rigid vs. organic flow
- Symmetrical vs. intentionally asymmetric
- How does negative space function? (Breathing room? Luxury? Focus?)

**Paragraph 3 — Material & Color Language:**
What is the color telling the viewer?
- Warm palette = approachable, human, emotional
- Cool palette = professional, technical, trustworthy
- Monochrome + single accent = premium, focused, decisive
- Gradient-rich = dynamic, modern, energetic
- Earth tones = natural, authentic, grounded

**Paragraph 4 — Typography as Voice:**
How does the type speak?
- Heavyweight sans-serif = confident, bold, direct
- Light-weight serif = elegant, refined, intellectual
- Monospace = technical, honest, developer-friendly
- Hand-drawn = personal, creative, approachable
- Mixed weights = dynamic, hierarchical, editorial

**Paragraph 5 — The Anti-Slop Declaration:**
Explicitly state what this design REFUSES to be:
- "This is not a template. This is not InterFont on a purple gradient."
- Name the 3-5 specific AI default patterns this philosophy rejects
- State what replaces each rejected pattern

**Paragraph 6 — Craftsmanship Standard:**
Define what "done" looks like:
- "This should appear as though a senior designer spent 40 hours on it"
- "Every alignment is deliberate, every color choice is traceable, every spacing value is systematic"
- The museum test: could this be displayed as professional work?

### Phase 4: Philosophy Validation

Test the philosophy against these criteria:

| Criterion | Question | Pass |
|-----------|----------|------|
| **Specificity** | Could two designers read this and produce similar work? | Must be specific enough to constrain |
| **Distinctiveness** | Does this describe something that looks different from AI defaults? | Must have ≥3 Anti-Slop features |
| **Completeness** | Does it address color, type, space, motion, and mood? | All five must be covered |
| **Implementability** | Could this philosophy be translated into CSS in under an hour? | Yes — philosophy must map to code |
| **Emotional clarity** | Is the intended audience feeling obvious? | One reader should immediately know the mood |

## Output
- Design Philosophy Document (`.md`)
- Reference collection with annotations
- Anti-Slop checklist specific to this project
- Ready to feed into: `/design-system-forge`, `/website-build`, `/presentation-build`

## Output Schema
```
Design Philosophy Document: [project name]
├── Paragraph 1: Core Aesthetic Vision   (named movement, e.g. "Brutalist Joy")
├── Paragraph 2: Spatial Philosophy
├── Paragraph 3: Material & Color Language
├── Paragraph 4: Typography as Voice
├── Paragraph 5: Anti-Slop Declaration   (3-5 rejected patterns + replacements)
├── Paragraph 6: Craftsmanship Standard  (the "done" test)
├── Reference Collection                 (annotated, per Phase 2 extraction questions)
└── Anti-Slop Checklist                  (project-specific, feeds /design-system-forge)
```

## Quality Gate
This workflow's Quality Gate is Phase 4 above, run against the finished document before handoff:
- **Specificity**: two different designers reading the document would produce recognizably similar work — vague adjectives ("modern," "clean") fail this criterion.
- **Distinctiveness**: at least 3 named Anti-Slop features in Paragraph 5 — fewer than 3 fails the gate.
- **Completeness**: color, type, space, motion, and mood are all explicitly addressed — a philosophy silent on motion is incomplete.
- **Implementability**: a developer could translate the philosophy into CSS in under an hour — abstract mood language with no concrete mapping fails.
- **Emotional clarity**: the intended audience feeling is stated in one sentence a reader can repeat back correctly.
- Document is not handed to `/design-system-forge` until all five criteria pass — a philosophy that fails Specificity or Distinctiveness produces a generic DESIGN.md downstream.
