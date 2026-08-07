# LinkedIn Profile Extraction Prompt
## Use: Fire in Gemini browser agent while on Cooz's LinkedIn profile
## Output: Structured dump of current state for V2 profile rebuild

---

## How to Use

1. Open Cooz's LinkedIn profile in Chrome: `linkedin.com/in/coachcooz` (or whatever the actual URL is)
2. Open Gemini browser extension (side panel) on the same page
3. Paste the prompt below
4. Gemini reads the page DOM and returns the structured dump
5. Paste the result back to Farrice → we use it to finalize V2 profile rebuild against actual current state (instead of the inferred state in `01-LINKEDIN-ALGORITHM-AUDIT.md`)

---

## THE PROMPT

```
You are extracting the complete current state of this LinkedIn profile for a strategic profile rebuild. You have full access to the page I'm viewing. Extract EVERY field below verbatim — do not summarize, do not paraphrase, do not interpret. If a field is empty or hidden, say "EMPTY" or "NOT VISIBLE." If a field has multiple entries, list all of them.

Return the output as structured markdown using these exact section headers:

## 1. THE 5 AUTHOR FIELDS (the algorithm-load-bearing fields)
- **Full Name** (verbatim, including any nickname in quotes):
- **Headline** (verbatim, full text — capture all 220 characters if used):
- **Industry** (the dropdown LinkedIn assigned):
- **Current Title** (top-of-Experience-section job title):
- **Current Company** (top-of-Experience-section company name):

## 2. PROFILE PHOTO + BANNER
- **Profile photo description** (describe what's visible: headshot/full-body, attire, background, expression):
- **Banner image description** (describe visual: photo/graphic, any text overlay, color palette, style):
- **Profile photo dimensions** (note if it appears cropped/blurry):

## 3. ABOUT SECTION (verbatim)
Copy the entire About section text VERBATIM. Include line breaks. Include any emoji. Do not summarize. If it's truncated with "see more," click and capture the full text.

## 4. FEATURED SECTION
List every Featured item visible on the profile:
- Item 1: [type — link/post/article/document] | [headline/title] | [description if any] | [thumbnail description]
- Item 2: ...
- (continue for all featured items)

## 5. EXPERIENCE SECTION
For EACH experience entry (current and past):
- **Title**:
- **Company**:
- **Date range**:
- **Location**:
- **Description** (verbatim — full text):
- **Skills associated** (if listed):

## 6. EDUCATION SECTION
For each entry:
- **School**:
- **Degree / Field**:
- **Date range**:
- **Description** (if any):

## 7. SKILLS SECTION
List the top 10-15 skills visible. Note which are pinned to the top of the profile.

## 8. RECOMMENDATIONS
- **Number of recommendations received**:
- **Number of recommendations given**:
- **Most recent received recommendation** (verbatim, including author name and title):

## 9. ACTIVITY / RECENT POSTS
For the 10 most recent posts (or all visible if fewer than 10), capture:
- **Post 1**:
  - Date posted
  - First 50 words verbatim
  - Engagement (likes / comments / reposts visible)
  - Format (text-only / image / carousel / video / link)
  - Post type if obvious (story / framework / hot take / question / case study)
- **Post 2**: ...
- (continue for 10 posts)

If posts are older than 6 weeks, note that LinkedIn appears paused.

## 10. CONNECTIONS + FOLLOWERS
- **Connection count** (visible number):
- **Follower count** (if Creator Mode is on):
- **"Open to work" / "Open to providing services" badge**: [yes/no — if yes, what services]

## 11. CREATOR MODE / PROFILE FEATURES
- **Creator Mode**: [on/off]
- **Hashtags followed** (if visible on Creator dashboard or under name):
- **"Talks about" / "Top of mind topics" tags** (if visible):
- **Newsletter** (if linked):
- **Custom URL** (vanity slug):

## 12. CONTACT INFO + LINKS
- **Email** (if visible):
- **Phone** (if visible):
- **Website** (the public link):
- **Other social links** (Twitter/X, Instagram, YouTube, podcast, etc.):

## 13. ABOUT THE PUBLIC IMPRESSION (your synthesis)
In 3-5 sentences, describe the FIRST IMPRESSION a cold visitor would form from this profile:
- What does the headline make them think this person does?
- What does the About section emphasize most?
- What's the dominant signal: business / coaching / fitness / spiritual / personal-brand / other?
- Is the profile cohesive or scattered?

## 14. ANY ALGORITHMIC RED FLAGS YOU NOTICE
List anything that appears suppressive:
- Vague/vanity headline
- Low engagement on recent posts (relative to follower count)
- Profile photo issues (blurry, cropped weird, off-brand)
- About section opens with "you" or filler
- Posts have story-first openers without topic anchors
- Featured section empty or with placeholder content
- Industry mismatched to actual content topic
- Etc.

## 15. ANY POSITIVE ASSETS WORTH PRESERVING
List anything strong that the rebuild should keep:
- Specific phrases in About that land
- Specific posts that performed well
- Strong recommendations
- Visual assets that are working
- Etc.

---

END OF EXTRACTION. Return the full dump in one response. Do not omit sections.
```

---

## What to Do With the Output

When Cooz (or Farrice) fires this and gets the dump:

1. **Save the output** as `09-LINKEDIN-CURRENT-STATE.md` in the same folder
2. **Compare against `01-LINKEDIN-ALGORITHM-AUDIT.md`** — the audit was inferred. The dump is real. Where they diverge, the dump wins.
3. **Update the V2 profile rebuild** (`05-LINKEDIN-PROFILE-REBUILD.md`) with calibrated truth: actual current headline, actual About content, actual recent posts, actual recommendations.
4. **Re-score the algorithm audit** with real data. The 25/60 score is now testable. If actual is higher (say 35/60), recovery timeline shortens. If lower, the rebuild is even more urgent.

---

## Why This Prompt Is Built This Way

Three design choices worth noting:

1. **Verbatim extraction, no interpretation.** Most LLM extraction prompts ask for "summary" — that's the wrong move when the goal is calibrated rebuild. We need raw input. Gemini's interpretation will color the data. The prompt explicitly forbids it for sections 1-12.

2. **Synthesis is gated to sections 13-15.** Once raw data is captured, we DO want Gemini's read on first-impression, red flags, and assets to preserve. But that synthesis is segregated from the raw extraction — we can ignore it if it's wrong without losing the data.

3. **Section 9 (recent posts) is the highest-value section.** The algorithm audit's biggest gap was "Layer 2: First-50-Word Truncation" — we inferred from voice profile patterns. Real first-50-words from real posts is the calibrated input. If the dump shows Cooz's posts already front-load topic anchors, his Layer 2 score is higher than 3/10 and the rebuild changes.
