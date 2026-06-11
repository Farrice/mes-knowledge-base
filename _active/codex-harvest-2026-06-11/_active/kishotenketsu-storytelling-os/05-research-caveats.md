# Research Synthesis And Caveats

## Current Research Status

This implementation uses the video transcript as the primary evidence and treats broader narrative-theory material as enrichment. A selective research pass identified dictionary, rhetoric, manga-format, practitioner, and game-design transfer sources that support the general structure while warning against overclaiming.

External research pointers to preserve for future hardening:

- ZDIC on `qichengzhuanhe` / Chinese term history.
- Kotobank on Japanese `kishotenketsu`.
- Kirkpatrick and Xu on Chinese rhetoric context.
- BNF short formats material on yonkoma / 4-koma format.
- September C. Fawkes as a modern practitioner explanation with caveats.
- MCV/Develop coverage of Nintendo-style four-step level-design transfer.

## Working Understanding

Kishotenketsu is commonly described as a four-part narrative structure:

| Term | Working Role |
|---|---|
| Ki | Introduction or establishment |
| Sho | Development or continuation |
| Ten | Turn, change, or shift |
| Ketsu | Conclusion, reconciliation, or integration |

Related terms include `qichengzhuanhe` and variants used in Chinese, Japanese, Korean, Vietnamese, manga/storytelling, and other time-based contexts. The system should not pretend every tradition uses the structure identically.

The strongest implementation point: `Ten` is not always a twist. It is often a recontextualizing turn. The audience's attention comes from the gap between the established pattern and the new element. `Ketsu` then integrates that gap.

## Cultural Guardrails

- Do not call Kishotenketsu "superior" to Western structure.
- Do not say it is conflict-free; say it can be driven by contrast, shift, process, and reconciliation rather than direct antagonistic conflict.
- Do not imply all East Asian storytelling follows one structure.
- Do not package the structure as an "Eastern hack" for Western productivity.
- Do not use Ghibli, manga, or Parasite examples as proof unless they are labeled as transcript-backed, research-backed, or interpretive.
- Do not turn the structure into a rigid four-box template. Use it as an engine choice.

## Claim Boundaries

| Claim | Allowed Wording |
|---|---|
| Universal story structure | "A high-leverage alternative structure for certain writing problems." |
| No conflict | "Not dependent on a villain or direct fight." |
| Western model is bad | "The conflict-first model can be the wrong tool for quieter, internal, world-driven, or reflective material." |
| Used everywhere | "Appears in several East Asian narrative contexts and is often discussed in relation to manga, poetry, and films." |
| Works for marketing | "Transfers well when marketing needs world invitation, process, contrast, or adaptation rather than problem-agitation." |

## Well-Supported Vs Uncertain

| Status | Claim |
|---|---|
| Well-supported | `Qi/ki`, `cheng/sho`, `zhuan/ten`, and `he/ketsu` are widely described as opening/introduction, continuation/development, turn/change, and joining/conclusion. |
| Well-supported | Yonkoma / 4-koma is commonly mapped to the four-part pattern. |
| Well-supported | The structure has been adapted beyond poetry into prose, comics, games, and other sequential media. |
| Uncertain | Exact origin and timeline are not cleanly settled across sources. |
| Uncertain | Specific works should not be claimed as Kishotenketsu unless there is scene-level evidence or creator/critic support. |
| Uncertain | "Used in the Western world" needs specific evidence per domain and should be phrased carefully. |

## Research Questions To Keep Open

1. Which claims about Tang poetry, Japanese/Korean refinement, and manga usage are independently verified?
2. Which Ghibli/Totoro claims are the source's interpretation vs widely supported criticism?
3. How should the OS distinguish `Ten` as surprise from `Ten` as structural recontextualization?
4. Which commercial writing scenarios actually improve from this pass, and which need conflict, proof, or offer clarity first?

## Implementation Rule

Use the structure respectfully and operationally: preserve source boundaries, label enrichment, keep original terms visible, and judge the OS by changed writing behavior rather than by how many cultural references it names.
