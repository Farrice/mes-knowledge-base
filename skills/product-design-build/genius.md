# Product Design Build — Deep Reference (Tier 2)

This is the deep reference for `skills/product-design-build/SKILL.md`. Load it when:
- Designing a new component variant API
- Implementing accessibility for complex interactives (combobox, date picker, modal)
- Setting up a fresh Next.js / Vite project to consume DESIGN.md
- Bridging DESIGN.md tokens into Tailwind v4 / CSS-in-JS / Vanilla Extract
- Writing the preview-iterate Playwright loop

---

## 1. Variant Architecture (CVA Pattern)

The `class-variance-authority` library is the cleanest mapping from DESIGN.md `components` blocks to React component APIs. Pattern:

### DESIGN.md side
```yaml
components:
  button-primary:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.on-primary}"
    rounded: "{rounded.md}"
    padding: 12px
  button-primary-hover:
    backgroundColor: "{colors.tertiary}"
  button-secondary:
    backgroundColor: "transparent"
    textColor: "{colors.primary}"
    rounded: "{rounded.md}"
    padding: 12px
```

### React component
```tsx
import { cva, type VariantProps } from 'class-variance-authority'

const buttonStyles = cva(
  // base styles — apply to every variant
  ['inline-flex items-center justify-center font-medium transition-colors',
   'focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary',
   'disabled:opacity-50 disabled:pointer-events-none'],
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

interface ButtonProps
  extends React.ButtonHTMLAttributes<HTMLButtonElement>,
    VariantProps<typeof buttonStyles> {}

export function Button({ intent, size, className, ...props }: ButtonProps) {
  return <button className={buttonStyles({ intent, size, className })} {...props} />
}
```

### Why CVA over alternatives
- **vs. inline `className` strings**: CVA gives you typed variants, autocomplete, and exhaustiveness checking
- **vs. styled-components / Emotion**: CVA stays static — no runtime cost, no CSS-in-JS overhead, full Tailwind JIT
- **vs. tw-classed**: CVA has better TypeScript ergonomics

---

## 2. Token → Tailwind Mapping

When DESIGN.md is exported via `npx @google/design.md export --format tailwind`, the output extends `theme.extend`:

```javascript
// tailwind.theme.generated.js
export const theme = {
  colors: {
    primary: '#1A1C1E',
    secondary: '#6C7278',
    tertiary: '#B8422E',
    neutral: '#F7F5F2',
    surface: '#FCFAFA',
    'on-primary': '#FFFFFF',
    'on-tertiary': '#FFFFFF',
  },
  fontSize: {
    'hero-display': ['56px', { lineHeight: '1.07', letterSpacing: '-0.02em', fontWeight: '600' }],
    'headline-lg': ['40px', { lineHeight: '1.1', letterSpacing: '-0.01em', fontWeight: '600' }],
    'body-md': ['16px', { lineHeight: '1.6', fontWeight: '400' }],
    'label-caps': ['12px', { lineHeight: '1', letterSpacing: '0.1em', fontWeight: '500' }],
  },
  borderRadius: { sm: '4px', md: '8px', lg: '12px', full: '9999px' },
  spacing: { xs: '4px', sm: '8px', md: '16px', lg: '32px', xl: '64px' },
  fontFamily: {
    sans: ['Public Sans', 'system-ui', 'sans-serif'],
    mono: ['Space Grotesk', 'monospace'],
  },
}
```

### Wire it
```typescript
// tailwind.config.ts
import type { Config } from 'tailwindcss'
import { theme } from './tailwind.theme.generated.js'

export default {
  content: ['./src/**/*.{ts,tsx}'],
  theme: { extend: theme },
} satisfies Config
```

### Rebuild trigger
Add to `package.json` scripts:
```json
{
  "scripts": {
    "design:lint": "npx @google/design.md lint DESIGN.md",
    "design:export": "npx @google/design.md export --format tailwind DESIGN.md > tailwind.theme.generated.js",
    "design:check": "npm run design:lint && npm run design:export"
  }
}
```

