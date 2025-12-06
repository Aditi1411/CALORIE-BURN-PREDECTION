import streamlit as st
import numpy as np
import pickle
import os
import gdown

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Calorie Burn Predictor",
    layout="wide"
)

# ---------------- MODEL DOWNLOAD ---------------- #
MODEL_PATH = "calorie_model.pkl"

# ✅ YOUR GOOGLE DRIVE FILE ID LINK (PUBLIC)
MODEL_URL = "https://drive.google.com/uc?id=1GLKTe4EyvAaLPBY2FU2Z"

if not os.path.exists(MODEL_PATH):
    with st.spinner("Downloading ML model..."):
        gdown.download(
            url=MODEL_URL,
            output=MODEL_PATH,
            quiet=False,
            fuzzy=True
        )

# ---------------- LOAD MODEL ---------------- #
with open(MODEL_PATH, "rb") as f:
    rfr = pickle.load(f)

# ---------------- CSS (NO WHITE BOX BUG) ---------------- #
st.markdown("""
<style>
/* Hide empty Streamlit containers */
div:empty {
    display: none;
}

/* Center form card */
.form-card {
    background: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0 6px 18px rgba(0,0,0,0.2);
}
</style>
""", unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
st.sidebar.title("📌 Project Info")
st.sidebar.markdown("""
**Project:** Calorie Burn Prediction  
**Algorithm:** Random Forest Regressor  

### Inputs
- Gender  
- Age  
- Height  
- Weight  
- Duration  
- Heart Rate  
- Body Temperature  

### Output
Calories burned during workout
""")

# ---------------- MAIN UI ---------------- #
st.markdown("## 🔥 Calorie Burn Predictor")
st.markdown("Enter your workout details below")

col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    st.markdown('<div class="form-card">', unsafe_allow_html=True)

    Gender = st.selectbox("Gender", ["Male", "Female"])
    Age = st.number_input("Age", 1, 100, 25)
    Height = st.number_input("Height (cm)", 100.0, 250.0, 170.0)
    Weight = st.number_input("Weight (kg)", 30.0, 200.0, 65.0)
    Duration = st.number_input("Exercise Duration (minutes)", 1, 300, 30)
    Heart_rate = st.number_input("Heart Rate (bpm)", 60, 200, 120)
    Body_temp = st.number_input("Body Temperature (°C)", 35.0, 42.0, 37.0)

    if st.button("🔥 Predict Calories"):
        gender_val = 1 if Gender == "Male" else 0
        input_data = np.array([[gender_val, Age, Height, Weight, Duration, Heart_rate, Body_temp]])
        prediction = rfr.predict(input_data)
        st.success(f"✅ Estimated Calories Burned: **{int(prediction[0])} kcal**")

    st.markdown("</div>", unsafe_allow_html=True)



