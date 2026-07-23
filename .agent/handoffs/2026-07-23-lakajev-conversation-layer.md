---
thread: lakajev-conversation-layer
status: done
resume_hint: Deploy: /ml-closed-lost campaign in BLEND voice for Signal Pilot lane
unfinished: Deployment only — skill itself is A-tier complete; corpus refresh with 2026-era posts optional
branch: main
pin: true
---

# Matthew Lakajev — Forge Expansion v2 (Six Gates + Conversation Layer, A-Tier)

## Purpose
- **Next session should do:** Deploy the new A-tier Lakajev conversation layer for Signal Pilot send-work — run `/ml-closed-lost` to build Farrice's campaign (everyone he's ever talked to about ghostwriting/AI/audit work, scripts in BLEND voice), then `/ml-six-gates` on the Signal Pilot outreach path to find the stall gate.
- **Not in scope:** Re-extracting or rebuilding the skill (v3.0 is A-tier, extend never rebuild); new content engines; anything that builds before sending (send-before-build is binding on Signal Pilot).

## Load First
- `skills/matthew-lakajev-linkedin/SKILL.md` + `genius.md` — the A-tier spine (13 workflows, 8 v2 prompts)
- `skills/matthew-lakajev-linkedin/references/prompts-v2/closed-lost-campaign-build.md` — Output Contract for the first deliverable
- `_active/farrice-brand/voice/VOICE-CARD.md` + `skills/voice-os/SKILL.md` — BLEND layer (binding: anything in Farrice's voice)
- `_active/linkedin-launch/02-offer/` — Signal Pilot offer master doc ($2K exec-ghostwriting pilot; the campaign's scarcity ask must match its real capacity)
- `docs/solutions/2026-07-21-linkedin-authwall-corpus-via-public-post-permalinks.md` — if corpus refresh (2026-era posts) comes up

## Current State
- **Objective (parent session):** /extract-forge on the Agency Podcast Lakajev interview → complete.
- **What is already done:** Skill expanded 3 → 13 workflows (v3.0); Six Gates of Trust, closed-lost campaign, opinion ladder, twin targeting, daily rhythm, network ladder, influence audit, state reset, model mining, high agency. 13 `/ml-*` commands live. 5 new born-v2 prompts wired (renaissance audit 0 fail). Heartbeat gate 6/6. Finalize 8.33 PASS (Notion-logged). **A-tier confirmed 2026-07-23**: Farrice-judged blind pass EVAL-054 — he preferred the artifact-only generated post over two real Lakajev posts. All commits pushed to main (through 235073bcc).
- **What is uncertain or stale:** Reference corpus is 2023-era (both real posts from Sept/Oct 2023); Farrice accurately dated them as feeling old — refresh with 2026-era public posts when fetchable. Farrice's own contact database reality (CRM vs calendar-only) is unknown — first input the closed-lost build needs.
- **Latest proof/receipt:** `extractions/matthew-lakajev-linkedin/blind-pass-log.md` (EVAL-054 Farrice PASS) · finalize trace `trace_20260721_142944_matthew-lakajev-linkedin.json`.

## Suggested Skills / Workflows
- `/ml-closed-lost` — the first deliverable; honor `closed-lost-campaign-build.md` Output Contract; BLEND voice layer loads first
- `/ml-six-gates` — second deliverable; LENS mode on the actual Signal Pilot outreach assets, quoted-evidence verdicts
- `/voice-os` — the binding voice layer for anything shipping under Farrice's name
- `/ml-opinion-ladder` — queue behind the campaign for reply handling

## Exact Next Prompt
```text
/ml-closed-lost — build my closed-lost campaign for the Signal Pilot lane: everyone I've ever talked to about ghostwriting, AI, or audit work. Ask me the five inputs (database reality, capacity, last-touch history, voice sample) one at a time, then produce the full campaign per the prompt's Output Contract, scripts in my BLEND voice.
```

## Acceptance Criteria
- Campaign deliverable matches the v2 prompt's Output Contract: database build plan, 3 segment scripts + personalized variants, 30-day calendar, monthly cadence card
- Zero pitches anywhere; scarcity number = real Signal Pilot capacity; every script references a real prior interaction
- Voice: passes BLEND (Farrice's surface, Lakajev's mechanics) — no unicode-heavy Lakajev formatting under Farrice's name (his stated taste, 2026-07-23 blind pass)
- Six-gates audit names ONE dominant stall gate with quoted evidence and gate-ordered prescriptions

## Risk Notes
- Send-before-build is BINDING on the Signal Pilot thread — if the session drifts toward building assets before sends go out, flag and stop.
- Never pitch in any script; a single "buy now" line breaks the system's core law.
- Contact data is personal — keep names/emails in local files, out of any published artifact.
