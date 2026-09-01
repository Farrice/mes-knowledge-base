---
name: ai-creative-studio
description: "AI creative asset production: images (portraits, products, posters, UI mockups, logos, 3D renders), videos (UGC, orbits, cinematic, multi-shot sequences, motion graphics), hybrid pipelines, and design systems. Professional creative direction with camera specs, lighting, composition, and mood. Use for: generate image, create visual, produce video, design mockup, product shot, illustration, animation, brand kit, style guide, social content, marketing visual, logo concept, poster design, AI art, or any visual/creative output."
---

> **Provenance:** Imported from Cowork 2026-09-01 (Fresh's exported skills package).

# AI Creative Studio Skill

## Overview

This skill orchestrates the creation of world-class creative assets using state-of-the-art AI generation tools. It combines professional creative direction, technical specification, reference-based styling, and platform expertise to produce photorealistic images, cinematic video, hybrid pipelines, and design systems.

Use this skill when:
- A user requests any visual asset (image, video, design, mockup)
- Creative direction or art direction is needed
- Multiple iterations or refinements are required
- Professional quality and brand consistency matter
- Technical specifications (aspect ratio, resolution, format) are involved

---

## Creative Workflow: Decision Tree

**User request arrives →**

```
┌─ IMAGE REQUEST?
│  ├─ Photorealistic portrait, product shot, commercial photo
│  ├─ UI mockup, poster, logo concept, illustration
│  ├─ 3D render, cutout effect, border-break composition
│  └─ → Load references/image-generation.md
│
├─ VIDEO REQUEST?
│  ├─ UGC-style video, cinematic motion, orbit shot
│  ├─ Commercial video, animation, motion graphics
│  ├─ Multi-shot sequence, explainer, promotional content
│  └─ → Load references/video-generation.md
│
├─ HYBRID PIPELINE?
│  ├─ Image-to-video generation
│  ├─ Multi-shot continuous sequences
│  ├─ Camera movement over static subject
│  └─ → Load both image-generation.md + video-generation.md
│
└─ DESIGN SYSTEM?
   ├─ Brand kit, style guide, asset collection
   ├─ Color palette, typography system, component library
   └─ → Load image-generation.md + prompt-library.md
```

---

## The Creative Brief Protocol

Before generating ANY asset, extract or establish these five dimensions:

### 1. Subject / Product
**What are we creating?**
- Specific subject matter (product name, character, scene, concept)
- Key features or unique selling points
- What should be the visual focus

### 2. Purpose / Context
**Where will this be used?**
- Platform (Instagram, website header, email, print, pitch deck, billboard, etc.)
- Audience (B2B, consumer, niche community, etc.)
- Narrative purpose (hero image, social proof, educational, promotional, etc.)

### 3. Mood / Aesthetic
**What feeling or style?**
- Luxury, editorial, street, minimalist, bold, playful, serious, aspirational, etc.
- Genre references (sci-fi, fantasy, documentary, fashion, architecture, etc.)
- Any specific art movements or design eras to reference

### 4. Technical Specs
**Constraints and requirements?**
- Aspect ratio (16:9, 1:1, 9:16, 4:3, custom)
- Resolution or dimensions
- Format (JPG, PNG, MP4, MOV, WebM, etc.)
- File size limits or quality tiers
- Duration (for video)

### 5. Reference Style
**What visual references guide this?**
- Specific photographers, artists, or designers to channel
- Competitor or brand examples to match
- Color palettes, material finishes, lighting setups to echo
- Mood board links or image references

---

## Professional Prompt Architecture

Apply this universal structure across ALL image and video generation tools:

### Image Prompts

**Foundation Layer:**
```
[SUBJECT] + [ACTION/POSE] + [ENVIRONMENT/SETTING]
Example: "A luxury leather handbag on a marble vanity table in soft morning light"
```

**Technical Specification Layer:**
```
[CAMERA/LENS]: "Shot on Sony A7IV with 85mm f/1.4 prime lens"
[LIGHTING]: "Rembrandt lighting with warm rim light from the left"
[COMPOSITION]: "Rule of thirds, shallow depth of field, centered subject"
[MATERIAL/TEXTURE]: "Brushed aluminum, matte ceramic, raw concrete, etc."
[MOOD/COLOR]: "Desaturated pastels, warm golden tones, cool shadows, high contrast"
```

**Quality Anchors:**
```
"Editorial quality" / "Vogue-level photography" / "Hyperrealistic" / "Magazine spread"
```

**Negative Prompts** (where supported):
```
"No watermarks, text, AI artifacts, extra limbs, melted objects, blurry focus"
```

### Video Prompts

**Foundation:**
```
[SUBJECT/CHARACTER] + [ACTION SEQUENCE] + [ENVIRONMENT]
Example: "A barista expertly pouring latte art in a sunlit coffee shop"
```

**Camera Vocabulary:**
```
"Slow push-in on subject" / "Cinematic orbit shot" / "Camera pans left to right"
"Handheld motion, steadicam glide, drone orbit, static wide shot"
```

**Temporal Specification:**
```
"8-second clip, 24fps, natural motion timing"
"Smooth acceleration into subject, deceleration at end"
```

---

## Tool Selection Quick Reference

| Creative Need | Primary Tool | Alternative | Notes |
|---|---|---|---|
| Photorealistic portrait | NanoBanana Pro (Google) | Flux Pro | Best facial detail |
| Product/commercial photo | Midjourney v7 | DALL-E / Flux | Consistency, materials |
| Typography/text in images | Ideogram 3 | GPT Image | Accurate legibility |
| 3D poster / border-break cutout | Lovart + NanoBanana | Midjourney | Dimension effect |
| UGC-style video | Arcads + Veo 3.1 | Kling 3.0 | Authentic imperfection |
| Cinematic orbit shots | Higgsfield + Kling | Runway Gen-4 | Smooth camera motion |
| Multi-shot sequences | Artlist + Kling 2.5 | Runway Gen-4 | Narrative continuity |
| Motion graphics / text anim | Runway Gen-4 | Kling 3.0 | Advanced effects |

---

## Quality Assurance Checklist

Before delivering any asset, verify:

- [ ] **Anatomy**: Hands, fingers, teeth rendered correctly (no extra limbs, fused digits)
- [ ] **Text/Typography**: Legible, correctly spelled, aligned to brief (if present)
- [ ] **Lighting**: Consistent light direction and intensity across the frame
- [ ] **AI Artifacts**: No melted objects, transparency errors, or generation glitches
- [ ] **Aspect Ratio**: Matches intended platform/use case exactly
- [ ] **Color/Mood**: Aligns with creative brief and aesthetic direction
- [ ] **Background**: Coherent environment with appropriate depth and context
- [ ] **Composition**: Follows specified rule of thirds / framing / balance
- [ ] **Technical Quality**: Resolution, file format, metadata correct

---

## Key Techniques Reference

Brief signatures with pointers to detailed execution guides:

### Image Techniques

**Hybrid Reality Assets**
Seamlessly blend AI-generated elements with real photography for authenticity and control. Useful for product shots, environmental portraits, and commercial work.
→ See `references/image-generation.md`

**3D Border-Break / Cutout Effect**
Create subjects bursting from 2D poster frames with dimensional depth, enhanced by Lovart's 3D capabilities and NanoBanana's realism.
→ See `references/platform-guides.md`

### Video Techniques

**First Frame / Last Frame Control**
Lock the starting or ending visual state to control generation outcomes. Essential for multi-shot sequences and narrative continuity.
→ See `references/video-generation.md`

**Stone Statue Trick**
Freeze subject in place while camera orbits or moves, maintaining character integrity across motion.
→ See `references/video-generation.md`

**UGC Imperfection Prompting**
Add realism cues and intentional "flaws" to video generation prompts (natural breathing, minor hesitations, authentic lighting) to avoid the polished AI look.
→ See `references/video-generation.md`

**Continuous Multi-Shot Sequences**
Maintain character appearance, lighting consistency, and narrative flow across multiple generated clips with reference frames and detailed character briefs.
→ See `references/video-generation.md`

**Cinematic Orbit Shots**
Generate 360-degree camera movements around static subjects (products, environments, portraits) for immersive presentation.
→ See `references/platform-guides.md`

---

## Workflow Execution Steps

When handling a creative request:

1. **Extract the Brief** — Ask clarifying questions (if needed) to establish all five brief dimensions
2. **Load References** — Based on asset type (image/video/hybrid), load the corresponding reference file
3. **Select Tools** — Use the Quick Reference table and `references/tool-selection.md` to pick optimal platforms
4. **Architect Prompt** — Build the prompt using Professional Prompt Architecture above
5. **Generate & Iterate** — Create initial asset, gather feedback, refine prompts
6. **Quality Check** — Run through the QA Checklist before delivery
7. **Deliver & Document** — Provide final asset with generation notes (prompt, tool, settings used)

---

## References Index

Load these files as needed:

| Reference | Purpose |
|---|---|
| `references/image-generation.md` | Professional image prompting: camera specs, lighting, composition, platform-specific techniques, Lovart/Midjourney/Flux/DALL-E workflows |
| `references/video-generation.md` | Video workflows: First Frame/Last Frame, orbits, multi-shot sequencing, speed ramping, camera motion vocabulary, UGC prompting |
| `references/platform-guides.md` | Deep dives: Lovart (3D/border-break), Arcads (UGC video), Higgsfield (cinematic), Artlist (sequences), Midjourney, Flux, Ideogram |
| `references/prompt-library.md` | Ready-to-use templates: luxury product, editorial portrait, commercial video, motion graphics, brand systems, social assets |
| `references/tool-selection.md` | Detailed comparison: pricing, API access, strengths/weaknesses, quality tiers, when to use each platform |

---

## Creative Direction Principles

When advising the user or refining their vision:

- **Reference Early** — Gather visual references before prompting; they reduce ambiguity by 80%
- **Specificity Wins** — "Rembrandt lighting" beats "dramatic light"; "85mm f/1.4" beats "professional lens"
- **Constraint Clarity** — Explicit aspect ratios and technical specs prevent wasted generation cycles
- **Mood Over Medium** — Start with desired feeling, then select tools that best express it
- **Iteration is Design** — AI generation is a conversation; expect 3-5 refinement cycles for final quality
- **Negative Guidance** — Use negative prompts to block common AI failure modes (artifacts, styles, elements)
- **Authenticity Over Perfection** — Sometimes imperfections (UGC style, film grain, natural motion) create better creative impact

---

## When to Escalate or Consult References

**Load `references/image-generation.md` when:**
- Portrait photography, beauty, or glamour shots
- Product/commercial photography requiring material accuracy
- Poster, logo, or typography-heavy visuals
- 3D effects, cutouts, or border-break compositions

**Load `references/video-generation.md` when:**
- Any video generation request (UGC, cinematic, animation, motion graphics)
- Multi-shot sequences or continuous narratives
- Camera motion or orbit shots
- Speed ramping or temporal effects

**Load `references/platform-guides.md` when:**
- Using Lovart, Arcads, Higgsfield, or Artlist specifically
- Needing detailed platform walkthroughs or capabilities
- Troubleshooting platform-specific issues

**Load `references/prompt-library.md` when:**
- Needing ready-to-use prompt templates
- Time is tight and patterns apply to the request
- Building brand systems or asset collections

**Load `references/tool-selection.md` when:**
- Comparing multiple tools for the same task
- Deciding between primary and alternative platforms
- Understanding pricing, API limits, or access constraints

---

## Notes for Claude Instances

This skill is designed for hand-off to other Claude instances. When executing:

- Use imperative language ("Load reference X", "Extract the brief", "Generate asset Y")
- Provide explicit file paths to reference documents
- Include specific tool names and platform capabilities
- Quote user requests precisely to maintain creative intent
- Document all prompts, tool choices, and generation settings
- Ask clarifying questions when brief dimensions are ambiguous
- Treat this workflow as a conversation with the user, not a series of commands

---

**Maintained by:** AI Creative Studio Team
**Last Updated:** February 2026
**Reference Set Version:** 1.0
