# Import a Brand from the Library

Pull a curated DESIGN.md from `knowledge/design-libraries/brands/` (58 brands), customize at minimum 3 elements, and save as the project's starter DESIGN.md.

## When to use

- User says "make it look like Apple/Stripe/Linear/Notion/[etc.]"
- User wants a high-quality starting point and will customize from there
- Speed matters more than originality (early prototyping, throwaway demos)

## Inputs

- `brand_slug` — e.g., `apple`, `stripe`, `linear-app`, `cursor`, `vercel`
- `output_path` — where to write (default: `./DESIGN.md`)
- `customize_name` — required new project name
- (optional) `customize_description` — new description sentence
- (optional) `customize_accent` — new tertiary/accent hex if user has a brand color

## Workflow

### Step 1 — Verify the brand is in the library

```bash
python3 execution/design_md_brand_lookup.py search "<query>"
# or list all
python3 execution/design_md_brand_lookup.py list
```

If not in local library, fall back to upstream:
```bash
cd /tmp && npx -y getdesign@latest add <slug>
# Then copy /tmp/DESIGN.md to knowledge/design-libraries/brands/<slug>/DESIGN.md
```

### Step 2 — Read the source brand file

```bash
cat knowledge/design-libraries/brands/<brand_slug>/DESIGN.md
```

Note:
- Total token count (color count, typography levels, components defined)
- The cultural anchor in the description
- Any signature elements (a specific font pairing, a unique component pattern)

### Step 3 — Customize three elements minimum

**The library is reference, not output.** Never ship an unmodified brand file. At minimum change:

1. **`name`** — to the user's project name (e.g., `Heritage Ledger` instead of `Apple`)
2. **`description`** — preserve the aesthetic but rename to the user's brand voice
3. **One signature token** — typically the tertiary/accent color, or a typography weight pairing

**For deeper differentiation** (recommended for client work):
- Swap the body font (e.g., Inter → IBM Plex Sans) — same family weight but distinct character
- Adjust corner radius register (4px sharp → 12px friendly, or vice versa)
- Tighten or loosen the spacing scale
- Add or remove a color palette tier

### Step 4 — Update the markdown body

Don't just edit YAML and leave the prose pointing at the old brand. The `## Overview` and `## Colors` sections must be rewritten to match the new identity. The library prose is reference; the user's prose is canonical.

### Step 5 — Validate

```bash
python3 execution/design_md_validate.py <output_path>
```

Brand-library files are pre-linted and pass cleanly. If lint fails after your customization, you broke a token reference — review your edits.

### Step 6 — Write attribution comment

At the top of the markdown body, add:
```markdown
<!-- Customized from knowledge/design-libraries/brands/<brand_slug>/DESIGN.md (getdesign.md, MIT license) -->
```

## Customization Patterns

### "Apple but warmer"
- Source: `apple` (cool ink + clinical white)
- Swap `colors.canvas` from `#FFFFFF` to `#FAF7F2` (warm paper)
- Swap `colors.primary` from `#0066CC` (Action Blue) to a warmer accent like `#C2410C` (terracotta)
- Keep the typography (SF Pro is the signature)

### "Stripe but darker"
- Source: `stripe`
- Invert: swap `colors.canvas` to `#0F172A`, `colors.ink` to `#F8FAFC`
- Keep the gradient accent system but adjust contrast

### "Linear but with personality"
- Source: `linear-app` (precise, monochromatic)
- Add a single accent color (e.g., `#F59E0B` amber) for primary CTAs
- Add a display typography level with more character (e.g., a serif for headlines)

## Quality bar

A brand-imported DESIGN.md is acceptable when:
- Three or more elements are demonstrably different from the source
- The `## Overview` is rewritten in the user's voice (not just "Apple-inspired")
- Lint passes with 0 errors
- WCAG AA still holds after color customization

## See also

- [04-synthesize-from-brief.md](04-synthesize-from-brief.md) — when no brand fits, build fresh from a brief
- [knowledge/design-libraries/INDEX.md](../../../knowledge/design-libraries/INDEX.md) — full brand library index
