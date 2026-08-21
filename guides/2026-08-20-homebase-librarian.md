---
date: 2026-08-20
session: homebase-librarian
tier: operator-guide
status: enriched
---

# System: Homebase + Ambient Librarian — What We Built 2026-08-20 and How to Use It

> One day took the Readout OS from six disconnected boards to a two-surface command system with an intelligence layer and a permanent memory: **The Homebase** (act) + **Briefing Room** (read), deep mission pages that mine session narratives, a judged analyst voice on every card, **The Library** (a ~1,000-row permanent catalog with a Worth-Resuming shelf), and ambient filing that runs at every session close in both harnesses with zero commands. Companions: `.agent/workflows/homebase.md` · `.agent/workflows/catalog.md` · `guides/2026-08-06-readout-os.md` (base system) · `docs/solutions/2026-08-06-live-local-board-pattern.md` (the pattern).

## ⚡ If you only read 10 lines

- `open "http://127.0.0.1:8765/"` (or `/homebase` in any session) — the ONE page to work from. Server is always-on; `↻ refresh data` reruns the whole pipeline.
- `/library` route (or `/catalog` command) — everything you've ever worked on, searchable; **★ Worth Resuming** = merit that went quiet, the lost-work fix.
- `python3 execution/work_catalog.py find "<half-remembered words>"` — retrieval by memory; also fires inside `memory_facade.py` for every session.
- Click **open brief ↗** on any card — the deep page: what it is, the state as the last session left it, resume/park/**kill** live buttons, copy-paste pickup prompts.
- `kill <slug> --reason` = dead + hidden (ledger-recoverable) · `park` = quiet + resumable (never ranks urgent — that was a bug, fixed).
- Filing is AUTOMATIC: every session close deposits its work in the catalog and is asked once for a 3-line narrative; nightly 02:45 sweeps + regenerates everything; Sunday 07:00 the Shelf Report lands in the Room.
- The analyst layer (ledes, assessments, options-with-tradeoffs) refreshes nightly via `claude -p` — **currently degraded until the CLI is re-authed** (run `claude` once in a terminal); the last valid analysis is kept and its age disclosed on the page.
- Judged prose can NEVER carry a number, path, or URL — the fail-closed validator rejects the whole pass. Facts are mechanical; judgment is judgment.
- Write a real `/handoff` at close: the deep brief pages are only as rich as the narrative the session deposits (stubs degrade honestly).
- Retired: Pulse and Mission Control as pages (`/pulse`, `/missions` → 302 to `/`); their generators live on as libraries.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/homebase` | Opens the command center | Start of any work block |
| `/catalog` | Opens the Library | "Where's that thing I did about…" |
| `python3 execution/work_catalog.py find "<q>"` | Ranked rows + resume commands | Half-remembered retrieval from terminal or scripts |
| `python3 execution/work_catalog.py report` | Weekly Shelf Report brief in the Room | Manual estate read (auto: Sundays 07:00) |
| `python3 execution/pulse_actions.py kill <slug> --reason "…"` | Ledger `killed` line + handoff archived | A thread is dead weight — hide it for good |
| `python3 execution/brief_synthesis.py run` / `triage` | Judged analyst slots / resume-shelve-kill calls | After CLI re-auth, or to refresh judgment on demand |
| `python3 execution/pulse_actions.py refresh` | Full pipeline: sweep → index → judge → briefs → catalog → surfaces | The ↻ button's CLI twin |
| `zsh execution/session_sweep_run.sh` | The entire nightly chain, on demand | Proving the night job before trusting it |

## The mental model

1. **Two surfaces, one library.** Homebase is where you decide and act; the Briefing Room is where you read deeply; the Library is where nothing is ever lost. Everything else is a route into one of those three.
2. **Facts are mechanical, judgment is judged, and the boundary is enforced.** Every number/path/date on a page comes from ledgers; every "so what" comes from a validated synthesis pass that is structurally unable to state a fact. A failed judge degrades to last-valid-with-age-disclosed, never to silence or destruction.
3. **Filing happens at the edges of a session, not in an archive pass.** Birth: the catalog row exists the moment work is named. Death: the Stop hook extracts the three lines only the working session knows. The nightly sweep is the net, not the mechanism.
4. **Merit is sticky and deterministic.** A good verdict, a finalize ≥8, or a pin marks a row forever; dormant+merit is the shelf that answers "what did I lose that mattered."

## Capability: the ambient librarian (Stop hook, both harnesses)

**What it is:** `session_ledger_hook.py stop` (shared by Claude Code and Codex) files every producing session into `work_catalog` and single-fires a block asking for a 3-line narrative handoff (Purpose · Current State · Remaining Priority).
**Honest edges:** a session that ignores the ask still exits — the auto-pin stub then carries a narrative-missing marker; loop-guard (`stop_hook_active`) and single-fire (`narrative_asked`) were both proven by synthetic firing. Crashed sessions are caught by the nightly merge within a day.

## Capability: the nightly chain (02:45)

**What it is:** `session_sweep_run.sh` — lock-claim → sweep (+catalog merge) → facts-only briefs → judged synthesis + triage (restore-not-discard) → rebuild briefs → regen Homebase + Library → receipt to `.agent/health/session-sweep.json`.
**Honest edges:** skips honestly when a live session holds the tree lock; with the CLI unauthed it reports `synthesis_degraded` while keeping the last valid judgment (survival proven md5-identical through a full dead-CLI run — the pre-2026-08-20 script destroyed the synthesis nightly, which is why briefs were always bland).

## Capability: kill / park semantics

**What it is:** `kill` appends a terminal ledger line + archives the handoff — gone from every board and sweep, recoverable only via `reopen` + `unarchive`. `park` annotates the handoff `parked` — visible, muted, never urgent.
**Honest edges:** killing a thread whose mission is still open elsewhere keeps the thread alive by design (an open sibling mission outranks a kill).
