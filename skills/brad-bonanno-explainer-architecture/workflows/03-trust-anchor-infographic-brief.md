---
name: "The Trust-Anchor Infographic Brief"
produces: "Design briefs for 2-4 branded infographic frames that anchor the highest-trust-impact claims in a video script"
expert: "Brad Bonanno"
load_context: "genius.md"
---

# Brad Bonanno — The Trust-Anchor Infographic Brief

## Role

Generative pre-production workflow. Identifies the 2-4 highest-trust-impact CLAIMS in a video script and produces design briefs for branded infographic frames that anchor each claim numerically or visually. Output: complete design specs ready to hand to a motion-graphics designer (or Canva/Figma session).

**Before executing**: Read [genius.md](../genius.md) — especially Pattern 4 (Branded Infographic Frames as Trust Anchors), Pattern 5 (Pre-empt the Skeptic), HK3 (Cost Transparency as Defensive Moat), and Exemplar B (Cost Chart Pre-emption).

## Input Required

1. **The video script** — Full script, ideally with timestamps. Could also be a structured outline.
2. **Audience skepticism profile** — Where will the viewer push back? ("They'll think this is too expensive" / "They'll assume it doesn't scale" / "They'll question the claim of N customers")
3. **Brand visual language** — Existing palette, fonts, icon style (if any). For new creators: define here.
4. **Production capacity** — DIY in Canva (limits complexity), motion-graphics designer available (high fidelity), AI image gen acceptable (medium fidelity)?
5. **Total infographic budget** — Number of frames AND seconds per frame in final cut. Brad's ratio: 2-4 frames at ~3 seconds each.

## Workflow

### Phase 1 — Claim Inventory

Scan the script and extract every CLAIM that:
- Makes a specific assertion (number, comparison, range, scope)
- Could trigger viewer skepticism ("really?" / "what's the catch?" / "how?")
- Materially affects the buying / believing decision

For each claim, score on 3 axes (1-5):
| Axis | High | Low |
|---|---|---|
| **Skepticism Risk** | Viewer's instinct is "what's the catch?" | Viewer accepts at face value |
| **Decision Weight** | Affects whether viewer adopts/buys | Cosmetic claim |
| **Anchor-ability** | Has specific numbers, exact scope, or visual structure | Vague, opinion-based |

Total score 12+ = candidate for infographic. Stack-rank by total score.

### Phase 2 — Select 2-4 Claims to Anchor (Pattern 4)

