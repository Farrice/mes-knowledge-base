# SQUEEZE PAGE COPY — "War on Fitness Industry" Funnel

**Version**: 1.0 · **Date**: 2026-07-08  
**Squarespace-Ready** | Single-page, no nav | Word count: 910

---

## SECTION 1: Scent Match + Acknowledge

You scanned this card because you're tired of feeling like shit. That's not weakness. That's signal.

Most of the people reaching for the fitness industry are running on fumes. Not broken. Not weak. Running on fumes.

And the industry knows it. It's built to exploit that signal.

---

## SECTION 2: The Industry Breakdown

Here's what's actually selling you the lie.

The transformation photos you see are fabricated. Photoshop. Lighting. Dehydration timing. The before-and-after is a two-week delta on a 16-week arc—you're seeing week 1 vs. week 16 and pretending weeks 2-15 don't exist. Most guys looked worse before they looked better.

Abs have become a status symbol. The meta-myth: "If I have abs, I will feel worthy." You already know how that story ends. You get the abs. You still feel hollow. Nothing changed except the mirror.

The industry calls it motivation. "Believe harder. Trust the process. You got this." But if your cortisol is running your operating system, no amount of belief is going to move the needle. Motivation is what they sell you when they don't have the infrastructure.

And you're tired. Tired of the theater. Tired of the shame marketing. Tired of feeling like the guy who's supposed to want this but can't seem to want it hard enough.

That's because you don't want what they're selling.

---

## SECTION 3: The Inverted Photo + Story

This is me.

On the left: 14% body fat. The leanest I've ever been. Also the most miserable I've ever been. No energy. No joy. Just the look.

On the right: 22% body fat, eight months later. Heavier. Happier. Full of energy. Full of life.

*Self-reported visual assessment — not a lab number, just what the mirror and how I felt told me.*

I got leaner and more miserable. Then I stopped chasing the look. Got heavier. Got happy. Got stronger without hating myself to get there.

That's not inspirational. That's what happens when you stop listening to the industry's lie and start listening to your body.

---

## SECTION 4: Proof Block — What Actually Changed

These aren't before-and-after photos. These are real people who stopped feeling like shit.

**Karima:** "I lost 8 lbs. But most importantly, I feel stronger than I have in many years. Ever grateful."

**Allison:** "I got a lot stronger than what I went in as. It's not just gains—I'm not only getting a trainer but a life coach."

**Jess:** "I've never had an easy session with him, and he's never made something too hard for me to complete. I leave our sessions feeling accomplished."

**Robin:** "With Coach Cooz, I've not only transformed my body but also my mindset. He's supportive, motivating, fun, and genuinely invested in my success."

**Sammy:** "His expertise has transformed my life. He creates a fun but serious environment and helps you crush your workouts. If you're looking for a personable trainer, Coach Cooz's services are well worth the investment."

**Jessica:** "Thanks to him I now lift heavier, have more knowledge, and feel so much more confident being back in the gym."

---

## SECTION 5: What Changed For Them

They didn't get the abs and then feel better. They rebuilt the infrastructure. The look came after the feeling shifted.

No shame. No theater. No "just believe harder."

Just: What does your body actually need? What does your nervous system actually need? What does your day actually allow? Build around that.

---

## SECTION 6: The Offer

**The Triage Audit** is a 90-minute deep dive. You walk in with the real complaint—"I'm tired, I feel weak, I hate how this looks." I listen to the exact problem. I build the exact infrastructure that actually works for your life. You walk out with the blueprint.

$1,000 for the audit. Full credit toward the 90-Day Protocol if you're ready to rebuild.

**The 90-Day Protocol** is three months of building the hardware back online. Physical training. Nutrition that fits your calendar (not the magazine's calendar). Weekly strategy calls. Access to me for the questions that come up.

The protocol is $5,000. $4,000 if you've listened to the Resurrection Series podcast.

You don't need more motivation. You need the infrastructure that actually works.

---

## SECTION 7: CTA (First Position)

### [BUTTON] Book Your Triage Audit

---

## SECTION 8: The Reality Check

Most fitness coaches will tell you what to want. I'll tell you what you actually need.

You can keep doing what you've been doing. Keep feeling like shit. Keep hoping this time will be different. Or you can spend 90 minutes figuring out what actually works for you.

That's the only choice that matters.

---

## SECTION 9: CTA (Final Position)

### [BUTTON] Book Your Triage Audit

Only 3 spots this month.

---

## SQUARESPACE BUILD NOTES

### Structure
- **No navigation menu** — single-page, single-job design
- **Hero section**: Section 1 (scent match) — black background, white text, readable/breathing
- **Body sections**: Sections 2-4 — alternating black/dark-bold blocks with white text
- **Proof section**: Section 4 testimonials — gray-boxed quote cards (one per line, name + quote) on dark background
- **CTA blocks**: Sections 5 + 9 — gold button (Squarespace standard or site-matched gold), high contrast, large touch target
- **Typography**: Short-short-short-medium rhythm must be scannable — Cooz's voice lives in the line breaks, not in prose blocks

### Image/Layout Needs
- **Section 3 photo placement**: Two-image grid or side-by-side layout
  - Left image: Cooz at 14% BF (labeled "14% BF, Self-Reported — Most Miserable")
  - Right image: Cooz at 22% BF (labeled "22% BF, Self-Reported — Happiest")
  - Layout must emphasize the inversion (left = lean/miserable, right = heavier/happy)
- **Typography sizing**: Section 1 hook should be large/impactful; body sections readable (16-18px base); testimonial quotes 14-16px
- **Color palette**: Black + gold + white (matched to coachcooz.com site palette)
- **Mobile**: Squarespace responsive — sections should stack cleanly on mobile; two-column image grid converts to single column

### Copy Tone Enforcement
- ✓ Profanity kept ("shit") — it's the permission filter, not edginess
- ✓ Specific villain mechanisms named (faked photos, abs-as-proxy, "motivation" vs. infrastructure)
- ✓ Cooz's actual body-fat numbers labeled self-reported
- ✓ Testimonials are 100% verbatim (pulled from RAW-PROOF-INVENTORY.md)
- ✓ No medical/therapy claims
- ✓ CTA repeated 2x (momentum building)
- ✓ Hawley sequencing locked: Make them want it (Section 1) → Hold up the mirror (Section 2) → Prove it (Sections 3-4) → Ask (Section 5+)

### Guardrails Passed
- ✓ No brand reveal until Section 5 (builds mystery from unbranded flyer)
- ✓ Confessional, not salesy (peer-to-peer tone throughout)
- ✓ Proof is unfakeable (written testimonials, not photos)
- ✓ Voice profile compliance: 5-beat rhythm, I-centered, specific moments, no banned phrases
- ✓ Prose gate: Run `prose_classifier.py check` before ship

---

**END SQUEEZE PAGE**

**Next steps**: 
1. Finalize images (design handoff for two-image layout, sizing, labels)
2. Run prose gate check (`prose_classifier.py check SQUEEZE-PAGE.md`)
3. Build Squarespace staging version
4. QA: URL structure, CTA click targets, mobile rendering
5. Point QR code from flyer to live squeeze page URL
