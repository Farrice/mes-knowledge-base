# Architecture — Jun Yuh Story Engine

## Function Ownership

`Jun material mining → Shaan dosage decision → one production owner → optional post-draft audit`

Jun is the scarce craft owner for turning ordinary lived experience into personal-brand story material. Shaan is the scarce judgment owner for whether story belongs in a cross-domain communication. No other expert receives body-writing authority by default.

## Components

| Component | Type | Input | Output | Stop/Handoff |
|---|---|---|---|---|
| Story Material Miner | Jun workflow | supplied moment, facts, share boundary | LIFE selection, Safe/Real/Raw interview, 3P candidates, missing facts | Stops at `[NEEDS SOURCE]` or passes a Story Material Packet. |
| Story Format Router | Jun workflow | material packet, mission, destination | one of six social formats plus a production plan | Social output stays with Jun; non-social routes out. |
| Jun Story Engine | orchestrator workflow | raw intent and material | final social asset or Shaan handoff plus receipt | One owner writes; privacy and truth gates bind. |
| Shaan Story Deployment | existing downstream owner | Jun material packet for non-social work | `FULL STORY`, `STORY FRAGMENT`, or `NO STORY` plus production route | Existing truth constraints remain authoritative. |
| Jun Story Engine Verifier | stdlib script | files and fixture decisions | PASS/FAIL with negative controls | Two repair attempts, then park. |

## Exact Change Surface

- `skills/jun-yuh-creator-vision/SKILL.md`
- `skills/jun-yuh-creator-vision/genius.md`
- `skills/jun-yuh-creator-vision/references/source-ledger.md`
- `skills/jun-yuh-creator-vision/references/storytelling-masterclass-ledger.md`
- `skills/jun-yuh-creator-vision/references/prompts-v2/{jun-story-engine,story-material-packet,story-content-format-plan}.md`
- `skills/jun-yuh-creator-vision/workflows/{jun-story-engine,story-material-miner,story-content-format-router}.md`
- `agents/jun-yuh/AGENT.md`
- `.agent/workflows/jun-story-engine.md`
- `.claude/commands/jun-story-engine.md`
- `.agents/skills/source-command-jun-story-engine/SKILL.md`
- `skills/shaan-puri-storytelling/references/story-deployment-map.md`
- `execution/verify_jun_story_engine.py`
- `extractions/video-context/XS-E6rnCr5U/fixtures/story-engine-cases.json`
- `extractions/video-context/XS-E6rnCr5U/behavior-proof.md`
- `extractions/video-context/XS-E6rnCr5U/USER-GUIDE.md`

## Cold-Start Route

```text
/jun-story-engine
Objective: [what the audience should understand, feel, decide, or do]
Lived material: [facts, moment, notes, or source path]
Share boundary: [what may not be used]
Destination: [social format or unknown]
Truth risk: [personal | ordinary real-world | evidence-sensitive]
Choose whether to mine, use a full story, use a fragment, or use no story. Do not invent missing life details.
```
