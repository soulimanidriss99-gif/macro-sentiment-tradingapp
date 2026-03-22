import streamlit as st
import streamlit.components.v1 as components
from transformers import pipeline
from impact_logic import get_market_impact, get_weekly_outlook

st.set_page_config(page_title="2026 Macro Sentinel", layout="wide", initial_sidebar_state="collapsed")

# --- UI STYLING ---
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: white; }
    div[data-testid="stMetricValue"] { font-size: 1.8rem; color: #00ffcc; }
    </style>
    """, unsafe_allow_html=True)

# --- AI MODEL LOADING ---
@st.cache_resource
def load_sentiment_model():
    return pipeline("sentiment-analysis", model="ProsusAI/finbert")

nlp = load_sentiment_model()

# --- HEADER ---
st.title("🏛️ Macro Sentiment & Weekly Outlook")
st.caption("Intelligence for March 2026 Markets | ES • NQ • GC • EUR/USD")

# --- TABS ---
tab1, tab2, tab3 = st.tabs(["📅 Weekly Strategy", "📰 News Analyzer", "📈 Live Charts"])

with tab1:
    data = get_weekly_outlook()
    st.subheader(f"Current Theme: {data['Theme']}")
    
    col1, col2 = st.columns(2)
    with col1:
        st.write("### Instrument Bias")
        for inst, bias in data['Bias'].items():
            st.info(f"**{inst}**: {bias}")
    
    with col2:
        st.write("### Economic Calendar")
        for event in data['Calendar']:
            st.write(f"📅 {event}")

with tab2:
    st.subheader("Analyze Headline Impact")
    col_a, col_b = st.columns([3, 1])
    with col_a:
        news_text = st.text_area("Paste News Item:", "The PCE data shows inflation is not cooling as fast as expected.")
    with col_b:
        category = st.selectbox("Category", ["Inflation", "Geopolitics", "Central Bank", "Employment"])
    
    if st.button("Calculate Market Shift"):
        result = nlp(news_text)[0]
        impacts = get_market_impact(result['label'], result['score'], category)
        
        st.divider()
        st.markdown(f"**Sentiment Analysis:** {result['label'].upper()} ({result['score']:.2%})")
        
        m_cols = st.columns(4)
        for i, (inst, val) in enumerate(impacts.items()):
            m_cols[i].metric(inst, val)

with tab3:
    st.subheader("Market Overview (TradingView)")
    # TradingView Ticker Tape Widget
    tradingview_html = """
    <div class="tradingview-widget-container">
      <script type="text/javascript" src="https://s3.tradingview.com/external-embedding/embed-widget-ticker-tape.js" async>
      {
      "symbols": [
        {"proName": "CME_MINI:ES1!", "title": "S&P 500 Futures"},
        {"proName": "CME_MINI:NQ1!", "title": "Nasdaq 100 Futures"},
        {"proName": "COMEX:GC1!", "title": "Gold Futures"},
        {"proName": "FX:EURUSD", "title": "EUR/USD"}
      ],
      "colorTheme": "dark",
      "isTransparent": true,
      "displayMode": "adaptive",
      "locale": "en"
    }
      </script>
    </div>
    """
    components.html(tradingview_html, height=100)
    st.info("The charts above provide real-time price action for your core instruments.")

st.sidebar.markdown("---")
st.sidebar.write("Developed for Team Leader Operations | 2026")
