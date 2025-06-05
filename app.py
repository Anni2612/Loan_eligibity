import streamlit as st
from streamlit_lottie import st_lottie
import requests

# Load animation
def load_lottieurl(url):
    try:
        r = requests.get(url)
        if r.status_code == 200:
            return r.json()
    except:
        return None


lottie_hello = load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_1pxqjqps.json")

# Page setup
st.set_page_config(page_title="Loan Eligibility App", layout="centered")
st.title("🏠 Welcome to the Loan Eligibility Predictor")

st.markdown("""
This application helps users check their **loan eligibility** using machine learning.

**Problem Statement:**  
Millions of loan applications are rejected due to incomplete evaluation or poor profiling.  
Our model predicts whether your application is likely to be **approved** or **rejected**, enabling better planning.

**How it works:**
- We trained a model on historical data using features like income, credit history, and education.
- We chose **XGBoost** due to its superior performance.
- The model returns the **probability of loan approval**.
""")

if lottie_hello:
    st_lottie(lottie_hello, height=800)

st.markdown("---")
st.subheader("🔍 Navigate using the sidebar:")
st.markdown("""
- 📄 Check your loan eligibility on **Predictor**  
- 📊 Explore data & model performance in **Insights**
""")