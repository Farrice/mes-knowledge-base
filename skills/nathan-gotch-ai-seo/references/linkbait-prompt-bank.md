# Linkbait Prompt Bank — Verbatim Prompts from the 2026-07-15 Video

Captured from screen at 1024px (frames at 15:40, 16:20, 16:35 — ledger:
`extractions/nathan-gotch/visual-context.md`). These are Gotch's actual working prompts.
Bracketed variables added for reuse; everything else is as-shown or faithfully reconstructed
from the visible screen text.

## 1. The Category Linkbait Ideation Prompt (15:40, ChatGPT)

As shown on screen (category templatized):

> We're trying to build topic authority for [CATEGORY, e.g. "best healthy beef jerky"], and we
> need to create informational content to build topic support for this topic. I wanted you to
> come up with some data-driven, statistics-driven ideas and other types of topics that would
> function well to attract backlinks naturally. They can be used in our outreach processes for
> PR and also angles that would do well for social media distribution. Give me 25 ideas.

Why it works (Gotch, 15:20): "If you come into ChatGPT and say 'give me link bait ideas' it's not
that useful. Even if you say 'oh, we're a beef jerky company, give us link bait ideas' — it's not
that useful. You want to get real focused on just that one category cuz you get way better ideas."
Grounding check (15:55): the model did research — ideas arrived with named data sources.

What a good response item looks like (verbatim shape from the screen, idea #1):
- **Named asset**: "The State of Healthy Beef Jerky Report"
- **Method**: analyze 100-250 products across Protein / Sodium / Added sugar / Saturated fat / Calories / Ingredient count / Price per ounce / Certifications and claims; publish annually with rankings, charts, downloadable data
- **PR hook**: "We analyzed 150 beef jerky products. Only X% met our healthy jerky criteria."
- **Why it attracts links**: becomes a primary-source benchmark journalists, dietitians, and other articles can reference
- **Data seed**: USDA FoodData Central branded-food and nutrition-label data

## 2. The Prioritization Move (16:15)

Not a prompt — a judgment step. From 25 ideas, name "the five I'd prioritize" (his picks: State
of the Category Report, Sodium Index, A Decade of Recalls, Healthy Halo Audit, Blind Taste Test).
Selection logic visible in the response: flagship industry report + newsworthy investigations +
one public-safety resource + one highly distributable social experiment; "the strongest structure
would be a single proprietary database powering the annual report, individual statistics pages,
rankings, comparison tools and recurring PR campaigns."

## 3. The Deep Research Handoff (16:17)

> [Chosen idea title] — Conduct deep research on this topic.

His run: 12m 10s. Then the QA layer — read the research's **"Important limitations"** section and
adopt the **most defensible lead statistic** as the headline claim (his: recalls → "recalls and
public health alerts"; lead stat: 72% of events came down to labels/allergens/inspection, not
pathogens). "Could you take this and just slap it on your website? Probably, but I wouldn't
recommend that. I would just use the research and convert it into a very structured asset."

## 4. The Design-Agent Bridge Prompt (17:04)

> Create a prompt for my design agent for the visual assets to support this data-driven study.

Then paste the generated design prompt into the design agent (he used Claude design) unedited —
"I didn't do anything wild. I just [pasted] the exact prompt in here… It asked some clarifying
questions. I literally just skipped them… and I just let it cook."

The generated design brief's load-bearing elements (visible 17:06-17:50):
- Complete asset system, not one image: hero 1600×900 + OG 1200×630 + mobile 1080×1350, key-findings summary card, cause-breakdown donut, ten-year timeline, U.S. tile map, explainer cards, full 1200px infographic with methodology + limitations
- "Use the website's existing typography, colors, logo, and design system"
- Tone guardrail: "should feel like a serious consumer research report, not a sensational food-scare campaign"
- ALT TEXT specified per asset

## 5. The Edit Doctrine (18:10)

"This is not going to be perfect out of the gate… you can dig into this and start to just focus
on editing. These days the key to using AI is you don't ever need to start with a blank canvas
basically ever. The magic is in the edit. This is even before AI — the magic of writing was
always in the edit… true with design, it's true with AI content, it's true with AI coding."
Edit pass = hallucination check + refinement inside the brand system; human hours land here.
