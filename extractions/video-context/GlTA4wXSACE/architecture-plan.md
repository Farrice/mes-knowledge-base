# Architecture Plan: Shaan Puri Story Deployment System

**Checkpoint:** 3 of 3 validated; architecture approved by Farrice on 2026-08-02
**Architecture verdict:** One new decision behavior, six preserved production workflows, no duplicate storytelling system

## The decision

Add one canonical `/shaan-story-deploy` front door inside the existing `shaan-puri-storytelling` skill. It decides the narrative dosage before Shaan's full methodology loads:

```text
User brief + supplied facts + truth risk
                |
       Shaan Story Deployment Router
          /            |             \
   Full story    Story fragment     No story
       |               |               |
 Story Compass    Evidence/direct     Direct domain
 if needed        spine + one move    owner
       \               |               /
          exactly one production owner
                       |
              truth and quality gates
                       |
        final asset + deployment receipt
```

This is not “make everything a story.” It is “apply story judgment to every communication task.” The system becomes more portable because it can refuse its own signature technique.

## What amplification changed

The Vision proposed two possible behaviors. The amplification pass revised that to one:

- **Build:** Story Deployment Router.
- **Integrate:** adjacent-field mechanic transfer as a bounded handoff to an existing function owner.
- **Reject:** a standalone transfer workflow, second Shaan skill or agent, second writing conductor, or arbitrary workflow-count expansion.

## Workflow architecture

| Tier | Workflow | Job | Primary stacking partner | Status |
|---|---|---|---|---|
| Foundation | `shaan-story-deploy` | Decide full story, truthful fragment, or no story; select one route; protect facts | Story Compass, How I Write, verification, or one transfer owner only when selected | New |
| Foundation | `narrative-script-optimization-audit` | Diagnose and reconstruct supplied narrative or script material | Story Compass, then How I Write for long-form copy | Preserve and repair |
| Foundation | `signature-story-bank` | Build a bounded bank of identity-bearing stories from supplied facts | How I Write for public-facing composition | Preserve and repair |
| Practitioner | `brand-identity-emotional-blueprint` | Define audience, feeling, position, voice, and content implications | Brand or positioning owner when the job exceeds storytelling | Preserve and repair |
| Practitioner | `viral-social-content-engine` | Turn supplied expertise into framed social-content options and selected executions | Current research or platform adaptation when needed | Preserve and repair |
| Practitioner | `story-driven-sales-conversion-funnel` | Build a story-led sales page and email sequence when narrative is justified | Copy owner plus fact and claim gate | Preserve and repair |
| Practitioner | `voice-transfer-engine` | Create a trainable voice-transfer kit from real source samples | Voice source, How I Write, and voice verification | Preserve and repair |

There is deliberately no new stacking-tier workflow. Stacking is conditional routing, not another production engine.

## Prompt execution layer

Forge requires one born-v2 prompt per distinct deliverable and an execution-prompt pointer in every producing workflow. The current six workflows return composite deliverables that do not match any single one of the sixteen current atomic prompts. The plan therefore adds seven exact-stem prompts:

| New born-v2 prompt | Purpose |
|---|---|
| `shaan-story-deploy.md` | Produce the decision brief and handoff; no body copy |
| `narrative-script-optimization-audit.md` | Stabilize the current diagnosis, hooks, rebuilt asset, and production notes |
| `signature-story-bank.md` | Stabilize the current story-bank and origin-story deliverable |
| `brand-identity-emotional-blueprint.md` | Stabilize the current audience, feeling, position, voice, and audit deliverable |
| `viral-social-content-engine.md` | Stabilize the current content dossier and ranked executions |
| `story-driven-sales-conversion-funnel.md` | Stabilize the current sales-page, email-sequence, and nested-story deliverable |
| `voice-transfer-engine.md` | Stabilize the current format, rationale, example bank, filters, and apprenticeship kit |

Only the first prompt represents new source-derived behavior. The other six are execution-debt repairs required by the invoked Forge contract; they do not inflate the source-mechanics count.

The current sixteen atomic prompts remain available. The four active surfaces with incomplete truth guards—Story Architecture, Viral Content Engineering, Email Sequence Architect, and Video Script Transformer—receive a shared factual-integrity repair. Matching source prompts are updated where they are the declared provenance. `_legacy-prompts/` remains untouched.

## Exact file plan

### Create: canonical capability

