# THE CLAIM CHECK — live-audit artifact kit

### A public Claude artifact that performs one slice of the paid audit, live, on the visitor's own claim.

> **What this is (built 2026-07-01):** the interactive lead magnet — modeled on the public-artifact play (cf. Diandra Escobar's cited-by-AI artifact) but one level up: instead of teaching, it **does the work**. A brand operator pastes their strongest marketing claim; the artifact runs Farrice's two-gate read on it live (Will a regulator flag it? Will AI repeat it?), shows the verdict like a lab report, hands them one safe-and-citable rewrite, and routes to `DM 'AUDIT'`.
> **Why it converts:** it's the P sound bite made experiential. They feel the gap on their OWN claim, by their own hand — then learn the real audit does their top 8–12 claims plus the questions where competitors get named instead of them.
> **How it works technically:** public Claude artifacts can call Claude from inside the artifact (`window.claude.complete`) — the VIEWER's Claude account powers it. Zero API cost to you, no backend, no data stored. Viewers need a free Claude login for the AI part (same as Diandra's; your no-login fallback stays the 7-check Google Doc).

---

## STEP 1 — Build it (10 minutes, in claude.ai or Claude CoWork)

Open a new chat on claude.ai (or CoWork) and paste the entire block below as one message:

```
Build me a single-file React artifact called "The Claim Check". It is a live diagnostic tool for health/supplement/wellness brand operators. Follow this spec exactly.

WHAT IT DOES
The user pastes ONE marketing claim from their brand (e.g. "Clinically proven to reduce cortisol by 23%"). Optionally they can add: product type, hero ingredient, and dose (three small optional fields). They press "Run the check." The artifact calls Claude via window.claude.complete with the GRADING PROMPT below, parses the JSON response, and renders a lab-report-style verdict.

SCREENS / STATES
1. INTRO (compact, above the fold):
   - H1: "The Claim Check"
   - Sub: "Paste your strongest marketing claim. Find out in 20 seconds whether it's an asset — or a liability."
   - One line under it: "When your buyers ask AI about your category, somebody else's name comes back. This shows you one reason why."
   - A single large textarea ("Paste your claim — the one on your hero banner"), the 3 optional small inputs (product type / hero ingredient / dose), and one button: "Run the check".
   - Tiny footnote: "Nothing you paste is stored. This is an educational read from a credentialed practitioner's rubric, not legal advice."
2. LOADING: a short sequence of status lines that appear one by one while waiting ("Reading the claim like a regulator would…", "Reading it like ChatGPT would…", "Drafting the version that survives both…"). Keep it honest and calm, no fake progress bars.
3. RESULTS (the lab report):
   - Big verdict banner: CLEAR (green) / CAUTION (amber) / LANDMINE (red) with the combined read in one plain sentence.
   - Two gate cards side by side (stack on mobile):
     GATE 1 — "Would a regulator flag it?" → score 0–100, the 1–3 specific danger words highlighted inline in their claim, and 2–3 plain-English reasons. If treat/cure/prevent language is detected, say: "Supplements may only *support* — this verb is a drug claim." Mention the $53,088-per-violation FTC penalty ONLY when risk is CAUTION or LANDMINE.
     GATE 2 — "Would AI repeat it?" → score 0–100 and 2–3 plain reasons (Is there a receipt? A named human? A mechanism? Or does it read like marketing the machine filters out?).
   - THE REWRITE card: one version of their claim rewritten to be safe AND citable (structure/function verb, mechanism named, selling power kept), plus one line: "Evidence you'd want on file: …"
   - THE BRIDGE (end card): "This was ONE claim. The real version of this — The Claim-Safe Citation Audit — grades your top 8–12 claims, shows you the 3–5 questions where AI names a competitor instead of you, and hands you the fix map. DM me 'AUDIT' on LinkedIn." Button: "DM me 'AUDIT'" linking to https://www.linkedin.com/in/REPLACE-WITH-FARRICE-PROFILE (open in new tab). Sub-line: "Farrice Cain — 18 years in human performance (NASM ×3). I read the science under the claim before I grade the claim."
   - "Check another claim" button that resets.
4. NO-LOGIN state (critical — most visitors arrive logged OUT of Claude): if window.claude is unavailable, or the completion call fails for auth/permission reasons, do NOT show a generic error. Show: "This tool runs on a free Claude login. No login? Run the no-login version instead — the 7-check AI-Search Visibility Test:" with a prominent link button to [7-CHECK-DOC-URL — replace before publishing]. The fallback must be RENDERED in this state, not implied.
5. ERROR state (everything else): if the response fails to parse or the input is empty/not-a-claim, show a kind plain-language message and let them retry.

DESIGN DIRECTION (anti-generic, mobile-first)
- Feels like a clean lab report, not a SaaS landing page: off-white background, ink-dark text, ONE accent per verdict state (deep green / amber / signal red), generous whitespace, tabular-number font for scores, subtle 1px borders. No purple gradients, no emoji spray, no stock-illustration vibe, no three-equal-cards hero. One memorable touch: the verdict banner types itself in like a report line printing.
- Every visible string in sentence case. Short lines. No exclamation marks.

GRADING PROMPT (embed as a template; interpolate the user's claim + optional fields; instruct Claude to return ONLY valid JSON):
"You are grading ONE health/supplement marketing claim through a two-gate rubric written by a practitioner with 18 years in human performance. Be direct, warm, specific — a guide, not a lecturer. Never invent regulations or studies. The only hard regulatory facts you may cite: supplements may claim to *support* structure/function but never *treat, cure, prevent, or diagnose* (21 CFR 101.93); FTC health-claim violations run $53,088 each; the FTC standard is 'competent and reliable scientific evidence' for this product at this dose.
CLAIM: {claim}
CONTEXT (may be empty): product type {type}; hero ingredient {ingredient}; dose {dose}.
GATE 1 — regulator read. Look for: drug verbs (treat/cure/prevent/heal/diagnose/reverse) or disease names used as outcomes; absolutist words (guaranteed, eliminates, melts, erases, clinically proven without visible support); implied medical outcomes; whether honest evidence would need to exist for THIS product at THIS dose. Score 0 (untouchable) to 100 (defensible), list the exact risky words, give 2–3 short plain-English reasons.
GATE 2 — will AI repeat it read. Engines repeat claims that carry: a mechanism (how it works in the body), a receipt shape (source/study/number that could be checked), a named credentialed human, specificity over hype. They skip: superlatives, vague benefit language, marketing tone. Score 0–100, give 2–3 short reasons.
REWRITE: one version that keeps the selling power but survives both gates — structure/function verb, mechanism named, honest hedge only where needed. Also produce one line: the evidence they'd want on file to stand behind it.
VERDICT: CLEAR if both gates ≥70; LANDMINE if either ≤35; else CAUTION. One-sentence combined read in plain words, no jargon.
Return ONLY JSON: {\"verdict\":\"CLEAR|CAUTION|LANDMINE\",\"summary\":\"...\",\"gate1\":{\"score\":n,\"riskyWords\":[\"...\"],\"reasons\":[\"...\"]},\"gate2\":{\"score\":n,\"reasons\":[\"...\"]},\"rewrite\":\"...\",\"evidenceLine\":\"...\"}"

IMPLEMENTATION NOTES
- Use window.claude.complete(prompt) for the call; JSON.parse defensively (strip any text around the JSON; on parse failure, retry once with "Return ONLY the JSON object.").
- No external network calls, no localStorage, no analytics. Everything in one file.
- Keep total interface copy under ~150 words. Every word earns its place.
```

