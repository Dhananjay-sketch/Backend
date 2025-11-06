import streamlit as st
from app import add_custom_style

add_custom_style()

st.title("💪 Gym Diet Plan")
st.caption("Get your personalized diet plan, daily protein target, and fitness recommendations powered by AI.")

st.markdown("<hr style='border:1px solid #2bc0a8;'>", unsafe_allow_html=True)

# --- User Inputs ---
st.subheader("🏋️ Enter Your Details")

col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Weight (kg)", min_value=30.0, max_value=200.0, value=70.0)
    height = st.number_input("Height (cm)", min_value=120.0, max_value=230.0, value=170.0)
with col2:
    age = st.number_input("Age", min_value=15, max_value=70, value=25)
    gender = st.selectbox("Gender", ["Male", "Female"])

goal = st.selectbox("🎯 Fitness Goal", ["Muscle Gain", "Fat Loss", "Maintenance"])
activity_level = st.selectbox(
    "⚡ Activity Level",
    ["Sedentary", "Lightly Active", "Moderately Active", "Very Active"]
)

# --- When Button Clicked ---
if st.button("📊 Generate Diet Plan"):
    st.markdown("<hr>", unsafe_allow_html=True)
    
    # --- BMI Calculation ---
    height_m = height / 100
    bmi = weight / (height_m ** 2)

    if bmi < 18.5:
        bmi_status = "Underweight"
        st.warning(f"⚠️ Your BMI is **{bmi:.1f}**, which falls under the **Underweight** category. You may need to increase calorie intake.")
    elif 18.5 <= bmi < 24.9:
        bmi_status = "Normal"
        st.success(f"✅ Your BMI is **{bmi:.1f}**, which is in the **Healthy/Normal** range. Keep maintaining your diet!")
    elif 25 <= bmi < 29.9:
        bmi_status = "Overweight"
        st.warning(f"⚠️ Your BMI is **{bmi:.1f}**, which falls under the **Overweight** category. A calorie deficit plan is recommended.")
    else:
        bmi_status = "Obese"
        st.error(f"🚨 Your BMI is **{bmi:.1f}**, classified as **Obese**. Focus on gradual fat loss with consistent diet and light workouts.")
    
    st.markdown("<br>", unsafe_allow_html=True)

    # --- Calculate BMR ---
    if gender == "Male":
        bmr = 88.36 + (13.4 * weight) + (4.8 * height) - (5.7 * age)
    else:
        bmr = 447.6 + (9.2 * weight) + (3.1 * height) - (4.3 * age)

    # --- Activity factor ---
    factors = {
        "Sedentary": 1.2,
        "Lightly Active": 1.375,
        "Moderately Active": 1.55,
        "Very Active": 1.725,
    }
    maintenance_calories = bmr * factors[activity_level]

    # --- Adjust for fitness goal ---
    if goal == "Muscle Gain":
        target_calories = maintenance_calories + 300
    elif goal == "Fat Loss":
        target_calories = maintenance_calories - 300
    else:
        target_calories = maintenance_calories

    protein = weight * 1.8  # grams per day

    # --- Output results ---
    st.subheader("📈 Your Personalized Plan")
    st.info(f"**Daily Calorie Target:** {target_calories:.0f} kcal")
    st.success(f"**Recommended Protein Intake:** {protein:.0f} g/day")

    # --- Meal Recommendations ---
    st.markdown("### 🥗 Suggested Full-Day Diet Plan")
    if goal == "Muscle Gain":
        st.markdown("""
        **Breakfast:**  
        - Oats with milk, banana, and peanut butter 🥣  
        - 4 boiled eggs 🥚  
        - Green tea ☕  

        **Mid-Morning Snack:**  
        - Handful of almonds or a protein smoothie  

        **Lunch:**  
        - Brown rice or quinoa 🍚  
        - Grilled chicken or paneer 🍗  
        - Steamed vegetables 🥦  

        **Evening Snack:**  
        - Protein shake with fruit or yogurt 🥤  

        **Dinner:**  
        - Whole wheat roti with lentils 🍠  
        - Grilled tofu or fish 🐟  
        - Salad 🥗  
        """)
    elif goal == "Fat Loss":
        st.markdown("""
        **Breakfast:**  
        - Egg white omelette or Greek yogurt 🥚  
        - Apple or berries 🍎  

        **Mid-Morning Snack:**  
        - Black coffee or green tea ☕  

        **Lunch:**  
        - Brown rice or millets 🍚  
        - Grilled paneer, fish, or chicken 🍗  
        - Cucumber salad 🥒  

        **Evening Snack:**  
        - Handful of nuts or boiled sprouts 🌰  

        **Dinner:**  
        - Vegetable soup 🥣  
        - Tofu or lean meat with vegetables 🥦  
        """)
    else:
        st.markdown("""
        **Breakfast:**  
        - Oats with milk 🥣  
        - 3 boiled eggs 🥚  
        - Coffee or green tea ☕  

        **Lunch:**  
        - Rice with lentils 🍛  
        - Mixed salad 🥗  

        **Dinner:**  
        - Roti with paneer curry or tofu 🥘  
        - Fruit bowl 🍉  
        """)

    st.markdown("""
    💧 **Tip:** Stay hydrated — aim for at least 3L of water per day.  
    🕒 **Best practice:** Sleep 7–8 hours for muscle recovery and hormone balance.
    """)

# --- Footer ---
st.markdown("""
<div style="text-align:center; color:#5b6c6e; font-size:14px; margin-top:30px;">
    <hr style="width:80%; margin:auto; border:1px solid #2bc0a8; opacity:0.4;">
   <b>Allera</b> - Built with ❤️  | AI Health Assistant © 2025
</div>
""", unsafe_allow_html=True)
