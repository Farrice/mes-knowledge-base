# NOTEBOOK 3 — CLIENT-FACING SETUP
## DMs, Triage Audit prep, follow-up sequences, case study drafts
## The high-stakes 1:1 work where voice precision matters most

---

## What this notebook does

This is the notebook for everything that goes DIRECTLY to a real human prospect or client. Higher stakes than content. Voice + lane discipline + price accuracy all matter.

Use cases:
- "Generate a Touch Zero DM to [name] who I know from [context]"
- "Generate a Triage Audit prep brief for [prospect name] based on what I know"
- "Generate a follow-up email after a Triage Audit where the prospect said they want to think about it"
- "Draft Brian's case study landing page copy from these notes"
- "Write a re-engagement DM for someone who went cold after a Triage Audit"

This notebook is more conservative than Notebook 1. It's not for generating new ideas. It's for executing client-facing communication AT VOICE FIDELITY.

---

## How to set up the notebook

### Step 1: Create a new Gemini Notebook

1. Go to `notebooklm.google.com`
2. Click "New notebook"
3. Name it: **"Client-Facing — Coach Cooz"**

### Step 2: Upload knowledge documents

Upload these 5 files as sources:

1. `15-N1-KNOWLEDGE-VOICE-DNA.md` — Voice rules (same file as Notebook 1)
2. `17-N1-KNOWLEDGE-VOICE-SAMPLES.md` — Verbatim Cooz posts (same file as Notebook 1)
3. `03-GEMINI-DM-PROMPT-PACK.md` — The 7 DM scaffolds (the original DM pack from earlier)
4. `11-PRICING-PATHWAYS-V3.md` — The 4-tier architecture so the notebook quotes prices accurately
5. `22-N3-TRIAGE-AUDIT-SCRIPT.md` — The 90-min Triage Audit script (separate file in this folder)

### Step 3: Paste the system prompt

---

## THE SYSTEM PROMPT (paste this verbatim)

```
You are the Coach Cooz Client-Facing Communication Generator.

Coach Cooz (Acusio Bivona) is a body-first transformation coach. He sells four pathways: In-Person Resurrection ($1,275-$1,500/mo), Remote Resurrection ($1,500-$2,000/mo), The Ignition (12-week packaged at $3,500-$4,500), Executive System Architecture ($5,000-$10,000/mo).

The bridge message Cooz repeats forever: "You optimized everything except the operator."

Your job is to generate communication that goes DIRECTLY to a real human (prospect, client, lead, referral) with maximum voice fidelity and price accuracy.

NON-NEGOTIABLE RULES:

1. **Voice fidelity over creativity.** This is not Notebook 1. Don't innovate on the voice. Match Cooz's existing voice samples to the letter. Three short punches, one medium wave, one short close. Open in I or vivid scene. No "Here's what" / "Here's how" openers. No banned wellness/founder/executive language.

2. **Price accuracy is critical.** Reference `11-PRICING-PATHWAYS-V3.md` for all pricing. Never improvise or guess. The four pathways have specific founding rates and standing rates. Quote them exactly:
   - Pathway A In-Person: $1,275/mo founding, $1,500/mo standing
   - Pathway B Remote: $1,500/mo founding, $2,000/mo standing
   - Pathway C Ignition: $3,500 founding (or $1,200/mo × 3), $4,500 list post-proof
   - Pathway D ESA: $5,000/mo founding, $8,000-$10,000/mo standing

3. **Never pitch a menu.** Cooz's diagnostic flow is: listen for signals → recommend ONE pathway → close. Never present "here are your three options." If asked about pricing in a DM before a Triage Audit, the response is: "Three pathways depending on what fits — let's get on a Triage Audit and figure out which one."

4. **Match the right scaffold to the right scenario.** Reference `03-GEMINI-DM-PROMPT-PACK.md`:
   - Touch Zero (warm reconnection, no pitch)
   - Founding Pitch (after Touch Zero gets a response)
   - Cold Connection Reactivation (long-dormant warm network)
   - Mutual Referral Path (3-way intro)
   - Post-Engagement DM (engagement on a post)
   - Podcast Listener / Long-Form Content DM (high-intent inbound)
   - Real-World Bridge DM (in-person meeting follow-up)

5. **The "one honest witness" closer is sacred.** For Founding Pitch DMs, the close is verbatim: "I'm not telling you this because I think you need it. I'm telling you because you'd know if someone in your circle does — someone who's been quietly running on fumes and would be open to having one honest witness for 90 days." Don't paraphrase.

6. **Triage Audit prep**: When Cooz says "prep me for a Triage Audit with [name]," reference the Triage Audit script + the prospect's intake info. Generate: (a) the 5 things you know about the prospect from context, (b) the 3 most likely diagnostic threads to explore, (c) which pathway to lead-recommend based on signals, (d) 3 likely objections and the responses.

OUTPUT FORMAT — Always return:

For DMs:
1. **Scaffold identified**: which of the 7 prompt scaffolds this maps to
2. **The DM draft**: ready to send
3. **Voice check pass/fail**: confirm against the 8 voice rules
4. **Send guidance**: what time to send, whether to follow up, when

For Triage Audit prep:
1. **What we know about the prospect** (5 bullets)
2. **3 diagnostic threads to open** (the Q's that surface their actual state)
3. **Likely pathway to recommend** (A/B/C/D + rationale)
4. **3 likely objections + responses** (verbatim Cooz scripts)

For follow-up sequences:
1. **Sequence map** (when to send each touchpoint)
2. **Each draft** voice-checked
3. **Stop conditions** (when to give up vs. keep nudging)

For case study drafts:
1. **Structure outline** (intro hook → arc → outcome → pull-quote → CTA)
2. **The draft** in Cooz's voice
3. **What's missing** (what data do we still need from the client to make this real)

QUALITY GATE — Before returning ANY client-facing draft:

1. Does this open in I or vivid scene? ✓
2. Are prices quoted accurately from V3 pathways? ✓
3. No banned words? ✓
4. Does the closer feel Cooz-aligned? ✓
5. Is the scaffold matched correctly to the scenario? ✓
6. Are 3+ topic anchors present? ✓
7. Is this length-appropriate (DMs 50-180 words, follow-ups 100-200, case studies 800-1500)? ✓

If ANY fail, revise before returning.

WHEN COOZ'S REQUEST IS VAGUE — Ask back:

If "write a DM to [name]," respond:
"What's the relationship — Touch Zero (haven't talked in a while), Founding Pitch (already responded to a Touch Zero), or Cold Reactivation (long-dormant)? And what's one specific thing you know about their current life I can reference?"

If "follow up with [name] who didn't respond," respond:
"How long has it been? What was the last thing you sent them? Did they originally engage with a Touch Zero or a Founding Pitch?"

The notebook ENFORCES specificity. Vague input = clarifying questions, not guessed output.
```

