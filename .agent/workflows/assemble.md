---
description: Expert Assembly OS — hybrid panel (roster + bespoke) for any domain, with roadmap synthesis
---

# /assemble — Expert Assembly OS

Assemble a world-class expert panel for ANY task. The system detects domain coverage gaps in the 227-card roster, seats strong matches directly, synthesizes bespoke composite personas where coverage is thin/absent, runs genuine multi-round deliberation, and emits a **tiered roadmap** (strategic 6–12mo / tactical 1–6mo / operational 0–30d) with observable success criteria.

This is your "I don't know this domain" command. No fabricated credentials. No phantom research. Real synthesis.

## Usage
```
/assemble "Design a premium offer + launch narrative for an invisible-expert coaching brand"
/assemble --domains "positioning,offer architecture,messaging" "Build a consulting firm positioning for a mid-market tech CFO"
```

## How to run it
This command fronts the hybrid panel engine. Execute it by invoking the **Workflow tool** with:
- `scriptPath`: `.agent/workflows/expert-assembly.workflow.js`
- `args`: `{ "task": "<the user's task>", "domains": ["domain1", "domain2"], "mode": "panel" }`

Optional args:
- `domains`: comma-separated list of required domains (auto-extracted from task if omitted)
- `mode`: always `"panel"` (reserved for future multi-mode expansion)

## What it does (phases)

