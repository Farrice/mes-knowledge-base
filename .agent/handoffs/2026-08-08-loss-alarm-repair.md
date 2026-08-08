---
thread: loss-alarm-repair
status: ready
resume_hint: Fix citation_integrity.py ~/ expansion + template exclusion, and EMPTY-ABSORB merge-commit baseline
unfinished: 383 MOVED citations unrepointed; patrick-debois-cdlc missing execution layer; character-sheets lane unmerged
branch: main
pin: true
---

# Ops: Loss-Alarm False Positives — Audited, Repair Specced

## Purpose
- **Next session should do:** Fix the two scanner defects that manufacture ~180 false "loss" signals per session open — `citation_integrity.py` (`~/` path mangling + template example-path exclusion) and `divergence_alarm_hook.py` (`_detect_empty_absorbs` compares against current HEAD instead of the merge commit).
- **Not in scope:** Repointing the 383 MOVED citations (do that *after* the scanner is fixed, or you'll repoint noise). Building the missing `patrick-debois-cdlc` execution layer. Merging `worktree-farrice-character-sheets` (blocked on a live concurrent session, not on code).

## Load First
- `execution/citation_integrity.py` — the 565-pointer scanner. Defects are in path normalization and the absence of a template-exclusion rule.
- `execution/hooks/divergence_alarm_hook.py` — `_detect_empty_absorbs()` at line ~54. The bug is line ~74: it checks `{baseline}:{f}` against current main, so any later legitimate move re-flags a cleanly-merged file.
- `docs/solutions/2026-07-13-divergent-branch-work-silently-lost.md` — the real loss class both alarms exist to catch. Do not weaken detection of *that*; only remove the false-positive classes.
- `_active/_archive/MOVED.md` — the arena-sweep manifest; explains why 103 of 104 EMPTY-ABSORB flags are moves.

## Current State

**Objective:** Make the session-open loss alarms trustworthy. Right now they cry wolf at ~100% false-positive rate, which trains the operator to ignore a genuine loss signal.

**What is already done (this session):**
- Working tree cleared: 28 files committed + pushed to `origin/main` (content vault drafts, health-performance daily cuts + ledgers, LinkedIn context-OS maps, recurring reports archived).
- Full forensic audit of both alarms. **Verdict: 0 confirmed content losses out of 669 flags.**
  - 104 EMPTY-ABSORB files → 60 MOVED byte-identical, 43 MOVED content-evolved, 1 renamed (`MOVED-2026-08-07.md` → `MOVED.md`, per LIVING-vs-RECORD doctrine). Comparing branch-created files against the *merge commits* directly: **0 dropped, all four merges absorbed cleanly.**
  - 565 citations → 413 MOVED, 106 PHANTOM, 27 RUNTIME, 19 DELETED. All 19 DELETED verified as intentional restructures (12 = `riley-brown-marketing-automation` workflow renames in the v2 forge rebuild; rest = a prompt migration + a deleted E2E probe).
- Diagnosed why Fable 5 is absent from the VS Code extension: the extension ships its **own** pinned `claude` binary (`resources/native-binary/claude`, v2.1.156, **0** hits for `claude-fable-5`) while the PATH CLI is v2.1.220 (**32** hits). Not a plan/entitlement issue, not the ZDR restriction. No `executablePath` setting exists — fix is updating the extension.

**What is uncertain or stale:**
- `.agent/session-state.md` and `.agent/intent-memory/current.json` are both from *other* sessions (Elizabeth Stone extraction; eightward from 2026-07-04). Do not treat either as this thread's state.
- `worktree-farrice-character-sheets` is 4 commits ahead and unmerged — blocked by live session `ca6d17f0` writing to main (watched `.agent/perplexity-usage.json` tick 266→268 mid-audit). Retry when quiet: `python3 execution/worktree_lane.py merge --lane worktree-farrice-character-sheets`
- `codex/expert-practice-os-v2-architecture` has 43 uncommitted files — **Codex is live in there.** Left untouched deliberately.

**Latest proof/receipt:** `origin/main` = `f980c2fd1`, working tree clean, 0 unpushed at close.

## The Four Fixes (specced, not applied)

1. **`~/` mangling** — `citation_integrity.py` strips the `~/.` prefix, turning `~/.agents/.skill-lock.json` into `agents/.skill-lock.json` and reporting it missing. The real file exists (17KB, modified Aug 7). This is the **only BINDING-tier finding**, and it is false. Expand `~` before the existence check.
2. **Template example-paths counted as citations** — 61 of 106 phantoms live inside `skills/*/references/prompts*/` and `_legacy-prompts/`, where paths like `ROSTER-YYYY-MM-DD.md`, `products/catalog.md`, `deliverables/carousel_scripts/YOUR_FILE.md` are *illustrations inside extracted expert prompts*, not pointers. Exclude those dirs, or skip paths matching placeholder syntax.
3. **`_legacy-prompts/` double-counting** — 28 pointers are exact duplicates of the adjacent `prompts/` dir. Exclude the legacy mirror from the scan.
4. **EMPTY-ABSORB baseline** — `_detect_empty_absorbs()` must compare branch-created files against the **merge commit's tree**, not current `main`. As written, the 2026-08-07 arena sweep (`43ebc4014`, 66 folders → 10 arenas) re-flags every prior merge in the 14-day window. Any future reorg will do the same.

Fixes 1–3 drop 565 → roughly 420. Fix 4 drops the EMPTY-ABSORB block to silent.

## Genuine findings worth acting on separately
- **`skills/patrick-debois-cdlc/` is non-operational.** Four of its workflows cite ten execution scripts that were never built: `skill_security_scan.py`, `skill_versions.py`, `skill_dependencies.py`, `observability_scanner.py`, `context_filter.py`, plus `evolution_store/observability/*.jsonl`. Decide: build the layer, or mark the workflows non-operational.
- Small dangling refs: `skills/nba-betting-edge/genius.md` → `execution/perplexity.py` (real path is `research.py`); `guides/2026-07-26-opus-5-dialect.md` → `execution/jsonl_surgery.py`; `.agent/workflows/roth-content.md` → two missing `eric-roth-writing-mastery` workflows.
- **Filing bug:** `guides/2026-07-24-.md` has an empty slug and a blank `session:` frontmatter field. Something wrote a guide with no title; it's also the noisiest stale citer (12 of the 19 DELETED pointers).
- **Doctrine note:** 65 of the 565 pointers live in dated RECORD files (handoffs, `guides/2026-*`). Per LIVING-vs-RECORD these are session receipts, never truth — **do not repoint them.** Only the 500 in LIVING docs are candidates.

## Do NOT Rebuild
- **The audit itself is done — do not re-run the forensic classification.** 669 flags were classified against git history this session; the verdict (0 losses) and the four fixes are recorded above. Re-deriving it costs a session and changes nothing.
- `citation_integrity.py` and `divergence_alarm_hook.py` both exist and work — **patch them, never rewrite.** The detection logic for the real loss class is correct; only the baselines and exclusions are wrong.
- Before building anything named above: `/arsenal <task>` and read this handoff first. Re-solving shipped work is the #1 next-session failure mode.

## Remaining priority
Patch `execution/citation_integrity.py` (`~` expansion + prompt-template/`_legacy-prompts` exclusion) and `execution/hooks/divergence_alarm_hook.py` (`_detect_empty_absorbs` → compare against the merge commit's tree, not current HEAD). Then rerun the scanner and show the remaining ~420 before repointing anything.

## Suggested Skills / Workflows
- `/self-heal` — after the scanner fix, rerun to confirm the count drops and nothing real got suppressed.
- `/arsenal citation integrity` — check before writing any new scanner logic; extend, never rebuild.
- `/extract-approach` — the "alarm measures against the wrong baseline" pattern is card-worthy once fixed.

## Exact Next Prompt
```text
Fix the two loss-alarm scanners so they stop manufacturing false positives, then verify.

1. execution/citation_integrity.py — (a) expand `~` before the existence check (currently
   mangles ~/.agents/.skill-lock.json into agents/.skill-lock.json and reports the only
   BINDING-tier finding, falsely); (b) exclude skills/*/references/prompts*/ ,
   prompts-v2/ and _legacy-prompts/ from scanning — 61 of 106 phantoms are illustrative
   example paths inside extracted expert prompts, and _legacy-prompts is a duplicate
   mirror adding 28 more.

2. execution/hooks/divergence_alarm_hook.py — _detect_empty_absorbs() currently checks
   branch-created files against CURRENT main HEAD, so any later legitimate move re-flags
   a cleanly-merged file. Compare against the merge commit's own tree instead. Verified:
   all 4 flagged merges absorbed 0 dropped files when compared correctly.

Do NOT weaken detection of the real loss class in
docs/solutions/2026-07-13-divergent-branch-work-silently-lost.md — only remove the
false-positive classes above.

Then run `python3 execution/citation_integrity.py` and confirm the count drops from 565
to roughly 420, and that the EMPTY-ABSORB block goes silent. Show me what the remaining
~420 are before repointing anything.
```

## Acceptance Criteria
- `python3 execution/citation_integrity.py` reports ~420, not 565, with **zero** BINDING-tier findings.
- `~/.agents/.skill-lock.json` no longer appears as missing.
- Session-open EMPTY-ABSORB block is silent, and re-running the merge-commit comparison on `43ebc4014 / 06b5e1b29 / ae3c7d8b2 / c9678c4e9` still yields 0 dropped.
- A deliberately unmerged branch with real content still alarms (don't break the detector proving it works).

## Risk Notes
- **Do not over-suppress.** These alarms exist because a June 2026 session's work sat unmerged for three weeks while memory cited it as live. The fix is a better baseline, not a lower sensitivity.
- **Concurrent writers.** 2–3 sessions have been active on main this whole session; `.agent/perplexity-usage.json` churns constantly. Claim the session lock before multi-file work, or the lane merge gate will refuse.
- Nothing in this thread requires paid API calls — the entire audit was local git + strings. $0.
