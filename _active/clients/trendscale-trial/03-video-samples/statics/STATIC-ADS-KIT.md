# Static Ads Kit - JCKED + Puravita

Four statics per brand, each extending the briefed concept exactly. Prompts are GPT Image 2.0 Format A (structured JSON) per `skills/gpt-image-2-director/SKILL.md` - every region named, real overlay text embedded in quotes. Formats pulled from the Dara Denney 7-archetype system: educational infographic, comparison/us-vs-them, headliner, product-hero + offer callout. Prompt-only, $0 spend, nothing rendered.

All eight briefs pass the 60-second execution test: a designer or AI render tool can build the ad from the card alone, no follow-up questions.

---

## JCKED - Liquid L-Carnitine 4000mg

Palette: dark navy + brushed steel, amber accent reserved for the enzyme name and dose numbers only. Editorial, not gym-bro. No before/after, no scales, no doctors, no urgency. "Top of the studied range," never "the clinical dose."

### JCKED Ad 1 - The CPT-1 Cutaway (educational infographic)

**Format:** Educational infographic, mechanism diagram. 4:5 (1080x1350) primary. 1:1 crop-safe: keep headline and the lock-cutaway centered inside the middle 1080x1080 - the annotation labels sit closest to the crop edges and are the first thing lost.

**Overlay copy:**
- Headline (53 chars): "One enzyme decides if your fat burns or stays locked."
- Support (80 chars): "CPT-1 is the lock. L-carnitine is the key. Without it, stored fat does not move."
- CTA (30 chars): "See the mechanism at jcked.com"

**GPT Image 2 prompt:**
```json
{
  "type": "editorial infographic, cutaway diagram",
  "style": "dark navy and brushed steel palette, single warm amber accent light, editorial magazine restraint, clean vector-realist rendering, no gym or fitness cliché imagery, typography feel of Inter Tight or Sohne",
  "background": "solid dark navy #0d1420, faint steel brushed-metal texture",
  "layout": {
    "header": {
      "position": "top-center",
      "text": "One enzyme decides if your fat burns or stays locked.",
      "style": "large bold Inter Tight, white, tight tracking, two lines max"
    },
    "centerpiece": {
      "position": "center",
      "subject": "cutaway cross-section of a steel vault door revealing an internal lock mechanism, the lock face engraved 'CPT-1' in amber glowing letters, a single brass key mid-turn inside it labeled 'L-carnitine' on a small steel tag",
      "lighting": "single amber light source from inside the mechanism, rest of scene in cool steel shadow"
    },
    "annotations": {
      "count": 2,
      "items": ["thin amber leader line to the lock, label 'the lock' in small caps", "thin amber leader line to the key, label 'the key' in small caps"]
    },
    "footer": {
      "position": "bottom-center",
      "support_text": "CPT-1 is the lock. L-carnitine is the key. Without it, stored fat does not move.",
      "cta": "See the mechanism at jcked.com",
      "style": "small caps Inter Tight, white on navy bar"
    }
  }
}
```

**Product-fidelity note:** No bottle in this card, so no compositing needed; if a bottle is later added to this frame, pull the real photo from jcked.com/products/liquid-l-carnitine-4000mg rather than let the model invent a label.

### JCKED Ad 2 - The Two Keys (comparison / us-vs-them)

**Format:** Comparison callout. 4:5 (1080x1350) primary. 1:1 crop-safe: both keys and the divider must stay inside the center 1080x1080 - the dose labels are the first casualty on a tight crop.

**Overlay copy:**
- Headline (59 chars): "Most carnitine products stop at 500mg. A fraction of a key."
- Support (97 chars): "JCKED carries 4,000mg, the top of the studied range in a 2023 review of 37 trials, 2,000+ people."
- CTA (37 chars): "Get the full key. $49.95 at jcked.com"

**GPT Image 2 prompt:**
```json
{
  "type": "comparison infographic, us vs them",
  "style": "dark navy and brushed steel, amber accent reserved for the two dose numbers only, editorial and restrained, Inter Tight or Sohne typography",
  "background": "dark navy #0d1420, vertical steel divider line down the center",
  "layout": {
    "header": {
      "position": "top-center",
      "text": "Most carnitine products stop at 500mg. A fraction of a key.",
      "style": "bold Inter Tight, white, two lines"
    },
    "left_panel": {
      "position": "mid-left",
      "subject": "a short stub key, clearly cut too short to reach a lock, resting on dark steel",
      "label": "500mg - most brands",
      "label_color": "amber"
    },
    "right_panel": {
      "position": "mid-right",
      "subject": "a full-length brass key, fully cut, resting on dark steel, subtly larger and more defined than the left key",
      "label": "4,000mg - JCKED",
      "label_color": "amber"
    },
    "footer": {
      "position": "bottom-center",
      "support_text": "JCKED carries 4,000mg, the top of the studied range in a 2023 review of 37 trials, 2,000+ people.",
      "cta": "Get the full key. $49.95 at jcked.com",
      "style": "small caps Inter Tight, white on navy bar"
    }
  }
}
```

