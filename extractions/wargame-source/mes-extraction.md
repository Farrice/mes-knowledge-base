# Mark Kashef — WARGAMING Methodology (MES 3.0 Deep-Tier Expansion)

## Content Assessment

- **Source**: YouTube video (~13:58) + 44 extracted frames + "The Laundry List" PDF (28 pp) + shipped kit (README, SUCCESS.md, LEDGER.md, 10 task files, worked `01-website.md` output).
- **Expert**: Mark Kashef (Prompt Advisers / Early AI Dopters) — AI orchestration practitioner.
- **Domain**: Pre-execution adversarial simulation — "wargaming" a mission on paper with a frontier model so a cheaper model executes it blind.
- **Depth Tier**: Deep — multi-artifact, a complete worked exemplar on disk, a formal 8-point standard, and a two-command operating system (`/goal`, `/loop`).
- **Existing Overlap**: `mark-kashef-agent-orchestration` (assembly lines, tollbooths, phase-gating, circuit breakers, files-are-truth). Wargaming is a NEW upstream layer — it *produces the plan* the orchestration layer executes. Connections flagged inline as **[→ORCH]**.

**The new thing in one line**: Kashef stops using the frontier model to *build* and starts using it to *pre-fight* — converting its intelligence into a portable failure-map (move → expected observation → likely failure + cause + counter-move → fork trigger → RECON NEEDED → abort → verification run) that a cheap model runs without asking a single question.

---

## Genius Patterns

### 1. The Third Move (Judgment Arbitrage)
- **The thinking**: When a premium model is about to get expensive, the crowd bifurcates into panic-spend or under-use. Kashef's move is to extract the model's *judgment* as a durable asset before the price changes, then rent cheaper execution against it forever. He is arbitraging the gap between what intelligence costs to *generate* vs. to *replay*.
- **Anchor**: *"the goal of this video is I want to give you a third move. One that takes the single most valuable thing that I find about Fable 5 and allows you to use it well after it's out of your subscription."* Also PDF p.28: *"Make the smartest model you'll ever rent do the thinking while it's still on salary."*
- **Why it works**: Plans decay; failure-maps don't. A wargame captures the reasoning, not the artifact, so it survives the model's departure.
- **Transfer**: Any expiring-access resource — a departing consultant, an expensive API, a limited trial. Extract the judgment, not the deliverable.

### 2. Don't Ask For Plans, Ask For Wargames
- **The thinking**: Anthropic's own guidance says use the frontier model as an *executor* fed an Opus plan. Kashef inverts twice: don't use it to execute (too expensive), and don't ask it for a *plan* (a plan assumes success). Ask it to fight the mission adversarially.
- **Anchor**: *"the fix isn't asking for better plans. It's actually not asking for plans at all."* And: *"a language model will know the difference between a plan and a war-game."*
- **Why it works**: *"even with a model as smart as Fable, [a plan] will assume linearity, a blue-sky scenario... it doesn't really demonstrate what could happen if things don't go as planned."* A plan is the happy path; a wargame is every path.
- **Transfer**: Any high-stakes execution where the cost of a wrong turn mid-run exceeds the cost of simulating it first — surgery prep, incident runbooks, launch sequences.

### 3. Action → Reaction → Counteraction (The Agentic Loop, Pre-Run)
- **The thinking**: Kashef models execution as a three-beat combat loop and forces the frontier model to pre-play all three beats *on paper* so the cheap model doesn't have to reason them live.
- **Anchor**: *"You have action, reaction, and counteraction. So, the AI makes a move, and then reality humbles it by throwing some form of error, and then it has to take some form of counteraction... this is what we call the modern-day agentic loop."*
- **Why it works**: The agentic loop normally runs at execution time (expensive, live, error-prone). Wargaming *pre-computes* the loop so execution collapses to lookup, not reasoning. **[→ORCH: this is the assembly-line handoff moved upstream — the failure resolution happens before the executor ever runs.]**
- **Transfer**: Any place where reasoning-at-runtime is costlier than reasoning-ahead — trading systems, ops automation, negotiation prep.

