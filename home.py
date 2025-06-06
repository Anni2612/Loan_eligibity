



# import streamlit as st
# from streamlit_lottie import st_lottie
# import requests
# import pandas as pd
# import joblib
# from io import BytesIO
# from fpdf import FPDF

# # Page Config
# st.set_page_config(page_title="🏠 Loan Advisor", page_icon="🏠", layout="wide")

# # Load Lottie Animations
# def load_lottieurl(url):
#     try:
#         r = requests.get(url)
#         if r.status_code == 200:
#             return r.json()
#         return None
#     except:
#         return None

# chatbot_animation = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_1pxqjqps.json")
# lottie_approved = load_lottieurl("https://assets1.lottiefiles.com/packages/lf20_jbrw3hcz.json")
# lottie_rejected = load_lottieurl("https://lottie.host/2bb97f59-47f6-44b4-84c8-39fef1e5ceee/G01Uq6Qm8i.json")

# # Style
# st.markdown("""
#     <style>
#     @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&display=swap');

#     html, body {
#         font-family: 'Poppins', sans-serif;
#         background: #ffffff;
#         color: #222222;
#     }
#     .main { padding: 2rem; }
#     footer { visibility: hidden; }

#     .custom-footer {
#         text-align: center;
#         padding: 1rem;
#         font-size: 0.8rem;
#         color: #aaa;
#         background-color: #111;
#         border-top: 1px solid #333;
#     }

#     .banner-text {
#         text-align: center;
#         padding: 3rem 1rem;
#         background: linear-gradient(to right, #004e92, #000428);
#         color: #fff;
#         font-size: 3rem;
#         font-weight: 700;
#         border-radius: 10px;
#         box-shadow: 0 0 20px rgba(0,0,0,0.2);
#         margin-bottom: 3rem;
#     }
#     </style>
# """, unsafe_allow_html=True)

# # Banner
# st.markdown('<div class="banner-text">🧠 Smarter Loan Decisions, Powered by AI.</div>', unsafe_allow_html=True)

# # --- Description Section ---
# st.markdown("### 🧠 Why We Built This App")
# st.markdown("""
# Applying for a loan is more than a transaction — it’s a step toward building a home, pursuing an education, or growing a dream.  
# But for many, it becomes a confusing process filled with jargon, unpredictable outcomes, and silent rejections.

# **We built this tool to change that.**

# "Your Smart Loan Advisor" is designed to bring **transparency, confidence, and clarity** to your loan journey — before you even apply.
# """)

# st.markdown("### 🔍 What This App Does")
# st.markdown("""
# At its core, this app is powered by a finely tuned **XGBoost AI model** trained on real-world banking patterns.  
# You simply input your financial and personal details, and it instantly predicts your likelihood of loan approval — just like a digital pre-check.

# Here’s what makes it helpful:

# - 📈 **Instant Eligibility Predictions** – Know your approval chances in seconds  
# - 🧾 **Application Insights** – Understand which features affect your outcome  
# - 📚 **Helpful Recommendations** – Get simple tips to improve your chances  
# """)

# st.markdown("### 🔐 Your Privacy, Respected")
# st.markdown("""
# This tool runs entirely within your session. That means:

# - No data is stored  
# - No information is shared  
# - No user login is required  

# We value your trust — your inputs are used for prediction only, and everything stays on your device.
# """)

# st.markdown("### 🚀 Built with AI, Designed for You")
# st.markdown("""
# From a student applying for an education loan to a family buying their first home —  
# this app is meant for anyone who wants a **stress-free, intelligent start** to their loan journey.

# With a beautiful interface, fast predictions, and no learning curve, it acts as your personal eligibility guide in real-time.
# """)

# # Predictor Section
# st.markdown('<h4 style="margin-bottom: 1rem;">📋 Loan Eligibility Predictor</h4>', unsafe_allow_html=True)

# # Load predictor animation
# lottie_predictor = load_lottieurl("https://lottie.host/d53f26dc-9c8d-45a1-8d0a-f321eb007185/390SpfPpMv.json")

# # Display animation right after the title
# if lottie_predictor:
#     st_lottie(lottie_predictor, height=230, speed=1)

# # Loan Form
# with st.form("loan_form"):
#     st.markdown("### ✍️ Fill Your Details Below")
#     col1, col2 = st.columns([1, 1])

