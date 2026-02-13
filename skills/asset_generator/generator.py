import os
import argparse
from jinja2 import Environment, FileSystemLoader
from content_engine import generate_site_content
from visual_engine import get_visual_assets

# Setup directories
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
OUTPUT_DIR = os.path.join(BASE_DIR, '_site')

def generate_site(niche, city, brand_name):
    """
    Orchestrates the generation of the website.
    """
    
    print(f"🚀 Generating Asset for: {brand_name} ({niche} in {city})")
    print("   ...Fetching Content (Content Engine)")
    content_data = generate_site_content(niche, city, brand_name)
    
    print("   ...Fetching Visuals (Visual Engine)")
    visual_data = get_visual_assets(niche, city)
    
    # Merge Data
    # We need to map the visual data service images to the content services
    # Ideally, content engine should return the list of services, and visual engine matches them
    # For this MVP, we map by index
    
    context = content_data.copy()
    context['hero_image_url'] = visual_data['hero_image_url']
    context['about_image_url'] = visual_data['about_image_url']
    
    # Inject images into services
    for i, service in enumerate(context['services']):
        if i < len(visual_data['service_images']):
            service['image_url'] = visual_data['service_images'][i]
        else:
             service['image_url'] = 'https://source.unsplash.com/400x300/?tools'

    # Render Template
    print("   ...Rendering HTML")
    env = Environment(loader=FileSystemLoader(TEMPLATE_DIR))
    template = env.get_template('master_theme.html')
    output_html = template.render(context)
    
    # Write Output
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    output_path = os.path.join(OUTPUT_DIR, 'index.html')
    with open(output_path, 'w') as f:
        f.write(output_html)
        
    print(f"✅ Website generated at: {output_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Antigravity Asset Generator')
    parser.add_argument('--niche', type=str, required=True, help='Business Niche (e.g. Plumber)')
    parser.add_argument('--city', type=str, required=True, help='Target City')
    parser.add_argument('--brand', type=str, required=True, help='Brand Name')
    
    args = parser.parse_args()
    
    generate_site(args.niche, args.city, args.brand)
