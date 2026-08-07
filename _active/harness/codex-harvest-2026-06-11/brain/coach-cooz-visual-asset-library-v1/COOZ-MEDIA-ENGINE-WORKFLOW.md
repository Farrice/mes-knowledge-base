# Cooz Media Engine Workflow V1

## Purpose

Use this workflow when Farrice or Cooz wants to turn a topic, voice memo, post, or offer idea into a high-quality visual/media asset.

This is the repeatable bridge from strategy to finished social media.

## Inputs

Required:

- topic or voice memo
- target platform
- desired format
- CTA intent
- selected image or visual direction

Optional:

- proof story
- Triage Audit angle
- platform constraint
- design reference
- video length

## Format Options

- LinkedIn static image
- LinkedIn banner
- Instagram carousel
- Instagram Reel
- Instagram Story
- YouTube thumbnail
- YouTube Short
- blog/social header
- Triage Audit one-page asset
- warm referral PDF

## Workflow Stack

### 1. Content Strategy

Use:

- `cooz-flywheel`
- `content-audience-profile`
- `belief-shift-content`
- `new-media-content-engine`
- `diandra-save-architect`
- `diandra-semantic-lanes`

Output:

- reader recognition
- emotional tension
- useful insight
- practical next move
- platform-native copy

### 2. Visual Brief

Use:

- `COOZ-DESIGN-MARKETING-ASSET-GEM`
- `design-brief`
- `creative-review`

Output:

- asset job
- buyer moment
- copy
- visual direction
- chosen reference image
- CTA
- production notes

### 3. Static Image / Graphic Production

Use:

- `generate-image`
- `generate-handcrafted-carousel`
- Canva plugin when final layout is needed
- `design-first-build` if building a more complex visual system

Rules:

- Start from an approved reference image.
- Save generated outputs into `generated-derivatives/`.
- Use `platform-ready/` if the asset needs a fast crop.
- Do not overwrite originals.

### 4. Video / Motion Production

Use:

- `storyboard`
- `generate-video-asset`
- Remotion

Output:

- storyboard
- start frame
- end frame if needed
- motion prompt
- caption text
- edit notes
- final render direction

### 5. QA

Use:

- `creative-review`
- `design-taste-gate`
- `anti-slop-audit`
- `anti-homogenization-audit`

Pass only if:

- clear in under 3 seconds
- one idea only
- no generic trainer feel
- no fake proof implication
- premium without fake luxury
- Cooz voice and visual world match

## Output Template

```text
Asset:
Platform:
Format:
CTA:

Buyer moment:

Core insight:

Copy:

Selected image:

Visual direction:

Image generation prompt, if needed:

Canva/Figma layout notes:

Remotion plan, if video:

QA notes:
```

## Example: 4 PM Fog Carousel

Asset:

Instagram carousel

Buyer moment:

The professional over 40 hits the afternoon wall and keeps calling it age, stress, or busyness.

Core insight:

The 4 PM fog is usually traceable before it is mysterious.

Selected image:

`carousel_cover_kettlebell_1080x1080.png`

Visual direction:

Dark, warm, minimal. Kettlebell image as cover or final slide. Large headline, no more than one thought per slide.

CTA:

Save this and track the five inputs for seven days.

## Example: Triage Audit Reel

Asset:

Instagram Reel / YouTube Short

Buyer moment:

They are about to buy another plan, but they do not know what keeps breaking.

Core insight:

Do not buy another plan until you know what keeps breaking.

Selected image:

`story_gym_teaching_1080x1920.png`

Remotion plan:

- 0-2 sec: pattern hook
- 2-10 sec: list what may be breaking
- 10-22 sec: diagnosis before prescription
- 22-30 sec: Triage Audit CTA

CTA:

Message "audit."

## Future Automation Idea

Create a `/cooz-media-engine` command that asks for:

- topic
- platform
- format
- CTA
- selected asset

Then produces:

- copy
- visual brief
- image prompt
- Canva instructions
- Remotion storyboard if video
- QA checklist
