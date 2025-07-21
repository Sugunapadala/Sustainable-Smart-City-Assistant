import streamlit as st
from frontend.components.summary_card import summary_card_ui
from frontend.components.eco_tips import eco_tips_ui
from frontend.components.forecasting_dashboard import forecasting_dashboard_ui
from frontend.components.anomaly_detector import anomaly_detector_ui
from frontend.components.report_generator import report_generator_ui
from frontend.components.chat_assistant_ui import chat_assistant_ui  # 🧠 AI Chatbot

# Page config
st.set_page_config(
    page_title="Sustainable Smart City Assistant 🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

# App Title
st.title("🏙️ Sustainable Smart City Assistant")

# Sidebar
st.sidebar.header("🔧 Features")
page = st.sidebar.radio(
    "Select a Feature",
    (
        "🌟 City Summary Dashboard",
        "📈 Forecast City Metrics",
        "📉 Detect Anomalies",
        "📥 Generate City Report",
        "💬 Smart AI Chat Assistant",
        "🌿 Eco-Friendly Tips"
    )
)

# Sample summary data for the summary card UI
summary_data = {
    "Pollution": "42 AQI",
    "Temperature": "30°C",
    "Water Quality": "Good",
    "Traffic": "Moderate"
}

# Page Navigation Logic
if page == "🌟 City Summary Dashboard":
    summary_card_ui(summary_data)

elif page == "📈 Forecast City Metrics":
    forecasting_dashboard_ui()

elif page == "📉 Detect Anomalies":
    anomaly_detector_ui()

elif page == "📥 Generate City Report":
    report_generator_ui()

elif page == "💬 Smart AI Chat Assistant":
    chat_assistant_ui()

elif page == "🌿 Eco-Friendly Tips":
    eco_tips_ui()

# Footer (Optional)
st.markdown("---")
st.markdown("Built with ❤️ by Suguna Padala | Powered by Streamlit, IBM Watsonx & Pinecone")
