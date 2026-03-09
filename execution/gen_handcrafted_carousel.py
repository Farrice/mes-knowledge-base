"""
Handcrafted Carousel Asset Generator
=====================================
Generates consistent, on-brand artwork backgrounds using Nano Banana 2.
Outputs clean illustrations on vintage parchment — ready to drop into
Canva, Figma, or any design tool for text composition.

Usage:
    python execution/gen_handcrafted_carousel.py carousel_script.md
    python execution/gen_handcrafted_carousel.py carousel_script.md --out-dir deliverables/my_assets
    python execution/gen_handcrafted_carousel.py carousel_script.md --with-text  # adds Pillow text overlay
"""

import argparse
import asyncio
import os
import re
import textwrap
from pathlib import Path
import sys

from PIL import Image, ImageDraw, ImageFont

# Ensure execution package is reachable
sys.path.insert(0, str(Path(__file__).resolve().parent))
from gemini_client import GeminiClient, load_env

# ---------------------------------------------------------------------------
# CONFIGURATION
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent
FONT_DIR = BASE_DIR / "assets" / "fonts"

# Colors matching the reference aesthetic
COLOR_BLACK = (45, 35, 25)        # Charcoal-brown for headlines
COLOR_BODY = (55, 45, 35)         # Slightly lighter for body text
COLOR_COPPER = (163, 82, 42)      # Warm copper for labels + slide numbers
COLOR_UNDERLINE = (140, 70, 35)   # Copper underline

# Canvas
CANVAS_W = 1080
CANVAS_H = 1350  # 3:4 portrait for LinkedIn

# Safe margins
MARGIN_LEFT = 60
MARGIN_RIGHT = 60
MARGIN_TOP = 50
MARGIN_BOTTOM = 50
TEXT_AREA_W = CANVAS_W - MARGIN_LEFT - MARGIN_RIGHT

# Parchment overlay color (warm cream with alpha for text backdrop)
PARCHMENT_RGBA = (235, 220, 195, 210)  # Semi-transparent warm cream

# NB2 prompt suffix — generates artwork ONLY, no text
ART_PROMPT_SUFFIX = """
CRITICAL RENDERING RULES:
- This is a hand-drawn charcoal ink sketch on vintage cream/parchment paper.
- DO NOT include ANY text, letters, numbers, words, or typography of any kind.
- The illustration should occupy roughly the top 40-50% of the image.
- Leave the bottom 50-60% as clean, empty parchment paper with natural grain.
- Use charcoal/dark brown ink lines for the sketch. Warm copper/brown accents sparingly.
- The parchment background should have realistic paper grain and subtle aging marks.
- Style: Analog, tactile, hand-drawn. Like a brilliant strategist's moleskine notebook.
- Absolutely NO digital gradients, 3D renders, vector graphics, or clean digital lines.
"""

# ---------------------------------------------------------------------------
# FONT LOADING
# ---------------------------------------------------------------------------

def load_fonts():
    """Load the font family, with graceful fallback."""
    fonts = {}
    pm_path = FONT_DIR / "PermanentMarker-Regular.ttf"
    cav_path = FONT_DIR / "Caveat-Regular.ttf"

    if not pm_path.exists() or not cav_path.exists():
        print(f"WARNING: Fonts not found in {FONT_DIR}. Using system defaults.")
        pm_path = None
        cav_path = None

    def _font(path, size):
        if path:
            return ImageFont.truetype(str(path), size)
        return ImageFont.load_default()

    fonts["headline"] = _font(pm_path, 100)
    fonts["headline_small"] = _font(pm_path, 76)
    fonts["label"] = _font(pm_path, 36)
    fonts["body"] = _font(cav_path, 48)
    fonts["body_small"] = _font(cav_path, 40)
    fonts["bullet"] = _font(cav_path, 44)
    fonts["slide_num"] = _font(pm_path, 48)
    return fonts


# ---------------------------------------------------------------------------
# TEXT RENDERING UTILITIES
# ---------------------------------------------------------------------------

def wrap_text(text, font, max_width, draw):
    """Word-wrap text to fit within max_width pixels."""
    words = text.split()
    lines = []
    current_line = ""
    for word in words:
        test = f"{current_line} {word}".strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        w = bbox[2] - bbox[0]
        if w <= max_width:
            current_line = test
        else:
            if current_line:
                lines.append(current_line)
            current_line = word
    if current_line:
        lines.append(current_line)
    return lines


def draw_text_block(draw, text, x, y, font, color, max_width, line_spacing=1.25):
    """Draw a wrapped text block. Returns the y position after the last line."""
    lines = wrap_text(text, font, max_width, draw)
    for line in lines:
        draw.text((x, y), line, fill=color, font=font)
        bbox = draw.textbbox((0, 0), line, font=font)
        h = bbox[3] - bbox[1]
        y += int(h * line_spacing)
    return y


def draw_underline(draw, text, x, y, font, color, thickness=3):
    """Draw a hand-style underline beneath text."""
    bbox = draw.textbbox((x, y), text, font=font)
    line_y = bbox[3] + 4
    draw.line([(bbox[0], line_y), (bbox[2], line_y)], fill=color, width=thickness)


