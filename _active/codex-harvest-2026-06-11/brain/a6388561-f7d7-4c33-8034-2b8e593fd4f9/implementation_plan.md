# Kingmaker Cross-Pollination Build

The first build gave you the a16z new media skill in isolation. This build cross-pollinates it across your entire expert stack — copywriting, content strategy, ghostwriting, marketing, and media — to create compound capabilities no single skill provides.

## What "Kingmaker" Means Here

In the video, a16z became kingmakers because they could:
1. **Launch** any portfolio company into public consciousness via platform-native campaigns
2. **Dominate** narratives through OODA loop speed advantage
3. **Protect** anyone under attack via flood-the-zone doctrine
4. **Position** any founder as magnetically interesting and direct-to-audience
5. **Export** all of this as a SERVICE to allies

This build gives you all 5 capabilities as compound workflows chained across your existing expert stack.

---

## Proposed Changes

### 1. New Compound Skill: `new-media-kingmaker`

The flagship cross-domain skill. Chains: new media audit → founder positioning → content architecture → launch campaign → crisis protection → narrative warfare — touching Grace Andrews, Luke Iha, Nicolas Cole, Lara Acosta, and Cardinal Mason at each stage.

#### [NEW] [SKILL.md](file:///Users/farricecain/Google%20Antigravity/skills/new-media-kingmaker/SKILL.md)
Cross-domain skill index referencing all 5 sub-workflows

#### [NEW] [01-kingmaker-sprint.md](file:///Users/farricecain/Google%20Antigravity/skills/new-media-kingmaker/workflows/01-kingmaker-sprint.md)
30-day end-to-end "take any founder/brand from invisible to dominant":
- Day 1-3: New media audit + founder voice mining (a16z)
- Day 4-7: Content city blueprint with oral/written culture layer (Grace × a16z)
- Day 8-14: Proof ladder deployment across platforms (Luke Iha × a16z)
- Day 15-21: Platform-native launch campaign (a16z prompt #6)
- Day 22-28: LinkedIn revenue bridge + authority build (Lara Acosta × a16z)
- Day 29-30: Crisis protocol setup + OODA loop establishment

#### [NEW] [02-narrative-warfare.md](file:///Users/farricecain/Google%20Antigravity/skills/new-media-kingmaker/workflows/02-narrative-warfare.md)
OODA-powered competitive narrative dominance:
- Benchmark competitors' OODA loop speeds
- Build pre-drafted position templates for top scenarios
- Design proactive disruption calendar
- Proof-stack each public position using Luke Iha proof ladder
- Flood-zone any counter-narrative within 36 hours

#### [NEW] [03-platform-launch.md](file:///Users/farricecain/Google%20Antigravity/skills/new-media-kingmaker/workflows/03-platform-launch.md)
Full extraction prompt #6 as a cross-domain workflow:
- Platform-native content slate using oral/written culture matrix
- Founder go-direct activation using a16z positioning
- Luke Iha vicious hooks per platform
- Grace Andrews trust pathway mapping per launch phase
- Ally amplification network + cascade sequence

---

### 2. New Compound Skill: `new-media-ghostwriting`

Nicolas Cole's ghostwriting methodology + a16z founder voice extraction + oral/written culture architecture = premium ghostwriting that goes beyond "write LinkedIn posts" to "build your entire media presence."

#### [NEW] [SKILL.md](file:///Users/farricecain/Google%20Antigravity/skills/new-media-ghostwriting/SKILL.md)
Cross-domain skill combining Nicolas Cole + a16z

#### [NEW] [01-voice-to-media-empire.md](file:///Users/farricecain/Google%20Antigravity/skills/new-media-ghostwriting/workflows/01-voice-to-media-empire.md)
End-to-end premium ghostwriting service:
- Voice capture via Nicolas Cole methodology
- Joe Rogan test diagnosis of the client
- Unscripting protocol to de-PR them
- Content culture map for platform allocation
- Written-first production pipeline
- Platform-native content production (different voice register per platform)

---

### 3. Seven New Slash Commands

#### [NEW] [kingmaker-sprint.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/kingmaker-sprint.md)
"Take any founder/brand from invisible to dominant in 30 days" — chains 5+ expert skills

#### [NEW] [narrative-warfare.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/narrative-warfare.md)
OODA-powered competitive narrative dominance with proof-stacking

#### [NEW] [platform-launch.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/platform-launch.md)
Platform-native launch-as-a-service campaign builder

#### [NEW] [new-media-ghostwriting.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/new-media-ghostwriting.md)
Premium ghostwriting with new media positioning layer

#### [NEW] [proof-across-platforms.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/proof-across-platforms.md)
Luke Iha proof ladder × oral/written culture modes = proof deployed per-platform natively

#### [NEW] [grace-new-media.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/grace-new-media.md)
Grace city blueprint enhanced: OODA loop speed layer + oral/written culture per content line

#### [NEW] [new-media-content-engine.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/new-media-content-engine.md)
Master copy engine that produces platform-aware content using oral/written cultural physics

---

### 4. Enhanced Existing Workflows (Non-Breaking Additions)

#### [MODIFY] [grace-to-copy.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/grace-to-copy.md)
Add Step 2.5: Load oral/written culture matrix from a16z skill → tag each trust stage's copy for cultural mode → ensure written-culture content anchors before oral extraction

#### [MODIFY] [grace-post-viral.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/grace-post-viral.md)
Add flood-zone integration to Stage 2 (Trust Damage Repair) → if attack vector detected, execute flood-zone crisis protocol instead of standard recovery

#### [MODIFY] [grace-vs-competitors.md](file:///Users/farricecain/Google%20Antigravity/.agent/workflows/grace-vs-competitors.md)
Add Step 3.5: OODA Loop benchmarking → for each competitor, estimate their decision-to-publish cycle → calculate dominance ratio → add to competitive intelligence output

---

## Verification Plan

This is a system-building task (skills/workflows), not application code. No unit tests apply.

### Automated Verification
```bash
# 1. Verify all files exist and have non-zero content
find skills/new-media-kingmaker skills/new-media-ghostwriting -name "*.md" -exec wc -l {} \;

# 2. Verify all 7 new slash commands exist
ls -la .agent/workflows/kingmaker-sprint.md .agent/workflows/narrative-warfare.md .agent/workflows/platform-launch.md .agent/workflows/new-media-ghostwriting.md .agent/workflows/proof-across-platforms.md .agent/workflows/grace-new-media.md .agent/workflows/new-media-content-engine.md

# 3. Sync registries to verify discoverability
python3 execution/sync_registries.py
```

### Manual Verification
- Confirm each cross-pollinated workflow references the correct source skills by path
- Confirm modified workflows have clear additions that don't break existing functionality
- Run `/recommend "I need to launch a product"` and verify it surfaces the new platform-launch workflow
