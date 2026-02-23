import streamlit as st

st.title("Welcome!")

name = st.text_input("Enter your name:")

if st.button("Submit"):
    if name:
        st.success(f"Hello, **{name}**! lub ju bhai")
    else:
        st.warning("Please enter your name first.")