**Product-fidelity note:** Keys are illustrative props, not the bottle, so no PDP compositing required for this frame.

### JCKED Ad 3 - "That Fat Is Locked" (headliner, verbatim hook)

**Format:** Headliner, text-led. 4:5 (1080x1350) primary. 1:1 crop-safe: the headline sits dead-center and survives any crop; keep support/CTA close enough to center that a square crop doesn't clip them.

**Overlay copy:**
- Headline (19 chars): "That fat is locked."
- Support (89 chars): "The effort was never the problem. CPT-1 holds the door shut until the right key turns it."
- CTA (26 chars): "Open the lock. Shop JCKED."

**GPT Image 2 prompt:**
```json
{
  "type": "headline-led editorial poster",
  "style": "dark navy and brushed steel, one amber accent word, Ogilvy-style headliner restraint, Inter Tight or Sohne bold typography, message is the focal point",
  "background": "dark navy, a closed steel vault door faint and out of focus behind the text, single dim amber light bleeding from its seam",
  "layout": {
    "headline": {
      "position": "center",
      "text": "That fat is [locked].",
      "style": "very large bold Inter Tight, white, the word 'locked' rendered in amber, rest of headline white",
      "note": "render literal text 'That fat is locked.' with only the word locked in amber"
    },
    "support": {
      "position": "below headline, mid-lower-center",
      "text": "The effort was never the problem. CPT-1 holds the door shut until the right key turns it.",
      "style": "small regular Inter Tight, steel gray"
    },
    "footer": {
      "position": "bottom-center",
      "cta": "Open the lock. Shop JCKED.",
      "style": "small caps, white, thin underline in amber"
    }
  }
}
```

**Product-fidelity note:** No product shown; pure headline card, no compositing needed.

### JCKED Ad 4 - The Key Now Fits (product-hero + offer)

**Format:** Product-hero + offer card. 4:5 (1080x1350) primary. 1:1 crop-safe: keep the bottle and price badge inside the center 1080x1080; the guarantee ribbon is the first element a square crop should be allowed to trim.

**Overlay copy:**
- Headline (26 chars): "The key, cut to your lock."
- Support (92 chars): "First bottle $49.95. Backed by a 365-day guarantee, full refund even if the bottle is empty."
- CTA (31 chars): "Shop the full dose at jcked.com"

**GPT Image 2 prompt:**
```json
{
  "type": "product hero ecommerce ad card",
  "style": "dark navy and brushed steel palette, amber accent on the enzyme/dose callouts only, editorial product photography lighting, Inter Tight or Sohne typography",
  "background": "steel vault door swung open onto warm amber light, dark navy shadow at the frame edges",
  "layout": {
    "header": {
      "position": "top-center",
      "text": "The key, cut to your lock.",
      "style": "bold Inter Tight, white"
    },
    "centerpiece": {
      "position": "center",
      "subject": "PLACEHOLDER for real JCKED liquid L-carnitine 4000mg bottle product photo, composited in post, standing in the warm light where the vault lock used to be",
      "note": "render a generic amber-liquid dropper bottle silhouette here as a stand-in; do not invent brand label text"
    },
    "offer_badge": {
      "position": "bottom-left",
      "text": "$49.95 first bottle",
      "style": "small steel card, white text, amber border"
    },
    "guarantee_ribbon": {
      "position": "bottom-right",
      "text": "365-DAY GUARANTEE",
      "style": "small steel card, amber text"
    },
    "footer": {
      "position": "bottom-center",
      "support_text": "First bottle $49.95. Backed by a 365-day guarantee, full refund even if the bottle is empty.",
      "cta": "Shop the full dose at jcked.com"
    }
  }
}
```

**Product-fidelity note:** GPT Image 2 will not reproduce the real JCKED bottle label. Render the placeholder silhouette, then composite the actual product photo from jcked.com/products/liquid-l-carnitine-4000mg in post before this ad ships.

---

## Puravita - Magnesium Complex (12-form)

Palette: quiet, muted, NYT-Magazine restraint, sage accent reserved for callouts. Never diagnose the viewer, no disease or treatment language, no doctors, no urgency, no stock tired-person footage.

