# Mark Kashef — Wargame OS: Genius Context

> The new thing in one line: stop asking the frontier model to build or to plan — make it **pre-fight the mission on paper** (move → expected observation → likely failure + the cause it signals + counter-move → fork triggers → RECON NEEDED with the exact settling check → abort conditions → verification runs), so a cheaper model executes the route blind, without asking a single question. "You pay for the genius once. You keep it forever."

**Recognition test**: would Kashef read this wargame and see a route *fought on paper* — or a plan wearing a costume? If you can't name the attack it survived, it isn't wargamed. "Wargamed means it survives contact."

**Layer note**: this skill is the planning layer ABOVE `mark-kashef-agent-orchestration`. Wargaming produces the failure-map; orchestration executes it. Don't blend them into one pass.

---

## The Epistemics (why this beats better prompting)

"Every unknown lives in one of four boxes." Your prompt is only ever **known knowns**. **Known unknowns** you could ask about. But **unknown knowns** ("known to you, never written down" — your tacit context the model lacks) and **unknown unknowns** ("what you never thought to ask") are invisible to prompting *by definition* — you can't prompt for what you don't know you don't know. "Your prompt only fills the first box. The wargame drags the other three into the light." Better prompting only ever improves boxes 1–2; adversarial simulation is the only move that reaches 3–4.

Root metaphor (from the "Field Guide to Fable" post he cites): **the map is not the territory**. The map = your prompts/skills/context; the territory = the codebase, the real world, its actual constraints. Unknowns are the gap. Wargaming shrinks the gap *before* anyone walks the route.

## The Economics (why now, why at all)

- **Judgment arbitrage**: "Make the smartest model you'll ever rent do the thinking while it's still on salary." Frontier judgment is expensive to *generate*, nearly free to *replay*. A wargame is judgment frozen into a durable, portable artifact any model can execute.
- **Token shape**: "Wargaming is judgment-dense but token-light, no edit loops, no test runs, so the cap goes far." The expensive part of AI work is the edit-test-fix churn of execution, not the thinking. Pure thinking is cheap per unit of value.
- **The 80/20 trap it kills**: plans get you "80% of the way there, and then [you] have to go back... to finish executing the 20%, which ironically is typically one of the hardest things to do." The wargame pre-fights the 20%.
- **Antigravity fit**: this is the artifact form of "Fable orchestrates, Sonnet executes," and the mechanism that makes the Opus-fallback tier-degrade policy safe — the intelligence gap is caught by the banked route, not absorbed by the cheaper model.

## Core Mechanism — Supervision Transfer

You cannot transfer judgment to a cheap model. You CAN transfer the *outputs* of judgment: predicted observables. "Every move states its expected observation, exactly what you should see if it worked" — and what you'd see if it didn't. That converts every step from a judgment ("is this right?") into a comparison ("does what I see match what was predicted?"). A cheap model can't judge well, but it matches well. Remove expected observations and the whole thing collapses back into a plan a smart model still has to reason through. **This is the load-bearing element — grade it hardest.**

The unit of work is the pre-run agentic loop: "action, reaction, and counteraction. The AI makes a move, and then reality humbles it by throwing some form of error, and then it has to take some form of counteraction." Wargaming pre-computes that loop so execution collapses to lookup.

## Decision Heuristics (when X → do Y because Z)

1. **When a mission will be executed by a cheaper model/session than the one planning it** → wargame it, don't plan it — because "even with a model as smart as Fable, [a plan] will assume linearity, a blue-sky scenario."
2. **When you hit a choice the executor could get wrong** (design tokens, URLs, framework, tone) → freeze it in the wargame ("Design tokens fixed now so the executor never chooses") — because every choice left downstream is a failure surface.
3. **When recon can't settle an assumption** → mark RECON NEEDED with the *exact* settling check plus both branch routes ("If found, copy into /site/assets/...; if not, inline SVG placeholders, zero `<img>` tags") — because an unknown with a settling check is a deferred decision, not a blocker.
4. **When an input is genuinely missing** ({{PLACEHOLDER}} unfilled) → mark the mission BLOCKED in the ledger, state what you need, move on — "Never invent the missing input" — because one invented input silently breaks the map-territory contract everywhere downstream.
5. **When you have a portfolio of missions** → "Draft all ten before polishing any. Breadth first, the refinement loop owns depth" — because breadth reveals which failure patterns are cross-cutting before you over-fit refinement to one mission's texture, and under a cap it guarantees ten usable-if-rough assets over three perfect ones and seven blanks.
6. **When refining** → take the WEAKEST draft, "play the executor following it blind and attack the route, find the move where it breaks," patch, re-grade — because quality is proven by attack, not asserted. DONE = all 8 points hold AND one honest break attempt failed.
7. **When simulation could recurse forever** → the human sets the consequence horizon ("second, third, fourth order... you decide how far to war-game a certain scenario") — because unbounded simulation burns tokens on scenarios that never fire.
8. **When the executor model is known** → tailor the wargame to its dialect via docs/system card ("tailor this war game to exactly how Sonnet 5 would execute it") — because executors differ, and a route in the recipient's dialect fails less.
9. **When tempted to ask the wargamer to show its reasoning** → don't. "Ask for artifacts, findings, quotes, and rewrites, never for the thinking itself" — because on reasoning models this can silently reroute the session mid-run.
10. **When budget tightens** → degrade the refinement loop first, protect the drafting pass ("drop the refinement loop to high and keep the drafting pass at xhigh") — because drafting is where the judgment density lives.

