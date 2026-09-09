---
title: One-page visual readout of a client system beats forty markdown files
date: 2026-09-02
tags: [jen, readout, artifact, visual-delivery, client-systems]
status: active
---

## Problem

After a night of building Jen's content system across two lanes (ENGINE-V2, Valley Editions, weeks 1–3, funnel math, vault, amendments), Farrice could not see whether it worked: "I can't even see the captions, the reels, the scripts. The markdown files are impossible to read." Every gate passed; the product was invisible. The reset memo had already named this failure ("we showed the system before the post") and the next session repeated it.

## Solution

One HTML artifact, generated from the real outputs, in the client's own palette and type, with five sections in this order: the honest read (why it isn't landing), the loop as a stage strip, every produced post as a card (actual frame thumbnails, caption as it posts, reel beat by beat, reply routing, placeholder badge), the client's assets marked used/unused with thumbnails, gates and receipts, and the gaps against the competitor being replicated. Thumbnails are resized JPEGs base64-embedded (sips + ffmpeg first frame), so the page is ~2.8 MB and needs no external assets.

Farrice's verdict: "That gave me the exact high-level overview of everything I need to do to understand where we went wrong and what's happening. We need to be able to replicate that."

Banked as `execution/jen_os_page_thumbs.py` + `execution/jen_os_page.py`; POSTS / MEMOS / HERS / OTHER tables are the data to edit as weeks ship. Publish with the Artifact tool using the existing url to keep the link.

## When to reach for it

- A client system has more than ~10 files and the operator asks "how does this work" or "is this even using X."
- A deliverable's quality question ("are the hooks good?") can only be judged by seeing the pieces side by side.
- Before any second rebuild: show the posts, then the calendar, then the system. Never the reverse.

## Related

- Memory `research-brief-system` (Visual Delivery Doctrine: reusable deliverables default to briefs, never md walls)
- Memory `jen-presentation-framing`, `jen-hands-off-photo-look`
- `_active/clients/jen-listings/06-system/ENGINE-V2.md`
