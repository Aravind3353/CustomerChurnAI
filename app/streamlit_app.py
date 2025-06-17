# streamlit_app.py

import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load model
model = joblib.load('../models/churn_model.pkl')

st.title("🔍 Customer Churn Prediction App")
st.markdown("Enter customer information below to predict churn:")

# User Inputs
gender = st.selectbox("Gender", ['Female', 'Male'])
SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
Partner = st.selectbox("Has Partner", ['Yes', 'No'])
Dependents = st.selectbox("Has Dependents", ['Yes', 'No'])
tenure = st.slider("Tenure (Months)", 0, 72, 12)
MonthlyCharges = st.number_input("Monthly Charges", 0.0, 200.0, 70.0)
TotalCharges = st.number_input("Total Charges", 0.0, 10000.0, 2000.0)

# Data Preprocessing
data = {
    'tenure': [tenure],
    'MonthlyCharges': [MonthlyCharges],
    'TotalCharges': [TotalCharges],
    'gender_Male': [1 if gender == 'Male' else 0],
    'Partner_Yes': [1 if Partner == 'Yes' else 0],
    'Dependents_Yes': [1 if Dependents == 'Yes' else 0],
    'SeniorCitizen': [SeniorCitizen]
}

# Ensure all features are included
X_input = pd.DataFrame(data)

# Fill missing model features with 0
model_features = model.get_booster().feature_names
for col in model_features:
    if col not in X_input.columns:
        X_input[col] = 0

# Reorder columns to match training data
X_input = X_input[model_features]

# Predict button
if st.button("Predict"):
    prediction = model.predict(X_input)[0]
    st.success("Prediction: **Churn**" if prediction == 1 else "Prediction: **Not Churn**")

if __name__ == "__main__":
    main()