Run `npm run design:check` in CI and as a pre-commit hook.

---

## 3. Accessibility Patterns

The lint rule `contrast-ratio` only checks defined component pairs. **You** are responsible for everything else. Key patterns:

### Focus rings
Every interactive element needs a visible focus state. The DESIGN.md primary color usually provides the ring color:
```tsx
className="focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2"
```

### Skip-to-content
Every page needs a hidden-until-focused skip link:
```tsx
<a href="#main" className="sr-only focus:not-sr-only focus:absolute focus:top-md focus:left-md focus:z-50 bg-primary text-on-primary px-md py-sm rounded-md">
  Skip to main content
</a>
```

### Form labels
Every input needs an associated label. Use `htmlFor` or wrap:
```tsx
<label className="block">
  <span className="block text-body-sm text-primary mb-xs">Email</span>
  <input type="email" className="w-full ..." />
</label>
```

### Modal / Dialog
Use a battle-tested primitive (Radix, Headless UI). Never roll your own. Trap focus, restore on close, escape key, click-outside.

### Dynamic content
Announce changes to screen readers:
```tsx
<div role="status" aria-live="polite" className="sr-only">
  {saved && 'Settings saved'}
</div>
```

### Test it
Install axe-core in the preview project and run via the React dev integration. In `.preview/src/main.tsx` (dev only):
```tsx
if (import.meta.env.DEV) {
  import('@axe-core/react').then(({ default: axe }) => {
    axe(React, ReactDOM, 1000)
  })
}
```
Violations stream to the browser console; capture with `mcp__playwright__browser_console_messages()`.

---

## 4. The Preview-Iterate Playwright Loop

### Setup
Either you have a running dev server (Next.js, Vite) or you scaffold one:

```bash
# If no preview exists, create a minimal Vite preview
npm create vite@latest .preview -- --template react-ts
cd .preview
npm install
# Symlink the DESIGN.md
ln -s ../DESIGN.md DESIGN.md
# Or: copy and re-export tailwind config
cp ../DESIGN.md . && npx @google/design.md export --format tailwind DESIGN.md > tailwind.theme.generated.js
```

### The loop

```
1. Write component
2. Start dev server (background): npm run dev (logs to .tmp/dev.log)
3. mcp__playwright__browser_navigate("http://localhost:5173/preview/Button")
4. mcp__playwright__browser_take_screenshot(filename: ".tmp/iter-1.png")
5. Read screenshot — critique against DESIGN.md
6. Edit component
7. Vite hot-reloads automatically
8. mcp__playwright__browser_take_screenshot(filename: ".tmp/iter-2.png")
9. Compare iter-1 and iter-2 — did the change land?
10. Repeat steps 5-9 until convergence (max 3 iterations)
```

