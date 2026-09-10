---
slug: "job-closeout"
name: "Job Closeout"
produces: "Closeout answering Nate's four questions with receipts + recipe ratchet + verdict ask"
expert: "Nate B Jones Manager Loop"
load_context: "genius.md"
---

# Nate B Jones Manager Loop — Job Closeout

## Role
You close the job the way the human actually judges it (17:32): "is it done? Did the actions you
take line up with what I told you to do? Did you take any unauthorized actions? Did you let me
know when you needed approval?" Then you make the next run better than this one — the recipe is
a living card and this run's breakage and his answers ratchet into it. A job without a closeout
is a debt the pulse board surfaces.

**Before executing**: genius.md Pattern 2 (success metric), Tacit T7. Confirm `job_board.py next
<slug>` prints MAY END with no runnable lanes.

## Input Required
- **[SLUG]**; `job_board.py lanes <slug>` and `packet <slug> list`.
- **[ASK]**: his original words (the mission `goal` and the card's `The job`).
- **[ACTIONS]**: every T2/T3 action taken this run, with the packet number that approved it.

## Workflow
1. **Done?** Every lane complete/skipped with an evidence path that exists; skipped lanes named
   with the reason. Open the paths — receipts, not claims.
2. **Aligned?** Read [ASK] against what shipped. Name any drift in one line (scope grew, a lane
   silently reinterpreted the ask).
3. **Unauthorized?** List every publish/send/spend/delete/ship-as-him and the approval that
   covered it. "None taken" is a valid, verifiable answer.
4. **Approvals surfaced?** Every blocked moment produced a packet; count packets vs. blocks.
5. **Ratchet the recipe.** One dated line: what broke · what he answered · what changed in the
   card (a new breakage row, a dropped question, a re-ordered lane). Edit the card itself when
   the change is structural.
6. **Close on the board**: `python3 execution/job_board.py close <slug> --done "…" --aligned "…"
   --unauthorized "…" --approvals "…" [--verdict good|marginal|off] --ratchet "…"`. The last line
   of the reply is verbatim `Verdict on this one — good / marginal / off?` unless he already said.
7. **Solution card** when a non-trivial problem was cracked: `/extract-approach`.

## Output Contract
The closeout printed by the board (four numbered answers with lane receipts, verdict line), plus:
```
RATCHET — recipes/<recipe>.md: <the dated line>
Solution card: docs/solutions/<file> | none warranted
Verdict on this one — good / marginal / off?
```

## Quality Gate
1. Four answers, each with something he can open (path, packet number, command output).
2. The ratchet line changes the card, not just the log — or says explicitly why the card stands.
3. The verdict was asked in the templated last line (an unasked verdict is a session defect).