#     with col1:
#         gender = st.selectbox("Gender", ["Male", "Female"])
#         married = st.selectbox("Married", ["Yes", "No"])
#         dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
#         education = st.selectbox("Education", ["Graduate", "Not Graduate"])
#         self_employed = st.selectbox("Self Employed", ["Yes", "No"])
#         property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])

#     with col2:
#         applicant_income = st.number_input("Applicant Income (₹)", min_value=0.0)
#         coapplicant_income = st.number_input("Coapplicant Income (₹)", min_value=0.0)
#         loan_amount = st.number_input("Loan Amount (₹ thousands)", min_value=10.0)
#         loan_term = st.selectbox("Loan Term (months)", [360, 180, 120, 60])
#         credit_history = st.selectbox("Credit History", [1.0, 0.0])
#         purpose = st.radio("Loan Purpose", ["Home", "Car", "Education", "Other"])

#     submitted = st.form_submit_button("🔍 Predict")

# if submitted:
#     df = pd.DataFrame([{ 
#         "Gender": gender,
#         "Married": married,
#         "Dependents": dependents,
#         "Education": education,
#         "Self_Employed": self_employed,
#         "ApplicantIncome": applicant_income,
#         "CoapplicantIncome": coapplicant_income,
#         "LoanAmount": loan_amount,
#         "Loan_Amount_Term": loan_term,
#         "Credit_History": credit_history,
#         "Property_Area": property_area,
#         "Purpose": purpose
#     }])

#     df["Dependents"] = df["Dependents"].replace("3+", "3").astype(int)
#     label_map = {
#         'Gender': {'Male': 1, 'Female': 0},
#         'Married': {'Yes': 1, 'No': 0},
#         'Education': {'Graduate': 1, 'Not Graduate': 0},
#         'Self_Employed': {'Yes': 1, 'No': 0},
#         'Property_Area': {'Urban': 2, 'Semiurban': 1, 'Rural': 0}
#     }
#     for col, mapping in label_map.items():
#         df[col] = df[col].map(mapping)

#     model = joblib.load("xgboost_loan_model.pkl")
#     with open("best_threshold.txt", "r") as f:
#         threshold = float(f.read().strip().split(":")[-1])

#     prob = model.predict_proba(df.drop("Purpose", axis=1))[0][1]
#     pred = int(prob >= threshold)

#     with st.expander("🧾 Your Loan Application Summary", expanded=True):
#         st.write(df)

#     st.markdown("### 🧠 AI Insight")
#     if pred == 1:
#         st.success("✅ Your loan is likely to be Approved")
#         if lottie_approved:
#             st_lottie(lottie_approved, height=250)
#     else:
#         st.error("❌ Your loan is likely to be Rejected")
#         if lottie_rejected:
#             st_lottie(lottie_rejected, height=250)
#         st.warning("💡 Consider applying for a smaller amount, or increasing tenure.")

#     if st.button("📄 Download Summary Report"):
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.set_font("Arial", size=12)
#         pdf.cell(200, 10, txt="Loan Prediction Summary", ln=True, align='C')
#         for col in df.columns:
#             pdf.cell(200, 10, txt=f"{col}: {df[col].values[0]}", ln=True)
#         pdf.cell(200, 10, txt=f"Prediction: {'Approved ✅' if pred else 'Rejected ❌'}", ln=True)
#         pdf.cell(200, 10, txt=f"Probability: {prob:.2%}", ln=True)
#         buffer = BytesIO()
#         pdf.output(buffer)
#         st.download_button("⬇️ Get PDF Report", buffer.getvalue(), file_name="LoanReport.pdf", mime="application/pdf")


# # Loan Calculator
# st.markdown("---")
# st.header("🧮 Loan Repayment Calculator")
# amount = st.number_input("Loan Amount ($)", value=300000, step=1000)
# rate = st.number_input("Annual Interest Rate (%)", value=6.5, step=0.1)
# years = st.slider("Loan Term (Years)", 1, 30, 20)

# monthly_rate = rate / 100 / 12
# months = years * 12
# if monthly_rate > 0:
#     payment = amount * monthly_rate / (1 - (1 + monthly_rate) ** -months)
# else:
#     payment = amount / months
# st.success(f"💵 Monthly Payment Estimate: **${payment:,.2f}**")

# # FAQ
# st.markdown("---")
# st.header("❓ Frequently Asked Questions")

