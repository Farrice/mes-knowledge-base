---
description: Mission-queue front door — multi-mission continuity for any objective; status, new, next, done subcommands over CAMPAIGN.md + the SessionStart beacon
---

# /missions — The Campaign-Continuity Front Door (v1, 2026-07-28)

One project = one CAMPAIGN.md = one pointer. The beacon (`execution/hooks/campaign_beacon.py`, SessionStart) announces state every session; this workflow is the hands. Works for ANY objective — client work, content engines, system builds, books.

> **Naming:** `/campaign` (council preset) and `/mission` (JCC) were taken — this front door is `/missions`, plural, because that's what it manages.

## The operator flow (the whole system in five keystrokes)

1. **Once per project:** `/missions new <name> — <goal>` → scaffolds CAMPAIGN.md, sets the pointer.
2. **Any session, any day:** open a session → the beacon tells you the campaign + next open mission before you type.
3. `/missions` → see the full queue.
4. `/missions next` → the top OPEN mission compiles through /go (plan card → approve → run → deliver).
5. At close: `/missions done <n> "<one-line note>"` → queue updated, log appended, commit reminded. `/end-session` when stopping.

Off-queue idea mid-flow? `/go <raw dump>` still works for anything; if it belongs to the campaign, add it as a queue row instead of losing it.

## Subcommand behavior (conductor instructions)

### `/missions` (no args — status)
1. Read `.agent/active-campaign.json`. No file or `active:false` → say "no active campaign" and offer `/missions new`.
2. Read the campaign file. Present in ONE screen: name, goal, queue table verbatim, next open mission called out, last log line. No editorializing, no expansion.

### `/missions new <name> — <goal>`
1. Determine the project folder (existing `_active/<slug>/` or `projects/<slug>/`; create `_active/<slug>/` if new — then numbered subfolders per project-organization policy as work arrives, never empty scaffolds).
2. Write `CAMPAIGN.md` in that folder from the template below (root of the project folder ON PURPOSE — front-door file, same exception as INDEX.md; note it in the project INDEX).
3. Write `.agent/active-campaign.json`: `{"campaign": "<name>", "file": "<repo-relative path>", "active": true}`.
4. Confirm: run `python3 execution/hooks/campaign_beacon.py` and show its output — proof the next session opens warm.
5. Only ONE campaign is active at a time (the pointer is singular by design — focus is the feature). Switching projects = rewrite the pointer; the old CAMPAIGN.md keeps its state and reactivates the same way.

### `/missions next`
1. Read the campaign file; take the topmost row whose status contains OPEN.
2. If the row is marked FARRICE (human-only work — sends, taste picks): surface it and STOP — never simulate his actions; offer the next system-runnable row.
3. Otherwise compile that row's mission through `/go` (full Stage -1 → Stage 3; the campaign file's Standing Facts section is required reading in Stage 0's inventory).

### `/missions done <n> [note]`
1. Flip row n to `✅ DONE <date>`, append the note to the Log section.
2. Remind: commit to main. If the mission produced or retired canonical docs, run `python3 execution/canon_audit.py <project-folder>` to refresh CANON.md.

## Doc-status convention (the canon vocabulary, used by canon_audit.py + the read guard)

Load-bearing project docs carry frontmatter: `status: canonical | draft | superseded | archived`, plus `superseded_by: <path>` when superseded and optionally `supersedes: <path>` on the successor. A prose "SUPERSEDED" banner without frontmatter is drift — `canon_audit.py` detects it and offers the stamp. Reading a `superseded` file triggers a one-line redirect from `superseded_read_guard.py` — compass, never cage.

## CAMPAIGN.md template (paste for /missions new)

```markdown
# CAMPAIGN — <Name>

**Goal:** <outcome + number + deadline, in Farrice's words>
**The standard every mission holds:** the five-move recipe — inventory before generate · fresh receipts before judgment · isolated adversarial skeptic · felt standard as the test · decisions-not-homework. (Floor, not ceiling.)
**Rule for any session touching this campaign:** read this file, take the top OPEN mission through /go, update the queue at close. Farrice edits this file freely.

## Mission queue

| # | Mission | Status | Artifacts |
|---|---|---|---|
| 1 | <first mission> | ⚪ OPEN | |

## Standing facts (so no session re-asks)

- <decisions made, locked choices, binding constraints>

## Close-of-session ritual

1. Update the queue row(s) you touched. 2. Commit to main. 3. One-line log note below.

## Log

- <date>: Campaign created.
```
