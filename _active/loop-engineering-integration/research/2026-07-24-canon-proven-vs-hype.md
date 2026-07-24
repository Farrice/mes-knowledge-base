# Loop Engineering & Compound Engineering — The Evidenced Canon
**Ticket:** wayfinder research · **Date:** 2026-07-24 · **Standard:** receipt-carrying (URL + who + when). No claim from training memory.
**Labels:** PROVEN = independent or first-party operational receipt with numbers · PLAUSIBLE = named practitioner + mechanism, self-reported or single-source · HYPE = circulating claim without a checkable receipt, or receipt that doesn't support the claim.

---

## TL;DR (10 lines)

1. Two distinct canons got fused in discourse. **Compound engineering** (Every / Klaassen, 2025) = *learning* loop — make the next unit of work cheaper. **Loop engineering** (Steinberger / Cherny / Osmani, June 2026) = *autonomy* loop — replace yourself as the thing that prompts the agent. They compose; they are not the same claim.
2. The single most evidenced primitive in the entire field is not compounding — it's **verification**. "Give the agent a check it can run" is now first-party Anthropic doctrine, shipped as product (`/goal`, Stop hooks, verification subagents).
3. The strongest hard receipt in the field is **OpenAI's harness-engineering post**: ~1M LOC, ~1,500 merged PRs, 3→7 engineers, 5 months, zero hand-written code, explicitly using a "Ralph Wiggum Loop." First-party, dated, specific.
4. The second strongest is **Karpathy's autoresearch → Shopify**: a 630-line loop, independently re-run by Shopify and generalized to **40+ metrics** with an open-sourced repo. That's replication, not marketing.
5. Boris Cherny's canon is *not* "compound engineering." It's **loops + verification + a pruned CLAUDE.md**. He explicitly warns the opposite of "log every failure into your rules file."
6. The 2–3x verification claim is **Cherny's own self-report** — widely quoted, never independently measured. PLAUSIBLE, not PROVEN.
7. Ralph works where success is *mechanically checkable* and the codebase is *greenfield*. Huntley himself says he'd never run it in an existing codebase.
8. The most underrated loops found: **metric-ratchet loops (autoresearch)**, **fresh-context-per-iteration loops**, and **adversarial-reviewer-in-a-separate-context loops**. All three are cheap, all three have receipts, none dominate the threads.
9. The most-cited productivity skeptic (METR) is being **misquoted in both directions**; its 2026 update is directionally positive but METR itself says the number is unreliable.
10. Biggest documented failure mode is not agents going rogue. It's **compound liability**: rules files that grow until the agent stops reading them.

---

## PART 1 — Headline canon: Compound engineering

