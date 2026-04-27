# /spiegel-workaround — Screenshot Mindset

> When everyone says "impossible," find the side-channel. The constraint isn't real — the workaround is waiting.

## When to Use
- Facing a constraint everyone accepts as fixed
- Platform, API, or technical limitation blocking progress
- Competitive restriction that seems insurmountable
- Any "you can't do that" moment

## Inputs Required
1. The constraint (what you're told you can't do)
2. Why it matters (what achieving this would unlock)
3. Current approaches tried and why they failed
4. The system environment (what platforms, tools, APIs are involved)

## Execution Steps

### Step 1: Constraint Documentation
State the constraint precisely:
- "I cannot [specific action] because [specific limitation]"
- Who says it's impossible? (platform docs, engineers, conventional wisdom)
- What's the assumed finality? (API limitation, policy, physics)

### Step 2: Adjacent System Behavior Mapping
The Spiegel Question: "What changes in the system when [the impossible thing] happens?"
- Map every observable side effect of the blocked action
- What signals does the system emit even if it doesn't provide direct access?
- What proxy behaviors correlate with the target action?

Example (Screenshot Detection):
- Direct API: None (Apple doesn't provide screenshot detection)
- Side effect: Taking a screenshot triggers a touch event (finger lifts)
- Proxy signal: Monitoring touch events reveals screenshot timing
- Workaround: Use touch event monitoring as screenshot proxy

### Step 3: Side-Channel Inventory
Brainstorm 10+ potential side-channels:
| Side-Channel | Signal Type | Reliability | Implementation Difficulty |
|---|---|---|---|
| | | | |

### Step 4: Workaround Design
For the most promising side-channel:
1. How reliable is the signal? (false positive/negative rate)
2. How difficult to implement? (engineering effort)
3. How durable is it? (will a platform update break it?)
4. What's the user experience? (transparent or awkward?)

### Step 5: Implementation Roadmap
1. Prototype the workaround (48-hour spike)
2. Test reliability across edge cases
3. Design fallback for when the workaround fails
4. Monitor for platform changes that could break it

## Output Format
```
## SCREENSHOT MINDSET — [Constraint]
### Constraint: "I cannot ___ because ___"
### Adjacent System Map: [all side effects]
### Side-Channel Inventory: [10+ options]
### Selected Workaround: [design + reliability]
### Implementation: [48-hour prototype plan]
### Durability Assessment: [how long this lasts]
```

## Quality Gate
- Must state constraint precisely (not vaguely)
- Adjacent system map must identify at least 3 observable side effects
- Side-channel inventory must have 10+ options (volume kills preciousness)
- Implementation must include durability/fragility assessment

## Stacking
- **× Nick Saraev** → Technical automation infrastructure for workaround implementation
- **× Nathan Gotch** → Platform workarounds for SEO/distribution constraints
