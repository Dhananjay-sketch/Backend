import streamlit as st
from app import add_custom_style

add_custom_style()

st.title("🩺 Health Conditions")
st.caption("Get condition-based food suggestions and diet tips for a healthy lifestyle.")

st.markdown("<hr style='border:1px solid #2bc0a8;'>", unsafe_allow_html=True)

conditions = {
    "Diabetes": {
        "foods": ["Brown rice", "Quinoa", "Oats", "Green veggies", "Nuts"],
        "tip": "Focus on low glycemic index foods and balanced protein."
    },
    "PCOS": {
        "foods": ["High-protein meals", "Omega-3 rich foods", "Leafy greens", "Whole grains"],
        "tip": "Avoid refined sugars and processed carbs; prefer natural fiber."
    },
    "Hypertension": {
        "foods": ["Low-sodium meals", "Leafy greens", "Bananas", "Oats", "Fish"],
        "tip": "Reduce salt intake and processed food."
    }
}

choice = st.selectbox("💡 Select your condition", ["", *conditions.keys()])

if choice:
    st.subheader(f"✅ Recommended foods for {choice}")
    for food in conditions[choice]["foods"]:
        st.markdown(f"- 🥗 **{food}**")
    st.info(conditions[choice]["tip"])
st.markdown(
    """
    <div style="text-align:center; color:#5b6c6e; font-size:14px; margin-top:30px;">
        <hr style="width:80%; margin:auto; border:1px solid #2bc0a8; opacity:0.4;">
        All rights reserved <b>Allera © 2025</b>
    </div>
    """,
    unsafe_allow_html=True
)

