# The 8-Point Standard — What "Properly Wargamed" Means

Source: `SUCCESS.md` from Kashef's fable-wargame-kit (verbatim points, annotated for graders). A wargame passes only when ALL eight hold. "A wargame is DONE when it passes all eight points AND one honest attempt to break it fails." (Laundry List p.27)

| # | The point (verbatim) | What it catches | How to grade it |
|---|---|---|---|
| 1 | "Every move states its expected observation, exactly what you should see if the move worked." | Moves written as intentions ("set up the hero section") instead of falsifiable predictions. | For each move ask: could an executor compare reality against this line and get a yes/no? Vague = fail. |
| 2 | "Every move carries its most likely failure, the cause that failure signals, and the counter-move." | Blue-sky plans. The failure must name its *cause-signal* — what the failure tells you about the world — not just "might not work." | Three parts per move: failure, cause it signals, counter-move. Missing any part = fail. |
| 3 | "Every fork has a trigger. If you observe X, take route B. No judgment calls left to the executor." | Branches that say "use your judgment" or "if appropriate." The executor is assumed cheaper — judgment stays banked in the wargame. | Scan for conditional language without an observable trigger. Any decision the executor must *decide* rather than *observe* = fail. |
| 4 | "Every assumption recon could not settle is marked RECON NEEDED with the exact check that settles it." | Silent assumptions. The check must be exact — a shell command, a URL to open, a file to read — not "verify this." | Each RECON NEEDED carries a runnable settling check with branch logic for both outcomes (see 01-website exemplar: R1–R5 each name the command AND both routes). |
| 5 | "Abort conditions exist, the moments to stop and flag rather than improvise." | Executors improvising past a blocker. | At least one abort condition, each tied to an observable state (e.g., "if site/ lists ANY files, ABORT A1"). |
| 6 | "Verification is spelled out, which runs the executor performs, when, and what pass looks like for each." | "Test it when done." Verification without a pass-definition is theater. | Each verification run names the action, the timing, and the observable pass state. |
| 7 | "It has survived a red-team pass. The doc records the attack that failed against it, and the patch born from the attack that did not." | First drafts shipping as final. The red-team evidence lives IN the document. | Look for the recorded attack + patch. No record = point 7 fails even if the wargame "seems" solid. |
| 8 | "It is executable blind. A mid-tier model could run the mission end to end without asking a single question." | The summary bar. Points 1–7 are the mechanism; 8 is the outcome. | Read as the executor: every question you'd need to ask is a hole. One question = fail. |

## Grading discipline (from the /loop contract)

- Grade point by point, log grades in the ledger — never a single holistic score.
- "Do not soften the grading to finish faster, a draft that passes on paper but dies at first contact is a failure of this loop." (p.27)
- Take the WEAKEST draft first each refinement cycle.
- Stop condition: every wargame DONE or BLOCKED, or two consecutive cycles improve nothing.