**Selection rules**:
- 2 minimum (anything less = under-anchored video)
- 4 maximum (more than 4 dilutes each frame's impact)
- If candidates >4: pick the highest-scoring on **Skepticism Risk × Decision Weight** (multiplied, not summed — both must be high)
- ALWAYS include the cost claim if there is one (HK3 — cost transparency is a defensive moat)
- ALWAYS include the breadth/scope claim if "this works on N things" is a key value prop

**Anti-pattern check**: If you have 5+ "important" claims, your script is overloaded. Consider splitting into 2 videos OR demoting some claims to talking-head-only (no infographic backing).

### Phase 3 — Map Each Claim to an Infographic Archetype

Brad's source video uses 3 archetypes — pick which applies:

#### Archetype A — The Pipeline Diagram (3-5 step flow)
**When**: Claim describes a process or transformation
**Visual**: Horizontal sequence of icon → arrow → icon → arrow → icon, with labels under each
**Example from source**: Frame 44 — "Video with captions → Skill pulls captions → Transcript Ready (Free)"
**Best for**: "Here's how it works" claims, technical pipeline reveals

#### Archetype B — The Cost/Performance Chart (axis-anchored numbers)
**When**: Claim involves cost, time, scale, or performance comparison
**Visual**: Horizontal axis (time/duration/scope) with discrete points, vertical labels showing the metric (cost, frames, output)
**Example from source**: Frame 49 — Cost chart with 1min/10min/30min/1hour and exact dollars + "100 frame cap" callout
**Best for**: Cost claims (HK3), speed claims, scaling claims

#### Archetype C — The Logo Grid / Scope Card (breadth visualization)
**When**: Claim is "this works on N platforms/systems"
**Visual**: Rounded card with platform logos arranged in grid, optional creator PIP on right
**Example from source**: Frame 60 — 10 platform logos (YouTube, Twitch, Vimeo, TikTok, X, Instagram, Facebook, Reddit, SoundCloud, Dailymotion)
**Best for**: Compatibility claims, integration claims, "works with everything" claims

### Phase 4 — Visual Language Lock

Before designing individual infographics, lock the cross-frame visual language:

- **Background**: White or near-white (`#FFFFFF` or `#FAFAFA`) — Brad's choice. Maximum contrast for icons.
- **Primary palette**: 3 colors — neutral text (`#1A1A1A`), accent (channel brand color), highlight (yellow/orange for callouts like "100 frame cap")
- **Typography**: Single sans-serif family across all infographics (Inter, Söhne, or similar). Two weights: bold for labels, regular for body.
- **Icon style**: One icon library across all infographics (don't mix flat with 3D, don't mix outline with filled). Brad uses simple flat icons.
- **Whitespace**: Aggressive. 4-7 elements maximum per frame. Anything more = visual noise.
- **PIP rule**: Optional. If included, bottom-left or bottom-right corner, smaller than infographic content (per HK2).

### Phase 5 — Per-Infographic Design Brief

For each selected claim, produce:

```markdown
### Infographic N: [Claim being anchored]

**Archetype**: [A / B / C]
**Where in video**: [Timestamp range, e.g., 04:35-04:38]
**Duration on screen**: [3-5 seconds — aim for screenshot-ability]
**Triggered by**: [Script line that immediately precedes the cut]

**Visual specification**:
- Background: [color hex]
- Layout: [Specific layout — e.g., "horizontal 3-step flow centered" or "axis chart with 4 data points"]
- Elements (4-7 max):
  1. [Element 1: text + position]
  2. [Element 2: icon + position]
  3. [Element 3: arrow / line / divider]
  4. [Element 4: number / label]
  5. [Optional callout: highlight color + text]
- PIP: [Yes/No — if yes, position]

**Typography**:
- Headline: [font / weight / size]
- Body labels: [font / weight / size]
- Numbers/data: [font / weight / size]

**Production notes**:
- Tool: [Canva template / Figma / Motion graphics]
- Animation: [Static / Animated entry of elements / Animated reveal]
- Export: [PNG/MP4 — include alpha if compositing]

**Trust function**:
[1 sentence on what this infographic does for the viewer's belief — e.g., "Numerically anchors the cost claim so 'essentially free' becomes defensible specifics."]

**Pre-emption pairing** (if applicable per Pattern 5):
[The script line that names the objection in viewer's voice, immediately before this infographic appears. Format: "And you're probably thinking..." → infographic]
```

### Phase 6 — Cross-Infographic Consistency Audit

Before delivering the brief:
- [ ] All infographics use the SAME background color
- [ ] All infographics use the SAME typography family + weights
- [ ] All infographics use icons from the SAME library (no mixing flat + 3D + outline)
- [ ] Total infographic count is 2-4 (not 1, not 5+)
- [ ] At least one infographic anchors a cost claim (HK3) IF the video makes any cost claim
- [ ] Each infographic has 4-7 elements maximum
- [ ] Each infographic is paired with a pre-emption beat in the script (Pattern 5)

## Output Schema

```yaml
trust_anchor_brief:
  video_title: string
  total_infographics: int (2-4)
  visual_language:
    background_color: string (hex)
    palette: array of strings (hex)
    typography_family: string
    icon_library: string
    whitespace_rule: string
  claim_inventory:
    - claim_text: string
      timestamp: string
      skepticism_risk: int (1-5)
      decision_weight: int (1-5)
      anchor_ability: int (1-5)
      total_score: int
      selected_for_infographic: bool
  infographics:
    - number: int
      claim_anchored: string
      archetype: enum [A_Pipeline, B_Chart, C_LogoGrid]
      timestamp_in_video: string
      duration_on_screen_seconds: int
      visual_spec:
        background: string
        layout: string
        elements: array of element objects
        pip: object (position or null)
      typography:
        headline: string
        body: string
        numbers: string
      production_notes:
        tool: string
        animation: string
        export_format: string
      trust_function: string
      preemption_pairing:
        script_line_before: string (verbatim)
        objection_named: string
  consistency_audit:
    same_background: bool
    same_typography: bool
    same_icon_library: bool
    cost_claim_anchored: bool
    element_count_check: bool
```

## Example Output

**Scenario**: A creator drafted a video about a new AI scheduling agent. Script has 5 claims. Wants 3 infographics.

```markdown
## Trust-Anchor Brief: "AI That Schedules Your Whole Week (For Free)"

**Total infographics**: 3
**Visual language locked**:
- Background: `#FAFAFA` (warm white)
- Palette: `#1A1A1A` text, `#3B82F6` accent blue, `#FBBF24` callout yellow
- Typography: Inter (700 bold for labels, 500 medium for body)
- Icon library: Phosphor Icons (flat, single-weight)
- Whitespace: aggressive, 4-7 elements per frame

### Claim Inventory (top scorers selected)
| # | Claim | Skep | Weight | Anchor | Total | Selected? |
|---|---|---|---|---|---|---|
| 1 | "It costs me $0 per week to run" | 5 | 5 | 5 | 15 | ✓ |
| 2 | "It connects to 8 calendar systems" | 3 | 4 | 5 | 12 | ✓ |
| 3 | "It saves me 4 hours/week on average" | 5 | 5 | 4 | 14 | ✓ |
| 4 | "I built it in 3 days" | 2 | 3 | 4 | 9 | (cut — talking-head only) |
| 5 | "It learns my preferences over time" | 3 | 3 | 2 | 8 | (cut — too vague to anchor) |

### Infographic 1: The Cost Chart (Archetype B)

**Where**: 04:30-04:33
**Triggered by**: "And you're probably thinking — 'Brad, this MUST cost something to run.' Let's do the math."

**Visual spec**:
- Background: `#FAFAFA`
- Layout: Horizontal axis chart, 4 data points
- Elements:
  1. Headline (top): "Monthly Cost Breakdown"
  2. Axis points: "Free tier", "Pro plan", "Team plan", "Enterprise"
  3. Cost labels under each: "$0", "$0", "$0", "$0"
  4. Yellow callout box: "Yes — actually free, all tiers"
  5. Footnote (small text): "Includes Google Calendar, Notion, Outlook, Linear API access"
- PIP: None (full-frame infographic)

**Typography**: Inter Bold 32pt headline, Bold 24pt cost labels, Regular 14pt footnote

**Trust function**: Numerically defeats the "what's the catch?" reaction. The yellow callout pre-empts the "but enterprise must cost something" follow-up.

**Pre-emption pairing**: "And you're probably thinking — 'Brad, this MUST cost something to run.' Let's do the math." → infographic appears

### Infographic 2: The Calendar Compatibility Grid (Archetype C)

**Where**: 05:45-05:48
**Triggered by**: "Works with whatever calendar you already use."

**Visual spec**:
- Background: `#FAFAFA`
- Layout: 8-logo grid, 4 columns × 2 rows, rounded cards each
- Elements:
  1. Logo 1: Google Calendar (full color)
  2. Logo 2: Outlook (full color)
  3. Logo 3: Apple Calendar (full color)
  4. Logo 4: Notion Calendar (monochrome)
  5. Logo 5: Linear (monochrome)
  6. Logo 6: Cron (monochrome)
  7. Logo 7: Fantastical (monochrome)
  8. Logo 8: Reclaim (monochrome)
- PIP: Brad's webcam right side, small (per HK2)

**Typography**: No body text on this frame — logos do the work.

**Trust function**: Visualizes breadth. "8 calendars" claim becomes immediately concrete and verifiable (viewer can scan-and-confirm their own calendar is supported).

**Pre-emption pairing**: None — this is a positive scope claim, not an objection rebuttal.

### Infographic 3: The Time Saved Visualization (Archetype B)

**Where**: 06:50-06:53
**Triggered by**: "Across 30 days, that's 16 hours back. Half a workweek."

**Visual spec**:
- Background: `#FAFAFA`
- Layout: Horizontal bar chart comparing "Manual scheduling" vs "Agent scheduling"
- Elements:
  1. Headline: "Hours per Week — Scheduling Effort"
  2. Bar 1: "Manual" — 5.2 hours (long bar, neutral gray)
  3. Bar 2: "Agent" — 1.0 hours (short bar, blue accent)
  4. Difference callout: yellow box "4.2 hrs/week saved"
  5. Footnote: "Avg. across 8 weeks of usage, n=1 (me)"
- PIP: None

**Typography**: Inter Bold 32pt headline, Bold 28pt bar labels, Regular 14pt footnote

**Trust function**: The "n=1 (me)" footnote is the credibility signal — Brad's not faking N=100 user studies. Honest small-N data is more trustworthy than overclaimed "studies show."

**Pre-emption pairing**: "I tracked this for 8 weeks. Sample size of one — me. But the data was wild." → infographic appears

### Cross-Infographic Audit
- [✓] All use `#FAFAFA` background
- [✓] All use Inter typography
- [✓] All use Phosphor icons + monochrome logos consistently
- [✓] Cost claim anchored (Infographic 1)
- [✓] All have ≤7 elements
- [✓] 2 of 3 have pre-emption pairings (Pattern 5 — count = 2)
```

**What makes this excellent**: The brief is hand-off-able. A motion graphics designer (or the creator in Canva) can produce these 3 frames in a single afternoon and they'll be visually consistent. Each frame's TRUST FUNCTION is named, so the creator understands what each infographic is doing for the viewer's belief — not just decorating the script. The "n=1 (me)" footnote in Infographic 3 is the kind of honest credibility signal that distinguishes Brad's style from corporate over-polish.

## Quality Gate

Before delivering, verify:

- [ ] 2-4 infographics selected (not 1, not 5+)
- [ ] If video has any cost claim, an infographic anchors it (HK3)
- [ ] Visual language locked across all frames (background, typography, icons)
- [ ] Each infographic has 4-7 elements maximum
- [ ] Each infographic has a "Trust function" 1-sentence statement
- [ ] At least 1 infographic has a pre-emption pairing (Pattern 5)
- [ ] Production tool specified (Canva / Figma / Motion graphics)
- [ ] Each frame designed for screenshot-ability (clean, complete, attribution-friendly)

**Pass standard**: If the creator screenshots any one of these infographics and posts it standalone on Twitter/LinkedIn, would it deliver value out-of-context? If yes, ship it. If no, the frame is too dependent on surrounding video.
