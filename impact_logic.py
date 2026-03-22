def get_market_impact(sentiment_label, score, category):
    impacts = {"ES": "Neutral", "NQ": "Neutral", "GC": "Neutral", "EUR/USD": "Neutral"}
    
    if category == "Inflation":
        if sentiment_label == "Negative": # Meaning Inflation is HIGH/Sticky
            impacts.update({"ES": "🔻 Bearish", "NQ": "🔻 Bearish", "GC": "🚀 Bullish", "EUR/USD": "🚀 Bullish"})
        else:
            impacts.update({"ES": "🚀 Bullish", "NQ": "🚀 Bullish", "GC": "🔻 Bearish", "EUR/USD": "🔻 Bearish"})
            
    elif category == "Geopolitics":
        if sentiment_label == "Negative": # Conflict Escalation
            impacts.update({"ES": "🔻 Bearish", "NQ": "🔻 Bearish", "GC": "🚀 Bullish", "EUR/USD": "🔻 Bearish"})
        else:
            impacts.update({"ES": "🚀 Bullish", "NQ": "🚀 Bullish", "GC": "Neutral", "EUR/USD": "Neutral"})
            
    return impacts

def get_weekly_outlook():
    return {
        "Theme": "PCE Inflation & Geopolitical Tension",
        "Bias": {
            "ES (S&P 500)": "⚠️ Neutral/Bearish - Watching 5850 support.",
            "NQ (Nasdaq)": "🔻 Bearish - High yields (10Y @ 4.5%) weighing on tech.",
            "GC (Gold)": "🚀 Bullish - Safe haven demand holding prices near $4,700.",
            "EUR/USD": "🔻 Bearish - Energy costs hitting EU growth harder than US."
        },
        "Calendar": [
            "Tuesday: Flash PMIs (US & Europe)",
            "Thursday: GDP Final Revision",
            "Friday: Core PCE Price Index (High Impact)"
        ]
    }
