def get_market_impact(sentiment_label, score, category):
    # Mapping logic for 2026 Macro Environment
    impacts = {
        "ES": "Neutral", "NQ": "Neutral", 
        "GC": "Neutral", "EUR/USD": "Neutral"
    }
    
    if category == "Inflation":
        if sentiment_label == "Negative": # i.e., Inflation is HIGH
            impacts["ES"] = "🔻 Bearish (Rate hike fears)"
            impacts["NQ"] = "🔻 Bearish (Valuation compression)"
            impacts["GC"] = "🚀 Bullish (Inflation hedge)"
            impacts["EUR/USD"] = "🚀 Bullish (Relative USD weakness)"
        else:
            impacts["ES"] = "🚀 Bullish (Soft landing)"
            impacts["NQ"] = "🚀 Bullish (Tech rally)"
            
    elif category == "Geopolitics":
        if sentiment_label == "Negative":
            impacts["GC"] = "🚀 Bullish (Safe Haven)"
            impacts["ES"] = "🔻 Bearish (Uncertainty)"
            impacts["EUR/USD"] = "🔻 Bearish (Flight to USD)"
            
    return impacts
