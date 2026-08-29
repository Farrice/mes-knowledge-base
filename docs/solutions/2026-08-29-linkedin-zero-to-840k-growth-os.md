---
name: linkedin-zero-to-840k-growth-os
problem_signature: "Turn a YouTube video and full HubSpot guide into a source-grounded, runnable LinkedIn growth operating system for personal and client accounts"
domain: system
tags: [linkedin, source-to-skill, diandra, ben-meer, hubspot, rule-of-100]
date: 2026-08-29
status: verified
session: "LinkedIn: 800K Growth OS - Build and Validate"
---

## Problem

The source taught seven useful LinkedIn growth moves but did not provide persistent client state, deterministic idea ranking, a safe boundary around peer engagement, or a proof-bounded review loop. A static summary would leave the operator to connect profile, content, distribution, and analytics by hand.

## Root Cause

The source was optimized as educational media rather than an operating system. The workspace already had strong Diandra components, but lacked one bounded route that joined Ben Meer's idea selection and Rule-of-100 mechanics to those existing components.

## Approach That Worked

1. Harvest the video transcript, reviewed frames, full HubSpot guide, and hook deck into one evidence package with uncertainty separated from observed material.
2. Extend `/diandra-linkedin-system` with one workflow, one born-v2 prompt, one source reference, and one stdlib runtime that initializes account state, ranks ideas, reviews results, and rejects false-green inputs.

## Dead Ends

The default YouTube downloader entered a PO-token retry loop; the documented embedded-client fallback acquired the public video. The newer video-context builder also depended on absent helper modules in this lane, so the already-proven Watch VTT parser assembled the canonical source package instead.

## Verification

- `verify_video_context_source_package.py`: PASS, 316 transcript rows and 4,279 clean words.
- `verify_linkedin_840k_growth_os.py`: PASS for source, wiring, runtime, and safeguards.
- `test_linkedin_growth_os.py`: PASS for initialization, ranking, review, and three negative controls.
- `renaissance_audit.py --quiet`: 3,927 v2 prompt files pass, zero fail.
- Cold-start workspace initialization and `doctor`: PASS.
- Anti-slop classifier on the new prompt: CLEAN, score 0/10.

## Weaker-Model Trap

Do not create a new mega-skill or imply that the reported 840K result will reproduce. Keep Diandra as function owner, preserve the source as a bounded layer, require account data before outcome claims, and separate private peer feedback from coordinated public engagement.

## Pointers

- `extractions/video-context/GKbNTGLfd34/source-to-skill-contract.md`
- `skills/diandra-escobar-linkedin-growth/workflows/23-zero-to-840k-operating-system.md`
- `execution/linkedin_growth_os.py`
- `execution/verify_linkedin_840k_growth_os.py`
