---
description: The Homebase — open the Agentic OS command center (cockpit · Launch · Library) served live at http://127.0.0.1:8765/
---

# /homebase — The Agentic OS Command Center (2026-08-20; cockpit 2026-08-21)

One page Farrice opens to work. **Above the fold — the COCKPIT** (ARMS-video
harvest 2026-08-21; Jarvis status core 2026-08-22): brand header + live clock,
then the center **STATUS CORE** — a 6-tile vitals strip (missions · need-you ·
outcomes · routines-dark · deck state · sweep age, color = status only, tiles
jump to their widgets), the **TODAY** panel (sprint target, money line, next
move, compact second-brain disc → `/brain`), and the **LIVE ACTIVITY feed**
(deck runs w/ measured cost, commits, briefs compiled, routines fired — one
merged newest-first stream from existing receipts). Columns: Micro apps,
⚑ Needs-you, **Skills deck** (headless `claude -p` runs with model + effort
pickers, measured cost per receipt), **Routines** (all launchd jobs, next fire
first), system counts. Widgets drag-reorder; layout persists per browser.
(The artifact ring is RETIRED 2026-08-22 — Farrice's verdict: decoration
without function; the feed replaced it.)
**Below the fold**: LAUNCH (resumable sweep threads with one-click `/resume`
copy) and LIBRARY (fresh briefs, dark asset shelf, catalog) unchanged.
Every other home base is one nav hop away — and on a served page the nav stays
inside the live server (surface_nav route rewrite, 2026-08-20).

## Open it

```bash
open "http://127.0.0.1:8765/"
```

The server is always-on via launchd (`com.antigravity.pulse-serve`, KeepAlive,
`--idle 0`). If it's somehow down:

```bash
launchctl kickstart -k gui/501/com.antigravity.pulse-serve
```

or fallback: `python3 execution/pulse_serve.py --open`.

## Routes (pulse_serve.py)

`/` homebase · `/brain` second-brain graph · `/room` briefs · `/library`
catalog · `/assets` asset board · `/oracle` · `/repo/<path>` files. `/pulse`
and `/missions` are RETIRED (two-surfaces collapse, 2026-08-20) and
302-redirect here.

## The second brain (`/brain`) — v2 2026-08-22

Curated-canon workspace graph (allowlist, ~1,300 nodes — never a directory
walk), organized so every visual channel carries a variable (Hansen HUD-bible
discipline): angle = department (labeled annular arcs), sub-position = FAMILY
(real name-prefix families: oren-*, verify_*…, 66 detected), size =
importance, star = top-44 canon. **Semantic zoom**: at rest you see labeled
arcs + the star constellation; mid-zoom adds family discs + labels; close-up
shows everything. **Hover = snapshot**: 300ms dwell opens a card with the
node's AI summary; click pins the full detail (summary, open/editor/copy/zoom,
live preview); double-click opens; search matches summaries too.

Snapshots come from `.agent/brain/summaries.json`, built by
`python3 execution/brain_summaries.py run` — batched Haiku with per-file
mtime caching (only changed files respend) and a MEASURED-cost receipt in
`.agent/brain/summary-receipts.jsonl`. First 1,272 snapshots were authored by
in-session subagents (2026-08-22, $0 API). Note: `claude -p` needs a valid
CLI login (`claude login`) — an expired OAuth fails fast with $0.00 receipts.
Graph rebuild: `python3 execution/brain_graph.py --if-stale` (what regen
calls); the fingerprint includes summaries.json so fresh snapshots re-render.

## The skills deck

Cards live in `.agent/homebase/skills-deck.json` (hand-curated — only cards in
this file can run). Run fires `POST /action run_skill` → guarded
`execution/skill_deck_runner.py`: params validated as indices against the deck
file, `mission_runner.FORBIDDEN_RE` refusal net, mandatory `session_lock`
claim, detached `claude -p <cmd> --model M --effort E --output-format json`.
Receipts (state, duration, **measured `total_cost_usd`**) + a markdown report
land in `.agent/homebase/deck-runs/` and surface on the board + artifacts
ring. CLI equivalent: `python3 execution/skill_deck_runner.py run <card>
--model sonnet --effort low`.

## The deep mission pages

Click **open brief ↗** on any Launch card → the thread's context-rich page:
instant summary (handoff Purpose), the state as the last session left it
(Current State + staleness warning), resume/park/**kill** decision + LIVE
buttons, copy-paste blocks (Exact Next Prompt, context pack, operator run
prompt), then numbers, assets (with generation prompts), deduped timeline
(with finalize notes), and the mission record (outcomes + verdicts).
Rich narrative comes from the thread's own handoff — a stub handoff degrades
honestly, so **writing a real /handoff at session close is what feeds this**.

`kill <slug> --reason "…"` = dead + hidden: ledger line + handoff archived;
never resurfaces (recover: `pulse_actions.py reopen` + `handoff_store.py
unarchive`). `park` = shelved + quiet: resumable, muted, never ranks urgent.

## Refresh

The header's **↻ refresh data** button (or `python3 execution/pulse_actions.py
refresh`) re-runs the session sweep + asset index, then regenerates the boards;
the open page reloads itself when the data is actually fresh (mtime poll).
Sweep also runs nightly via `com.antigravity.session-sweep`.

## Regenerate manually

```bash
python3 execution/homebase_board.py
```

Doctrine: reads `.agent/sweep/latest.json` + existing ledgers only — never a
second collector (docs/solutions/2026-08-06-live-local-board-pattern.md).
Palette/typography come from `execution/board_theme.py` (one skin, every
board; client reskin = alternate token dict).
Deferred by decision (2026-08-20 mission): asset-board register reconciliation,
deliverables librarian. The workspace force-graph shipped 2026-08-21 as
`/brain`. Deferred to v2 (Farrice, 2026-08-21): Google email/calendar widgets,
client-reskin demo.
