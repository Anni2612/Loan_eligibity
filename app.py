import streamlit as st
import pandas as pd
import joblib

# Load model and threshold
model = joblib.load("xgboost_loan_model.pkl")
with open("best_threshold.txt", "r") as f:
    threshold = float(f.read().strip().split(":")[-1])

# Input options
def preprocess_input(data):
    df = pd.DataFrame([data])
    df['Dependents'] = df['Dependents'].replace('3+', '3').astype(int)
    map_dict = {
        'Gender': {'Male': 1, 'Female': 0},
        'Married': {'Yes': 1, 'No': 0},
        'Education': {'Graduate': 1, 'Not Graduate': 0},
        'Self_Employed': {'Yes': 1, 'No': 0},
        'Property_Area': {'Urban': 2, 'Semiurban': 1, 'Rural': 0}
    }
    for col, mapping in map_dict.items():
        df[col] = df[col].map(mapping)
    return df

# UI
st.title("🏦 Loan Eligibility Prediction")
st.write("Enter your loan application details:")

gender = st.selectbox("Gender", ["Male", "Female"])
married = st.selectbox("Married", ["Yes", "No"])
dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
education = st.selectbox("Education", ["Graduate", "Not Graduate"])
self_employed = st.selectbox("Self Employed", ["Yes", "No"])
income = st.number_input("Applicant Income", min_value=0)
co_income = st.number_input("Coapplicant Income", min_value=0)
loan_amount = st.number_input("Loan Amount (in thousands)", min_value=0)
loan_term = st.selectbox("Loan Term (months)", [360, 180, 120, 60])
credit_history = st.selectbox("Credit History", ["1", "0"])
property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

if st.button("Predict"):
    input_data = {
        'Gender': gender,
        'Married': married,
        'Dependents': dependents,
        'Education': education,
        'Self_Employed': self_employed,
        'ApplicantIncome': income,
        'CoapplicantIncome': co_income,
        'LoanAmount': loan_amount,
        'Loan_Amount_Term': loan_term,
        'Credit_History': float(credit_history),
        'Property_Area': property_area
    }

    processed = preprocess_input(input_data)
    prob = model.predict_proba(processed)[0][1]
    pred = int(prob >= threshold)

    st.markdown(f"### 🧮 Approval Probability: **{prob:.2%}**")
    st.success("✅ Loan Approved!") if pred == 1 else st.error("❌ Loan Rejected")