### 4. Expected Observation Is The Load-Bearing Element
- **The thinking**: Every move must declare *exactly what you'd see if it worked* AND what you'd see if it didn't. This is the single mechanic that makes a blind executor possible — it converts judgment ("is this right?") into a comparison ("does what I see match what was predicted?").
- **Anchor**: *"every move states its expected observation, exactly what you should see if it worked, and then conversely, what it should see if it didn't work."* Worked example (`01-website.md`, Move 1): *"Expect = site/ and inputs/ absent, grep matches only ASSUMPTIONS.md."*
- **Why it works**: A cheap model can't *judge* well but it can *match* well. Expected-observation turns every step into a pass/fail assertion the executor checks itself against — no taste required.
- **Transfer**: Test-driven development, checklist medicine, any handoff to a less-capable operator. Predict the observable, and supervision becomes verification.

### 5. Every Fork Gets A Trigger (No Judgment Calls Left)
- **The thinking**: Branches aren't described, they're *triggered*. The condition that selects the branch is written as an observable, so the executor never decides — it matches and routes.
- **Anchor**: *"every fork gets a trigger, and if you observe X, then you should... take this route if this happens versus that."* SUCCESS.md #3: *"Every fork has a trigger. If you observe X, take route B. No judgment calls left to the executor."* Worked: Move 1 *"if site/ exists, ABORT A1; if inputs/ exists, reroute to R3's real-content path in Moves 8–9."*
- **Why it works**: Judgment is where cheap models fail. Converting every decision into an if-observed-then-route rule removes the failure surface entirely.
- **Transfer**: Runbooks, decision trees, delegated authority — anywhere you hand control to someone you can't supervise in real time.

### 6. RECON NEEDED With The Exact Settling Check
- **The thinking**: Unresolvable assumptions aren't guessed and aren't hand-waved — they're tagged with the *precise command or check* that would resolve them, so the executor settles them itself at runtime.
- **Anchor**: *"assumptions that your reconnaissance or due diligence could not resolve, basically flag it to us."* SUCCESS.md #4: *"marked RECON NEEDED with the exact check that settles it."* Worked (R2): *"find ... -iname *.png ... returned nothing. If found, copy into /site/assets/... if not, inline SVG placeholders, zero <img> tags."*
- **Why it works**: An unknown with a settling check is not a blocker — it's a deferred, self-resolving decision. The wargame stays executable even where the wargamer lacked information. **[→ORCH: cousin of files-are-truth — resolve against physical state, never a claim.]**
- **Transfer**: Spec-writing under uncertainty, delegation with incomplete info, research protocols where later data resolves earlier branches.

### 7. Breadth-First, Depth Later (Draft All Ten Before Polishing Any)
- **The thinking**: Get every mission to first-draft *before* refining any one. Polishing mission 1 to perfection before starting mission 2 is the trap — breadth is a separate pass from depth, owned by a separate command (`/loop`).
- **Anchor**: `/goal` contract #4: *"Draft all ten before polishing any. Breadth first, the refinement loop owns depth."* Spoken: *"draft all 10 before polishing any."*
- **Why it works**: Under a token/time cap, breadth-first guarantees ten usable-if-rough assets rather than three perfect ones and seven blanks. It also surfaces cross-mission patterns you'd miss going deep on one. **[→ORCH: parallel fan-out — the `/goal` run *"fan[s] out a series of parallel agents to go and execute each one of those tasks at the same time."*]**
- **Transfer**: Any portfolio of work under a deadline — never let perfect-on-one starve the rest.

