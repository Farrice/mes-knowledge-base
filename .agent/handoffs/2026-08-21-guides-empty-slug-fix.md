---
thread: guides-empty-slug-fix
status: done
resume_hint: Closeout spine ready to run; guides fix merged to main at 125da18b5
unfinished: None — this work is complete
branch: main
pin: true
---

# System: Guides Stub Fix - Merged and Verified

## Summary

Fixed critical bug in `execution/end_session_closeout.py` where empty session slugs produced filenames like `guides/YYYY-MM-DD-.md` instead of proper kebab-case slugs. The fix implements a safe fallback chain: sanitize passed slug → derive from title → use "unnamed-session" sentinel. All changes committed and merged to main.

## What Was Completed

**Merged Commits:**
- `125da18b5`: "fix(closeout): guides stub never gets a blank filename…" — complete fix with test harness
- Fixed `step_session_guide()` in execution/end_session_closeout.py (lines 673-681) with slug fallback logic
- Changed regex from `r"[^a-z0-9-]+"` to `r"[^a-z0-9]+"` to collapse consecutive hyphens correctly
- Renamed orphan stub `guides/2026-08-20-.md` → `guides/2026-08-20-system-opus-5-gap-diagnosis-resolved-defaults-installed.md`
- Updated guides/INDEX.md reference (line 59)
- Created test harness to verify three cases: empty slug + title, empty slug + no title, normal slug

**Verification:**
- All test cases passed
- No regressions in existing guide generation
- Main branch is clean and ready

## Current State

- Branch: main (clean)
- Last commit: 125da18b5 (merged)
- No uncommitted changes
- Guides directory properly organized with correct filenames

## Next Session Focus

Run the full end-session closeout spine per `.agent/workflows/end-session.md`:

1. Run `/handoff` skill (already done in this handoff)
2. Save handoff via `handoff_store.py save` with thread slug `guides-empty-slug-fix`
3. Run closeout spine: `python3 execution/end_session_closeout.py run --slug "guides-empty-slug-fix" --handoff "<path>" --git-policy legacy`
4. Generate insightful momentum follow-ups via `contextual_next_prompts.py`
5. Update conversation index

Thread status should be: `done` (this work is complete)

## Files Changed

- `execution/end_session_closeout.py` — slug fallback logic added
- `guides/2026-08-20-system-opus-5-gap-diagnosis-resolved-defaults-installed.md` — renamed from blank slug version
- `guides/INDEX.md` — reference updated

## Hot Experts This Session

- system-ops (execution/system primitives and closeout spine maintenance)

## Suggested Skills

- `handoff` — already invoked; next session uses for momentum routing
- No additional skills required for closeout; all Python scripts are deterministic

---

**Ready for:** Closeout spine completion + momentum prompts generation

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
