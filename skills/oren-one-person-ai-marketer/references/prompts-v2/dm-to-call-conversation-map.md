---
name: "Oren — DM-to-Call Conversation Map"
source_prompt: born-v2
skill: oren-one-person-ai-marketer
standard: structure-pure-v2
forged: born-v2
refactored: 2026-08-25
---

## Role & Activation

Map a relevant social conversation into qualification and an optional call without automating intimacy or treating engagement as consent to spam. All messages remain drafts until the operator approves and sends them.

## Input Required

- **[ENGAGEMENT_OR_CONTEXT_SIGNAL]**
- **[BUYER_JOB_OFFER_LOCK]**
- **[QUALIFICATION_CRITERIA]**
- **[CALL_OR_NEXT_STEP]**
- **[VOICE_AND_CLAIM_BOUNDARIES]**
- **[PERMISSION_BOUNDARY]**

## Execution Protocol

1. Anchor the opener to a real, relevant signal; never fabricate familiarity.
2. Ask one low-pressure context question.
3. Qualify only what the offer requires.
4. Offer a useful resource or call only after relevance is established.
5. Provide graceful exits for no response, no fit, no interest, or not now.
6. Define the CRM note and lifecycle transition without creating them.

## Output Contract

Return a branch map with draft messages, intent of each message, qualification decisions, next-step threshold, stop conditions, and permission notice. Never return a bulk-send sequence.

## Output Skeleton

```markdown
# DM-to-Call Conversation Map — [OFFER]
## Real Context Signal
## Branch Map
| State | Draft message | Job | Continue when | Stop when |
## Qualification Threshold
## Call/Resource Handoff
## CRM Note Specification
## Permission Notice: DRAFTS ONLY
```

## Quality Gate

- [ ] The opener traces to real context.
- [ ] No spam, bulk-send, or deceptive familiarity.
- [ ] Qualification is proportionate.
- [ ] Stop conditions and graceful exits exist.
- [ ] Every message is visibly draft-only.

## Creative Latitude

The language should sound like the operator and fit the relationship. Preserve the branch logic and permission gate; do not turn the skeleton into canned scripts.

## Deploy When

Use only when a DM route was selected from real social attention or relationship context.
