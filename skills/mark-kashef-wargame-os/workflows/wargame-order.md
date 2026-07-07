---
description: Any goal or mission that will be executed later by a cheaper model/session than the one planning it — turn it into a wargame order file, the front door of the wargame OS
---

# /wargame-order — The Front Door

Takes any goal Farrice hands over and turns it into a WARGAME ORDER file: the mode-switch preamble plus a mission brief with every ambiguous choice frozen. This does not fight the mission on paper yet — that's `/wargame-run`. This workflow only writes the order the frontier model will later execute against.

## Pre-Flight Gate

1. **Would a cheaper executor actually run this mission?** (genius.md heuristic 1) If Farrice is asking for this to be done right now, in this session, by this model — there is no execution gap to bank judgment across. Skip the wargame apparatus, do the work directly.
2. **Is a wrong turn on this mission expensive relative to simulating it first?** A one-line Slack reply or a trivial file rename does not earn a wargame order — reserve this for missions with real build/edit/decision surface.
3. **Does `.agent/missions/<mission-slug>/` already exist?** Governs whether Step 2 below scaffolds fresh or reuses the existing folder.
4. **Is this a new mission or a refinement of an existing task file?** Check `tasks/` for a file already describing this initiative before assigning a new `NN`.

**Do NOT use this when**: the mission is already a wargame in progress (route to `/wargame-run` or `/wargame-grade` instead) or the executor is the current session (no judgment-arbitrage gap to exploit).

## Skill Acquisition

Load before executing:
- `skills/mark-kashef-wargame-os/genius.md` — heuristics 1, 2, 4; Signature Moves (mode-switch open, mission-brief separation, active-aggressive titles); Anti-Patterns 1, 3, 4
- `skills/mark-kashef-wargame-os/references/goal-and-loop-contracts.md` — `/goal` contract point 6 (BLOCKED discipline)
- `skills/mark-kashef-wargame-os/assets/wargame-folder-template/` — `SUCCESS.md`, `LEDGER.md`, and one `tasks/*.md` matching this mission's content type (below), as the exact preamble shape to reuse

## Execution

1. **Slugify the mission.** Derive `<mission-slug>` from the goal (kebab-case, e.g. `client-onboarding-rebuild`).
2. **Scaffold the mission folder if absent** — `Bash`: `mkdir -p .agent/missions/<mission-slug>/{tasks,wargames}`, then copy `SUCCESS.md` and `LEDGER.md` from `assets/wargame-folder-template/` into the mission root if they don't already exist there.
3. **Assign `NN`** — `Bash`: `ls .agent/missions/<mission-slug>/tasks/` to find the next unused two-digit prefix; never overwrite an existing task file.
4. **Gather real context to fill placeholders** — `Read`/`Grep` any brief, prior chat, project CLAUDE.md, or Recall grounding (`mcp__recall__search`) that names the audience, CTA, tone, or reference material for this mission. Only what you can point to a real source for gets filled in; everything else stays `{{PLACEHOLDER}}`.
5. **Write the order** — `Write` to `.agent/missions/<mission-slug>/tasks/NN-<name>.md`, reusing the exact preamble verbatim from the template, customizing only the recon-first line to this mission's actual terrain:
   - "WARGAME ORDER. You are not executing this mission, you are wargaming it. A cheaper executor (`<name the executor>`) runs the brief below later. Your job is the route it will follow."
   - "Recon first, read-only: `<this mission's actual recon target>`."
   - The five schema bullets verbatim (expected observation / failure+cause+counter / fork triggers / RECON NEEDED / aborts + verification).
   - "Write it so the executor can run the brief end to end without asking a single question."
   - `=== THE MISSION BRIEF (the executor's orders, not yours) ===`
6. **Freeze every choice the executor could get wrong.** Design tokens, voice adjectives, file paths, frameworks, scope boundaries — anything ambiguous gets a specific answer written into the brief now, not left for the executor to decide later.
7. **Give the mission an active-aggressive title** in the file's opening comment or first line (e.g. "Hunt the Bugs," "Tear Down the Competition") — the verb sets the posture.
8. **Log the BLOCKED gaps, if any** — `Edit` `.agent/missions/<mission-slug>/LEDGER.md`: append one line per unfilled `{{PLACEHOLDER}}` naming exactly what input is needed. Never invent the missing value.

