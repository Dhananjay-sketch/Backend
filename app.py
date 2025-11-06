import streamlit as st

# -----------------------------------------------------------
# GLOBAL APP CONFIGURATION
# -----------------------------------------------------------
st.set_page_config(
    page_title="Allera | AI Health Assistant",
    page_icon="🧬",
    layout="wide"
)

# -----------------------------------------------------------
# CUSTOM GLOBAL STYLE
# -----------------------------------------------------------
def add_custom_style():
    st.markdown("""
        <style>
        body {
            background: linear-gradient(135deg, #e8f7f5, #f1fbf0);
            color: #0f1720;
            font-family: 'Poppins', sans-serif;
        }
        .sidebar .sidebar-content {
            background: #f7fffd !important;
        }
        .stButton > button {
            background: linear-gradient(90deg, #43cea2, #185a9d);
            color: white;
            border: none;
            border-radius: 10px;
            font-weight: 600;
            padding: 0.5em 1em;
        }
        .stButton > button:hover {
            background: linear-gradient(90deg, #2bc0a8, #0a6db7);
            transform: translateY(-2px);
            transition: 0.2s ease;
        }
        h1, h2, h3, h4 {
            color: #0f5a52 !important;
        }
        hr {
            border: 1px solid #2bc0a8;
            opacity: 0.4;
        }
        </style>
    """, unsafe_allow_html=True)

add_custom_style()

# -----------------------------------------------------------
# SIDEBAR NAVIGATION
# -----------------------------------------------------------
st.sidebar.title("🧬 Allera Navigation")

page = st.sidebar.radio(
    "Go to",
    [
        "🏠 Home",
        "🔍 Find Allergen",
        "📊 Find Allergy",
        "🩺 Health Conditions",
        "💪 Gym Diet Plan"
    ]
)