### 1.1 The core thesis
**Claim:** Every unit of engineering work should make subsequent units *easier*, not harder — inverting the technical-debt curve.
**Receipt:** Dan Shipper + Kieran Klaassen, "Compound Engineering: How Every Codes With Agents," every.to, **2026-01-30**. Loop = **Plan → Work → Review → Compound → Repeat**. "Roughly 80 percent of compound engineering is in the plan and review parts, while 20 percent is in the work and compound." Reported operating result: **five products, each maintained by a single developer**, serving "thousands of daily users." Origin quote (Shipper, Lenny's Podcast, 2025): "Kora — it's Kieran, Nateesh and 15 Claude Code instances."
**Label: PLAUSIBLE.** The *mechanism* is well documented and the products demonstrably exist; the *causal* productivity claim ("a single developer can do the work of five") is a first-party estimate with no measurement methodology attached.

### 1.2 The v2 loop (what changed)
**Claim:** As models got better, the middle of the loop became boring; human attention moved to the ends.
**Receipt:** Kieran Klaassen, "Compound Engineering Gets an Upgrade," every.to, **2026-05-29**. Loop expands to **Ideate → Brainstorm → Plan → Work → Review → Polish → Compound**. Klaassen: "The middle of a lot of work will get automated. But if you want the work to be good, and if you want it to feel like yours, you still need to be there at the beginning and the end."
**Label: PLAUSIBLE** (conceptual evolution; no numbers reported in the piece).

### 1.3 The "Compound" step is the load-bearing one
**Claim:** Steps 1–3 produce a feature; step 4 produces a system that builds features better each time. Mechanics: capture solution → `docs/solutions/` with YAML frontmatter → update CLAUDE.md → create agents → "verify the learning" (would the system catch this automatically next time?).
**Receipt:** every.to (2026-01-30) + Compound Engineering Plugin (`EveryInc/compound-engineering-plugin`; 40+ agents, 30+ slash commands, 35+ skills; command surface renamed `/workflows:*` → `/ce-*` in v3). Klaassen's other stated rules: **80/20 plan-vs-build**, and a **50/50 rule** — "50% of time should be worked on the actual feature and 50% on making sure the meta layer is there" (Compound Engineering Explained, 2026-02-24).
**Label: PROVEN as a shipped, adopted mechanism** (open-source plugin, near-daily releases, 153 releases by May 2026). **PLAUSIBLE as a productivity claim.**

### 1.4 The best independent read
**Receipt:** Will Larson, "Learning from Every's Compound Engineering," lethain.com, **2026-01-19**: "Compound Engineering is two extremely well-known patterns, one moderately well-known pattern, and one pattern that I think many practitioners have intuited but have not found a consistent mechanism to implement... This interplay between the **compound** and **plan** steps creates the compounding mechanism."
**Label: PROVEN framing.** Larson is the receipt that the *novel* part is narrow: the plan-step retrieval of compounded artifacts. Everything else was already table stakes.

### 1.5 The "300–700% faster" number
**Claim:** Compound engineering yields 300–700% development speedups.
**Receipt:** vincirufus.com blog and downstream aggregators. Traced back, the figure measures **code output** (LOC, PRs, features), not business outcomes, and is not sourced to Every.
**Label: HYPE.** Direct counter-receipt: tianpan.co forum teardown (**2026-02-12**) — "A feature built 5x faster that creates 5x the bugs isn't a productivity gain — it's a debt accelerator... compound engineering is a valid **prototyping approach**, not a software engineering methodology."

---

## PART 2 — The Boris Cherny section (explicitly requested)

Cherny is creator/head of Claude Code at Anthropic. Important framing correction: **he does not use the phrase "compound engineering."** Third parties map his practice onto it. His own words are about **loops** and **verification**. "Loop engineering" as a term is also **not his coinage** — it was applied by commentators (Osmani named it in writing).

### 2.1 The canonical statement
**Claim:** "I don't prompt Claude anymore. I have loops that are running. They're the ones that are prompting Claude and kind of figuring out what to do. **My job is to write loops.**"
**Receipt:** Acquired Unplugged (presented by WorkOS), on-stage with Ben Gilbert / David Rosenthal, **2026-06** (video: youtube.com/watch?v=RkQQ7WEor7w). Corroborated at Sequoia AI Ascent 2026 with Lauren Reeder (youtube.com/watch?v=SlGRN8jh2RI, **2026-05-25**).
**Label: PROVEN (as a statement he made).** Whether the *workflow* generalizes is a separate question.

### 2.2 What his loops actually are
**Claim:** `/loop` = cron-scheduled repeat prompts. He runs "dozens."
**Receipt (verbatim, Sequoia AI Ascent transcript):** "this is /loop, and it's just like the coolest thing. It's like the simplest thing that works. All it is is you have Claude use cron to schedule a job for some point in the future, and it's a repeat job... at this point, I have like dozens of loops that are running for stuff. So, I have one that's babysitting my PRs, like fixing CI, auto-rebasing. I have another one that keeps CI healthy... I have another one that grabs feedback from Twitter and kind of clusters it for me every 30 minutes... **I sort of feel like loops are the future at this point.**"
**Label: PROVEN (first-party, transcript).**
Corroboration on scale: Business Insider, **2026-05-13** — Cherny told Sequoia (May 4) he runs "five to 10 sessions," and "usually, every night, I have like a few thousand [agents] that are doing kind of deeper work," relying on **`/loops` (cron, local)** and **Routines (server-side, laptop closed)**.
Specific loop names circulating (`5m /babysit`, `30m /slack-feedback`, `1h /pr-pruner`, `post-merge-sweeper`) come from a secondary aggregator (noqta.tn, 2026-06-19). **Label for the specific names: PLAUSIBLE, not verified to a primary source.**

### 2.3 Verification — his highest-leverage claim
**Claim:** Giving Claude a way to verify its own work improves final quality by **2–3x**.
**Receipt:** Cherny's X/Threads workflow thread, reported by InfoQ **2026-01-10** and VentureBeat **2026-01-04**. Verbatim: "Claude tests every single change I land to claude.ai/code using the Claude Chrome extension. It opens a browser, tests the UI, and iterates until the code works and the UX feels good."
**Label: PLAUSIBLE.** It is a first-party self-report with no measurement method. It is the single most-quoted number in the field and should never be cited as measured.
**But the doctrine is now PROVEN as institutional:** Anthropic's official best-practices doc (code.claude.com/docs/en/best-practices) leads with "**Give Claude a way to verify its work**" — "Claude stops when the work looks done. Without a check it can run, 'looks done' is the only signal available, and **you become the verification loop**." It enumerates four gating strengths: in-prompt → `/goal` condition → **Stop hook (deterministic, blocks turn end; Claude Code overrides after 8 consecutive blocks)** → verification subagent, "so the agent doing the work isn't the one grading it."

### 2.4 His CLAUDE.md practice — and the correction
**Claim (widely repeated):** "Anytime we see Claude do something incorrectly we add it to the CLAUDE.md."
**Receipt:** Cherny, via VentureBeat 2026-01-04 and InfoQ 2026-01-10. He tags `@claude` on coworkers' PRs to fold learnings in via the Claude Code GitHub Action. **Their CLAUDE.md was ~2.5k tokens.**
**The correction most people miss:** Anthropic's own doc says "**Bloated CLAUDE.md files cause Claude to ignore your actual instructions!**" and "If Claude keeps doing something you don't want despite having a rule against it, the file is probably too long and the rule is getting lost... prune it regularly." Cross-source: AI Fire Daily's Boris-method breakdown (2026-04-07) reports a "2026 consensus: keep it under 100 instructions."
**Label: PROVEN that he runs an append loop. PROVEN that append-without-pruning is a documented anti-pattern.** These are the same claim only if you add the pruning half — which most secondary coverage drops.

### 2.5 Other verified Cherny practices
- 5 local Claude sessions (numbered iTerm2 tabs + system notifications) + 5–10 on claude.ai; each local session its own `git checkout`, not branches/worktrees; `--teleport` to move sessions. ~10–20% of sessions abandoned. (InfoQ 2026-01-10) — **PROVEN (first-party report).**
- Plan mode first, then auto-accept edits: "A good plan is really important!" — **PROVEN.**
- Slash commands in `.claude/commands/`; `/commit-push-pr` "dozens of times daily"; subagents for `code-simplifier` and `verify-app`. — **PROVEN.**
- **PostToolUse hook running a formatter** so CI doesn't fail on style. — **PROVEN.** (This is a compilation-loop, not a prompt.)
- Almost never uses `--dangerously-skip-permissions`; allowlists via `/permissions`. — **PROVEN.**
- "Ships 10–30 PRs daily" (Lenny's Podcast, 2026-02-19); "259 PRs in 30 days" (Threads, 2025-12-27); "Claude Code is 100% written by Claude Code" (X, 2026-03-07). — **PLAUSIBLE** (first-party, uncorroborated; and Anthropic's own blog has cautioned that LOC-productivity claims are "almost certainly an overstatement").

### 2.6 What Cherny does NOT say
He does not claim a compounding-returns curve, does not use Every's vocabulary, and does not advocate unbounded autonomy. His loops are narrow, scheduled, and mechanically verifiable. **Anyone citing Cherny as the proof-point for "compound engineering" is citing the wrong person.**

---

## PART 3 — Lesser-known / underrated loops (the real value of this ticket)

### 3.1 The metric-ratchet loop (autoresearch) — most underrated overall
**Claim:** Give an agent (a) one file it may edit, (b) one objectively measurable metric, (c) a fixed time box per experiment, and (d) a git-commit-on-improvement / rollback-on-regression ratchet. Run overnight.
**Receipts:**
- Karpathy released `autoresearch` **2026-03-08** — 630 lines of Python, single GPU, MIT. Agent edits `train.py`, runs a 5-min training run, measures `val_bpb`, commits or rolls back. ~12 experiments/hour, ~100/night.
- Karpathy's own 2-day run: **~700 experiments → ~20 real improvements → 11% training speedup** (time-to-GPT-2 2.02h → 1.80h), and all 20 **transferred** to a larger depth-24 model. (Fortune, **2026-03-17**; philschmid.de, 2026-03-10)
- **Independent replication:** Tobi Lütke (Shopify CEO) ran it overnight on a query-expansion model — **37 experiments in 8 hours, 19% validation improvement, and a 0.8B model beating his hand-tuned 1.6B.** (Fortune 2026-03-17; LinkedIn 2026-03-12)
- **Production generalization:** Shopify Engineering, "Autoresearch isn't just for training models," **2026-04-15** (David Cortés + Lütke): generalized to **40+ metrics across Shopify**, open-sourced as `pi-autoresearch`. Reported: Polaris build time **65% faster**; Liquid parse+render **53% faster with 61% fewer object allocations**; React component mounting 20% faster. System prompt literally says "NEVER STOP LOOPING."
- **Their own caveat, verbatim:** results can be "somewhat overfit"; agents produce "ugly hacks" (e.g. deleting files); manual review needed to "throw away all the hacks and keep the good stuff."
**Label: PROVEN.** This is the only loop in the whole survey with an independent third-party replication *and* a first-party engineering-blog production writeup *and* stated failure modes. It is also the least discussed in agentic-coding threads because it isn't about writing features.

### 3.2 The fresh-context-per-iteration loop (true Ralph)
**Claim:** Progress should accumulate in *files and git history*, never in the context window. Each iteration spawns a **new process with an empty context**, reads specs from disk, does **one** thing, exits.
**Receipts:** Geoffrey Huntley, ghuntley.com/ralph, **2025-07-14**: "In its purest form, Ralph is a Bash loop. `while :; do cat PROMPT.md | claude-code ; done`." Huntley: "Ralph is a deliberate attempt to minimize allocation so I never get a compaction event." Cost receipt: a $50,000-quoted MVP "delivered, tested + reviewed" for **$297 in tokens**; Sonnet 4.5 on a bash loop ≈ **$10.42/hour** (linearb.io/blog/ralph-loop-agentic-engineering-geoffrey-huntley).
**Huntley's own limits, verbatim:** "There's no way in heck would I use Ralph in an existing code base." "Ralph can replace the majority of outsourcing at most companies **for greenfield projects**." "There is no way this is possible without senior expertise guiding Ralph. Anyone claiming engineers are no longer required... is peddling horseshit."
**Label: PROVEN for greenfield + mechanically-checkable work. HYPE for the "software development is dead" framing — the inventor disowns it.**

**The underrated sub-finding:** Anthropic ships an official `ralph-loop` / `ralph-wiggum` plugin (claude.com/plugins/ralph-loop, `/plugin install ralph-wiggum@claude-plugins-official`). But **it is not Huntley's Ralph**. Mario Giancini, mariogiancini.com, **2026-01-20**: "Their ralph-wiggum plugin uses a stop hook to re-feed prompts **within the same session**. Your context accumulates. Failed attempts stay in the transcript. There's no re-anchoring from source files." Also flagged: `--completion-promise` uses exact string matching and is unreliable — "**iteration limits are your real safety net**" (paddo.dev, 2025-12-02).
**Label: PROVEN divergence.** Anyone installing the official plugin expecting context-reset behavior gets the opposite.

### 3.3 The agent-to-agent review loop at industrial scale
**Claim:** Drive a PR to merge by having the agent review its own diff locally, then request reviews from *other agent instances in the cloud*, respond to feedback, and iterate until all agent reviewers are satisfied. Human review becomes **optional**.
**Receipt:** OpenAI, "Harness engineering: leveraging Codex in an agent-first world," openai.com/index/harness-engineering/, **~Feb 2026**. Verbatim: "To drive a PR to completion, we instruct Codex to review its own changes locally, request additional specific agent reviews both locally and in the cloud, respond to any human or agent given feedback, and iterate in a loop until all agent reviewers are satisfied (**effectively this is a Ralph Wiggum Loop**)." And: "Humans **can** review pull requests, but are not required to. Over time we directed almost all review effort to be handled agent-to-agent."
**Numbers:** ~1,000,000 LOC; ~1,500 PRs opened and merged; 5 months; 3 engineers → 7; **3.5 merged PRs per engineer per day**, throughput *increasing* as the team grew; "about 1/10th the time it would have taken to write the code by hand"; **zero manually-written code** (application logic, tests, CI config, docs, observability). Product has "hundreds of internal users including daily active power users."
**Supporting mechanics:** Chrome DevTools Protocol wired into the agent runtime (isolated app instance per worktree, screenshots for visual regression, LogQL/PromQL queries, "loop: fix → restart → revalidate until clean"). Architectural invariants enforced "mechanically via custom linters (generated by Codex, of course!) and structural tests." Single Codex runs "work on a single task for upwards of **six hours** (often while the humans are sleeping)."
**Label: PROVEN** — first-party, dated, specific, with named mechanism. Caveat: it is a greenfield internal beta, and OpenAI publishes no defect/incident data. Treat throughput as measured, quality as unmeasured.

### 3.4 The "map, not encyclopedia" rules-file loop (anti-bloat)
**Claim:** The rules file should be an **index**, not a knowledge base. Knowledge lives in structured `docs/`; the injected file is a navigation map.
**Receipt:** OpenAI harness post, verbatim: "give Codex **a map, not a 1,000-page instruction manual**"; "instead of treating `AGENTS.md` as an encyclopedia, we treat it as an index. The repo's knowledge base lives in a structured `docs/` directory treated as the system of record. A short `AGENTS.md` (**~100 lines**) is injected into context to serve primarily as a map."
Convergent receipt from the other lab: Anthropic best-practices — "CLAUDE.md is loaded every session, so only include things that apply broadly. For domain knowledge or workflows that are only relevant sometimes, use **skills** instead. Claude loads them on demand without bloating every conversation." Plus the test: "For each line, ask: *Would removing this cause Claude to make mistakes?* If not, cut it."
**Label: PROVEN** — two frontier labs independently converged on ~100-line index files + on-demand loading. This is the strongest signal in the entire survey, and it directly contradicts the popular "log every failure into CLAUDE.md" version of compound engineering.

### 3.5 The self-updating rules loop (with honest counter-evidence)
**Claim:** The agent reads its own session logs, spots recurring corrections, and proposes CLAUDE.md updates.
**Receipt:** Martin Alderson, "Self-improving CLAUDE.md files," martinalderson.com — mines project JSONL chat logs for points where the user got frustrated or repeated a correction, turning rule-maintenance into "a 30 second job." Self-reported, no metrics. Also: HN thread 47957402 — ending every session with "reflect on this session and encode via claude.md or skills what you learned"; "without this, every session starts from zero, repeating mistakes I've already corrected."
**Counter-receipt:** MindStudio, "Context Rot in Claude Code Skills" — context rot is "the gradual degradation in agent performance caused by skill files that have grown too large, too dense, or too cluttered." Recommends keeping skill files **~2,000–3,000 tokens**; warns explicitly against loops that append a new rule per failure without auditing conflicts, and recommends subdirectory-scoped files to localize behavior.
**Label: PLAUSIBLE with a hard ceiling.** The loop works; the *unbounded* version is a known regression. Pair any self-update loop with a pruning loop or you build compound liability.

### 3.6 The critic-score gate loop (`/grep-loop`)
**Claim:** Push → external reviewer scores the PR (n/5) → agent reads the review, fixes, pushes, waits for re-review → repeat until score ≥ threshold.
**Receipt:** Practitioner walkthrough in Recall card `de8f25c3` ("Why This Dev Ships 100x Faster Than 99% of Engineers," 2026-05-20): "Greptile gives me these confidence scores. Four out of five, three out of five, five out of five... I install the skill. All I do is `/grep-loop` and I hit enter. The agent is going to read the PR, read the feedback, fix the feedback, and wait for a new review." Same practitioner's honest boundary: "If I told it... slash grep loop, we have Ralph Wiggum. And we've all seen where that led us... **human approval, human thought really, really matters.**" Vendor-side numbers (greptile.com: "4x faster merges, 3x more bugs caught") are **marketing self-reports**.
**Label: PLAUSIBLE.** The mechanism is real and cheap to run. The numbers are not independently verified. The key design property worth stealing: the stop condition is an **external numeric score**, not the working agent's own judgment.

### 3.7 The two-command primitive split (`/goal` vs `/loop`)
**Claim:** There are two structurally different loops and conflating them is the most common design error. `/goal` = **inner** loop, progress-driven, next turn starts when the last finishes, stops when a *separate judge model confirms the condition*. `/loop` = **outer** loop, clock-driven, next turn starts when an interval elapses, stops when you stop it.
**Receipt:** code.claude.com/docs/en/goal (first-party): "`/goal` is a wrapper around a session-scoped prompt-based Stop hook. Each time Claude finishes a turn, the condition and the conversation so far are sent to your configured small fast model, which defaults to **Haiku**." Versions: `/loop` since **v2.1.72**, `/goal` in **v2.1.139** (desktheory.com 2026-06-08; dev.classmethod.jp 2026-07-01). Codex shipped the same primitive in CLI 0.128.0 (2026-04-30) plus an Automations tab.
**Critical, rarely-mentioned gotcha (first-party docs):** the Haiku judge **does not run commands** — it reads the transcript. So the condition must be written so the agent leaves evidence in the conversation. Effective conditions have three parts: measurable end state, explicit verification method (`npm test` exits 0), and an invariant constraint ("don't modify other test files").
**Label: PROVEN** (product documentation). Underrated because most write-ups treat "loop" as one thing.

### 3.8 The adversarial-reviewer-in-fresh-context loop — with a built-in warning
**Claim:** Before counting work done, a subagent reviews the diff in a fresh context, seeing only the diff and criteria — not the reasoning that produced it.
**Receipt:** Anthropic best-practices, verbatim: "A reviewer running in a fresh subagent context sees only the diff and the criteria you give it, not the reasoning that produced the change, so it evaluates the result on its own terms." Also documents the Writer/Reviewer two-session pattern.
**The warning nobody quotes, verbatim:** "**A reviewer prompted to find gaps will usually report some, even when the work is sound, because that is what it was asked to do. Chasing every finding leads to over-engineering:** extra abstraction layers, defensive code, and tests for cases that can't happen. Tell the reviewer to flag only gaps that affect correctness or the stated requirements, and treat the rest as optional."
**Label: PROVEN pattern with a PROVEN failure mode.** The failure mode is under-circulated relative to the pattern.

### 3.9 Evolving-context as a research object (ACE)
**Claim:** Treat context as an evolving playbook updated by **incremental modular deltas**, never destructive rewrites — avoiding "brevity bias" and "context collapse."
**Receipt:** Zhang, Hu, Upasani et al., "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models," arXiv **2510.04618** (submitted 2025-10-06, v3 2026-03-29), **ICLR 2026**. Reported: **+10.6% on agent benchmarks, +8.6% on finance tasks**, reduced adaptation latency and rollout cost; matches a top-ranked production agent on AppWorld overall and surpasses it on the harder test-challenge split using a smaller open-source model.
**Label: PROVEN as a benchmark result; PLAUSIBLE as a transfer to CLAUDE.md-style workflows.** No published replication of ACE inside a coding-agent harness was found. It is, however, the closest thing to a theory of *why* pruned/modular rules files beat append-only ones.

---

## PART 4 — Counter-evidence and honest gaps

**METR — and the misquote in both directions.**
- Original RCT (metr.org, **2025-07-10**): 16 experienced OSS devs, 246 tasks, own mature repos, early-2025 tools. "When developers are allowed to use AI tools, they take **19% longer**." Devs forecast +24% faster; post-hoc believed +20% faster. A ~40-point perception gap.
- Update (metr.org, **2026-02-24**), verbatim: "Our raw results show some evidence for speedup... For the subset of the original developers who participated in the later study, we now estimate a **speedup of -18%** with a confidence interval between -38% and +9%. Among newly-recruited developers the estimated speedup is **-4%**."
- **Sign convention matters and is being reported wrong.** METR's own figure caption reads: "**Late-2025 AI likely accelerated open-source developers, but selection effects obscure the true speedup.**" So negative = *less time* = faster. At least one widely-shared 2026 post (particula.tech, 2026-07-02) reads the same numbers as an 18% *slowdown*. **That reading contradicts METR's own caption.**
- METR's own honesty: results are "only very weak evidence"; 30–50% of devs declined the no-AI arm; they are redesigning the study. **Label: the 19% slowdown is PROVEN for early-2025 tools on mature repos by experienced devs. Any 2026 number, in either direction, is UNCONFIRMED.**

**Anthropic's own expertise study (the closest thing to a real N).**
anthropic.com/research/claude-code-expertise, **2026-06-16**: ~400,000 Claude Code sessions from ~235,000 people, Oct 2025–Apr 2026. Findings: users make ~**70% of planning decisions but only 20% of execution decisions**; expert sessions trigger action chains "more than twice as long (12 actions) carrying five times the output (3,200 words)" vs. novice (5 actions, 600 words); **verified success 15% (novice) vs 28–33% (intermediate–expert)**; abandonment **5–7% (expert) vs 19% (novice)**.
**Label: PROVEN as observational.** It is correlational, first-party, and cannot separate "expertise causes success" from "easy tasks attract experts." But the 15%→33% success gradient is the strongest quantitative support in existence for the claim that *how you structure the loop* matters more than the model.

**Token blowups.** Requesty's guide: a goal loop with no `max_iterations` can burn $500/hour. Peter Steinberger reportedly ran ~€1.3M in token cost in 30 days (per a German breakdown, 2026-06-17 — which also notes ~70% of that was Fast Mode and that he works at OpenAI and didn't pay personally). **Label: PLAUSIBLE. Directionally: iteration ceilings and budget ceilings are not optional.**

