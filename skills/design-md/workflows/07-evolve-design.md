# Evolve a Design System (Diff and Merge)

Compare two versions of a DESIGN.md, surface drift and regression, and propose a merge strategy.

## When to use

- Before approving a brand refresh / redesign
- When a designer + engineer have diverged on the same DESIGN.md
- Quarterly design system review

## Inputs

- `before` — earlier version of DESIGN.md (typically `git show HEAD~10:DESIGN.md > /tmp/before.md`)
- `after` — current version
- `output_format` — `summary` | `merge-proposal`

## Workflow

### Step 1 — Run the official diff

```bash
npx @google/design.md diff <before> <after> --format json > /tmp/diff.json
```

Output structure:
```json
{
  "tokens": {
    "colors": { "added": ["accent"], "removed": [], "modified": ["tertiary"] },
    "typography": { "added": [], "removed": ["caption-xs"], "modified": [] },
    "rounded": { "added": [], "removed": [], "modified": ["md"] },
    "spacing": { "added": [], "removed": [], "modified": [] },
    "components": { "added": ["chip"], "removed": [], "modified": ["button-primary"] }
  },
  "regression": false
}
```

`regression: true` means the linter detected a change that would break existing usage (a token was renamed without alias, a contrast pair fell below AA after the change, etc.). **Treat regression: true as a blocker.**

### Step 2 — Categorize changes

Group findings into four buckets:

| Bucket | Examples | Action |
|---|---|---|
| **Additive** | new color, new component variant | Safe to merge; document in changelog |
| **Refinement** | shade adjusted, line-height tweaked | Safe but verify visual impact via product-design-build preview |
| **Breaking** | token removed, name changed, semantic role swapped | Provide migration path: alias the old name, deprecation comment |
| **Regression** | contrast fell below AA, broken-ref introduced | Block; require fix |

### Step 3 — Visual diff

For refinement-bucket changes, render before + after components side by side. Use product-design-build:

```bash
# Stage 1: build a sample component with before
cp <before> /tmp/before-DESIGN.md
# Generate a button with the old tokens

# Stage 2: build same component with after
cp <after> /tmp/after-DESIGN.md

# Compare via Playwright screenshots
```

Refer to `skills/product-design-build/workflows/03-preview-iterate.md` for the screenshot workflow.

### Step 4 — Author the merge proposal

For non-trivial diffs, write a `MERGE-PROPOSAL.md`:

```markdown
# DESIGN.md Merge Proposal

## Summary
Brand refresh: warmer accent, tightened type scale, new chip component.

## Token Changes

### Added
- `colors.accent: #B8422E` (Boston Clay) — for highlight states

### Modified
- `colors.tertiary`: `#3B82F6` → `#B8422E` (the brand pivot)
- `rounded.md`: `8px` → `6px` (tighter geometric register)
- `components.button-primary.backgroundColor`: now references `{colors.accent}` instead of `{colors.tertiary}`

### Removed
- `typography.caption-xs` (replaced by `body-sm` for legibility)

### Breaking
- `colors.tertiary` semantic role shifted — code referencing `colors.tertiary` for primary CTAs will visually shift from blue to clay. **Migration:** review all `tertiary` usage; alias if needed.

## WCAG Impact
- New pair `colors.accent` + `colors.neutral` → 4.4:1 (FAILS AA for normal text)
- **Mitigation:** restrict to large/bold text; document in `## Do's and Don'ts`

## Recommendation
Approve with the WCAG mitigation. The shift to clay strengthens the editorial gravitas without losing accessibility for primary CTAs (which use white-on-clay = 4.4:1 + bold = AA-compliant).
```

### Step 5 — Validate the merged result

```bash
python3 execution/design_md_validate.py <after>
```

Confirm 0 errors and any new warnings are intentional.

### Step 6 — Document in changelog

If the project maintains a `CHANGELOG.md`, add an entry:
```markdown
## [2026-04-27] Design system v2

- **Brand refresh:** primary accent shifts from cool blue (#3B82F6) to warm clay (#B8422E)
- **Tightened geometry:** `rounded.md` 8px → 6px
- **New component:** `chip` (selection + filter variants)
- **Removed:** `typography.caption-xs` (use `body-sm`)
- **Migration notes:** see MERGE-PROPOSAL.md in this commit
```

## Heuristics for Common Evolution Patterns

### "We're going darker"
- Inverting the system: `colors.canvas` flips from light to dark
- Re-validate every component pair (most contrast issues will surface here)
- Add explicit `dark-` variants for components rather than swapping semantics

### "We're tightening the scale"
- Spacing scale gets compressed: `lg: 32px → 24px`
- Typography may need re-sampling: tight body sizes become uncomfortable
- Watch for cascading layout breaks in product-design-build previews

### "We're adding a new product line"
- Don't fork the DESIGN.md — extend it
- Add new component blocks: `card-product-a`, `card-product-b`
- Or add a new color palette tier: `colors.product-line-2`

### "Designer keeps pushing illegible contrast"
- Honor the brand intent but encode the failure as a usage rule
- Add to `## Do's and Don'ts`: "Don't use `colors.muted-text` on `colors.surface-tinted` — fails AA; reserved for icon-only labels"

## See also

- [05-validate-and-refine.md](05-validate-and-refine.md) — full lint workflow
- [genius.md Section 4](../genius.md) — lint rules
- [06-export-and-handoff.md](06-export-and-handoff.md) — re-export Tailwind / DTCG after merge
