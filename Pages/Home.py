#Home.py
import streamlit as st
from streamlit_lottie import st_lottie
import requests

st.set_page_config(page_title="🏠 Home | Loan App", layout="centered")

# Helper to load animation
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
        return None
    except:
        return None



st.title("🏦 Welcome to the Loan Eligibility Predictor")

st.markdown("""
This application helps users check their **loan eligibility** using machine learning.

**Problem Statement:**
Millions of loan applications are rejected due to incomplete evaluation or poor profiling. Our model uses historical loan data to predict whether your application is likely to be **approved** or **rejected**, allowing better planning.

**How it works:**
- We trained a model using features like income, credit history, and education.
- XGBoost was chosen for its superior performance.
- The model outputs the probability of loan approval.

""")


st.markdown("---")

st.subheader("🔍 Navigate using the sidebar to:")
st.markdown("- 📋 Check your loan eligibility on **Predictor**")
st.markdown("- 📊 See data & model **Insights**")
