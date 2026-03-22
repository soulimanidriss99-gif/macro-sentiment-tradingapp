import streamlit as st
from transformers import pipeline
from impact_logic import get_market_impact

# App Config
st.set_page_config(page_title="Macro Sentiment AI", layout="wide")
st.title("🏛️ Macro Sentiment & Cross-Asset Analyzer")

# Load AI Model (FinBERT)
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis", model="ProsusAI/finbert")

sentiment_pipe = load_model()

# Sidebar Inputs
st.sidebar.header("Analysis Settings")
macro_cat = st.sidebar.selectbox("Macro Category", ["Inflation", "Employment", "Geopolitics", "Central Bank"])
news_input = st.text_area("Paste Market News/Headline here:", "The Federal Reserve suggests inflation remains sticky, delaying expected rate cuts.")

if st.button("Analyze Impact"):
    # 1. Run Sentiment
    result = sentiment_pipe(news_input)[0]
    label = result['label']
    score = result['score']
    
    # 2. Get Impacts
    impact_results = get_market_impact(label, score, macro_cat)
    
    # 3. Display Results
    st.subheader(f"Sentiment: {label} ({score:.2%})")
    
    cols = st.columns(4)
    instruments = [("ES (S&P)", "ES"), ("NQ (Nasdaq)", "NQ"), ("GC (Gold)", "GC"), ("EUR/USD", "EUR/USD")]
    
    for col, (name, sym) in zip(cols, instruments):
        with col:
            st.metric(label=name, value=impact_results[sym])

st.info("Note: This is an AI-driven simulation for March 2026 macro conditions.")
