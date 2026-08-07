---
name: david-perell-placeful-voice-audit
produces: evidence-safe Placefulness Audit with heatmap, edits, and repair route
expert: David Perell
load_context: genius.md
routing: long-tail
when_to_use: Competent prose feels interchangeable and needs a truthful person-or-place diagnosis.
---

# Placeful Voice Audit

## Pre-Flight Gate

Read `genius.md` and `references/exemplars-QsHm_0MEhX8.md`. Require a draft or a specific evidence-boundary question, plus supplied lived details and permission boundaries. Audience, format, and protected lines are required before a deeper repair handoff, but their absence does not block a bounded evidence audit or supported micro-edit; mark them `NOT SUPPLIED` and do not infer them. A voice sample is optional; without it mark `VOICE MATCH UNAVAILABLE`. Classify each detail `AUTHORIZED FOR USE`, `PRIVATE CONTEXT ONLY`, `NO PERMISSION`, or `UNCONFIRMED`. This workflow audits and makes evidence-safe micro-edits; it does not invent or perform a full literary rewrite.

## Input Required

1. Draft.
2. Optional writer-owned voice sample.
3. Supplied lived details and authorized place or biography facts.
4. Permission and privacy classification for each detail.
5. Audience, format, and protected lines — required for deeper repair; optional for a bounded evidence audit.

## Procedure

### 1. Create the Evidence Boundary

Index every supplied detail, source, permission state, and allowed use. Keep private or forbidden material outside downstream prompts.

### 2. Run the Could-Be-Anywhere Test

Mark passages that erase source, place, maker presence, observation, or human choice. Functional plainness is not automatically a defect.

### 3. Build the Heatmap

Rate each passage 0–3 for generic setting, template phrase, abstract emotion, missing maker, generic sensory language, or observable voice mismatch.

### 4. Compare Voice Evidence

When a sample exists, compare syntax, rhythm, vocabulary, stance, detail type, and self-insertion. Cite the sample; do not manufacture a voice profile.

### 5. Make Evidence-Safe Edits

Edit only when an authorized detail directly supports the change. Every added concrete detail cites its detail ID. Otherwise return an exact evidence request.

### 6. Route Deeper Repair

Ocean Vuong or `high-taste-writing-os` owns perceptual or literary line repair. `how-i-write-os` owns multi-expert composition. Platform formatting occurs only after repair.

## Output Schema

```text
## Placefulness Audit
Verdict: PLACEFUL | SALVAGEABLE | PLACELESS | INSUFFICIENT EVIDENCE
Voice state: MATCHED | PARTIAL | VOICE MATCH UNAVAILABLE

## Evidence and Permission Boundary
| Detail ID | Detail | Source | Permission | Allowed use |

## Placelessness Heatmap
| Locator | Severity 0-3 | Failure type | Exact evidence | Repair state |

## Template Residue
| Locator | Phrase or pattern | Why interchangeable | Safe action |

## Observable Voice Fingerprint
| Feature | Evidence from supplied sample | Draft alignment |

## Evidence-Safe Edits
| Locator | Before | After | Detail ID used | Why safe |

## Missing-Evidence Requests
| Passage | Exact question | Why needed | Blocking? |

## Repair Route
- Owner:
- Mode:
- Artifact supplied:
- Invention veto:
```

## Quality Gate

- [ ] No street, location, memory, emotion, sensory fact, dialogue, date, or biography was invented.
- [ ] Every added concrete detail cites an authorized detail ID.
- [ ] `NO PERMISSION` and private details appear in no edit or handoff.
- [ ] Sparse truth outranks vivid fabrication.
- [ ] Audit and micro-edit boundaries remain distinct from deep rewriting.
- [ ] The workflow diagnoses placefulness without imitating David Perell or another writer.

Execution prompt: references/prompts-v2/david-perell-placeful-voice-audit.md — honor its Output Contract.
