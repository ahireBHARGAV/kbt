import streamlit as st

st.title("Calculator")
num1 = st.number_input("Enter first number", value=0, step=1)
num2 = st.number_input("Enter second number", value=0, step=1)
operator = st.selectbox("Select operator", ["Add", "Subtract", "Multiply", "Divide"])

if st.button("Calculate"):
    if operator == "Add":
        st.write("Result: ", num1 + num2)
    elif operator == "Subtract":
        st.write("Result: ", num1 - num2)
    elif operator == "Multiply":
        st.write("Result: ", num1 * num2)
    elif operator == "Divide":
        st.write("Result: ", num1 / num2)
