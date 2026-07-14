# Test Listings for RE-1 Audit

Sample MLS listings for auditing workflow validation. These are *fictional* but representative of real violations found in SFV and LA County MLS data.

---

## Test Listing 1: High Violation Count (Training Example)

**Original MLS Remarks:**

```
Beautiful 4-bedroom home in prestigious gated community. Perfect for growing families. 
Walking distance to award-winning schools including Lincoln Elementary and Central Middle. 
Safe, quiet neighborhood ideal for retirees. Excellent area for active professionals and 
young couples. Near ethnic restaurants, diverse cultural centers, and shopping. Large 
backyard perfect for children. No smokers. Charming tree-lined street. Move-in ready!
```

**Expected audit result:**
- RED violations: 5 (familial status × 3, age × 2)
- YELLOW cautions: 2 (schools context, ethnic restaurants)
- BLUE improvements: 2 (charming, safe)
- Status: VIOLATIONS_FOUND

---

## Test Listing 2: Moderate Violations (Common Case)

**Original MLS Remarks:**

```
Charming 3-bedroom cottage on quiet cul-de-sac. Perfect for families starting out. 
Close to top schools. Great for retirees who want an active lifestyle. Community 
pool and recreation center. Peaceful setting ideal for those seeking privacy.
```

**Expected audit result:**
- RED violations: 2 (families, retirees)
- YELLOW cautions: 2 (quiet, active lifestyle)
- BLUE improvements: 1 (top schools → specific schools)
- Status: VIOLATIONS_FOUND

---

## Test Listing 3: Compliant Listing (Baseline)

**Original MLS Remarks:**

```
Spacious 4-bedroom home in established residential neighborhood. Walking distance 
to Lincoln Elementary (9.2/10) and Central Middle School (8.8/10). Tree-lined 
cul-de-sac with parks nearby. Low-maintenance landscaping. Recently renovated kitchen 
and bathrooms. Convenient to downtown employment centers. Multiple deck levels for 
entertaining. Move-in ready.
```

**Expected audit result:**
- RED violations: 0
- YELLOW cautions: 0
- BLUE improvements: 0
- Status: PASS

---

## Test Listing 4: Dog-Whistle Codes (Subtle Violations)

**Original MLS Remarks:**

```
Charming home in safe, established neighborhood with strong community feel. 
Quiet street perfect for peaceful living. Close to fine schools. Great investment 
in up-and-coming area. Diverse dining and cultural options. Perfect for those who 
appreciate a slower pace of life.
```

**Expected audit result:**
- RED violations: 1 ("perfect for those who appreciate slower pace" — age-coded)
- YELLOW cautions: 3 ("safe," "quiet," "up-and-coming")
- BLUE improvements: 1 ("fine schools" → specific schools)
- Status: VIOLATIONS_FOUND

---

## Test Listing 5: Disability-Coded Language

**Original MLS Remarks:**

```
Wonderful home perfect for active individuals. Features a beautiful two-story design 
with hardwood stairs. Ideal for the outdoor lifestyle with deck and garden. Active 
community with regular neighborhood events and hiking groups. Not suitable for those 
seeking low-maintenance.
```

**Expected audit result:**
- RED violations: 2 ("active individuals," "not suitable for")
- YELLOW cautions: 1 ("active community")
- BLUE improvements: 1 (stairs → descriptive fact)
- Status: HIGH_RISK

---

## Test Listing 6: Nationality/Language Coding

**Original MLS Remarks:**

```
Vibrant, international community with bilingual residents. Walking distance to 
Spanish-language schools and ethnic market. Perfect for Hispanic families. 
Authentic cultural atmosphere with traditional restaurants nearby.
```

**Expected audit result:**
- RED violations: 2 (explicit nationality/language targeting, "perfect for Hispanic families")
- YELLOW cautions: 2 ("bilingual residents," "ethnic market" as neighborhood marker)
- Status: HIGH_RISK

---

## Audit These (Jen's Real Listings)

*To be populated once Jen shares current MLS listings.*

- [ ] Address: ________________
- [ ] Address: ________________
- [ ] Address: ________________