# with st.expander("How can I improve my loan approval chances?"):
#     st.markdown("""
#     - Keep a strong credit score  
#     - Submit all documents  
#     - Declare consistent income  
#     - Avoid multiple loan requests
#     """)

# with st.expander("What affects my monthly repayment?"):
#     st.markdown("""
#     - Loan amount  
#     - Interest rate  
#     - Tenure  
#     - Type of interest: Fixed or variable
#     """)

# with st.expander("What is LVR (Loan-to-Value Ratio)?"):
#     st.markdown("""
#     LVR = Loan Amount ÷ Property Value  
#     Lower LVR (typically <80%) increases approval chances.
#     """)

# with st.expander("Do you store my information?"):
#     st.markdown("No. This app runs locally and does not store any data.")
# # --- Footer ---
# st.markdown("""
#     <div class="custom-footer">
#         © 2025 | Your Smart Loan Advisor · Built with 💻 & ❤️ by Animesh
#     </div>
# """, unsafe_allow_html=True)












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
st.set_page_config(page_title="\U0001F3E0 Loan Advisor", page_icon="\U0001F3E0", layout="wide")

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
st.markdown('<div class="banner-text">\U0001F9E0 Smarter Loan Decisions, Powered by AI.</div>', unsafe_allow_html=True)

# --- Description Section ---
st.markdown("### \U0001F9E0 Why We Built This App")
st.markdown("""
Applying for a loan is more than a transaction — it’s a step toward building a home, pursuing an education, or growing a dream.
But for many, it becomes a confusing process filled with jargon, unpredictable outcomes, and silent rejections.
**We built this tool to change that.**
""")

st.markdown("### \U0001F50D What This App Does")
st.markdown("""
At its core, this app is powered by a finely tuned **XGBoost AI model** trained on real-world banking patterns.
Input your financial and personal details, and it predicts your loan approval chances instantly.
""")

st.markdown("### \U0001F512 Your Privacy, Respected")
st.markdown("""
This tool runs entirely within your session:
- No data is stored
- No information is shared
- No user login is required
""")

# Predictor Section
st.markdown('<h4 style="margin-bottom: 1rem;">\U0001F4CB Loan Eligibility Predictor</h4>', unsafe_allow_html=True)
if lottie_predictor:
    st_lottie(lottie_predictor, height=230, speed=1)

with st.form("loan_form"):
    st.markdown("### ✍️ Fill Your Details Below")
    col1, col2 = st.columns([1, 1])
    with col1:
        gender = st.selectbox("Gender", ["Male", "Female"])
        married = st.selectbox("Married", ["Yes", "No"])
        dependents = st.selectbox("Dependents", ["0", "1", "2", "3+"])
        education = st.selectbox("Education", ["Graduate", "Not Graduate"])
        self_employed = st.selectbox("Self Employed", ["Yes", "No"])
        property_area = st.selectbox("Property Area", ["Urban", "Semiurban", "Rural"])
    with col2:
        applicant_income = st.number_input("Applicant Income (₹)", min_value=0.0)
        coapplicant_income = st.number_input("Coapplicant Income (₹)", min_value=0.0)
        loan_amount = st.number_input("Loan Amount (₹ thousands)", min_value=10.0)
        loan_term = st.selectbox("Loan Term (months)", [360, 180, 120, 60])
        credit_history = st.selectbox("Credit History", [1.0, 0.0])
        purpose = st.radio("Loan Purpose", ["Home", "Car", "Education", "Other"])
    submitted = st.form_submit_button("\U0001F50D Predict")

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

    st.markdown("### \U0001F9E0 AI Insight")
    if pred == 1:
        st.success("✅ Your loan is likely to be Approved")
        if lottie_approved:
            st_lottie(lottie_approved, height=250)
    else:
        st.error("❌ Your loan is likely to be Rejected")
        if lottie_rejected:
            st_lottie(lottie_rejected, height=250)
        st.warning("\U0001F4A1 Consider applying for a smaller amount, or increasing tenure.")

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
st.success(f"\U0001F4B5 Monthly Payment Estimate: **${payment:,.2f}**")

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
    <div class="custom-footer-banner">
        © 2025 | Your Smart Loan Advisor · Built with 💻 & ❤️ by Animesh
    </div>
""", unsafe_allow_html=True)
