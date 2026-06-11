# Coach Cooz Gem Setup Guide
## Setup Principle

Do not build one giant Cooz Gem.

Build a small team of specialized Gems:

- one brain for brand/offer/voice guardrails
- one guard for proof and claims
- one creator for content
- one operator for LinkedIn distribution
- one builder for design and marketing assets
- one assistant for service operations

This keeps each Gem focused and easier for Cooz to use.

## How To Create Each Gem

In Gemini:

1. Go to `gemini.google.com`.
2. Open Explore Gems.
3. Create a new Gem.
4. Give it the exact Gem name from the file.
5. Paste the full "Copy-Paste Gem Instructions" block into the instructions field.
6. Add the recommended knowledge files if the account supports Gem knowledge files.
7. Preview the Gem with one test prompt from `COOZ-GEM-TESTING-PROTOCOL.md`.
8. Save only after the output passes the relevant quality gate.

Google notes that Gem instructions should include goals, desired behaviors, and preferred formats. Google also documents that Gems can use uploaded files for more context.

## Knowledge File Priority

If Gemini lets you upload files to the Gem, upload only the files each Gem needs.

Do not upload everything into every Gem.

Use this order:

1. Master north star, positioning, offer, service, triage, proof docs.
2. Avatar and content strategy docs.
3. Example posts and platform cascade.
4. Voice memo prompts and proof inventory.
5. Any future Cooz transcripts, client-safe notes, or approved examples.

## Recommended File Uploads By Gem

| Gem | Upload These First |
|---|---|
| Master Brand Brain | North Star, Positioning, Offer Architecture, Proof Map, Avatar Profile |
| Proof And Claims Guard | Proof Map, Offer Architecture, Triage System, client permission tracker if created |
| Content Flywheel | Avatar Profile, Content Strategy, LinkedIn Posts, Platform Cascade, Voice Memo Prompts, Proof Map |
| LinkedIn Distribution | Avatar Profile, Positioning Lock, Content Strategy, Triage System, Proof Map |
| Design And Marketing Asset Builder | Content Strategy, Platform Cascade, Positioning Lock, Offer Architecture, Proof Map |
| Service Ops | Service Map, Triage System, Offer Architecture, Proof Map, Avatar Profile |

## If File Uploads Are Limited

Use the Gem instructions anyway.

When starting a chat, paste the most relevant section from the source docs before asking for output.

Example:

```text
Use this source as truth for this task:

<source_truth>
[Paste the relevant section from Content Strategy V3 or Proof Map]
</source_truth>

Now help me turn this voice memo into one LinkedIn post and one Instagram carousel.
```

## Sharing Caution

Google states that people with access to a shared Gem can view the Gem instructions and uploaded files, and editors can change or delete them.

Do not share Gems that include private client notes, client names, measurement details, or internal revenue strategy unless the access level and file visibility are intentional.

Best default:

- Farrice owns the master Gems.
- Cooz gets viewer access when possible.
- If Cooz needs edit access, use copies that do not include sensitive client files.

## Naming Convention

Use these names:

1. `Cooz Master Brand Brain`
2. `Cooz Proof And Claims Guard`
3. `Cooz Content Flywheel`
4. `Cooz LinkedIn Distribution`
5. `Cooz Design And Marketing Asset Builder`
6. `Cooz Service Ops`

## Human Approval Rules

Cooz can use Gem outputs directly for:

- comment drafts
- connection note drafts
- service check-in drafts
- internal prep notes
- rough content ideas
- voice memo prompts

Farrice should review before public use:

- flagship LinkedIn posts
- profile copy
- offer pages
- claim-heavy proof posts
- client stories
- Instagram carousels
- YouTube scripts
- anything using named clients, numbers, or measurement claims

## The Main Rule For Cooz

Do not accept the first answer if it sounds like a trainer on the internet.

Run this:

```text
Audit this against the Coach Cooz quality gate. Tell me what feels generic, over-polished, vague, unsupported, or weak for my buyer. Then rewrite it once.
```
