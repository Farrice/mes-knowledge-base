---
description: Audit any AI tool/workflow for teaching residue — would removing it leave the team better than before it existed? — and redesign it from crutch to coach
---

# hg-kick-the-crutch — Tools That Teach

Her design law: "Build these tools in such a way that they are teaching your team what good looks like — such that if you kicked the crutch out tomorrow, they wouldn't say 'oh no, I haven't learned anything.'" This workflow audits an existing tool (or tool design) against that law and redesigns it to pass. The difference decides whether the org spins the virtuous cycle or the slop doom loop.

## Pre-Flight Gate

- Load `skills/hilary-gridley/genius.md` §Patterns 10-11.
- Input: one specific tool/workflow (custom GPT, skill, agent, automation) + who uses it + what it produces. "Audit all our tools" → start with the most-used one.

## Skill Acquisition

- `genius.md` §Kick-the-Crutch Tool Design, §Virtuous Cycle vs Slop Doom Loop, §Editor-Not-Author Split

## Execution

1. **Run the thought experiment.** Tool disappears tomorrow. Are its users better at this work than before it existed — or newly helpless? Evidence beats intuition: do users ever pre-empt the tool's feedback? Has anyone graduated (needs it less)? Or has usage deepened while skill flatlined?
2. **Locate the tool on the crutch→coach spectrum**:
   - **Crutch**: does the work, hides the reasoning, returns a finished artifact (silent full-rewrites are the classic)
   - **Assistant**: does the work, shows the output, reasoning opaque
   - **Coach**: evaluates against visible criteria, explains the why, suggests targeted changes, returns the work to the author for their pass
3. **Check the judgment seat.** Does the tool leave choose/judge/elevate to the human, or did automation swallow it? ("Too much focus on automation — starts the job AND finishes the job.") A tool can be excellent at 0→80 and still fail by also doing the 80→great.
4. **Redesign toward coach.** Levers: expose the criteria (plain-English pass/fail, visible every run) · replace full-rewrites with targeted suggestions + why · return work to the author with the next pass named · add a graduation dial (feedback verbosity drops as the user's pass rate rises) · keep 0→80 automated, hand 80→great back.
5. **Set the flywheel check.** One observable, dated: e.g. "by [date], N users pre-empt criterion X before running the tool" — the signal the tool is teaching, not just serving.

## Content Type Adaptations

| Tool type | Emphasis |
|---|---|
| Feedback/evaluator tools | Criteria visibility + rewrite discipline (suggest, don't replace) |
| Generation tools (drafts from scratch) | Judgment seat: options-not-answers (3 angles to choose between beats 1 finished piece); human picks and elevates |
| Agent pipelines | Which stations are judgment stations; agent shows its criteria at gates |
| Team rollouts | Graduation path explicit: what users should no longer need in 90 days |

## Output Requirements

- Deliverable: verdict (crutch/assistant/coach + evidence) + redesign spec (concrete lever changes, not principles) + the dated flywheel check.
- Redesign preserves the tool's speed win — coaching must not reinstall the bottleneck the tool removed.
- Execution prompt: shares `references/prompts-v2/evaluator-fleet.md` §crutch-audit block

## Quality Gate

genius.md rubric: teaching residue (savant = users pre-empt feedback), human seat clarity. Anti-patterns: silent full-rewrites, criteria hidden in the prompt, automation-first framing, "coaching" that just slows the tool down without transferring the standard.