### 8. Never Invent The Missing Input (The Ledger Discipline)
- **The thinking**: The ledger's job is to expose blockers honestly, not paper over them. An unfilled placeholder is *definitionally* a block — the model writes what it needs and moves on, and is explicitly forbidden from fabricating the value.
- **Anchor**: `/goal` contract #6: *"A mission with an unfilled {{PLACEHOLDER}} is BLOCKED. Write what you need in LEDGER.md and move on. Never invent the missing input."* Spoken: *"if it's war gaming and there's some form of variable that's undefined, it should populate a little parentheses variable placeholder for something that it needs your input on."*
- **Why it works**: A wargame built on invented inputs *"passes on paper but dies at first contact."* Honest blocking preserves the trust that the map matches the territory. **[→ORCH: the Human Tollbooth, relocated — instead of pausing execution for approval, it pauses the *simulation* to flag a missing input.]**
- **Transfer**: Estimating, scoping, any handoff document — a labeled gap is an asset; a silent guess is a landmine.

### 9. The Ledger Never Softens Its Own Grade
- **The thinking**: The refinement loop must red-team honestly and refuse to lower the bar to finish faster. A wargame is DONE only when it passes all eight points AND survives one genuine break attempt.
- **Anchor**: `/loop`: *"Do not soften the grading to finish faster, a draft that passes on paper but dies at first contact is a failure of this loop."* SUCCESS.md #7: *"It has survived a red-team pass. The doc records the attack that failed against it, and the patch born from the attack that did not."*
- **Why it works**: Self-grading systems drift toward leniency to reach "done." Naming the failure mode ("dies at first contact") pre-commits the model against its own laziness. **[→ORCH: adversarial refine / circuit-breaker — quality is proven by attack, not asserted.]**
- **Transfer**: Any self-evaluating loop — code review bots, self-critique chains, QA gates. Build the leniency-resistance into the instruction.

### 10. Second/Third/Fourth-Order Consequences (You Set The Depth)
- **The thinking**: A simulation needs a defined end. Kashef makes the *human* decide how many orders of consequence deep to fight each scenario — the wargamer doesn't recurse infinitely, the operator scopes the blast radius.
- **Anchor**: *"as with any simulation, you need to define an end. So, I like to call this a second, third, fourth order consequence... this is the part where you come in and you decide how far to war-game a certain scenario."*
- **Why it works**: Wargaming has diminishing returns past a certain depth; unbounded simulation burns tokens on scenarios that never fire. Human-set depth keeps it judgment-dense but token-light.
- **Transfer**: Risk modeling, scenario planning, threat modeling — depth is a dial the operator owns, not a default the tool picks.

### 11. Recon First, Read-Only (Route Built From Reality, Not Memory)
- **The thinking**: Before fighting anything on paper, the model reads the actual terrain — reference site, machine specs, transcripts, repo — but changes *nothing*. The route is grounded in observed state.
- **Anchor**: template: *"Recon first, read-only"* and `/goal` #2: *"Recon is read-only. Read anything you need, run nothing that changes state."* Worked: the entire RECON NEEDED block runs real shell greps/finds against the repo.
- **Why it works**: A wargame built from training memory hallucinates the territory. Grounding recon in read-only reality is what lets the map match. **[→ORCH: files-are-truth applied to the *planning* phase.]**
- **Transfer**: Any plan that must survive contact — audit before advising, read the codebase before proposing, observe before prescribing.

### 12. Tail The Executor To The Model (Model-Card Tailoring)
- **The thinking**: The wargame should be geared to *the specific model that will run it*. Kashef spins a guide sub-agent to read the executor's system/model card so the route matches that model's actual behavior.
- **Anchor**: *"you could take this to the next level by tagging a Claude Code Guide agent and then say, 'I want you to tailor this war game to exactly how Sonnet 5 would execute it'... spin up a sub agent or sub agents to go through all the documentation, maybe the system card of that model."*
- **Why it works**: Executors differ (context handling, formatting, capability gaps). A route tuned to the actual executor's dialect fails less. **[→ORCH: direct reuse of Model-Card Dialect Migration.]**
- **Transfer**: Any handoff spec — write it in the recipient's dialect, not the author's.

