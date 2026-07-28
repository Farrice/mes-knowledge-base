# Latest Handoff

**Thread:** opus5-adaptation-layer  
**Full path:** .agent/handoffs/2026-07-28-opus5-adaptation-layer.md  
**Date:** 2026-07-28 (today)  
**Status:** active  
**Title:** Opus 5 Adaptation Layer — Model-Dialect Resilience (Fable seat)

> Not auto-loaded. Run `/resume` to choose any thread, or `/resume opus5-adaptation-layer` for this one.

---

# Opus 5 Adaptation Layer — Model-Dialect Resilience (Fable seat)

**Thread:** opus5-adaptation · **From session:** a919a6cd (2026-07-27→28, Opus 5 seat)
**Next seat:** Fable 5 — conductor-grade, per orchestration-doctrine Ladder.

## The mission for the next session

Design the harness layer that survives model releases — so a model swap (4.8→5, 5→next)
never again means weeks of repair mode. Two halves:

1. **Model-dialect adaptation as MECHANISM, not prose.** The dialect rules live in
   CLAUDE.md § Model Dialect — the channel proven dead three times this week (PARTNER
   dial: 11 days, 0 fires; dialect block: prose; failure registry: 115 days empty).
   The proposed-but-unbuilt piece: a **per-prompt bound injector** in
   `steering_loop_hook.py` that attaches what Opus 5 won't infer — word ceiling, scope
   ceiling, delegation cap, negative subagent brief — derived from the ask, silent,
   same channel as the Step 0 injection that demonstrably fires every exchange.
   Evidence base: `directives/model-dialects/claude-opus-5.md` (P2/P6 verbosity,
   P9 scope explosion, over-delegation).

2. **Wired-vs-built audit loop.** Farrice: "we're missing a lot of hooks and certain
   loops... building assets that aren't actually wired to anything." Measured instances
   this session: /aar 0 uses ever → registry empty 115 days; verify fleet red since
   Sunday, unseen; 13 sessions produced deliverables with 0 skill loads. Prior card:
   docs/solutions/2026-07-21-wired-but-never-loaded-prompts.md. The pattern class:
   **an asset is real only when a hook, cron, or spine step fires it.** Candidate
   build: a "dead-channel detector" — for every built asset, prove a firing path
   exists (hook/launchd/spine/explicit command with usage>0), else flag it.

## What already shipped (do NOT rebuild — extend)

All verified 2026-07-28, all uncommitted in the working tree, 102 checks green:

| Layer | Files | State |
|---|---|---|
| Execution Receipt (what actually ran) | `execution/execution_receipt.py`, manifest capture in `execution/hooks/session_ledger_hook.py` | 34/34 checks |
| Self-Heal (AUTO/EVIDENCE/JUDGMENT) | `execution/self_heal.py` | 38/38, scoped auto-commit, never `git add -A` |
| Anti-repeat learner | `execution/failure_learning.py` → `evolution_store/failure-registry.md` (canonical; plugin path is mirror) | 30/30, thresholds pinned 3/5/5/7 |
| Session-close heal (PRIMARY path) | `end_session_closeout.py` `step_self_heal` before `commit-gate`; 06:45 cos-prep demoted to `report` | dry-run verified |
| Session-open surface | `execution/hooks/pending_decisions_hook.py` (SessionStart, 0.04s, silent when clean) | registered in .claude/settings.json |
| Command surfaces | `.agent/workflows/self-heal.md`; weekly-closeout Step 1.5 rewritten; aar.md+solo.md repointed | done |
| Handoff store: near-dup threads AUTO-ADOPT (`--new-thread` to force separate); missing Do-NOT-Rebuild section auto-scaffolded into the body | `execution/handoff_store.py` cmd_save | live-tested both paths; NO verifier suite yet — worth adding |

## Open JUDGMENT items (surfaced by pending_decisions_hook at your next session open)

- `generate_slash_commands.py` generator bug — `--check` reports 2,398 to append, `main()` writes ~6 lines; 817 workflows missing from SLASH_COMMANDS.md
- Router ranking degradation — corpus grew to 3,186 commands; 3 verifiers fail on /steering-compass not ranking top-3; fix is `routing: long-tail` demotion (taste call)
- `platform_compiler` drift ×2 — classify-only by decision; auto-write deferred until healer has a week of runs
- 6 fleet verifiers exceed the 90s budget (perf, not correctness)
- 2 citation-integrity broken pointers incl. `execution/jsonl_surgery.py` — never committed anywhere, genuine lost work

## Hard-won lessons (cost real debugging this session — carry them)

1. **Prose is not a mechanism.** Only hooks, launchd, and spine steps fire. Every dead channel this week was a rule written where nothing executes.
2. **A test that reads the constant it tests cannot detect that constant changing.** Pin thresholds; hardcode probe counts. (NC-A escaped detection.)
3. **String-matching source produces false REDs** — tripped 3× on docstrings/comments/variable names documenting the very hazard. Parse the AST.
4. **First plausible root cause is often wrong.** Re-introduce the alleged cause; if the test still passes, the diagnosis is wrong (DELIVERABLE_ROOTS bug).
5. **Verify claims from subagents** — the Explore agent's fleet-timeout claim was false (real secs: 0.8s/1.2s); its double-sync claim overstated.
6. Solution Cards: `2026-07-27-verification-with-no-reader.md`, `2026-07-27-every-failure-defaults-to-the-human.md`

## First safe actions for the Fable session

1. `git status` — session-close spine should have committed this work; if not, review diff and commit.
2. Read the two Solution Cards + `directives/model-dialects/claude-opus-5.md` before designing.
3. Then design the bound injector + dead-channel detector as ONE coherent layer, not two bolt-ons.

