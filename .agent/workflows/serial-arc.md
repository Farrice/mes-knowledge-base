---
description: "Fresh Voice System — plan and produce serial narrative LinkedIn content for Farrice's personal brand"
---

# /serial-arc — Serial Narrative Content Engine

Plan and produce serial narrative LinkedIn content — posts that function as chapters in a story people can't stop following. Uses the Fresh Voice System skill.

## Usage

```
/serial-arc plan [theme]     — Design a narrative arc (5-7 chapters)
/serial-arc next [arc-name]  — Produce the next chapter(s) in an arc
/serial-arc bridge [arc-name] — Produce a conversion post within an arc
/serial-arc status           — Show active arcs, progress, and open loops
/serial-arc                  — Show usage guide
```

**Examples:**
- `/serial-arc plan "the invisible expert pattern"` — Design a 5-7 chapter arc around expertise translation
- `/serial-arc next voice-discovery` — Write the next chapter in the Voice Discovery arc
- `/serial-arc bridge voice-discovery` — Write the conversion post for the Voice Discovery arc
- `/serial-arc status` — See all active arcs and what chapter is next

---

## Execution

### For `/serial-arc plan [theme]`

#### 1. Load Context
Read:
- `skills/fresh-voice-system/genius.md` (serial narrative methodology)
- `skills/fresh-voice-system/SKILL.md` (voice DNA)
- `_active/linkedin-launch/arcs/` (check for active arcs — avoid theme collisions)

#### 2. Execute Workflow
Run `skills/fresh-voice-system/workflows/01-arc-planning.md`:
- Input: the theme provided
- Pull personal stories from user or existing material
- Design the arc with chapter outlines, open loops, and bridge point

#### 3. Save Output
Create directory: `_active/linkedin-launch/arcs/[NN]-[arc-slug]/`
Save arc plan to: `_active/linkedin-launch/arcs/[NN]-[arc-slug]/arc-plan.md`

#### 4. Present for Review
Show the arc plan to Farrice. This is a checkpoint — the arc plan must be approved before producing chapters.

---

### For `/serial-arc next [arc-name]`

#### 1. Load Context
Read:
- `skills/fresh-voice-system/genius.md` (methodology + meta-prompt)
- `skills/fresh-voice-system/SKILL.md` (voice DNA)
- The arc plan: `_active/linkedin-launch/arcs/[arc-name]/arc-plan.md`
- All existing chapters in the arc (for continuity)

#### 2. Determine Next Chapter
Check which chapters already exist in the arc folder. The next chapter is the lowest-numbered one that doesn't have a file yet.

If user specifies a range (e.g., "chapters 3-5"), produce that batch.
Default: produce the single next chapter.

#### 3. Execute Workflow
Run `skills/fresh-voice-system/workflows/02-serial-content-production.md`:
- Input: arc plan + chapter number(s) + previous chapters
- Apply the meta-prompt from genius.md
- Produce chapter post(s)

#### 4. Quality Gate
Every chapter must pass the Serial Narrative Standard (genius.md) AND Voice Quality checks (SKILL.md) before delivery.

#### 5. Save Output
Save each chapter to: `_active/linkedin-launch/arcs/[arc-name]/ch[NN]-[slug].md`

---

### For `/serial-arc bridge [arc-name]`

#### 1. Load Context
Same as `/serial-arc next` plus:
- Current offer details from `_active/linkedin-launch/offers/proof-run-offer-page.md`

#### 2. Execute Workflow
Run `skills/fresh-voice-system/workflows/03-bridge-post-production.md`:
- Input: arc plan + all existing chapters + offer details
- Produce the bridge post

#### 3. Quality Gate
Must pass all serial narrative checks PLUS bridge-specific checks (Remove-the-Offer Test, Earn Test, Understatement Test, Friend Test).

#### 4. Save Output
Save to: `_active/linkedin-launch/arcs/[arc-name]/bridge-[slug].md`

---

### For `/serial-arc status`

#### 1. Scan Active Arcs
Read `_active/linkedin-launch/arcs/` directory.

#### 2. For Each Arc
- Read the arc plan
- Count how many chapters exist vs. planned
- Identify the next chapter to produce
- List open loops that need closing
- Note if the bridge post has been written

#### 3. Present Status
Show a summary table:

```
Active Arcs:
┌──────────────────────┬────────────┬──────────────┬───────────┐
│ Arc Name             │ Progress   │ Next Chapter │ Bridge    │
├──────────────────────┼────────────┼──────────────┼───────────┤
│ voice-discovery      │ 3/6        │ ch04-valley  │ Not yet   │
│ invisible-expert     │ 1/5        │ ch02-deepen  │ Not yet   │
└──────────────────────┴────────────┴──────────────┴───────────┘

Open loops to close in next chapter:
- [Loop description from previous chapter]
```
