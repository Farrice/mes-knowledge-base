# MES 3.0 Extraction — Nate B Jones: Manager Loop + Recipe Cards

Source: "There Are Jobs You Could Never Give AI. I Gave GPT-6 Astra 20 Hours Of Admin." · youtube ix8SsXjBc7M · 26:58 · pulled 2026-09-09 · transcript: `manager-loop-recipe-cards-transcript.txt` (5,479 words, original-English auto captions; frames talking-head only).
Expert: Nate B Jones | Transcribed by: YouTube captions. Existing expert → **Extension Mode** (8th topic skill beside 7 siblings; `agents/nate-b-jones/` extended).

## CONTENT ASSESSMENT
- Source: 27-minute video essay with a worked example (a household move) and one verbatim starter card.
- Expert: Nate B Jones — AI strategy analyst; prior extractions here: intent engineering, orchestration intelligence, auto-improvement loops, context engineering, trust architecture, taste mastery, agent deployment strategy.
- Domain: agent delegation — the human↔manager-agent relationship for long-horizon work; the post-prompt artifact.
- Depth tier: **Standard** (corpus 5.5k words; enrichment attempted from free same-expert sources — see `skills/nate-b-jones-manager-loop/references/source-quotes.md` § Enrichment; `fidelity: medium`). Not padded.
- Genius patterns: 9 · Hidden knowledge: 9 tacit insights.
- Existing overlap: `spec-first-delegation` (six-line spec = a task-scale card), `/go` + `/mission` (compile/charter, no driving), wargame ledger, `docs/solutions/` cards. Gap filled: the driving loop + the job-scale card + the turn-end rule + harness independence.

## EXECUTIVE SUMMARY
Three shapes of work (task / job / human decision). Jobs need a manager loop: interview once, assign lanes, run the unblocked ones in parallel, batch questions, one point of contact. The artifact that carries a job is a recipe card, not a prompt. What the human judges at the end: done? aligned? unauthorized? approvals surfaced? What stays human: choice, risk, responsibility. The paywalled 23 cards were not used; ours are seeded from Farrice's own recurring jobs.

## 5-LAYER ANALYSIS (condensed; full text in `skills/nate-b-jones-manager-loop/genius.md`)
- **L1 Surface**: manager loop; recipe cards; three questions per job; the four closeout questions; the short starter card.
- **L2 Hidden patterns**: the confidence gap is the bottleneck; nobody writes the spec at need; drudgery is an ordering chain; five capacities changed, not intelligence; the loop manages the human too.
- **L3 Meta-cognition**: shape first, then hand off; wrestle undefined with one model, execute defined with another; supervision by agents is how trust scales.
- **L4 Contradictions**: "agent supervision" vs "I approve the important choices" — resolved by tiering (T1 auto / T2-T3 wait) and packets; "start with the whole job" vs "don't hand it your credit card" — resolved by the card's approvals section.
- **L5 Transcendence**: make the turn-end rule physical (`job_board.py next`); make the card a living ratcheted asset; make the job harness-independent (portable packets) — none of which the video does.

## DEPLOYABLE ASSETS (built this run)
- Skill `skills/nate-b-jones-manager-loop/` — SKILL.md, genius.md, 6 workflows, 5 prompts-v2, 4 references.
- Standard `directives/recipe-card-standard.md`; library `recipes/` (8 seed cards); `execution/recipe_cards.py`; `execution/job_board.py`; hook mode `JOB-HANDOFF` + Stop observer; `execution/verify_job_handoff.py` (31 checks both directions); `/job` front door; dialect lines for Fable and Astra.

## ENRICHMENT (P1.5, free sources only)
Four same-expert videos with full captions (support-inbox agent 2026-07-26; long-running agents 2025-12-09; human-throttle 2025-12-29; task queues 2026-01-14) — quotes in the skill's `source-quotes.md` § Enrichment. They supply the trust/irreversibility framing ("how bad is it if you're wrong and how can you undo it"), the proposed-state rule, queryable action history, and "memory is the system" (why job state lives on disk). The literal manager-loop / recipe-card vocabulary lives in two paid posts (`/p/ai-loop-managers` 2026-06-24, `/p/grab-the-delegation-kit-i-use-to` 2025-12-30) — pointers only.

## VERIFICATION
Quotes byte-checked against the transcript record; timestamps are caption-segment starts. UNCONFIRMED: none in the primary source. Paid guide contents: not accessed, not inferred.
