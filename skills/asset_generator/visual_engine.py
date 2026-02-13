"""
Visual Engine v2.0 - Elevated with "Taste Mastery" Principles (Oren)

This engine handles visual assets for Rank & Rent sites.

ARCHITECTURE NOTE (v2.0):
The Agent should use the `generate_image` tool to create unique, premium visuals
BEFORE calling the generator. This engine provides fallback URLs and guidance
for the Agent's image generation prompts.

Oren's "Taste Mastery" Principles Applied:
1. Premium over generic (no obvious stock photos)
2. Authentic over polished (real work environments)
3. Trust signals (uniforms, trucks, clean equipment)
"""

def get_visual_assets(niche: str, city: str, generated_images: dict = None):
    """
    Returns visual asset URLs for the site.
    
    Args:
        niche: The service niche
        city: The target city
        generated_images: (Optional) Dictionary with AI-generated image paths.
            Expected keys:
            - 'hero_image': Path to generated hero image
            - 'about_image': Path to generated about section image
            - 'service_images': List of paths for service cards
    
    Returns:
        Dictionary with image URLs for the template.
    """
    
    if generated_images:
        # Use AI-generated images if the Agent provided them
        return {
            'hero_image_url': generated_images.get('hero_image', get_fallback_hero(niche)),
            'about_image_url': generated_images.get('about_image', get_fallback_about(niche)),
            'service_images': generated_images.get('service_images', get_fallback_services(niche))
        }
    else:
        # Fallback to Unsplash (acceptable for MVP speed)
        return {
            'hero_image_url': get_fallback_hero(niche),
            'about_image_url': get_fallback_about(niche),
            'service_images': get_fallback_services(niche)
        }


def get_fallback_hero(niche: str) -> str:
    """Returns a high-quality Unsplash URL for the hero section."""
    query = niche.lower().replace(" ", ",")
    return f'https://source.unsplash.com/1600x900/?{query},professional,work'


def get_fallback_about(niche: str) -> str:
    """Returns a high-quality Unsplash URL for the about section."""
    query = niche.lower().replace(" ", ",")
    return f'https://source.unsplash.com/800x600/?{query},team,worker'


def get_fallback_services(niche: str) -> list:
    """Returns a list of Unsplash URLs for service cards."""
    query = niche.lower().replace(" ", ",")
    return [
        f'https://source.unsplash.com/400x300/?{query},emergency',
        f'https://source.unsplash.com/400x300/?{query},residential,home',
        f'https://source.unsplash.com/400x300/?{query},commercial,business'
    ]


def get_image_generation_prompts(niche: str, city: str) -> dict:
    """
    Returns optimized prompts for the Agent to use with generate_image tool.
    
    Follows Oren's "Taste Mastery" principles:
    - Premium, not stock-photo generic
    - Authentic work environments
    - Trust signals (uniforms, branded trucks, clean equipment)
    """
    
    return {
        'hero_prompt': f"""
            Professional {niche} technician at work in a {city} home.
            Clean uniform with company logo, modern equipment, warm lighting.
            High-end architectural photography style, 8K, photorealistic.
            The worker is focused, competent, trustworthy.
            No text, no logos, no watermarks.
        """.strip(),
        
        'about_prompt': f"""
            Team of {niche} professionals standing in front of their branded work van.
            Clean uniforms, friendly expressions, {city} neighborhood visible in background.
            Natural daylight, candid but professional pose.
            Inspires trust and local connection.
        """.strip(),
        
        'service_prompts': [
            f"Emergency {niche} job at night, professional technician with headlamp, dramatic lighting, {city} home",
            f"Residential {niche} work in a modern kitchen, clean workspace, homeowner in background looking satisfied",
            f"Commercial {niche} job in a {city} office building, professional equipment, minimal disruption to workers"
        ]
    }


# For Agent reference: How to use generate_image with these prompts
AGENT_INSTRUCTIONS = """
## How to Generate Premium Visuals for a Rank & Rent Site

Before running the generator, use the `generate_image` tool with these prompts:

1. **Hero Image**:
   ```
   generate_image(
       Prompt=get_image_generation_prompts(niche, city)['hero_prompt'],
       ImageName="hero_[brand]"
   )
   ```

2. **About Image**:
   ```
   generate_image(
       Prompt=get_image_generation_prompts(niche, city)['about_prompt'],
       ImageName="about_[brand]"
   )
   ```

3. **Service Images**: Generate 3 images using the `service_prompts` list.

4. Pass the generated image paths to `generator.py` via the `--images` flag or
   modify the call to `get_visual_assets()` with the `generated_images` dict.
"""
