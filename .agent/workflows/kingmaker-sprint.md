---
description: Chains 5+ expert skills through a16z kingmaker methodology
---

# /kingmaker-sprint — Invisible to Dominant in 30 Days

The full a16z playbook deployed across your expert stack: audit → position → build → launch → protect.

## Usage

```
/kingmaker-sprint [founder/brand name] --niche "[niche]"
/kingmaker-sprint "Alex Chen" --niche "AI dev tools for indie hackers"
```

## Steps

### 1. Load Context
Read these files in order:
1. `skills/new-media-kingmaker/SKILL.md`
2. `skills/new-media-kingmaker/workflows/01-kingmaker-sprint.md`

### 2. Collect Inputs
Gather from user:
- Target founder/brand name, company, industry
- Current media presence (or "starting from zero")
- Key competitors (2-5)
- Core product/service
- Founder's suppressed opinions (the ones they don't say publicly)
- Weekly capacity for content production

### 3. Execute the Sprint
Follow all 12 steps in `01-kingmaker-sprint.md` in sequence.

At each phase, load the referenced source skills:
- Phase 1: a16z new-media + Nicolas Cole ghostwriting
- Phase 2: Grace Andrews media company + a16z OODA
- Phase 3: Luke Iha proof copy + Lara Acosta LinkedIn + Cardinal Mason email
- Phase 4: a16z launch service + Luke Iha hooks
- Phase 5: a16z OODA loop + flood-zone

### 4. Quality Gate
- Is every content piece tagged for oral/written culture mode?
- Does the founder pass the Joe Rogan test at +3 from baseline?
- Is the OODA loop speed under 12 hours?
- Are 15+ proof assets deployed across platforms?
- Is the crisis protocol built and ready?

### 5. Output
Save to `deliverables/kingmaker-sprint-[brand-slug]-[date].md`

### 6. Finalize
```bash
python3 execution/chain_runner.py finalize "Kingmaker Sprint for [brand]" \
    --expert "andreessen-horowitz" \
    --skill "new-media-kingmaker" \
    --workflow "kingmaker-sprint" \
    --type Strategy \
    --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "Cross-pollinated 5+ experts through a16z methodology"
```
