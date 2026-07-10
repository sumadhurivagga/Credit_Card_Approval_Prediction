import streamlit as st
import pandas as pd
import joblib
from pathlib import Path

MODEL_PATH = Path(__file__).resolve().parent / "credit_model.pkl"

# 1. Load the saved model pipeline
@st.cache_resource
def load_model():
    if not MODEL_PATH.exists():
        st.error(f"Model file not found: {MODEL_PATH.name}. Place it in the app folder.")
        return None
    return joblib.load(MODEL_PATH)

model = load_model()
if model is None:
    st.stop()

st.title("💳 Credit Card Approval Prediction App")
st.write("Enter the applicant's details below to predict credit card eligibility.")

# 2. Create the input fields matching your model features
col1, col2 = st.columns(2)

with col1:
    gender = st.selectbox("Gender", ["F", "M"])
    own_car = st.selectbox("Owns a Car?", ["N", "Y"])
    own_realty = st.selectbox("Owns Real Estate?", ["N", "Y"])
    income = st.number_input("Total Annual Income ($)", min_value=0, value=50000)
    children = st.number_input("Number of Children", min_value=0, max_value=20, value=0)

with col2:
    income_type = st.selectbox("Income Type", ["Working", "Commercial associate", "Pensioner", "State servant", "Student"])
    education = st.selectbox("Education Level", ["Secondary / secondary special", "Higher education", "Incomplete higher", "Lower secondary", "Academic degree"])
    family_status = st.selectbox("Family Status", ["Married", "Single / not married", "Civil marriage", "Separated", "Widow"])
    housing_type = st.selectbox("Housing Type", ["House / apartment", "With parents", "Municipal apartment", "Rented apartment", "Office apartment", "Co-op apartment"])

st.subheader("Demographics & Employment")
col3, col4 = st.columns(2)

with col3:
    age = st.number_input("Age (Years)", min_value=18, max_value=100, value=30)
    years_employed = st.number_input("Years of Employment", min_value=0.0, max_value=60.0, value=2.0)

with col4:
    family_members = st.number_input("Family Members Size", min_value=1, max_value=20, value=2)
    unemployed = st.selectbox("Currently Unemployed?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")

# Hardcoded flags that your data expects (defaulting to safe values)
flag_mobil = 1
flag_work_phone = st.selectbox("Has a Work Phone?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
flag_phone = st.selectbox("Has a Personal Phone?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
flag_email = st.selectbox("Has an Email?", [0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
occupation_type = "Unknown"

# 3. Predict button
if st.button("Predict Approval Status", type="primary"):
    # Format the input features strictly into a dataframe matching original features
    input_data = pd.DataFrame([{
        'CODE_GENDER': gender,
        'FLAG_OWN_CAR': own_car,
        'FLAG_OWN_REALTY': own_realty,
        'CNT_CHILDREN': children,
        'AMT_INCOME_TOTAL': float(income),
        'NAME_INCOME_TYPE': income_type,
        'NAME_EDUCATION_TYPE': education,
        'NAME_FAMILY_STATUS': family_status,
        'NAME_HOUSING_TYPE': housing_type,
        'FLAG_MOBIL': flag_mobil,
        'FLAG_WORK_PHONE': flag_work_phone,
        'FLAG_PHONE': flag_phone,
        'FLAG_EMAIL': flag_email,
        'OCCUPATION_TYPE': occupation_type,
        'CNT_FAM_MEMBERS': float(family_members),
        'AGE': float(age),
        'UNEMPLOYED': unemployed,
        'YEARS_EMPLOYED': float(years_employed)
    }])
    
    # Run prediction
    prediction = model.predict(input_data)[0]
    
    st.write("---")
    if prediction == 0:
        st.success("🎉 **Approved!** This applicant is predicted to be a **Good/Low-Risk** client.")
    else:
        st.error("❌ **Rejected.** This applicant is predicted to be a **High-Risk/Bad** credit profile.")
