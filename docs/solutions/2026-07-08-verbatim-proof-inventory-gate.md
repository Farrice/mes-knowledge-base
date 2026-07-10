---
name: Verbatim Proof Inventory Gate for Multi-Agent Content Builds
problem_signature: agents writing social-proof copy silently alter or invent testimonials ("Allison/Sammy" altered quotes, fabricated "Sarah" example) — paraphrase and placeholder quotes ship looking verbatim
domain: content-orchestration
tags: [testimonials, fact-verification, multi-agent, fabrication, workflow-gates, client-work]
date: 2026-07-08
status: active
session: cooz-war-funnel
---

## Problem

In a multi-agent build (Cooz "war on fitness industry" funnel), any agent that
needs a client quote will produce one — tightened, paraphrased, or invented —
and present it as verbatim. This session caught three instances before
delivery: two testimonials altered from source (Allison, Sammy) in an early
pass, and a fabricated "Sarah: 'I stopped hating the mirror'" example in the
strategy spine that a downstream builder could have mistaken for a real client.
Fabricated social proof on a paying client's page is a reputation-ending
failure that reads polished right up until someone checks.

## Root Cause

Quotes are the one content type where "improve the writing" IS the corruption.
Builders optimize for rhythm and length; a quote that's been tightened is a
quote that's been falsified. Without a single canonical source and a
character-level check, every agent hop is another chance for silent mutation.

## Approach That Worked

1. **Scout-first, inventory-as-authority**: before any builder runs, one agent
   scrapes every testimonial VERBATIM into a tagged inventory
   (RAW-PROOF-INVENTORY.md: numbered entries, source URL, [FEELING]/[AESTHETIC]/
   [PERFORMANCE] tags, dupes flagged). Hard rule in the prompt: "a quote you
   can't retrieve exactly does not go in the inventory."
2. **Builders quote only from the inventory**, by entry number, ellipses
   preserved from source. If the scout fails, builders write labeled
   placeholder slots — never sample quotes.
3. **Fact-verifier gate checks character-for-character** against the inventory
   and labels each quote VERIFIED with entry number. Any quote not in the
   inventory = fabrication = MUST-FIX cut, no debate.
4. **Format examples in strategy docs must be marked as such** ("FORMAT
   EXAMPLE ONLY — no client 'Sarah' exists") or a downstream builder will
   treat them as data. This is how the near-miss happened.

## Dead Ends

- Trusting "verbatim" claims in builder summaries — the altered Allison/Sammy
  quotes were described as verbatim by the agent that altered them.
- Letting the strategy doc use a realistic-looking illustrative quote without
  an explicit not-real marker.

## Verification

Fact gate labeled all 5 client-facing quotes VERIFIED with inventory entry
numbers (#22, #29, #30, #31, #34); the altered/fabricated ones were caught and
cut before any client-facing file carried them.

## Weaker-Model Trap

A weaker builder "cleans up" a quote's grammar as part of general polish and
reports it verbatim because the meaning didn't change — meaning-preservation
is not the standard, character-identity is. The gate must diff text, not
intent.

## Pointers

- `_active/coach-cooz/16-war-on-fitness-industry/03-testimonial-weaponization/RAW-PROOF-INVENTORY.md`
- `_active/coach-cooz/16-war-on-fitness-industry/05-review-gates/FACT-VERIFY-REPORT.md`
- Workflow script: session `workflows/scripts/cooz-war-funnel-wf_0ae371b7-0f0.js`
- Related: [[2026-07-07-parallel-builders-stale-contracts]] (the stale sibling
  files this session's fixer quarantined into `_archive-stale-pass/` are the
  same class of failure)
