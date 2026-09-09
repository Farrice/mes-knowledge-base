---
thread: homebase-librarian
status: done
resume_hint: Re-auth claude CLI (60s), then send-week: teardowns, claim-check launch, offer-fork decision — use the system, don't build
unfinished: CLI re-auth (his), send-week execution; system itself has no build debt
branch: main
pin: true
---

# System: Homebase + Ambient Librarian - Shipped and Verified

## Purpose

Next session should do: **use the system, don't build.** One 60-second unlock
(re-auth the `claude` CLI in any terminal — just run `claude`, log in, close),
then act on the librarian's standing calls. Every surface, hook, and nightly
job shipped 2026-08-20 is complete, E2E-verified, committed, and pushed to
main (`402731f85`).

Not in scope: rebuilding or extending the Readout OS surfaces. The analyst's
own portfolio read is binding context: *"the portfolio has a release
constraint, not a production constraint — five finished cash assets each
waiting on one human act."*

## Load First

- `guides/2026-08-06-readout-os.md` — the operator guide; the "If you only read 10 lines" block now covers Homebase, the two-surfaces collapse, deep mission pages, and the Library.
- `.agent/workflows/homebase.md` + `.agent/workflows/catalog.md` — operator cards for the two commands (`/homebase`, `/catalog` — both minted and fireable).
- `docs/solutions/2026-08-06-live-local-board-pattern.md` — the binding pattern any new surface must follow (writers-first CLI → server → dual-mode JS).
- `.agent/sweep/synthesis.json` + `.agent/catalog/triage.json` — the current judged layer (authored in-session 2026-08-20, validated fail-closed).

## Current State

**What is done (all verified, all on main):**
- **The Homebase** at `http://127.0.0.1:8765/` — the one ACT surface: Focus (sprint + money line + needs-you with analyst read-lines) · Launch (merged thread cards: why-needs-you, resume/context/brief/done/park/kill) · Library zone (Worth-Resuming strip, briefs, dark asset shelf) · collapsed Outcomes-due/Recently-closed. Server always-on via launchd `com.antigravity.pulse-serve`.
- **Two-surfaces collapse** — Pulse + Mission Control retired (`/pulse`, `/missions` → 302 to `/`); Briefing Room is the READ surface; generators survive as libraries (`pulse_dashboard.py --open` still feeds hooks).
- **Deep mission pages** — every mission brief mines its handoff body (Purpose/Current State/Exact Next Prompt/risks), finalize notes, outcomes+verdicts, asset prompts, contract, on-page context pack, live resume/park/kill buttons. `kill` = dead+hidden (new verb); park no longer ranks urgent (was a real bug).
- **The Library** at `/library` — permanent catalog (~1,000 rows: sweep census beyond the 14-day window + deliverables/extractions/knowledge/guides/solutions/briefs), Worth-Resuming shelf, tag facets, search, triage chips, Graveyard. `work_catalog.py find "<half-remembered>"` works; also a memory_facade source (`--sources catalog`).
- **Ambient filing (both harnesses)** — Stop hook files every session's work in the catalog and asks ONCE for a 3-line narrative handoff (single-fire, receipt-keyed, loop-guard proven). Nightly 02:45 sweep chains catalog merge + brief rebuild + all-surface regen. Sundays 07:00 the Shelf Report renders into the Room (`com.antigravity.shelf-report`).
- **Critical fix proven:** the old nightly script MOVED synthesis.json aside every night (with the dead CLI it would have destroyed the judged layer nightly). Rewritten to `brief_synthesis.py` restore-not-discard; survival proven by md5-identical synthesis through a full dead-CLI nightly run.

**What is uncertain / degraded (honest):**
- `claude -p` OAuth is EXPIRED → nightly analyst synthesis + librarian triage run in degraded mode (last valid judged layer kept, age surfaced on briefs as a caveat at 3+ days). Farrice's one-time re-auth unlocks them.
- Current judged layer was authored in-session 2026-08-20 by Fable (validated through the same fail-closed contract); it ages until the nightly judge runs.
- A sibling session is fixing the empty-slug closeout-stub filename (task chip `task_a4a663eb`, lane `worktree-guides-empty-slug-fix`).

**Latest proof/receipts:**
- E2E matrix (all passed): routes 200/302/404/403 as designed incl. `.env` denial; nav 5/5 labels on every surface; action-wire negatives (unknown action, bad content-type, cross-origin, reasonless kill all refused); kill/park/reopen roundtrips through the exact button wire; Stop-hook synthetic fires (block-once, loop-guard, no-writes-no-fire); nightly chain dry-run receipt `.agent/health/session-sweep.json` (`synthesis_degraded` + `synthesized: true`).
- Git: main == origin/main at `402731f85`, tree clean.

## Remaining Priority

1. **Re-auth `claude` CLI** (Farrice, 60s) → nightly judge self-activates.
2. **Act on the librarian's calls** (all sitting finished): send the three teardowns; publish the claim-check surface + set profile live (geo-content handoff carries the exact checklist); decide the offer fork (One-Workflow Pilot as door vs Angle Map — composition recommended in `mission-first-client-engine` brief).
3. Worth-resuming (judged): Jen voice-lock reels (`/resume listing-hook-set-v2`), LinkedIn About rebuild (`/resume writers-room`) — both "one session from shipping."

## Do Not Rebuild

- Homebase/Library/briefs surfaces — extend `homebase_board.py`, `catalog_board.py`, `work_catalog.py`, `mission_brief.py` only. Never a parallel dashboard, never a second collector (read `.agent/sweep/latest.json` + catalog).
- The synthesis/triage contracts — slots + FORBIDDEN value guard are the safety; do not relax to "make prose richer." Richness comes from handoff bodies.
- The kill/park verbs and their ranking semantics (park=quiet+resumable, kill=hidden+ledger-recoverable).
- Do not re-add mission-control/pulse routes; 302s are deliberate.

## Suggested Skills / Workflows

- `/homebase` — open the command center (minted 2026-08-20).
- `/catalog` — open the Library.
- `/resume <slug>` — pick up any thread; the Launch cards carry copy-ready commands.
- `Skill: handoff` at close — the Stop hook now insists on the 3-line narrative anyway; writing a real one feeds the deep brief pages.

## Exact Next Prompt

```
Open the Homebase (http://127.0.0.1:8765/). I've re-authed the claude CLI.
Run: python3 execution/brief_synthesis.py run && python3 execution/brief_synthesis.py triage
then confirm the nightly receipt goes green. After that: walk me through
executing the send-week the mission-board brief recommends — teardown sends
first, claim-check launch second, offer-fork decision third. No new builds.
```

## Acceptance Criteria

- Nightly receipt `.agent/health/session-sweep.json` shows `status: ok` after the next 02:45 run (post re-auth).
- At least one teardown sent, or the claim-check surface live, or the offer fork logged — a release, not an artifact.
- No new surfaces or collectors added.

## Risk Notes

- The pane/browser preview can render blank on scroll (known harness quirk, affects screenshots only — pages are fine in the real browser).
- `session_sweep_run.sh` claims the session lock; a live working session at 02:45 makes the sweep skip honestly (logged, not silent).
- Judged-prose age caveat appears on briefs when synthesis is 3+ days old — that is the system being honest, not broken.
