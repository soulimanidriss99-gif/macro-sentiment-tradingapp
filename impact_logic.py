def get_futures_impact(sentiment_label, score, category):
    # March 2026 Impact Matrix for Futures
    impacts = {
        "ES (E-mini S&P)": "Neutral", 
        "NQ (E-mini Nasdaq)": "Neutral", 
        "GC (Gold)": "Neutral", 
        "EUR/USD (6E)": "Neutral"
    }
    
    if category == "Inflation":
        if sentiment_label == "Negative": # i.e., Inflation is HIGHER than expected
            impacts.update({
                "ES (E-mini S&P)": "🔻 Bearish (Rate hike fears)", 
                "NQ (E-mini Nasdaq)": "🔻 Bearish (Yield sensitivity)", 
                "GC (Gold)": "🚀 Bullish (Inflation hedge)", 
                "EUR/USD (6E)": "🚀 Bullish (USD weakness)"
            })
        else: # Inflation cooling
            impacts.update({"ES (E-mini S&P)": "🚀 Bullish", "NQ (E-mini Nasdaq)": "🚀 Bullish", "GC": "🔻 Bearish"})
            
    elif category == "Geopolitics":
        if sentiment_label == "Negative": # Conflict Escalation
            impacts.update({
                "ES (E-mini S&P)": "🔻 Bearish (Energy Costs)", 
                "NQ (E-mini Nasdaq)": "🔻 Bearish (Risk-Off)", 
                "GC (Gold)": "🚀 Bullish (Safe Haven)", 
                "EUR/USD (6E)": "🔻 Bearish (Flight to USD)"
            })
    return impacts

def get_weekly_outlook():
    # Tailored for the week of March 22, 2026
    return {
        "Theme": "PCE Inflation Data & Global Supply Chain Volatility",
        "Analysis": {
            "ES (E-mini S&P)": "⚠️ Neutral/Bearish. Major resistance at 6000. Watching 5850 support.",
            "NQ (E-mini Nasdaq)": "🔻 Bearish Bias. Tech under pressure as 10Y Yields remain above 4.5%.",
            "GC (Gold)": "🚀 Bullish. Strong safe-haven bid due to Middle East tensions.",
            "EUR/USD (6E)": "🔻 Bearish. Target 1.1350 as energy costs pressure the Eurozone."
        },
        "Calendar": [
            "Tuesday: US Flash PMIs (Manufacturing/Services)",
            "Thursday: GDP Final Revision (Q4 2025)",
            "Friday: Core PCE Price Index (High Volatility Expected)"
        ]
    }
