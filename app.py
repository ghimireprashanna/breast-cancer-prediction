import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("breast_cancer_model.pkl")

st.set_page_config(page_title="Breast Cancer Prediction", page_icon="💉")
st.title("💉 Breast Cancer Prediction App")
st.write("Enter the values below to predict whether the tumor is **Benign (B)** or **Malignant (M)**.")

# Top 10 features used in retrained model
features = [
    'area_worst', 'concave points_mean', 'concave points_worst', 'area_smoothness',
    'perimeter_worst', 'radius_worst', 'radius_mean', 'perimeter_mean',
    'concavity_mean', 'area_se'
]

inputs = []
for feature in features:
    value = st.number_input(f"{feature}", min_value=0.0, value=1.0)
    inputs.append(value)

input_data = np.array(inputs).reshape(1, -1)

if st.button("🔍 Predict"):
    prediction = model.predict(input_data)[0]
    if prediction == 1:
        st.error("⚠️ The tumor is **Malignant (Cancerous)**")
    else:
        st.success("✅ The tumor is **Benign (Non-Cancerous)**")
