---
description: Cold companion gate for copy that feels smart but makes readers decode the offer; audits messaging, content, offers, and copy for one-problem clarity, five-soundbite fit, hero/guide alignment, cognitive load, and repeatable language before downstream writing or copy work
---

# /low-cognitive-load-message-gate

Use this when a message, offer, draft, hook, homepage, pitch, content package, or sales copy is structurally useful but still makes the reader think too hard.

This is a companion OS layer. It does not replace `/storybrand-message-clarity-system`, `/farrice-content-os`, `/high-taste-writing-os`, `/publishable-copy-gate`, Writing Agent, Copywriting Agent, or the Donald Miller skills. It gives those owners a low-cognitive-load checkpoint before they polish, package, or score the output.

Function owner: the downstream workflow owns the final artifact. This gate owns only the clarity stop condition and the handoff.

## Use When

- The reader should understand the message in one pass.
- The draft has multiple problems, benefits, audiences, or promises fighting each other.
- The copy sounds smart, sophisticated, clever, or complete but not instantly repeatable.
- The copy feels smart but the reader has to decode the offer, problem, or next step.
- A source, product, service, offer, or brand message needs to become content or sales copy.
- `/storybrand-message-clarity-system` is producing or revising a Message Clarity Pack.
- Public, revenue, client, or authority-building writing needs a clarity check before craft or conversion scoring.

Skip when the user only wants raw notes, private brainstorming, or a pure literary/craft pass with no offer, brand, product, or service message.

## Source Authority

Load only what the current step needs:

1. `semantic_libraries/antigravity/primitives/low-cognitive-load-message-gate.md`
2. `extractions/donald-miller/storybrand-message-clarity-system/source-map.md`
3. `extractions/donald-miller/storybrand-message-clarity-system/extraction-brief.md`
4. `skills/donald-miller-cognitive-load/SKILL.md`
5. `skills/donald-miller-cognitive-load/workflows/02-peace-soundbite-generator.md`
6. `skills/donald-miller-storybrand/SKILL.md`
7. `.agent/workflows/storybrand-message-clarity-system.md` when building a full Message Clarity Pack

Use `extractions/video-context/SzugliCQ3XY/` as the newest interview package. Preserve its uncertainty report: if transcript, frame, or OCR evidence is unavailable, say so instead of treating public transcript notes or inference as observed evidence.

## Phrase Load Categories

Score actual customer-facing phrases before rewriting them. Do not score a summary of the message.

| Category | Signal | Typical Fix |
|---|---|---|
| Jargon load | Internal, technical, or category language the customer would not say. | Replace with the customer's felt wording. |
| Abstract promise load | Big outcomes with no concrete before/after. | Name the specific relief, result, or job done. |
| Multi-problem load | One phrase tries to solve several problems. | Pick the most felt problem and move the rest downstream. |
| Cleverness load | The phrase sounds smart but requires interpretation. | Say the simple thing directly. |
| Hero confusion load | The brand, method, or founder becomes the main character. | Move the customer back into the hero position. |
| Product-first load | The product appears before the problem is understood. | Start with the problem, then introduce the answer. |

Use `0 lbs`, `25 lbs`, `50 lbs`, `75 lbs`, or `100 lbs` as the score. A phrase only earns `0 lbs` if a non-specialist can understand and repeat it on the first read.

## Skill System Contract

| Field | Required Output |
|---|---|
| Source evidence | Local source path, supplied message/copy, and uncertainty limits. |
| Objective | Decide whether a message is easy to understand, easy to repeat, and ready for downstream writing or copy work. |
| Components | Donald Miller cognitive-load skill, StoryBrand skill, source map, target downstream workflow, and optional copy/content quality gate. |
| Step order | evidence check -> one-hole lock -> PEACE fit -> hero/guide fit -> cognitive-load risks -> repeatability lock -> required fixes -> verdict. |
| Inputs | Business or object, target reader/customer, current message or draft, offer/product/service, intended channel, optional existing PEACE sound bites. |
| Outputs | Gate report with verdict, required fixes, and a compact handoff to the downstream owner. |
| Handoff summary | Pass only the locked problem, selected sound bites, heavy phrases, hero/guide correction, repeatability lock, and open risks. |
| Composition rule | This gate owns clarity only; downstream workflow owns final content, copy, design, or delivery. |
| Human checkpoint | Ask only when the target reader, offer, or primary problem cannot be inferred without changing the message. |
| Validation | Phrase-level load scores, one problem, plain language, customer-as-hero, exact repeated phrase, and clear PASS/REVISE/REWORK verdict. |
| Result surface | Rendered gate report in conversation or embedded as a section inside the downstream workflow output. |
| Context policy | Keep this workflow cold and compact; load source packages and component workflows on demand. |
| Reuse hook | Call before StoryBrand packs, Farrice content packaging, high-taste polishing, and publishable copy scoring. |