### Puravita Ad 1 - The Battery the Blood Test Can't See (educational infographic)

**Format:** Educational infographic, split mechanism diagram. 4:5 (1080x1350) primary. 1:1 crop-safe: keep both the phone and the lab-report panel inside the center 1080x1080 - the sage annotation is the first casualty on a tight crop.

**Overlay copy:**
- Headline (49 chars): "Your phone warns you at 5%. Your body never does."
- Support (111 chars): "A standard blood test sees under 1% of the magnesium in your body. The other 99% runs you from bone and muscle."
- CTA (25 chars): "See what the test misses."

**GPT Image 2 prompt:**
```json
{
  "type": "editorial infographic, split diagram",
  "style": "quiet muted palette, warm neutral tones, NYT Magazine restraint, sage green reserved for the callout labels only, Inter Tight or Sohne typography, no clinical or diagnostic imagery",
  "background": "soft warm-gray gradient, minimal shadow",
  "layout": {
    "header": {
      "position": "top-center",
      "text": "Your phone warns you at 5%. Your body never does.",
      "style": "bold Inter Tight, dark charcoal, two lines"
    },
    "left_panel": {
      "position": "mid-left",
      "subject": "a hand only, no face, holding a phone at dawn, screen reading 5 percent with a soft dim red pulse",
      "label": "5% and you know",
      "label_color": "sage"
    },
    "right_panel": {
      "position": "mid-right",
      "subject": "a plain lab report page on a kitchen table, one small green checkmark in the top corner, the rest of the page in soft shadow, unreadable",
      "label": "under 1% visible",
      "label_color": "sage"
    },
    "footer": {
      "position": "bottom-center",
      "support_text": "A standard blood test sees under 1% of the magnesium in your body. The other 99% runs you from bone and muscle.",
      "cta": "See what the test misses.",
      "style": "small regular Inter Tight, charcoal on soft-gray bar"
    }
  }
}
```

**Product-fidelity note:** No bottle in this frame; phone and lab report are illustrative props, no PDP compositing needed.

### Puravita Ad 2 - One Form vs Twelve (comparison / us-vs-them)

**Format:** Comparison callout. 4:5 (1080x1350) primary. 1:1 crop-safe: keep both capsule groupings and the divider inside center 1080x1080.

**Overlay copy:**
- Headline (48 chars): "One form covers one job. Your body needs twelve."
- Support (111 chars): "Most magnesium supplements carry a single form. Puravita carries all twelve, the forms your body actually uses."
- CTA (25 chars): "Start the 90-day. $39.99."

**GPT Image 2 prompt:**
```json
{
  "type": "comparison infographic",
  "style": "quiet muted palette, sage green reserved for checkmarks and callouts, NYT Magazine restraint, Inter Tight or Sohne typography",
  "background": "soft warm-white, thin vertical divider line down the center",
  "layout": {
    "header": {
      "position": "top-center",
      "text": "One form covers one job. Your body needs twelve.",
      "style": "bold Inter Tight, charcoal, two lines"
    },
    "left_panel": {
      "position": "mid-left",
      "subject": "a single small capsule icon, minimal line-art style, alone on the panel",
      "label": "1 form - most brands",
      "label_color": "muted gray"
    },
    "right_panel": {
      "position": "mid-right",
      "subject": {
        "count": 12,
        "layout": "grid of 12 small capsule icons, minimal line-art style, each with a tiny sage checkmark"
      },
      "label": "12 forms - Puravita",
      "label_color": "sage"
    },
    "footer": {
      "position": "bottom-center",
      "support_text": "Most magnesium supplements carry a single form. Puravita carries all twelve, the forms your body actually uses.",
      "cta": "Start the 90-day. $39.99.",
      "style": "small regular Inter Tight, charcoal on soft-white bar"
    }
  }
}
```

**Product-fidelity note:** Capsule icons are illustrative, not the bottle; no PDP compositing needed for this frame.

### Puravita Ad 3 - "The Battery You Can't See" (headliner, verbatim hook)

**Format:** Headliner, text-led. 4:5 (1080x1350) primary. 1:1 crop-safe: headline is dead-center and survives any crop; keep support/CTA close to center.

**Overlay copy:**
- Headline (26 chars): "The battery you can't see."
- Support (119 chars): "Magnesium powers over 600 reactions in your body. When it runs low, nothing alarms you. You just call it getting older."
- CTA (23 chars): "Start the 90-day today."

