# SamCart Landing Page Assets — Invisible Expert Scorecard
## Everything You Need to Build the Page in 15 Minutes

---

## Quick Setup Guide (SamCart)

1. **Dashboard** → **Pages** → **Create New** → **Lead Capture**
2. Name: "Invisible Expert Scorecard" / Slug: `scorecard`
3. Pick a clean template (minimal — you want ONE action: enter email)
4. Paste the copy below into the relevant sections
5. **Form Settings**: Email only (no name, no phone — maximum conversion)
6. **After Submitting**: Set to **Redirect** → paste your Custom GPT link
7. **App Integrations**: Connect to your email tool (Mailchimp, ConvertKit, etc.) → Add subscriber to "Scorecard Leads" list
8. Publish → copy the URL → paste into LinkedIn comment

---

## Landing Page Copy (Section by Section)

### Headline (H1)
```
How Visible Is Your Expertise?
```

### Subheadline
```
A 3-minute diagnostic for S&C coaches, sports scientists, and performance consultants.
Score yourself. Then get 5 LinkedIn posts built for your sport and methodology.
```

### Body Copy (Keep Short — 3-4 Lines Max)
```
I audited the LinkedIn profiles of coaches who've trained NBA MVPs, Olympic champions, and NFL teams.

6 out of 8 scored 1 out of 9 on content infrastructure.

This scorecard uses the same 9-point framework. It takes 3 minutes, scores your digital visibility, and generates personalized LinkedIn post templates you can use this week.
```

### Form Label (Above Email Field)
```
Enter your email to access the scorecard:
```

### Button Text
```
Score My Visibility
```

### Below-Form Trust Line (Small Text)
```
Free. No spam. Just the scorecard + your personalized templates.
```

---

## Prompt for SamCart's AI Page Builder

If SamCart's AI asks you to describe what you're building, paste this:

```
I'm building a lead capture page for a free interactive scorecard tool aimed at strength and conditioning coaches, sports scientists, and performance consultants.

The scorecard helps them evaluate their digital visibility across 9 dimensions. After entering their email, they get redirected to an interactive experience (Custom GPT) that walks them through the assessment and generates 5 personalized LinkedIn post templates based on their specific sport and coaching methodology.

The tone should be professional and direct — these are serious professionals (PhD-level, 10-25 years experience, work with elite athletes). NOT influencer energy. NOT hype. Think "diagnostic tool from a colleague" not "free webinar from a marketer."

Headline: "How Visible Is Your Expertise?"
Subheadline: "A 3-minute diagnostic for S&C coaches, sports scientists, and performance consultants."
Key stat: "6 out of 8 elite coaches scored 1 out of 9 on content infrastructure."
CTA: "Score My Visibility"
Form: Email only.
Color palette: Clean, professional. Dark backgrounds or muted tones — not bright/flashy.
```

---

## Page Structure (If Building Manually)

```
┌──────────────────────────────────────────┐
│                                          │
│   How Visible Is Your Expertise?         │  ← H1 Headline
│                                          │
│   A 3-minute diagnostic for S&C coaches, │  ← Subheadline
│   sports scientists, and performance     │
│   consultants.                           │
│                                          │
├──────────────────────────────────────────┤
│                                          │
│   I audited the LinkedIn profiles of     │  ← Body (3-4 lines)
│   coaches who've trained NBA MVPs...     │
│   6 out of 8 scored 1 out of 9.         │
│                                          │
├──────────────────────────────────────────┤
│                                          │
│   ┌──────────────────────────────────┐   │
│   │  Enter your email:               │   │  ← Email field
│   │  [________________________]      │   │
│   │                                  │   │
│   │  [ Score My Visibility ]         │   │  ← CTA button
│   └──────────────────────────────────┘   │
│                                          │
│   Free. No spam. Just the scorecard +    │  ← Trust line
│   your personalized templates.           │
│                                          │
└──────────────────────────────────────────┘
```

**That's it.** One section. No scrolling. No testimonials section. No feature lists. The post already did the selling — this page just captures the email and redirects. Don't over-design this.

---

## After-Submit Redirect

**Redirect URL**: [Your Custom GPT link — paste after creating the GPT]

Format: `https://chatgpt.com/g/g-[your-gpt-id]`

The redirect sends them straight into the GPT, which starts the scorecard experience immediately.

---

## Email Automation (Optional but Recommended)

If you connect to an email tool, set up a simple 2-email sequence for the "Scorecard Leads" list:

**Email 1 (Immediate / 1 hour after)**:
- Subject: "Your scorecard link (in case you need it again)"
- Body: "Hey [Name], here's your Invisible Expert Scorecard link: [GPT URL]. If you haven't scored yourself yet — it takes 3 minutes and generates 5 LinkedIn posts built for your sport. Most coaches score between 1 and 3. Where did you land? — Farrice"

**Email 2 (3 days later)**:
- Subject: "What most coaches do after scoring a 2"
- Body: "Most S&C coaches who take the scorecard land between 1 and 3. The number itself doesn't matter as much as what it reveals: the gap isn't talent — it's translation. The coaches I work with typically make 3 changes first: [1] Rewrite LinkedIn headline from credentials to transformation. [2] Post one athlete story this week. [3] Set up email capture before their next speaking gig. If you want help with any of those — or want to see what your content could look like — DM me on LinkedIn or reply to this email. No pitch. Just perspective. — Farrice"

---

## Pixel / Tracking (Optional)

In SamCart's Settings → Pixels and Scripts:
- Add LinkedIn Insight Tag (if you have one) — tracks conversions from the LinkedIn post
- Add Google Analytics / GA4 tag (if you have one)
- Add Meta Pixel (if running ads later)

Not essential for launch. Add later if needed.
