# Recruiter Send Guide

## Best Send Package

Send both:

1. A live site URL.
2. The PDF attachment.

The live URL feels polished and easy to browse. The PDF is safer for forwarding internally or uploading into an applicant tracking system.

## Ready Now

PDF:

`_active/farrice-brand/farrice-creative-strategist-portfolio/90-exports/Farrice-Cain-Creative-Strategist-Portfolio.pdf`

Local site preview:

`http://127.0.0.1:8765`

## To Make It A Functional Public Site

This is already a static website. It can be published to:

- Netlify
- Vercel
- GitHub Pages
- a custom domain

Publishing is an external write, so Codex should stop for explicit approval before doing it.

Before publishing, build the clean public folder:

`node build-public.mjs`

Publish this folder, not the editor folder:

`_active/farrice-brand/farrice-creative-strategist-portfolio/dist/`

## To Edit Text Before Publishing

Use the local editor:

`http://127.0.0.1:8766/editor.html`

The editor saves text changes into:

`_active/farrice-brand/farrice-creative-strategist-portfolio/01-source/site-edits.json`

After editing, regenerate the PDF before sending it.

## Prompt To Publish

```text
Publish the recruiter portfolio as a live static site.

Project folder: _active/farrice-brand/farrice-creative-strategist-portfolio/
Preferred host: [Netlify | Vercel | GitHub Pages | advise me]
URL preference: [custom domain if any]

Before publishing, verify desktop, mobile, PDF export, and no face-cropping.
Stop before any paid step or DNS/custom-domain change unless I approve it.
```

## Prompt For Text Changes

```text
Update the recruiter portfolio text.

Section: [hero | proof-lens | about | ad-script | hooks | brief | analysis | roadmap | interview | footer]
Replace: "[current text]"
With: "[new text]"

Keep the layout, face-safe image cropping, and PDF export intact.
Regenerate the PDF after patching.
```
