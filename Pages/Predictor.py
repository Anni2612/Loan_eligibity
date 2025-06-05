# Predictor.py
import streamlit as st
import pandas as pd
import joblib
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="📋 Predictor | Loan App", layout="centered")

# Load Lottie animations
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        return None
    except:
        return None

lottie_approved = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_jbrw3hcz.json")
lottie_rejected = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_qp1q7mct.json")

# Load model and threshold
model = joblib.load("xgboost_loan_model.pkl")
with open("best_threshold.txt", "r") as f:
    threshold = float(f.read().strip().split(":")[-1])

st.title("📋 Loan Eligibility Predictor")

with st.form("loan_form"):
    col1, col2 = st.columns(2)
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"], help="Children/elders supported")
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
    with col2:
        applicant_income = st.number_input("Applicant Income (₹)", min_value=0.0)
        coapplicant_income = st.number_input("Coapplicant Income (₹)", min_value=0.0)
        loan_amount = st.number_input("Loan Amount (in ₹ thousands)", min_value=10.0)
        loan_term = st.selectbox("Loan Term (months)", [360, 180, 120, 60])
        credit_history = st.selectbox("Credit History", [1.0, 0.0])
    submitted = st.form_submit_button("🔍 Predict")

if submitted:
    df = pd.DataFrame([{
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

    df["Dependents"] = df["Dependents"].replace("3+", "3").astype(int)
    label_map = {
        'Gender': {'Male': 1, 'Female': 0},
        'Married': {'Yes': 1, 'No': 0},
        'Education': {'Graduate': 1, 'Not Graduate': 0},
        'Self_Employed': {'Yes': 1, 'No': 0},
        'Property_Area': {'Urban': 2, 'Semiurban': 1, 'Rural': 0}
    }
    for col, mapping in label_map.items():
        df[col] = df[col].map(mapping)

    prob = model.predict_proba(df)[0][1]
    pred = int(prob >= threshold)

    st.subheader("Result")
    st.write(f"Approval Probability: **{prob:.2%}**")
    if pred == 1:
        st.success("Loan is likely to be Approved ✅")
        if lottie_approved:
            st_lottie(lottie_approved, height=250)
    else:
        st.error("Loan is likely to be Rejected ❌")
        if lottie_rejected:
            st_lottie(lottie_rejected, height=250)
