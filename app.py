import streamlit as st
import streamlit.components.v1 as components
from transformers import pipeline
from impact_logic import get_futures_impact, get_weekly_outlook

# --- APP CONFIG ---
st.set_page_config(page_title="2026 Futures Sentinel", layout="wide")

# --- CUSTOM DARK THEME CSS ---
st.markdown("""
    <style>
    .stMetric { background-color: #1e1e26; padding: 15px; border-radius: 10px; border: 1px solid #333; }
    [data-testid="stMetricValue"] { color: #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

# --- LOAD AI MODEL ---
@st.cache_resource
def load_nlp():
    # Using FinBERT for financial-specific sentiment
    return pipeline("sentiment-analysis", model="ProsusAI/finbert")

nlp_model = load_nlp()

# --- HEADER ---
st.title("🛰️ 2026 Futures Macro Sentinel")
st.caption("Strategic Intelligence for Professional Futures Trading")

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["📅 Weekly Strategy", "📰 News Analysis", "🔧 Contract Specs"])

with tab1:
    outlook = get_weekly_outlook()
    st.info(f"**Primary Market Driver:** {outlook['Theme']}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("### 📉 Futures Instrument Bias")
        for inst, bias in outlook['Analysis'].items():
            st.markdown(f"**{inst}**: {bias}")
    
    with col2:
        st.write("### 📅 High-Impact Calendar")
        for event in outlook['Calendar']:
            st.write(f"• {event}")

with tab2:
    st.write("### Instant News Impact Analyzer")
    news_col, cat_col = st.columns([3, 1])
    with news_col:
        news_input = st.text_area("Paste Headline/Data Point:", "PCE Inflation comes in at 2.9%, higher than the expected 2.6%.")
    with cat_col:
        cat = st.selectbox("Category", ["Inflation", "Geopolitics", "Employment", "Central Bank"])
        
    if st.button("Analyze Futures Impact"):
        res = nlp_model(news_input)[0]
        impacts = get_futures_impact(res['label'], res['score'], cat)
        
        st.success(f"AI Sentiment: {res['label']} ({res['score']:.2%})")
        m_cols = st.columns(4)
        for i, (name, val) in enumerate(impacts.items()):
            m_cols[i].metric(name, val)

with tab3:
    st.write("### 📝 Futures Contract Reference (CME/COMEX)")
    specs = {
        "Instrument": ["ES (E-mini S&P)", "NQ (E-mini Nasdaq)", "GC (Gold)", "6E (Euro)"],
        "Tick Size": ["0.25", "0.25", "0.10", "0.0001"],
        "Tick Value": ["$12.50", "$5.00", "$10.00", "$12.50"],
        "Point Value": ["$50", "$20", "$100", "$125,000 (Full)"]
    }
    st.table(specs)
    st.caption("Note: Values based on March 2026 CME Specifications.")

st.sidebar.markdown("---")
st.sidebar.write("Team Leader Operations Edition")
st.sidebar.caption("Last Deployment: March 22, 2026")
