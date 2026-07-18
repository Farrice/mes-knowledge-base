---
description: Transform property listings from boring billboards into signature-format showcases that sell lifestyle
---

# /enrico-listing — Listing Showcase System

Transform any property listing from a "billboard" (static photo + price) or "lazy reel" (photo + trending audio) into a signature-format showcase that sells LIFESTYLE, not specs. Produces ready-to-film scripts for any listing.

## Usage

```
/enrico-listing [property description or MLS link]
```

Examples:
- `/enrico-listing "4bd/3ba in Palmdale, 2,200 sqft, pool, $650K"`
- `/enrico-listing "luxury condo downtown LA, 2bd penthouse"`
- `/enrico-listing [paste MLS description]`

## Context Loading

// turbo-all

Before executing, read:
1. `skills/enrico-incarnati-instagram-realestate/genius.md` — Patterns 1, 2, 3, 8
2. `skills/enrico-incarnati-instagram-realestate/references/content-expansion-templates.md`

## Steps

### Step 1: Listing Intelligence Gathering

```
LISTING PROFILE
───────────────
Address/Area: [Location]
Price: [Price]
Specs: [Beds/Baths/SqFt/Lot]
Top Features: [Pool, view, kitchen, garage, etc.]
Target Buyer: [Who would buy this — families, DINKs, investors, downsizers]
Neighborhood Vibe: [What's nearby, walkability, school district, lifestyle]
Unique Angle: [What makes this home different from every other listing?]
Agent's Signature Format: [From /enrico-format — what's their recurring format?]
```

### Step 2: Anti-Billboard Audit

Check if the current listing content plan falls into Incarnati's three anti-patterns:

```
❌ THE BILLBOARD: Are they just posting a photo with price + caption?
❌ THE DUMP: Are they posting a carousel of MLS photos with specs?
❌ THE LAZY REEL: Are they putting a photo on trending audio?

If YES to any → This listing needs the full treatment.
```

### Step 3: Lifestyle Translation

Transform specs into feelings:

```
LIFESTYLE TRANSLATION
─────────────────────
SPEC → LIFESTYLE

[4 bedrooms] → "Space for the kids to each have their own room + a home office for you"
[Pool] → "July 4th BBQs, teaching your kids to swim, 6 PM wine floats after a long day"
[Close to downtown] → "15-minute walk to your favorite restaurant. No DUI risk, just vibes"
[New kitchen] → "The kitchen where you finally host Thanksgiving YOUR way"
[Large garage] → "Room for your project car AND the family SUV"
[View] → "The coffee-on-the-balcony moment every morning"

KEY QUESTION: "If a buyer can't picture themselves getting coffee down the street or
walking their kids to the local school, they aren't going to buy the home."

What life moments does this home enable?
1. [Moment]
2. [Moment]
3. [Moment]
4. [Moment]
5. [Moment]
```

### Step 4: Multi-Format Listing Content

Generate 4 content pieces for the same listing:

#### Piece 1: Signature Format Application
```
Apply the agent's signature format to this listing.
If agent is @_jiing and her format is [TBD from /enrico-format]:
- How does the format's recurring element work in THIS specific home?
- What's the unique twist for this property?
- Script: [Full script using the format]
```

#### Piece 2: The Lifestyle Reel
```
LIFESTYLE REEL
──────────────
Hook (3 seconds): "[Lifestyle moment, not a spec]"
Example: "Imagine waking up to THIS every morning..."

FLOW:
Scene 1: [Opening shot — the best feature of the home filmed cinematically]
Scene 2: [The lifestyle moment — cooking in the kitchen, swimming in the pool]
Scene 3: [The neighborhood — walk to coffee, parks, schools]
Scene 4: [The money shot — the feature that sells this home]

Voiceover: "[Lifestyle narrative — what it FEELS like to live here]"

Music: [Recommend specific vibe — chill, upbeat, luxury]
Duration: 30-60 seconds
CTA: "DM me 'tour' if you want to see this in person"
```

