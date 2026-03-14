---
description: "Mine podcast appearances for powerful untold stories the client doesn't realize they have"
---

# /hidden-gems — Hidden Gems Story Miner

Systematically mine a thought leader's podcast appearances, interviews, and casual content for stories they tell naturally but would never suggest for content.

## Usage

```
/hidden-gems [client name or paste transcripts]
```

## Steps

### 1. Load the Skill
// turbo
Read `skills/sean-mabry-voice-mastery/genius.md` — load the Hidden Gem Collector pattern.

### 2. Load the Prompt
// turbo
Read `skills/sean-mabry-voice-mastery/references/prompts/hidden-gems-story-miner.md` — the full story mining workflow.

### 3. Gather Input
Ask the user:
- **Client name**: Who is the client?
- **Source material**: Provide podcast transcripts, interview content, or URLs (minimum 3 appearances)
- **Known stories**: What stories does the client already use consciously?
- **Content purpose**: What will the stories be used for? (book, LinkedIn series, email, keynotes)

### 4. Execute
Follow the prompt:
1. Story detection pass — flag every narrative moment
2. Hidden gem filter — score on Character Reveal, Concrete Detail, Host Reaction
3. Classify by deployment context (origin, failure, wisdom, humor, relationship, turning point)
4. Write enhancement notes + follow-up questions per gem
5. Assemble dual-bank: Their Picks vs. My Picks

### 5. Deliver
Present the Hidden Gems Story Bank. Target: My Picks outnumber Their Picks 2:1.
Recommend: "Feed these into `/story-remix` for multi-format deployment."

## Chain Compatibility
- **Follows**: `/voice-calibrate`
- **Leads to**: `/story-remix`, `/memoir-architect`, `/book-atomize`
