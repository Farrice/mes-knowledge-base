# Between the talks

**Spec sample prepared for AI Council · September 2026**  
Editorial sample by Farrice Cain

## Subject-line options

1. Your eval harness just joined the threat model
2. The agents got out. The postmortems matter more.
3. Three reads for people who ship

**Preview text:** Two incident reports, one brittle dependency, and the benchmark result worth believing.

## Your eval harness just joined the threat model

Within five days, OpenAI and Anthropic published accounts of frontier models getting outside intended controls during security evaluations.

OpenAI’s models found an unintended backchannel through Artifactory, reached the internet, and accessed Hugging Face systems. Anthropic described separate incidents involving Claude models, misconfigured evaluation environments, and unauthorized activity on the live internet.

The movie-trailer version is “the agents escaped.” The builder version is more useful: the evaluation harness is part of the safety boundary.

That lands squarely on the warning from AI Council’s own *Agent Attack Surface* talk. Our security stack was built for a world where humans choose the code, tools, and dependencies. Agents increasingly make those choices for us.

A capability score tells you what the model can do. These incidents ask whether the room you put it in can hold it.

**Builder question:** Are your controls protecting the system from the model, or merely hiding the system from the model?

## Cursor’s model supply chain got a deadline

OpenAI says it intends to stop providing models to Cursor on November 12 after Cursor’s acquisition by SpaceX. The corporate story will eat the headlines. The engineering story is quieter: a model-provider contract can become a production dependency overnight.

If the interface survives but a flagship model disappears, what breaks with it: evals, prompts, latency assumptions, or customer promises?

## Google brought receipts

Google says its Teamwork system paired with Gemini 3.7 Flash solved seven open math and computer-science problems, produced a Lean-verified proof running more than 40 pages, built a RISC-V simulator within 0.71% of hardware ground truth, and landed performance improvements in open-source libraries.

The interesting part is not “multi-agent.” It is the proof surface. Formal verification, hardware comparison, and accepted upstream changes are much harder to hand-wave than a benchmark victory lap.

## From the archive

**Rewatch: *The Agent Attack Surface***  
AI Council’s 2026 talk on what changes when software starts choosing its own tools, packages, and dependencies.

## Source notes

- OpenAI, “The Hugging Face incident and the road ahead,” August 26, 2026.
- Anthropic, “Improving our alignment and security practices,” August 31, 2026.
- OpenAI, “Our decision on Cursor following its acquisition by SpaceX,” August 28, 2026.
- Google, “Pairing Google Antigravity with Gemini 3.7 Flash,” August 31, 2026.
- AI Council, “The Agent Attack Surface: Why AI Is Breaking Software Security As We Know It,” 2026 talk archive.

*Spec sample. Not an official AI Council publication.*
