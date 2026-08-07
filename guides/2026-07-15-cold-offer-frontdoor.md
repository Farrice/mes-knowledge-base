---
date: 2026-07-15
session: cold-offer-frontdoor
tier: operator-guide
status: enriched
---

# Cold-Offer OS + Expert Front Doors — What We Built 2026-07-15 and How to Use It

> One session, four assets: **`skills/jeremy-haynes-cold-offer`** (cold-traffic offer mastery, 13 workflows, the gap the harness had been missing), the **Expert Front-Door System** (`/[expert-name]` summons persona + full arsenal, all 222 experts), **generator-enforced registration** across the entire Forge/extraction pipeline (fireable-but-invisible commands structurally ended), and the **concurrent-session alarm** (Golden Rule as a mechanism). Applied work: the DWA Ship Sprint presale page audited (7.75) and fixed — ticket 0006 conditions MET, GO gate is Farrice's. Companions: `extractions/jeremy-haynes/extraction-report-cold-offer.md`, `_active/clients/dwa-threads-engine-2026-07-05/04-deliverables/26-jh-offer-audit-ship-sprint.md`, `docs/solutions/2026-07-15-concurrent-session-race-accept-repair-dedupe.md`.

## ⚡ If you only read 10 lines

- `/[expert-name]` now loads ANY expert whole — persona + every skill, tier-gated. Try `/jeremy-haynes`, `/lara-acosta`.
- Cold-traffic offer work starts at `/jh-offer-stack` (build) or `/jh-offer-audit` (teardown); `/jh-plateau-diagnostic` arbitrates "offer problem vs. funnel problem."
- The offer doctrine in one line: every component must name the narrative element it neutralizes — "This isn't random shit that's included in the offer stack."
- Haynes' revenue figures are QUARANTINED (`skills/jeremy-haynes-cold-offer/references/source-receipts.md`) — never cite as verified.
- Registration is generators-only now: `python3 execution/sync_registries.py && python3 execution/generate_slash_commands.py`. Never hand-edit registries or menu.
- Dry-run first on big syncs: `sync_registries.py --check --experts-scope multi|all`.
- New extractions auto-ship front doors — /extract §7, /extract-forge Phase 6, /forge Gates all run the generators.
- A second live session on this tree now triggers a SessionStart alarm; if files change that you didn't write: accept → repair → dedupe, never revert (solution card 2026-07-15).
- DWA next: Farrice's felt verdict on `24-ship-sprint-presale.md`, build the Day-0 stall self-check form, set [DATE], lock name+price (ticket 0005).
- A-tier promotion for the cold-offer skill awaits Farrice's judged blind pass: generated blueprint vs. `extractions/jeremy-haynes-cold-offer/reference-corpus/`.

## Command table

| Command | Produces | Reach for it when |
|---|---|---|
| `/jeremy-haynes` (any `/[expert-name]`) | Full expert: persona + skill arsenal, tier-gated | You want "the expert in the room," not one workflow |
| `/jh-offer-stack` | Offer Stack Blueprint (narrative→components, core/editions) | Building an offer for cold traffic |
| `/jh-offer-audit` | Traceability teardown + rubric scorecard + top-3 fixes | An offer underperforms and you need to know why |
| `/jh-plateau-diagnostic` | OFFER vs. FUNNEL verdict via lead-temperature drift | Growth stalled at scale, leads "arriving colder" |
| `/jh-objection-mine` | Objection pie chart → core additions vs. closer editions | 10+ sales conversations exist |
| `/jh-offer-to-copy` | Articulation brief (two-cliffs order, specificity ledger) | Handing offer architecture to copy/creative |
| `/jh-temp-migrate` | Re-composition plan for colder audience stage | In-market pool exhausted (earned via diagnostic) |
| `sync_registries.py [--check] [--experts-scope multi\|all]` | Indexes + skill shims + expert front doors | After ANY skill/agent/workflow creation |
| `generate_slash_commands.py` | SLASH_COMMANDS.md menu rebuild | Same moment — always paired with the above |
| `/resume cold-offer-frontdoor` | This thread's handoff | Continuing the DWA gate work |

## The mental model