**GPT Image 2 prompt:**
```json
{
  "type": "headline-led editorial poster",
  "style": "quiet muted palette, NYT Magazine restraint, sage accent on one glowing element only, Inter Tight or Sohne bold typography, message is the focal point",
  "background": "soft dark warm-gray, a phone battery icon glowing dim in soft focus behind the headline, faint sage glow",
  "layout": {
    "headline": {
      "position": "center",
      "text": "The battery you can't see.",
      "style": "very large bold Inter Tight, off-white on dark warm-gray"
    },
    "support": {
      "position": "below headline, mid-lower-center",
      "text": "Magnesium powers over 600 reactions in your body. When it runs low, nothing alarms you. You just call it getting older.",
      "style": "small regular Inter Tight, muted gray"
    },
    "footer": {
      "position": "bottom-center",
      "cta": "Start the 90-day today.",
      "style": "small caps, off-white, thin sage underline"
    }
  }
}
```

**Product-fidelity note:** No product shown; pure headline card, no compositing needed.

### Puravita Ad 4 - Twelve Forms, One Battery (product-hero + offer)

**Format:** Product-hero + offer card. 4:5 (1080x1350) primary. 1:1 crop-safe: keep the bottle and offer badge inside the center 1080x1080.

**Overlay copy:**
- Headline (26 chars): "Twelve forms. One battery."
- Support (94 chars): "The label asks for 6 to 8 weeks. Start the 90-day and give it the runway. $39.99, buy 2 get 1."
- CTA (36 chars): "Start the 90-day at shoppuravita.com"

**GPT Image 2 prompt:**
```json
{
  "type": "product hero ecommerce ad card",
  "style": "quiet muted palette, sage accent on the offer badge only, NYT Magazine editorial product photography lighting, Inter Tight or Sohne typography",
  "background": "soft morning kitchen light, a phone in the background showing a full glowing battery icon, out of focus",
  "layout": {
    "header": {
      "position": "top-center",
      "text": "Twelve forms. One battery.",
      "style": "bold Inter Tight, charcoal"
    },
    "centerpiece": {
      "position": "center",
      "subject": "PLACEHOLDER for real Puravita Magnesium Complex bottle product photo, composited in post, standing in soft morning light",
      "note": "render a generic neutral supplement bottle silhouette here as a stand-in; do not invent brand label text"
    },
    "offer_badge": {
      "position": "bottom-left",
      "text": "90-day, $39.99",
      "style": "small soft-white card, charcoal text, sage border"
    },
    "footer": {
      "position": "bottom-center",
      "support_text": "The label asks for 6 to 8 weeks. Start the 90-day and give it the runway. $39.99, buy 2 get 1.",
      "cta": "Start the 90-day at shoppuravita.com"
    }
  }
}
```

**Product-fidelity note:** GPT Image 2 will not reproduce the real Puravita label. Render the placeholder silhouette, then composite the actual product photo from shoppuravita.com/products/puravita-magnesium-complex in post before this ad ships.

---

## QA Checklist

1. **Constraint compliance per brand** - JCKED: no before/after, no scales, no doctors, no urgency stinger, "top of the studied range" not "the clinical dose." Puravita: no diagnosis of the viewer, no disease/treatment language, no doctors, no urgency, no stock tired-person footage.
2. **No AI-slop phrases** - scanned against banned vocabulary (breathtaking, seamlessly, unlock, elevate, game-changer); none present in any headline, support line, or CTA.
3. **No em dashes** - every copy line checked; none used.
4. **Claim-safety** - every number traces to the brief: JCKED 4,000mg / 500mg / 2023 review / 37 trials / 2,000+ people / $49.95 / 365-day guarantee; Puravita 5% / under 1% / 99% / 600+ reactions / 12 forms / 6 to 8 weeks / $39.99 90-day / buy 2 get 1. No invented statistics.
5. **Text legibility at feed size** - headlines capped at 60 characters, support lines under 120, single focal point per card, no more than two type sizes competing for attention.
6. **Brand palette held** - JCKED stays dark navy/steel with amber reserved for enzyme name and dose numbers only; Puravita stays quiet and muted with sage reserved for callouts only. No cross-contamination between the two palettes.

## Which 2 to Send

**JCKED Ad 3, "That Fat Is Locked"** - the verbatim hook line is the single most-tested phrase in the brief's own script; a text-led headliner proves the concept survives without any diagram support, which is the strongest signal of concept strength.

**Puravita Ad 1, "The Battery the Blood Test Can't See"** - the mechanism card does the most work in one frame: it earns the analogy (phone at 5%) and the proof (blood test misses 99%) simultaneously, which is exactly what an unaware-to-problem-aware buyer needs before any offer lands.
