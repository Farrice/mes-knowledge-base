# Workflow 03 — Voice & Performance Direction Plan

**Produces:** a **voice and performance plan** — voice-bed casting spec per character, per-line
direction written as a director's note, the consistency rung chosen per character with its known
failure mode, the audio-stem handoff spec, and the ADR seam where AI hands off to a human.

**Use when:** anyone speaks on camera; the same character sounds like a different person from shot
to shot; a piece has to survive a real mix; or you're deciding whether to hire voice actors.

**Load first:** `genius.md` section F. Built almost entirely from [VOICE26] (2026-06-23) and
[ANIME26] (2026-06-30).

> **Tool-independent by design.** The plan names *rungs and seams*, not products. Which tool sits on
> which rung changes monthly — that mapping lives in `references/era-bound-mechanics.md`.

---

## Step 0 — The problem, stated the way he states it

> *"If you've ever tried to put together an AI film, then you probably have ran into one big problem.
> The voices are crazy inconsistent."* — [VOICE26] 00:00–00:09

And the sequencing insight that reorganises the whole pipeline:

> *"You might think that it's now time to create our voices. But when you're working in an AI
> pipeline, it's actually easier to apply the voices in post-production using ADR."*
> — [ANIME26] 08:49–09:00

**Voice is a post decision made in pre-production.** You plan it before you shoot; you execute it
after the picture moves.

## Step 1 — Cast the voice as an asset, with range

The character sheet's logic, applied to sound. *"All you need is about 15 seconds of your character's
performance. Now, it is better if you have different stylistic clips to inform the tonality of your
character when they're performing different types of audio. So, for example, 15 seconds of them being
kind of sad or 15 seconds of them being excited."* [VOICE26] 13:50–14:12.

Spec per speaking character:

- **Source** — who is the voice? (you, a hired actor, a licensed library voice). Name a real source;
  a voice with no owner is a continuity risk and a rights risk.
- **Registers** — a short clip per emotional register the script actually needs. Neutral is not
  enough if the character breaks down in scene four.
- **Where it's carried** — the bed is a *file*, referenced into generation, not a setting you retype.
- **Rights note** — same discipline as the IP gate in Workflow 01. A cloned voice needs a consenting
  owner.

## Step 2 — Write the line as a director's note

His prompt shape is a note to a performer, not a query to a machine — camera behaviour + **the line
in quotation marks** + the emotional state + a camera constraint:

> *"a handheld camera shot of a man with trepidation saying, 'So, I've been thinking a lot lately and
> I don't know if we should drink coffee anymore.'"* … *"he's having a serious conversation, really
> reinforcing what we want to see from the character, and then the camera stays on the man. We don't
> want the camera to be moving around the scene."* — [VOICE26] 03:00–03:17

Ordering follows CCR — camera, character, rig [CINE26] 13:12.

And keep the *critique* in the same register. When a performance is wrong he says what a director
would say on set: *"the director on set needs to tell her, 'Hey, you got to look at me. You're
breaking the fourth wall a little too much. You're making the audience uncomfortable.'"* [CINE26]
13:41–13:47. **Naming the fault in performance language is what makes the fix findable.** "The model
is bad at faces" is not a note.

## Step 3 — Choose the consistency rung, per character

Four rungs, each with the failure Ward observed on camera. Pick per character, and write down why.

