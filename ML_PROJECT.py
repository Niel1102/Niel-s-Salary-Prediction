import streamlit as st
import joblib

model = joblib.load("Salary.model.pkl")
#APP TITLE
st.title("Niel's Salary Prediction")
st.write("Predict Salary based on Years of Experience")
#INPUT FROM USER
Exp = st.number_input("Enter years of experience: ", min_value=0.0, max_value=25.0, step=0.1)

# Prediction button
if st.button("Predict Salary"):
    salary = model.predict([[Exp]])
    st.success(f"Estimated Salary: ₹{salary[0]:.2f}")








