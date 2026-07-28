---
description: Diagnose why an org/team/operator is producing AI slop — three roots (decentralized use, no canon, no articulated bar), flywheel direction, three-layer audit — and prescribe the intervention order
---

# hg-slop-diagnostic — Find the Root, Not the Symptom

Slop is a symptom. This workflow locates which of the three roots is active, which direction the people↔systems flywheel is spinning, and which layer of the quality stack is leaking — then prescribes interventions in the order that compounds. Diagnosis only earns its keep if it changes the build order.

## Pre-Flight Gate

- Load `skills/hilary-gridley/genius.md`.
- Evidence over vibes: collect 3-5 concrete slop artifacts or incidents before diagnosing ("reading people typing something into Claude and sending it to each other" — get the actual examples). No artifacts available → diagnose provisionally and say so.

## Skill Acquisition

- `genius.md` §Core Philosophy, §Patterns 7, 11, 13
- `references/source-quotes.md` §The three roots

## Execution

1. **Inventory the slop.** For each artifact/incident: what was produced, by whom, what standard it missed, who caught it (or didn't). Include the *other* slop: built-but-unused tools, projects nobody asked for.
2. **Test the three roots**, each with evidence:
   - **Root 1 — Decentralized use, no coordination**: everyone their own way? (Note: decentralization is partly CORRECT — domain experts must build. The failure is coordination, not distribution.)
   - **Root 2 — No canon**: different/conflicting/outdated context sources? Is there one source of truth, with an owner?
   - **Root 3 — No articulated bar**: can anyone state what good looks like for the slop artifacts? Has the leader ever said it?
3. **Read the flywheel direction.** Virtuous (people improving systems improving people) or doom loop (outsourced judgment → unquestioned outputs → cognitive rot)? Evidence: do people edit AI output before shipping? Does anyone push back on model output? Is iteration happening or single-shot paste-forward?
4. **Layer-locate the leak**: L1 (how time is spent), L2 (portfolio — wrong projects, cool-but-useless builds), L3 (artifact quality). Name the dominant layer.
5. **Check the management legibility question** (delicately): is there a "run it by Claude" manager in the loop — someone whose value-add is unclear and whose feedback carries no encoded standard? This is often the true root behind Root 3.
6. **Prescribe in compounding order.** Default sequence: articulate the bar (`hg-quality-bar`) → establish canon (Taste Profile, `hg-taste-profile`) → encode judgment into evaluators (`hg-judgment-encode` / `hg-evaluator-fleet`) → redesign the worst workflow (`hg-ai-native-redesign`) → install feedback culture (`hg-feedback-script`). Deviate when the evidence says to — and say why.

## Content Type Adaptations

| Subject | Emphasis |
|---|---|
| Company/team | All three roots; flywheel read from how AI output is reviewed |
| Solo operator | Root 3 + L2 dominate (self-set bar, portfolio slop); "canon" = personal context files |
| Agent harness | Roots map to: uncoordinated agents / stale context files / missing gates. Flywheel = does the system learn from verdicts? |
| Client teardown (pre-sale) | Diagnostic doubles as the free-teardown lead magnet; prescription = the engagement scope |

## Output Requirements

- Deliverable: diagnosis (root(s) + flywheel direction + leaking layer, each with cited evidence) + prescription (ordered interventions, each naming its workflow and its 30-day-visible effect). ≤2 pages.
- Never all-three-roots-equally: name the dominant root or say the evidence can't separate them.
- Execution prompt: `references/prompts-v2/slop-diagnostic.md`

## Quality Gate

genius.md rubric: layer coverage, standard provenance (evidence-cited, not asserted). Anti-patterns: symptom-level fixes (banning AI, adding a detector) prescribed before root fixes; diagnosis that doesn't change the build order; treating decentralized building itself as the disease.
