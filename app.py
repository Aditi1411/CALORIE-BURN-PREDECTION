import streamlit as st
import numpy as np
import pickle
from huggingface_hub import hf_hub_download

# ---------------- PAGE CONFIG ---------------- #
st.set_page_config(
    page_title="Calorie Burn Prediction",
    layout="wide"
)

# ---------------- LOAD MODEL FROM HUGGING FACE ---------------- #
MODEL_PATH = hf_hub_download(
    repo_id="aditi1411963/calorie-burn-prediction",
    filename="calorie_model.pkl"
)

with open(MODEL_PATH, "rb") as f:
    model = pickle.load(f)

# ---------------- SIDEBAR (NO HTML) ---------------- #
st.sidebar.title(" Calorie Burn Predictor")

st.sidebar.subheader("📌 About Project")
st.sidebar.write(
    "This **Calorie Burn Prediction System** uses a "
    "**ML model** trained on fitness data "
    "to estimate calories burned during physical activity."
   
)

st.sidebar.subheader("🧠 Features Used")
st.sidebar.markdown("""
- Gender  
- Age  
- Height (cm)  
- Weight (kg)  
- Exercise Duration (min)  
- Heart Rate (bpm)  
- Body Temperature (°C)
""")

st.sidebar.subheader("🎯 Applications")
st.sidebar.markdown("""
• Fitness tracking apps  
• Health monitoring systems  
• Machine learning academic projects
""")

st.sidebar.subheader("👩‍💻 Developed By")
st.sidebar.write("Aditi Tripathi")

# ---------------- MAIN TITLE ---------------- #
st.markdown(
    "<h1 style='text-align:center;'>🔥 Calorie Burn Prediction</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>Enter your details below to predict calories burned</p>",
    unsafe_allow_html=True
)

# ---------------- CENTER INPUTS ---------------- #
left, center, right = st.columns([1, 2, 1])

with center:
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age (years)", 1, 100, 25)
    height = st.number_input("Height (cm)", 100.0, 250.0, 170.0)
    weight = st.number_input("Weight (kg)", 30.0, 200.0, 65.0)
    duration = st.number_input("Exercise Duration (minutes)", 1.0, 300.0, 30.0)
    heart_rate = st.number_input("Heart Rate (bpm)", 40.0, 200.0, 90.0)
    body_temp = st.number_input("Body Temperature (°C)", 35.0, 42.0, 37.0)

    predict_btn = st.button(" Predict Calories Burned")

# ---------------- PREDICTION ---------------- #
if predict_btn:
    gender_encoded = 1 if gender == "Male" else 0

    input_data = np.array([[
        gender_encoded,
        age,
        height,
        weight,
        duration,
        heart_rate,
        body_temp
    ]])

    prediction = model.predict(input_data)

    st.success(f"✅ Estimated Calories Burned: **{prediction[0]:.2f} kcal**")

# ---------------- FOOTER ---------------- #
st.markdown(
    "<hr><p style='text-align:center; font-size:13px;'>"
    "Calorie Burn Prediction System | Machine Learning Project"
    "</p>",
    unsafe_allow_html=True
)




