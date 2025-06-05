 #Insights.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="📊 Insights | Loan App", layout="wide")

st.title("📊 Data & Model Insights")

st.markdown("""
Explore key patterns in the dataset that influenced the model's decisions.

""")

# Load data
train = pd.read_csv("train_u6lujuX_CVtuZ9i.csv")

# Basic stats
st.subheader("Overview")
st.write(train.describe())

# Target variable count
st.subheader("Loan Status Distribution")
fig, ax = plt.subplots()
sns.countplot(x='Loan_Status', data=train, ax=ax)
st.pyplot(fig)

# Income vs Loan Status
st.subheader("Income vs Loan Approval")
fig, ax = plt.subplots()
sns.boxplot(x='Loan_Status', y='ApplicantIncome', data=train, ax=ax)
st.pyplot(fig)

# Credit History Impact
st.subheader("Credit History vs Loan Approval")
fig, ax = plt.subplots()
sns.countplot(x='Credit_History', hue='Loan_Status', data=train, ax=ax)
st.pyplot(fig)