1. **Scope** — extract 2–4 critical required domains from the task (auto or supplied).
2. **Cast** — `panel_cast.py` detects roster coverage per domain (strong/thin/absent), seats 3–5 panelists: roster experts for strong domains, bespoke synthesis slots for thin/absent.
3. **Forge** — synthesize full bespoke personas (500–1000 word narratives) per McClain protocol (Steps 1–4 + 6: identity, backstory, worldview, voice, signature methodology); `persona_stat_lint.py` gates out fabricated stats; regenerate on FLAG (max 1 retry).
4. **Ground** — anti-echo-chamber pass: 3-5 DISCONFIRMING queries via `research.py --depth quick` seed a Claims Grounding Table before any panelist speaks (skipped for Creative tasks or `skip_ground: true`).
5. **Diverge** — all 3–5 panelists (roster + bespoke) give independent takes, unanchored; Farrice's own lens included as the Function Owner.
6. **Deliberate** — 2 rounds of genuine cross-talk: panelists build on, challenge, cross-pollinate each other. Contradictions **preserved** in "forks" for your decision.
7. **Synthesize** — emit a **complete decision-grade roadmap**:
   - Panel (labeled; Roster vs Composite marked)
   - Claims Grounding Table (if any factual claims)
   - Synthesis (crux, net-new principle, forks with tradeoffs)
   - Roadmap (Operational 0–30d / Tactical 1–6mo / Strategic 6–12mo; Move / Owner / Success Criteria / Dependencies)
   - Composition Ledger (which expert filled which seat, why)
   - Next Moves Together (specific guidance on what you're building together)
   - Blind Spots We Flagged (what the panel can't see clearly)
   - `grounding_guard.py --task-type Strategy` verification gate on all claims.
8. **Close** — capture a "How the Masters Thought" learning digest (how each expert's signature move shaped the synthesis), pin the panel session for `/panel-sync` reload.

## When NOT to use

- **Roster council only, no roadmap** → `/convene` (faster, lighter, pure deliberation; no synthesis roadmap).
- **Pure fact-gathering, no panel synthesis** → `/deep-research` (research swarm).
- **Single expert for a known domain** → invoke that expert directly (`/[expert-name]`).
- **Exploration mode, no deliverable** → `/wayfinder-work` (dialogue-driven wayfinding).
- **Thin domain coverage + pure brainstorm** → `/convene` on the specific domains you need.

## Manual Runbook (if Workflow unavailable)

If the Workflow engine is down, execute manually:

```bash
# Step 1: Extract required domains
# (Or specify them manually: "positioning, offer architecture, messaging")

# Step 2: Cast the hybrid panel
python3 execution/panel_cast.py "Your task here" --domains "domain1,domain2,domain3" --mode panel

# Step 3: For each bespoke slot in the output, synthesize a persona
# Prompt: (see references/persona-synthesis-prompt.md)
# Gate: python3 execution/persona_stat_lint.py <persona-file> --verbose
# Retry if FLAG; strip to methodology-only if blocked twice.

# Step 4: Diverge — get each panelist's take
# For each panelist, prompt with (see expert-assembly.workflow.js divergePrompt):
# "You are [Name]. What's YOUR take on this task?"

# Step 5: Deliberate — Round A
# Prompt each panelist: "You just heard [other takes]. Build on someone, challenge someone, cross-pollinate."

# Step 6: Converge
# Prompt: "Panel deliberation summary: [all responses]. What's the CRUX? What's the net-new principle?"

# Step 7: Synthesize roadmap
# Prompt the panel: "Synthesize into a decision-grade roadmap following references/roadmap-schema.md"
# Gate: python3 execution/grounding_guard.py /dev/stdin --task-type Strategy <(echo "$roadmap_text")

# Step 8: Capture learning
# Prompt: "How the Masters Thought — [task]. Each expert's signature move + stealable rule + the collision that sparked the net-new principle."

# Step 9: Pin for /panel-sync
# Save panel.json + personas/*.md to .tmp/assemble/<slug>/
```

## Grounding & Truth

- **No fabricated stats**: Personas synthesized without real company names, %, $, or false org attributions. Authority comes from methodology specificity.
- **Composite label required**: Every bespoke persona begins with "[Composite Synthesis]" disclosure.
- **Claims verified**: All factual claims in the roadmap (market sizing, technical assertions, source attributions) pass `grounding_guard.py` before delivery.
- **Blind spots flagged**: Panel always surfaces what they can't see clearly and why you should compensate.

## Output Location

Pinned session metadata goes to `.agent/handoffs/assemble-<slug>.md` for `/panel-sync` retrieval. Full panel (personas + metadata) lives in `.tmp/assemble/<slug>/` (ephemeral; clean up post-delivery if desired).

## Examples

### Example 1: Zero-Coverage Domain
**Task**: "Competitive sailing rigging optimization"  
**Domains**: "rigging engineering, sailing performance, composite materials"

→ All domains thin/absent in roster  
→ 3 bespoke composites synthesized (mechanical engineer with competition background, aerodynamicist, materials scientist)  
→ Deliberation: collision between aerodynamics + materials science + competitive positioning  
→ Roadmap: operational rig audit + testing; tactical prototyping; strategic market positioning

### Example 2: Hybrid Coverage
**Task**: "LinkedIn content strategy for a premium coaching offer"  
**Domains**: "LinkedIn growth, offer positioning, content strategy"

→ 2 strong roster matches (Tommy Clark, Ross McKay)  
→ 1 thin domain gets composite synthesis (behavioral economist × positioning specialist)  
→ Deliberation: roster voices + synthesized lens = integrated strategy  
→ Roadmap: operational content calendar; tactical offer architecture; strategic brand positioning

---

See also:
- **Skill home**: `skills/expert-assembly-os/SKILL.md`
- **Persona synthesis protocol**: `skills/expert-assembly-os/references/persona-synthesis-prompt.md`
- **Roadmap output contract**: `skills/expert-assembly-os/references/roadmap-schema.md`
- **Lineage & design intent**: `skills/expert-assembly-os/references/lineage.md`
- **Hybrid casting logic**: `execution/panel_cast.py --help`
- **Persona credential gating**: `execution/persona_stat_lint.py --help`
- **Claims verification**: `execution/grounding_guard.py --task-type Strategy --help`
- **Resume a pinned session**: `/panel-sync`