1. **An offer is a living stack, not a launch artifact.** Components are derived from the ICP's umbrella narrative (problems → circumstances → desired outcomes + failure scars), re-composed as audiences get colder (in-market → needs-convinced → mass-market), and augmented from objection data. Hormozi optimizes an offer once; Haynes keeps it converting as traffic cools. Lineage: Schwartz's awareness ladder, operationalized — named, not overclaimed.
2. **Experts are summoned whole, by name.** The agent folder's name IS the command; skills prefixed with that name auto-group under it. Naming convention is the glue; generators enforce everything else.
3. **Registration has one exit.** Every lane of Forge OS and both extraction pipelines end in the same two generators. "Fireable but not in the menu" is now a detectable failure, not a silent state (this session found 1,192 accumulated strays).
4. **One live writer per tree.** The workspace stays central (it's the OS, projects are documents); concurrency is handled by the alarm + worktrees for second drivers, not by splitting the workspace.

## Capability 1 — `jeremy-haynes-cold-offer` (the skill)

**What it is:** 13 workflows + 10 born-v2 execution prompts encoding Haynes' cold-traffic offer methodology: umbrella-narrative grammar, audience-temperature bifurcation, objection→component conversion, offer layers (core vs. closer-held "editions"), next-problem absorption, show-rate-as-offer-telemetry. Built from the source video (kiWQ3M6fiH4) + `/watch` visual layer (100 frames — the frameworks are literally drawn on his whiteboard) + 5 primary blog articles + verification brief.

**When to reach for it:** any offer meant to convert strangers; "warm converts but cold doesn't"; scaling plateau with colder leads; sales floor stalling deals at the finish line.

**When NOT to:** warm-relationship nurture sequences (Suby's ladder is the cheaper fit); back-end LTV economics (Sultanic); one-time offer polish where the value equation suffices (`/jh-value-crosscheck` pairs Hormozi instead of replacing him).

**How to invoke:** `/jh-offer-stack` front door; full list in `skills/jeremy-haynes-cold-offer/SKILL.md`. Standard sequence: `/avatar-machine` → `/jh-avatar-bridge` → `/jh-offer-stack` → `/jh-value-crosscheck` → `/jh-offer-to-copy` → `/copy-engine`.

**Worked example (live, this session):** `/jh-offer-audit` on the DWA Ship Sprint — found zero orphan components (rare) but three misalignments: authorless page, checkout→day-0 dead air, unused insurance pricing frame. All three fixed same-session; composite 7.75; ticket 0006 flipped to conditions-MET.

**Honest edges:** blind pass is model-judged only (EVAL-037) — A-tier needs Farrice's read; `/jh-objection-mine` untested on a real transcript corpus; all Haynes revenue claims are self-reported and quarantined.

## Capability 2 — Expert Front-Door System

**What it is:** `sync_registries.py` now discovers expert groups (`agents/<slug>/AGENT.md` + all skills prefixed `<slug>-`), renders `.claude/commands/<slug>.md` front doors (embody persona → tier-gated skill table → flagship workflow offer), handles name collisions (158 short-name shims demoted to full slugs, 12 exact-match skills subsumed), and never clobbers hand-written commands.

**When to reach for it:** whenever you'd work "with" an expert across their domains — `/jeremy-haynes` for offer AND mindset — or can't remember a skill's exact slug.

**When NOT to:** single-deliverable tasks where the narrow command is cheaper (`/jh-offer-audit` beats `/jeremy-haynes` + navigation); front doors deliberately do NOT bulk-load all skills.

**How to invoke:** type the expert's name as a command. Regenerate after changes: `python3 execution/sync_registries.py` (add `--check` to preview; `--experts-scope multi|all`). Fixed-point verified: re-running with no changes writes nothing.

**Worked example:** `/jeremy-haynes` front door lists both his skills with Tier-1/Tier-2 paths and flagship workflows; live in this session's own skill menu.

**Honest edges:** a skill named WITHOUT its expert's prefix won't group (convention is load-bearing); front-door descriptions fall back to weak text for the ~218 AGENT.md files without `role:` frontmatter (cosmetic); one foreign-skip honored (`research-intelligence-agent`).

## Capability 3 — Generator-enforced registration (pipeline wiring)

**What it is:** `/extract` §7, `/extract-forge` Phase 6/7, `workflow-forge` Wire step, `agent-forge` step 7, and `/forge` Gates all now name the two generators as the ONLY registration mechanism, with the invariant stated: fireable-but-not-in-menu = registration failure.

**When to reach for it:** automatic — but if a command ever seems missing, run the two generators before debugging anything else.

**When NOT to:** plugin lane (produces installables, no menu surface — by design).

**Honest edges:** the invariant lives in workflow prose, not a hook; a conductor that ignores the workflow can still skip it (the menu-stray count at next regen is the tripwire).

## Capability 4 — Concurrent-session alarm

**What it is:** `execution/hooks/concurrent_session_alarm.py` (SessionStart) detects sibling session transcripts with writes in the last 10 min and warns with lock/worktree guidance. Warns, never blocks. PoC'd 4/4 cases.

**When to reach for it:** automatic. If it fires and you're building: claim `session_lock.py`, or move the second session to a `git worktree`.

**When NOT to:** don't wire session_lock into every session — PARKED with a named re-trigger (a second race despite the alarm). Opt-in locks stay opt-in until reality votes again.

**Honest edges:** 10-min window is a heuristic (`CONCURRENT_ALARM_WINDOW_MIN` env tunes it); read-only siblings cause harmless warnings.

## Composition options (never forced)

| Stack | When it earns its cost |
|---|---|
| `/jh-offer-stack` × `/avatar-machine` | New market, no narrative yet — GROUND feeds the umbrella directly |
| `/jh-objection-mine` × `jeremy-miner` NPQ | Sales floor: mine decides what stops needing handling; NPQ handles what remains |
| `/jh-value-crosscheck` × `alex-hormozi` | Stack composed; per-component value pressure-test before copy |
| `/jh-offer-to-copy` × `/copy-engine` / `luke-iha-*` | Articulation locked before hook craft — hooks on a misaligned offer are wasted |
| Front doors × `/convene` | Council seats can now be summoned by name at full arsenal |
