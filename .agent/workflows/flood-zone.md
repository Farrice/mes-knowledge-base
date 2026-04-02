---
description: Crisis response that buries attacks under volume
---

# /flood-zone — Flood the Zone Crisis Protocol

Deploy when under narrative attack. Never defend — PRODUCE. Bury the attacking narrative under 3-5 pieces of genuinely interesting content within 36 hours, exploiting the viral post lifecycle (12h up, 24h down, 36h forgotten). Produces a minute-by-minute crisis response playbook with content slate, ally coordination plan, and 48-hour assessment protocol.

**When to use**: Under active attack — hit piece published, narrative misinterpretation going viral, competitor FUD, disgruntled ex-employee, journalist hit. ALSO: proactively designing crisis protocols BEFORE a crisis hits.

## Usage

```
/flood-zone "Active: [description of attack]" --channels "twitter,linkedin,substack"
/flood-zone --proactive "Design crisis protocol for [company]"
```

## Steps

### 1. Load Skills
Read these files:
1. `skills/andreessen-horowitz-new-media/SKILL.md`
2. `skills/andreessen-horowitz-new-media/genius.md`
3. `skills/andreessen-horowitz-new-media/references/prompts/05-flood-the-zone-crisis-protocol.md`

### 2. Assess Viral Lifecycle Position
Where is the attack right now?
- **Pre-viral** (just published, <500 views): Maximum window to execute. You can get ahead of it.
- **Spiking** (0-12 hours, share velocity increasing): Act immediately. Flood starts NOW.
- **Decaying** (12-24 hours, velocity slowing): Produce 2-3 flood pieces to accelerate the decay.
- **Dying** (24-36 hours, negligible sharing): One more interesting piece finishes it off. Resume normal.

### 3. Design the One-Touch Contextual Address
If the attack contains factual misinterpretation:
- Write/outline a 10-15 min long-form piece (video, podcast segment, or Substack)
- NOT defensive. NOT an apology.
- Structure: Acknowledge → contextualize → pivot to something more interesting
- Publish ONCE. Then never reference the attack again.

### 4. Design the Flood (3-5 Content Pieces)
For each piece:
- MUST be genuinely interesting on its own merits (not distractions)
- Different platform, different cultural mode
- Accelerate announcements, product updates, interviews, or data-driven content you were saving

| Piece | Platform | Type | Why It's Genuinely Interesting |
|-------|----------|------|-------------------------------|

### 5. Coordinate Ally Amplification
Identify 3-5 allies (investors, partners, friendly KOLs, portfolio companies):
- They don't need to address your crisis
- They create their own interesting content during the same 36-hour window
- Provide them with shareable assets and talking points

### 6. Build 48-Hour Assessment Checklist
- [ ] Is the original attacking piece still being actively shared?
- [ ] Does searching for [brand name] surface the attack or your flood content?
- [ ] Have journalists picked up the story?
- [ ] Is audience sentiment trending toward attack or your content?

→ If all indicators show decay: crisis is over. Resume normal cadence.

### 7. Save Output
Save to `research_outputs/[date]-flood-zone-[slug].md`

## Output Structure

```
# Flood the Zone Protocol: [Situation]

## Viral Lifecycle Position: [stage]
## One-Touch Contextual Address (script/outline)
## The Flood (3-5 Content Pieces)
| Piece | Platform | Timeline | Brief |
## Ally Amplification Plan (3-5 allies + coordination)
## Minute-by-Minute Timeline (hour 0 → 48)
## 48-Hour Assessment Checklist
```
