import streamlit as st
from PIL import Image
import pytesseract
import re
from fuzzywuzzy import fuzz
from app import add_custom_style

add_custom_style()

st.title("🔍 Find Allergen")
st.caption("Scan or paste ingredients to detect allergens instantly.")

# Color accent divider
st.markdown("<hr style='border:1px solid #2bc0a8;'>", unsafe_allow_html=True)

ALLERGENS = {
    "milk": ["milk", "lactose", "butter", "cream", "cheese"],
    "egg": ["egg", "albumen", "yolk"],
    "peanut": ["peanut", "groundnut"],
    "gluten": ["wheat", "barley", "rye", "gluten"],
    "soy": ["soy", "soya", "soybean"],
}

def normalize(text):
    text = text.lower()
    text = re.sub(r"[^a-z ]", " ", text)
    return text

def find_allergens(text):
    text = normalize(text)
    found = []
    for allergen, words in ALLERGENS.items():
        for w in words:
            if w in text:
                found.append(allergen)
    return list(set(found))

option = st.radio("Choose input type:", ["Paste ingredients", "Upload label image"])
text_input = ""

if option == "Paste ingredients":
    text_input = st.text_area(
        "🧾 Enter ingredients:",
        placeholder="e.g. Wheat flour, sugar, milk powder, eggs, soy lecithin..."
    )
else:
    file = st.file_uploader("📷 Upload label image", type=["png", "jpg", "jpeg"])
    if file:
        img = Image.open(file)
        st.image(img, caption="Uploaded Label", use_column_width=True)
        extracted = pytesseract.image_to_string(img)
        text_input = st.text_area("🔠 Extracted text:", value=extracted, height=150)

if st.button("🔍 Analyze"):
    if not text_input.strip():
        st.warning("Please paste text or upload an image first.")
    else:
        allergens = find_allergens(text_input)
        if allergens:
            st.error(f"⚠️ Allergens found: **{', '.join(allergens)}**")
        else:
            st.success("✅ No common allergens detected.")
st.markdown(
    """
    <div style="text-align:center; color:#5b6c6e; font-size:14px; margin-top:30px;">
        <hr style="width:80%; margin:auto; border:1px solid #2bc0a8; opacity:0.4;">
        All rights reserved <b>Allera © 2025</b>
    </div>
    """,
    unsafe_allow_html=True
)