## Operating Flow

### 1. Evidence Check

Identify what the gate is judging:

- supplied draft, offer, homepage text, hook, social post, pitch, or raw idea
- source evidence path, if any
- intended downstream workflow
- evidence limits

If the source is `SzugliCQ3XY`, preserve whether the local package contains observed spoken rows, frame rows, OCR rows, or only uncertainty rows.

### 2. One-Hole Lock

Name exactly one customer or reader problem.

Fail this step if the problem:

- contains commas that bundle multiple problems
- names a category instead of a felt problem
- starts with the product, method, mission, company, or credentials
- could apply to almost any business

Output:

- selected problem
- rejected problem bundles
- why the selected problem is the clearest hole

### 3. PEACE Soundbite Fit

Check whether the message has the five roles:

| Role | Test |
|---|---|
| Problem | Names one felt hole. |
| Empathy | Shows the guide understands without becoming the hero. |
| Answer | Names the simplest action, product, service, or mechanism. |
| Change | Shows who the reader/customer becomes. |
| End Result | Mirrors the problem in positive form. |

If PEACE sound bites are missing, draft the minimum viable candidates. If they exist, audit them and preserve the strongest phrasing.

### 4. Hero/Guide Fit

Check whether the audience is the hero and the brand/product/service is the guide, tool, or rope.

Flag:

- company-as-hero language
- founder story before customer problem
- credentials before empathy
- product explanation before the hole is clear
- CTA that asks the reader to decode the next step

### 5. Cognitive Load Risks

Score and identify heavy language:

- jargon
- abstract category words
- stacked promises
- vague transformation language
- clever phrases that require interpretation
- internal language the customer would not repeat

For each heavy phrase, give a zero-load rewrite direction. Do not over-polish; plain beats clever.

Output at least one scored phrase row when supplied copy exists. If no copy exists, score the proposed problem, answer, and repeatability-lock candidates instead.

### 6. Repeatability Lock

Choose the exact phrase that should repeat across channels. It can be the Problem, End Result, Answer, or a short one-liner.

The phrase must pass:

- a non-specialist can repeat it after one read
- it works outside the current paragraph
- it can survive website, social bio, email, proposal, and sales-call use
- it does not depend on trend timing or hidden context

### 7. Required Fixes

List only the fixes required before downstream work. Do not rewrite the whole artifact unless the downstream owner needs it.

Use:

- `Keep`: strongest phrase or structure
- `Change`: exact clarity issue
- `Fix`: replacement direction or wording
- `Downstream handoff`: who owns the next pass

### 8. Verdict

Use one verdict:

- `PASS`: message is clear enough for downstream craft, content, or copy work.
- `REVISE`: the message can proceed after named clarity fixes.
- `REWORK`: do not polish or publish yet; one-hole, hero/guide, or repeatability is broken.

## Output Schema

```markdown
## Low-Cognitive-Load Message Gate

### Route
- Owner:
- Downstream workflow:
- Source evidence:
- Evidence limits:

### One-Hole Lock
- Selected problem:
- Rejected bundles:
- Why this problem wins:

### PEACE Soundbite Fit
| Role | Current / Candidate | Verdict | Required Fix |
|---|---|---|---|

### Hero/Guide Fit
- Customer-as-hero:
- Brand-as-guide:
- Product placement:
- CTA clarity:

### Cognitive Load Risks
| Phrase | Load | Category | Why It Is Heavy | Zero-Load Direction |
|---|---:|---|---|---|

### Repeatability Lock
- Phrase to repeat:
- Where it should appear first:
- Do not vary:

### Required Fixes
| Keep | Change | Fix | Downstream Handoff |
|---|---|---|---|

### Verdict
- PASS / REVISE / REWORK:
- Reason:
- Next owner:
```

## Quality Gate

Reject the run if:

- no single problem is locked
- supplied phrases are not scored
- the business is the hero
- the product appears before the reader knows why it matters
- the strongest phrase cannot be repeated by a non-specialist
- the report praises clever language that adds cognitive load
- source claims exceed the local evidence package
- the output becomes a standalone rewrite instead of a gate/handoff
- expert names are used as proof of integration

## Verification

After changing this workflow or wiring it into another surface, run:

```bash
python3 execution/command_menu.py search "low cognitive load message gate soundbite offer clarity"
python3 execution/workflow_router.py search "message makes reader think too hard one problem soundbite gate"
python3 execution/command_menu.py search "StoryBrand soundbite strategy clarify my business message"
python3 execution/validate_skill.py donald-miller-storybrand
python3 execution/validate_skill.py donald-miller-cognitive-load
python3 execution/codex_live_surface_audit.py --strict
python3 execution/codex_harness_check.py
```

**Execution prompts**: before producing the deliverable, check `skills/donald-miller-cognitive-load/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
