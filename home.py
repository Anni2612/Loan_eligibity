import streamlit as st
from streamlit_lottie import st_lottie
import requests
import pandas as pd
import joblib

# --- Page Config ---
st.set_page_config(page_title="🏠 Loan Advisor", page_icon="🏠", layout="wide")

# --- Animation Loader ---
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        return None
    except:
        return None

chatbot_animation = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_1pxqjqps.json")
lottie_approved = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_jbrw3hcz.json")
lottie_rejected = load_lottieurl("https://assets5.lottiefiles.com/packages/lf20_qp1q7mct.json")
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

    html, body {
        font-family: 'Poppins', sans-serif;
        background: linear-gradient(to bottom right, #0f0f0f, #1a1a1a);
        color: #f0f0f0;
        margin: 0;
        padding: 0;
    }

    .main {
        background: transparent;
        padding: 2rem;
    }

    footer {visibility: hidden;}

    .custom-footer {
        text-align: center;
        padding: 1rem;
        font-size: 0.8rem;
        color: #aaa;
        background-color: #111;
        border-top: 1px solid #333;
        position: relative;
        bottom: 0;
        width: 100%;
        margin: 0;
    }

    .block-container {
        padding-bottom: 0 !important;
    }

    .banner-text {
        text-align: center;
        padding: 3rem 1rem;
        background: linear-gradient(to right, #222, #333, #222);
        color: #fff;
        font-size: 3rem;
        font-weight: 700;
        border-radius: 10px;
        box-shadow: 0 0 20px rgba(255,255,255,0.1);
        margin-bottom: 3rem;
    }
    </style>
""", unsafe_allow_html=True)

# --- Banner ---
st.markdown('<div class="banner-text">🧠 Smarter Loan Decisions, Powered by AI.</div>', unsafe_allow_html=True)

# --- Description ---
st.markdown("## 🏠 Welcome to Your Smart Loan Advisor")
st.markdown("""
💬 *"I wasn’t sure if I’d get approved for a home loan, but this app helped me find out in seconds!"*  
> — A real user navigating uncertainty with AI support.
""")

st.markdown("### 🤔 The Problem Many Face")
st.markdown("""
Thousands of applicants face silent loan rejections due to unclear eligibility or missing data.  
Most don’t know where they stand — leaving them anxious and unprepared.
""")

st.markdown("### 💡 The Solution")
st.markdown("""
**Your Smart Loan Advisor** uses machine learning to give you a personal eligibility estimate before you even apply.  
Built on **XGBoost** and real banking data.
""")

st.markdown("### 🔧 What This App Does")
st.markdown("""
- ✅ Predict approval probability instantly  
- 📊 Visual insights on your application  
- 📘 Loan education & improvement tips  
- 🔐 Privacy-first (data not stored)
""")

# --- Predictor ---
st.markdown("---")
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

    model = joblib.load("xgboost_loan_model.pkl")
    with open("best_threshold.txt", "r") as f:
        threshold = float(f.read().strip().split(":")[-1])

    prob = model.predict_proba(df)[0][1]
    pred = int(prob >= threshold)

    st.subheader("📊 Result")
    st.write(f"**Approval Probability:** {prob:.2%}")
    if pred == 1:
        st.success("✅ Your loan is likely to be Approved")
        if lottie_approved:
            st_lottie(lottie_approved, height=250)
    else:
        st.error("❌ Your loan is likely to be Rejected")
        if lottie_rejected:
            st_lottie(lottie_rejected, height=250)

# --- Loan Calculator ---
st.markdown("---")
st.header("🧮 Quick Loan Repayment Estimator")

amount = st.number_input("Loan Amount ($)", value=300000, step=1000)
rate = st.number_input("Annual Interest Rate (%)", value=6.5, step=0.1)
years = st.slider("Loan Term (Years)", 1, 30, 20)

monthly_rate = rate / 100 / 12
months = years * 12

if monthly_rate > 0:
    payment = amount * monthly_rate / (1 - (1 + monthly_rate) ** -months)
else:
    payment = amount / months

st.success(f"💵 Monthly Payment Estimate: **${payment:,.2f}**")

# --- FAQ Section ---
st.markdown("---")
st.header("❓ Frequently Asked Questions")

with st.expander("How can I improve my loan approval chances?"):
    st.markdown("""
    - Keep a strong credit score  
    - Submit all documents  
    - Declare consistent income  
    - Avoid multiple loan requests  
    """)

with st.expander("What affects my monthly repayment?"):
    st.markdown("""
    - Loan amount  
    - Interest rate  
    - Tenure  
    - Type of interest: Fixed or variable
    """)

with st.expander("What is LVR (Loan-to-Value Ratio)?"):
    st.markdown("""
    LVR = Loan Amount ÷ Property Value  
    Lower LVR (typically <80%) increases approval chances.
    """)

with st.expander("Do you store my information?"):
    st.markdown("No. This app runs locally and does not store any data.")

# --- Footer ---
st.markdown("""
    <div class="custom-footer">
        © 2025 | Your Smart Loan Advisor · Built with 💻 & ❤️ by Animesh
    </div>
""", unsafe_allow_html=True)