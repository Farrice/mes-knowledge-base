---
description: Biweekly zeitgeist ear-to-the-floor — delta-research each platform's narrative temperature, propose card patches, surface trends scoped to Farrice's lanes
---

# /platform-pulse — Biweekly Platform Narrative Pulse

Runs as a scheduled cloud routine (1st + 15th monthly) AND on demand via `/platform-pulse`. One job: keep `_active/farrice-brand/voice/PLATFORM-NARRATIVE-CARD.md` true without Farrice having to chase platform meta himself.

## The Five Design Rules (why this isn't a generic trend report)

1. **Delta over dump.** Read the current PLATFORM-NARRATIVE-CARD first. The report covers MOVEMENTS only — what shifted, what's newly winning, what died — never a re-statement of stable rows. A pulse with no movement says so in one line per platform (that's a good outcome, not a thin one).
2. **Propose-only card patches.** The pulse NEVER edits the card. It ends with proposed row edits (exact old → new cell text, one line of receipt-backed reasoning each). Farrice ratifies with a word; felt verdicts stay sovereign over metrics (binding: auto-evolution ≠ ground truth).
3. **Own-floor triangulation.** External trend claims get checked against Farrice's own floor: `_active/farrice-brand/voice/calibration-log.md` (voice-ratchet verdicts) + anything new in `deliverables/linkedin/` since the last pulse. Where his shipped results contradict the external read, HIS floor wins and the conflict is surfaced explicitly.
4. **Scoped to his lanes.** Wellness/fitness brand founders + invisible-expert practitioners (Millennial buyers). Generic-creator virality only matters where it changes HIS dials. Trend candidates get a RIDE / SKIP flag filtered through the anti-guru lens and the Practitioner Test (would he actually do this format?).
5. **Receipts or it didn't happen.** Every claim labeled VERIFIED / LIKELY / UNCONFIRMED with named source + URL + date. Thin evidence flagged plainly. No ghost citations, no training-memory answers. Engagement multiples are directional compass, never quotable fact.

## Run Protocol

1. Read (from repo): `_active/farrice-brand/voice/PLATFORM-NARRATIVE-CARD.md` · the most recent report in `research_outputs/platform-pulse/` (if any; first fallback: `research_outputs/2026-07-16-platform-narrative-temperature.md`) · `_active/farrice-brand/voice/calibration-log.md` · file list of `deliverables/linkedin/` newer than the last pulse.
2. Research the delta window (last ~2 weeks) per platform: LinkedIn, IG Reels/feed, TikTok, YT Shorts, YT long-form, X, Substack (newsletter + Notes), Threads. Per platform answer: any movement on the three dials (POV-mode / arc appetite / polish)? What formats are newly winning or dying? Anything specific to wellness/fitness or expert-practitioner content?
3. Check the card's standing ⚑ gut-check flags (X narrative-penalty, Threads B2B fit) for new evidence either way.
4. Write the report to `research_outputs/platform-pulse/YYYY-MM-DD-pulse.md`:
   - **Movement summary** (top — 5 lines max, only what changed)
   - **Per-platform delta** (movement / no-movement + receipts + confidence)
   - **Trend candidates** (RIDE / SKIP flags with one-line reasoning against his lens)
   - **Own-floor check** (his shipped results vs the external read; conflicts surfaced)
   - **Proposed card patches** (exact old → new; or "no patches proposed")
   - **Source inventory** (all receipts; note any tool/quota gaps honestly)
   ≤1,800 words. Density over completeness.
5. Commit the report to main with message `chore(pulse): platform narrative pulse YYYY-MM-DD — <movement one-liner>` and push. Never edit the card, the voice card, or any workflow — report + proposals only.
6. **Drive library export**: create a Google Doc of the report via the Google Drive MCP `create_file` — title `Platform Pulse — YYYY-MM-DD`, parentId `1ojcfIQpS_Cecs_C0nRLV3fi0yHgOzFB8` ("Platform Pulse Library" folder, https://drive.google.com/drive/folders/1ojcfIQpS_Cecs_C0nRLV3fi0yHgOzFB8), contentMimeType `text/markdown`, textContent = the full report. Phone-readable library; repo copy stays canonical. Drive tool unavailable → note it and continue, never block.
7. In-session runs additionally: surface the movement summary inline and offer the ratification prompt ("apply patches 1,3" → conductor edits the card + bumps its version).

## Failure honesty

If search tooling is degraded or a platform's evidence is thin, the report says exactly that per platform — a labeled gap beats a confident guess. Zero-survivor guard: if NO platform section could be researched, the report is NOT written; fail loudly instead (no phantom deliverable).
