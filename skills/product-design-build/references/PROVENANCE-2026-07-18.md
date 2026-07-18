# Provenance — product-design-build repair (Wave 3 Lane 4 Batch 14)

No `extractions/` directory exists for this skill — it is a method/tool skill (DESIGN.md → UI codegen), not a persona extraction. Ground truth = live technical documentation for the libraries/standards this skill wires together, plus this skill's own pre-existing files (verified by direct read, not re-derived).

| Anchor (as it appears in genius.md / workflows) | Source | Location | Label |
|---|---|---|---|
| "Class Variance Authority," typed variant API | github.com/joe-bell/cva | Repo description, fetched 2026-07-18 | VERIFIED |
| "Focus is automatically trapped within modal" / "Esc closes the component automatically" / focus → `Dialog.Trigger` | radix-ui.com/primitives/docs/components/dialog | Dialog docs, fetched 2026-07-18 | VERIFIED |
| WCAG 2.2 SC 1.4.11 — "a contrast ratio of at least 3:1 against adjacent color(s)" | w3.org/WAI/WCAG21/Understanding/non-text-contrast.html | Understanding doc, fetched 2026-07-18 | VERIFIED |
| `hover:` → `@media (hover: hover)`; `pointer-coarse:` targets touchscreen | tailwindcss.com/docs/hover-focus-and-other-states | Docs page, fetched 2026-07-18 | VERIFIED |
| axe-core — "Accessibility engine for automated Web UI testing" | github.com/dequelabs/axe-core | Repo description, fetched 2026-07-18 | VERIFIED |
| "code reading is unreliable for visual work; always render" | `skills/product-design-build/workflows/03-preview-iterate.md` | Anti-patterns section (pre-existing, unchanged) | VERIFIED — read directly |
| `refactored: 2026-07-13` | `skills/product-design-build/references/prompts-v2/component-build.md` | YAML frontmatter (pre-existing, unchanged) | VERIFIED — read directly |
| "`rounded.md` corners (8px in Heritage example)" | `skills/product-design-build/workflows/03-preview-iterate.md` | Critique table, line 113 (pre-existing, unchanged) | VERIFIED — read directly; the underlying "Heritage" DESIGN.md itself is not in this repo, so the 8px figure is this skill's own prior internal claim, carried forward, not independently re-derived |
| CVA vs. styled-components/Emotion vs. tw-classed tradeoffs | Pre-existing genius.md text | Section "Why CVA over alternatives" (carried forward) | LIKELY — general ecosystem knowledge, not re-fetched from one primary source this pass |
| Tailwind v4 `@theme` block compatible with `theme.extend` wiring | General Tailwind v4 migration knowledge | Not independently re-fetched this pass | LIKELY |
| Style Dictionary `ios-swift` transform group | Pre-existing genius.md text | Section 7, SwiftUI bridge (carried forward) | LIKELY |
| `@google/design.md` CLI itself (`lint`, `export --format tailwind\|dtcg`) | Pre-existing skill convention, no external listing fetched | Used throughout genius.md and workflows/*.md (pre-existing) | UNCONFIRMED as external package; treated as this skill's own internal convention, not upgraded |
| Sample hex tokens (`#1A1C1E` etc.) in Token → Tailwind Mapping example | Pre-existing genius.md text | Section 2 | Explicitly illustrative, not sourced as a real brand's tokens anywhere in the text |

Full claim-by-claim detail: [references/source-ledger.md](references/source-ledger.md).