## The Document Schema (what a wargame file contains, in order)

1. **Mission spec** — problem, audience, CTA/definition of done, all ambiguous choices pre-frozen.
2. **RECON NEEDED block** — numbered items, each with the exact runnable check + both branch routes.
3. **Moves 1–N** — each: Move / Expect (observable) / Fail (+ the cause it signals) / Counter-move / Trigger (reroutes).
4. **Abort conditions** — observable states where the executor stops and flags rather than improvises.
5. **Verification runs** — which checks, when, and what pass looks like for each.

Worked exemplar: `references/` source ledger + the 01-website wargame captured in `extractions/wargame-source/visual-context.md` — including its crown detail: Move 9 predicts a failure *caused by the executor pattern-matching Move 7* (headshot SVG inheriting `aria-hidden="true"` from the icon pattern). Kashef-grade wargames anticipate the executor's own mistakes, not just the world's.

## Quality Rubric (anchored — name the anchor before scoring ≥8)

| # | Criterion | 4 (barely) | 7 (solid) | 10 (Kashef-grade, named anchor) |
|---|---|---|---|---|
| 1 | Expected-observation specificity | "it should work" | observable per move | **"grep matches only ASSUMPTIONS.md"** — string-match, zero judgment |
| 2 | Failure causality | names the failure | failure + counter | **"overflow at 375px → missing flex-wrap → add flex-wrap: wrap"** — failure + cause-signal + counter |
| 3 | Fork determinism | branches described | most forks triggered | **"if site/ lists ANY files, ABORT A1"** — zero judgment calls left |
| 4 | Recon groundedness | assumed from memory | some read-only checks | **R1–R5 pattern** — every unknown has an exact settling command run against real state |
| 5 | Blind-executability | executor would ask | minor stumbles | **"without asking a single question"** — verified by simulating the executor |
| 6 | Honest blocking | invents inputs | flags some gaps | **"BLOCKED... Never invent the missing input"** — every gap surfaced in the ledger |
| 7 | Survived contact | passes on paper | self-graded pass | **recorded attack that failed + patch from one that didn't** (SUCCESS #7) |
| 8 | Anticipates executor's own mistakes | — | predicts task failures | **Move 9/Move 7 aria-hidden inheritance** — predicts the executor's pattern-matching errors |
| 9 | Token discipline | edit-loop bloat | reasonable | **"judgment-dense but token-light"** — pure thinking, no execution churn |

Gut check line: "A draft that passes on paper but dies at first contact is a failure of this loop."

## Anti-Patterns (Kashef would never)

1. **Ship a plan as a wargame** — linear phases, blue-sky, "high degree of success" on paper. The happy path omits exactly the hard 20%.
2. **Soften the grading to finish faster** — the /loop text pre-commits against it verbatim.
3. **Invent a missing input** — a blocked mission honestly flagged beats a "finished" one built on a guess.
4. **Leave a judgment call to the executor** — "No judgment calls left to the executor." Every decision becomes an if-observe-X-then-route trigger.
5. **Ask the model to expose its reasoning** — artifacts, findings, quotes, rewrites only (silent model-swap landmine).
6. **Polish one mission while nine wait** — "Don't Run Them One by One. Run the List."
7. **Recon that mutates state** — "Read anything you need, run nothing that changes state."
8. **Claims without evidence** — "If you cannot quote it, it does not exist" / "Anything you cannot verify gets marked unverified rather than smoothed over."

## Signature Moves (deploy verbatim)

- **The mode-switch open**: "WARGAME ORDER. You are not executing this mission, you are wargaming it." — a model knows the difference between a plan and a wargame; say the word.
- **Name whose orders these are**: "=== THE MISSION BRIEF (the executor's orders, not yours) ===" — separates wargamer from executor in the prompt's own voice.
- **One template, many missions**: identical WARGAME ORDER block across all missions; only the recon-target line changes.
- **End with aborts + verification**: "end with abort conditions, and the verification runs the executor must perform with what pass looks like for each."
- **Active-aggressive mission titles**: Hunt the Bugs, Tear Down the Competition, Refine the High-Ticket Offer — the verb sets the posture.
- **The autonomy tripwire** (for unattended runs): "Before you end a turn, check your last paragraph. If it is a plan, a question, or a promise about work not yet done, do that work now instead."

## Voice / Register (preserve texture — anti-overpolish)

Military register applied literally, never decoratively: "fought on paper," "recon," "counter-move," "abort," "survives contact" (from "no plan survives contact with the enemy"). Rental/salary economics: "while it's still on salary," "pay for the genius once." The surgeon analogy for plan-vs-do: asking a top surgeon to *diagram* the operation vs. having them do it. Teaching cadence is plain-spoken with "So,"/"Now," openers and mid-sentence self-corrections — keep the roughness; "it's not rocket science, but it's really taking the paradigm of planning to its natural extreme."

## Machinery Invisible

Execute the moves; never label them in output. A delivered wargame says "RECON NEEDED: run `ls site/`" — it does not say "per Kashef's supervision-transfer pattern, I am now converting judgment into observables."
