import streamlit as st

st.title("BMI Calculator")

mass = st.number_input("Enter Weight in kg", step = 0.1)
height = st.number_input("Enter your height in metres", step = 0.01)
button = st.button("Calculate BMI")

if button:
  bmi = mass / (height)**2
  st.success(f"Your BMI is {bmi}.")
