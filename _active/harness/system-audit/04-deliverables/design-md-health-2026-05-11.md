# DESIGN.md v2 — 14-Day Health Report

**Date**: 2026-05-11
**Integration commit**: f95fcc94 (2026-04-27)
**Check window**: 2026-04-27 → 2026-05-11 (14 days)

---

## Status: NEEDS_ATTENTION

Routing infrastructure is intact and lint is clean, but the validation log instrumentation never fired (`.agent/design-md-validations.jsonl` absent despite confirmed lint usage), and the standard routing integrity grep pattern for SLASH_COMMANDS.md underspecifies the full 10-workflow set — returning 6 of 10 matches rather than the expected ≥10.

---

## Real-Usage Signal: TRUE

Two project DESIGN.md files created post-integration via the Creative Director chain:

| Commit | Date | File | Notes |
|---|---|---|---|
| e5b346f | 2026-04-28 | `projects/farrice-brand/parallax-design-system/DESIGN.md` (270 lines) | Explicitly documented as "First real-world dogfood test of DESIGN.md v2 + product-design-build infrastructure." Full chain fired: design-md skill → product-design-build → Playwright preview. Lint-clean: 0 errors, 2 intentional contrast warnings. |
| fa9a1b0 | ~2026-04-29 | `extractions/andrea-dj/brand-operating-system/01-visual/DESIGN.md` (321 lines) | Andrea DJ brand OS, created via Creative Director brand-system-builder path. |

The skill files (`skills/design-md/`, `skills/product-design-build/`) and the Creative Director agent have no post-integration edits — only the initial f95fcc94 commit. This is expected; the infrastructure is consumed, not modified, during normal usage.

---

## Validation Log Summary

**File**: `.agent/design-md-validations.jsonl`
**Status**: Absent — file does not exist.
**Lint run count**: 0 logged.
**Error/warning trends**: No data.

The e5b346f commit message explicitly states lint was run ("lint-clean: 0 errors, 2 expected contrast warnings"), confirming that `npx @google/design.md lint` was invoked during the dogfood session. However, `execution/design_md_validate.py` did not write a JSONL entry. The instrumentation gap is the validate script: it runs the linter but never creates or appends to the log file.

---

## Lint Sample Results

5 brands sampled from `ls knowledge/design-libraries/brands/ | shuf -n 5`. Format per manifest noted.

| Brand | Format | Errors | Warnings | Exit | Notes |
|---|---|---|---|---|---|
| linear-app | legacy-prose | 0 | 1 | 0 ✅ | "No YAML content found" — expected for legacy-prose format |
| cursor | legacy-prose | 0 | 1 | 0 ✅ | Same as above |
| replicate | legacy-prose | 0 | 1 | 0 ✅ | Same as above |
| sentry | legacy-prose | 0 | 1 | 0 ✅ | Same as above |
| apple | spec-v1 | 0 | 7 | 0 ✅ | 7 unreferenced color tokens (`primary-focus`, `body`, `body-on-dark`, `body-muted`, `ink-muted-48`, `divider-soft`, `hairline`); 1 info (21 colors, 16 type scales, 7 rounding, 8 spacing, 24 components) |

**All 5 pass (exit 0).** No blocking errors across the sample.

**Format breakdown across full library** (58 brands):
- `spec-v1`: 9 brands — these have YAML structure; lint produces token-level warnings
- `legacy-prose`: 49 brands (84%) — these universally trigger "No YAML content found"; this is expected behavior, not a defect

The "No YAML content found" warning will fire on 49 of 58 brands in any lint batch. This isn't an error but creates noise that can obscure real warnings in aggregate reporting.

---

## Routing Integrity

