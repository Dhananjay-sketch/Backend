import streamlit as st
def add_custom_style():
    st.markdown("""
        <style>
        /* Global background gradient */
        .stApp {
            background: linear-gradient(135deg, #e0f7f4, #ccecf7);
            font-family: 'Poppins', sans-serif;
            color: #022b28;
        }

        /* Header styling */
        h1, h2, h3 {
            color: #2bc0a8 !important;
        }

        /* Streamlit buttons */
        button[kind="primary"] {
            background-color: #2bc0a8 !important;
            color: white !important;
            border-radius: 8px !important;
            font-weight: 600 !important;
            transition: all 0.2s ease-in-out !important;
        }
        button[kind="primary"]:hover {
            background-color: #26a893 !important;
            transform: scale(1.05);
        }

        /* Text inputs & boxes */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea {
            border-radius: 10px;
            border: 1px solid #b2e0d4;
            background-color: #ffffffcc;
        }

        /* Info / Success / Error boxes */
        .stAlert {
            border-radius: 10px;
            background-color: #f7fffd !important;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background-color: #f0faf9 !important;
            color: #022b28;
        }

        /* Center containers */
        .main > div {
            padding: 2rem;
        }
        </style>
    """, unsafe_allow_html=True)

st.set_page_config(
    page_title="Allera — Health & Allergy Companion",
    page_icon="🧬",
    layout="centered"
)

st.title("🧬 Allera")
st.caption("Your AI-powered Health & Allergy Companion")

st.markdown("""
Welcome to **Allera**, your personal assistant for:
- 🔍 Detecting allergens from ingredients or food labels  
- 🩺 Managing your health conditions like Diabetes, PCOS, or Hypertension  
- 📊 Tracking allergies and identifying symptom patterns  

Use the **left sidebar** or links from your landing page to navigate.
""")

st.info("👉 Tip: Click the sidebar menu to explore different sections.")
