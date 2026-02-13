---
description: Generate a high-fidelity "Rank and Rent" website asset with elevated copy and visuals.
---

# ⚠️ This workflow has been ELEVATED to use Agentic Research and AI-generated visuals.

## Phase 1: Gather Inputs
Ask the user for:
- **Niche** (e.g., "Emergency Plumber", "Solar Installation")
- **City** (e.g., "Seattle", "Austin")
- **Brand Name** (e.g., "Seattle Rapid Flow")

## Phase 2: Agentic Research (OPTIONAL but Recommended)
Before generating, perform quick research to ground the copy in real data.

Use `search_web` to find:
1. **Local Competitors**: `"[Niche] [City]"` → Note their weaknesses (slow response, no reviews).
2. **Unique Selling Point**: What can this site claim that competitors can't? (24/7 service, specific area coverage)
3. **FAQs**: `"[Niche] [City] questions"` OR check "People Also Ask" in search results.

Create a `researched_data` dictionary:
```python
researched_data = {
    'unique_selling_point': "Only 24/7 licensed plumber serving Ballard & Fremont",
    'local_proof': "Trusted by 847 Seattle families (4.9★ on Google)",
    'response_time': "45 minutes",
    'competitors_weakness': "Top competitor has 3.2 stars and no after-hours service",
    'faqs_from_research': [
        {'question': "...", 'answer': "..."}
    ]
}
```

## Phase 3: Generate Premium Visuals (OPTIONAL but Recommended)
Use the `generate_image` tool to create unique visuals instead of stock photos.

**Hero Image Prompt** (Oren "Taste Mastery" style):
```
Professional [Niche] technician at work in a [City] home.
Clean uniform with company logo, modern equipment, warm lighting.
High-end architectural photography style, 8K, photorealistic.
The worker is focused, competent, trustworthy.
No text, no logos, no watermarks.
```

**About Image Prompt**:
```
Team of [Niche] professionals standing in front of their branded work van.
Clean uniforms, friendly expressions, [City] neighborhood visible in background.
Natural daylight, candid but professional pose.
```

Save generated images and note their paths.

## Phase 4: Generate the Site
Run the generator with the researched data:
```bash
python3 skills/asset_generator/generator.py \
    --niche "[Niche]" \
    --city "[City]" \
    --brand "[Brand Name]"
```

> **Note**: The current generator.py reads from content_engine and visual_engine.
> For full research integration, the Agent should manually call the engines with
> the researched data and then render the template, OR modify generator.py to
> accept a JSON file with researched_data.

## Phase 5: Deliver
- Provide the user with the file path: `skills/asset_generator/_site/index.html`
- Offer to:
  1. Preview the site in a browser
  2. Generate AI visuals to replace placeholders
  3. Deploy to Netlify/Vercel
  4. Generate another asset

## Elevation Notes
This workflow now applies:
- **Harry Dry "Concrete Copy"**: Specificity over vagueness (e.g., "45 mins" not "fast")
- **Oren "Taste Mastery"**: Premium AI visuals, not generic stock photos
- **Agentic Research**: Grounded in local competitor analysis when used with research phase