#### Piece 3: Digital Clipboard — Listing Edition
```
DIGITAL CLIPBOARD — PROPERTY WALKTHROUGH
─────────────────────────────────────────
Video: Walk through the property
Overlay checklist shows KEY details buyers care about:

✅ [Beds/Baths]
✅ [Square footage]
✅ [Year built / renovated]
✅ [School district rating]
✅ [Property features — pool, garage, view]
✅ [Monthly estimated mortgage at current rates]
✅ [Distance to key amenities]
✅ [HOA fee if applicable]
✅ [What's included in the sale]
✅ [Open house date or showing availability]

CTA: "Comment 'details' for the full property sheet"
```

#### Piece 4: Neighborhood Context Piece
```
NEIGHBORHOOD INTEGRATION
────────────────────────
Don't just show the home — show the life around it.

SCRIPT:
"Before I show you inside [address], let me show you WHY this location matters..."
[Walk/drive to nearby coffee shop, park, school]
"You're 2 minutes from [Y], 5 minutes from [Z]..."
[Cut to inside the home]
"And then you come home to THIS."
[Show the best room/feature]

CTA: "Would you live here? Comment your [City] neighborhood below 👇"
```

### Step 5: Posting Strategy for This Listing

```
LISTING CONTENT SCHEDULE
────────────────────────
Day 1: Lifestyle Reel (discovery — catches attention on explore)
Day 2: Stories — behind-scenes of filming / sneak peek
Day 3: Signature Format piece (your audience already follows for this)
Day 4: Digital Clipboard (save-magnet — stays in collections)
Day 5: Neighborhood Context piece (proximity play — attracts local followers)

STORIES THROUGHOUT:
- "New listing alert — would you pay $[X] for this?"
- Poll: "Pool or no pool — what matters more?"
- "Taking you inside my latest listing today..."
```

### Step 6: Deliverable

Produce a conversation artifact containing:
1. Listing intelligence profile
2. Anti-billboard audit result
3. Lifestyle translation (specs → feelings)
4. All 4 content scripts (ready to film)
5. Posting schedule
6. Thumbnail/cover suggestions
7. ManyChat keywords + auto-DM templates for this listing

---

## Output Schema

The final deliverable is a single artifact with these required fields:

```
- listing_profile: { address_area, price, specs, top_features, target_buyer, neighborhood_vibe, unique_angle, signature_format }
- anti_billboard_audit: explicit YES/NO on Billboard / Dump / Lazy Reel collision
- lifestyle_translation_table: minimum 5 rows, spec → feeling (each feeling names an actual moment, not an adjective)
- four_content_scripts: Signature Format Application, Lifestyle Reel, Digital Clipboard (Listing Edition),
  Neighborhood Context Piece — each a full script (hook/scenes/voiceover/CTA), not an outline
- posting_schedule: 5-day sequence with stated reason for each day's placement
- manychat_config: keyword + auto-DM template specific to THIS listing
```

## Quality Gate

Before delivering, verify:
1. **Lifestyle translation names a moment, not an adjective.** "Pool → great for entertaining" fails; "Pool → July 4th BBQs, teaching your kids to swim, 6 PM wine floats after a long day" (the source's own example) is the bar. Per the core principle: "If a buyer can't picture themselves getting coffee down the street or walking their kids to the local school, they aren't going to buy the home."
2. **The Anti-Billboard Audit is honest, not a formality.** If the described content plan is "post a listing photo with price and specs in caption," it must be flagged YES on Billboard and the deliverable must show the corrected version — not silently skip past it.
3. **Signature Format Application is agent-specific, not generic.** This piece must reuse the actual format discovered in `/enrico-format` for this agent (e.g., the golf-putter walkthrough) — if no format exists yet, the deliverable must say so explicitly rather than inventing a placeholder.
4. **Digital Clipboard checklist items are buyer-specific to this listing**, not the generic "12 things to check" template reused verbatim — HOA fee, school rating, and mortgage estimate should reflect this property's actual numbers where given.
5. **Recognition check**: would Enrico Incarnati recognize this as "selling the lifestyle around the home," per his stated principle — or does it read as a standard MLS listing dressed up with a video script?

---

## Stacking Chains

- **Requires**: `/enrico-format` completed first (need the signature format)
- **Compound with Luke Iha** → Write vicious hooks for each content piece
- **Compound with Eric Roth** → Add cinematic narrative structure to the lifestyle reel
- **After posting** → Track performance and feed into `/enrico-expand` for winning format amplification
