# design-sync notes — @farrice/premium-minimal

Repo-specific gotchas for future syncs. Read this before anything else.

## What this package is

A React library built to the approved **P2-01 Premium Minimal V1** design contract at `../package/02-DESIGN-CONTRACT.md`. The contract is the source of truth; this library is its executable form. **If the contract changes, change the library — never the reverse.** Token values in `src/premium-minimal.css` are copied verbatim from `../package/tokens/design-tokens.css`.

## Build

- `npm run build` runs `tsc` and then copies `src/premium-minimal.css` plus two guideline docs into `dist/`. There is no bundler — `dist/index.js` is plain ESM from tsc, and the converter's esbuild handles bundling.
- `dist/guidelines/*.md` is **generated on every build** by copying `../package/02-DESIGN-CONTRACT.md` and `../package/01-BRAND-FOUNDATION.md`. This is deliberate: it means the uploaded guidelines can never drift from the canonical package. Don't hand-edit anything in `dist/`.
- Converter invocation needs `--entry ./dist/index.js` (the package isn't installed into its own `node_modules`).

## Decisions recorded

- **Font substitution — approved by Farrice, 2026-08-29.** The contract specifies Helvetica Neue only and says an asset stays in `review` if it's unavailable. Claude Design renders in a browser where Helvetica Neue is Mac-only, so the bundle ships the contract's own fallback chain (Helvetica Neue → Helvetica → Arial → sans-serif). Non-Mac viewers get Arial. This is a **screen-work-only** deviation and it is stated in `conventions.md`. It does not authorize any other font, and it does not apply to produced assets (SVG/PPTX), which still require real Helvetica Neue.
- **All twelve components get `cardMode: "column"`.** Every preview cell is a full design surface, not a small widget. Side-by-side cells clipped at the card edge and shrank the type past legibility. Column mode gives one export per row at full card width. Don't remove this.
- **Preview scope: all twelve authored.** No floor cards. The library is small enough that floor cards would have been a weak first look.

## Known render warns

None. The final validate run was fully clean: 12/12 previews render, no `[FONT_MISSING]`, no `[TOKENS_MISSING]`, no `[GRID_OVERFLOW]`. **Any warn on a future run is new** — look at it, then fix it or record it here.

## Gotchas hit during the first sync

- **`Surface size="feed"` overflows its capture frame at full card width.** The 1080×1350 aspect at ~700px wide renders ~875px tall, and content anchored to the bottom with a `flex: 1` spacer falls below the visible cell. The render check passes (the text is in the DOM) so nothing flags it — it only shows up by eye on the review sheet. Fix used: wrap the preview in `<div style={{ maxWidth: 420 }}>`. **Any future preview using `feed` or `carousel` needs the same wrapper.**
- Components use `cqw` units for type sizing, which resolve against `Surface`'s `container-type: inline-size`. **Every preview must be wrapped in a `Surface`** or type renders at viewport scale and blows out the card. This is also true for real designs, and `conventions.md` says so.

## Tidy for next sync (cosmetic, not broken)

The guidelines land at `guidelines/dist/guidelines/design-contract.md` — the converter preserves the glob's directory path, and `cfg.guidelinesGlob` points at `dist/guidelines/*.md`. Content and reachability are correct; the path just reads badly in the project tree. Fixing it means copying the guideline docs to a shallower build output and re-pointing the glob, then a full driver rebuild and re-upload. Untested — verify the emitted path actually flattens before assuming a shallower glob fixes it.

## Re-sync risks

- **Contract drift.** `dist/guidelines/` regenerates from `../package/`, so guideline content self-heals. But `src/premium-minimal.css` token values are a **manual copy** of `../package/tokens/design-tokens.css`. If that file changes, nothing detects it. Diff the two before any re-sync that follows a contract revision.
- **`conventions.md` names real things.** It enumerates twelve component names, seven colour tokens, the spacing scale, and three rule widths. All verified against the build as of 2026-08-29. Re-validate every name after any rename — a conventions file that names something that no longer exists is worse than no file, because the design agent will trust it and emit vocabulary that silently doesn't resolve.
- **Playwright was installed fresh for this run** (chromium-headless-shell 1234, `~/Library/Caches/ms-playwright/`). A future run on a different machine needs it again.
- **Only screen rendering was verified.** Nothing here was checked as a produced asset at native pixel dimensions — no 1584×396 export, no PPTX, no print. The `Surface` padding maths is proportional and should hold, but it has not been proven against a real export.
- **The Parallax design system is a separate project and must stay separate.** Mixing the two in one Claude Design project would let the design agent blend Parallax editorial styling into Premium Minimal work.
