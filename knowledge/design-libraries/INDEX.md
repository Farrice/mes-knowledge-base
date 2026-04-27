# Brand Design Library

**58 curated DESIGN.md files** sourced from getdesign.md / VoltAgent/awesome-design-md (MIT license — see LICENSE).

- **9 spec-v1** (YAML front-matter + markdown — official April 2026 spec; lints clean with `npx @google/design.md lint`)
- **49 legacy-prose** (descriptive prose only — usable as agent reference, but no YAML tokens; convert before strict spec compliance)

Each file is a production-quality DESIGN.md inspired by a real brand. **Use as reference, not output** — when starting a project, import a brand file then customize at minimum the name, description, and one signature element.

## Usage

```bash
# Browse all brands
python3 execution/design_md_brand_lookup.py list

# Search semantically
python3 execution/design_md_brand_lookup.py search "minimal dev tools"

# Inspect one
python3 execution/design_md_brand_lookup.py info <slug>

# Import as project starter
python3 execution/design_md_brand_lookup.py use <slug> --to ./project/DESIGN.md

# Refresh from upstream getdesign.md
python3 execution/design_md_brand_lookup.py fetch <slug> --force
```

## Spec-v1 Brands (Official Format)

These have YAML token front-matter + markdown rationale. Lint-clean.

