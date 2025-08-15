import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load the saved model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("🩺 Diabetes Prediction App")
st.write("Enter the patient's details to predict if they are diabetic or not.")

# Input fields
pregnancies = st.number_input("Pregnancies", min_value=0, max_value=20, value=0)
glucose = st.number_input("Glucose Level", min_value=0, max_value=300, value=120)
blood_pressure = st.number_input("Blood Pressure", min_value=0, max_value=200, value=70)
skin_thickness = st.number_input("Skin Thickness", min_value=0, max_value=100, value=20)
insulin = st.number_input("Insulin", min_value=0, max_value=900, value=80)
bmi = st.number_input("BMI", min_value=0.0, max_value=70.0, value=25.0)
dpf = st.number_input("Diabetes Pedigree Function", min_value=0.0, max_value=2.5, value=0.5)
age = st.number_input("Age", min_value=0, max_value=120, value=33)

# Prediction button
if st.button("Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])
    prediction = model.predict(input_data)[0]
    result = "Diabetic" if prediction == 1 else "Not Diabetic"

    st.subheader("Prediction Result:")
    if prediction == 1:
        st.error(f"⚠️ The patient is **{result}**")
    else:
        st.success(f"✅ The patient is **{result}**")
