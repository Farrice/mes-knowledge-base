---
description: A drafted wargame exists and needs its honest DONE/NOT-DONE verdict — grade point-by-point against the 8-point standard, red-team it with an actual attack, patch the break, log to the ledger
---

# /wargame-grade — Grade It, Then Try To Break It

Takes one drafted wargame (`wargames/NN-<name>.md`) and produces a verdict Farrice can trust: a point-by-point grade against `references/eight-point-standard.md`, a recorded attack against the route, the patch it forced, and a re-grade. "Wargamed means it survives contact" — this workflow is where that claim gets tested, not asserted.

## Pre-Flight Gate

1. **Does the wargame have a self-grade in `LEDGER.md` already?** This workflow supersedes the drafting-time self-grade with an adversarial one — read the self-grade first so you know which points the drafter already flagged as weak.
2. **Is this the weakest undone draft in the mission set?** Per genius.md heuristic 6 / the `/loop` contract, take the weakest draft first each cycle — don't polish an already-strong wargame while others sit ungraded.
3. **Has a red-team attack already been recorded for this wargame?** If yes, this is a re-grade cycle — grade against the patched version, not the original.
4. **Are you tempted to soften a grade to finish faster?** If yes, stop — "a draft that passes on paper but dies at first contact is a failure of this loop." Grade what's actually on the page.

**Do NOT use this when**: the wargame hasn't been drafted yet (run `/wargame-run` first) or grading is being done to rubber-stamp a deadline — the stop condition for a whole mission set is "two consecutive cycles improve nothing," not "we're out of time so call it DONE."

This workflow never invents work the drafter should have done — if the wargame is missing a whole Document Schema section (no RECON NEEDED block at all, no abort conditions), that's an automatic FAIL on the corresponding point, not something to quietly write in during grading.

## Skill Acquisition

Load before executing:
- `skills/mark-kashef-wargame-os/genius.md` — heuristic 6, Anti-Pattern 2 (softened grading), the Quality Rubric (all 9 criteria)
- `skills/mark-kashef-wargame-os/references/eight-point-standard.md` — full file, the "How to grade it" column for each of the eight points
- `skills/mark-kashef-wargame-os/references/goal-and-loop-contracts.md` — the `/loop` refinement prompt verbatim

## Execution

1. **Read the wargame** — `Read` `wargames/NN-<name>.md` in full.
2. **Grade point-by-point** — for each of the eight points in `eight-point-standard.md`, quote the specific line in the wargame that satisfies it (or note its absence). No holistic score; eight separate PASS/FAIL calls, each with the quoted evidence.
3. **Red-team it with a fresh, uncontaminated attacker** — dispatch via `Agent`: a fresh sub-agent with no memory of writing this wargame, instructed to "play the executor, follow this route blind, and report the exact move where it would have to stop and ask a question or where reality would diverge from the Expect line." A wargamer grading its own document is exactly the leniency-drift genius.md warns against; a fresh agent has nothing to protect.
4. **Name the break** — record the specific move number, what the attack revealed, and why (a missing trigger, a vague Expect, an assumption that should have been RECON NEEDED).
5. **Patch it** — `Edit` `wargames/NN-<name>.md`: fix the named move — add the missing branch, sharpen the Expect line to a string-match-able observable, or convert the assumption to a RECON NEEDED mark with its settling command.
6. **Re-grade the patched wargame** — repeat step 2 against the new version; confirm the previously-failing point now holds.
7. **Attempt one more honest break** against the patched version. If it holds, the wargame is DONE. If it breaks again, repeat steps 4–6 — do not declare DONE on an unproven patch.
8. **Log to the ledger** — `Edit` `LEDGER.md`: append the per-point grade table, the recorded attack, the patch, the re-grade result, and the final verdict.

## Worked Example (a real break, from the exemplar)

The `01-website.md` wargame's Move 9 predicts a failure caused by the *executor's own* pattern-matching: the About-page headshot SVG inheriting `aria-hidden="true"` from Move 7's icon pattern, when it should be `role="img" aria-label=...` because it's meaningful content, not decoration. That's the level a red-team attack should be finding — not "what if the API is down" (a world-caused failure the drafter probably already covered) but "where will the executor confuse two of *this wargame's own* patterns." If your red-team pass only finds world-caused breaks, it hasn't looked hard enough; also check where two moves resemble each other closely enough that a cheap model would conflate them.

## Content Type Adaptations

| Mission type | Red-team attack shape |
|---|---|
| **Code build** | Actually run the read-only recon commands the wargame specifies and diff the real output against the Expect line — a code wargame's attack is physical, not imagined |
| **Copy-content** | Read the drafted move as the stated skeptical ICP ("who has seen ten pages like this today") and find the line that doesn't survive that read |
| **Research-analysis** | Check whether every claim in the moves actually traces to a citable source per the mission's own verification standard — an unsourced claim is the break |
| **Ops-automation** | Trace the guardrail-firing order: does the wargame's abort condition actually fire before the failure it's meant to catch, or after? |

## Output Schema

```markdown
# Wargame Grade — [mission] — cycle [N]

## Point-by-Point (references/eight-point-standard.md)
| # | Point | PASS/FAIL | Evidence quoted from the wargame |
|---|---|---|---|
| 1 | Expected observation | | |
| 2 | Failure + cause + counter | | |
| 3 | Fork determinism | | |
| 4 | RECON NEEDED settling check | | |
| 5 | Abort conditions | | |
| 6 | Verification spelled out | | |
| 7 | Survived red-team | | |
| 8 | Executable blind | | |

## Recorded Attack
[what the fresh sub-agent tried, and the exact move where it broke]

## Patch
[what changed, and why it closes that specific break]

## Re-Grade
[which points flipped to PASS after the patch]

## VERDICT: [DONE / NOT-DONE — cycle again / BLOCKED — {{PLACEHOLDER}} discovered]
```

## Quality Gate

- [ ] Every point is graded with quoted evidence from the wargame text, never asserted from memory of having read it
- [ ] The red-team attack was run by an agent with no authorship stake in the wargame, not self-assessed
- [ ] DONE requires BOTH all eight points holding AND one honest attack that failed against the patched version — never either alone
- [ ] No grade was softened to close the loop faster (Anti-Pattern 2) — if in doubt, the grade is FAIL, not "mostly fine"
- [ ] A BLOCKED verdict states exactly which `{{PLACEHOLDER}}` stopped the grade, never a vague "needs more info"
- [ ] At least one recorded attack targets the executor's own pattern-matching, not only external/world-caused failure modes (rubric criterion 8)
- [ ] Where two-plus wargames sit ungraded in the same mission set, the weakest one was graded first — polishing a strong draft while a weak one waits violates Anti-Pattern 6 ("don't run them one by one")
- [ ] The final verdict is exactly one of DONE / NOT-DONE / BLOCKED — no fourth state, no hedged verdict
- [ ] Every FAIL on the grade table names the missing Document Schema section or line, not a vague "needs work"
