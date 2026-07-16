---
description: "Design the personal → team → company brain ladder — the graduated three-tier architecture Kieran Flanagan names as 'the hard thing nobody has figured out': access, formality, and contribution rules per tier, plus the promote/inherit logic that navigates between them."
---

# Library Brain Ladder

A second brain is not one artifact — it is three graduated tiers. This produces the tier map + boundary rules + promotion protocol so a personal KB can grow into a team brain and a company brain without collapsing into one undifferentiated dump.

> Kieran Flanagan: "the hard thing that no one has figured out... is how do you build a system that easily helps you navigate between your personal brain, your team brain, and your company brain." This workflow is that navigation layer.

## Pre-Flight Gate
- Load `genius.md` §Two Substrates + §The Brain Ladder + §Decision Framework.
- **Sequencing law (Kieran, verbatim)**: "I would start with my personal brain, and then if you get really into this, you're going to start to figure out, 'Hey, how do I build something for my team and my company?'" → A working personal KB must exist (or ship via `/library-second-brain`) BEFORE designing team/company tiers. Refuse to architect team/company-first.
- One subject per KB still holds within each tier.

## Skill Acquisition
Read `genius.md` + `references/kb-schema.md`. For a company tier, also load `liam-mley-ai-brain-builder/genius.md` (the company brain = an AIOS Context Layer with contribution governance).

## Execution
1. **Locate the current tier**: is there a proven personal loop (dump → wiki → ingest → compounding)? If not, stop and run `/library-second-brain` first. The ladder inherits a working substrate; it does not invent one.
2. **Map the three tiers** against three variables Kieran's framing changes at each rung:
   - **Personal** — access: you only · formality: fast, Untested entries OK · contribution: dump freely, zero gating. "How it is mapped to all of the work that you do."
   - **Team** — access: your colleagues read + write · formality: shared schema enforced, dup/conflict handling required · contribution: co-authored, so identity/source per entry matters. Rationale (verbatim): "all of the things that you're capturing are as applicable to your colleague as they are to you."
   - **Company / org** — access: gated read, gated promotion · formality: curated, provenance-clean, contradiction-audited · contribution: promotion-only (nothing lands raw). Rationale (verbatim): "how companies will likely differentiate themselves... their raw intelligence of the company, the things that the company know and have figured out that no one else has is really their asset." **Frame the company brain as MOAT, not productivity.**
3. **Write the promote/inherit protocol** (the net-new object — "navigate between" made concrete): for each item, which tier owns it and what graduates upward. Default rules: personal → team when an entry is validated AND non-private AND applies to a colleague; team → company when Proven-confidence AND represents durable org knowledge (a decision-with-reasoning, a validated experiment, a differentiating capability). Private/half-baked/personal-context entries never graduate. Down-inheritance: lower tiers READ higher tiers (a colleague's personal agent reads the company brain), never write to them.
4. **Set contribution rules per tier** in that tier's CLAUDE.md / instruction page: who may dump into raw, who may trigger ingest, who approves promotions, what the confidence floor is for promotion.
5. **Wire the substrate**: file substrate = parent folder holds `personal/`, `team/`, `company/` KBs each with its own CLAUDE.md; parent CLAUDE.md holds the promotion protocol. Notion substrate = separate DBs per tier with a promotion view; use `/library-notion-port`. Company tier: hand to liam-mley — see Stacking.
6. **Prove one promotion**: take one real personal entry, run it through the promote rule, land it in the team tier with provenance intact. If nothing qualifies yet, say so honestly — an empty team brain on day one is correct.

## Content Type Adaptations
| Context | Adaptation |
|---|---|
| Solo operator (no team yet) | Build personal only; write the team/company tiers as a dormant spec so growth is pre-planned, not retrofitted |
| Small team | Personal KBs + one shared team brain; promotion approved by the owner, not committee |
| Company / org build | Company tier = liam-mley AIOS Context Layer (BRAIN.md + 8-dim Business DNA) + promotion governance; this workflow supplies the graduation rules |
| Notion substrate | Tier = DB; promotion = a status property + view; port via `/library-notion-port` |

## Output Requirements
Tier map (3 tiers × access/formality/contribution) + the promote/inherit protocol (explicit rules both directions) + per-tier contribution rules landed in each CLAUDE.md/instruction page + substrate wiring (paths or Notion DBs) + one demonstrated promotion (or an honest "nothing qualifies yet"). State which tier the user is actually at and what unlocks the next rung.

Execution prompt: references/prompts-v2/brain-ladder-architecture.md — honor its Output Contract.

## Quality Gate
- Was the personal loop proven BEFORE team/company was architected? (Kieran's sequencing law — else fail.)
- Do all three variables (access, formality, contribution) differ per tier, or did the tiers collapse into one flat brain? (`genius.md` §Anti-Patterns — flat brain = fail.)
- Is the promote/inherit protocol explicit in both directions (what graduates up, what only inherits down)?
- Is the company tier framed as a differentiation MOAT with provenance-clean, promotion-only entry — not a productivity dump?
- §Rubric Tier-fit ≥8 requires named navigate/promote rules, not just three folders.

## Stacking
Company tier hands to `liam-mley-ai-brain-builder` (`/ai-brain-context` / workflow 02): the company brain IS the AIOS Context Layer — this workflow supplies the graduated-contribution governance liam-mley's flat BRAIN.md lacks. Pair with `/library-notion-port` for a Notion tier substrate and `/library-health-check` per tier (company tier audited most strictly).
