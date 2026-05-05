# Phase C — Visual

**Duration**: ~half-day. Sequential within phase.

## Required inputs

From Phase B:
- `00-foundation/01-brand-bible.md` (visual direction section)
- `00-foundation/05-non-negotiables.md` (any visual non-negotiables, e.g., Resonance's daytime-as-mechanic rule)

## Steps

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

## Quality gate (Phase C → D)

Before advancing to Phase D:
- [ ] DESIGN.md exists and lints clean (`npx @google/design.md lint` returns 0 errors)
- [ ] DESIGN.md photography rules encode the brand mechanic (not generic "warm-toned" advice)
- [ ] All hex colors hit WCAG AA contrast minimums
- [ ] photography-rules.md has the gating rule named explicitly
- [ ] component-tokens.md has ≥3 locked component templates
- [ ] aesthetic-references.md has ≥6 specific references (not generic Pinterest categories)
- [ ] brand-library-entry.md is registered in `knowledge/design-libraries/brands/`

If any unchecked, halt. Visual drift in Phase C produces mismatched briefs in Phase D — costly to fix downstream.
