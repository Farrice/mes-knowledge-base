# CMS-Backed Portfolio Deployment Guide

## What This Gives You

This turns the portfolio into a simple CMS-backed site:

- public visitors see the normal portfolio
- you open `/?edit=1` to edit text in place
- saved edits write to `site-edits.json`
- the site applies those edits on every page load
- the editor can regenerate the PDF

## Best Use

Use this when you want to edit after publishing without asking Codex to patch files every time.

## Local Command

```bash
node editor-server.mjs
```

Open:

`http://127.0.0.1:8766/editor.html`

## Hosted Command

For a real public deployment, run the Node server with a token:

```bash
HOST=0.0.0.0 PORT=8766 CMS_TOKEN="choose-a-long-private-token" node editor-server.mjs
```

Open the editor at:

`https://your-domain.com/?edit=1`

Then click **Set CMS token** and paste the same token.

## Hosting Requirements

This needs a host that can run a persistent Node process and write files, such as:

- Render
- Railway
- Fly.io
- a VPS

Static-only hosts such as plain GitHub Pages cannot save edits after publishing. Netlify and Vercel need a database/serverless adapter for true CMS behavior.

## Security Boundary

- The write endpoints require `CMS_TOKEN` when deployed with that environment variable.
- Do not share the token with recruiters.
- Do not publish the local project folder to a static host if you do not want `editor.html` visible.
- For static publishing, run `node build-public.mjs` and publish `dist/`.

## Recommended Workflow

1. Edit locally with `http://127.0.0.1:8766/editor.html`.
2. Click **Regenerate PDF**.
3. Run `node build-public.mjs` for a static version, or deploy the Node server for CMS-backed editing.
4. Send recruiters the public URL and the PDF.