---

## Hidden Knowledge (Tacit / Unstated)

- **Why "expected observation" is load-bearing, not just nice**: The entire method is a *supervision-transfer* trick. The frontier model has judgment; the cheap model doesn't. You cannot transfer judgment, but you *can* transfer the *outputs* of judgment — the predicted observables. Every "expect X" is a frozen judgment call the executor replays as a string-match. Remove expected observations and the whole thing collapses back into "a plan a smart model still has to reason through."

- **Why breadth-first is epistemically correct, not just efficient**: Depth-first on mission 1 over-fits your refinement to one problem's failure texture before you've seen the others. Ten rough drafts reveal which failure patterns are *cross-cutting* (worth systematizing) vs. mission-specific. Breadth-first is how you learn the *shape* of your whole risk surface before investing in any corner of it.

- **The 2×2's real claim**: *"Your prompt only fills the first box. The wargame drags the other three into the light."* The epistemics: your prompt is only ever **known knowns**. **Known unknowns** ("gaps you can name") you could ask about. But **unknown knowns** (*"known to you, never written down"* — your tacit context the model lacks) and **unknown unknowns** (*"what you never thought to ask"*) are invisible to prompting *by definition* — you can't prompt for what you don't know you don't know. Wargaming is the only move that reaches them, because the model's adversarial simulation surfaces failure modes *you* never thought of. This is why it beats better prompting: better prompts can only ever improve box 1 and 2.

- **Why the ledger never invents inputs (the trust chain)**: The wargame's entire value proposition is "the map matches the territory." One invented input silently breaks that contract everywhere downstream — the executor runs confidently into a wall. Honest blocking keeps the map *trustworthy*, which is worth more than the map being *complete*. A blocked mission you know is blocked beats a "finished" mission built on a guess.

- **Why wargaming is token-light despite being judgment-dense**: PDF: *"wargaming is judgment-dense but token-light, no edit loops, no test runs, so the cap goes far."* The insight: the expensive part of AI work is the *edit-test-fix churn* of execution, not the thinking. Wargaming does pure thinking with zero execution churn, so a small budget buys a lot of judgment — which is exactly the resource you're trying to bank before the price changes.

- **The reasoning-extraction landmine (platform-specific tacit knowledge)**: PDF WATCH OUT (mission 06): *"Do not ask the model to explain its thinking or reproduce its reasoning in the output. On Fable that can trigger the reasoning-extraction safeguard and silently route your session to Opus 4.8. Ask for artifacts, findings, quotes, and rewrites, never for the thinking itself."* This is a subtle operating truth: on a reasoning model, requesting chain-of-thought can cause an *invisible model swap* mid-session — corrupting the very judgment you're paying to bank. Ask for the *artifact of thought*, never the thought.

- **Effort economics (the cap-management dial)**: *"Run it at effort xhigh, this is exactly the work the deep thinking is for. If the cap gets tight, drop the refinement loop to high and keep the drafting pass at xhigh."* Tacit rule: the *drafting* pass is where depth matters most — protect it at xhigh, sacrifice refinement depth first. XHIGH missions (Website, Tax, Offer, Bugs) are the least-forgiving, highest-stakes ones.

- **The autonomy self-check**: `/goal` #7: *"I am not watching in real time. Before you end a turn, check your last paragraph. If it is a plan, a question, or a promise about work not yet done, do that work now instead."* Tacit: unattended agents drift toward *promising* work instead of *doing* it. The last-paragraph check is a cheap tripwire against deferral.

---

## Hall of Fame Exemplars

