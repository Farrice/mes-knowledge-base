#!/usr/bin/env python3
"""
Image Generator — Nano Banana 2 (gemini-3.1-flash-image-preview)

Generate images from text prompts using Google's Gemini image generation model.

Usage:
    python generate_image.py "A futuristic logo for an AI consulting company"
    python generate_image.py --aspect 16:9 "A wide banner for a LinkedIn post about AI agents"
    python generate_image.py --output my_image.png "A minimalist icon"
    python generate_image.py --edit input.png "Make the background darker and add a subtle glow"
"""

import asyncio
import argparse
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from gemini_client import GeminiClient, load_env

load_env()


OUTPUT_DIR = Path(__file__).parent.parent / "deliverables" / "images"


async def generate(prompt: str, aspect_ratio: str = "1:1",
                   output_path: str = None, edit_path: str = None):
    """Generate an image and save to disk."""
    client = GeminiClient()

    print(f"\n{'='*50}")
    print(f"🎨 NANO BANANA 2 — Image Generation")
    print(f"{'='*50}")
    print(f"📝 Prompt: {prompt}")
    print(f"📐 Aspect: {aspect_ratio}")
    if edit_path:
        print(f"✏️  Editing: {edit_path}")
    print(f"{'='*50}\n")

    start = time.time()

    images, meta = await client.generate_image(
        prompt,
        aspect_ratio=aspect_ratio,
        input_image_path=edit_path,
    )

    duration = time.time() - start

    if not images:
        print("❌ No images generated. The model may have declined the prompt.")
        print("   Try rephrasing or adjusting the prompt.")
        return

    # Determine output path
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    if output_path:
        save_path = Path(output_path)
    else:
        timestamp = time.strftime("%Y%m%d_%H%M%S")
        slug = prompt[:40].lower().replace(" ", "_").replace("/", "-")
        slug = "".join(c for c in slug if c.isalnum() or c in "_-")
        save_path = OUTPUT_DIR / f"{timestamp}_{slug}.png"

    save_path.parent.mkdir(parents=True, exist_ok=True)

    # Save first image (model typically returns 1)
    save_path.write_bytes(images[0])

    print(f"✅ Image generated successfully!")
    print(f"📂 Saved to: {save_path}")
    print(f"📊 Tokens: {meta.total_tokens:,}")
    print(f"💰 Est. Cost: ${meta.estimated_cost_usd:.4f}")
    print(f"⏱️  Duration: {duration:.1f}s")

    if len(images) > 1:
        for i, img in enumerate(images[1:], 2):
            extra_path = save_path.with_stem(f"{save_path.stem}_{i}")
            extra_path.write_bytes(img)
            print(f"📂 Extra image {i}: {extra_path}")

    return save_path


def main():
    parser = argparse.ArgumentParser(
        description="Nano Banana 2 — Generate images with Gemini",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python generate_image.py "A logo for an AI company called Antigravity"
  python generate_image.py --aspect 16:9 "LinkedIn banner about AI agents"
  python generate_image.py --output brand/logo.png "Minimalist gravity logo"
  python generate_image.py --edit photo.png "Add cinematic lighting"
        """
    )
    parser.add_argument("prompt", help="Text description of the image to generate")
    parser.add_argument("--aspect", default="1:1",
                        choices=["1:1", "16:9", "9:16", "4:3", "3:4"],
                        help="Aspect ratio (default: 1:1)")
    parser.add_argument("--output", "-o", help="Output file path (default: auto-generated)")
    parser.add_argument("--edit", help="Path to input image for editing (text+image mode)")

    args = parser.parse_args()

    result = asyncio.run(generate(
        args.prompt,
        aspect_ratio=args.aspect,
        output_path=args.output,
        edit_path=args.edit,
    ))

    if not result:
        sys.exit(1)


if __name__ == "__main__":
    main()
