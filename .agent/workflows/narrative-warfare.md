---
description: OODA-powered competitive narrative dominance
---

> **Browser tools**: Step 1 (Intelligence Gathering) and Step 6 (Monthly Warfare Review) require live competitor channel monitoring (LinkedIn / Twitter / Substack — all JS-rendered or login-gated). Use Playwright (`mcp__playwright__browser_*`) per `directives/browser-automation-routing.md`. WebFetch returns hydration shells on these surfaces and silently degrades the OODA assessment.

# /narrative-warfare — Competitive Narrative Dominance

Combine OODA loop speed advantage with proof-stacked content and flood-zone tactics. After this, competitors are always responding to YOU — never the reverse.

## Usage

```
/narrative-warfare --competitors "Competitor A, Competitor B, Competitor C"
/narrative-warfare "AI coaching space" --competitors "Dan Koe, Justin Welsh"
```

## Steps

### 1. Load Context
Read these files:
1. `skills/new-media-kingmaker/SKILL.md`
2. `skills/new-media-kingmaker/workflows/02-narrative-warfare.md`
3. `skills/andreessen-horowitz-new-media/genius.md` (OODA section)

### 2. Collect Inputs
- Your brand/founder/organization
- 2-5 key competitors with their public channels
- Current OODA loop speed (or "unknown")
- Active narrative battles (if any)
- Available publishing channels

### 3. Execute Warfare Build
Follow all 6 steps in `02-narrative-warfare.md`:
1. Intelligence Gathering (competitor OODA assessment + narrative map)
2. Speed Architecture (your OODA loop designed for minimum cycle time)
3. Proof-Armed Positions (Luke Iha proof stacks on your top 5 positions)
4. Offensive Disruption Calendar (4-week proactive plan)
5. Defensive Flood Protocol (crisis arsenal pre-built)
6. Monthly Warfare Review (recurring maintenance)

### 4. Source Skill Loading (as needed per step)
- Step 3 → Load `skills/luke-iha-proof-copy/SKILL.md`
- Step 4 → Load `skills/grace-andrews-media-company/workflows/11-content-sprint-planner.md`
- Step 5 → Load `skills/andreessen-horowitz-new-media/references/prompts/05-flood-the-zone-crisis-protocol.md`

### 5. Quality Gate
- Is the speed dominance ratio ≥ 2:1 against nearest competitor?
- Are 5+ positions proof-armed with 3+ proof types each?
- Is the content bank stocked with 10+ emergency pieces?
- Is the disruption calendar actionable (not aspirational)?

### 6. Output
Save to `research_outputs/narrative-warfare-[date].md`

### 7. Finalize
```bash
python3 execution/chain_runner.py finalize "Narrative Warfare Build" \
    --expert "andreessen-horowitz" \
    --skill "new-media-kingmaker" \
    --workflow "narrative-warfare" \
    --type Strategy \
    --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "OODA loop + proof ladder + flood-zone compound"
```
