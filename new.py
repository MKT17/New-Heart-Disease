# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:48:35 2024

@author: MKT17
"""

import streamlit as st
import joblib


# Load the machine learning model
model = joblib.load('model_joblib_heart')

# Set page configuration
st.set_page_config(page_title="Heart Disease Predictor", layout="wide")

# Custom CSS for header
st.markdown("""
    <style>
        .header {
            font-family: 'Times New Roman', Times, serif;
            font-size: 36px;
            font-weight: bold;
            color: white;
            background-color: lightblue;
            padding: 20px;
            border-radius: 10px;
            text-align: center;
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .footer {
            font-family: 'Times New Roman', Times, serif;
            font-size: 16px;
            color: black;
            text-align: center;
            margin-top: 30px;
        }
        .main-container {
            padding: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Header with heart emoji
st.markdown('<div class="header">Heart Disease Predictor &#x1F493;</div>', unsafe_allow_html=True)

# Main container
st.markdown('<div class="main-container">', unsafe_allow_html=True)

# User input parameters
st.header("Enter Parameters")
age = st.number_input("Age:", min_value=0, max_value=120, value=50)
sex = st.selectbox("Sex:", ["Male", "Female"])
chest_pain_type = st.selectbox("Chest Pain Type:", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
trestbps = st.number_input("Resting Blood Pressure (mm Hg):", min_value=0, max_value=300, value=120)
chol = st.number_input("Serum Cholestoral (mg/dl):", min_value=0, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar (mg/dl):", ["False", "True"])
restecg = st.selectbox("Resting Electrocardiographic Results:", ["Normal", "Having ST-T Wave Abnormality", "Showing Probable or Definite Left Ventricular Hypertrophy by Estes' Criteria"])
thalach = st.number_input("Maximum Heart Rate Achieved:", min_value=0, max_value=300, value=150)
exang = st.selectbox("Exercise Induced Angina:", ["No", "Yes"])
oldpeak = st.number_input("ST Depression Induced by Exercise Relative to Rest:", min_value=0, max_value=10, value=0)
slope = st.selectbox("Slope of the Peak Exercise ST Segment:", ["Upsloping", "Flat", "Downsloping"])
ca = st.number_input("Number of Major Vessels Colored by Flourosopy:", min_value=0, max_value=3, value=0)
thal = st.selectbox("Thal:", ["Normal", "Fixed Defect", "Reversible Defect"])

# Convert categorical values to numeric
sex = 0 if sex == "Male" else 1
chest_pain_type_mapping = {"Typical Angina": 0, "Atypical Angina": 1, "Non-Anginal Pain": 2, "Asymptomatic": 3}
chest_pain_type = chest_pain_type_mapping[chest_pain_type]
fbs = 1 if fbs == "True" else 0
restecg_mapping = {"Normal": 0, "Having ST-T Wave Abnormality": 1, "Showing Probable or Definite Left Ventricular Hypertrophy by Estes' Criteria": 2}
restecg = restecg_mapping[restecg]
exang = 1 if exang == "Yes" else 0
slope_mapping = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
slope = slope_mapping[slope]
thal_mapping = {"Normal": 3, "Fixed Defect": 6, "Reversible Defect": 7}
thal = thal_mapping[thal]

# Prediction button
if st.button("Predict"):
    # Prepare input data for prediction
    input_data = [[age, sex, chest_pain_type, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]]
    # Make prediction
    prediction = model.predict(input_data)[0]
    # Display prediction result
    if prediction == 0:
        st.success("Prediction Result: You do not have a heart disease")
    else:
        st.error("Prediction Result: You have a heart disease. See your Doctor today 😊")

# Close main container
st.markdown('</div>', unsafe_allow_html=True)

# Footer
st.markdown('<div class="footer">Made with ❤️ by Kelani</div>', unsafe_allow_html=True)
