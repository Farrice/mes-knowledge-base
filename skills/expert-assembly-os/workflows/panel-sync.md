---
description: Reload a pinned expert panel and reconvene for follow-up deliberation
---

# /panel-sync — Reload & Reconvene

Reload a previously pinned expert panel from a `/assemble` session and reconvene the same voices for follow-up deliberation, refinement, or a new angle on the same task.

This is your "I want the same panel back" command. No re-synthesis. Same roster + bespoke personas. New deliberation.

## Usage
```
/panel-sync "Now let's refine the offer architecture piece"
/panel-sync --session "competitive-sailing-rigging-optimization" "What about durability tradeoffs?"
```

## How to run it

This command reloads and reconvenes the pinned panel. Execute it by:
1. Reading the pinned session from `.agent/handoffs/assemble-<slug>.md` (auto-discovered from recent sessions or specified via `--session`).
2. Loading panel metadata + synthesized personas from `.tmp/assemble/<slug>/`.
3. Reconvening for new deliberation on your follow-up query.

Optional args:
- `session`: slug of a prior `/assemble` session (auto-discovered if omitted; picks the most recent).
- `task`: the follow-up task or refinement question.

## What it does

1. **Reload** — fetch the pinned panel metadata + all synthesized personas from the prior `/assemble` session.
2. **Status** — display panel composition (roster + bespoke members), domains covered, and net-new principle from the original deliberation.
3. **Diverge (refinement)** — all panelists give takes on the follow-up question, reusing their original methodology + voice.
4. **Deliberate** — 1 round of cross-talk on the refinement; contradictions preserved.
5. **Converge** — updated crux + next moves for the refinement.
6. **Learn** — brief digest: how the panel adapted their thinking + what shifted.

## When to use

- **Follow-up refinement** after `/assemble`: "Now let's stress-test the positioning against objections."
- **New angle, same domain**: "How would this shift if we target a different ICP?"
- **Multi-turn deliberation**: "Pause, pivot, continue with the same voices."

## When NOT to use

- **New task, different domains** → use `/assemble` (fresh panel cast).
- **Single-expert follow-up** → invoke that expert directly.
- **Panel composition shift** → `/assemble` for a new cast.

## Output Location

Follow-up deliberation is appended to the session record in `.agent/handoffs/assemble-<slug>.md`. Personas remain in `.tmp/assemble/<slug>/` (unchanged).

## Output Requirements

Unlike `/assemble`, this workflow does NOT re-emit a full roadmap — it appends a **Refinement Note** to the existing session record:

1.  **Panel Status Recap**: which panelists reloaded (name + `[Roster]`/`[Bespoke Composite]` label, unchanged from original session), confirming zero re-cast happened.
2.  **Refinement Takes**: each panelist's response to the follow-up question, written in their original voice/methodology — no persona drift, no re-synthesis.
3.  **Updated Crux**: how the central tension shifted (or didn't) given the new angle — one paragraph, not a restatement of the original.
4.  **Updated Next Moves**: only the roadmap items that change as a result of this refinement — never a full roadmap reprint of unaffected sections.
5.  **Learn Digest**: what shifted in the panel's thinking between the original session and this refinement, in 3–5 sentences.

If the follow-up question turns out to require a domain the original panel doesn't cover, this workflow stops and hands off to `/assemble` for a fresh cast — it never silently stretches an existing panelist outside their seated domain.

## Quality Gate

1.  **The No-Respawn Test**: Did every panelist reload from the pinned session with their original persona intact — zero re-synthesis, zero new `persona_stat_lint.py` calls needed?
2.  **The Continuity Test**: Do the refinement takes use each panelist's original methodology and voice, not a generic restatement?
3.  **The Scope-Fit Test**: Is the follow-up question actually inside the domains this panel was cast for — and if not, did the workflow hand off to `/assemble` instead of forcing a mismatched panelist to answer?
4.  **The Delta Test**: Does the Updated Next Moves section contain only what changed, not a full reprint of the original roadmap?
5.  **The Appended-Not-Replaced Test**: Was the refinement appended to `assemble-<slug>.md`, preserving the original session record rather than overwriting it?

> **🛡️ Anti-Pattern Check**: Before delivering, review the output against the **Anti-Patterns (Sourced)** section in `genius.md` — especially unlabeled panel composition and vague roadmap moves, both of which can creep back in during a refinement pass. Flag and fix before delivery.

---

See also:
- **Original assembly**: `/assemble`
- **Skill home**: `skills/expert-assembly-os/SKILL.md`
