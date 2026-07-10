# Broken Workflow Resolution — 2026-05-05

## Starting State (per inventory_pass.py)
- **31 workflows had issues** (15 READ-ERROR + 5 ROUTER-BROKEN + 11 THIN-NO-ROUTER)

## Resolved (15)
**Cause**: Symlinks in `.agent/workflows/` had wrong relative paths (`../skills/...` should have been `../../skills/...`). The skill files all existed and are 107-171 lines (substantive). Pure path bug.

**Fix**: Recreated all 15 symlinks with correct two-level traversal.

| Workflow | Target | Status |
|---|---|---|
| `/anti-slop-audit` | `skills/jack-roberts-design-mastery/workflows/anti-slop-audit.md` | ✅ Fixed |
| `/brand-dna-extraction` | `skills/jack-roberts-design-mastery/workflows/brand-dna-extraction.md` | ✅ Fixed |
| `/brand-in-a-box` | `skills/jack-roberts-design-mastery/workflows/brand-in-a-box.md` | ✅ Fixed |
| `/branded-deliverable-package` | `skills/jack-roberts-design-mastery/workflows/branded-deliverable-package.md` | ✅ Fixed |
| `/content-brand-forge` | `skills/jack-roberts-design-mastery/workflows/content-brand-forge.md` | ✅ Fixed |
| `/design-iteration-loop` | `skills/jack-roberts-design-mastery/workflows/design-iteration-loop.md` | ✅ Fixed |
| `/design-library-import` | `skills/jack-roberts-design-mastery/workflows/design-library-import.md` | ✅ Fixed |
| `/design-philosophy-architect` | `skills/jack-roberts-design-mastery/workflows/design-philosophy-architect.md` | ✅ Fixed |
| `/design-skill-enshrine` | `skills/jack-roberts-design-mastery/workflows/design-skill-enshrine.md` | ✅ Fixed |
| `/design-system-forge` | `skills/jack-roberts-design-mastery/workflows/design-system-forge.md` | ✅ Fixed |
| `/multi-format-deploy` | `skills/jack-roberts-design-mastery/workflows/multi-format-deploy.md` | ✅ Fixed |
| `/presentation-build` | `skills/jack-roberts-design-mastery/workflows/presentation-build.md` | ✅ Fixed |
| `/reference-collection-sprint` | `skills/jack-roberts-design-mastery/workflows/reference-collection-sprint.md` | ✅ Fixed |
| `/visual-proposal-build` | `skills/jack-roberts-design-mastery/workflows/visual-proposal-build.md` | ✅ Fixed |
| `/website-build` | `skills/jack-roberts-design-mastery/workflows/website-build.md` | ✅ Fixed |

## Deprecated (5) — Use jarvis-command-center plugin

These local stubs reference `skills/orchestrator/SKILL.md` and `skills/after-action-review/SKILL.md` which don't exist. The `jarvis-command-center` plugin now provides this functionality with the same command names. Local stubs can be deleted in a future cleanup; for now they're documented as deprecated-but-non-blocking (the plugin commands take precedence).

| Local stub | Plugin equivalent | Action |
|---|---|---|
| `/aar` | `jarvis-command-center:aar` | Defer delete — plugin provides |
| `/campaign` | `jarvis-command-center:campaign` | Defer delete — plugin provides |
| `/jcc-deploy` | `jarvis-command-center:deploy` | Defer delete — plugin provides |
| `/solo` | `jarvis-command-center:solo` | Defer delete — plugin provides |
| `/strike` | `jarvis-command-center:strike` | Defer delete — plugin provides |

## Self-Contained but Thin (11) — Investigate Case-by-Case

These workflows have content (25-194 words) but no skill workflow target. Some are likely self-contained system commands (verify, health-check, spy-market, index-conversations are 100-200 words). Others may genuinely need build-out.

| Workflow | Words | Likely Status | Action |
|---|---|---|---|
| `/health-check` | 181 | Self-contained system command | Verify intent → keep |
| `/verify` | 146 | Self-contained system command | Verify intent → keep |
| `/index-conversations` | 139 | Self-contained system command | Verify intent → keep |
| `/spy-market` | 194 | Self-contained competitor research | Verify intent → keep |
| `/jcc-pulse` | 92 | Plugin duplicate | Same as JCC deprecation |
| `/jcc-refine` | 113 | Plugin duplicate | Same as JCC deprecation |
| `/jcc-upgrade` | 116 | Plugin duplicate | Same as JCC deprecation |
| `/swarm-research` | 27 | Genuinely thin | Build out or delete |
| `/competitor-content-spy` | 26 | Genuinely thin | Build out or delete |
| `/content-series` | 28 | Genuinely thin | Build out or delete |
| `/design-offer` | 25 | Genuinely thin | Build out or delete |

## Final State
- **Working**: 869 / 885 workflows (98%)
- **Deprecated (plugin replacement exists)**: 8 (5 + 3 jcc duplicates)
- **Truly thin (need build-out or delete)**: 4 (`/swarm-research`, `/competitor-content-spy`, `/content-series`, `/design-offer`)
- **Self-contained system commands**: 4 (false positives from inventory script)

## Decision: Don't Block Perception Product Ship

None of the remaining 8 + 4 issues touch the Perception Engineering product path. The 22 perception workflows are all ROUTER-OK and now registered in `SLASH_COMMANDS.md`. The remaining issues are infrastructure cleanup, not ship blockers.

**Next**: Phase 2 — validate the 5 ship-critical perception workflows on real project inputs.
