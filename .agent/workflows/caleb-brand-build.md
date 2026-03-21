---
description: "Take anyone from zero to revenue-generating personal brand — 6-phase pipeline chaining all Caleb Ralston workflows: discovery → architecture → platform → content → packaging → revenue"
---

# /caleb-brand-build — Full Personal Brand Operating System

Build a complete personal brand from scratch using Caleb Ralston's trust-first methodology. Chains 6 phases through component workflows with stage assessment, quality gates, and cross-skill enrichment.

**The standard**: This is the "Caleb as a service" command — the output is a complete Brand Operating System document that anyone can immediately execute against.

## Usage

```
/caleb-brand-build [person/brand name] --niche "[niche description]"
/caleb-brand-build "Alex Chen" --niche "AI dev tools for indie hackers"
/caleb-brand-build   # (will prompt for inputs)
```

## Steps

### 1. Load Skills
// turbo
Read these files in order:
1. `skills/caleb-ralston-personal-brand/genius.md`
2. `skills/caleb-ralston-personal-brand/workflows/caleb-brand-build.md`

### 2. Load Agent
// turbo
Read: `agents/caleb-ralston/AGENT.md`

### 3. Stage Assessment
Ask the user: "Where are you in your personal brand journey?" and route per the workflow's stage assessment table.

### 4. Execute All Applicable Phases
Follow the 6-phase pipeline in `caleb-brand-build.md`:
- Phase 1: Discovery (zero-to-brand-launchpad)
- Phase 2: Architecture (authority-foundation-blueprint)
- Phase 3: Platform Strategy (content-format-strategy-engine)
- Phase 4: Content Engine (trust-based-content-engine)
- Phase 5: Packaging (wrapping-paper-library-builder)
- Phase 6: Revenue Activation (growth-revenue-activation)

Run quality gates between each phase. Do NOT advance if the gate fails.

### 5. Assemble Master Blueprint
Combine all phase outputs into a single Brand Operating System document per the workflow template.

### 6. Cross-Skill Enrichment
Check if stacking would improve the output:
- LinkedIn → Lara Acosta
- Copy → Luke Iha
- YouTube → Kallaway
- Offers → Nicolas Cole
- Email → Cardinal Mason

### 7. Save Output
Save to `deliverables/caleb-brand-build-[name-slug]-[date].md`

### 8. Finalize
```bash
python3 execution/chain_runner.py finalize "Full Caleb Brand Build for [name]" \
    --expert caleb-ralston \
    --skill caleb-ralston-personal-brand \
    --workflow caleb-brand-build \
    --type Strategy \
    --intent 9 --expert-score 8 --adversarial 8 \
    --notes "[what worked, what needed adjustment]"
```
