import streamlit as st

st.title("Chatbot")
user_input = st.text_input("ask me anything ")
if st.button("Send"):
    st.write("Bot: ", user_input)
    if user_input == "hello":
        st.write("Bot: Hello")
    elif user_input == "how are you":
        st.write("Bot: I am fine")
    elif user_input == "what is your name":
        st.write("Bot: My name is Chatbot")
    else:
        st.write("Bot: I don't understand")