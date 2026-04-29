# Workflow 05: Sound Bite Deployment Matrix

> **Produces**: Channel-by-channel deployment plan with verbatim sound bites
> **Use When**: Mapping sound bites across all channels for decade-long consistency
> **Genius Context**: Load `genius.md` before executing
> **Prerequisite**: Run `02-peace-soundbite-generator` first

## Pre-Flight

**Required Inputs:**
- Completed PEACE Sound Bite System (from Workflow 02)
- Active channels (website, social platforms, email, ads, sales team, events, print, partnerships)
- Team roles (who creates content for each channel?)

> **🔒 Pre-Flight Gate**: PEACE sound bites must exist and be locked. This workflow deploys — it does NOT modify sound bites.

## Execution

You are Donald Miller deploying sound bites across every customer touchpoint. The mandate: same words, same order, every channel, 10+ years (GP6). No creative variations. No "refreshing." Verbatim.

### Step 1: Channel Inventory

List every active customer-facing channel. For each, identify current messaging status:

| Channel | Active? | Current Messaging | Sound Bite Present? |
|---------|---------|-------------------|-------------------|
| Website (hero) | ✅/❌ | [current header] | ✅/❌ |
| Website (about) | ✅/❌ | [current copy] | ✅/❌ |
| Instagram | ✅/❌ | [bio/captions] | ✅/❌ |
| LinkedIn | ✅/❌ | [headline/posts] | ✅/❌ |
| Email signatures | ✅/❌ | [current sig] | ✅/❌ |
| Sales scripts | ✅/❌ | [opening] | ✅/❌ |
| Business cards | ✅/❌ | [current text] | ✅/❌ |
| Proposals/decks | ✅/❌ | [cover slide] | ✅/❌ |
| Ads (paid) | ✅/❌ | [current copy] | ✅/❌ |
| Newsletter | ✅/❌ | [subject lines] | ✅/❌ |

**Output**: Complete channel inventory with gap analysis.

### Step 2: The Deployment Matrix

For every active channel, specify WHICH sound bite is deployed, WHERE it appears, and the EXACT copy:

```
══════════════════════════════════════════════════
SOUND BITE DEPLOYMENT MATRIX: [BUSINESS NAME]
══════════════════════════════════════════════════

WEBSITE
├── Hero H1: [Problem sound bite — verbatim]
├── Hero subtext: [Empathy + Answer — verbatim]
├── CTA button: [Answer — verbatim]
├── About page opener: [Problem + Empathy — verbatim]
└── Footer tagline: [Change — verbatim]

SOCIAL MEDIA
├── Bio/headline: [Change + Answer — verbatim]
├── Pinned post: [Full PEACE chain]
├── Post templates: [Problem or End Result as opener]
└── Stories/reels hook: [Problem — verbatim]

EMAIL
├── Welcome email subject: [Problem — verbatim]
├── Welcome email opener: [Empathy — verbatim]
├── Signature line: [Change — verbatim]
└── Newsletter subject lines: [Rotate P and E2]

SALES
├── Script opening: [Problem + Empathy]
├── Pitch deck slide 1: [Problem]
├── Pitch deck slide 2: [Answer + Change]
├── Pitch deck closer: [End Result]
└── Proposal cover: [Problem → End Result]

ADVERTISING
├── Headline: [Problem — verbatim]
├── Body: [Empathy + Answer]
├── CTA: [Answer — verbatim]
└── Retargeting: [End Result — verbatim]

PRINT / PHYSICAL
├── Business card: [Answer — verbatim]
├── Signage: [Problem or Change]
└── Packaging: [End Result]
══════════════════════════════════════════════════
```

**Output**: Complete deployment matrix.

### Step 3: Team Assignment Table

Map who is responsible for each deployment:

| Channel | Responsible Person/Role | Sound Bite(s) to Use | Update Frequency | Lock Status |
|---------|----------------------|---------------------|-----------------|-------------|
| Website | [role] | [which bites] | Permanent — no changes | 🔒 LOCKED |
| Social | [role] | [which bites] | Embedded in every post | 🔒 LOCKED |
| Email | [role] | [which bites] | Every send | 🔒 LOCKED |
| Sales | [role] | [which bites] | Every conversation | 🔒 LOCKED |

**The Lock Rule**: Sound bites are LOCKED. No team member may "refresh," "update," or "get creative with" the sound bites. If someone wants to change them, the answer is no. Decade mandate (GP6).

**Output**: Team assignment with lock status.

### Step 4: Consistency Audit Checklist

Create a monthly audit checklist the team uses to verify sound bite consistency:

- [ ] Website hero still displays Problem sound bite verbatim
- [ ] Social bios still contain Change + Answer verbatim
- [ ] Last 10 social posts contain at least one PEACE sound bite each
- [ ] Last 5 emails used Problem or End Result in subject lines
- [ ] Sales team can recite all 5 sound bites from memory
- [ ] No team member has "improved" or "refreshed" any sound bite
- [ ] All new collateral created this month embeds at least one sound bite

**Output**: Monthly audit checklist.

## Output Schema

```yaml
deliverable: "Sound Bite Deployment Matrix"
components:
  channel_inventory: "All channels mapped with gap analysis"
  deployment_matrix: "Channel-by-channel exact copy specifications"
  team_assignments: "Who deploys what, with lock status"
  audit_checklist: "Monthly consistency verification"
deployment: "1 deployment matrix, shared with all team members"
```

## Quality Gate

- [ ] Every active channel has at least one sound bite assigned
- [ ] Sound bites appear VERBATIM — no paraphrasing, no creative variations
- [ ] Team assignments are specific (named roles, not "marketing team")
- [ ] Lock status is explicit on every channel
- [ ] Monthly audit checklist is actionable
- [ ] Decade repetition mandate is documented and communicated

**ENFORCEMENT**: Any creative variation of a sound bite = FATAL (GP6). Sound bites are not suggestions — they are locked, verbatim, permanent.

> **🛡️ Anti-Pattern Check**: Verify against GP5 (Guitar Chord), GP6 (Decade Repetition) in `genius.md`.
