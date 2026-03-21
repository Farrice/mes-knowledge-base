---
description: "Premium ghostwriting with new media positioning — build media empires, not just write posts. Nicolas Cole + a16z founder voice + oral/written culture"
---

# /new-media-ghostwriting — Build Media Empires, Not Just Posts

Premium ghostwriting engagement that goes beyond "write LinkedIn posts" to "build your entire media presence with authentic voice, strategic positioning, and platform-native content."

## Usage

```
/new-media-ghostwriting "[client/founder name]"
/new-media-ghostwriting "Sarah Kim" --industry "climate tech" --platforms "LinkedIn, Substack, X"
```

## Steps

### 1. Load Context
Read these files:
1. `skills/new-media-ghostwriting/SKILL.md`
2. `skills/new-media-ghostwriting/workflows/01-voice-to-media-empire.md`

### 2. Collect Inputs
- Client/founder name, company, industry
- Existing content samples (posts, interviews, presentations)
- Business goals (hiring, sales, fundraising, authority)
- Weekly engagement time
- Current and desired platforms
- Competitors to outposition

### 3. Execute Engagement Build
Follow all phases in `01-voice-to-media-empire.md`:

**Phase 1 — Voice Intelligence (Week 1)**:
1. Nicolas Cole voice capture (interview protocol + content analysis)
2. Joe Rogan test diagnosis (score 1-10)
3. Unscripting protocol (kill list + liberation list + controversy map)

**Phase 2 — Content Architecture (Week 2)**:
4. Oral/written culture platform map (with voice adaptation per platform)
5. Content city blueprint with Grace Andrews methodology
6. LinkedIn power base architecture with Lara Acosta methodology

**Phase 3 — Production Pipeline (Ongoing)**:
7. Long-form anchor production (monthly Substack/YouTube scripts)
8. Platform-native extraction (different content per platform, not reformatted)
9. Real-time OODA content (rapid-response in client's voice)

**Phase 4 — Protection (Month 1)**:
10. Context-length defense (canonical references for controversial positions)
11. Flood-zone preparation (crisis arsenal pre-built)

### 4. Source Skill Loading (per phase)
- Phase 1 → `skills/nicolas-cole-ghostwriting/SKILL.md` + `skills/andreessen-horowitz-new-media/workflows/04-founder-go-direct.md`
- Phase 2 → `skills/grace-andrews-media-company/SKILL.md` + `genius.md` + `skills/lara-acosta/SKILL.md`
- Phase 3 → `skills/luke-iha-proof-copy/SKILL.md` (proof loading)
- Phase 4 → `skills/andreessen-horowitz-new-media/references/prompts/05-flood-the-zone-crisis-protocol.md`

### 5. Quality Gate
- Voice fidelity: Would a colleague believe the client wrote this? (8+/10)
- Culture-mode match: Oral content FEELS oral, written FEELS written?
- No cross-posting: Every piece is natively designed?
- Controversy calibration: Bold positions have long-form context?
- Trust pathway coherence: Every piece serves a specific trust stage?

### 6. Output
Save service blueprint to `deliverables/ghostwriting-engagement-[client-slug]-[date].md`

### 7. Finalize
```bash
python3 execution/chain_runner.py finalize "New Media Ghostwriting for [client]" \
    --expert "nicolas-cole" \
    --skill "new-media-ghostwriting" \
    --workflow "voice-to-media-empire" \
    --type "Client Work" \
    --intent 9 --expert-score 9 --adversarial 8 \
    --notes "Premium ghostwriting with a16z media empire layer"
```
