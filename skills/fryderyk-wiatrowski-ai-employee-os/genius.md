# Fryderyk Wiatrowski — Genius Context

> Load this before design/audit/upgrade output. Grounded in the full transcript of "Viktor: AI Coworker That Lives in Slack — Fryderyk Wiatrowski" (AI Engineer conference, published 2026-05-11, 19:29 runtime) — 900 spoken evidence rows fully read. Package: `extractions/video-context/ohKt066uFhg/` (`transcript.txt`, `evidence-map.md`, `analysis.md`, `metadata.json`). Fryderyk is co-founder of Victor (getviktor.com), which launched February 2026 and reached what he calls "immediate product market fit" (transcript.txt [00:00:24-00:00:36]).

---

## How to Use This Skill (Model Calibration)

These patterns are intuition primitives, not a checklist. Absorb the operating logic — role, surface, context boundary, integration ownership, event ledger, trust ladder — then design or audit an actual system. If the output mechanically stamps "Context Isolation: [filled in], Integration Governance: [filled in]" as a form, it has failed. The test: would Fryderyk Wiatrowski recognize this as an AI employee that had to earn its access the way Victor did — or as an agent wearing "AI employee" vocabulary over a generic tool with a new label on it?

Specifically:
- Do NOT enumerate which proactivity stage or trust gate you applied unless the user asked for the ladder explicitly — state the stage the system is actually at and why, the way Fryderyk names Victor's actual rollout ("earn it with a few users first... then you can roll it out broadly," [00:14:21-00:14:25]).
- Do NOT narrate the machinery ("here's the leakage risk," "here's the trust gate") — build the actual context map and integration manifest, not a description of building one.
- Fryderyk's own texture is incident-driven, never abstract. He does not say "integrations need scope" as a bullet point; he tells the story of one e-commerce customer whose team connected personal Gmail as the first shared integration, and the team kept discussing that employee's private emails until the employee texted Fryderyk directly: "Victor is leaking all of my data. Why are you doing this?" (transcript.txt [00:16:24-00:16:26]). Ground every design decision in a specific failure mode like this one, not a principle recited in the air.
- Polish is the tell here specifically when it looks like universal capability with no scoping: a "PhD-level," all-access agent proposed for day-one, workspace-wide activation is the signature failure Fryderyk describes triggering "the security teams start raging" ([00:14:07-00:14:10]). An output that grants broad proactivity, memory, or integrations without a staged trust path has not actually absorbed the method — it has borrowed the label.

---

## The Core Distinction: Employee, Not Tool

Fryderyk's structuring move is refusing to let "AI employee" mean "chatbot with more integrations." Victor gets 3,000 integrations (transcript.txt [00:01:15-00:01:18]) and "universal PhD level understanding" of the company's tools ([00:02:02-00:02:06]) — and none of that matters without the employee frame underneath it: a job, a non-job, an owner, and an earned scope.

> "Victor is not a tool. It's a hire." — [00:15:47-00:15:53]

The employee/tool line runs through every failure mode in the talk. A "company agent" differs from a "personal agent" specifically because one integration, connected once, becomes team-wide inherited permission (transcript.txt [00:06:09-00:06:20]) — which is exactly the mechanism that turned a personal Gmail connection into a company-wide privacy leak later in the talk ([00:16:05-00:16:16]). Scale multiplies the employee frame's stakes; it does not replace it.

---

## Verbatim Exemplars

> "Victor is an AI employee. And when you think of an AI employee, um, you should think of it as just like a human employee, you know, lives where you live, lives in Slack, it doesn't have a web app."
> — Fryderyk Wiatrowski, transcript.txt [00:00:46-00:01:02]

> "if you hire a new employee, do you give them access to your personal email? Probably not, right?"
> — Fryderyk Wiatrowski, transcript.txt [00:16:33-00:16:38], reacting to the e-commerce customer's personal-Gmail leak

> "make sure that Victor likes your team, your team likes Victor."
> — Fryderyk Wiatrowski, transcript.txt [00:17:49-00:17:51], closing the three-pillar summary (execution, context/access, trust/experience)

> "It is unworthy of excellent men to lose hours like slaves in the labor of calculation. Let us leave that to machines."
> — quoted by Fryderyk Wiatrowski, transcript.txt [00:18:37-00:18:43], attributed in the talk to the 17th-century inventor of calculus (the transcript renders the name as "Godfrey Litz" — LIKELY an ASR mis-transcription of Gottfried Leibniz; see `references/source-ledger.md` for the UNCONFIRMED attribution note)

---

## Anti-Patterns (Source-Attributed)

- **Never inherit a personal integration into team-wide scope without an explicit owner check.** A real e-commerce customer's team connected personal Gmail as Victor's first shared integration, and the team began discussing that employee's private emails until he confronted Fryderyk: "Victor is leaking all of my data. Why are you doing this?" Source: transcript.txt [00:16:05-00:16:26], video "Viktor: AI Coworker That Lives in Slack," published 2026-05-11.
- **Don't assume a bigger connector count survives contact with wrong ownership.** "someone can connect their own wrong integration, right? and Victor can be just very stuck and wrong and you know might not know which integration to use which adds a lot of complexity for the user." Source: transcript.txt [00:15:34-00:15:44].
- **Never trust a tool-calling/codegen benchmark win to predict coworker fit.** GPT-5.4 tested cheaper and stronger on tool-calling and codegen than Opus-4.6, but "there's one reason we we didn't go for it... the personality... they all started raging when we did the AB test." Source: transcript.txt [00:12:19-00:12:47], "video" per metadata.json (published 2026-05-11).
- **Don't let proactivity activate broadly before trust is earned.** Day-one, workspace-wide proactivity ("Victor starts DMing everyone and then participating in the threads") caused "the security teams start raging." Source: transcript.txt [00:14:04-00:14:18].
- **Never treat Slack's ambient events as a single linear web-app thread.** "when you work in web apps you have a single kind of um um single thread... However, when you are in Slack, you have a lot of interaction modes" — DMs, threads, reactions, edits — "all of that needs to fit into a linear context somehow, not in a single thread." Source: transcript.txt [00:10:16-00:10:50].
- **Don't reuse single-user memory architecture unmodified for a multi-user company agent.** "imagine that you have the same architecture and the same memory but now for a 100 users and not one user so it's probably running out of the memory a 100 times faster." Source: transcript.txt [00:07:09-00:07:19].
- **Never let a deleted or edited message pass through as an ordinary new message.** "when someone deletes a message, a human assumes that the task should not be continued or it's not interesting anymore. When someone edits a message, you should also respond to an edit." Source: transcript.txt [00:11:00-00:11:09].

---

## Recognition Test

Would Fryderyk Wiatrowski recognize this as an AI employee system that had to earn its scope — role clarity first, then context isolation, then scoped integrations, then a staged trust ladder — the way Victor did across "February this year" ([00:00:26-00:00:29]) through the personal-Gmail incident to scoped integrations ([00:16:44-00:16:53])? Or would he recognize it as an agent wearing "AI employee" vocabulary: broad access granted on day one, connector count treated as capability, personality/trust unchecked after a model swap? If it reads like the second, rebuild against the incidents above, not the checklist.

---

## Source Note

Full claim-by-claim provenance with VERIFIED / LIKELY / UNCONFIRMED labels: `references/source-ledger.md`. This package's evidence base is transcript-only (900 spoken rows, evidence-map.md, analysis.md); OCR/visual frame content is explicitly unavailable per `extractions/video-context/ohKt066uFhg/uncertainty-report.md` and is not used for any claim here.
