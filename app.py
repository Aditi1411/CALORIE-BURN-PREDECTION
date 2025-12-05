import streamlit as st
import numpy as np
import pickle

# ---------------- PAGE SETTINGS ---------------- #
st.set_page_config(
    page_title="Calorie Burn Predictor",
    layout="wide"
)

# ---------------- STYLE ---------------- #
st.markdown("""
<style>

    /* Reduce spacing under input fields */
    .css-1y4p8pa, .css-q8sbsg, .stNumberInput, .stSelectbox {
        margin-bottom: -10px !important;
    }

    /* Button Style */
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

    /* Hover — text stays white */
    .stButton>button:hover {
        background-color: #FF9F9F !important;
        color: white !important;
    }

    /* Active (clicked) — text stays white */
    .stButton>button:active {
        background-color: #FF9F9F !important;
        color: white !important;
    }

    /* Title Color */
    h1 {
        color: #FF6B6B !important;
    }

</style>
""", unsafe_allow_html=True)

# ---------------- LOAD MODEL ---------------- #
rfr = pickle.load(open("rfr.pkl", "rb"))

# ---------------- PREDICTION FUNCTION ---------------- #
def pred(Gender, Age, Height, Weight, Duration, Heart_rate, Body_temp):
    features = np.array([[Gender, Age, Height, Weight, Duration, Heart_rate, Body_temp]])
    return rfr.predict(features)[0]

# ---------------- TITLE ---------------- #
st.markdown("<h1>Calorie Burn Predictor</h1>", unsafe_allow_html=True)

st.write("")

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

# Convert Gender to numerical
Gender = 1 if Gender == "Male" else 0

# ---------------- PREDICTION BUTTON ---------------- #
st.write("")
if st.button("Predict"):
    cal = pred(Gender, Age, Height, Weight, Duration, Heart_rate, Body_temp)
    cal_int = int(cal)

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
            Estimated Calories Burned: {cal_int} kcal
        </div>
    """, unsafe_allow_html=True)

# ---------------- SIDEBAR ---------------- #
st.sidebar.header("How This Works")
st.sidebar.write("""
This tool predicts calorie burn using a machine learning model trained on:

- Age  
- Gender  
- Height  
- Weight  
- Exercise Duration  
- Heart Rate  
- Body Temperature  
""")

st.sidebar.header("Tips to Burn More Calories")
st.sidebar.write("""
- Increase workout intensity gradually.  
- Add cardio: running, cycling, skipping.  
- Strength training boosts metabolism.  
- Keep heart rate elevated during workout.  
- Maintain consistent workout habits.  
""")

st.sidebar.header("Note")
st.sidebar.write("""
This is a prediction tool and should not replace professional medical or fitness advice.
""")

