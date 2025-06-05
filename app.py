import streamlit as st
import pandas as pd
import joblib
import requests
from streamlit_lottie import st_lottie

# --- Helper to load Lottie animations ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        return None
    except:
        return None

# Load the trained model
model = joblib.load("xgboost_loan_model.pkl")
with open("best_threshold.txt", "r") as f:
    threshold = float(f.read().strip().split(":")[-1])

# Load animations
lottie_intro = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_totrpclr.json")
lottie_approved = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_jbrw3hcz.json")
lottie_rejected = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_qp1q7mct.json")

# App layout
st.set_page_config(page_title="Loan Eligibility Predictor", page_icon="🏦", layout="centered")

st.title(":bank: Loan Eligibility Predictor")
st.markdown("""
Use this friendly AI-powered tool to find out your chances of getting a loan approved. 
Just fill in your details and click 'Check Eligibility'!
""")

if lottie_intro:
    st_lottie(lottie_intro, height=200)
else:
    st.info(":information_source: Animation failed to load. Continue with the form below.")

st.header(":clipboard: Application Details")

# --- User input form ---
with st.form("loan_form"):
    col1, col2 = st.columns(2)

    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"], help="Select your gender")
        married = st.selectbox("Married", ["Yes", "No"], help="Are you married?")
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"], help="Number of dependents")
        education = st.selectbox("Education", ["Graduate", "Not Graduate"], help="Your highest qualification")
        self_employed = st.selectbox("Self Employed", ["Yes", "No"], help="Are you self-employed?")
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"], help="Your residential area")

    with col2:
        applicant_income = st.number_input("Applicant Income (monthly)", min_value=0.0, step=100.0)
        coapplicant_income = st.number_input("Coapplicant Income (monthly)", min_value=0.0, step=100.0)
        loan_amount = st.number_input("Loan Amount (in thousands)", min_value=10.0, step=10.0)
        loan_term = st.selectbox("Loan Term (in months)", [360, 180, 120, 60], help="Total loan duration")
        credit_history = st.selectbox("Credit History", [1.0, 0.0], help="1: Good credit history, 0: Poor")

    submitted = st.form_submit_button(":mag: Check Eligibility")

# --- Prediction logic ---
if submitted:
    # Create DataFrame
    user_input = pd.DataFrame([{
        "Gender": gender,
        "Married": married,
        "Dependents": dependents,
        "Education": education,
        "Self_Employed": self_employed,
        "ApplicantIncome": applicant_income,
        "CoapplicantIncome": coapplicant_income,
        "LoanAmount": loan_amount,
        "Loan_Amount_Term": loan_term,
        "Credit_History": credit_history,
        "Property_Area": property_area
    }])

    # Preprocess input
    user_input["Dependents"] = user_input["Dependents"].replace("3+", "3").astype(int)
    label_map = {
        'Gender': {'Male': 1, 'Female': 0},
        'Married': {'Yes': 1, 'No': 0},
        'Education': {'Graduate': 1, 'Not Graduate': 0},
        'Self_Employed': {'Yes': 1, 'No': 0},
        'Property_Area': {'Urban': 2, 'Semiurban': 1, 'Rural': 0}
    }
    for col, mapping in label_map.items():
        user_input[col] = user_input[col].map(mapping)

    # Make prediction
    prob = model.predict_proba(user_input)[0][1]
    pred = int(prob >= threshold)

    # Show result
    st.subheader(":abacus: Prediction Result")
    st.write(f"**Approval Probability:** {prob:.2%}")

    if pred == 1:
        st.success("\u2705 Your loan is likely to be approved!")
        if lottie_approved:
            st_lottie(lottie_approved, height=250)
    else:
        st.error("\u274c Sorry, your loan is likely to be rejected.")
        if lottie_rejected:
            st_lottie(lottie_rejected, height=250)
