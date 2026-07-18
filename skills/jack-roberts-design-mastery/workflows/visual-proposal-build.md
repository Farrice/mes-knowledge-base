# Visual Proposal Build

> Build branded, interactive HTML proposal decks that demonstrate the quality of your work BEFORE the client hires you — the proposal itself becomes the proof of competence.

## Context Required
- **Load First**: `genius.md` — Jack Roberts' full design system methodology
- **Complementary**: `/brand-dna-extraction` for prospect's brand, `/presentation-build` for slide mechanics

## When to Use
- Sending a proposal to a prospective client (ghostwriting, strategy, design, consulting)
- You want the proposal document itself to demonstrate your production quality
- You need to stand out against competitors sending plain-text or basic PDF proposals
- Deploying the "unsolicited demo" pipeline where the free sample IS the pitch

## The Insight
> Most freelancers send proposals in Google Docs. The prospect reads it in the same format as everything else in their inbox. A branded HTML proposal in the prospect's own visual language says "I already understand your world" before they read a single word.

## Inputs
- **Required**: Prospect's website URL (for brand extraction)
- **Required**: What you're proposing (service, scope, deliverables, pricing)
- **Optional**: Meeting transcript or prior conversation context (via Granola)
- **Optional**: Your own brand DESIGN.md (for dual-branding)

## Workflow

### Phase 1: Prospect Brand Extraction

1. Run `/brand-dna-extraction` on the prospect's website URL
2. Pull: logo, primary colors, typography, overall visual personality
3. Create a lightweight `prospect-DESIGN.md` — you don't need the full system, just enough to match their visual language:
   - 3-4 key colors (primary, accent, background, text)
   - Font families (or close equivalents if custom)
   - Border-radius and spacing feel (sharp vs. rounded, dense vs. airy)

### Phase 2: Proposal Architecture

Structure the proposal as a presentation deck (not a document):

```markdown
## Proposal Slide Structure

1. **Cover Slide**: Prospect's logo + your brand mark + project title
2. **Understanding Slide**: "Here's what I understand about your challenge" (shows you listened)
3. **Approach Slide**: Your methodology — visual, not paragraph-heavy
4. **Deliverables Slide**: What they get — timeline, format, scope
5. **Proof Slide**: 1-2 results, testimonials, or samples (not a portfolio dump)
6. **Investment Slide**: Pricing — clean, clear, confident
7. **Next Steps Slide**: Exact action to take (CTA button: "Let's Start" → scheduling link)
```

### Phase 3: Brand-Merged Design System

Merge the prospect's brand DNA with your professional presentation standards:

- **Colors**: Prospect's primary + your accent (shows partnership, not servitude)
- **Logo placement**: Their logo on cover, your logo at bottom-right of all slides
- **Typography**: Use their font if available, professional alternative if not
- **Layout**: Clean, spacious, presentation-weight text (not document-weight)

### Phase 4: Build the HTML Proposal

Using `/presentation-build` as the engine:

1. Generate a self-contained HTML file with:
   - Keyboard navigation (arrow keys)
   - Smooth slide transitions
   - Responsive design (works on phone, tablet, desktop)
   - No external dependencies

2. Apply these proposal-specific rules:
   - **Max 4 lines of text per slide** — less than a standard presentation
   - **One number per data slide** — make metrics impossible to miss
   - **CTA button on final slide** — links to calendar/scheduling tool
   - **Professional motion**: Subtle entrance animations, nothing flashy

### Phase 5: Content Injection

If meeting/conversation context is available:
- Reference specific things the prospect said: *"You mentioned X — here's how we address that"*
- Include relevant data from their industry (factchecked via sub-agents)
- Mirror their language and priorities, not generic proposal copy

If unsolicited (cold outreach):
- Lead with a specific observation about their current content/brand
- Show you did homework, not template mail-merge
- Include a micro-sample: one paragraph in their voice, one redesigned page element

### Phase 6: Polish & Deliver

1. Run `/anti-slop-audit` on the finished HTML — must score 13+/15
2. Verify all links work (scheduling, portfolio, social)
3. Test on mobile (most first-views happen on phone)
4. Export as both:
   - **HTML file** (attach directly or host)
   - **PDF backup** (for prospects who won't open HTML)
5. Send with a one-line email: "Built this for you — 7 slides, 2 minutes. [Link]"

## Output
- Self-contained HTML proposal deck (branded to the prospect)
- PDF backup export
- Anti-Slop scorecard
- Follow-up email template (one-liner)

## Why This Works
The proposal demonstrates FOUR things simultaneously:
1. **You understand their brand** (you matched their visual language)
2. **Your production quality is professional** (HTML, not Google Docs)
3. **You respect their time** (7 slides, not 12 pages)
4. **You can execute** (the proposal IS the proof of work)

## Output Schema
```
Visual Proposal: [prospect name]
├── proposal.html         (self-contained, 7-slide structure per Phase 2, prospect-branded)
├── proposal.pdf          (backup export for non-HTML viewers)
├── Anti-Slop Scorecard   (must show 13+/15)
└── Follow-up Email       (one-line template, per Phase 6 send step)
```

## Quality Gate
- `/anti-slop-audit` score of 13+/15 (Phase 6) — this is a hard numeric floor, not a suggestion; below threshold, iterate before sending.
- Max 4 lines of text per slide (Phase 4) — a proposal that reads document-weight fails the format's own premise.
- Every link tested and working (scheduling, portfolio, social) — a broken CTA link on the Next Steps slide undermines "you can execute."
- Mobile tested — per Phase 6, most first-views happen on phone; a proposal that breaks on mobile fails regardless of desktop polish.
- Content Injection (Phase 5) reflects real context — a cold-outreach proposal includes a genuine specific observation about the prospect, not generic template language dressed in their brand colors.
