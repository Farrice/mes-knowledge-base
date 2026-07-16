# /gw-voice-persona

A writing-persona style guide in markdown, built by Woods' exact recipe (20-50 samples → communications-expert role → interview → markdown voice file), then reconciled against this workspace's Voice OS. Serves refresh / expand / new-client personas — it does NOT replace Voice OS.

## Trigger
`/gw-voice-persona`

## Workflow
`skills/geoff-woods-ai-thought-partner/workflows/12-voice-persona.md`

## Quick Use
Provide:
1. Whose voice — Farrice (refresh/expand only) or a new subject (client / guest / sub-brand)
2. 20-50 raw writing samples (emails, posts, drafts, DMs — mess is fine, volume beats polish)
3. The purpose — refresh, expand a channel/register, or build a net-new persona
4. For Farrice's own voice: confirm `VOICE-CARD.md` is loaded (output reconciles into it, never over it)

## Output
Route + Voice OS boundary → corpus fingerprint read → interview (≤5 questions, one at a time) → the markdown voice file (with anti-tell guardrails + the 10-20% leak warning) → reconciliation (standalone for a new persona; propose-only diff against `VOICE-CARD.md` for Farrice).

## Stacks With
→ `/voice-os` + `_active/farrice-brand/voice/VOICE-CARD.md` (the canonical authority for Farrice's voice — this workflow serves it, reconciles into it, never replaces it)
→ `/voice-ratchet` (accept a proposed diff into the card via the calibration loop)
→ `/gw-crit` (the Context-Role-Interview-Task engine the recipe runs on)
→ `/gw-jam-fusion` (build a per-client persona here, then jam inside it)