- `skills/shaan-puri-storytelling/workflows/shaan-story-deploy.md`
- `skills/shaan-puri-storytelling/references/story-deployment-map.md`
- seven exact-stem files under `skills/shaan-puri-storytelling/references/prompts-v2/`
- `extractions/video-context/GlTA4wXSACE/behavior-proof.md` after the fixtures run
- sidecar metadata for long-form human-facing proof artifacts

### Create: invocation and compatibility

- `.agent/workflows/shaan-story-deploy.md`: explicit thin bridge that loads the decision workflow before `genius.md`
- `.claude/commands/shaan-story-deploy.md`: compatibility shim
- `.agents/skills/source-command-shaan-story-deploy/SKILL.md`: live Codex bridge, logically cold unless directly invoked or routed
- `.agent/workflows/shaan-puri.md`: repaired expert front door pointing to story deployment
- `.agent/workflows/shaan-puri-storytelling.md`: repaired skill front door pointing to story deployment
- `.agents/skills/source-command-shaan-puri-storytelling/SKILL.md`: missing live Codex bridge
- decision-first direct bridge triplets for the brand, narrative-audit, and viral-social workflow names; repaired direct shims for signature-story, sales-funnel, and voice-transfer routes

The current `.agents/skills/source-command-shaan-puri/` bridge is updated in place. No global `~/.codex` mirror is created.

### Update: current Shaan package

- `skills/shaan-puri-storytelling/SKILL.md`: repair truncation; make `shaan-story-deploy` primary; list seven workflows; explain decision-first loading, handoffs, and refusal.
- `skills/shaan-puri-storytelling/genius.md`: add the source-backed applicability rule; add real Decision Framework and Voice DNA sections already referenced by all six workflows; repair the truncated exemplar and duplicate heading; label constructed examples; distinguish internal evolution from Shaan-derived mechanics.
- `skills/shaan-puri-storytelling/references/genius-patterns.md`: replace the stale duplicate with a compact, source-labeled pattern index.
- `skills/shaan-puri-storytelling/references/source-ledger.md`: register the canonical source package, timestamps, claims, and limits; remove the stale no-package statement.
- `skills/shaan-puri-storytelling/references/PROVENANCE-2026-07-18.md`: add the current native package without erasing the earlier receipt.
- `agents/shaan-puri/AGENT.md`: remove or mark unconfirmed 8-figure and 400K claims; add conditional deployment, refusal, and handoffs.
- all six current workflow files: valid frontmatter; consistent pre-flight and referenced sections; required content adaptations; shared truth invariant; exact prompt pointer; preserved methodology and output.
- four active v2 prompts and their declared source prompts: complete factual-integrity repair.
- `.agent/workflows/narrative-script-optimization-audit.md` and its Claude shim: remove the stale unsupported credential description.
- `.agents/skills/source-command-shaan-puri/SKILL.md`: make the new router the flagship path.
- `atomize`, `launch-day`, `parallel-content`, `jackpost`, `ship`, `yt-flywheel`, and `watch-and-remix`: replace eager Shaan loading with the dosage-first front door; retain their existing output jobs.
- `execution/context_retriever.py` and the Shaan chunk subset in `execution/skill_chunks.json`: enforce skill-only preselection retrieval and keep `genius.md` cold until a route is selected.

### Generated or synchronized with inspection

- prompt index and execution-prompt menu;
- Shaan-attributable skill and slash-command index entries;
- skill-command registry and relevant command menu entries.
- Shaan-only context-retrieval chunks, with `genius.md` excluded from preselection retrieval by the skill's declared cold-context policy.

Repository-wide generators will run only after the source edits are complete. Every generated diff is inspected; unrelated Alex Copper, orphan-shim, or arsenal-index churn is rejected. The menu minter is preview-only unless its output preserves decision-first context isolation.

### Explicitly untouched

- `skills/story-compass/**`
- `skills/how-i-write-os/**`
- current transfer engines and their behavior contracts, except a bounded `watch-and-remix` adapter repair that adds dosage-first loading and evidence labels without replacing its remix contract
- `SKILL.md.old`
- `_legacy-prompts/**`
- semantic control-plane primitives
- global `~/.codex` files
- Mission state, publication surfaces, connectors, and external systems

## Router contract

The router must return:

1. `Narrative decision`: `FULL STORY`, `STORY FRAGMENT`, or `NO STORY`.
2. `Why`: objective, audience, medium, material sufficiency, and truth-risk reasoning.
3. `Selected mechanic`: one Shaan operation or `NONE`.
4. `Production owner`: exactly one workflow or external route.
5. `Truth constraints`: facts, uncertainty, prohibited inventions, and required labels.
6. `Execution handoff`: compact inputs and paths for the selected owner.
7. `Exit condition`: what must be true before the asset can ship.

