import streamlit as st
import numpy as np
import pickle
import os
import gdown

# ---------------- PAGE SETTINGS ---------------- #
st.set_page_config(
    page_title="Calorie Burn Predictor",
    layout="wide"
)

# ---------------- DOWNLOAD & LOAD MODEL ---------------- #
MODEL_FILE_ID = "1GLKTe4EyvAaLPBY2FU2ZolVnB6DCu7vz"  # your Drive file ID
MODEL_PATH = "rfr.pkl"

if not os.path.exists(MODEL_PATH):
    url = f"https://drive.google.com/uc?id={MODEL_FILE_ID}"
    gdown.download(url, MODEL_PATH, quiet=False)

with open(MODEL_PATH, "rb") as f:
    rfr = pickle.load(f)

# ---------------- STYLE ---------------- #
st.markdown("""
<style>
    .css-1y4p8pa, .css-q8sbsg, .stNumberInput, .stSelectbox {
        margin-bottom: -10px !important;
    }

    .stButton>button {
        background-color: #FF6B6B !important;
        color: white !important;
        padding: 10px;
        border-radius: 10px;
        font-size: 18px;
        width: 220px;
        border: none !important;
        transition: 0.3s;
    }

    .stButton>button:hover,
    .stButton>button:active {
        background-color: #FF9F9F !important;
        color: white !important;
    }

    h1 {
        color: #FF6B6B !important;
    }
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ---------------- #
st.markdown("<h1>Calorie Burn Predictor</h1>", unsafe_allow_html=True)
st.write("Enter your details below to estimate calories burned during exercise.")

# ---------------- PREDICTION FUNCTION ---------------- #
def predict_calories(gender, age, height, weight, duration, heart_rate, body_temp):
    features = np.array([[gender, age, height, weight, duration, heart_rate, body_temp]])
    return rfr.predict(features)[0]

# ---------------- INPUTS ---------------- #
st.subheader("Enter Your Details")

col1, col2, col3 = st.columns(3)

with col1:
    gender = st.selectbox("Gender", ["Male", "Female"])
    age = st.number_input("Age (years)", min_value=1, max_value=120, step=1)

with col2:
    height = st.number_input("Height (cm)", min_value=50, max_value=250, step=1)
    weight = st.number_input("Weight (kg)", min_value=20, max_value=200, step=1)

with col3:
    duration = st.number_input("Exercise Duration (minutes)", min_value=1, step=1)
    heart_rate = st.number_input("Heart Rate (bpm)", min_value=40, max_value=200, value=70)

body_temp = st.number_input(
    "Body Temperature (°C)",
    min_value=28.0,
    max_value=42.0,
    value=36.5
)

# Convert gender to numeric
gender = 1 if gender == "Male" else 0

# ---------------- PREDICT BUTTON ---------------- #
st.write("")
if st.button("Predict"):
    calories = predict_calories(
        gender, age, height, weight, duration, heart_rate, body_temp
    )

    st.markdown(f"""
        <div style="
            padding: 20px;
            border-radius: 12px;
            background: linear-gradient(90deg, #FF6B6B, #FF9F9F);
            text-align: center;
            font-size: 26px;
            color: black;
            font-weight: bold;
            margin-top: 20px;">
            Estimated Calories Burned: {int(calories)} kcal
        </div>
    """, unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
st.sidebar.header("How This Works")
st.sidebar.write("""
This web app predicts calories burned using a machine learning
model trained on fitness and physiological data.

**Features used:**
- Age
- Gender
- Height
- Weight
- Exercise Duration
- Heart Rate
- Body Temperature
""")

st.sidebar.header("Health Tip")
st.sidebar.write("""
Predictions are estimates.
Always consult a fitness or medical professional for personalized advice.
""")





