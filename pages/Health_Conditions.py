import streamlit as st
from app import add_custom_style

# Apply consistent theme styling
add_custom_style()

# Title and description
st.title("🩺 Health Conditions")
st.caption("Get condition-based food recommendations, lifestyle tips, and AI-driven nutrition insights.")

st.markdown("<hr style='border:1px solid #2bc0a8;'>", unsafe_allow_html=True)

# ---------------------------
# Data
# ---------------------------
conditions = {
    "Diabetes": {
        "foods": ["Brown rice", "Quinoa", "Oats", "Leafy greens", "Nuts", "Lean protein"],
        "avoid": ["White rice", "Sugary drinks", "Pastries", "Refined flour foods"],
        "tip": "Focus on low glycemic index foods and add fiber to control sugar spikes."
    },
    "PCOS": {
        "foods": ["High-protein meals", "Omega-3 rich foods", "Leafy greens", "Whole grains", "Seeds"],
        "avoid": ["Refined sugar", "White bread", "Junk food", "Dairy (in excess)"],
        "tip": "Balance insulin levels with low-carb, high-protein meals."
    },
    "Hypertension": {
        "foods": ["Low-sodium meals", "Leafy greens", "Bananas", "Oats", "Fish", "Garlic"],
        "avoid": ["Salty snacks", "Pickles", "Processed meat", "Caffeine"],
        "tip": "Reduce salt intake and processed foods; increase potassium intake."
    },
    "Heart Disease": {
        "foods": ["Oats", "Salmon", "Avocado", "Nuts", "Berries", "Olive oil"],
        "avoid": ["Fried foods", "Processed meat", "Butter", "Sugar"],
        "tip": "Focus on healthy fats and antioxidants for heart health."
    },
    "Obesity": {
        "foods": ["Whole grains", "Legumes", "Fruits", "Lean meats", "Vegetables"],
        "avoid": ["Fast food", "Sugary beverages", "Refined carbs"],
        "tip": "Control portion size and prefer high-fiber, low-calorie meals."
    },
    "Chronic Kidney Disease": {
        "foods": ["Cauliflower", "Blueberries", "Olive oil", "Cabbage", "Egg whites"],
        "avoid": ["High-sodium foods", "Red meat", "Dairy", "Canned food"],
        "tip": "Limit sodium and potassium; maintain hydration carefully."
    },
    "Anemia": {
        "foods": ["Spinach", "Lentils", "Red meat (moderate)", "Iron-fortified cereals"],
        "avoid": ["Tea/Coffee with meals", "Processed food"],
        "tip": "Increase iron intake and pair with vitamin C-rich foods."
    },
    "Thyroid Disorder": {
        "foods": ["Iodized salt", "Brazil nuts", "Eggs", "Berries", "Lean protein"],
        "avoid": ["Soy", "Cruciferous vegetables (excess)", "Refined sugar"],
        "tip": "Ensure proper iodine intake and avoid excessive processed foods."
    },
}

# ---------------------------
# Selection box
# ---------------------------
choice = st.selectbox("💡 Select your condition", ["", *conditions.keys()])

# ---------------------------
# Default dashboard (before selection)
# ---------------------------
if not choice:
    st.markdown("""
    <div style='background:linear-gradient(180deg,rgba(255,255,255,0.8),rgba(255,255,255,0.5));padding:25px;border-radius:15px;text-align:center;box-shadow:0 8px 20px rgba(0,0,0,0.05);'>
        <h3 style='color:#00796b;'>🌱 Live Better with Smarter Nutrition</h3>
        <p style='color:#555;font-size:15px;'>Your health journey starts with understanding what your body needs.</p>
        <div style='display:flex;justify-content:space-around;flex-wrap:wrap;margin-top:20px;'>
            <div style='width:240px;padding:15px;border-radius:12px;background-color:#e8f7f5;margin:8px;'>
                <h4>🥦 Eat Smart</h4>
                <p style='font-size:14px;color:#333;'>Choose fresh, whole foods that support your condition.</p>
            </div>
            <div style='width:240px;padding:15px;border-radius:12px;background-color:#eaf8fb;margin:8px;'>
                <h4>💧 Stay Hydrated</h4>
                <p style='font-size:14px;color:#333;'>Water supports digestion, circulation, and detoxification.</p>
            </div>
            <div style='width:240px;padding:15px;border-radius:12px;background-color:#f0f9e8;margin:8px;'>
                <h4>🏃‍♂️ Move Daily</h4>
                <p style='font-size:14px;color:#333;'>Even light exercise improves energy and overall health.</p>
            </div>
            <div style='width:240px;padding:15px;border-radius:12px;background-color:#fdf6e8;margin:8px;'>
                <h4>🧘 Manage Stress</h4>
                <p style='font-size:14px;color:#333;'>Meditation, yoga, and rest are vital for wellness.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------
# Condition-specific recommendations
# ---------------------------
if choice:
    data = conditions[choice]
    st.markdown(f"<h3 style='color:#00897b;'>✅ Recommended foods for {choice}</h3>", unsafe_allow_html=True)
    st.markdown("<ul style='list-style-type:none;'>", unsafe_allow_html=True)
    for food in data["foods"]:
        st.markdown(f"<li>🥗 <b>{food}</b></li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)

    st.markdown(f"<h3 style='color:#e53935;'>🚫 Avoid these foods</h3>", unsafe_allow_html=True)
    st.markdown("<ul style='list-style-type:none;'>", unsafe_allow_html=True)
    for food in data["avoid"]:
        st.markdown(f"<li>❌ <b>{food}</b></li>", unsafe_allow_html=True)
    st.markdown("</ul>", unsafe_allow_html=True)

    st.info(f"💬 Tip: {data['tip']}")

# ---------------------------
# Footer
# ---------------------------
st.markdown("""
<div style="text-align:center; color:#5b6c6e; font-size:14px; margin-top:30px;">
    <hr style="width:80%; margin:auto; border:1px solid #2bc0a8; opacity:0.4;">
   <b>Allera</b> - Built with ❤️ | AI Health Assistant © 2025
</div>
""", unsafe_allow_html=True)
