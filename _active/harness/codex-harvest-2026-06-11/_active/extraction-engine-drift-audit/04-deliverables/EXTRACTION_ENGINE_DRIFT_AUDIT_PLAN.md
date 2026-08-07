# Extraction Engine Drift Audit And Slash Surface Recovery

## Summary

This plan audits whether the current extraction engine has drifted away from the user's intended Extraction Forge standard: source-truth first, expert operating method extracted deeply, command surfaces deployable, and behavior-changing proof visible.

The immediate Meg repair fixed one concrete failure class: YouTube captions were preserved as row-shaped ledger evidence but not reconstructed into a clean transcript surface. It also exposed a second failure class: core extraction commands existed but were cold-quarantined away from live Codex slash access.

This follow-up audit treats those as symptoms, not the whole disease.

## Audit Goals

- Determine whether `/extraction-governor-agent` is over-triaging source work into conceptual templates instead of preserving source mechanics.
- Determine whether `/extract-forge` still produces mastery-grade extraction or has been weakened by routing, source-package, or bridge drift.
- Determine whether `/source-to-skill-system` is creating durable behavior-changing systems or just skill wrappers and proof language.
- Determine whether video source packages preserve clean transcripts, timestamped evidence, visual/OCR limits, and source claim boundaries.
- Determine whether slash command access is restored for the extraction routes the user expects to deploy directly.

## Baseline Comparisons

Use prior high-quality extraction wins as regression references:

| Reference | Why It Matters |
|---|---|
| Oren solo AI marketing extraction | Transcript-backed build with workflow bridge and validation passes. |
| Sam Parr copywriting companion OS | Before/after proof lab, behavior-changing extraction contract, and live-surface validation. |
| Agentic engineering harvest | Transcript grounding, additive contract wiring, and verifier-backed source truth. |
| Josh first-drop package | Concrete launch package, visible approval gate, demand-test framing, and inside-joke readability. |

## Audit Passes

### 1. Source Package Truth

Check recent YouTube-backed extractions for:

- raw transcript or VTT preserved;
- clean continuous transcript available;
- timestamped segments or ledger available;
- visual/OCR claims separated from spoken evidence;
- uncertainty report present;
- no synthesis when source fetch failed.

Primary verifier: `execution/verify_video_context_source_package.py`.

### 2. Extraction Command Surface

Check that the expected extraction commands are live and deployable:

- `/extract`
- `/extract-forge`
- `/extract-vision`
- `/extract-amplify`
- `/video-source-extract`
- `/video-transcript-ledger`
- `/source-to-skill-system`
- `/extraction-governor-agent`

Primary verifier: `execution/verify_extraction_command_surface.py`.

### 3. Forge Quality Regression

Compare current forge outputs against prior strong outputs using these criteria:

- source mechanics preserved;
- verbatim or timestamp-backed evidence available;
- hidden knowledge extracted, not paraphrased into generic advice;
- workflows are practitioner-grade and executable;
- examples are concrete and source-derived where possible;
- behavior-changing proof exists before deployment is claimed;
- command bridges and routing surfaces are usable from cold start.

### 4. Governor Behavior Audit

Audit whether `/extraction-governor-agent` is:

- correctly deciding build shape;
- preventing duplicate systems without suppressing useful source depth;
- handing off to `/source-to-skill-system` or `/extract-forge` when a build is needed;
- preserving source grounding before synthesis;
- avoiding rigid proof templates that narrow future deployment.

### 5. Restore-The-Magic Regression Set

Create a small regression set from known good work. Each future extraction must pass:

- source package truth check;
- clean transcript availability;
- build-shape decision;
- behavior proof;
- cold-start command invocation;
- one output that changes a real artifact, not only a theory map.

## Repair Backlog Shape

Each issue found should be logged with:

| Field | Meaning |
|---|---|
| Severity | Critical, High, Medium, Low |
| Failure Class | Source truth, command access, forge depth, governor routing, proof quality, template drift |
| Evidence | File, verifier output, or before/after comparison |
| Owner Route | `/system-audit`, `/repeatability-spine`, `/skill-anneal`, `/source-to-skill-system`, or `/extract-forge` |
| Repair | The smallest change that fixes behavior |
| Proof | The verifier or cold-start run that proves repair |

## First Audit Run Recommendation

Start with a read-only audit before more mutation:

```text
/system-audit extraction engine drift, slash command access, source package truth, and forge quality regression. Use the Meg repair as the triggering incident and compare against Oren, Sam Parr, agentic engineering, and Josh prior wins.
```

## Acceptance Criteria

The extraction engine is not considered repaired until:

- core extraction commands are live or intentionally documented as cold;
- YouTube source packages include clean transcripts and timestamped evidence;
- extraction outputs separate source mechanics from domain extrapolation;
- at least two recent extractions are checked against the restore-the-magic regression set;
- future agents can run `/extract-forge` or `/video-source-extract` from a cold start without needing the conversation history.
