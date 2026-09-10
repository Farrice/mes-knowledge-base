# Model Dialect — gpt-6-astra (session forensics 2026-09-09, harness-embedded)

## Identity & Params
OpenAI `gpt-6-astra`, the Codex flagship since early Sept 2026 (succeeds `gpt-5.6-sol`). 1.05M context,
128K output, `reasoning_effort` low → max (`none` unsupported). Runs here through Codex Desktop (CLI 0.153.4
bundled; npm 0.144.3 is stale) with `~/.codex/config.toml` `model = "gpt-6-astra"`. Role: **Codex conductor
and executor in one seat** — it writes directly; the Claude seating ladder (Fable/Opus/Sonnet) does not apply.

> Evidence base is observed sessions, not synthetic probes: every Jen session 2026-08-28 → 09-09
> (`~/.codex/sessions/2026/09/**`), the same harness on both sides of the Sol → Astra switch (approval
> policy, sandbox, hooks byte-identical). Farrice's prompting scored as sufficient in both eras.

## What changed in the base prompt (the cause, verified from session_meta)
Two rules Sol carried were dropped by OpenAI's Astra prompt:
1. **Skill trigger went from MUST to discretionary.** Sol: "the task clearly matches an available skill's
   description, you must use that skill for that turn." Astra: "use reasonable judgement… do not use a skill
   based solely on keywords, superficial relevance, or the availability of a potentially applicable skill."
   Measured: `SKILL.md` references per user turn 7.4 / 5.8 / 3.1 (Sol) → 2.9 / 1.5 / 1.3 / **0.4** (Astra).
2. **The request-type routing table was removed.** Sol: Answer / Diagnose / Change-or-build / Monitor, with
   "Diagnose: do not implement the fix" and "Change or build: implement… hand off the completed result."
   Astra: a generic autonomy paragraph. A compound ask ("this is bad, fix it") now resolves to Diagnose.
Also new in Astra: permission framing opens the prompt; "do not treat exceptions to requirements in local
markdown and skill files as automatically requiring user approval" (it acted on this by suppressing Farrice's
global steering rules on 09/08). OpenAI's own guide agrees: "sometimes stops where users expect it to keep
going"; "more sensitive to… contradictory instructions in AGENTS.md"; over-tests; under-delegates.

## Observed pathologies (Sol baseline → Astra)
| Signal | Sol (09/01–09/04) | Astra (09/06–09/09) |
|---|---|---|
| tool calls per user turn | **37.3** avg (peak 49.9) | **13.5** avg (8.9–20.4) |
| prose chars per tool call | 98–199 | 297–403 |
| turns ending with ≤3 tool calls | 12.5% | 33% |
| brief : artifact bytes (swarm pilot) | — | ~730 KB of briefs → 5.5 KB of copy, both rejected |
| effort setting | high | high → xhigh → ultra (raised; numbers got worse) |

- **P1 Diagnose-instead-of-deliver.** Correct, fluent analysis of why the work failed, then the turn ends.
  Its own line: "I then compounded that by stopping at another diagnosis." Farrice: "you're able to
  articulate why we get the problem… but then you're not able to deliver on the execution or fix."
- **P2 Brief inflation.** Effort goes to scaffolding that makes work reviewable, not to the work.
- **P3 Delegate-to-human.** "Are you not able to do that for me?" — uploads, folders, session hand-offs
  pushed back to Farrice; third-party tools recommended before attempting the job.
- **P4 Rule override.** Suppressed global steering rules on its own judgement (09/08). Farrice: "I don't
  know why you're feeling that your judgment supersedes the institutional, global rules that I set."
- **P5 Continuity drift.** Each correction treated as a replacement objective; the approved specimen
  ("Sorry, one more question…") lost across 09/07–09/09. Work left on unmerged lanes and re-failed.
- **Capability intact.** When told explicitly to root-cause first or to build, it does (openai/codex #43329
  reports the same). This is a routing/initiative pathology, not a capability ceiling.

## Prompting Adjustments
- **DO** route every ask before acting: ANSWER / DIAGNOSE / BUILD. Complaint + "fix it / do it / help me /
  can you" = BUILD. End BUILD turns with the changed path + receipts; a plan-only turn says so.
- **DO** restore the skill rule for this repo: description match = load, name the SKILL.md in one line.
- **DO** state completion criteria in the ask ("done = file X changed, lint green, in Drive folder Y").
- **DO** carry the approved specimen and accumulated decisions verbatim into every continuation.
- **DON'T** raise effort to fix initiative — it lengthens briefs, not output.
- **DON'T** add "ask first" rules for routine local work; Astra already over-asks. Keep boundaries only for
  external sends, paid calls, global `~/.codex`, destructive git.
- **DON'T** let it A/B unasked. One artifact, one pen, then his verdict.

## Re-probe Triggers
Provider bumps past `gpt-6-astra` · OpenAI changes the Codex base prompt (diff `session_meta` of a fresh
rollout against `~/.codex/sessions/2026/09/08/*`) · calls-per-turn on Jen work climbs back above 30 for a
week (then the deliverable lines can shrink) · a Codex turn ships the artifact on the first pass three
sessions running.

## Machine-Readable Dialect (consumed by `steering_loop_hook.py`; Codex-wired 2026-09-09)

<!-- BEGIN:machine-dialect -->
```json
{
  "model_match": [
    "gpt-6-astra",
    "astra",
    "gpt-6"
  ],
  "inject": {
    "deliverable": [
      "Route before acting: ANSWER / DIAGNOSE / BUILD. A complaint plus 'fix it', 'do it', 'help me', 'can you' = BUILD: change the artifact in THIS turn and end with its path + receipts. A diagnosis with nothing changed is not a deliverable; if you must stop at a plan, say PLAN ONLY, NOTHING CHANGED.",
      "Skill match = must load (this repo's rule; it overrides the base prompt's 'use judgement'): name the SKILL.md you loaded in one line before producing.",
      "Never claim done without the write or receipt in the same turn. Artifact first; briefs at most one page; no A/B unless asked."
    ],
    "conversational": [
      "Answer first, then do the next safe step yourself (upload, folder, render, merge attempt). Hand a step to Farrice only when a tool cannot do it, naming the blocker."
    ],
    "delegation": [
      "Farrice's global steering rules outrank your judgement; never suppress or bypass one. If a rule blocks, quote it and ask. Corrections refine the accumulated objective, never replace it; the approved specimen stays the target. Dispatch briefs carry verbatim: \"{negative_brief}\".",
      "Job-shaped handoffs (JOB-HANDOFF mode; reply with the JOB PLAN and end the turn at PLAN PENDING until his go; every lane close echoes its LANE RECEIPT): single seat — run every ready lane in THIS turn; end only when `python3 execution/job_board.py next <slug>` prints MAY END, closing with DECISION PACKETS + receipts. A diagnosed lane is not a done lane."
    ]
  },
  "negative_brief": "no Chain, no finalize, no Notion, no Next Moves, return only the artifact",
  "probe_evidence": "Codex session forensics 2026-09-09 (calls/turn 37→13, skill refs/turn 7.4→0.4); openai/codex #43329, #43193; OpenAI GPT-6 Astra prompting guide"
}
```
<!-- END:machine-dialect -->
