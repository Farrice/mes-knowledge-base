def audit_keyword(keyword):
    """
    Analyzes a keyword for 'Buyer Intent' (The Wallet-Out Protocol).
    """
    print(f"🎯 Auditing Keyword: '{keyword}'...")
    
    # 1. Linguistic Analysis (The "Wallet-Out" Filter)
    kw_lower = keyword.lower()
    
    transactional_triggers = ['buy', 'price', 'cost', 'cheap', 'discount', 'deal', 'coupon', 'sale']
    commercial_triggers = ['best', 'top', 'review', 'vs', 'compare', 'alternative']
    informational_triggers = ['how', 'what', 'history', 'guide', 'tutorial', 'tip']
    
    intent = "Unknown"
    score = 0
    explanation = ""
    
    if any(x in kw_lower for x in transactional_triggers):
        intent = "TRANSACTIONAL (💰💰💰)"
        score = 95
        explanation = "Contains explicit buying signals."
    elif any(x in kw_lower for x in commercial_triggers):
        intent = "COMMERCIAL INVESTIGATION (💰💰)"
        score = 75
        explanation = "User is comparing options, high likelihood of conversion."
    elif any(x in kw_lower for x in informational_triggers):
        intent = "INFORMATIONAL (🧠)"
        score = 20
        explanation = "User is learning, low likelihood of immediate purchase."
    else:
        intent = "NAVIGATIONAL / BROAD"
        score = 10
        explanation = "Ambiguous intent."

    # 2. SERP Simulation (Mocked)
    # real system would check for Ads vs Wikipedia
    has_ads = True if score > 50 else False
    difficulty = "Hard" if score > 80 else "Medium"
    
    print(f"\n📊 INTENT ANALYSIS REPORT")
    print("-" * 50)
    print(f"KEYWORD: {keyword}")
    print(f"INTENT CLASS: {intent}")
    print(f"VALUE SCORE: {score}/100")
    print(f"DIFFICULTY (Est): {difficulty}")
    print(f"REASONING: {explanation}")
    
    if has_ads:
        print("SERP SIGNALS: 🚨 High Ads presence detected (Validates Commercial Intent)")
    else:
        print("SERP SIGNALS: ℹ️ Mostly organic/informational results")
        
    print("-" * 50)

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='Market Intelligence - Intent Analyzer')
    parser.add_argument('--keyword', type=str, required=True, help='Keyword to analyze')
    args = parser.parse_args()
    
    audit_keyword(args.keyword)
