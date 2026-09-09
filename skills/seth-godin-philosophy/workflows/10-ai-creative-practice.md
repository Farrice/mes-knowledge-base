---
name: "AI Creative Practice"
produces: "Project Ownership Lock + System Gap Map + Proud Artifact Spec + bounded AI Task Packets + Cheap Failure Ladder + traction verdict"
expert: "Seth Godin"
load_context: "genius.md"
description: "Turn a system problem into a human-owned, AI-assisted artifact through bounded task delegation, inexpensive experiments, and traction-based iteration"
---

# Workflow 10: AI Creative Practice

> **Prerequisite:** Load [genius.md](../genius.md) before running this workflow.
> **Source:** Digital Cut × Seth Godin, complete 62:09 interview; timestamped evidence in `extractions/video-context/DHTgH34inHY/`.
> **Uses:** Patterns 5, 7, 8, 10, 17, 21, 27, 33, and 36–40.

## When to Use

- The user wants AI to help turn a system problem or underserved audience gap into something worth shipping.
- The operator needs a clear boundary between the project they own and the tasks AI may execute.
- An AI-assisted concept needs cheap experiments, a public-quality artifact, and traction measures before expansion.

Do not activate for a simple production request such as “draft five posts.” Do not use it to decide a public brand promise or customer-facing AI permission boundary; route those to `seth-godin-brand`. Do not delegate the desired change, audience choice, consequential judgment, release approval, or final quality decision to AI.

## Input Required

- **[DESIRED_CHANGE]**: The change the human is trying to make, stated as behavior or condition—not output volume.
- **[SMALLEST_VIABLE_AUDIENCE]**: The smallest group for whom the change would be worth making, plus who is outside the test.
- **[CONSTRAINTS]**: Time, money, tools, claims, brand, privacy, safety, and non-negotiable life constraints.
- **[HUMAN_ONLY_DECISIONS]**: Objective, audience, tradeoffs, claims, taste, release, and other judgments AI may inform but not own.
- **[CANDIDATE_AI_TASKS]**: Research, sorting, drafting, comparison, synthesis, prototyping, QA, or other bounded work.
- **[FAILURE_BUDGET]**: Maximum time, money, exposure, reputation, and data risk across the experiment ladder.
- **[EVIDENCE]**: Observed audience behavior, source material, prior attempts, constraints, and unknowns.
- **[PUBLISHING_BOUNDARY]**: Internal-only, private preview, approval-before-public, or already approved public release.

When low-risk inputs are absent, label a conservative assumption. Ask only when the missing fact changes the human ownership boundary, failure cap, audience, external action, or public promise.

## Execution Protocol

### Phase 1: Project Ownership Lock

1. Write the project as: “We seek to create `[DESIRED_CHANGE]` for `[SMALLEST_VIABLE_AUDIENCE]`.”
2. Name one human outcome owner. That person retains responsibility even when AI performs most tasks.
3. Lock the human-only decisions: desired change, audience boundary, protected constraints, consequential claims, taste threshold, release approval, and stop/scale authority.
4. Reject any candidate task that silently contains the project objective. Rewrite it until the output can be inspected without surrendering the decision.

### Phase 2: System Gap Map

5. Use the systems-thinking overlay only if a genuine system is implicated. Step out exactly one level and return as soon as the diagnosis changes the project.
6. Map: current system, who benefits, who is underserved, repeated friction, evidence, and the smallest plausible leverage point.
7. Separate observations from hypotheses. A system story without evidence becomes a testable question, not doctrine.
8. Choose one gap only. If several appear, select the gap closest to the audience and cheapest to test.

### Phase 3: Proud Artifact Spec

9. Define the artifact a real audience member can use: form, user, moment of use, promised change, minimum spec, proof needed, and why the human would be proud to put their name on it.
10. Distinguish internal rough work from the public artifact. AI may generate abundant internal variants; only human-selected work crosses the publishing boundary.
11. If the artifact changes a public brand promise or customer-facing AI relationship, pause this phase and consult `seth-godin-brand` before release.

### Phase 4: Bounded AI Task Packets

12. Convert `[CANDIDATE_AI_TASKS]` into discrete packets. Every packet must contain:
    - task purpose and its connection to the human-owned project;
    - exact inputs and source truth;
    - output shape;
    - acceptance test;
    - human reviewer and consequential judgment retained;
    - stop condition and prohibited actions.
13. Keep packets independent where practical. A failed research task must not silently authorize a draft, a publication, or a spend.
14. Remove packets that exist only to increase volume. Reclaimed capacity must improve problem-solving, artifact usefulness, or learning.

### Phase 5: Three-Step Cheap Failure Ladder

15. Allocate the failure budget before proposing experiments. The three rungs share the total cap.
16. Build exactly three tests:
    1. **Internal proof:** shortest reversible test of the mechanism using existing evidence; no public exposure.
    2. **Smallest-audience use:** put the minimum usable artifact in front of the fewest qualified people needed to change a decision.
    3. **Bounded release:** only within `[PUBLISHING_BOUNDARY]`; test repeated use, commitment, payment, or referral without expanding the project objective.
17. For each rung state owner, audience, artifact version, time cap, money cap, exposure cap, signal, decision, and stop rule.
18. If the publishing boundary is internal-only or approval-before-public, prepare rung three but do not execute it.

### Phase 6: Traction Measures

19. Prefer observed behavior from the chosen audience: successful use, return, repeat use, completion, specific request, deposit/payment, qualified referral, or adoption by another person.
20. Label likes, impressions, generic praise, model scores, and production volume as spectator or diagnostic metrics unless they directly predict the desired change.
21. Set a precommitted threshold and observation window for each traction measure. Do not invent a universal number.

### Phase 7: Decision

22. End with exactly one verdict:
    - **STOP:** the boundary prevents a valid test or the artifact is not yet usable;
    - **ITERATE:** the signal reveals a specific repair worth one more capped test;
    - **SCALE:** the precommitted traction threshold is met and the next increment remains inside the constraints;
    - **KILL:** repeated qualified evidence rejects the gap, artifact, or audience hypothesis.
23. Name the evidence that would reverse the verdict. A decision without a falsifier is attachment, not practice.
24. Reuse `02-ship-it-protocol.md` for a ready-but-hidden artifact and `09-problem-to-action-loop.md` when fear or entanglement prevents the next experiment. Do not duplicate their mechanics here.

## Output Contract

Produce one **AI Creative Practice Design** containing:

1. Project Ownership Lock;
2. System Gap Map with observations, hypotheses, and one leverage point;
3. Proud Artifact Spec;
4. bounded AI Task Packets;
5. exactly three Cheap Failure Ladder experiments;
6. traction measures and thresholds;
7. one STOP, ITERATE, SCALE, or KILL verdict with reversal evidence.

Execution prompt: `references/prompts-v2/ai-creative-practice-design.md`. Honor its Output Contract.

After an experiment, use `references/prompts-v2/ai-creative-practice-traction-review.md` for the post-experiment decision.

## Quality Gate

- [ ] A named human owns the project, consequential judgment, release, and recovery path.
- [ ] AI receives tasks with acceptance tests; no packet contains the project objective.
- [ ] The audience and one system gap are specific and evidence-labeled.
- [ ] The artifact is usable by someone and worthy of the human’s name, not an AI demonstration.
- [ ] The three experiments share an explicit failure budget and become progressively more exposed.
- [ ] Traction uses qualified behavior and a precommitted threshold, not output or applause.
- [ ] The result ends with one explicit STOP, ITERATE, SCALE, or KILL decision.
- [ ] Public release, spend, outreach, or brand-promise change remains behind its approval boundary.

