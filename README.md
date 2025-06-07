# 🧞‍♂️ CrediGenie: Your Smart Loan Advisor

CrediGenie is an intelligent AI-powered web app that helps users assess their **loan eligibility** with transparency and precision. Designed for simplicity and backed by robust machine learning, CrediGenie empowers users to understand their approval chances before approaching a financial institution.

---

## 🔍 Overview

✅ Predicts loan approval based on financial and demographic inputs  
✅ Offers easy-to-understand advice based on your credit history and loan term  
✅ Built with **Streamlit**, powered by **XGBoost**, and deployed with a responsive UI  
✅ Includes downloadable PDF summaries and educational guidance  

---

## 📊 Dataset & Preprocessing

- **Source**: Loan Prediction dataset inspired by real-world scenarios
- **Missing Values**: Handled using `KNNImputer`
- **Categorical Encoding**: Manual mapping + `LabelEncoder`
- **Feature Engineering**:
  - `Income_Ratio` = ApplicantIncome / LoanAmount
  - `Property_Credit` = Combination of PropertyArea & CreditHistory
  - Additional binary & interaction features for education, employment

---

## ⚙️ Modeling Process

### 🔧 Models Trained:
- Logistic Regression (baseline)
- Decision Tree
- Random Forest
- ✅ **XGBoost** (Best performing)

### 💡 Optimization:
- **Class imbalance** solved using `SMOTE` and `SMOTETomek`
- **Hyperparameter tuning** with `RandomizedSearchCV`
- **Evaluation** with 5-Fold Cross-Validation (stratified)

---

## 📈 Final Model Performance

| Metric            | Value        |
|------------------|--------------|
| ✅ Accuracy        | 83.74%       |
| ✅ Precision       | 86.52%       |
| ✅ Recall          | 90.59%       |
| ✅ F1 Score        | 88.51%       |
| ✅ ROC AUC         | 86.19%       |
| ✅ CV F1 Score     | 82.90% ± 5.65 |

> 📌 **Industry Standard**: 75–80% accuracy  
> 🏆 **CrediGenie Result**: 83.74% accuracy, 88.51% F1  
> 📈 **Improvement**: 8–13% better than typical models

---

## 🖥️ Application Features

- 🔍 Real-time eligibility prediction
- 📄 PDF export of loan application summary
- 🧮 Loan term calculator
- 🧠 Financial literacy tooltips for each input
- ⚠️ Privacy-friendly (no login required)

---

## 🚀 Tech Stack

- **Frontend & App**: Streamlit, HTML/CSS, Lottie
- **Backend & Modeling**: Python, XGBoost, scikit-learn
- **Data Imbalance**: imbalanced-learn (SMOTE)
- **PDF Reports**: FPDF
- **Hosting**: Streamlit Cloud
- **Version Control**: Git + GitHub

---

## 📁 Repository Structure
📦Loan_Eligibility
├── home.py                     # Streamlit app
├── xgboost_loan_model.pkl      # Final trained model
├── best_threshold.txt          # Optimal threshold value
├── requirements.txt            # All dependencies
├── loan_prediction.ipynb       # Model training notebook
├── *.csv                       # Dataset files
└── README.md                   # You’re here!


## 🖥️ App Features

- 🔍 Real-time loan eligibility prediction
- 📄 Exportable loan application summary in PDF
- 💬 Credit tips based on selected values
- 🧠 Tooltips and helper texts for financial clarity
- 🎯 No login or account creation required

---

## 🚀 Tech Stack

- **Frontend**: Streamlit, HTML/CSS, Lottie animations
- **Modeling**: Python, XGBoost, scikit-learn
- **Data Processing**: Pandas, imbalanced-learn
- **PDF Reports**: FPDF
- **Deployment**: Streamlit Cloud (No virtual environment needed)
- **Version Control**: Git + GitHub

---

## 🧾 Deployment Note

This project was deployed **directly to Streamlit Cloud**.  
⚠️ No virtual environment setup is required manually.  
Just push to GitHub → Connect repo on Streamlit → Done!
to run locally clone this repo and add these lines 
python3 -m venv venv
pip install -r requirements.txt
streamlit run home.py

---

## 📬 Connect with Me

🔗 [GitHub](https://github.com/Anni2612)  
🔗 [LinkedIn](https://linkedin.com/in/animesh-d-525826104)  
🔗 [Portfolio](https://animesh.fyi)

---

## 🙌 Acknowledgments

- Machine Learning: [XGBoost](https://xgboost.readthedocs.io/), [scikit-learn](https://scikit-learn.org/)
- UI: [Streamlit](https://streamlit.io/), [LottieFiles](https://lottiefiles.com/)
- Inspiration: Real-world loan pre-screening use cases

---

## 🏁 Final Thoughts

CrediGenie isn't just a model—it's a **decision support assistant** for those navigating loan eligibility. From feature engineering to deployment, this project reflects a deep blend of **technical precision** and **user-first design**.
source venv/bin/activate
