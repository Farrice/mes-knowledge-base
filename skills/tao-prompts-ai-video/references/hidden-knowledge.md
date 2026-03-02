# Hidden Knowledge: Tao Prompts AI Video Architecture

## 1. The Decoupling Law
**Tacit Insight**: Never prompt for intense physical action and dialogue lip-sync in the same generation. Create the action shots as B-roll, and create "low-movement" close-ups specifically for lip-syncing. Connect them in the edit.
**Why Others Miss This**: Amateurs try to ask a single model to "show a man running while yelling at his friend." The compute requirement for accurate lip-sync conflicts with high physics action, resulting in warped faces or melted environments. Professionals decouple the two.
**Deploy When**: Planning a character-driven sequence involving action and dialogue.

## 2. The Storyboard Bridge
**Tacit Insight**: Text is too fluid for cohesive multi-shot sequences. A visual storyboard grid (e.g. a 3x3 Midjourney character grid) is the mandatory bridge between a script and a multi-shot video generation.
**Why Others Miss This**: People go straight from script to video generator and get varied, disconnected clips that don't look like they exist in the same universe.
**Deploy When**: Generating complex scenes that require true narrative arc and structural continuity across different shots for multiple tools.

## 3. Prompt Complexity ≠ Aesthetic Quality
**Tacit Insight**: Adding more words and adjectives to a prompt doesn't automatically make the video look "better." Modern models can produce hyper-realistic output from one sentence. Adding complexity to a prompt is strictly for adding *control and specificity*, not beauty.
**Why Others Miss This**: Beginners believe there's a "magic keyword" for ultra-realism and end up cluttering prompts with redundant descriptors, confusing the model's subject focus.
**Deploy When**: Debugging a prompt that produced beautiful but incorrect framing, or when simplifying instructions to regain subject continuity in sequential shots.
