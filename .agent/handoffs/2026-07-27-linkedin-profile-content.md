---
thread: linkedin-profile-content
status: ready
resume_hint: Propose 3 teardown brands, pick one, DM it before publishing
unfinished: Nothing sent yet; teardown brand unpicked; client count still rounded; no calendar path wired
branch: main
pin: true
---

# Farrice Brand — LinkedIn Profile Rewrite v2 (Proof-to-Market Positioning + Voice Card 1.1)

## Purpose

- **Next session should do:** Teardown #1 on a named supplement/performance brand, DM'd to the brand before publishing, then the first 3 LinkedIn posts. Register reference is About v9.
- **Not in scope:** more profile drafts (nine exist, the copy is done and gated), pricing decisions (frozen until three real conversations price-test them), any new offer definition.

## Load First

- `_active/linkedin/03-launch/2026-07-27-profile-and-content-package.md` — all final copy. **§3 About v9 is the register reference**; §0 holds the Wide→Deep→Bridge→Home architecture that governs every downstream piece.
- `_active/farrice-brand/voice/VOICE-CARD.md` v1.1 — §4 "The Spine Choice" (confession-I vs recognition-you vs banned dictation-you) and §6 "The imperfection principle."
- `_active/farrice-brand/thought-bank/inbox/2026-07-27.md` — Farrice's raw supplement lived-experience, verbatim. Use his words, not better-written versions of them.
- `.agent/missions/teardown-first-sends/portable.md` — the paste-ready prompt for the fresh session.

## Current State

- **Objective:** convert a finished positioning surface into a first buyer contact. Path A / Proof-to-Market.
- **What is already done:**
  - Profile copy final: headline (3 treatments), About v9 (2,600/2,600, `prose_classifier` CLEAN 0/10), Experience, Featured plan, Ward device ledger.
  - Offer restructured from 2 tiers to 3 — free teardown → sprint → **retainer**. The retainer is the structural change that keeps Farrice in the strategist chair instead of production (Dara Pattern 21: own the outcome, deliverables are evidence not product). Explicit boundary line in-copy: "I don't build the ads, run the account, or write your calendar."
  - Biography corrected: **3 years at a vitamin shop counter** (the only setting where "put it back on the shelf" is literal) + 18 years training where supplement questions came via nutrition plans, program design, and gym-floor conversations. Prior drafts fabricated a "bottle from a gym bag mid-session" scene.
  - Two content pieces drafted and gated: "Cards Face Up" LinkedIn post, and "Why the Better Product Loses" long-form article (Bayer Mirror). Both in §4/§5 of the package.
  - VOICE-CARD compiled 1.0 → 1.1; 7 pending verdicts folded to 0. Resolved a live contradiction: dictation-you (banned) vs recognition-you (PASS 10/10) share a pronoun and nothing else.
- **What is uncertain or stale:**
  - Real client count still rounded ("1,000+") — only Farrice can supply it.
  - VOICE-CARD §3 stylometrics claim em-dashes trend 2–4 per piece pre-polish; three new corpus pieces ran zero without effort. One more sample and §3 earns a rewrite.
  - No teardown brand selected. No custom button / calendar wired — DM is still the only conversion path.
- **Latest proof/receipt:** `prose_classifier.py check` CLEAN 0/10 on About v9, the post, and the article. `voice_ratchet.py status` → v1.1, 22 entries, 0 pending.

## Suggested Skills / Workflows

- `/resume linkedin-profile-content` — pulls this pinned thread with status and what's unfinished.
- `/pt-profile-funnel` — only when traffic exists; wires the two conversion paths (high-intent → calendar, curious → Featured).
- `/voice-audit` — pressure-test whether card v1.1 catches what v1.0 missed.
- `/offer-redteam` + `offer_gate.py check` — for the new retainer tier, **after** a buyer has seen it, not before.

## Exact Next Prompt

```text
Read .agent/missions/teardown-first-sends/portable.md and follow it. Start by proposing 3 candidate brands for teardown #1 with a one-line reason each, then wait for me to pick.
```

## Acceptance Criteria

- A teardown published on a named brand, and a DM sent to someone at that brand before publication.
- The send logged by Farrice via `revenue_tracker.py` — a draft on disk does not count.
- Three LinkedIn posts drafted in the About v9 register, each passing `prose_classifier.py check`.

## Risk Notes

- **The dominant risk is build-instead-of-send.** Four offer definitions in 26 days, $0 collected, zero sends. Everything produced this session is an asset. Send-before-build is binding and still unmet.
- **Anchoring, not context bloat, degraded this session.** Nine near-identical drafts in one thread pulled every new attempt toward the previous one; three explicit factual corrections from Farrice were needed to break patterns. Start fresh, seed narrow.
- No prices may be published anywhere (frozen 2026-07-25 until three conversations price-test them).
- `raw_intent_run_packet.py` returned a packet about its own machinery instead of the LinkedIn work — the portable handoff at `.agent/missions/teardown-first-sends/portable.md` is hand-authored, not generated. Do not trust that generator's output unchecked.
- Claude Code and Codex must not run against this working tree simultaneously.
