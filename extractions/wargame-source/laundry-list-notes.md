# The Laundry List (PDF) — Delta Notes

Source: `/Users/farricecain/Downloads/fable-wargame-kit/The Laundry List.pdf` (28 pages, Mark Kashef's visual companion to the wargame kit). Cross-checked against `fable-last-week/tasks/01-website.md` … `10-automation.md`, `README.md`, `SUCCESS.md`, `LEDGER.md`.

**Headline finding: the 10 mission-brief prompt bodies in the PDF are byte-identical to the `tasks/*.md` files.** No prompt-language deltas exist there. Everything below is what the PDF adds *around* those prompts: the sales/framing layer, the meta-system (the `/goal` contract and `/loop` refinement loop — not present anywhere in the task-file kit), per-mission packaging (domain tags, effort tags, "you get" lines), and one operational safety callout.

---

## 1. Framing / Positioning Language

The deck is built as a pitch-then-payoff sequence before the missions ever appear, then closes with a "how to actually run this" operator's manual. The positioning move: reframe wargaming as *purchasing a general's judgment once, before the API meter changes hands to a cheaper model.*

**Opening beat (pp. 1-5), one screen per idea:**
- Page 1 — title "The Laundry List" over a clothesline illustration, tagged **THE OBJECTION**: *"Anthropic built an executor."* — this is the provocation the whole kit answers (implicit continuation: Fable/Claude is being used as a planner, not a doer).
- Page 2 — **THE UNKNOWNS**: a 2×2 (Known knowns / Known unknowns / Unknown knowns / Unknown unknowns) with the line *"Your prompt only fills the first box. The wargame drags the other three into the light."* This is the conceptual justification for why wargaming beats prompting — a framework not present in the task files, which only assert the *mechanics* (RECON NEEDED, forks, triggers) without ever naming the epistemics behind them.
- Page 3 — **THE STANDARD**: *"Wargamed means it survives contact."* (military-borrowed language — "survives contact with the enemy" is the implicit reference).
- Page 4 — **THE PAYOFF**: *"From outline to battle plan."* with a before/after visual (scribbled outline → annotated battlefield map with flags, X's, warning triangles).

**Per-mission framing (one page each, 10 total):** every mission gets a title that differs from the file's implicit name, a domain tag, an effort tag, and a "→ You get" benefit line that summarizes the wargame's payoff in plain language — none of this exists in the task files, which are prompt-only with no packaging.

| # | PDF title | Domain tag | Effort tag | "You get" line |
|---|---|---|---|---|
| 01 | Build the Website | CODE | XHIGH | the site build fought on paper, every move with its expected observation and failure branch |
| 02 | Write the Copy | COPY | HIGH | the copy mission wargamed, section order, voice risks, and the skeptic pass pre-planned |
| 03 | Set Up Local AI | LOCAL AI | HIGH | your exact machine's local stack wargamed, runtime, models, quants, fallbacks, and the speed checks |
| 04 | The Tax Strategy Review | FINANCE | XHIGH | the tax memo route with every unverifiable number flagged RECON NEEDED before your accountant sees it |
| 05 | Refine the High-Ticket Offer | OFFER DESIGN | XHIGH | the offer rebuild wargamed, buyer counterattacks and their patches already fought |
| 06 | Upgrade the Chatbot From Real Conversations | AI SYSTEMS | HIGH | the chatbot upgrade route, failure patterns quoted, rewrite moves with expected outcomes |
| 07 | Hunt the Bugs | CODE | XHIGH | a bug-hunt wargame, candidate bugs ranked with the exact verification run for each |
| 08 | Build the Financial Model | FINANCE | HIGH | the model build wargamed, formulas, levers, and sensitivity checks pre-fought |
| 09 | Tear Down the Competition | RESEARCH | HIGH | the teardown route, sources to pull, conflicts expected, and the gap-map criteria set |
| 10 | Map the Automation | OPERATIONS | HIGH | the automation blueprint wargamed, checkpoints, what breaks first, and abort lines per phase |

Notice the naming logic: task 04 ("tax.md") becomes "**The Tax Strategy Review**," task 05 ("offer.md") becomes "**Refine the High-Ticket Offer**," task 09 ("competitors.md") becomes "**Tear Down the Competition**." Each title upgrades a neutral file-slug into an active, slightly aggressive verb phrase ("Hunt," "Tear Down," "Map," "Refine") — consistent wargame/military register across all ten, not present in the file names themselves.

Each mission card also states which model plays "cheaper executor" for that mission — this detail lives in the task-file prose too ("a cheaper executor (Sonnet)," "(Opus)," "(a mid-tier model)," "(Claude Code on a cheaper model)") but the PDF's effort tag (HIGH vs. XHIGH) is a layer the task files never expose. The four XHIGH missions are Website, Tax, Offer, and Bugs — the ones the deck implicitly treats as highest-stakes/least-forgiving.

---

## 2. Prompts / Rules That Differ From or Extend the Task Files

**No mission-brief deltas** — every "=== THE MISSION BRIEF ===" block, every "WARGAME ORDER" preamble, matches its `tasks/NN-*.md` counterpart word for word, including placeholder syntax (`{{BUSINESS}}`, `{{ICP}}`, etc.).

**One addition that exists ONLY in the PDF, absent from `tasks/06-chatbot.md`** — a red-boxed "WATCH OUT" callout directly beneath mission 06's brief (p. 16):

> "WATCH OUT — Do not ask the model to explain its thinking or reproduce its reasoning in the output. On Fable that can trigger the reasoning-extraction safeguard and silently route your session to Opus 4.8. Ask for artifacts, findings, quotes, and rewrites, never for the thinking itself."

This is a real operational landmine for anyone running these prompts on Fable specifically: asking a model to show its reasoning can cause an invisible model swap (to Opus 4.8) mid-session. It's placed specifically on the chatbot-transcript mission because that's the one most likely to invite "explain why it failed" phrasing — but the warning is general and would apply to any wargame draft that leans on chain-of-thought exposure.

**The `/goal` contract and `/loop` refinement command — entirely new content, not referenced anywhere in `tasks/`, `SUCCESS.md`, or `LEDGER.md`.** These are the "how you actually operate the kit" instructions promised in the README's closing line ("If you want the full wargaming system including the /goal contract, the refinement loop... check out the Early AI Dopters community") — except the PDF *does* give the exact contract, not a teaser:

Exact `/goal` prompt (p. 26-27):

> "/goal Every mission file in ./tasks has a first-draft wargame in ./wargames, logged in LEDGER.md with a self-grade against SUCCESS.md.
>
> The contract.
>
> 1. Each file in ./tasks is a mission. The mission text is the executor's definition of done. You do not execute any mission this week, you wargame it.
> 2. Recon is read-only. Read anything you need, run nothing that changes state.
> 3. For each mission, write wargames/.md, the route move by move: expected observation per move, most likely failure with the cause it signals and the counter-move, triggers that reroute, RECON NEEDED marks with the exact settling check, abort conditions, and the executor's verification runs with what pass looks like.
> 4. Draft all ten before polishing any. Breadth first, the refinement loop owns depth.
> 5. After each draft, append a LEDGER.md entry: the mission, the draft's location, and an honest point-by-point self-grade against all eight points of SUCCESS.md.
> 6. A mission with an unfilled {{PLACEHOLDER}} is BLOCKED. Write what you need in LEDGER.md and move on. Never invent the missing input.
> 7. You are operating autonomously. I am not watching in real time. Before you end a turn, check your last paragraph. If it is a plan, a question, or a promise about work not yet done, do that work now instead.
> 8. Stop when all ten missions are DRAFTED or BLOCKED in LEDGER.md."

Exact `/loop` prompt (p. 27):

> "/loop 20m Loop through every first draft in ./wargames until each one is properly wargamed to the best of your ability. Properly wargamed means all eight points of SUCCESS.md hold, no exceptions.
>
> Each cycle: grade every draft point by point against SUCCESS.md and log the grades in LEDGER.md. Take the weakest draft and red-team it, play the executor following it blind and attack the route, find the move where it breaks. Patch the break, add the branch that catches it next time, upgrade vague moves with expected observations, convert every unstated assumption to a RECON NEEDED mark with its settling check. Re-grade and log what changed.
>
> A wargame is DONE when it passes all eight points AND one honest attempt to break it fails. Do not soften the grading to finish faster, a draft that passes on paper but dies at first contact is a failure of this loop.
>
> When every wargame is DONE or BLOCKED, or two consecutive cycles improve nothing, post the final ledger and stop the loop."

Also present, a budget note (red box, p. 27) that is operationally important and appears nowhere else in the kit:

> "BUDGET THE CAP — You get Fable at 50% of your weekly limits through July 7, and wargaming is judgment-dense but token-light, no edit loops, no test runs, so the cap goes far. Run it at effort xhigh, this is exactly the work the deep thinking is for. If the cap gets tight, drop the refinement loop to high and keep the drafting pass at xhigh."

This confirms the effort tags on each mission card (HIGH/XHIGH) map to a literal `effort` parameter the user is meant to set when invoking Fable, and gives the fallback order (keep drafting at xhigh, drop only the refinement loop to high if budget-constrained).

---

## 3. Structural / Design Choices

- **Sequence**: hook/objection → conceptual framework (four-box unknowns) → definition of "wargamed" → payoff visual → 10 mission cards (one per page-pair, each with title/tag/illustration/"you get" line/full prompt) → "THE MACHINE" section divider → "RUN IT" operator's manual (folder structure, SUCCESS.md, `/goal`, `/loop`, budget note) → closing black call-to-action bar.
- **Per-mission layout is a fixed template**: number + title + two tags (domain, effort) at top; a single hand-drawn illustration; one italic "→ You get" benefit sentence; then the full WARGAME ORDER + MISSION BRIEF prompt in a monospace box, identical to the task file. Only mission 06 breaks the template with the added WATCH OUT box.
- **The "RUN IT" section is genuinely new operational content** organized as four numbered steps: Step 1 "The folder" (shows the exact directory tree: `tasks/`, `wargames/` starts empty, `SUCCESS.md`, `LEDGER.md`), Step 2 "The standard" (verbatim SUCCESS.md, matches the file exactly), Step 3 "The contract" (the `/goal` prompt above), Step 4 "The refinement loop" (the `/loop` prompt above, plus the budget callout).
- **Sequencing advice embedded in the contract itself**, not stated separately: "Draft all ten before polishing any. Breadth first, the refinement loop owns depth" (contract point 4) — i.e., don't perfect mission 1 before starting mission 2; get all ten to first-draft, then let `/loop` iterate depth across all of them. This is the single clearest piece of process guidance in the whole PDF and it exists nowhere in the individual task files (each of which is mission-agnostic and doesn't reference the other nine).
- **Autonomy instruction embedded in the contract** (point 7): a self-check the agent runs before ending any turn — if the last paragraph is a plan, a question, or a promise instead of completed work, do that work now. This is a directive about *how an autonomous agent should behave mid-session*, distinct from anything in SUCCESS.md's grading criteria.
- **The "watch out" callout format** (red-outlined box, small-caps "WATCH OUT" label) appears exactly once in the deck (mission 06) — suggesting it's reserved for platform-specific gotchas rather than general wargaming advice, and that Kashef considers it high-severity enough to break the template for.

---

## 4. Verbatim Quotable Lines (with page numbers)

1. "Anthropic built an executor." — p.1 (THE OBJECTION)
2. "Every unknown lives in one of four boxes." — p.2
3. "Your prompt only fills the first box. The wargame drags the other three into the light." — p.2
4. "Make it fight the build on paper." — p.3
5. "Wargamed means it survives contact." — p.3 (THE STANDARD)
6. "From outline to battle plan." — p.4 (THE PAYOFF)
7. "→ You get the site build fought on paper, every move with its expected observation and failure branch" — p.5 (mission 01 tagline)
8. "→ You get the offer rebuild wargamed, buyer counterattacks and their patches already fought" — p.13 (mission 05 tagline)
9. "Do not ask the model to explain its thinking or reproduce its reasoning in the output. On Fable that can trigger the reasoning-extraction safeguard and silently route your session to Opus 4.8." — p.16 (WATCH OUT, mission 06)
10. "Ask for artifacts, findings, quotes, and rewrites, never for the thinking itself." — p.16
11. "Don't Run Them One by One. Run the List." — p.26 (RUN IT header)
12. "One /goal contract makes Fable draft a wargame for all ten, breadth first." — p.26
13. "The kit ships this folder ready... an unfilled placeholder means that mission is blocked by definition." — p.26
14. "You do not execute any mission this week, you wargame it." — p.26 (goal contract, point 1)
15. "Draft all ten before polishing any. Breadth first, the refinement loop owns depth." — p.27 (goal contract, point 4)
16. "A mission with an unfilled {{PLACEHOLDER}} is BLOCKED... Never invent the missing input." — p.27 (goal contract, point 6)
17. "I am not watching in real time. Before you end a turn, check your last paragraph. If it is a plan, a question, or a promise about work not yet done, do that work now instead." — p.27 (goal contract, point 7)
18. "A wargame is DONE when it passes all eight points AND one honest attempt to break it fails." — p.27 (loop prompt)
19. "A draft that passes on paper but dies at first contact is a failure of this loop." — p.27
20. "Ten tasks. Five days. Make the smartest model you'll ever rent do the thinking while it's still on salary." — p.28 (closing bar)

---

**Not covered above (confirmed identical to existing files, no delta):** all 10 WARGAME ORDER preambles, all 10 MISSION BRIEF bodies, and the full text of SUCCESS.md as reproduced in Step 2 of the RUN IT section.
