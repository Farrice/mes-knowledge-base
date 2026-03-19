---
description: Audit any content for inauthenticity signals — flag phrases that feel foreign, scripted, or robotic, then prescribe voice-pocket rewrites
---

# Believability Audit

> **Produces**: Line-by-line authenticity map with flagged inauthenticity signals, diagnosed root causes, and specific rewrite prescriptions to bring content inside the voice pocket

## When to Use
- AI-generated content that technically sounds fine but feels "off"
- Ghostwritten content that doesn't sound like the attributed author
- Any content that triggers the "this doesn't sound like a real person" response
- Post-production quality gate before publishing content under your name
- Diagnosing WHY a piece feels inauthentic when everything seems technically correct

## Input Required
1. **Content to audit** — the piece suspected of inauthenticity
2. **Voice reference** (optional but powerful) — a sample of the author's natural writing/speaking (tweets, casual emails, voice memos, transcripts)
3. **Publishing context** — where this will appear

> **🔒 Pre-Flight Gate**: Before executing, run the **Decision Framework** in `genius.md` § Decision Framework. Confirm all diagnostic questions are answered.


## Execution Protocol

### Step 1: First-Read Gut Check
Read the full content once, quickly. Flag every sentence where your attention snags — where something feels "off" even if you can't immediately articulate why. Trust the instinct. Mark these as [SNAG].

### Step 2: Inauthenticity Signal Detection
Scan the full content for these specific inauthenticity signals:

**A. Template Language**
Phrases that appear in thousands of AI-generated or templated pieces:
- "In today's fast-paced world..."
- "It's no secret that..."
- "Here's the thing..."
- "Let me be clear..."
- "At the end of the day..."
- Any phrase that completes itself predictably

**B. Uniform Sophistication**
Every sentence at the same complexity level. Real writers have variable sophistication — sometimes simple, sometimes complex, sometimes sloppy.

**Flag**: If all sentences are similarly constructed with similar vocabulary complexity → robotic.

**C. Perfect Grammar Without Voice**
Grammatically flawless prose with no personality quirks. Real writers have specific grammatical habits — some start sentences with "And." Some use fragments. Some over-use dashes. Perfection signals machine.

**D. Hedging Overload**
AI-generated content often hedges obsessively:
- "It's worth noting that..."
- "While it's important to consider..."
- "It's worth mentioning..."
- "Some experts suggest..."

One hedge per piece is fine. Three or more signals insurance-policy writing.

**E. Emotional Incongruence**
Content that claims emotion but doesn't demonstrate it. "I'm really passionate about this topic" followed by clinical, detached prose. The claimed emotion and demonstrated energy must match.

**F. Missing Idiosyncratic Detail**
Real people include oddly specific, unnecessary details that prove lived experience. AI and template writing stays at the "useful" level without the texture of real life.

**G. Vocabulary Above Station**
Words the attributed author would never naturally use. If the author normally says "use" but the content says "utilize" — inauthenticity signal.

### Step 3: Inauthenticity Map
Produce a line-by-line map:

```
BELIEVABILITY AUDIT RESULTS
────────────────────────────
Overall Believability Score: [1-10]
Inauthenticity Signals Found: [count]

LINE-BY-LINE MAP:
[Line #] [Signal Type] [Flagged Phrase] [Why It's Inauthentic] [Rewrite Prescription]
```

### Step 4: Root Cause Diagnosis
For each flagged signal, diagnose the root cause:

| Root Cause | What It Looks Like | Fix |
|-----------|-------------------|-----|
| AI-generated | Template language, uniform sophistication, perfect grammar | Rewrite with idiosyncratic detail, vary complexity, add personality quirks |
| Ghostwriter mismatch | Vocabulary above station, emotional incongruence | Map author's voice pocket, rewrite in their natural register |
| Over-editing | Original voice edited out, hedging added by editor | Restore original phrasing where it was stronger, remove safety hedges |
| Performative writing | Trying to sound smart vs. being clear | Simplify, use the words you'd actually say to a friend |

### Step 5: Voice Pocket Rewrite
For each flagged line, produce a rewrite that sits inside the author's voice pocket:

