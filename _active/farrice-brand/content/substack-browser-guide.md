# Substack Publication Setup — Complete Browser Automation Guide

Paste this entire prompt into Claude at claude.ai (or any AI browser agent). It will walk you through every click, field, and setting to launch a professional Substack publication from scratch.

---

## HOW TO USE THIS GUIDE

I'm going to walk you through setting up your Substack publication step by step. You'll need two things open:

1. **This guide** (for the instructions)
2. **Your Substack setup content file** (for the exact text to paste into each field — that's `substack-profile-complete.md`)

At each step, I'll tell you:
- Exactly what to click
- What you should see on screen
- What to paste (marked as `[CONTENT FROM SETUP FILE — Section X]`)
- What it should look like when done
- Common mistakes to avoid

Tell me what you see on your screen right now and I'll guide you from there.

---

## SECTION 1: SUBSTACK NAVIGATION MAP (2026 Dashboard)

The Substack dashboard (as of 2026) has ALL navigation on the **left sidebar**. There is no top navigation bar for settings anymore. Here is the complete map:

```
LEFT SIDEBAR (your dashboard)
├── [Publication name dropdown] ← top of sidebar, switch between publications
├── Website ← opens your public-facing site in new tab
├── Create new ← new post, video, audio, note, chat, live video
│
├── CONTENT
│   ├── Posts (Published / Scheduled / Drafts)
│   ├── Podcast
│   └── Chat
│
├── SUBSCRIBERS
│   ├── Subscribers
│   └── Growth
│
├── STATS
│   └── Stats
│
├── CREATOR TOOLS
│   ├── Payments
│   ├── Recommendations
│   └── Branding ← opens the Theme/Website Editor
│
├── SUPPORT & SETTINGS
│   └── Settings ← THE MAIN HUB (at the very bottom of sidebar)
│
└── [Your avatar/profile] ← bottom-left or top-right, for personal profile
```

### INSIDE SETTINGS (left sidebar within Settings page)

When you click **Settings**, you get a new left sidebar with these sections:

```
SETTINGS LEFT SIDEBAR
├── BASICS
│   ├── Publication name
│   ├── Publication URL / Subdomain
│   ├── Short description (tagline, 255 char max)
│   ├── Categories (primary + secondary)
│   ├── Language
│   └── About page → "Edit" button (opens rich text editor)
│
├── PAYMENTS
│   ├── Connect Stripe
│   ├── Monthly / Annual pricing
│   └── Paid benefits description
│
├── APPEARANCE
│   ├── Website
│   │   ├── Publication logo (square, 256x256 min)
│   │   ├── Cover photo (600x600 min)
│   │   ├── Wordmark (1344x256 min)
│   │   ├── Short description display toggle
│   │   ├── Go to Website Theme Editor → opens visual editor
│   │   ├── Navigation bar links (add/remove/reorder)
│   │   ├── Homepage links (sidebar links)
│   │   ├── About page (also accessible from Basics)
│   │   └── Custom pages
│   ├── Welcome page (what first-time visitors see)
│   └── Branding → Theme Editor (colors, fonts, layout)
│
├── CONTENT
│   ├── Emails
│   │   ├── Email header / footer (edit)
│   │   └── Welcome emails
│   │       ├── Welcome email to new subscribers → "Edit"
│   │       ├── Welcome email to imported subscribers → "Edit"
│   │       ├── (If payments on) Welcome email to paid subscribers
│   │       └── (If payments on) Welcome email to founding subscribers
│   ├── Community & Chat
│   ├── Live video
│   ├── Podcasts
│   └── Sections
│
├── ADMINISTRATION
│   ├── Team
│   ├── Privacy
│   ├── Notifications
│   └── Connected accounts
│
└── ADVANCED
    ├── Domain (custom domain)
    ├── Analytics (Google Search Console, etc.)
    ├── Details
    └── Import/Export
```

### PERSONAL PROFILE (separate from publication)

Your personal profile is NOT in publication settings. To find it:
- Click your **avatar/profile picture** (usually bottom-left of sidebar or top-right)
- Select **"Settings"** or **"Edit profile"**
- This takes you to `substack.com/settings` (your personal account settings)
- Here you can edit: Name, Handle, Bio, Profile photo, Theme color

---

## SECTION 2: STEP-BY-STEP SETUP WALKTHROUGH

### PHASE A: Account Creation (skip if you already have an account)

**Step A1: Create your Substack account**
1. Go to `substack.com`
2. Click **"Start publishing"** (or **"Get started"** — large button, usually center of page)
3. Enter your email address and create a password (or sign in with Google/Apple/Twitter)
4. You'll be asked to follow some topics and writers — you can skip this for now by clicking **"Skip"** or scrolling to the bottom

**Step A2: Create your publication**
1. After account creation, Substack will prompt you to create a publication
2. If not prompted: click the **three-line menu** (bottom-left) → **"Settings"** → **"Create publication"** or **"Create another publication"**
3. You'll see these fields:
   - **Your name** → Enter your personal name (e.g., "Farrice Cain")
   - **Publication name** → `[CONTENT FROM SETUP FILE — Section 1: Publication Name]`
   - **Handle/URL** → `[CONTENT FROM SETUP FILE — Section 2: Publication URL]` (this becomes yourname.substack.com)
   - **What's your publication about?** → `[CONTENT FROM SETUP FILE — Section 3: Short Description]`
4. Upload a profile picture if prompted
5. Click **"Create"** or **"Continue"**

> **PITFALL:** Your URL/handle can only be changed ONCE after creation. Triple-check the spelling before confirming. Lowercase letters, no spaces, no special characters.

> **PITFALL:** If you see "This URL is already taken," try a slight variation. But your first choice should be the clean publication name.

---

### PHASE B: Publication Basics (Settings > Basics)

**Step B1: Navigate to Settings**
1. Look at the **left sidebar** of your dashboard
2. Scroll to the very bottom
3. Click **"Settings"** (under "Support & Settings")
4. You should now see the Settings page with its own left sidebar

**Step B2: Publication Name**
1. You should already be in the **"Basics"** section (it's the default when you open Settings)
2. Find the field labeled **"Publication name"**
3. If it's not already set, type: `[CONTENT FROM SETUP FILE — Section 1]`
4. This can be changed later, but consistency matters

**Step B3: Short Description / Tagline**
1. Still in Basics, find **"Publication short description"** (sometimes labeled "What's it about?" or "Tagline")
2. This field has a **255 character limit**
3. Paste: `[CONTENT FROM SETUP FILE — Section 3: Short Description]`
4. Verify the character count — if you see a counter, make sure you're under 255

> **PITFALL:** This short description appears under your publication name on the homepage AND in Substack's search/recommendations. It is NOT the same as the About page. Keep it tight.

**Step B4: Categories**
1. Still in Basics, find **"Categories"**
2. Select a **primary category** that best fits your publication
3. Optionally select a **secondary category**
4. Note: once you select a primary category, you cannot go back to having none selected

> **TIP:** Your primary category matters more than secondary — it determines which Substack recommendation lists you appear on.

**Step B5: About Page**
1. Still in Basics (or go to Settings > Appearance > Website), find **"About page"**
2. Click the **"Edit"** button next to it
3. This opens a **rich text editor** (like writing a post — bold, italic, headings, links, images all work)
4. **Clear any default/placeholder text** that Substack pre-filled
5. Paste: `[CONTENT FROM SETUP FILE — Section 4: About Page]`
6. Format the text:
   - Make the opening line bold (if indicated in your content file)
   - Use line breaks between paragraphs
   - Bold any key phrases as indicated
7. **CRITICAL: Click "Save" at the bottom** before navigating away
8. If you try to leave without saving, you'll see an "Unsaved changes" warning — click Save

> **PITFALL:** The About page is a SEPARATE page from the short description. The short description is 255 chars max and shows everywhere. The About page is unlimited length and lives at yourdomain.substack.com/about. Many people confuse these two.

> **PITFALL:** If you just close the editor without clicking Save, your changes are LOST. Always hit Save.

> **VERIFICATION:** After saving, open a new tab and go to `yourdomain.substack.com/about` to confirm your content is live.

---

### PHASE C: Personal Profile (Separate from Publication)

**Step C1: Navigate to your personal profile settings**

This is NOT in publication settings. Do one of the following:

- **Option A:** Click your **avatar/profile picture** in the sidebar (usually bottom-left or top-right) → Click **"Settings"** or **"Edit profile"**
- **Option B:** Go directly to `substack.com/settings` in your browser
- **Option C:** From the dashboard sidebar, click your name at the very top or bottom → look for **"Profile"** or **"Account settings"**

**Step C2: Edit your bio**
1. You should see fields for: Name, Handle, Bio, Profile photo
2. Find the **"Bio"** field
3. Paste: `[CONTENT FROM SETUP FILE — Section 5: Author Bio]`
4. This is a SHORT bio — it appears next to your name on posts and in the Substack app
5. Click **"Save"**

**Step C3: Profile photo**
1. Click on your current profile photo or the upload area
2. Upload a clear, friendly headshot
3. This appears as a **circle crop** — make sure your face is centered

**Step C4: Profile theme (optional)**
1. You may see an option to set a **profile theme color**
2. Pick something that matches your publication's brand
3. Save

> **PITFALL:** Your personal profile bio is different from the publication's About page. The bio is short (1-2 sentences), the About page is long-form. Both are visible to readers but in different places.

---

### PHASE D: Welcome Email Setup

**Step D1: Navigate to email settings**
1. Go to **Settings** (bottom of left sidebar)
2. In the Settings left sidebar, look under the **"Content"** heading
3. Click **"Emails"**
4. Scroll down to the section labeled **"Welcome emails"**

**Step D2: Edit the welcome email for new subscribers**
1. You'll see **"Welcome email to new subscribers"** with an **"Edit"** button
2. Click **"Edit"**
3. This opens an email editor with two fields:
   - **Subject line** → Clear the default and paste: `[CONTENT FROM SETUP FILE — Section 6: Welcome Email Subject]`
   - **Email body** → Clear the default text and paste: `[CONTENT FROM SETUP FILE — Section 6: Welcome Email Body]`
4. You can format the body text (bold, italic, links, etc.)
5. You may see a **"Button" dropdown** — this lets you add action buttons (like "Read latest post" or "Subscribe"). Optional but nice to have.
6. **Click "Save"** in the upper right corner

**Step D3: Edit the welcome email for imported subscribers**
1. Go back to the Welcome emails section
2. Click **"Edit"** next to **"Welcome email to imported subscribers"**
3. Substack sometimes auto-copies your new subscriber email here — verify the content is correct
4. If blank, paste the same content (or a slightly modified version acknowledging they were imported)
5. **Click "Save"**

> **PITFALL:** There's a difference between the Welcome PAGE (what visitors see on your site) and the Welcome EMAIL (sent to inboxes). You're editing the EMAIL here. The Welcome Page is under Settings > Appearance > Welcome page.

> **TIP:** Welcome emails have 60-80% open rates — the highest of any email you'll send. Make it count. Keep it under 200 words for best engagement.

---

### PHASE E: Email Header & Footer

**Step E1: Navigate to email header/footer**
1. Still in **Settings > Emails** (or Settings > Content > Emails)
2. Look for **"Edit header and footer"** or separate **"Header"** and **"Footer"** options
3. Click **"Edit"** on the header

**Step E2: Set email header**
1. You can upload a **header image** (your publication logo works well)
2. Or leave it as the default Substack header
3. Keep it clean — a simple logo or wordmark is enough
4. **Click "Save"**

**Step E3: Set email footer**
1. Click **"Edit"** on the footer
2. This is a good place to add: social media links, a one-line CTA, or your publication tagline
3. **Click "Save"**

---

### PHASE F: Payments / Paid Tier (Optional — skip if launching free-only)

**Step F1: Navigate to payment settings**
1. Go to **Settings** → click **"Payments"** in the left sidebar
2. Or from the dashboard sidebar: **Creator Tools > Payments**

**Step F2: Connect Stripe**
1. Click **"Set up payments"** or **"Connect Stripe"**
2. You'll be redirected to Stripe's website
3. If you don't have a Stripe account, create one (you'll need: email, bank account/debit card, SSN for tax purposes, address)
4. Complete the Stripe onboarding and you'll be redirected back to Substack
5. Stripe connection may take a few minutes to verify

**Step F3: Set pricing**
1. Once Stripe is connected, you'll see pricing fields:
   - **Monthly price** → `[CONTENT FROM SETUP FILE — Section 7: Paid Tier Monthly]`
   - **Annual price** → `[CONTENT FROM SETUP FILE — Section 7: Paid Tier Annual]`
2. Set both prices
3. Click **"Save"**

**Step F4: Paid benefits description**
1. You may see a field for describing what paid subscribers get
2. Paste: `[CONTENT FROM SETUP FILE — Section 7: Paid Benefits]`
3. Click **"Save"**

> **NOTE:** Once payments are turned on, you'll also see additional welcome email options for Paid subscribers and Founding subscribers in the Emails section. Go back to Phase D and set those up too.

---

### PHASE G: Website Theme & Branding

**Step G1: Open the Theme Editor**

Two ways to get there:
- **Option A:** Dashboard sidebar → **Creator Tools > Branding** → this opens the Theme Editor directly
- **Option B:** Settings → Appearance → Website → click **"Go to Website Theme Editor"** or **"Customize"**

**Step G2: The Theme Editor interface**

You'll see a **visual preview** of your site on the right, and editing panels on the left. The left panel has these tabs/sections:

```
THEME EDITOR LEFT PANEL
├── Homepage
│   ├── Header (logo, wordmark, navigation layout)
│   ├── Hero (how top posts display: Feature/Magazine/Newspaper/Highlight/Media Feature)
│   ├── Body (posts layout: List/Grid/Groups)
│   └── Footer (columns, social buttons)
├── Welcome page (what first-time visitors see)
├── Posts (typography, drop caps, bylines, read-aloud voice)
└── Podcast (if applicable)

THEME SETTINGS (accessible from within editor)
├── Branding
│   ├── Logo
│   └── Publication Wordmark
├── Colors
│   ├── Web background color
│   └── Accent color (buttons, links, pull quotes)
├── Typography
│   ├── Heading font (options: Default, Fancy Serif, Sans, Heavy Sans, Mono, Slab)
│   └── Body font
├── Image settings
│   ├── Cropping (Smart crop vs Center)
│   └── Corner rounding (None, Small, Medium, Large, "Absurd")
└── Link styles
```

**Step G3: Set your brand colors**
1. In the Theme Editor, find **Colors** (or **Branding**)
2. Set your **accent color** — this affects buttons, links, pull quotes
3. Set your **background color** — white/off-white is safest for readability
4. Changes preview in real-time on the right side

**Step G4: Set typography**
1. Find **Typography**
2. Choose a **heading font** — Substack offers limited but quality options
3. Choose a **body font** (or leave default — the default is very readable)

**Step G5: Upload your logo**
1. Find **Logo** in Branding
2. Upload a square image, at least 256x256 pixels, transparent background preferred
3. This appears in the navigation bar and as your favicon

**Step G6: Set homepage layout**
1. Click on **Hero** section
2. Choose your layout style:
   - **Feature** — single post, front and center (good for starting out)
   - **Magazine** — five posts displayed (good once you have content)
   - **Newspaper** — eight posts (for high-volume publishers)
   - **Highlight** — one featured + three on the side
   - **Media Feature** — visual-forward single post
3. For your **first launch**, "Feature" is recommended — it showcases your one post beautifully

**Step G7: Set posts body layout**
1. Click on **Body** (below Hero)
2. Choose **List** or **Grid**
   - List = clean, traditional newsletter look
   - Grid = more visual, shows post images prominently
3. For text-heavy publications, **List** is usually better

**Step G8: Configure the footer**
1. Click on **Footer**
2. Choose: No footer, Centered, 2-column, or 3-column
3. Add social media links if desired

**Step G9: Save and exit**
1. Click **"Done"** in the Theme Editor
2. This auto-saves your changes
3. Visit your site (`yourdomain.substack.com`) to verify

> **PITFALL:** Changes in the Theme Editor preview in real-time, but ONLY save when you click "Done." If you close the browser tab without clicking Done, changes may be lost.

---

### PHASE H: Welcome Page (different from Welcome Email)

The **Welcome Page** is what people see when they visit your Substack for the FIRST time (before subscribing). It's basically your landing page / subscription page.

**Step H1: Navigate to Welcome Page settings**
- **Option A:** In the Theme Editor (Phase G), click **"Welcome page"** in the left panel
- **Option B:** Settings → Appearance → **"Welcome page"**

**Step H2: Set your Welcome Page photo**
1. You can upload a **welcome photo** — this appears as a large hero image
2. Use a high-quality image that represents your publication's vibe
3. Recommended: at least 600x600 pixels

**Step H3: Review Welcome Page content**
1. The Welcome Page automatically pulls your publication name and short description
2. It shows a subscribe button/form
3. You can optionally add additional text or customize the layout
4. Click the **three dots** (if available) → **"Edit"** to customize further

---

### PHASE I: Navigation Bar Configuration

**Step I1: Navigate to navigation settings**
1. Go to **Settings → Appearance → Website**
2. Scroll down to **"Navigation bar links"** (or find it under "Pages and Navigation")

**Step I2: Review default navigation items**

By default, your nav bar includes (in this fixed order, left to right):
- **Home** — always present, cannot be renamed
- **Podcast** — toggle on/off
- **Notes** — toggle on/off
- **Chat** — toggle on/off
- **Archive** — toggle on/off (KEEP THIS ON — readers use it)
- **About** — toggle on/off (KEEP THIS ON — it's your sales page)

**Step I3: Toggle unnecessary items off**
1. Each default item has a **toggle switch**
2. Turn OFF anything you're not using yet:
   - **Podcast** — off (unless you're launching a podcast)
   - **Chat** — off (unless you want a community chat)
   - **Notes** — your call (Notes is Substack's social feed)
3. Keep **Archive** and **About** ON

**Step I4: Add custom links (optional)**
1. Click **"Add"** or **"Add item"** to add a custom navigation link
2. Enter a **Title** (what appears in the nav bar) and a **URL**
3. Useful for: linking to your main website, social media, a "Start Here" post

> **TIP:** Don't overload your nav bar. 4-6 items max. A cluttered nav bar confuses visitors.

---

## SECTION 3: PUBLISHING YOUR FIRST POST

### Step P1: Create a new post
1. In the dashboard left sidebar, click **"Create new"** (or the **"+"** icon)
2. Select **"Text post"** (this is your standard article/newsletter)
3. You'll see the Substack editor with three main areas:
   - **Title** field (large text at the top)
   - **Subtitle** field (smaller text below title — optional but recommended)
   - **Body** area (the main writing area below)

### Step P2: Choose a section (if applicable)
1. At the very top of the editor, you may see **"Choose a section"**
2. If you haven't created sections yet, skip this
3. If you have sections, select the appropriate one

### Step P3: Enter your title
1. Click the **Title** field
2. Type or paste your post title: `[CONTENT FROM SETUP FILE — First Post Title]`
3. Keep it under 60 characters for best email subject line performance

### Step P4: Enter your subtitle
1. Click the **Subtitle** field (below the title)
2. Type or paste: `[CONTENT FROM SETUP FILE — First Post Subtitle]`
3. The subtitle appears below the title in emails and on the web
4. It also auto-fills the SEO description if you don't set a custom one

### Step P5: Write/paste your post body
1. Click in the body area and paste your post content
2. Format using the toolbar:
   - **Bold**, *Italic*, ~~Strikethrough~~
   - Heading 1, Heading 2, Heading 3 (use H2 for main sections, H3 for subsections)
   - Bullet lists, numbered lists
   - Links (highlight text → click link icon → paste URL)
   - Images (click the "+" or image icon → upload)
   - Dividers (horizontal line between sections — great for visual breathing room)
   - Pull quotes
   - Subscribe button widget (use the "+" insert menu to add mid-post)
   - Share button
3. Add a **subscribe call-to-action** within the body (not just at the end) using the Subscribe button widget

> **TIP FROM EXPERTS:** Don't write inside Substack's editor for long pieces. Write in Google Docs or Notion first, then copy-paste into Substack and fix formatting. This prevents losing work to browser crashes.

### Step P6: Add a post image
1. Add at least one image to your post (it becomes the social preview default)
2. Click the image → click three dots → add **alt text** for accessibility
3. If you want a specific social preview image, you'll set that in post settings (Step P8)

### Step P7: Preview your post
1. Click **"Preview"** (usually top-right area of editor)
2. Check how it looks as both an email and a web post
3. Click **"Done"** to return to editing

### Step P8: Configure post settings (IMPORTANT)
1. Click the **settings/gear icon** (bottom-right of the editor, or look for "Settings" button)
2. You'll see a settings panel with:

**Audience:**
- **"This post is for: Everyone"** or **"Paid subscribers only"**
- For your first post: select **"Everyone"** (free)

**Comments:**
- **"Allow comments from: Everyone"** or **"No one"**
- Recommended: **"Everyone"** (engagement helps growth)

**Tags:**
- Add relevant tags (e.g., "welcome," "manifesto," or your content topics)
- Tags help organize posts on your homepage

**Social Preview:**
- **Preview image** — click to change (upload a custom image or select from post images)
- **Preview title** — auto-filled from post title
- **Preview description** — auto-filled from subtitle

**SEO Options** (scroll to the BOTTOM of settings — easy to miss):
1. Toggle **"SEO options"** to expand
2. **SEO Title** — auto-filled from post title. Customize if you want a different title for Google (keep under 60 characters)
3. **SEO Description** — auto-filled from subtitle. Write a compelling 150-160 character description with your target keyword
4. **Post URL** — auto-generated from title. You CAN customize this:
   - Use lowercase, hyphens between words
   - Include your main keyword
   - Keep it short (3-5 words)
   - Example: `welcome-to-parallax` instead of the auto-generated slug
5. **IMPORTANT: Click "Save" on SEO settings before clicking into other settings** — or changes may not persist

> **CRITICAL:** NEVER change the Post URL after publishing. It breaks all existing links, damages SEO, and confuses subscribers. Get it right before you publish.

### Step P9: Publish
1. Click **"Continue"** (top-right of editor) — this opens the publish panel
2. You'll see a final review screen with:
   - **Audience** — confirm "Everyone" (free)
   - **Comments** — confirm your preference
   - **Email delivery toggle** — make sure **"Send to email subscribers"** is ON (checked)
     - If you see an option to "Publish to web only" vs "Send and publish" — choose **"Send and publish"**
   - **Schedule** — you can schedule for later or send immediately
3. To publish immediately: click **"Send to everyone now"**
4. Substack will ask: **"Publish without buttons"** or **"Add subscription button"**
   - Choose **"Add subscription button"** — this adds a subscribe CTA to your post for non-subscribers who discover it via search or social
5. Your post is now LIVE and emailed to all subscribers

> **PITFALL:** If you uncheck the email delivery toggle, your post goes to the web but does NOT email anyone. For your first post, you want BOTH web + email. Double-check this.

> **TIP:** After publishing, Substack will offer you sharing options (Twitter/X, Facebook, Instagram, LinkedIn, copy link, share as image). Share it everywhere immediately — the first 24 hours matter for algorithmic reach.

---

## SECTION 4: POST-PUBLISH CHECKLIST

Run through each of these within 30 minutes of publishing:

### Verify the About Page
- [ ] Open `yourdomain.substack.com/about` in a new tab
- [ ] Confirm all your content is there and formatted correctly
- [ ] Check it on mobile (pull up on your phone)
- [ ] Verify bold text, line breaks, and any formatting came through

### Verify the Welcome Email
- [ ] Open a private/incognito browser window
- [ ] Go to `yourdomain.substack.com`
- [ ] Subscribe with a secondary email address (one you can check)
- [ ] Check that email inbox for the welcome email
- [ ] Verify the subject line and body match what you set up
- [ ] Check it renders correctly on mobile

### Verify Your First Post
- [ ] Open `yourdomain.substack.com` — your post should be the first/featured item
- [ ] Click into the post and read through it on the web
- [ ] Check your primary email — you should have received the post as an email
- [ ] Open the email on your phone — check formatting, images, readability
- [ ] Verify the subscribe button appears in the post (if you chose that option)
- [ ] Click the "Archive" tab — your post should appear there

### Verify Your Profile
- [ ] Click your author name on the post — it should show your bio
- [ ] Visit `substack.com/@yourhandle` to see your public profile
- [ ] Confirm your bio, photo, and name are correct

### Verify Navigation
- [ ] Check the navigation bar at the top of your publication site
- [ ] Confirm "Home," "Archive," and "About" are visible
- [ ] Confirm any items you toggled off (Podcast, Chat) are NOT showing
- [ ] Click each nav item to confirm it works

### Check SEO
- [ ] Google your publication name — it may not show up immediately (can take days/weeks)
- [ ] Open your published post → right-click → "View Page Source" → search for your SEO title and description in the HTML
- [ ] Share the post URL on a messaging app to yourself — verify the social preview (image, title, description) looks correct

### Mobile Check
- [ ] Pull up your Substack on your phone's browser
- [ ] Check: homepage, about page, your first post, navigation
- [ ] Open the post email on your phone
- [ ] Everything should be readable without horizontal scrolling

---

## SECTION 5: TROUBLESHOOTING

### "I can't find Settings"
The Settings link is at the very BOTTOM of the left sidebar. You may need to scroll down past all the other menu items. Look under "Support & Settings."

### "I can't find the About page editor"
Two paths: (1) Settings → Basics → scroll down to "About page" → click "Edit." (2) Settings → Appearance → Website → find "About page" → click "Edit." (3) Go to `yourdomain.substack.com/about` directly and look for an "Edit page" option if you're logged in.

### "I can't find the Welcome email settings"
Settings → Content → Emails (in the left sidebar within Settings) → scroll down past email header/footer to "Welcome emails."

### "My changes aren't saving"
- Make sure you click the **"Save"** button (usually bottom of page or top-right)
- For the Theme Editor, click **"Done"** to save all changes
- For SEO settings within a post, save them BEFORE navigating to other settings panels
- Check your internet connection
- Try refreshing the page and re-entering

### "Character limit error on the short description"
The short description/tagline field has a 255-character limit. Count your characters (paste into a character counter website if needed). Cut words, not meaning.

### "My post didn't send as an email"
- You may have unchecked the email delivery toggle during publishing
- Check: did you click "Publish to web only" instead of "Send to everyone"?
- Fix: You CANNOT re-send a published post as an email. You would need to duplicate the post (copy content → new post → publish as email)

### "My About page shows default Substack text"
You either didn't edit it, or you forgot to click Save. Go to Settings → Basics → About page → Edit → paste your content → SAVE.

### "I can't see my publication when I search Substack"
New publications take time to appear in Substack's search index. This is normal. It can take several days to a few weeks. Publishing consistent content speeds this up.

### "The social preview image is wrong"
Go to your post → Settings (gear icon) → Social Preview → click on the image → upload the correct image → Save. Then re-share the link (social platforms cache preview images, so you may need to use a cache-clearing tool or wait for the cache to expire).

### "I'm seeing the old dashboard layout"
Substack rolled out a new dashboard in 2025. If you see the old layout with top navigation, look for a **"Switch to new dashboard"** option, or check if there's a toggle. The new layout has everything in the left sidebar.

### "Where is the SEO options section in post settings?"
It's hidden at the very BOTTOM of the post settings panel. Click the gear/settings icon in the post editor, then scroll ALL the way down. You should see a collapsible section labeled "SEO options" — click it to expand.

---

## SECTION 6: SETTINGS YOU SHOULD CONFIGURE BUT MIGHT FORGET

These aren't urgent for launch but should be done within your first week:

### Google Search Console verification
1. Settings → Advanced → Analytics
2. Paste your Google Search Console HTML meta tag verification code
3. Go back to Google Search Console and click Verify
4. Then: Google Search Console → Sitemaps → add `sitemap.xml` → Submit

### Custom email header
1. Settings → Content → Emails → Edit header
2. Upload your logo or a clean publication banner image
3. This appears at the top of every email you send

### Recommendations
1. Dashboard sidebar → Creator Tools → Recommendations (or Settings → Growth)
2. Add 3-5 publications you genuinely recommend
3. This activates Substack's reciprocal recommendation engine — other publishers may recommend you back

### Pin your best post
1. Go to your published post
2. Click the three dots (...)  → **"Pin to top"** or **"Feature"**
3. This makes it the hero post on your homepage — visitors see it first

### Social preview image for the publication
1. Settings → Appearance → Website → look for **"Social preview image"**
2. Upload an image (recommended: 1456x1048 pixels, 14:10 aspect ratio)
3. This is what shows when someone shares your homepage URL (not a specific post)

---

## QUICK REFERENCE: WHAT GOES WHERE

| Content | Where It Lives | How to Get There |
|---------|---------------|-----------------|
| Publication name | Settings > Basics | Settings (bottom of sidebar) |
| Tagline / Short description | Settings > Basics | 255 char limit |
| About page (long-form) | Settings > Basics > About page > Edit | Rich text editor, no char limit |
| Author bio (short) | Personal Profile > Settings | Click avatar → Settings/Edit profile |
| Welcome email (new subscribers) | Settings > Content > Emails > Welcome emails | Subject + body editor |
| Welcome email (imported) | Settings > Content > Emails > Welcome emails | Separate from new sub email |
| Paid tier pricing | Settings > Payments | Requires Stripe connection |
| Logo & branding | Theme Editor (Branding tab) | Creator Tools > Branding, or Settings > Appearance |
| Colors & fonts | Theme Editor | Same as above |
| Homepage layout | Theme Editor > Homepage > Hero | Feature/Magazine/Newspaper |
| Navigation bar | Settings > Appearance > Website > Navigation bar links | Toggle items on/off, add custom links |
| SEO for posts | Post editor > Settings (gear) > scroll to bottom > SEO options | Per-post, set before publishing |
| Welcome page (landing) | Settings > Appearance > Welcome page | What first-time visitors see |
| Email header/footer | Settings > Content > Emails > Edit header/footer | Appears on all emails |

---

## YOU'RE DONE

If you've completed Phases A through I and published your first post, your Substack is professionally set up. Here's what you have:

- A named publication with a clear tagline
- A compelling About page that sells the subscription
- A personal profile with your bio and photo
- A welcome email that greets new subscribers
- Brand colors and typography that feel intentional
- A clean navigation bar
- Your first post — published, emailed, and live on the web
- SEO configured for discoverability

Your next priorities:
1. Share your first post everywhere (social media, messaging apps, email signature)
2. Publish your second post within 3-7 days (consistency signals commitment)
3. Set up Google Search Console (Section 6 above)
4. Add recommendations to activate Substack's growth engine
5. Write 3-5 posts before worrying about any paid tier
