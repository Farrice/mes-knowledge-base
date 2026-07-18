# Provenance — lulu-cheng-meservey-communications repair pass (2026-07-18)

Anchor → source file + location, for the 8 anti-pattern items rewritten as
sourced list bullets in `genius.md § Lulu Cheng Meservey Would Never...`.
Source file: `extractions/lulu-cheng-meservey/transcript.txt` (82,334 bytes,
single-file transcript, no line numbers in the source — it is one long
paragraph-style ASR transcript, so location is given as the nearest unique
surrounding phrase, confirmed via `grep -n -i -o` this pass).

| Anchor | Quote | Nearest transcript context |
|---|---|---|
| AN-1 | "cobbled together some words, run it through Chat GPT, and then hit publish" | "...release things that have no voice or vision of the founder in there. Just random collection of generic people could have cobbled together some words, run it through Chat GPT, and then hit publish." |
| AN-1 | "the crux of it has to come directly from you speaking in the first person" | "...some of it has to come from you. The crux of it has to come directly from you speaking in the first person. And I think it has to be the founder..." |
| AN-2 | "CrowdStrike is actively working with customers impacted by a defect found in a single content update for Windows hosts" | "...Can we talk about the Crowd Strike rewrite that you did? Sure. Okay. So this was the original message. CrowdStrike is actively working with customers impacted by a defect found in a single content update for Windows hosts. Mac and Linux hosts are not impacted." |
| AN-3 | "I've always wanted to do this and now here it is and I'm excited to announce because I've done this and it was hard and congratulations to me" | "...experience gone wild and uh the whole thing is I've always wanted to do this and now here it is and I'm excited to announce because I've done this and it was hard and congratulations to me and you kind of forget to tell people why any of it should matter to them." |
| AN-4 | "the energy of an al-Qaeda hostage video is coming through in their post" | "...can you amplify this? Can you tweet? Can you reply? And you can tell when someone is doing it because the like the energy of an al-Qaeda hostage video is coming through in their post." |
| AN-5 | "I spend 487 hours learning to do this and this is what I discovered" | "...one of the most common formulas is basically goes like this. I spend 487 hours learning to do this and this is what I discovered." |
| AN-5 | "disgusts me on a really viscerable level" | "...there are people who want engagement just for the sake of engagement. And it disgusts me on a really viscerable level. Like I feel exploited and taken advantage of..." (transcript's own ASR spelling of "visceral") |
| AN-5 | "after the cognition launch with the with Devon, there were some launches that were like tweet for tweet almost word for word following the template" | "...you're trying to outrun the thing that works. Like once something works, everybody starts doing it. Um, after the cognition launch with the with Devon, there were some launches that were like tweet for tweet almost word for word following the template..." |
| AN-6 | "sit on a can of gasoline and hope that you'll end up at your office" | "...you need to convert the attention into motion. It's like if you were to just sit on a can of gasoline and hope that you'll end up at your office." |
| AN-6 | "it's kind of this empty cycle" | "...if you're getting attention just for the sake of attention, it's kind of this empty cycle and then you're on the rat race and then your dopamine goes away..." |
| AN-7 | "I don't care that he's in a Lincoln commercial" | "...like Matthew McConna is cool, but I don't care that he's in a Lincoln commercial. Yeah. Yeah. Exactly. Oh, you didn't go buy a Lincoln when you saw the commercial." (transcript's ASR renders "McConaughey" as "McConna") |
| AN-7 | "he's the ultimate UT fanboy and he's on the sidelines of every single football game he's like hitting the drum at big games" | "...he's the ultimate UT fanboy and he's on the sidelines of every single football game he's like hitting the drum at big games and I'm like Matthew Mccah you're the man cuz he's there cuz he loves it." |
| AN-8 | "Coca-Cola versus Pepsi or Chick-fil-A versus Taco Bell... created an unnecessary debate among your own base" | "...if they had said, 'We're choosing whatever Coca-Cola versus Pepsi or Chick-fil-A versus Taco Bell.' Now, you've just created an unnecessary debate among your own base, which is distracting." |
| AN-8 | "you have created civil war among your employees" | "...if you were to choose a political party to support. Now you have created civil war among your employees, right?" |

## How to Use This Skill (Model Calibration) — supporting anchors

| Quote | Location |
|---|---|
| "if the writing is bad, it's better for it to be bad and honest" | "...polished to the point where it loses its soul. Yeah. If the writing is bad, it's better for it to be bad and honest, right?" |
| "cobbled together some words, ran it through ChatGPT, and hit publish" | see AN-1 above (paraphrase mirrors AN-1's already-verified quote) |

## Method

All quotes located via `grep -n -i -o ".\{N\}<phrase>.\{N\}" extractions/lulu-cheng-meservey/transcript.txt` against the actual file on disk this repair pass (2026-07-18), not recalled from memory or invented. No quote in this file or in the repaired `genius.md` anti-pattern section lacks a verbatim grep hit in the source transcript.
