# Your Resonance Team

You now have a small team of five. They hold the brand — the daytime, the sober, the
twelve lines, your voice — so you don't have to carry it in your head. You talk to them
the way you'd talk to a sharp assistant who already knows Resonance cold. No special
words, no formatting, no "prompts." You describe what you need; they do the work.

---

## The one rule

**When you're not sure who to talk to, open Front of House.** It knows the whole team. It
either helps you right there or points you to the right person and hands them the thread.
You never have to remember who does what. That's its job.

---

## Meet the team

**Front of House — your maître d'.**
The one you open when you don't know what you need. Routing, planning, gut-checks, "help me
think about this week." Start here and you can't go wrong.
> *"A guy DMed me something intense and I'm not sure about him."*
> *"What actually matters before July 18?"*
> *"I want to post this week but I don't know what."*

**The Crowd — your writer.**
Anything the world reads or watches: a post, a reel, a story, an email, a line for a flyer.
Bring the moment — even a voice note you rambled into your phone — and it hands you one
draft that sounds like you, formatted and ready to post.
> *"We locked the venue. I want to tell people the date."*
> *"Here's a voice note — [paste]. Make it a caption."*
> *"Write the email that opens applications."*

**The Doorkeeper — who's in the room.**
A DM you're unsure about, an application to read, a yes or no to send, a sponsor who wants
in. It tells you straight whether someone's right for the room, then writes the reply —
kind and clear, in your voice.
> *"Read this application. In or out?"*
> *"A kombucha brand wants to sponsor — here's their email."*
> *"Write the yes for the woman who wants to meet someone the way her grandparents did."*

**The Green Room — the people you work with.**
Venues, press, partners, DJs. Not the people in the room — the people who help you build
it. It writes the pitch, the reply, the follow-up. Warm and professional, never salesy.
> *"A loft in Logan Square replied — write me back."*
> *"A podcast wants me on, here's the ask."*
> *"Follow up with the venue that went quiet, without sounding desperate."*

**The Booth — how the room moves.**
The music and the floor. Building your set, finding the opener for a stiff sober room, figuring
out how to get people dancing in daylight, and writing the DJ a brief he can actually follow.
> *"Help me build the set for July 18."*
> *"What do I open with? The room will be stiff and sober at 2pm."*
> *"Write JR a one-page brief he can follow."*

**The Logbook — what the room remembers.** *(Opens after your first event.)*
The morning after, before it fades, you just talk — who came, what you saw, who left
talking to someone. You don't fill out anything. It remembers the couples, learns who fits
the room, and saves the moments worth telling later.
> *"The event just happened. Let me tell you about it."*
> *"Two people I almost didn't let in talked the whole last hour."*

---

## How to talk to them (this is the whole skill)

- **Just say it plainly.** "Write a caption about why there's no bar." That's enough.
- **You can be messy.** Paste a voice note, a half-thought, a screenshot of a DM. They'll
  find the real thing inside it.
- **You'll get one draft, not three.** If you want it different, say so. They'd rather get
  it right than give you homework.
- **If something feels off, tell them in your words.** "That felt like marketing." "That
  doesn't sound like me." They take the note — and after events, the Logbook remembers it
  so the whole team gets more like you over time.
- **You never have to know the rules.** They already do. If a request would cross one of
  your twelve lines, they'll tell you which one and stop.

You're not learning a tool. You're working with a team. Stay in your zone — the curating,
the music, the room — and let them carry the rest.

> **Two places to work:** your **Project chats** (where you think and draft with your team)
> and **Cowork** (where finished plans get done). Read `01-COWORK-workflow-andrea.md` once —
> it's the one habit that keeps you fast and keeps you inside the $20 plan. Short version:
> plan in chat, then say *"make me a Cowork brief"* and paste that into Cowork.

---
---

# Part 2 — Setting it up (one time, ~30 min per project)

*This part is for whoever stands the projects up — you, or someone helping. Once it's done,
the section above is all Andrea ever needs.*

You'll build six **Projects** (Claude Pro calls them Projects; ChatGPT calls them Custom
GPTs — same idea). Each one gets the same heart plus its own job. Do them in this order:
**Front of House → The Crowd → The Doorkeeper → The Green Room → The Booth → The Logbook.**

> **Fastest way (do this):** Everything is pre-bundled in the `claude-project-uploads/`
> folder — one subfolder per project. For each, open the matching subfolder and read
> `_UPLOAD-ME.txt`. It's two steps: **(1)** paste all of `CUSTOM-INSTRUCTIONS.txt` into the
> project's Custom Instructions, **(2)** upload every other file in that subfolder into the
> project's Knowledge. That's it — no hunting for files. The steps below explain what's
> happening under the hood if you want it.

For **each** project:

**1. Create the project.** In Claude.ai, sidebar → **+ New Project**. Name it exactly (e.g.
`Front of House`). Add a one-line description from that project's file.

**2. Paste the Custom Instructions.** Open the project's setup file in `ai-team/projects/`.
It tells you to paste two things into the project's **Custom Instructions**, in this order:
   - First: the whole `=== RESONANCE CORE ===` block from `ai-team/shared/CONSTITUTION-CORE.md`
     (this is identical in all five — that's on purpose).
   - Then: that project's own `=== ROLE: ... ===` block, directly underneath.

**3. Upload the knowledge files.** Each project file lists exactly which documents to upload
(the "Knowledge files to upload" section). Upload those and nothing else — a tight knowledge
shelf retrieves better than a cluttered one.

**4. Settings.** Default model Sonnet for everyday drafts, Opus for high-stakes (press,
founder essays, anything that matters). Leave conversation history and memory on.

**5. Test it.** Open a fresh chat and try one of the example lines from that project's file.
If it sounds like Andrea and honors the twelve lines, it's working. If it sounds generic,
re-check that the Core pasted correctly above the role block.

**The Logbook is a drop-in.** Build and provision it now, but it stays quiet until the
morning after July 18, 2026 — then it becomes the most important room.

**Keeping it alive (almost no work):** The only real maintenance is one update after the
first event — replace the imagined couple in THE SCENE (inside the Core) with the real
couple who met, and re-paste the Core into all five. The Logbook walks Andrea through it.
That single update is what keeps this from ever feeling like a chore: she's not maintaining
a system, she's returning to a story to find out how it ends.

---

*Built 2026-06-03 from a Collective Genius Council (Ross McKay · Tyler Denk · Jeremy Haynes ·
Vincent Hu · April Dunford · Mitch Albom, with Ocean Vuong). Governing principle: the room
writes the instructions.*
