---
description: Platform-native launch-as-a-service
---

# /platform-launch — Launch as a Service

Design and execute a product/company/feature launch that treats every platform as a different medium. Different content, different taste, different creative execution — NOT reformatted versions of the same announcement.

## Usage

```
/platform-launch "[product/feature name]" --audience "[target]"
/platform-launch "CodeReview AI v2" --audience "indie developers and startup CTOs"
```

## Steps

### 1. Load Context
Read these files:
1. `skills/new-media-kingmaker/SKILL.md`
2. `skills/new-media-kingmaker/workflows/03-platform-launch.md`
3. `skills/andreessen-horowitz-new-media/references/prompts/06-platform-native-launch-service.md`

### 2. Collect Inputs
- Product/feature being launched
- Target audience segments
- Available platforms
- Founder's capacity for direct involvement
- Existing assets (demos, screenshots, data, customer stories)
- Launch date and timeline

### 3. Execute Launch Build
Follow all 8 steps in `03-platform-launch.md`:
1. Core Launch Concept (the single unifying insight)
2. Platform-Native Content Slate (different content per platform)
3. Proof Loading Per Platform (Luke Iha methodology)
4. Founder Go-Direct Activation (personal deliverables)
5. Cascade Sequence Design (minute-by-minute timeline)
6. Ally Amplification Network (10-20 coordinated allies)
7. Real-Time OODA Protocol (monitoring + rapid iteration)
8. Post-Launch Assessment (7-day scorecard)

### 4. Source Skill Loading
- Step 2 → Load `skills/andreessen-horowitz-new-media/genius.md`
- Step 3 → Load `skills/luke-iha-proof-copy/SKILL.md`
- Step 4 → Load `skills/lara-acosta/SKILL.md` (for LinkedIn piece)
- Step 5 → Load `skills/cardinal-mason/SKILL.md` (for email sequence)

### 5. Quality Gate
- Is every platform's content genuinely DIFFERENT (not reformatted)?
- Does each piece match its platform's culture mode (oral/written)?
- Is the founder personally involved (not just the brand)?
- Is the cascade sequence timed to the minute?
- Are 10+ allies pre-coordinated?

### 6. Output
Save to `deliverables/platform-launch-[product-slug]-[date].md`

### 7. Finalize
```bash
python3 execution/chain_runner.py finalize "Platform Launch for [product]" \
    --expert "andreessen-horowitz" \
    --skill "new-media-kingmaker" \
    --workflow "platform-launch" \
    --type Strategy \
    --intent [evidence-based] --expert-score [evidence-based] --adversarial [evidence-based] \
    --notes "Platform-native launch with cross-expert content slate"
```
