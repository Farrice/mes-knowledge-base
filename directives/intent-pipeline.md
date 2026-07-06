# Intent Pipeline (MANDATORY)

> Single pipeline for processing every user request. Replaces intent_refiner, pre_flight_validation, expert_auto_routing.

---

## Stage 1: SCORE (Rate 1-5)

+1 each: specific **deliverable** | defined **audience** | stated **context** | clear **end state** | **specific language**

| Score | Next Step |
|-------|-----------|
| 1-2 | → Stage 2 (full DICE) |
| 3 | → Stage 2 (present sharpened version, confirm) |
| 4-5 | → Stage 3 (route directly) |

## Stage 2: SHARPEN (DICE on missing dimensions only, 1 round max)

- **D — Deliverable**: "What concrete thing do you want when this is done?"
- **I — Intended Audience**: "Who specifically will consume this?"
- **C — Context**: "Any constraints, deadlines, or prior work?"
- **E — End State**: "What does 'nailed it' look like?"

Rules: Don't ask all 4 if some are clear. Fill in inferences, confirm. Anti-interrogation: one concise block. After sharpening, present refined intent with score change.

## Stage 3: ROUTE

**Step 1 — Domain match** (primary tool: `python3 execution/expert_router.py route "query"`):

| Request Type | Signals | Default Route | Domain |
|:---|:---|:---|:---|
| Research (Deep) | deep research, analyze market, competitive intel | `/deep-research` + Manus.AI | 12 |
| Research (Standard) | research, find out, fact check | `/research-topic` | 12 |
| Content Creation | write, create, draft, content | Content experts | 2, 7 |
| Strategy/Decision | should I, what's the best, how do I approach | Jim O'Shaughnessy + domain | 12 |
| Copywriting | sales page, email, headline, convert | Cardinal Mason + Harry Dry | 1 |
| Personal Brand | LinkedIn, positioning, brand, authority | Lara Acosta + Caleb Ralston | 3 |
| Ghostwriting | ghostwrite, voice capture, proof run | `/ghostwrite` | — |
| Product/Offer | product, offer, pricing, launch | Nicolas Cole + Monk.AI | 8 |
| Sales/Persuasion | objection, close, persuade, sell | Jeremy Miner + Jason Fladlien | 4 |
| Storytelling | story, narrative, hook, engage | Shaan Puri + Lucas Alpay | 7 |
| Video/Media | video, TikTok, cinematic | Seena Rez + Tao Prompts | 11 |
| AI/Automation | automate, workflow, agent, AI | Nick Saraev + Boris | 6 |
| SEO/Search | rank, SEO, keywords, traffic | Nathan Gotch + Ethan Smith | 9 |
| Design/Visual | design, visual, website, typography | Oren + Kittl + Andy Lo | 10 |
| Audience/Growth | grow, newsletter, subscriber | Tyler Denk + Dan Koe | 13 |
| Mindset/Messaging | stuck, blocked, mindset, messaging | Jeremy Haynes + Heath Brothers | 14 |
| Consumer Research | customer, persona, buyer, psychology | Dai Media + Kallaway | 5 |
| Monetization | monetize, revenue, recurring | Paul James + Sabrina Ramonov | 8 |
| Advertising | ads, paid, campaign, Facebook | Sabri Suby | 15 |
| Real Estate | real estate, listing, property | Joshua Smith | 15 |
| Launch/Innovation | launch, validate, early adopter | Seena Rez + Samuel Thompson | 8, 12 |

Full routing trees: `DOMAIN_REGISTRY.md`

**Step 2 — Mode:**

| Mode | Signals | Effect |
|:---|:---|:---|
| OUTPUT | write me, create, build, draft | Load T1-2, produce artifact |
| EXPERTISE | how should I, advise, review | Load T0-1, expert analysis |
| HYBRID | help me with | Ask: produce or advise? |

**Step 3 — Multi-domain?** Select ensemble via `DOMAIN_REGISTRY.md`.

**Step 3b — Gap Check:** Verify expert coverage → `invocation-cards.md` → `DOMAIN_REGISTRY.md` → if none: trigger `directives/expertise-gap-protocol.md`.

**Step 4 — Load via Context Engine** (semantic-first: `context_retriever.py search "query"`, fallback: T0→T1→T2→T3). Full protocol: `directives/agent-loading-protocol.md`.

**Step 5 — Log routing** (fire-and-forget, never block for analytics):
```bash
python execution/routing_intelligence.py log --request "[summary]" --score [N] --domain "[slug]" --experts "[names]" --tier [N] --mode [mode]
```

## Stage 4: PRESENT (for complex/multi-expert only)

Show domain, expert table, approach. Skip for: single-expert tasks with prior approval, or "just do it."

---

## Step Narrowing

| Condition | Steps shortened |
|-----------|----------------|
| Score 4-5 | Skip Stage 2 |
| Follow-up, same plan | Reuse Stage 3 route |
| "Just do it" | Skip Stage 2 + PRESENT |

If request touches expert domain, all stages fire.

---

## Proactive Deployment

| Cue | Auto-Action |
|-----|-------------|
| LinkedIn, posts, content, hooks | Content/brand (2, 3, 13) |
| Sales page, offer page, email | Copywriting (1) |
| Positioning, brand, differentiation | Brand (3, 12) |
| Products, pricing, monetization | Product (8) |
| SEO, ranking, traffic | SEO (9) |
| Video, TikTok, AI video | Video (11, 2) |
| AI tools, automation, agents | AI (6) |
| Stuck, blocked, afraid | Mindset (14) |
| Design, website, visual identity | Design (10) |
| Pastes transcript / "I watched video" | `/extract` |
| Feels broken, cluttered, slow | `/system-audit` |
| Excited, firing off ideas | Pause → sharpen → execute |

Fallback: `/recommend`

---

## Usage Tracking

| Field | Value |
|-------|-------|
| **Last Activated** | 2026-07-06 (codex parity verifier run) |
| **Activation Count** | 1 |
| **30-Day Review Date** | 2026-08-05 |

*Created: 2026-03-02 | Compressed: 2026-04-13*
