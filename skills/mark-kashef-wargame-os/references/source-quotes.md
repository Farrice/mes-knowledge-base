# Source Ledger — Wargame OS Extraction

Expert: Mark Kashef (Prompt Advisers / Early AI Dopters). Extraction date: 2026-07-07.
Sources: (A) YouTube nuwlyQXrADg, 13:58, transcript 2,946 words · (B) The Laundry List PDF, 28 pp · (C) fable-wargame-kit files (README, SUCCESS.md, LEDGER.md, tasks/01–10) · (D) 45 video frames incl. full scroll of a worked `01-website.md` wargame.

Labels: VERIFIED = read directly from source artifact in this session · LIKELY = stated by Kashef, plausible, not independently checked · UNCONFIRMED = could not verify.

| Signal (verbatim) | Source | Label | Translation |
|---|---|---|---|
| "War-game order. You are not executing this mission, you are purely war-gaming it." | A (transcript) + C (all 10 task files) | VERIFIED | The mode-switch line — separates simulation from execution at the top of every order. |
| "A language model will know the difference between a plan and a war-game." | A | LIKELY | Naming the frame changes model behavior; the word "wargame" carries adversarial expectations "plan" doesn't. |
| "action, reaction, and counteraction... this is what we call the modern-day agentic loop" | A | VERIFIED | The three-beat unit every move is built from. |
| "every move states its expected observation, exactly what you should see if it worked" | A + C | VERIFIED | The falsifiability discipline — moves are predictions, not intentions. |
| "every fork gets a trigger, if you observe X, take route B" | C (all tasks) | VERIFIED | Judgment stays banked in the wargame; executor only observes. |
| "second, third, fourth order consequence... you decide how far to war-game a certain scenario" | A | VERIFIED | Simulation depth is the human dial; the human sets the consequence horizon. |
| "Your prompt only fills the first box. The wargame drags the other three into the light." | B p.2 + D frame 17 | VERIFIED | The 2×2 epistemics: known knowns / known unknowns / unknown knowns / unknown unknowns. |
| "the map is not the territory... Fable is the first model where I find the quality of the work is bottlenecked by my ability to clarify its unknowns" | D frame 16 (Field Guide post, quoting an Anthropic engineer's article per A) | VERIFIED (on-screen) | The conceptual root: the gap between prompt and reality is "unknowns," and wargaming is unknown-extraction. |
| "Wargamed means it survives contact." | B p.3 | VERIFIED | The standard, in military register (survives contact with reality). |
| "Write it so the executor can run the brief end to end without asking a single question." | C (all tasks) | VERIFIED | Executable-blind is THE bar (SUCCESS point 8). |
| "Draft all ten before polishing any. Breadth first, the refinement loop owns depth." | B p.27 (/goal contract pt 4) | VERIFIED | Breadth-first drafting; depth belongs to a separate graded loop. |
| "A mission with an unfilled {{PLACEHOLDER}} is BLOCKED... Never invent the missing input." | B p.27 (/goal pt 6) | VERIFIED | Blocked-inputs discipline — the ledger surfaces gaps, never papers over them. |
| "A wargame is DONE when it passes all eight points AND one honest attempt to break it fails." | B p.27 (/loop) | VERIFIED | Done = rubric pass + survived red-team. Both, never either. |
| "Do not soften the grading to finish faster, a draft that passes on paper but dies at first contact is a failure of this loop." | B p.27 | VERIFIED | Anti-sycophancy grading rule. |
| "Ask for artifacts, findings, quotes, and rewrites, never for the thinking itself." | B p.16 (WATCH OUT) | VERIFIED (as his claim); the Fable→Opus rerouting mechanism itself | LIKELY | Wargame orders request artifacts, never exposed reasoning. |
| "You pay for the genius once. You keep it forever." | C (README) | VERIFIED | The economics of judgment banking. |
| "Ten tasks. Five days. Make the smartest model you'll ever rent do the thinking while it's still on salary." | B p.28 | VERIFIED | Closing frame — frontier access is rented; bank it. |
| "If you cannot quote it, it does not exist." | C (task 06; echoed 07 "If you cannot point to evidence, it does not go in the report", 09 "marked unverified rather than smoothed over") | VERIFIED | Evidence-or-absent rule inside mission briefs. |
| "Design tokens fixed now so the executor never chooses" | D frames 22–31 (01-website.md) | VERIFIED (on-screen) | Worked-example proof: every aesthetic/judgment choice pre-made; executor only executes. |
| "Do the simplest thing that works well. No features, no abstractions, nothing beyond this list." | C (task 01) | VERIFIED | Scope clamp written INTO the executor's orders. |
| Effort economics: "Run it at effort xhigh... If the cap gets tight, drop the refinement loop to high and keep the drafting pass at xhigh." | B p.27 | VERIFIED | Budget fallback order: refinement degrades before drafting. |
| Live fan-out: parallel general-purpose agents each wargaming one mission (~34–37k tokens each) | D frame 20 | VERIFIED (on-screen) | Bulk drafting parallelizes cleanly — one agent per mission. |

## Provenance caveats

- The "top Anthropic engineer article" on unknowns (A, ~2:00) is shown on-screen as "A Field Guide to Fable: Finding Your Unknowns" (D frame 16) — author name not visible in frames; attribution to a specific engineer is LIKELY, not verified.
- The worked 01-website.md wargame (D frames 22–31) uses Kashef's own demo business (Prompt Advisers); demo values (Calendly URL, testimonials) are marked as demo IN his own artifact — he models the honest-demo-labeling discipline he preaches.
- Video runtime 13:58; frames 36–45 are sponsor/outro content (Living Course promo) — excluded from methodology extraction.