The workflow continues into the selected route in the same run. Farrice does not manually copy and paste the handoff. The final response returns the produced asset and a compact receipt.

## Shared factual-integrity invariant

Every branch and producing workflow must preserve supplied facts and uncertainty. It may not invent dialogue, chronology, numbers, results, motives, emotional states, or sensory details as real. Constructed examples, composites, and analogies must be labeled. In evidence-sensitive work, story may aid comprehension or recall but cannot replace evidence or strengthen causality.

## Context plan

| State | Loaded material |
|---|---|
| Hot | User brief, Story Deployment Map, decision schema, truth invariant |
| On demand | `genius.md`; exactly one selected workflow and prompt; Story Compass; How I Write; one transfer owner |
| Cold | Full transcript, frames, complete ledgers, other Shaan workflows and prompts, unrelated experts |

This prevents eager Shaan context from turning every problem into a story.

The policy is executable: `context_retrieval: skill-only-until-selected` in the skill frontmatter tells `execution/context_retriever.py` to index only `SKILL.md` for preselection. The selected workflow loads `genius.md` explicitly after routing. Checkpoint 3 also repaired seven existing callers—`atomize`, `launch-day`, `parallel-content`, `jackpost`, `ship`, `yt-flywheel`, and `watch-and-remix`—that previously bypassed the new order.

## Checkpoint 3 proof

| Fixture | Expected decision | Acceptance condition | Automatic failure |
|---|---|---|---|
| Synthetic founder fact packet | `FULL STORY` | Story Compass passes; result gains intention, obstacle, five-second turn, and supplied-fact contrast | Invented dialogue, emotion, chronology, metrics, or transformation |
| Evidence-sensitive patient explainer | `STORY FRAGMENT` | Evidence spine and uncertainty remain primary; one analogy or moment is clearly labeled | Anecdote presented as evidence or stronger causality |
| Synthetic API-migration decision memo | `NO STORY` | Decision, owner, deadline, options, and tradeoffs become easier to scan without a dramatic arc | Protagonist arc, outage scene, emotionalized risk, or buried decision |

For every fixture, record the weak input, diagnosis, mechanics, output, behavior delta, validation, and remaining risk. Pass requires the correct route and zero invented facts. The review loop stops after two failed repair passes on the same defect.

## Verification sequence

1. Source package verification.
2. Renaissance prompt audit at zero failures.
3. Prompt index build and mandatory pointer wiring; keep only attributable changes.
4. Explicit bridge checks across `.agent`, `.claude`, and `.agents`.
5. `validate_skill.py` and `skill_auditor.py` for `shaan-puri-storytelling`.
6. `verify_extraction_command_surface.py` for `shaan-story-deploy`, `shaan-puri`, and `shaan-puri-storytelling`.
7. Natural-language probes through the command menu, workflow router, and context retriever.
8. Three detached behavior fixtures and factual-integrity review.
9. Strict Codex live-surface and system checks, with unrelated baseline failures separated.
10. Human-facing artifact prose and export guards.
11. Forge finalize and local usage record.

The documented active behavior-proof verifier is absent, so the proof contract is enforced manually in `behavior-proof.md` rather than hidden behind a false green check. A detached fixture pass proves repository behavior, not market performance. A-tier embodiment remains pending a real reference corpus and Farrice's recognition judgment.

## Architecture decision ledger

### LOCKED

- One in-place Shaan expansion.
- One new behavioral workflow.
- Decision first; methodology loads second.
- Full story, truthful fragment, and no-story refusal.
- Six current workflows preserved and repaired.
- Forge-complete exact execution prompts.
- One production owner and a uniform truth invariant.
- Three detached fixtures before deployment.

### PARKED

- New Shaan skill or agent.
- Generic adjacent-field-transfer workflow.
- New How I Write or Story Compass system.
- Additional storyteller stack.
- Global mirrors or hot-default promotion.
- External publication or deployment.
- Universal, causal, demand, or market-performance claims.

### REJECTED

- Forcing a story into every domain or task.
- Treating structural validators as behavior proof.
- Preloading the full Shaan context before the applicability decision.
- Absorbing unrelated generator churn.

## Approval record

Farrice approved this architecture on 2026-08-02. The bounded local skill, workflow, prompt, agent, bridge, and attributable registry changes are implemented in the isolated Codex worktree and passed Checkpoint 3 local proof. Global mirrors, publication, external deployment, commits, pushes, and claims of market effectiveness remain outside that approval.
