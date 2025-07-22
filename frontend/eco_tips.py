import streamlit as st

eco_tips_data = {
    "plastic": [
        "Use reusable cloth bags instead of plastic ones.",
        "Avoid single-use plastic bottles; use steel or glass alternatives.",
        "Encourage local plastic collection drives."
    ],
    "energy": [
        "Switch to LED bulbs and energy-efficient appliances.",
        "Unplug electronics when not in use.",
        "Consider rooftop solar panels for homes."
    ],
    "water": [
        "Fix leaking taps immediately.",
        "Harvest rainwater during monsoons.",
        "Use low-flow showerheads to conserve water."
    ],
    "transport": [
        "Use bicycles or walk for short distances.",
        "Carpool to reduce emissions.",
        "Prefer electric or hybrid vehicles."
    ],
    "waste": [
        "Segregate dry and wet waste at source.",
        "Compost organic kitchen waste.",
        "Avoid buying over-packaged goods."
    ]
}

def eco_tips_ui():
    st.subheader("🌿 Eco Advice Generator")
    st.markdown("Get sustainable living tips based on a topic like plastic, water, solar, recycling, etc.")

    keyword = st.text_input("Enter a keyword (e.g., plastic, energy, water):").strip().lower()

    if st.button("🌱 Generate Tips"):
        if keyword in eco_tips_data:
            st.markdown(f"### ✅ Tips for {keyword.title()}")
            for tip in eco_tips_data[keyword]:
                st.markdown(f"- {tip}")
        else:
            st.warning("Sorry, no tips available for this topic. Try: plastic, energy, water, waste, or transport.")
