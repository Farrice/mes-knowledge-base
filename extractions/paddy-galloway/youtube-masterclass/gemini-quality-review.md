# Full-video Gemini test: useful perception, unreliable precise extraction

**Verdict: retain Gemini as an optional perception aid; do not replace the source-grounded watch/extraction workflow.** One real request processed the entire 02:45:08 video at 1 fps, low resolution. It completed remotely after the local connection timed out. The response was recovered from the matching Google AI Studio log, without a second inference request.

## What was actually tested

The model was Gemini 3.8 Flash through the Interactions API. The input was the public YouTube URL, offsets 0–9908 seconds, and an analysis question. No transcript, chapter names or summary were supplied. This was static video understanding, not agentic seeking. One frame per second is sampling; it does not inspect every original video frame.

The request asked for whole-video coverage, visual evidence, methods, counterexamples and final-section content. The output contains observations from the beginning through the last minute. That demonstrates successful video-input processing, not exhaustive understanding or correct timestamps. The preserved transcript contains 39,091 words and provides a separate textual evidence channel.

## Recovery and usage

Google log: `v1_ChdYOXFvYW9IbURlZm9xdHNQd2VPR3FBVRIXWDlxb2FvSG1EZWZvcXRzUHdlT0dxQVU`, project Gemini Antigravity; created Sep 14, 2026, 10:50:12 PM as displayed by AI Studio. Status: 200 / completed. Downloaded output JSON is preserved as `gemini-recovered-response.json`; readable model output is `gemini-video-analysis.md`. Original timeout receipt is preserved separately.

The returned counters are inconsistent: total input 0; raw prompt 1,048,427; total tokens 1,014,815; output 6,052; modality details list 901,622 video tokens and 39,909 text tokens, and 6,056 output text tokens. Tool-use and thought counters are zero. Zero input is plainly incompatible with the other counters and is not treated as free input.

At the checked rates of $0.75/M input and $3.75/M output, using the larger raw-prompt count and larger output count yields **about $0.81** for this request. This is a usage-derived planning estimate, **not a verified invoice**. Actual billing remains unreconciled; the conservative $1.25 reservation remains against the $10 authorization. No new paid dispatch is permitted by this trial while that reconciliation hold exists. No second call, automated retry or fallback ran.

## Independent checks

Browser observations below used the actual YouTube player and visible playback time, not an unloaded poster image. Screenshots are in this task's tool record. These checks are a small diagnostic sample, not an accuracy percentage for the entire output.

| Gemini claim | Independent evidence | Finding |
|---|---|---|
| Host name lower-third at 00:41 | Loaded, paused player at 00:41 shows a wide studio two-shot without that lower-third | Exact visual citation fails. Host surname should not be established from this claim. |
| Astrophotography comparison graphic at 01:15:36 | Loaded player at 01:15:36 shows the curly-haired speaker at the desk; the chapter is thumbnail production | Exact visual citation fails. The substantive astrophotography example is earlier in the captions, around 00:11–00:14. |
| Dog Instagram profile projected at 02:44:34 | At 02:44:34 there is a wide two-shot; at 02:44:39 the fluffypacino profile is visibly projected | Correct late-video visual subject, citation about five seconds early in this sample. |
| Paper-ball/punch demonstration at 01:40–01:42 | Captions place the relevant punch example at 01:59:40–01:59:49 | Material timestamp error, roughly eighteen minutes. |
| A fixed 50–60 character title limit | Captions at 01:28:52–01:29:03 introduce this as a common rule being questioned; the Porsche sequence later earns additional length | The summary turns a qualified discussion into a rule the expert explicitly complicates. |
| Revisit formats every 6–12 months | Full-caption search and the relevant internal-ideas passage do not establish this fixed cadence | Unsupported precision excluded from the skill. |
| Repeated packaging swaps are necessary to avoid a permanent recommendation failure | The source's 01:24–01:27 discussion distinguishes good, bad and insufficient data and warns against over-attributing swaps | The generated rule loses the source's restraint; excluded. |

The model's general set description and recognition of a projected dog profile provide useful visual leads. Its chronology mixes correct subjects with incorrect locations; some derived rules add unsupported thresholds. A polished, detailed response is insufficient evidence of fidelity.

## Decision for recurring use

1. Capture captions and public metadata once, preserving source version and timecodes.
2. Let the native analyst extract the spoken method from those captions.
3. Use approved Gemini perception for visual questions that captions cannot answer. Validate decisive claims against actual frames; use smaller explicit intervals when precise visual localization matters.
4. Keep performance, taste and mechanism separate. A model cannot infer private retention or a causal reason for virality from the video alone.
5. Cache the source and completed analysis. Chargeable analysis is on demand; a skill invocation never grants money permission.

Agentic navigation remains NOT_RUN: the current API contract did not provide a verified total internal-processing bound suitable for this job's hard cap. No claim of agentic parity, expert equivalence, measured time savings or guaranteed virality is made. The next engineering improvement is recoverable request tracking plus strict usage reconciliation, followed by a bounded precision test. The original watch skill remains available.

## Price context

At approximately 100–110 low-resolution input tokens per video second and the above input rate, rough input-only costs are $0.05 for ten minutes, $0.14–$0.15 for thirty minutes, $0.27–$0.30 for an hour, and $0.74–$0.82 for this 165-minute source. Output adds roughly $0.02 for 6,000 tokens. Audio treatment, model, resolution, repeated passes and billing details can change the charge; these figures are estimates for this static route, not a universal quote or a subscription entitlement.

Official references: [video understanding](https://ai.google.dev/gemini-api/docs/video-understanding), [pricing](https://ai.google.dev/gemini-api/docs/pricing), [Interactions API](https://ai.google.dev/api/interactions-api).
