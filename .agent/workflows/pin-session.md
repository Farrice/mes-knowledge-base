---
description: Pin the current work session — stamp a Session title into today's briefing (or --file) and drop a thread pointer so /resume surfaces it by name. Manual lever for the auto-pin formula (chain_runner.finalize + /end-session + the Stop-hook backstop also pin automatically).
---

# /pin-session — stamp + pin the current session

Make the current session a **retrieval handle**: stamp a `Session title:` line into the
active artifact's header AND drop a pinned thread pointer into the handoff store, so
`/resume` surfaces it **by name** (title verbatim on the `↪` line) and
`handoff_store.py show <thread>` resolves it.

Works for any briefing/handoff-style markdown, not just LinkedIn. This is the **manual
lever** — the same pin runs automatically via `chain_runner.finalize()` (every producer
workflow), `/end-session`, and the deterministic Stop-hook backstop. Use this to pin
mid-session, re-title, or pin a session that shipped through some other route.

## The consistent formula (why this exists)
> Every session that produces a durable artifact gets a titled pin — written automatically
> at the ship/finalize point, backstopped by the `Stop` hook in `session_ledger_hook.py`,
> which nudges (once) whenever an artifact shipped but no pin was recorded. This command is
> the on-demand version of that same write. You never have to remember it.

## Inputs (parse from the invocation)
- **TITLE** (auto-derived — do NOT ask Farrice to name or confirm it) — use the shared
  session naming convention (same as `/end-session`):
  `[Project or Client] — [Work Type][ vN if iterated] ([key scope])`
  (e.g. `TrendScale Creative Strategist Trial — Script Rework v2 (JCKED + Puravita)`).
  Title Case; ` — ` is the sanctioned separator (display title, exempt from the prose em-dash
  ban). Only ask if the session's primary object is genuinely ambiguous.
- **--file PATH** (optional) — markdown to stamp. DEFAULT: today's LinkedIn briefing
  `_active/linkedin/06-automation/daily/briefing-<today>.md`. If that file is missing, **ASK**
  which file to stamp — never invent one.
- **--thread SLUG** (optional) — stable work-stream selector (the `/resume` row label +
  the dedup key). DEFAULT derivation:
    - file under `_active/linkedin/06-automation/daily/` → `linkedin-daily`
    - else slugify the basename with any leading `YYYY-MM-DD` and `briefing-` stripped
  Always pass it **explicitly** to `handoff_store.py` — a drifted auto-derived slug splits
  the `/resume` menu into two rows.
- **--status** (optional) — one of `active|blocked|ready|mid-build|done`. DEFAULT `active`.
  Never `done` unless the work-stream is truly closed (`done` is hidden from `/resume`).

## Steps
1. **Resolve** TARGET (= `--file` or today's briefing) and THREAD. Read TARGET to confirm it
   exists; if not, stop and ask.
2. **Stamp the header.** Insert one line into TARGET's header, immediately after the last
   contiguous header line (the last `>` blockquote line for briefings, else right after the
   H1):

       > Session title: {TITLE}

   If a `> Session title:` line already exists, **replace it** (idempotent) — anchor the
   Edit on the existing line.
3. **Write a lightweight pointer doc** to the scratchpad (a pointer, NOT the whole artifact):

       # {TITLE}

       **Pointer:** `{TARGET}`

       **Next session focus**: {one line — the very next action}

4. **Pin to the handoff store** (title rides in `resume_hint`; `--slug {THREAD}` keeps
   re-pins overwriting one file for idempotency; `--pin` floats it to the top):

   ```bash
   python3 execution/handoff_store.py save <pointer.md> \
     --thread {THREAD} --slug {THREAD} \
     --status {STATUS} \
     --hint "{TITLE}" \
     --pin --overwrite
   ```

   Pass the pointer file **explicitly** — do NOT use `--from-temp` unless a `/handoff` just
   ran. Confirm the output shows `saved:`.
5. **Confirm.** Run `python3 execution/handoff_store.py list --rich`, show the row, and print
   the reuse selector `/resume {THREAD}`. Confirm the verbatim TITLE shows on the `↪` line.

## Notes
- **Idempotent**: re-running same day for the same thread UPDATES the one row (no menu
  pile-up). `--slug {THREAD}` is what makes that true.
- **Two handles, written together**: the `> Session title:` header line is the grep/recall
  handle; the handoff pin is the `/resume` handle. This command writes both so they never
  drift apart.
- **Registration**: none needed — `.agent/workflows/pin-session.md` IS the registration
  (CLAUDE.md Workflow Override). Never touch `.agent/skill-index.json` (auto-built from
  `skills/` only).
- **Relationship to the auto-pin**: when `chain_runner.finalize` or `/end-session` already
  pinned this session, you don't need this command — the Stop hook stays quiet. Run it only
  to override the title/thread or to pin work that shipped off the happy-path.