# -----------------------------------------------------------
# HOME PAGE
# -----------------------------------------------------------
if page == "🏠 Home":
    st.markdown("""
        <div style="text-align:center; padding: 40px 10px; background: linear-gradient(135deg, #e8f7f5, #f3fdf7); border-radius: 20px;">
            <h1 style="color:#0f5a52; font-size:48px;">🌿 Welcome to <b>Allera</b></h1>
            <h3 style="color:#2bc0a8; font-weight:500;">Your AI-powered companion for smarter health, diet, and allergy insights.</h3>
            <p style="color:#4f5d5d; font-size:18px; margin-top:15px;">Empowering healthier lifestyles through data-driven nutrition and personalized wellness.</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # Quick Navigation Buttons
    st.markdown("""
        <div style="display:flex; justify-content:center; gap:20px; flex-wrap:wrap;">
            <a href="https://allera.streamlit.app/Find_Allergen" target="_blank" style="background:#2bc0a8; color:white; padding:14px 28px; border-radius:12px; text-decoration:none; font-weight:600;">🔍 Find Allergens</a>
            <a href="https://allera.streamlit.app/Health_Conditions" target="_blank" style="background:#43cea2; color:white; padding:14px 28px; border-radius:12px; text-decoration:none; font-weight:600;">🩺 Health Conditions</a>
            <a href="https://allera.streamlit.app/Find_Allergy" target="_blank" style="background:#185a9d; color:white; padding:14px 28px; border-radius:12px; text-decoration:none; font-weight:600;">📊 Allergy Tracker</a>
            <a href="https://allera.streamlit.app/Gym_Diet_Plan" target="_blank" style="background:#2bc0a8; color:white; padding:14px 28px; border-radius:12px; text-decoration:none; font-weight:600;">💪 Gym Diet Planner</a>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='margin-top:40px;'>", unsafe_allow_html=True)

    # Why Choose Allera Section
    st.markdown("## 🌟 Why Choose Allera?")
    st.markdown("""
        <div style="display:flex; flex-wrap:wrap; justify-content:space-around; margin-top:20px;">
            <div style="background:white; box-shadow:0 4px 10px rgba(0,0,0,0.05); border-radius:15px; padding:20px; width:300px; margin:10px;">
                <h3 style="color:#2bc0a8;">🤖 Smart Allergen Detection</h3>
                <p style="color:#5b6c6e;">Upload your food labels or paste ingredients, and let AI instantly identify harmful allergens for you.</p>
            </div>
            <div style="background:white; box-shadow:0 4px 10px rgba(0,0,0,0.05); border-radius:15px; padding:20px; width:300px; margin:10px;">
                <h3 style="color:#2bc0a8;">🧠 Health Condition Insights</h3>
                <p style="color:#5b6c6e;">Get food recommendations tailored for Diabetes, PCOS, Hypertension, and other chronic conditions.</p>
            </div>
            <div style="background:white; box-shadow:0 4px 10px rgba(0,0,0,0.05); border-radius:15px; padding:20px; width:300px; margin:10px;">
                <h3 style="color:#2bc0a8;">📈 Allergy Tracker</h3>
                <p style="color:#5b6c6e;">Log your symptoms, monitor reactions, and gain insights into your body’s food tolerance trends.</p>
            </div>
            <div style="background:white; box-shadow:0 4px 10px rgba(0,0,0,0.05); border-radius:15px; padding:20px; width:300px; margin:10px;">
                <h3 style="color:#2bc0a8;">💪 Personalized Gym Diet</h3>
                <p style="color:#5b6c6e;">Get custom protein, calorie, and meal recommendations based on your fitness goals and activity level.</p>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<hr style='margin-top:40px;'>", unsafe_allow_html=True)

    # Mission and About
    st.markdown("""
        ### 🌱 Your Health, Simplified

        At **Allera**, we believe that technology and empathy can come together to revolutionize the way you take care of your health.  
        Our AI-driven platform helps you make smarter dietary decisions, prevent allergic reactions, and maintain a balanced lifestyle with ease.

        **Here’s what you can do with Allera:**
        - 🧾 **Instant Allergen Detection:** Get real-time insights into potential allergens.
        - 🩺 **Condition-Aware Diet Plans:** Personalized for Diabetes, PCOS, and Hypertension.
        - 📊 **Symptom Tracker:** Detect possible food-related reactions.
        - 💪 **AI Gym Diet Plan:** Get daily calorie, protein, and meal guidance.

        ---
        ### 💡 How Allera Works
        1. Input or scan your food details using the app.  
        2. AI instantly analyzes and identifies allergens or harmful ingredients.  
        3. The system provides health-safe alternatives and recommendations.  
        4. Track your diet, symptoms, and goals — all in one place!

        ---
        ### ❤️ Our Mission
        To make **personal health management intelligent, accessible, and proactive**.  
        We aim to empower individuals to take control of their well-being using data, AI, and personalized insights.

        > “Healthy living isn’t about restriction — it’s about awareness, balance, and making informed choices.”

        ---
        ### 🚀 What’s Next
        - Integrating wearable health data (like smartwatches)  
        - Personalized supplement recommendations  
        - AI chatbot for real-time nutrition guidance  
    """, unsafe_allow_html=True)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
        <div style="text-align:center; color:#5b6c6e; font-size:14px; margin-top:30px;">
            <b>Allera</b> - Built with ❤️ | AI Health Assistant © 2025
        </div>
    """, unsafe_allow_html=True)


# -----------------------------------------------------------
# PAGE IMPORTS (DIRECTLY RUN PAGES)
# -----------------------------------------------------------
elif page == "🔍 Find Allergen":
    import pages.Find_Allergen
elif page == "📊 Find Allergy":
    import pages.Find_Allergy
elif page == "🩺 Health Conditions":
    import pages.Health_Conditions
elif page == "💪 Gym Diet Plan":
    import pages.Gym_Diet_Plan
