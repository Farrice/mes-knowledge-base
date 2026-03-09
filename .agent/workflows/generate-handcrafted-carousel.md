---
description: Generate a guaranteed 8-slide handcrafted LinkedIn carousel using Nano Banana 2
---

# /generate-handcrafted-carousel — Hand-Drawn Carousel Generator

Generates a LinkedIn-optimized (3:4 aspect ratio, 2K resolution) carousel using the signature "Tactile Strategist" aesthetic:
- Hand-drawn vintage parchment paper backgrounds
- Charcoal sketches and marker typography
- Warm copper/brown accent colors
- High visual anchoring (uses Slide 1 as a style reference for 2-8)

## Usage

```bash
/generate-handcrafted-carousel [path/to/script.md]
```

Example:
```bash
/generate-handcrafted-carousel deliverables/design-brief-my-topic.md
```

## Input Formatting Instructions

The script expects a simple text/Markdown file containing your slide scripts.
Format each slide with `Slide X:` and optionally a `Visual:` prompt.

Example `carousel_script.md`:
```markdown
Slide 1:
Visual: A drawn door slightly cracked open, inviting the viewer in.
THE AUTHENTICITY TRAP
Why "being yourself" keeps you stuck—and what elite executives do instead.

Slide 2:
Visual: An empty meeting room with one person standing outside.
THE PARADOX
You've been told to "just be yourself." But every time you do, you feel more stuck.

Slide 3:
Visual: A tangled knot of thick rope.
The truth? Authenticity without strategy is just unfiltered chaos.
```

## Steps

### 1. Validate the Input File
Ensure the user has provided a path to a properly formatted text file (using `Slide 1:`, `Slide 2:` syntax). If they haven't written the script yet, use the `@Kallaway` or `@Mark Kashef` skills to write a high-dwell-time carousel script first, save it to a `.md` file, and then proceed.

### 2. Execute the Pipeline
Run the dedicated execution script:
// turbo
```bash
python /Users/farricecain/Google\ Antigravity/execution/gen_handcrafted_carousel.py [path/to/script.md] --out-dir deliverables/crafted_carousel
```

### 3. Deliver
- The slides will be populated in `deliverables/crafted_carousel/`.
- Tell the user to combine the 8 images into a PDF to upload as a native LinkedIn carousel.
- Ask if they want to revise any specific slide's text or visual concept.

## Psychology & Vibe Context
This pipeline actively combats "generic AI slop." It leverages Nano Banana 2's texture and style-transfer capabilities to make the digital asset feel analog, tactile, and highly crafted. Executive audiences trust visual restraint over flashy gradients.
