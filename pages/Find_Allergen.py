import streamlit as st
from PIL import Image
import re
from fuzzywuzzy import fuzz
import easyocr
from app import add_custom_style

# Apply consistent theme styling
add_custom_style()

# Page title and subtitle
st.title("🔍 Find Allergen")
st.caption("Scan or paste ingredients to detect allergens instantly using AI-powered text analysis.")

# Divider line
st.markdown("<hr style='border:1px solid #2bc0a8;'>", unsafe_allow_html=True)

# Allergen database
ALLERGENS = {
    "milk": ["milk", "lactose", "butter", "cream", "cheese", "yogurt", "ghee"],
    "egg": ["egg", "albumen", "yolk"],
    "peanut": ["peanut", "groundnut"],
    "gluten": ["wheat", "barley", "rye", "gluten"],
    "soy": ["soy", "soya", "soybean"],
    "fish": ["fish", "salmon", "tuna"],
    "shellfish": ["prawn", "crab", "shrimp"],
    "tree nuts": ["almond", "cashew", "walnut", "hazelnut"],
    "sesame": ["sesame", "tahini"],
}


# ---------------------------
# Helper functions
# ---------------------------

def normalize(text):
    """Cleans and standardizes text for allergen matching."""
    text = text.lower()
    text = re.sub(r"[^a-z ]", " ", text)
    return text


def find_allergens(text, threshold=90):
    """Detects allergens using both direct and fuzzy matching."""
    text = normalize(text)
    found = set()

    for allergen, words in ALLERGENS.items():
        for w in words:
            if w in text or fuzz.partial_ratio(w, text) > threshold:
                found.add(allergen)

    return list(found)


# ---------------------------
# UI Input Section
# ---------------------------

option = st.radio("Choose input type:", ["Paste ingredients", "Upload label image"])
text_input = ""

# ---------------------------
# Default informative dashboard
# ---------------------------
if not text_input and option == "Paste ingredients":
    st.markdown("""
    <div style='background:linear-gradient(180deg,rgba(255,255,255,0.85),rgba(255,255,255,0.7));
    padding:25px;border-radius:15px;text-align:center;box-shadow:0 6px 18px rgba(0,0,0,0.05);'>
        <h3 style='color:#00796b;'>🌾 How Allera Detects Allergens</h3>
        <p style='color:#555;font-size:15px;'>
            Upload your food label or paste ingredient text — our AI scans it for known allergens like
            <b>milk, nuts, gluten, soy, and shellfish</b> using advanced text recognition.
        </p>
        <div style='display:flex;justify-content:center;flex-wrap:wrap;margin-top:20px;'>
            <div style='width:220px;padding:15px;border-radius:12px;background-color:#e8f7f5;margin:8px;'>
                <h4>📷 Scan Label</h4>
                <p style='font-size:13px;color:#333;'>Upload clear food label images for automatic detection.</p>
            </div>
            <div style='width:220px;padding:15px;border-radius:12px;background-color:#eaf8fb;margin:8px;'>
                <h4>🔠 Paste Ingredients</h4>
                <p style='font-size:13px;color:#333;'>Manually paste ingredients from websites or packaging.</p>
            </div>
            <div style='width:220px;padding:15px;border-radius:12px;background-color:#f0f9e8;margin:8px;'>
                <h4>⚙️ Analyze Instantly</h4>
                <p style='font-size:13px;color:#333;'>AI identifies allergens using pattern and fuzzy matching.</p>
            </div>
            <div style='width:220px;padding:15px;border-radius:12px;background-color:#fdf6e8;margin:8px;'>
                <h4>🩺 Stay Safe</h4>
                <p style='font-size:13px;color:#333;'>Make informed food choices, avoid allergic triggers.</p>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

# ---------------------------
# Paste Ingredients Mode
# ---------------------------

if option == "Paste ingredients":
    text_input = st.text_area(
        "🧾 Enter ingredients:",
        placeholder="e.g. Wheat flour, sugar, milk powder, eggs, soy lecithin...",
    )

    if st.button("🔍 Analyze"):
        if not text_input.strip():
            st.warning("Please paste ingredients first.")
        else:
            with st.spinner("⚙️ Analyzing allergens..."):
                allergens = find_allergens(text_input)
                if allergens:
                    st.error(f"⚠️ Allergens found: **{', '.join(allergens)}**")
                else:
                    st.success("✅ No common allergens detected.")


# ---------------------------
# Upload Label Image Mode
# ---------------------------

else:
    file = st.file_uploader("📷 Upload label image", type=["png", "jpg", "jpeg"])
    if file:
        img = Image.open(file)
        st.image(img, caption="Uploaded Label", use_container_width=True)

        with st.spinner("🔎 Extracting text using EasyOCR..."):
            try:
                reader = easyocr.Reader(['en'], gpu=False)
                result = reader.readtext(img, detail=0)
                extracted = " ".join(result)
            except Exception as e:
                st.error(f"❌ OCR failed: {e}")
                extracted = ""

        if extracted.strip():
            st.success("✅ Text successfully extracted from image.")
            text_input = st.text_area("🔠 Extracted text (editable):", value=extracted, height=150)

            # Auto-analyze immediately
            with st.spinner("⚙️ Analyzing allergens..."):
                allergens = find_allergens(extracted)
                if allergens:
                    st.error(f"⚠️ Allergens found: **{', '.join(allergens)}**")
                else:
                    st.success("✅ No common allergens detected.")
        else:
            st.warning("⚠️ Could not extract readable text. Try uploading a clearer image.")


# ---------------------------
# Safety Tips Section
# ---------------------------

st.markdown("""
<div style='margin-top:30px;padding:20px;border-radius:15px;background-color:#f1fbf0;
box-shadow:0 6px 16px rgba(0,0,0,0.05);'>
    <h4>🧠 Tips for Better Accuracy</h4>
    <ul style='color:#333;font-size:14px;text-align:left;line-height:1.6;'>
        <li>📸 Ensure your label photo is clear and well-lit for OCR accuracy.</li>
        <li>🔠 If AI misses something, edit the extracted text and re-analyze.</li>
        <li>🧾 Cross-check results with packaging warnings (e.g., “May contain traces of nuts”).</li>
        <li>💬 You can paste ingredients from websites for quick verification.</li>
    </ul>
</div>
""", unsafe_allow_html=True)


# ---------------------------
# Centered Footer
# ---------------------------

st.markdown("""
<div style="text-align:center; color:#5b6c6e; font-size:14px; margin-top:30px;">
    <hr style="width:80%; margin:auto; border:1px solid #2bc0a8; opacity:0.4;">
    Built with ❤️ for <b>Allera</b> | AI Health Assistant © 2025
</div>
""", unsafe_allow_html=True)
