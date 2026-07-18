# Reference Collection Sprint

> Rapidly curate a library of visual references that define what "excellent" looks like for any design project — the fuel for Step 3 of the 5-Step System.

## Context Required
- **Load First**: `genius.md` — Reference-First Excellence (Genius Pattern #5)

## Inputs
- **Required**: What you're designing (website, presentation, social post, brand identity, etc.)
- **Required**: What industry/domain this is for
- **Optional**: Existing brands or sites you already admire
- **Optional**: Specific aesthetic direction (dark/light, minimal/dense, playful/serious)

## Workflow

### Step 1: Define the Reference Hunt

Set clear targets:
```
Format:          [website / presentation / social / brand / report]
Industry:        [SaaS / fintech / health / creative / education / etc.]
Mood Target:     [3 adjectives that describe the desired feeling]
Anti-Targets:    [3 things it must NOT look like]
Reference Count: [10-15 references is the sweet spot]
```

### Step 2: Source Mining

Search these sources systematically:

**For Websites & Landing Pages:**
1. **Godly.website** — Search by industry/style tag
2. **Awwwards.com** — Search "site of the day" in target category
3. **Lapa.ninja** — Landing page inspiration by category
4. **SaaS Pages (saaspages.xyz)** — If SaaS-specific
5. **Land-book.com** — Searchable landing page gallery

**For Presentations:**
1. **Google Images**: "beautiful [topic] presentation"
2. **Slidesgo/SlidesCarnival** — Free template structures
3. **Speaker Deck** — Real conference presentations
4. **Canva** — Template patterns (structural, not aesthetic)

**For Brand Identity:**
1. **Brand New (underconsideration.com)** — Brand identity case studies
2. **BP&O (bpando.org)** — Branding and packaging
3. **The Dieline** — Packaging-specific
4. **Logo Design Love** — Logo-focused

**For Visual Style / Illustration:**
1. **Midjourney** — Search/generate style variations
2. **Dribbble** — Illustration and UI exploration
3. **Behance** — Full project case studies
4. **Pinterest** — Mood board aggregation

**For Components & Interactions:**
1. **25.dev** — Community-built components
2. **UI Patterns** — Interaction design patterns
3. **Mobbin** — Mobile UI patterns
4. **Refero Design** — Real product screenshots

**For DESIGN.md Systems (Google Stitch Format):**
1. **awesome-design-md** (`github.com/xb1g/awesome-design-md`, 56k+ stars) — 55+ complete brand DESIGN.md files (Stripe, Linear, Vercel, Apple, Nike, etc.). Browse these to understand what world-class design systems look like in plain-text markdown before building your own.
2. **Google Stitch** — The emerging standard for AI-readable design system specifications. All DESIGN.md files should follow or reference this format for maximum interoperability.
3. Use `/design-library-import` to fork any of these as a starting point instead of building from scratch.

### Step 3: Reference Evaluation

For each collected reference, document:

```markdown
### Reference [#]: [Name/Source]
**URL**: [link]
**Screenshot**: [saved locally]

**What makes this excellent:**
- [Specific element 1 — not "looks good"]
- [Specific element 2]
- [Specific element 3]

**Design decisions worth stealing:**
- Color: [specific observation]
- Typography: [specific observation]
- Layout: [specific observation]
- Detail: [specific observation]

**What to avoid from this:**
- [Element that doesn't fit our project]

**Transferable pattern:**
[One sentence: the design "move" we can extract and reuse]
```

### Step 4: Pattern Synthesis

After collecting 10-15 references, synthesize:

1. **Common patterns** (3-5): What do the best references share?
   - These become your design system's foundations

2. **Differentiating moves** (2-3): What does ONE reference do that no others do?
   - These become your visual signature

3. **Anti-patterns** (2-3): What did you reject, and why?
   - These feed your Anti-Slop declaration

4. **Color consensus**: What palette direction emerges from the collection?
5. **Typography consensus**: What font personality appears?
6. **Layout consensus**: Dense or airy? Grid-rigid or organic?

### Step 5: Reference Package Assembly

Compile into a single reference document:

```markdown
# Design Reference Package: [Project Name]

## Target Definition
- Format: [what we're building]
- Mood: [3 adjectives]
- Anti-targets: [what to avoid]

## Top 5 References (Ranked)
[The 5 strongest references with full annotations]

## Design Pattern Extraction
### Must-Have Patterns
[3-5 patterns that appear across top references]

### Signature Moves
[2-3 unique elements to make this project distinctive]

### Anti-Slop Declaration
[Specific patterns rejected from this reference collection]

## Direction Recommendation
[2-3 paragraphs synthesizing all references into a clear aesthetic direction]

## Next Step
→ Feed this into `/design-philosophy-architect` or `/design-system-forge`
```

## Output
- Reference Package Document (`.md`)
- Reference screenshots saved locally
- Pattern synthesis with actionable design direction
- Clear handoff to the next workflow in the pipeline

## Output Schema
```
Design Reference Package: [project name]
├── Target Definition          (Format, Mood x3, Anti-targets x3)
├── Top 5 References (Ranked)  (full Step 3 annotation per reference: What makes this excellent / Decisions worth stealing / What to avoid / Transferable pattern)
├── Design Pattern Extraction  (Must-Have Patterns 3-5, Signature Moves 2-3, Anti-Slop Declaration 2-3)
├── Direction Recommendation   (2-3 paragraphs)
└── Next Step                  (named handoff workflow)
```

## Quality Gate
- Reference count falls in the 10-15 sweet spot named in Step 1 — fewer than 10 references produces a thin, unreliable pattern synthesis.
- Every reference in Step 3 names at least 3 specific elements ("clean" or "nice" fails — must name the actual color, typography, or layout decision).
- Pattern Synthesis (Step 4) produces at least 3 Common Patterns AND at least 2 Anti-Patterns — a package with zero rejected references has not done real curation.
- Anti-Slop Declaration in the final package is populated (not left as "[Specific patterns rejected]" placeholder text) — this feeds directly into `/design-philosophy-architect`'s Paragraph 5.
- Next Step names the specific downstream workflow (`/design-philosophy-architect` or `/design-system-forge`) rather than leaving the handoff implicit.
