import streamlit as st
import numpy as np
import pickle
import os
import urllib.request

# ---------------- LOAD MODEL FROM GOOGLE DRIVE ---------------- #
MODEL_URL = "https://drive.google.com/uc?id=1GLKTe4EyvAaLPBY2FU2ZolVnB6DCu7vz"
MODEL_PATH = "rfr.pkl"

if not os.path.exists(MODEL_PATH):
    urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)

rfr = pickle.load(open(MODEL_PATH, "rb"))

# ---------------- PAGE SETTINGS ---------------- #
st.set_page_config(
    page_title="Calorie Burn Predictor",
    layout="wide"
)

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

# ---------------- PREDICTION FUNCTION ---------------- #
def pred(Gender, Age, Height, Weight, Duration, Heart_rate, Body_temp):
    features = np.array([[Gender, Age, Height, Weight, Duration, Heart_rate, Body_temp]])
    return rfr.predict(features)[0]

# ---------------- TITLE ---------------- #
st.markdown("<h1>Calorie Burn Predictor</h1>", unsafe_allow_html=True)

# ---------------- INPUTS ---------------- #
st.subheader("Enter Your Details")

col1, col2, col3 = st.columns(3)

with col1:
    Gender = st.selectbox("Gender", ["Male", "Female"])
    Age = st.number_input("Age", min_value=1, max_value=120, step=1)

with col2:
    Height = st.number_input("Height (cm)", min_value=50, max_value=250, step=1)
    Weight = st.number_input("Weight (kg)", min_value=20, max_value=200, step=1)

with col3:
    Duration = st.number_input("Duration (min)", min_value=1, step=1)
    Heart_rate = st.number_input("Heart Rate", min_value=40, max_value=200, value=70)

Body_temp = st.number_input("Body Temperature (°C)", min_value=28.0, max_value=42.0, value=36.5)

Gender = 1 if Gender == "Male" else 0

# ---------------- PREDICTION BUTTON ---------------- #
if st.button("Predict"):
    cal = pred(Gender, Age, Height, Weight, Duration, Heart_rate, Body_temp)
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
            Estimated Calories Burned: {int(cal)} kcal
        </div>
    """, unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
st.sidebar.header("How This Works")
st.sidebar.write("""
This tool predicts calorie burn using:
- Age
- Gender
- Height
- Weight
- Exercise Duration
- Heart Rate
- Body Temperature
""")

st.sidebar.header("Note")
st.sidebar.write("This is a prediction tool and should not replace medical advice.")


