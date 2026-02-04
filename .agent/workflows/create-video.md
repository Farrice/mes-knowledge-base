# /create-video

Streamlined video creation workflow combining @pj-accetturo viral strategy with @remotion programmatic video.

## Usage

```
/create-video [type]
```

Types: `teaser` | `testimonial` | `demo` | `announcement` | `custom`

---

## The Workflow

### Phase 1: Strategy (@pj-accetturo)

Invoke PJ Accetturo for viral video strategy:

1. **Read** `skills/pj-accetturo-ai-video/SKILL.md`
2. **Read** the relevant prompt:
   - `prompt_01_script_generator` - For scripts
   - `prompt_10_viral_mechanics` - For hook/retention
   - `prompt_05_brand_strategy` - For brand alignment

3. **Define the Brief:**
   - Video length (15s, 30s, 60s)
   - Platform (Instagram Reels, TikTok, LinkedIn, YouTube Shorts)
   - Hook strategy
   - Core message
   - CTA

### Phase 2: Build (@remotion)

Invoke Remotion to build the composition:

1. **Read** `skills/remotion-video-creation/SKILL.md`
2. **Read** relevant rules from `rules/`:
   - `animations.md` - Core animation patterns
   - `text-animations.md` - Typography effects
   - `timing.md` - Interpolation and springs
   - `sequencing.md` - Scene transitions

3. **Create composition in:**
   ```
   projects/remotion-studio/src/[VideoName].tsx
   ```

4. **Register in Root.tsx:**
   - Add import
   - Add Composition with defaultProps

### Phase 3: Preview & Iterate

```bash
cd projects/remotion-studio
npm start
```

Open http://localhost:3000 and preview.

### Phase 4: Render

```bash
# Render to MP4
npx remotion render [CompositionId] out/video.mp4

# Render specific format for platform
npx remotion render [CompositionId] out/video.mp4 --codec h264 --crf 18
```

---

## Quick Templates

### 15-Second Product Teaser
- **Structure:** Hook (3s) → Feature (4s) → Result (5s) → CTA (3s)
- **Best for:** Instagram Reels, TikTok
- **Dimensions:** 1080x1920 (9:16)

### 30-Second Testimonial
- **Structure:** Quote (8s) → Context (7s) → Results (10s) → CTA (5s)
- **Best for:** LinkedIn, YouTube Pre-roll
- **Dimensions:** 1920x1080 (16:9) or 1080x1080 (1:1)

### 60-Second Demo
- **Structure:** Problem (10s) → Solution intro (10s) → Demo (30s) → CTA (10s)
- **Best for:** YouTube, Website
- **Dimensions:** 1920x1080 (16:9)

---

## Available Compositions

Check current compositions:
```bash
npx remotion compositions
```

| Composition | Duration | Dimensions | Use Case |
|-------------|----------|------------|----------|
| HelloWorld | 5s | 1920x1080 | Test/demo |
| ProductTeaser | 15s | 1080x1920 | Social teaser |

---

## Adding New Templates

1. Create component in `src/[Name].tsx`
2. Export main component with typed props
3. Register in `src/Root.tsx` with defaultProps
4. Test in Studio
5. Document in this workflow

---

## Rendering Tips

| Platform | Codec | Size | FPS |
|----------|-------|------|-----|
| Instagram/TikTok | h264 | 1080x1920 | 30 |
| LinkedIn | h264 | 1920x1080 | 30 |
| YouTube | h264 | 1920x1080 | 30-60 |
| Twitter/X | h264 | 1920x1080 | 30 |

---

## Expert Agents for Video

| Agent | Use For |
|-------|---------|
| `@pj-accetturo` | Viral strategy, scripts, visual direction |
| `@remotion` | Code, animations, rendering |
| `@kallaway` | Content psychology, hook engineering |
| `@seena-rez` | TikTok-specific viral patterns |

