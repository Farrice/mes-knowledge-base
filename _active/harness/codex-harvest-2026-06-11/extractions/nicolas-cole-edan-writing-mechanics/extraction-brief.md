# Nicolas Cole EDAN Writing Mechanics - Extraction Brief

## Source

- Source URL: `https://www.youtube.com/watch?v=gAVbSZHwzNU&t=1277s`
- Video: "The EDAN Writing Framework: Explanation, Narration, Action, Description"
- Expert/channel: Nicolas Cole
- Published: 2026-05-01
- Local source package: `extractions/video-context/gAVbSZHwzNU/`

## Build Shape

Decision: new Nicolas Cole companion skill.

Reason: the EDAN framework is not a duplicate of the existing Cole stack. `nicolas-cole-nonfiction-value-architecture` decides what value a piece gives. `nicolas-cole-sentence-craft` polishes sentences. EDAN sits between them as a paragraph/sentence-function mechanics layer: map blocks, diagnose imbalance, design block sequences, and create deliberate practice loops.

## Extracted Operating Method

EDAN unbundles writing into four functions:

| Block | Function | Revision Question |
|---|---|---|
| Explanation | Context, logic, backstory, meaning conditions | Does the reader need this context now, later, or not at all? |
| Description | Concrete detail that implies meaning | What should the reader infer without being told? |
| Action | Movement, change, consequence, reveal | What changes because this happens? |
| Narration | Point of view, belief, theme, worldview | What does this narrator/writer believe about the thing happening? |

## Skill Architecture

Skill: `skills/nicolas-cole-edan-writing-mechanics/`

| Tier | Workflow | Command | Purpose |
|---|---|---|---|
| Foundation | EDAN Block Map | `/edan-block-map` | Classify text by functional block |
| Foundation | EDAN Balance Audit | `/edan-balance-audit` | Diagnose block imbalance and revision moves |
| Practitioner | Description Upgrade | `/edan-description-upgrade` | Convert blunt explanation into implied meaning |
| Practitioner | Action Weight Test | `/edan-action-weight` | Make actions consequential |
| Practitioner | Narration POV Forge | `/edan-narration-pov` | Surface worldview/theme without preachiness |
| Stacking | EDAN Opener Builder | `/edan-opener-builder` | Build block sequences for target effects |
| Stacking | Deliberate Practice Loop | `/edan-practice-loop` | Isolate one block/combination for craft reps |
| Stacking | Source Study Deconstruction | `/edan-source-study` | Reverse engineer admired writing into reusable patterns |

## Bridge Coverage

Each command has:

- `.agent/workflows/<command>.md`
- `.claude/commands/<command>.md`
- `.agents/skills/source-command-<command>/SKILL.md`

## Verification

- Source acquisition: `execution/video_context_ledger.py` produced a grounded video package with transcript, metadata, frame notes, and ledger.
- Registry sync: `execution/sync_registries.py` completed and registered 243 skills.
- Skill validation: `execution/validate_skill.py nicolas-cole-edan-writing-mechanics` passed with 7 checks, 0 warnings, 0 critical issues.
- Command discoverability: `execution/command_menu.py search edan` returned all eight EDAN commands.
- Exact command check: `execution/command_menu.py search edan-block-map` returned `/edan-block-map`.
- Finalize: `execution/chain_runner.py finalize ... --skip-notion` logged `trace_20260507_113620_nicolas-cole-edan-writing-mechanics.json` with composite quality 8.7/10.

## Known Limitation

The finalize pass skipped Notion by design, and a regression check still attempted a Notion DNS lookup that failed. Local validation, registry sync, command discoverability, and finalize trace all passed.
