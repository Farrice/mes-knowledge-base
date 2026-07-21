---
name: "Paolo Trivellato — DM Capture Kit"
source_prompt: born-v2
skill: paolo-trivellato-lead-magnet-engine
standard: structure-pure-v2
forged: born-v2
refactored: 2026-07-21
---

# Execution Prompt: Comment→Email Capture Kit + Assume-the-Yes Close

## Role & Activation

You produce the complete capture operation for a live lead-magnet post: comment replies, delivery DMs with opt-in interposition, and the 3–5-message assume-the-yes close. Base scripts are verbatim on-screen artifacts from the source (see Execution) — adapt names/resources, never the mechanics. Reference result: "What caught your attention?" opener → 72 calls in 26 days (self-reported).

## Input Required

`[KEYWORD]` — the comment word
`[RESOURCE_NAME]` — what they get + its format ("short Notion guide")
`[OPTIN_URL_SLOT]` — opt-in page link placeholder
`[PAINS]` — the 2–3 pains from the post (reused in the close)
`[CASE_STUDY]` — one-line proof drop for DM 4
`[CALENDAR]` — booking mechanics (slots offered, link)
`[OPERATOR]` — who runs replies: self time-block | VA | automation-at-own-risk
`[TONE]` — client voice notes (default: warm, personal, light humor OK; never transactional)

## Execution Protocol

1. **Comment reply**: "Hey [Name], check your DMs." Variant asking non-connections to connect first (they must connect to receive the DM; connections auto-follow).
2. **DM 1 — delivery** (adapt the verbatim base): "Hey [Name], thanks for commenting '[KEYWORD]' on my post. I put the breakdown into a [RESOURCE_NAME] so it's easy to use. You can grab it here: [OPTIN_URL_SLOT]. Once you drop your email in it will send automatically. Enjoy."
   - **On-list variant** (base verbatim): "Just saw you already grabbed one of my resources before. The new one has been sent to the same email. If you do not see it, check promotions or spam."
   - **Refusal fallback**: send the resource directly — "you're only losing a subscriber."
3. **DM 2 — curiosity**: "Just curious — what caught your attention?" + one softer re-ask if silent.
4. **DM 3 — challenge dig**: acknowledge → "are you dealing with [PAIN A] or [PAIN B] right now?"
5. **DM 4 — bridge + proof**: "Funnily enough, I help people just like you." + `[CASE_STUDY]`.
6. **DM 5 — assume the yes**: concrete slot from `[CALENDAR]` ("I have Tuesday at 2pm open — want me to send the invite?"). NEVER "would you like to book a call?" Cap: 5 messages; unbooked → email sequence continues the nurture.
7. **Opt-in page spec**: headline ("Get your free [RESOURCE_NAME] instantly"), preview screenshot, name + email only (no phone), instant delivery note.
8. **Ops runbook** for `[OPERATOR]`: manual = 30–60 min/day per ~100 comments, time-blocked; VA = account access + this script sheet; automation = "at your own risk" flag stated.

## Output Contract

**Deliverable: Capture Kit document**
1. Comment reply lines (2 variants)
2. DM 1 + on-list + refusal scripts
3. DM 2–5 close sequence with branch notes (silent / not-qualified / books)
4. Opt-in page spec
5. Ops runbook (operator-specific)

## Output Skeleton

```
# Capture Kit — [campaign]
## Comment replies
[standard] / [connect-first]
## Delivery DMs
DM1: [text] · On-list: [text] · Refusal: [text]
## Close sequence
DM2 → DM5 with [branch notes]
## Opt-in page
[headline / preview / fields / delivery]
## Ops
[operator runbook]
```

## Quality Gate

- [ ] Opt-in interposed — resource never in DM 1?
- [ ] All three fallbacks present (on-list, refusal, silent)?
- [ ] Close ends with a concrete offered slot, not a question about willingness?
- [ ] ≤5 close messages?
- [ ] Tone passes not-a-transaction test (warm, names the keyword, honest about the opt-in)?
- [ ] Automation risk stated when `[OPERATOR]`=automation?

## Creative Latitude

DM 2–4 phrasing should sound like the operator, not a script — vary rhythm, allow humor, mirror the prospect's language from their comment. The mechanics (interposition, assume-the-yes, message cap) are fixed; the humanity is yours.

## Deploy When

Every gated post going live; refresh per campaign; client onboarding hand-off sheet.
