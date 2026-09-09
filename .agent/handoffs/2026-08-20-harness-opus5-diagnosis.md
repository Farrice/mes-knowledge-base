---
thread: harness-opus5-diagnosis
status: done
resume_hint: Live-fire the Intent Brief Default with one raw ask in a fresh session
unfinished: platform_compiler sync (Codex constitution); optional taste n=2 before 08-31
branch: main
pin: true
---

# System: Opus 5 Gap Diagnosis - Resolved, Defaults Installed

**Date:** 2026-08-20 · **Thread:** harness-opus5-diagnosis · **Status:** done (pushed to main @ d4e5879ff)

## What this session established

Farrice asked why his Opus 5 experience was "horrible" and how the 4.8→5 gap plays with the harness. Answered with measurement, not vibes:

1. **Mechanical re-probe (Fable seat, satisfies the opus card's independence caveat):** scope expansion reproduced (identical 2-sentence ask: Opus 9 tool calls/86s/2 takes vs Sonnet 0 calls/25s) but softer than July (no Notion write, no self-run Chain). Verbosity is largely HARNESS-amplified, not Opus-specific (Sonnet ~380w on a bare question too). Exact-count bounds now miss family-wide (both 43/40).
2. **Blind 3-seat taste A/B (LinkedIn post, identical brief + voice files):** Opus take = GREAT, Sonnet = GREAT, Fable = TERRIBLE ("no sentence rhythm"). n=1. Verdicts logged to voice_ratchet (60 total). **Conclusion: his Opus pain = interaction ergonomics, NOT artifact taste.**
3. **Seating ruling (written into the opus dialect card):** interactive front seat = Fable while available (to 2026-08-31), then Sonnet 5; Opus 5 = dispatched executor including creative drafting under the negative brief.
4. **Why Fable lost the blind test:** disposition mismatch — Fable compresses (briefing gait), Opus narrates (story gait); the dense-not-long register tuned for talking to Farrice bleeds into prose. Seat by disposition: conductor ≠ pen.

## What got built (all committed + pushed, main @ d4e5879ff)

- **Intent Brief Default** (plan-mode co-shaped, his 3 forks answered): `steering_loop_hook.py` — raw ask → INTENT BRIEF card (compile ≤10-line brief, confirm before producing); artifact-shaped ask → FRESH PEN card (never produce in-thread; fresh executor, seat per Executor Registry); sharp ask → one-line mirror and go; "just do it" skips confirm, never the fresh dispatch. Sabotage-tested 5 paths. Plan: `~/.claude/plans/i-don-t-know-i-recursive-eclipse.md`.
- **SessionStart digest**: `execution/hooks/session_brief.py` — 8 startup hooks → 3, one line per domain (his "infinite scroll" complaint).
- **Hookify noise diet**: 7 mention-based stop/warn rules disabled (fired on injected trigger words every session); 3 command-guards (fal/Notion/Perplexity) stay live.
- **Dialect cards**: opus card § Fable-Seat Re-probe (full findings + seating); **sonnet card got its missing machine-dialect block** (injector was silent for the post-08-31 conductor — verified firing now).
- **Memory**: `feedback_fresh-pen-protocol` (Intent Brief Default, BINDING), `feedback_no-mention-based-stop-warn-hooks`, `feedback_session-start-scroll-diet`, opus-dialect resolution addendum, co-creation addendum (system builds count as taste-bearing — scar: fresh-pen hook built without shaping, he corrected hard). MEMORY.md compacted 19.7→15.6KB.

## Next session focus (per Farrice)

1. **Live-fire the Intent Brief Default**: give a raw ask in a fresh session; the brief-confirm beat should appear before any production. If the beat feels wrong → reshape the injected card in `steering_loop_hook.py` (one-line change), not the doctrine.
2. **Codex constitution sync**: `python3 execution/platform_compiler.py check` shows CLAUDE.md drifted ahead of GEMINI.md + `.agent/rules/constitution.md`. Review the diff, then `python3 execution/platform_compiler.py sync`. Until synced, Codex sessions get the Intent Brief doctrine only via the memory file (the hook is Claude-Code-only).
3. **Optional, before 2026-08-31 (Fable window closes):** second blind taste pair on a Parallax passage → takes Opus-writes-great from n=1 to n=2. Re-use this session's method: identical brief + voice files, dispatch via Agent tool with model opus/sonnet/fable, present unlabeled, log verdicts to voice_ratchet.

## Artifacts / references (don't duplicate — read these)

- `directives/model-dialects/claude-opus-5.md` § Fable-Seat Re-probe — full probe data + seating ruling
- `directives/model-dialects/claude-sonnet-5.md` § Machine-Readable Dialect — new block
- `execution/hooks/steering_loop_hook.py` — INTENT BRIEF + FRESH PEN injection (search "2026-08-20")
- `execution/hooks/session_brief.py` — startup digest
- Blind takes B/C (rated GREAT) are in this session's transcript — Take B/C are one edit pass from a postable Cash Launch LinkedIn asset

## Suggested skills for next session

- `/resume harness-opus5-diagnosis` — reload this thread
- `voice-os` / `ghostwrite` — if shipping Take B or C as a real post
- `system-audit` — if the intent-brief beat misfires in live use

## Do NOT Rebuild (auto-scaffolded — the store adds this when a handoff omits it)
- (first handoff on this thread — list shipped assets here as they land)
- Before building anything named above: `/arsenal <task>` and read the prior handoff first. Re-solving shipped work is the #1 next-session failure mode.
