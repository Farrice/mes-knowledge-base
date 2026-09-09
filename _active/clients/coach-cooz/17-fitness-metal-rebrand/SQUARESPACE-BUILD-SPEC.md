# Squarespace build specification

## Implementation verdict

The local HTML preview is a visual prototype and implementation reference. Squarespace does not provide a one-click way to import this complete HTML page as an editable Squarespace 7.1 page.

Build the approved design with native Fluid Engine sections, text blocks, image blocks, buttons, testimonial blocks, and a Squarespace form. Add the palette, type, borders, and restrained poster details through Site Styles and a small Custom CSS layer. This keeps the page editable, responsive, accessible, and connected to Squarespace's form storage and analytics.

Do not paste the whole prototype into one Code Block. That route makes routine copy and layout edits harder, weakens native form behavior, and creates more mobile-testing risk. Use Code Blocks only for isolated details that Fluid Engine cannot reproduce cleanly.

## Available build path in Codex

There is no dedicated Squarespace connector or installed Squarespace plugin. Codex can still build the page through controlled browser interaction with Squarespace's own editor.

The safe sequence is:

1. Farrice opens the correct Squarespace site and logs in directly. Credentials never enter the chat.
2. Farrice authorizes an unpublished build.
3. Codex creates a new page outside the live navigation, recreates the approved design with native blocks, connects the Form Block, and applies the bounded CSS layer.
4. Farrice and Acusio review the unpublished URL on desktop and mobile.
5. Publication, homepage replacement, redirects, navigation changes, and domain changes remain separate approval steps.

Browser access makes the build executable; it does not remove Squarespace's normal editor or approval boundaries.

## The page to build first

Create one unpublished homepage that can also function as the coaching sales page. Do not rebuild every legacy page before this page proves the direction.

Use `RECOMMENDED-HOMEPAGE-V2-CONVERSION.md` for the current copy pass. Keep the earlier files as version history until Acusio approves the direction.

## Page order

| Section | Purpose | Squarespace treatment |
|---|---|---|
| Header | Make Acusio and the action unmistakable | Wordmark left, four links, gold CTA right; compact sticky header |
| Hero | Clarify service, location, and result | Split layout with real coaching image; one primary button; no autoplay video |
| Problem | Show that Acusio understands the buyer | Short text block with one supporting candid image |
| Difference | Explain why generic plans fail and why coaching helps | Two-column text section; no icons |
| Coaching | Make Acusio's adaptive coaching tangible | Bone-background split section with short paragraphs |
| Proof | Replace brand claims with client experience | One large quote, two smaller quotes; use real names only |
| Fit | Qualify the prospect before the form | Two-column text section; strong-fit and poor-fit language |
| Process | Reduce uncertainty | Three simple steps with restrained numbering |
| About | Transfer trust to Acusio the person | Portrait or in-session image, 120 words maximum |
| Culture | Seed the metal community and future gym | Full-width poster-like section; future tense must remain explicit |
| Final CTA | Convert interest into an inquiry | Short form or booking link; repeat availability language |
| Footer | Close cleanly | Name, service area, Instagram, privacy, copyright |

## Visual direction

### Palette

- **Matte black:** `#0B0B0B`
- **Warm charcoal:** `#1A1917`
- **Bone:** `#EEE7D8`
- **Brass gold:** `#B58A3A`
- **Oxblood accent:** `#6D1F1C`, used sparingly

Gold should behave like metal under stage light, not like luxury-business decoration. Bone carries most body text so the page does not become a black rectangle.

### Type

- Display: a condensed sans with poster weight, such as **Anton**, **Bebas Neue**, or **Oswald**
- Body and controls: **Inter**, **Source Sans 3**, or the closest clean Squarespace system font
- Avoid blackletter for paragraphs, buttons, or navigation
- Use all caps only for small labels and short display lines

### Photography

Prioritize, in order:

1. Acusio actively coaching a client
2. A direct portrait in the real training environment
3. Hands, equipment, chalk, plates, and ordinary signs of work
4. A candid human moment after or between sets

Do not use abstract lions, generic executives, synthetic bodies, empty luxury gyms, or staged trauma imagery. If the existing professional photo set is unavailable, use one honest current image and controlled typography before reaching for stock.

### Graphic language

- Band-poster hierarchy without concert-poster clutter
- Thin brass rules, oversized section numbers, subtle grain
- Slightly imperfect crops and asymmetry
- Clean forms and buttons so the cultural layer never hurts usability
- Motion limited to quick fades or image reveals; no parallax spectacle

## Mobile rules

- Put service and location above the first button
- Keep the first CTA visible without scrolling past a video
- Minimum 17px body copy and 48px tap targets
- Show the strongest client quote first
- Crop faces and coaching action intentionally at mobile width
- Use a sticky mobile CTA only after the first proof block
- Test the inquiry path on a real phone before publication

## Current-site migration

### Replace on launch

- The Resurrection Coach logo and descriptor
- Executive Health & Performance positioning
- Promotional bar
- Audit CTA and audit pricing
- Trauma-led home copy
- Generic executive and machinery metaphors

### Preserve until approved

- Existing pages and URLs
- Search metadata needed for redirects
- Original testimonial source records
- Form submissions and analytics history

### Recommended redirect map after review

| Current path | Proposed destination | Status |
|---|---|---|
| `/` | New homepage | Ready after approval |
| `/briefing` | New inquiry or coaching section | Pending CTA decision |
| `/the-protocol` | New coaching section | Pending final offer details |
| `/resurrections` | `/results` | Pending proof-page rewrite |
| `/the-series` | Archive or retained story page | Client decision required |
| Trauma-led articles | Preserve, noindex, or archive individually | Client decision required |

Do not bulk-delete legacy pages. The identity is changing quickly; preservation makes rollback and selective reuse possible.

## Form fields

Keep the first inquiry light:

- Name
- Email
- Preferred contact method
- Training location or neighborhood
- What would you like help with?
- What has made that difficult so far?
- Preferred training times

Avoid a long diagnostic application until Acusio confirms that he needs stronger qualification.

## Launch checklist

- [ ] Acusio approves Direction A, Direction B, or the recommended hybrid
- [ ] Location and radius confirmed
- [ ] Availability confirmed
- [ ] CTA destination works
- [ ] Pricing decision made
- [ ] Hero and proof images approved
- [ ] Testimonial names and excerpts approved
- [ ] Old navigation hidden, not deleted
- [ ] Redirects reviewed
- [ ] Mobile page checked on iPhone and Android-sized screens
- [ ] Form submission tested end to end
- [ ] Page title, meta description, favicon, and social-share image updated
- [ ] Final Squarespace preview approved before publication
