# Presentation Build

> Build interactive, brand-consistent HTML slide decks that make PowerPoint and Keynote look like relics — the format Jack Roberts uses for his own videos.

## Context Required
- **Load First**: `genius.md` — Presentation-specific patterns from the 5-Step System
- **Required**: A `DESIGN.md` file OR brand to extract from
- **Optional**: Meeting transcript (via Granola integration) for context-aware content

## Inputs
- **Required**: Presentation topic or brief
- **Required**: Audience and purpose (education, sales pitch, internal review, keynote)
- **Required**: Brand/DESIGN.md to style against
- **Optional**: Slide count target
- **Optional**: Content outline or talking points
- **Optional**: Client brand to feature (for client-facing decks)

## Workflow

### Phase 0: Context Injection (Meeting-Aware Presentations)

If this presentation is for a specific meeting, client, or project:

1. **Check Granola for meeting transcripts:**
   - Search for recent meetings with the client/stakeholder
   - Extract key discussion points, decisions, and action items
   - Pull direct quotes that should appear in the deck
   - Note any commitments or metrics mentioned

2. **Check Gmail/Calendar for context:**
   - Upcoming meeting details (attendees, agenda, time constraints)
   - Previous email threads with relevant data points
   - Attachments or documents referenced in correspondence

3. **Synthesize context brief:**
   ```
   Meeting Context: [who, when, what was discussed]
   Key Points to Address: [from transcript/email]
   Audience Expectations: [derived from prior interactions]
   Data Points Available: [stats, metrics, claims from context]
   ```

> This phase is what separates a generic deck from a context-aware presentation. Jack Roberts: "I want you to pull the meeting transcript and use that to populate the content." Skip this phase ONLY for topic-driven (non-meeting) presentations.

### Phase 1: Presentation Architecture

1. **Define the deck structure:**
   - Opening slide: Logo centered, title, subtitle
   - Content slides: Topic-per-slide, not paragraph-per-slide
   - Data slides: Visualization > tables > bullet points
   - Transition slides: Section breaks with visual breathing room
   - Closing slide: CTA or client logo (context-dependent)

2. **Set presentation specifications:**
   ```
   Format:          HTML (self-contained, single file)
   Aspect Ratio:    16:9
   Navigation:      Arrow keys + click
   Slide Count:     [target number]
   Text Density:    Presentation-weight (NOT document-weight)
   Animation:       Slide transitions + element entrance effects
   ```

3. **Content research** (if topic-based, not content-provided):
   - Research the topic comprehensively
   - Fact-check with sub-agent verification
   - Extract 3-5 key insights per slide
   - Source all statistics and claims

### Phase 2: Slide Design System

Map the DESIGN.md to presentation-specific rules:

```markdown
## Presentation Design Rules

### Slide Master
- Background: [DESIGN.md background color or gradient]
- Max content width: 85% of slide width
- Vertical alignment: Center-weighted
- Logo placement: Bottom-right, 5% height, 50% opacity

### Typography Mapping
- Slide Title: DESIGN.md H1 → [size for 16:9]
- Key Statement: DESIGN.md H2 → [large, impactful]
- Body Text: DESIGN.md Body Large → [legible at distance]
- Labels/Captions: DESIGN.md Small → [supporting text]
- Data/Numbers: DESIGN.md Display → [highlighted stats]

### Color Usage
- Title text: [DESIGN.md primary text color]
- Accent elements: [DESIGN.md accent color]
- Background variation: Alternate between [2-3 backgrounds]
- Data visualization: [3-4 colors from palette for charts]

### Visual Elements
- Icons: [line/filled, from DESIGN.md icon style]
- Dividers: [style from DESIGN.md borders]
- Image treatment: [rounded corners per DESIGN.md]
- Charts/graphs: [DESIGN.md colors, clean axes]
```

### Phase 3: Slide-by-Slide Production

For each slide, produce:

1. **HTML structure** with semantic slide containers
2. **CSS styling** using DESIGN.md tokens exclusively
3. **Content** formatted for presentation (not document) density:
   - Maximum 6 lines of text per slide
   - One key idea per slide
   - Metrics/numbers get their own visual treatment
   - Lead with metaphors where possible (Jack Roberts signature)
4. **Animations:**
   - Slide transition: CSS transform + opacity (300-500ms ease)
   - Element entrance: Staggered fade-up (50-100ms delay per element)
   - Data reveals: Progressive disclosure on click/advance

### Phase 4: Interactive Features

Build these interactive capabilities:

- **Keyboard navigation**: Left/Right arrows, Escape for overview
- **Progress indicator**: Slide number (e.g., "01/15") or progress bar
- **Slide overview mode**: Grid view of all slides (press 'O' or 'Escape')
- **Presenter notes**: Hidden by default, togglable (press 'N')
- **Full-screen mode**: F11 or button
- **Print/Export**: CSS print stylesheet for PDF export

### Phase 5: Brand Injection

If this is a client-facing or branded presentation:
1. Extract client logo via Firecrawl/Brand DNA Extraction
2. Place client logo on final slide
3. Your brand logo on slide 1 and bottom-right of all slides
4. Match primary CTA/accent colors to the presentation's brand
5. Include brand-consistent imagery

### Phase 6: Quality Validation

| Check | Standard |
|-------|----------|
| **Text density** | No slide has more than 6 lines of body text |
| **Visual hierarchy** | Every slide has a clear focal point |
| **Brand consistency** | Every color/font traces to DESIGN.md |
| **Readability** | Text is legible at presentation distance (min 24px effective) |
| **Animation polish** | Transitions are smooth, not distracting |
| **Navigation works** | Arrows, clicks, keyboard all functional |
| **Anti-Slop** | No generic AI aesthetics; this looks custom-designed |
| **Content accuracy** | All facts and claims are sourced |

## Output
- Self-contained HTML file (single file, portable)
- Runs in any browser with no dependencies
- Print-ready CSS for PDF export
- Presenter notes embedded (togglable)
- Quality scorecard

## Output Schema
```
Presentation Deck: [topic/client]
├── deck.html                 (self-contained, 16:9, keyboard-navigable)
├── Presentation Design Rules (Slide Master / Typography Mapping / Color Usage / Visual Elements — per Phase 2)
├── Presenter Notes           (embedded, togglable via 'N')
├── Print stylesheet          (PDF export path)
└── Quality Scorecard         (Phase 6 table, one row scored per check)
```

## Quality Gate
This workflow's Quality Gate is Phase 6 above — every row required before delivery:
- **Text density**: no slide exceeds 6 lines of body text (Phase 3's own production rule).
- **Visual hierarchy**: every slide has one clear focal point, not competing elements.
- **Brand consistency**: every color and font traces to the DESIGN.md — zero off-system values.
- **Readability**: minimum 24px effective text size at presentation distance.
- **Navigation works**: arrow keys, click-advance, and overview mode ('O'/Escape) all functional — test before delivery, don't assume.
- **Content accuracy**: if Phase 1's content research step ran, every stat and claim is sourced — an unsourced number on a slide fails this gate regardless of visual polish.
