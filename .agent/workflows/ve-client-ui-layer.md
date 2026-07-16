---
description: "/ve-client-ui-layer — Adam Sandler (The Viable Edge): branded clickable KB UI (markdown browser + relationship-narrator graph, Claude-design styled, OSS graph packages) + the anti-slop voice charter."
---

# Client KB UI + Voice Charter (Adam Sandler — The Viable Edge)

Make a folder of markdown feel like a product — and keep its output from reading like slop.

## Steps
1. Load the spine: read `skills/adam-sandler-second-brain-gtm/genius.md` (§Pattern 7 UI/graph-narrator + §Pattern 8 voice charter; disambiguation — NOT the actor).
2. Read and execute `skills/adam-sandler-second-brain-gtm/workflows/07-ve-client-ui-layer.md` exactly. Honor the Execution prompt at `references/prompts-v2/client-kb-ui-and-voice-charter.md`.
3. Wire voice enforcement: `execution/prose_classifier.py check` + `directives/ai-slop-ban-bank.md` + `oren-anti-slop-classifier`.
4. Run the Quality Gate before delivering. UI abstracts the chat box; graph is a NARRATOR; styled to the client's brand; voice charter has all four parts; content KB → charter mandatory.
