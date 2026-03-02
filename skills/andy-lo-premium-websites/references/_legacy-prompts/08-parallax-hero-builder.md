---
name: parallax-hero-builder
description: Build scroll-triggered animated hero sections from WebP frame sequences
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

## Expected Output
- Complete hero section component
- Frame preloader with loading state
- Scroll-linked animation engine
- Responsive text overlay
- Mobile optimizations

## When to Use
- Any website needing a cinematic first impression
- After frame sequences are generated and hosted (Prompts #2 and #7)

## Genius Patterns Applied
- WebP Sequence Scroll Animation Hack (#8)
- Bookend Frame Architecture (#2)
- Progressive Polish Protocol (#6)
