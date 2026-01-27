# Attention-to-Value Conversion Engine

> Deploy this prompt to build complete conversion infrastructure that captures viral moments into recruiting, sales, and funding pipelines.

---

## Deployment Prompt

```
You are the Attention-to-Value Conversion Engine, channeling Lulu Cheng Meservey's discipline of treating attention as potential energy that must be immediately converted to business value. Your outputs build complete capture systems BEFORE attention hits.

MY CONVERSION PARAMETERS:
- Anticipated Attention Event: [PRODUCT LAUNCH / VIRAL POST / PRESS COVERAGE / FOUNDER MOMENT]
- Primary Conversion Goal: [RECRUITING / SALES / FUNDRAISING / WAITLIST]
- Secondary Goals: [ANY ADDITIONAL OUTCOMES TO CAPTURE]
- Company/Product: [INSERT]
- Target Audience: [WHO SHOULD CONVERT]
- Current Infrastructure: [WHAT EXISTS ALREADY]
- Timeline: [WHEN DOES ATTENTION HIT]

CONVERSION ARCHITECTURE PROTOCOL:

Execute the following and produce complete capture system:

1. CONVERSION GOAL HIERARCHY
Prioritize what attention should become:
- Primary: [Main outcome]
- Secondary: [Fallback if primary doesn't fit]
- Tertiary: [Capture for future]
Map each goal to specific landing page/funnel

2. 2-CLICK PATH ENGINEERING
Design frictionless paths from attention to action:
- Attention Source → Landing Page → Action Form
- No more than 2 clicks from awareness to commitment
- Mobile-optimized, fast-loading, tracked

3. LANDING PAGE ARCHITECTURE
For each conversion goal, specify:
- Headline that connects to attention source
- 3-5 key elements to include
- Social proof placement
- CTA design and copy
- Form fields (absolute minimum required)
- Confirmation page/message strategy

4. URGENCY MECHANISMS
Build time pressure without manipulation:
- Scarcity signals (real, not fake)
- Momentum indicators (social proof live updating)
- Deadline communication (if applicable)
- FOMO triggers (others are applying/signing up)

5. AUTOMATED CAPTURE SYSTEMS
Post-submission automation:
- Immediate confirmation (what happens next)
- 24-hour follow-up (deepen engagement)
- Drip sequence (for non-immediate converters)
- Retargeting for visitors who didn't convert

6. TRACKING & ATTRIBUTION
Measurement system:
- UTM parameters for all links
- Conversion tracking setup
- Source attribution tracking
- Dashboard for real-time monitoring

7. COMPLETE LANDING PAGE COPY
Full copy for primary conversion page, ready to deploy

OUTPUT:
- Conversion goal hierarchy with paths
- Landing page specifications
- Complete landing page copy (ready to build)
- Automated sequence outlines
- Tracking implementation guide
- Pre-launch checklist

Generate the complete conversion system now.
```

---

## What It Produces

- Complete conversion architecture before attention hits
- Landing page copy ready to deploy
- Automated follow-up sequences
- Tracking and attribution setup
- Real-time monitoring dashboard specs

---

## Example Output: Recruiting Conversion System

**Parameters Used:**
- Event: Founder's "Why I quit my $500K job" post going viral
- Primary Goal: Senior engineer applications
- Secondary: Engineering newsletter signups
- Company: AI infrastructure startup
- Target: FAANG senior engineers
- Timeline: Post going live Tuesday

**Generated Conversion Architecture:**

---

## CONVERSION GOAL HIERARCHY

| Priority | Goal | Landing Page | Friction Level |
|----------|------|--------------|----------------|
| Primary | Job application | /join-us | Medium (deliberate) |
| Secondary | Newsletter signup | /engineering-updates | Low |
| Tertiary | Follow company social | Inline CTAs | Minimal |

---

## 2-CLICK PATH ENGINEERING

**Path 1: Job Application**
Viral Post → [Link in bio/post] → /join-us → Submit application
- 2 clicks to submit
- Mobile form optimized (auto-save, progress indicator)

**Path 2: Newsletter (for not-yet-ready)**
Viral Post → /join-us → [Not ready? Get our engineering newsletter] → Email submit
- 2 clicks to subscribe
- One field (email only)

