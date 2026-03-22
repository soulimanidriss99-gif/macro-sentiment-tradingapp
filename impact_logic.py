def get_futures_impact(sentiment_label, score, category):
    # Mapping for March 2026 Futures Market
    impacts = {"ES (S&P)": "Neutral", "NQ (Nasdaq)": "Neutral", "GC (Gold)": "Neutral", "6E (Euro)": "Neutral"}
    
    if category == "Inflation":
        if sentiment_label == "Negative": # Hot Inflation / Sticky
            impacts.update({
                "ES (S&P)": "🔻 Bearish (Rate Pressure)", 
                "NQ (Nasdaq)": "🔻 Bearish (Yield Sensitivity)", 
                "GC (Gold)": "🚀 Bullish (Hedge)", 
                "6E (Euro)": "🚀 Bullish (USD Weakness)"
            })
        else:
            impacts.update({"ES (S&P)": "🚀 Bullish", "NQ (Nasdaq)": "🚀 Bullish", "GC": "🔻 Bearish"})
            
    elif category == "Geopolitics":
        if sentiment_label == "Negative": # Conflict Escalation
            impacts.update({
                "ES (S&P)": "🔻 Bearish (Risk-Off)", 
                "NQ (Nasdaq)": "🔻 Bearish (Energy Tax)", 
                "GC (Gold)": "🚀 Bullish (Safe Haven)", 
                "6E (Euro)": "🔻 Bearish (Energy Vulnerability)"
            })
    return impacts

def get_fundamental_strategy():
    # Strategy based on March 22, 2026 Global Macro conditions
    return [
        {
            "Rank": "🥇 Top Conviction",
            "Instrument": "Gold (GC)",
            "Direction": "Long (Bullish)",
            "Rationale": "Geopolitical safe-haven bid + decoupling from yields. Central bank buying remains high in 2026.",
            "Timing": "Accumulate on pullbacks; high volatility expected Friday morning.",
            "Target": "5,200"
        },
        {
            "Rank": "🥈 Macro Play",
            "Instrument": "Euro (6E)",
            "Direction": "Short (Bearish)",
            "Rationale": "Eurozone growth-inflation gap widening vs US. Energy import costs spiking.",
            "Timing": "Sell rallies toward 1.1520; Target 1.1300.",
            "Target": "1.1300"
        },
        {
            "Rank": "🥉 Tactical Play",
            "Instrument": "Nasdaq (NQ)",
            "Direction": "Short (Bearish)",
            "Rationale": "10Y Treasury yields hitting 4.5% are a headwind for high-multiple tech.",
            "Timing": "Best entry after Thursday's GDP revision if data is hot.",
            "Target": "18,200"
        }
    ]

def get_weekly_outlook():
    return {
        "Theme": "PCE Inflation & Global Supply Chain Volatility",
        "Analysis": {
            "ES (E-mini S&P)": "⚠️ Neutral/Bearish. Range bound between 5850 and 6020.",
            "NQ (E-mini Nasdaq)": "🔻 Bearish. Growth stocks underperforming as yields rise.",
            "GC (Gold)": "🚀 Bullish. The 'Fear Trade' is currently the strongest narrative.",
            "6E (EUR/USD)": "🔻 Bearish. US Dollar dominance remains the default 2026 trend."
        },
        "Calendar": [
            "Tuesday: US Flash PMIs (Initial Q1 Signal)",
            "Thursday: GDP Final Revision (Q4 2025)",
            "Friday: Core PCE Price Index (High Volatility)"
        ]
    }
