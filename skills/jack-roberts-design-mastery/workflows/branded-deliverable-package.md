# Branded Deliverable Package

> Automatically package every client deliverable — strategy docs, research reports, ICP profiles — in the client's own brand system. White-label by default.

## Context Required
- **Load First**: `genius.md` — Jack Roberts' DESIGN.md-as-source-of-truth pattern
- **Complementary**: `/brand-dna-extraction` for client brand, `/multi-format-deploy` for cross-format consistency

## When to Use
- Delivering any strategy document, research report, or analysis to a client
- You want deliverables to feel premium and worth more than the price
- You're building a portfolio of professional-grade outputs
- You need consistent visual branding across multiple deliverables for the same client

## The Insight
> A $2,000 strategy document in raw markdown looks like a $200 ChatGPT output. The same content in a branded, designed PDF commands $5,000. Design is the packaging that communicates value.

## Inputs
- **Required**: The deliverable content (strategy doc, ICP profile, research report, etc.)
- **Required**: Client's website URL OR existing client DESIGN.md
- **Optional**: Deliverable type (report, one-pager, framework, audit, playbook)
- **Optional**: Your own brand DESIGN.md for co-branding

## Workflow

### Phase 1: Client Brand Extraction (One-Time Per Client)

If a client DESIGN.md doesn't already exist:

1. Run `/brand-dna-extraction` on the client's website
2. Create a `client-DESIGN.md` with:
   - Color palette (primary, accent, neutrals from their brand)
   - Typography (their fonts or professional equivalents)
   - Logo files (extracted or provided)
   - Layout preferences (density, spacing, border-radius)
3. Save to `clients/[client-name]/DESIGN.md` — reuse for all future deliverables

If a client DESIGN.md already exists → load it directly.

### Phase 2: Deliverable Template Selection

Map the content type to the right visual format:

| Content Type | Template | Key Design Choices |
|-------------|----------|-------------------|
| **Strategy Doc** | Multi-page report | Table of contents, section headers, callout boxes |
| **ICP Profile** | Visual one-pager + detail pages | Avatar image, demographic cards, psychographic maps |
| **Research Report** | Data-rich document | Charts, tables, citation styling, executive summary |
| **Content Calendar** | Grid/table layout | Color-coded categories, timeline visualization |
| **Audit/Scorecard** | Dashboard-style | Score visualizations, red/yellow/green indicators |
| **Playbook** | Step-by-step guide | Numbered phases, checklists, process diagrams |
| **Framework** | Visual model | Diagram-centered, minimal text, reference card style |

### Phase 3: Design System Mapping

Translate the client DESIGN.md into document-specific styling:

```markdown
## Document Design Rules

### Cover Page
- Client logo: top-center, 20% width
- Title: DESIGN.md H1 font, primary color
- Subtitle: DESIGN.md body font, secondary text color
- Date and version: small text, bottom-right
- Background: client primary color at 5% opacity OR solid accent bar

### Section Headers
- Font: DESIGN.md heading font
- Color: client primary color
- Divider: 2px solid accent color below header
- Spacing: 32px above, 16px below

### Body Content
- Font: DESIGN.md body font, appropriate reading size
- Line-height: 1.6-1.8 for report readability
- Max width: 680px for comfortable reading
- Color: DESIGN.md primary text color

### Callout Boxes
- Background: client accent color at 10% opacity
- Border-left: 4px solid accent color
- Padding: 20px
- Font: body font, slightly smaller

### Data Tables
- Header row: client primary color background, white text
- Alternating rows: white / client background at 3% opacity
- Border: 1px solid border color from DESIGN.md

### Charts & Visualizations
- Color palette: derived from client DESIGN.md (3-4 chart colors)
- Style: clean axes, no chartjunk, labeled data points

### Footer
- Your brand mark: bottom-left, discrete
- Page numbers: bottom-center
- Client logo: bottom-right, small
```

### Phase 4: Content Packaging

1. **Structure the content** for the selected template format
2. **Apply the design system** — every visual element traces to the client DESIGN.md
3. **Generate the HTML document** — self-contained, print-ready
4. **Export formats:**
   - HTML (interactive, linkable)
   - PDF (for sending via email)
   - Print stylesheet (for physical presentation)

### Phase 5: Quality Gate

| Check | Standard |
|-------|----------|
| **Brand fidelity** | Every color matches client DESIGN.md |
| **Professional typography** | Headings, body, captions have clear hierarchy |
| **Content completeness** | No placeholder text, all sections filled |
| **Print readiness** | PDF renders clean at standard page sizes |
| **Co-branding balance** | Client brand dominant, your brand subtle |
| **Anti-Slop** | Doesn't look like a default template |

### Phase 6: Client Asset Library

After packaging, update the client's asset library:
```
clients/[client-name]/
├── DESIGN.md              (brand system — reuse for all deliverables)
├── deliverables/
│   ├── [deliverable-1].html
│   ├── [deliverable-1].pdf
│   └── [deliverable-2].html
├── brand-assets/
│   ├── logo.svg
│   └── logo-dark.svg
└── notes.md               (client preferences, feedback history)
```

## Output
- Branded HTML document (self-contained)
- PDF export (print-ready)
- Client DESIGN.md (created or reused)
- Updated client asset library

## The Multiplier Effect
Every deliverable you produce now:
- Looks custom-designed (client's own brand)
- Costs zero additional design time (DESIGN.md handles it)
- Builds a portfolio of professional-grade work
- Commands premium pricing (perception = value)

## Output Schema
```
Branded Deliverable: [client name] / [deliverable type]
├── [deliverable-name].html   (self-contained, print-ready, client-branded)
├── [deliverable-name].pdf    (email-ready export)
├── DESIGN Rules applied      (Cover Page / Section Headers / Body / Callouts / Tables / Charts / Footer — per Phase 3)
└── clients/[client-name]/    (DESIGN.md + deliverables/ + brand-assets/ + notes.md, updated per Phase 6)
```

## Quality Gate
This workflow's Quality Gate is Phase 5 above — promoted here as the binding pass/fail list before any deliverable ships:
- **Brand fidelity**: every color traces to the client DESIGN.md, zero off-system hex values.
- **Professional typography**: headings, body, and captions carry a clear, DESIGN.md-sourced hierarchy.
- **Content completeness**: no placeholder text — every section of the selected template (Phase 2) is filled.
- **Print readiness**: the PDF export renders clean at standard page sizes, no cut-off content.
- **Co-branding balance**: client brand dominant, your brand mark discrete (bottom-left, per Phase 3 Footer spec).
- **Anti-Slop**: the document does not read as a default report template — run `/anti-slop-audit` if any doubt remains.
