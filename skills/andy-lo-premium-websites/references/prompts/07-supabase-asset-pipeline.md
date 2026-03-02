---
name: supabase-asset-pipeline
description: Set up Supabase as a visual CDN for WebP frame sequences and generated assets
---

# Supabase Asset Pipeline

## Purpose
Set up Supabase as a free, high-performance public storage bucket for website visual assets — particularly WebP frame sequences used in scroll-triggered animations. This solves the "where do I host 50+ animation frames" problem without paid CDN services.

## System Prompt

You are Andy Lo. You know that animation frames need fast, reliable hosting with public URLs. Supabase's storage serves as a free CDN that handles this perfectly. You set this up once per project and it handles all visual asset delivery.

## User Prompt

```
Set up Supabase storage as a visual CDN for my website project.

**Project:** {{PROJECT_NAME}}
**Assets to store:**
- WebP animation frame sequences (typically 30-120 frames per animation)
- Generated product/brand images
- Background textures and patterns

**Setup Instructions:**

### Step 1: Supabase Project
1. Create a new Supabase project (or use existing)
2. Navigate to Storage section
3. Create a new bucket: `{{PROJECT_NAME}}-assets`
4. Set bucket to **Public** (these are visual assets, not secrets)

### Step 2: Folder Structure
Create the following folder structure inside the bucket:
```
{{PROJECT_NAME}}-assets/
├── frames/
│   ├── hero/          (hero section animation frames)
│   ├── section-1/     (first animated section frames)
│   └── section-2/     (additional section frames)
├── images/
│   ├── products/      (product shots and renders)
│   ├── backgrounds/   (textures, gradients, patterns)
│   └── branding/      (logos, icons, brand marks)
└── videos/
    └── raw/           (original Flow exports before conversion)
```

### Step 3: Upload Protocol
For WebP frame sequences:
1. Name frames sequentially: `frame_001.webp`, `frame_002.webp`, etc.
2. Upload all frames to the appropriate folder
3. Note the public URL pattern: `https://[PROJECT_REF].supabase.co/storage/v1/object/public/{{PROJECT_NAME}}-assets/frames/hero/frame_001.webp`

### Step 4: Generate Frame URL List
Create a JSON file mapping all frame URLs for the website assembly step:
```json
{
  "hero_frames": [
    "https://[PROJECT_REF].supabase.co/storage/v1/object/public/{{PROJECT_NAME}}-assets/frames/hero/frame_001.webp",
    "...etc"
  ],
  "section_1_frames": ["..."],
  "images": {
    "product_hero": "...url...",
    "background_main": "...url..."
  }
}
```

### Step 5: Performance Verification
- [ ] All frame URLs resolve correctly (200 status)
- [ ] Images load in < 200ms from cold cache
- [ ] WebP format is serving correctly (check content-type header)
- [ ] Bucket is set to public (no auth required for reads)
```

## Expected Output
- Configured Supabase bucket with folder structure
- All assets uploaded and publicly accessible
- JSON manifest of all asset URLs
- Performance verification checklist

## When to Use
- After WebP conversion (Prompt #2) when you need to host frame sequences
- Any project with generated visual assets that need public hosting

## Genius Patterns Applied
- WebP Sequence Scroll Animation Hack (#8)
- Tool Specialization Pipeline (#3)
