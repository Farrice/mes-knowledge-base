---
description: "Luke Iha proof ladder deployed across oral/written culture modes — platform-aware proof stacking with culturally native proof types per channel"
---

# /proof-across-platforms — Culturally Native Proof Deployment

Deploy the Luke Iha proof ladder across ALL platforms — but with the a16z oral/written culture matrix determining WHICH proof types work on WHICH platforms. Proof that's native to each platform's cultural physics.

## Usage

```
/proof-across-platforms --topic "[what you're proving]" --platforms "X, LinkedIn, YouTube, Substack"
/proof-across-platforms --topic "Our AI tool reduces churn by 40%" --platforms "all"
```

## Steps

### 1. Load Context
Read these files:
1. `skills/luke-iha-proof-copy/SKILL.md`
2. `skills/luke-iha-proof-copy/genius.md`
3. `skills/andreessen-horowitz-new-media/genius.md` → Oral/Written Culture Matrix section

### 2. Identify Proof Assets
Ask the user to list all available proof:
- Personal experience results
- Customer testimonials and case studies
- Statistical data and research
- Third-party endorsements
- Before/after demonstrations
- Social proof (audience size, engagement, following)

### 3. Map Proof Types to Culture Modes

Build the proof deployment matrix:

| Proof Type | Oral Platforms (X, Shorts, Reels) | Hybrid (LinkedIn) | Written Platforms (Substack, YouTube Long, Blog) |
|-----------|--------------------------------|--------------------|-----------------------------------------------|
| **Demonstration** | ✅ PRIMARY — show don't tell, visual | ✅ Screengrab + narrative | ✅ Full walkthrough with context |
| **Before/After** | ✅ PRIMARY — side-by-side visuals | ✅ Story format with transformation | ✅ Detailed timeline with data |
| **Social Proof** | ✅ Screenshots, quote cards | ✅ Tagged endorsements | ✅ Case study deep dives |
| **Statistical** | ⚠️ One extreme number only | ✅ 2-3 key stats with story | ✅ PRIMARY — full data with analysis |
| **Third-Party** | ⚠️ Name-drop only | ✅ "According to [authority]..." | ✅ PRIMARY — full citation with context |
| **Case Study** | ⚠️ 30-sec version only | ✅ Condensed narrative | ✅ PRIMARY — comprehensive story |
| **Experiential** | ✅ "Watch me do this live" | ✅ "Here's what I learned" | ✅ Full reflection with lessons |

### 4. Generate Platform-Native Proof Content

For EACH active platform, produce proof-loaded content:

**X / Twitter (Oral Culture)**
- Lead with the single most extreme metric or visual
- Hook → proof → "here's why this matters" → CTA
- Generate 5 vicious hooks per position (Luke Iha methodology)
- Maximum 2 proof types per thread (don't overload oral mode)

**LinkedIn (Hybrid)**
- Personal narrative wrapping the proof
- 2-3 proof types braided throughout
- Lara Acosta formatting best practices
- CTA to long-form canonical reference

**YouTube Long / Substack / Blog (Written Culture)**
- Full proof ladder deployment (all 5 rungs)
- Evidence-based argument structure
- Multiple proof types layered
- This is the canonical reference other platforms point to

**Shorts / Reels / TikTok (Oral Culture)**
- ONE proof moment — the most visually compelling
- 30-60 seconds maximum
- Show, don't explain

### 5. Build the Proof Ecosystem
Map how proof flows between platforms:

```
Written-culture anchor (full argument + all proof)
    ↓ Extract
Hybrid post (narrative + 2-3 proof types)
    ↓ Extract
Oral burst (1 extreme proof moment)
```

Never deploy proof in oral-first order. Always establish the full proof structure in written first, then extract.

### 6. Quality Gate
- Is each platform using proof types native to its culture mode?
- Are oral platforms leading with visual/demonstration proof (not research citations)?
- Are written platforms using full proof ladders with evidence stacking?
- Is there a canonical written reference for every claim?
- Would each piece look native on its platform (not like a reformatted essay or a threadified chart)?

### 7. Output
Save to `.tmp/proof-across-platforms/[topic-slug]-[date].md`

### 8. Finalize
```bash
python3 execution/chain_runner.py finalize "Proof Across Platforms" \
    --expert "luke-iha" \
    --skill "luke-iha-proof-copy" \
    --workflow "proof-across-platforms" \
    --type Content \
    --intent 9 --expert-score 8 --adversarial 8 \
    --notes "Cross-pollinated proof ladder with oral/written culture matrix"
```
