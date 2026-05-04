---
description: Inject Satori's grid taxonomy + leverage rules into a DESIGN.md spec — composition tokens that make Jack Roberts' code-first system inherit Satori's composition theory
---

# /satori-design-md-grid — Inject Composition Theory Into DESIGN.md (Jack Roberts Stack)

`design-md` and `jack-roberts-design-mastery` produce DESIGN.md files that codify visual identity into reusable tokens. But most DESIGN.md output captures *colors, type, components* — not composition theory. This workflow injects Satori's grid taxonomy + leverage rules + movement-level defaults into a DESIGN.md spec, so generated UI/page code inherits composition discipline at the token level.

## Pre-Flight Gate

**Use this when**:
- Building a new DESIGN.md from scratch with Satori-grade composition
- Auditing an existing DESIGN.md that produces "AI-default" page layouts
- Need composition consistency across many pages produced from one DESIGN.md
- Want to encode "anti-AI-slop" defaults at the system level

**Do NOT use this when**:
- DESIGN.md is for a brand whose strategy explicitly calls for "neutral / templatable / fast-shipping" — over-specifying composition slows generation
- The system is for highly-variable creative content (each piece composed by a designer) — composition tokens constrain creativity inappropriately
- You don't have an existing DESIGN.md or design-md skill loaded

## Stacks With

- **`design-md`** (skills/design-md, Google Labs DESIGN.md v2 spec) — primary stacking partner
- **`jack-roberts-design-mastery`** (skills/jack-roberts-design-mastery) — secondary; if Jack Roberts forge produced the DESIGN.md, this workflow extends it
- **`product-design-build`** (skills/product-design-build) — UI/component generation downstream consumes the enhanced DESIGN.md

## Skill Acquisition

