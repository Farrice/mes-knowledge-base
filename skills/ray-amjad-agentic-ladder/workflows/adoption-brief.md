---
description: Client/org-facing AI-adoption ladder brief — where they are, the next unlock, ROI framing; consulting deliverable form
---

# Adoption Brief — The Ladder as a Client Instrument

Tier-3 stacking workflow: packages a ladder diagnosis + one-rung climb plan as a client-facing brief. The commercial frame is Boris's own: "one person is 10x'ing their output with Claude but the rest of the org hasn't caught up." Stacks with `geoff-woods-ai-thought-partner` (operator coaching) and consulting offers (Proof-to-Market pattern: diagnostic as door-opener, implementation as the paid engagement).

## Pre-Flight Gate

Load `genius.md` + `references/boris-ladder-source.md`. Require a real diagnosis (run `ladder-diagnostic` / `system-ladder-audit` on actual client facts first — never draft a brief from assumptions). Client-facing = implementation-grade ALWAYS: depth stays in, ≤2 pages.

## Skill Acquisition

- `references/boris-ladder-source.md` — unlock column (the ROI language), bottlenecks, L0 gating list for enterprise
- `genius.md` — Ladder honesty moves; the 90%-teach-level-1 market context

## Execution

1. **Open with their gap**: perceived vs actual level, in their own operational facts (which setups, what happens after "done"). One paragraph, no jargon.
2. **Show the ladder** (5 rows, compressed) with THEIR position marked and the 10x-individual-vs-org observation where an internal champion exists.
3. **Name the unlock in business terms**: quote the level's unlock line and translate to their backlog ("the [X] that takes your team weeks becomes one afternoon of orchestration").
4. **One-rung plan**: 3 phases from `level-up-plan` (build mechanism → manual trust runs → widen autonomy) with the trust exit-test as the milestone. Never promise two rungs.
5. **Expected pain, stated up front** (honesty move): the next level's bottleneck from the source table — sets expectations and positions you as the guide who's seen it.
6. **L0 orgs**: lead with the gating checklist (SSO/SCIM, budget caps, data governance, exec alignment) — the 0→1 transition IS the engagement.

## Content Type Adaptations

| Audience | Adaptation |
|---|---|
| Non-technical founder | Levels as staffing metaphors (pair programmer → orchestrator → manager of managers → VP); artifacts as "receipts" |
| Engineering leader | Keep tooling specifics; annex the `system-ladder-audit` table |
| Enterprise/gated org | L0 checklist first; security framing before capability framing |
| Workshop/content use | Ladder + two-test challenge as the interactive segment |

## Output Requirements

≤2-page brief: gap paragraph · marked ladder · unlock-in-their-terms · one-rung plan with trust milestone · expected-pain note · next-step CTA. Production-sheet formatting (labeled sections, no prose blobs).
Execution prompt: `references/prompts-v2/adoption-brief.md` — honor its Output Contract.

## Quality Gate

Reject if: brief precedes a real diagnosis; two rungs promised; unlock not translated to their backlog; expected pain omitted (over-selling); >2 pages; template/AI-slop phrasing (run prose check).
