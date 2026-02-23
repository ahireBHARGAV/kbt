import streamlit as st

st.title("Form")
name = st.text_input("Enter your name")
age = st.number_input("Enter your age")

if st.button("Submit"):
    st.write("Name: ", name)
    st.write("Age: ", age)


st.markdown("""

    <style>
        .stTextInput>name {
            width: 100%;
            colour: blue; 
            background-color: red;
            
        }
        .stButton>button {
            width: 100%;
            colour: blue; 
            background-color: red;
            border-radius: 10%;
        }
    </style>

""", unsafe_allow_html=True)