Load:
- `genius.md` — GP-05 (Grid Taxonomy), GP-06 (LIFT), GP-04 (Movement Ladder), GP-11 (Anti-AI-Slop)
- `references/grid-taxonomy-selector.md`
- `references/lift-system-decision-criteria.md`
- The DESIGN.md being enhanced (read it first; understand the brand's color/type/component tokens already locked)

## Execution

### Step 1: Audit the Existing DESIGN.md

Read the existing DESIGN.md and identify:
- **Color system**: locked? complete?
- **Type system**: scale + leading + tracking documented?
- **Component patterns**: defined?
- **Composition tokens**: usually NOT present — this is the gap we're filling
- **Movement / grid guidance**: usually NOT present — this is the gap we're filling

Document the gap explicitly: "DESIGN.md has [X complete], lacks [composition theory tokens]."

### Step 2: Identify Brand Composition DNA

Determine the brand's composition character. This drives every subsequent token:

- **Density**: airy / balanced / dense
- **Asymmetry tolerance**: none / low / high
- **Movement energy**: calm / steady / kinetic / pulsing
- **Grid breakage tolerance**: none / occasional / frequent (brand-identity-level)
- **Friction philosophy**: smooth-everything / strategic-friction / friction-as-identity

Document each as a single value. Brand-DNA-level decisions; not page-level.

### Step 3: Inject Grid Taxonomy Tokens

Add a `## Composition` section (or extend an existing layout/grid section) with grid-system tokens:

```markdown
## Composition

### Grid Taxonomy
- **Default grid**: [one of: column / modular / hierarchy / asymmetric / manuscript / etc.]
- **Default columns**: [n]
- **Default gutter**: [px / rem]
- **Default margin**: [outer page margin spec]
- **Baseline grid**: [body leading × multiples for headlines]

### Per-Page-Type Grid Defaults
| Page type | Grid | Columns | Breakage allowed? |
|---|---|---|---|
| Marketing landing | Asymmetric | 12 (3+6+3) | Yes — hero only |
| Product detail | Modular | 12 | Featured product spans 8/12 |
| Article / blog | Manuscript + Baseline | Single col | None |
| Dashboard | Hierarchy | 12 | Primary widget spans 12 |
| Listing / index | Modular | 12 | None |
| Settings | Hierarchy | 12 | None — clarity first |
```

### Step 4: Inject Leverage Rules

Add leverage-point defaults — every page generated from this DESIGN.md should have an unmistakable leverage point.

```markdown
### Leverage Defaults
- **Per-page rule**: every page must have ONE leverage point
- **Marketing pages**: leverage = primary CTA OR primary message (specify per page-type)
- **Product pages**: leverage = primary product image
- **Article pages**: leverage = headline (or featured pull-quote for long articles)
- **Dashboard pages**: leverage = current-state primary metric

### Dominance Tools (per leverage)
- Scale: leverage element ≥ 1.5× next-largest
- Contrast: leverage uses primary brand color OR highest-contrast pair
- Position: leverage at upper-third intersection (rule-of-thirds default)
- Isolation: ≥ 2× standard padding around leverage

### Anti-Pattern Veto
- Two equal-weight focal points → REWORK
- Brand mark dominating where message should → REWORK
- Decoration outweighing content → REWORK
```

### Step 5: Inject Movement Level Defaults

Add movement-level guidance per page type:

```markdown
### Movement & Flow
- **Default level**: [1-6 from Satori ladder]
- **Per-page-type defaults**:

| Page type | Movement level |
|---|---|
| Marketing landing | 2-3 (hierarchy + multiple flows) |
| Product detail | 2 (hierarchy-driven) |
| Article | 2 (hierarchy) |
| Dashboard | 1-2 (clarity-first) |
| Onboarding | 1-2 (instructional) |
| Hero campaign | 4-5 (implied motion + disruption) |

### Disruption Budget
- ≤1 disruption per page
- Disruption must serve leverage or closing message
- Forbidden: multiple competing flows on one page
```

### Step 6: Inject Friction & Flow Tokens

Add friction-flow philosophy tokens:

```markdown
### Friction & Flow
- **Brand friction philosophy**: [smooth-everything / strategic-friction / friction-as-identity]
- **Default friction zones**: [where intentional friction lives]
- **Friction-flow ratio**: [80/20 standard, 60/40 editorial, never 50/50]
- **Good friction examples** (allowed): tight leading on featured quotes, blur reinforcing theme, single rotated element, half-cut text at edge
- **Bad friction examples** (forbidden): 4+ fonts, multiple high-contrast focal points, decorative noise without rent
```

### Step 7: Inject Transferability Tokens

Add transferability requirements:

```markdown
### Transferability
- **Mandatory aspect ratios**: [list every format the system must support]
- **Thumbnail integrity**: every component must hold at thumbnail size (test at 64×64 px for icons, 200×140 px for cards, 600×400 px for heroes)
- **Light/dark parity**: every component has light + dark variant; identity preserved
- **Print considerations** (if applicable): CMYK-safe palette, bleed margins, paper-texture compensation
```

### Step 8: Inject Anti-AI-Slop Defaults

Add system-level imperfection injection rules:

```markdown
### Anti-AI-Slop Defaults
The system enforces composition character through these defaults:
1. **Asymmetric breathing**: outer margins NOT symmetric — left:right ratio [e.g., 1.0:1.15]
2. **Type-size variance**: type scale NOT a smooth ratio — explicit jumps (14/22/52, not 14/24/40)
3. **Color punctuation**: accent color used in ≤1 zone per page
4. **Hand-feel element**: at least one component carries a hand-drawn / textured / non-vector treatment
5. **Off-grid budget**: 1 element per page may break grid (with reason documented)

### Forbidden Patterns
- Center-aligned everything (perfect symmetry without reason)
- Even spacing across all gaps (no rhythm variation)
- Default 12-column without breakage (template feel)
- Equal weight across 4 quadrants (no leverage)
- Smooth color ramps without punctuation
```

### Step 9: Lint Existing Components Against New Tokens

For each component currently in the DESIGN.md, validate against the new composition tokens:

| Component | Grid? | Leverage? | Movement | Friction | Transferable | Anti-slop |
|---|---|---|---|---|---|---|
| Hero | Asymmetric ✓ | CTA ✓ | L3 ✓ | None ✗ — needs friction | Lacks 64px thumb | Symmetric — needs imbalance |
| Card | Modular ✓ | Image ✓ | L2 ✓ | OK | OK | Type-size ratio too smooth |
| ... | ... | ... | ... | ... | ... | ... |

For each gap, propose a specific token-level fix.

### Step 10: Output the Enhanced DESIGN.md

Produce the updated DESIGN.md with composition section injected. Format:

```markdown
# Enhanced DESIGN.md — [brand name]

## [Existing sections retained]
[colors, type, components — unchanged unless specifically edited]

## Composition (NEW — Satori injection)
### Brand Composition DNA
[density / asymmetry tolerance / movement energy / breakage tolerance / friction philosophy]

### Grid Taxonomy
[default grid + per-page-type grids]

### Leverage Defaults
[per-page rule + dominance tools + anti-pattern veto]

### Movement & Flow
[default level + per-page levels + disruption budget]

### Friction & Flow
[philosophy + zones + ratio + good/bad examples]

### Transferability
[aspect ratios + thumbnail + light/dark + print]

### Anti-AI-Slop Defaults
[5 imperfection defaults + forbidden patterns]

## Component Audit Results
[table of existing components scored against new tokens + per-component fixes]

## CLI Validation
After writing: run `npx @google/design.md lint <file>` to verify v2 spec compliance.
```

## Content Type Adaptations

| Brand type | Composition emphasis |
|---|---|
| **Editorial / publication** | Manuscript + Baseline grids; movement L3; friction philosophy = strategic |
| **E-commerce / product** | Modular grid; leverage = product image; movement L2; smooth flow |
| **SaaS / dashboard** | Hierarchy grid; movement L1-2; clarity-first friction |
| **Streetwear / lifestyle brand** | Asymmetric; movement L4-5; high breakage tolerance; friction-as-identity |
| **Luxury / premium** | Asymmetric or Hierarchy; movement L5-6; restrained friction |
| **Real estate brokerage** | Hierarchy + Modular; movement L2; trust-first (low breakage) |
| **Personal brand / creator** | Variable — match creator's voice DNA |
| **Tech infrastructure** | Hierarchy; movement L1-2; system-trust feel |

## Output Requirements

Enhanced DESIGN.md must include:
1. Brand composition DNA (5 axes documented)
2. Grid taxonomy (default + per-page-type)
3. Leverage defaults (rule + tools + veto)
4. Movement defaults (default + per-page + disruption budget)
5. Friction & flow tokens (philosophy + zones + ratio + good/bad)
6. Transferability requirements
7. Anti-AI-slop defaults (5+ imperfection rules + forbidden patterns)
8. Component audit + per-component fixes
9. CLI validation reference

## Quality Gate (Genius Rubric)

- [ ] **All 6 Satori dimensions** added (composition DNA, grid, leverage, movement, friction, transferability, anti-slop)
- [ ] **Per-page-type defaults** specified (not just system-level abstractions)
- [ ] **Component audit** completed (existing components scored)
- [ ] **Per-component fixes** proposed at token level
- [ ] **No abstract directives** — every token is implementable
- [ ] **DESIGN.md v2 lint passes** (`npx @google/design.md lint`)

## Source Grounding

This workflow extends the Google Labs DESIGN.md spec (auto-memory: `project_design-md-v2-integration.md`) with Satori's composition theory:
- GP-05 (Grid Taxonomy) becomes per-page-type grid defaults
- GP-06 (LIFT) becomes leverage rules + transferability requirements
- GP-04 (Movement Ladder) becomes per-page movement-level defaults
- GP-11 (Anti-AI-Slop) becomes system-level imperfection injection rules

> *"AI can give you the clean version every time, but only you can give the human version."* — Satori. This workflow makes "the human version" the system default.

## Memory Note

DESIGN.md v2 integration project (auto-memory `project_design-md-v2-integration.md`):
- 58-brand library at `knowledge/design-libraries/brands/`
- CLI: `npx @google/design.md lint|diff|export|spec`
- New skills: `skills/design-md/`, `skills/product-design-build/`
- New capabilities: `/design-md-extract`, `/design-md-synthesize`, `/design-md-validate`, `/brand-library`, `/product-build`
