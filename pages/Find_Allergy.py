import streamlit as st
from datetime import datetime
from app import add_custom_style

add_custom_style()

st.title("📊 Allergy Tracker")
st.caption("Log your symptoms and track possible allergens over time.")

st.markdown("<hr style='border:1px solid #2bc0a8;'>", unsafe_allow_html=True)

symptom = st.text_input("🤧 Symptoms", placeholder="e.g., itching, rash, nausea")
food = st.text_input("🍽️ Suspected food", placeholder="e.g., Milkshake, Bread, Peanuts")
notes = st.text_area("🗒️ Additional notes", placeholder="How did you feel after eating?")
submitted = st.button("💾 Save Entry")

if submitted:
    with open("allergy_log.txt", "a") as f:
        f.write(f"{datetime.now()} | Food: {food} | Symptoms: {symptom} | Notes: {notes}\n")
    st.success("✅ Entry saved successfully!")

st.markdown("---")
st.subheader("📜 Previous Entries")
try:
    with open("allergy_log.txt", "r") as f:
        logs = f.readlines()
    for log in reversed(logs[-10:]):
        st.markdown(f"🔹 {log.strip()}")
except FileNotFoundError:
    st.info("No logs yet. Start by adding your first entry above.")
st.markdown(
    """
    <div style="text-align:center; color:#5b6c6e; font-size:14px; margin-top:30px;">
        <hr style="width:80%; margin:auto; border:1px solid #2bc0a8; opacity:0.4;">
        All rights reserved <b>Allera © 2025</b>
    </div>
    """,
    unsafe_allow_html=True
)