**Compound liability.** aipatternbook.com/compound-engineering states the failure honestly: "Codified knowledge can rot. Rules contradict each other. Skills go out of date. Hooks block work nobody remembers asking for. Without an explicit pruning discipline, the compounding asset turns into a **compounding liability**." And the subtlest failure: "codifying lessons that aren't true yet, then watching the agent obediently apply a wrong rule everywhere."
**Label: PROVEN as a design risk** (converges with Anthropic's bloat warning and MindStudio's context rot).

**Ceremony risk.** Ry Walker's plugin review (2026-02-20): "the full seven-step loop is overkill for quick fixes"; "parallel review agents consume significant context"; near-daily releases mean "docs and habits go stale fast." Klaassen himself (2026-02-24): "if you're on the $20 plan, it's like not the ideal plugin to use because it will just use more tokens."

**Honest gaps — nothing found:**
- No independent (non-vendor, non-self-report) measurement of the 2–3x verification claim.
- No published defect-rate or incident data for OpenAI's 1M-LOC agent-built codebase.
- No RCT isolating any *specific loop design* (vs. AI tooling in general).
- No replication of ACE inside a production coding harness.
- No systematic public corpus of loop *failures* — as one analyst put it, the absence of published failure case studies is itself evidence that failures aren't being measured or aren't being shared.

