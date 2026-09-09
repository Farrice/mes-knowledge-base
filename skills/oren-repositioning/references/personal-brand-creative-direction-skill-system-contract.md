# Personal Brand Creative Direction Skill System Contract

## Source Evidence

- Public source: `https://www.youtube.com/watch?v=tUlkycPTZm0`
- Verified package: `extractions/video-context/tUlkycPTZm0/`
- Mastery extraction: `extractions/oren-personal-brand-creative-direction/mastery-extraction.md`
- Evidence state: 822 cleaned native-caption segments, 5,638 continuous transcript words, and 40 reviewed scene-aware frames
- Limits: speaker-reported results and budgets are not independently verified; market outcomes, human taste preference, and publishing behavior are untested

## Objective

Turn a founder or creator's positioning, lived source material, and existing assets into a 90-day personal-brand creative-direction system that keeps content, distribution, visuals, styling, collaborators, and launches inside one coherent world.

## Components

| Component | Function | Ownership Boundary |
|---|---|---|
| `oren-repositioning` | Function owner and integrator | Diagnoses counterposition, vision vector, and overall personal-brand direction |
| `/personal-brand-creative-direction` | Front door | Produces the integrated 90-day system and routes specialist work |
| `/personal-brand-idea-room` | Source-rich ideation | Runs the biweekly conversational mining protocol and creates the ranked concept slate |
| `/personal-brand-world-kit` | Visual/world translation | Defines repeatable set, design, styling, collaboration, and campaign signals |
| `oren-identity-brand-os` | Upstream identity | Used when the founder's public identity or audience bond is not yet grounded |
| `oren-content-team-architecture` | Team and operating system | Used for pod design, cadence, founder-as-character, content flywheel, and production scaling |
| `oren-taste-development` | Scarce craft judgment | Used for art direction, moodboard alignment, and human taste review |
| `oren-norton-world-building` | Deep construction | Used when the job requires institutions, props, lore, initiation, or a full world bible |
| `oren-operational-systems` | Execution infrastructure | Used when briefs, assets, approvals, and production need a durable operating layer |

## Composition Rule

`oren-repositioning` is the sole function owner. Supporting components contribute only their bounded specialty. The front door passes source paths and compact handoffs, never the full transcript. No expert name or file presence counts as integration proof; the final 90-day system must show which contribution changed which decision.

## Step Order

1. **Evidence and identity intake** — gather founder facts, current assets, category context, constraints, and source boundaries.
2. **Role-ladder diagnosis** — separate creative strategy, content operations, and full creative-direction scope; assign owners.
3. **Direction spine** — lock authority promise, cultural root, counterposition, transformation narrative, and 10-year vector.
4. **Idea Room** — mine niche news, recent life, camera-roll history, outlier formats, and AI provocations; tier concepts.
5. **World Kit** — translate the spine into recurring topics, formats, stories, sets, design, styling, collaborators, and campaign sequences.
6. **Distribution and operations** — map digital, physical, collaborator, and audience-participation surfaces; assign cadence and handoffs.
7. **Pilot and review** — create three briefs across at least two formats; run source, taste, feasibility, and permission checks.
8. **90-day lock** — keep winning signals, record evidence gaps, and produce the execution calendar without publishing automatically.

## Inputs

- Founder or creator identity, expertise, lived history, and non-negotiables
- Audience and authority outcome
- Current content, platforms, offers, collaborators, assets, and production capacity
- Category references and codes to preserve or invert
- Real stories, camera-roll evidence, topical inputs, and known proof
- Budget, team, cadence, access, privacy, and publishing constraints

## Outputs

- Role Ladder and ownership map
- Direction Spine and evidence ledger
- Ranked biweekly Idea Room slate
- Topics × Formats × Stories matrix
- Personal Brand World Kit
- Distribution and collaborator map
- Three pilot briefs
- 90-day direction and operating plan
- Proof gaps, human review points, and explicit no-action boundaries

## Handoff Summaries

### Intake -> Direction Spine

- Source evidence: founder facts, current assets, category context
- Output: verified facts, opinions, taste choices, unknowns, and constraints
- Open risk: missing private history or ungrounded audience assumptions

### Direction Spine -> Idea Room

- Source evidence: authority promise, cultural root, counterposition, recurring themes
- Output: bounded mining brief and forbidden invention list
- Open risk: founder language not yet captured conversationally

### Idea Room -> World Kit

- Source evidence: ranked concepts with real story anchors
- Output: Priority, Middle, and Backburner slate plus format/story inputs
- Open risk: topical or AI suggestions that lack founder conviction

### World Kit -> Operations

- Source evidence: approved visual grammar, styling axis, collaborators, and campaign sequence
- Output: executor-ready briefs and asset requirements
- Open risk: human taste approval, production capacity, and rights/permissions

### Operations -> 90-Day Lock

- Source evidence: pilot outputs and review notes
- Output: keep/change/kill decisions, cadence, owners, and evidence plan
- Open risk: live performance remains untested until approved publication and measurement

## Human Checkpoints

- Founder confirms private history, cultural identity, and claims before they appear in briefs.
- Farrice or the named creative owner approves the visual grammar, styling axis, and collaborator fit.
- Publishing, outreach, paid tools, purchases, location bookings, and external production require explicit approval.
- A failed taste or source check returns to the nearest reversible artifact; it does not trigger a wholesale rebuild.

## Validation

- `python3 execution/verify_video_context_source_package.py extractions/video-context/tUlkycPTZm0`
- `python3 skills/oren-repositioning/tests/verify_personal_brand_creative_direction_system.py`
- `python3 execution/renaissance_audit.py`
- `python3 execution/validate_skill.py source-command-personal-brand-creative-direction`
- Natural-language router checks for personal-brand creative direction, biweekly idea mining, and creator world kits
- Negative controls for invented founder facts, automated publishing, full-AI founder voice, and unsupported outcome claims

## Behavior-Changing Proof

The cold-start fixture transforms a generic health-performance expert brief into a direction system that:

- diagnoses Strategy vs Operations vs Direction instead of prescribing "post more";
- replaces generic tips with source-rich Topic × Format × Story concepts;
- defines a recognizable set/design/styling grammar;
- distributes the world across founder, collaborators, events, and owned surfaces;
- blocks invented founder stories, automatic publishing, and performance claims.

Proof artifact: `skills/oren-repositioning/tests/receipts/personal-brand-cold-start-output.md`.

## Result Surface

The user receives a readable Personal Brand Creative Direction System in conversation, with local Markdown persistence copies when requested or when the work must survive handoff. No external export is created by default.

## Context Policy

- **Hot:** front-door workflow, contract, current founder brief, and compact handoffs.
- **On demand:** relevant Oren component skill and the matching v2 prompt.
- **Cold:** raw transcript, full frame ledger, unrelated Oren skills, and historical extraction corpus.
- Founder voice remains human-reviewed; meeting capture may preserve language but may not authorize autonomous voice generation.

## Reuse Hook

Use `/personal-brand-creative-direction` whenever the real job is to align a founder's authority, content machine, visual identity, distribution surfaces, and collaborator world. Route narrower jobs directly to `/personal-brand-idea-room` or `/personal-brand-world-kit`. Keep deep identity, team, taste, and world construction in their existing owners.

## Promotion Boundary

This is an extension of `oren-repositioning`, not a new skill. The new front door may become a preferred Oren route only after the cold-start proof passes and at least one human-reviewed real run is preferred to the prior generic path. File presence and deterministic checks alone do not prove taste, publishing performance, or commercial results.
