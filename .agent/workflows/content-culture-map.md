---
description: Map content to oral/written cultural modes
---

# /content-culture-map — Oral/Written Culture Content Architect

Design content strategy using Andreessen's oral/written culture matrix. Instead of "what platform should I post on?", this answers "what CULTURAL MODE is each piece of content?" and maps it to the correct platform. Produces a production flow where written culture content is produced FIRST, oral culture content is EXTRACTED from it, and no complex position ever debuts in short form.

**When to use**: Content feels generic or cross-posted. You're reformatting instead of creating platform-native content. You don't know WHY certain content fails on certain platforms. You need a content production system, not just a posting schedule.

## Usage

```
/content-culture-map [brand/person]
/content-culture-map "My Brand" --platforms "twitter,linkedin,youtube,substack,tiktok"
/content-culture-map --messages "list of key messages to classify"
```

## Steps

### 1. Load Skills
Read these files:
1. `skills/andreessen-horowitz-new-media/SKILL.md`
2. `skills/andreessen-horowitz-new-media/genius.md`
3. `skills/andreessen-horowitz-new-media/workflows/03-culture-content-architect.md`

### 2. Gather Key Messages
From user input, determine:
- Brand's key messages, positions, and arguments
- Available platforms
- Weekly content capacity (how much can they produce?)
- Team size and skills

### 3. Execute Workflow
Follow every step in `03-culture-content-architect.md`:
- Step 1: Platform-Culture Matrix (classify every active platform)
- Step 2: Content Library Classification (sort messages into oral/written/cross-mode)
- Step 3: Production Flow Design (written-first pipeline)
- Step 4: Staffing Recommendations (matched to culture mode)
- Step 5: Weekly Content Calendar

### 4. Cross-Reference with Existing Workflows
Integrate with the broader content system:
- If the user also runs `/grace-city-blueprint`: map culture modes to city districts
- If the user also runs `/launch-day`: use the culture matrix to inform expert routing per platform
- If the user also runs `/atomize`: use the written→oral extraction flow as the atomization backbone

### 5. Save Output
Save to `research_outputs/[date]-content-culture-map-[brand-slug].md`

## Output Structure

```
# Oral/Written Culture Architecture: [Brand]

## Platform-Culture Matrix
| Platform | Culture Mode | Your Play |

## Content Classification
### Oral-Native Messages
### Written-Native Messages
### Cross-Mode Messages (two-stage plan)

## Production Flow
[Written → Oral extraction pipeline]

## Staffing Model
[Who does what]

## Weekly Content Calendar
| Day | Activity | Mode | Output |

## The Cardinal Rule
Written anchor → oral extraction. Always.
Never debut a complex position in oral-mode format.
```

**Execution prompts**: before producing the deliverable, check `skills/andreessen-horowitz-new-media/references/prompts-v2/` for the matching structure-pure prompt and honor its Output Contract (prompt-load sweep, 2026-07-21).
