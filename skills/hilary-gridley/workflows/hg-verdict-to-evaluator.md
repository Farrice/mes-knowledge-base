---
description: Harness bridge — mine Farrice's accumulated felt verdicts, voice-ratchet history, and taste-calibration logs into minted evaluator tools; the sitting Column A/B data becomes fireable quality gates
---

# hg-verdict-to-evaluator — Compile the Taste Already on Disk

This system has been logging Farrice's judgment for months — felt verdicts, voice-ratchet corrections, taste-calibration passes, finalize notes. That is Column A/B data nobody has mined. This workflow runs the judgment-encoding pipeline over the harness's own logs and ships evaluators native to this system (skills/gates, not GPTs). Every solved taste-problem stops being re-solved.

## Pre-Flight Gate

- Load `skills/hilary-gridley/genius.md` §Crown Jewel.
- Scope ONE artifact class per run (LinkedIn posts, Substack sections, headlines, client docs...). The fleet grows one narrow tool at a time.
- Coordination: writes into the harness → session lock etiquette applies for multi-file installs.

## Skill Acquisition

- `genius.md` §Edit-Pair Rubric Mining
- Workflow `hg-edit-pair-harvest` (source-mapping discipline)

## Execution

1. **Mine the stores.** For the chosen artifact class, pull verdict-bearing records:
   - `memory_facade.py "<artifact class> verdict feedback"` — sovereign + episodic + solutions in one call
   - `.agent/sessions/` verdict/steering logs; voice-ratchet + taste-calibration entries; finalize `--notes` with felt verdicts
   - Draft-vs-shipped pairs in deliverables/ and _active/ (the strongest signal: what Farrice actually changed or chose)
2. **Assemble pairs** per `hg-edit-pair-harvest` discipline: rejected-vs-accepted siblings, corrected-vs-original, PASS-vs-FAIL exemplars from the bimodal taste signature. Filter to Farrice's judgment only. Grade provenance honestly.
3. **Run the encoding**: recurring patterns → 5±2 criteria in Farrice's vocabulary → plain-English pass/fail with real examples from the logs → evaluator.
4. **Deduplicate against standing rules.** Cross-check mined criteria against the ban-bank, VOICE-CARD, reader-contract dials, I-narrative rule. Already-canonical → the evaluator CITES the canonical file rather than restating it (one source of truth). Genuinely new patterns → these are the payload; list them explicitly as "new since last codification."
5. **Ship native.** Evaluator lands as a skill workflow / pre-delivery check usable in-session (compass-mode: it nudges, never blocks). Register per arsenal loop — wrappers are minted, never hand-written.
6. **Set the re-mine cadence**: note in the evaluator's header when to re-run this workflow (default: +10 new verdicts on this artifact class).

## Content Type Adaptations

| Artifact class | Richest stores |
|---|---|
| LinkedIn posts | Verdict logs + published-vs-draft; reader-contract dial outcomes |
| Substack/Parallax | Edition drafts vs shipped; felt verdicts on interiority/polish |
| Headlines/hooks | The 8-round variant session logs (failure-rich = signal-rich) |
| Client deliverables | Format corrections (production-sheet rule origin) + revision requests |

## Output Requirements

- Deliverable: pattern report (with "new since last codification" section) + native evaluator + provenance grade + re-mine cadence.
- New-pattern section is the headline — restating known rules as discoveries is the fail mode.
- Execution prompt: shares `references/prompts-v2/judgment-encode.md` (same contract; harness-native deploy)

## Quality Gate

genius.md rubric: standard provenance, purpose specificity. Anti-patterns: blending authors, re-encoding canon as new, evaluators that block instead of nudge (Compass Doctrine binds), skipping registration.
