import streamlit as st
from datetime import datetime
import pandas as pd
import os
from app import add_custom_style

# Apply custom Allera theme
add_custom_style()

# ---------------------------
# Page Header
# ---------------------------
st.title("📊 Allergy Tracker")
st.caption("Log your symptoms, track patterns, and identify potential allergens over time.")

st.markdown("<hr style='border:1px solid #2bc0a8;'>", unsafe_allow_html=True)

# ---------------------------
# Input Section
# ---------------------------
st.subheader("🩹 Add a New Entry")

col1, col2 = st.columns(2)
with col1:
    symptom = st.text_input("🤧 Symptoms", placeholder="e.g., itching, rash, nausea")
with col2:
    food = st.text_input("🍽️ Suspected Food", placeholder="e.g., Milkshake, Bread, Peanuts")

notes = st.text_area("🗒️ Additional Notes", placeholder="How did you feel after eating? Any patterns noticed?")
submitted = st.button("💾 Save Entry")

log_file = "allergy_log.csv"

# ---------------------------
# Save Data
# ---------------------------
if submitted:
    if symptom.strip() == "" or food.strip() == "":
        st.warning("⚠️ Please fill both symptom and food fields before saving.")
    else:
        entry = {
            "Date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "Symptom": symptom.strip(),
            "Food": food.strip(),
            "Notes": notes.strip()
        }
        df = pd.DataFrame([entry])
        if os.path.exists(log_file):
            df_existing = pd.read_csv(log_file)
            df = pd.concat([df_existing, df], ignore_index=True)
        df.to_csv(log_file, index=False)
        st.success("✅ Entry saved successfully!")

# ---------------------------
# Dashboard Overview
# ---------------------------
st.markdown("---")
st.subheader("📈 Allergy Insights")

if os.path.exists(log_file):
    logs = pd.read_csv(log_file)

    if len(logs) > 0:
        # Most frequent foods and symptoms
        common_foods = logs['Food'].value_counts().head(3)
        common_symptoms = logs['Symptom'].value_counts().head(3)

        col1, col2 = st.columns(2)
        with col1:
            st.markdown("### 🍞 Most Common Foods Triggering Reactions")
            for food, count in common_foods.items():
                st.markdown(f"- {food} ({count}×)")

        with col2:
            st.markdown("### 🤧 Most Frequent Symptoms")
            for sym, count in common_symptoms.items():
                st.markdown(f"- {sym} ({count}×)")

        # Display recent entries
        st.markdown("---")
        st.subheader("📜 Recent Allergy Log Entries")

        for _, row in logs.tail(8).iloc[::-1].iterrows():
            st.markdown(
                f"""
                <div style='background:rgba(255,255,255,0.75);padding:10px;border-radius:10px;
                margin-bottom:10px;box-shadow:0 4px 10px rgba(0,0,0,0.05);'>
                    <b>🕒 {row['Date']}</b><br>
                    <b>🍽️ Food:</b> {row['Food']}<br>
                    <b>🤧 Symptom:</b> {row['Symptom']}<br>
                    <b>🗒️ Notes:</b> {row['Notes'] if row['Notes'] else '—'}
                </div>
                """,
                unsafe_allow_html=True
            )
    else:
        st.info("No logs yet. Start by adding your first entry above.")
else:
    # Empty state info section
    st.markdown("""
    <div style='background:linear-gradient(180deg,rgba(255,255,255,0.85),rgba(255,255,255,0.6));padding:25px;border-radius:15px;text-align:center;
    box-shadow:0 6px 18px rgba(0,0,0,0.05);'>
        <h3 style='color:#00897b;'>🧬 Start Tracking Your Allergies</h3>
        <p style='color:#555;font-size:15px;'>Record what you eat and how you feel to identify hidden triggers.</p>
        <div style='display:flex;justify-content:center;flex-wrap:wrap;margin-top:20px;'>
            <div style='width:250px;padding:15px;border-radius:12px;background-color:#e8f7f5;margin:8px;'>
                <h4>🍽️ Log Meals</h4>
                <p style='font-size:13px;color:#333;'>Track foods that cause discomfort or allergic responses.</p>
            </div>
            <div style='width:250px;padding:15px;border-radius:12px;background-color:#eaf8fb;margin:8px;'>
                <h4>🧾 Observe Patterns</h4>
                <p style='font-size:13px;color:#333;'>Over time, see which foods appear most frequently in your logs.</p>
            </div>
            <div style='width:250px;padding:15px;border-radius:12px;background-color:#f0f9e8;margin:8px;'>
                <h4>💡 Gain Insights</h4>
                <p style='font-size:13px;color:#333;'>Identify allergens faster and make diet adjustments confidently.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------
# Footer
# ---------------------------
st.markdown(
    """
    <div style="text-align:center; color:#5b6c6e; font-size:14px; margin-top:30px;">
        <hr style="width:80%; margin:auto; border:1px solid #2bc0a8; opacity:0.4;">
        Built with ❤️ for <b>Allera</b> | AI Health Assistant © 2025
    </div>
    """,
    unsafe_allow_html=True
)
