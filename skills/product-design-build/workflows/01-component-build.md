# Build a Component from DESIGN.md

Generate a single working component (Button, Card, Modal, etc.) consuming DESIGN.md tokens.

## Inputs

- `design_md_path` — path to validated DESIGN.md
- `component_spec` — what to build (e.g., "Button with primary, secondary, ghost intents and sm/md/lg sizes")
- `target_framework` — `react` | `vue` | `swiftui` (default: `react`)
- `output_path` — where to write (default: `./src/components/<Name>.tsx`)

## Workflow

### Step 1 — Read and parse the DESIGN.md

```bash
cat <design_md_path>
```

Pull out:
- Tokens for the component type (e.g., `components.button-primary`, `components.button-primary-hover`)
- Relevant typography level (`label-md` or `body-md` for buttons)
- Relevant rounded / spacing / color references
- The component's mention in `## Components` markdown — read the rationale for variants

### Step 2 — Inventory variants

For a Button, look for:
- Intent variants: `button-primary`, `button-secondary`, `button-tertiary`, `button-ghost`, `button-destructive`
- State variants: `-hover`, `-active`, `-disabled`, `-loading`
- Size variants: `-sm`, `-md`, `-lg`

If only `button-primary` exists, infer the others from the markdown rationale or ask the user one question. Don't fabricate variants the design system doesn't authorize.

### Step 3 — Pick the variant API

For React + TypeScript, use [class-variance-authority](https://cva.style):

```tsx
import { cva, type VariantProps } from 'class-variance-authority'

const buttonStyles = cva(
  'inline-flex items-center justify-center font-medium transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary disabled:opacity-50 disabled:pointer-events-none',
  {
    variants: {
      intent: {
        primary: 'bg-primary text-on-primary hover:bg-tertiary',
        secondary: 'border border-primary text-primary hover:bg-surface',
        ghost: 'text-primary hover:bg-surface',
      },
      size: {
        sm: 'rounded-sm px-sm py-xs text-sm',
        md: 'rounded-md px-md py-sm text-base',
        lg: 'rounded-lg px-lg py-md text-lg',
      },
    },
    defaultVariants: { intent: 'primary', size: 'md' },
  }
)
```

Map each entry to a DESIGN.md token. **No literal hex values.** Only Tailwind class references that resolve to DESIGN.md tokens.

### Step 4 — Implement the component

```tsx
import * as React from 'react'
import { cva, type VariantProps } from 'class-variance-authority'

const buttonStyles = cva(/* ... see Step 3 ... */)

interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonStyles> {
  /** Show a loading spinner instead of text */
  loading?: boolean
}

export const Button = React.forwardRef<HTMLButtonElement, ButtonProps>(
  ({ intent, size, loading, className, children, disabled, ...props }, ref) => (
    <button
      ref={ref}
      className={buttonStyles({ intent, size, className })}
      disabled={disabled || loading}
      aria-busy={loading || undefined}
      {...props}
    >
      {loading ? <Spinner /> : children}
    </button>
  )
)
Button.displayName = 'Button'
```

### Step 5 — Accessibility checklist

- [ ] Native semantic element (`<button>` not `<div role="button">` unless impossible)
- [ ] Focus ring visible (`focus:ring-*`)
- [ ] Disabled state visually distinct (`disabled:opacity-50`)
- [ ] Loading state announced (`aria-busy`)
- [ ] Keyboard accessible (Enter / Space activate by default for `<button>`)
- [ ] Forwarded ref for parent control
- [ ] `displayName` set

For inputs, modals, dropdowns — use Radix UI or Headless UI primitives. Don't roll your own.

### Step 6 — Write test stub

```tsx
// Button.test.tsx
import { render, screen } from '@testing-library/react'
import { Button } from './Button'

describe('Button', () => {
  it('renders children', () => {
    render(<Button>Save</Button>)
    expect(screen.getByRole('button', { name: 'Save' })).toBeInTheDocument()
  })

  it('disables when loading', () => {
    render(<Button loading>Save</Button>)
    expect(screen.getByRole('button')).toBeDisabled()
  })
})
```

### Step 7 — Preview

If a dev server isn't running:
```bash
# Quick preview via Vite
npm create vite@latest .preview -- --template react-ts && cd .preview && npm i
# Symlink DESIGN.md and export Tailwind theme
cp ../DESIGN.md . && npx @google/design.md export --format tailwind DESIGN.md > tailwind.theme.generated.js
# Edit src/App.tsx to render <Button> variants
npm run dev  # background
```

Then:
```
mcp__playwright__browser_navigate("http://localhost:5173")
mcp__playwright__browser_take_screenshot(filename: ".tmp/button-preview.png")
```

Read the screenshot. Critique:
- Does corner radius match `rounded.md` token?
- Does padding match `padding: 12px` from DESIGN.md?
- Is hover state visually distinct (try hovering programmatically)?
- Are typography levels correct?

### Step 8 — Iterate (max 3 cycles)

If fidelity is off, edit and re-screenshot. After 3 iterations without convergence, the DESIGN.md is under-specified — return to `skills/design-md/workflows/05-validate-and-refine.md`.

### Step 9 — Final checks

```bash
npx tsc --noEmit                    # TypeScript
npm run lint                         # ESLint
npx @google/design.md lint DESIGN.md # design system still valid
```

All three must pass. Then commit.

## Output Schema

A single component file at `output_path` that:
- Compiles
- Renders all declared variants
- Uses only DESIGN.md tokens (no literal hex / px values)
- Passes axe-core accessibility audit
- Has a test stub (Step 6)

Plus a one-paragraph build summary:
```
- Component: <name>
- Variants implemented: <intent/size/state list, each tagged with the source DESIGN.md token path>
- Accessibility checklist (Step 5): <pass/fail per item>
- Preview screenshot: <path under .tmp/, or "not taken" — see Quality Gate>
- Iterations used: <n> of 3 max
```

## Quality Gate

- Every className in the component traces to a named DESIGN.md token — zero literal hex, zero inline `style={{}}` (Step 3 rule).
- Only DESIGN.md-authorized variants were implemented — no fabricated intent/size/state combinations (Step 2).
- The component was actually rendered and screenshotted via Playwright (Step 7) — a code-only review does not satisfy this gate.
- All 7 Step 5 accessibility checklist items are checked, with Radix/Headless UI used for any input, modal, or dropdown rather than a hand-rolled primitive.
- `npx tsc --noEmit`, `npm run lint`, and `npx @google/design.md lint DESIGN.md` (Step 9) all pass.
- If 3 iterations didn't converge (Step 8), the under-specification is named and routed to `skills/design-md/workflows/05-validate-and-refine.md` rather than guessed past.

## See also

- [02-page-build.md](02-page-build.md) — when building a full page
- [03-preview-iterate.md](03-preview-iterate.md) — Playwright loop in detail
- [genius.md Section 1](../genius.md) — variant architecture

**Execution prompts**: before producing the deliverable, check `skills/design-md/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