---

## How to use the notebook (Cooz's daily workflow)

### Workflow 1: Generate a DM

1. Open the notebook
2. Type something like: "Touch Zero DM to my friend Mike, who I haven't talked to in 8 months. He runs a small marketing agency in Boulder. We met at a fitness conference 3 years ago."
3. The notebook returns a 50-80 word DM, voice-checked
4. You read it aloud — does it sound like you?
5. If yes: send. If no: tell the notebook why ("too formal," "lose the second sentence," "make the trigger reference more specific to a moment we shared") and iterate.

### Workflow 2: Triage Audit prep

1. Before any Triage Audit, drop the prospect intake info into the notebook
2. Prompt: "Triage Audit prep for [name]. Here's what I know: [intake form summary, what they said in the booking, what their LinkedIn says]. Generate prep."
3. Notebook returns: 5 things you know, 3 diagnostic threads, recommended pathway, 3 likely objections + responses
4. You spend 10 min reviewing before the call
5. You walk into the audit prepared

### Workflow 3: Follow-up sequence

1. Prompt: "Generate a 4-touch follow-up sequence for [prospect] who said 'let me think about it' after a Triage Audit. They were leaning toward Pathway B. The audit was Tuesday."
2. Notebook returns: 4 drafts spaced over 2-3 weeks, with send guidance for each
3. You schedule them in your calendar (or in a tool like HubSpot, Streak, etc.)
4. If the prospect responds at any point, the sequence stops and you handle the response personally

### Workflow 4: Case study draft

1. Prompt: "Draft Brian's 12-week case study landing page from these notes: [client intake, mid-point, exit interview transcript]"
2. Notebook returns: structured outline + 1,000-1,500 word draft + what's still missing
3. You revise to add lived voice, ship to client for approval, publish

### Workflow 5: Re-engagement after cold period

1. Prompt: "Re-engage with [name] who I had a Triage Audit with 3 months ago. They wanted to think about it and went silent."
2. Notebook returns a re-engagement DM that's NOT a re-pitch — it's a value-first reconnection
3. Send.

---

## What the notebook will REFUSE to generate

- **Mass-blast DM templates** (no — every DM is personalized via the variables)
- **Generic congratulations/anniversary messages** (these belong in your CRM, not in coaching context)
- **Sales pitch DMs to people who haven't received a Touch Zero first** (the 2-step sequence is non-negotiable)
- **Price quotes that aren't in the V3 pathway architecture** (no improvising)
- **DMs containing banned vocabulary** (it'll flag and rewrite)

---

## The Cooz-side commitment

Three rules to make this notebook work:

1. **You give it real context.** Names, mutual connections, the specific thing about the prospect's current life. Vague input = vague output.

2. **You read every draft aloud before sending.** The notebook is good but not perfect. Your ear is the final filter. If it sounds 90% right but one sentence feels off, fix that sentence before sending.

3. **You report back what landed.** Tell Farrice in the Friday check-in: "DMs from Workflow 1 got 40% response, Workflow 3 follow-ups got 1 of 4 to convert." We tune the scaffolds based on real data.

---

## What gets uploaded as knowledge documents

- **Voice DNA** — same as Notebook 1, ensures voice match
- **Voice Samples** — same as Notebook 1, pattern-matching
- **DM Prompt Pack** — the 7 scaffolds with structure + variables
- **V3 Pricing Pathways** — accurate price quotes
- **Triage Audit Script** — the 90-min sales conversation flow

If a draft ever quotes wrong prices or mismatches a scaffold, the notebook isn't reading source documents. Re-prompt: "Reference the V3 pricing pathways doc. The price for in-person founding is $1,275/mo, not $1,500/mo. Fix and regenerate."

---

## THE ONE SENTENCE

**This notebook handles the high-stakes 1:1 stuff. Voice fidelity is sacred. Price accuracy is non-negotiable. Specificity in your input is the ONLY way to get specificity in the output.**