---

## PART 5 — Source inventory

**Internal (Recall):** cards `e06d4cb6` (Dan Shipper / Lenny's, compounding engineering origin), `8f70253c` (Shipper: "the agent never makes the same mistake twice"), `fdd4a14b` (Cherny private lesson: `@claude` on PRs → CLAUDE.md, "our version of Dan Shipper's compounding engineering"), `de8f25c3` (`/grep-loop`, Ralph skepticism), `a4b3d9a9` ("FORGET Loop Engineering", 2026-07-14), `407035a8` (Karpathy autoresearch / meta-agent), `1513179b` (Klaassen 50-min Claude Code tutorial).

**Primary / first-party:**
- code.claude.com/docs/en/best-practices (Anthropic)
- code.claude.com/docs/en/goal (Anthropic, `/goal` vs `/loop` vs Stop hook)
- anthropic.com/research/claude-code-expertise (2026-06-16)
- anthropic.com/engineering/demystifying-evals-for-ai-agents
- claude.com/plugins/ralph-loop (official plugin listing)
- openai.com/index/harness-engineering/ (~Feb 2026)
- shopify.engineering/autoresearch (2026-04-15)
- ghuntley.com/ralph (2025-07-14); github.com/ghuntley/how-to-ralph-wiggum
- every.to/source-code/compound-engineering-how-every-codes-with-agents (2026-01-30)
- every.to/p/compound-engineering-gets-an-upgrade (2026-05-29)
- every.to/source-code/my-ai-had-already-fixed-the-code-before-i-saw-it (2025-08-18)
- metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/ ; metr.org/blog/2026-02-24-uplift-update/
- arxiv.org/abs/2510.04618 (ACE, ICLR 2026)
- youtube.com/watch?v=SlGRN8jh2RI (Cherny, Sequoia AI Ascent 2026) ; youtube.com/watch?v=RkQQ7WEor7w (Cherny, Acquired Unplugged)

**Secondary / practitioner:**
- infoq.com/news/2026/01/claude-code-creator-workflow/ (2026-01-10)
- venturebeat.com — Cherny workflow (2026-01-04)
- businessinsider.com — Cherny "few thousand agents overnight" (2026-05-13)
- lethain.com/everyinc-compound-engineering/ (Will Larson, 2026-01-19)
- addyosmani.com/blog/loop-engineering/ (2026-06-07)
- fortune.com/2026/03/17/andrej-karpathy-loop-autonomous-ai-agents-future/
- philschmid.de/autoresearch (2026-03-10)
- mariogiancini.com/ralph-loop-plugin-pattern-for-multiple-projects (2026-01-20)
- paddo.dev/blog/ralph-wiggum-autonomous-loops/ (2025-12-02)
- mindstudio.ai/blog/context-rot-claude-code-skills-bloated-files
- martinalderson.com/posts/self-improving-claude-md-files/
- aipatternbook.com/compound-engineering
- rywalker.com/research/compound-engineering-plugin (2026-02-20)
- tianpan.co forum teardown (2026-02-12)
- github.com/cocodedk/loop-engineering (third-party sourced dossier on Cherny; useful as a claim index, not as a primary source)

**Deliberately excluded / flagged:** noqta.tn (2026-06-19) specific loop-name list — single low-authority aggregator, PLAUSIBLE only. vincirufus.com "300–700%" — HYPE, unsourced. greptile.com "4x/3x" — vendor marketing. particula.tech METR reading — contradicts METR's own figure caption.
