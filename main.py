import streamlit as st
from analysis_dashboard import show_dashboard
from prediction_module import show_predictions

st.set_page_config(page_title="AI Expense Analyzer", layout="wide")

st.title("💸 AI-Driven Expense Analyzer")

menu = st.sidebar.radio(
    "Select Feature",
    ("📊 Expense Dashboard", "🤖 AI Expense Prediction")
)

if menu == "📊 Expense Dashboard":
    show_dashboard()
elif menu == "🤖 AI Expense Prediction":
    show_predictions()

st.markdown("---")
st.markdown("Built with ❤️ by Hasitha | Powered by AI & Streamlit")
