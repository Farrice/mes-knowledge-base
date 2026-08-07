# Source-To-Skill System Pilot Extraction

## Source

- Video: `THIS Gives Claude Skills a Massive Upgrade (It’s Easy!)`
- Channel: Simon Scrapes
- Local package: `extractions/video-context/FD53kEpLh9c/`
- Evidence: transcript-only package with 780 observed spoken rows
- Limitation: frame extraction and OCR were skipped, so visual claims are unavailable

## Operating Lesson

The source argues that skill quality is not mainly about having more skills. The durable pattern is:

1. keep skills small and focused
2. avoid isolated one-off calls that leave the user as the connector
3. avoid mega-skills that destroy modularity and progressive disclosure
4. wire components together with an orchestrator
5. define inputs, outputs, handoffs, checkpoints, validation, and result display
6. reuse components across multiple systems

## Codex Antigravity Translation

Codex Antigravity should treat source-to-capability work as a system design problem:

- component skills and workflows stay modular
- `/autopilot`, `/mission`, and `/source-to-skill-system` provide orchestration
- bridge wrappers remain compatibility surfaces, not proof of real usage
- validation proves routing, bridge coverage, contract completeness, and cold-start usability
- hot routes stay visible while the broad command library remains router-accessed

## Pilot Build Decision

Build shape: companion OS layer plus pilot workflow.

Not a standalone expert skill. The method changes how future skills and workflows should be assembled across the whole Codex workspace.

## First Use

Run:

```bash
/source-to-skill-system [source URL or package path]
```

Expected first artifact: a filled skill-system contract that names source evidence, components, order of operations, handoffs, checkpoints, validation, result surface, context policy, and reuse hook.
