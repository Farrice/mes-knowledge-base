# AI Model Selector

Choose the optimal AI model for your specific design task.

## Role

You are applying Kittl's model-to-task matching for maximum first-generation accuracy.

## Required Input

- **TASK DESCRIPTION**: What you're trying to generate or edit
- **QUALITY REQUIREMENTS**: Speed vs. fidelity tradeoffs
- **OUTPUT USE**: Where and how image will be used

## Execution

Match task to model strength:

| Task Type | Recommended Model | Why |
|-----------|------------------|-----|
| Graphic design with text | Ideogram 2/3 | Best text rendering |
| Photorealistic images | Google Image Gen 4 | Highest photorealism |
| Artistic/stylized | Seedream 3/4 | Best artistic interpretation |
| Fast concepting | Flux/Flash | Speed over fidelity |
| Image editing | Nana Banana | Surgical precision |
| Abstract/patterns | Midjourney | Aesthetic strength |

## Output

- **Model Selection**: Which AI to use
- **Prompt Adjustments**: Model-specific formatting
- **Fallback Options**: If first choice doesn't work

## Example Usage

**Input**: "Product mockup showing coffee packaging in lifestyle setting"

**Selection**:
- Primary: Google Image Gen 4 (photorealism needed)
- Prompt adjustment: Use photography terminology (shallow DOF, natural lighting)
- Fallback: Ideogram if text on packaging is critical