**The Voice Pocket** = the set of sentence structures, vocabulary, and rhythms that feel effortless for the author. Everything outside it reads as performative.

**Rewrite rules**:
1. Read the line aloud — if you stumble or feel disconnected, the words aren't yours
2. Rewrite in the words you'd use to explain this to a friend at a bar
3. Keep the meaning, change the delivery
4. Add one idiosyncratic detail if the line feels too clean
5. Match the emotional claim to demonstrated energy

### Step 6: Before/After Comparison
For the top 5 most impactful fixes, show before/after:

```
BEFORE: [Original flagged text]
SIGNAL: [What was wrong]
AFTER: [Rewritten in voice pocket]
WHY: [What the fix accomplishes]
```

## Output Schema

```yaml
deliverable: "Believability Audit"
components:
  believability_score:
    description: "Overall score [1-10] with justification"
  inauthenticity_map:
    description: "Every flagged line with signal type, root cause, and rewrite"
  top_5_comparisons:
    description: "Before/after comparisons with reasoning"
    count: 5
  rewritten_content:
    description: "Full piece with all fixes applied"
  voice_pocket_notes:
    description: "Author's natural patterns for future reference"
```

## Quality Gate
- [ ] Every template phrase has been replaced with original language?
- [ ] Sophistication varies naturally — simple and complex sentences mixed?
- [ ] Grammar has personality — not robotically perfect?
- [ ] Hedging reduced to maximum 1 instance per piece?
- [ ] Emotional claims match demonstrated energy?
- [ ] At least 2 idiosyncratic details add texture?
- [ ] Author would read this and think "yes, that sounds like me"?


> **🛡️ Anti-Pattern Check**: Before delivering, review output against the **Anti-Patterns** in `genius.md` § Anti-Patterns. Flag and fix any violations. Cross-reference **Voice DNA** for tonal accuracy.
## Example Output

**Context**: Believability audit of a 1,200-word LinkedIn post about startup lessons (AI-assisted draft)

**OVERALL BELIEVABILITY SCORE: 4/10**
Primary issue: The post sounds like a confident outsider narrating someone else's experience. Generic intensity without specificity.

**INAUTHENTICITY MAP (Top 5 flags):**
| Line | Signal Type | Severity |
|------|------------|----------|
| "The journey taught me invaluable lessons" | Template phrase — no human says "invaluable lessons" naturally | 🔴 High |
| "I was passionate about disrupting the industry" | Retrospective inflation — people don't think in these terms at the time | 🔴 High |
| "After countless sleepless nights..." | Cliché exhaustion — overused to the point of invisibility | ⚠️ Medium |
| "The key takeaway is..." | Lecture format — transitions into teacher mode without earning it | ⚠️ Medium |
| "If there's one thing I've learned..." | Wisdom-claiming — announces the insight before delivering it | ⚠️ Medium |

**TOP 3 BEFORE/AFTER:**

**Fix #1 — Template → Voice pocket:**
- **Before**: "The journey taught me invaluable lessons about resilience and adaptability."
- **After**: "I didn't learn anything during the hard part. I was too busy panicking. The learning happened six months later, sitting in a coffee shop with nothing to do, when I finally had the bandwidth to ask: what just happened to me?"
- **Why**: Real learning is messy and delayed. The original sentence sounds like a LinkedIn template because it is one.

**Fix #2 — Retrospective inflation → Honest memory:**
- **Before**: "I was passionate about disrupting the healthcare industry with AI-powered solutions."
- **After**: "I thought the idea was cool. My cofounder's mom was a nurse and she kept complaining about the scheduling software. That's it. That's how it started."
- **Why**: Origin stories are never as clean as we present them. The messy truth (cofounder's mom complained about software) is 10x more believable than "disrupting the industry."

**VOICE POCKET NOTES:**
The author's natural voice emerges in paragraphs 4 and 7 — shorter sentences, self-deprecating humor, concrete details. The rest of the piece was likely written in a different session or with heavy AI assistance. Recommendation: rewrite the entire piece in the voice of paragraphs 4 and 7.
