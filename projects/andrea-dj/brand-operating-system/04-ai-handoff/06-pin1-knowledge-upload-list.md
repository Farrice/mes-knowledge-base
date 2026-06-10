# PIN 1 — Knowledge Upload List

*Paste the file list below into PIN 1's knowledge file uploads in Claude Projects settings. These 8 files give Front-of-House everything it needs to JUDGE (admission triage) and VOICE (message composition).*

---

## Files to Upload (in this order)

### Tier 1 — The Constitution (Already in Custom Instructions, but uploaded for search/reference)

1. **projects/andrea-dj/brand-operating-system/04-ai-handoff/03-constitution-core.md**
   - Movement 1 (Scene), Movement 2 (Flinch), Movement 3 (Gate), the 12, Living Ledger
   - *Why*: Ground truth for every decision

### Tier 2 — Triage & Curation

2. **projects/andrea-dj/brand-operating-system/00-foundation/05-non-negotiables.md**
   - The 12 verbatim (redundant with CONSTITUTION-CORE, but isolated for grep/search)
   - *Why*: When PIN 1 says "that's line X," it quotes this file

3. **projects/andrea-dj/brand-operating-system/05-ops/03-drift-signals.md**
   - Early-warning indicators: when a sponsor, venue, or submission is drifting
   - *Why*: Helps PIN 1 recognize what's wrong before Andrea even asks

### Tier 3 — Voice & Messaging

4. **projects/andrea-dj/brand-operating-system/00-foundation/03-voice-document.md**
   - 6 patterns, 10 rules, 46 GOOD/BAD pairs, 23 banned moves
   - *Why*: When PIN 1 composes a message (VOICE mode), it lives in Andrea's voice using these patterns

5. **projects/andrea-dj/brand-operating-system/00-foundation/04-positioning-one-pager.md**
   - One-paragraph positioning, positioning map, differentiation
   - *Why*: When triaging a venue pitch or sponsor, PIN 1 knows what Resonance is *not*

### Tier 4 — Briefs & Context (Optional, for richness)

6. **projects/andrea-dj/brand-operating-system/02-briefs/press-one-sheeter.md**
   - Press reply template + key talking points
   - *Why*: If Andrea gets a media inquiry, PIN 1 can draft a response

7. **projects/andrea-dj/brand-operating-system/02-briefs/venue-pitch.md**
   - Venue pitch structure + red flags
   - *Why*: When a venue comes calling, PIN 1 knows what the ask is and what we won't negotiate

### Tier 5 — Visual (If Needed for Context)

8. **projects/andrea-dj/brand-operating-system/01-visual/DESIGN.md**
   - Visual identity, color, typography, image style
   - *Why*: If Andrea needs to describe the visual system to a designer or venue, PIN 1 can reference it

---

## Upload Instructions

1. **Format**: Copy the absolute file path (e.g., `/Users/farricecain/Google Antigravity/projects/andrea-dj/brand-operating-system/...`)
2. **Method**: In Claude Projects, click **Knowledge** → **Upload Files** → paste the file paths one by one OR drag-and-drop the files
3. **Order**: Upload in the order above (Constitution first, then Triage, then Voice)
4. **Verify**: After upload, test one of the 8 voice-test inputs to confirm the files loaded

---

## Why This List (Not More)

PIN 1 is a **dispatcher**, not a full content studio. It:
- **JUDGES**: Is this person/sponsor in? (needs the 12, drift signals, positioning)
- **VOICES**: What should I say to them? (needs voice doc, positioning, maybe press template)

It does NOT:
- Create full social content (that's PIN 3 — THE FLOOR, which loads more)
- Plan full marketing campaigns (that's for PIN 4 — THE BOOTH, or a dedicated strategy room)
- Generate images (that's a design-system task; front-of-house routes to it)

**Smaller knowledge load = faster responses, clearer focus.** If Andrea opens PIN 1 and files are slow, quality drops.

---

## If You Add More Files Later

Do not bulk-upload. Test each file first:
1. Upload one file
2. Run one voice-test input
3. If it improves the answer (makes PIN 1 smarter without bloating), keep it
4. If it adds noise, remove it

The living ledger grows post-event, not pre-launch. Let the floor write the instructions.

