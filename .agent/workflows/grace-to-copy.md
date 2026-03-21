---
description: "Grace → Copy pipeline — convert city strategy into executable copy via Cardinal Mason, Luke Iha, and Lara Acosta"
---

# /grace-to-copy — Strategy to Copy Pipeline

Take Grace Andrews' city map strategy and convert it into executable copy across email, ads, LinkedIn, and sales pages. The bridge from "what content to make" to "what words to put on the page."

**The problem this solves**: Grace designs the architecture. But architecture without copy is a blueprint without a builder. This command hands off Grace's strategic output to the copywriting experts who know how to write for each trust stage and platform.

## Usage

```
/grace-to-copy --input [path to city map or trust pathway output]
/grace-to-copy --trust-stage [attention|connection|trust|conversion] --platform [linkedin|email|ads|sales-page]
/grace-to-copy --full  # Generates copy for ALL trust stages across ALL platforms
```

## Steps

### 1. Load Grace Context
Read these files:
1. `skills/grace-andrews-media-company/SKILL.md`
2. `skills/grace-andrews-media-company/genius.md`

Read the city map or trust pathway output (from the `--input` path or generate inline using Workflow 01/02).

### 2. Map Trust Stages to Copy Experts

| Trust Stage | Copy Expert | Their Role | What They Produce |
|------------|------------|-----------|-------------------|
| **Attention** | Seena Rez + Luke Iha | Hook engineering + proof-first hooks | Social hooks, thumbnail copy, ad hooks |
| **Discoverability** | Lara Acosta | LinkedIn + social platform copy | LinkedIn posts, Twitter threads, social bios |
| **Connection** | Nicolas Cole | Newsletter + long-form narrative | Email sequences, newsletter editions, blog posts |
| **Trust** | Luke Iha | Proof stacking + mechanism copy | Case study copy, testimonial layouts, authority content |
| **Conversion** | Cardinal Mason + Luke Iha | Email sequences + sales copy | Sales pages, launch emails, CTAs, VSLs |

### 2.5. Load Oral/Written Culture Matrix (a16z Enhancement)
Read `skills/andreessen-horowitz-new-media/genius.md` → Oral/Written Culture Matrix section.

Tag each trust stage's copy output for cultural mode:

| Trust Stage | Primary Culture Mode | Why |
|------------|---------------------|-----|
| **Attention** | Oral | Burst energy, hooks, interpersonal — campfire physics |
| **Discoverability** | Hybrid (LinkedIn) | Personal story + professional authority |
| **Connection** | Written | Depth builds connection — newsletter, long-form |
| **Trust** | Written | Evidence, proof ladders, case studies need analytical rigor |
| **Conversion** | Written → Direct | Email sequences, sales pages — written culture anchors the close |

**Rule**: Ensure written-culture copy is produced BEFORE oral-culture extraction. Connection/Trust stage content anchors → Attention stage hooks are derived from those anchors.

### 3. Load Copy Expert Skills (per stage)

For each trust stage the user specifies (or ALL if `--full`):

**Attention Stage Copy**:
- Load `skills/luke-iha-proof-copy/SKILL.md` — vicious hooks
- Execute hook generation for the attention district content

**Connection Stage Copy**:
- Load `skills/nicolas-cole-ghostwriting/SKILL.md` — newsletter voice
- Generate 3 newsletter editions that build connection

**Trust Stage Copy**:
- Load `skills/luke-iha-proof-copy/SKILL.md` — proof ladder
- Build proof stacks for 2-3 key authority claims

**Conversion Stage Copy**:
- Load `skills/cardinal-mason/SKILL.md` — email sequences
- Generate a 5-email conversion sequence bridging trust to sale

**LinkedIn Execution**:
- Load `skills/lara-acosta/SKILL.md` — LinkedIn content
- Generate 5 LinkedIn posts mapped to different trust stages

### 4. Cross-Reference with City Map
Verify that every piece of copy:
- ✅ Serves a specific trust stage (tagged)
- ✅ Connects to the next trust stage (has a bridge)
- ✅ Matches the voice register for that trust stage (from Brand Voice Districts, Workflow 10)

### 5. Assemble Copy Kit
Package all copy into a single organized deliverable.

### 6. Save Output
Save to `.tmp/grace-to-copy/copy-kit-[date].md`

## Output Structure

```
# Copy Kit: [Brand Name]
## Mapped to City: [Reference to city map]

### Attention Stage Copy
- [X] hooks (scored)
- [X] thumbnail copy options
- [X] social ad concepts

### Connection Stage Copy
- [X] newsletter editions (drafted)
- [X] long-form blog post outlines

### Trust Stage Copy
- [X] proof stacks
- [X] case study frameworks
- [X] authority content outlines

### Conversion Stage Copy
- [X]-email conversion sequence
- Sales page copy blocks
- CTA variations

### LinkedIn Execution
- [X] posts across trust stages
- Profile optimization recommendations
```
