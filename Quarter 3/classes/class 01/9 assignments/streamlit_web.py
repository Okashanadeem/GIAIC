import streamlit as st
import random
import string

# App Title
st.title("Multi-Feature Streamlit App 🎉")

# Sidebar Navigation
menu = st.sidebar.selectbox("Choose a Feature", ["Home", "BMI Calculator", "Password Generator"])

# Home Page
if menu == "Home":
    st.header("Welcome to the Multi-Feature App! 🚀")
    st.write("Select a feature from the left sidebar.")

# BMI Calculator
elif menu == "BMI Calculator":
    st.header("BMI Calculator ⚖️")
    
    weight = st.number_input("Enter your weight (kg):", min_value=1.0, format="%.2f")
    height = st.number_input("Enter your height (m):", min_value=0.1, format="%.2f")
    
    if st.button("Calculate BMI"):
        if weight > 0 and height > 0:
            bmi = weight / (height ** 2)
            st.success(f"Your BMI is: {bmi:.2f}")
            if bmi < 18.5:
                st.info("You are underweight.")
            elif 18.5 <= bmi < 24.9:
                st.success("You have a normal weight.")
            elif 25 <= bmi < 29.9:
                st.warning("You are overweight.")
            else:
                st.error("You are obese.")
        else:
            st.error("Please enter valid weight and height.")

# Password Generator
elif menu == "Password Generator":
    st.header("Random Password Generator 🔒")
    
    length = st.slider("Select Password Length", 4, 20, 12)
    if st.button("Generate Password"):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))
        st.success(f"Generated Password: `{password}`")
