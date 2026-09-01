# Phase C — Visual

**Duration**: ~half-day. Sequential within phase.

## Required inputs

From Phase B:
- `00-foundation/01-brand-bible.md` (visual direction section)
- `00-foundation/05-non-negotiables.md` (any visual non-negotiables, e.g., Resonance's daytime-as-mechanic rule)
- `_working/A4-design-challenge-ledger.md` (evidence-backed questions, proving surfaces, and falsifiers)

## Steps

### C0 — Direction decision spine

Before tokenizing the system, use the Andrew Lane vibe-foundation workflow and its [Brand Direction Decision Spine](../../andrew-lane-design-systems/references/brand-direction-decision-spine.md):

1. Build a broad, categorized internal exploration board.
2. Translate it into three strategically distinct client stylescapes. Every direction must answer at least one A4 design challenge.
3. Annotate dominant references with role, exact borrowed quality, and implication; record any material production or licensing consequence.
4. Select one direction, explicitly borrow or reject elements from the others, then apply it to the named proving surface.
5. Convert only the direction that survives that application test into reusable rules and tokens.

Outputs:

- `01-visual/internal-exploration-board.md`
- `01-visual/direction-set.md`
- `01-visual/direction-decision-ledger.md`
- `01-visual/proving-surface.md`

### C1 — DESIGN.md

Run `/design-md-synthesize` (skill: `skills/design-md/`):

> Produce a DESIGN.md v2 (Google Labs spec) for the brand. Both layers:
> 1. YAML front-matter — design tokens (colors, typography, spacing, components)
> 2. Markdown body — 8 ordered sections explaining WHY the tokens exist
>
> Photography rules MUST encode the brand mechanic. For Resonance: "If a photo could have been taken at 11pm, it fails." For other brands: derive the equivalent gating rule from the non-negotiables.
>
> WCAG AA contrast on all color tokens. Lints clean via `npx @google/design.md lint`.

Output: `01-visual/DESIGN.md`.

**Verification**:
```bash
npx @google/design.md lint <output>/01-visual/DESIGN.md
```
Must return clean. If lints fail, fix before proceeding.

### C2 — Brand library entry

Run `/brand-library` (skill: `skills/design-md/` workflow):

> Produce the brand-library entry that feeds the design-md tooling. Token block + library metadata + "import-brand" path so other projects can `import-brand` from this BOS.

Output: `01-visual/brand-library-entry.md` + entry in `knowledge/design-libraries/brands/<brand-slug>/`.

### C3 — Aesthetic refs + component tokens + photography rules

Run `/junyuh-brandbook` (skill: `skills/junyuh-brandbook/`):

> Produce the visual + verbal brandbook supporting docs:
> 1. **aesthetic-references.md** — mood board with links + descriptions, visual proof points for AI prompt scaffolding (Midjourney, Sora). Reference real-world examples that match the brand mechanic.
> 2. **component-tokens.md** — locked IG template, flyer template, ticket template, etc. Repeatable design tokens.
> 3. **photography-rules.md** — explicit rules: real bodies / lighting / composition / what fails the gate. The standalone version of DESIGN.md's photography section, expanded.

Output:
- `01-visual/aesthetic-references.md`
- `01-visual/component-tokens.md`
- `01-visual/photography-rules.md`

## Output Schema

Phase C produces the 5 visual-layer docs, all downstream of the mechanic locked in Phase B:

- **`01-visual/DESIGN.md`** — Google Labs v2 spec: YAML front-matter (color/typography/spacing/component tokens) plus an 8-section markdown body explaining why each token exists. Photography rules must encode the brand's specific mechanic (Resonance's gating rule: "if a photo could have been taken at 11pm, it fails") — a generic "warm-toned, aspirational" rule fails this schema. Must lint clean via `npx @google/design.md lint` and pass WCAG AA contrast on every color token.
- **`01-visual/internal-exploration-board.md`** — broad, categorized research with a named role and borrowed quality for every retained reference; never sent as the client commitment artifact.
- **`01-visual/direction-set.md`** — three distinct client stylescapes, each tied to the A4 challenge ledger and edited into a coherent argument.
- **`01-visual/direction-decision-ledger.md`** — trace from discovery evidence through selected/borrowed/rejected direction elements to system rules.
- **`01-visual/proving-surface.md`** — the chosen direction applied to the highest-consequence first touchpoint, with failures and revisions recorded.
- **`01-visual/brand-library-entry.md`** — the token block plus library metadata plus import-brand path, registered under `knowledge/design-libraries/brands/<brand-slug>/`.
- **`01-visual/aesthetic-references.md`** — ≥6 specific real-world references (not generic Pinterest categories) that double as visual proof points for AI image-prompt scaffolding.
- **`01-visual/component-tokens.md`** — ≥3 locked, repeatable component templates (IG post, flyer, ticket, etc.).
- **`01-visual/photography-rules.md`** — the standalone, expanded version of DESIGN.md's photography section, with the gating rule named explicitly rather than implied.

## Quality gate (Phase C → D)

Before advancing to Phase D:
- [ ] Three directions answer named A4 challenges rather than expressing three cosmetic variants
- [ ] Every dominant reference has a role, borrowed quality, and stated implication; cost or licensing consequences are explicit when material
- [ ] The chosen direction has been revised in context on the named proving surface
- [ ] Every visual rule can be traced through the direction-decision ledger to evidence or an explicit human taste decision
- [ ] DESIGN.md exists and lints clean (`npx @google/design.md lint` returns 0 errors)
- [ ] DESIGN.md photography rules encode the brand mechanic (not generic "warm-toned" advice)
- [ ] All hex colors hit WCAG AA contrast minimums
- [ ] photography-rules.md has the gating rule named explicitly
- [ ] component-tokens.md has ≥3 locked component templates
- [ ] aesthetic-references.md has ≥6 specific references (not generic Pinterest categories)
- [ ] brand-library-entry.md is registered in `knowledge/design-libraries/brands/`

If any unchecked, halt. Visual drift in Phase C produces mismatched briefs in Phase D — costly to fix downstream.
