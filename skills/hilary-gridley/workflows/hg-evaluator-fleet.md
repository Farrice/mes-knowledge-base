---
description: Plan the fleet of narrow evaluator tools for a role/team — scoped artifact × audience × outcome, prioritized by asymmetric downside, with the anti-second-brain gate enforced
---

# hg-evaluator-fleet — Dozens of Narrow Tools, Never One Wide One

She made "dozens of these, all that specific." This workflow plans that fleet for a given role/team/operator: which evaluators to mint, in what order, each passing the narrow-scope gate. Output feeds `hg-judgment-encode` one tool at a time.

## Pre-Flight Gate

- Load `skills/hilary-gridley/genius.md` §Pattern 2 + §Anti-Patterns.
- **Anti-second-brain gate**: if the ask is "build an AI that knows everything about X / a second [person]" — refuse the shape, split into narrow tools, explain in one line why ("there's no me in that equation" cuts both ways: a general brain has no bar).

## Skill Acquisition

- `genius.md` §Purpose-Driven Tool Scoping, §Editor-Not-Author Split
- `references/source-quotes.md` §Tool scoping

## Execution

1. **Inventory recurring artifacts.** Everything this role produces repeatedly: emails, posts, briefs, decks, PRDs, test designs, proposals, agent outputs. Everyone has "six to eight they should build."
2. **Score each candidate** on: frequency × **asymmetric downside** (the launch-date-email test: small artifact, catastrophic tail = build first) × evidence availability (do edit pairs exist?) × iteration bottleneck (is a human currently the feedback gate?).
3. **Scope each tool** as artifact × audience × outcome, named in that grammar ("Executive Email Editor — get to yes," not "email helper"). A tool whose upload target is ambiguous → split it.
4. **Sequence the fleet.** First build: highest asymmetric downside WITH existing edit pairs. Cap the first wave at 3 — fleet breadth comes over time; portfolio slop (10 tools nobody uses) is a failure mode of this very workflow.
5. **Per tool, spec the card**: name, scoped input, whose judgment it encodes, corpus source, deploy surface (custom GPT / skill / gem / harness gate), kick-the-crutch feature (it shows criteria, returns work to the author).
6. **Route to minting**: each wave-1 card → `hg-judgment-encode` (corpus exists) or `hg-edit-pair-harvest` (corpus needs assembly).

## Content Type Adaptations

| Subject | Fleet character |
|---|---|
| Manager + team | Manager's judgment encoded; tools unblock team iteration without the manager gate |
| Solo operator | Own past-self's best work is the corpus; tools guard against fatigue-slop |
| Client engagement | Fleet = the delivery vehicle of the Taste Profile offer (Layer 3 operationalized) |
| Agent harness | Evaluators become gates/hooks; corpus = human-corrected agent outputs |

## Output Requirements

- Deliverable: scored inventory table + wave-1 (max 3) tool cards + build routing. One page.
- Every tool name passes the grammar test (artifact × audience × outcome legible in the name).
- Execution prompt: `references/prompts-v2/evaluator-fleet.md`

## Quality Gate

genius.md rubric: purpose specificity (savant = users never wonder what to upload). Anti-patterns: second-brain shape, wave-1 > 3 tools, any tool without a corpus source, building by coolness instead of downside × frequency.