def draw_slide_number(draw, num, fonts):
    """Draw the slide number in the bottom-right corner."""
    num_text = f"{num:02d}"
    font = fonts["slide_num"]
    bbox = draw.textbbox((0, 0), num_text, font=font)
    w = bbox[2] - bbox[0]
    x = CANVAS_W - MARGIN_RIGHT - w
    y = CANVAS_H - MARGIN_BOTTOM - (bbox[3] - bbox[1]) - 10

    # Small arrow before the number
    arrow_y = y + (bbox[3] - bbox[1]) // 2
    draw.line([(x - 50, arrow_y), (x - 15, arrow_y)], fill=COLOR_COPPER, width=3)
    # Arrowhead
    draw.polygon([(x - 15, arrow_y - 5), (x - 5, arrow_y), (x - 15, arrow_y + 5)], fill=COLOR_COPPER)

    draw.text((x, y), num_text, fill=COLOR_COPPER, font=font)

# ---------------------------------------------------------------------------
# SLIDE COMPOSITION
# ---------------------------------------------------------------------------

def compose_slide(bg_image_path, slide_data, fonts, slide_type="content"):
    """
    Composite text onto a NB2-generated background.

    slide_data keys:
        number: int
        label: str (section label, e.g. "THE PROBLEM")
        title: str (main headline)
        body: str (body paragraph or bullet list)
        bullets: list[str] (optional, if body is bullet points)
    """
    img = Image.open(bg_image_path).convert("RGBA")
    img = img.resize((CANVAS_W, CANVAS_H), Image.LANCZOS)

    # ── STEP 1: Add semi-transparent parchment backdrop behind text zone ──
    # This prevents artwork from bleeding through and ruining legibility.
    text_zone_top = int(CANVAS_H * 0.38) if slide_type == "cover" else int(CANVAS_H * 0.40)
    backdrop = Image.new("RGBA", img.size, (0, 0, 0, 0))
    bd_draw = ImageDraw.Draw(backdrop)
    # Gradient fade: fully transparent at top edge, then solid parchment
    fade_height = 60  # pixels of soft gradient fade
    for row in range(fade_height):
        alpha = int(PARCHMENT_RGBA[3] * (row / fade_height))
        y_pos = text_zone_top + row
        bd_draw.line([(0, y_pos), (CANVAS_W, y_pos)],
                     fill=(PARCHMENT_RGBA[0], PARCHMENT_RGBA[1], PARCHMENT_RGBA[2], alpha))
    # Solid parchment below the gradient
    bd_draw.rectangle([(0, text_zone_top + fade_height), (CANVAS_W, CANVAS_H)],
                      fill=PARCHMENT_RGBA)
    img = Image.alpha_composite(img, backdrop)

    # ── STEP 2: Render text overlay ──
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # Text starts right after the gradient fade
    text_y = text_zone_top + fade_height + 10
    x = MARGIN_LEFT
    max_w = TEXT_AREA_W

    # --- Section Label (e.g. "THE PROBLEM") ---
    label = slide_data.get("label", "")
    if label:
        draw.text((x, text_y), label.upper(), fill=COLOR_COPPER, font=fonts["label"])
        bbox = draw.textbbox((x, text_y), label.upper(), font=fonts["label"])
        text_y = bbox[3] + 12

    # --- Headline ---
    title = slide_data.get("title", "")
    if title:
        # Choose font size based on title length
        if len(title) > 25:
            hfont = fonts["headline_small"]
        else:
            hfont = fonts["headline"]

        title_lines = wrap_text(title, hfont, max_w, draw)
        for i, line in enumerate(title_lines):
            draw.text((x, text_y), line, fill=COLOR_BLACK, font=hfont)
            bbox = draw.textbbox((x, text_y), line, font=hfont)
            line_h = bbox[3] - bbox[1]

            # Underline the last line of the title
            if i == len(title_lines) - 1:
                draw_underline(draw, line, x, text_y, hfont, COLOR_UNDERLINE, thickness=5)

            text_y += int(line_h * 1.12)

        text_y += 24  # Gap after headline

    # --- Body Text ---
    body = slide_data.get("body", "")
    if body:
        text_y = draw_text_block(draw, body, x, text_y, fonts["body"], COLOR_BODY, max_w, line_spacing=1.35)
        text_y += 16

    # --- Bullet Points ---
    bullets = slide_data.get("bullets", [])
    if bullets:
        for bullet in bullets:
            bullet_text = f"• {bullet}"
            text_y = draw_text_block(draw, bullet_text, x + 10, text_y, fonts["bullet"], COLOR_BODY, max_w - 20, line_spacing=1.3)
            text_y += 10

    # --- Slide Number ---
    draw_slide_number(draw, slide_data.get("number", 0), fonts)

    # Composite
    result = Image.alpha_composite(img, overlay)
    return result.convert("RGB")


# ---------------------------------------------------------------------------
# INPUT PARSER
# ---------------------------------------------------------------------------