### Critique checklist
- Does the corner radius match the `rounded.*` token in DESIGN.md?
- Do the colors match (use DigitalColor Meter on macOS to verify exact hex)?
- Is the typography hierarchy honored (h1 > h2 > body > caption)?
- Does the hover state actually change appearance (often forgotten)?
- Is the focus state visible (often invisible by default in Tailwind)?
- Is there enough padding (cramped components are the #1 brand-fidelity failure)?

### Convergence rule
If after 3 iterations you can't get visual fidelity, the DESIGN.md is under-specified. **Stop. Return to `skills/design-md/workflows/05-validate-and-refine.md`** to add the missing rules. Don't keep guessing in code.

---

## 5. Page Composition Patterns

### Hero section
```tsx
<section className="bg-neutral text-primary px-md py-xl md:py-2xl">
  <div className="max-w-7xl mx-auto">
    <h1 className="text-hero-display text-primary mb-md">{title}</h1>
    <p className="text-body-lg text-secondary max-w-3xl mb-lg">{tagline}</p>
    <div className="flex gap-sm">
      <Button intent="primary">{primaryCta}</Button>
      <Button intent="secondary">{secondaryCta}</Button>
    </div>
  </div>
</section>
```

### Card grid
```tsx
<div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-md">
  {items.map(item => (
    <Card key={item.id} className="rounded-md p-md bg-surface">
      <h3 className="text-headline-md text-primary mb-sm">{item.title}</h3>
      <p className="text-body-md text-secondary">{item.description}</p>
    </Card>
  ))}
</div>
```

### Settings list
For settings-style pages (the verification scenario in the plan):
```tsx
<dl className="divide-y divide-secondary/20">
  {settings.map(setting => (
    <div key={setting.id} className="py-md flex items-center justify-between">
      <div>
        <dt className="text-body-md text-primary font-medium">{setting.label}</dt>
        <dd className="text-body-sm text-secondary mt-xs">{setting.description}</dd>
      </div>
      <Toggle checked={setting.value} />
    </div>
  ))}
</dl>
```

---

## 6. Common Anti-Patterns

| Anti-pattern | Why it's bad | Fix |
|---|---|---|
| Hardcoded hex values in className | Breaks token cascade | Reference Tailwind class: `bg-primary` |
| `style={{ }}` inline styles | Bypasses Tailwind / token system | Use className with Tailwind utility |
| `!important` to override DESIGN.md | Brand drift; system erodes | Update DESIGN.md if the override is correct; remove if not |
| Disabled-state has no visual difference | Accessibility failure | Add `disabled:opacity-50 disabled:cursor-not-allowed` |
| Hover state disappears on touch | Mobile broken | Use `@media (hover: hover)` or accept Tailwind's default |
| Component has its own font-size override | Sprawl | Map to DESIGN.md typography level |
| Margin between siblings via `mt-*` everywhere | Implicit; fragile | Use parent flex/grid `gap-*` instead |
| Building a Modal from scratch | Accessibility nightmares | Use Radix Dialog, Headless UI Dialog, or shadcn/ui |

---

## 7. SwiftUI / Native Bridge

For iOS/macOS native, the path is:

```
DESIGN.md
  → npx @google/design.md export --format dtcg → tokens.json
  → Style Dictionary → DesignTokens.swift (constants)
  → SwiftUI consumes via:
      Color("primary"), Font.custom("PublicSans-SemiBold", size: 56)
```

Style Dictionary config (`config.json`):
```json
{
  "source": ["tokens.json"],
  "platforms": {
    "ios": {
      "transformGroup": "ios-swift",
      "buildPath": "ios/",
      "files": [{ "destination": "DesignTokens.swift", "format": "ios-swift/class.swift" }]
    }
  }
}
```

This is more setup than React, but DESIGN.md remains the single source. Updates flow web + iOS in one regenerate.

---

## 8. Verification Tactics

### Visual regression testing
Once a component is approved, snapshot it:
```bash
mcp__playwright__browser_take_screenshot(filename: "tests/visual/Button-primary.png")
```

In CI, re-screenshot and pixel-diff. If pixels diverge unintentionally, fail the build.

### Token coverage report
After building a component or page, grep for hex values in your code:
```bash
grep -RE '#[0-9a-fA-F]{6}' src/ --include="*.tsx" | grep -v 'DESIGN.md\|generated'
```

If hits exist, you have token drift. Fix by replacing with class references.

### The lint chain
```bash
npm run design:lint           # validate DESIGN.md
npm run design:export         # regenerate Tailwind theme
npm run typecheck             # TypeScript
npm run test                  # vitest / jest
npm run a11y                  # axe-core via Playwright
```

All five must pass before merging.

---

## 9. When to Stop

This skill ships shippable code. You're done when:
- Component / page renders without errors
- Tailwind classes consistently reference tokens (no literal hex)
- Visual fidelity to DESIGN.md confirmed via Playwright screenshot
- axe-core finds 0 violations
- All three Quality Method passes pass (structural / brand / Virgil)

If you can't reach all five, escalate:
- Failing structural? → re-check React/Tailwind setup; missing peer deps
- Failing brand fidelity? → DESIGN.md is under-specified; route to `skills/design-md/`
- Failing Virgil Test? → the design itself is generic; route to `skills/oren-taste-development/`