### Exemplar 1: The `01-website.md` Wargame (the crown artifact)
- **Context**: The frontier model wargames "build the marketing site" so Sonnet executes it blind. This is the fullest demonstration of the method — a real document on disk, scrolled top to bottom in the video.
- **The example (structure, verbatim from visual-context)**: Mission spec fixes design tokens *"so the executor never chooses"* (`Background #ffffff, text #1a1a2e, accent deep blue #1e3a8a...`). Then a **RECON NEEDED** block of five items each with the exact shell command AND the branch: *"R2, brand assets... `find ... -iname *.png...` returned nothing. If found, copy into /site/assets/... if not, inline SVG placeholders, zero `<img>` tags."* Then **Moves 1–11**, each Move/Expect/Fail/Trigger: *Move 6 — social proof strip, `Fail case = fixed-width stat items overflowing 375px, signaling missing flex-wrap, counter-move = add flex-wrap: wrap.`* *Move 9 — the About headshot SVG must be `role="img" aria-label=...`, Fail case = it "incorrectly inherits aria-hidden='true' from Move 7's icon pattern — counter-move = it must be labeled, not hidden."* *Move 10 — FAQ, Fail case = "temptation to build a JS accordion, flagged as scope creep, counter-move = delete the JS, keep native details/summary."*
- **What makes it excellent**: The failures are *specific and physical* — "overflowing 375px," "inherits aria-hidden from Move 7." Move 9's fail case even predicts a failure *caused by the executor pattern-matching Move 7* — the wargamer anticipates the executor's own likely mistake. Demo content is honestly tagged (`<!-- DEMO CONTENT -->`) and Move 8's counter-move is *"the final summary must explicitly list every demo-content section."* This is a document that could genuinely be run without one question.

### Exemplar 2: The `/goal` Contract (the breadth-first bulk-draft engine)
- **Context**: One command that makes the frontier model draft all ten wargames in parallel, self-graded, blocked-not-guessed.
- **The example (verbatim, PDF pp.26-27)**: 8 numbered points. #1 *"The mission text is the executor's definition of done. You do not execute any mission this week, you wargame it."* #4 *"Draft all ten before polishing any. Breadth first, the refinement loop owns depth."* #5 *"append a LEDGER.md entry... an honest point-by-point self-grade against all eight points of SUCCESS.md."* #6 *"Never invent the missing input."* #7 the autonomy self-check. #8 *"Stop when all ten missions are DRAFTED or BLOCKED."*
- **What makes it excellent**: It encodes an entire operating discipline into eight lines — parallelism, honest grading, block-don't-guess, unattended autonomy, and a hard stop condition. Every clause closes a specific failure mode of autonomous agents.

### Exemplar 3: The `/loop` Refinement Command (the honest red-team)
- **Context**: Iterative depth pass that red-teams the weakest draft each cycle.
- **The example (verbatim, PDF p.27)**: *"Take the weakest draft and red-team it, play the executor following it blind and attack the route, find the move where it breaks. Patch the break, add the branch that catches it next time, upgrade vague moves with expected observations, convert every unstated assumption to a RECON NEEDED mark... A wargame is DONE when it passes all eight points AND one honest attempt to break it fails... When every wargame is DONE or BLOCKED, or two consecutive cycles improve nothing, post the final ledger and stop."*
- **What makes it excellent**: "Play the executor following it blind and attack the route" — the refinement *simulates the cheap model's experience* to find where the map fails the territory. The DONE condition requires a *failed* break attempt (proof by surviving attack), and the stop condition ("two consecutive cycles improve nothing") prevents infinite polishing.

### Anti-Exemplar: The Blue-Sky Plan
- **What mediocre looks like**: A phased plan that *"break[s] down exactly how it could build this endpoint"* — logical, linear, high apparent success probability.
- **Why it fails**: *"it doesn't really demonstrate what could happen if things don't go as planned."* It gets you *"80% of the way there, and then [you] have to go back to something like Opus 4.8... to finish executing the 20%, which ironically is typically one of the hardest things to do."* The plan optimizes for looking complete, not for surviving contact.

---

## Signature Moves