def parse_carousel_file(filepath):
    """
    Parse a markdown file into structured slide data.
    
    Expected format per slide:
        Slide N:
        Label: THE PROBLEM
        Title: The Authenticity Trap
        Body: Your body text here...
        Bullets:
        - First bullet
        - Second bullet
        Visual: A tangled knot of rope (used for NB2 artwork prompt)
    """
    content = Path(filepath).read_text()
    
    # Split by "Slide N:" pattern
    raw_slides = re.split(r'(?im)^slide\s+(\d+)\s*:', content)
    
    slides = []
    # raw_slides[0] is text before "Slide 1:", then pairs of (number, content)
    for i in range(1, len(raw_slides), 2):
        num = int(raw_slides[i])
        block = raw_slides[i + 1].strip() if i + 1 < len(raw_slides) else ""
        
        slide = {"number": num}
        
        # Extract fields
        label_m = re.search(r'(?im)^label:\s*(.+)', block)
        title_m = re.search(r'(?im)^title:\s*(.+)', block)
        visual_m = re.search(r'(?im)^visual:\s*(.+)', block)
        body_m = re.search(r'(?im)^body:\s*([\s\S]*?)(?=^(?:label|title|visual|bullets|slide)\s*:|\Z)', block)
        bullets_m = re.search(r'(?im)^bullets:\s*\n((?:\s*-\s*.+\n?)+)', block)
        type_m = re.search(r'(?im)^type:\s*(.+)', block)
        
        slide["label"] = label_m.group(1).strip() if label_m else ""
        slide["title"] = title_m.group(1).strip() if title_m else ""
        slide["visual"] = visual_m.group(1).strip() if visual_m else "Abstract sketch related to the topic."
        slide["type"] = type_m.group(1).strip().lower() if type_m else "content"
        
        if body_m:
            body_text = body_m.group(1).strip()
            # Remove any field markers that leaked in
            body_text = re.sub(r'(?im)^(label|title|visual|bullets|type|slide)\s*:.*', '', body_text).strip()
            slide["body"] = body_text
        else:
            slide["body"] = ""
            
        if bullets_m:
            raw_bullets = bullets_m.group(1).strip().split("\n")
            slide["bullets"] = [b.strip().lstrip("- ").strip() for b in raw_bullets if b.strip()]
        else:
            slide["bullets"] = []
            
        slides.append(slide)
    
    return sorted(slides, key=lambda s: s["number"])


# ---------------------------------------------------------------------------
# MAIN PIPELINE
# ---------------------------------------------------------------------------

async def main():
    parser = argparse.ArgumentParser(description="Generate a handcrafted carousel (hybrid NB2 + Pillow)")
    parser.add_argument("input_file", help="Markdown file with structured slide data")
    parser.add_argument("--out-dir", default="deliverables/crafted_carousel", help="Output directory")
    parser.add_argument("--with-text", action="store_true", help="Also generate text-composited slides (default: artwork only)")
    args = parser.parse_args()

    load_env()
    client = GeminiClient()
    fonts = load_fonts()
    
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    art_dir = out_dir / "artwork"
    art_dir.mkdir(exist_ok=True)
    
    slides = parse_carousel_file(args.input_file)
    if not slides:
        print("ERROR: No slides found. Use 'Slide 1:', 'Slide 2:' format.")
        return

    print(f"Parsed {len(slides)} slides. Starting hybrid generation...\n")
    reference_path = None
    
    for slide in slides:
        num = slide["number"]
        print(f"--- Slide {num:02d} ---")
        
        # STEP 1: Generate artwork with NB2 (NO TEXT)
        art_prompt = f"""
Create a single hand-drawn illustration on vintage cream parchment paper:
Subject: {slide['visual']}

{ART_PROMPT_SUFFIX}
"""
        print(f"  [1/2] Generating artwork: {slide['visual'][:60]}...")
        
        kwargs = {"aspect_ratio": "3:4", "image_size": "2K"}
        if reference_path:
            kwargs["reference_image_paths"] = [reference_path]
        
        try:
            images, meta = await client.generate_image(art_prompt, **kwargs)
            if not images:
                print(f"  FAILED: NB2 returned no image for slide {num}. Skipping.")
                continue
                
            art_path = art_dir / f"art_{num:02d}.png"
            art_path.write_bytes(images[0])
            print(f"  Artwork saved: {art_path}")
            
            if num == 1:
                reference_path = str(art_path)
                print(f"  Style anchor set from Slide 1.")
        except Exception as e:
            print(f"  ERROR generating artwork: {e}")
            continue
        
        # STEP 2: Overlay text with Pillow (optional)
        if args.with_text:
            print(f"  [2/2] Compositing text overlay...")
            try:
                final = compose_slide(str(art_path), slide, fonts, slide_type=slide.get("type", "content"))
                final_path = out_dir / f"slide_{num:02d}.png"
                final.save(str(final_path), quality=95)
                print(f"  Composited slide saved: {final_path}")
            except Exception as e:
                print(f"  ERROR compositing text: {e}")
        print()

    print("=" * 50)
    print(f"DONE. {len(slides)} slides generated in: {out_dir}")
    print("Combine into PDF for LinkedIn upload.")


if __name__ == "__main__":
    asyncio.run(main())
