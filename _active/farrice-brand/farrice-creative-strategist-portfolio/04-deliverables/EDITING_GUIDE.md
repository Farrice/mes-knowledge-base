# Editing Guide

Use this when you want targeted text changes without digging through the page source.

## Live Local Editor

Run the local editor server, then open:

`http://127.0.0.1:8766/editor.html`

Click **Open live editor**, click any outlined text on the page, edit it in place, then click **Save text**. The changes are saved to:

`../01-source/site-edits.json`

The public portfolio reads that JSON file and applies your saved text automatically.

Important: after text edits, regenerate the PDF so the PDF and site match.

The editor also has **Regenerate PDF**. It saves your text first, then updates:

`../90-exports/Farrice-Cain-Creative-Strategist-Portfolio.pdf`

## How To Ask Codex For Edits

Paste the section id and the exact replacement text:

```text
Update the recruiter portfolio.

File: _active/farrice-brand/farrice-creative-strategist-portfolio/index.html
Section: [hero | proof-lens | about | ad-script | hooks | brief | analysis | roadmap | interview | footer]
Change: Replace "[current text]" with "[new text]".
Keep layout and PDF export working.
Verify desktop, mobile, and PDF after patching.
```

## Section Map

| Section | What It Controls |
|---|---|
| `hero` | First screen headline, intro paragraph, CTA, first portrait |
| `proof-lens` | The four fast proof cards after the hero |
| `about` | Strategy approach and benchmark cards |
| `ad-script` | FolliGuard script and beat sheet |
| `hooks` | FloraBalance hook lab and hook list |
| `brief` | VitalPaws creator brief and dog storyboard |
| `analysis` | Competitor teardown |
| `roadmap` | Four-week creative test plan and charts |
| `interview` | Interview answer and closing CTA |
| `footer` | Claim/disclaimer language |

## CMS-Backed Editing After Publishing

For true after-publish editing, host this as a Node app instead of a static-only site.

Local-only command:

`node editor-server.mjs`

Hosted CMS command pattern:

`HOST=0.0.0.0 PORT=8766 CMS_TOKEN="[choose-a-secret-token]" node editor-server.mjs`

Then open:

`https://your-domain.com/?edit=1`

Click **Set CMS token**, paste the token, edit text, then save.

## Recruiter-Ready Export Options

### Best for a recruiter

Send a live URL plus attach the PDF. The URL feels current and interactive; the PDF protects you if the recruiter forwards it internally.

### What Codex can do locally

- Fix text and layout.
- Generate a PDF.
- Prepare a deploy-ready static folder.
- Create a ZIP if you need to upload it manually.

### What needs explicit approval

- Publishing to Netlify, Vercel, GitHub Pages, or a custom domain.
- Adding real contact info if it is not already supplied.
- Sending anything directly to a recruiter.

## Current Local Preview

`http://127.0.0.1:8765`

## Current Export Target

`_active/farrice-brand/farrice-creative-strategist-portfolio/90-exports/Farrice-Cain-Creative-Strategist-Portfolio.pdf`
