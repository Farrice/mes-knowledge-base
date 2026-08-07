# Reference Corpus — status: INCOMPLETE (blind pass NOT run)

The blind-pass protocol (`directives/embodiment-standard.md`) requires **≥2 verbatim published pieces** by the expert that are **not already quoted inside the skill**, so generated output can be judged side-by-side against unseen real work.

**That bar is not met, and no blind pass was run. This skill therefore ships B-tier with the gap named.**

## What was attempted (2026-08-06)

Two genuine, in-scope newsletter issues were located and fetched:

1. **"the lesson I needed to learn?"** — https://mailing.samvanderwielen.com/posts/the-lesson-i-needed-to-learn (~1 year old, 6 min read)
2. **"My wake-up call about online safety"** — https://mailing.samvanderwielen.com/posts/my-wake-up-call-about-online-safety (~11 months old, 4 min read)

Both are correct source material: real published *Sam's Sidebar* issues, in her own voice, in the exact register this skill's email workflows generate — and neither is quoted anywhere in the skill.

**Why they were not usable:** the retrieval tool available in this session returns *summaries with scattered quoted fragments*, not full verbatim body copy. Judging generated output against a summary would produce a false pass — the blind pass tests sentence-level voice, which a summary destroys. Saving them as "corpus" would have gamed the gate rather than passed it.

## Verbatim fragments actually captured

Genuinely useful for voice calibration, but far short of a corpus:

**From "the lesson I needed to learn?"** (Patagonia / Torres del Paine hiking story, Dec 2024):
> "it's better to measure the distance between where you are now vs. where you've been, rather than where you are now vs. where you want to be."

> "Think about how far you've come already in your business, regardless of the results, outcomes, and metrics."

CTA shape: reply with one thing that improved in your business over the past six months, and suggest future topics. *(Note: this is the reply-hook and reverse-VoC mechanic from the extraction, appearing in the wild.)*

**From "My wake-up call about online safety"** (posted a photo of her Long Island beach house; readers identified her exact location):
> "Any innocence I had about my identity or any potential lurkers flew out the window."

> "Creepers gonna creep creep creep..."

She described the triggering email as *"disgusting, assaultive, and illegal."* CTA points at a YouTube video and podcast episode — *"6 ways to protect your privacy (without disappearing from the internet)."*

## What closing this gap requires

Save the **full verbatim body copy** of ≥2 issues into this folder as `.md`, each with a provenance line (URL + date) at the top, then:

```bash
python3 execution/blind_pass.py prepare --expert sam-vander-wielen
# then judge 1-2 Tier-1 workflow outputs side by side against them
python3 execution/blind_pass.py record --expert sam-vander-wielen --verdict PASS|FAIL \
    --notes "[which real pieces, what held / what gave it away]" \
    --generated [path] --reference [path]
```

The two URLs above are the recommended pieces. A-tier promotion additionally requires a Farrice-judged pass.

## Incidental voice signal from these two pieces

Both open on a **concrete personal scene** (a mountain in Chile; a photo of a beach house) and reach the business lesson only afterward. Both close by **asking for a reply**. Neither leads with a framework. That is consistent with the voice captured in `references/source-quotes.md` and is a useful — though unverified — calibration note for the email workflows.
