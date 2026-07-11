---
name: "Parallax Hero Builder"
source_prompt: "skills/andy-lo-premium-websites/references/prompts/08-parallax-hero-builder.md"
skill: andy-lo-premium-websites
standard: structure-pure-v2
refactored: 2026-07-11
---

# Parallax Hero Builder

## Purpose
Build a premium, scroll-triggered animated hero section that plays through a WebP frame sequence as the user scrolls. This is the signature visual technique that makes Andy Lo websites feel cinematic and premium.

## System Prompt

You are Andy Lo. You understand that the hero section IS the website for most visitors — they judge everything in milliseconds. Your parallax heroes use scroll-linked frame playback to create motion that responds to user interaction, making the site feel alive without heavy video files.

## User Prompt

```
Build a scroll-triggered parallax hero section for my website.

**Assets:**
- Frame sequence URLs: {{FRAME_URLS}} (from Supabase)
- Total frames: {{FRAME_COUNT}}
- Frame dimensions: {{WIDTH}}x{{HEIGHT}}
- Brand overlay text: {{HEADLINE}}
- Subtext: {{SUBTEXT}}

**Build the following:**

### 1. Frame Preloader
```javascript
// Preload all frames on page load for smooth playback
// Show a minimal loading indicator until frames are cached
// Use IntersectionObserver to trigger preload when hero approaches viewport
```

### 2. Scroll-Linked Playback Engine
```javascript
// Map scroll position to frame index
// scrollProgress (0-1) → frameIndex (0 to FRAME_COUNT-1)
// Use requestAnimationFrame for smooth rendering
// Canvas element for frame rendering (better performance than img swapping)
// Debounce/throttle for mobile performance
```

### 3. Hero Layout
```css
/* Full viewport height */
/* Frame canvas positioned absolutely, covering entire hero */
/* Text overlay with proper z-index */
/* Gradient overlay for text readability (bottom-to-top dark fade) */
/* Text entrance animation (fade-up on initial load) */
```

### 4. Text Overlay Styling
```css
/* Large, editorial heading typography */
/* Subtle text shadow for depth */
/* Entrance animation: opacity 0→1, translateY 20px→0px, 800ms ease-out */
/* Scroll indicator at bottom (animated chevron or "scroll" text) */
```

### 5. Mobile Optimization
- Reduce frame count for mobile (skip every other frame)
- Fall back to static image on very slow connections
- Touch-scroll sensitivity adjustment
- Ensure text remains readable at all breakpoints

### 6. Performance Checklist
- [ ] All frames preloaded before playback starts
- [ ] No jank during scroll (60fps target)
- [ ] Loading indicator shows during preload
- [ ] Fallback image for JS-disabled browsers
- [ ] Works on iOS Safari (test scroll events)
- [ ] Memory usage stays reasonable (dispose frames not in view)

**The hero should feel like scrolling through a film sequence — smooth, intentional, premium.**
```

## Output Contract
- A frame preloader that caches the sequence on load/approach, with a loading indicator
- A scroll-linked playback engine mapping scroll progress (0-1) to frame index, rendered via canvas
- A hero layout: full-viewport frame canvas, text overlay, readability gradient, text entrance animation
- Text overlay styling with defined entrance-animation timing
- Mobile optimizations: reduced frame count, slow-connection fallback, touch sensitivity, readable text at all breakpoints
- A completed performance checklist

## Output Skeleton
```
FRAME PRELOADER
Trigger: [on load / IntersectionObserver near viewport]
Loading indicator: [confirm present]

SCROLL-LINKED PLAYBACK ENGINE
Mapping: scrollProgress (0-1) → frameIndex (0 to {{FRAME_COUNT}}-1)
Render method: [canvas, not img-swap]
Perf technique: [requestAnimationFrame + debounce/throttle for mobile]

HERO LAYOUT
Viewport: full-height
Canvas position: [absolute, covers hero]
Text overlay z-index: [confirm above canvas]
Readability gradient: [direction + purpose]
Entrance animation: [confirm present]

TEXT OVERLAY STYLING
Typography: [editorial heading style]
Entrance animation: opacity [0→1], translateY [Npx→0px], duration [Nms], easing [type]
Scroll indicator: [confirm present]

MOBILE OPTIMIZATION
- Frame count reduction: [rule]
- Slow-connection fallback: [static image trigger condition]
- Touch sensitivity: [adjustment]
- Text readability: [confirmed at all breakpoints]

PERFORMANCE CHECKLIST RESULT
- [ ] All frames preloaded before playback starts
- [ ] No jank during scroll (60fps target)
- [ ] Loading indicator shows during preload
- [ ] Fallback image for JS-disabled browsers
- [ ] Works on iOS Safari (test scroll events)
- [ ] Memory usage stays reasonable (dispose frames not in view)
```

## Quality Gate
- [ ] Frame rendering uses canvas, not sequential img-tag swapping
- [ ] The scroll-to-frame mapping covers the full range (0 to FRAME_COUNT-1) with no dead zones
- [ ] A static-image fallback exists for JS-disabled browsers and very slow connections
- [ ] Mobile frame count is explicitly reduced, not left identical to desktop
- [ ] The performance checklist is fully checked, including an explicit iOS Safari scroll-event test

## Deploy When
- Any website needing a cinematic first impression
- After frame sequences are generated and hosted (Prompts #2 and #7)

## Genius Patterns Applied
- WebP Sequence Scroll Animation Hack (#8)
- Bookend Frame Architecture (#2)
- Progressive Polish Protocol (#6)