Then: test it (Step 2), click **Publish** on the artifact, copy the public link.

## STEP 2 — QA with these three claims before publishing (2 minutes)

1. **Should come back LANDMINE:** `"Clinically proven to cure anxiety and eliminate cortisol spikes in 7 days"` (drug verb + disease outcome + absolutism + unsupported "clinically proven").
2. **Should come back CAUTION:** `"Boosts testosterone by up to 42% — guaranteed results in 30 days"` (implied medical outcome, absolutist, receipt-shaped number with no source).
3. **Should come back CLEAR-ish:** `"Magnesium glycinate, 300mg — the form used in most sleep studies, chosen because it actually absorbs. Supports deeper, calmer sleep."` (structure/function verb, mechanism, receipt shape).
   Also test: empty input, a non-claim ("hello"), one run with the optional fields filled, and **the logged-out state** (open the public link in a private/incognito window — the no-login fallback with the 7-check link must render, not a generic error). Check it on your phone.

**Pre-publish checklist (dead-button guard):** ① the LinkedIn profile URL placeholder is replaced with your real profile URL; ② the [7-CHECK-DOC-URL] placeholder is replaced with the live Google Doc link; ③ both buttons actually open in a new tab. Publish only after all three.

## STEP 3 — Wire it in (10 minutes)

1. **Featured card (takes slot [1]; the 7-check Doc takes slot [4] as the no-login path; the POV manifesto moves to the About's link line):**
   - Title: `The Claim Check — paste your claim, see if it survives (live, 20 seconds)`
   - Description: `Paste your strongest marketing claim. Find out whether a regulator would flag it and whether AI would ever repeat it — plus the rewrite that survives both. Free. No email. Nothing stored. (Runs on a free Claude login — no login? The 7-check test below needs none.)`
   - Link: the public artifact URL.
2. **Update the profile About's test line** when you're ready: the 7-check Doc stays (no-login fallback); the Claim Check becomes the headline free thing.
3. **The DM flow:** anyone who posts/DMs a screenshot of their verdict gets the §7-A teardown DM with their result as the opener ("saw your LANDMINE — want me to run your other seven?").
4. **Creative Book §5:** add the artifact link next to the 7-check test once live.

## STEP 4 — The launch post (voice-gated, ready to ship)

```
I built a tool that does something uncomfortable.

You paste your brand's strongest marketing claim — the one on your hero banner right now — and in 20 seconds it tells you two things:

Would a regulator flag it?
Would AI ever repeat it?

Most operators have never seen their claim graded on both at once. Which is strange, because in a health category they stopped being separate questions: the words that get you fined are the same words AI will never repeat.

I watched a claim I'd have called "aggressive but fine" come back as a $53,088 sentence with a competitor's name in the answer box.

It's free. It's live. No email, nothing stored. Paste the claim you're most confident about — that's the one worth checking.

[artifact link in first comment]
```

First comment: the link + `If your verdict says LANDMINE, DM me 'AUDIT' — the full version grades your top 8–12 and shows where AI names a competitor instead of you.`

## Notes & guardrails

- **Viewer requirement:** the AI part needs the visitor to be logged into a (free) Claude account — same trade Diandra's artifact makes. The Google-Doc 7-check test remains the zero-login path; the two cross-link.
- **The disclaimer is load-bearing** ("educational read, not legal advice") — it's in the artifact footer and the results card. Never remove it.
- **Nothing is stored** — say so proudly; it's a trust feature for this exact buyer.
- **Rubric integrity:** the grading prompt above is the same two-gate logic as the paid audit (`claim-safe-citation-audit-TEMPLATE.md`) at 1-claim scope. If the template's rubric evolves, update the artifact's prompt to match — one source of truth.
- **Proof flywheel:** screenshot interesting (anonymized) verdicts as post material; every LANDMINE screenshot is a teardown invitation.
