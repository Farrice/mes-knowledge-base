---
description: Capture one felt verdict (praise or wince) on a line, verbatim, the moment Farrice reacts to it
tier: atom
---

# /voice-ratchet — Calibration Capture

The physical write path for Voice OS's felt-verdict loop. Same law as thought-bank capture: a reaction not logged in-session is a reaction the system never learns from — never defer this to "I'll remember later."

## Usage

```
/voice-ratchet --verdict pass|fail --line "..." --why "..." [--source "..."]
```

Or trigger silently: any time Farrice reacts to a specific line — praise ("that's it," "yes," "that lands") or wince ("no," "not this," visible discomfort, a rewrite request) — during ANY session, not just voice-focused ones.

## Steps

### 1. Capture the exact inputs
- **Line**: the verbatim line, not a paraphrase. Copy it exactly as written.
- **Verdict**: `pass` or `fail` — his reaction, not your judgment of the line's quality.
- **Why**: one sentence on what made it land or fail. Specific to this line, not a generic voice-rule restatement.
- **Source**: what piece it came from (edition name, LinkedIn draft, DM, date) — optional but strengthens the calibration bank's traceability.

### 2. Write it
// turbo
Run:
```bash
python3 execution/voice_ratchet.py add --verdict <pass|fail> --line "<verbatim line>" --why "<why>" --source "<source>"
```

The script dedupes on exact line text — if it reports "Already logged," don't re-run with variations to force a new entry.

### 3. Confirm
Report the script's confirmation output (total count, PASS/FAIL split, pending-since-last-compile) in one line. No further action needed unless pending crosses 5 — then mention `/voice-compile` is due.

## Note on Silent Capture

Agents operating under Voice OS should run this workflow silently whenever Farrice gives line-level feedback in any session — content review, casual reaction to a draft, editing a piece together. This mirrors the thought-bank capture pattern: the capture is the agent's responsibility, not something Farrice has to remember to ask for.

## Chain Compatibility

- **Feeds**: `_active/farrice-brand/voice/calibration-log.md` (raw append log) → `/voice-compile` (folds into VOICE-CARD.md §6)
- **Follows**: any content review, `/voice-os apply`, `/voice-audit`, or ordinary conversation where a reaction happens
- **Leads to**: `/voice-compile` once 5+ entries are pending
