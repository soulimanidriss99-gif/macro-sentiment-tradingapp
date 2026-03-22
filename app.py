import streamlit as st
import pandas as pd
from transformers import pipeline
from impact_logic import get_futures_impact, get_weekly_outlook, get_fundamental_strategy

# --- PAGE CONFIG ---
st.set_page_config(page_title="2026 Trading Sentinel", layout="wide", initial_sidebar_state="collapsed")

# --- CUSTOM CSS ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    .stMetric { background-color: #1e1e26; border: 1px solid #444; padding: 15px; border-radius: 10px; }
    div[data-testid="stExpander"] { background-color: #1e1e26; border: none; }
    </style>
    """, unsafe_allow_html=True)

# --- CACHE AI MODEL ---
@st.cache_resource
def load_nlp():
    # Loading FinBERT for financial-specific sentiment analysis
    return pipeline("sentiment-analysis", model="ProsusAI/finbert")

nlp_model = load_nlp()

# --- HEADER ---
st.title("🛰️ 2026 Futures Trading Sentinel")
st.caption("Fundamental, Sentiment & Macro Analysis | Week of March 22, 2026")

# --- FUNDAMENTAL STRATEGY SECTION ---
st.markdown("### 💡 Fundamental Strategy & Top Picks")
strategy_list = get_fundamental_strategy()
cols = st.columns(len(strategy_list)) # Dynamically create columns for strategies

for i, trade in enumerate(strategy_list):
    with cols[i]:
        st.info(f"**{trade['Rank']}**")
        st.markdown(f"**{trade['Instrument']} | {trade['Direction']}**")
        st.write(f"**Rationale:** {trade['Rationale']}")
        st.write(f"**Target:** {trade['Target']}")
        st.caption(f"🕒 **Timing:** {trade['Timing']}")

st.divider()

# --- MAIN TABS ---
tab1, tab2, tab3 = st.tabs(["📊 Market Outlook", "📰 News Analyzer", "🔧 Contract Specs"])

with tab1:
    outlook = get_weekly_outlook()
    st.info(f"**Primary Weekly Driver:** {outlook['Theme']}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Instrument Bias")
        for inst, bias in outlook['Analysis'].items():
            st.markdown(f"**{inst}**: {bias}")
    
    with col2:
        st.write("### High-Impact Calendar")
        for event in outlook['Calendar']:
            st.write(f"📅 {event}")

with tab2:
    st.subheader("Instant Sentiment Analyzer")
    news_col, cat_col = st.columns([3, 1])
    with news_col:
        news_input = st.text_area("Paste News Headline:", "Fed officials suggest interest rates may need to move higher if PCE remains sticky.")
    with cat_col:
        cat = st.selectbox("Category", ["Inflation", "Geopolitics", "Central Bank", "Employment"])
        
    if st.button("Calculate Market Shift"):
        res = nlp_model(news_input)[0]
        # Get the dictionary of impacts
        impacts = get_futures_impact(res['label'], res['score'], cat)
        
        st.success(f"AI Sentiment: {res['label']} ({res['score']:.2%})")
        
        # FIX: Dynamically create exactly the number of columns needed for the results
        instrument_names = list(impacts.keys())
        m_cols = st.columns(len(instrument_names))
        
        for i, name in enumerate(instrument_names):
            m_cols[i].metric(label=name, value=impacts[name])

with tab3:
    st.write("### 📝 Futures Contract Reference (CME)")
    specs = {
        "Instrument": ["ES (S&P 500)", "NQ (Nasdaq 100)", "GC (Gold)", "6E (Euro)"],
        "Tick Size": ["0.25", "0.25", "0.10", "0.0001"],
        "Tick Value": ["$12.50", "$5.00", "$10.00", "$12.50"],
        "Point Value": ["$50", "$20", "$100", "$125,000 (Full)"]
    }
    st.table(pd.DataFrame(specs))

st.sidebar.markdown("---")
st.sidebar.write("**Developed for Ops Team Leader**")
st.sidebar.caption("Current Date: March 22, 2026")
