---
description: Update the Root-Core Operator Guide with any operator assets built or changed since the last sync — surgical per-asset sections, never wholesale regeneration — then stamp the sync state
tier: system
---

# /operator-guide-sync — Keep the Operator's Source of Truth Current

`docs/ROOT-CORE-OPERATOR-GUIDE.md` is Farrice's external memory for how to run what we build — so he never has to hold the system in his head. This workflow is the model half of a deterministic loop: `execution/operator_guide_sync.py check` (wired into the closeout spine) detects when operator assets changed; this workflow writes the update; `record` stamps it quiet.

## Process

1. **Get the delta**: `python3 execution/operator_guide_sync.py check` — the list of changed/new operator assets since the last stamp.

2. **Filter for operator relevance** (the detector over-reports on purpose — you judge): an asset earns a guide entry when it changes *how Farrice runs something* — a new/renamed workflow or skill, a new front door, changed invocation, new capability or limit, a new standing doctrine. Ignore: telemetry-only edits, internal refactors, content deliverables, solution cards that only record history (those already auto-resurface), tracker/map files under `_active/`.

3. **Update surgically.** For each relevant asset, read it and write or revise **its own section** in the guide, matching the established anatomy: *what it is → the trigger feeling → copy-paste invocation examples → a worked example if one exists → can/can't → honest edges*. Rules:
   - Never regenerate the whole guide — the spine stays, sections change (multi-engine-rebuild lesson: preserve elevated prose, surgical passes only).
   - New tools also get a line in the guide's **mental model** or **chain diagram** only when they genuinely change the flow.
   - Prune as you go: if an asset was superseded/renamed/archived, its section is updated or removed *in the same pass* — a guide that only grows becomes sediment.
   - Keep each section tight enough to re-read in under a minute; deep detail belongs in the asset's own file, linked.
   - If the guide passes ~600 lines, split a domain into `docs/operator-guides/<domain>.md` and leave a one-line pointer — progressive disclosure, one level deep.

4. **Stamp**: `python3 execution/operator_guide_sync.py record` — snapshots the synced state so the closeout nudge goes quiet until the next real change. Stamp LAST, after all guide edits are written.

5. **Report** one line to Farrice: sections added/updated/pruned, guide line count.

## When this fires

- The closeout spine (`end_session_closeout.py` → `operator-guide-nudge`) reports "OPERATOR GUIDE UPDATE DUE" at `/end-session` or SessionEnd.
- Directly after any extraction, skill/workflow build, import refresh, or harness change — run it before closing out rather than letting debt pile up.
- Manually anytime: cheap when current (check exits 0 and you're done).

## Boundaries

The guide documents how to RUN things — it is not a changelog (git is), not a project tracker (maps/handoffs are), and not a skill index (SLASH_COMMANDS.md is). One reader: Farrice-as-operator.
