---
description: Resume (or realign from) any past work-thread — you choose which, not just the last
---

# /resume — Multi-thread session resume

Pick up ANY past work-thread, not just the most recent. One menu row per **thread** (work-stream), backed by the deterministic `execution/handoff_store.py` over the `.agent/handoffs/` store.

> Sibling: **`/realign <thread>`** runs the same engine but loads the thread as *background context for new work* — not bound to its old plan.

## Usage
- `/resume` — show the triage menu (live threads), then WAIT for the user to pick
- `/resume <thread|keyword|number>` — resume that thread directly
- `/realign <thread>` — load a thread as background, start adjacent work

---

## Step 1 — Menu (no argument)
// turbo
```bash
python execution/handoff_store.py list --rich
```
Present the menu verbatim-ish. Each row = one thread (latest handoff): age, STATUS, what's unfinished. Then ask:
`Which thread? (number, name, or keyword) — or /realign <thread> to start adjacent. (list --all for archived/done.)`
**WAIT for the user's pick.** Do not auto-pick.

## Step 2 — Resume a thread (selector given)
// turbo
```bash
python execution/handoff_store.py resume "<selector>"
```
This echoes the **resolved thread** (confirm it's the one they meant — if it resolved a number/keyword to the wrong thread, stop and re-ask), prints a **"Since this handoff"** drift block (branch/staleness), then the full handoff.

Then RECONSTITUTE the working context — don't just read it:
1. **Re-read** the deliverable/spec files the handoff references that still exist.
2. **Re-warm experts** — load the skills listed under the handoff's "Suggested skills".
3. **Branch** — if the drift block flags a different or missing branch, surface it and offer `git checkout <branch>` (never auto-force; the git hook blocks pushes anyway).
4. **Reconcile with live truth** — read the matching `MEMORY.md` project entry and `.agent/session-state.md`. If memory contradicts the handoff's plan (e.g. memory says "shipped", handoff says "ship it"), trust memory and flag the divergence. Check `docs/solutions/index.md` for any card matching this thread's domain — a past solved problem may be directly relevant to what's resuming.
5. Present a short **Realignment Brief**: what was true · what CHANGED since (from drift + memory) · the first 2–3 actions, each labeled **VALID / CHANGED / DONE**.

## Step 3 — Continue + close the loop
Proceed from the first VALID action. When the session ends, `/end-session` must write the next handoff under the **same thread** (`--thread <thread>`), so the menu keeps one clean row per thread instead of piling up versions.

---

## /realign mode
Run the same Step 2 load, but frame the handoff as **background only**: "Here's the context from `<thread>`; we're starting new work, not resuming its plan." Do NOT anchor to its priority order — surface its facts, constraints, and assets, then take the user's new direction.

## Notes
- Selector resolution is deterministic (handoff_store.py): exact thread → keyword (slug+title) → number. 0 matches lists candidates; >1 stops and asks. Numbers are cosmetic and always echo the resolved thread.
- Resolving by **thread name** is the stable path; numbers can shift as threads are added.