| Check | Expected | Actual | Result |
|---|---|---|---|
| `grep -c 'design-md\|product-design-build' CLAUDE.md` | ≥5 | 5 | PASS ✅ |
| `grep -c 'design-md\|product-build' SLASH_COMMANDS.md` | ≥10 | 6 | FAIL ⚠️ |
| All 10 symlinks in `.agent/workflows/` resolve | All present | All 10 present and resolving | PASS ✅ |
| `ls knowledge/design-libraries/brands/ \| wc -l` | 58 | 58 | PASS ✅ |
| `manifest.json` entry count | 58 | 58 | PASS ✅ |

**SLASH_COMMANDS.md note**: The grep pattern `'design-md\|product-build'` matches only 6 of the 10 registered workflow commands. The 4 not captured — `/brand-library` (line 551), `/component-build` (line 553), `/preview-iterate` (line 554), `/design-system-deploy` (line 555) — are all present in SLASH_COMMANDS.md. The commands are there; the check pattern is underspecified. A broader grep confirms all 10 workflows are registered.

---

## Top 3 Recommended Improvements

### 1. Fix `execution/design_md_validate.py` to write the validation log

Lint was run during the e5b346f dogfood session but no entry was created in `.agent/design-md-validations.jsonl`. The file doesn't exist at all. Add a `log_result()` call at the end of `design_md_validate.py` that appends a JSONL record with:

```json
{"ts": "ISO-8601", "slug": "<brand-or-project>", "path": "<DESIGN.md path>", "errors": N, "warnings": N, "exit": 0}
```

Create the file on first write. This is the only change needed — the lint tool works, the log wire is just missing. Without it, the 14-day check will always show 0 logged runs regardless of actual usage.

### 2. Widen the routing integrity check pattern for SLASH_COMMANDS.md

The spec'd grep `'design-md\|product-build'` returns 6 of 10 commands and will always appear to fail the ≥10 threshold. Update the check (in this health report template, the CLAUDE.md quality-check notes, and any future automation) to:

```bash
grep -c 'design-md\|product-build\|brand-library\|component-build\|preview-iterate\|design-system-deploy' SLASH_COMMANDS.md
```

This returns 10, matching actual coverage. The fix is a one-line change to the check command — the underlying SLASH_COMMANDS.md registration is already correct and does not need editing.

### 3. Batch-convert the top 10 most-used brands from legacy-prose to spec-v1 YAML

49 of 58 brands (84%) are `legacy-prose` format and will fire "No YAML content found" on every lint call. This warning noise is benign individually but degrades aggregate reporting signal — if a real token error emerges in a batch run, it will be buried in 49 identical "No YAML" lines.

Priority brands to convert first (highest reference frequency in prompts, routes, and brand-library workflow examples): **linear**, **stripe**, **figma**, **notion**, **vercel**, **openai**, **github**, **anthropic**, **framer**, **shadcn**. Run `execution/design_md_extract.py --slug <slug>` to regenerate each as spec-v1 from the existing prose, then lint to confirm 0 errors. This is a ~2-hour batch job that upgrades the signal-to-noise ratio for all future lint runs.

---

## Appendix: Symlink Map (verified 2026-05-11)

```
.agent/workflows/brand-library.md       → skills/design-md/workflows/03-import-brand.md
.agent/workflows/component-build.md     → skills/product-design-build/workflows/01-component-build.md
.agent/workflows/design-md-evolve.md    → skills/design-md/workflows/07-evolve-design.md
.agent/workflows/design-md-export.md    → skills/design-md/workflows/06-export-and-handoff.md
.agent/workflows/design-md-extract.md   → skills/design-md/workflows/01-extract-from-url.md
.agent/workflows/design-md-synthesize.md → skills/design-md/workflows/04-synthesize-from-brief.md
.agent/workflows/design-md-validate.md  → skills/design-md/workflows/05-validate-and-refine.md
.agent/workflows/design-system-deploy.md → skills/product-design-build/workflows/04-design-system-deploy.md
.agent/workflows/preview-iterate.md     → skills/product-design-build/workflows/03-preview-iterate.md
.agent/workflows/product-build.md       → skills/product-design-build/workflows/02-page-build.md
```
