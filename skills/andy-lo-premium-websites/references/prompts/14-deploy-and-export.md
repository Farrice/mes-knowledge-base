---
name: deploy-and-export
description: Deploy to Netlify/Vercel or export for any hosting platform
---

# Deploy and Export

## Purpose
Take a completed website project and deploy it to production. Covers Netlify (primary), Vercel (alternative), and generic export for any hosting platform. Includes custom domain setup and social sharing optimization.

## System Prompt

You are Andy Lo. Deployment isn't an afterthought — it's the moment of truth. You build with export-ready architecture so projects can move between environments without restructuring. You always verify the production build matches the development preview.

## User Prompt

```
Deploy my completed website to production.

**Project:** {{PROJECT_NAME}}
**Build tool:** {{BUILD_TOOL}} (Vite / Create React App / static HTML)
**Custom domain:** {{DOMAIN}} (optional)
**Preferred host:** {{HOST}} (Netlify / Vercel / other)

**Deployment Protocol:**

### Option 1: Netlify (Recommended)

#### Direct Upload
1. Build the production bundle:
   ```
   npm run build
   ```
2. Navigate to app.netlify.com → "Add new site" → "Deploy manually"
3. Drag and drop the `/dist` (Vite) or `/build` (CRA) folder
4. Site is live at a `.netlify.app` subdomain

#### GitHub Connected (Auto-Deploy)
1. Push project to a GitHub repository
2. In Netlify: "Import from Git" → select your repo
3. Build settings:
   - Build command: `npm run build`
   - Publish directory: `dist` (Vite) or `build` (CRA)
4. Every push to main auto-deploys

### Option 2: Vercel
1. Push to GitHub
2. Import in Vercel dashboard
3. Auto-detects Vite/React → deploys automatically
4. Live at `.vercel.app` subdomain

### Option 3: Firebase Studio Export
1. In Firebase Studio code editor
2. Select all project files
3. Download as ZIP
4. Unzip locally → deploy to any host above

### Option 4: Any Static Host
1. Build production bundle (`npm run build`)
2. Upload contents of `/dist` folder to your host
3. Ensure host serves `index.html` for all routes (SPA routing)

---

### Custom Domain Setup (After Deployment)
1. In your hosting dashboard, go to domain settings
2. Add your custom domain: {{DOMAIN}}
3. Update DNS records at your registrar:
   - **A Record**: Point to host's IP
   - **CNAME**: `www` → your `.netlify.app` or `.vercel.app` URL
4. Enable HTTPS (automatic on Netlify/Vercel)
5. Wait for DNS propagation (up to 48h, usually minutes)

---

### Social Sharing Optimization
Add these meta tags to your `index.html` (or equivalent):
```html
<!-- Primary Meta Tags -->
<title>{{SITE_TITLE}}</title>
<meta name="description" content="{{META_DESCRIPTION}}">

<!-- Open Graph / Facebook -->
<meta property="og:type" content="website">
<meta property="og:url" content="https://{{DOMAIN}}">
<meta property="og:title" content="{{SITE_TITLE}}">
<meta property="og:description" content="{{META_DESCRIPTION}}">
<meta property="og:image" content="{{OG_IMAGE_URL}}">

<!-- Twitter -->
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{{SITE_TITLE}}">
<meta name="twitter:description" content="{{META_DESCRIPTION}}">
<meta name="twitter:image" content="{{OG_IMAGE_URL}}">
```

**Use the hero starting frame as the OG image** — it's already designed to make a strong first impression.

---

### Production Verification
- [ ] Production URL loads correctly
- [ ] All pages render as expected
- [ ] Animations play smoothly
- [ ] CMS content loads (if integrated)
- [ ] Mobile responsive on real devices
- [ ] HTTPS enabled (no mixed content warnings)
- [ ] OG image displays in social media previews
- [ ] Custom domain resolves correctly
- [ ] Page speed: Lighthouse score > 80
- [ ] Console free of errors
```

## Expected Output
- Live, deployed website
- Custom domain configured (if applicable)
- Social sharing optimized
- Production verification completed

## When to Use
- After website assembly is complete (Prompt #3)
- When ready to go live

## Genius Patterns Applied
- Export-Ready Architecture (#12)
- Progressive Polish Protocol (#6)
