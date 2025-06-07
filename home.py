


import os
os.system("pip install streamlit-lottie")
import streamlit as st
from streamlit_lottie import st_lottie
import requests
import pandas as pd
import joblib
from io import BytesIO
from fpdf import FPDF

# Page Config
st.set_page_config(page_title="Loan Advisor", page_icon="\U0001F3E0", layout="wide")

# Load Lottie Animations
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
lottie_rejected = load_lottieurl("https://lottie.host/2bb97f59-47f6-44b4-84c8-39fef1e5ceee/G01Uq6Qm8i.json")
lottie_predictor = load_lottieurl("https://lottie.host/d53f26dc-9c8d-45a1-8d0a-f321eb007185/390SpfPpMv.json")

# Style
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');
    html, body {
        font-family: 'Poppins', sans-serif;
        background: #ffffff;
        color: #222222;
    }
    .main { padding: 2rem; }
    footer { visibility: hidden; }
    .custom-footer {
        text-align: center;
        padding: 1rem;
        font-size: 0.8rem;
        color: #aaa;
        background-color: #111;
        border-top: 1px solid #333;
    }
    .banner-text {
        text-align: center;
        padding: 3rem 1rem;
        background: linear-gradient(to right, #004e92, #000428);
        color: #fff;
        font-size: 3rem;
        font-weight: 700;
        border-radius: 10px;
        box-shadow: 0 0 20px rgba(0,0,0,0.2);
        margin-bottom: 3rem;
    }
    </style>
""", unsafe_allow_html=True)

# Banner
st.markdown('<div class="banner-text">Smarter Loan Decisions, Powered by AI.</div>', unsafe_allow_html=True)

# --- Description Section ---
st.markdown("###  Why We Built This App")
st.markdown("""
Applying for a loan is more than a transaction — it’s a step toward building a home, pursuing an education, or growing a dream.
But for many, it becomes a confusing process filled with jargon, unpredictable outcomes, and silent rejections.
**We built this tool to change that.**
""")

st.markdown("### What This App Does")
st.markdown("""
At its core, this app is powered by a finely tuned **XGBoost AI model** trained on real-world banking patterns.
Input your financial and personal details, and it predicts your loan approval chances instantly.
""")

st.markdown("###  Your Privacy, Respected")
st.markdown("""
This tool runs entirely within your session and is absoulutely free:
- No data is stored
- No information is shared
- No user login is required
""")

st.markdown("### 🧞‍♂️ What is CrediGenie?")
st.markdown("""
CrediGenie is your smart, AI-powered assistant that helps you check your loan eligibility in seconds. Whether you're planning to buy a home, a car, or fund your education, it analyzes your input and predicts your chances instantly, securely, and without needing a login.
""")

st.markdown("### 📋 How to Use")
st.markdown("""
1. Fill in your personal and financial details  
2. Select your loan purpose  
3. Click **'Predict'** to see your eligibility result  
4. Review suggestions to understand your loan status
""")

st.markdown("### ⚠️ Disclaimer", unsafe_allow_html=True)
st.markdown("""
**CrediGenie provides predictions based on data models and helps you to make financial decision.**  
Please consult a certified financial advisor before making major financial decisions.
""", unsafe_allow_html=True)
if lottie_predictor:
    st_lottie(lottie_predictor, height=230, speed=1)

with st.form("loan_form"):
    st.markdown("### ✍️ Fill Your Details Below")
    col1, col2 = st.columns([1, 1])

    with col1:
        st.caption("🔹 Select your gender as mentioned in official documents.")
        gender = st.selectbox("Gender", ["Male", "Female"], key="gender")

        st.caption("🔹 'Yes' if you are legally married; affects financial responsibility evaluation.")
        married = st.selectbox("Married", ["Yes", "No"], key="married")

        st.caption("🔹 Number of dependents in your household (children, elders).")
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"], key="dependents")

        st.caption("🔹 'Graduate' if you have a university degree; can influence creditworthiness.")
        education = st.selectbox("Education", ["Graduate", "Not Graduate"], key="education")

        st.caption("🔹 'Yes' if you run your own business or freelance full-time.")
        self_employed = st.selectbox("Self Employed", ["Yes", "No"], key="self_employed")

        st.caption("🔹 Your residential area can affect loan approval trends.")
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"], key="property_area")

    with col2:
        st.caption("🔹 Your monthly income before tax deductions.")
        applicant_income = st.number_input("Applicant Income ($)", min_value=0.0, key="applicant_income")

        st.caption("🔹 Co-applicant's income, if any (leave 0 if none).")
        coapplicant_income = st.number_input("Coapplicant Income ($)", min_value=0.0, key="coapplicant_income")

        st.caption("🔹 Total loan amount you're applying for, in thousands.")
        loan_amount = st.number_input("Loan Amount ($ thousands)", min_value=10.0, key="loan_amount")

        st.caption("🔹 Loan duration in months.")
        loan_term = st.selectbox("Loan Term (months)", [360, 180, 120, 60], key="loan_term")

        st.caption("🔹 **1.0** = Good credit history (no defaults), **0.0** = Poor or no credit history (defaults or first-time applicant).")
        credit_history = st.selectbox("Credit History", [1.0, 0.0], key="credit_history")

        st.caption("🔹 Purpose for which you are applying the loan.")
        purpose = st.radio("Loan Purpose", ["Home", "Car", "Education", "Other"], key="loan_purpose")

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
        "Property_Area": property_area,
        "Purpose": purpose
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

    prob = model.predict_proba(df.drop("Purpose", axis=1))[0][1]
    pred = int(prob >= threshold)

    with st.expander("\U0001F9FE Your Loan Application Summary", expanded=True):
        st.write(df)
        if st.button("\U0001F4C4 Download Summary Report"):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(200, 10, txt="Loan Prediction Summary", ln=True, align='C')
            for col in df.columns:
                pdf.cell(200, 10, txt=f"{col}: {df[col].values[0]}", ln=True)
            pdf.cell(200, 10, txt=f"Prediction: {'Approved ✅' if pred else 'Rejected ❌'}", ln=True)
            pdf.cell(200, 10, txt=f"Probability: {prob:.2%}", ln=True)
            buffer = BytesIO()
            pdf.output(buffer)
            st.download_button("⬇️ Get PDF Report", buffer.getvalue(), file_name="LoanReport.pdf", mime="application/pdf")

    st.markdown("### CrediGenie  Insight")
    if pred == 1:
        st.success("✅ Your loan application is likely to be Approved")
        if lottie_approved:
            st_lottie(lottie_approved, height=250)
    else:
        st.error("❌ Your loan application is likely to be Rejected")
        if lottie_rejected:
            st_lottie(lottie_rejected, height=250)
        st.warning("\U0001F4A1 Consider applying for a smaller amount, or increasing tenure.")
        st.warning("\U0001F4A1  Build a credit history or consult a credit counselor before applying.")
        st.warning("\U0001F4A1  Consider increasing your income or including a co-applicant for better eligibility..")

# Loan Calculator
st.markdown("---")
st.header("\U0001F9EE Loan Repayment Calculator")
amount = st.number_input("Loan Amount ($)", value=300000, step=1000)
rate = st.number_input("Annual Interest Rate (%)", value=6.5, step=0.1)
years = st.slider("Loan Term (Years)", 1, 30, 20)

monthly_rate = rate / 100 / 12
months = years * 12
if monthly_rate > 0:
    payment = amount * monthly_rate / (1 - (1 + monthly_rate) ** -months)
else:
    payment = amount / months
st.success(f" Monthly Payment Estimate: **${payment:,.2f}**")

# FAQ
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

st.markdown("""
    <style>
    /* Remove extra margin/padding from Streamlit's default body */
    .block-container {
        padding-bottom: 0rem !important;
        margin-bottom: 0rem !important;
    }

    body {
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Ensure footer hugs the bottom */
    .custom-footer-banner {
        margin-bottom: 0 !important;
        text-align: center;
        padding: 1rem;
        font-size: 0.85rem;
        color: #aaa;
        background-color: #000;
        border-top: 1px solid #333;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(0,0,0,0.2);
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("""
    <style>
        .custom-footer-banner {
            text-align: center;
            padding: 1rem;
            font-size: 0.9rem;
            color: #6c757d;
        }
        .footer-links a {
            margin: 0 8px;
            color: #4c8bf5;
            text-decoration: none;
        }
        .footer-links a:hover {
            text-decoration: underline;
        }
    </style>
    
    <div class="custom-footer-banner">
        © 2025 | Your Smart Loan Advisor · Built with 💻 & ❤️ by Animesh <br>
        <div class="footer-links">
            🔗 
            <a href="https://github.com/Anni2612" target="_blank">GitHub</a> |
            <a href="https://linkedin.com/in/animesh-d-525826104" target="_blank">LinkedIn</a> |
            <a href="https://animesh.fyi" target="_blank">Portfolio</a>
        </div>
    </div>
""", unsafe_allow_html=True)