- **Write the WARGAME ORDER preamble, swap only the recon line** → Reuse the identical instruction block across every mission; change only the mission-specific opening. *"every other prompt would look very similar, where you'd have the same template at the top, you'd outline the mission briefs down below."* **Deploy when**: standing up any multi-mission wargame set.
- **Separate the wargamer from the executor in the prompt's own voice** → *"=== THE MISSION BRIEF (the executor's orders, not yours) ==="* — the frontier model is told its output is orders for someone else, not instructions for itself. **Deploy when**: writing any handoff spec — name whose orders these are.
- **Fix the ambiguous choices so the executor never picks** → Pre-decide design tokens, URLs, fonts *in the wargame* (`Design tokens fixed now so the executor never chooses`). **Deploy when**: any choice a cheap model might get wrong is cheaper to freeze upstream.
- **End every wargame with abort conditions + verification runs** → *"end with abort conditions, and the verification runs the executor must perform with what pass looks like for each."* **Deploy when**: closing any route — define both the "stop and flag" lines and the "prove it worked" checks.
- **Give active, slightly aggressive mission titles** → File slug `competitors.md` → *"Tear Down the Competition"*; `tax.md` → *"The Tax Strategy Review"*; also *"Hunt the Bugs," "Refine the High-Ticket Offer," "Map the Automation."* Military register throughout. **Deploy when**: naming missions — the verb sets the posture.
- **Tag the depth dial to the human** → Explicitly hand the operator the "how far do we war-game this scenario" decision rather than defaulting. **Deploy when**: any simulation that could recurse — make depth an operator choice.
- **Run the list, not the items** → PDF: *"Don't Run Them One by One. Run the List."* Fire `/goal` once to fan out all ten in parallel. **Deploy when**: you have a portfolio of independent simulations.

---

## Quality Rubric — Is This Wargame Kashef-Grade?

Built ON SUCCESS.md's 8 points (expected observation / failure+cause+counter / fork triggers / RECON NEEDED / abort / verification / survived red-team / executable blind), adding what the standard implies but doesn't state:

