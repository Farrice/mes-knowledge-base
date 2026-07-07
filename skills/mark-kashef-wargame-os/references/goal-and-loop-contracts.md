# The /goal Contract and /loop Refinement Prompt — Verbatim Operating System

Source: The Laundry List PDF pp. 26–27 ("RUN IT" section). These are Kashef's exact operating prompts — the machine that runs the missions in bulk. Adapt paths to the mission folder in use (Antigravity convention: `.agent/missions/<name>/{tasks,wargames}/` with `SUCCESS.md` + `LEDGER.md` at the mission root; template at `../assets/wargame-folder-template/`).

## The /goal contract (bulk breadth-first drafting)

> /goal Every mission file in ./tasks has a first-draft wargame in ./wargames, logged in LEDGER.md with a self-grade against SUCCESS.md.
>
> The contract.
>
> 1. Each file in ./tasks is a mission. The mission text is the executor's definition of done. You do not execute any mission this week, you wargame it.
> 2. Recon is read-only. Read anything you need, run nothing that changes state.
> 3. For each mission, write wargames/<NN>.md, the route move by move: expected observation per move, most likely failure with the cause it signals and the counter-move, triggers that reroute, RECON NEEDED marks with the exact settling check, abort conditions, and the executor's verification runs with what pass looks like.
> 4. Draft all ten before polishing any. Breadth first, the refinement loop owns depth.
> 5. After each draft, append a LEDGER.md entry: the mission, the draft's location, and an honest point-by-point self-grade against all eight points of SUCCESS.md.
> 6. A mission with an unfilled {{PLACEHOLDER}} is BLOCKED. Write what you need in LEDGER.md and move on. Never invent the missing input.
> 7. You are operating autonomously. I am not watching in real time. Before you end a turn, check your last paragraph. If it is a plan, a question, or a promise about work not yet done, do that work now instead.
> 8. Stop when all ten missions are DRAFTED or BLOCKED in LEDGER.md.

## The /loop refinement prompt (depth pass)

> /loop 20m Loop through every first draft in ./wargames until each one is properly wargamed to the best of your ability. Properly wargamed means all eight points of SUCCESS.md hold, no exceptions.
>
> Each cycle: grade every draft point by point against SUCCESS.md and log the grades in LEDGER.md. Take the weakest draft and red-team it, play the executor following it blind and attack the route, find the move where it breaks. Patch the break, add the branch that catches it next time, upgrade vague moves with expected observations, convert every unstated assumption to a RECON NEEDED mark with its settling check. Re-grade and log what changed.
>
> A wargame is DONE when it passes all eight points AND one honest attempt to break it fails. Do not soften the grading to finish faster, a draft that passes on paper but dies at first contact is a failure of this loop.
>
> When every wargame is DONE or BLOCKED, or two consecutive cycles improve nothing, post the final ledger and stop the loop.

## Effort economics (PDF p.27, red box)

> "BUDGET THE CAP — ... wargaming is judgment-dense but token-light, no edit loops, no test runs, so the cap goes far. Run it at effort xhigh, this is exactly the work the deep thinking is for. If the cap gets tight, drop the refinement loop to high and keep the drafting pass at xhigh."

- Effort tags per mission card: XHIGH = website, tax, offer, bugs; HIGH = copy, local AI, chatbot, model, competitors, automation.
- Fallback order: drafting pass keeps xhigh; the refinement loop degrades first.
- Antigravity mapping: wargame drafting = highest-tier model / highest effort; refinement loop degrades a tier before the drafting pass ever does (consistent with the Opus-fallback policy: degrade a tier, don't stall).

## Platform landmine (PDF p.16, WATCH OUT box — mission 06)

> "Do not ask the model to explain its thinking or reproduce its reasoning in the output. On Fable that can trigger the reasoning-extraction safeguard and silently route your session to Opus 4.8. Ask for artifacts, findings, quotes, and rewrites, never for the thinking itself."

General rule, not chatbot-specific: wargame orders request ARTIFACTS (routes, moves, checks, quotes), never exposed chain-of-thought.