| Rung | What it is | Known failure | Use when |
|---|---|---|---|
| **1 — Prompt-directed native audio** | Describe the accent/delivery; take whatever the generator sings | *"This tends to work better if your characters are much more over the top. Whenever they are more basic as characters, it can be very noticeable that the voice will change from scene to scene."* [VOICE26] 01:54–02:07 | Broad or comic characters; single-shot appearances |
| **2 — The generator's built-in voice clone** | Clone a voice inside the video tool | Rejected for professional work: *"you can hear that metallic AI timbre that ultimately is not what you would want inside a professional project."* [VOICE26] 07:00–07:12 | Speed tests only |
| **3 — Speech-to-speech replacement + stem re-layer** | Convert the generated read to a target voice, then rebuild the world around it | Strips the room: *"the voice is now consistent, but the big problem is the sound effects and kind of room tone are not being introduced into the scene."* [VOICE26] 08:38–08:46. Fix: isolate the background stem, re-layer, and *"adjust EQ and add in reverb if they're inside of a room just to help it match and feel like it lives together in the scene."* 10:07–10:17 | You already have takes you love and only the voice is wrong |
| **4 — Voice-conditioned generation** *(his current best)* | Pass the voice bed as a reference *into* the generation, so performance and voice are produced together | Close, not identical: *"it's not identical to my voice, but it's pretty much as close as you could hope to get utilizing AI tools before you literally have to go through the ADR process."* [VOICE26] 13:33–13:43 | Default for any character with more than one line |

**The ceiling is named, not hidden.** Rung 4 is where AI stops. Above it is a human.

## Step 4 — Plan the ADR seam (the hybrid rule)

The load-bearing hybrid move in this skill, and it inverts traditional practice:

> *"You're going to take the voice that AI gives you, and then have a live-action voice actor speak
> over it. And they're then going to apply the voice once the timing has been worked out and
> animated."* — [ANIME26] 09:02–09:13
>
> *"Work with your voice actors to do ADR in post to match their lips exactly to what the character's
> performance looks like."* — [ANIME26] 18:43–18:49

Traditional ADR locks picture to a human performance. Here **the generation authors the timing** — the
thing that is hardest to art-direct — and **the human matches it**. That inversion is why voice comes
last: relock timing after the fact and you've thrown away the take.

Decide and record: which characters go to ADR, which stay synthetic, and what triggers an escalation
(a hero monologue, an emotional beat rung 4 can't hold, a client who needs a named performer).

## Step 5 — Spec the stem handoff

Editorial and the voice actor need clean material. The enabling step is **source separation**: pull
the voice out of the generated clip and keep everything else. *"Not only did it remove the voice, it
also left the sound effects and the music bed intact."* [ANIME26] 18:33–18:36.

Deliver per shot:
- **Picture** with the generated performance intact (this is the timing reference for ADR)
- **Background stem** — sound effects and room tone, voice removed
- **Isolated voice stem** — the generated read, as the actor's timing/intonation guide
- **A mix note** — where EQ and reverb have to place the new voice in that room [VOICE26] 10:07

## Step 6 — Audition the performance, don't trust the spec

Run the same shot across several generators in parallel and judge on craft, because *"there's not a
best AI video tool on the market… for some specific shots, you may have to hop between different AI
video models."* [FILM26] 13:21–13:31; the parallel-run habit is [VOICE26] 02:21–02:39.

Judge on his four ears:
1. **Timbre** — is it metallic? [VOICE26] 04:09
2. **Presence** — does it sit in the mix, or is it *"muted, like it's really not rising to the
   surface"*? 05:26
3. **Timing** — his highest praise is about timing: *"especially that second shot there, the timing.
   It really is just frankly really really nice."* 05:58
4. **Consistency across two shots** — the whole point. A great single read that changes identity in
   the next shot is a fail. 06:02–06:06

---

## Quality gate

- [ ] Every speaking character has a voice-bed spec with a **named source** and a rights note
- [ ] Registers are specced against what the script actually demands — not neutral-only
- [ ] Every line has a direction note in performer language: camera + line-in-quotes + emotional state + constraint
- [ ] A rung is chosen **per character**, with its known failure mode written next to it
- [ ] Rung 2 is not used for anything shipping
- [ ] The ADR decision is explicit per character, with an escalation trigger named
- [ ] The stem handoff is specced: picture, background stem, isolated voice stem, mix note
- [ ] Audition criteria are the four ears — timbre, presence, timing, cross-shot consistency
- [ ] Voice is sequenced **after** motion, and the plan says why
- [ ] No model name, product name, price or setting anywhere in the output

**Execution prompt:** `references/prompts-v2/voice-performance-plan.md` — honor its Output Contract.
