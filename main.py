import streamlit as st
import pickle
import numpy as np

# Load trained model
with open("crop_yield_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Crop Yield Prediction", layout="centered")

st.title("🌾 Crop Yield Prediction App")
st.write("Predict crop yield using environmental and agricultural factors.")

st.subheader("Enter Input Features")

area = st.number_input("Area", min_value=0.0)
annual_rainfall = st.number_input("Annual Rainfall (mm)", min_value=0.0)
fertilizer = st.number_input("Fertilizer Usage", min_value=0.0)
pesticide = st.number_input("Pesticide Usage", min_value=0.0)

if st.button("Predict Yield"):
    input_data = np.array([[area, annual_rainfall, fertilizer, pesticide]])
    prediction = model.predict(input_data)

    st.success(f"🌱 Predicted Crop Yield: {prediction[0]:.2f}")

