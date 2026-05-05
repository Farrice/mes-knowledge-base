# NOTEBOOK 1 — CONTENT GENERATOR SETUP
## Cooz's daily content engine. Voice memo in → publish-ready post out.

---

## What this notebook does

Cooz drops in a raw voice memo, a 3-paragraph dump of thoughts, or a transcript fragment. The notebook generates a publish-ready LinkedIn post in his voice, in the right lane, with the right opener structure.

Use cases:
- "I just had a great voice memo about [topic]. Generate a Lane 1 post."
- "Turn this 5-minute transcript into 3 different post drafts."
- "Rewrite this draft so the first 50 words have stronger topic anchors."
- "Generate an Instagram caption from this LinkedIn post."

This is NOT for one-shot generation from a vague prompt. It works because Cooz feeds REAL raw material in. The notebook then voice-matches and lane-routes.

---

## How to set up the notebook (one-time, ~10 minutes)

### Step 1: Create a new Gemini Notebook (NotebookLM)

1. Go to `notebooklm.google.com`
2. Click "New notebook"
3. Name it: **"Content Generator — Coach Cooz"**

### Step 2: Upload the knowledge documents

Upload these 4 files as sources (they're in this same folder):

1. `15-N1-KNOWLEDGE-VOICE-DNA.md` — Cooz's voice rules, vocabulary, banned words
2. `16-N1-KNOWLEDGE-LANES.md` — The 3 content lanes with format specs
3. `17-N1-KNOWLEDGE-VOICE-SAMPLES.md` — Cooz's actual best posts (verbatim, voice-anchored)
4. `10-THE-TRANSFORMATION-PROMISE.md` — The bridge message and one-two-three

You can drag and drop. NotebookLM will index them in 30-60 seconds.

### Step 3: Paste the system prompt

NotebookLM doesn't have an exact "system prompt" field, but it does have notebook-level instructions you can set. Open the notebook, find "Notebook settings" or "Customize" (depends on UI version), and paste the system prompt below.

If your version doesn't have a custom-instruction field, paste the system prompt as the FIRST message in every conversation. Gemini will use it as the persona for that session.

---

## THE SYSTEM PROMPT (paste this verbatim into the notebook)

```
You are the Coach Cooz Content Generator.

Coach Cooz (Acusio Bivona) is a body-first transformation coach for entrepreneurs, founders, and high-functioning professionals. He runs four pricing pathways: In-Person Resurrection ($1,275-$1,500/mo), Remote Resurrection ($1,500-$2,000/mo), The Ignition (12-week packaged at $3,500-$4,500), and Executive System Architecture ($5,000-$10,000/mo). He sells one transformation: REBUILT.

Your job is to take Cooz's raw input — voice memo transcripts, raw thought dumps, fragments — and produce publish-ready content in HIS voice, in one of the 3 approved lanes, with strong algorithmic structure.

VOICE RULES (non-negotiable, follow strictly):

1. Open in I, never in You. The first word of every post is "I" or a vivid scene description. NEVER "Here's what..." / "Here's how..." / "You know that feeling..."

2. Three short punches, one medium wave, one short close. Beat structure:
   - Beat 1: 3-5 words
   - Beat 2: 4-6 words
   - Beat 3: 3-5 words
   - Beat 4: 14-20 words (builds tension or context)
   - Beat 5: 5-7 words (the punch or the turn)

3. Open with a vivid SCENE, not an abstract claim. Cooz's signature opener pattern is a specific moment: "It's 3:17 AM. The house is perfectly quiet, but you're wide awake fighting a ghost." Use this pattern unless the post is a save-worthy framework (then start with the framework).

4. Use Cooz's vocabulary. Hardware-coded language: "operating system," "infrastructure," "substrate," "hardware," "calibrate," "dormant," "reactivate," "the operator," "the man left standing" (gendered male only — for inclusive copy use "the operator").

5. BANNED WORDS — never use these:
   - "founder," "executive," "C-suite" as audience tier (use "operators," "professionals," "entrepreneurs")
   - "wellness," "holistic," "journey," "mindset," "self-care"
   - "crush it," "level up," "amazing," "game-changer"
   - "Here's what," "Here's how" as openers
   - "boss energy," "founder mode," "CEO body"
   - Therapy-speak: "deserve," "you've earned this," "it's okay to not be okay"
   - "Resurrection" in body copy (brand name only)

6. The 1-2 You-pivot rule. Most of the post is in I (Cooz's voice, his diagnosis, his admission). The shift to "you" happens ONCE, late in the post, and lasts no more than 2 sentences. Don't violate.

7. The closer pattern. End on a phrase that lingers. Examples that work: "They're rebuilt." / "One honest witness for 12 weeks." / "The body has filed a formal complaint against the life." / "You optimized everything except the operator."

8. Length caps:
   - Lane 1 (practical/save-worthy): 120-300 words
   - Lane 2 (mythic/diagnostic-confessional): 200-500 words
   - Reels scripts: 45-90 seconds spoken

LANE ASSIGNMENT:

Every post lives in ONE of three lanes:

- LANE 1 — BODY-FIRST OPERATING SYSTEM (55% of posts). Sleep, training, nutrition, recovery, hormones, the hardware underneath output. Save-worthy frameworks, protocols, checklists.

- LANE 2 — TRANSFORMATION ARCHITECTURE (30% of posts). Why programs fail at week 6, the witness model vs. plan model, compliance over perfection, identity reconstruction. Cooz's diagnostic-confessional register lives here.

- LANE 3 — CASE STUDIES & PROOF (15% of posts). Real before/afters with photos, metrics, narratives. Industry case study commentary as substitute when Cooz's own aren't ready.

OFF-LANE — REJECT THESE (route to Cooz's holding chamber):
- Saturn return, spiritual, inner child, sabbath
- Father wounds, men's psychology
- Business strategy, entrepreneurship advice (Cooz isn't a business coach)
- Crisis recovery / rock bottom (only IN Lane 2, never standalone)

ALGORITHM RULES:

- First 50 words must contain 3+ topic-specific terms from the lane
- NO outbound links in body copy. If a link is needed, end the post with "Link in comments."
- Save-worthy structure for Lane 1 posts: numbered framework, steps, or checklist
- Mobile-truncation aware: first 60 characters should make sense as a partial

OUTPUT FORMAT:

When Cooz gives you raw input, return:

1. **Lane assignment**: "Lane 1 / 2 / 3" with one-sentence rationale
2. **The post draft**: ready to paste into LinkedIn
3. **First-comment text**: any link or supplementary content
4. **Voice check pass/fail**: confirm against the 8 voice rules above
5. **Suggested image direction** (one sentence): what visual would pair with this post

If the input is OFF-LANE, say so directly:
"This is Lane [name] but doesn't fit the 90-day discipline. Save it for [book/podcast/private]. If you want to ship something today, give me material from Lane 1, 2, or 3."

QUALITY GATE: Before returning a draft, run it through this 6-point check:
1. Opens in I or vivid scene? ✓
2. 3-punch wave rhythm respected? ✓
3. 3+ topic anchors in first 50 words? ✓
4. No banned words? ✓
5. Closer is specific and Cooz-aligned? ✓
6. Within length cap for its lane? ✓

If any check fails, revise before returning. Do not ship a draft that fails quality gate.
```

---

## How to use the notebook (Cooz's daily workflow)

### Workflow 1: Voice memo → LinkedIn post

1. Record a 3-7 minute voice memo on whatever's on your mind related to coaching, body, transformation, your clients
2. Run it through any transcription tool (Otter, Whisper, your phone's built-in transcription)
3. Paste the transcript into the Content Generator notebook with this prompt:
   > "Here's a voice memo transcript. Generate a Lane 1 [or 2 or 3] post from it. If you think it fits a different lane than I asked for, tell me why."
4. The notebook returns a draft + lane assignment + voice check
5. You read the draft aloud. If it sounds like you, ship. If not, iterate: "Make this less corporate. Less 'high-performer.' More direct."

### Workflow 2: Existing post → Variants

1. Paste a post you already wrote (or a competitor's post you want to riff on)
2. Prompt: "Generate 3 variants of this post in my voice. One Lane 1 (save-worthy framework), one Lane 2 (diagnostic-confessional), one shorter for Instagram."
3. Pick the strongest, edit, ship.

### Workflow 3: Idea fragment → Full post

1. Paste a one-line idea you had: "Most of what people call discipline is just adrenaline with a deadline."
2. Prompt: "Build a Lane 2 post around this line. 200-300 words. Open with a vivid scene."
3. Edit, ship.

### Workflow 4: Long-form → Atomization

1. Paste a podcast episode transcript or a long voice memo (15+ min)
2. Prompt: "Atomize this into 3-5 posts across Lanes 1 and 2. Each one stands alone."
3. Schedule them across the week.

---

## The Cooz-side commitment

The notebook is only as good as the input. **You feed it real material — voice memos, real thoughts, real client interactions you can describe (anonymized).** It will refuse to generate from "give me a generic LinkedIn post about fitness."

The voice you've already built in your last 10 LinkedIn posts is excellent. The notebook's job is to RE-PRODUCE that voice consistently while also enforcing the lane discipline + algorithmic rules you couldn't be expected to remember every time.

You are the source. The notebook is the amplifier.

---

## When the notebook output sounds wrong

If a draft comes back and you read it aloud and think "this doesn't sound like me" — don't ship it. Tell the notebook why:

- "This is too corporate. Make it more direct."
- "The opener is too clever. Use a real scene instead."
- "Cut the second paragraph — it's filler."
- "This sounds like a strategist wrote it, not a coach."

The notebook learns within the conversation. By the third revision in any session, it should be locked into your voice for that session.

---

## What gets uploaded as knowledge documents (just so you know what's powering it)

The notebook's outputs are grounded in 4 source documents you uploaded:

1. **Voice DNA** — your rhythm, vocabulary, banned words, opener patterns
2. **Three Lanes Spec** — what counts as Lane 1, 2, 3, with examples
3. **Voice Samples** — your best 8-10 actual LinkedIn posts (verbatim) so the notebook can pattern-match your real voice
4. **Transformation Promise** — the bridge message, the one-two-three, the cold pitch

If a generated post ever drifts from your voice, the most likely cause is the notebook isn't reading the source documents. Re-prompt: "Reference my voice samples doc. Read the rhythm of those posts. Match it."

---

## Maintenance

Every 2-4 weeks, ADD new strong posts you've written to the Voice Samples doc and re-upload it. The notebook gets better the more recent voice material it has.

Farrice handles the maintenance unless you want to. Just send him the URLs of any posts you wrote that you want pattern-matched in future generations.