---

## LANDING PAGE: /join-us

### Headline
"You felt something reading that post. Here's what to do about it."

### Key Elements (in order)

1. **Recognition Hook**
"If you've spent years wondering why you're optimizing ad clicks for a trillion-dollar company when you could be building something that matters—you're not crazy. You're just in the wrong place."

2. **The Opportunity Crystallized**
"We're building [specific thing]. We're 23 people. We have $40M in funding. And we need 5 senior engineers who are angry enough about [problem] to help us solve it."

3. **What We Actually Need**
- Staff-level systems engineers (not 10 years of experience—10 years of caring)
- Infra architects who've built at scale and hated how it was done
- ML engineers who want to work on [specific challenge]

4. **Social Proof**
"Our engineering team came from: [Google] [Meta] [Netflix] [Stripe]. They left for the same reason you're thinking about it."

5. **Anti-Pitch Honesty**
"We're not offering the highest salary. We're not offering the cushiest job. We're offering hard problems, a team that ships, and work you'll actually be proud of in 10 years."

6. **CTA: Simple Application**
FORM:
- Name
- Email
- LinkedIn (or resume upload)
- "Why does building [thing] matter to you?" (100 words max)

7. **For the Not-Ready**
"Not ready to apply? No pressure. Get our engineering newsletter—what we're building, what we're learning, no recruiter spam."
[Email signup]

---

## URGENCY MECHANISMS

- "Currently reviewing applications weekly. Next batch closes Friday."
- Live counter: "47 applications received in the last 24 hours"
- "Our last senior hire came from a viral post like this one. Don't overthink it."
- Social proof update: "Congrats to [Name] who joined from our last post"

---

## AUTOMATED SEQUENCES

**Immediate (Application Submitted):**
```
Subject: We got your application (and we actually read them)

Hey [Name],

This isn't an automated email. Okay, it is, but I'm the one who wrote it.

Your application hit our system. Here's what happens next:
- Week 1: Our eng leads review every application (yes, all of them)
- Week 2: If there's a fit, you'll get a personal email from me or our VP Eng
- Week 3+: Real conversations, not gauntlet interviews

In the meantime, here's what we've shipped this month: [Link]

Thanks for taking the shot.

— [Founder]
```

**48-Hour Follow-Up (Newsletter Signups):**
```
Subject: The post that broke my inbox

So that post went a little viral.

Result: 400+ applications, 2,000 newsletter signups, and my calendar is a disaster for the next two weeks.

But I wanted to share something with you that I didn't put in the post: [Insider content about the mission/challenge]

If you're on the fence about applying, here's what I'd tell you: We're not looking for perfect. We're looking for people who care enough to learn.

[Apply link]

— [Founder]
```

---

## TRACKING IMPLEMENTATION

**UTM Structure:**
- Post link: `?utm_source=twitter&utm_medium=social&utm_campaign=viral-post-jan`
- Bio link: `?utm_source=twitter&utm_medium=bio&utm_campaign=viral-post-jan`
- Newsletter embedded: `?utm_source=landing&utm_medium=newsletter_cta`

**Conversion Events to Track:**
1. Landing page view
2. Form started
3. Form completed
4. Newsletter signup (secondary)
5. Social follow (tertiary)

**Dashboard Metrics:**
- Real-time applicant count
- Conversion rate (views → applications)
- Source breakdown
- Time-on-page
- Drop-off point in form

---

## PRE-LAUNCH CHECKLIST

- [ ] Landing page live and mobile-tested
- [ ] Forms working (submit test application yourself)
- [ ] Tracking pixels firing correctly
- [ ] Automated emails loaded and tested
- [ ] UTM links created for all distribution points
- [ ] Dashboard set up for real-time monitoring
- [ ] Team briefed on response protocols
- [ ] Capacity confirmed (can handle volume)
- [ ] 48-hour follow-up scheduled

---

## SUCCESS METRICS

| Metric | Target | Exceptional |
|--------|--------|-------------|
| View → Application Rate | 2% | 5%+ |
| Applications in 48 hours | 100 | 300+ |
| Newsletter signups | 500 | 1000+ |
| Quality applications (reviewed+) | 20% | 35%+ |
| Time from post to first interview | 7 days | 3 days |
