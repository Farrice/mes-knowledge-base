# Architecture Checkpoint: Profit-Finder Opportunity Scan

**Checkpoint:** 2 of 3 (approved by Farrice)
**Verdict:** Build one upstream Luke Iha workflow, not a new Adil system

## What Changed Since Vision

The approved Vision called the capability **Profit-Finder Market Whitespace Scan**. The Deep Extraction and adversarial proof pass exposed one naming risk: absence from a brand's account does not prove a market gap or profit.

The recommended production name is now **Profit-Finder Opportunity Scan**. It preserves Adil's source phrase while requiring the output to distinguish account, category, and market evidence.

## Net-New Capability

The current Creative Strategy Brief begins after the user supplies `[Target Market]`. It develops that target into audience psychographics, positioning, category-pattern disruption, hooks, proof requirements, and an asset brief.

The proposed workflow sits one decision earlier:

`unresolved target or repetitive strategy → variable triage → one selected-or-held hypothesis → existing Creative Strategy Brief`

It owns only the current fingerprint, evidence receipt, three opportunity lanes, scope label, selection or hold, compact handoff, and falsifiable test design. It emits no hooks or creative assets.

## Architecture

Layer | Artifact | Purpose
---|---|---
Source memory | `references/source-delta-zX61pyC1vLM.md` | Preserve timestamps, joint Adil/Matthew attribution, mechanics, anecdotes, and evidence boundaries
Execution | `workflows/profit-finder-opportunity-scan.md` | Diagnose strategy sameness, run three lanes, select one hypothesis or hold
Deterministic prompt | `references/prompts-v2/profit-finder-opportunity-scan.md` | Produce the same evidence-bounded packet across runs
Router | Focused `SKILL.md` update | Fire before the Creative Strategy Brief when the correct target or market variable is unresolved
Front door | Minimal `agents/luke-iha/AGENT.md` reference | Surface the new Domain 2 capability without creating or changing an Adil identity
Judgment layer | Focused `genius.md` update | Add the fingerprint, whitespace scopes, hold state, and anti-patterns without copying all fourteen source patterns
Provenance | Existing Luke source ledger plus the source delta | Keep Luke and Adil sources distinguishable
Menu | Generated `/profit-finder-opportunity-scan` wrapper | Make the workflow reachable without duplicating its method
Behavior proof | Frozen Fieldwell before/after fixture | Prove variable triage changes the decision, not merely the prose

## Three-Lane Decision Model

Lane | Question | Allowed result
---|---|---
Product/use case | Does a substantiated product truth intersect an observed buyer situation the current strategy does not address? | `TEST HYPOTHESIS` or `HOLD`
Adjacent surface | Does the buyer appear in another identity, community, channel, or distribution context with evidence and access? | `TEST HYPOTHESIS` or `HOLD`
Language/geography | Is another market supported by demand, native language, operational readiness, rights, compliance, and economics? | `TEST HYPOTHESIS` or `HOLD`

The workflow never fabricates three opportunities to complete a template. All three lanes may hold.

## Evidence Scope

Scope | What it proves
---|---
Account whitespace | The inspected brand assets do not contain the idea
Category whitespace | A named, bounded competitor set does not contain the idea
Market whitespace | Wider evidence supports demand and underserved supply

Only the third supports the phrase `market whitespace`. None of the three alone proves profit.

## Frozen Proof Case

The behavior test uses fictional composite brand Fieldwell: a $78 split-front canvas apron marketed only to US home cooks. Twelve of eighty supplied reviews mention pottery or ceramics.

The expected new behavior is to classify the current hook set as one strategy, identify pottery as account-level evidence, select wheel-throwing ceramicists as a bounded use-case test hypothesis, hold pottery-studio distribution, hold language/geography, and pass the result into the existing Creative Strategy Brief. The workflow must not claim segment size, demand, profit, or product intent.

The complete assertion set is in [behavior-proof-plan.md](behavior-proof-plan.md).

## Build Contract

The exact new, modified, unchanged, validation, and approval surfaces are frozen in [skill-system-contract.md](skill-system-contract.md).

The build adds one workflow, one born-v2 prompt, one source delta, one thin generated wrapper, and one behavior fixture. It makes focused updates to Luke's `SKILL.md`, `genius.md`, source ledger, and one Domain 2/activation reference in the existing Luke agent. Luke's identity and domain architecture stay intact. So do sibling skills and every global or external surface.

## Quality Gates

1. The current seven-workflow Luke skill must retain its `0/7` baseline in `skill_auditor.py`.
2. The new prompt must pass the structure-pure v2 audit with zero failures.
3. Natural-language routing must rank the new workflow for target-selection and cosmetic-angle-churn requests, while ordinary brief-writing requests still route to the existing Creative Strategy Brief.
4. The Fieldwell fixture must pass all ten success assertions and none of the failure assertions.
5. Runtime observation, behavioral reliability, localization, demand, and market performance must remain distinct proof states.
6. A health-related input must hold unsupported claims and route to claim clearance before creative work.
7. A direct-translation request without market readiness must return `HOLD`.
8. Workflow, prompt, and generated wrapper stems must match exactly: `profit-finder-opportunity-scan`.

## Function Ownership

Owner | Owns | Does not own here
---|---|---
Profit-Finder Opportunity Scan | Variable triage and locked hypothesis | Hooks, assets, localization, outreach, or full research execution
Luke Creative Strategy Brief | Develops the selected target into a complete brief | Reopening the locked target without new evidence
Luke Avatar Machine or Dara Denney | VOC and persona evidence | Declaring market whitespace from account absence
Tim Danilov | Adjacent-format/community execution | Market-demand validation
Alex Myatt | Concept diversity and production testing | Upstream target selection
April Dunford plus native/legal/operations owners | Localization and market-entry validation | Automatic translation or legal clearance

## Proof Ladder

State | Meaning after this checkpoint
---|---
Source captured | Yes
Deep mechanics extracted | Yes
Architecture approved | Yes
Skill files built | Yes — scoped Luke in-place extension
Structural proof | PASS — 3,773/3,773 prompt files and Luke 0/7 failures
Routing observed | PASS — `workflow_router.py` ranks all three approved positives first; negatives retain existing owners
Runtime observed | `RUNTIME_OBSERVED — ONE FROZEN FIXTURE`
Behavioral reliability | Untested
Market performance | Untested

## Decision Surface

### LOCKED

One functional owner, one upstream workflow, one deterministic prompt, one source delta, and one frozen before/after fixture.

The workflow can select one hypothesis or hold. It labels account, category, and market evidence separately.

The existing Creative Strategy Brief remains the downstream owner of psychographics, positioning, hooks, proof architecture, and asset briefing.

### PARKED

A new Adil skill or agent, a 10–15 workflow package, a new expert front door, downstream production methods, list-rental tactics, unsupported health claims, direct translation, and all external deployment.

### NEXT ACTION

Architecture was approved. The scoped Luke extension is now built and checkpoint 3 contains the sample output, structural checks, route evidence, and unresolved proof gaps. The next action is to approve or reject Verification before Phase 8 closeout.
