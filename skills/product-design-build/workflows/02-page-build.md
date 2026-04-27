# Build a Page from DESIGN.md

Generate a complete page or screen from a DESIGN.md plus a page specification. Composes primitives → composites → patterns.

## Inputs

- `design_md_path` — path to validated DESIGN.md
- `page_spec` — description of the page (e.g., "settings page with profile, billing, notifications sections")
- `output_path` — where to write (default: `./src/pages/<name>/page.tsx`)
- `target_framework` — `react` (default), `vue`, etc.

## Workflow

### Step 1 — Decompose the page spec

A page is built from layers:

```
Page (e.g., SettingsPage)
├── Layout (Header, Sidebar, Main, Footer — global chrome)
├── Sections (e.g., ProfileSection, BillingSection)
├── Composites (Card, Form, List)
└── Primitives (Button, Input, Toggle, Avatar)
```

For the verification scenario "settings page with profile, billing, notifications":
- Top-level: `SettingsPage`
- Sections: `ProfileSection`, `BillingSection`, `NotificationsSection`
- Composites needed: `SectionCard`, `Field`, `ToggleRow`
- Primitives: `Button`, `Input`, `Toggle`, `Avatar`, `Label`

### Step 2 — Inventory missing components

Check what exists in `./src/components/`. For anything missing, run [01-component-build.md](01-component-build.md) per primitive **before** building the page. Don't cram component creation into a page file.

### Step 3 — Read DESIGN.md for layout cues

Pull from `## Layout` and `## Components`:
- Max content width (`max-w-7xl` typical for 1440px)
- Spacing rhythm between sections (often `lg` or `xl` from DESIGN.md spacing)
- Whether to use a sidebar (settings often have nav rail) or single-column
- Card vs flat list style

### Step 4 — Compose the page

```tsx
// src/pages/settings/page.tsx
import { ProfileSection } from './sections/ProfileSection'
import { BillingSection } from './sections/BillingSection'
import { NotificationsSection } from './sections/NotificationsSection'

export default function SettingsPage() {
  return (
    <main className="min-h-screen bg-neutral">
      <div className="max-w-5xl mx-auto px-md py-xl">
        <header className="mb-xl">
          <h1 className="text-headline-lg text-primary mb-sm">Settings</h1>
          <p className="text-body-md text-secondary">
            Manage your account, billing, and notification preferences.
          </p>
        </header>

        <div className="space-y-xl">
          <ProfileSection />
          <BillingSection />
          <NotificationsSection />
        </div>
      </div>
    </main>
  )
}
```

### Step 5 — Build each section

```tsx
// src/pages/settings/sections/ProfileSection.tsx
import { SectionCard } from '@/components/composites/SectionCard'
import { Field } from '@/components/composites/Field'
import { Button } from '@/components/primitives/Button'

export function ProfileSection() {
  return (
    <SectionCard
      title="Profile"
      description="How others see you on the platform."
    >
      <div className="space-y-md">
        <Field label="Display name" defaultValue="Farrice Cain" />
        <Field label="Email" type="email" defaultValue="farrice@example.com" />
        <Field label="Bio" as="textarea" rows={3} />
        <div className="flex justify-end pt-md border-t border-secondary/20">
          <Button intent="primary">Save changes</Button>
        </div>
      </div>
    </SectionCard>
  )
}
```

### Step 6 — Reusable composites

`SectionCard` consolidates the section pattern from DESIGN.md:

```tsx
// src/components/composites/SectionCard.tsx
interface SectionCardProps {
  title: string
  description?: string
  children: React.ReactNode
}

export function SectionCard({ title, description, children }: SectionCardProps) {
  return (
    <section className="bg-surface rounded-lg p-lg">
      <header className="mb-md pb-md border-b border-secondary/20">
        <h2 className="text-headline-md text-primary">{title}</h2>
        {description && (
          <p className="text-body-sm text-secondary mt-xs">{description}</p>
        )}
      </header>
      {children}
    </section>
  )
}
```

`Field` consolidates label + input + error pattern:

```tsx
// src/components/composites/Field.tsx
interface FieldProps {
  label: string
  helperText?: string
  error?: string
  // ... input props passthrough
}

export function Field({ label, helperText, error, ...inputProps }: FieldProps) {
  const id = React.useId()
  return (
    <div className="space-y-xs">
      <label htmlFor={id} className="block text-body-sm font-medium text-primary">
        {label}
      </label>
      <input
        id={id}
        className="w-full rounded-sm border border-secondary/30 bg-neutral px-md py-sm text-body-md text-primary focus:border-primary focus:ring-2 focus:ring-primary/20 focus:outline-none"
        aria-describedby={error ? `${id}-error` : helperText ? `${id}-helper` : undefined}
        aria-invalid={error ? 'true' : undefined}
        {...inputProps}
      />
      {error && (
        <p id={`${id}-error`} className="text-body-sm text-tertiary">
          {error}
        </p>
      )}
      {helperText && !error && (
        <p id={`${id}-helper`} className="text-body-sm text-secondary">
          {helperText}
        </p>
      )}
    </div>
  )
}
```

### Step 7 — Responsive

Test at three breakpoints minimum:
- Mobile: 375px
- Tablet: 768px
- Desktop: 1280px

Common adjustments:
```tsx
className="px-sm md:px-md lg:px-lg"      // padding scales
className="text-headline-md md:text-headline-lg"  // type scales
className="grid grid-cols-1 md:grid-cols-2"       // layout shifts
```

For settings-style pages, single column on mobile, optional two-column on desktop with sidebar.

### Step 8 — Preview-iterate loop

Per [03-preview-iterate.md](03-preview-iterate.md):

```
1. Start dev server: npm run dev (background)
2. mcp__playwright__browser_navigate("http://localhost:5173/settings")
3. mcp__playwright__browser_take_screenshot(filename: ".tmp/settings-1.png")
4. Resize: mcp__playwright__browser_resize(width: 375, height: 812)
5. Screenshot mobile: filename: ".tmp/settings-mobile.png"
6. Critique against DESIGN.md
7. Edit; iterate
```

### Step 9 — Accessibility audit

```javascript
// In browser via Playwright evaluate
await import('axe-core').then(({ default: axe }) => axe.run())
```

Address all violations. Common issues for settings pages:
- Missing labels on form inputs (use `htmlFor` or wrap)
- Insufficient contrast on `text-secondary` against `bg-surface` (check pairing)
- No skip-to-content link (add to layout)

### Step 10 — Final pass

The Three Pass Quality Method (from SKILL.md Section "The Three-Pass Quality Method"):

1. **Structural** — TypeScript + ESLint clean; renders without console errors
2. **Brand fidelity** — Screenshot matches DESIGN.md's visual identity
3. **Virgil Test** — Has POV, has tension, one-sentence concept, every element earns its place

If any pass fails, iterate. Pass all three → ship.

## Output

A complete page (or page directory) at `output_path` that:
- Compiles + renders
- Passes accessibility audit
- Uses only DESIGN.md tokens
- Responsive across mobile / tablet / desktop
- Demonstrates the page spec end-to-end

## See also

- [01-component-build.md](01-component-build.md) — build primitives first
- [03-preview-iterate.md](03-preview-iterate.md) — Playwright preview loop
- [04-design-system-deploy.md](04-design-system-deploy.md) — wire DESIGN.md into the codebase