## Worked Example (code-build mission, order only — not fought yet)

```
WARGAME ORDER. You are not executing this mission, you are wargaming it. A cheaper
executor (Sonnet) runs the brief below later. Your job is the route it will follow.

Recon first, read-only: the reference site at {{URL}} and the repo's existing site/ dir.

Then fight the mission on paper, move by move, and write it to wargames/11-rebuild.md:
- every move states its expected observation, exactly what you should see if it worked
- every move carries its most likely failure, the cause it signals, and the counter-move
- every fork gets a trigger, if you observe X, take route B
- assumptions recon could not settle get marked RECON NEEDED with the exact check that settles it
- end with abort conditions, and the verification runs the executor must perform with what pass looks like for each

Write it so the executor can run the brief end to end without asking a single question.

=== THE MISSION BRIEF (the executor's orders, not yours) ===
I'm rebuilding {{BUSINESS}}'s site because {{PROBLEM}}. ...
```

Note what's already frozen even at the order stage: the recon target is a real URL, not "the site," and the wargames output path is named — both come from Step 3/5 above, not left for `/wargame-run` to guess.

## Content Type Adaptations

| Mission type | Recon-first line targets | Executor named | Frozen-choice focus |
|---|---|---|---|
| **Code build** (site, feature, bug hunt) | reference codebase/site, repo README, core flows | Sonnet / Claude Code cheaper tier | design tokens, file structure, scope clamp ("no features beyond this list") |
| **Copy-content** (page copy, sequence, hooks) | current page + voice samples on file | mid-tier model | voice adjectives, CTA, section list, variant limits |
| **Research-analysis** (competitor map, market scan) | each named property/source directly | Opus / research-tier model | verification standard ("cite a source for every claim"), conflict-disclosure rule |
| **Ops-automation** (process → blueprint) | the process description + every tool it touches | Claude Code cheaper tier | automate/checkpoint/human-keep classification, guardrail naming |

Naming the executor concretely matters — genius.md heuristic 8 (tail the executor to the model) only works if `/wargame-run` knows which model's dialect to write for. If Farrice hasn't said, default to the tier one step below the drafting model per the Opus-Fallback Policy, and say so in the order rather than leaving it implicit.

## Output Requirements

Single file at `.agent/missions/<mission-slug>/tasks/NN-<name>.md` containing, in order: the WARGAME ORDER preamble (mode-switch open, customized recon line, five schema bullets, blind-execution close), then `=== THE MISSION BRIEF (the executor's orders, not yours) ===`, then the mission-specific brief with every freezable choice frozen and every unfillable one left as `{{PLACEHOLDER}}`. A companion `LEDGER.md` entry names any BLOCKED gaps.

## Quality Gate

- [ ] The order literally says "you are wargaming it," never "execute this mission" (Anti-Pattern 1: plan wearing a wargame costume)
- [ ] Every ambiguous choice the executor could get wrong is frozen in the brief, not left to "use your judgment" (Anti-Pattern 4)
- [ ] No `{{PLACEHOLDER}}` was filled with an invented value — unfillable ones stay literal placeholders, and each has a matching LEDGER.md line (Anti-Pattern 3)
- [ ] Rubric criterion 6 (honest blocking): every gap is named, none smoothed over
- [ ] The recon-first line names a real, checkable target — not "wherever seems relevant"
- [ ] The named executor matches the tier `/wargame-run` and `/wargame-execute` will actually use — no mismatch between who the order says will run it and who eventually does
- [ ] The mission title carries a verb, not a noun (a title is "Hunt the Bugs," never "bugs.md")
- [ ] `NN` was assigned by checking `tasks/` first — no collision with an existing mission file

## Handoff

This workflow's only output is the order file — it does not fight the mission and does not touch `wargames/`. The moment `tasks/NN-<name>.md` is written and any BLOCKED gaps are logged, hand off to `/wargame-run` for the same `NN`. Do not draft moves here even if the shape is obvious; keeping the boundary clean is what lets `/wargame-run` route to a different (higher) model tier without re-deriving context this workflow already gathered.
