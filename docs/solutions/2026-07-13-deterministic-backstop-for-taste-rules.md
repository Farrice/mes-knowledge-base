---
name: deterministic-backstop-for-taste-rules
problem_signature: "Taste/style rules stored as memory-or-doc-only kept shipping violations — three posts passed CLEAN while carrying the exact banned tells"
domain: system
tags: [prose-classifier, ai-slop, enforcement, deterministic-backstop, taste-rules]
date: 2026-07-13
status: active
session: "085d3918-6379-4389-8d36-a939854e85e6"
---

## Problem

AI-slop tells and em-dash caps were documented in the ban bank and in memory, yet three posts shipped as CLEAN while carrying the exact banned tells. Enforcement depended entirely on the model remembering the rules at generation time, and it didn't.

## Root Cause

A rule bank that lives only in docs or memory is advisory. The model can load it, agree with it, and still emit the banned pattern — nothing physical stands between the violation and delivery. The existing `prose_classifier.py` detector lagged the ban bank: new tells (reveal lead-ins, contrast-reveal antithesis, question-closes, LinkedIn tropes) had entries in the doc but no matching signal in the code.

## Approach That Worked

1. Paired the rule bank with a deterministic detector: extended `execution/prose_classifier.py` with ~16 signal tiers — reveal lead-ins, contrast-reveal antithesis, mascot reveals, em-dash counter, question-close, LinkedIn tropes, and structural movers (anaphora, gerund openers, mic-drop closers).
2. Calibrated precision-over-recall so clean human prose never flags: stopword-filtered the anaphora detector, narrowed the stakes-phrase list.
3. Regression-tested against 4 approved posts (must stay CLEAN) plus tell-stuffed samples (must flag). Both suites pass.

## Dead Ends

- Writing the ban doc and stopping — the doc is advisory; violations shipped anyway.
- Recall-heavy detector tuning — early broad patterns flagged approved human prose, which would train operators to ignore the gate. False positives kill a taste gate faster than false negatives.

## Verification

Regression suite: 4 previously approved posts run through the extended classifier return CLEAN; tell-stuffed samples flag on the expected tiers. The three originally missed posts now flag on their exact banned tells.

## Weaker-Model Trap

Writing the ban doc and stopping. The doc is advisory; the regex is physical. Every taste rule added to `directives/ai-slop-ban-bank.md` needs a matching signal in `prose_classifier.py` or it will ship violations the moment the model forgets.

## Pointers

- `directives/ai-slop-ban-bank.md` — canonical ban bank (64 entries)
- `execution/prose_classifier.py` — the deterministic detector, ~16 signal tiers
- Memory: `feedback_ai-slop-ban-bank.md` — the always-on rule pointing at both
