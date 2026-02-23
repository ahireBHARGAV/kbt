import streamlit as st

st.title("Welcome")
st.subheader("select your age")
age = st.slider("Age", 0, 100)
city = st.selectbox("Select your city", ["New York", "Los Angeles", "Chicago"])

if st.button("show details"):
    st.write("Age: ", age)
    st.write("City: ", city)