| # | Criterion | Score 4 (barely) | Score 7 (solid) | Score 10 (Kashef-grade) |
|---|-----------|------------------|-----------------|--------------------------|
| 1 | **Expected-observation specificity** | Vague ("it should work") | Observable per move | Physical & exact ("site/ and inputs/ absent, grep matches only ASSUMPTIONS.md") — a string-match, not a judgment |
| 2 | **Failure causality** | Names the failure | Failure + counter-move | Failure + *the cause it signals* + counter-move ("stat items overflow 375px → missing flex-wrap → add flex-wrap: wrap") |
| 3 | **Fork determinism** | Branches described | Most forks triggered | Zero judgment left — every fork is if-observe-X-then-route, no "use your best guess" anywhere |
| 4 | **Recon groundedness** | Assumed from memory | Some read-only checks | Every unknown = RECON NEEDED + the *exact* settling command, run against real state |
| 5 | **Blind-executability** | Executor would ask questions | Runs with minor stumbles | *"end to end without asking a single question"* — verified by simulating the executor blind |
| 6 | **Honest blocking** | Invents missing inputs | Flags some gaps | Every `{{PLACEHOLDER}}` = BLOCKED in ledger, need stated, nothing fabricated |
| 7 | **Survived contact (red-team)** | Passes on paper only | Self-graded pass | Records an attack that *failed against it* + a patch born from one that didn't. *"A draft that passes on paper but dies at first contact is a failure."* |
| 8 | **Anticipates the executor's own mistakes** | — | Predicts task failures | Predicts failures *caused by the executor's pattern-matching* (Move 9 inheriting Move 7's aria-hidden) |
| 9 | **Token-discipline** | Bloated, edit-loops | Reasonable | Judgment-dense, token-light: pure thinking, no test-run churn, xhigh where stakes justify it |

**The one-line gut check**: *"Wargamed means it survives contact."* If you can't name the attack it survived, it isn't wargamed — it's a plan wearing a costume.

---

## Voice / Register Notes

- **Military / combat register throughout, applied literally**: "WARGAME ORDER," "fight the mission on paper move by move," "recon," "abort conditions," "red-team," "the route it will follow," "counter-move," "survives contact." The metaphor is load-bearing, not decorative — *"survives contact"* directly borrows *"no plan survives contact with the enemy."*
- **Active-aggressive mission verbs**: "Hunt the Bugs," "Tear Down the Competition," "Refine the Offer," "Map the Automation." Neutral file slugs get upgraded to combat postures.
- **"Fought on paper" as the signature phrase**: *"the site build fought on paper," "make it fight the build on paper," "fight the mission on paper move by move."* The verb *fight* (never "plan," never "outline").
- **Plain-spoken teaching cadence, not polished**: conversational, mid-sentence self-corrections, "So," and "Now," openers, "it's not rocket science, but it's really taking the paradigm of planning and taking it to its natural extreme." Preserve this texture — do not tidy into essay prose.
- **Rental/salary economic framing**: *"the smartest model you'll ever rent... while it's still on salary," "You pay for the genius once. You keep it forever," "purchasing a general's judgment once."*
- **Surgeon analogy for the plan-vs-do inversion**: *"the equivalent of bringing a top-rated surgeon and asking them to write you a diagram of how you would operate on someone versus actually having them do it."*

---

## Anti-Patterns (What Kashef Rules Out)

- **Plans-as-wargames** — a linear phased plan that *"assume[s] linearity, a blue-sky scenario"* and gets you 80% there. A plan is the happy path; the hard 20% is exactly what it omits.
- **Softened grading to reach "done"** — *"Do not soften the grading to finish faster."* The DONE bar requires surviving a real attack, not a lenient self-pass.
- **Invented placeholders** — *"Never invent the missing input."* A blocked mission honestly flagged beats a "finished" one built on a guess.
- **Reasoning-extraction requests** — *"Do not ask the model to explain its thinking... Ask for artifacts, findings, quotes, and rewrites, never for the thinking itself"* (can trigger a silent model swap on Fable).
- **One-by-one polishing** — *"Don't Run Them One by One. Run the List."* / *"Draft all ten before polishing any."* Perfecting one mission starves the other nine.
- **Leaving judgment to the executor** — *"No judgment calls left to the executor."* Every decision must be pre-converted to an observable trigger; a cheap model asked to judge is a cheap model about to fail.
- **Recon that changes state** — *"run nothing that changes state."* Reconnaissance is strictly read-only; a wargame must never mutate the territory it's mapping.
- **Claims not backed by evidence** — across missions: *"If you cannot quote it, it does not exist"* (chatbot), *"If you cannot point to evidence, it does not go in the report"* (bugs), *"Anything you cannot verify gets marked unverified rather than smoothed over"* (competitors). **[→ORCH: files-are-truth, generalized to all recon.]**
- **Idle agents left running** — implied by **[→ORCH]** graceful-shutdown; the `/loop` stops when "two consecutive cycles improve nothing" rather than burning tokens indefinitely.

---

## Connections To Existing Kashef Skills (not re-extracted)

Wargaming is the **planning layer above** `mark-kashef-agent-orchestration`, not a replacement. The orchestration skill executes; wargaming produces the failure-map the execution follows. Direct reuses: parallel fan-out (`/goal` = agent-team fan-out), files-are-truth (recon read-only), Human Tollbooth (block-don't-guess = a simulation-time tollbooth), circuit-breaker red-teaming (`/loop`), Model-Card Dialect Migration (tailor the wargame to the executor model), phase-gating (the second/third-order depth dial). **New and non-overlapping**: the 2×2 unknowns epistemics, the Move/Expect/Fail/Trigger/RECON/Abort/Verify document schema, the plan-vs-wargame inversion, "expected observation as supervision-transfer," breadth-first drafting as an epistemic (not just efficiency) choice, and the effort-economics cap-management dial.
