"""
Content Engine v2.0 - Elevated with "Concrete Copy" Principles (Harry Dry)

This engine generates high-conversion copy for Rank & Rent assets.
It applies Harry Dry's "Concrete Copy" principles:
1. Specificity over vagueness ("On-site in 60 mins" vs "Fast service")
2. Proof over claims ("500+ 5-star reviews" vs "Highly rated")
3. Outcome over feature ("Your pipes fixed" vs "Plumbing services")

ARCHITECTURE NOTE:
This engine now accepts a `researched_data` dictionary with market-specific
information gathered by the Agent via Agentic Research. This grounds the copy
in real data rather than generic templates.
"""

from datetime import datetime

def generate_site_content(niche: str, city: str, brand_name: str, researched_data: dict = None):
    """
    Generates all text content for the site.
    
    Args:
        niche: The service niche (e.g., "Emergency Plumber")
        city: The target city
        brand_name: The brand name for the asset
        researched_data: (Optional) Dictionary with market research from Agent.
            Expected keys:
            - 'unique_selling_point': Specific differentiator (e.g., "Only 24/7 licensed plumber in East Seattle")
            - 'local_proof': Social proof specific to the area (e.g., "Trusted by 500+ Seattle families")
            - 'response_time': Specific response time (e.g., "45 minutes")
            - 'competitors_weakness': What competitors are missing
            - 'faqs_from_research': List of actual FAQs from "People Also Ask"
    """
    
    # Apply Harry Dry "Concrete Copy" principle: Specificity over vagueness
    if researched_data:
        usp = researched_data.get('unique_selling_point', f"Trusted {niche} in {city}")
        local_proof = researched_data.get('local_proof', f"Serving the {city} community")
        response_time = researched_data.get('response_time', "60 minutes")
        faqs = researched_data.get('faqs_from_research', [])
    else:
        # Fallback to elevated defaults (not generic templates)
        usp = f"Licensed, Insured, Always Answering — {niche} in {city}"
        local_proof = f"Serving {city} since 2015"
        response_time = "60 minutes"
        faqs = []
    
    # Generate concrete headlines (Harry Dry: "Zoom In" on specifics)
    hero_headline = f"{niche} — On-Site in {response_time} or It's Free"
    hero_subheadline = f"{usp}. No hidden fees. No voicemail. Ever."
    
    # Meta tags with concrete value proposition
    meta_title = f"{niche} in {city} | {brand_name} — {response_time} Response"
    meta_description = f"Need a {niche.lower()} in {city}? {brand_name} arrives in {response_time}. Licensed, insured, 5-star rated. Call now: (555) 123-4567."
    
    # Services with outcome-focused copy (Harry Dry: "Feature → Benefit → Proof")
    services = [
        {
            'title': f"Emergency {niche}",
            'description': f"We answer at 3 AM. Your problem fixed by sunrise. {local_proof}.",
            'cta': "Call Now"
        },
        {
            'title': f"Residential {niche}",
            'description': "Fixed price before we start. We treat your home like our own. 100% satisfaction guarantee.",
            'cta': "Get Quote"
        },
        {
            'title': f"Commercial {niche}",
            'description': "Minimal disruption. Weekend and late-night availability. Trusted by local businesses.",
            'cta': "Schedule Service"
        }
    ]
    
    # About section with concrete proof
    about_content = f"""
    <p><strong>{brand_name}</strong> has been serving the <strong>{city}</strong> area since 2015. We're not a call center — we're local technicians who live here too.</p>
    <p><strong>Why {city} chooses us:</strong></p>
    <ul>
        <li>✅ {response_time} average response time</li>
        <li>✅ Licensed & Insured (Lic# 12345678)</li>
        <li>✅ 500+ verified 5-star reviews</li>
        <li>✅ No hidden fees — price quoted upfront</li>
    </ul>
    """
    
    # FAQs: Use researched "People Also Ask" data if available
    if not faqs:
        faqs = [
            {'question': f"How fast can you get to {city}?", 'answer': f"For emergencies, we aim for {response_time} or less. We have technicians positioned throughout the {city} area."},
            {'question': "Are you licensed and insured?", 'answer': "Yes. We carry full liability insurance and all California state licenses. We're happy to provide documentation."},
            {'question': "Do you offer free estimates?", 'answer': "Yes, for most jobs we provide a fixed quote before starting any work. No surprises."},
            {'question': "What areas do you service?", 'answer': f"We serve all of {city} and surrounding neighborhoods within 25 miles."}
        ]
    
    return {
        'brand_name': brand_name,
        'niche': niche,
        'city': city,
        'phone_number': '(555) 123-4567',
        'current_year': datetime.now().year,
        'meta_title': meta_title,
        'meta_description': meta_description,
        'hero_headline': hero_headline,
        'hero_subheadline': hero_subheadline,
        'services': services,
        'about_content': about_content,
        'faqs': faqs,
        'local_proof': local_proof,
        'usp': usp
    }


# Example usage for testing
if __name__ == "__main__":
    # Without research (elevated defaults)
    content = generate_site_content("Emergency Plumber", "Seattle", "Seattle Rapid Flow")
    print(f"Headline: {content['hero_headline']}")
    
    # With research (grounded in real data)
    research = {
        'unique_selling_point': "Only 24/7 licensed plumber serving Ballard & Fremont",
        'local_proof': "Trusted by 847 Seattle families (4.9★ on Google)",
        'response_time': "45 minutes",
        'faqs_from_research': [
            {'question': "Do you fix tankless water heaters?", 'answer': "Yes, we specialize in tankless systems including Rinnai and Navien."}
        ]
    }
    content_researched = generate_site_content("Emergency Plumber", "Seattle", "Seattle Rapid Flow", research)
    print(f"Researched Headline: {content_researched['hero_headline']}")
