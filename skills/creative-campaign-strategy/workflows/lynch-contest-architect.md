# /lynch-contest-architect — Contest & Data Capture Architecture

> Design the daily giveaway mechanism that simultaneously captures data, educates on product range, and converts through "I'll never win but I really want this" psychology.

## When to Use
- Building a lead generation engine with physical product giveaways
- When you need to combine data capture with product education
- When acquisition costs are too high for direct advertising alone
- Complementing a customer-as-media strategy with contest-driven UGC

## Inputs Required
1. Product catalog (full range with cost of goods for each)
2. Target data to capture (email, demographics, preferences, purchase intent)
3. Website or platform where the contest will live
4. Current lead generation costs
5. Product education goals (what do you want prospects to know?)

## Execution Steps

### Step 1: Prize Economics (GP-3)
Calculate the true cost of a daily giveaway:
- Select the most DESIRABLE product (not the cheapest, not the most expensive)
- Cost of goods per unit = daily cost
- Annual cost = 365 × daily cost of goods
- Compare to: annual cost of equivalent lead volume via paid ads

### Step 2: Data Capture Architecture
Design the progressive data collection:
- **Entry gate**: Email + name (minimum barrier)
- **Bonus entries**: Additional data points for extra chances
  - Share on social media (+1 entry)
  - Answer product preference survey (+2 entries)
  - Refer a friend (+3 entries)
- **Post-entry flow**: Product range education sequence

### Step 3: Product Education Layer
Design the post-entry exposure:
- After entering, the contestant sees the FULL product catalog
- Each product shown with transformation-first framing (not specs)
- "While you wait for results, check out these..." 
- Track which products each contestant views → personalized follow-up

### Step 4: Conversion Psychology
Engineer the "I'll never win but I really want this" mechanism:
- Winner announcements VISIBLE to all entrants (FOMO + legitimacy)
- Product pages 1 click away from contest page
- Limited-time offer for non-winners ("You didn't win today — here's 10% off")
- Daily re-entry requirement = daily brand touchpoint

### Step 5: UGC Integration
Connect the contest to customer-as-media:
- Contest entries can include submitted content (photos, videos, stories)
- Best submissions featured on brand channels (recognition incentive)
- Winning criteria includes "best content" alongside random drawing
- Each submission = free branded content for the brand

## Output Format
```
## CONTEST ARCHITECTURE — [Product/Brand]

### Prize Economics
- Daily prize: [Product name]
- Cost of goods per unit: $[X]
- Annual contest cost: $[Y]
- Equivalent paid acquisition cost: $[Z]
- Savings: $[Z - Y]

### Data Capture Flow
[Entry gate → bonus entries → post-entry education]

### Product Education Sequence
[What the contestant sees after entry + tracking mechanism]

### Conversion Psychology
[Winner announcements + product proximity + non-winner offers]

### UGC Integration
[How contest entries become brand content]

### Technical Requirements
[Platform, email integration, tracking, random selection mechanism]

### 30-Day Launch Plan
[Week-by-week implementation timeline]
```

## Quality Gate
- Prize must be a DESIRABLE product (not a token giveaway)
- Annual contest cost must be calculated and compared to equivalent ad spend
- Data capture must be progressive (not a massive form)
- Product education must happen AFTER entry (not as a gate)
- UGC integration must be included (contest + media, not contest alone)
- Score ≥7 on Contest Architecture in the Ron Lynch Quality Rubric