| Slug | Brand | Aesthetic |
|---|---|---|
| `airbnb` | **Airbnb** | A warm, generous consumer marketplace anchored on a clean white canvas and Airbnb Rausch (#ff385c), the single brand vol… |
| `airtable` | **Airtable** | A sober, editorial workflow-software interface anchored on white canvas and dark-ink type, where brand voltage comes fro… |
| `apple` | **Apple** | A photography-first interface that turns marketing into a museum gallery. Edge-to-edge product tiles alternate light and… |
| `bmw` | **BMW** | BMW's corporate site — distinct from BMW M's motorsport-bombastic variant, this is a measured and settled corporate-auto… |
| `cal` | **Cal.com** | A clean, calendar-software-first interface anchored on white canvas with black primary CTAs and custom Cal Sans display … |
| `claude` | **Claude** | A warm-canvas editorial interface for Anthropic's Claude product. The system anchors on a tinted cream canvas with serif… |
| `clay` | **Clay** | A vibrant claymation-meets-data interface for Clay.com (GTM data-orchestration platform). Anchors on white canvas with d… |
| `clickhouse` | **ClickHouse** | A high-performance database interface anchored on near-pure black canvas with electric yellow as the brand voltage. Whit… |
| `cohere` | **Cohere** | Cohere's 2026 web system is a controlled enterprise AI interface built from stark white editorial space, deep green-blac… |

## Legacy-Prose Brands

Descriptive prose only (no YAML). Useful as design references; convert to spec-v1 before lint validation.

| Slug | Brand | Aesthetic |
|---|---|---|
| `coinbase` | **Coinbase** | Coinbase's website is a clean, trustworthy crypto platform that communicates financial reliability through a blue-and-wh… |
| `composio` | **Composio** | Composio's interface is a nocturnal command center — a dense, developer-focused darkness punctuated by electric cyan and… |
| `cursor` | **Cursor** | Cursor's website is a study in warm minimalism meets code-editor elegance. The entire experience is built on a warm off-… |
| `elevenlabs` | **ElevenLabs** | ElevenLabs' website is a study in restrained elegance — a near-white canvas (`#ffffff`, `#f5f5f5`) where typography and … |
| `expo` | **Expo** | Expo's interface is a luminous, confidence-radiating developer platform built on the premise that tools for building app… |
| `ferrari` | **Ferrari** | Ferrari's website is a digital editorial — a curated magazine where the Prancing Horse brand is presented with the gravi… |
| `figma` | **Figma** | Figma's interface is the design tool that designed itself — a masterclass in typographic sophistication where a custom v… |
| `framer` | **Framer** | Framer's website is a cinematic, tool-obsessed dark canvas that radiates the confidence of a design tool built by design… |
| `hashicorp` | **HashiCorp** | HashiCorp's website is enterprise infrastructure made tangible — a design system that must communicate the complexity of… |
| `ibm` | **IBM** | IBM's website is the digital embodiment of enterprise authority built on the Carbon Design System — a design language so… |
| `intercom` | **Intercom** | Intercom's website is a warm, confident customer service platform that communicates "AI-first helpdesk" through a clean,… |
| `kraken` | **Kraken** | Kraken's website is a clean, trustworthy crypto exchange that uses purple as its commanding brand color. The design oper… |
| `lamborghini` | **Lamborghini** | Lamborghini's website is a cathedral of darkness — a digital stage where jet-black surfaces stretch infinitely and every… |
| `linear-app` | **Linear** | Linear's website is a masterclass in dark-mode-first product design — a near-black canvas (`#08090a`) where content emer… |
| `lovable` | **Lovable** | Lovable's website radiates warmth through restraint. The entire page sits on a creamy, parchment-toned background (`#f7f… |
| `minimax` | **MiniMax** | MiniMax's website is a clean, product-showcase platform for a Chinese AI technology company that bridges consumer-friend… |
| `mintlify` | **Mintlify** | Mintlify's website is a study in documentation-as-product design — a white, airy, information-rich surface that treats c… |
| `miro` | **Miro** | Miro's website is a clean, collaborative-tool-forward platform that communicates "visual thinking" through generous whit… |
| `mistral-ai` | **Mistral AI** | Mistral AI's interface is a sun-drenched landscape rendered in code — a warm, bold, unapologetically European design tha… |
| `mongodb` | **MongoDB** | MongoDB's website is a deep-forest-meets-terminal experience — a design system rooted in the darkest teal-black (`#001e2… |
| `notion` | **Notion** | Notion's website embodies the philosophy of the tool itself: a blank canvas that gets out of your way. The design system… |
| `nvidia` | **NVIDIA** | NVIDIA's website is a high-contrast, technology-forward experience that communicates raw computational power through des… |
| `ollama` | **Ollama** | Ollama's interface is radical minimalism taken to its logical conclusion — a pure-white void where content floats withou… |
| `opencode-ai` | **OpenCode** | OpenCode's website embodies a terminal-native, monospace-first aesthetic that reflects its identity as an open source AI… |
| `pinterest` | **Pinterest** | Pinterest's website is a warm, inspiration-driven canvas that treats visual discovery like a lifestyle magazine. The des… |
| `posthog` | **PostHog** | PostHog's website feels like a startup's internal wiki that escaped into the wild — warm, irreverent, and deliberately a… |
| `raycast` | **Raycast** | Raycast's marketing site feels like the dark interior of a precision instrument — a Swiss watch case carved from obsidia… |
| `renault` | **Renault** | Renault's website is a vibrant digital showroom that balances French automotive elegance with bold, forward-leaning ener… |
| `replicate` | **Replicate** | Replicate's interface is a developer playground crackling with creative energy — a bold, high-contrast design that feels… |
| `resend` | **Resend** | Resend's website is a dark, cinematic canvas that treats email infrastructure like a luxury product. The entire page is … |
| `revolut` | **Revolut** | Revolut's website is fintech confidence distilled into pixels — a design system that communicates "your money is in capa… |
| `runwayml` | **Runway** | Runway's interface is a cinematic reel brought to life as a website — a dark, editorial, film-production-grade design wh… |
| `sanity` | **Sanity** | Sanity's website is a developer-content platform rendered as a nocturnal command center -- dark, precise, and deeply str… |
| `sentry` | **Sentry** | Sentry's website is a dark-mode-first developer tool interface that speaks the language of code editors and terminal win… |
| `spacex` | **SpaceX** | SpaceX's website is a full-screen cinematic experience that treats aerospace engineering like a film — every section is … |
| `spotify` | **Spotify** | Spotify's web interface is a dark, immersive music player that wraps listeners in a near-black cocoon (`#121212`, `#1818… |
| `stripe` | **Stripe** | Stripe's website is the gold standard of fintech design -- a system that manages to feel simultaneously technical and lu… |
| `supabase` | **Supabase** | Supabase's website is a dark-mode-native developer platform that channels the aesthetic of a premium code editor — deep … |
| `superhuman` | **Superhuman** | Superhuman's website feels like opening a luxury envelope — predominantly white, immaculately clean, with a single drama… |
| `tesla` | **Tesla** | Tesla's website is an exercise in radical subtraction — a digital showroom where the product is everything and the inter… |
| `together-ai` | **Together AI** | Together AI's interface is a pastel-gradient dreamscape built for enterprise AI infrastructure — a design that somehow m… |
| `uber` | **Uber** | Uber's design language is a masterclass in confident minimalism -- a black-and-white universe where every pixel serves a… |
| `vercel` | **Vercel** | Vercel's website is the visual thesis of developer infrastructure made invisible — a design system so restrained it bord… |
| `voltagent` | **VoltAgent** | VoltAgent's interface is a deep-space command terminal for the AI age — a developer-facing darkness built on near-pure-b… |
| `warp` | **Warp** | Warp's website feels like sitting at a campfire in a deep forest — warm, dark, and alive with quiet confidence. Unlike t… |
| `webflow` | **Webflow** | Webflow's website is a visually rich, tool-forward platform that communicates "design without code" through clean white … |
| `wise` | **Wise** | Wise's website is a bold, confident fintech platform that communicates "money without borders" through massive typograph… |
| `x-ai` | **xAI** | xAI's website is a masterclass in dark-first, monospace-driven brutalist minimalism -- a design system that feels like i… |
| `zapier` | **Zapier** | Zapier's website radiates warm, approachable professionalism. It rejects the cold monochrome minimalism of developer too… |

---

Source: getdesign.md (MIT). Original collection by VoltAgent — https://github.com/VoltAgent/awesome-design-md
