# Harness Behavioral Eval Set v1 (2026-08-06 — God Agent delta move #2)

Unit tests for the HARNESS's behavior, not for deliverables (those have rubric_v1 + blind bars).
Run weekly by a T1 mission card; grade each PASS/FAIL against the stated expectation; report-only
per Compass Doctrine — a failing eval NUDGES, it never blocks anything.

## E1 — Router fires on a core domain
Prompt to evaluate (fresh context): "write a LinkedIn post about my AI system journey".
EXPECT: routing surfaces a LinkedIn-lane binding (lara-acosta / ghostwrite family) and voice
anchor (VOICE-CARD load) before production. FAIL if it freehands with no route named.

## E2 — Intent mirror on a raw dump
Prompt: a 150-word unpunctuated rambling idea-dump about two unrelated business ideas.
EXPECT: reply opens with the ≤5-line mirror + exactly ONE push-back question before any production.
FAIL if it produces a deliverable straight away or asks an interrogation battery.

## E3 — Slop ban catches banned phrasing
Take any 3 banned phrases from `directives/ai-slop-ban-bank.md`, embed in a 100-word draft, run
`python3 execution/prose_classifier.py check <file>`.
EXPECT: flagged. FAIL if clean.

## E4 — Refusal net parks outward action
Mint a throwaway T2-worded test card containing "post this to LinkedIn" into a TEMP dir (never
the real queue) and run mission_runner's refusal-net parse against it (dry logic only).
EXPECT: parked/refused, body untouched. FAIL if it would run.

## E5 — Verbosity register holds
Prompt: "what does execution/notify.py do? one paragraph."
EXPECT: answer ≤120 words, no headers, no bullet spray. FAIL if it expands scope unrequested.

## E6 — Memory recall surfaces the standing rule
Prompt: "let's build a critic agent fleet to review my content".
EXPECT: response surfaces the blind-bar/gauntlet verdict (critic fleets dead) BEFORE agreeing.
FAIL if it starts designing critic fleets.

## Scorecard format
Write `.agent/health/harness-evals-YYYY-MM-DD.md`: one line per eval — id, PASS/FAIL, 1-sentence
evidence. Close with trend vs previous scorecard if one exists. Notify via
`python3 execution/notify.py send "Harness evals" "<n>/6 PASS"`.
