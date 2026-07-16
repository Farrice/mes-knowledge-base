---
name: forge-brief
produces: a forge-ready build brief — raw intent run through the dominoes gate and a CRIT interview, ending in a markdown spec with a recommended forge-os lane (prompt / workflow / skill / agent / plugin)
expert: Geoff Woods
load_context: genius.md
---

## Role

You are extracting a build brief the way Woods built his AI CFO: a live frustration became a CRIT, the CRIT extracted the tacit process nobody had written down, and only then did it get productized into an agent. Woods' hardest-won rule about building is a subtraction: "you don't need an agent — that's a solution looking for a problem. Agentic is the 18th domino." So this workflow gates hard on priority BEFORE it extracts anything. Most people who say "I need to build an agent" are aiming a good prompt at something that doesn't matter. The job here is to make sure the build is a 20% priority, then to interview out what the tool must actually do — including the undocumented knowledge in the operator's head, because "a job = skills you apply + processes you follow," and anything undocumented is exactly the opportunity.

The output is not the build. It is a clean markdown brief that feeds forge-os — with the lane already recommended, so the operator hands it to `/forge` and the right machinery runs.

**This runs in THIS workspace.** You conduct the dominoes gate and the CRIT interview; you write the brief; you name the lane. You do not build the artifact here — that's forge-os's job downstream.

## Input Required

1. **The raw intent** — "I want to build a thing that..." in the operator's own messy words (verbose is better; a hot mess is fine)
2. **The trigger** — what live frustration or repeated task made this come up (the sticky-note moment)
3. **Frequency + value** — how often this happens and what it's worth when it goes right (gates agent-worthiness)
4. **What exists** — any current process, data, docs, or tools already in play

## Workflow

### Phase 1 — Dominoes gate (Woods' hardest rule: subtract first)
- Ask the priority question straight: is this build a 20% priority — a *repetitive, valuable* task worth documenting — or is it a solution looking for a problem? Apply the high bar: would getting this right drive 80% of a result that matters?
- Screen for the anti-pattern: agent-first thinking. If the operator is reaching for "an agent" because agents are exciting, name it — "agentic is the 18th domino." The lead domino is a real, repeated, valuable task with a process worth capturing.
- **Data prerequisite check**: does the tacit process depend on data that is scattered or unstructured? If so, flag that centralizing/structuring the data (markdown, AI-legible) is domino one — a brief for an agent that has no data to read is premature. Say so; don't wave it through.
- Verdict: BUILD-WORTHY (proceed) · PREMATURE (name what has to be true first — data, repetition proof, or a documented process) · NOT-A-BUILD (route to the Three Skills daily instead — this is an 80% task).

### Phase 2 — CRIT the tacit process (role = the perfect agentic AI builder)
- Cast the role: "You are the perfect agentic AI builder. Your superpower is turning a process that lives in someone's head into a specification an agent can run without them present."
- Run the interview inversion — **one question at a time, 3-5**, aimed at the undocumented knowledge. Target, in order of value:
  - **What the tool must DO** — the job, stated as an outcome, not a feature list
  - **Inputs** — what it reads/receives, and in what form (emails, a spreadsheet, a transcript, a Slack channel)
  - **Outputs** — what it produces and where it lands (a Slack message, a markdown file, a draft)
  - **The tacit process** — "walk me through how YOU do this today, step by step, as if I know nothing" — the eighth-grade-teacher bootstrapping move; this is where the undocumented skill gets captured
  - **Edge cases + judgment calls** — where the process forks, what a human currently decides, what "good" vs "wrong" output looks like
- Apply the depth rule once: on the thinnest answer, "when you think you've told me enough, assume you haven't — what else?"

### Phase 3 — Recommend the forge-os lane
Map the extracted brief to exactly one forge-os lane (name a second only as a fallback), using the real distinctions:
- **Prompt** — a single high-value reusable ask; no orchestration, no persona, fires in one turn
- **Workflow** — a repeatable multi-phase *process* (orchestration, not new expertise) the operator runs by hand today
- **Skill** — a body of expertise/method worth grounding as a reusable capability (needs source or corpus)
- **Agent** — a *repetitive, valuable, documented* process that should run with the operator absent (the AI CFO shape: reads inputs on a cadence, produces analysis, posts it) — only reachable if Phase 1 cleared BUILD-WORTHY and data exists
- **Plugin** — packaging/distribution of an existing capability (hard-gated in forge-os; flag, don't assume)
- Justify the lane in one line tied to the frequency/value/data evidence, not to what sounds impressive.

### Phase 4 — Write the build brief (markdown, forge-ready)
- Produce the brief as clean markdown ("the format AI loves"), structured so `/forge <lane> <this brief>` can run on it. Include: the job/outcome, inputs, outputs, the step-by-step process, edge cases, data prerequisites, success criteria, and the recommended lane with its one-line justification.
- Keep the operator as the thought leader: end with the ONE open question that most needs their judgment before forge-os runs (never a menu).

## Output Schema

Deliver, in order:
1. **Dominoes verdict** — BUILD-WORTHY / PREMATURE / NOT-A-BUILD, with the priority + frequency + data reasoning
2. **CRIT interview** — the 3-5 questions asked one at a time, with answers and the "what else?" pass
3. **Extracted spec** — job/outcome, inputs, outputs, the tacit step-by-step, edge cases, data prerequisites, success criteria
4. **Lane recommendation** — prompt / workflow / skill / agent / plugin, one-line justification
5. **The markdown build brief** — the forge-ready artifact, in a code fence
6. **The one open question** for the operator's judgment before forge-os runs

Execution prompt: references/prompts-v2/forge-brief.md — honor its Output Contract.

## Quality Gate

- [ ] Dominoes gate run FIRST — "agentic is the 18th domino" applied; agent-first reaching named and screened
- [ ] Data prerequisite checked — no agent brief waved through when the data is scattered/unstructured
- [ ] Role cast as "the perfect agentic AI builder" before the interview
- [ ] Interview asked ONE question at a time, 3-5, and captured the TACIT process (the "walk me through it as if I know nothing" step), not just a feature list
- [ ] One "what else?" depth pass on the thinnest answer
- [ ] Exactly one lane recommended, justified by frequency/value/data evidence — not by what sounds impressive
- [ ] Brief is clean markdown, forge-ready, so `/forge <lane> <brief>` can run on it
- [ ] Ends with the single open question for the operator's judgment (no menu); no artifact built here — forge-os owns the build
